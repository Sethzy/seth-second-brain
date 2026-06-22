#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

exec python3 "$ROOT/scripts/capture-missing-x-links.py" "$@"
