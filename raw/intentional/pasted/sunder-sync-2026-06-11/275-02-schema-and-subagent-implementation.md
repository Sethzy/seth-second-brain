---
type: raw_capture
source_type: pasted
title: "Sunder sync: 02-schema-and-subagent-implementation.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/02-schema-and-subagent-implementation.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/02-schema-and-subagent-implementation.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/02-schema-and-subagent-implementation.md"
sha256: "22082923a91365ee0069e87bb4167be6f084dada3df70ffde2de134b9861b1fc"
duplicate_of: ""
---

# Sunder sync: 02-schema-and-subagent-implementation.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/02-schema-and-subagent-implementation.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/02-schema-and-subagent-implementation.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Schema and Subagent Implementation

## Base schema

Primary monitor table fields:
- URL
- target price
- last observed price
- last check timestamp
- notification sent timestamp

Optional support tables:
- price history
- execution log

## Idempotent setup posture

- `CREATE TABLE IF NOT EXISTS`
- avoid duplicate inserts by using unique constraints and upserts where possible

## Subagent contract

Subagent responsibilities:
1. scrape page
2. extract price candidate(s)
3. compare against stored state
4. return structured JSON result

Parent responsibilities:
- trigger scheduling
- decision to notify
- notification dispatch
- persistent state updates

## Subagent output contract

Use strict structured result (success, current/previous price, price_changed, error) to avoid brittle text parsing in parent.


