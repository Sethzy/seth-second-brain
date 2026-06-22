#!/usr/bin/env python3
"""
Capture recent OpenAI, Claude, and Cursor blog posts into raw/intentional/web.

Window: 2025-12-14 through 2026-06-14, inclusive.
"""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


ROOT = Path(__file__).resolve().parents[1]
CUTOFF = dt.date(2025, 12, 14)
END = dt.date(2026, 6, 14)
FETCHED_AT = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
OUT_DIR = ROOT / "raw" / "intentional" / "web"
MANIFEST_DIR = ROOT / "raw" / "intentional" / "pasted"
SOURCE_MAP = ROOT / "state" / "source-map.json"
REPORT = ROOT / "tmp" / "vendor_blog_sweep_report.json"
UA = "Mozilla/5.0 (compatible; SethSecondBrainVendorBlogSweep/1.0; +local)"

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA})


MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def fetch(url: str, timeout: int = 25) -> str:
    resp = SESSION.get(url, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def slugify(text: str, max_len: int = 72) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len].strip("-") or "untitled"


def parse_loose_date(text: str, default_year: int | None = None) -> dt.date | None:
    text = clean_text(text)
    iso = re.search(r"(20\d{2})-(\d{2})-(\d{2})", text)
    if iso:
        return dt.date(int(iso.group(1)), int(iso.group(2)), int(iso.group(3)))

    m = re.search(
        r"\b("
        + "|".join(MONTHS.keys())
        + r")\.?\s+(\d{1,2})(?:,\s*(20\d{2}))?\b",
        text,
        flags=re.I,
    )
    if not m:
        return None
    month = MONTHS[m.group(1).lower().rstrip(".")]
    day = int(m.group(2))
    year = int(m.group(3)) if m.group(3) else default_year
    if year is None:
        year = 2025 if month == 12 else 2026
    try:
        return dt.date(year, month, day)
    except ValueError:
        return None


def json_ld_objects(soup: BeautifulSoup) -> list[dict]:
    out: list[dict] = []
    for script in soup.find_all("script", {"type": "application/ld+json"}):
        raw = script.string or script.get_text() or ""
        if not raw.strip():
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue
        if isinstance(data, list):
            out.extend(x for x in data if isinstance(x, dict))
        elif isinstance(data, dict):
            if isinstance(data.get("@graph"), list):
                out.extend(x for x in data["@graph"] if isinstance(x, dict))
            out.append(data)
    return out


def pick_title(soup: BeautifulSoup, url: str) -> str:
    for obj in json_ld_objects(soup):
        title = obj.get("headline") or obj.get("name")
        if title:
            return clean_text(str(title))
    meta = soup.find("meta", property="og:title") or soup.find("meta", attrs={"name": "twitter:title"})
    if meta and meta.get("content"):
        return clean_text(meta["content"]).removesuffix(" | OpenAI").removesuffix(" | Cursor").removesuffix(" \u5e73 Anthropic")
    if soup.title:
        return clean_text(soup.title.get_text()).split("|")[0].strip()
    return urllib.parse.urlparse(url).path.strip("/").split("/")[-1].replace("-", " ").title()


def pick_description(soup: BeautifulSoup) -> str:
    for obj in json_ld_objects(soup):
        desc = obj.get("description")
        if desc:
            return clean_text(str(desc))
    meta = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", property="og:description")
    if meta and meta.get("content"):
        return clean_text(meta["content"])
    return ""


def pick_article_markdown(soup: BeautifulSoup, vendor: str) -> str:
    for selector in ["article", "main", "[data-testid='article']", ".blog-post", ".post"]:
        node = soup.select_one(selector)
        if node:
            return md(str(node), heading_style="ATX").strip()
    body = soup.body or soup
    for tag in body(["script", "style", "noscript", "svg"]):
        tag.decompose()
    return md(str(body), heading_style="ATX").strip()


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/") + "/", "", "", ""))


def existing_urls() -> set[str]:
    urls: set[str] = set()
    for path in OUT_DIR.glob("*.md"):
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        m = re.search(r'(?m)^url:\s*["\']?([^"\'\n]+)', text)
        if m:
            urls.add(normalize_url(m.group(1).strip()))
    if SOURCE_MAP.exists():
        try:
            data = json.loads(SOURCE_MAP.read_text())
            entries = data.values() if isinstance(data, dict) else data
            if isinstance(entries, list):
                iterable = entries
            else:
                iterable = data.values() if isinstance(data, dict) else []
            for item in iterable:
                if isinstance(item, dict):
                    url = item.get("url") or item.get("source_url") or item.get("canonical_url")
                    if url:
                        urls.add(normalize_url(str(url)))
        except Exception:
            pass
    return urls


