---
type: raw_capture
source_type: web
title: "Sunder sync: 02-write_file.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/02-write_file.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/02-write_file.md"
sha256: "d4094eed4516def3bcdf8edd60813fa5a6a05f0c630234c24440115c15402482"
duplicate_of: ""
---

# Sunder sync: 02-write_file.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/02-write_file.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 2. write_file

- Group: Built-In Tools
- Category: Filesystem
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "write_file",
  "description": "Creates, edits, or deletes a file in the filesystem. Supports three operations: write (create or overwrite), edit (find and replace text), and delete.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["op", "path", "action_pending", "action_finished", "action_error"],
    "additionalProperties": false,
    "properties": {
      "op": {
        "type": "string",
        "enum": ["write", "edit", "delete"],
        "description": "The operation type"
      },
      "path": {
        "type": "string",
        "description": "Path for the file"
      },
      "content": {
        "type": "string",
        "description": "File content, overwrites existing content (required for write op)"
      },
      "old_string": {
        "type": "string",
        "minLength": 1,
        "description": "Exact text to find and replace in the file (required for edit op)"
      },
      "new_string": {
        "type": "string",
        "description": "Replacement text, can be empty to delete old_string (required for edit op)"
      },
      "replace_all": {
        "type": "boolean",
        "description": "If true, replace all occurrences. If false (default), fails on multiple matches."
      },
      "action_pending": {
        "type": "string",
        "description": "Custom UI status text shown while running. IMPORTANT: Output these three action_ parameters before all other parameters."
      },
      "action_finished": {
        "type": "string",
        "description": "Custom UI status text shown on success."
      },
      "action_error": {
        "type": "string",
        "description": "Custom UI status text shown on failure."
      }
    }
  }
}
```

