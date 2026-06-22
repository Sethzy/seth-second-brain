---
type: wiki_article
title: Acme Agentic GTM OS
updated_at: 2026-06-16
status: active
source_count: 24
tags:
  - acme
  - gtm
  - company-os
  - sales
  - marketing
  - design-system
  - account-research
---

# Acme Agentic GTM OS

> Sources: Seth pasted Acme bundle, 2026-06-11; Dan Rosenthal X post, 2026-05-01; Shann Holmberg X post, 2026-05-02; Actively AI homepage, 2026-06-11 capture; LangChain GTM agent blog, 2026-06-11 capture; Browserbase GTM page, 2026-06-11 capture; Remotion X post, 2026-01-20; HyperFrames/Editframe X posts, 2026-04/05; Open Design README, 2026-06-11 capture; Claude Design/brand/design posts, 2026-04/05; Anthropic growth marketing article, 2026-06-11 capture; cold outbound/API-tool notes from Seth pasted bundle
> Raw: [Acme GTM OS pasted bundle](../../raw/intentional/pasted/2026-06-11-acme-gtm-os-agentic-sales-marketing-and-design-bundle.md); [Dan Rosenthal company brain X post](../../raw/intentional/x/2050289242371178569-dan-rosenthal-service-as-a-software-is-here-we-moved-our-entire-company-brain-to-github-an.md); [Shann Holmberg proposal agent X post](../../raw/intentional/x/2050500596839682157-shannholmberg-create-high-converting-proposals-in-under-15-minutes-save-this-blueprint-and.md); [Actively AI homepage](../../raw/intentional/web/2026-06-11-actively-ai-homepage.md); [LangChain GTM agent blog](../../raw/intentional/web/2026-06-11-langchain-gtm-agent-blog.md); [Browserbase GTM industry page](../../raw/intentional/web/2026-06-11-browserbase-gtm-industry-page.md); [Remotion agent skills X post](../../raw/intentional/x/2013626968386765291-remotion-remotion-now-has-agent-skills-make-videos-just-with-claude-code-npx-skills-add-re.md); [HyperFrames example X post](../../raw/intentional/x/2050296972222124286-liu8in-this-is-an-incredible-hyperframes-example-our-ceo-joshua-xu-took-it-and-built-2-dif.md); [Editframe launch X post](../../raw/intentional/x/2049888877129707759-yuddidit-today-editframe-emerges-from-stealth-agents-need-video-editframe-agent-skills-npm.md); [Open Design README](../../raw/intentional/web/2026-06-11-open-design-readme.md); [Nate Herk Claude Design X Article](../../raw/intentional/x/2049671370099826725-nateherk-claude-design-built-my-brand-end-to-end-without-hitting-limits-i-burned-500-in-ex.md); [Leon Lin image-to-code X Article](../../raw/intentional/x/2048791596137632126-lexnlin-building-better-frontends-with-an-image-to-code-approach-most-ai-generated-website.md); [Leon Lin image-to-website example X Article](../../raw/intentional/x/2050179260892029179-lexnlin-how-to-turn-an-image-into-a-website-example-you-may-have-read-this-tutorial-and-st.md); [Luca Da Corte calculator X post](../../raw/intentional/x/2050286605944946832-lucadacorte-savings-estimator-built-in-framer-https-t-co-pglob4u9wj.md); [Cursor starter projects X post](../../raw/intentional/x/2049499874043830389-cursor-ai-we-ve-open-sourced-a-few-starter-projects-for-you-to-build-on-a-coding-agent-cli.md); [Arrakis Codex app server X post](../../raw/intentional/x/2049484893877637359-arrakis-ai-the-codex-app-server-is-massively-underrated-you-can-inject-codex-level-intelli.md); [Founders Inc cold DM X post](../../raw/intentional/x/2050285858285400537-fdotinc-how-to-cold-dm-anyone-complete-basics-00-00-why-i-love-cold-emails-02-36-inbound-v.md); [Pallavi Replit slides X post](../../raw/intentional/x/2050226416999080182-pallavi-benawri-brb-making-slides-for-everything-now-https-t-co-nfgs1uvwb8.md)
> 2026-06-16 additions: [Acme/eGiro first-10-day goals](../../raw/intentional/pasted/2026-06-16-acme-egiro-first-10-day-goals-and-side-projects.md); [GTM workspace agentic outbound and Acme OS docs](../../raw/intentional/pasted/2026-06-16-gtm-workspace-agentic-outbound-and-acme-os-docs.md); [sales plugin account-research and outreach skills](../../raw/intentional/pasted/2026-06-16-sales-plugin-account-research-and-outreach-skills.md); [enterprise sales high-signal transcript](../../raw/intentional/pasted/2026-06-16-enterprise-sales-high-signal-transcript.md); [enterprise sales X profile backdated digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-backdated-digest.md); [Chris Pisarski posts 101-200](../../raw/sweeps/x/2026-06-16-chrispisarski-posts-101-200.md)

