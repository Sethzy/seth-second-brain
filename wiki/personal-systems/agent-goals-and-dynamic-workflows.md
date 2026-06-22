---
type: wiki_article
title: Agent Goals And Dynamic Workflows
updated_at: 2026-06-12
status: draft
source_count: 21
tags:
  - codex
  - goals
  - agent-workflows
  - dynamic-workflows
---

# Agent Goals And Dynamic Workflows

> Sources: Thariq X Article, 2026-06-02; Dominik Kundel X Article, 2026-06-04; Matt Van Horn X Article, 2026-06-08; JUMPERZ X post, 2026-06-08; Seth pasted opportunity dump, 2026-06-10; OpenAI Cookbook, 2026-06-10 capture; Vaibhav Srivastav X posts, 2026-05-23 and 2026-05-24; ECC README, 2026-06-10 capture; Seth pasted agent workflow batch, 2026-06-10; Alok Bishoyi X Article, 2026-05-27; sysls X Article, 2026-03-03; Jason Liu Codex-maxxing, 2026-05-10; Thariq implementation-notes X post, 2026-05-18; Linas Beliunas X post, 2026-05-19; Seth pasted Codex maxxing/GTM bundle, 2026-06-10; Lance Martin X post, 2026-05-13; Joao Moura X post, 2026-05-17; Lance Martin loop design X Article, 2026-06-09; Addy Osmani loop engineering X Article, 2026-06-08; Sairahul loops X Article, 2026-06-09
> Raw: [Thariq dynamic workflows X Article](../../raw/intentional/x/2061907337154367865-trq212-a-harness-for-every-task-dynamic-workflows-in-claude-code-last-week-we-released-dyn.md); [Dominik Kundel guide to goal X Article](../../raw/intentional/x/2062650378089594955-dkundel-a-guide-to-goal-we-launched-the-goal-mode-or-goal-as-a-way-to-help-you-have-codex.md); [Matt Van Horn loop X Article](../../raw/intentional/x/2063865685558903149-mvanhorn-wtf-is-a-loop-peter-steinberger-vs-boris-cherny-the-most-repeated-sentence-in-ai.md); [JUMPERZ X post](../../raw/intentional/x/2063948602313965580-jumperz-peter-is-right-in-other-words-you-have-to-know-how-to-coordinate-and-give-the-righ.md); [first ingestion test](../../raw/intentional/pasted/2026-06-10-first-second-brain-ingestion-test-ai-gtm-opportunities-and-l.md); [OpenAI Cookbook Goals notebook](../../raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex.md); [VB repeated workflows X post](../../raw/intentional/x/2058315996260102376-reach-vb-copy-and-paste-this-into-your-codex-look-through-my-recent-codex-sessions-and-ide.md); [VB self-improvement loop X post](../../raw/intentional/x/2058538305872949490-reach-vb-update-came-up-with-an-even-better-version-of-this-prompt-after-the-feedback-ask.md); [ECC README](../../raw/intentional/web/2026-06-10-ecc-readme.md); [agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md); [Alok Bishoyi autoresearch X Article](../../raw/intentional/x/2059610305408462898-alokbishoyi97-using-autoresearch-to-improve-harness-skills-with-detailed-example-run-self.md); [sysls world-class agentic engineer X Article](../../raw/intentional/x/2028814227004395561-systematicls-how-to-be-a-world-class-agentic-engineer-introduction-you-re-a-developer-you.md); [Jason Liu Codex-maxxing](../../raw/intentional/web/2026-06-10-jason-liu-codex-maxxing.md); [Thariq implementation-notes X post](../../raw/intentional/x/2056418157305454805-trq212-okay-this-is-going-kinda-viral-and-tbh-my-original-text-was-kind-of-messy-so-here-s.md); [Linas Beliunas AI operating system X post](../../raw/intentional/x/2056679329484927356-linasbeliunas-can-t-believe-anthropic-just-quietly-dropped-a-founder-playbook-for-building.md); [Codex maxxing and GTM agent opportunity bundle](../../raw/intentional/pasted/2026-06-10-codex-maxxing-and-gtm-agent-opportunity-bundle.md); [Lance Martin Outcomes/Dreaming X post](../../raw/intentional/x/2053906836181668241-rlancemartin-self-verification-outcomes-self-learning-dreaming-are-two-of-the-most-interes.md); [Joao Moura Iris self-improvement X post](../../raw/intentional/x/2055317550326776264-joaomdmoura-we-let-an-ai-agent-rewrite-its-own-code-in-production-it-s-been-running-with-o.md); [Lance Martin loop design X Article](../../raw/intentional/x/2064397389189071163-rlancemartin-designing-loops-with-fable-5-mythos-class-models-like-claude-fable-5-have-cha.md); [Addy Osmani loop engineering X Article](../../raw/intentional/x/2064127981161959567-addyosmani-loop-engineering-loop-engineering-is-replacing-yourself-as-the-person-who-promp.md); [Sairahul loops X Article](../../raw/intentional/x/2064277888216555684-sairahul1-loops-what-every-ai-engineer-needs-to-know-in-2026-peter-steinberger-creator-of.md)

