#!/usr/bin/env python3
"""Audit and capture X/Twitter status URLs referenced in the Markdown corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://(?:www\.)?(?:x|twitter)\.com/([A-Za-z0-9_]+)/status/(\d+)(?:[^\s)\]>]*)?", re.I)
STATUS_ID_RE = re.compile(r"status_id:\s*(\d+)")
FILENAME_STATUS_RE = re.compile(r"^(\d+)-")
AUTH_FAILURE_PATTERNS = (
    "Could not extract X auth cookies",
    "AUTH_TOKEN",
    "CT0",
)
RATE_LIMIT_PATTERNS = (
    "rate limit",
    "Too Many Requests",
    "429",
)


@dataclass
class StatusRef:
    status_id: str
    handle: str
    url: str
    locations: list[str] = field(default_factory=list)


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def now_local() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:90] or fallback).strip("-")


def markdown_files(include_sweeps: bool) -> list[Path]:
    roots = [ROOT / "wiki", ROOT / "raw" / "intentional", ROOT / "staging"]
    if include_sweeps:
        roots.append(ROOT / "raw" / "sweeps")
    out: list[Path] = []
    for root in roots:
        if root.exists():
            out.extend(path for path in root.rglob("*.md") if ".qmd" not in path.parts and ".git" not in path.parts)
    return sorted(out)


def discover_status_refs(include_sweeps: bool) -> dict[str, StatusRef]:
    refs: dict[str, StatusRef] = {}
    for path in markdown_files(include_sweeps):
        rel = path.relative_to(ROOT).as_posix()
        try:
            lines = path.read_text(errors="replace").splitlines()
        except OSError:
            continue
        for lineno, line in enumerate(lines, 1):
            for match in URL_RE.finditer(line):
                handle, status_id = match.groups()
                url = f"https://x.com/{handle}/status/{status_id}"
                ref = refs.setdefault(status_id, StatusRef(status_id=status_id, handle=handle, url=url))
                ref.locations.append(f"{rel}:{lineno}")
    return refs


def known_capture_ids() -> dict[str, list[str]]:
    known: dict[str, list[str]] = {}
    for folder in (ROOT / "raw" / "intentional" / "x", ROOT / "staging" / "incomplete-captures" / "x"):
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            filename_match = FILENAME_STATUS_RE.match(path.name)
            if filename_match:
                known.setdefault(filename_match.group(1), []).append(rel)
            try:
                head = path.read_text(errors="replace")[:1500]
            except OSError:
                continue
            status_match = STATUS_ID_RE.search(head)
            if status_match:
                known.setdefault(status_match.group(1), []).append(rel)
    return known


def audit(include_sweeps: bool) -> tuple[dict[str, StatusRef], dict[str, list[str]], list[StatusRef]]:
    refs = discover_status_refs(include_sweeps)
    known = known_capture_ids()
    missing = [ref for status_id, ref in sorted(refs.items()) if status_id not in known]
    return refs, known, missing


def print_audit(include_sweeps: bool) -> int:
    refs, known, missing = audit(include_sweeps)
    print(f"X status URLs discovered: {len(refs)}")
    print(f"X status IDs with capture records: {sum(1 for status_id in refs if status_id in known)}")
    print(f"Unresolved X status IDs: {len(missing)}")
    if missing:
        print("")
        print("Unresolved sample:")
        for ref in missing[:50]:
            first = ref.locations[0] if ref.locations else "unknown"
            print(f"- {ref.status_id} {ref.url} ({first})")
    return 1 if missing else 0


def render_failed_capture(ref: StatusRef, error: str) -> str:
    locations = "\n".join(f"- `{location}`" for location in ref.locations[:25])
    if len(ref.locations) > 25:
        locations += f"\n- ... {len(ref.locations) - 25} more location(s)"
    return f"""---
type: incomplete_capture
source_type: x
url: https://x.com/{ref.handle}/status/{ref.status_id}
original_url: {ref.url}
author: "Unknown"
handle: {ref.handle}
status_id: {ref.status_id}
captured_at: {now_local()}
published_at: "Unknown"
capture_quality: failed
status: failed
trust_lane: incomplete
---

# Failed X capture for @{ref.handle}

## Source

