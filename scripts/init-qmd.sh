#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

if ! command -v qmd >/dev/null 2>&1; then
  echo "qmd is not installed. Install with: npm install -g @tobilu/qmd" >&2
  exit 1
fi

ensure_collection() {
  local name="$1"
  local path="$2"
  if qmd collection list | grep -q "^$name "; then
    echo "collection exists: $name"
  else
    qmd collection add "$path"
  fi
}

ensure_context() {
  local name="$1"
  local summary="$2"
  if qmd context list | grep -q "^$name$"; then
    echo "context exists: $name"
  else
    qmd context add "qmd://$name/" "$summary"
  fi
}

ensure_collection "wiki" "wiki"
ensure_collection "intentional" "raw/intentional"
ensure_collection "sweeps" "raw/sweeps"
ensure_collection "staging" "staging"

ensure_context "wiki" "Compiled durable knowledge articles, index, log, and archived query answers for Seth Second Brain."
ensure_context "intentional" "Full immutable source snapshots intentionally saved by Seth, including exact X links, web articles, YouTube transcripts, papers, books, and pasted text."
ensure_context "sweeps" "Automated or semi-automated recent-signal research outputs, especially Last30Days raw runs. Treat as candidate intelligence, not durable knowledge."
ensure_context "staging" "Review queue for Last30Days digests, promotion candidates, proposed merges, proposed prunes, and other material waiting before wiki compilation."

qmd update
qmd status
