---
type: raw_capture
source_type: pasted
title: "Sunder sync: 07-reliability-characteristics.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/07-reliability-characteristics.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/07-reliability-characteristics.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/07-reliability-characteristics.md"
sha256: "2048c71963d4e4dcbf80935a60becef1b0606f5bfcea3e1cc488f9ed5a2acd2c"
duplicate_of: ""
---

# Sunder sync: 07-reliability-characteristics.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/07-reliability-characteristics.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/07-reliability-characteristics.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Reliability Characteristics

## Variance Sources

1. Model non-determinism
- Same inputs can produce different decomposition and recovery behavior.

2. External dependency volatility
- API failures, rate limits, schema drift, auth expiry.

3. Context and payload constraints
- Truncation or oversized tool outputs can degrade decisions.

## Reliability Improvement Levers

- Highly specific subagent instructions
- Explicit config files for parameters and limits
- Deterministic scripts for fragile data logic
- Persistent state tracking for retries/idempotency
- Concrete error-handling branches in instructions

## Anti-Patterns

- Vague trigger names
- Thin/no operational instructions
- Implicit state with no artifact trail
- Assuming model will infer exact desired behavior every run

