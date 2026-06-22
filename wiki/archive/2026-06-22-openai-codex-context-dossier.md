# OpenAI And Codex Context Dossier For Strategic BDR APAC

> Sources: [Vendor Agentic Engineering Blogs](../ai-coding/vendor-agentic-engineering-blogs-2026.md); [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md); [AI Engineering Talks On Agentic Coding](../ai-coding/ai-engineering-talks-on-agentic-coding.md); [Agent Framework Landscape](../agent-frameworks/agent-framework-landscape.md); [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md); [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md); [High-Signal Enterprise Sales](../gtm-sales/high-signal-enterprise-sales.md)
> Archived: 2026-06-22

## Overview

This is a point-in-time dossier for talking about OpenAI while applying for the Strategic Business Development Representative, APAC role. The search used QMD first, then exact `rg` backstops across `wiki/`, `raw/`, and `staging/`. Coverage: 3,161 indexed markdown files; the first audit found exact term hits including `OpenAI` in 420 files, `Codex` in 292, `ChatGPT` in 232, `GPT-5` in 109, `OpenAI Developers` in 19, `Agents SDK` in 23, and `Apps SDK` in 3. The re-audit expanded the competitive pass: exact markdown file hits now include `OpenAI` in 439 files, `Codex` in 298, `ChatGPT` in 233, `Claude` in 1,056, `Anthropic` in 511, `Claude Code` in 624, `Claude Cowork` in 83, and `Managed Agents` in 72. A broader metadata scan produced 718 candidate files; the source index below keeps direct OpenAI/Codex company, product, operator, GTM, market-context, and OpenAI-vs-Claude sources, while leaving out generic "supports OpenAI as a provider" mentions unless they add role-relevant signal.

## Executive Summary

OpenAI should be framed as an AI research and deployment company that is turning frontier models into enterprise work systems. The strongest repo evidence points to four linked narratives: ChatGPT as the user-facing work surface, OpenAI APIs and the Responses/Agents stack as the developer platform, Codex as the proof that long-running agents can execute and verify real work, and Apps/MCP/connectors as the bridge into customer systems.

For this role, the most useful story is not "OpenAI has great models." It is: enterprise customers are moving from experimentation to durable deployment when OpenAI can connect usage signals, trusted data, workflow integration, safety controls, and executive-level business outcomes. The BDR job is to find those early pockets of product pull, identify the stakeholders around them, and turn them into high-conviction enterprise opportunities.

The repo's clearest enterprise proof point is the LSEG/financial-data thread: OpenAI plus ChatGPT Enterprise/API is positioned as a reasoning layer over trusted, permissioned, auditable institutional data, not merely a chatbot for analysts. That maps directly to the role posting's Financial Services, Life Sciences, and Retail framing: regulated customers need data boundaries, audit trails, workflow proof, and a credible bridge between technical buyers and C-suite outcomes.

The Claude comparison sharpens the story. Anthropic's corpus signal is strongest around professional trust, Claude Code mindshare, Claude Cowork as a knowledge-work surface, Managed Agents as production infrastructure, and very explicit GTM dogfooding. OpenAI's strongest counter-frame is broader distribution and a more complete work platform: ChatGPT, API/Responses, Codex, Apps, connectors, MCP, evals, and enterprise deployments can all be treated as one pathway from usage to governed workflow transformation.

## How To Talk About OpenAI

Use this positioning:

- OpenAI is moving from model access to workflow ownership: models, tools, Codex, ChatGPT, Apps SDK, MCP/connectors, and enterprise controls combine into an execution surface.
- ChatGPT Enterprise is the adoption surface; the API platform is the build surface; Codex is the execution and proof-of-work surface; Apps SDK and MCP are the integration surface.
- The strategic buyer cares about transformation, not prompts. The relevant outcomes are faster product cycles, better internal knowledge retrieval, safer data workflows, shorter research/reporting loops, and operational processes that become auditable.
- The technical buyer cares about primitives: Responses API, tools, file/search/code/computer use, Realtime, Agents SDK, AgentKit, evals, graders, prompt caching, background mode, webhooks, rate/cost controls, sandboxing, AGENTS.md, skills, and MCP.
- The enterprise seller's job is to connect those two worlds: identify where usage or pilots already exist, ask what business process they touch, map who owns risk/value/budget, and shape an expansion path.

## Role-Specific Lens

The attached role asks for a strategic BDR who can turn product usage, pilots, inbound demand, and targeted outbound into qualified opportunities for large Enterprise and Strategic Accounts. The repo's best prep themes:

- Discovery should be workflow-first: "Which decisions or processes are you trying to compress?" beats "Are you using AI?"
- Outbound should be signal-led: product/category engagement, AI adoption language, competitor content, governance/compliance signals, hiring, event attendance, and usage breadcrumbs all create better entry points than generic AI copy.
- Stakeholder mapping should span business owner, technical buyer, data/security owner, procurement/legal, and executive sponsor.
- Regulated-industry accounts need proof of controls: data residency, retention, encryption, access control, auditability, permissioned connectors, and human approval boundaries.
- The best APAC wedge is to be fluent in both transformation and implementation: speak to C-suite value while understanding enough of APIs, agents, MCP, and Codex to earn credibility with technical buyers.

## Product And Platform Map

**ChatGPT and ChatGPT Enterprise:** the primary user surface for knowledge work. The repo's LSEG capture frames ChatGPT Enterprise and APIs as moving into product, engineering, research, operations, reporting, market-data synthesis, prototyping, and internal workflow transformation.

**API platform and Responses:** OpenAI's 2025 developer roundup describes the shift to agent-native APIs: multimodal inputs/outputs, reasoning controls, tool calling during reasoning, durable conversation state, connectors/MCP, built-in tools, background mode, webhooks, prompt caching, evals, graders, and tuning.

**Agents SDK and AgentKit:** code-first and higher-level building blocks for tools, handoffs, guardrails, tracing, and agent orchestration. The local `Agent Framework Landscape` page says OpenAI Agents SDK is strongest when the app is already OpenAI/Responses-centric or needs sandbox workspaces.

