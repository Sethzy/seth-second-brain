---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-execution-modes-and-rediscovery.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/04-execution-modes-and-rediscovery.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/04-execution-modes-and-rediscovery.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/core-architecture/04-execution-modes-and-rediscovery.md"
sha256: "39f1da06b308523e1d3a80aeea01c839ac7335e62becf6cb4e65b030359cc5df"
duplicate_of: ""
---

# Sunder sync: 04-execution-modes-and-rediscovery.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/04-execution-modes-and-rediscovery.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/core-architecture/04-execution-modes-and-rediscovery.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Execution Modes and Rediscovery

## Mode 1: Interactive Chat

Flow:
- User message -> LLM -> tools -> LLM -> response
- Conversation context accumulates during session
- Session end drops transient conversational memory

## Mode 2: Trigger Execution

Flow:
- Event fires -> fresh LLM instance
- Prompt is reconstructed from system prompt + system reminder + trigger payload
- Model must rediscover intent from persisted artifacts

## Rediscovery Pattern

Because trigger invocations start fresh, effective runs require:
- Reading subagent instructions
- Reading config/state files
- Querying DB/task state as needed

Without rediscoverable artifacts, behavior degrades into probabilistic guesswork.

