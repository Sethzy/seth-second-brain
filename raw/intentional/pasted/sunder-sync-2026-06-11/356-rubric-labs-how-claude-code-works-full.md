---
type: raw_capture
source_type: web
title: "Sunder sync: rubric-labs-how-claude-code-works-FULL.md"
url: "https://rubriclabs.com/blog/how-does-claude-code-work"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/rubric-labs-how-claude-code-works-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/rubric-labs-how-claude-code-works-FULL.md"
sha256: "db98051f93118ddc5ae9d6d7e62903dd4f76570f8529c9a1d4b6a7d0ad9f7b3c"
duplicate_of: ""
---

# Sunder sync: rubric-labs-how-claude-code-works-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/rubric-labs-how-claude-code-works-FULL.md`

Primary URL: https://rubriclabs.com/blog/how-does-claude-code-work

Duplicate of existing source-map entry: `none`

## Capture Text

# How does Claude Code actually work?

**Source:** Rubric Labs Blog
**Author:** Sarim Malik
**Date:** February 10, 2026
**URL:** https://rubriclabs.com/blog/how-does-claude-code-work

---

## Summary

A first-principles breakdown of Claude Code's architecture — the gather/act/verify loop, tool design, context window management, sub-agent orchestration via Task, and why the terminal environment is the key ingredient.

---

## Key Concepts

### The Core Loop: Gather → Act → Verify

Claude Code runs a tight agentic loop that alternates between three phases:

1. **Gather (read)** — Read files, find relevant code, pull in just enough evidence to choose the next step.
2. **Act (write)** — Make the change: edit code, write files, or run a command to move the task forward.
3. **Verify (test)** — Confirm it worked: inspect changes, check errors, and run tests until the evidence is clean.

The loop stretches or shrinks based on the task. A small request might complete in a few steps. A bigger request loops until it's solid.

### The Agent Harness

An **agent harness** is the runtime layer around a language model that lets it call tools safely, keep working state, and take actions in an environment. In Claude Code, that execution environment is your filesystem, terminal commands, and test tooling.

Most of the practical value comes from the harness layer, not just the base model.

### Autonomy Spectrum

- **Autocomplete:** suggests the next lines
- **Copilot:** helps draft and edit, but you still run commands and verify outcomes
- **Agent:** can run the loop against a real project by using tools and feeding results back into context

Claude Code sits near the agentic end — terminal-native, strongly harnessed, and opinionated about verification (tests, diffs, builds), while still asking for explicit approval on risky actions.

---

## The Core System (Single Request Flow)

```
Context Window (200K) → Decide → Tool Call → Result → Context (updated) → Repeat
```

1. **Start state:** your request + current context window (system instructions, prior messages, recent tool results)
2. **Decision:** the model reads that state and chooses the next move — answer now or call a tool to reduce uncertainty
3. **Execution:** tools run in the terminal environment and return results
4. **Update:** results appended back into context window, loop repeats until Claude can stop confidently

---

## Model Tiers

| Model | Best For | Notes |
|-------|----------|-------|
| **Sonnet** (default) | 80% of coding tasks — file navigation, straightforward edits, test runs | Right call for most work |
| **Opus** | Reasoning-heavy — architecture, debugging race conditions, multi-file refactors, migrations | Slower/costlier but fewer dumb mistakes on complex tasks. Rubric uses as daily driver — fewer loops and less rework |
| **Haiku** | Fast/cheap grep-like tasks or simple lookups | Loses nuance, not great for multi-step reasoning |
| **Extended thinking** | Any tier, genuinely hard problems | More compute before responding — longer internal chains of thought, more self-correction |

Current state of the art: **Sonnet 4.5** and **Opus 4.6**.

---

## Context Window: What Claude Code Sees

Contents of the window:
- **System instructions** — rules of the tool + project rules (CLAUDE.md)
- **Conversation history** — your messages and Claude's responses
- **Tool results** — file contents, search results, terminal output, diffs, failing tests
- **Loaded skills and tool definitions** — extra capabilities

All current models have **200K token** context. When the window fills up, Claude Code manages it automatically:
1. Clears older tool outputs first
2. Summarizes conversation if needed
3. Latest request usually survives, but early details can disappear

This process is called **context compaction**. Persistent rules belong in CLAUDE.md.

---

## Tools: The Building Blocks

