---
type: raw_capture
source_type: pasted
title: "Sunder sync: 01-persistence-model.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/01-persistence-model.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/01-persistence-model.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/01-persistence-model.md"
sha256: "c8378b4c978d7834385b3ad0ac093eb86a0ec72b62c3f28b81435952d710a28c"
duplicate_of: ""
---

# Sunder sync: 01-persistence-model.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/01-persistence-model.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/01-persistence-model.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Persistence Model

This document normalizes how state persists in Tasklet-style agents.

## Core principle

Persistence is explicit, not learned.

If behavior is not encoded into artifacts, future runs will not reliably reproduce it.

## Persistence surfaces

1. Filesystem artifacts
- `/agent/home/`: scripts, configs, templates, outputs
- `/agent/subagents/`: reusable workflow instructions

2. SQL state
- schema + rows created through `run_agent_memory_sql`
- used for caches, logs, and cross-run state

3. System-managed objects
- triggers (when to invoke)
- connections (credential-backed tool access)

## Non-persistent by default

- conversation-level intent unless written down
- implicit setup rationale
- unwritten heuristics/preferences


