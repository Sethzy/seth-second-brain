---
type: raw_capture
source_type: web
title: "Sunder sync: 17-manage_active_triggers.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/17-manage_active_triggers.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/17-manage_active_triggers.md"
sha256: "69a85ec8c2352934ce7001637e430169d2abb67175e15048de040d35bb4f5ef8"
duplicate_of: ""
---

# Sunder sync: 17-manage_active_triggers.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/17-manage_active_triggers.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 17. manage_active_triggers

- Group: Built-In Tools
- Category: Triggers
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "manage_active_triggers",
  "description": "Manage the agent's active triggers.\n\nActions:\n- list: Returns all active triggers with their IDs, names, titles, and arguments.\n- view: Shows detailed information for a specific trigger. Requires trigger_instance_id.\n- delete: Removes an active trigger. Requires trigger_instance_id. This is destructive.\n- simulate: Fires a test event on a trigger to test the agent's response. Requires trigger_instance_id and payload.\n\nUse list first to see available triggers and get their instance IDs.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["action"],
    "additionalProperties": false,
    "properties": {
      "action": {
        "type": "string",
        "enum": ["list", "view", "delete", "simulate"],
        "description": "The action to perform: \"list\" returns all active triggers, \"view\" shows details for a specific trigger, \"delete\" removes a trigger, \"simulate\" fires a test event"
      },
      "trigger_instance_id": {
        "type": "string",
        "description": "The ID of the trigger instance. Required for view, delete, and simulate actions."
      },
      "payload": {
        "type": "object",
        "additionalProperties": {},
        "propertyNames": {
          "type": "string"
        },
        "description": "Test payload for the simulate action. Required when action is \"simulate\"."
      }
    }
  }
}
```