**Codex:** no longer just "a coding model." In the repo, Codex is a long-horizon execution loop: plan, edit, run tests/build/lint, observe, repair, document status, and repeat. The official long-horizon post reports a 25-hour run, about 13M tokens, and about 30k lines of code for a design-tool experiment, with verification after milestones.

**Skills, AGENTS.md, and Goals:** the most reusable Codex story for a GTM interview. Skills package operational knowledge; `AGENTS.md` makes repo rules mandatory; Goals turn open-ended work into durable execution with concrete exit criteria. This maps well to the role requirement to build AI-enabled GTM workflows.

**Apps SDK:** OpenAI's app layer for AI-first product experiences inside ChatGPT. The captured ChatGPT Apps article says app builders must explicitly manage model, widget, and user context; design for natural-language filtering; handle files and widgets; and treat CSP/tool boundaries as production concerns.

**MCP and connectors:** the bridge into customer systems. The repo repeatedly treats MCP/connectors as the safe way to expose external tools, data, and workflows to agents.

**Codex Security:** a role-relevant trust story. The wiki describes Codex Security as scanning connected GitHub repos through Codex Cloud, generating a threat model, producing findings, and creating remediation PRs. The broader lesson is that enterprise AI needs separate levers for context, environment, findings, validation, and PR generation.

## Evolution Of Agentic Coding

This is the Codex narrative to sell: developer tooling has moved from helping people type code to helping organizations delegate bounded work. The arc in the repo is clear:

1. **Autocomplete and IntelliSense:** assisted at the syntax/API level. Useful, but the human still held the whole task, architecture, and verification loop.
2. **Copilots and tab completion:** generated small spans of code. They increased local speed, but they still operated inside the developer's keystroke-by-keystroke workflow.
3. **Chat-based coding:** could explain, draft files, and answer questions, but the user still had to shuttle context, paste errors, apply edits, and decide when the task was done.
4. **Synchronous coding agents:** began reading files, planning, editing, running tests, and iterating inside an IDE or CLI. The core loop became `read -> plan -> code -> validate -> iterate`.
5. **Long-horizon and cloud agents:** moved from "help me with this line" to "take this goal, work for hours, leave me logs/artifacts/diffs/previews, and let me review the result."
6. **Agentic SDLC:** the mature pattern is no longer "AI writes code." Specs define intent, skills encode reusable expertise, harnesses route context and tools, tests/evals define done, and humans review architecture, risk, and business fit.

Coding is the first mass-market arena where this works because software already has agent-friendly feedback: files, git diffs, tests, typechecks, build logs, linters, browsers, screenshots, issue trackers, and PR review. That makes Codex more than a coding SKU. Codex is OpenAI's most concrete demonstration that models can operate inside a governed loop: take a goal, inspect context, act through tools, verify, repair, preserve state, and return reviewable work.

The sales story is therefore:

- **Do not sell Codex as faster typing.** Sell it as the first credible enterprise pattern for delegating digital work with evidence.
- **Do not sell only model intelligence.** Sell the loop around the model: context, tools, worktrees, tests, skills, goals, approvals, docs, traces, and reviewable artifacts.
- **Do not stop at engineering.** Use coding as the proof case, then generalize: sales reports, financial analysis, customer research, compliance prep, data workflows, product operations, and internal knowledge work need the same pattern of context, action, verification, approval, and audit trail.
- **Do not pitch autonomy as magic.** Pitch bounded autonomy: clear goals, scoped permissions, durable memory, validation gates, human review, and receipts for what changed.

### Codex Narrative Summary

The most compact version: **Codex is the place where OpenAI proves that AI can move from answering questions to completing work.** Coding is the beachhead because it has the cleanest feedback loops, but the deeper enterprise narrative is agentic work: humans define intent and judgment, agents execute bounded loops, and the organization gets faster workflows with more traceability than ad hoc manual work.

## OpenAI vs Claude / Anthropic

The right competitive frame is not "which chatbot is smarter?" The repo points to a surface-and-workflow race: both companies are converging on agents that read context, use tools, execute work, verify outputs, and leave artifacts. OpenAI's center of gravity is a unified ChatGPT/API/Codex/Apps work surface. Anthropic's center of gravity is Claude Code plus Claude Cowork plus Managed Agents, with unusually strong public proof that its own sales, data, finance, security, and product teams use those tools internally.

- **Default work surface:** OpenAI can talk about ChatGPT as the adoption surface, the API/Responses stack as the build surface, Codex as the execution surface, and Apps/MCP/connectors as the integration surface. Claude's comparable surface is more segmented but very legible: Claude chat for thinking, Claude Code for code and computer-backed work, Claude Cowork for cross-app knowledge work, and Claude Managed Agents for production agents.
- **Developer and agent-harness credibility:** The local vendor sweep says OpenAI emphasizes Codex, skills, evals, long-horizon work, and multimodal product-building, while Claude emphasizes Claude Code, skills, dynamic workflows, subagents, routines, session management, MCP, managed agents, and enterprise/security patterns. The practical point: both are selling "agents that do work," but OpenAI should make Codex feel like part of a broader enterprise platform, not a standalone coding tool.
- **GTM dogfooding:** Anthropic has unusually crisp GTM case studies: a seller used Claude Code to build CLAFTS, saved 10-15 hours per week, and helped drive a Sales plugin used by about 80 percent of Anthropic's sales org; a sales leader used Claude Cowork to score 4,000 accounts overnight and turn the output into a territory dashboard. OpenAI has comparable internal-Codex proof in the corpus: Codex is reported as used weekly by more than 85 percent of OpenAI across engineering, finance, communications, marketing, data science, and product; it reviewed 24,771 K-1 tax forms across 71,637 pages and helped one GTM employee save 5-10 hours per week on weekly reports.
- **Enterprise trust and controls:** Claude has a strong security/compliance narrative around Compliance API, more than 60 security and compliance integrations, RBAC, spend limits, analytics, OpenTelemetry, tool-level connector controls, self-hosted sandboxes, vaults, persistent sessions, and credential separation. OpenAI needs to answer with enterprise controls, permissioned connectors, sandboxing, evals, auditability, data boundaries, and concrete customer workflows like LSEG.
- **Distribution and adoption:** A saved Ramp AI Index note says Anthropic had 34.4 percent business adoption versus 32.3 percent for OpenAI at that point, with Anthropic adoption rising quickly. This should not be treated as the whole market, but it is a useful competitive signal: Anthropic is credible in business adoption, not only developer mindshare.
- **Market architecture:** The Stratechery note frames Anthropic as using Fable/Mythos-style segmentation by trust level and willingness to pay, while OpenAI's operator-tier model makes capability broadly available and differentiates through customization. In an interview, that becomes a sharp POV: OpenAI can win by making powerful agentic capability accessible across the enterprise while giving strategic accounts the controls and customization they need.
- **Risk for OpenAI:** The unified workbench thesis is powerful, but the corpus warns that solving app fragmentation can create mode fragmentation. A user should not have to know whether work belongs in ChatGPT, Codex, Atlas, an app, a connector, or agent mode; they should understand the task, context, permissions, and review state.
- **Risk for Claude:** Claude's narrative is cleaner in some professional workflows, but it has less consumer distribution than ChatGPT and a more segmented product story. Anthropic validates enterprise agent demand; OpenAI can position itself as the broader deployment layer when customers need user adoption, developer extensibility, data connections, multimodal surfaces, and governed execution in one motion.

