---
type: raw_capture
source_type: x
title: "Sunder sync: Codex Guidelines.md"
url: "https://steipete.me/posts/2025/shipping-at-inference-speed"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/04_Archive/Codex Guidelines.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "04_Archive/Codex Guidelines.md"
sha256: "04c4aa6bf9bd8902b0aed7c56237a5bd94a16a1241c779c3d2bbea32a61c70a5"
duplicate_of: ""
---

# Sunder sync: Codex Guidelines.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/04_Archive/Codex Guidelines.md`

Primary URL: https://steipete.me/posts/2025/shipping-at-inference-speed

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-19
tags: [guideline, ai-tools]
status: active
---

# Codex Guidelines

Reference material for using ChatGPT Codex effectively.

---

## Shipping at Inference Speed

**Source:** https://steipete.me/posts/2025/shipping-at-inference-speed

### Summary
Peter Steinberger documents how AI coding agents (particularly GPT-5.2 Codex) have transformed development workflow, enabling building software at unprecedented speeds with minimal manual code reading.

### Key Takeaways

**Model Performance:**
- Quality prompts produce working code immediately
- Codex excels at large refactors through deep file analysis (10-15 min reading before writing)
- GPT-5.2's knowledge cutoff (Aug 2024) provides advantage over Claude Opus

**Paradigm Shifts:**
- No longer reads most code—"watches the stream" and focuses on architecture/structure
- Moved away from "plan mode" → collaborative conversations where model explores and builds together
- Language/ecosystem and dependency selection remain highest-value decisions

### Best Practices

1. **Start with CLIs first** before UI—agents verify output efficiently
2. **Structure codebases for agent efficiency** rather than human readability
3. **Use documentation strategically**: maintain docs/*.md files for consistency
4. **Embrace linear development**: commit to main directly; ongoing refactoring
5. **Cross-reference existing solutions** across projects
6. **Pair images with minimal text** for UI iteration
7. **Configure appropriately**: increase token limits and auto-compact thresholds

### Critical Point
Agent-assisted development still requires understanding "where things are and how systems connect"—architectural thinking remains essential.

---

## OpenAI ExecPlans Framework

**Source:** https://cookbook.openai.com/articles/codex_exec_plans

### Summary
ExecPlans are comprehensive design documents enabling Codex to tackle multi-hour, complex tasks. One case: "seven hours from a single prompt."

### Core Principles

**Self-Containment:** Plans must include all knowledge needed—no external references

**Living Documents:** Continuous updates required. "It should always be possible to restart from only the ExecPlan."

**Observable Outcomes:** Success = demonstrable behavior, not mere code changes

### Essential Sections

Every ExecPlan needs:
- **Progress:** Timestamped checkbox tracking
- **Surprises & Discoveries:** Unexpected findings with evidence
- **Decision Log:** Rationale for changes
- **Outcomes & Retrospective:** Lessons and remaining work

### Best Practices

- Define terminology in plain language immediately
- Prioritize user-visible effects over implementation details
- Include concrete test commands and expected transcripts
- Write prose-first narratives (not checklists except Progress)
- Provide recovery paths for risky operations
- Validate comprehensively before completion

### Philosophy
"A single, stateless agent—or human novice—can read your ExecPlan from top to bottom and produce a working, observable result."

---

## Dual-Agent Workflow: Codex + Claude Code

**Source:** https://x.com/alexfinn/status/2012653446349131953

### Setup
- **Left screen:** Codex 5.2 xhigh
- **Right screen:** Claude Code Opus 4.5

### Workflow

1. **Start with Claude Code in plan mode** — let it design the approach
2. **Validate plans with Codex** — copy/paste every plan, get critical feedback, feed back to CC
3. **Use Codex to fix CC mistakes** — when Claude messes up, have Codex diagnose and fix
4. **Cross-review all changes** — every change either agent makes, have the other review it
5. **Let the cleaner win** — primarily use whichever agent is last to clean up the other's mess

### Benefits
- 10x faster app production
- Feels like managing a team of engineers
- Each agent catches the other's blind spots