## Overview

This cluster frames modern agent work as harness design, not better one-shot prompting. The JUMPERZ post treats `/goal` as an agent coordination primitive. Dominik Kundel's guide and the OpenAI Cookbook treat goals as concrete exit criteria for long-running Codex work. Thariq's dynamic workflows article shows Claude Code creating task-specific harnesses. Matt Van Horn's loop article connects the same pattern to repeated AI-coding debates: the expensive part is increasingly the loop around the model.

This is directly relevant to Seth Second Brain because the repo itself needs durable workflows: ingestion, exact source capture, wiki compilation, qmd refresh, maintenance, event/opportunity monitoring, and later automated sweeps. The second brain should not depend on remembering a perfect prompt; it should encode reusable loops that can be run, checked, and improved.

The newer sources add a self-improvement layer. VB's prompts ask Codex to look across recent sessions, memories, rollout summaries, existing skills, custom agents, and automations, then package only repeated, high-confidence work into the smallest useful form. ECC is a broader open-source example of the same instinct: cross-harness skills, agents, hooks, memory, verification, and continuous learning wrapped into an operator system.

Alok's autoresearch example makes the self-improvement loop more explicit: define "better," build or reuse a benchmark, run parallel experiments against editable harness files, gate against cheating or regressions, and keep the best-scoring skill/prompt/config with an audit trail. The sysls article adds a caution: avoid context bloat, keep global rules small, and prefer fresh sessions per well-specified contract.

Jason Liu's Codex-maxxing article gives this a user-facing operating model: durable threads, voice input, steering, memory, browser/computer use, mobile/remote control, Heartbeats, goals, and side-panel artifact review. Thariq's implementation-notes prompt turns the same idea into a concrete scratch-log: while implementing a spec, maintain an `implementation-notes.html` that records ambiguous design decisions, deviations, tradeoffs, and open questions.

Linas Beliunas's AI operating-system post adds a founder/startup lens: AI compresses execution, but judgment about what not to build, which customer signal is real, and where scope creep hides becomes more important.

Lance Martin and Joao Moura add two signs that the loop is moving from "run a task" toward "maintain an agent system." Lance's note names self-verification through outcomes and self-learning through dreaming as interesting Claude-style features. Moura's Iris example describes a production agent that receives tasks through Slack, uses memory/skills/flows, opens PRs, observes review feedback, and feeds repeated patterns back into the agent's operating system.

The newer loop-engineering captures sharpen the same idea into an operating model. Addy Osmani argues that the leverage point has moved from manually prompting the agent to designing a loop that finds work, hands it out, checks it, records state, and decides the next run. Sairahul breaks the loop into discovery, planning, execution, verification, and iteration, while warning that open-ended loops become token-expensive quickly and should usually start as closed loops with clear scopes. Lance Martin adds a practical reliability pattern: use independent verifier or grader contexts and cross-session memory so the same model that produced work is not the only judge of completion.

