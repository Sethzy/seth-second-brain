---
type: raw_capture
source_type: web
title: "Sunder sync: 28-reauthorize_connection.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/28-reauthorize_connection.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/28-reauthorize_connection.md"
sha256: "49f7d87f465c05ac9665fbe99c04942c0a94099044e0f6ba13ea313206e0a4b4"
duplicate_of: ""
---

# Sunder sync: 28-reauthorize_connection.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/28-reauthorize_connection.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 28. reauthorize_connection

- Group: Built-In Tools
- Category: Connections
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "reauthorize_connection",
  "description": "Re-authorizes an existing connection that has expired or needs new permissions. Displays a UI card where the user can complete the auth flow to re-authorize the connection.\n\nUse this tool if and only if there were authorization errors with a connection or the user explicitly asks you to.\nThe connection must already exist in the user's account.\nRe-authorizing cannot change which account the connection is logged into in the external service.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["connectionId"],
    "additionalProperties": false,
    "properties": {
      "connectionId": {
        "type": "string",
        "description": "The connectionId to reauthorize. This must be a valid connectionId from the user's existing connections."
      }
    }
  }
}
```

