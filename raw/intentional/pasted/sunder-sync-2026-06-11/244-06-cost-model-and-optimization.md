---
type: raw_capture
source_type: pasted
title: "Sunder sync: 06-cost-model-and-optimization.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/06-cost-model-and-optimization.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/06-cost-model-and-optimization.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/06-cost-model-and-optimization.md"
sha256: "1aa224ec0c0398117fa54ced570fc15386ce96ddac811731714798e409ecfe7e"
duplicate_of: ""
---

# Sunder sync: 06-cost-model-and-optimization.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/06-cost-model-and-optimization.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/06-cost-model-and-optimization.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Cost Model and Optimization

## Primary Cost Structure

Each invocation incurs token cost from:
- Input context (system prompt + history + tool outputs)
- Output tokens (responses and tool-call scaffolding)

## Major Cost Drivers

- Large raw tool outputs
- Long interactive sessions
- Repeated subagent calls
- Verbose intermediate reasoning/formatting

## Optimization Patterns

1. Deterministic scripts for heavy data processing
- Let runtime scripts do compute-intensive transformation.
- Return compact summaries to LLM context.

2. Subagent isolation
- Push bulky tasks into subagents.
- Return only final distilled outputs to parent.

3. Query minimization
- Request only required fields and bounded ranges.
- Avoid dumping large payloads into context.

## Practical Note

Cost optimization is usually emergent from architecture and prompting discipline, not guaranteed by default behavior.

