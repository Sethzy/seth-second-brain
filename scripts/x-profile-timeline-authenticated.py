#!/usr/bin/env python3
"""Capture X profile timelines into the Second Brain sweep lane."""

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
USER_TWEETS_SCRIPT = ROOT / "scripts" / "x-bird-user-tweets.mjs"
PROFILE_RE = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/([A-Za-z0-9_]+)(?:/?(?:\?[^\s]*)?)?$")
HANDLE_RE = re.compile(r"^@?([A-Za-z0-9_]{1,15})$")


def parse_handle(value: str) -> tuple[str, str]:
    value = value.strip()
    match = PROFILE_RE.match(value)
    if match:
        handle = match.group(1)
        return handle, f"https://x.com/{handle}"
    match = HANDLE_RE.match(value)
    if match:
        handle = match.group(1)
        return handle, f"https://x.com/{handle}"
    raise ValueError(f"Not an X profile URL or handle: {value}")


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


def fetch_timeline(handle: str, count: int, offset: int, creds: dict[str, str]) -> dict:
    env = os.environ.copy()
    env.update(creds)
    fetch_count = count + offset
    result = subprocess.run(
        ["node", str(USER_TWEETS_SCRIPT), handle, "--count", str(fetch_count)],
        text=True,
        capture_output=True,
        timeout=180,
        env=env,
        cwd=str(ROOT),
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "UserTweets failed")
    payload = json.loads(result.stdout)
    all_tweets = payload.get("tweets") or []
    payload["fetched_count"] = len(all_tweets)
    payload["tweets"] = all_tweets[offset:offset + count]
    return payload


def safe_filename(base: str) -> Path:
    target = ROOT / "raw" / "sweeps" / "x" / base
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    for index in range(2, 100):
        candidate = target.with_name(f"{stem}-{index}{suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Too many existing captures matching {target.name}")


def metric(value: object) -> str:
    return "Unknown" if value is None else str(value)


def render_media(media: list[dict]) -> list[str]:
    lines: list[str] = []
    for item in media:
        if item.get("url"):
            lines.append(f"- {item.get('type')}: {item.get('url')}")
        if item.get("videoUrl"):
            lines.append(f"- video: {item.get('videoUrl')}")
    return lines


def render_post(index: int, tweet: dict) -> list[str]:
    author = tweet.get("author") or {}
    username = author.get("username") or "unknown"
    url = f"https://x.com/{username}/status/{tweet.get('id')}"
    lines = [
        f"### {index}. {tweet.get('createdAt') or 'Unknown'}",
        "",
        f"- URL: [{url}]({url})",
        f"- Author: {author.get('name') or username} (@{username})",
        f"- Metrics: replies {metric(tweet.get('replyCount'))}, reposts {metric(tweet.get('retweetCount'))}, likes {metric(tweet.get('likeCount'))}",
        "",
        "#### Verbatim Text",
        "",
        (tweet.get("text") or "").strip() or "(No text captured.)",
    ]
    quoted = tweet.get("quotedTweet")
    if quoted:
        q_author = quoted.get("author") or {}
        q_user = q_author.get("username") or "unknown"
        lines.extend([
            "",
            "#### Quoted Post",
            "",
            f"- URL: https://x.com/{q_user}/status/{quoted.get('id')}",
            f"- Author: {q_author.get('name') or q_user} (@{q_user})",
            "",
            (quoted.get("text") or "").strip(),
        ])
    media = tweet.get("media") or []
    if media:
        lines.extend(["", "#### Media", "", *render_media(media)])
    return lines


