---
type: raw_capture
source_type: pasted
title: "Sunder sync: 10-summary-mental-model.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/10-summary-mental-model.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/10-summary-mental-model.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/10-summary-mental-model.md"
sha256: "892f7e128fadab2c53d1b89f83c379ec7d754dfb6b39f09e6d0dd187075d14fa"
duplicate_of: ""
---

# Sunder sync: 10-summary-mental-model.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/10-summary-mental-model.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/10-summary-mental-model.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Summary Mental Model

Tasklet can be modeled as:

`Stateless LLM + Persistence Layer + Tool Bridge`

## Implications

1. Fresh-run amnesia is normal.
- Every trigger run starts with limited immediate memory.

2. Intent must be rediscoverable.
- Durable artifacts (subagents/config/state) are mandatory for reliability.

3. Quality of artifacts drives outcomes.
- Better instructions + explicit state -> higher determinism.

4. Cost scales with model usage and context size.
- Architecture choices directly shape token spend.

## One-Line Operating Principle

Engineer for rediscovery, not recall.