### Three Buckets

| Bucket | Tools | Purpose |
|--------|-------|---------|
| **Workspace** | Read, Write, Edit, Glob, Grep, Bash | Inspect codebase + make changes |
| **Web** | WebSearch, WebFetch | Pull external context |
| **Interaction** | AskUserQuestion | Get unstuck via multiple-choice questions |

### Core Tools by Phase

| Tool | What it does | Phase |
|------|-------------|-------|
| AskUserQuestion | Asks multiple-choice questions to gather requirements or clarify ambiguity | Gather |
| Bash | Executes shell commands in your environment | Action, Verify |
| Edit | Makes targeted edits to specific files | Action |
| Glob | Finds files based on pattern matching | Gather, Verify |
| Grep | Searches for patterns in file contents | Gather, Verify |
| Read | Reads the contents of files | Gather, Verify |
| WebFetch | Fetches content from a specified URL | Gather, Verify |
| WebSearch | Performs web searches with domain filtering | Gather, Verify |
| Write | Creates or overwrites files | Action |

### Supporting Tools
- **Orchestration:** Task, TaskList, TaskOutput
- **Integrations:** MCP for tool discovery and loading
- **Editing:** NotebookEdit for notebooks, LSP for language-server code intelligence
- **Control:** ExitPlanMode, KillShell for session management

---

## Task: Sub-Agent Orchestration

A **Task** spins up a sub-agent — a separate, focused agent instance with its own context window that does one scoped unit of work and returns a condensed result to the main agent.

### Three Benefits:
1. **Context isolation** — sub-agent keeps its own context, deep exploration doesn't pollute the main thread
2. **Parallelism** — multiple sub-agents run at once (find files, check tests, review diffs), then merge outcomes
3. **Tool scoping** — sub-agents can be restricted to smaller tool sets (read-only review, test runner), reducing risk

Mental model: main agent stays in charge of the narrative and final decision. Sub-agents are disposable workers that hand back a result the same way a tool returns output.

---

## Tool Interface Design Principles

Claude Code works because **tool interfaces are constrained**. A good tool is a small contract with clear inputs, bounded scope, and outputs the agent can trust.

### Text Editor Example
- Limited to a small command set: view, create, insert, str_replace
- `str_replace` requires an exact match (including whitespace) — surgically targeted
- **Fails loudly** — if the old snippet doesn't exist or appears multiple times, returns an error
- Forces the agent back into gather phase — exactly what you want when a change would be ambiguous

### Key Tool Design Insights
- **Bash:** Commands run in YOUR environment — verification becomes factual (run tests, check diffs)
- **Web tools:** WebSearch for freshness/citations, WebFetch pulls full pages
- The model proposes a small next step → tool layer turns it into **evidence or a clear error**

---

## Terminal as an Environment

The terminal creates a **clean permission boundary**:
- Claude inherits whatever your shell user can do
- Every meaningful action routes through explicit tool calls you can audit, constrain, or deny
- Interacts with the same primitives you already trust: files, diffs, tests, commands

> The same agent in a generic cloud environment is often less effective. Without your project's existing scripts, linters, and build/test commands, taking action becomes guesswork and verifying becomes weak. Claude Code feels strong because the environment provides the primitives, and the model composes them.

---

## Key Takeaways

1. **Agent quality is mostly about clear contracts** — tight tool interfaces, bounded outputs, and fail-loudly behavior that turns intent into evidence inside real workflows
2. **The harness matters more than the model** — the better the harness, the dumber the model can be
3. **Scalable via sub-agents** — break work into parallel sub-tasks via Task, pull back condensed results, let context compaction keep the main thread focused
4. **Terminal = power** — the environment provides the primitives, the model composes them
5. **Future direction** — agents will run longer, coordinate more parallel work, and take on larger end-to-end slices as tool ecosystems mature and permissioning/verification get stronger

---

## Relevance to RE AI CRM

- Validates our "harness > model" philosophy — Claude Agent SDK inside E2B sandbox IS the harness
- The gather/act/verify loop maps directly to how our sandbox agent should operate
- Sub-agent pattern (Task) = exactly what we do with subagents to protect main context from bloat
- Tool design principles (constrained, fail-loudly) should guide our custom tool interfaces
- Context compaction is why CLAUDE.md/persistent rules matter — early details can disappear

