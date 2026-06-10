#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

OUT_DIR="staging/maintenance"
mkdir -p "$OUT_DIR"
out="$OUT_DIR/$(date +%F)-maintenance-report.md"

wiki_count="$(find wiki -type f -name '*.md' ! -name 'index.md' ! -name 'log.md' | wc -l | tr -d ' ')"
raw_count="$(find raw -type f -name '*.md' | wc -l | tr -d ' ')"
staging_count="$(find staging -type f -name '*.md' | wc -l | tr -d ' ')"

{
  echo "---"
  echo "type: maintenance_report"
  echo "created_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "status: proposed"
  echo "---"
  echo
  echo "# Maintenance Report - $(date +%F)"
  echo
  echo "## Counts"
  echo
  echo "- Wiki articles: $wiki_count"
  echo "- Raw captures: $raw_count"
  echo "- Staging files: $staging_count"
  echo
  echo "## Lint"
  echo
  if scripts/lint-second-brain.sh >/tmp/seth-second-brain-lint.$$ 2>&1; then
    sed 's/^/- /' /tmp/seth-second-brain-lint.$$
  else
    sed 's/^/- /' /tmp/seth-second-brain-lint.$$
  fi
  rm -f /tmp/seth-second-brain-lint.$$
  echo
  echo "## Candidate Raw Captures Not In Source Map"
  echo
  python3 - <<'PY'
import json
from pathlib import Path

root = Path.cwd()
state = json.loads((root / "state/source-map.json").read_text())
known = {item.get("raw_path") for item in state.get("sources", [])}
missing = []
for path in sorted((root / "raw").rglob("*.md")):
    rel = path.relative_to(root).as_posix()
    if rel not in known:
        missing.append(rel)

if missing:
    for rel in missing:
        print(f"- {rel}")
else:
    print("- None")
PY
  echo
  echo "## Suggested Agent Review"
  echo
  echo
  echo "- Look for near-duplicate wiki pages."
  echo "- Look for source clusters that deserve a medium-length synthesis page."
  echo "- Look for stale claims whose raw sources are older than newer captures on the same topic."
  echo "- Keep raw files immutable; edit only wiki, staging, source map, and logs."
} > "$out"

echo "$out"
