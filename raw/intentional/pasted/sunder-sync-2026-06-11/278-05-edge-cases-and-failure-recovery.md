---
type: raw_capture
source_type: pasted
title: "Sunder sync: 05-edge-cases-and-failure-recovery.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/05-edge-cases-and-failure-recovery.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/05-edge-cases-and-failure-recovery.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/05-edge-cases-and-failure-recovery.md"
sha256: "efcbda4d504bd20c8ee1b8211b1145ba0dc917c3721813e95e4d50b677a5f61d"
duplicate_of: ""
---

# Sunder sync: 05-edge-cases-and-failure-recovery.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/05-edge-cases-and-failure-recovery.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/05-edge-cases-and-failure-recovery.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Edge Cases and Failure Recovery

## Failure domains

1. Scrape failures
- parse drift after site redesign
- transient HTTP failures
- long-term page removal

2. State failures
- DB write failure after notification
- concurrent trigger overlap causing duplicate sends

3. Messaging failures
- notification dispatch fails or attachment constraints

## Recovery patterns

1. Failure counters + escalation thresholds
- notify user only after repeated consecutive failures

2. Idempotent operations
- guard duplicate inserts/sends
- use conditional updates and unique constraints

3. Graceful degradation
- keep core alerting alive when non-critical telemetry fails

4. Checkpointed setup
- schema -> monitor record -> subagent -> validation -> trigger
- resume from failed step instead of full reset