def render_snapshot(handle: str, profile_url: str, requested_count: int, offset: int, payload: dict) -> str:
    tweets = payload.get("tweets") or []
    fetched_count = payload.get("fetched_count") or len(tweets)
    captured_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    range_start = offset + 1
    range_end = offset + len(tweets)
    lines = [
        "---",
        "type: raw_sweep",
        "source_type: x_profile_timeline",
        f"url: {profile_url}",
        f"handle: {handle}",
        f"user_id: {payload.get('userId') or 'Unknown'}",
        f"captured_at: {captured_at}",
        f"requested_count: {requested_count}",
        f"captured_count: {len(tweets)}",
        f"timeline_offset: {offset}",
        f"timeline_range: {range_start}-{range_end}",
        f"fetched_for_offset_count: {fetched_count}",
        "capture_quality: generated_profile_timeline_snapshot",
        "status: staged",
        "trust_lane: sweep",
        "---",
        "",
        f"# X profile timeline snapshot: @{handle} posts {range_start}-{range_end}",
        "",
        "## Source",
        "",
        f"- Profile: [{profile_url}]({profile_url})",
        f"- Timeline range: posts {range_start}-{range_end} at capture time",
        f"- Timeline offset: {offset}",
        f"- Requested posts: {requested_count}",
        f"- Captured posts: {len(tweets)}",
        "- Capture method: authenticated Bird/X UserTweets timeline via Chrome Profile 3 cookies.",
        "",
        "## Capture Notes",
        "",
        "This is a sweep snapshot for review and synthesis. It preserves the timeline text returned by X at capture time, but durable wiki claims should cite this file and remain conservative about recency, deleted posts, or ranking differences.",
        "",
        "## Posts",
        "",
    ]
    for index, tweet in enumerate(tweets, start=1):
        lines.extend(render_post(index, tweet))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_source_map(path: Path, handle: str, profile_url: str, requested_count: int, offset: int, captured_count: int) -> None:
    state_path = ROOT / "state" / "source-map.json"
    state = json.loads(state_path.read_text())
    sources = state.setdefault("sources", [])
    rel = path.relative_to(ROOT).as_posix()
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    existing = next((item for item in sources if item.get("id") == rel), None)
    range_start = offset + 1
    range_end = offset + captured_count
    payload = {
        "id": rel,
        "title": f"X profile timeline snapshot: @{handle} posts {range_start}-{range_end}",
        "url": profile_url,
        "source_type": "x_profile_timeline",
        "trust_lane": "sweep",
        "capture_quality": "generated_profile_timeline_snapshot",
        "raw_path": rel,
        "staging_path": None,
        "status": "staged",
        "wiki_paths": [],
        "staging_paths": [],
        "created_at": existing.get("created_at", now) if existing else now,
        "updated_at": now,
        "notes": f"Captured {captured_count} posts from timeline offset {offset} through authenticated Bird/UserTweets profile timeline path.",
    }
    if existing:
        existing.clear()
        existing.update(payload)
    else:
        sources.append(payload)
    state_path.write_text(json.dumps(state, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture X profile timelines into raw/sweeps/x.")
    parser.add_argument("profiles", nargs="+", help="X profile URLs or handles")
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--offset", type=int, default=0, help="Skip this many newest timeline posts before writing the snapshot")
    parser.add_argument("--chrome-profile", default="Profile 3")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and print counts without writing files")
    ns = parser.parse_args()

    if ns.count <= 0:
        raise SystemExit("--count must be positive")
    if ns.offset < 0:
        raise SystemExit("--offset must be non-negative")

    parsed = [parse_handle(value) for value in ns.profiles]
    creds = extract_credentials(ns.chrome_profile)
    out_dir = ROOT / "raw" / "sweeps" / "x"
    out_dir.mkdir(parents=True, exist_ok=True)
    capture_date = dt.date.today().isoformat()

    for handle, profile_url in parsed:
        payload = fetch_timeline(handle, ns.count, ns.offset, creds)
        tweets = payload.get("tweets") or []
        if ns.dry_run:
            print(f"@{handle}: fetched {payload.get('fetched_count') or len(tweets)} posts, selected {len(tweets)} after offset {ns.offset}")
            continue
        range_start = ns.offset + 1
        range_end = ns.offset + len(tweets)
        path = safe_filename(f"{capture_date}-{handle.lower()}-posts-{range_start}-{range_end}.md")
        path.write_text(render_snapshot(handle, profile_url, ns.count, ns.offset, payload))
        update_source_map(path, handle, profile_url, ns.count, ns.offset, len(tweets))
        print(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
