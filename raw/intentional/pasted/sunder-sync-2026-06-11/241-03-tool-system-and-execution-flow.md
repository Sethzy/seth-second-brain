---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-tool-system-and-execution-flow.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/03-tool-system-and-execution-flow.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/03-tool-system-and-execution-flow.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/03-tool-system-and-execution-flow.md"
sha256: "34f8a9eb6fb434e0f42d1fcea957085c458e1af1dffc9f327c92e0a0d34b126a"
duplicate_of: ""
---

# Sunder sync: 03-tool-system-and-execution-flow.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/03-tool-system-and-execution-flow.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/03-tool-system-and-execution-flow.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Tool System and Execution Flow

## Tool Classes

1. Built-in tools
- Always available (filesystem, command execution, DB/task/trigger/contact/UI primitives).

2. Connection tools
- Namespaced by connection ID prefix.
- Activated/deactivated per connection with user approval.
- Provided by integrations or MCP-backed services.

## Execution Pipeline

1. LLM emits a structured tool call intent.
2. Orchestration validates + executes in the proper runtime boundary.
3. Tool result is returned as structured output.
4. LLM continues reasoning with the returned state.

## Important Behavior

- Tools are the only mutation path for external state.
- Output size from tools directly impacts token cost and reliability.
- Tool design quality strongly influences determinism.

