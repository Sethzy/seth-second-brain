---
type: wiki_article
title: Agentic Engineering Practices
updated_at: 2026-07-03
status: draft
source_count: 12
tags:
  - agentic-engineering
  - context-engineering
  - verification
  - harness-engineering
  - task-contracts
---

# Agentic Engineering Practices

> Sources: sysls X Article, 2026-03-03; Alok Bishoyi X Article, 2026-05-27; Peter Wang X Article, 2026-06-11; Zach Lloyd X Article, 2026-06-11; Vox prompt-shaping X post, 2026-06-17; Sairahul harness engineering X Article, 2026-06-07; LangChain Deep Agents overview, 2026-06-12 capture; walkinglabs Awesome Harness Engineering selected set, 2026-06-13 capture; Garrett Lord evals X Article, 2026-06-25; AI Engineering Talks, 2026-06-12 batch; Geoffrey Litt X thread on agent-generated understanding tools, 2026-07-02 capture; Richard MacManus / Latent.Space interview with Pauline Brunet, 2026-07-01.
> Raw: [sysls world-class agentic engineer X Article](../../raw/intentional/x/2028814227004395561-systematicls-how-to-be-a-world-class-agentic-engineer-introduction-you-re-a-developer-you.md); [Alok Bishoyi autoresearch X Article](../../raw/intentional/x/2059610305408462898-alokbishoyi97-using-autoresearch-to-improve-harness-skills-with-detailed-example-run-self.md); [Peter Wang vertical-agent context hierarchy X Article](../../raw/intentional/x/2065190286519906657-brainsandtennis-building-a-good-vertical-agent-how-do-you-build-an-agent-that-actually-per.md); [Zach Lloyd spec-driven development X Article](../../raw/intentional/x/2065154860337508577-zachlloydtweets-three-skills-you-need-for-spec-driven-development-if-you-want-to-increase.md); [Vox prompt-shaping X post](../../raw/intentional/x/2067237707483337118-voxyz-ai-stop-telling-claude-code-codex-do-this-stop-telling-claude-code-codex-write-code.md); [Sairahul harness engineering X Article](../../raw/intentional/x/2063544956158185927-sairahul1-harness-engineering-what-every-ai-engineer-needs-to-know-in-2026-in-february-202.md); [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md); [Awesome Harness Engineering selected article resource set](../../raw/intentional/pasted/2026-06-13-awesome-harness-engineering-selected-article-resource-set.md); [Garrett Lord evals as strategic IP X Article](../../raw/intentional/x/2068754262440767500-garrettlord-evals-the-strategic-ip-that-will-define-the-next-era-of-ai-we-ve-spoken-to-hun.md); [OpenAI harness engineering talk](../../raw/intentional/youtube/2026-06-12-harness-engineering-how-to-build-software-when-humans-steer-agents-execu.md); [Geoffrey Litt agents can write code that helps humans understand code](../../raw/intentional/x/2026-07-02-geoffrey-litt-agents-can-write-code-that-helps-humans-unders.md); [How Cursor deploys AI inside the enterprise](../../raw/intentional/web/2026-07-03-how-cursor-deploys-ai-inside-the-enterprise.md)

## Overview

Agentic engineering is the discipline of making AI systems do useful work through bounded loops: clear task contracts, curated context, tool and permission boundaries, verification, and durable learning. The model matters, but the wrapper around the model is now a first-class engineering surface. Skills, rules, specs, evals, worktrees, sandboxes, memory files, and review gates can improve faster than model weights because they are editable local infrastructure.

For Seth, this page is now the router. Use it to choose which narrower page to open before a coding-agent task:

- [Agentic SDLC And Task Contracts](agentic-sdlc-and-task-contracts.md) - how to define work, prompt agents, gate implementation, review output, and fold lessons back into the repo.
- [Context Engineering For Coding Agents](context-engineering-for-coding-agents.md) - how to decide what goes into context, how to split research from implementation, and how to expose source systems without prompt bloat.
- [Harness Engineering And Runtime Control](harness-engineering-and-runtime-control.md) - how to design the control plane around agents: tools, permissions, sandboxes, evals, observability, and cross-model review.

## Seth Default Loop

The default AI-coding loop should be: discover -> plan -> implement -> verify -> review -> learn.

Discovery gathers source-grounded facts before design. Planning turns those facts into a contract: objective, constraints, files, edge cases, tests, screenshots, blocked conditions, and reporting requirements. Implementation should happen in small verified slices. Verification needs real feedback from tests, typechecks, lint, browser screenshots, CLI output, or deterministic reviewers. Review should inspect diffs, artifacts, and trace notes. Learning means updating skills, docs, source maps, or wiki pages when the task produced reusable operating knowledge.

