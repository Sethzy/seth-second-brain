#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

LOCK_DIR="$ROOT/.tmp/x-backfill-checkpoint.lock"
LIMIT="${X_BACKFILL_LIMIT:-120}"

mkdir -p "$ROOT/.tmp"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "Another X backfill checkpoint is already running; exiting."
  exit 0
fi
trap 'rmdir "$LOCK_DIR"' EXIT

echo "== X backfill checkpoint =="
date
echo ""

set +e
scripts/capture-missing-x-links.sh \
  --no-refresh \
  --limit "$LIMIT" \
  --rate-limit-sleep 0 \
  --max-rate-limit-sleeps 0
capture_status=$?
set -e

echo ""
echo "== Audit after capture attempt =="
set +e
scripts/capture-missing-x-links.sh --audit-only
audit_status=$?
set -e

echo ""
echo "== Refresh QMD =="
scripts/qmd-refresh.sh --embed

echo ""
echo "== QMD status =="
qmd status

echo ""
echo "Capture exit status: $capture_status"
echo "Audit exit status: $audit_status"

if [ "$audit_status" -eq 0 ]; then
  exit 0
fi

# A nonzero capture status is expected when the limited batch leaves unresolved
# IDs or when X rate-limits the current run. The audit result is the durable
# completion signal, so keep scheduled runs healthy until the audit reaches zero.
exit 0
