---
type: raw_capture
source_type: pasted
title: "Sunder sync: 09-non-goals-and-limitations.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/09-non-goals-and-limitations.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/09-non-goals-and-limitations.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/09-non-goals-and-limitations.md"
sha256: "ddb6e90a8918f2ad210a852dd54365320fd9fda081d83502f45e58844ff3d24d"
duplicate_of: ""
---

# Sunder sync: 09-non-goals-and-limitations.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/09-non-goals-and-limitations.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/09-non-goals-and-limitations.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Non-Goals and Limitations

## What Tasklet Is Not

1. Not a deterministic workflow engine
- No strict DAG semantics by default
- No guaranteed same-path execution per trigger

2. Not self-improving by default
- No autonomous learning loop unless explicitly built

3. Not version-controlled by default
- Artifact overwrites can be destructive without external VCS backup

4. Not automatically cost-optimized
- Token usage scales with context/tool payload growth

## Architectural Consequence

Robustness depends more on engineered artifacts and operating discipline than on base platform magic.

