---
type: raw_capture
source_type: pasted
title: "Sunder sync: 01-core-runtime-model.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/01-core-runtime-model.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/01-core-runtime-model.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/01-core-runtime-model.md"
sha256: "67edf6a46c647c4e8b19750a71402b57ea97727745c0eae6ee29ed70b4d4fbec"
duplicate_of: ""
---

# Sunder sync: 01-core-runtime-model.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/01-core-runtime-model.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/01-core-runtime-model.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Core Runtime Model

## Layer 1: Orchestration Layer (Backend)

Responsibilities:
- Account, quota, billing management
- Connection registry and credential lifecycle management
- Trigger registration and event routing
- Tool-call execution and result marshalling

## Layer 2: LLM Instance (Per Invocation)

Properties:
- Stateless by default across runs
- Receives system prompt and invocation context
- No direct raw access to external secrets
- Operates through tool interfaces, not direct privileged channels

## Layer 3: Sandbox Runtime

Execution capabilities:
- Shell command execution via `run_command`
- Script execution (for example Python workflows)
- Ephemeral compute + persistent mounted storage zones

Sandbox activation rule:
- Sandbox execution is on-demand for `run_command`.
- Tool calls like `read_file`, `write_file`, SQL tools, and web tools do not require shell execution.
- In practice: shell/Python/`curl`/`apk` work happens in sandbox; non-shell tool calls do not.

Filesystem profile:
- Persistent: `/agent/home/`, `/agent/subagents/`
- Read-only inputs/instructions: `/agent/uploads/`, `/agent/skills/`, `/agent/toolcalls/`
- Ephemeral: `/tmp/`

## Runtime Model Summary

Tasklet behaves as orchestrated tool-use over a stateless model runtime, with persistence externalized into files, task state, triggers, and connections.