- Original: [{ref.url}]({ref.url})
- Canonical: [https://x.com/{ref.handle}/status/{ref.status_id}](https://x.com/{ref.handle}/status/{ref.status_id})

## Capture Failure

The authenticated X capture path could not retrieve this status during the batch capture run.

```text
{error.strip() or "Unknown capture error."}
```

## Referenced From

{locations or "- Unknown"}
"""


def update_source_map_for_failed(path: Path, ref: StatusRef, error: str) -> None:
    state_path = ROOT / "state" / "source-map.json"
    state = json.loads(state_path.read_text())
    sources = state.setdefault("sources", [])
    rel = path.relative_to(ROOT).as_posix()
    now = now_iso()
    existing = next(
        (
            item
            for item in sources
            if item.get("id") == rel
            or item.get("url") == f"https://x.com/{ref.handle}/status/{ref.status_id}"
            or item.get("url") == ref.url
        ),
        None,
    )
    payload = {
        "id": rel,
        "title": f"Failed X capture @{ref.handle} {ref.status_id}",
        "url": f"https://x.com/{ref.handle}/status/{ref.status_id}",
        "source_type": "x",
        "trust_lane": "incomplete",
        "capture_quality": "failed",
        "raw_path": None,
        "staging_path": rel,
        "status": "failed",
        "wiki_paths": [],
        "staging_paths": [rel],
        "created_at": existing.get("created_at", now) if existing else now,
        "updated_at": now,
        "notes": f"Batch capture failed through authenticated X path: {(error.strip() or 'unknown error')[:500]}",
    }
    if existing:
        existing.clear()
        existing.update(payload)
    else:
        sources.append(payload)
    state["updated_at"] = now
    state_path.write_text(json.dumps(state, indent=2) + "\n")


def write_failed_capture(ref: StatusRef, error: str) -> Path:
    staging_dir = ROOT / "staging" / "incomplete-captures" / "x"
    staging_dir.mkdir(parents=True, exist_ok=True)
    path = staging_dir / f"{ref.status_id}-{slugify(ref.handle, 'x')}-failed.md"
    if not path.exists():
        path.write_text(render_failed_capture(ref, error))
    update_source_map_for_failed(path, ref, error)
    return path


def run_capture(ref: StatusRef) -> tuple[bool, str]:
    command = [str(ROOT / "scripts" / "x-capture-to-raw.sh"), ref.url]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=90)
    output = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part)
    return result.returncode == 0, output


def is_rate_limit(output: str) -> bool:
    return any(pattern.lower() in output.lower() for pattern in RATE_LIMIT_PATTERNS)


def is_auth_failure(output: str) -> bool:
    return any(pattern.lower() in output.lower() for pattern in AUTH_FAILURE_PATTERNS)


def capture_missing(
    include_sweeps: bool,
    limit: int | None,
    refresh: bool,
    write_failures: bool,
    rate_limit_sleep: int,
    max_rate_limit_sleeps: int,
) -> int:
    refs, known, missing = audit(include_sweeps)
    if limit is not None:
        missing = missing[:limit]
    print(f"Discovered {len(refs)} X status IDs; {len(missing)} unresolved ID(s) selected for capture.", flush=True)
    if not missing:
        return 0

    completed = 0
    failed = 0
    rate_limit_sleeps = 0
    for index, ref in enumerate(missing, 1):
        while True:
            print(f"[{index}/{len(missing)}] {ref.url}", flush=True)
            ok, output = run_capture(ref)
            if ok:
                completed += 1
                print(output, flush=True)
                break
            if is_rate_limit(output) and rate_limit_sleep > 0 and rate_limit_sleeps < max_rate_limit_sleeps:
                rate_limit_sleeps += 1
                print(
                    f"Rate limited by X; sleeping {rate_limit_sleep}s before retry "
                    f"({rate_limit_sleeps}/{max_rate_limit_sleeps}).",
                    flush=True,
                )
                time.sleep(rate_limit_sleep)
                continue
            break
        if ok:
            continue
        if is_auth_failure(output) or is_rate_limit(output):
            print("Capture path appears globally blocked; stopping without converting the rest to failed records.", file=sys.stderr)
            print(output, file=sys.stderr)
            return 2
        failed += 1
        if write_failures:
            failed_path = write_failed_capture(ref, output)
            print(f"failed -> {failed_path.relative_to(ROOT)}", flush=True)
        else:
            print(output, file=sys.stderr)

    _, _, remaining = audit(include_sweeps)
    print("", flush=True)
    print(f"Capture pass complete: {completed} complete/partial via capture script, {failed} failed staging record(s).", flush=True)
    print(f"Rate-limit sleeps: {rate_limit_sleeps}", flush=True)
    print(f"Remaining unresolved X status IDs: {len(remaining)}", flush=True)
    if refresh:
        print("")
        subprocess.run([str(ROOT / "scripts" / "qmd-refresh.sh"), "--embed"], cwd=ROOT, check=True)
    return 1 if remaining else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture or audit missing X/Twitter status captures.")
    parser.add_argument("--audit-only", action="store_true", help="Only report unresolved X status IDs.")
    parser.add_argument("--include-sweeps", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--limit", type=int, default=None, help="Capture at most N unresolved IDs.")
    parser.add_argument("--no-refresh", action="store_true", help="Skip QMD refresh after capture.")
    parser.add_argument("--no-write-failures", action="store_true", help="Do not create failed staging records for per-post failures.")
    parser.add_argument("--rate-limit-sleep", type=int, default=0, help="Seconds to sleep and retry when X returns 429.")
    parser.add_argument("--max-rate-limit-sleeps", type=int, default=10, help="Maximum number of 429 sleep/retry cycles.")
    args = parser.parse_args()

    if args.audit_only:
        return print_audit(args.include_sweeps)
    return capture_missing(
        include_sweeps=args.include_sweeps,
        limit=args.limit,
        refresh=not args.no_refresh,
        write_failures=not args.no_write_failures,
        rate_limit_sleep=args.rate_limit_sleep,
        max_rate_limit_sleeps=args.max_rate_limit_sleeps,
    )


if __name__ == "__main__":
    raise SystemExit(main())
