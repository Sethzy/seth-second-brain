---
type: raw_capture
source_type: web
title: "Sunder sync: 16-setup_trigger.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/16-setup_trigger.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/16-setup_trigger.md"
sha256: "32bddc5d77625f303fe273b4ba6929f4e2bc92e77d67635b5e3f3869d6cce337"
duplicate_of: ""
---

# Sunder sync: 16-setup_trigger.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/16-setup_trigger.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 16. setup_trigger

- Group: Built-In Tools
- Category: Triggers
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "setup_trigger",
  "description": "Set up a new trigger instance. First use search_triggers to find available triggers\nand their setup schemas, then call this tool with the trigger ID and required parameters.\nOn completion, shows the user a UI card with the trigger details.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["trigger_id", "params"],
    "additionalProperties": false,
    "properties": {
      "trigger_id": {
        "type": "string",
        "description": "The ID of the trigger type to set up (e.g., \"schedule\", \"webhook\", \"gmail\", \"rss\")"
      },
      "params": {
        "type": "object",
        "additionalProperties": {},
        "propertyNames": {
          "type": "string"
        },
        "description": "Setup parameters as defined by the trigger's setupSchema"
      }
    }
  }
}
```

