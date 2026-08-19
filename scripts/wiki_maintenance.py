#!/usr/bin/env python3
"""Maintenance helpers for Seth Second Brain.

This module intentionally writes proposals/reports, not wiki edits. The wiki
compile step still requires human approval in chat.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


STATUS_ID_RE = re.compile(r"(\d{15,25})")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

REQUIRED_WIKI_FIELDS = ["type", "title", "updated_at", "status", "tags"]
LINT_STOP_PHRASES = {
    "Active Threads",
    "Agent",
    "Agents",
    "Article",
    "Articles",
    "Candidate",
    "Candidates",
    "Capture",
    "Captures",
    "Code",
    "Compiled",
    "Context",
    "Draft",
    "Evidence",
    "Examples",
    "File",
    "Files",
    "Index",
    "Key Ideas",
    "Markdown",
    "My Take",
    "Open Questions",
    "Overview",
    "Page",
    "Pages",
    "Raw",
    "Report",
    "Review",
    "See Also",
    "Source",
    "Sources",
    "Status",
    "Summary",
    "Unknown",
    "Updated",
    "Workflow",
    "Workflows",
}
PHRASE_LEADING_STOPWORDS = {"For", "If", "Should", "That", "The", "This", "Use", "What", "When", "Where", "Why"}
TOKEN_STOPWORDS = {
    "about",
    "after",
    "agent",
    "agents",
    "also",
    "and",
    "article",
    "based",
    "because",
    "brain",
    "capture",
    "captures",
    "code",
    "coding",
    "compiled",
    "context",
    "data",
    "does",
    "from",
    "have",
    "into",
    "more",
    "note",
    "notes",
    "page",
    "pages",
    "pattern",
    "patterns",
    "raw",
    "source",
    "sources",
    "system",
    "systems",
    "that",
    "their",
    "this",
    "with",
    "workflow",
    "workflows",
}
REVIEW_MARKERS = [
    "contradiction",
    "[!contradiction]",
    "[!gap]",
    "[!stale]",
    "needs source",
    "needs verification",
    "verify",
    "unverified",
    "unclear",
    "todo",
    "tbd",
]


CLUSTERS = [
    {
        "id": "ai-coding",
        "title": "AI Coding / Agents / Skills",
        "priority": 1,
        "targets": [
            "ai-coding/agentic-engineering-practices.md",
            "ai-coding/agent-skill-libraries-and-requirements.md",
            "agent-frameworks/agent-framework-landscape.md",
            "personal-systems/agent-goals-and-dynamic-workflows.md",
        ],
        "keywords": [
            "agent",
            "agents",
            "claude",
            "codex",
            "cursor",
            "skill",
            "skills",
            "harness",
            "mcp",
            "sandbox",
            "workflow",
            "workflows",
            "vercel",
            "devin",
            "langgraph",
            "openclaw",
            "fable",
            "mythos",
            "context engineering",
        ],
    },
    {
        "id": "gtm-sales",
        "title": "GTM / Sales / Outbound",
        "priority": 2,
        "targets": [
            "gtm-sales/agentic-gtm-campaign-workflows.md",
            "gtm-sales/ai-native-account-intelligence.md",
            "gtm-sales/high-signal-enterprise-sales.md",
        ],
        "keywords": [
            "gtm",
            "sales",
            "outbound",
            "crm",
            "lead",
            "leads",
            "account",
            "accounts",
            "prospect",
            "pipeline",
            "b2b",
            "cold email",
            "linkedin",
            "founder-led",
            "enterprise sales",
            "abm",
        ],
    },
    {
        "id": "marketing",
        "title": "Marketing / SEO / Content Systems",
        "priority": 3,
        "targets": [
            "marketing/agentic-marketing-workflows.md",
            "marketing/seo-aeo-geo-content-systems.md",
            "marketing/content-ops-and-editorial-systems.md",
            "marketing/performance-marketing-creative-ops.md",
            "marketing/ugc-and-creator-systems.md",
        ],
        "keywords": [
            "marketing",
            "seo",
            "aeo",
            "geo",
            "ai search",
            "google",
            "content",
            "ads",
            "ad ",
            "ugc",
            "creator",
            "landing page",
            "landing pages",
            "creative",
            "campaign",
            "brand",
            "search visibility",
            "lifecycle",
            "analytics",
        ],
    },
    {
        "id": "workflow-hustle",
        "title": "Workflow Hustle / Vertical Agents",
        "priority": 4,
        "targets": [
            "workflow-hustle/workflow-hustle-while-job-hunting.md",
            "workflow-hustle/zhao-orderops-prd.md",
            "personal-systems/agent-platforms-and-work-surfaces.md",
        ],
        "keywords": [
            "workflow",
            "vertical",
            "startup",
            "orderops",
            "automation",
            "small business",
            "side project",
            "service business",
        ],
    },
    {
        "id": "personal-systems",
        "title": "Personal Systems / Knowledge Work",
        "priority": 5,
        "targets": [
            "personal-systems/personal-agent-ops-stack.md",
            "ai-knowledge-work/agentic-artifact-surfaces.md",
        ],
        "keywords": [
            "second brain",
            "karpathy",
            "wiki",
            "obsidian",
            "memory",
            "voice",
            "contacts",
            "personal agent",
            "personal agents",
            "artifact",
            "artifacts",
        ],
    },
    {
        "id": "finance-ops",
        "title": "Finance / Trading / Money Workflows",
        "priority": 6,
        "targets": ["finance-ops/agentic-finance-workflows.md"],
        "keywords": [
            "finance",
            "trading",
            "trade",
            "nq",
            "mnq",
            "quant",
            "billing",
            "invoice",
            "revenue",
            "bitcoin",
            "metaplanet",
        ],
    },
    {
        "id": "job-apps",
        "title": "Job Search / Career Signals",
        "priority": 7,
        "targets": ["job-apps/startup-funding-signal-job-search.md"],
        "keywords": ["job", "hiring", "career", "role", "roles", "recruit", "funding round"],
    },
]

CLUSTER_BY_ID = {cluster["id"]: cluster for cluster in CLUSTERS}
RISK_KEYWORDS = [
    "ban",
    "banned",
    "lawsuit",
    "sued",
    "layoff",
    "fired",
    "pricing",
    "rumor",
    "leaked",
    "deprecated",
    "dead",
    "replacing",
    "kill",
    "scam",
]


def today() -> str:
    return dt.date.today().isoformat()


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def relpath(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.resolve().relative_to(root.resolve()).as_posix()


def load_source_map(root: Path) -> list[dict]:
    path = root / "state" / "source-map.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    sources = data.get("sources", [])
    if isinstance(sources, dict):
        records = list(sources.values())
    else:
        records = list(sources)

    seen_paths = set()
    for record in records:
        if not isinstance(record, dict):
            continue
        for key in ("raw_path", "staging_path", "id"):
            value = record.get(key)
            if isinstance(value, str):
                seen_paths.add(value)

    captures = data.get("captures", {})
    if isinstance(captures, dict):
        for raw_path, capture in captures.items():
            if raw_path in seen_paths:
                continue
            if isinstance(capture, dict):
                record = dict(capture)
            else:
                record = {}
            record.setdefault("id", raw_path)
            record.setdefault("raw_path", raw_path)
            record.setdefault("source_type", "unknown")
            record.setdefault("trust_lane", "intentional")
            record.setdefault("capture_quality", "complete")
            compiled_to = record.get("compiled_to") or record.get("wiki_paths") or []
            if compiled_to:
                record["status"] = "compiled"
                record.setdefault("wiki_paths", compiled_to)
            else:
                status = str(record.get("status") or "")
                record["status"] = "compiled" if "compiled" in status else "raw"
            records.append(record)
    return records


def parse_wiki_index(root: Path) -> dict[str, dict]:
    index = root / "wiki" / "index.md"
    entries: dict[str, dict] = {}
    if not index.exists():
        return entries
    for line in index.read_text(errors="replace").splitlines():
        match = re.search(r"\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]*)\|", line)
        if not match:
            continue
        title, path, summary = match.groups()
        entries[path.strip()] = {"title": title.strip(), "summary": summary.strip()}
    return entries


def source_text(source: dict) -> str:
    parts = [
        str(source.get("title") or ""),
        str(source.get("raw_path") or ""),
        str(source.get("url") or ""),
        str(source.get("notes") or ""),
    ]
    return " ".join(parts).lower().replace("-", " ")


def classify_source(source: dict) -> tuple[str, int]:
    haystack = source_text(source)
    best_id = "unrouted"
    best_score = 0
    for cluster in CLUSTERS:
        score = 0
        for keyword in cluster["keywords"]:
            if keyword in haystack:
                score += 1
        if score > best_score:
            best_id = cluster["id"]
            best_score = score
    return best_id, best_score


def raw_only_sources(sources: list[dict], source_type: str | None = None) -> list[dict]:
    selected = []
    for source in sources:
        if source.get("status") != "raw":
            continue
        if source_type and source.get("source_type") != source_type:
            continue
        if not source.get("raw_path"):
            continue
        selected.append(source)
    return selected


def source_sort_key(source: dict) -> tuple[int, int, str]:
    cluster_id, score = classify_source(source)
    cluster = CLUSTER_BY_ID.get(cluster_id)
    priority = cluster["priority"] if cluster else 99
    return (priority, -score, str(source.get("raw_path") or source.get("id") or ""))


def source_handle(source: dict) -> str:
    raw_path = str(source.get("raw_path") or "")
    name = Path(raw_path).name
    parts = name.split("-")
    if len(parts) >= 2 and STATUS_ID_RE.fullmatch(parts[0]):
        return parts[1]
    return "unknown"


def markdown_source_row(source: dict) -> str:
    title = str(source.get("title") or "(untitled)").replace("|", "\\|")
    path = str(source.get("raw_path") or source.get("staging_path") or source.get("id") or "")
    cluster_id, score = classify_source(source)
    cluster_title = CLUSTER_BY_ID.get(cluster_id, {"title": "Unrouted"})["title"]
    return f"| {title} | `{path}` | {cluster_title} | {score} |"


def run_qmd_status(root: Path) -> str:
    try:
        result = subprocess.run(
            ["qmd", "status"],
            cwd=root,
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"QMD status unavailable: {exc}"
    text = result.stdout.strip() or result.stderr.strip()
    if not text:
        return "QMD status unavailable: command produced no output."
    lines = text.splitlines()
    return "\n".join(lines[:28])


def build_organization_proposal(
    root: Path,
    limit: int = 100,
    source_type: str | None = "x",
    include_qmd: bool = True,
) -> str:
    sources = load_source_map(root)
    index_entries = parse_wiki_index(root)
    raw_only = raw_only_sources(sources, source_type)
    selected = sorted(raw_only, key=source_sort_key)[:limit]

    grouped: dict[str, list[dict]] = defaultdict(list)
    for source in selected:
        cluster_id, _ = classify_source(source)
        grouped[cluster_id].append(source)

    total_label = "X" if source_type == "x" else (source_type or "all")
    lines = [
        "---",
        "type: wiki_organization_proposal",
        f"created_at: {utc_now()}",
        "status: proposed",
        f"source_type: {source_type or 'all'}",
        f"limit: {limit}",
        "---",
        "",
        f"# Wiki Organization Proposal - {today()}",
        "",
        "This is a proposal only. Do not compile these sources into `wiki/` until Seth approves specific sections.",
        "",
        "## Counts",
        "",
        f"- Source-map entries: {len(sources)}",
        f"- Raw-only {total_label} sources total: {len(raw_only)}",
        f"- Raw-only {total_label} sources selected: {len(selected)}",
        f"- Wiki index entries read: {len(index_entries)}",
        "",
    ]

    if include_qmd:
        lines.extend(["## QMD Snapshot", "", "```text", run_qmd_status(root), "```", ""])

    lines.extend(
        [
            "## Existing-Page Update Candidates",
            "",
            "These clusters appear to belong in existing medium-length synthesis pages.",
            "",
        ]
    )
    wrote_existing = False
    for cluster in sorted(CLUSTERS, key=lambda item: item["priority"]):
        cluster_sources = grouped.get(cluster["id"], [])
        if not cluster_sources:
            continue
        wrote_existing = True
        target_bits = []
        for target in cluster["targets"]:
            title = index_entries.get(target, {}).get("title") or Path(target).stem.replace("-", " ").title()
            target_bits.append(f"[{title}](../../wiki/{target})")
        lines.extend(
            [
                f"### {cluster['title']} ({len(cluster_sources)} selected)",
                "",
                f"Candidate target pages: {', '.join(target_bits)}",
                "",
                "| Source | Raw Path | Cluster | Score |",
                "|---|---|---|---|",
            ]
        )
        for source in cluster_sources[:12]:
            lines.append(markdown_source_row(source))
        remaining = len(cluster_sources) - 12
        if remaining > 0:
            lines.append(f"| ... | {remaining} more selected sources in this cluster | | |")
        lines.append("")
    if not wrote_existing:
        lines.extend(["- No selected raw-only sources matched existing-page clusters.", ""])

    handle_counts = Counter(source_handle(source) for source in selected)
    dense_handles = [(handle, count) for handle, count in handle_counts.most_common() if handle != "unknown" and count >= 5]
    lines.extend(["## New-Page Candidates", ""])
    if dense_handles:
        lines.append("Dense author/source-series clusters may deserve a new synthesis page only if their repeated posts add reusable ideas rather than one-off links.")
        lines.append("")
        lines.append("| Candidate | Selected Sources | Suggested Action |")
        lines.append("|---|---:|---|")
        for handle, count in dense_handles[:10]:
            lines.append(f"| `{handle}` source series | {count} | Review for a medium synthesis page or merge into an existing domain page |")
    else:
        lines.append("- No selected source series crossed the new-page threshold. Prefer updating existing pages.")
    lines.append("")

    unrouted = grouped.get("unrouted", [])
    failed_or_partial = [
        source
        for source in sources
        if source.get("capture_quality") in {"partial", "failed", "noisy_sweep", "generated_sweep"}
    ]
    lines.extend(
        [
            "## Skip / Defer",
            "",
            f"- Unrouted selected sources: {len(unrouted)}",
            f"- Partial/failed/noisy sources in source map: {len(failed_or_partial)}",
            "- Keep one-off, promotional, deleted, failed, or preview-only captures searchable in raw/staging unless they repeat across a useful cluster.",
            "",
        ]
    )

    review_needed = []
    for source in selected:
        haystack = source_text(source)
        if any(keyword in haystack for keyword in RISK_KEYWORDS):
            review_needed.append(source)
    lines.extend(["## Review Needed", ""])
    if review_needed:
        lines.extend(["| Source | Raw Path | Cluster | Score |", "|---|---|---|---|"])
        for source in review_needed[:20]:
            lines.append(markdown_source_row(source))
        if len(review_needed) > 20:
            lines.append(f"| ... | {len(review_needed) - 20} more review-needed sources | | |")
    else:
        lines.append("- No selected sources matched the current review-risk keyword list.")
    lines.append("")

    lines.extend(
        [
            "## Approved-Apply Workflow",
            "",
            "1. Seth approves specific clusters or rows from this proposal.",
            "2. Agent reads the full raw captures before making claims.",
            "3. Agent updates the relevant `wiki/` page or creates one medium synthesis page if approved.",
            "4. Agent updates `wiki/index.md`, appends `wiki/log.md`, updates `state/source-map.json`, and runs `scripts/qmd-refresh.sh --embed`.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def extract_status_id(path: Path) -> str | None:
    match = STATUS_ID_RE.search(path.name)
    if match:
        return match.group(1)
    try:
        match = STATUS_ID_RE.search(path.read_text(errors="replace"))
    except OSError:
        return None
    return match.group(1) if match else None


def wiki_articles(root: Path) -> list[Path]:
    wiki = root / "wiki"
    if not wiki.exists():
        return []
    return [
        path
        for path in wiki.rglob("*.md")
        if path.name not in {"index.md", "log.md"}
    ]


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    return parts[2]


def frontmatter_block(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def frontmatter_tags(text: str) -> list[str]:
    block = frontmatter_block(text)
    tags = []
    in_tags = False
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("tags:"):
            in_tags = True
            inline = stripped.split(":", 1)[1].strip()
            if inline.startswith("[") and inline.endswith("]"):
                tags.extend(tag.strip().strip("\"'") for tag in inline[1:-1].split(",") if tag.strip())
            elif inline:
                tags.extend(tag.strip().strip("\"'") for tag in inline.split(",") if tag.strip())
            continue
        if in_tags and stripped.startswith("-"):
            tag = stripped[1:].strip().strip("\"'")
            if tag:
                tags.append(tag)
            continue
        if not line.startswith((" ", "\t", "-")):
            in_tags = False
    return tags


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def page_title(path: Path, text: str) -> str:
    fm = frontmatter(text)
    if fm.get("title"):
        return fm["title"]
    for line in strip_frontmatter(text).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def article_lookup(root: Path, articles: list[Path], texts: dict[Path, str]) -> tuple[dict[str, list[Path]], dict[str, str]]:
    lookup: dict[str, list[Path]] = defaultdict(list)
    titles: dict[str, str] = {}
    for article in articles:
        title = page_title(article, texts[article])
        rel = relpath(root, article)
        titles[rel] = title
        candidates = {
            title,
            article.stem,
            article.name.removesuffix(".md"),
            article.stem.replace("-", " "),
        }
        for candidate in candidates:
            normalized = normalize_title(candidate)
            if normalized:
                lookup[normalized].append(article)
    return lookup, titles


def parse_wikilinks(text: str) -> list[str]:
    targets = []
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).strip()
        target = target.split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            targets.append(target)
    return targets


def markdown_link_records(path: Path) -> list[dict[str, object]]:
    text = path.read_text(errors="replace")
    records = []
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        records.append({"target": target, "clean": clean, "resolved": (path.parent / clean).resolve()})
    return records


def markdown_links(path: Path) -> list[Path]:
    links = []
    for record in markdown_link_records(path):
        links.append(record["resolved"])
    return links


def raw_ref_count(text: str) -> int:
    return text.count("../../raw/") + text.count("raw/intentional/") + text.count("raw/sweeps/")


def duplicate_x_capture_records(root: Path) -> dict[str, list[str]]:
    by_id: dict[str, list[str]] = defaultdict(list)
    for directory in [root / "raw" / "intentional" / "x", root / "staging" / "incomplete-captures" / "x"]:
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            if "staging" in path.parts:
                fm = frontmatter(path.read_text(errors="replace"))
                if fm.get("status") in {"resolved", "superseded", "archived"}:
                    continue
            status_id = extract_status_id(path)
            if status_id:
                by_id[status_id].append(relpath(root, path))
    return {status_id: paths for status_id, paths in by_id.items() if len(paths) > 1}


def source_map_path_sets(sources: list[dict]) -> tuple[set[str], set[str]]:
    raw_paths = set()
    staging_paths = set()
    for source in sources:
        raw_path = source.get("raw_path")
        if raw_path:
            raw_paths.add(raw_path)
        staging_path = source.get("staging_path")
        if staging_path:
            staging_paths.add(staging_path)
        for path in source.get("staging_paths") or []:
            staging_paths.add(path)
    return raw_paths, staging_paths


def source_map_missing_paths(root: Path, sources: list[dict]) -> tuple[list[str], list[str]]:
    raw_paths, staging_paths = source_map_path_sets(sources)
    raw_missing = []
    for path in sorted((root / "raw").rglob("*.md")) if (root / "raw").exists() else []:
        rel = relpath(root, path)
        if rel not in raw_paths:
            raw_missing.append(rel)

    staging_missing = []
    staging_roots = [
        root / "staging" / "incomplete-captures",
        root / "staging" / "last30days",
        root / "staging" / "x-profile-digests",
    ]
    for base in staging_roots:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            rel = relpath(root, path)
            if rel not in staging_paths:
                staging_missing.append(rel)
    return raw_missing, staging_missing


def staging_promotion_candidates(root: Path) -> list[tuple[str, str]]:
    candidates = []
    base = root / "staging" / "last30days"
    if not base.exists():
        return candidates
    for path in sorted(base.glob("*.md")):
        text = path.read_text(errors="replace")
        match = re.search(r"Compile Recommendation:\s*([^\n]+)", text, re.IGNORECASE)
        recommendation = match.group(1).strip() if match else "Unknown"
        if "promote" in recommendation.lower():
            candidates.append((relpath(root, path), recommendation))
    return candidates


def section_heading_issues(text: str) -> list[tuple[str, int]]:
    lines = strip_frontmatter(text).splitlines()
    headings = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        if level == 1:
            continue
        headings.append((index, level, match.group(2).strip()))

    issues = []
    for position, (line_index, level, heading) in enumerate(headings):
        end = len(lines)
        for next_line, next_level, _ in headings[position + 1 :]:
            if next_level <= level:
                end = next_line
                break
        body = [
            line.strip()
            for line in lines[line_index + 1 : end]
            if line.strip() and not line.strip().startswith("<!--")
        ]
        if not body:
            issues.append((heading, line_index + 1))
    return issues


def parse_index_paths(root: Path) -> set[str]:
    paths = set(parse_wiki_index(root).keys())
    index = root / "wiki" / "index.md"
    if not index.exists():
        return paths
    for record in markdown_link_records(index):
        resolved = record["resolved"]
        try:
            rel = relpath(root, resolved)
        except ValueError:
            continue
        if rel.startswith("wiki/") and rel.endswith(".md"):
            paths.add(rel.removeprefix("wiki/"))
    return paths


def is_archive_page(path: Path) -> bool:
    return "archive" in path.parts


def parse_date(value: str | None) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def page_tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 2 and token not in TOKEN_STOPWORDS
    }


def content_tokens(text: str) -> set[str]:
    body = strip_frontmatter(text)
    return {
        token
        for token in re.findall(r"[a-z][a-z0-9-]{3,}", body.lower())
        if token not in TOKEN_STOPWORDS
    }


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def duplicate_page_candidates(root: Path, articles: list[Path], texts: dict[Path, str]) -> list[tuple[float, str, str, str]]:
    metadata = []
    for article in articles:
        if is_archive_page(article):
            continue
        text = texts[article]
        metadata.append(
            {
                "path": relpath(root, article),
                "title_tokens": page_tokens(page_title(article, text)),
                "tags": set(frontmatter_tags(text)),
                "content_tokens": content_tokens(text),
            }
        )

    candidates = []
    for index, left in enumerate(metadata):
        for right in metadata[index + 1 :]:
            title_score = jaccard(left["title_tokens"], right["title_tokens"])
            tag_score = jaccard(left["tags"], right["tags"])
            content_score = jaccard(left["content_tokens"], right["content_tokens"])
            shared_title = len(left["title_tokens"] & right["title_tokens"])
            shared_tags = len(left["tags"] & right["tags"])
            reason = ""
            score = 0.0
            if title_score >= 0.45 and shared_title >= 2:
                score = title_score
                reason = f"title overlap ({shared_title} shared title tokens)"
            elif tag_score >= 0.55 and shared_tags >= 3:
                score = tag_score
                reason = f"tag overlap ({shared_tags} shared tags)"
            elif content_score >= 0.35:
                score = content_score
                reason = "content-token overlap"
            if reason:
                candidates.append((score, left["path"], right["path"], reason))
    return sorted(candidates, key=lambda item: item[0], reverse=True)[:20]


def repeated_unpaged_phrases(root: Path, articles: list[Path], texts: dict[Path, str], title_norms: set[str]) -> list[tuple[str, list[str]]]:
    phrase_pages: dict[str, set[str]] = defaultdict(set)
    phrase_display: dict[str, str] = {}
    phrase_re = re.compile(r"\b([A-Z][A-Za-z0-9]+(?:[- ][A-Z][A-Za-z0-9]+){1,5})\b")
    for article in articles:
        if is_archive_page(article):
            continue
        body = strip_frontmatter(texts[article])
        rel = relpath(root, article)
        for match in phrase_re.finditer(body):
            phrase = re.sub(r"\s+", " ", match.group(1).strip())
            first_word = phrase.split(" ", 1)[0]
            if first_word in PHRASE_LEADING_STOPWORDS:
                continue
            if phrase in LINT_STOP_PHRASES:
                continue
            normalized = normalize_title(phrase)
            if not normalized or normalized in title_norms:
                continue
            tokens = page_tokens(phrase)
            if len(tokens) < 2:
                continue
            phrase_display.setdefault(normalized, phrase)
            phrase_pages[normalized].add(rel)

    candidates = []
    for normalized, pages in phrase_pages.items():
        if len(pages) >= 3:
            candidates.append((phrase_display[normalized], sorted(pages)))
    return sorted(candidates, key=lambda item: (-len(item[1]), item[0].lower()))[:25]


def linked_article_paths(root: Path, path: Path, text: str, lookup: dict[str, list[Path]]) -> set[str]:
    linked = set()
    for record in markdown_link_records(path):
        resolved = record["resolved"]
        try:
            rel = relpath(root, resolved)
        except ValueError:
            continue
        if rel.startswith("wiki/") and rel.endswith(".md"):
            linked.add(rel)
    for target in parse_wikilinks(text):
        matches = lookup.get(normalize_title(target), [])
        for match in matches:
            linked.add(relpath(root, match))
    return linked


def unlinked_title_mentions(
    root: Path,
    articles: list[Path],
    texts: dict[Path, str],
    lookup: dict[str, list[Path]],
    titles: dict[str, str],
) -> list[tuple[str, str]]:
    mentions = []
    title_items = []
    for rel, title in titles.items():
        tokens = page_tokens(title)
        if len(tokens) >= 2:
            title_items.append((rel, title, title.lower()))

    for article in articles:
        if is_archive_page(article):
            continue
        rel = relpath(root, article)
        text = texts[article]
        body_lower = strip_frontmatter(text).lower()
        linked = linked_article_paths(root, article, text, lookup)
        for target_rel, title, title_lower in title_items:
            if target_rel == rel or target_rel in linked:
                continue
            if title_lower in body_lower:
                mentions.append((rel, target_rel))
    return mentions[:60]


def review_marker_snippets(root: Path, articles: list[Path], texts: dict[Path, str]) -> list[tuple[str, int, str]]:
    snippets = []
    for article in articles:
        if is_archive_page(article):
            continue
        for line_number, line in enumerate(texts[article].splitlines(), start=1):
            if "../../raw/" in line or "raw/intentional/" in line or "raw/sweeps/" in line:
                continue
            lowered = line.lower()
            if any(marker in lowered for marker in REVIEW_MARKERS):
                snippets.append((relpath(root, article), line_number, line.strip()[:180]))
    return snippets[:40]


def build_wiki_lint_report(root: Path, stale_days: int = 30) -> str:
    sources = load_source_map(root)
    articles = wiki_articles(root)
    texts = {article: article.read_text(errors="replace") for article in articles}
    lookup, titles = article_lookup(root, articles, texts)
    actual_rels = {relpath(root, article) for article in articles}

    frontmatter_gaps = []
    empty_sections = []
    broken_markdown_links = []
    broken_raw_links = []
    dead_wikilinks = []
    inbound = Counter()
    raw_evidence_gaps = []
    huge_pages = []
    stale_or_flagged_pages = []
    today_date = dt.date.today()

    for article in articles:
        rel = relpath(root, article)
        text = texts[article]
        fm = frontmatter(text)
        missing = [field for field in REQUIRED_WIKI_FIELDS if field not in fm]
        if missing:
            frontmatter_gaps.append((rel, missing))

        for heading, line_number in section_heading_issues(text):
            empty_sections.append((rel, line_number, heading))

        for record in markdown_link_records(article):
            resolved = record["resolved"]
            target = str(record["target"])
            try:
                target_rel = relpath(root, resolved)
            except ValueError:
                target_rel = ""
            if target_rel.startswith("wiki/") and target_rel.endswith(".md"):
                inbound[target_rel] += 1
            if target_rel.startswith("raw/") and not resolved.exists():
                broken_raw_links.append((rel, target))
            elif target_rel and not resolved.exists():
                broken_markdown_links.append((rel, target))

        for target in parse_wikilinks(text):
            matches = lookup.get(normalize_title(target), [])
            if matches:
                for match in matches:
                    inbound[relpath(root, match)] += 1
            else:
                dead_wikilinks.append((rel, target))

        words = len(text.split())
        refs = raw_ref_count(text)
        if not is_archive_page(article) and (words >= 2500 or refs >= 80):
            huge_pages.append((rel, words, refs))
        if not is_archive_page(article) and refs == 0 and "Sources:" not in text and "## Sources" not in text:
            raw_evidence_gaps.append(rel)

        updated = parse_date(fm.get("updated_at") or fm.get("updated"))
        status = fm.get("status", "")
        if status in {"stale", "contradicted"}:
            stale_or_flagged_pages.append((rel, status, fm.get("updated_at") or fm.get("updated") or "<missing>"))
        elif updated and (today_date - updated).days > stale_days and status in {"active", "draft"}:
            stale_or_flagged_pages.append((rel, f"older than {stale_days} days", updated.isoformat()))
        elif not updated and not is_archive_page(article):
            stale_or_flagged_pages.append((rel, "missing updated_at", "<missing>"))

    orphan_pages = [
        rel
        for rel in sorted(actual_rels)
        if not rel.startswith("wiki/archive/") and inbound[rel] == 0
    ]

    index_paths = {f"wiki/{path}" if not path.startswith("wiki/") else path for path in parse_index_paths(root)}
    index_missing_entries = sorted(rel for rel in actual_rels if rel not in index_paths and rel not in {"wiki/log.md"})
    index_dead_entries = sorted(rel for rel in index_paths if rel not in actual_rels and rel not in {"wiki/index.md", "wiki/log.md"})

    title_norms = {normalize_title(title) for title in titles.values()}
    missing_page_candidates = repeated_unpaged_phrases(root, articles, texts, title_norms)
    cross_ref_gaps = unlinked_title_mentions(root, articles, texts, lookup, titles)
    duplicate_candidates = duplicate_page_candidates(root, articles, texts)
    review_snippets = review_marker_snippets(root, articles, texts)
    raw_missing, staging_missing = source_map_missing_paths(root, sources)
    duplicate_x_records = duplicate_x_capture_records(root)

    critical_count = (
        len(frontmatter_gaps)
        + len(broken_markdown_links)
        + len(broken_raw_links)
        + len(dead_wikilinks)
        + len(raw_missing)
        + len(staging_missing)
        + len(index_dead_entries)
    )
    warning_count = (
        len(orphan_pages)
        + len(empty_sections)
        + len(raw_evidence_gaps)
        + len(huge_pages)
        + len(stale_or_flagged_pages)
        + len(duplicate_x_records)
    )
    suggestion_count = (
        len(index_missing_entries)
        + len(missing_page_candidates)
        + len(cross_ref_gaps)
        + len(duplicate_candidates)
        + len(review_snippets)
    )
    safe_fix_count = (
        len(frontmatter_gaps)
        + len(broken_markdown_links)
        + len(dead_wikilinks)
        + len(index_missing_entries)
        + len(index_dead_entries)
        + len(empty_sections)
    )
    needs_review_count = (
        len(orphan_pages)
        + len(raw_evidence_gaps)
        + len(huge_pages)
        + len(stale_or_flagged_pages)
        + len(missing_page_candidates)
        + len(cross_ref_gaps)
        + len(duplicate_candidates)
        + len(review_snippets)
    )

    lines = [
        "---",
        "type: wiki_lint_report",
        f"created_at: {utc_now()}",
        "status: proposed",
        f"stale_days: {stale_days}",
        "---",
        "",
        f"# Second Brain Lint Report - {today()}",
        "",
        "This is a read-only report. Do not merge, delete, archive, or rewrite wiki pages until Seth approves the cleanup target.",
        "",
        "## Summary",
        "",
        f"- Pages scanned: {len(articles)}",
        f"- Critical issues: {critical_count}",
        f"- Warnings: {warning_count}",
        f"- Suggestions: {suggestion_count}",
        f"- Safe fix candidates: {safe_fix_count}",
        f"- Needs-review candidates: {needs_review_count}",
        "",
    ]

    lines.extend(["## Critical", ""])
    if not any([frontmatter_gaps, broken_markdown_links, broken_raw_links, dead_wikilinks, raw_missing, staging_missing, index_dead_entries]):
        lines.append("- No critical deterministic issues detected.")
    if frontmatter_gaps:
        lines.extend(["", "### Frontmatter Gaps", "", "| Page | Missing Fields |", "|---|---|"])
        for rel, missing in frontmatter_gaps[:50]:
            lines.append(f"| `{rel}` | {', '.join(missing)} |")
    if broken_markdown_links or broken_raw_links or dead_wikilinks:
        lines.extend(["", "### Broken Links", "", "| Page | Target | Type |", "|---|---|---|"])
        for rel, target in broken_markdown_links[:40]:
            lines.append(f"| `{rel}` | `{target}` | markdown |")
        for rel, target in broken_raw_links[:40]:
            lines.append(f"| `{rel}` | `{target}` | raw evidence |")
        for rel, target in dead_wikilinks[:40]:
            lines.append(f"| `{rel}` | `[[{target}]]` | wikilink |")
    if raw_missing or staging_missing:
        lines.extend(["", "### Source-Map Drift", ""])
        lines.append(f"- Raw markdown files missing from source map: {len(raw_missing)}")
        lines.append(f"- Staging markdown files missing from source map: {len(staging_missing)}")
        for path in raw_missing[:10]:
            lines.append(f"- Raw miss: `{path}`")
        for path in staging_missing[:10]:
            lines.append(f"- Staging miss: `{path}`")
    if index_dead_entries:
        lines.extend(["", "### Stale Index Entries", ""])
        for rel in index_dead_entries[:40]:
            lines.append(f"- `{rel}` is listed in `wiki/index.md` but no file exists.")
    lines.append("")

    lines.extend(["## Warnings", ""])
    if not any([orphan_pages, empty_sections, raw_evidence_gaps, huge_pages, stale_or_flagged_pages, duplicate_x_records]):
        lines.append("- No warning-level structural issues detected.")
    if orphan_pages:
        lines.extend(["", "### Orphan Pages", ""])
        for rel in orphan_pages[:50]:
            lines.append(f"- `{rel}` has no inbound wiki links.")
    if empty_sections:
        lines.extend(["", "### Empty Sections", "", "| Page | Line | Heading |", "|---|---:|---|"])
        for rel, line_number, heading in empty_sections[:50]:
            lines.append(f"| `{rel}` | {line_number} | {heading} |")
    if raw_evidence_gaps:
        lines.extend(["", "### Raw Evidence Gaps", ""])
        for rel in raw_evidence_gaps[:40]:
            lines.append(f"- `{rel}` has no obvious raw/source citation marker.")
    if huge_pages:
        lines.extend(["", "### Huge / Junk-Drawer Candidates", "", "| Page | Words | Raw Refs |", "|---|---:|---:|"])
        for rel, words, refs in sorted(huge_pages, key=lambda item: item[1], reverse=True)[:30]:
            lines.append(f"| `{rel}` | {words} | {refs} |")
    if stale_or_flagged_pages:
        lines.extend(["", "### Stale Or Flagged Pages", "", "| Page | Reason | Updated |", "|---|---|---|"])
        for rel, reason, updated in stale_or_flagged_pages[:50]:
            lines.append(f"| `{rel}` | {reason} | {updated} |")
    if duplicate_x_records:
        lines.extend(["", "### Duplicate X Capture/Staging Records", "", "| Status ID | Records |", "|---|---|"])
        for status_id, paths in sorted(duplicate_x_records.items())[:20]:
            joined = "<br>".join(f"`{path}`" for path in paths)
            lines.append(f"| {status_id} | {joined} |")
    lines.append("")

    lines.extend(["## Suggestions", ""])
    if not any([index_missing_entries, missing_page_candidates, cross_ref_gaps, duplicate_candidates, review_snippets]):
        lines.append("- No suggestion-level knowledge-health issues detected.")
    if index_missing_entries:
        lines.extend(["", "### Pages Missing From Index", ""])
        for rel in index_missing_entries[:50]:
            lines.append(f"- `{rel}` exists but is not listed in `wiki/index.md`.")
    if missing_page_candidates:
        lines.extend(["", "### Repeated Concepts / Entities Without Pages", "", "| Phrase | Mentioned In |", "|---|---|"])
        for phrase, pages in missing_page_candidates[:20]:
            joined = "<br>".join(f"`{page}`" for page in pages[:6])
            suffix = f"<br>... {len(pages) - 6} more" if len(pages) > 6 else ""
            lines.append(f"| {phrase} | {joined}{suffix} |")
    if cross_ref_gaps:
        lines.extend(["", "### Missing Cross-Reference Candidates", "", "| Source Page | Mentioned Page |", "|---|---|"])
        for source_rel, target_rel in cross_ref_gaps[:40]:
            lines.append(f"| `{source_rel}` | `{target_rel}` |")
    if duplicate_candidates:
        lines.extend(["", "### Duplicate / Overlap Candidates", "", "| Score | Page A | Page B | Reason |", "|---:|---|---|---|"])
        for score, left, right, reason in duplicate_candidates[:20]:
            lines.append(f"| {score:.2f} | `{left}` | `{right}` | {reason} |")
    if review_snippets:
        lines.extend(["", "### Semantic Review Markers", "", "| Page | Line | Snippet |", "|---|---:|---|"])
        for rel, line_number, snippet in review_snippets[:30]:
            safe_snippet = snippet.replace("|", "\\|")
            lines.append(f"| `{rel}` | {line_number} | {safe_snippet} |")
    lines.append("")

    lines.extend(
        [
            "## Cleanup Policy",
            "",
            "Safe to auto-fix after review:",
            "- Add missing placeholder frontmatter fields.",
            "- Repair obvious broken markdown paths when there is exactly one matching target.",
            "- Add missing `wiki/index.md` rows for existing pages.",
            "- Add obvious wikilinks for exact title mentions.",
            "",
            "Needs Seth review first:",
            "- Merge duplicate or overlapping pages.",
            "- Archive or delete orphan pages.",
            "- Split huge pages.",
            "- Resolve contradictions or stale claims.",
            "- Compile raw-only source clusters into wiki pages.",
            "",
            "## Recommended Next Action",
            "",
        ]
    )
    if critical_count:
        lines.append("1. Fix critical deterministic issues before semantic cleanup.")
    elif huge_pages:
        lines.append("1. Pick one huge page and decide whether to split it or tighten it in place.")
    elif missing_page_candidates or cross_ref_gaps:
        lines.append("1. Approve one cross-link or missing-page cluster for cleanup.")
    else:
        lines.append("1. No urgent cleanup. Keep the weekly lint running and compile approved raw-only clusters.")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_health_report(root: Path, include_qmd: bool = True) -> str:
    sources = load_source_map(root)
    raw_only = raw_only_sources(sources, None)
    raw_only_by_type = Counter(source.get("source_type", "<missing>") for source in raw_only)
    status_by_type = defaultdict(Counter)
    for source in sources:
        status_by_type[source.get("source_type", "<missing>")][source.get("status", "<missing>")] += 1

    articles = wiki_articles(root)
    inbound = Counter()
    for article in articles:
        for target in markdown_links(article):
            try:
                rel_target = relpath(root, target)
            except ValueError:
                continue
            if rel_target.startswith("wiki/") and rel_target.endswith(".md"):
                inbound[rel_target] += 1

    huge_pages = []
    stale_pages = []
    for article in articles:
        text = article.read_text(errors="replace")
        fm = frontmatter(text)
        words = len(text.split())
        refs = raw_ref_count(text)
        if not is_archive_page(article) and (words >= 2500 or refs >= 80):
            huge_pages.append((relpath(root, article), words, refs))
        if fm.get("status") in {"stale", "contradicted"} or not fm.get("updated_at"):
            stale_pages.append((relpath(root, article), fm.get("status", "<missing>"), fm.get("updated_at", "<missing>")))

    orphan_pages = [
        relpath(root, article)
        for article in articles
        if not relpath(root, article).startswith("wiki/archive/") and inbound[relpath(root, article)] == 0
    ]
    raw_missing, staging_missing = source_map_missing_paths(root, sources)
    duplicates = duplicate_x_capture_records(root)
    promotion_candidates = staging_promotion_candidates(root)

    lines = [
        "---",
        "type: wiki_health_report",
        f"created_at: {utc_now()}",
        "status: proposed",
        "---",
        "",
        f"# Wiki Health Report - {today()}",
        "",
        "## Counts",
        "",
        f"- Source-map entries: {len(sources)}",
        f"- Wiki articles: {len(articles)}",
        f"- Raw-only sources: {len(raw_only)}",
        "",
        "### Raw-Only By Source Type",
        "",
        "| Source Type | Raw-Only Count |",
        "|---|---:|",
    ]
    for source_type, count in raw_only_by_type.most_common():
        lines.append(f"| {source_type} | {count} |")
    if not raw_only_by_type:
        lines.append("| None | 0 |")
    lines.append("")

    lines.extend(["### Status By Source Type", "", "| Source Type | Status Counts |", "|---|---|"])
    for source_type in sorted(status_by_type):
        status_text = ", ".join(f"{status}: {count}" for status, count in status_by_type[source_type].most_common())
        lines.append(f"| {source_type} | {status_text} |")
    lines.append("")

    if include_qmd:
        lines.extend(["## QMD Snapshot", "", "```text", run_qmd_status(root), "```", ""])

    lines.extend(["## Wiki Shape", ""])
    lines.append("### Huge / Junk-Drawer Candidates")
    lines.append("")
    if huge_pages:
        lines.extend(["| Page | Words | Raw Refs |", "|---|---:|---:|"])
        for page, words, refs in sorted(huge_pages, key=lambda item: item[1], reverse=True)[:20]:
            lines.append(f"| `{page}` | {words} | {refs} |")
    else:
        lines.append("- No huge pages crossed the current thresholds.")
    lines.append("")

    lines.append("### Orphan Wiki Pages")
    lines.append("")
    if orphan_pages:
        for page in sorted(orphan_pages)[:30]:
            lines.append(f"- `{page}`")
    else:
        lines.append("- No non-archive orphan pages detected.")
    lines.append("")

    lines.append("### Stale / Missing Lifecycle Metadata")
    lines.append("")
    if stale_pages:
        lines.extend(["| Page | Status | Updated |", "|---|---|---|"])
        for page, status, updated in stale_pages[:30]:
            lines.append(f"| `{page}` | {status} | {updated} |")
    else:
        lines.append("- No stale, contradicted, or metadata-missing pages detected.")
    lines.append("")

    lines.extend(["## Source Map Hygiene", ""])
    lines.append(f"- Raw markdown files missing from source map: {len(raw_missing)}")
    lines.append(f"- Staging markdown files missing from source map: {len(staging_missing)}")
    if raw_missing[:10]:
        lines.append("")
        lines.append("First raw misses:")
        for path in raw_missing[:10]:
            lines.append(f"- `{path}`")
    if staging_missing[:10]:
        lines.append("")
        lines.append("First staging misses:")
        for path in staging_missing[:10]:
            lines.append(f"- `{path}`")
    lines.append("")

    lines.append("### Duplicate X capture/staging records")
    lines.append("")
    if duplicates:
        lines.extend(["| Status ID | Records |", "|---|---|"])
        for status_id, paths in sorted(duplicates.items())[:20]:
            joined = "<br>".join(f"`{path}`" for path in paths)
            lines.append(f"| {status_id} | {joined} |")
    else:
        lines.append("- None detected.")
    lines.append("")

    lines.extend(["## Staging Ready For Promotion", ""])
    if promotion_candidates:
        lines.extend(["| Staging Digest | Recommendation |", "|---|---|"])
        for path, recommendation in promotion_candidates:
            lines.append(f"| `{path}` | {recommendation} |")
    else:
        lines.append("- No Last30Days staging digests currently say `promote`.")
    lines.append("")

    next_actions = []
    if raw_missing or staging_missing:
        next_actions.append("Backfill `state/source-map.json` for markdown files missing from the provenance map.")
    if duplicates:
        next_actions.append("Resolve duplicate X staging records after their raw captures are confirmed in source-map.")
    next_actions.extend(
        [
            "Run `scripts/wiki-organize.sh --propose --limit 100` to generate a raw-only X promotion queue.",
            "Approve one proposal cluster, then compile it into existing medium wiki pages before creating new pages.",
            "Split or tighten huge pages only when a cluster has a clear reusable concept boundary.",
            "Run `scripts/qmd-refresh.sh --embed` after approved wiki/source-map changes.",
        ]
    )
    lines.extend(["## Ranked Next Actions", ""])
    for index, action in enumerate(next_actions[:5], start=1):
        lines.append(f"{index}. {action}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def find_intentional_raw_quality_errors(root: Path) -> list[str]:
    sources = load_source_map(root)
    complete_raw_paths = {
        source.get("raw_path")
        for source in sources
        if source.get("capture_quality") == "complete" and source.get("raw_path")
    }
    errors = []
    base = root / "raw" / "intentional"
    if not base.exists():
        return errors
    for raw_path in sorted(base.rglob("*.md")):
        text = raw_path.read_text(errors="replace")
        rel = relpath(root, raw_path)
        if "capture_quality: complete" in text:
            continue
        if rel in complete_raw_paths:
            continue
        errors.append(
            f"{rel}: intentional raw files must declare capture_quality: complete "
            "or have a complete source-map entry"
        )
    return errors


def unique_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    for index in range(2, 1000):
        candidate = path.with_name(f"{stem}-{index}{suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not find available output path near {path}")


def write_report(root: Path, name: str, content: str) -> Path:
    out_dir = root / "staging" / "maintenance"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = unique_output_path(out_dir / f"{today()}-{name}.md")
    path.write_text(content)
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Seth Second Brain wiki maintenance helpers")
    parser.add_argument("--root", default=".", help="Repository root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    organize = subparsers.add_parser("organize", help="Generate a wiki organization proposal")
    organize.add_argument("--limit", type=int, default=100)
    organize.add_argument("--source-type", default="x")
    organize.add_argument("--no-qmd", action="store_true")
    organize.add_argument("--stdout", action="store_true")

    health = subparsers.add_parser("health", help="Generate a wiki health report")
    health.add_argument("--no-qmd", action="store_true")
    health.add_argument("--stdout", action="store_true")

    lint = subparsers.add_parser("lint", help="Generate a read-only wiki lint report")
    lint.add_argument("--stale-days", type=int, default=30)
    lint.add_argument("--stdout", action="store_true")

    subparsers.add_parser("lint-raw-quality", help="Report intentional raw quality metadata errors")

    args = parser.parse_args()
    root = Path(args.root).resolve()

    if args.command == "organize":
        content = build_organization_proposal(
            root,
            limit=args.limit,
            source_type=None if args.source_type == "all" else args.source_type,
            include_qmd=not args.no_qmd,
        )
        if args.stdout:
            print(content, end="")
            return 0
        path = write_report(root, "wiki-organization-proposal", content)
        print(path.relative_to(root).as_posix())
        return 0

    if args.command == "health":
        content = build_health_report(root, include_qmd=not args.no_qmd)
        if args.stdout:
            print(content, end="")
            return 0
        path = write_report(root, "wiki-health-report", content)
        print(path.relative_to(root).as_posix())
        return 0

    if args.command == "lint":
        content = build_wiki_lint_report(root, stale_days=args.stale_days)
        if args.stdout:
            print(content, end="")
            return 0
        path = write_report(root, "wiki-lint-report", content)
        print(path.relative_to(root).as_posix())
        return 0

    if args.command == "lint-raw-quality":
        errors = find_intentional_raw_quality_errors(root)
        for error in errors:
            print(error)
        return 1 if errors else 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
