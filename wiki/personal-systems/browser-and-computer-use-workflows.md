---
type: wiki_article
title: Browser And Computer-Use Workflows
updated_at: 2026-07-26
status: active
source_count: 7
tags:
  - computer-use
  - browser-agents
  - chatgpt-work
  - scraping
  - workflow-design
---

# Browser And Computer-Use Workflows

> Sources: OliviscusAI Lightpanda post; Charlie Kerr Hermes saved-TikTok workflow; Jack Dorsey Buzz workspace post; Mike Nevermiss PhoneDriver story; ChatGPT and Codex workflow field guide; Seth's ChatGPT Work VM and Booking.com benchmark notes; OpenAI ChatGPT Work official-source synthesis, captured through 2026-07-26.
> Raw: [Lightpanda browser lead](../../raw/intentional/x/2080965029877461277-oliviscusai-every-ai-agent-scraping-the-web-right-now-is-running-full-chrome-to-do-it-rend.md); [Hermes saved-TikTok workflow](../../raw/intentional/x/2080830108013670549-charliekerr-my-girlfriend-has-thousands-of-tiktok-s-saved-day-trips-vacation-ideas-restaur.md); [Buzz workspace](../../raw/intentional/x/2080056638820450400-jack-why-we-re-buzzing-yesterday-we-released-buzz-it-s-an-open-source-workspace-that-puts.md); [PhoneDriver story](../../raw/intentional/x/2080183484371320975-mikenevermiss-a-22-year-old-college-student-in-shenzhen-reportedly-made-14-700-in-one-mont.md); [ChatGPT and Codex workflow field guide](../../raw/intentional/web/2026-07-26-work-in-progress-chatgpt-and-codex-workflow-field-guide.md); [Seth saved-link notes](../../raw/intentional/pasted/2026-07-26-saved-link-batch-notes-and-ingestion-intent.md); [ChatGPT Work official capture](../../raw/intentional/web/2026-07-09-openai-chatgpt-work.md)

## Overview

Computer use is the execution layer for work that still lives behind human-oriented interfaces. A useful agent can browse, collect information, operate desktop or web applications, save results into durable files, and let the human inspect or approve the consequential steps. The relevant product question is not whether an agent can click. It is whether the workflow has the right environment, identity, context, verification, and recovery design.

## Three Runtime Shapes

### Lightweight browser execution

The Lightpanda lead represents an efficiency-first runtime for scraping and web automation. A smaller browser can reduce the cost of running many agents, but compatibility, rendering fidelity, authentication, anti-bot behavior, and browser-specific features still require benchmarking against Chrome-class automation.

### Full browser or desktop computer use

Full browser/desktop control is appropriate when the workflow needs sign-in, downloads, multiple tabs, visual state, native apps, or manual handoff. It is more capable and more exposed: device state, credentials, downloads, notifications, and accidental actions become part of the threat model.

### Remote workspace execution

ChatGPT Work and related remote work surfaces make a disposable machine available to a broad user. The strategic effect is that non-technical operators can delegate package installation, browser research, file transformation, and artifact production without first provisioning a server. Treat exact VM specifications in social posts as volatile until confirmed by an official product surface.

## Workflow Pattern

The Hermes saved-TikTok example is a good end-to-end shape:

1. detect or watch a user-selected source;
2. extract structured details;
3. store them in a durable vault;
4. make the saved corpus conversationally retrievable;
5. keep the original source pointer.

This pattern generalizes to travel research, prospect research, product monitoring, content libraries, and customer-support evidence.

## Booking.com Benchmark

Seth's proposed airport-transfer benchmark is a useful computer-use evaluation:

1. search ten travel destinations;
2. inspect whether airport-transfer options exist and how they are presented;
3. record price, availability, pickup constraints, cancellation terms, and source URL;
4. capture evidence screenshots or page excerpts;
5. normalize results into a comparison table;
6. flag ambiguous or login-gated cases for review.

This tests browsing, repetition, extraction, state management, and evidence quality without authorizing a purchase. It should remain read-only unless Seth explicitly expands the task.

## Enterprise Controls

- Isolate sessions and credentials.
- Default to read-only collection.
- Require approval for purchases, messages, uploads, or account changes.
- Save source URLs and evidence beside extracted claims.
- Detect partial pages and login walls.
- Log browser actions and failures.
- Separate public-cloud browsing from local-device access.
- Use narrow, task-specific environments rather than a permanently privileged machine.

## See Also

- [ChatGPT Work](../openai/chatgpt-work.md)
- [Agent Platforms And Work Surfaces](agent-platforms-and-work-surfaces.md)
- [Sandbox Filesystem Agent Architecture](../agent-frameworks/sandbox-filesystem-agent-architecture.md)
- [Personal Agent Ops Stack](personal-agent-ops-stack.md)

