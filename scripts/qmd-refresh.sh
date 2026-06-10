#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

scripts/init-qmd.sh

if [[ "${1:-}" == "--embed" ]]; then
  qmd embed --max-docs-per-batch 25
else
  echo "Skipping vector embeddings. Run scripts/qmd-refresh.sh --embed when you want vector search ready too."
fi
