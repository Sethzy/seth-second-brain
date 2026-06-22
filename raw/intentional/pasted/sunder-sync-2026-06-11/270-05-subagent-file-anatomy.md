---
type: raw_capture
source_type: pasted
title: "Sunder sync: 05-subagent-file-anatomy.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/05-subagent-file-anatomy.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/05-subagent-file-anatomy.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/persistence-and-cron/05-subagent-file-anatomy.md"
sha256: "660cae231b0023c1360b01c630c8cf876058aab0de5ddbcff599845abe33622f"
duplicate_of: ""
---

# Sunder sync: 05-subagent-file-anatomy.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/05-subagent-file-anatomy.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/persistence-and-cron/05-subagent-file-anatomy.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Subagent File Anatomy

Subagent files are markdown instruction contracts for a fresh model instance.

## Typical sections

1. Title/description
- what the subagent does

2. Input contract
- expected payload fields and constraints

3. Procedure/instructions
- ordered execution steps

4. Output contract
- strict response shape (prefer JSON schema-like structure)

5. Error handling
- retries, fallback behavior, partial-result policy

6. Caching/state policy
- SQL/table usage, TTL, idempotency behavior

## Execution model

`run_subagent(path, payload)` spawns a new model context that reads markdown + payload, runs tools, then returns only final output to parent.

## Reliability rule

Subagent markdown should be written as executable SOP, not as a short reminder.


