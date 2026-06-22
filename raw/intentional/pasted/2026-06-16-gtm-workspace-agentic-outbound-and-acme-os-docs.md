---
type: raw_capture
source_type: pasted
title: "GTM workspace agentic outbound and Acme OS docs"
url: "/Users/sethlim/Documents/gtm-workspace"
collected_at: 2026-06-16T04:58:44Z
published_at: "Unknown"
capture_quality: complete
status: raw
trust_lane: intentional
---

# GTM workspace agentic outbound and Acme OS docs

Source: /Users/sethlim/Documents/gtm-workspace

## Capture Text

## Agentic outbound stack 2026

Source file: `/Users/sethlim/Documents/gtm-workspace/agentic-outbound-stack-2026.md`

```markdown
# Agent‑Powered Multi‑Channel Outbound 2026: LinkedIn + Cold‑Email Playbook for Autonomous Scaling

## Executive Summary

The landscape of B2B outbound in 2026 has fundamentally shifted from static, rule-based SaaS sequencers to autonomous, agentic workflows. With average cold email reply rates dropping to 3.4% [1] and SDR churn costing companies $78,000 to $149,000 per departure [2], operators are replacing traditional headcount with AI agents. Vercel successfully replaced 9 out of 10 inbound SDRs with an AI agent in just six weeks, maintaining conversion rates while improving speed [3]. 

The winning 2026 architecture combines data enrichment (Clay), channel-specific sequencers (Instantly/Smartlead for email, Expandi/HeyReach for LinkedIn), and an agent orchestration layer (Manus or Claude Code) [4] [5] [6] [7]. This stack allows for dynamic, multi-channel playbooks—such as Jed Mahrle's 10-Day Multi-Channel Sequence [8] —that adapt in real-time to prospect behavior, handling everything from initial research to AI-driven reply triage in under 5 minutes [9].

## 1. Market Context – Why Agentic Outbound Is the New Normal

In 2026, outbound sales is recognized as a high-volume, repetitive process that follows predictable patterns, making it the primary target for AI agents [10]. The traditional model of hiring large SDR teams is being upended by "forward deployed engineers" and AI sales agents [11]. Vercel's deployment of an AI sales agent allowed them to reduce their SDR team from 10 to 1 in six weeks, shifting the remaining human effort to outbound and deeper relationship building [3] [12] [13]. This transition is driven by the need to combat declining baseline metrics, such as the 40% average open rate and 3.4% reply rate [1], by utilizing agents that can execute hyper-personalized, multi-channel campaigns at scale.

## 2. Core Stack Architecture

The modern outbound engine requires a tri-layer architecture to function autonomously without triggering spam filters or platform bans.

### 2.1 Data Enrichment (Clay)

Clay serves as the foundational data layer. In 2026, operators use Clay's AI Agent (Claygent) to visit websites, extract specific information, and deliver structured results [14]. Agencies generating $4M ARR cite Clay's AI Agent as their "secret weapon" for finding the right data [15]. Teams utilize webhooks—automated messages sent when a specific event occurs—to push this real-time data directly to their agent orchestrators [16].

### 2.2 Channel Engines

For execution, operators rely on specialized tools for email and LinkedIn to manage deliverability and safety.

| Channel | Tool | Key Capabilities & 2026 Positioning |
| :--- | :--- | :--- |
| **Email** | Smartlead | Strong for API-heavy technical users prioritizing raw sending volume; features AI reply handling [7] [17]. |
| **Email** | Instantly | Offers AI agents for research, campaign creation, and an AI Reply Agent that handles responses in under 5 minutes [9]. |
| **LinkedIn** | HeyReach | Cloud-based automation with safe daily limits (around 200 actions per day) that automatically pauses when caps are hit [6]. |
| **LinkedIn** | Expandi | Supports CSV imports, connection requests, and cloud-based automation with safe daily limits to reduce risk [18]. |

*Takeaway:* Smartlead and Instantly dominate the email layer due to their API flexibility and built-in AI reply handling, while cloud-based tools like HeyReach and Expandi are mandatory for LinkedIn to avoid account restrictions.

### 2.3 Agent Orchestration Layer

The orchestration layer acts as the "brain," connecting Clay's data to the channel engines.

| Agent Platform | 2026 Operator Consensus | Best Use Case |
| :--- | :--- | :--- |
| **Manus** | Highlighted as one of the top two AI tools for 2026 (alongside Claude) [4]. Powers agentic outbound systems that find leads, write outreach, and book calls [19]. | Full-stack orchestration and browser-based ops [20] [21]. |
| **Claude Code** | Utilizes "computer use" features with non-blocked browsers to send personalized LinkedIn connection requests automatically at scale [22]. | Complex, multi-step browser automation [22]. |
| **RunLobster** | Cited in startup stacks for doing the "actual work autonomously" like pulling metrics and ops [23]. | Lightweight ops and metric tracking [23]. |

*Takeaway:* Manus and Claude Code are the dominant orchestrators in 2026, capable of executing complex, cross-platform workflows that traditional Zapier/Make setups struggle to handle dynamically.

## 3. Agent vs. SaaS Trade-Off Matrix

While agents offer superior flexibility, traditional SaaS sequencers still have a place for simple, high-volume tasks.

| Feature | Agentic Execution (Manus/Claude) | Traditional SaaS (Lemlist/Dripify) |
| :--- | :--- | :--- |
| **Branching Logic** | Dynamic, context-aware (adapts to the specific text of a reply). | Rigid IF/THEN rules based on binary triggers (open/click). |
| **Personalization** | Real-time synthesis of web data via Claygent [14]. | Static merge tags ({{first_name}}, {{company}}). |
| **Cost at Scale** | Higher compute/token costs per lead. | Fixed monthly seat licenses; highly cost-effective for volume. |
| **Setup Complexity** | High; requires prompt engineering and webhook routing [16]. | Low; plug-and-play templates. |

*Takeaway:* Use agents when campaigns require deep research and complex branching based on prospect sentiment. Default to SaaS for simple, high-volume, low-touch email blasts.

## 4. LinkedIn Automation Risk Landscape

LinkedIn's detection algorithms in 2026 heavily penalize aggressive automation. The safety spectrum ranges from high-risk browser extensions to low-risk cloud platforms [24].

| Tool Type | Examples | Ban Risk | Safety Mechanisms |
| :--- | :--- | :--- | :--- |
| **Cloud Platforms** | Expandi, HeyReach, Botdog | Low | Smart throttling, random delays, weekend pauses, strict daily caps (e.g., 200 actions/day) [24] [6] [25]. |
| **Browser Extensions** | Dux-Soup | Medium/High | Requires gradual scaling (starting at 25 actions/day) and strict adherence to limits (100-250/week depending on Premium status) [26] [27]. |

*Takeaway:* Cloud tools are the only viable option for scaled agentic outbound in 2026. Extensions carry too much risk of account restriction if limits are pushed.

### 4.1 Daily/Weekly Action Caps

To avoid account restrictions, operators must adhere to strict limits. HeyReach caps accounts at around 200 actions per day, automatically pausing activity once hit [6]. Dux-Soup advises users to start conservatively at 25 actions per day and slowly increase, noting that weekly connection invitation limits are up to 100/week on Free plans and 250/week on Sales Navigator [26] [27].

## 5. Cold-Email Deliverability Stack (2026)

Deliverability management is the most critical component of the email stack, requiring dedicated infrastructure for warming domains, rotating IPs, and monitoring inbox placement [28].

| Component | 2026 Table Stakes |
| :--- | :--- |
| **Infrastructure** | 10+ domains and 20+ inboxes set up correctly [29]. |
| **Authentication** | Strict enforcement of DKIM, DMARC, and SPF. |
| **Warmup** | Continuous AI warmup using tools like Smartlead or Mailreach to maintain sender reputation [30] [31] [32]. |
| **Monitoring** | 30/60/90-day plans to measure inbox placement and fix spam issues [31]. |

*Takeaway:* Without a robust, multi-domain infrastructure and continuous AI warmup, scaling volume will inevitably result in emails slipping into Promotions or Spam folders [33].

### 5.1 Warm-up Service Comparison

Smartlead offers unlimited mailboxes and AI warmups built to land emails in the primary inbox [32]. Mailreach focuses on a proven 30/60/90-day plan to restore and measure inbox placement [31]. Instantly aims for 90%+ deliverability but users note that scaling quickly can still lead to spam issues without proper management [9] [33].

## 6. Clay + Agent Integration Patterns

The integration of Clay with AI agents is driving the highest conversion rates in 2026. Operators use Clay directly in ChatGPT to research people and companies, and draft personalized outbound [34]. The standard pattern involves using Claygent to scrape specific website data [14], which is then pushed via webhooks [16] to an orchestrator like Manus. This allows the agent to generate highly contextualized messaging based on live GTM data rather than stale database fields.

## 7. Multi-Step Orchestration Playbooks

Successful 2026 campaigns combine email and LinkedIn within the same sequence, using LinkedIn for warming up prospects [35]. Jed Mahrle's "Cold Prospect Playbook: The 10-Day Multi-Channel Sequence" is a prime example of this approach [8]. 

A standard agentic playbook looks like:
* **Day 0:** Agent uses Claude Code to send a personalized LinkedIn connection request [22].
* **Day 2:** Agent performs a profile view to trigger a notification.
* **Day 3:** If accepted, agent sends a contextual DM. If not, agent triggers a highly personalized cold email via Smartlead.
* **Day 7:** Agent drafts and sends a follow-up email based on the prospect's company news (via Claygent).
* **Day 10:** Multi-channel touch (e.g., voice note or final email).

## 8. Reply Handling & AI-Inbox Fusion

Handling replies manually is no longer viable at scale. Instantly provides an AI Reply Agent that auto-handles replies in under 5 minutes (costing 5 credits per AI reply) [9]. Similarly, Smartlead's AI email response generator reads, categorizes, and replies to leads automatically, significantly boosting reply rates and booked meetings [17]. These AI inboxes triage responses, handle objections, and route hot leads directly to calendar links without human intervention.

## 9. Cost, Scale, and ROI Modeling

The economics of outbound have shifted. With SDR churn costing up to $149,000 [2], the ROI of agentic systems becomes clear at scale.

| Metric | Traditional SDR Model | Agentic Outbound Model |
| :--- | :--- | :--- |
| **Personnel Cost** | High (Base + Commission + Churn costs) [2]. | Low (1 part-time GTM engineer can manage the system) [3]. |
| **Speed to Lead** | Hours to Days. | Under 5 minutes (via AI Reply Agents) [9]. |
| **Conversion Rates** | Baseline (3.4% reply rate) [1]. | Maintained or improved due to hyper-personalization [3]. |

*Takeaway:* While the initial setup cost and API/token usage for agents are higher than basic SaaS subscriptions, the elimination of SDR headcount and churn costs makes the agentic model vastly more profitable at medium-to-high volumes.

## 10. The "Agent Intern" Pattern

The "Agent Intern" pattern involves using tools like Manus or Claude Code as browser-based ops teammates rather than relying entirely on backend APIs. Claude Code's computer use feature allows it to operate a non-blocked browser to send personalized LinkedIn connection requests automatically [22]. Manus operates similarly, handling tasks that require navigating complex UIs that lack clean APIs [21]. This pattern wins when dealing with platforms that aggressively block API-based automation, as the agent mimics human browser behavior.

## 11. Expert Consensus & Recommended Stack

Top GTM operators in 2026 agree that the era of manual prospecting is over. Jason Bay emphasizes context-driven outbound and notes the changing future of cold calling and outreach [36] [37]. Tomasz Tunguz highlights the massive efficiency gains of replacing inbound SDRs with AI sales agents [3]. The consensus recommended stack for late 2025/2026 is:
1. **Data:** Clay + Claygent for live enrichment [14] [15].
2. **Orchestration:** Manus or Claude Code for decision-making and browser tasks [4] [22].
3. **Execution:** Smartlead/Instantly for email [9] [32] and HeyReach/Expandi for safe LinkedIn cloud automation [18] [6].

## 12. Implementation Blueprint

To transition to an agentic outbound model in 2026:
1. **Week 1 (Infrastructure):** Set up 10+ domains and 20+ inboxes. Connect them to Smartlead or Instantly and begin AI warmup [29] [30].
2. **Week 2 (Data Layer):** Build Clay tables. Configure Claygent to scrape target accounts and set up webhooks to push data to your orchestrator [16] [14].
3. **Week 3 (Orchestration):** Deploy Manus or Claude Code. Program the agent to receive Clay webhooks, draft personalized copy, and route it to Smartlead (email) or HeyReach (LinkedIn) [6] [22] [32].
4. **Week 4 (Testing & Triage):** Launch a small batch (50-100 leads). Activate the AI Reply Agent in Instantly/Smartlead to ensure responses are handled in under 5 minutes [9] [17]. Monitor LinkedIn daily limits strictly (max 200/day on cloud tools) [6].

## References

1. *Outbound Cost Calculator - Model Your True Cost Per Meeting | Orbis*. https://meetorbis.com/resources/outbound-calculator
2. *The State of B2B Outbound 2026: Benchmarks & Trends - Leadriver*. https://www.leadriver.io/blog/state-of-b2b-outbound-2026
3. *Vercel's AI Sales Agent : 10 SDRs Down to 1 in Six Weeks*. https://tomtunguz.com/vercel-ai-sales-agents-jeanne-grosser/
4. *Claude and Manus: My Top 2 AI Tools for 2026*. https://www.linkedin.com/posts/jakeheller1_if-i-could-only-use-two-ai-tools-for-the-activity-7413625276967972864-LQd9
5. *Clay - Woodpecker*. https://woodpecker.co/integrations/clay/
6. *Best LinkedIn connection automation tool: 8 rules for safe ...*. https://www.heyreach.io/blog/linkedin-connection-automation-tool
7. *Smartlead vs. Instantly & 5 More: 2026 Comparison for Pipeline Per ...*. https://instantly.ai/blog/smartlead-alternatives-pipeline-2026/
8. *Outbound Prospecting Changes After Jed Mahrle's Course - LinkedIn*. https://www.linkedin.com/posts/lillian-chukwueze_i-just-changed-my-entire-outbound-approach-activity-7459971758604009472-PSGx
9. *How to Achieve 90%+ Cold Email Deliverability in 2026 - Instantly*. https://instantly.ai/blog/how-to-achieve-90-cold-email-deliverability-in-2025/
10. *Best AI Agents for Business in 2026 (Ranked by Use Case)*. https://crea.la/blog/p/best-ai-agents
11. *The Sales Strategy Conquering the AI Market - Tomasz Tunguz*. https://tomtunguz.com/fde-cs/
12. *Vercel's AI Sales Agent : 10 SDRs Down to 1 in Six Weeks - LinkedIn*. https://www.linkedin.com/pulse/vercels-ai-sales-agent-10-sdrs-down-1-six-weeks-tomasz-tunguz-4dxtc
13. *I remember hosting a dinner of sales leaders to talk about AI.*. https://www.linkedin.com/posts/tomasztunguz_i-remember-hosting-a-dinner-of-sales-leaders-activity-7401315652772270080--xSv
14. *How to Use The Clay AI Claygent: A Beginner's Step-by-Step Guide*. https://utmost.agency/blogs/clay-ai-claygent/
15. *My agency hit $4M ARR with Clay as our 'secret' weapon.*. https://www.linkedin.com/posts/michel-lieben_my-agency-hit-4m-arr-with-clay-as-our-secret-activity-7314958569739620353-x3om
16. *What is Webhooks?*. https://www.clay.com/glossary/webhooks
17. *How Smartlead's AI Agent Handles Replies and Boosts Meetings*. https://www.smartlead.ai/blog/ai-email-response-generator
18. *Can Expandi or HeyReach fully replace my PhantomBuster LinkedIn ...*. https://www.reddit.com/r/b2bmarketing/comments/1o51bce/can_expandi_or_heyreach_fully_replace_my/
19. *Manus super-agent for team collaboration - Facebook*. https://www.facebook.com/groups/evolutionunleashedai/posts/24396819606605794/
20. *Armand Ruiz's Post - Manus Demo Walkthrough 2026*. https://www.linkedin.com/posts/armand-ruiz_manus-demo-walkthrough-2026-activity-7420797566151483392-3n1U
21. *Fred Tanzella - The Rise of Agentic AI*. https://www.linkedin.com/posts/fredtanzella_ai-agenticai-manus-activity-7305351417437847553-Zep_
22. *How to Use Claude Code Computer Use to Automate ...*. https://www.mindstudio.ai/blog/claude-code-computer-use-linkedin-outreach/
23. *What is your full AI Agent stack in 2026? : r/AI_Agents*. https://www.reddit.com/r/AI_Agents/comments/1rqnv3a/what_is_your_full_ai_agent_stack_in_2026/
24. *40 Best LinkedIn Automation Tools of 2026*. https://sbl.so/blog/best-linkedin-automation-tools/
25. *Best LinkedIn Automation Tools: 2026 Complete Guide - Botdog*. https://www.botdog.co/blog-posts/best-linkedin-automation-tools-2026
26. *LinkedIn Automation Safety Guide: How to Avoid Account ...*. https://www.dux-soup.com/blog/linkedin-automation-safety-guide-how-to-avoid-account-restrictions-in-2026
27. *LinkedIn Limits - Dux-Soup*. https://www.dux-soup.com/blog/linkedin-limits
28. *9 Best Cold Email Software Tools for Sales Teams in 2026*. https://pipeline.zoominfo.com/sales/cold-email-software
29. *The Ultimate Guide to Cold Email Deliverability in 2026 - YouTube*. https://www.youtube.com/watch?v=DIUObYQih3s
30. *Email Warm-Up Guide: Get to the Inbox Every Time - Smartlead*. https://www.smartlead.ai/blog/email-warm-up-guide
31. *Inbox Placement Guide: Fix Cold mail Deliverability in 2026*. http://mailreach.co/blog/inbox-placement-guide
32. *Smartlead.ai*. http://smartlead.ai/
33. *How's deliverability with Instantly.ai? : r/coldemail - Reddit*. https://www.reddit.com/r/coldemail/comments/1pmmvgc/hows_deliverability_with_instantlyai/
34. *Clay in ChatGPT: AI-Powered GTM Research for Sellers*. https://www.clay.com/blog/clay-in-chatgpt
35. *Outbound Marketing Best Practices for Q2 2026 | Harry Rawles ...*. https://www.linkedin.com/posts/harryrawles_q2-2026-outbound-playbook-activity-7437422942579445760-zahy
36. *Boosting Cold Calling Success with Context-Driven PBOs*. https://www.linkedin.com/posts/jasondbay_30-minutes-to-presidents-club-recorded-me-activity-7402013812528418818-ArbS
37. *The Future of Cold Calling: Why Voicemails and AI ...*. https://www.linkedin.com/posts/jasondbay_the-future-for-cold-calling-as-we-know-it-activity-7397302731100614656-KICw
```

