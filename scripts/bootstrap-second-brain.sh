#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

usage() {
  cat <<'EOF'
Usage: scripts/bootstrap-second-brain.sh [--embed]

Checks the local toolchain, creates this clone's private QMD index, runs the
repository lint, and runs the maintenance unit tests. Pass --embed to also
download/use QMD's local models and build vector embeddings.
EOF
}

embed=0
case "${1:-}" in
  "") ;;
  --embed) embed=1 ;;
  -h|--help) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

missing=0
for command in git python3 node npm qmd; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Missing required command: $command" >&2
    missing=1
  fi
done

if [[ "$missing" -ne 0 ]]; then
  cat >&2 <<'EOF'

Install Git, Python 3.12+, and Node.js/npm first. Then install QMD with:
  npm install -g @tobilu/qmd
EOF
  exit 1
fi

python3 - <<'PY'
import sys

if sys.version_info < (3, 12):
    raise SystemExit("Python 3.12+ is required for the full capture toolchain.")
PY

if [[ "$embed" -eq 1 ]]; then
  scripts/qmd-refresh.sh --embed
else
  scripts/qmd-refresh.sh
fi

scripts/lint-second-brain.sh
python3 -m unittest discover -s tests -v

echo
echo "Second Brain is ready at: $ROOT"
echo "Open this folder in Codex or Obsidian. Start with wiki/index.md."
