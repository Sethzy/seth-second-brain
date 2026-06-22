#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/new-raw-capture.sh [--quality complete|partial|failed] <source-type> "<title>" ["<url>"] < source.txt

Source types:
  x web youtube papers books pasted

Creates an immutable raw capture under raw/intentional/<source-type>/ only
when --quality complete is used. Partial/failed captures are staged under
staging/incomplete-captures/<source-type>/ and should not be compiled as raw
evidence.

The source body is read from stdin.
EOF
}

quality="complete"
if [[ "${1:-}" == "--quality" ]]; then
  quality="${2:-}"
  shift 2
fi

if [[ $# -lt 2 || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

lane="$1"
title="$2"
url="${3:-Unknown}"

case "$lane" in
  x|web|youtube|papers|books|pasted) ;;
  *)
    echo "Unsupported source type: $lane" >&2
    usage >&2
    exit 1
    ;;
esac

case "$quality" in
  complete|partial|failed) ;;
  *)
    echo "Unsupported quality: $quality" >&2
    usage >&2
    exit 1
    ;;
esac

ROOT="$(git rev-parse --show-toplevel)"
if [[ "$quality" == "complete" ]]; then
  OUT_DIR="$ROOT/raw/intentional/$lane"
  trust_lane="intentional"
  status="raw"
  rel_prefix="raw/intentional"
else
  OUT_DIR="$ROOT/staging/incomplete-captures/$lane"
  trust_lane="incomplete"
  status="$quality"
  rel_prefix="staging/incomplete-captures"
fi
mkdir -p "$OUT_DIR"

body="$(cat)"
if [[ -z "${body//[[:space:]]/}" ]]; then
  echo "No source body provided on stdin." >&2
  exit 1
fi

slug="$(printf '%s' "$title" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//' \
  | cut -c 1-60)"
if [[ -z "$slug" ]]; then
  slug="capture"
fi

date="$(date +%F)"
target="$OUT_DIR/$date-$slug.md"
n=2
while [[ -e "$target" ]]; do
  target="$OUT_DIR/$date-$slug-$n.md"
  n=$((n + 1))
done

{
cat <<EOF
---
type: $([[ "$quality" == "complete" ]] && echo "raw_capture" || echo "incomplete_capture")
source_type: $lane
title: "$title"
url: "$url"
collected_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
published_at: Unknown
capture_quality: $quality
status: $status
trust_lane: $trust_lane
---

# $title

Source: $url

## Capture Text

EOF
printf '%s\n' "$body"
} > "$target"

python3 - "$ROOT/state/source-map.json" "$target" "$url" "$lane" "$title" "$quality" "$trust_lane" <<'PY'
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

state_path = Path(sys.argv[1])
raw_path = Path(sys.argv[2])
url = sys.argv[3]
lane = sys.argv[4]
title = sys.argv[5]
quality = sys.argv[6]
trust_lane = sys.argv[7]
root = state_path.parents[1]

state = json.loads(state_path.read_text())
sources = state.setdefault("sources", [])
rel = raw_path.relative_to(root).as_posix()
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

if not any(item.get("raw_path") == rel for item in sources):
    is_raw = quality == "complete"
    sources.append({
        "id": rel,
        "title": title,
        "url": url,
        "source_type": lane,
        "trust_lane": trust_lane,
        "capture_quality": quality,
        "raw_path": rel if is_raw else None,
        "staging_path": None if is_raw else rel,
        "status": "raw" if is_raw else quality,
        "wiki_paths": [],
        "staging_paths": [] if is_raw else [rel],
        "created_at": now,
        "updated_at": now,
        "notes": "Created by scripts/new-raw-capture.sh"
    })

state_path.write_text(json.dumps(state, indent=2) + "\n")
PY

echo "$target"