## Overview

This is a working design for an Acme/eGiro agentic GTM operating system. The durable goal is not "automate sales" in one giant step. It is to build a company brain shared by tech and sales, then layer account data, trigger monitoring, research skills, positioning drafts, decks, website/assets, and low-touch onboarding around that shared memory.

The Dan Rosenthal company-brain post is the closest reference architecture: markdown company OS in GitHub, org-wide context plugin, client/account repos synced from Slack/calls/Drive/campaign systems, MCPs for action, self-improvement from campaign performance, and safeguards. Actively, LangChain, and Browserbase show the market version of the same direction: per-account agents, GTM agents, and browser/cloud research systems that keep accounts warm.

## System Shape

- Company brain: a shared markdown/GitHub or wiki repo that sales and tech can both contribute to, with Slackbot access for lookup and capture.
- Domain fluency: a banking/payment cheat sheet with terminology, quirks, objections, compliance vocabulary, onboarding steps, and stakeholder roles.
- CRM: move from spreadsheet to Attio-style CRM, but keep a headless agent interface for updates, pulls, and audit logs. WhatsApp conversations should sync into account/contact context before the agent writes claims.
- TAM and licensed company list: scrape the regulated universe, preserve source URLs, normalize into Supabase/CSV, and keep license status current.
- Trigger monitoring: cron jobs for license announcements, expansions, hiring, job changes, regulatory news, funding, partnerships, and product launches.
- Account graph: stakeholders, roles, LinkedIn URLs, email confidence, job-change checks every two weeks, and provenance from Crustdata/Clay/Parallel/OpenWeb-style sources.
- Account research skill: for each key account, generate at least five sales angles, supporting evidence, objections, and a first-draft deck or one-pager.
- Daily sales cadence: one thoughtful, researched outreach per target account per day, with human approval before sending.
- Low-touch onboarding: turn eGiro into a self-serve agent-assisted path for smaller customers so humans can focus on enterprise deals.

## First 10-Day Operating Priorities

The 2026-06-16 goals make the OS less abstract. The first win is the second-brain Slackbot/company brain, because it is the shared interface between sales, tech, and future agents. The choice between Viktor.ai, Nanoclaw plus a Karpathy-style VPS, Scout-style company brain, or this repo pattern should be judged by one practical test: can everyone contribute source material, retrieve account/domain context from Slack, and trace answers back to raw evidence?

The second priority is domain fluency. The banking/payments pain-point deep dive should produce a memorized cheat sheet: regulatory terms, onboarding steps, compliance constraints, bank/payment quirks, stakeholder roles, objection patterns, and trigger events. This is sales enablement and agent context at the same time.

The operating stack should then move in this order:

- CRM migration: move spreadsheet state into Attio, but keep updates and pulls agent-accessible through MCP or a controlled CLI. WhatsApp sync belongs in the evidence lane first; contact/account claims should cite conversation excerpts before becoming CRM fields.
- TAM scrape: finish the licensed-company universe with source URLs, license status, geography, product category, and freshness dates.
- Trigger cron: monitor license announcements, market expansion, hiring, leadership changes, regulatory/news mentions, new product launches, and bank/payment partnerships.
- Account graph: maintain stakeholders, influence maps, social/LinkedIn evidence, job-change checks, and confidence scores in Supabase or Attio.
- Research-to-outreach loop: generate at least five sales angles per priority account, draft a deck or one-pager, and send only one thoughtful researched outreach per day after review.
- eGiro low-touch onboarding: document the current onboarding/sales process, then automate the repeatable pieces so humans focus on enterprise accounts.

## Sales Operating Cadence

The backdated X sweep adds a practical cadence for making the OS useful to humans, not just agents:

