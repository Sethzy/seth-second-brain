---
type: wiki_article
title: ChatGPT Work
updated_at: 2026-07-28
status: active
source_count: 13
tags:
  - openai
  - chatgpt-work
  - codex
  - workspace-agents
  - knowledge-work
  - enterprise-ai
---

# ChatGPT Work

> Sources: OpenAI ChatGPT Work launch, product page, release notes, Work and Codex guide, Plugins guide, Workspace Agents guide, and GPT-5.6 material, checked 2026-07-23.
> Raw: [ChatGPT Work announcement](../../raw/intentional/web/2026-07-09-openai-chatgpt-work.md); [GPT-5.6 announcement](../../raw/intentional/web/2026-07-09-openai-gpt-5-6.md); [interview-prep migration snapshot](../../raw/intentional/pasted/2026-07-23-openai-technical-acumen-pack-migration-snapshot.md)

> 2026-07-26 addendum: [ChatGPT and Codex workflow field guide](../../raw/intentional/web/2026-07-26-work-in-progress-chatgpt-and-codex-workflow-field-guide.md); [Seth saved-link notes](../../raw/intentional/pasted/2026-07-26-saved-link-batch-notes-and-ingestion-intent.md)
> 2026-07-28 addendum: [Tibo and Sam Altman on a delegated group-trip workflow](../../raw/intentional/x/2081444811647963244-thsottiaux-let-chatgpt-work-for-you-how-many-time-have-you-wanted-to-negotiate-your-intern.md)

## Definition

ChatGPT Work is OpenAI's general-purpose execution agent for knowledge work. It can stay with a task for hours, gather context from files and connected systems, break an outcome into steps, act across tools, and produce finished spreadsheets, documents, presentations, analyses, and Sites while the user reviews, redirects, or approves consequential actions.

The strategic shift is from **a response** to **a completed artifact or maintained workflow**.

## Capability Stack

| Layer | Current role |
|---|---|
| Context | Projects, uploaded/local files, plugins, apps, web sources, and project instructions. |
| Planning | Plan mode gathers context, asks questions, proposes steps, and accepts edits or approval before execution. |
| Execution | Cloud browser and connected apps on web/mobile; local files, desktop apps, built-in browser, and Computer Use on desktop. |
| Artifacts | Editable docs, slides, sheets, analyses, reports, and Sites/web apps. |
| Persistence | Scheduled Tasks can run once, repeat, trigger, or monitor changes. |
| Control | Progress review, mid-task steering, approval gates, app permissions, and auto-review for important actions. |
| Models | GPT-5.6 Sol, Terra, and Luna provide capability/speed/cost choices where eligible. |

OpenAI says more than five million people use Codex weekly and more than one million use it outside software development. Work productizes that non-developer behavior in a business-native surface.

## Product Boundaries

| Surface | Primary job | Best seller framing |
|---|---|---|
| Chat | Quick questions, search, brainstorming, and conversational help. | Fast assistance. |
| Work | Long multi-step knowledge work and finished business artifacts. | Outcome execution for an individual or project. |
| Codex | Repository, terminal, test, command, review, and software-delivery work. | Engineering execution. |
| Workspace Agents | Published, governed, repeatable team workflows. | Centralized build, decentralized use. |
| Presence | Managed real-time voice/chat agents in production. | High-value customer/internal workflow resolution. |

Work and Codex share execution patterns, pricing, credits, and usage limits, but the user-facing jobs remain distinct. The Codex app merged into the ChatGPT desktop shell while Codex remained a separate view with its own workflows and history.

The natural adoption loop is:

1. Discover a valuable process through an individual Work thread.
2. Refine context, tools, review rules, and success criteria.
3. Package the repeatable process as a Workspace Agent.
4. Use Presence or a custom API build when the workflow becomes a real-time production service rather than employee work.

## Cloud, Mobile, And Local Continuity

The July 16 desktop update made cloud Work conversations continuous across web, mobile, and desktop; Chat and Work share Recents, and Projects can seed Work with durable context.

The important boundary is **cloud versus local**:

- Cloud Work can continue across devices.
- Local desktop threads can use local folders and apps but remain on that computer.
- Web/mobile cannot directly access desktop files.
- The cloud browser supports public pages but not authenticated sites or payments at launch.
- The desktop browser can support sign-in, downloads, multiple tabs, and richer inspection, which creates stronger device and credential governance requirements.

## Availability Snapshot

As of 2026-07-23:

- Desktop Work is available on macOS and Windows across plans, including Free, with plan-dependent model/usage behavior.
- Web/mobile Work is available on paid plans listed by the current product page: Plus, Pro, Business, Enterprise, and Edu.
- Enterprise/Edu rollout and admin defaults depend on tenant timing and configuration.
- Individual plugins, Sites publishing, browser capabilities, and models vary by plan, role, region, workspace settings, and rollout state.
- Work usage is task-variable and shares the Codex usage/credit structure; it should not be forecast as a flat message count.

These boundaries are moving quickly. Verify the current product and help pages before quoting plan access.

## Use-Case Discovery Library

The OpenAI-branded `Work, in progress` catalog is useful as a discovery prompt bank rather than product documentation. It groups examples across agent workflows, coding/building, knowledge work, and creative work: cloud Work tasks, browser research, pull-request review, computer-use window management, Sites, video editing, multi-agent work, documents, spreadsheets, and remote control.

Convert an example into a qualified workflow by asking who performs it today, which systems and permissions it needs, how often it runs, what evidence proves completion, where human review belongs, and what cycle time, quality, or throughput improvement matters. Treat exact machine specifications or plan entitlements repeated in social posts as volatile until confirmed from official product surfaces.

A vivid consumer example is Altman's reported group-trip delegation: infer preferences from chat history, research three options, build a coordination site for nine people, wait for group agreement, prepare reservations, and draft the invitation email. The product lesson is broader than travel: Work can join personal context, research, artifact creation, multi-person coordination, browser action, and an approval boundary inside one outcome.

## Enterprise Buying Implications

### Sell workflows, not prompts

OpenAI's launch proof points are month-end close, forecasting, pipeline recovery, launch governance, competitive research, product operations, and event preparation. A credible rollout should measure cycle time, quality, rework, approval burden, adoption, and credit cost per workflow.

### Connected context is the bottleneck

Work becomes more useful as it gains access to CRM, email, messaging, calendars, documents, and project systems. That makes permissions, OAuth, source-system access, regional availability, action controls, and app administration central to deployment.

### Governance is product architecture

Enterprise buyers should evaluate workspace roles, plugin/app permissions, browser/network controls, approvals, Compliance API visibility, local-device governance, and review of important actions—not just model quality.

### Agent FinOps replaces seat-only FinOps

Business value and cost vary by workflow, model tier, task length, context volume, retrieval, and tool use. Admins need to compare cost and quality across ad hoc Work, scheduled tasks, Codex, and published Workspace Agents.

## Limitations And Diligence

- The rollout is new and official pages still expose slightly different plan language.
- "1,400+ plugins" does not mean every integration is available to every user.
- Cloud browser cannot yet handle authenticated websites or payments.
- Sites remains a public beta with administrative and regional constraints.
- Approval and auto-review reduce risk but do not remove the need to verify sources, spreadsheet logic, recipients, permissions, and high-impact actions.
- Business/Enterprise data is not used for training by default; personal workspace settings differ and should be checked.

## Interview Talk Track

> ChatGPT Work is the productization of what OpenAI learned from people using Codex for non-code work. It gives long-horizon delegation a native surface for research, connected apps, browser and desktop action, office artifacts, Sites, and scheduled workflows. The coherent operating loop is Projects for context, plugins for systems, Work for execution, Sites for interactive output, and Workspace Agents for standardizing the patterns that prove valuable.

Best question to ask:

> How will admins compare quality, cost, approvals, and failure modes across ad hoc Work threads, Scheduled Tasks, and published Workspace Agents so experimentation can become governed scale?

## See Also

- [OpenAI Release Radar](release-radar.md)
- [OpenAI Enterprise Product Framing](openai-enterprise-product-framing.md)
- [OpenAI Presence](openai-presence.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
- [Browser And Computer-Use Workflows](../personal-systems/browser-and-computer-use-workflows.md)
