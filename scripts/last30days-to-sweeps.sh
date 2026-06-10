#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: scripts/last30days-to-sweeps.sh "<topic>" [last30days flags...]

Runs the GTM-installed Last30Days engine and saves raw output into this repo's
raw/sweeps/last30days directory.

For X via Chrome Profile 3, use:
  scripts/last30days-to-sweeps.sh --x-profile3 "<topic>" --search x,web,youtube
EOF
  exit 0
fi

ROOT="$(git rev-parse --show-toplevel)"
OUT="$ROOT/raw/sweeps/last30days"
mkdir -p "$OUT"

if [[ "${1:-}" == "--x-profile3" ]]; then
  shift
  cd /Users/sethlim/Documents/gtm-workspace
  LAST30DAYS_MEMORY_DIR="$OUT" scripts/last30days-x-profile3.sh "$@"
else
  LAST30DAYS_MEMORY_DIR="$OUT" python3 /Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/last30days.py "$@"
fi
