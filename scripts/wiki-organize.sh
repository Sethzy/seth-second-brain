#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

propose=0
limit=100
source_type="x"
extra=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --propose)
      propose=1
      shift
      ;;
    --limit)
      limit="${2:?--limit requires a value}"
      shift 2
      ;;
    --source-type)
      source_type="${2:?--source-type requires a value}"
      shift 2
      ;;
    --no-qmd|--stdout)
      extra+=("$1")
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ "$propose" -ne 1 ]]; then
  echo "Refusing to organize without --propose. This command only creates staging proposals." >&2
  exit 2
fi

cmd=(python3 scripts/wiki_maintenance.py organize --limit "$limit" --source-type "$source_type")
if [[ "${#extra[@]}" -gt 0 ]]; then
  cmd+=("${extra[@]}")
fi

"${cmd[@]}"
