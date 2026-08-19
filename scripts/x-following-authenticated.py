#!/usr/bin/env python3
"""Export an X account's Following list using authenticated Chrome cookies."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path

from last30days_runtime import extract_browser_credentials, resolve_last30days_scripts_dir


ROOT = Path(__file__).resolve().parents[1]
FOLLOWING_SCRIPT = ROOT / "scripts" / "x-bird-following.mjs"
URL_RE = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/([A-Za-z0-9_]+)(?:/following)?(?:\?[^\s]*)?$")
HANDLE_RE = re.compile(r"^@?([A-Za-z0-9_]{1,15})$")


def parse_handle(value: str) -> str:
    value = value.strip()
    match = URL_RE.match(value) or HANDLE_RE.match(value)
    if not match:
        raise ValueError(f"Not an X profile/following URL or handle: {value}")
    return match.group(1)


def fetch_following(handle: str, count: int, creds: dict[str, str]) -> dict:
    command_env = os.environ.copy()
    command_env.update(creds)
    command_env["LAST30DAYS_SCRIPTS_DIR"] = str(resolve_last30days_scripts_dir())
    result = subprocess.run(
        ["node", str(FOLLOWING_SCRIPT), handle, "--count", str(count)],
        text=True,
        capture_output=True,
        timeout=600,
        env=command_env,
        cwd=str(ROOT),
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Following export failed")
    return json.loads(result.stdout)


def write_csv(path: Path, users: list[dict]) -> None:
    fields = [
        "id", "username", "name", "description", "followersCount",
        "followingCount", "isBlueVerified", "profileImageUrl", "createdAt", "url",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for user in users:
            row = {field: user.get(field) for field in fields}
            row["url"] = f"https://x.com/{user.get('username')}"
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export an authenticated X Following list to CSV and JSON.")
    parser.add_argument("profile", help="X profile/following URL or @handle")
    parser.add_argument("--count", type=int, default=5000, help="Maximum accounts to fetch (default: 5000)")
    parser.add_argument(
        "--chrome-profile",
        default=os.environ.get("SECOND_BRAIN_X_CHROME_PROFILE", "Profile 3"),
    )
    parser.add_argument("--output-dir", type=Path, default=ROOT / "outputs" / "x-following")
    ns = parser.parse_args()
    if ns.count <= 0:
        raise SystemExit("--count must be positive")

    handle = parse_handle(ns.profile)
    payload = fetch_following(handle, ns.count, extract_browser_credentials(ns.chrome_profile))
    users = payload.get("users") or []
    ns.output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{dt.date.today().isoformat()}-{handle.lower()}-following"
    json_path = ns.output_dir / f"{stem}.json"
    csv_path = ns.output_dir / f"{stem}.csv"
    handles_path = ns.output_dir / f"{stem}-handles.txt"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(csv_path, users)
    handles_path.write_text(
        "".join(f"@{user['username']}\n" for user in users),
        encoding="utf-8",
    )
    print(json.dumps({
        "count": len(users),
        "pagesFetched": payload.get("pagesFetched"),
        "csv": str(csv_path),
        "json": str(json_path),
        "handles": str(handles_path),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