- Daily deal review: a 15-minute CEO/sales/growth war room that only asks "what was the last touch?" and "what do we do next?" for the most important open deals.
- CRM note quality: after every real conversation, capture problem, root cause, quantified impact, deadline, and consequence so the next agent/human can reason from the deal thesis.
- Demo prep: before showing product, ask the buyer what proof would convince them, then tailor the demo to those criteria.
- Champion package: for strategic accounts, generate an internal memo, ROI math, implementation outline, risk/procurement answers, and next-step email the champion can forward.
- Skill bootstrap: sales skills should inherit Acme/eGiro's brand, banking terminology, ICP, proof points, CRM schema, and approved claims from the company brain before writing anything.

## Build Order

1. Build the Acme company brain and Slackbot first. It becomes the shared context layer for every later agent.
2. Compile the banking/payments terminology and pain-point cheat sheet.
3. Normalize the CRM/account schema before moving data into Attio or Supabase.
4. Finish the licensed-company TAM scrape and source every claim.
5. Add trigger monitors and a job-change/stakeholder refresh loop.
6. Build the key-account research skill and deck/positioning generator.
7. Add the low-touch onboarding assistant only after the existing sales/onboarding process is documented.
8. Automate marketing artifacts once brand guidelines and design system are stable.

## Marketing And Design System

The marketing side should start with a brand guideline and design system, then generate assets from that source of truth. The Claude Design/Open Design sources point at the same workflow: brainstorm outside the expensive design surface, lock `DESIGN.md`/brand guidelines, generate high-fidelity visual directions, hand off to Codex/Claude/Cursor, then validate with screenshots.

Artifact priorities:

- Enterprise website refresh with clearer positioning, proof, calculators, and self-serve onboarding CTAs.
- Calculator pages, especially savings/ROI estimators.
- LLM-friendly API docs and a repo of frontend/API demo artifacts.
- Programmatic launch videos for product, bank, and feature announcements using Remotion, HyperFrames, or Editframe.
- Slide/deck generator for account-specific first drafts, possibly Replit Slides/Presenton/Open Design style.
- Design inspiration and components from Refero, Jiro, Aura, shadcn UI illustrations, Grainient, and brand-resource lists, but only after Acme's own design rules exist.

## GTM Data Stack Leads

The pasted outbound list is a useful provider map:

- Clay/Claygent for orchestration, job/hiring signals, department counts, cached AI runs, and tool calls.
- Prospeo/BlitzAPI for company/contact finding, LinkedIn-based enrichment, org structure, and role lookup.
- OpenWeb Ninja for Google-style scraping, news, blogs, and competitor research.
- RapidAPI/Apify for marketplace scrapers.
- Parallel Web Systems for deep research when the data is unstructured.
- Scrape Creators for social scraping.
- DiscoLike/Ocean.io for lookalikes.
- BuiltWith/Store Leads for tech/ecommerce targeting.
- ZenRows/Spider.Cloud for bot-resistant web scraping.
- Browser Use or Browserbase for click-around workflows.
- Trigger.dev for scheduled scrapers that save results and push approved records into campaign tools.

## Open Questions

- Should the Acme company brain be this repo pattern, Scout, Viktor.ai, Nanoclaw + Karpathy wiki on a VPS, or a Slack-native company OS?
- Which system should be the source of truth for accounts: Attio, Supabase, the markdown wiki, or a split?
- How much WhatsApp history can be synced safely, and what approval/privacy rules are needed?
- Which first TAM source defines "every licensed company" in Acme's space?
- Which trigger monitor is highest ROI: license changes, new hires, market expansion, job changes, or regulatory/news events?
- Which design surface should drive the website refresh: Codex Build Web Apps, Claude Design, Open Design, Cursor, or a manual design system plus Codex?
- What is the smallest demo that proves the OS: one account, five angles, one deck, one approved outreach, and one tracked follow-up?
- What exact acceptance test proves the first-10-day OS is real: one account with source-backed stakeholders, five angles, a reviewed deck, a single outbound message, and a logged follow-up?

## See Also

- [Agentic GTM Campaign Workflows](agentic-gtm-campaign-workflows.md)
- [AI-Native Account Intelligence](ai-native-account-intelligence.md)
- [High-Signal Enterprise Sales](high-signal-enterprise-sales.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
