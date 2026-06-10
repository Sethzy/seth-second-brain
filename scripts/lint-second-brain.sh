#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

missing=0

require_path() {
  if [[ ! -e "$1" ]]; then
    echo "MISSING: $1"
    missing=1
  fi
}

require_path README.md
require_path AGENTS.md
require_path docs/architecture.md
require_path docs/workflows.md
require_path wiki/index.md
require_path wiki/log.md
require_path templates/raw-capture-template.md
require_path templates/x-capture-template.md
require_path templates/wiki-article-template.md
require_path templates/last30days-digest-template.md
require_path templates/archive-template.md
require_path templates/maintenance-proposal-template.md
require_path config/qmd-index.example.yml
require_path state/source-map.json
require_path scripts/x-capture-to-raw.sh
require_path scripts/new-raw-capture.sh
require_path scripts/import-x-kb-captures.sh
require_path scripts/init-qmd.sh
require_path scripts/qmd-refresh.sh
require_path scripts/maintenance-report.sh
require_path scripts/stage-last30days-digest.sh
require_path .agents/skills/karpathy-llm-wiki/SKILL.md
require_path .agents/skills/seth-second-brain/SKILL.md
require_path .agents/skills/qmd/SKILL.md
require_path skills-lock.json

for dir in \
  raw/intentional/x \
  raw/intentional/web \
  raw/intentional/youtube \
  raw/intentional/papers \
  raw/intentional/books \
  raw/intentional/pasted \
  raw/sweeps/last30days \
  staging/last30days \
  staging/incomplete-captures \
  staging/maintenance \
  state \
  wiki \
  wiki/archive \
  outputs
do
  require_path "$dir"
done

python3 - <<'PY'
from pathlib import Path
import re
import sys
import json

root = Path.cwd()
errors = []
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    if ".agents" in path.parts:
        continue
    if "templates" in path.parts:
        continue
    text = path.read_text(errors="replace")
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        if not target or "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(root)}: broken link -> {target}")

if errors:
    print("Broken markdown links:")
    for error in errors:
        print(f"  {error}")
    sys.exit(1)

state_path = root / "state" / "source-map.json"
try:
    state = json.loads(state_path.read_text())
except Exception as exc:
    print(f"Invalid JSON in {state_path.relative_to(root)}: {exc}")
    sys.exit(1)

if not isinstance(state, dict) or not isinstance(state.get("sources"), list):
    print("state/source-map.json must be an object with a sources list.")
    sys.exit(1)

for raw_path in sorted((root / "raw").rglob("*.md")):
    text = raw_path.read_text(errors="replace")
    if "capture_quality: complete" not in text:
        errors.append(f"{raw_path.relative_to(root)}: raw files must declare capture_quality: complete")

for item in state.get("sources", []):
    quality = item.get("capture_quality")
    raw_path = item.get("raw_path")
    staging_path = item.get("staging_path")
    if quality == "complete" and not raw_path:
        errors.append(f"state/source-map.json: complete source missing raw_path -> {item.get('id')}")
    if quality in {"partial", "failed"} and raw_path:
        errors.append(f"state/source-map.json: incomplete source must not have raw_path -> {item.get('id')}")
    if quality in {"partial", "failed"} and not staging_path:
        errors.append(f"state/source-map.json: incomplete source missing staging_path -> {item.get('id')}")

if errors:
    print("Second brain lint errors:")
    for error in errors:
        print(f"  {error}")
    sys.exit(1)
PY

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "Second brain lint passed."
