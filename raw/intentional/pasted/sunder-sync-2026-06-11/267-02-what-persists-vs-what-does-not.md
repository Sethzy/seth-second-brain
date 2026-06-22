---
type: raw_capture
source_type: pasted
title: "Sunder sync: 02-what-persists-vs-what-does-not.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/02-what-persists-vs-what-does-not.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/02-what-persists-vs-what-does-not.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/02-what-persists-vs-what-does-not.md"
sha256: "6db3ff900c7ac76fbac4fc3d8b424c489e02e8189e94a5d5849bebcbac7b6b33"
duplicate_of: ""
---

# Sunder sync: 02-what-persists-vs-what-does-not.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/02-what-persists-vs-what-does-not.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/02-what-persists-vs-what-does-not.md

Duplicate of existing source-map entry: `none`

## Capture Text

# What Persists vs What Does Not

## Persists

- Trigger definitions and schedules
- Connection registrations and activated tools
- Files under `/agent/home` and `/agent/subagents`
- SQL tables and data

## Does not persist reliably

- The model's prior run conversational context
- Setup-time reasoning unless encoded into files/DB
- Unwritten preferences and decision rules

## Operational consequence

Rerun reliability depends on artifact quality, not on model memory.


