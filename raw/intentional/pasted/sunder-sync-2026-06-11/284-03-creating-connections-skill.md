---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-creating-connections-skill.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/03-creating-connections-skill.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/03-creating-connections-skill.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/skills-system/03-creating-connections-skill.md"
sha256: "9fdd7201fd0b0733cd0a888b082ea4c20f7eb5daf74bf18084da14d87e642320"
duplicate_of: ""
---

# Sunder sync: 03-creating-connections-skill.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/03-creating-connections-skill.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/03-creating-connections-skill.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Creating Connections Skill

Source: `/agent/skills/system/creating-connections/SKILL.md`

## Intent

Defines preferred order and constraints for establishing new external-service connections.

## Connection Type Priority

1. `integrations`
- First choice when available.
- Use discovery and capability tools before creating.

2. `mcp`
- Custom MCP server connections when integration coverage is insufficient.

3. `direct_api`
- HTTP API connections requiring explicit endpoint/auth correctness.
- Requires reading `create-direct-api-connection.md` before use.

4. `computer_use`
- Remote browser/desktop runtime.
- Useful but slower/expensive; prefer when explicitly needed.

## Required Behaviors

- Verify capability match before creating connection.
- Avoid hallucinated endpoints/URLs.
- Offer alternative connection strategies when one path is unavailable.
- Avoid exhaustive service-list claims; frame capability as broad and extensible.

## Practical Consequence

This skill enforces a conservative "safest/highest-leverage first" connection strategy and discourages speculative setup.


