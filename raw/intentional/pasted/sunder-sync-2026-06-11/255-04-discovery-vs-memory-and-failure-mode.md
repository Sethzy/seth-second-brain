---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-discovery-vs-memory-and-failure-mode.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/04-discovery-vs-memory-and-failure-mode.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/04-discovery-vs-memory-and-failure-mode.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/first-run-lifecycle/04-discovery-vs-memory-and-failure-mode.md"
sha256: "ab8ddc2bc51836f1171ddad834c483db53e548dd73d5f31dd7b8bae15a4204f7"
duplicate_of: ""
---

# Sunder sync: 04-discovery-vs-memory-and-failure-mode.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/04-discovery-vs-memory-and-failure-mode.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/first-run-lifecycle/04-discovery-vs-memory-and-failure-mode.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Discovery vs Memory and Failure Mode

## Discovery vs memory

Persistent trigger workflows are reconstructed through artifacts.

What is not reliably present on future runs:
- Original setup chat
- Setup rationale details
- Implicit assumptions never written down

What must be present for reliable execution:
- Explicit subagent instructions
- Explicit config files
- Optional SQL state schema/logging
- Trigger metadata and connection availability

## Failure mode: underspecified subagent

If instructions are vague (for example, "do the briefing thing"), the future run must infer missing details from generic priors.

Likely outcomes:
- Inconsistent behavior across runs
- Wrong ordering of operations
- Incorrect output format/content

## Hard rule

Treat setup as writing an operational contract for a future stateless executor.


