---
type: raw_capture
source_type: pasted
title: "Sunder sync: 11-direct-tool-access-vs-nested-agent-runtime.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/11-direct-tool-access-vs-nested-agent-runtime.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/11-direct-tool-access-vs-nested-agent-runtime.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/11-direct-tool-access-vs-nested-agent-runtime.md"
sha256: "f39644ffa7b3f4349798b0e599052deea17b7b7b0faceedb5764463be332cdd3"
duplicate_of: ""
---

# Sunder sync: 11-direct-tool-access-vs-nested-agent-runtime.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/11-direct-tool-access-vs-nested-agent-runtime.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/11-direct-tool-access-vs-nested-agent-runtime.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Direct Tool Access vs Nested Agent Runtime

## Clarification

Tasklet's default model is:

- One active LLM context
- One flat tool list at that same level (for example `run_command`, `read_file`, `write_file`, web tools, and `run_subagent`)
- A sandbox used only as command execution infrastructure for `run_command`

Tasklet does **not** need to run a second Agent SDK instance inside the sandbox just to use filesystem or shell tools.

## Why This Matters

If you nest an inner agent runtime inside a sandbox, you create an avoidable communication boundary:

- Inner-agent output must be serialized back to outer-agent context
- Error handling gets split between sandbox errors and inner-agent errors
- Token usage/accounting becomes harder to reason about
- Context passing turns into prompt-within-prompt protocol work

With direct tools, the active agent just calls the needed tool immediately.

## Specialization Pattern

Use subagents for specialization, not for basic tool access:

1. Parent agent invokes `run_subagent` with specialist instructions + payload.
2. Platform spawns a fresh LLM instance with the same core tool surface (unless policy-restricted).
3. Subagent returns a final message string to the parent and exits.

This gives context isolation and reusable specialist behavior without nested runtime complexity.

## Practical Rule

- Default: direct tool access on the main agent.
- Optional: fresh subagent for specialist workflows.
- Avoid: agent-inside-sandbox nesting unless strict process isolation is an explicit requirement.

