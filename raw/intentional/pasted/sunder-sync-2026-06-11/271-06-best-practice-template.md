---
type: raw_capture
source_type: pasted
title: "Sunder sync: 06-best-practice-template.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/06-best-practice-template.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/06-best-practice-template.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/06-best-practice-template.md"
sha256: "c09a9be564f8fd08e070b5aba71da9117d1a67027f431895e5228e779a138913"
duplicate_of: ""
---

# Sunder sync: 06-best-practice-template.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/06-best-practice-template.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/06-best-practice-template.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Best-Practice Template for Reliable Reruns

Use this pattern for recurring automations:

1. Trigger
- narrow and explicit name
- explicit schedule/timezone

2. Main subagent
- clear objective
- deterministic step sequence
- strict output schema

3. Config artifact
- `/agent/home/config/<workflow>.json`
- all tunable behavior externalized

4. SQL schema
- cache + execution log tables
- idempotency keys when relevant

5. Deterministic worker script (optional but preferred)
- place non-LLM transforms in script
- subagent acts as orchestrator + exception handler

## One-line guidance

If it must rerun predictably, encode it as artifacts plus deterministic code, not implicit model memory.


