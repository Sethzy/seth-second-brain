---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-trigger-timing-and-cron-strategy.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/04-trigger-timing-and-cron-strategy.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/04-trigger-timing-and-cron-strategy.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/04-trigger-timing-and-cron-strategy.md"
sha256: "99c56bc9b1a22f96d0851b23787e1f360de61498f5e3b0756b259e9c9231fe24"
duplicate_of: ""
---

# Sunder sync: 04-trigger-timing-and-cron-strategy.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/04-trigger-timing-and-cron-strategy.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/04-trigger-timing-and-cron-strategy.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Trigger Timing and Cron Strategy

## Timing constraint

Target behavior: briefing arrives roughly before first meeting.

## Main design options

1. Fixed early trigger + in-run delay
- limited practicality in one-shot run models

2. Fixed trigger + immediate send with first-meeting context
- simple and reliable
- does not guarantee exact minus-30-minute delivery

3. Multi-trigger probing window
- closer timing accuracy
- higher complexity and idempotency requirements

## Chosen tradeoff in source

Fixed weekday morning trigger with immediate send and explicit first-meeting timestamp in subject/body.

## Timezone concerns

- UTC cron conversion must be explicit.
- DST-observing zones can shift local delivery hour.
- travel/timezone changes can make "morning" semantics drift.

## Guardrail

Document timezone assumptions and provide adjustment instructions for users who travel or change locale.


