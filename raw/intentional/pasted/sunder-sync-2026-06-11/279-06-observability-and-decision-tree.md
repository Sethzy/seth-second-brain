---
type: raw_capture
source_type: pasted
title: "Sunder sync: 06-observability-and-decision-tree.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/06-observability-and-decision-tree.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/06-observability-and-decision-tree.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/06-observability-and-decision-tree.md"
sha256: "b3fc7d9578ec0d24744a83c5a11d9adae14ee6fd8b9e96c537e7b7a3a7868596"
duplicate_of: ""
---

# Sunder sync: 06-observability-and-decision-tree.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/06-observability-and-decision-tree.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/06-observability-and-decision-tree.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Observability and Decision Tree

## What to persist for debugging

- execution log per trigger run (success/error/duration)
- price history snapshots
- parse snippets when extraction fails
- failure counters and rate-limit timestamps

## What is not inherently replayable

- full internal reasoning path
- exact historical context window content

## Operational implication

Without explicit logs, postmortem analysis is shallow. Treat observability as part of core design, not optional extras.

## Decision tree summary

1. Validate request parameters.
2. Choose recurring architecture with explicit persistence.
3. Build schema and subagent.
4. Validate scrape once.
5. Register trigger.
6. On each run: scrape -> compare -> update -> notify conditionally.
7. Apply anti-spam and failure escalation rules.


