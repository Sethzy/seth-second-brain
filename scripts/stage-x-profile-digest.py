#!/usr/bin/env python3
"""Create a deterministic staged digest from an X profile timeline snapshot."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "AI and GTM systems": (" ai ", "agent", "claude", "automation", "workflow", "gtm", "revops"),
    "Outbound and pipeline generation": ("outbound", "pipeline", "prospect", "cold email", "meeting", "lead"),
    "Enterprise deal execution": ("enterprise", "deal", "discovery", "champion", "stakeholder", "procurement", "close"),
    "Messaging and content": ("content", "message", "copy", "story", "linkedin", "brand"),
    "Sales leadership and coaching": ("coach", "leader", "manager", "rep", "quota", "team", "hire"),
}


def parse_posts(text: str) -> list[dict]:
    chunks = re.split(r"(?m)^### (\d+)\. ", text)[1:]
    posts = []
    for index in range(0, len(chunks), 2):
        number = int(chunks[index])
        body = chunks[index + 1]
        date, _, rest = body.partition("\n")
        url_match = re.search(r"^- URL: \[([^\]]+)\]", rest, re.MULTILINE)
        metrics = re.search(r"^- Metrics: replies (\d+|Unknown), reposts (\d+|Unknown), likes (\d+|Unknown)", rest, re.MULTILINE)
        text_match = re.search(r"#### Verbatim Text\n\n(.*?)(?=\n\n#### |\n### |\Z)", rest, re.DOTALL)
        def value(group: int) -> int:
            if not metrics or metrics.group(group) == "Unknown":
                return 0
            return int(metrics.group(group))
        posts.append({
            "number": number,
            "date": date.strip(),
            "url": url_match.group(1) if url_match else "",
            "replies": value(1),
            "reposts": value(2),
            "likes": value(3),
            "text": (text_match.group(1).strip() if text_match else ""),
        })
    return posts


def hook(text: str, limit: int = 180) -> str:
    compact = re.sub(r"\s+", " ", text).strip() or "(No text captured.)"
    return compact if len(compact) <= limit else compact[: limit - 1].rstrip() + "…"


def update_source_map(raw_rel: str, digest_rel: str, title: str, profile_url: str, count: int) -> None:
    state_path = ROOT / "state" / "source-map.json"
    state = json.loads(state_path.read_text())
    sources = state.setdefault("sources", [])
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    raw = next((item for item in sources if item.get("id") == raw_rel), None)
    if raw:
        raw["staging_path"] = digest_rel
        raw["staging_paths"] = [digest_rel]
        raw["updated_at"] = now
    payload = {
        "id": digest_rel,
        "title": title,
        "url": profile_url,
        "source_type": "x_profile_digest",
        "trust_lane": "staging",
        "capture_quality": "deterministic_digest_from_authenticated_timeline",
        "raw_path": raw_rel,
        "staging_path": digest_rel,
        "status": "staged",
        "wiki_paths": [],
        "staging_paths": [digest_rel],
        "updated_at": now,
        "notes": f"Fresh routing digest over {count} authenticated X timeline posts; not promoted to wiki.",
    }
    existing = next((item for item in sources if item.get("id") == digest_rel), None)
    if existing:
        created = existing.get("created_at", now)
        existing.clear(); existing.update(payload); existing["created_at"] = created
    else:
        payload["created_at"] = now
        sources.append(payload)
    state_path.write_text(json.dumps(state, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_file")
    parser.add_argument("slug")
    parser.add_argument("name")
    args = parser.parse_args()
    raw_path = (ROOT / args.raw_file).resolve()
    text = raw_path.read_text()
    posts = parse_posts(text)
    if len(posts) != 100:
        raise SystemExit(f"Expected exactly 100 posts, parsed {len(posts)}")
    handle = re.search(r"(?m)^handle: (.+)$", text).group(1)
    profile_url = re.search(r"(?m)^url: (.+)$", text).group(1)
    captured_at = re.search(r"(?m)^captured_at: (.+)$", text).group(1)
    counts = {
        theme: sum(1 for post in posts if any(term in f" {(post['text']).lower()} " for term in terms))
        for theme, terms in THEMES.items()
    }
    ranked = sorted(posts, key=lambda p: p["likes"] + 2 * p["replies"] + 3 * p["reposts"], reverse=True)
    date = captured_at[:10]
    digest_path = ROOT / "staging" / "x-profile-digests" / f"{date}-{args.slug}-latest-100-posts-digest.md"
    if digest_path.exists():
        raise SystemExit(f"Refusing to overwrite {digest_path}")
    lines = [
        "---",
        f"title: {args.name} X Latest 100 Posts Digest",
        f"created: {date}",
        "status: staged",
        "source_type: x",
        "trust_lane: sweep",
        "capture_quality: authenticated_latest_100_with_deterministic_digest",
        f"raw_path: ../../{raw_path.relative_to(ROOT).as_posix()}",
        "compiled_to_wiki: false",
        "---",
        "",
        f"# {args.name} X Latest 100 Posts Digest",
        "",
        "## Source Snapshot",
        "",
        f"- Raw snapshot: [latest 100 posts](../../{raw_path.relative_to(ROOT).as_posix()})",
        f"- Profile: [{profile_url}]({profile_url})",
        f"- Handle: @{handle}",
        f"- Captured: {captured_at}",
        "- Records reviewed: 100",
        "- Status: staged only; no wiki promotion.",
        "",
        "## Theme Counts",
        "",
        "| Theme | Matching posts |",
        "|---|---:|",
    ]
    for theme, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"| {theme} | {count} |")
    lines.extend(["", "## Highest-Engagement Signals For Review", ""])
    for index, post in enumerate(ranked[:10], start=1):
        score = post["likes"] + 2 * post["replies"] + 3 * post["reposts"]
        lines.append(f"{index}. [{hook(post['text'])}]({post['url']}) — engagement score {score}; {post['date']}.")
    lines.extend([
        "",
        "## Review Guidance",
        "",
        "- Prioritize recurring enterprise-sales mechanisms over engagement bait and isolated promotion.",
        "- Treat commercial results and product claims as author positioning until independently verified.",
        "- Use the raw timeline snapshot for exact wording and context.",
        "- Keep this digest staged until Seth requests promotion.",
        "",
    ])
    digest_path.parent.mkdir(parents=True, exist_ok=True)
    digest_path.write_text("\n".join(lines))
    raw_rel = raw_path.relative_to(ROOT).as_posix()
    digest_rel = digest_path.relative_to(ROOT).as_posix()
    update_source_map(raw_rel, digest_rel, f"{args.name} X latest 100 posts digest", profile_url, len(posts))
    print(digest_rel)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
