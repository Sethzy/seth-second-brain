---
type: raw_capture
source_type: pasted
title: "Sunder sync: README.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/README.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/README.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/README.md"
sha256: "f627b8e9c5be18b7fb0da3bf34f807447504df8080d118553aa7c098077a6d24"
duplicate_of: ""
---

# Sunder sync: README.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/README.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/README.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Tasklet Reverse-Engineered Architecture

This folder contains explicit component documentation for Tasklet.

## Sandbox Activation Model (Important Clarification)

Tasklet does **not** need the Linux sandbox for every assistant response.

- The sandbox is used when `run_command` is invoked.
- File operations (`read_file`, `write_file`) run through filesystem tools and do not require shell execution.
- SQL tools and web tools also run as tool calls without direct shell execution.
- Commands like Python/shell scripts, `curl`, or package installs (`apk`) require `run_command`, so they use the sandbox.
- Sandbox environments are ephemeral by design. Installed packages do not persist between sessions.
- Tasklet uses one active LLM context with a flat first-class tool list; it is not an "inner agent running in sandbox" model for normal tool use.
- Subagent specialization uses fresh LLM invocation (`run_subagent`), not nested Agent SDK runtime inside shell execution.

Quick reference:

| Action | Needs sandbox? |
|---|---|
| Chat responses / reasoning | No |
| `read_file` / `write_file` | No |
| SQL tools | No |
| Web search / web scrape tools | No |
| Shell, Python, `curl`, `apk` via `run_command` | Yes |

## Components

- `tools/` - AI agent tool definitions (complete: 33 tools)
- `linkedin-automation/` - LinkedIn/browser automation architecture docs
- `core-architecture/` - Runtime, tooling, state, and reliability architecture docs
- `skills-system/` - System skill files and normalized behavior contracts
- `first-run-lifecycle/` - First-run setup, persistence, and rediscovery behavior docs
- `persistence-and-cron/` - Explicit persistence, cron invocation, and determinism docs
- `complex-multi-integration-workflow/` - End-to-end complex recurring workflow design and trace docs
- `simple-price-monitor-workflow/` - Baseline recurring price-monitor workflow design and trace docs
- `system-prompt-wholesale/` - Full system prompt verbatim reference
- `other-system-prompts-and-e2e-architecture/` - Supplemental prompt context and E2E operating loop reference

## Current Scope

Phase 1 is complete: all AI-agent tools are documented with labeled markdown files, including:

- One verbatim master source file
- One file per tool (33 total)
- Indexed README with categories and links

Phase 2 is added: LinkedIn automation architecture documentation, including:

- One raw source capture file
- Four normalized architecture/analysis files
- Component README index

Phase 3 is added: complete Tasklet architecture documentation, including:

- One raw source breakdown capture file
- Ten normalized subsystem files
- Component README index

Phase 4 is added: skills-system documentation, including:

- One raw skill source capture file
- Three normalized skill analysis files
- One artifact/corruption notes file
- Component README index

Phase 5 is added: first-run lifecycle documentation, including:

- One raw lifecycle source capture file
- Four normalized lifecycle analysis files
- Component README index

Phase 6 is added: persistence-and-cron documentation, including:

- One raw persistence/cron source capture file
- Six normalized persistence/determinism analysis files
- Component README index

Phase 7 is added: complex multi-integration workflow documentation, including:

- One raw complex-workflow source capture file
- Seven normalized workflow analysis files
- Component README index

Phase 8 is added: simple price monitor workflow documentation, including:

- One raw simple-workflow source capture file
- Six normalized workflow analysis files
- Component README index

Phase 9 is added: system prompt wholesale documentation, including:

- One full verbatim system prompt file
- Component README index

Phase 10 is added: other system prompts and E2E architecture documentation, including:

- One verbatim supplemental prompt/E2E walkthrough file
- Component README index

