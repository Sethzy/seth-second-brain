---
type: raw_capture
source_type: web
title: "Sunder sync: 03-web_search_web.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/03-web_search_web.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/03-web_search_web.md"
sha256: "34c81054f7dcf81bb5ccaeac74f0a4510b74e13541a2122830da3233c924943d"
duplicate_of: ""
---

# Sunder sync: 03-web_search_web.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/03-web_search_web.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 3. web_search_web

- Group: Built-In Tools
- Category: Web
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "web_search_web",
  "description": "Searches the web for relevant content based on a query",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["query"],
    "additionalProperties": false,
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query to use for web search"
      },
      "limit": {
        "type": "number",
        "minimum": 1,
        "maximum": 100,
        "description": "Maximum number of results to return (default: 10, max: 100)"
      },
      "location": {
        "type": "string",
        "description": "Geographic location for search results. Examples: \"Germany\", \"San Francisco,California,United States\". Default: \"US\""
      },
      "tbs": {
        "type": "string",
        "description": "Time-based search parameter. Use predefined values: qdr:h (hour), qdr:d (day), qdr:w (week), qdr:m (month), qdr:y (year). Or custom date range: cdr:1,cd_min:MM/DD/YYYY,cd_max:MM/DD/YYYY"
      }
    }
  }
}
```

