#!/usr/bin/env python3
"""Capture exact X URLs via Last30Days' authenticated Bird/TweetDetail path."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GTM_SCRIPTS = Path("/Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts")
DETAIL_SCRIPT = ROOT / "scripts" / "x-bird-tweet-detail.mjs"
URL_RE = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/([A-Za-z0-9_]+)/status/(\d+)(?:[^\s]*)?")


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:90] or fallback).strip("-")


def extract_credentials(profile: str) -> dict[str, str]:
    sys.path.insert(0, str(GTM_SCRIPTS))
    from lib import env  # type: ignore

    creds = env.extract_browser_credentials({
        "FROM_BROWSER": "chrome",
        "LAST30DAYS_CHROME_PROFILE": profile,
    })
    if not creds.get("AUTH_TOKEN") or not creds.get("CT0"):
        raise RuntimeError(f"Could not extract X auth cookies from Chrome {profile}.")
    return creds


def tweet_detail(status_id: str, creds: dict[str, str]) -> dict:
    env = os.environ.copy()
    env.update(creds)
    result = subprocess.run(
        ["node", str(DETAIL_SCRIPT), status_id],
        text=True,
        capture_output=True,
        timeout=45,
        env=env,
        cwd=str(ROOT),
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "TweetDetail failed")
    return json.loads(result.stdout)


def parse_urls(values: list[str], stdin_text: str) -> list[tuple[str, str, str]]:
    text = "\n".join(values) + "\n" + stdin_text
    out: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for match in URL_RE.finditer(text):
        handle, status_id = match.groups()
        url = f"https://x.com/{handle}/status/{status_id}"
        if url in seen:
            continue
        seen.add(url)
        out.append((handle, status_id, url))
    return out


def is_complete_x_capture(tweet: dict) -> tuple[bool, str]:
    text = (tweet.get("text") or "").strip()
    if not text:
        return False, "TweetDetail returned no text."
    article = tweet.get("article")
    if article:
        preview = (article.get("previewText") or "").strip()
        title = (article.get("title") or "").strip()
        body_without_title = text
        if title and body_without_title.startswith(title):
            body_without_title = body_without_title[len(title):].strip()
        if preview and len(body_without_title) <= len(preview) + 80:
            return False, "TweetDetail exposed an X Article card/title/preview, but not confirmed full article body."
        if len(body_without_title) < 500:
            return False, "TweetDetail exposed article text, but it is too short to trust as the full article body."
        return True, "TweetDetail returned full X Article text through article field toggles."
    return True, "TweetDetail returned complete normal-post text."


def render_common(tweet: dict, source_url: str, quality: str, status: str, trust_lane: str, note: str) -> str:
    author = tweet.get("author") or {}
    username = author.get("username") or "unknown"
    name = author.get("name") or username
    created = tweet.get("createdAt") or "Unknown"
    canonical = f"https://x.com/{username}/status/{tweet.get('id')}"
    text = (tweet.get("text") or "").strip()
    article = tweet.get("article") or {}
    quoted = tweet.get("quotedTweet")
    media = tweet.get("media") or []
    captured_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")

    lines = [
        "---",
        f"type: {'raw_capture' if quality == 'complete' else 'incomplete_capture'}",
        "source_type: x",
        f"url: {canonical}",
        f"original_url: {source_url}",
        f"author: {json.dumps(name)}",
        f"handle: {username}",
        f"status_id: {tweet.get('id')}",
        f"captured_at: {captured_at}",
        f"published_at: {json.dumps(created)}",
        f"capture_quality: {quality}",
        f"status: {status}",
        f"trust_lane: {trust_lane}",
        "metrics:",
        f"  replies: {tweet.get('replyCount')}",
        f"  reposts: {tweet.get('retweetCount')}",
        f"  likes: {tweet.get('likeCount')}",
        "---",
        "",
        f"# X post by @{username}",
        "",
        "## Source",
        "",
        f"- Original: [{source_url}]({source_url})",
        f"- Canonical: [{canonical}]({canonical})",
        f"- Author: {name} (@{username})",
        "",
        "## Verbatim Text",
        "",
        text or "(No text captured.)",
    ]
    if article:
        lines.extend([
            "",
            "## X Article Metadata",
            "",
            f"- Title: {article.get('title') or 'Unknown'}",
            f"- Preview: {article.get('previewText') or 'Unknown'}",
            "",
            "Note: X Article metadata is not the full article body.",
        ])
    if quoted:
        q_author = quoted.get("author") or {}
        q_user = q_author.get("username") or "unknown"
        lines.extend([
            "",
            "## Quoted Post",
            "",
            f"- URL: https://x.com/{q_user}/status/{quoted.get('id')}",
            f"- Author: {q_author.get('name') or q_user} (@{q_user})",
            "",
            quoted.get("text") or "",
        ])
    if media:
        lines.extend(["", "## Media", ""])
        for item in media:
            if item.get("url"):
                lines.append(f"- {item.get('type')}: {item.get('url')}")
            if item.get("videoUrl"):
                lines.append(f"- video: {item.get('videoUrl')}")
    lines.extend(["", "## Capture Note", "", note])
    return "\n".join(lines).strip() + "\n"


def update_source_map(path: Path, tweet: dict, quality: str, source_url: str) -> None:
    state_path = ROOT / "state" / "source-map.json"
    state = json.loads(state_path.read_text())
    sources = state.setdefault("sources", [])
    rel = path.relative_to(ROOT).as_posix()
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    title = f"X post by @{(tweet.get('author') or {}).get('username', 'unknown')} {tweet.get('id')}"
    existing = next((item for item in sources if item.get("id") == rel or item.get("url") == source_url), None)
    payload = {
        "id": rel,
        "title": title,
        "url": f"https://x.com/{(tweet.get('author') or {}).get('username', 'unknown')}/status/{tweet.get('id')}",
        "source_type": "x",
        "trust_lane": "intentional" if quality == "complete" else "incomplete",
        "capture_quality": quality,
        "raw_path": rel if quality == "complete" else None,
        "staging_path": None if quality == "complete" else rel,
        "status": "raw" if quality == "complete" else "partial",
        "wiki_paths": [],
        "staging_paths": [] if quality == "complete" else [rel],
        "created_at": existing.get("created_at", now) if existing else now,
        "updated_at": now,
        "notes": "Captured through Last30Days authenticated Bird/TweetDetail path.",
    }
    if existing:
        existing.clear()
        existing.update(payload)
    else:
        sources.append(payload)
    state_path.write_text(json.dumps(state, indent=2) + "\n")


def remove_prior_incomplete(status_id: str) -> None:
    staging = ROOT / "staging" / "incomplete-captures" / "x"
    for path in staging.glob(f"{status_id}-*.md"):
        path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture exact X URLs through Last30Days authenticated Bird/TweetDetail.")
    parser.add_argument("urls", nargs="*")
    parser.add_argument("--chrome-profile", default="Profile 3")
    ns = parser.parse_args()

    stdin_text = "" if sys.stdin.isatty() else sys.stdin.read()
    urls = parse_urls(ns.urls, stdin_text)
    if not urls:
        print("No X status URLs found.", file=sys.stderr)
        return 2

    creds = extract_credentials(ns.chrome_profile)
    raw_dir = ROOT / "raw" / "intentional" / "x"
    staging_dir = ROOT / "staging" / "incomplete-captures" / "x"
    raw_dir.mkdir(parents=True, exist_ok=True)
    staging_dir.mkdir(parents=True, exist_ok=True)

    for _handle, status_id, source_url in urls:
        detail = tweet_detail(status_id, creds)
        tweet = detail["tweet"]
        complete, note = is_complete_x_capture(tweet)
        username = (tweet.get("author") or {}).get("username") or _handle
        title_bits = [username, tweet.get("text") or status_id]
        filename = f"{status_id}-{slugify(' '.join(title_bits), status_id)}.md"
        remove_prior_incomplete(status_id)
        if complete:
            path = raw_dir / filename
            text = render_common(tweet, source_url, "complete", "raw", "intentional", note)
        else:
            path = staging_dir / filename
            text = render_common(tweet, source_url, "partial", "partial", "incomplete", note)
        if path.exists() and complete:
            print(path)
            update_source_map(path, tweet, "complete", source_url)
            continue
        path.write_text(text)
        update_source_map(path, tweet, "complete" if complete else "partial", source_url)
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
