---
type: raw_capture
source_type: web
title: "Sunder sync: 05-run_command.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/05-run_command.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/05-run_command.md"
sha256: "b0599d2f3af3331885ae8b48805ad7f311265f85e98355d4bed32acba66091fa"
duplicate_of: ""
---

# Sunder sync: 05-run_command.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/05-run_command.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 5. run_command

- Group: Built-In Tools
- Category: Sandbox
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "run_command",
  "description": "Executes shell commands in the sandbox environment.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["command", "action_pending", "action_finished", "action_error"],
    "additionalProperties": false,
    "properties": {
      "command": {
        "type": "string",
        "description": "The shell command to execute in the sandbox environment."
      },
      "timeout": {
        "type": "number",
        "maximum": 300,
        "description": "Timeout in seconds for the command. Defaults to 60 seconds."
      },
      "action_pending": {
        "type": "string",
        "description": "Custom UI status text shown while running. IMPORTANT: Output these three action_ parameters before all other parameters."
      },
      "action_finished": {
        "type": "string",
        "description": "Custom UI status text shown on success."
      },
      "action_error": {
        "type": "string",
        "description": "Custom UI status text shown on failure."
      }
    }
  }
}
```