## Key Ideas

- A goal should be a durable execution loop around an objective, with verifiable exit criteria.
- Dynamic workflows are task-specific harnesses. The agent can create or adapt the harness when the default coding loop is too generic.
- Loops should decompose work, assign roles, coordinate dependencies, execute in order, review against the objective, gate before shipping, save what worked, and report only what matters.
- The value of `/goal` is less about producing a single long response and more about reducing the user's role as the bottleneck.
- Long-form agent work needs budgets, verification, and resumable state; otherwise the loop can burn tokens without improving outcomes.
- This applies beyond Codex: the same pattern can structure Claude Code, custom agent stacks, second-brain maintenance, research sweeps, and recurring operating loops.
- Good Goals define the outcome, verification surface, constraints, boundaries, progress reporting, and blocked condition before the agent starts.
- Completion should be evidence-based: files, tests, logs, benchmark output, generated artifacts, source captures, or another concrete audit surface.
- Repeated work should be packaged only when it has stable inputs, a repeatable procedure, a clear output or stopping condition, and enough evidence that it will recur.
- The smallest useful package matters: use a skill for a reusable workflow, a custom subagent for a bounded role or investigation task, an automation for a recurring check, and skip speculative or overlapping assets.
- Bigger refactors and long-running goals should maintain a scratch-log of decisions, tradeoffs, review fixes, and underspecified assumptions so future reviews can recover the reasoning trail.
- Self-improving harness work needs a benchmark, isolated workspaces, parallel hypotheses, score tracking, and anti-cheating gates.
- Long-running automation should usually be decomposed into contracts and fresh sessions instead of one giant session that accumulates unrelated context.
- Codex-maxxing is an operating loop, not a bag of features: keep work in durable threads, feed it richer context through voice and memory, steer after tool calls, inspect artifacts in-place, and use recurring Heartbeats where work should keep checking for changes.
- Scratch-log artifacts should be part of large implementation prompts. The artifact can be HTML or markdown, but it should explicitly capture decisions, deviations, tradeoffs, and unresolved questions while the work is happening.
- Agent systems improve when review feedback, successful flows, and repeated failure modes are promoted into memory, skills, workflows, or evals instead of remaining trapped in a single run transcript.
- Self-verification should be explicit enough to audit: define the expected outcome, observe whether it happened, and preserve enough evidence to decide whether the agent learned the right lesson.
- Loop engineering means the human designs the recurring system that prompts agents, rather than manually prompting every turn.
- Practical loops need discovery triggers, plans, execution slots, independent verification, memory/state, and cost controls.
- Closed loops with explicit scopes, tests, and verifier contexts are the current pragmatic default; open-ended loops are powerful but can burn budget and drift.

## Open Questions

- What should Seth's default `/goal` template be for second-brain ingestion?
- Which recurring second-brain loops deserve first-class scripts: exact capture, X/LinkedIn monitoring, event monitoring, contracting pipeline review, or wiki maintenance?
- How should completed goal learnings get written back into `wiki/` versus `staging/maintenance/`?
- What verification gates prevent automated loops from quietly filling the corpus with low-quality material?
- What should the default scratch-log file name and retention policy be for large Codex refactors?
- Should Seth run a monthly "package repeated workflows" review across Codex sessions and this repo's wiki/log?
- Which recurring personal loop should become the first closed-loop automation: source capture triage, wiki lint, CI-failure summaries, or stale-source review?

## Sources

