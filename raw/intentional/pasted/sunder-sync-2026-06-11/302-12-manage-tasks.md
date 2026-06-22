---
type: raw_capture
source_type: web
title: "Sunder sync: 12-manage_tasks.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/12-manage_tasks.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/12-manage_tasks.md"
sha256: "e0ee17a9799a46d04c005256a6bd4e4a2dccf3833ba79a83bb06c1785711ec58"
duplicate_of: ""
---

# Sunder sync: 12-manage_tasks.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/12-manage_tasks.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 12. manage_tasks

- Group: Built-In Tools
- Category: Tasks
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "manage_tasks",
  "description": "Manage task items for this agent. Supports batch operations for efficiency.\n\nOperations:\n- add: Create a new task with a title and optional payload. taskId MUST NOT be set.\n- update: Modify an existing task's title or payload. taskId is REQUIRED.\n- delete: Remove a task to mark it as done. taskId is REQUIRED.\n\nYou can perform multiple operations in a single call (e.g., add multiple tasks, update several at once, or mix different operations).\n\nNote: All current tasks are visible in the agent's synced state.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["operations"],
    "additionalProperties": false,
    "properties": {
      "operations": {
        "type": "array",
        "minItems": 1,
        "description": "Array of task operations to perform. You can add, update, or delete multiple tasks in a single call.",
        "items": {
          "type": "object",
          "required": ["operation"],
          "additionalProperties": false,
          "properties": {
            "operation": {
              "type": "string",
              "enum": ["add", "update", "delete"],
              "description": "The operation to perform: add (create new task, taskId must NOT be set), update (modify existing task), delete (remove task to mark it as done)"
            },
            "taskId": {
              "type": "string",
              "description": "The ID of the task. REQUIRED for update and delete operations. MUST NOT be set for add operation."
            },
            "title": {
              "type": "string",
              "description": "The title of the task (required for add, optional for update)"
            },
            "payload": {
              "description": "Optional JSON payload attached to the task for additional information in addition to the title"
            }
          }
        }
      }
    }
  }
}
```

