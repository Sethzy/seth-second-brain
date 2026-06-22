---
type: raw_capture
source_type: pasted
title: "Sunder sync: 06-edge-case-and-partial-failure-policy.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/06-edge-case-and-partial-failure-policy.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/06-edge-case-and-partial-failure-policy.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/06-edge-case-and-partial-failure-policy.md"
sha256: "d3925f4636eb04d9dd69b291b1e6c8cb55babb3dd7d819554076ec75f029ce3e"
duplicate_of: ""
---

# Sunder sync: 06-edge-case-and-partial-failure-policy.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/06-edge-case-and-partial-failure-policy.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/06-edge-case-and-partial-failure-policy.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Edge Case and Partial-Failure Policy

## Edge case domains

1. Calendar anomalies
- all-day/private/tentative events
- very large attendee lists
- multi-calendar aggregation

2. Research anomalies
- ambiguous identities
- sparse/no public presence
- stale or conflicting sources
- non-company email domains

3. Timing anomalies
- early first meetings
- long processing windows
- DST and travel timezone drift

## Partial-failure contract

User-facing output should remain useful even when some enrichments fail.

Policy:
- include all relevant attendees
- attach confidence and missing-data notes
- do not block briefing on single-person research failure
- persist failure reasons for later debugging

## Success semantics

`partial` is a valid terminal status when core delivery succeeded but enrichment completeness is below target.


