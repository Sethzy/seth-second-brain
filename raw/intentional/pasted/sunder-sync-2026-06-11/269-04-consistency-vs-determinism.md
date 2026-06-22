---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-consistency-vs-determinism.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/04-consistency-vs-determinism.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/04-consistency-vs-determinism.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/04-consistency-vs-determinism.md"
sha256: "df16d8890560e2ac7cc9260e4de5c634b07de31f7a4526f8977e66a53b328047"
duplicate_of: ""
---

# Sunder sync: 04-consistency-vs-determinism.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/04-consistency-vs-determinism.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/04-consistency-vs-determinism.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Consistency vs Determinism

## Determinism ladder

1. Trigger name only
- low determinism
- model re-derives most behavior

2. Trigger + subagent
- medium determinism
- behavior follows instruction quality

3. Trigger + detailed subagent + explicit config/DB contracts
- high determinism
- less interpretive ambiguity

4. Trigger + subagent that invokes deterministic script
- very high determinism
- model orchestrates, script performs exact logic

## Drift modes

- model forgets to invoke intended subagent
- vague subagent text allows interpretation drift
- missing config defaults cause behavior variation

## Mitigation

- strict subagent contracts (input/output/errors)
- explicit config files and schema
- deterministic code for fragile business logic


