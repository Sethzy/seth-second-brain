---
type: raw_capture
source_type: web
title: "Sunder sync: 04-web_scrape_website.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Sunder - Source of Truth/references/tasklet/tools/built-in/04-web_scrape_website.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "02_Areas/Product/Sunder - Source of Truth/references/tasklet/tools/built-in/04-web_scrape_website.md"
sha256: "76e8dbad54c1fa916e705d40be9028053313bb321d0c2831e2f9f2753ef0797b"
duplicate_of: ""
---

# Sunder sync: 04-web_scrape_website.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Sunder - Source of Truth/references/tasklet/tools/built-in/04-web_scrape_website.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# 4. web_scrape_website

- Group: Built-In Tools
- Category: Web
- Source: ../00-complete-tasklet-tool-definitions-verbatim.md

```json
{
  "name": "web_scrape_website",
  "description": "Reads a single webpage and extracts its content as markdown",
  "parameters": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["url"],
    "additionalProperties": false,
    "properties": {
      "url": {
        "type": "string",
        "description": "The URL of the webpage to scrape. Must be either a http:// or https:// URL."
      }
    }
  }
}
```

