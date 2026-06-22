---
type: raw_capture
source_type: web
title: "Sunder sync: 25-get_integrations_capabilities.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/25-get_integrations_capabilities.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/25-get_integrations_capabilities.md"
sha256: "09587d9a21b7bafa1c1176300ad73ae7f30ba8df1cf8b82b4ddcf0cfb346095c"
duplicate_of: ""
---

# Sunder sync: 25-get_integrations_capabilities.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/25-get_integrations_capabilities.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 25. get_integrations_capabilities

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "get_integrations_capabilities",
  "description": "Lists the capabilities available via the given integrations, including tools (if available), quality information (GREAT, GOOD, OK, LIMITED, and UNKNOWN), and notes.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["integrationIds"],
    "additionalProperties": false,
    "properties": {
      "integrationIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The list of integration IDs to get capabilities for."
      }
    }
  }
}
```

