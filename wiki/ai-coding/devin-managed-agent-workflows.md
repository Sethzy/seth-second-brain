---
type: wiki_article
title: Devin Managed Agent Workflows
updated_at: 2026-06-12
status: draft
source_count: 4
tags:
  - devin
  - cognition
  - coding-agents
  - managed-agents
  - review-loops
  - playbooks
---

# Devin Managed Agent Workflows

> Sources: Cognition Team, 2025-06-27; Cognition Team, 2026-02-10; Cognition Team, 2026-02-27.
> Raw: [How Cognition Uses Devin to Build Devin](../../raw/intentional/web/2026-06-12-cognition-how-cognition-uses-devin-to-build-devin.md); [Closing the Agent Loop: Devin Autofixes Review Comments](../../raw/intentional/web/2026-06-12-cognition-closing-the-agent-loop-devin-autofixes-review-comments.md); [Cognition Coding Agents 101 pointer](../../raw/intentional/web/2026-06-12-cognition-coding-agents-101-the-art-of-actually-getting-things-done-pointer.md); [Devin Coding Agents 101 guide](../../raw/intentional/web/2026-06-12-devin-coding-agents-101-the-art-of-actually-getting-things-done.md)

## Overview

These Cognition/Devin captures are one of the strongest managed-agent counterweights to custom harness building. They show Devin not just as a web app, but as a cloud agent platform embedded across web, Slack, Linear/Jira, CLI, API, PR review, code search, DeepWiki, playbooks, MCPs, session insights, and automated triggers.

The throughline is that autonomous coding works best when the agent is treated like a teammate with context, access, feedback loops, and repeatable procedures. Humans still own correctness and judgment, but the platform absorbs more of the mechanical engineering loop: scoping, investigation, PR creation, review, autofix, CI/test/lint remediation, documentation updates, and recurring operational tasks.

## Captured Sources

### How Cognition Uses Devin to Build Devin

Cognition says it has used Devin to build Devin from the beginning, and reports a week with 659 Devin PRs merged into its own codebase. The article describes Devin as a multi-surface work platform: a teammate can tag Devin in Slack, Linear, Jira, the web app, CLI, or API depending on where the work starts.

The operational stack is broad:

- Core conversational tasking across repositories.
- Ask Devin for codebase Q&A and task scoping before starting sessions.
- Automated code review through Devin Review, including organized diffs, copy/move detection, Bug Catcher annotations, and codebase-aware PR chat.
- Design-system enforcement through human-spotted Slack screenshots plus automatic detection.
- Bug triage from Linear tickets, with Datadog MCP/log context.
- End-to-end bug debugging with logs, read-only database access, git-history tracing, regression tests, and PRs.
- DANA for database analysis, dashboards, SQL, and ad hoc data questions.
- DeepWiki indexing for architecture diagrams, source links, and codebase summaries.
- Playbooks for repeated tasks, including desired outcome, steps, postconditions, priors to correct, forbidden actions, and required context.
- MCP Marketplace connections for Sentry, Datadog, Vercel, Notion, Airtable, Linear, databases, and other tools.
- Session Insights to analyze completed sessions, summarize challenges, suggest action items, and generate improved prompts for future sessions.
- REST API triggers from crash logs, bug reports, deployment failures, and review requests.

This makes Devin a managed agent platform, not just a coding chat interface. The strong pattern is "work arrives wherever the team already is; Devin scopes, executes, reviews, and learns from the session."

### Closing the Agent Loop

The autofix article describes a tighter write-catch-fix-merge loop. When a GitHub bot comments on a PR, whether from a linter, CI, security scanner, or dependency manager, Devin can automatically pick up the comment and fix it. Cognition frames this as closing the loop between the coding agent and the bug catcher.

The important distinction is between a coding agent as a tool and a coding agent plus review agent plus bot-triggered autofix as a system. One agent writes, another reviews, bot triggers expose mechanical issues, and Devin applies fixes back into the PR before human review.

The human role narrows toward architecture, product direction, domain edge cases, and final judgment. Mechanical issues such as lint failures, missed null checks, and off-by-one bugs should be caught and fixed before the reviewer spends attention.

### Coding Agents 101

