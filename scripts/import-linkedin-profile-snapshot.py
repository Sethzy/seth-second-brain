#!/usr/bin/env python3
"""Import an authenticated LinkedIn activity capture into raw + staging lanes."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "Champion enablement and internal selling": ("champion", "internal", "stakeholder", "consensus", "multithread", "buying team"),
    "Discovery and deal process": ("discovery", "deal", "decision", "next step", "procurement", "pipeline", "forecast"),
    "Executive messaging and business cases": ("executive", "business case", "memo", "deck", "story", "message", "forwardable"),
    "Outbound and account strategy": ("outbound", "prospect", "account", "cold", "territory", "personalization"),
    "AI and GTM systems": (" ai ", "agent", "automation", "context layer", "revops", "gtm", "workflow"),
    "Sales leadership and coaching": ("coach", "leader", "manager", "rep", "quota", "enablement", "hiring"),
}


def safe_int(value: object) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def first_line(text: str, limit: int = 180) -> str:
    line = re.sub(r"\s+", " ", text).strip()
    if len(line) <= limit:
        return line
    return line[: limit - 1].rstrip() + "…"


def render_raw(name: str, slug: str, profile_url: str, posts: list[dict], captured_at: str) -> str:
    lines = [
        "---",
        "type: raw_capture",
        "source_type: linkedin_profile_timeline",
        f"url: {profile_url}",
        f"profile_slug: {slug}",
        f"captured_at: {captured_at}",
        "requested_count: 100",
        f"captured_count: {len(posts)}",
        f"capture_quality: {'complete_authenticated_profile_activity' if len(posts) >= 100 else 'complete_available_profile_activity_under_100'}",
        "status: staged",
        "trust_lane: intentional",
        "---",
        "",
        f"# {name} — latest 100 LinkedIn posts",
        "",
        "## Source",
        "",
        f"- Profile: [{profile_url}]({profile_url})",
        f"- Captured: {captured_at}",
        f"- Captured posts: {len(posts)}",
        f"- Availability: {'Latest 100 captured.' if len(posts) >= 100 else f'Profile exposed only {len(posts)} posts; all available history captured.'}",
        "- Method: authenticated LinkedIn profile activity feed; full screen-reader-visible post bodies preserved.",
        "- Date note: LinkedIn exposed relative publication dates in this view; these are preserved verbatim.",
        "",
        "## Posts",
        "",
    ]
    for index, post in enumerate(posts[:100], start=1):
        url = post.get("url") or f"https://www.linkedin.com/feed/update/{post.get('urn')}/"
        lines.extend([
            f"### {index}. {post.get('published_relative') or 'Unknown date'}",
            "",
            f"- URL: [{url}]({url})",
            f"- Activity URN: `{post.get('urn') or 'Unknown'}`",
            f"- Author: {post.get('author') or name}",
            f"- Headline: {post.get('author_headline') or 'Unknown'}",
            f"- Engagement: {safe_int(post.get('reactions'))} reactions, {safe_int(post.get('comments'))} comments, {safe_int(post.get('reposts'))} reposts",
            "",
            "#### Verbatim visible post body",
            "",
            (post.get("content") or post.get("visible_text") or "(No text captured.)").strip(),
            "",
        ])
        if post.get("embedded_text"):
            lines.extend(["#### Embedded or reshared visible text", "", post["embedded_text"].strip(), ""])
        if post.get("media_alt"):
            lines.extend(["#### Media descriptions", "", *[f"- {item}" for item in post["media_alt"]], ""])
    return "\n".join(lines).rstrip() + "\n"


def render_digest(name: str, slug: str, profile_url: str, posts: list[dict], raw_rel: str, captured_at: str) -> str:
    theme_counts = {}
    for theme, needles in THEMES.items():
        theme_counts[theme] = sum(
            1 for post in posts if any(needle in f" {(post.get('content') or '').lower()} " for needle in needles)
        )
    ranked = sorted(
        posts,
        key=lambda post: safe_int(post.get("reactions")) + 2 * safe_int(post.get("comments")) + 3 * safe_int(post.get("reposts")),
        reverse=True,
    )
    lines = [
        "---",
        f"title: {name} LinkedIn Latest 100 Posts Digest",
        f"created: {captured_at[:10]}",
        "status: staged",
        "source_type: linkedin",
        "trust_lane: intentional",
        f"capture_quality: {'authenticated_latest_100_with_deterministic_digest' if len(posts) >= 100 else 'authenticated_complete_available_history_with_deterministic_digest'}",
        f"raw_path: ../../{raw_rel}",
        "compiled_to_wiki: false",
        "---",
        "",
        f"# {name} LinkedIn Latest 100 Posts Digest",
        "",
        "## Source Snapshot",
        "",
        f"- Raw snapshot: [latest 100 posts](../../{raw_rel})",
        f"- Profile: [{profile_url}]({profile_url})",
        f"- Captured: {captured_at}",
        f"- Records reviewed: {len(posts)}",
        f"- Availability: {'Latest 100 captured.' if len(posts) >= 100 else f'Only {len(posts)} posts were available; all were captured.'}",
        "- Status: staged only; no wiki promotion.",
        "",
        "## Theme Counts",
        "",
        "| Theme | Matching posts |",
        "|---|---:|",
    ]
    for theme, count in sorted(theme_counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"| {theme} | {count} |")
    lines.extend(["", "## Highest-Engagement Signals For Review", ""])
    for index, post in enumerate(ranked[:10], start=1):
        score = safe_int(post.get("reactions")) + 2 * safe_int(post.get("comments")) + 3 * safe_int(post.get("reposts"))
        lines.append(
            f"{index}. [{first_line(post.get('content') or post.get('visible_text') or '(No text)')}]"
            f"({post.get('url')}) — engagement score {score}; {post.get('published_relative') or 'unknown date'}."
        )
    lines.extend([
        "",
        "## Review Guidance",
        "",
        "- Prioritize recurring enterprise-sales mechanisms over isolated promotional claims.",
        "- Treat product results, customer outcomes, and market-size claims as author positioning until independently verified.",
        "- Use the raw snapshot for exact wording, context, and activity URLs.",
        "- Keep this digest staged until Seth requests promotion.",
        "",
    ])
    return "\n".join(lines)


def update_source_map(raw_path: Path, digest_path: Path, name: str, profile_url: str, count: int, captured_at: str) -> None:
    state_path = ROOT / "state" / "source-map.json"
    state = json.loads(state_path.read_text())
    sources = state.setdefault("sources", [])
    raw_rel = raw_path.relative_to(ROOT).as_posix()
    digest_rel = digest_path.relative_to(ROOT).as_posix()
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    def upsert(item_id: str, payload: dict) -> None:
        existing = next((item for item in sources if item.get("id") == item_id), None)
        if existing:
            created = existing.get("created_at", now)
            existing.clear()
            existing.update(payload)
            existing["created_at"] = created
        else:
            payload["created_at"] = now
            sources.append(payload)

    upsert(raw_rel, {
        "id": raw_rel,
        "title": f"{name} LinkedIn latest 100 posts",
        "url": profile_url,
        "source_type": "linkedin_profile_timeline",
        "trust_lane": "intentional",
        "capture_quality": "complete_authenticated_profile_activity" if count >= 100 else "complete_available_profile_activity_under_100",
        "raw_path": raw_rel,
        "staging_path": digest_rel,
        "status": "staged",
        "wiki_paths": [],
        "staging_paths": [digest_rel],
        "updated_at": now,
        "notes": f"Authenticated capture of {count} latest visible LinkedIn profile posts at {captured_at}; staged without wiki promotion.",
    })
    upsert(digest_rel, {
        "id": digest_rel,
        "title": f"{name} LinkedIn latest 100 posts digest",
        "url": profile_url,
        "source_type": "linkedin_digest",
        "trust_lane": "staging",
        "capture_quality": "deterministic_digest_from_authenticated_snapshot",
        "raw_path": raw_rel,
        "staging_path": digest_rel,
        "status": "staged",
        "wiki_paths": [],
        "staging_paths": [digest_rel],
        "updated_at": now,
        "notes": "Fresh deterministic routing digest; not promoted to wiki.",
    })
    state_path.write_text(json.dumps(state, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capture_json")
    parser.add_argument("slug")
    parser.add_argument("name")
    parser.add_argument("profile_url")
    parser.add_argument("--allow-fewer", action="store_true")
    args = parser.parse_args()
    payload = json.loads(Path(args.capture_json).read_text())
    posts = payload.get("posts") or []
    if len(posts) < 100 and not args.allow_fewer:
        raise SystemExit(f"Refusing incomplete capture: expected 100 posts, found {len(posts)}")
    posts = posts[:100]
    captured_at = payload.get("captured_at") or dt.datetime.now().astimezone().isoformat(timespec="seconds")
    date = captured_at[:10]
    raw_path = ROOT / "raw" / "intentional" / "web" / f"{date}-{args.slug}-linkedin-latest-100-posts.md"
    digest_path = ROOT / "staging" / "linkedin-profile-digests" / f"{date}-{args.slug}-latest-100-posts-digest.md"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    digest_path.parent.mkdir(parents=True, exist_ok=True)
    if raw_path.exists() or digest_path.exists():
        raise SystemExit("Refusing to overwrite an existing capture or digest")
    raw_text = render_raw(args.name, args.slug, args.profile_url, posts, captured_at)
    raw_path.write_text(raw_text)
    digest_path.write_text(render_digest(args.name, args.slug, args.profile_url, posts, raw_path.relative_to(ROOT).as_posix(), captured_at))
    update_source_map(raw_path, digest_path, args.name, args.profile_url, len(posts), captured_at)
    print(json.dumps({
        "raw": raw_path.relative_to(ROOT).as_posix(),
        "digest": digest_path.relative_to(ROOT).as_posix(),
        "count": len(posts),
        "sha256": hashlib.sha256(raw_text.encode()).hexdigest(),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