def discover_openai() -> list[dict]:
    url = "https://developers.openai.com/blog"
    soup = BeautifulSoup(fetch(url), "html.parser")
    posts: dict[str, dict] = {}
    for a in soup.find_all("a", href=True):
        href = urllib.parse.urljoin(url, a["href"])
        if urllib.parse.urlparse(href).netloc != "developers.openai.com":
            continue
        if "/blog/" not in urllib.parse.urlparse(href).path or href.rstrip("/") == url:
            continue
        text = clean_text(a.get_text(" ", strip=True))
        date = parse_loose_date(text)
        if not date:
            # Look nearby for a visible card date.
            parent_text = clean_text(a.find_parent().get_text(" ", strip=True) if a.find_parent() else text)
            date = parse_loose_date(parent_text)
        if not date:
            continue
        if CUTOFF <= date <= END:
            posts[normalize_url(href)] = {"vendor": "openai", "url": normalize_url(href), "published_at": date.isoformat()}
    return sorted(posts.values(), key=lambda x: x["published_at"], reverse=True)


def discover_claude() -> list[dict]:
    xml_text = fetch("https://claude.com/sitemap.xml", timeout=45)
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", ns):
        value = loc.text or ""
        parsed = urllib.parse.urlparse(value)
        if parsed.netloc != "claude.com":
            continue
        path = parsed.path.rstrip("/")
        if not path.startswith("/blog/"):
            continue
        if path in {"/blog", "/blog-category"} or "/blog-category/" in path:
            continue
        if re.match(r"^/(de|fr|ja|ko|es|it|pt|zh|ar|hi|id)/", path):
            continue
        urls.append(normalize_url(value))
    return [{"vendor": "claude", "url": u} for u in sorted(set(urls))]


def discover_cursor() -> list[dict]:
    xml_text = fetch("https://cursor.com/sitemap.xml", timeout=45)
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", ns):
        value = loc.text or ""
        parsed = urllib.parse.urlparse(value)
        path = parsed.path.rstrip("/")
        if parsed.netloc != "cursor.com":
            continue
        if path == "/blog" or not path.startswith("/blog/"):
            continue
        urls.append(normalize_url(value))
    return [{"vendor": "cursor", "url": u} for u in sorted(set(urls))]


def extract_date_from_page(soup: BeautifulSoup, vendor: str) -> dt.date | None:
    for obj in json_ld_objects(soup):
        for key in ["datePublished", "dateCreated", "dateModified"]:
            if obj.get(key):
                parsed = parse_loose_date(str(obj[key]))
                if parsed:
                    return parsed
    time_tag = soup.find("time")
    if time_tag:
        if time_tag.get("datetime"):
            parsed = parse_loose_date(time_tag["datetime"])
            if parsed:
                return parsed
        parsed = parse_loose_date(time_tag.get_text(" ", strip=True))
        if parsed:
            return parsed
    for meta_name in ["article:published_time", "publish_date", "date", "datePublished"]:
        meta = soup.find("meta", property=meta_name) or soup.find("meta", attrs={"name": meta_name})
        if meta and meta.get("content"):
            parsed = parse_loose_date(meta["content"])
            if parsed:
                return parsed
    text = clean_text(soup.get_text(" ", strip=True)[:8000])
    return parse_loose_date(text)


def fetch_and_extract(post: dict) -> dict:
    url = post["url"]
    vendor = post["vendor"]
    try:
        text = fetch(url)
        soup = BeautifulSoup(text, "html.parser")
        date = dt.date.fromisoformat(post["published_at"]) if post.get("published_at") else extract_date_from_page(soup, vendor)
        title = pick_title(soup, url)
        desc = pick_description(soup)
        body = pick_article_markdown(soup, vendor)
        ok = date is not None and CUTOFF <= date <= END
        return {
            **post,
            "published_at": date.isoformat() if date else None,
            "title": title,
            "description": desc,
            "body": body,
            "status": "selected" if ok else "excluded_date",
            "body_chars": len(body),
        }
    except Exception as e:
        return {**post, "status": "fetch_error", "error": repr(e)}


