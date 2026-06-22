---
type: raw_capture
source_type: web
title: "Sunder sync: 09-reply_message.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/09-reply_message.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/09-reply_message.md"
sha256: "c672087db0c8415758e48be9c092d4f92f9d0ef3035cf10b163dda12798b4d86"
duplicate_of: ""
---

# Sunder sync: 09-reply_message.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/09-reply_message.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 9. reply_message

- Group: Built-In Tools
- Category: Messaging
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "reply_message",
  "description": "Reply to an existing message thread. For email, this sends a reply-all. For text, this continues the same conversation.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["messageId", "body"],
    "additionalProperties": false,
    "properties": {
      "messageId": {
        "type": "string",
        "description": "The message ID to reply to. This continues the conversation thread."
      },
      "body": {
        "type": "string",
        "description": "The body of the reply. Supports markdown for email."
      },
      "attachments": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "File paths in /agent/ to attach to the reply."
      }
    }
  }
}
```