This is not ceremony for its own sake. The practical point is to prevent long agent runs from becoming unreviewable drift. The stronger the context and verification loop, the more autonomy Seth can safely hand over.

Post-run learning artifacts are part of the loop. Geoffrey Litt's captured thread points to the useful move: the agent can generate code or artifacts that help the human understand other code. Seth's local `explain-diff-html` skill operationalizes this after a session: take a diff or PR, build a self-contained HTML lesson with system background, intuition, code walkthrough, diagrams, toy examples, and an interactive quiz. The artifact is not decoration; it is the review and teaching surface that keeps the human's mental model from lagging behind the agent's output.

Cursor's forward-deployed engineering interview adds a deployment-level version of this loop. Pauline Brunet frames enterprise AI coding as an "AI software factory": long-running agents should help across planning, design, PRD creation, demos, code, tests, review, production deployment, maintenance, and feedback intake. The important retrieval point is that agentic engineering stops being a personal productivity trick when the same agent process is standardized across teams, functions, and workflows. That requires leadership sponsorship, workflow champions, cloud agents for consistent execution, and FDEs who can work inside customer systems while feeding deployment lessons back into product.

## Key Principles

- Context is scarce. Keep global instructions small and route agents to only the rules, files, and sources relevant to the task.
- Task contracts beat one-line imperatives. Senior agents need role, goal, constraints, deliverables, edge cases, verification expectations, and a stop condition.
- Specs are control surfaces for intent and verification; they do not replace engineering judgment.
- Separate research from implementation when the implementation path is uncertain. Bad research can create hundreds of bad lines of code.
- Tools and permissions are part of the product surface. Narrow tools, scoped secrets, disposable sandboxes, and audit trails matter more as autonomy rises.
- Harness engineering is software engineering around the model: context delivery, middleware, tool lifecycle, state, memory, feedback loops, and human checkpoints.
- Evals should measure private workflow judgment, tool use, taste, and business outcomes, not only public benchmark performance.
- Cross-model review is useful when risk is high: a different model/runtime can expose blind spots a same-model reviewer may share.
- Durable learning compounds. Plans, review notes, skills, and wiki updates should make the next similar task easier.
- Review should include understanding, not only approval. A good post-run artifact teaches the diff back to Seth so he can explain, modify, and challenge it.
- Buy-versus-build is a first-order harness decision: use managed platforms when orchestration is not the advantage; build thin internal control planes only when proprietary context and workflow fit justify it.
- Enterprise rollout changes the unit of design from "one agent helps one developer" to "shared long-running agents run the same process across teams." That makes champions, cloud execution, measurable ROI, evals, and production-system tradeoff explanations part of the engineering discipline.

## My Take

Seth's most useful local stack is not a maximal agent framework. It is a small repo-native operating system: clear `AGENTS.md` routing, task contracts for non-trivial work, focused skills, source-grounded context retrieval, narrow tool permissions, deterministic validation, and periodic wiki cleanup. When the work gets serious, add cross-model review and a written post-run learning artifact. Tiny loop, sharp teeth.

## Open Questions

- What should Seth's minimal AGENTS.md router look like after this repo grows further?
- Should large tasks create a `TASK_CONTRACT.md` plus a scratch log by default?
- Should important PRs standardize on cross-model adversarial review?
- Which Second Brain workflow should become the first benchmarked self-improvement loop?
- Which internal source deserves the first context-provider wrapper: this repo, Gmail, Slack, Drive, CRM, or a GTM enrichment API?
- For Acme/Seth, is the next platform decision "plug into Devin/Codex" or "build a thin Inspect-like harness"?
- Which recurring Codex use-case prompts should become reusable Second Brain skills?
- Which proof-of-work project best demonstrates FDE readiness: an end-to-end production workflow with design decisions, customer-facing tradeoffs, measurable ROI, and evals?

## See Also

- [Agentic SDLC And Task Contracts](agentic-sdlc-and-task-contracts.md)
- [Context Engineering For Coding Agents](context-engineering-for-coding-agents.md)
- [Harness Engineering And Runtime Control](harness-engineering-and-runtime-control.md)
- [Agent Skill Libraries And Requirements](agent-skill-libraries-and-requirements.md)
- [AI Engineering Talks On Agentic Coding](ai-engineering-talks-on-agentic-coding.md)
- [Vendor Agentic Engineering Blogs, Last Six Months](vendor-agentic-engineering-blogs-2026.md)
- [Agent Framework Landscape](../agent-frameworks/agent-framework-landscape.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