The Cognition blog URL is a pointer to the substantive `devin.ai/agents101` guide, which is product-aware but broadly useful for any coding agent.

The guide's strongest advice:

- Tell agents how to do the work, not just what to accomplish.
- Point agents to where they should start: repo, docs, files, components, and relevant context.
- Practice defensive prompting by preempting likely confusion.
- Give agents CI, tests, types, linters, browser access, and instructions for running common checks.
- Use human expertise for verification; ownership remains with the engineer.
- Delegate quick wins, chores, documentation, analysis prototypes, and competing implementation options.
- Use preview deployments for frontend review.
- Break large tasks into smaller independent sessions.
- Use planning/search modes or codebase search before launching expensive work.
- Save testing procedures and repeated instructions into memory/playbooks.
- Use agent-triggering workflows from Slack, GitHub, Linear/Jira, CLI, API, and MCP-connected systems.
- Teach the agent architecture, conventions, test strategy, important commands, and preferred tools through knowledge files.

The guide's closing point is important for Seth's state-of-the-art framing: software engineers are not disappearing. Deep codebase knowledge, technical ownership, verification, and judgment matter more as agents make parallel execution possible.

## Key Ideas

- Devin represents the "buy the code factory" path: managed cloud execution, codebase indexing, review surfaces, playbooks, MCPs, API triggers, and session analytics as one platform.
- The managed-agent loop is broader than implementation: scope, investigate, execute, review, autofix, test, update docs, analyze sessions, and improve future prompts/playbooks.
- Treat agents like teammates: give context, conventions, tools, memory, feedback, and clear task boundaries.
- Agent effectiveness scales with specificity. Well-scoped tasks with explicit criteria outperform vague requests.
- Review loops should compound. A review agent or bot comment is more valuable when it can trigger an automatic fix and feed the result back into the PR.
- Playbooks are Devin's version of durable skills: repeated work becomes a reusable prompt/procedure with outcome, steps, postconditions, corrected priors, forbidden actions, and required context.
- Session insights are the learning loop: completed work should reveal technical problems, communication gaps, scope creep, efficiency bottlenecks, and improved future prompts.
- MCP and API access turn Devin from an app into an automation surface: Sentry/Datadog/Vercel logs, databases, Linear/Jira, Slack, Notion, and deployment failures can all start or enrich sessions.
- Humans still own architecture, product intent, risk, and final correctness.

## My Take

For Seth, these sources justify a practical fork in the AI-coding strategy. If the task is ordinary software throughput, a managed platform like Devin/Codex may be the right default. If the advantage is proprietary context, custom verification, or a unique work surface, then a thin internal harness is worth considering. Either way, the target loop is the same: clear context, specific task contracts, tests and preview environments, review agents, autofixable mechanical feedback, and durable playbooks/skills.

## Open Questions

- Which Seth/Acme tasks should be sent to managed cloud agents versus kept in local Codex/Claude workflows?
- Should Devin-style playbooks become the vocabulary for repeated coding work alongside Codex skills and Superpowers tasks?
- What would a minimal "autofix review comments" loop look like in this repo using Codex, GitHub comments, lint/test output, and source-map/wiki validation?
- Should this Second Brain use session-insight summaries after large agent runs to improve prompts, skills, and wiki maintenance rules?

## Sources

- [How Cognition Uses Devin to Build Devin](../../raw/intentional/web/2026-06-12-cognition-how-cognition-uses-devin-to-build-devin.md)
- [Closing the Agent Loop: Devin Autofixes Review Comments](../../raw/intentional/web/2026-06-12-cognition-closing-the-agent-loop-devin-autofixes-review-comments.md)
- [Cognition Coding Agents 101 pointer](../../raw/intentional/web/2026-06-12-cognition-coding-agents-101-the-art-of-actually-getting-things-done-pointer.md)
- [Devin Coding Agents 101 guide](../../raw/intentional/web/2026-06-12-devin-coding-agents-101-the-art-of-actually-getting-things-done.md)

## See Also

- [Agentic Engineering Practices](agentic-engineering-practices.md)
- [AI Engineering Talks On Agentic Coding](ai-engineering-talks-on-agentic-coding.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