## Acme GTM operating system playbook

Source file: `/Users/sethlim/Documents/gtm-workspace/docs/architecture/2026-05-24-acme-gtm-operating-system-playbook.md`

```markdown
---
title: Acme GTM operating system playbook
type: architecture
status: active
date: 2026-05-24
owner: Seth
---

# Acme GTM Operating System Playbook

This is the end-to-end operating model for Seth's Acme GTM workspace.

The short version:

```text
Live signals -> Notion current state -> Agent Command Center -> reviewed execution
            \-> repo/qmd durable memory
            \-> Drive formal artifacts
```

The system is deliberately boring. Notion shows current work. The repo explains and remembers. Drive stores finished customer/legal artifacts. Automations stage work, but reviewed human action remains the boundary for outbound messages, commercial commitments, and high-impact CRM fields.

## Source Of Truth Map

| Layer | System | Role | What belongs here | What must not live here |
|---|---|---|---|---|
| Live signals | Slack, Gmail, WhatsApp, Calendar, Granola | Fresh input | Asks, blockers, replies owed, meeting context, source evidence | Permanent memory by itself |
| Current operating state | Notion To-dos | Canonical action queue | Concrete actions, blockers, waiting items, decisions, strategic signals, review flags | Long-form research, signed docs, raw transcripts |
| CRM context | Simple CRM | Context around actions | Accounts, Deals, People, Meeting Activities | A second task list |
| Durable operating memory | Repo + qmd | Searchable brain | Skills, plans, account briefs, pulses, playbooks, generated artifacts, runbooks | Live customer/legal document truth |
| Formal artifact truth | Google Drive | Filing cabinet | SOWs, MSAs, signed docs, customer-facing docs, templates | Agent scratch notes |
| Delegated execution | Codex / Claude | Worker layer | Drafts, research, repo edits, reviewable artifacts | Silent commitments or hidden state |

## Canonical Daily Surfaces

Use these in order:

1. `Acme Sales CRM` launcher.
2. `Acme Sales CRM / To-dos` for action.
3. `Simple CRM` for account/deal/person/meeting context.
4. `Agent Command Center` views on the same To-dos database for delegation state.
5. Repo/qmd for long-form context and artifacts.
6. Drive for customer/legal finished documents.

The old Sales Command Center, old CRM databases, Timeline, Evidence, source-audit, and import residue are legacy. They are recovery sources only.

## Day-To-Day Loop

### 1. Intake

Inputs come from:

- manual user asks
- Slack and Slack DMs
- Gmail
- WhatsApp
- Calendar
- Granola
- Google Docs/Drive
- existing repo/qmd context

The intake rule is strict: create or update a To-do only for a real ask, blocker, waiting item, deadline, decision, reply owed, or strategic signal. Dedupe before creating. Preserve source refs.

Notion write rules:

- Task/action state goes to `Acme Sales CRM / To-dos`.
- Account/deal/person context goes to Simple CRM.
- Meetings go to `CRM Meeting Activities`.
- Meeting rows are not tasks. A To-do is created only when the meeting produces an action, blocker, decision, or strategic signal.

### 2. Meeting Memory

Calendar-driven meeting memory lives in `CRM Meeting Activities`.

Before the meeting:

1. `scripts/calendar_crm_briefing.py run --lookahead-days 7 --limit 10 --apply` can create/update external and relevant internal Meeting Activities.
2. Rows sit in `Meeting State = Prebrief Ready`.
3. The prebrief/postbrief process may fill `Prebrief`, CRM relations, attendee context, and source links.

After the meeting:

1. `scripts/calendar_crm_briefing.py postbrief-candidates --lookback-days 3` finds ended meetings needing Granola/postbrief follow-up.
2. The agent resolves the Granola meeting by pointer, title, date, attendees, or external domains.
3. The same Meeting Activity gets `Granola Meeting ID`, `Granola URL`, `Postbrief`, and `Next Step Summary`.
4. Only then should the agent create/update To-dos for concrete follow-up.
5. Generated To-dos must link back to the meeting through `Generated To-dos`.

### 3. Current-State Research

Use `pulse` when Seth asks for current deal/account/person/topic state.

Pulse is not a task runner. It is the freshness substrate:

- qmd/repo for history
- Slack/Gmail/Calendar/Granola/WhatsApp/Drive for live state
- markdown artifact as the default output
- qmd update/embed after material pulse writes

Pulse markdown remains the rich account running log. Notion mirrors only current state: next action, waiting/blocker, short last meaningful update, source links, and review flags.

### 4. Agent Command Center

The Agent Command Center is a runner-owned layer on the existing To-dos database. **There is no scheduled runner.** The script exists, but no cron or heartbeat invokes it. Execution is manual — by Seth, or by a Claude/Codex session Seth is in.

Commands (all manual):

```bash
python3 scripts/notion-agent-command-center.py setup
python3 scripts/notion-agent-command-center.py refresh --apply
python3 scripts/notion-agent-command-center.py run-once
python3 scripts/notion-agent-command-center.py run-once --apply
```

State model:

```text
open To-do
  -> refresh suggests Suggested Action / Proposed Prompt / Why Now / Risk
  -> Seth fills Approved Action
  -> Seth (or a Claude/Codex session) runs `run-once --apply` to execute the approved row
  -> Codex worker runs in per-task context
  -> row returns to Needs Review or Failed
  -> Seth reviews, sends, merges, marks done, edits, or retries
