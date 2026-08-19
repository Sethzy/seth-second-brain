#!/usr/bin/env bash
set -euo pipefail

if [[ $# -eq 0 || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  cat <<'EOF'
Usage: scripts/last30days-to-sweeps.sh "<topic>" [last30days flags...]

Runs an installed Last30Days engine and saves raw output into this repo's
raw/sweeps/last30days directory.

For X via the configured Chrome profile, use:
  scripts/last30days-to-sweeps.sh --x-profile3 "<topic>" --search x,web,youtube

Set LAST30DAYS_SCRIPTS_DIR if the skill is not installed in a standard location.
Set SECOND_BRAIN_X_CHROME_PROFILE to override the default Chrome profile.
EOF
  exit 0
fi

ROOT="$(git rev-parse --show-toplevel)"
OUT="$ROOT/raw/sweeps/last30days"
mkdir -p "$OUT"
if [[ -z "${LAST30DAYS_SCRIPTS_DIR:-}" ]]; then
  LAST30DAYS_SCRIPTS_DIR="$(python3 "$ROOT/scripts/last30days_runtime.py")"
fi
export LAST30DAYS_SCRIPTS_DIR
LAST30DAYS_MAIN="$LAST30DAYS_SCRIPTS_DIR/last30days.py"

if [[ "${1:-}" == "--x-profile3" ]]; then
  shift
  FROM_BROWSER=chrome \
  LAST30DAYS_CHROME_PROFILE="${SECOND_BRAIN_X_CHROME_PROFILE:-Profile 3}" \
  LAST30DAYS_MEMORY_DIR="$OUT" \
  python3 "$LAST30DAYS_MAIN" "$@" --save-dir "$OUT"
else
  LAST30DAYS_MEMORY_DIR="$OUT" python3 "$LAST30DAYS_MAIN" "$@" --save-dir "$OUT"
fi
