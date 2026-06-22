---
type: raw_capture
source_type: web
title: "Sunder sync: 32-gmail_get_threads.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/gmail-connection/32-gmail_get_threads.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/gmail-connection/32-gmail_get_threads.md"
sha256: "171052abdc98cfd8304abaa5975bffec23d7f2cc2c49b5ace443c07017056776"
duplicate_of: ""
---

# Sunder sync: 32-gmail_get_threads.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/gmail-connection/32-gmail_get_threads.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 32. gmail_get_threads

- Group: Gmail Connection Tools
- Category: Gmail (Connection)
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "gmail_get_threads",
  "description": "Get specific email threads by IDs from Gmail with configurable detail level using readMask",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["threadIds", "readMask"],
    "additionalProperties": false,
    "properties": {
      "threadIds": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The IDs of the threads to retrieve. Max 1000 threads."
      },
      "readMask": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["date", "participants", "subject", "bodySnippet", "bodyFull", "bodyHtml", "labels", "attachments"]
        },
        "default": ["date", "participants", "subject", "bodySnippet"],
        "description": "Array of fields to include in the response. Options: date (message date), participants (from/to/cc/bcc), subject (email subject), bodySnippet (brief excerpt), bodyFull (complete message body as markdown), bodyHtml (raw HTML body), labels (message labels), attachments (attachment info). Default includes basic metadata with snippet. Only include bodyFull or bodyHtml if you need to analyze message content."
      }
    }
  }
}
```

