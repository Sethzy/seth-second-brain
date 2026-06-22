---
type: raw_capture
source_type: web
title: "Sunder sync: 29-delete_connection.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/29-delete_connection.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/29-delete_connection.md"
sha256: "7a8ea2596d103512b7d254c19271a12c8ffa3c7bb55145dc709f21508fd509e9"
duplicate_of: ""
---

# Sunder sync: 29-delete_connection.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/29-delete_connection.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 29. delete_connection

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "delete_connection",
  "description": "PERMANENTLY DELETES a connection from the user's account. Displays a confirmation UI showing all agents that use this connection before deletion. This destroys the stored credentials and cannot be undone.\n\nWARNING: This is a destructive action. Only use when the user explicitly wants to DELETE the connection itself (e.g., \"delete this connection\", \"remove from my account\").\nDO NOT use this tool if the user wants to remove or deactivate tools from a connection (e.g., \"remove {connection name}\") → use manage_activated_tools_for_connections instead",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["connectionId"],
    "additionalProperties": false,
    "properties": {
      "connectionId": {
        "type": "string",
        "description": "The connectionId to delete. Must be a valid connectionId from the user's existing connections."
      }
    }
  }
}
```

