---
type: raw_capture
source_type: pasted
title: "Sunder sync: 02-what-gets-saved-and-where.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/02-what-gets-saved-and-where.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/02-what-gets-saved-and-where.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/first-run-lifecycle/02-what-gets-saved-and-where.md"
sha256: "229cb8e0c006342186d882cde98df733fb24b1c57bfef5e1f4e4f27972d9731e"
duplicate_of: ""
---

# Sunder sync: 02-what-gets-saved-and-where.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/02-what-gets-saved-and-where.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/02-what-gets-saved-and-where.md

Duplicate of existing source-map entry: `none`

## Capture Text

# What Gets Saved and Where

This document maps each persistence surface to storage owner, visibility, and lifetime.

## 1. Connection state

Examples:
- OAuth grant metadata
- Activated connection tools

Storage:
- System-managed connection store (not regular `/agent/home` files).

Agent visibility:
- Can list/use connection tools.
- Cannot read raw token secrets.

Lifetime:
- Persists until disconnected/revoked.

## 2. SQL state (`run_agent_memory_sql`)

Examples:
- Cache tables (`person_cache`)
- Execution logs (`briefing_log`)

Storage:
- Persistent agent SQL DB managed by platform.

Agent visibility:
- Full query/write via SQL tool.

Lifetime:
- Persists until rows/tables are deleted.

## 3. Subagent files (`/agent/subagents/`)

Examples:
- `calendar-briefing.md`
- `person-researcher.md`

Storage:
- Persistent filesystem under `/agent/subagents`.

Agent visibility:
- Read/write/delete via file tools.

Lifetime:
- Persists until edited/deleted.

## 4. Config files (`/agent/home/...`)

Examples:
- `briefing-preferences.json`

Storage:
- Persistent filesystem under `/agent/home`.

Agent visibility:
- Read/write via file tools.

Lifetime:
- Persists until edited/deleted.

## 5. Trigger definitions

Examples:
- Schedule trigger with cron/timezone

Storage:
- System-managed trigger registry.

Agent visibility:
- Can list/view/manage through trigger tools.

Lifetime:
- Persists until deleted/disabled.


