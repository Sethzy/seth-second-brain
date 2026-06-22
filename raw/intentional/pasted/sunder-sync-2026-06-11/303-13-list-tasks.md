---
type: raw_capture
source_type: web
title: "Sunder sync: 13-list_tasks.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/13-list_tasks.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/13-list_tasks.md"
sha256: "ce2dae5dcb4f66634a7a7bb4f406ed3e553a6c18ccc36ec951c2ad3a8e2afc82"
duplicate_of: ""
---

# Sunder sync: 13-list_tasks.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/13-list_tasks.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 13. list_tasks

- Group: Built-In Tools
- Category: Tasks
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "list_tasks",
  "description": "List tasks for this agent. Can optionally filter by specific task IDs.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "additionalProperties": false,
    "properties": {
      "taskIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Optional array of task IDs to filter. If not provided, returns all tasks."
      }
    }
  }
}
```

