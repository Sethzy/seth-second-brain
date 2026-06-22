---
type: raw_capture
source_type: web
title: "Sunder sync: 08-send_message.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/08-send_message.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/08-send_message.md"
sha256: "bac5e79fb24d002be7c0eacb893c2e108c31f3cf28be9e6bf3dbc35880fe1567"
duplicate_of: ""
---

# Sunder sync: 08-send_message.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/08-send_message.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 8. send_message

- Group: Built-In Tools
- Category: Messaging
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "send_message",
  "description": "Send a message to the user or other verified contact methods via:\n- Email\n- Text\n\nMessages will come from an email address or phone number associated with this agent.\n\nUse 'owner' as the recipient to send to the user's primary email (always available). For other addresses, they must be verified first using add_contact_method.\n\nFor replies to existing threads, use reply_message instead.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["to", "body"],
    "additionalProperties": false,
    "properties": {
      "to": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The recipients (at least one required). Use 'owner' to send to the account owner's primary email address. You can also use any verified email address or phone number. Note: You cannot mix email and text recipients in the same call."
      },
      "subject": {
        "type": "string",
        "description": "The subject of the message. Required for email, disallowed for others."
      },
      "body": {
        "type": "string",
        "description": "The body of the message to send. Supports markdown for email."
      },
      "attachments": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "File paths in /agent/ to attach to the message."
      }
    }
  }
}
```

