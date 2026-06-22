---
type: raw_capture
source_type: web
title: "Sunder sync: 26-search_for_integrations.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/26-search_for_integrations.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/26-search_for_integrations.md"
sha256: "da51565b73a9414d6bfababa04920b70ddb135b66c5ac58d1679c51dbfa7d079"
duplicate_of: ""
---

# Sunder sync: 26-search_for_integrations.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/26-search_for_integrations.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 26. search_for_integrations

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "search_for_integrations",
  "description": "Lists integrations that match one or more given keywords. Keywords are single words (e.g. email, billing, tasks, Gmail, Asana, etc.).\nSearches integrations built by the Tasklet team as well as integrations from Pipedream (over 3000 total) and returns:\n- Integration ID\n- Name and description\n- Quality score (GREAT/GOOD/OK/LIMITED/UNKNOWN)\n- Who built it\n- Additional context about its capabilities and usage\n\nNEVER mention integration quality scores or who built the integrations unless the user specifically asks.\n\nOnce you have the integration ID you can get more information about it if needed using get_integrations_capabilities.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["keywords"],
    "additionalProperties": false,
    "properties": {
      "keywords": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The list of keywords to search for. Each keyword must be a single word. Verify exact tool names by calling get_integrations_capabilities first."
      }
    }
  }
}
```

