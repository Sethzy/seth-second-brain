---
type: wiki_article
title: Workflow Hustle While Job Hunting
updated_at: 2026-06-15
status: draft
source_count: 1
tags:
  - workflow-hustle
  - vertical-agents
  - job-search
  - proof-of-work
  - hermes
  - tenant-isolation
---

# Workflow Hustle While Job Hunting

> Sources: Seth pasted vertical-agent startup note, 2026-06-15
> Raw: [vertical AI agent startup and workflow hustle note](../../raw/intentional/pasted/2026-06-15-vertical-ai-agent-startup-and-workflow-hustle-while-job-hunt.md)

## Overview

This page is the working lane for Seth's idea of building small, useful workflow businesses while applying for jobs. The core move is not to start with a broad SaaS product. Start with one painful workflow in a boring vertical, do the work manually, document every step and edge case, then gradually turn the repeatable parts into agent skills, automations, dashboards, and customer-specific execution environments.

The job-search angle matters. These workflow experiments should produce both possible revenue and proof-of-work artifacts: concrete workflow maps, raw customer conversations, schemas, before/after operating details, demos, pricing logic, and lessons about deployment. If a workflow does not become a business, it can still become evidence for operator, GTM, product, AI workflow, or solutions roles.

## Operating Thesis

The source's strongest pattern is: be the agent before building the agent. That means manually doing the painful workflow first, using the manual run to discover edge cases, then productizing only the parts that repeat across users.

The workflow-hustle version is deliberately small:

- Pick a boring, painful workflow where the buyer already understands the value of completion.
- Talk to people who do the workflow every day before building.
- Map tools, spreadsheets, calls, approvals, documents, emails, and failure modes.
- Do a concierge/manual version for a first user or customer.
- Use Codex, Claude Code, Hermes, Composio, and a markdown knowledge base to turn repeated moves into skills.
- Ship to a few initial users free or cheap enough to learn what they actually value.
- Charge around outcomes once value is obvious.
- Keep a daily review loop while the system is young.

This is not passive "build in public." The content strategy is to become useful inside a niche: publish the shortcuts, checklists, failure modes, workflow maps, and edge cases that only an operator would know.

## Workflow Selection Criteria

Good candidates should pass most of these gates:

- A real operator does the workflow repeatedly, not once a year.
- The workflow has visible pain: delays, messy handoffs, duplicate data entry, compliance checks, missed follow-ups, or spreadsheet sprawl.
- The workflow has an outcome someone can price: claim processed, lease renewed, candidate sourced, account researched, invoice reconciled, proposal sent, report generated.
- The manual version can be done by Seth with available time and public or customer-provided data.
- The workflow can be demonstrated without exposing confidential client material.
- A useful artifact can be produced in under a week: ranked list, researched brief, workflow map, approval queue, agent-run log, dashboard, or before/after demo.
- Edge cases can become durable memory, rules, or skills instead of staying in Seth's head.

Avoid workflows where the only value is novelty, generic content generation, or "an agent could probably do this." The better question is: would a tired operator pay to stop doing this exact annoying thing?

## First Experiment Loop

Use this as the default loop for a new workflow experiment:

1. Pick one vertical and one workflow.
2. Interview or observe 5 to 10 people who touch that workflow.
3. Write a workflow map: inputs, tools, handoffs, approvals, data fields, edge cases, failure modes, and output.
4. Do the workflow manually for one friendly user.
5. Save every reusable instruction into markdown: glossary, source list, decision rules, examples, edge cases, QA checklist.
6. Turn only the stable steps into 1 to 3 skills or scripts.
7. Add watchdogs: failed run alerts, missing-data checks, stale credential checks, and human approval gates.
8. Measure the outcome and cost: time saved, completion rate, money recovered, revenue created, user trust, model/tool spend.
9. Package the result as both an offer and a job-search proof artifact.
10. Decide whether to repeat, narrow, sell, or archive.

The first goal is learning density, not beautiful software. A spreadsheet plus a markdown runbook plus a rough agent loop can be enough if it proves the workflow.

## Architecture Pattern

The scaling architecture in the source is: shared platform, isolated customer/workflow agents.

Early stage:

- One isolated environment per customer or workflow.
- Separate vault, credentials, logs, config, vector namespace, and audit history.
- Shared skills repo where reusable workflow logic lives.
- Daily manual review by Seth.

Later stage:

- Control plane for customers, workflows, schedules, permissions, billing/outcomes, logs, alerts, and skill versions.
- Shared skill library for email, CRM, spreadsheets, document parsing, research, enrichment, and vertical-specific workflow steps.
- Agent runners scoped by customer or workflow.
- Per-customer memory, structured database, vector/search namespace, run history, documents, credentials, and edge-case notes.

The rule is: fork configuration, memory, credentials, and runtime context; do not fork product code unless isolation requires it.

## Isolation Rule

The page's most important architecture warning is that data separation is a plumbing problem, not a vibes problem. The danger is not that "the model knows too much" in the abstract. The danger is a global vector DB, an unscoped file tool, a shared prompt context, a loose SQL query, or reused credentials.

Every tool call should run inside explicit tenant/workflow context:

- `tenant_id`
- `workflow_id`
- `vault_path`
- `vector_namespace`
- `secrets_scope`
- `logs_path`
- `db tenant_id` or separate schema
- approval policy

For the first few customers, prefer hard isolation even if it feels inefficient. A separate runtime per customer is easier to debug and easier to trust. Multi-tenant convenience can come later, after the workflow has enough repetition to justify a control plane.

## Job-Search Proof-Of-Work

Each workflow hustle should produce evidence that can help in applications and interviews:

- A one-page workflow map.
- A system diagram of manual steps, tools, data transformations, and approval gates.
- A representative schema or field list.
- A short demo or artifact showing the output.
- A run log showing what the agent or workflow did.
- A "what broke" section with edge cases and mitigations.
- A pricing note explaining why the outcome has value.
- A truth boundary: what was real customer work, what was prototype, and what is a hypothetical extension.

This keeps the hustle from becoming a distraction. If it works commercially, good. If it does not, it still compounds into an interview-ready portfolio of workflow design, GTM judgment, systems thinking, and applied AI execution.

## Open Questions

- Which workflow should Seth test first while applications are active?
- Should the first lane be GTM/research workflows, job-search workflows, finance/ops workflows, recruiting workflows, or vertical back-office workflows?
- What is the smallest paid or free pilot Seth can run without creating support burden during job applications?
- Which proof artifact should be generated for every experiment: HTML case study, markdown runbook, demo video, or dashboard?
- Should Hermes be the first harness for these experiments, or should the first few be run with Codex/Claude Code plus simple scripts?
- What should the default customer/workflow folder structure be before any real customer data appears?

## Sources

- [Vertical AI agent startup and workflow hustle note](../../raw/intentional/pasted/2026-06-15-vertical-ai-agent-startup-and-workflow-hustle-while-job-hunt.md)

## See Also

- [Zhao OrderOps PRD](zhao-orderops-prd.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
- [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
