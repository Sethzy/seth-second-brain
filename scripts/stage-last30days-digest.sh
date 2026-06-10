#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

RAW="${1:?usage: scripts/stage-last30days-digest.sh raw/sweeps/last30days/<file>.md}"
if [[ ! -f "$RAW" ]]; then
  echo "No such raw Last30Days file: $RAW" >&2
  exit 1
fi

case "$RAW" in
  raw/sweeps/last30days/*) ;;
  *)
    echo "Expected a file under raw/sweeps/last30days/" >&2
    exit 1
    ;;
esac

base="$(basename "$RAW" .md)"
date="$(date +%F)"
out="staging/last30days/${date}-${base%-raw}-digest.md"
mkdir -p "$(dirname "$out")"

if [[ -e "$out" ]]; then
  echo "Digest already exists: $out" >&2
  exit 1
fi

title="$(sed -n '1s/^#\\{1,3\\}[[:space:]]*//p' "$RAW" | head -1)"
if [[ -z "$title" ]]; then
  title="$base"
fi

cat > "$out" <<EOF
# Last30Days Digest: ${title}

> Raw: ../../${RAW}
> Window: TODO
> Generated: ${date}
> Status: staged
> Compile Recommendation: TODO

## Strong Signals

- TODO

## Repeated Themes

- TODO

## Candidate Wiki Updates

- TODO

## Sources Worth Manual Capture

- TODO

## Cautions

- TODO
EOF

echo "$out"

