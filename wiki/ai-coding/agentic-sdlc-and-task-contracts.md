---
type: wiki_article
title: Agentic SDLC And Task Contracts
updated_at: 2026-06-30
status: draft
source_count: 10
tags:
  - agentic-engineering
  - task-contracts
  - spec-driven-development
  - verification
  - review
---

# Agentic SDLC And Task Contracts

> Sources: Zach Lloyd X Article, 2026-06-11; Karpathy spec-driven development X post, 2026-01-26; David Breunig spec-only library article, 2026-01-08; EveryInc Compound Engineering README, 2026-06-12 capture; obra Superpowers README, 2026-06-12 capture; Vox prompt-shaping X post and screenshots, 2026-06-17 to 2026-06-18; Matt Pocock and Kiro AI Engineer talks, 2026-06-12 captures; Thariq implementation-notes X post, 2026-05-18.
> Raw: [Zach Lloyd spec-driven development X Article](../../raw/intentional/x/2065154860337508577-zachlloydtweets-three-skills-you-need-for-spec-driven-development-if-you-want-to-increase.md); [Karpathy spec-driven development X post](../../raw/intentional/x/2015887154132746653-karpathy-airesearch12-spec-driven-development-it-s-the-limit-of-imperative-gt-declarative.md); [David Breunig spec-only library article](../../raw/intentional/web/2026-06-12-dbreunig-a-software-library-with-no-code.md); [EveryInc Compound Engineering Plugin README](../../raw/intentional/web/2026-06-12-everyinc-compound-engineering-plugin-readme.md); [obra Superpowers README](../../raw/intentional/web/2026-06-12-obra-superpowers-readme.md); [Vox prompt-shaping X post](../../raw/intentional/x/2067237707483337118-voxyz-ai-stop-telling-claude-code-codex-do-this-stop-telling-claude-code-codex-write-code.md); [Vox prompt templates screenshots](../../raw/intentional/pasted/2026-06-18-vox-claude-code-codex-prompt-templates-screenshots.md); [Matt Pocock workflow walkthrough](../../raw/intentional/youtube/2026-06-12-full-walkthrough-workflow-for-ai-coding-matt-pocock.md); [Kiro spec-driven development](../../raw/intentional/youtube/2026-06-12-spec-driven-development-agentic-coding-at-faang-scale-and-quality-al-har.md); [Thariq implementation-notes X post](../../raw/intentional/x/2056418157305454805-trq212-okay-this-is-going-kinda-viral-and-tbh-my-original-text-was-kind-of-messy-so-here-s.md)

## Overview

Agentic coding works best when it is treated as an SDLC, not a chat trick. The human's leverage is to define intent, constraints, verification, and review surfaces before the agent writes too much code. The recurring shape across the sources is compact but strict: discover context, write a plan or spec, implement in small slices, verify behavior with concrete feedback, review the result, and save reusable lessons.

## Default Task Contract

For non-trivial work, the minimum contract should name:

- Objective: the user-visible behavior or knowledge outcome.
- Context: relevant files, wiki pages, raw sources, APIs, docs, or examples.
- Constraints: ownership boundaries, files not to touch, style rules, security limits, and compatibility requirements.
- Deliverables: code, docs, tests, screenshots, PR notes, wiki edits, or artifacts.
- Verification: exact tests/checks, browser paths, screenshots, lint/type/build commands, or manual review steps.
- Stop condition: what "done" means, what to report, and when to stop for human input.

Vox's prompt templates are useful because they encode this shape: role, goal, work surface, edge cases, expected artifacts, verification, review loop, and completion standard. The point is not magic wording; it is preventing under-specified autonomy.

## Spec-Driven Development

Zach Lloyd's pattern makes specs reviewable repo artifacts. A product spec captures user behavior and invariants; a tech spec maps implementation strategy, files, interfaces, and risks; a validation pass compares the final diff against both. For UX work, a visual/computer-use pass becomes part of acceptance.

Karpathy and David Breunig push the idea further: in small, well-scoped utilities, the spec plus language-agnostic tests can become the portable artifact while the implementation is generated locally. That pattern is promising for tiny internal tools, but weak for foundational dependencies that need performance, security updates, interoperability, complicated test matrices, and community maintenance.

## Prompt Contracts

Strong prompts should tell the agent how to think about the job, not just what to produce. For larger tasks, the prompt should ask the agent to discover first, state assumptions, identify risks, propose a plan, and only then implement. Outcome-biased prompts are risky for review; ask the agent to inspect evidence and report findings instead of insisting that a bug or conclusion must exist.

Prompt contracts should also preserve handoff quality. Thariq's implementation-notes pattern is useful here: the agent should leave a trace of design choices, deviations from plan, tests run, unresolved questions, and files touched. That makes review cheaper and future reruns less blind.

## Implementation Gates

Compound Engineering and Superpowers both treat planning, review, and learning as leverage, not bureaucracy. The strict version is: brainstorm first, get design signoff when the blast radius is high, create an isolated worktree where appropriate, break the work into small tasks, use red/green TDD when possible, run focused subagents for research or review, and verify before completion.

Matt Pocock's talks add the engineering-fundamentals warning: agents amplify both good and bad structure. Shared language, small interfaces, vertical slices, tests, and deep modules matter more because agents can quickly produce plausible but incoherent changes. Kiro's spec-driven workflow reconciles agent speed with product quality by turning requirements into acceptance criteria, properties, mocks, tasks, and verification artifacts.

## Review And Learning

Review should inspect the contract, not just the diff. Did the agent solve the intended behavior? Did it stay inside the file and safety boundaries? Did tests actually prove the risky paths? Did it leave behind enough state for the next agent?

The learning loop is the compounding part. If a run discovers a reusable local rule, create or update a skill, wiki page, test fixture, checklist, or AGENTS.md instruction. If the lesson is too narrow, keep it in the task notes. The rule of thumb: promote lessons that reduce future context load or prevent repeated mistakes.

## See Also

- [Agentic Engineering Practices](agentic-engineering-practices.md)
- [Context Engineering For Coding Agents](context-engineering-for-coding-agents.md)
- [Harness Engineering And Runtime Control](harness-engineering-and-runtime-control.md)
- [Agent Skill Libraries And Requirements](agent-skill-libraries-and-requirements.md)
- [AI Engineering Talks On Agentic Coding](ai-engineering-talks-on-agentic-coding.md)
