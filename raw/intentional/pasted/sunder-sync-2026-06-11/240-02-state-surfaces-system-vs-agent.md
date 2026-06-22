---
type: raw_capture
source_type: pasted
title: "Sunder sync: 02-state-surfaces-system-vs-agent.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/02-state-surfaces-system-vs-agent.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/02-state-surfaces-system-vs-agent.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/02-state-surfaces-system-vs-agent.md"
sha256: "b462beed707fcbbada7b18776a6c22b6d885e61fc7a712cc39d46d8dfd046bbb"
duplicate_of: ""
---

# Sunder sync: 02-state-surfaces-system-vs-agent.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/02-state-surfaces-system-vs-agent.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/02-state-surfaces-system-vs-agent.md

Duplicate of existing source-map entry: `none`

## Capture Text

# State Surfaces: System-Managed vs Agent-Managed

## System-Managed (Opaque)

1. Connections
- Holds OAuth/API credentials and connection metadata.
- Agent can discover/use connection tools but does not read raw secrets.

2. Triggers
- Stores schedule/webhook/event subscriptions.
- Agent can create/delete trigger instances through tool APIs.

3. Contact Methods
- Stores verified outbound message destinations (email/text).
- Controlled through explicit add/list tools.

## Agent-Managed (Transparent)

1. Filesystem (`/agent/home/`)
- Durable storage for scripts, configs, outputs, datasets.
- Fully mutable by agent via file tools.

2. Subagents (`/agent/subagents/`)
- Markdown-defined reusable workflows.
- Created/edited by parent agent and executed via `run_subagent`.

3. Task List
- In-memory visible task state for progress management.
- Managed through `manage_tasks`/`list_tasks`.

## Practical Boundary

Reliable automation depends on storing intent and operational state in agent-managed artifacts that future invocations can rediscover.