def frontmatter_escape(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_capture(item: dict, existing: set[str]) -> dict:
    url_norm = normalize_url(item["url"])
    if url_norm in existing:
        item["capture_status"] = "skipped_existing_url"
        return item

    date = item["published_at"]
    slug = slugify(item.get("title") or urllib.parse.urlparse(item["url"]).path.strip("/").split("/")[-1])
    path = OUT_DIR / f"{date}-{item['vendor']}-{slug}.md"
    counter = 2
    while path.exists():
        path = OUT_DIR / f"{date}-{item['vendor']}-{slug}-{counter}.md"
        counter += 1

    fm = [
        "---",
        "type: raw_capture",
        "source_type: web",
        f"title: {frontmatter_escape(item.get('title', 'Untitled'))}",
        f"url: {frontmatter_escape(item['url'])}",
        f"canonical_url: {frontmatter_escape(url_norm)}",
        f"vendor_blog: {item['vendor']}",
        f"published_at: {date}",
        f"collected_at: {FETCHED_AT}",
        "capture_quality: extracted_markdown",
        "status: raw",
        "trust_lane: intentional",
        f"scrape_window_start: {CUTOFF.isoformat()}",
        f"scrape_window_end: {END.isoformat()}",
        "extraction_method: requests + BeautifulSoup + markdownify",
        "---",
        "",
        f"# {item.get('title', 'Untitled')}",
        "",
        f"Original URL: {item['url']}",
        f"Published: {date}",
        f"Captured: {FETCHED_AT}",
    ]
    if item.get("description"):
        fm.extend(["", f"Description: {item['description']}"])
    fm.extend(["", "## Extracted Article Text", "", item.get("body", "").strip(), ""])
    path.write_text("\n".join(fm), encoding="utf-8")
    item["capture_status"] = "created"
    item["path"] = str(path.relative_to(ROOT))
    existing.add(url_norm)
    return item


def update_source_map(created: list[dict]) -> None:
    if not created:
        return
    try:
        data = json.loads(SOURCE_MAP.read_text()) if SOURCE_MAP.exists() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {"legacy_entries": data}
    captures = data.setdefault("captures", {})
    if not isinstance(captures, dict):
        captures = {}
        data["captures"] = captures
    for item in created:
        key = item["path"]
        captures[key] = {
            "url": item["url"],
            "title": item.get("title"),
            "source_type": "web",
            "trust_lane": "intentional",
            "vendor_blog": item["vendor"],
            "published_at": item["published_at"],
            "collected_at": FETCHED_AT,
            "compiled_to": [],
            "status": "raw_captured_uncompiled",
            "notes": "Six-month vendor blog sweep for OpenAI, Claude, and Cursor.",
        }
    SOURCE_MAP.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    discovered = {
        "openai": discover_openai(),
        "claude": discover_claude(),
        "cursor": discover_cursor(),
    }
    candidates = [p for posts in discovered.values() for p in posts]

    selected: list[dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        for item in pool.map(fetch_and_extract, candidates):
            if item.get("status") == "selected":
                selected.append(item)

    selected.sort(key=lambda x: (x["vendor"], x["published_at"], x["url"]), reverse=True)
    existing = existing_urls()
    written = [write_capture(item, existing) for item in selected]
    created = [x for x in written if x.get("capture_status") == "created"]
    update_source_map(created)

    manifest_path = MANIFEST_DIR / f"{END.isoformat()}-vendor-blog-six-month-sweep-manifest.md"
    lines = [
        "---",
        "type: raw_capture_manifest",
        "source_type: pasted",
        "title: Vendor Blog Six-Month Sweep Manifest",
        f"collected_at: {FETCHED_AT}",
        f"scrape_window_start: {CUTOFF.isoformat()}",
        f"scrape_window_end: {END.isoformat()}",
        "status: raw",
        "trust_lane: intentional",
        "---",
        "",
        "# Vendor Blog Six-Month Sweep Manifest",
        "",
        f"Window: {CUTOFF.isoformat()} through {END.isoformat()}",
        "",
    ]
    for vendor in ["openai", "claude", "cursor"]:
        items = [x for x in written if x["vendor"] == vendor]
        lines.append(f"## {vendor.title()}")
        lines.append("")
        for item in sorted(items, key=lambda x: x["published_at"], reverse=True):
            local = item.get("path", "(existing raw capture)")
            lines.append(
                f"- {item['published_at']} - [{item.get('title','Untitled')}]({item['url']}) "
                f"- `{item.get('capture_status')}` - `{local}`"
            )
        lines.append("")
    manifest_path.write_text("\n".join(lines), encoding="utf-8")

    report = {
        "window_start": CUTOFF.isoformat(),
        "window_end": END.isoformat(),
        "fetched_at": FETCHED_AT,
        "discovered_counts": {k: len(v) for k, v in discovered.items()},
        "selected_counts": {k: len([x for x in written if x["vendor"] == k]) for k in discovered},
        "created_counts": {k: len([x for x in created if x["vendor"] == k]) for k in discovered},
        "manifest": str(manifest_path.relative_to(ROOT)),
        "items": [
            {
                k: v
                for k, v in item.items()
                if k
                in {
                    "vendor",
                    "url",
                    "published_at",
                    "title",
                    "description",
                    "capture_status",
                    "path",
                    "body_chars",
                    "status",
                    "error",
                }
            }
            for item in written
        ],
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["discovered_counts", "selected_counts", "created_counts", "manifest"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
