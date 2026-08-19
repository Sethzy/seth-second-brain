---
type: wiki_article
title: Context Engineering For Coding Agents
updated_at: 2026-06-30
status: draft
source_count: 8
tags:
  - context-engineering
  - coding-agents
  - retrieval
  - subagents
  - memory
---

# Context Engineering For Coding Agents

> Sources: sysls X Article, 2026-03-03; Peter Wang X Article, 2026-06-11; YC Root Access context-engineering talks, 2026-06-12 captures; Ashpreet Bedi Scout X Article, 2026-04-28; Kyle Jeong Browserbase bb X Article, 2026-04-16; Sebastian Raschka coding-agent components article, 2026-06-11 capture; Jason Liu Codex-maxxing, 2026-05-10.
> Raw: [sysls world-class agentic engineer X Article](../../raw/intentional/x/2028814227004395561-systematicls-how-to-be-a-world-class-agentic-engineer-introduction-you-re-a-developer-you.md); [Peter Wang vertical-agent context hierarchy X Article](../../raw/intentional/x/2065190286519906657-brainsandtennis-building-a-good-vertical-agent-how-do-you-build-an-agent-that-actually-per.md); [Context Engineering for Engineers](../../raw/intentional/youtube/2026-06-12-context-engineering-for-engineers.md); [Advanced Context Engineering for Agents](../../raw/intentional/youtube/2026-06-12-advanced-context-engineering-for-agents.md); [Ashpreet Bedi Scout company brain X Article](../../raw/intentional/x/2049180168200106150-ashpreetbedi-meet-scout-the-open-source-company-brain-yc-s-summer-2026-requests-for-startu.md); [Kyle Jeong Browserbase bb X Article](../../raw/intentional/x/2044878529666662616-kylejeong-how-we-build-internal-agents-at-browserbase-tldr-generalized-agents-will-become.md); [Sebastian Raschka coding-agent components article](../../raw/intentional/web/2026-06-11-sebastian-raschka-components-of-a-coding-agent.md); [Jason Liu Codex-maxxing](../../raw/intentional/web/2026-06-10-jason-liu-codex-maxxing.md)

## Overview

Context engineering is deciding what goes into the agent's working context: instructions, source facts, tools, examples, user intent, and prior state. Bigger context windows do not remove the need for curation. They make it easier to hide irrelevant, stale, or conflicting tokens inside a very expensive haystack. The useful operating frame is gather broadly, glean aggressively, and preserve the review trail.

## Context Budget

Every token competes with the task. Global instructions should stay small and stable. Project rules should route the agent to the right files or skills instead of embedding the whole operating manual. Raw sources should remain searchable and cited, while compiled wiki pages should carry the durable synthesis.

Tool count is context cost too. A single expressive execution surface can beat many overlapping narrow tools when the domain API is available through code and the docs are clear. The inverse is also true: when credentials, policies, or workflows are risky, a narrow tool with good descriptions and hard permissions may be better than a broad shell.

## L1/L2/L3 Memory

Peter Wang's vertical-agent hierarchy is the cleanest local mental model:

- L1: always-resident hot path. Short rules, active task contract, critical constraints, and the immediate files.
- L2: curated on-demand specs, skills, playbooks, source routers, and deferred tools.
- L3: full raw substrate: source captures, logs, transcripts, docs, and archives reachable through search.

The target is not to stuff everything into context. The target is to minimize context spent per task while preserving enough accuracy and provenance to avoid hallucinated work.

## Research And Planning Artifacts

Complex codebase work should often split research from implementation. A research pass should find files, APIs, invariants, tests, and failure modes, then write a compact plan with file paths and line references. A fresh implementation context can then execute against that plan without carrying the entire search history.

Dex Horthy's warning is the practical one: bad research upstream can create hundreds of bad lines downstream. Review the research artifact before implementation when the problem is ambiguous, cross-cutting, or brownfield.

## Context Providers And Tool Surfaces

Context providers reduce tool pollution by hiding source-specific quirks behind a small query/update interface. Ashpreet Bedi's Scout pattern points this way: put a provider or subagent between the main agent and each messy source so the main agent sees a compact surface while the provider handles pagination, identity lookup, thread traversal, and source-specific caveats.

Navigation can beat search when freshness and citations matter. For company context, a live traversal of docs, CRM, Slack, or web pages may be more trustworthy than a stale vector chunk. Browserbase's `bb` pattern extends that idea into a Slack-native internal agent with scoped skills, browser access, sandboxed compute, and a credential proxy.

## Failure Modes

Common failures are over-broad context, stale retrieval, link-only notes treated as evidence, hidden contradictions, tool descriptions that omit constraints, and long sessions that accumulate unrelated state. The mitigation is boring but strong: cite full sources, compact intentionally, use fresh sessions for well-scoped contracts, keep source maps current, and make the plan artifact reviewable.

For Seth Second Brain, the same pattern applies to the wiki itself. Raw stays immutable, wiki pages synthesize, the index routes, QMD retrieves, and maintenance passes split pages when one note starts carrying multiple jobs.

## See Also

- [Agentic Engineering Practices](agentic-engineering-practices.md)
- [Agentic SDLC And Task Contracts](agentic-sdlc-and-task-contracts.md)
- [Harness Engineering And Runtime Control](harness-engineering-and-runtime-control.md)
- [LLM Foundations](../llm-foundations/llm-foundations.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
