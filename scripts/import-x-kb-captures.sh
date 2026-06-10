#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/import-x-kb-captures.sh [--dry-run] [source-dir]

Copies existing x-kb-capture markdown notes into raw/intentional/x without
overwriting anything. Default source-dir:
  ~/Documents/Knowledge/x-posts
EOF
}

dry_run=0
if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi
if [[ "${1:-}" == "--dry-run" ]]; then
  dry_run=1
  shift
fi

ROOT="$(git rev-parse --show-toplevel)"
SRC="${1:-$HOME/Documents/Knowledge/x-posts}"
DST="$ROOT/raw/intentional/x"
STATE="$ROOT/state/source-map.json"

if [[ ! -d "$SRC" ]]; then
  echo "Source directory does not exist: $SRC" >&2
  exit 1
fi

mkdir -p "$DST"

copied=0
skipped=0
while IFS= read -r -d '' file; do
  base="$(basename "$file")"
  target="$DST/$base"
  if [[ -e "$target" ]]; then
    echo "skip existing: $target"
    skipped=$((skipped + 1))
    continue
  fi

  if [[ "$dry_run" -eq 1 ]]; then
    echo "would copy: $file -> $target"
  else
    cp "$file" "$target"
    python3 - "$STATE" "$target" <<'PY'
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

state_path = Path(sys.argv[1])
raw_path = Path(sys.argv[2])
root = state_path.parents[1]
rel = raw_path.relative_to(root).as_posix()
text = raw_path.read_text(errors="replace")

def frontmatter_value(key):
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.M)
    if not match:
        return "Unknown"
    return match.group(1).strip().strip('"')

state = json.loads(state_path.read_text())
sources = state.setdefault("sources", [])
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

if not any(item.get("raw_path") == rel for item in sources):
    sources.append({
        "id": rel,
        "title": frontmatter_value("title"),
        "url": frontmatter_value("url"),
        "source_type": "x",
        "trust_lane": "intentional",
        "raw_path": rel,
        "status": "raw",
        "wiki_paths": [],
        "staging_paths": [],
        "created_at": now,
        "updated_at": now,
        "notes": "Imported from existing x-kb-capture library."
    })

state_path.write_text(json.dumps(state, indent=2) + "\n")
PY
    echo "copied: $target"
  fi
  copied=$((copied + 1))
done < <(find "$SRC" -maxdepth 1 -type f -name '*.md' -print0 | sort -z)

echo "done: $copied candidate(s), $skipped skipped"
