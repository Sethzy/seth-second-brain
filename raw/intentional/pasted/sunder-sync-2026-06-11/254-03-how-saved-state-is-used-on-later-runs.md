---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-how-saved-state-is-used-on-later-runs.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/03-how-saved-state-is-used-on-later-runs.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/03-how-saved-state-is-used-on-later-runs.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/first-run-lifecycle/03-how-saved-state-is-used-on-later-runs.md"
sha256: "80592fae32e89615f7bd10b3db4bc00e3393e3a2296b1753acd9eac758caa20b"
duplicate_of: ""
---

# Sunder sync: 03-how-saved-state-is-used-on-later-runs.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/03-how-saved-state-is-used-on-later-runs.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/03-how-saved-state-is-used-on-later-runs.md

Duplicate of existing source-map entry: `none`

## Capture Text

# How Saved State Is Used on Later Runs

## Trigger-run input model

When the trigger fires on a future run, the model receives:

- The same base system prompt
- Current system reminder (connections, DB table counts, triggers, time)
- Trigger event payload

It does not receive prior conversation transcript by default.

## Rediscovery sequence

A typical run reconstructs intent by reading persisted artifacts:

1. Inspect `/agent/subagents/` to identify relevant workflow definitions.
2. Read primary subagent instructions to recover task semantics.
3. Read `/agent/home` config/preferences for user-specific parameters.
4. Query SQL state for cache/history/log information.
5. Execute workflow (often via `run_subagent`) and then write logs/results.

## Example usage pattern

- Parent trigger handler reads subagent/config.
- Parent runs main subagent with payload.
- Main subagent uses connection tools and SQL cache.
- Parent sends output and logs execution state.

## Key principle

Later runs rely on artifact discovery, not conversational memory recall.


