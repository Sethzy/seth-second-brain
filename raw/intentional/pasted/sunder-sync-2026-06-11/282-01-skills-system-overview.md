---
type: raw_capture
source_type: pasted
title: "Sunder sync: 01-skills-system-overview.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/01-skills-system-overview.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/01-skills-system-overview.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/skills-system/01-skills-system-overview.md"
sha256: "1adf6c9690654a5e906ee690f050fec304cfe3ef62824ab7d9a0fb69f6e456da"
duplicate_of: ""
---

# Sunder sync: 01-skills-system-overview.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/01-skills-system-overview.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/01-skills-system-overview.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Skills System Overview

This component documents Tasklet's system skills layer: markdown instruction files that constrain how the agent uses platform capabilities.

## Referenced Skill Files

- `/agent/skills/system/README.md`
- `/agent/skills/system/building-preview-apps/SKILL.md`
- `/agent/skills/system/creating-connections/SKILL.md`

## Purpose of Skills

- Standardize operational behavior for specific domains.
- Encode hard constraints (security, UX, tooling, and flow requirements).
- Reduce policy drift across sessions.

## Themes in Current Skills

1. Preview app development discipline
- CSP-safe dependencies
- strict response-shape validation
- optimistic UI with rollback
- persistence via SQL/file tools (not browser storage)

2. Connection-creation policy
- prefer pre-built integrations
- verify capabilities before enabling
- treat direct API/computer use as specialized paths


