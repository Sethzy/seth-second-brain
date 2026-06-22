---
type: raw_capture
source_type: web
title: "Sunder sync: 20-create_tasklet_app.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/20-create_tasklet_app.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/tools/built-in/20-create_tasklet_app.md"
sha256: "ad8f7f12c5017c3f87a4cec14262fb43c5ae2546162fc87b9a16a86c485edcb6"
duplicate_of: ""
---

# Sunder sync: 20-create_tasklet_app.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/tools/built-in/20-create_tasklet_app.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 20. create_tasklet_app

- Group: Built-In Tools
- Category: UI
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "create_tasklet_app",
  "description": "Scaffolds a new multi-file TSX preview app under /agent/home/apps/<name>/ with a working hello world, DaisyUI styling, and typed bridge wrappers.",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["name"],
    "additionalProperties": false,
    "properties": {
      "name": {
        "type": "string",
        "description": "App name (lowercase, hyphens allowed). Used as the directory name under /agent/home/apps/."
      }
    }
  }
}
```

