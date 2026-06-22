---
type: wiki_article
title: Agentic Classifiers
updated_at: 2026-06-10
status: draft
source_count: 2
tags:
  - classifiers
  - agents
  - knowledge-work
  - evals
---

# Agentic Classifiers

> Sources: Alvin Sng X post, 2026-05-22; Seth pasted agent workflow batch, 2026-06-10
> Raw: [Alvin Sng classifier X post](../../raw/intentional/x/2057928876266033174-alvinsng-one-of-my-favorite-superpowers-of-agents-is-building-classifiers-it-s-insanely-hi.md); [agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md)

## Overview

Agentic classifiers are lightweight classification systems produced and operated by agents rather than traditional ML teams. Alvin Sng's example frames the leverage: an agent can generate a markdown classifier for a specific domain, then other agents can run against it continuously. Seth labeled this source "Classifier," which makes it a reusable pattern to watch for personal knowledge work, GTM ops, bug triage, and document routing.

The important shift is not that every classifier becomes perfect. It is that many formerly expensive categorization workflows become cheap enough to prototype, run, inspect, and revise in plain text.

## Key Ideas

- A classifier can start as a markdown decision file rather than a trained model, especially when the categories are interpretable and the volume is moderate.
- Useful examples include customer-reported bugs, backend traffic analysis, fraudulent payment activity, email labeling, document organization, and personal finance categorization.
- The work loop should keep the classifier inspectable: define labels, run examples, review misclassifications, revise the rubric, and preserve changed decisions.
- Agentic classifiers fit the Second Brain because they can route captures, classify opportunity leads, label source quality, and separate complete evidence from partial leads.

## My Take

For Seth, the near-term high-leverage classifier is probably not a generic ML project. It is a small rubric that classifies incoming links into lanes: complete raw candidate, incomplete lead, GTM opportunity, agent workflow, browser automation, event lead, or personal operating-system idea.

## Open Questions

- Which recurring inbox should get the first markdown classifier: saved links, X captures, job/opportunity leads, or raw-to-wiki routing?
- What evaluation set would prove the classifier is useful enough to trust for first-pass routing?
- Should classifier changes be logged in `wiki/log.md`, a scratch-log, or a dedicated classifier version file?

## Sources

- [Alvin Sng classifier X post](../../raw/intentional/x/2057928876266033174-alvinsng-one-of-my-favorite-superpowers-of-agents-is-building-classifiers-it-s-insanely-hi.md)
- [Agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md)

## See Also

- [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md)
- [AI GTM Opportunity Leads](../gtm-sales/ai-gtm-opportunity-leads.md)