### Practical Competitive Talk Tracks

- Do not dunk on Claude. Treat Claude as evidence that the market has accepted agentic work. Then pivot to OpenAI's broader platform: "The question is not whether agents matter. It is how the customer turns scattered usage into a governed, measurable workflow layer."
- In an account already using Claude Code, ask where agent usage lives today, what work it has actually changed, who owns the security boundary, and whether non-engineering teams have equivalent access. Then position Codex as the proof-of-work pattern inside a broader ChatGPT/API/Apps environment.
- In accounts evaluating Claude Cowork, anchor discovery on knowledge-work workflows: recurring reports, account research, briefing, forecasting, compliance reviews, data analysis, and internal ops. Then connect OpenAI to enterprise data, trusted connectors, evals, approvals, and business outcomes.
- In regulated APAC accounts, make the comparison about trust architecture: data residency, permissioned access, audit trails, SIEM/DLP integration, model and tool logs, approvals, and human accountability.
- For GTM transformation, use Anthropic's own sales dogfood as category proof, then ask how OpenAI could help the customer build the same kind of signal-led account research, outbound prioritization, meeting prep, forecast reporting, and workflow automation using their own systems.

## Codex Talking Points

Codex is the best concrete way to explain OpenAI's "agentic work" thesis:

- Coding is the training ground for reliable agents because the task environment has files, tests, logs, diffs, command output, and clear pass/fail signals.
- The same mechanics generalize to sales, finance, legal, research, operations, marketing, and data work: gather context, plan, execute actions, verify outputs, ask for approval, and leave behind an artifact.
- Long-running agents need durable memory and project artifacts, not giant prompts. The official Codex post uses spec, plan, implementation, and documentation markdown files to prevent drift.
- The repo's `Agent Goals And Dynamic Workflows` page treats Goals as durable loops with verifiable exit criteria, constraints, boundaries, progress reports, and blocked conditions.
- The `Agentic Engineering Practices` page adds the operator lesson: prompt contracts should specify role, goal, deliverables, constraints, edge cases, verification, review loop, and completion standard.
- The narrative behind Codex is the evolution from assistive generation to delegated execution. That is the enterprise jump: AI moves from "help me think/write" to "work this bounded process, prove what happened, and hand me something reviewable."

## GTM And Enterprise Angles

The role is about turning early signal into enterprise opportunity. Strong talk tracks:

- **Usage to enterprise deployment:** "Where are employees already using ChatGPT or the API? What workflow is it touching? Who owns that process? What would make it safe to scale?"
- **Pilot to platform:** "What has to be true for this to become a governed, measured workflow rather than a team-level experiment?"
- **Regulated industries:** Financial Services, Life Sciences, and Retail need the same pattern: trustworthy data access, permissioning, audit trails, domain-specific evaluation, and careful human approval.
- **Business value translation:** product cycle compression, customer delivery speed, research/reporting acceleration, better internal data access, and workflow-level automation are more compelling than model benchmarks.
- **Outbound relevance:** use category intent, OpenAI/Anthropic/Codex engagement, AI governance posts, hiring signals, events, tech-stack clues, competitor usage, and workflow pain as entry points.

## Interview-Ready Points Of View

- "The frontier model is only one layer. Enterprise value shows up when the model is connected to trusted data, permissioned tools, evals, and human approval."
- "Codex matters beyond engineering because it teaches the operating pattern for agents: plan, act, verify, repair, and report."
- "A great OpenAI seller should know how to move from excitement to governance: what data is in scope, what actions are allowed, what needs approval, and how success will be measured."
- "The strongest enterprise opportunities start where there is already usage or urgency, but the buyer needs help translating it into a safe, durable deployment."
- "In APAC, regulated-industry trust and local operating context matter. Singapore can be a strong wedge for financial services, regional HQs, and cross-border enterprise workflows."

## Open Questions To Prepare

- Which APAC sectors are currently seeing the fastest ChatGPT Enterprise or API pull: banks, insurers, pharma, retail, government-linked enterprises, fintechs, or regional conglomerates?
- What account signals does OpenAI's GTM team already expose to BDRs: product usage, API volume, inbound, event attendance, content engagement, partner signals, or customer stories?
- How are Strategic BDRs expected to partner with Account Directors: account planning, multi-threading, discovery notes, stakeholder maps, competitive intel, or outbound experimentation?
- What separates a qualified OpenAI enterprise opportunity from a team-level AI enthusiast?
- How does OpenAI want sellers to talk about Codex and agents with non-engineering buyers?
- Where does OpenAI want to draw the boundaries between ChatGPT, Codex, Apps, connectors, and any broader workbench surface when selling against Claude Cowork?
- What competitive claims are acceptable against Anthropic in APAC enterprise conversations, and which should be avoided unless backed by approved internal data?

