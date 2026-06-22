---
type: wiki_article
title: AI-Native Account Intelligence
updated_at: 2026-06-16
status: active
source_count: 11
tags:
  - account-intelligence
  - ai-gtm
  - crm
  - signals
  - stakeholder-mapping
  - attio
  - supabase
---

# AI-Native Account Intelligence

> Sources: Acme/eGiro first 10 day goals, 2026-06-16; Seth enterprise-sales transcript, 2026-06-16; Cher Hao WhatsApp excerpt, 2026-06-16; Career Ops Enterprise Sales Playbook, 2026-06-16 import; Sales plugin account research/outreach skills, 2026-06-16 import; GTM workspace agentic outbound and Acme OS docs, 2026-06-16 import; Fivos Aresti X profile sweep, 2026-06-16; Chris Pisarski X profile sweep, 2026-06-16; Enterprise Sales X Profile Digest, 2026-06-16; Fivos Aresti backdated X profile sweep, 2026-06-16; Enterprise Sales X Profile Backdated Digest, 2026-06-16
> Raw: [Acme/eGiro first 10 day goals and side projects](../../raw/intentional/pasted/2026-06-16-acme-egiro-first-10-day-goals-and-side-projects.md); [enterprise sales high-signal transcript](../../raw/intentional/pasted/2026-06-16-enterprise-sales-high-signal-transcript.md); [Cher Hao high-signal outreach WhatsApp excerpt](../../raw/intentional/pasted/2026-06-16-cher-hao-high-signal-outreach-whatsapp-excerpt.md); [Career Ops enterprise sales playbook](../../raw/intentional/pasted/2026-06-16-career-ops-enterprise-sales-playbook.md); [Sales plugin account research and outreach skills](../../raw/intentional/pasted/2026-06-16-sales-plugin-account-research-and-outreach-skills.md); [GTM workspace agentic outbound and Acme OS docs](../../raw/intentional/pasted/2026-06-16-gtm-workspace-agentic-outbound-and-acme-os-docs.md); [Fivos Aresti X profile sweep](../../raw/sweeps/x/2026-06-16-fivosaresti-last-100-posts.md); [Chris Pisarski X profile sweep](../../raw/sweeps/x/2026-06-16-chrispisarski-last-100-posts.md); [Enterprise sales X profile digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-digest.md); [Fivos Aresti posts 101-190](../../raw/sweeps/x/2026-06-16-fivosaresti-posts-101-190.md); [Enterprise sales X profile backdated digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-backdated-digest.md)

## Overview

AI-native account intelligence is the research layer underneath high-signal enterprise sales. It is not a spam engine. Its job is to continuously answer:

- which accounts matter;
- which people matter inside each account;
- what changed recently;
- why now is or is not the right moment;
- what proof point and question should the seller use;
- what should be left alone until a better signal appears.

The seller-facing output should be small: the best three people to contact today, the top accounts to monitor, and the reason behind each recommendation. Retrieval alias: top 3 prospects.

## System Shape

The minimum system has five layers:

1. Account universe: licensed companies, ICP candidates, exclusions, and source URLs.
2. Stakeholder map: people, roles, LinkedIn/profile URLs, seniority, budget influence, likely blockers, and warm paths.
3. Signal store: first-party, second-party, and third-party events with dates and evidence.
4. Research brief: account context, current hypothesis, pain points, proof-point match, objections, and outreach angle.
5. Action queue: next best action, owner, cooldown, approval state, and outcome.

The system should store evidence before synthesis. Raw provider responses, source URLs, confidence, and timestamps matter because CRM fields go stale.

## Signal Taxonomy

Fivos's ABM signal stack is a useful field taxonomy:

- First-party signals: CRM notes, product usage, web visitors, demo forms, replies, meetings, Slack/Gmail/WhatsApp context, and prior conversations.
- Second-party signals: partner data, shared communities, warm-intro graphs, review sites, champion tracking, LinkedIn engagement, and event attendance.
- Third-party signals: licenses, job openings, executive changes, funding, market expansion, technology installs, competitor mentions, content, and news.

Signals should stay separate from scoring. A signal can be true but not messageable. The account-intelligence table should track event type, recency, account fit, event strength, messageability, source URL, confidence, and recommended angle.

## Signal Routing And Feedback

