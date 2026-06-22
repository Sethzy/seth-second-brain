---
type: raw_capture
source_type: x
title: "Sunder sync: the-agentic-workload-igor-zalutski.md"
url: "https://x.com/igorzij/status/2033316871928254530"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/references/sandboxes/the-agentic-workload-igor-zalutski.md"
source_root: "/Users/sethlim/Documents/sunder-next-migration-20260225"
source_relpath: "roadmap docs/Sunder - Source of Truth/references/sandboxes/the-agentic-workload-igor-zalutski.md"
sha256: "5da722bf7aab2eda45d719ea4f212ebab54cb9e1ece034ce0520fb50fe8e9f1c"
duplicate_of: ""
---

# Sunder sync: the-agentic-workload-igor-zalutski.md

Source file: `/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/references/sandboxes/the-agentic-workload-igor-zalutski.md`

Primary URL: https://x.com/igorzij/status/2033316871928254530

Duplicate of existing source-map entry: `none`

## Capture Text

# The Agentic Workload

**Author:** Igor Zalutski (@IgorZIJ)
**Date:** March 16, 2026
**Source:** https://x.com/igorzij/status/2033316871928254530

## Summary

Agent code is a new workload type — not a traditional backend service or frontend. The existing deployment paradigms (containers, serverless) don't fit well because agent sessions need ad-hoc sandboxes, file system access, and unpredictable resource consumption.

## Key Points

1. **Leading coding agents are CLIs for a reason.** Claude Code, Codex, Amp ship as CLIs because the "right" server-side design doesn't work in practice — dev environments live on laptops, not in clean remote setups. CLIs meet developers where they are with zero setup.

2. **Harness-based SDKs outperform DIY frameworks.** Claude Agent SDK and Codex SDK wrap the battle-tested CLI harnesses. Bill Chen (OpenAI) suggests treating the harness as the pluggable building block instead of making direct model calls.

3. **The agentic workload pattern.** Regardless of what the agent does, deploying it requires:
   - Creating an ad-hoc sandbox for every agent session (and tracking its lifecycle)
   - Putting a version of the agent's code into it
   - An always-on gateway service for handling incoming webhooks and requests
   - A queue to store incoming messages while the sandbox is being created

4. **No obvious deployment home yet.** This workload type doesn't fit neatly into existing infrastructure categories, but new dev platforms will likely emerge to serve it.

## Related References

- Michael Livshits — "A Thousand Ways to Sandbox an Agent" (referenced in article)
- Anthropic Agent SDK deployment patterns guide
- Fly.io — "Code and Let Live"

