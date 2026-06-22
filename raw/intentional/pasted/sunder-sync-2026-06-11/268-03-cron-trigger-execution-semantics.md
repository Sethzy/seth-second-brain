---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-cron-trigger-execution-semantics.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/03-cron-trigger-execution-semantics.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/03-cron-trigger-execution-semantics.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/03-cron-trigger-execution-semantics.md"
sha256: "fd84dd3d4a1f18afb000265b1f2e10335489850f9019f9af41d244689f5e1062"
duplicate_of: ""
---

# Sunder sync: 03-cron-trigger-execution-semantics.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/03-cron-trigger-execution-semantics.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/03-cron-trigger-execution-semantics.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Cron Trigger Execution Semantics

## Common misconception

Cron does not directly execute a deterministic workflow file.

## Actual model

When schedule fires:
1. System starts a fresh model invocation.
2. Invocation context includes:
- base system prompt
- runtime reminder/state summary
- trigger payload
3. Model decides what actions/tools to invoke.

## Implication

Execution is model-mediated each time. Consistency is guided by artifacts and naming conventions, not hard workflow-engine determinism.