The backdated Fivos sweep makes the signal pipeline stricter: signal capture is not the win. The win is routing the signal into the right action with enough context that a seller, founder, or agent can act.

For each signal, track:

- source and capture timestamp;
- signal type and evidence URL;
- account/person match;
- intent strength;
- awareness stage;
- recommended route: Slack alert, CRM task, outbound trigger, nurture, retargeting, research queue, or no action yet;
- owner and SLA;
- outcome;
- whether closed-won/closed-lost results should adjust future signal weights.

This prevents the common failure mode where Clay/RB2B/Jungler-style signals pile up in dashboards while reps keep working a static list.

## Daily And Weekly Outputs

Daily output:

- top three prospects to contact today;
- top ten prospects/accounts to monitor;
- "do not touch yet" list with missing-signal reasons;
- one thoughtful researched outreach draft for any account that crosses the threshold.

Weekly output:

- accounts with fresh triggers;
- new warm-intro paths;
- stakeholder/job changes;
- event hijacking opportunities;
- proof-point gaps;
- repeated objections and buyer anxieties;
- content topics generated by real conversations.

This matches the transcript's core operating line: always run a job that surfaces the best few people to reach out to today.

## CRM And Data Pipe

The Acme/eGiro plan points toward a split system:

- Attio or another CRM for current account/person/deal state.
- Supabase or a local database for raw/normalized account intelligence, provider responses, and scheduled checks.
- The Second Brain/wiki for durable playbooks, terminology, and synthesis.
- Slackbot/company-brain access so sales and tech can contribute and retrieve shared context.

CRM fields should be conservative. The agent can suggest updates, but high-impact commercial fields, customer claims, and outreach actions need human review.

## Stakeholder And Job-Change Monitoring

Stakeholder maps should refresh on a cadence, especially for regulated or enterprise accounts where people move roles. A two-week job-change check is a reasonable starting point for key accounts. Fields worth tracking:

- current company and title;
- prior companies and relevant workflow overlap;
- alumni/shared background;
- likely budget influence;
- champion/blocker/user/buyer role;
- last confirmed date;
- source URL;
- confidence;
- next action.

Job changes are not automatically outreach triggers. They become triggers when they create a plausible reason to speak: new mandate, inherited mess, relevant past workflow, or warm relationship path.

## WhatsApp, Slack, And Meeting Memory

The first-10-day goals include a WhatsApp CLI sync. Treat WhatsApp like other live signals:

- preserve raw conversation references where allowed;
- extract account/person facts into reviewable notes;
- do not silently convert informal claims into CRM truth;
- link any account update back to the original conversation.

Chris Pisarski's posts add two related patterns: shared Slack channels can become high-trust customer/prospect surfaces, and meeting/call data can power pre-call briefs. For Acme/eGiro, the useful workflow is: meeting transcript or chat context -> attendee enrichment -> account brief -> suggested questions -> human-reviewed next action.

## Account Research Skill Contract

Each key-account research run should produce:

- company profile and source URLs;
- stakeholder map;
- recent triggers;
- banking/payment pain points and terminology;
- five or more sales angles;
- matching proof points;
- likely objections;
- discovery questions;
- first-draft outreach;
- first-draft deck or one-pager when useful;
- confidence and missing-evidence notes.

The output should be structured enough to route into a CRM, deck generator, or outreach review queue. It should not die as a chat transcript.

## Approval Boundaries

Safe for automation:

- source discovery;
- enrichment;
- dedupe;
- signal classification;
- draft briefs;
- suggested CRM updates;
- suggested outreach/deck copy.

Needs human approval:

- sending messages;
- changing deal stage or commercial values;
- claiming customer facts;
- using confidential competitor intelligence externally;
- syncing unreviewed WhatsApp/social data into official CRM fields.

## Open Questions

- Which account store becomes canonical for Acme/eGiro: Attio, Supabase, or a split?
- Which first TAM source defines every licensed company in scope?
- Which provider should be tested first for job-change/stakeholder data: Crustdata, Clay MCP, People Data Labs, Apollo, or a custom scrape?
- What is the acceptance test for "one thoughtful researched outreach"?

## See Also

- [High-Signal Enterprise Sales](high-signal-enterprise-sales.md)
- [Acme Agentic GTM OS](acme-agentic-gtm-os.md)
- [Agentic GTM Campaign Workflows](agentic-gtm-campaign-workflows.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
