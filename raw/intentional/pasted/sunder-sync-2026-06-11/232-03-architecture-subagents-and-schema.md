---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-architecture-subagents-and-schema.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/03-architecture-subagents-and-schema.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/03-architecture-subagents-and-schema.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/03-architecture-subagents-and-schema.md"
sha256: "ec03bae48f8853202114928bf97579e1f95ac46c7e663a00b623fb62a28a7113"
duplicate_of: ""
---

# Sunder sync: 03-architecture-subagents-and-schema.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/03-architecture-subagents-and-schema.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/03-architecture-subagents-and-schema.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Architecture, Subagents, and Schema

## Layered design

1. Trigger layer
- schedule invocation

2. Main orchestration layer
- fetch meetings
- coordinate research
- compile and deliver briefing

3. Subagent layer
- person-research subagent
- company-research subagent

4. Data layer
- SQL caches and execution logs
- filesystem artifacts (templates, generated docs)

## Why split into two subagents

- domain specialization (person vs company)
- lower per-subagent context pressure
- cleaner failure isolation and cache boundaries

## Suggested SQL entities

- `person_research_cache`
- `company_research_cache`
- `briefing_executions`
- `meeting_history`

## Cache policy

Baseline strategy:
- time-based expiry (for example 30 days)
- refresh on expiry
- optional lightweight freshness checks on use


