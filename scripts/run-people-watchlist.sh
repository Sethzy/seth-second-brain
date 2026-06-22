#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
CONFIG="$ROOT/config/people-watchlist.json"
OUT="$ROOT/raw/sweeps/last30days"

usage() {
  cat <<'EOF'
Usage: scripts/run-people-watchlist.sh [slug ...]

Runs Last30Days sweeps for people listed in config/people-watchlist.json.
Each run is saved under raw/sweeps/last30days/ and scaffolded into
staging/last30days/. These are noisy sweeps, not durable wiki promotion.

Examples:
  scripts/run-people-watchlist.sh
  scripts/run-people-watchlist.sh matt-pocock nicbstme
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ ! -f "$CONFIG" ]]; then
  echo "Missing $CONFIG" >&2
  exit 1
fi

mkdir -p "$OUT"

python3 - "$CONFIG" "$@" <<'PY' | while IFS=$'\t' read -r slug name handle topic search; do
import json
import sys

config_path = sys.argv[1]
selected = set(sys.argv[2:])
data = json.load(open(config_path))
default_search = data.get("defaults", {}).get("search", "x,youtube")

for person in data.get("people", []):
    slug = person["slug"]
    if selected and slug not in selected:
        continue
    print("\t".join([
        slug,
        person.get("name", slug),
        person.get("x_handle", "").lstrip("@"),
        person.get("topic") or person.get("name", slug),
        person.get("search") or default_search,
    ]))
PY
  if [[ -z "$slug" || -z "$handle" ]]; then
    echo "Skipping invalid watchlist entry: slug=$slug handle=$handle" >&2
    continue
  fi

  before_file="$(mktemp)"
  find "$OUT" -maxdepth 1 -type f -name "*.md" -print | sort > "$before_file"

  echo "Running people watchlist sweep: $name (@$handle)"
  "$ROOT/scripts/last30days-to-sweeps.sh" \
    --x-profile3 "$topic" \
    --search "$search" \
    --x-handle "$handle" \
    --save-suffix "$slug"

  after_file="$(mktemp)"
  find "$OUT" -maxdepth 1 -type f -name "*.md" -print | sort > "$after_file"

  comm -13 "$before_file" "$after_file" | while IFS= read -r raw_file; do
    [[ -n "$raw_file" ]] || continue
    "$ROOT/scripts/stage-last30days-digest.sh" "${raw_file#$ROOT/}"
  done

  rm -f "$before_file" "$after_file"
done
