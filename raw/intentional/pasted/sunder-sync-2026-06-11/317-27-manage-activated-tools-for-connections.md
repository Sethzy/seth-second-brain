---
type: raw_capture
source_type: web
title: "Sunder sync: 27-manage_activated_tools_for_connections.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/27-manage_activated_tools_for_connections.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/27-manage_activated_tools_for_connections.md"
sha256: "733199b8504a7c6c3c34a615cfbf1da7857e1509999b73168fbc6c2c729499a6"
duplicate_of: ""
---

# Sunder sync: 27-manage_activated_tools_for_connections.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/27-manage_activated_tools_for_connections.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 27. manage_activated_tools_for_connections

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "manage_activated_tools_for_connections",
  "description": "Activates or deactivates tools for connections.\nChanging activation status of tools requires the user to approve the permission changes, so a UI card will be displayed to the user where they can approve or reject the changes.\nThe tool will return after the user approves or rejects the permission changes.\n\nReturns an array of objects for each connection:\n- connectionId: the connection ID\n- userAction: 'approved' if user approved the changes, 'skipped' if user rejected\n- tools: { activated: string[], deactivated: string[] } - lists of tool names currently activated/deactivated for the connection\n- skills: (optional) instructions to read the skills file for this connection.\n\nActivated tools will then become available to use and will appear in your tool context with the tool name prefixed by the connection ID.\nYou MUST always verify exact tool names before activating them. Use get_details_for_connections to see tool names and descriptions for a connection. Never guess a tool name.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["connections"],
    "additionalProperties": false,
    "properties": {
      "connections": {
        "type": "array",
        "items": {
          "type": "object",
          "required": ["connectionId", "activate", "deactivate"],
          "additionalProperties": false,
          "properties": {
            "connectionId": {
              "type": "string",
              "description": "The connectionId to activate or deactivate tools for. Must be a valid connectionId from the user's existing connections."
            },
            "activate": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Tool names to activate from this connection. Always verify exact tool names before activating them."
            },
            "deactivate": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "Tool names to deactivate from this connection."
            }
          }
        }
      }
    }
  }
}
```

