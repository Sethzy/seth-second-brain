---
type: raw_capture
source_type: web
title: "Sunder sync: 15-search_triggers.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/15-search_triggers.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/15-search_triggers.md"
sha256: "a0a29ce173b08b0e0eef523c6823d6f6819aa24d10fbe6c7e164ecbf951f6374"
duplicate_of: ""
---

# Sunder sync: 15-search_triggers.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/15-search_triggers.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 15. search_triggers

- Group: Built-In Tools
- Category: Triggers
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "search_triggers",
  "description": "Search for available triggers by keywords.\nReturns a list of trigger types that match the search criteria, along with their setup schemas and any prerequisites.\n\nUse this tool to discover what triggers are available before setting one up.\n\nThe setupSchema field of each returned trigger describes the schema of the params object that should\nbe passed into the setup_trigger tool.",
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
        "description": "One or more keywords to search for available triggers (e.g., [\"email\", \"schedule\"])"
      }
    }
  }
}
```