- [Thariq dynamic workflows X Article](../../raw/intentional/x/2061907337154367865-trq212-a-harness-for-every-task-dynamic-workflows-in-claude-code-last-week-we-released-dyn.md)
- [Dominik Kundel guide to goal X Article](../../raw/intentional/x/2062650378089594955-dkundel-a-guide-to-goal-we-launched-the-goal-mode-or-goal-as-a-way-to-help-you-have-codex.md)
- [Matt Van Horn loop X Article](../../raw/intentional/x/2063865685558903149-mvanhorn-wtf-is-a-loop-peter-steinberger-vs-boris-cherny-the-most-repeated-sentence-in-ai.md)
- [JUMPERZ X post](../../raw/intentional/x/2063948602313965580-jumperz-peter-is-right-in-other-words-you-have-to-know-how-to-coordinate-and-give-the-righ.md)
- [First second-brain ingestion test](../../raw/intentional/pasted/2026-06-10-first-second-brain-ingestion-test-ai-gtm-opportunities-and-l.md)
- [OpenAI Cookbook Goals notebook](../../raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex.md)
- [VB repeated workflows X post](../../raw/intentional/x/2058315996260102376-reach-vb-copy-and-paste-this-into-your-codex-look-through-my-recent-codex-sessions-and-ide.md)
- [VB self-improvement loop X post](../../raw/intentional/x/2058538305872949490-reach-vb-update-came-up-with-an-even-better-version-of-this-prompt-after-the-feedback-ask.md)
- [ECC README](../../raw/intentional/web/2026-06-10-ecc-readme.md)
- [Agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md)
- [Alok Bishoyi autoresearch X Article](../../raw/intentional/x/2059610305408462898-alokbishoyi97-using-autoresearch-to-improve-harness-skills-with-detailed-example-run-self.md)
- [sysls world-class agentic engineer X Article](../../raw/intentional/x/2028814227004395561-systematicls-how-to-be-a-world-class-agentic-engineer-introduction-you-re-a-developer-you.md)
- [Jason Liu Codex-maxxing](../../raw/intentional/web/2026-06-10-jason-liu-codex-maxxing.md)
- [Thariq implementation-notes X post](../../raw/intentional/x/2056418157305454805-trq212-okay-this-is-going-kinda-viral-and-tbh-my-original-text-was-kind-of-messy-so-here-s.md)
- [Linas Beliunas AI operating system X post](../../raw/intentional/x/2056679329484927356-linasbeliunas-can-t-believe-anthropic-just-quietly-dropped-a-founder-playbook-for-building.md)
- [Codex maxxing and GTM agent opportunity bundle](../../raw/intentional/pasted/2026-06-10-codex-maxxing-and-gtm-agent-opportunity-bundle.md)
- [Lance Martin Outcomes/Dreaming X post](../../raw/intentional/x/2053906836181668241-rlancemartin-self-verification-outcomes-self-learning-dreaming-are-two-of-the-most-interes.md)
- [Joao Moura Iris self-improvement X post](../../raw/intentional/x/2055317550326776264-joaomdmoura-we-let-an-ai-agent-rewrite-its-own-code-in-production-it-s-been-running-with-o.md)
- [Lance Martin loop design X Article](../../raw/intentional/x/2064397389189071163-rlancemartin-designing-loops-with-fable-5-mythos-class-models-like-claude-fable-5-have-cha.md)
- [Addy Osmani loop engineering X Article](../../raw/intentional/x/2064127981161959567-addyosmani-loop-engineering-loop-engineering-is-replacing-yourself-as-the-person-who-promp.md)
- [Sairahul loops X Article](../../raw/intentional/x/2064277888216555684-sairahul1-loops-what-every-ai-engineer-needs-to-know-in-2026-peter-steinberger-creator-of.md)

## See Also

- [AI GTM Opportunity Leads](../gtm-sales/ai-gtm-opportunity-leads.md)
- [Agentic Classifiers](../ai-knowledge-work/agentic-classifiers.md)
- [Browser Outreach Delegation](../scraping-revops/browser-outreach-delegation.md)
- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Personal Agent Ops Stack](personal-agent-ops-stack.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
