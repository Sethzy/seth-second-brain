---
type: raw_capture
source_type: web
title: "Sunder sync: 06-run_agent_memory_sql.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/06-run_agent_memory_sql.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/06-run_agent_memory_sql.md"
sha256: "58adbc4217285ae85be836a0b593170013e43ade3de07f6a8d38cb2694d2bc45"
duplicate_of: ""
---

# Sunder sync: 06-run_agent_memory_sql.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/06-run_agent_memory_sql.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 6. run_agent_memory_sql

- Group: Built-In Tools
- Category: Database
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "run_agent_memory_sql",
  "description": "Runs a SQL query against the agent's SQL database.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["query"],
    "additionalProperties": false,
    "properties": {
      "query": {
        "type": "string",
        "description": "The SQL query to execute. Must be a single SQL statement."
      }
    }
  }
}
```

