---
type: raw_capture
source_type: pasted
title: "Sunder sync: 01-system-architecture-overview.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/linkedin-automation/01-system-architecture-overview.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/linkedin-automation/01-system-architecture-overview.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/linkedin-automation/01-system-architecture-overview.md"
sha256: "aebaa628196dab57490c1cfb6a29425be8d6758ebd1ef785dd6d55d70a37994c"
duplicate_of: ""
---

# Sunder sync: 01-system-architecture-overview.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/linkedin-automation/01-system-architecture-overview.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/linkedin-automation/01-system-architecture-overview.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Tasklet LinkedIn Automation - System Architecture Overview

This document normalizes the reverse-engineered architecture for Tasklet-style LinkedIn browser automation.

## High-Level Flow

```text
Schedule Trigger
  -> Agent Orchestrator
  -> Computer Use Connection
  -> Remote VM + Browser Runtime
  -> LinkedIn Web UI
```

## Core Components

1. Schedule Trigger
- Starts an agent run using cron-like timing.
- Provides run context payload (trigger metadata + task intent).

2. Agent Orchestrator
- Receives trigger payload.
- Decides whether to initialize or reuse a browser control connection.
- Runs perception-action loops using screenshot-driven state detection.

3. Computer Use Connection
- Exposes browser-control primitives (for example: navigate, screenshot, click, type, scroll).
- Bridges tool calls to a remote execution environment.

4. Remote Runtime (VM/Container)
- Hosts browser process and input injection service.
- Isolates execution from user local machine.
- Can be ephemeral per run or semi-persistent across runs.

5. Target Surface (LinkedIn)
- UI-only interaction surface.
- State is inferred from pixels/OCR-like extraction, not DOM APIs.

## Data/Control Boundaries

- Trigger-to-agent: structured event payload.
- Agent-to-runtime: tool command RPC.
- Runtime-to-agent: screenshots and execution confirmations.
- Agent decision loop: deterministic policy + optional random delay functions.

## Operational Characteristic

The architecture is vision-first UI automation, not API automation.


