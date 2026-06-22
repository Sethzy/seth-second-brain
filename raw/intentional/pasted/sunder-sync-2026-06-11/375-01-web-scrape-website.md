---
type: raw_capture
source_type: web
title: "Sunder sync: 01-web_scrape_website.md"
url: "https://json-schema.org/draft/2020-12/schema"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/references/tasklet/tasklet tools/built-in/v2/01-web_scrape_website.md"
source_root: "/Users/sethlim/Documents/sunder-next-migration-20260225"
source_relpath: "roadmap docs/Sunder - Source of Truth/references/tasklet/tasklet tools/built-in/v2/01-web_scrape_website.md"
sha256: "ea3786609d4259de2b2f2dd3bf6bd1acd7faa2eac2f6fd4e1d2d8a7e5a9403a7"
duplicate_of: ""
---

# Sunder sync: 01-web_scrape_website.md

Source file: `/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/references/tasklet/tasklet tools/built-in/v2/01-web_scrape_website.md`

Primary URL: https://json-schema.org/draft/2020-12/schema

Duplicate of existing source-map entry: `none`

## Capture Text

# web_scrape_website

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

