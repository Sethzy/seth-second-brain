---
type: raw_capture
source_type: web
title: "Sunder sync: 24-get_details_for_connections.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/24-get_details_for_connections.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/24-get_details_for_connections.md"
sha256: "b48fc1b0cdb712b17f84605a3f3df8772d03e1f727f8687e5a88015203a1b91e"
duplicate_of: ""
---

# Sunder sync: 24-get_details_for_connections.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/24-get_details_for_connections.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 24. get_details_for_connections

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "get_details_for_connections",
  "description": "Gets detailed information for the listed connections.\nReturns a full list of tools, including both activated and deactivated tools, for each connection, including full detailed descriptions and arguments if requested.\nAlso returns connectionId, serviceName, description, accountName, connectionType, toolCount, and other connection-specific details.\n\nUse this to:\n- Discover what actions you can perform with a connection before activating it\n- Check which tools are already activated for a connection\n- Verify exact tool names before activating connections",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["connectionIds", "includeToolDetails"],
    "additionalProperties": false,
    "properties": {
      "connectionIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The connection IDs to get details for"
      },
      "includeToolDetails": {
        "type": "boolean",
        "description": "Pass true to include detailed descriptions and arguments for each connnection tool in the results"
      }
    }
  }
}
```

