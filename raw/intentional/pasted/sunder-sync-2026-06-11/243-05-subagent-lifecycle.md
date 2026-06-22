---
type: raw_capture
source_type: pasted
title: "Sunder sync: 05-subagent-lifecycle.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/05-subagent-lifecycle.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/05-subagent-lifecycle.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/05-subagent-lifecycle.md"
sha256: "f6ac30e0f7d96704528176a433153c66952fa9eff6b81efdbd3f53d572cd6be8"
duplicate_of: ""
---

# Sunder sync: 05-subagent-lifecycle.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/05-subagent-lifecycle.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/05-subagent-lifecycle.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Subagent Lifecycle

## Creation

Parent agent writes markdown instructions into `/agent/subagents/<name>.md`.

## Execution

1. Orchestrator spawns a new model instance.
2. Context includes system prompt + subagent markdown + optional payload.
3. Subagent executes with tool access.
4. Only final subagent message is returned to parent.
5. Subagent conversation context is discarded.

## Properties

- Same core runtime/tool surface as parent unless restricted by platform policy.
- No direct access to parent conversational chain-of-thought/context.
- Useful for context isolation and reusable operational modules.

## Why It Matters

Subagents are the main mechanism for composability and controlling context bloat in complex workflows.

