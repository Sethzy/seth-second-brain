---
type: wiki_article
title: Agent Goals And Dynamic Workflows
updated_at: 2026-06-10
status: draft
source_count: 5
tags:
  - codex
  - goals
  - agent-workflows
  - dynamic-workflows
---

# Agent Goals And Dynamic Workflows

> Sources: Thariq X Article, 2026-06-02; Dominik Kundel X Article, 2026-06-04; Matt Van Horn X Article, 2026-06-08; JUMPERZ X post, 2026-06-08; Seth pasted opportunity dump, 2026-06-10
> Raw: [Thariq dynamic workflows X Article](../../raw/intentional/x/2061907337154367865-trq212-a-harness-for-every-task-dynamic-workflows-in-claude-code-last-week-we-released-dyn.md); [Dominik Kundel guide to goal X Article](../../raw/intentional/x/2062650378089594955-dkundel-a-guide-to-goal-we-launched-the-goal-mode-or-goal-as-a-way-to-help-you-have-codex.md); [Matt Van Horn loop X Article](../../raw/intentional/x/2063865685558903149-mvanhorn-wtf-is-a-loop-peter-steinberger-vs-boris-cherny-the-most-repeated-sentence-in-ai.md); [JUMPERZ X post](../../raw/intentional/x/2063948602313965580-jumperz-peter-is-right-in-other-words-you-have-to-know-how-to-coordinate-and-give-the-righ.md); [first ingestion test](../../raw/intentional/pasted/2026-06-10-first-second-brain-ingestion-test-ai-gtm-opportunities-and-l.md)

## Overview

This cluster frames modern agent work as harness design, not better one-shot prompting. The JUMPERZ post treats `/goal` as an agent coordination primitive. Dominik Kundel's guide treats goals as concrete exit criteria for long-running Codex work. Thariq's dynamic workflows article shows Claude Code creating task-specific harnesses. Matt Van Horn's loop article connects the same pattern to repeated AI-coding debates: the expensive part is increasingly the loop around the model.

This is directly relevant to Seth Second Brain because the repo itself needs durable workflows: ingestion, exact source capture, wiki compilation, qmd refresh, maintenance, event/opportunity monitoring, and later automated sweeps. The second brain should not depend on remembering a perfect prompt; it should encode reusable loops that can be run, checked, and improved.

## Key Ideas

- A goal should be a durable execution loop around an objective, with verifiable exit criteria.
- Dynamic workflows are task-specific harnesses. The agent can create or adapt the harness when the default coding loop is too generic.
- Loops should decompose work, assign roles, coordinate dependencies, execute in order, review against the objective, gate before shipping, save what worked, and report only what matters.
- The value of `/goal` is less about producing a single long response and more about reducing the user's role as the bottleneck.
- Long-form agent work needs budgets, verification, and resumable state; otherwise the loop can burn tokens without improving outcomes.
- This applies beyond Codex: the same pattern can structure Claude Code, custom agent stacks, second-brain maintenance, research sweeps, and recurring operating loops.

## Open Questions

- What should Seth's default `/goal` template be for second-brain ingestion?
- Which recurring second-brain loops deserve first-class scripts: exact capture, X/LinkedIn monitoring, event monitoring, contracting pipeline review, or wiki maintenance?
- How should completed goal learnings get written back into `wiki/` versus `staging/maintenance/`?
- What verification gates prevent automated loops from quietly filling the corpus with low-quality material?

## Sources

- [Thariq dynamic workflows X Article](../../raw/intentional/x/2061907337154367865-trq212-a-harness-for-every-task-dynamic-workflows-in-claude-code-last-week-we-released-dyn.md)
- [Dominik Kundel guide to goal X Article](../../raw/intentional/x/2062650378089594955-dkundel-a-guide-to-goal-we-launched-the-goal-mode-or-goal-as-a-way-to-help-you-have-codex.md)
- [Matt Van Horn loop X Article](../../raw/intentional/x/2063865685558903149-mvanhorn-wtf-is-a-loop-peter-steinberger-vs-boris-cherny-the-most-repeated-sentence-in-ai.md)
- [JUMPERZ X post](../../raw/intentional/x/2063948602313965580-jumperz-peter-is-right-in-other-words-you-have-to-know-how-to-coordinate-and-give-the-righ.md)
- [First second-brain ingestion test](../../raw/intentional/pasted/2026-06-10-first-second-brain-ingestion-test-ai-gtm-opportunities-and-l.md)

## See Also

- [AI GTM Opportunity Leads](../gtm-sales/ai-gtm-opportunity-leads.md)