## Source Index

### Compiled Wiki Pages

- [Agent Framework Landscape](../agent-frameworks/agent-framework-landscape.md)
- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Vendor Agentic Engineering Blogs, Last Six Months](../ai-coding/vendor-agentic-engineering-blogs-2026.md)
- [Agent Skill Libraries And Requirements](../ai-coding/agent-skill-libraries-and-requirements.md)
- [AI Engineering Talks On Agentic Coding](../ai-coding/ai-engineering-talks-on-agentic-coding.md)
- [Devin Managed Agent Workflows](../ai-coding/devin-managed-agent-workflows.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
- [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [High-Signal Enterprise Sales](../gtm-sales/high-signal-enterprise-sales.md)
- [Acme Agentic GTM OS](../gtm-sales/acme-agentic-gtm-os.md)
- [SEO/AEO/GEO Content Systems](../marketing/seo-aeo-geo-content-systems.md)
- [OpenClaw Architecture And Operating Model](../openclaw/openclaw-architecture-and-operating-model.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
- [Workflow Hustle While Job Hunting](../workflow-hustle/workflow-hustle-while-job-hunting.md)
- [Desktop Archive Saved Inputs](2026-06-11-desktop-archive-saved-inputs.md)
- [Sunder Sync Source Captures](2026-06-11-sunder-sync-source-captures.md)

### Official OpenAI / OpenAI Developers / OpenAI GitHub Captures

- [Vendor Blog Six-Month Sweep Manifest](../../raw/intentional/pasted/2026-06-14-vendor-blog-six-month-sweep-manifest.md)
- [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md)
- [Updates for developers building with voice](../../raw/intentional/web/2025-12-22-openai-updates-for-developers-building-with-voice-openai-developers.md)
- [Supercharging Codex with JetBrains MCP at Skyscanner](../../raw/intentional/web/2026-01-11-openai-supercharging-codex-with-jetbrains-mcp-at-skyscanner-openai-developers.md)
- [Testing Agent Skills Systematically with Evals](../../raw/intentional/web/2026-06-13-testing-agent-skills-systematically-with-evals.md)
- [15 lessons learned building ChatGPT Apps](../../raw/intentional/web/2026-02-04-openai-15-lessons-learned-building-chatgpt-apps-openai-developers.md)
- [Shell + Skills + Compaction](../../raw/intentional/web/2026-02-11-openai-shell-skills-compaction-tips-for-long-running-agents-that-do-real-work-o.md)
- [Run long horizon tasks with Codex](../../raw/intentional/web/2026-02-23-openai-run-long-horizon-tasks-with-codex-openai-developers.md)
- [Building frontend UIs with Codex and Figma](../../raw/intentional/web/2026-02-26-openai-building-frontend-uis-with-codex-and-figma-openai-developers.md)
- [Using skills to accelerate OSS maintenance](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md)
- [From prompts to products: One year of Responses](../../raw/intentional/web/2026-03-11-openai-from-prompts-to-products-one-year-of-responses-openai-developers.md)
- [Designing delightful frontends with GPT-5.4](../../raw/intentional/web/2026-03-20-openai-designing-delightful-frontends-with-gpt-5-4-openai-developers.md)
- [How Perplexity brought voice search to millions using the Realtime API](../../raw/intentional/web/2026-03-25-openai-how-perplexity-brought-voice-search-to-millions-using-the-realtime-api-o.md)
- [OpenAI Codex use cases](../../raw/intentional/web/2026-06-11-openai-codex-use-cases.md)
- [OpenAI Codex Security setup docs](../../raw/intentional/web/2026-06-11-openai-codex-security-setup-docs.md)
- [OpenAI codex-plugin-cc README](../../raw/intentional/web/2026-06-12-openai-codex-plugin-cc-readme.md)
- [OpenAI Cookbook: Using Goals in Codex](../../raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex.md)

### Official OpenAI X Captures And Product Announcements

- [OpenAI DevDay is back](../../raw/intentional/x/2049534651702956103-openai-openai-devday-is-back-san-francisco-september-29.md)
- [OpenAI DevDay early ticket / GPT-5.5 build prompt](../../raw/intentional/x/2049535650626785334-openai-want-to-secure-an-early-ticket-to-openai-devday-build-something-with-gpt-5-5-and-im.md)
- [Codex for almost everything](../../raw/intentional/x/2044827705406062670-openai-codex-for-almost-everything-it-can-now-use-apps-on-your-mac-connect-to-more-of-your.md)
- [OpenAIDevs Codex memories expansion](../../raw/intentional/x/2046288243768082699-openaidevs-last-week-we-released-a-preview-of-memories-in-codex-today-we-re-expanding-the.md)
- [OpenAIDevs GPT-5.5 agentic coding model](../../raw/intentional/x/2047377234806374756-openaidevs-gpt-5-5-is-our-strongest-agentic-coding-model-to-date-it-reaches-82-7-on-termin.md)
- [OpenAI Codex in ChatGPT mobile app](../../raw/intentional/x/2055016850849993072-openai-you-ve-been-asking-for-this-one-now-in-preview-codex-in-the-chatgpt-mobile-app-star.md)
- [OpenAIDevs Goal graduates](../../raw/intentional/x/2057530209470210453-openaidevs-goal-has-graduated-from-an-experiment-for-tasks-big-and-small-codex-gets-your-w.md)
- [OpenAIDevs in-house AI data agent](../../raw/intentional/x/2016943147239329872-openaidevs-inside-our-in-house-ai-data-agent-it-reasons-over-600-pb-and-70k-datasets-enabl.md)
- [OpenAIDevs new primitives for building agents](../../raw/intentional/x/2021725246244671606-openaidevs-we-just-announced-new-primitives-for-building-agents-here-are-10-tips-on-runnin.md)
- [OpenAI math breakthrough post](../../raw/intentional/x/2057176201782075690-openai-today-we-share-a-breakthrough-on-the-planar-unit-distance-problem-a-famous-open-que.md)

### Direct Codex Operator And Harness Sources

- [Codex maxxing and GTM agent opportunity bundle](../../raw/intentional/pasted/2026-06-10-codex-maxxing-and-gtm-agent-opportunity-bundle.md)
- [Jason Liu Codex maxxing](../../raw/intentional/web/2026-06-10-jason-liu-codex-maxxing.md)
- [Agent workflow links: goals, classifier, Manus outreach, scratch logs](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md)
- [Harness/Codex/company-research/video workflow bundle](../../raw/intentional/pasted/2026-06-11-harness-codex-company-research-video-workflow-and-clay-mcp-bundle.md)
- [Vox Claude Code/Codex prompt templates screenshots](../../raw/intentional/pasted/2026-06-18-vox-claude-code-codex-prompt-templates-screenshots.md)
- [OpenAI harness engineering Codex agent-first](../../raw/intentional/pasted/sunder-sync-2026-06-11/154-openai-harness-engineering-codex-agent-first.md)
- [Codex Guidelines](../../raw/intentional/pasted/sunder-sync-2026-06-11/016-codex-guidelines.md)
- [Codex multi-agent playbook setup guide](../../raw/intentional/pasted/sunder-sync-2026-06-11/088-codex-multi-agent-playbook-part-1-setup-guide-twitter-llmjunky-2024152021436121220-full.md)
- [LLMJunky Codex multi-agent playbook X capture](../../raw/intentional/x/2024152021436121220-llmjunky-codex-multi-agent-playbook-part-1-setup-guide-greetings-builders-if-you-ve-been-u.md)
- [Alxfazio headless maxxing / codex exec](../../raw/intentional/x/2032556496781779302-alxfazio-headless-maxxing-in-this-article-i-ll-walk-through-how-to-wrap-codex-exec-for-you.md)
- [Kangwook Lee Codex context compaction investigation](../../raw/intentional/x/2028955292025962534-kangwook-lee-investigating-how-codex-context-compaction-works-for-non-codex-models-the-ope.md)
- [Dominik Kundel Codex features/memories/plugins](../../raw/intentional/x/2046297434205430130-dkundel-how-i-stopped-needing-to-explain-things-to-codex-last-week-we-launched-a-series-of.md)
- [Dominik Kundel guide to Goal](../../raw/intentional/x/2062650378089594955-dkundel-a-guide-to-goal-we-launched-the-goal-mode-or-goal-as-a-way-to-help-you-have-codex.md)
- [Reach VB prompt, goal, Colab run with Codex](../../raw/intentional/x/2057880274348695995-reach-vb-a-prompt-a-goal-and-a-colab-run-with-codex-couple-days-back-swyx-posted-a-challen.md)
- [Reach VB Codex transformer challenge follow-up](../../raw/intentional/x/2057882419257311652-reach-vb-couple-days-back-swyx-posted-a-challenge-code-a-10m-transformer-in-jax-flax-optax.md)
- [Cryps1s secure mobile control for Codex](../../raw/intentional/x/2055023414608597085-cryps1s-secure-mobile-control-for-codex-on-your-laptop-best-paired-with-auto-review-our-de.md)
- [Codex video editing/tutorials transcript](../../raw/intentional/youtube/2026-06-11-codex-just-replaced-1000-hours-of-video-editing-tutorials.md)
- [Awesome Codex Skills README](../../raw/intentional/web/2026-06-11-awesome-codex-skills-readme.md)
- [Bring Your AI MCP](../../raw/intentional/web/2026-06-13-bring-your-ai-mcp.md)
- [EveryInc Compound Engineering Plugin README](../../raw/intentional/web/2026-06-12-everyinc-compound-engineering-plugin-readme.md)
- [obra Superpowers README](../../raw/intentional/web/2026-06-12-obra-superpowers-readme.md)
- [Open Design README](../../raw/intentional/web/2026-06-11-open-design-readme.md)
- [AgriciDaniel Claude SEO / Codex SEO snapshot](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md)

### Evolution Of Agentic Coding Sources

- [AI Engineering Talks On Agentic Coding](../ai-coding/ai-engineering-talks-on-agentic-coding.md)
- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Vendor Agentic Engineering Blogs, Last Six Months](../ai-coding/vendor-agentic-engineering-blogs-2026.md)
- [Run long horizon tasks with Codex](../../raw/intentional/web/2026-02-23-openai-run-long-horizon-tasks-with-codex-openai-developers.md)
- [Coding Agents 101: The Art of Actually Getting Things Done](../../raw/intentional/web/2026-06-12-devin-coding-agents-101-the-art-of-actually-getting-things-done.md)
- [Cursor: The third era of AI software development](../../raw/intentional/web/2026-02-26-cursor-the-third-era-of-ai-software-development.md)
- [Context Engineering for Coding Agents](../../raw/intentional/web/2026-06-13-context-engineering-for-coding-agents.md)
- [Julian de Angelis coding-agent harness note](../../raw/intentional/x/2027888587975569534-juliandeangeiis-the-coding-agent-harness-how-to-actually-make-ai-coding-agents-work-at-sca.md)
- [Viv Trivedy anatomy of an agent harness](../../raw/intentional/x/2031408954517971368-vtrivedy10-the-anatomy-of-an-agent-harness-tldr-agent-model-harness-harness-engineering-is.md)
- [The agentic workload](../../raw/intentional/pasted/sunder-sync-2026-06-11/170-the-agentic-workload-igor-zalutski.md)
- [OpenAI harness engineering Codex agent-first](../../raw/intentional/pasted/sunder-sync-2026-06-11/154-openai-harness-engineering-codex-agent-first.md)

### OpenAI Business, Market, And GTM Signals

- [LSEG/OpenAI financial-services analysis](../../raw/intentional/x/2064833270643360187-ollobrains-this-is-not-just-a-financial-services-ai-customer-story-it-is-a-preview-of-how.md)
- [OpenAI unified ChatGPT/Codex/Atlas workbench analysis](../../raw/intentional/x/2062451606197825614-ollobrains-openai-is-trying-to-turn-chatgpt-from-a-chatbot-into-the-command-center-for-kno.md)
- [Generative AI S-curves with OpenAI usage/revenue/Codex WAU disclosures](../../raw/intentional/x/2065067184984928509-thevalueist-generative-ai-s-6-overlapping-s-curves-infrastructure-models-agents-apps-consu.md)
- [State of AI June 2026 with OpenAI Codex usage and Anthropic Mythos/Fable comparison](../../raw/intentional/x/2066178417486118981-singularityhsn-state-of-ai-june-2026-data-and-thesis-thesis-ai-progress-has-moved-from-cha.md)
- [Nichochar great convergence / OpenAI enterprise refocus thesis](../../raw/intentional/x/2039739581772554549-nichochar-the-great-convergence-over-the-last-year-a-strange-thing-has-happened-in-tech-ve.md)
- [Sunder sync great convergence duplicate](../../raw/intentional/pasted/sunder-sync-2026-06-11/162-the-great-convergence-nichochar.md)
- [Career ops enterprise sales playbook](../../raw/intentional/pasted/2026-06-16-career-ops-enterprise-sales-playbook.md)
- [Salescraft LinkedIn posts with OpenAI enterprise rep / credits notes](../../raw/intentional/pasted/2026-06-16-salescraft-patrick-spychalski-eric-nowoslawski-linkedin-posts.md)
- [Chris Pisarski frontier labs hiring sales/GTM talent](../../raw/intentional/x/2057183340273230228-chrispisarski-every-frontier-lab-is-hiring-sales-gtm-talent-right-now-this-is-the-summary.md)
- [Vlad Feinberg frontier lab career/wealth/job market post](../../raw/intentional/x/2056383124829872466-feinbergvlad-how-to-land-a-job-at-a-frontier-lab-https-t-co-ohiqlgbmbc.md)
- [Bosmeny YC OpenAI token offer](../../raw/intentional/x/2056914385814401238-bosmeny-a-mic-drop-moment-ycombinator-tonight-sama-just-offered-2m-in-openai-tokens-to-eve.md)
- [Greg Brockman YC API credits post](../../raw/intentional/x/2056948285038887255-gdb-openai-offering-to-invest-2m-in-api-credits-in-every-ycombinator-startup-in-the-curren.md)
- [Ashish Tuli AI credits as GTM strategy](../../raw/intentional/x/2058033486779527378-ashishtuli-ai-credits-are-becoming-a-go-to-market-strategy-openai-s-yc-offer-made-the-patt.md)
- [Reuters Malta ChatGPT Plus deal](../../raw/intentional/x/2055660819082252656-reuters-openai-seals-deal-in-malta-to-give-all-maltese-access-to-chatgpt-plus-https-t-co-2.md)
- [OpenAI close to funding phase / valuation signal](../../raw/intentional/x/2024384999773131104-wanso-log-signal-report-openai-is-near-finalizing-a-new-funding-phase-100b-with-valuation.md)
- [TradFi OpenAI funding round note](../../raw/intentional/x/2024307869341147499-tradfi-openai-close-to-finalizing-first-phase-of-new-funding-round-likely-to-bring-in-more.md)
- [SoftBank borrowing against OpenAI stock note](../../raw/intentional/x/2064601087768662077-ns123abc-breaking-softbank-tried-to-borrow-6-billion-against-its-13-openai-stock-to-keep-f.md)
- [JV Nixon OpenAI revenue report note](../../raw/intentional/x/1811278381184672156-jvnixon-the-report-on-openai-s-revenue-by-futureresearch-is-out-showing-1-9b-for-chatgpt-p.md)
- [Amir AI model/application revenue-share note](../../raw/intentional/x/2056041152500142259-amir-anthropic-amp-openai-s-share-of-ai-model-and-application-revenues-generated-by-34-top.md)
- [Peter Berezin OpenAI price cuts note](../../raw/intentional/x/2064901987817206035-peterberezinbca-i-got-a-lot-of-flack-when-i-said-this-before-but-i-continue-to-think-that.md)
- [WSJ OpenAI price cuts capture](../../raw/intentional/x/2064885410761671041-wsj-openai-is-considering-drastic-price-cuts-as-it-seeks-to-win-over-customers-from-archri.md)
- [Arakharazian Anthropic beats OpenAI in business adoption note](../../raw/intentional/x/2054563750548492549-arakharazian-anthropic-beats-openai-in-business-adoption-for-the-first-time-per-tryramp-da.md)
- [NYTimes Musk/OpenAI lawsuit rejected](../../raw/intentional/x/2056432766292492368-nytimes-breaking-news-a-jury-rejected-elon-musk-s-lawsuit-accusing-openai-of-putting-comme.md)
- [ZeffMax statute-of-limitations explanation](../../raw/intentional/x/2056476111459213511-zeffmax-i-m-seeing-lots-of-confusion-about-why-the-statute-of-limitations-issue-came-to-a.md)
- [Sporadica Musk/OpenAI suit comment](../../raw/intentional/x/2056438777258893731-sporadica-i-just-don-t-know-how-people-expected-elon-to-have-a-legit-case-it-was-always-so.md)
- [Max Uf nationalization analysis](../../raw/intentional/x/2062563590041645131-max-uf-new-from-me-a-literal-federal-takeover-of-openai-or-anthropic-remains-highly-unlike.md)
- [Hamandcheese nationalization analysis](../../raw/intentional/x/2062573851565772816-hamandcheese-nationalizing-ai-companies-is-a-terrible-idea-but-if-it-happens-it-s-likely-t.md)
- [Aaron Rupar government equity stake quote](../../raw/intentional/x/2062971806315585555-atrupar-trump-says-he-s-interested-in-the-government-taking-equity-stakes-in-the-giant-ai.md)
- [David Krueger government equity stake quote](../../raw/intentional/x/2063037960820490684-davidskrueger-things-are-moving-so-fast.md)
- [Jeff Stein WSJ government-shares detail](../../raw/intentional/x/2062887246617800750-jstein-star-wall-street-journal-confirming-our-reporting-today-with-some-new-details-that.md)
- [Neil Chilson regulatory-capture comment](../../raw/intentional/x/2062899104070385754-neil-chilson-partial-government-ownership-of-private-companies-is-regulatory-capture-on-st.md)
- [Robert Wiblin California regulatory-risk post](../../raw/intentional/x/2064300795525238945-robertwiblin-could-frontier-ai-model-developers-cut-ties-with-california-to-avoid-being-co.md)
- [Miranda Nazzaro Sam Altman / Greg Brockman nonprofit note](../../raw/intentional/x/2064324466260283590-mirandanazzaro-new-openai-amp-sam-altman-want-distance-from-greg-brockman-s-ties-to-leadin.md)
- [METR frontier risk report with OpenAI participation](../../raw/intentional/x/2056800023149760666-metr-evals-could-an-ai-company-lose-control-of-its-own-agents-to-find-out-anthropic-google.md)
- [AI slowdown leadership observation](../../raw/intentional/x/2064254768403378394-s-oheigeartaigh-important-and-noteworthy-that-this-year-we-ve-had-demis-hassabis-google-de.md)
- [TokenandoAI Stratechery Anthropic/OpenAI market-segmentation note](../../raw/intentional/x/2064726041730363503-tokenandoai-on-june-10-2026-ben-thompson-published-an-analysis-of-the-claude-fable-5-launc.md)
- [David Sacks Anthropic safety/marketing critique referencing OpenAI](../../raw/intentional/x/2065120386660880765-davidsacks-if-you-were-wondering-what-the-pause-was-all-about-ben-thompson-stratechery-has.md)
- [TheRealAdamG LSEG/OpenAI pointer](../../raw/intentional/x/2064724583391858879-therealadamg-https-t-co-viqctkwade-lseg-combines-openai-with-its-global-data-platform-to-a.md)
- [Physical AI post referencing OpenAI-backed 1X](../../raw/intentional/x/2062505722068500626-viks-rum-all-you-need-to-know-about-physical-ai-a-strange-thing-has-started-showing-up-in.md)
- [Karpathy joins Anthropic personal update](../../raw/intentional/x/2056753169888334312-karpathy-personal-update-i-ve-joined-anthropic-i-think-the-next-few-years-at-the-frontier.md)
- [Vijay Thirumalai Karpathy joins Anthropic note](../../raw/intentional/x/2056775329616978205-vijaythirumalai-i-simply-cannot-fathom-this-move-dario-doesn-t-look-that-charismatic-to-me.md)

### Claude / Anthropic Competitive Context Sources

- [The evolution of agentic surfaces: building with Claude Managed Agents](../../raw/intentional/web/2026-06-10-claude-the-evolution-of-agentic-surfaces-building-with-claude-managed-agents.md)
- [New in Claude Managed Agents: schedules and vaults](../../raw/intentional/web/2026-06-09-claude-new-in-claude-managed-agents-run-agents-on-a-schedule-and-store-environm.md)
- [Observability for developers building connectors](../../raw/intentional/web/2026-06-08-claude-observability-for-developers-building-connectors.md)
- [The Claude Cowork product guide](../../raw/intentional/web/2026-06-05-claude-the-claude-cowork-product-guide.md)
- [How one Anthropic seller rebuilt his team's workflows with Claude Code](../../raw/intentional/web/2026-06-05-claude-how-one-anthropic-seller-rebuilt-his-team-s-workflows-with-claude-code.md)
- [Running an AI-native engineering org](../../raw/intentional/web/2026-06-03-claude-running-an-ai-native-engineering-org.md)
- [How Anthropic enables self-service data analytics with Claude](../../raw/intentional/web/2026-06-03-claude-how-anthropic-enables-self-service-data-analytics-with-claude.md)
- [Best practices for getting started with Claude Cowork](../../raw/intentional/web/2026-06-03-claude-best-practices-for-getting-started-with-claude-cowork.md)
- [A harness for every task: dynamic workflows in Claude Code](../../raw/intentional/web/2026-06-02-claude-a-harness-for-every-task-dynamic-workflows-in-claude-code.md)
- [Introducing dynamic workflows in Claude Code](../../raw/intentional/web/2026-05-28-claude-introducing-dynamic-workflows-in-claude-code.md)
- [Zero Trust for AI agents](../../raw/intentional/web/2026-05-27-claude-zero-trust-for-ai-agents.md)
- [Claude now works with more security and compliance tools](../../raw/intentional/web/2026-05-21-claude-claude-now-works-with-more-security-and-compliance-tools.md)
- [How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book](../../raw/intentional/web/2026-05-20-claude-how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account.md)
- [How Claude Code works in large codebases](../../raw/intentional/web/2026-05-14-claude-how-claude-code-works-in-large-codebases-best-practices-and-where-to-sta.md)
- [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](../../raw/intentional/web/2026-05-12-claude-how-anthropic-s-cybersecurity-team-built-a-threat-detection-platform-wit.md)
- [Deploying Claude across financial services](../../raw/intentional/web/2026-05-05-claude-deploying-claude-across-financial-services.md)
- [How Kepler built verifiable AI for financial services with Claude](../../raw/intentional/web/2026-04-30-claude-how-kepler-built-verifiable-ai-for-financial-services-with-claude.md)
- [Building AI agents for the enterprise](../../raw/intentional/web/2026-04-30-claude-building-ai-agents-for-the-enterprise.md)
- [Deploying agentic AI across the enterprise with Claude Cowork](../../raw/intentional/web/2026-04-29-claude-deploying-agentic-ai-across-the-enterprise-with-claude-cowork.md)
- [Making Claude Cowork ready for enterprise](../../raw/intentional/web/2026-04-09-claude-making-claude-cowork-ready-for-enterprise.md)
- [Audit Claude Platform activity with the Compliance API](../../raw/intentional/web/2026-03-30-claude-audit-claude-platform-activity-with-the-compliance-api.md)
- [Claude Enterprise, now available self-serve](../../raw/intentional/web/2026-02-12-claude-claude-enterprise-now-available-self-serve.md)
- [How leading retailers are turning AI pilots into enterprise-wide transformation](../../raw/intentional/web/2026-01-28-claude-how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transfo.md)
- [Anthropic growth marketing article](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md)
- [Building agents with the Claude Agent SDK](../../raw/intentional/web/2026-06-13-building-agents-with-the-claude-agent-sdk.md)

### Direct OpenAI vs Claude Operator And Market Notes

- [OpenAI unified ChatGPT/Codex/Atlas workbench analysis](../../raw/intentional/x/2062451606197825614-ollobrains-openai-is-trying-to-turn-chatgpt-from-a-chatbot-into-the-command-center-for-kno.md)
- [Anthropic beats OpenAI in business adoption note](../../raw/intentional/x/2054563750548492549-arakharazian-anthropic-beats-openai-in-business-adoption-for-the-first-time-per-tryramp-da.md)
- [Stratechery Anthropic/OpenAI market-segmentation note](../../raw/intentional/x/2064726041730363503-tokenandoai-on-june-10-2026-ben-thompson-published-an-analysis-of-the-claude-fable-5-launc.md)
- [WSJ OpenAI price cuts capture](../../raw/intentional/x/2064885410761671041-wsj-openai-is-considering-drastic-price-cuts-as-it-seeks-to-win-over-customers-from-archri.md)
- [Peter Berezin model-provider commoditization note](../../raw/intentional/x/2064901987817206035-peterberezinbca-i-got-a-lot-of-flack-when-i-said-this-before-but-i-continue-to-think-that.md)
- [sameQCU switching from Claude Opus to Codex note](../../raw/intentional/x/2056532814364086522-sameqcu-switching-from-claude-opus-to-codex-makes-you-feel-like-you-re-so-smart-for-watchi.md)
- [Alex Finn dual Codex and Claude Code setup](../../raw/intentional/x/2012653446349131953-alexfinn-this-is-the-best-ai-coding-setup-ever-codex-5-2-xhigh-on-the-left-claude-code-opu.md)
- [Karpathy notes on Claude coding and Claude/Codex phase shift](../../raw/intentional/x/2015883857489522876-karpathy-a-few-random-notes-from-claude-coding-quite-a-bit-last-few-weeks-coding-workflow.md)
- [Meir Cohen task-router problem with Claude Code and Codex CLI](../../raw/intentional/x/2024389381486756217-meircohen-the-problem-i-run-a-personal-ai-agent-oz-that-spawns-sub-agents-for-heavy-work-e.md)
- [Meir Cohen task-router solution using Claude Code or Codex](../../raw/intentional/x/2024389391527882923-meircohen-the-solution-a-task-router-that-analyzes-every-incoming-task-and-routes-it-to-th.md)
- [Geoffrey Litt using Claude Managed, Claude Code, and Codex together](../../raw/intentional/x/2064731975009681521-geoffreylitt-dbmikus-we-use-claude-via-claude-managed-and-cursor-via-their-cloud-agents-bo.md)
- [Great convergence: OpenAI, Anthropic, Cursor, Notion, and others converge on agents](../../raw/intentional/pasted/sunder-sync-2026-06-11/162-the-great-convergence-nichochar.md)
- [Agent harness is the real product](../../raw/intentional/pasted/sunder-sync-2026-06-11/151-agent-harness-is-the-real-product.md)
- [The agentic workload](../../raw/intentional/pasted/sunder-sync-2026-06-11/170-the-agentic-workload-igor-zalutski.md)
- [Vox Claude Code/Codex prompt templates screenshots](../../raw/intentional/pasted/2026-06-18-vox-claude-code-codex-prompt-templates-screenshots.md)
- [Super good blog about Codex and Claude](../../raw/intentional/pasted/archive-2026-06-11/72-super-good-blog-about-codex-and-claude.md)
- [AgriciDaniel Claude SEO / Codex SEO snapshot](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md)

### ChatGPT, AI Search, And Demand Signals

- [ChatGPT Apps lessons](../../raw/intentional/web/2026-02-04-openai-15-lessons-learned-building-chatgpt-apps-openai-developers.md)
- [Chris Pisarski ChatGPT share of AI-sourced qualified leads](../../raw/intentional/x/2034325547917115475-chrispisarski-chatgpt-went-from-43-of-our-ai-sourced-qualified-leads-in-september-to-3-in.md)
- [Alex Groberman Airbnb/Shopify AI traffic conversion note](../../raw/intentional/x/2054551085277192671-alexgroberman-airbnb-says-chatgpt-traffic-converts-better-than-google-shopify-says-ai-traf.md)
- [Alex Groberman Reddit/Wikipedia ChatGPT citations](../../raw/intentional/x/2058170784351404277-alexgroberman-reddit-and-wikipedia-account-for-25-of-chatgpt-citations-it-s-hard-to-contro.md)
- [Alex Groberman AI referral traffic note](../../raw/intentional/x/2054910112742171055-alexgroberman-here-s-a-fun-fact-every-visitor-who-clicks-through-to-your-site-from-an-ai-r.md)
- [Microsoft guide to traffic from ChatGPT](../../raw/intentional/x/2059664468507000863-alexgroberman-microsoft-dropped-an-official-here-is-how-to-get-traffic-from-chatgpt-guide.md)
- [Nabeel Qureshi ChatGPT-generated story prize](../../raw/intentional/x/2056397504824963296-nabeelqu-well-this-is-a-first-a-chatgpt-generated-story-won-a-prestigious-literary-prize-t.md)

## See Also

- [Startup Funding Signal Job Search](../job-apps/startup-funding-signal-job-search.md)
- [AI-Native Account Intelligence](../gtm-sales/ai-native-account-intelligence.md)
- [Marketing Analytics And FDA Enablement](../marketing/marketing-analytics-and-fda-enablement.md)
- [Content Ops And Editorial Systems](../marketing/content-ops-and-editorial-systems.md)