```

Hard boundary:

- `refresh` never sets `Approved Action`.
- `run-once` never runs rows without `Approved Action`.
- worker success returns to `Agent Status = Needs Review`, not `Status = Done`.
- communication tasks create reviewable draft artifacts only.
- repo-mutating tasks use an isolated git worktree under `outputs/agent-runs/`.

If `Approved Action = true` ever needs to fire automatically on a schedule, that requires a new Codex automation (deliberately not built — wait for actual traffic justifying it).

### 5. Human Review

The review step is where Seth decides:

- send the draft
- edit the draft
- update the customer/partner/account
- mark the To-do done with a `Done Note`
- push/merge repo changes
- retry or reject the agent output

No automation should skip this step for customer-facing communication, commercial fields, legal/commercial promises, or ambiguous source conflicts.

## Automation Inventory

This table reflects the local Codex automation configs under `/Users/seth/.codex/automations` and repo automation folders as of 2026-05-24.

| Automation | Type | Status | Cadence | Owner role | Read/write posture |
|---|---|---|---|---|---|
| `acme-drive-local-sync-morning` | Codex cron | ACTIVE | Weekdays 07:30 SGT | Drive cache maintainer | Writes local cache + qmd index. Read-only on Drive. |
| `acme-gtm-intake-sweep` | Codex heartbeat | ACTIVE | Weekdays every 30 min (`:00`/`:30`) | **Owner of signal-derived To-dos + Gmail drafts** | 6 blocks: broad signal intake, Gmail waiting heuristic, follow-up drafts (5 patterns), CRM hygiene scan, new Account/People stubs, Deal field bumps on signal references. Persistent thread. |
| `acme-morning-brief` | Codex heartbeat | ACTIVE | Weekdays 08:05 SGT | **READ-ONLY synthesizer** | Reads Notion + Gmail drafts + Calendar + Slack + Granola. Writes only `outputs/briefings/morning/<date>.md` + GTM weekly pack (Fri-Mon). Persistent thread. |
| `acme-calendar-crm-briefing` | Codex heartbeat | ACTIVE | Weekdays every 2h | Meeting memory maintainer | 4 passes: pre-meeting Calendar sync + actual prebrief fill for near-term meetings, post-meeting Calendar+Granola, **off-calendar Granola sweep**, Deal field bumps. Writes Meeting Activities + filed transcripts on disk + Local Path pointer. Persistent thread. |
| `acme-sow-inbox-daily` | Codex heartbeat | ACTIVE | Weekdays 09:00 SGT | Signed-SOW pipeline | Detects signed SOWs via Gmail, runs full `acme-sow-postsign` pipeline. Staging only; never sends. Persistent thread. |
| `automations/_legacy-slack-research-bot/` | Legacy Claude Code loop | Local/manual only | `/loop 180s` if manually started | Slack research bot | Responds to `@claude-gtm` in prospect/ask Slack channels. Renamed from `automations/meeting-prep/` 2026-05-24. |
| `archive/spikes/notion-worker/` | Notion Worker spike | Archived | — | Notion worker exploration | Sample SDK scaffold. Moved to archive 2026-05-24. |

**Architectural notes:**

- Writer boundaries are source-based: `intake-sweep` owns signal-derived To-dos/Gmail drafts, `calendar-crm-briefing` owns Meeting Activities and meeting-derived To-dos, `sow-inbox-daily` owns SOW pipeline artifacts.
- `morning-brief` is strictly read-only on contested resources — only writes its own briefing artifact.
- Cadences are weekday-only and staggered: `intake-sweep` on `:00`/`:30`, `morning-brief` at `:05`, others on independent rhythms.
- `granola-nightly` was deleted 2026-05-24 — `calendar-crm-briefing` Pass 3 absorbed the off-calendar sweep.
- Calendar row seeding is not a completed prebrief. A Meeting Activity with only a Research Prompt must be reported as seeded, not briefed; `python3 scripts/calendar_crm_briefing.py prebrief-needed --lookahead-hours 36` is the deterministic checklist for near-term empty `Prebrief` rows, which must be filled by the `prebrief` skill workflow or flagged as blockers.
- The signed-SOW inbox heartbeat is unattended staging only: no Drive upload, master-sheet write, Slack draft/message, Measure change, or Deal stage mutation without interactive confirmation.
- `Review Flags` is append-only with dated entries (see `acme-todo-manager/SKILL.md`) — multiple writers safe.
- `Local Path` field added to CRM Meeting Activities schema 2026-05-24 to hold the disk pointer for filed transcripts.

## Audit Findings

### Working

- `CLAUDE.md` and `AGENTS.md` are one spine: `AGENTS.md` is a symlink to `CLAUDE.md`.
- Agent Command Center live setup is installed: no missing fields or views.
- Agent Command Center refresh applied to 114 active rows with 0 failed writes on 2026-05-24.
- `run-once` correctly found no approved tasks and did not execute anything.
- Calendar CRM briefing dry-run sees upcoming external meetings, performs read-only CRM matching, and prints the exact would-create/update payload.
- Calendar postbrief candidate check currently returns no candidates.
- Tests pass for the current command-center and calendar briefing scripts.
- `scripts/automation_doctor.py` passes for active automations; it currently reports the paused Chief of Staff stale dated prompt as a warning only.

### Drift / Risk

- `notion/agent-command-center/README.md` still said setup had only been previewed; it should say live setup has been applied.
- The Drive sync architecture recommends twice daily, while the live automation runs once daily.
- Agent Command Center has no scheduled runner — `Approved Action = true` rows are executed only when Seth (or a Claude/Codex session) manually runs `run-once --apply`. The script exists; no cron invokes it.

## Recommended Ownership Boundaries

| Loop | Owns | Does not own |
|---|---|---|
| Drive sync | Keeping `raw/converted/` and qmd fresh from Drive | Interpreting customer state or writing CRM |
| Calendar CRM briefing | Meeting Activity rows, prebrief/postbrief state, Granola pointers | Creating tasks before postbrief extraction |
| Intake sweep | Creating/updating source-linked To-dos from live sources | Agent execution, broad summaries |
| People Owe Me | Narrow waiting-on-others queue and reviewable Gmail drafts | Broad Slack triage, sending messages |
| Chief of Staff | P0/P1 operator summary and reviewable drafts | Maintaining a competing task list |
| Agent Command Center | Delegation triage and one approved worker at a time | Raw-source intake, autonomous execution |
| Pulse | Fresh current-state synthesis for one topic | Silent CRM mutations or task execution |

## Safe Write Policy

Allowed without extra confirmation when the relevant skill/runbook says so:

- runner-owned Agent Command Center fields
- low-risk To-do creation/update with source refs
- CRM Meeting Activities fields from Calendar/Granola context
- local markdown artifacts under `outputs/`, `docs/`, `notion/`, account `pulses/`
- Gmail drafts for review
- qmd update/embed after material local writes

Requires explicit Seth/Jx/human review:

- sending email or Slack messages
- changing ARR, stage, pricing status, signed/lost outcome, renewal outcome, legal terms, commercial commitments
- publishing Drive docs
- creating or changing SOW/MSA/customer legal artifacts
- claiming Acme supports bank/corridor coverage not in canonical bank docs
- running `run-once --apply` unless a To-do has explicit `Approved Action`

## Day-In-The-Life Scenarios

### Morning

1. Drive sync has refreshed the local cache at 07:30 SGT.
2. People Owe Me checks whether anyone owes Seth replies and may stage Gmail drafts.
3. Seth opens Notion `00 Today`, `01 Waiting / Watchlist`, and `Agent Command Center`.
4. Seth runs or reviews `python3 scripts/notion-agent-command-center.py refresh --apply`.
5. Seth fills `Approved Action` on one or more rows that look safe to delegate.

### Before A Meeting

1. Calendar CRM Briefing creates/updates a `CRM Meeting Activities` row.
2. The prebrief command enriches the row with account/person context and a short brief.
3. Seth uses the brief in chat or Notion.
4. No To-do is created unless there is already a concrete pre-meeting action.

### After A Meeting

1. Postbrief finds the Meeting Activity.
2. Granola pointer and postbrief summary are written to the same row.
3. Concrete actions become To-dos linked back through `Generated To-dos`.
4. Agent Command Center refresh proposes which of those can be drafted/researched.

### Delegating A Task

1. Seth reviews suggested action and proposed prompt in Agent Command Center.
2. Seth sets `Approved Action`.
3. `run-once --apply` claims exactly one row.
4. The worker writes artifacts under `outputs/agent-runs/`.
5. Notion row ends in `Needs Review` or `Failed`.
6. Seth reviews and decides final disposition.

### Account / Deal Status Question

1. Run qmd first for history.
2. Run `pulse` for live Slack/Gmail/Calendar/Granola/WhatsApp/Drive state.
3. Write a pulse markdown artifact.
4. Mirror only the current operating state into Notion if needed.

## Maintenance Checklist

Weekly:

- Run `python3 scripts/notion-agent-command-center.py setup` and confirm no missing fields/views.
- Run `python3 tests/test_notion_agent_command_center.py`.
- Run `python3 tests/test_calendar_crm_briefing.py`.
- Run `python3 scripts/automation_doctor.py`.
- Review paused/active automation list under `/Users/seth/.codex/automations`.

Before enabling a paused automation:

1. Read the repo recipe/runbook.
2. Inspect the live `automation.toml`.
3. Remove stale dated instructions.
4. Confirm allowed writes and forbidden writes.
5. Run the underlying script manually in dry-run mode.
6. Confirm the Notion fields/views it expects still exist.

## Next Refactors

1. Rewrite `chief-of-staff-checker` from the safer `chief-of-staff-v2.md` recipe and remove stale Monday-pack content.
2. Rewrite `acme-gtm-intake-sweep` and `acme-calendar-crm-briefing` against the current ownership map before reactivation.
3. Decide whether Drive sync should run morning only or add the documented evening run.
4. Keep Notion Worker as a spike until there is a specific worker use case.
```
