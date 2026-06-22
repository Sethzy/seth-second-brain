---
type: raw_capture
source_type: web
title: "Sunder sync: 21-rename_chat.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/21-rename_chat.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/21-rename_chat.md"
sha256: "fbf9724e9d8c7ed7c71561bd20e27f527cde83f92d4524e53a63de3a4093735c"
duplicate_of: ""
---

# Sunder sync: 21-rename_chat.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/21-rename_chat.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 21. rename_chat

- Group: Built-In Tools
- Category: UI
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "rename_chat",
  "description": "Renames the chat. Titles should be a concise 3-5 word summary that captures the goal and key tools. If the user requests a specific name, use that name.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["new_title"],
    "additionalProperties": false,
    "properties": {
      "new_title": {
        "type": "string",
        "description": "The new title for the chat."
      }
    }
  }
}
```

