---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-trigger-run-and-notification-logic.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/04-trigger-run-and-notification-logic.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/04-trigger-run-and-notification-logic.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/04-trigger-run-and-notification-logic.md"
sha256: "82c16a815f3721617eec39184d6f9f0f9c621c86c6687dce780ba9d0e713b1d1"
duplicate_of: ""
---

# Sunder sync: 04-trigger-run-and-notification-logic.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/04-trigger-run-and-notification-logic.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/04-trigger-run-and-notification-logic.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Trigger Run and Notification Logic

## Trigger model

Schedule trigger fires periodically (for example every 6 hours), starting a fresh model invocation.

## Runtime sequence

1. Load monitor record from SQL.
2. Invoke price-scraper subagent.
3. Evaluate threshold condition.
4. Update last price/check timestamps.
5. Send notification only when notification policy allows.

## Re-arm behavior

Typical anti-spam baseline:
- notify on first crossing below threshold
- suppress repeats while still below threshold
- re-arm when price moves back above threshold

## Recommended hardening

- atomic update guards (`WHERE notification_sent_at IS NULL` style)
- dedupe by last notified price/time window
- explicit cooldown interval support


