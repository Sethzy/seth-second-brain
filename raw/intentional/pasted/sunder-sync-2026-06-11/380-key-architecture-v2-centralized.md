---
type: raw_capture
source_type: x
title: "Sunder sync: KEY-ARCHITECTURE-v2-centralized.md"
url: "https://twitter.com/mrkurt/status/1759372733"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/01_Projects/RE-AI-CRM/01-architecture-history/KEY-ARCHITECTURE-v2-centralized.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "01_Projects/RE-AI-CRM/01-architecture-history/KEY-ARCHITECTURE-v2-centralized.md"
sha256: "49ed37415f32aa2fc60302fd3d7095134c86099ad4ceba24bbd54a02f9c62a1a"
duplicate_of: ""
---

# Sunder sync: KEY-ARCHITECTURE-v2-centralized.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/01_Projects/RE-AI-CRM/01-architecture-history/KEY-ARCHITECTURE-v2-centralized.md`

Primary URL: https://twitter.com/mrkurt/status/1759372733

Duplicate of existing source-map entry: `none`

## Capture Text

# RE AI CRM — Centralized Architecture (v2)

**Status:** Draft v3.5
**Date:** February 18, 2026
**Purpose:** Revised architecture — centralized AI with thin WhatsApp gateway + durable execution
**Supersedes:** ARCHITECTURE.md (v1.1) for deployment model; v1.1 remains as reference for domain logic, schema, and business model.
**References:** PRODUCT-VISION.md for full feature roadmap and validation hypotheses. SOUL.md for agent personality, tone, and heartbeat behavior.
**v3.5 changes:** Added execution pattern reference analysis — compared our Pattern 2 (JSON checkpointing) against Refly SkillEngine (DAG of LLM agents, parallel execution, PostgreSQL state) and BubbleLab (TypeScript code generation). Confirmed Fintool principle: skills define WHAT (reasoning), workflows define WHEN/HOW (orchestration) — complementary layers, not alternatives. Added Pattern 1b (Subagent Tasks) for single-shot intelligent tasks (<60s, one context window) — the Tasklet pattern where a single markdown file IS the entire agent. Added workflow visualization roadmap: Mermaid→PNG now, ReactFlow read-only viewer later. Source: DeepWiki analysis of refly-ai/refly, bubblelabai/BubbleLab; Fintool articles; Tasklet sales-qualifier.md.
**v3.4 changes:** Formalized "Siloed Skills, No Portability" as a design principle. Skills are intentionally non-portable — they depend on our tool schema (`query_crm`, `update_memory`, `generate_artifact`), execution patterns (JSON checkpointing, Trigger.dev), and Supabase data model. No skill export format, no workflow interchange standard, no marketplace compatibility. Combined with no-code authoring (Refly-inspired Copilot Agent via voice/chat), this creates compounding switching costs: every skill built, every extraction schema defined, every memory accumulated is platform-locked. Users who want to leave must rebuild from scratch. This is deliberate — the moat is accumulated configuration + AI memory, not code. Source: Refly architecture analysis (addendum), no-code interface decision.
**v3.3 changes:** Added Territory Scraper — nightly Trigger.dev cron that scrapes real estate listings across client territories using Browserbase parallel browsers, extracts lead-qualifying signals, enriches agent profiles via Perplexity API, scores leads, and syncs to CRM. Pattern 3 task: 25 parallel Browserbase sessions across 1,429 browser sessions per run, ~90 min runtime. Demolishes 40 hrs/week of manual prospecting per client. New scheduled task `territory-scrape-schedule` (daily 2am), child task `territory-scrape` with per-client queue, `scrape_territories` table for territory config, `scraped_listings` + `enriched_agents` tables for results. Source: Production-proven scraper pattern (12,105 listings / 314 ZIP codes / 4,446 enriched profiles in 90 min).
**v3.2 changes:** Three execution patterns clarified for sprites.dev hosting (persistent sandbox). Pattern 1: Basic skills via system cron (morning briefings, simple schedules, no checkpointing). Pattern 2: Workflows via JSON state files + Antfarm pattern (lead outreach pipelines, document processing, crash recovery via cron polling `workflow_state/` directory). Pattern 3: Platform tasks via Trigger.dev (bulk lead scraping 1000s concurrent, data migrations, infrastructure operations needing queue management + observability dashboard). Trigger.dev usage reduced to rare, long-running infrastructure tasks. User-facing multi-step workflows use JSON checkpointing pattern instead. Source: OpenClaw heartbeat analysis, Antfarm workflow architecture (YAML + SQLite adapted to JSON + filesystem), sprites.dev persistent hosting evaluation.
**v3.1 changes:** Added JIT UI for Ambiguity Resolution — when the AI can't confidently produce what the user wants, it scopes first (WhatsApp polls via `ask_user` tool) then shows a visual preview (web link via `generate_preview` tool) before generating the final output. Extends mid-workflow clarification pattern. Two new tools, one new table (`preview_specs`), new Next.js preview route. WhatsApp polls (native Baileys support) for scoping questions — braindead simple for non-technical users. Web preview pages (display-only, mobile-first) for visual confirmation. Inspired by Fintool's `AskUserQuestion` pattern adapted for WhatsApp-primary interface. Source: Tambo.co analysis (Zod schema → component rendering), Fintool chat-only article, json-render.dev, existing JIT UI PRD (2026-01-25).
**v3.0 changes:** Agent SDK + Model Routing overhaul. Main agent: OpenAI Agents SDK (TypeScript) with Vercel AI SDK adapter for multi-model routing — Gemini 2.5 Flash for daily chat/extraction ($0.075/1M tokens), Kimi 2.5 via OpenRouter for complex reasoning ($0.28/1M). Replaced "Vercel AI SDK runs inside Trigger.dev" with "OAI Agents SDK runs inside Trigger.dev." Sandbox: E2B replaces Vercel Sandbox, with Claude Agent SDK pre-installed as the execution harness (built-in error recovery, file ops, code execution). Claude Agent SDK IS the harness — no DIY error recovery needed. Updated Provider Registry → Model Routing Registry. Estimated cost: ~$90-500/mo vs ~$1,500+ all-Sonnet. Source: Research on OAI Agents SDK multi-model support (Vercel AI SDK adapter for TS, LiteLLM for Python), Claude Agent SDK programmatic API (`query()` + `ClaudeSDKClient`), E2B sandbox templates with Claude Code pre-installed.
**v2.9 changes:** Added task cancellation flow (gateway detects cancel intent → Trigger.dev `runs.cancel()` + queue flush, active run tracking via `active_agent_runs` table) and Tier 1 extraction idempotency (`processed_messages` dedup table, Baileys message ID as idempotency key, prevents re-extraction on gateway reconnect/webhook replay). Source: Fintool gap analysis — Fintool uses Temporal heartbeats for cancellation + document/alert pair tracking for idempotency.
**v2.8 changes:** Added Document System (Inbound Extraction) — self-serve schema builder, Gemini classification + extraction pipeline (reused from Sunder), two extraction backends (Gemini structured output for simple, ExtendAI for complex), three new tables (documents, document_extractions, extraction_schemas), five new document tools. Build phases 7-8 added for document processing. Source: Sunder pipeline analysis + Fintool metadata pattern.
**v2.7 changes:** Resolved sandbox decision — Vercel Sandbox for artifact generation, Browserbase for per-user authenticated browser sessions. Added browser research architecture (Browserbase Contexts API + Live View + Stagehand). Resolved "E2B vs Northflank" open question. Source: Sandbox provider comparison (E2B, Vercel Sandbox, Browserbase, Northflank).
**v2.6 changes:** Added raw SQL query tool (`query_crm`) for ad-hoc CRM queries, eval framework section (CRITICAL — even 20 test cases before MVP), mid-workflow clarification via Trigger.dev waitpoints, sandbox data staging for large payloads, context-aware data tiering for large result sets, creator path data validation. Source: Fintool/Braintrust pattern analysis — SQL agents achieve 100% accuracy on structured data (Vercel "bash is all you need" eval), hybrid SQL+bash verification wins for reliability.
**v2.5 changes:** Added skills filesystem architecture — two mount points (platform read-only + user read-write) following Fintool's sandbox pattern adapted for B2C. Skills are files in Supabase Storage, indexed in `skills_index` table, loaded into agent context at prompt-assembly time. Agent can create user skills via `manage_skill` tool. Source: Fintool mount-point architecture discussion.
**v2.4 changes:** Added domain knowledge scaling architecture (files in Supabase Storage + `domain_knowledge_index` table, Fintool's lazy-loading pattern), onboarding via chat history analysis + connected services (Composio). Source: Fintool gap analysis.
**v2.3 changes:** Added context compaction (conversation history management), semantic memory search (pgvector migration path), agent self-scheduling (recurring tasks), session boundaries (idle-based segmentation), SOUL.md personality definition, sub-agent spawning design (post-MVP). Source: OpenClaw gap analysis.
**v2.2 changes:** Added Trigger.dev for durable agent execution, replaced Vercel Cron with Trigger.dev scheduled tasks, replaced in-memory mutex with Trigger.dev per-client queues, added Trigger.dev waitpoints for Tier 3 approval flow.

---

## The One-Liner

An AI-first CRM for real estate agents. The AI **reads all WhatsApp conversations** to passively build and maintain the CRM. The agent **talks to the AI only in their own chat**. Sending messages to third-party contacts requires **explicit approval**. A thin gateway maintains the WhatsApp connection. All AI reasoning, CRM logic, and data live centrally. A web dashboard gives visibility into the pipeline.

---

## What Changed From v1

v1 assumed **OpenClaw on a per-client VPS** (edge-heavy, each client gets their own AI instance). v2 flips this:

| Dimension | v1 (edge-heavy) | v2 (centralized) |
|---|---|---|
| AI reasoning | Per-client VPS (OpenClaw) | OpenAI Agents SDK (model-agnostic via Vercel AI SDK adapter) |
| WhatsApp | Baileys on each VPS | Baileys workers on one gateway host |
| Tool calling | REST shell-out / MCP workaround | OAI Agents SDK native tool calling (Zod schemas) |
| Model lock-in | Claude only (via OpenClaw) | Provider registry — swap Claude, Kimi, DeepSeek |
| Skills | Markdown files pulled from CDN | Markdown files in Supabase Storage (two mount points: platform + user) |
| Infra per client | ~$5/mo VPS + LLM costs | ~$0.50/mo marginal (shared infra) |
| Updating skills | Update CDN, all VPSes refresh | Deploy once, done |
| Runtime dependency | OpenClaw (430K lines, no native MCP) | OAI Agents SDK + Vercel AI SDK adapter + Next.js — your code, your stack |

**Why the change:** The only thing that needs to run per-client is the WhatsApp WebSocket (Baileys). Everything else benefits from centralization: simpler deploys, one codebase, model-agnostic tool calling, lower cost.

---

## Key Architectural Decisions

Decisions made during Central API brainstorm sessions (Feb 2026):

| Decision | What | Why |
|---|---|---|
| **OpenAI Agents SDK** | Agent framework with built-in loop, handoffs, guardrails, tracing. Multi-model via Vercel AI SDK adapter (`@openai/agents-extensions`). | Built-in agent loop (no DIY). Multi-model via adapter: Gemini, Kimi, Claude, DeepSeek. TypeScript-native (`@openai/agents`). Not OpenAI-locked despite the name. |
| **Next.js unified app** | API routes + dashboard in one app | Simpler deploys. Dashboard and API share auth, types, DB client. |
| **Three execution modes** | Reasoner (structured tools → Supabase) + Document (Gemini/ExtendAI extraction pipeline) + Creator (sandbox for artifacts) | 85% of messages are CRM CRUD. 5% are document processing. 10% need file generation. Document path is a deterministic pipeline, not an LLM tool loop. |
| **Sandbox as a tool** | `generate_artifact` triggers E2B sandbox with Claude Agent SDK pre-installed; `browse_property_site` triggers Browserbase for browser sessions | E2B boots in 150ms. Claude Agent SDK IS the harness inside — built-in error recovery, file ops (Read/Write/Edit), code execution (Bash), search (Glob/Grep). No DIY harness needed. Browserbase for per-user authenticated browser sessions (property research). |
| **Browserbase for browser research** | Contexts API persists per-user cookies across sessions. Live View lets users authenticate via embedded iframe. Stagehand for AI-driven automation. | Property portals (99.co, PropertyGuru) require login. Need persistent cookies per user, anti-detection, and user-driven auth. Native Trigger.dev integration. |
| **Memory as a standard tool** | `update_memory` tool → Supabase `ai_memory` table | No Anthropic Memory Tool (lock-in). Any model can call `update_memory`. |
| **Model routing registry** | Route to different models by task type. Gemini Flash for extraction/chat ($0.075/1M), Kimi 2.5 for reasoning ($0.28/1M), Claude Sonnet in sandbox ($3/1M). | 94% cost savings vs all-Sonnet. OpenRouter gives one API key for Kimi/DeepSeek. Google direct for Gemini (lower latency). |
| **Two-SDK architecture** | OAI Agents SDK for main agent (multi-model), Claude Agent SDK for sandbox only (best harness) | Main agent needs model flexibility (cheap models for daily chat). Sandbox needs best one-shot rate (Claude Agent SDK has built-in error recovery, file ops, code execution). Accept Claude lock-in only in sandbox (5-10% of volume). |
| **Three execution patterns** | (1) **Basic skills** - simple cron, no checkpointing. (2) **Workflows** - JSON checkpointing (our AI Engineering Playbook pattern + Antfarm). (3) **Platform tasks** - Trigger.dev for long-running, deterministic, rarely-changed operations. | Pattern 1: Morning briefings, nudges (system cron). Pattern 2: Multi-step sales workflows like lead research → enrich → validate → personalize (JSON checkpoint after each step, resume on crash). Pattern 3: Scraping 1000 leads concurrently, bulk operations (Trigger.dev queues + observability). Hosted on sprites.dev (persistent sandbox), no serverless timeout issues. |
| **Basic skills (Pattern 1)** | Simple scheduled tasks via system cron. No checkpointing needed. | Morning briefings, daily nudges, simple reminders. Tasks complete in <30s, don't need crash recovery. Just run them. Example: `0 8 * * * node scripts/morning-briefing.ts` |
| **Workflows (Pattern 2)** | Multi-step processes with JSON checkpointing. Primary reference: our AI Engineering Playbook's `feature_list.json` pattern (proven — only flip status fields, never modify structure, batch execution with review checkpoints). Secondary: Antfarm's YAML+SQLite adapted to JSON+filesystem. State tracked in `workflow_state/{workflow_id}.json`. Cron polls for work, resumes from last checkpoint on crash. | Lead outreach pipeline: research → enrich → validate → personalize → queue. Each step writes progress to JSON. If crash at step 3, resume from step 3. SQLite tracks active workflows. Example: `sales-outreach-session-123.json` contains `{ currentStep: "validate", completedSteps: ["research", "enrich"], data: {...} }` |
| **Platform tasks (Pattern 3)** | Long-running, deterministic operations that rarely change. Use Trigger.dev for queues, concurrency control, observability. | Territory scraper (25 parallel Browserbase browsers, 90 min nightly), bulk lead scraping (1000 concurrent tasks), document batch processing, large-scale data migrations. These are infrastructure-level tasks, not user-facing workflows. Trigger.dev gives us dashboard, per-task queues, automatic retries. Worth the dependency for operational visibility. |
| **Vercel for CRUD + simple queries only** | Dashboard, auth, simple single-shot LLM calls stay on Vercel | Don't over-engineer. Most requests are fast. Only offload to Trigger.dev when durability matters. |
| **Skills are files, not code** | Skills (platform + user-created) are markdown files in Supabase Storage, indexed in `skills_index` table, loaded into agent context per request | Skills are composable, versionable, human-readable. Agent can create its own. Follows Fintool's mount-point pattern (adapted: 2 mount points for B2C, not 3). |
| **Siloed skills, no portability** | Skills are intentionally non-portable. No export format, no workflow interchange standard, no marketplace compatibility. WorkflowPlan JSON + SKILL.md only execute on our runtime. No-code authoring (Refly Copilot Agent pattern via voice/chat) means users never touch the underlying format. | **Moat = accumulated configuration + AI memory, not code.** Every skill the AI builds depends on our tools (`query_crm`, `update_memory`, `generate_artifact`), our execution patterns (JSON checkpointing, cron, Trigger.dev), and our Supabase schema. Combined with `ai_memory`, `extraction_schemas`, contact graph, and interaction history — switching cost compounds over time. Users who leave rebuild from scratch. This is deliberate. Source: Refly analysis (addendum) — their Apache 2.0 portability is a different product philosophy. Ours is a managed service where the AI does everything; users don't want portability, they want it to work. |
| **Raw SQL query tool** | `query_crm` tool lets agent write ad-hoc SELECT queries against Supabase | Pre-defined CRM tools can't anticipate every question. Agent needs flexible queries ("contacts with budget >$1.5M not contacted in 2 weeks"). SELECT-only, RLS-scoped, timeout + result limit enforced. Source: Braintrust eval — SQL agents achieve 100% accuracy on structured data, 7x more token-efficient than bash. |
| **No bash tool for agent** | Agent has no general bash tool. Bash only exists inside Vercel Sandbox during artifact generation | Agent runs in Trigger.dev tasks — no persistent filesystem to bash on. All CRM data is structured in Supabase (SQL handles it). Fintool needs bash because their agent runs inside a sandbox with S3-mounted files. Our data topology is different. |
| **Self-serve document extraction** | Users define custom extraction schemas via WhatsApp conversation. AI classifies, splits, and extracts structured data from forwarded documents. Two backends: Gemini (simple), ExtendAI (complex). | RE agents handle 100s of documents (brochures, floor plans, OTPs, valuations). Pipeline reused from Sunder product. Self-serve schema builder replaces developer-driven onboarding. |
| **Eval framework from day 1** | Domain-specific evals with test cases for extraction accuracy, conversation quality, artifact fidelity | Tier 1 reads ALL WhatsApp conversations autonomously. A bad extraction creates wrong contacts, logs incorrect deals, damages user's real client relationships. Even 20 test cases before MVP. Block deploys if eval score drops >5%. |
| **Mid-workflow clarification** | Extend Trigger.dev waitpoints (already used for Tier 3 approvals) to support agent asking user mid-conversation questions | "I see two Sarahs — which one?" Agent pauses, user answers, agent resumes. Same waitpoint infra, different use case. |
| **JIT UI for ambiguity resolution** | WhatsApp polls for scoping + web preview pages for visual confirmation. Two new tools: `ask_user` (polls) and `generate_preview` (preview link). | Users are non-technical RE agents — can't read schemas or JSON. When AI doesn't know exactly what to produce, it asks via polls (braindead simple, no typing), then shows a rendered preview on a mobile web page (tap link → see mockup → confirm or adjust in chat). TDD for AI outputs: define the "test" (preview) before the "implementation" (final output). Source: Fintool AskUserQuestion pattern adapted for WhatsApp. |
| **Context-aware data tiering** | Large result sets return summaries, not full data. Agent uses `query_crm` for detail on demand. | Don't load 200 contacts into context. Return counts + summaries for large sets. Agent drills down with SQL. |
| **Sandbox data staging** | Small data (<50 rows) passes as JSON in tool call. Large data (>50 rows) staged in Supabase Storage, URL passed to sandbox. | Avoids serializing megabytes through tool-call JSON. Sandbox downloads directly from Storage. |
| **Task cancellation via gateway** | Gateway detects cancel intent ("stop", "cancel", "nevermind") before routing to API. Cancels active Trigger.dev run + flushes queued runs for that client. | WhatsApp has no "stop" button. Cancel must be detected from natural language at the gateway level (fast, no LLM). Active run ID tracked in `active_agent_runs` table. Source: Fintool uses Temporal heartbeats for cancellation; Trigger.dev equivalent is `runs.cancel()`. |
| **Tier 1 extraction idempotency** | Every Baileys message has a unique `key.id`. Gateway checks `processed_messages` table before forwarding to API. Duplicate messages are silently dropped. | Baileys replays messages on reconnect (`syncFullHistory: true`). Webhooks can fire twice. Trigger.dev retries re-invoke tasks. Without dedup, same message creates duplicate contacts/interactions. Source: Fintool tracks processed document/alert pairs to prevent re-firing on reindex. |

**Patterns borrowed from Fintool (adapted, not copied):**
- Skill shadowing (platform defaults → client overrides) — future, not MVP
- Model routing (cheap model for simple, expensive for complex)
- **Eval framework (CRITICAL — even 20 test cases for MVP)** — Fintool has ~2,000 test cases, blocks PRs if eval score drops >5%. We start with 20 test cases for extraction accuracy, conversation quality, and artifact fidelity. See Eval Framework section below.
- S3-first for user files (skills, memories, artifacts) — adapted to Supabase Storage
- **Durable execution for agent tasks** — Fintool uses Temporal, we use Trigger.dev (managed equivalent)
- **Sandbox as tool, not environment** — agent calls sandbox when needed, orchestrator manages the loop
- **Two-mount-point filesystem for skills** — Fintool uses three mount points (private/shared/public) for isolated sandbox environments. We adapt for B2C (no org layer): two mount points in Supabase Storage — `platform/` (read-only, we ship) and `clients/{client_id}/` (read-write, agent creates). Skills are markdown files loaded at prompt-assembly time. Sandbox mounts are logical (fetched from Storage), not physical.
- **Domain knowledge as files + SQL index** — Fintool stores skills as S3 files indexed in `fs_files` Postgres table with YAML frontmatter metadata. We adapt: markdown files in Supabase Storage indexed in `domain_knowledge_index` table. Lazy-load only relevant chunks per request via tag/keyword matching.
- **Onboarding via artifact analysis** — Fintool reads user-uploaded files (investment memos, Excel models, email threads) to learn investment style. We adapt: read WhatsApp chat history (already flowing via Baileys) + prompt to connect external services (Google Calendar, Gmail via Composio) to pre-populate CRM and learn communication style.
- **Raw SQL for flexible agent queries** — Braintrust/Vercel eval tested SQL agents writing raw queries against structured data: 100% accuracy, 7x more efficient than bash, 6.5x cheaper. Fintool uses hybrid SQL+bash (bash for verification). We adopt SQL tool only (no bash — no filesystem). Agent writes SELECT-only queries, RLS enforces client scoping. Source: Vercel "Testing if bash is all you need" (Jan 2026).
- **Context-aware data tiering** — Fintool lazy-loads skills/knowledge to avoid "burning tokens." We extend to CRM data: large result sets return summaries, agent uses `query_crm` for detail on demand.
- **Sandbox data staging for large payloads** — Fintool writes intermediate data to filesystem for multi-step workflows. We adapt: Trigger.dev task stages large query results in Supabase Storage, passes URL to sandbox. Sandbox downloads directly. Small data (<50 rows) passes as JSON.
- **Task cancellation** — Fintool uses Temporal heartbeats to detect cancellation ("User clicks stop — activity is already running on a different server. Use heartbeats sent every few seconds.") We adapt: gateway detects cancel intent from natural language, calls Trigger.dev `runs.cancel()` + flushes queued runs. No heartbeat needed — Trigger.dev cancellation is immediate via API. Active run tracked in `active_agent_runs` table.
- **Idempotent event processing** — Fintool tracks processed document/alert pairs to prevent re-firing when documents get reindexed. We adapt: `processed_messages` table keyed on Baileys message ID. Gateway checks before forwarding. Prevents duplicate extraction on reconnect, webhook replay, or Trigger.dev retry.

**Patterns borrowed from OpenClaw (adapted):**
- Self-evolving memory (agent writes its own notes) — via `update_memory` tool
- Proactive cron (morning briefings, nudges) — via system cron (Pattern 1: basic skills)
- Heartbeat pattern (agents check for work periodically) — adapted for workflows (Pattern 2: cron polls `workflow_state/` directory)

---

## Execution Patterns: When to Use What

**Context:** Hosted on sprites.dev (persistent sandbox). No serverless timeouts. No Vercel 60s limit. We have system cron, persistent filesystem, and SQLite.

### Pattern 1: Basic Skills (System Cron)

**Use for:** Simple scheduled tasks that complete quickly (<30s) and don't need crash recovery.

**Examples:**
- Morning briefing at 8am
- Daily pipeline summary
- Weekly digest email
- Reminder nudges

**Implementation:**
```bash
# crontab
0 8 * * * node /app/scripts/morning-briefing.ts
0 0 * * 0 node /app/scripts/weekly-digest.ts
```

**State:** None. Task runs, completes, done.

**Cost:** Free (system cron)

**Observability:** Tail logs

---

### Pattern 2: Workflows (JSON Checkpointing)

**Use for:** Multi-step processes that need crash recovery and can be paused/resumed.

**Examples:**
- Lead research pipeline: `scrape LinkedIn → enrich contact → validate email → generate personalized copy → queue for review`
- Document processing: `classify → split → extract → link to CRM → notify user`
- Onboarding flow: `connect WhatsApp → analyze chat history → extract contacts → set preferences`

**Implementation:**

```typescript
// workflow_state/sales-outreach-session-123.json
{
  "workflowId": "sales-outreach-session-123",
  "type": "lead-outreach",
  "status": "in_progress",
  "currentStep": "validate-email",
  "completedSteps": ["scrape-linkedin", "enrich-contact"],
  "data": {
    "leadId": "lead-456",
    "linkedinData": {...},
    "enrichedContact": {...}
  },
  "createdAt": "2026-02-15T10:00:00Z",
  "updatedAt": "2026-02-15T10:05:00Z"
}
```

```typescript
// Workflow executor (runs via cron every 2 min)
// Poll workflow_state/ directory for active workflows
// Load JSON, execute next step, update JSON, save
// If crash → cron picks it up next run, resumes from currentStep
```

**State storage:**
- `workflow_state/{workflow_id}.json` - current progress
- SQLite `workflows` table - index of active workflows for fast polling

**Cost:** Free (system cron + local files)

**Observability:** JSON files + SQLite queries

**Crash recovery:** Cron polls directory every 2 min, resumes from `currentStep`

**References:**
- **Primary:** Our own AI Engineering Playbook's `feature_list.json` pattern — proven in production. JSON state file tracks progress per step, only status fields flip (never modify structure), batch execution with checkpoints for review. See: `03_Resources/Playbooks/Engineering/AI Engineering Playbook.md` § Feature Development + § Execute and check-off task list.
- **Secondary:** Antfarm's YAML + SQLite pattern — adapted to JSON + filesystem. Same idea (declarative state file, poll for work, resume on crash), different format.

---

### Pattern 3: Platform Tasks (Trigger.dev)

**Use for:** Long-running, deterministic, infrastructure-level tasks that rarely change.

**Examples:**
- **Territory listing scraper:** Nightly scrape of real estate listings across client territories — 25 parallel Browserbase sessions, 314 ZIP codes, 12K+ listings in 90 min. Extracts lead-qualifying signals, enriches agent profiles via Perplexity API, scores and syncs to CRM. (See Territory Scraper section.)
- **Bulk lead scraping:** Scrape 1000 LinkedIn profiles concurrently (10 min runtime, needs concurrency control)
- **Document batch processing:** Process 500 PDFs uploaded in bulk (queue management, retries on failure)
- **Data migration:** One-time operations when we change schema (observability, manual pause/resume)

**Why Trigger.dev for these:**
1. **Concurrency control** - "Scrape 1000 leads, max 50 concurrent" via queues
2. **Observability dashboard** - see all 1000 tasks, which failed, retry them
3. **Retries with backoff** - if LinkedIn rate-limits, auto-retry with exponential backoff
4. **Manual intervention** - pause runaway tasks, cancel bulk operations

**Implementation:**
```typescript
// Trigger once, runs 1000 tasks
await tasks.trigger("bulk-lead-scrape", {
  leadIds: [...1000 leads],
  queue: { name: "lead-scraper", concurrencyLimit: 50 }
});

// Dashboard shows:
// 750 completed, 200 in_progress, 50 failed
// Click "Retry failed" button → re-runs 50 failed tasks
```

**State:** Trigger.dev manages it

**Cost:** Trigger.dev free tier (500K tasks/month) or paid

**Observability:** Trigger.dev dashboard (timeline, logs, traces)

**When NOT to use:** User-facing workflows that change frequently. Use Pattern 2 instead.

---

### Decision Matrix

| Task | Pattern | Why |
|------|---------|-----|
| Morning briefing | 1 (cron) | Simple, fast, no crash recovery needed |
| Sales email qualifier | 1b (subagent) | Single-shot, one context window, <60s, trigger → LLM does everything → done |
| Inbound email responder | 1b (subagent) | Same — single trigger, reads thread, reasons, replies, logs |
| Single document classifier | 1b (subagent) | Classify one doc, update DB — doesn't need multi-step orchestration |
| Lead outreach pipeline (5 steps) | 2 (JSON workflow) | Multi-step, needs checkpointing, user-facing |
| Scrape 1000 leads concurrently | 3 (Trigger.dev) | Long-running, needs queue management, rare operation |
| Nightly territory listing scraper | 3 (Trigger.dev) | 25 parallel browsers, 90 min runtime, daily cron, needs concurrency control + observability |
| Daily pipeline summary | 1 (cron) | Simple, scheduled, completes quickly |
| Document extraction (classify → extract → link) | 2 (JSON workflow) | Multi-step, user-uploaded docs, crash recovery needed |
| Bulk data migration (change schema for 10K contacts) | 3 (Trigger.dev) | One-time, needs observability, manual pause/cancel |

---

### Why Not Trigger.dev for Everything?

**Before (original plan):** All multi-step tasks → Trigger.dev

**After (sprites.dev hosting):**
- No serverless timeout (sprites.dev is persistent)
- System cron available
- Persistent filesystem for JSON state
- SQLite for workflow indexing

**Trigger.dev adds value for:**
- Platform-level bulk operations (1000s of concurrent tasks)
- Rare, long-running migrations
- Tasks that benefit from visual dashboard (debug 1000 failed scrapes)

**Trigger.dev adds complexity for:**
- User-facing workflows that change weekly (lead outreach logic evolves)
- Simple scheduled tasks (why deploy to Trigger.dev when cron works?)

**Result:** Use Trigger.dev sparingly for infrastructure tasks. Use JSON workflows for user-facing multi-step processes. Use cron for simple schedules.

---

### Reference: Execution Pattern Analysis (Refly, BubbleLab, Fintool, Tasklet)

**Date:** February 2026. Source: Architecture comparison session — Refly (refly-ai/refly), BubbleLab (bubblelabai/BubbleLab), Fintool articles, Tasklet sales-qualifier example.

#### Skills and Workflows Are Complementary Layers, Not Alternatives

Fintool's architecture proves this. Their alert pipeline:

```
Document ingested → SQS queue → Lambda (deterministic filter: doc type, ticker, keyword, watchlist)
  → ALL pass? → Temporal workflow → LLM runs skill prompt with document context → email user
```

The LLM only runs at the end — for the part that actually needs reasoning. Everything before (trigger, filter, route) is deterministic code. Their scheduled alerts use bash pre-check scripts in E2B for conditional logic ("only fire if portfolio down >2%"). Not prompts. Code.

**The principle:** Skills define WHAT the LLM should do when it runs. Workflows define WHEN to run, HOW to recover from crashes, WHERE to route things. That's infrastructure, not intelligence.

| Concern | Fintool | Our equivalent |
|---|---|---|
| What to do (reasoning) | Skill (markdown) | Skill (markdown) |
| When to run | CloudWatch cron + SQS events | System cron (Pattern 1) |
| How to recover | Temporal | JSON checkpointing (Pattern 2) / Trigger.dev (Pattern 3) |
| Deterministic filtering | Lambda + SQL + Elasticsearch | Workflow executor code |
| Deterministic pre-checks | Bash scripts in E2B sandbox | Steps in JSON workflow |

**Source:** `extracted_content/Important Articles/Fintool/nicbustamante-fintool-lessons-building-ai-agents-FULL.md`, `jesseprovo-fintool-background-agents-reactive-to-proactive-FULL.md`

#### Subagent Tasks (Pattern 1b) — When the LLM IS the Workflow

Tasklet uses a single markdown file as the entire agent — personality, domain knowledge, decision logic, tool instructions, and sequential steps all in one prompt. Example: a sales qualifier that receives a Gmail thread ID and does everything in one shot (~5-10 seconds).

This works when: **single-shot** (trigger → do thing → done), **short-lived** (<60s), **idempotent-enough** (retry = worst case duplicate email), **linear** (no parallel branches).

This breaks when: **multi-step over time** (step 1 today, step 3 tomorrow), **needs partial progress** (step 3 fails, don't redo 1-2), **has expensive non-LLM steps** (scraping, parallel browsers), **needs determinism** (filter MUST always match the same way).

**Updated pattern spectrum:**

| Pattern | Name | Use for | State | Example |
|---|---|---|---|---|
| 1 | Basic cron | Simple scheduled tasks (<30s) | None | Morning briefing |
| 1b | Subagent tasks | Single-shot intelligent tasks (<60s, one context window) | DB only (reads/writes during execution) | Sales qualifier, email responder, document classifier, single-message handler |
| 2 | JSON workflows | Multi-step processes needing crash recovery, spanning time | `workflow_state/{id}.json` + SQLite | Lead outreach pipeline, document processing |
| 3 | Trigger.dev | Long-running infrastructure tasks needing queues + observability | Trigger.dev managed | Territory scraper, bulk lead scraping, data migrations |

**Source:** Tasklet `sales-qualifier.md` — subagent prompt pattern.

#### Refly SkillEngine vs Our JSON Checkpointing (Pattern 2)

Refly's SkillEngine executes workflows as a DAG of LLM agents — topological sort for execution order, parallel where dependencies allow, each node is an LLM in a ReAct loop (Reason → Act → Observe → Iterate). State stored in PostgreSQL (`WorkflowNodeExecution` rows). Retry with exponential backoff per node. Context flows downstream automatically via `contextItems`.

| Dimension | Our JSON Checkpointing | Refly SkillEngine |
|---|---|---|
| Execution model | Sequential linear pipeline | DAG with parallel execution levels |
| State storage | JSON file + SQLite | PostgreSQL rows |
| Checkpoint granularity | Per business step | Per tool call within each node |
| What runs at each step | Anything (LLM, API, script) | Always an LLM in ReAct loop |
| Parallelism | None (one step at a time) | Independent nodes run concurrently |
| Crash recovery | Cron re-reads file every 2 min | DB poll + timeout detection + retry policy |
| Retry logic | Hand-coded per step | Built-in: maxRetries, exponential backoff |
| Context passing | Manual via `data: {}` in JSON | Automatic via `contextItems` |
| Flexibility | Total — each step can be anything | Locked to "LLM agent with tools" per node |
| Infra required | Cron + filesystem + SQLite | PostgreSQL + queue system + polling service |
| Complexity | ~100 lines executor | Thousands of lines |

**Where Refly is better:** Parallel execution (independent steps run concurrently), fine-grained checkpointing (per tool call, not per business step), structured retry with backoff, automatic context routing between nodes.

**Where ours is better:** Steps aren't locked to LLM agents (raw API calls, deterministic scripts — anything), simplicity (~100 lines), cost (no unnecessary LLM calls for deterministic operations), determinism, zero infra dependencies.

**Future enhancement (steal from Refly if needed):** Upgrade Pattern 2 to DAG-based execution — `dependsOn` per step, `Promise.all` for parallel-ready steps, retry policy in the JSON. ~150 lines instead of 100, still zero infra dependencies. Only worth doing if we have workflows with parallelizable steps.

**Source:** DeepWiki analysis of `refly-ai/refly` — SkillEngine, WorkflowService, SkillInvokerService.

#### BubbleLab vs Refly — Code Generation vs Prompt Execution

BubbleLab (bubblelabai/BubbleLab) takes a fundamentally different approach: it generates actual TypeScript code. Four specialized AI agents (Coffee=planner on Gemini 3 Pro, Boba=builder, Pearl=editor on Claude Sonnet 4.5, MilkTea=configurator on Gemini 2.5 Flash) produce a `BubbleFlow` TypeScript class. Full AST parsing, scope analysis, TypeScript compilation, credential injection. Portable: `npm install @bubblelab/bubble-core` runs standalone.

Refly produces a `SKILL.md` — a markdown file with YAML frontmatter (name, triggers, input/output schemas) bound to a canvas workflow. Execution = LLM agents interpret and run each node non-deterministically at runtime.

**Our choice:** Refly-inspired pattern (structured prompts, not compiled code). Correct for mobile/chat delivery — can't preview TypeScript in WhatsApp. Skills as markdown files the model follows directly (Fintool's approach).

**Source:** DeepWiki analysis of `bubblelabai/BubbleLab`, `refly-ai/refly`.

#### Workflow Visualization (Future)

**Start with Mermaid** (zero effort): LLM generates Mermaid syntax → render to PNG via `mermaid.ink` API → send inline via WhatsApp. Covers 90% of visualization needs.

**Graduate to ReactFlow viewer** (when impressive matters): Tiny static React app (Vite + ReactFlow, ~200 lines), hosted free on Vercel/Cloudflare Pages. Read-only mode (`nodesDraggable={false}`, `nodesConnectable={false}`), mobile-optimized (`fitView`, pinch-zoom works natively). Send WhatsApp link + PNG thumbnail. Flow JSON stored in Supabase, fetched by ID. Good "wow" moment in sales context.

---

## System Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                        USERS (RE Agents)                          │
│   WhatsApp ──── AI reads ALL chats (passive CRM extraction)       │
│              ──── talk to AI in own chat (voice, text, photos)    │
│              ──── approve outbound messages (strict per-msg)      │
│   Dashboard ──── view pipeline, contacts, deals, pending msgs    │
└────────┬──────────────────────────────────────┬──────────────────┘
         │                                       │
         │ WhatsApp WebSocket                   │ HTTPS
         ▼                                       ▼
┌─────────────────────────┐       ┌──────────────────────────────────┐
│  GATEWAY HOST            │       │  NEXT.JS APP (Vercel)             │
│  (DigitalOcean droplet)  │       │                                   │
│                          │       │  CRUD / Fast path (no Trigger):   │
│  gateway-manager         │       │  ├── Dashboard pages (SSR)        │
│  ├── worker_001          │ HTTPS │  ├── Auth (Supabase Auth)         │
│  ├── worker_002          │──────▶│  ├── /api/extract (Tier 1, Haiku) │
│  ├── worker_003          │       │  │   Simple extraction, <10s      │
│  └── worker_N            │       │  └── /api/approve (Tier 3 input)  │
│                          │       │       Updates DB + completes token │
│  Each worker:            │       │                                   │
│  • Baileys WS conn       │       │  Trigger.dev kickoff:             │
│  • Reads ALL chats       │       │  ├── /api/message → triggers      │
│  • Replies to user       │       │  │   "agent-conversation" task     │
│  • Approved sends        │       │  └── Subscribes via Realtime      │
│  • ~50MB RAM             │       │      hooks for streaming          │
│                          │       │                                   │
│  Auth state:             │       │  Dashboard Pages:                 │
│  /data/sessions/*.json   │       │  ├── Agent view (RLS-scoped)      │
│  (persisted volume)      │       │  └── Admin view                   │
└──────────────────────────┘       └──────────────┬───────────────────┘
                                                   │
                                          tasks.trigger()
                                                   │
                                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│  TRIGGER.DEV (durable execution)                                      │
│                                                                       │
│  Agent Tasks (1-5 min, durable, checkpointed):                       │
│  ├── agent-conversation   → Tier 2 multi-step tool loop              │
│  ├── agent-extraction     → complex extraction (multi-msg batches)   │
│  ├── document-processing  → classify, split, extract from docs       │
│  ├── generate-artifact    → Creator path (calls sandbox)             │
│  ├── approved-send        → Tier 3 execute (after waitpoint resumes) │
│  └── onboarding-analysis  → one-time post-pairing history analysis   │
│                                                                       │
│  Scheduled Tasks (cron):                                              │
│  ├── morning-briefing     → daily per-client, batch triggered        │
│  ├── follow-up-nudge      → daily, check stale interactions          │
│  ├── stale-lead-check     → weekly                                   │
│  └── process-scheduled    → every minute, send approved messages     │
│                                                                       │
│  Infrastructure:                                                      │
│  ├── Per-client queue (concurrency: 1) — no interleaved responses   │
│  ├── Automatic retries with backoff                                  │
│  ├── Checkpointing at every await (survives crashes)                 │
│  ├── Waitpoints for Tier 3 approval (pause/resume, zero compute)    │
│  ├── Realtime streaming to Vercel frontend                           │
│  └── Full observability (traces, logs, run history)                  │
│                                                                       │
│  OAI Agents SDK runs INSIDE Trigger.dev tasks:                       │
│  ├── Vercel AI SDK adapter (google, openrouter)                      │
│  ├── Model routing: Flash (chat), Kimi (reasoning), Claude (sandbox) │
│  └── Agent.run() + tools (CRM, memory, sandbox, messaging)          │
└──────────────┬───────────────────────────────────┬───────────────────┘
               │                                    │
               ▼                                    ▼
┌──────────────────────────────────┐  ┌────────────────────────────────┐
│  SUPABASE (managed)               │  │  E2B SANDBOX (artifacts)         │
│                                   │  │                                 │
│  clients      contacts            │  │  Spins up when generate_artifact│
│  ├─ id        ├─ id               │  │  tool is called from inside a   │
│  ├─ email     ├─ client_id        │  │  Trigger.dev task. Boots 150ms. │
│  ├─ plan      ├─ name, email      │  │                                 │
│  ├─ stripe_id ├─ type, status     │  │  Claude Agent SDK (pre-installed)│
│  └─ paired?   ├─ structured       │  │  IS the harness:                │
│               └─ ai_summary       │  │  • Read/Write/Edit (file ops)   │
│                                   │  │  • Bash (code execution)        │
│  interactions  deals              │  │  • Glob/Grep (search)           │
│  ├─ client_id  ├─ contact_id      │  │  • Auto error recovery          │
│  ├─ contact_id ├─ property        │  │  • max_budget_usd cap           │
│  ├─ content    ├─ stage, value    │  │                                 │
│  └─ sentiment  └─ structured      │  │  Pre-installed Python libs:     │
│                                   │  │  matplotlib, reportlab, pandas, │
│                                   │  │  seaborn, plotly, Pillow, etc.  │
│                                   │  │                                 │
│                                   │  │  Returns file → Supabase Storage│
│                                   │  │  → URL sent to user via WhatsApp│
│                                   │  └────────────────────────────────┘
│                                   │
│                                   │  ┌────────────────────────────────┐
│                                   │  │  BROWSERBASE (browser research)  │
│                                   │  │                                 │
│                                   │  │  Spins up when                  │
│                                   │  │  browse_property_site tool is   │
│                                   │  │  called from agent-conversation │
│                                   │  │                                 │
│                                   │  │  • Contexts API (per-user       │
│                                   │  │    cookie persistence)          │
│                                   │  │  • Live View (user login via    │
│                                   │  │    embedded iframe)             │
│                                   │  │  • Stagehand (AI browser        │
│                                   │  │    automation)                  │
│                                   │  │                                 │
│                                   │  │  Returns structured data →      │
│                                   │  │  tool result to model           │
│                                   │  └────────────────────────────────┘
│  tasks          ai_memory         │
│  ├─ contact_id  ├─ client_id      │
│  ├─ type, due   ├─ key            │
│  ├─ ai_suggested├─ value (text)   │
│  └─ status      └─ updated_at    │
│                                   │
│  documents         document_extr  │
│  ├─ client_id      ├─ document_id │
│  ├─ contact_id FK  ├─ tag_id      │
│  ├─ deal_id FK     ├─ extracted   │
│  ├─ storage_path   │  _data JSONB │
│  ├─ primary_tag    ├─ confidence  │
│  ├─ tags JSONB     └─ split_idx   │
│  └─ status                        │
│                                   │
│  extraction_schemas               │
│  ├─ client_id                     │
│  ├─ slug, display_name            │
│  ├─ classification_hint           │
│  ├─ fields JSONB                  │
│  └─ extraction_backend            │
│                                   │
│  usage_log                        │
│  ├─ client_id                     │
│  ├─ tool_name                     │
│  ├─ tokens                        │
│  └─ cost_usd                      │
│                                   │
│  pending_messages (Tier 3)        │
│  ├─ id, client_id, contact_id    │
│  ├─ target_jid, content           │
│  ├─ status: awaiting | approved   │
│  ├─ trigger_token_id (waitpoint)  │
│  ├─ scheduled_at, approved_at     │
│  └─ sent_at                       │
│                                   │
│  artifacts                        │
│  ├─ id, client_id                 │
│  ├─ type, storage_url             │
│  └─ created_at                    │
│                                   │
│  domain_knowledge_index           │
│  ├─ id, slug                      │
│  ├─ storage_path                  │
│  ├─ client_id (null=platform)     │
│  ├─ tags[], trigger_keywords[]    │
│  ├─ always_load, token_estimate   │
│  └─ updated_at                    │
│                                   │
│  RLS: Every table filtered by     │
│  client_id                        │
│                                   │
│  Storage buckets:                 │
│  ├─ documents/{client_id}/        │
│  ├─ artifacts/{client_id}/        │
│  ├─ skills/platform/              │
│  ├─ skills/clients/{client_id}/   │
│  └─ domain-knowledge/             │
└───────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│  EXTERNAL APIS (called from Trigger.dev tasks)                       │
│                                                                      │
│  Gemini 2.5 Flash (Google AI)         ExtendAI                       │
│  ├─ Document classification           ├─ Complex document extraction │
│  ├─ Document splitting                ├─ Per-field OCR confidence    │
│  ├─ Simple structured extraction      ├─ Bounding box citations      │
│  └─ Google Files API (temp upload)    └─ Custom processors per tag   │
│                                                                      │
│  Called by: document-processing task                                 │
│  NOT called by: agent-conversation, generate-artifact                │
│  No sandbox involved — pure API calls → results to Supabase          │
└────────────────────────────────────────────────────────────────────┘
```

### Request Routing: What Goes Where

```
Incoming request
      │
      ▼
 Is it CRUD / dashboard?  ─── YES ──► Vercel directly (SSR, server actions)
 (auth, list contacts,                 No AI. No Trigger.dev.
  view pipeline, settings)
      │
      NO
      ▼
 Is it simple extraction?  ── YES ──► Vercel API route → Haiku → Supabase
 (single message, Tier 1,             Single generateText call, <10s.
  pattern-matching)                    No Trigger.dev needed.
      │
      NO
      ▼
 Is it a document/media?  ─── YES ──► Vercel saves to Storage, kicks off
 (PDF, image, forwarded                Trigger.dev "document-processing" task.
  file attachment)                      Gemini classifies → splits → extracts.
      │                                 No sandbox. No LLM conversation loop.
      NO                                Results stored in documents + extractions
      ▼                                 tables. Agent confirms via WhatsApp.
 Is it a user conversation? ─ YES ──► Vercel kicks off Trigger.dev task
 (Tier 2, may need tools,             "agent-conversation" with per-client
  multi-step, 10-300s)                 queue (concurrency: 1).
      │                                Streams back via Trigger.dev Realtime.
      NO
      ▼
 Is it artifact generation? ─ YES ──► Trigger.dev task calls sandbox.
 (PDF, chart, video)                   Checkpointed. Retries if sandbox fails.
      │
      NO
      ▼
 Is it a cron job?  ───────── YES ──► Trigger.dev scheduled task.
 (briefings, nudges)                   Batch triggers per client.
      │                                Concurrency-controlled.
      NO
      ▼
 Is it a Tier 3 approval?  ── YES ──► Vercel API route completes
 (user says "yes send it")             Trigger.dev waitpoint token.
      │                                Paused task resumes, sends message.
      NO
      ▼
 Is it a cancel?  ────────── YES ──► Vercel API route /api/cancel:
 (gateway regex matched                1. Cancel active Trigger.dev run
  "stop", "cancel", etc.)              2. Flush queued runs for this client
                                       3. Cancel pending waitpoints
                                       Gateway sends "Got it, cancelled."
```

---

## WhatsApp Permission Model

**Core principle: read everything, send almost nothing.**

Baileys `sendMessage(jid, ...)` targets a specific JID (phone number). There is no broadcast. Every send is a deliberate call. The permission model is enforced entirely in application code.

### Three permission tiers

```
TIER 1: READ ALL CHATS (always on)
───────────────────────────────────
• Baileys `messages.upsert` event fires for ALL incoming and outgoing messages
• `key.fromMe` flag distinguishes agent's own messages vs. received
• `syncFullHistory: true` + `Browsers.macOS('Desktop')` backfills history on first pair
• `fetchMessageHistory(50, key, timestamp)` pages through older messages
• AI extracts: contacts, interactions, follow-ups, deal signals, property mentions
• NEVER sends anything — pure observation

TIER 2: CONVERSE WITH USER ONLY (default on)
─────────────────────────────────────────────
• AI can send messages ONLY to the user's own JID (the paired phone number)
• This is the conversational interface — user talks to AI, AI responds
• Gateway enforces: sendMessage() only allowed where jid === client's own JID
• Morning briefings, nudges, task summaries — all sent to user's chat only

TIER 3: SEND TO THIRD-PARTY CONTACTS (explicit approval per message)
────────────────────────────────────────────────────────────────────
• User requests: "send [contact] a message about [topic]" or "schedule message to [contact] at [time]"
• AI drafts the message → sends preview to user's chat (Tier 2)
• User must explicitly approve: "yes send it" / "approve" / confirm button
• Only THEN does gateway execute sendMessage() to the third-party JID
• Scheduled messages: stored in `pending_messages` table with status `awaiting_approval`
• User can review/approve/reject pending messages via WhatsApp or dashboard
• NO auto-sends to third parties. Ever. Not even cron. Not even follow-ups.
```

### Why this matters

- **Trust:** Agent never worries AI will embarrass them with a client
- **Safety:** Worst case if AI hallucinates = a weird message to the user, not to their client
- **Adoption:** Lower barrier — "it just reads your chats" is way less scary than "it talks to your clients"
- **Upsell path:** Tier 3 approval flow is the premium feature agents unlock as trust builds

### Baileys implementation notes

```typescript
// Gateway worker enforces permission tiers
const CLIENT_JID = clientConfig.ownJid // e.g. '6591234567@s.whatsapp.net'

// Tier 1: Read all — just listen, never send
// Idempotency: Baileys replays messages on reconnect. Dedup by message key.id.
sock.ev.on('messages.upsert', async ({ messages, type }) => {
  for (const msg of messages) {
    // Dedup check — skip if already processed (survives reconnects, replays)
    const alreadyProcessed = await api.post('/api/extract/check', {
      clientId, messageId: msg.key.id
    })
    if (alreadyProcessed.duplicate) continue

    // Forward to Next.js API for extraction
    await api.post('/api/extract', {
      clientId, msg, type,
      fromMe: msg.key.fromMe,
      chatJid: msg.key.remoteJid,
      messageId: msg.key.id  // used for idempotency
    })
  }
})

// Cancel detection — check BEFORE routing to Trigger.dev
// Fast regex, no LLM. Runs in gateway for <1ms latency.
const CANCEL_PATTERNS = /^(stop|cancel|nevermind|never mind|nvm|wait no|hold on|abort|forget it)[\s!.]*$/i
async function handleUserMessage(msg: proto.IWebMessageInfo) {
  const text = msg.message?.conversation || msg.message?.extendedTextMessage?.text || ''
  if (CANCEL_PATTERNS.test(text.trim())) {
    await api.post('/api/cancel', { clientId })
    await sendToUser("Got it, cancelled.")
    return // don't route to agent
  }
  // Normal Tier 2 routing
  await api.post('/api/message', { clientId, text, messageType: 'text' })
}

// Tier 2: Only respond to user's own chat
async function sendToUser(text: string) {
  await sock.sendMessage(CLIENT_JID, { text })
}

// Tier 3: Approved sends only — gateway checks approval status
async function sendApproved(targetJid: string, messageId: string) {
  const pending = await db.getPendingMessage(messageId)
  if (pending.status !== 'approved') throw new Error('Not approved')
  if (pending.targetJid !== targetJid) throw new Error('JID mismatch')
  await sock.sendMessage(targetJid, { text: pending.content })
  await db.updatePendingMessage(messageId, { status: 'sent', sentAt: new Date() })
}
```

---

## Component 1: Baileys Gateway

### What it does

Maintains one WhatsApp WebSocket connection per user. Five jobs:
1. **Read all chats** → forward to Next.js API for CRM extraction (Tier 1) — with message dedup (LRU cache + DB check)
2. **Detect cancel intent** → regex match on "stop"/"cancel"/"nevermind" → POST /api/cancel (before routing to agent)
3. **Send AI responses to user only** → conversational interface (Tier 2)
4. **Execute approved sends** → third-party messages only after user approval (Tier 3)
5. **Health pings** → emit status to gateway manager

### Architecture

```
gateway-manager (Node.js process, DigitalOcean droplet)
├── REST API:
│   POST   /sessions              → provision new user
│   DELETE /sessions/:id          → tear down
│   GET    /sessions/:id/qr      → get QR code for pairing
│   GET    /sessions/:id/status  → connection status
│   GET    /sessions              → list all sessions + status
│   POST   /sessions/:id/send-approved → execute an approved Tier 3 send
│
├── Per-user Baileys workers (child processes):
│   Each worker:
│   ├── Connects to WhatsApp via Baileys
│   │   └── syncFullHistory: true (backfill on first pair)
│   ├── On ANY message (all chats):
│   │   POST next-app/api/extract { clientId, msg, chatJid, fromMe }
│   ├── On message from user's own JID (conversational):
│   │   POST next-app/api/message { clientId, text, media, messageType }
│   │   → Response sent back ONLY to user's JID
│   ├── On approved send (Tier 3):
│   │   Verify approval in DB → sendMessage(targetJid, content)
│   ├── Stores auth state to disk (/data/sessions/:id/auth.json)
│   └── Emits health pings to manager
│
├── Health monitor:
│   ├── Pings each worker every 30s
│   ├── Auto-restarts crashed workers
│   └── Reports status to admin dashboard
│
└── Auth state storage:
    /data/sessions/
    ├── client_abc/auth.json
    ├── client_def/auth.json
    └── ...
    (persisted volume — survives restarts)
```

### Key decisions

- **Child processes for MVP**, not Docker containers. Simpler. Move to containers later if isolation becomes important.
- **Auth state on disk.** Baileys stores session credentials as JSON. Persist to a mounted volume so users don't re-scan QR after server restart.
- **~50MB RAM per user.** 4GB server = ~60-70 users. 8GB = 120+.
- **Gateway-to-API auth:** Gateway signs requests with a shared secret (HMAC or API key). Next.js API route verifies the request came from the gateway, not spoofed.
- **Send guard:** Gateway code physically cannot send to a non-user JID without a DB-verified approval record. Defense in depth — even if the API has a bug, gateway blocks it.
- **Separate from Next.js app.** Gateway needs persistent WebSocket connections and disk-based auth state. Can't run on Vercel (serverless). Lives on DigitalOcean.

### Scaling

| Users | Infra |
|---|---|
| 1-70 | Single 4GB droplet ($24/mo) |
| 70-150 | Single 8GB droplet ($48/mo) |
| 150+ | Two gateway hosts + load balancer, sessions pinned by userId |

---

## Component 2: API Layer (Next.js API Routes + OAI Agents SDK)

### What it does

All AI reasoning lives here. Five jobs: extract CRM data from all chats, handle user conversations, generate artifacts, process approved sends, execute cron.

### Three Execution Modes

The API handles three fundamentally different types of requests:

```
REASONER PATH (~85% of messages)
─────────────────────────────────
User: "What's Sarah's status?"
→ OAI Agents SDK: run(chatAgent, message) — Gemini 2.5 Flash ($0.075/1M)
→ search_contacts("Sarah") → Supabase query
→ Return: "Sarah Lee — last contacted Jan 28, viewing at 38 Orchard..."
No sandbox. No extraction. Just structured tools + database.

DOCUMENT PATH (~5% of messages)
────────────────────────────────
User: [forwards a PDF brochure via WhatsApp]
→ File saved to Supabase Storage
→ Trigger.dev task: "document-processing"
→ Gemini 2.5 Flash classifies + splits the document
→ Per-split: Gemini structured output OR ExtendAI extracts fields
→ Auto-links to CRM (fuzzy match contact/deal)
→ Return: "Filed the brochure for Parc Clematis under Sarah's deal.
   Unit mix: 1BR-4BR. Pricing: $1.2M-$3.8M. TOP: 2027."
No sandbox. No LLM conversation loop. Purpose-built extraction pipeline.

CREATOR PATH (~10% of messages)
────────────────────────────────
User: "Generate a PDF comparison of these 3 properties"
→ OAI Agents SDK: run(reasoningAgent, message) — Kimi 2.5 ($0.28/1M) or Gemini Flash
→ CRM tools fetch property data from Supabase
→ generate_artifact({ task: "...", files: [...] }) → E2B sandbox boots (150ms)
→ Claude Agent SDK runs inside sandbox (Sonnet $3/1M):
  Claude reads data → writes Python → executes → fixes errors → saves output
→ Output uploaded to Supabase Storage → PDF link to user via WhatsApp
```

**How routing works:**
- **Reasoner + Creator** share a single OAI Agents SDK `run()` call. The model decides whether it needs the sandbox (by calling `generate_artifact`) or not. We don't classify — the model routes itself via tool selection. Classification between chatAgent (Gemini Flash) and reasoningAgent (Kimi 2.5) happens at the Trigger.dev task level based on message complexity.
- **Document path** is completely separate. Triggered by media type detection (PDF/image attachment), not by the conversational LLM. Runs a deterministic pipeline (classify → split → extract), not a tool loop. The agent-conversation task only gets involved AFTER extraction completes, to confirm results with the user.

```
              ┌─────────────────┐
              │  Message arrives │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  Has attachment? │
              └────┬────────┬───┘
                   │        │
                  YES       NO
                   │        │
                   ▼        ▼
         ┌─────────────┐  ┌──────────────────────────┐
         │  DOCUMENT    │  │  CONVERSATION              │
         │  PATH        │  │  (Reasoner or Creator)     │
         │              │  │                            │
         │  Trigger.dev │  │  Trigger.dev               │
         │  document-   │  │  agent-conversation        │
         │  processing  │  │                            │
         │              │  │  generateText + tools      │
         │  Gemini      │  │  ├─ CRM tools (Reasoner)   │
         │  classify →  │  │  ├─ query_crm (SQL agent)  │
         │  split →     │  │  ├─ search_documents 🔗    │
         │  extract     │  │  ├─ generate_artifact      │
         │              │  │  │  (Creator → sandbox)    │
         │  ExtendAI    │  │  └─ browse_property_site   │
         │  (complex)   │  │     (Browserbase)          │
         │              │  │                            │
         │  Results →   │  │  Model self-routes via     │
         │  Supabase    │  │  tool selection             │
         └──────┬───────┘  └──────────────┬─────────────┘
                │                          │
                │   ┌──────────────────┐   │
                └──►│  SUPABASE         │◄──┘
                    │                   │
                    │  contacts, deals  │
                    │  documents  🔗    │
                    │  extractions      │
                    │  ai_memory        │
                    │  artifacts        │
                    │  Storage buckets  │
                    └───────────────────┘

🔗 = The bridge. Document path WRITES to documents/extractions tables.
     Conversation path READS via search_documents + query_crm tools.
```

### Agent SDK + Model Routing (v3.0)

**Two-SDK architecture:** OpenAI Agents SDK for the main agent (multi-model, cheap), Claude Agent SDK inside E2B sandbox for artifact generation (best harness, Claude-only).

**Main agent setup:**

```typescript
// lib/agent.ts
import { Agent, run, tool } from '@openai/agents';
import { aisdk } from '@openai/agents-extensions';
import { google } from '@ai-sdk/google';
import { createOpenRouter } from '@openrouter/ai-sdk-provider';
import { z } from 'zod';

const openrouter = createOpenRouter({ apiKey: process.env.OPENROUTER_API_KEY! });

// ── Models ──────────────────────────────────
const flashModel = aisdk(google('gemini-2.5-flash'));
const kimiModel  = aisdk(openrouter.chat('moonshotai/kimi-k2'));

// ── Agents (same tools, different models) ───
const chatAgent = new Agent({
  name: 'RE Assistant',
  instructions: '...', // from SOUL.md
  model: flashModel,   // Gemini 2.5 Flash — $0.075/1M input
  tools: [getContact, updateContact, addInteraction, createTask,
          updateMemory, queryCrm, draftMessage, generateArtifact],
});

const reasoningAgent = new Agent({
  name: 'RE Analyst',
  instructions: '...', // enhanced for analysis
  model: kimiModel,    // Kimi 2.5 — $0.28/1M input
  tools: [getContact, updateContact, addInteraction, createTask,
          updateMemory, queryCrm, draftMessage, generateArtifact],
});

// ── Run inside Trigger.dev task ─────────────
const result = await run(agent, userMessage, { maxTurns: 10 });
```

**Sandbox tool (calls Claude Agent SDK inside E2B):**

```typescript
// lib/tools/sandbox.ts
const generateArtifact = tool({
  name: 'generate_artifact',
  description: 'Generate PDFs, charts, spreadsheets in a secure sandbox.',
  parameters: z.object({
    task: z.string(),
    files: z.array(z.object({ name: z.string(), storagePath: z.string() })).optional(),
  }),
  execute: async ({ task, files }) => {
    const sandbox = await Sandbox.create('claude-code-sandbox', {
      timeoutMs: 5 * 60 * 1000,
      envs: { ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY! },
    });
    // Upload files, then run Claude Agent SDK inside sandbox
    const result = await sandbox.commands.run(
      `echo '${escapeForShell(prompt)}' | claude -p --dangerously-skip-permissions --max-turns 20`,
      { timeoutMs: 4 * 60 * 1000 }
    );
    // Download output files → Supabase Storage → return URLs
    // ... (see DECISION-agent-sdk-model-routing.md for full implementation)
  },
});
```

**Model routing registry:**

| Task Type | Model | Provider | Cost (per 1M input) | When |
|---|---|---|---|---|
| **Tier 1: Extraction** | Gemini 2.0 Flash | Google direct | ~$0 (free preview) | Every WhatsApp message (passive CRM extraction) |
| **Tier 2: Simple chat** | Gemini 2.5 Flash | Google direct | $0.075 | "Show me John's deals", simple CRM ops |
| **Tier 2: Complex reasoning** | Kimi 2.5 | OpenRouter | $0.28 | Deal analysis, strategy, multi-step |
| **Tier 3: Draft messages** | Gemini 2.5 Flash | Google direct | $0.075 | Drafting outbound messages for approval |
| **Sandbox: Artifacts** | Claude Sonnet 4.5 | Anthropic (Claude Agent SDK) | $3.00 | PDF, charts, data pipelines |
| **Cron: Briefings** | Gemini 2.5 Flash | Google direct | $0.075 | Morning briefings, nudges (templated) |

**Cost estimate (1000 msgs/day):**

| Category | Volume | Model | Monthly Cost |
|---|---|---|---|
| Tier 1 extraction | 1000/day | Gemini 2.0 Flash | ~$0 |
| Simple chat | 900/day | Gemini 2.5 Flash | ~$27 |
| Complex reasoning | 50/day | Kimi 2.5 | ~$15 |
| Artifact generation | 50/day | Claude Sonnet (sandbox) | ~$450 |
| **Total** | | | **~$492/mo** |

vs. ~$1,500+/mo all-Sonnet. **~67% savings** (up to 94% if artifact volume is lower).

**Why Claude Agent SDK in sandbox is the harness:**

The entire harness we'd otherwise need to build (error recovery, file ops, code execution, search, pre-flight analysis, output validation) is built into Claude Agent SDK. It wraps the Claude Code CLI as a subprocess. Inside E2B:
- Claude reads data files itself (Read tool)
- Writes and executes Python code (Write + Bash tools)
- If code errors, Claude sees the error and fixes it autonomously
- Searches for files with Glob/Grep
- Budget capped via `max_budget_usd`
- Cost tracked via `total_cost_usd` in result

**Tradeoff:** Claude Agent SDK only works with Claude models (Claude-locked inside sandbox). Acceptable because sandbox tasks are rare (5-10% of volume) and high-value (artifact quality matters more than cost).

**Environment variables:**

```
# Main agent (OAI Agents SDK)
OPENROUTER_API_KEY=sk-or-v1-xxx       # Kimi, DeepSeek, fallback models
GOOGLE_GENERATIVE_AI_API_KEY=xxx      # Gemini Flash (direct, lower latency)

# Sandbox (passed to E2B at runtime)
ANTHROPIC_API_KEY=sk-ant-xxx          # Claude Agent SDK inside sandbox
E2B_API_KEY=e2b_xxx                   # E2B sandbox provisioning
```

**Packages:**

```bash
# Main agent
npm install @openai/agents @openai/agents-extensions zod
npm install @ai-sdk/google @openrouter/ai-sdk-provider

# Sandbox (E2B provisioning — Claude Agent SDK installed INSIDE template, not here)
npm install @e2b/code-interpreter
```

### Data Flows

**Flow 1: Passive CRM extraction (Tier 1 — all chats)**

```
Gateway POSTs to /api/extract (every message from every chat)
→ Auth: verify gateway HMAC signature, resolve clientId
→ Filter: skip delivery receipts, read receipts, group messages, status updates
→ If CRM-relevant:
    → generateText with Haiku + extraction tools
    → Extract: contact info, interaction summary, follow-up signals, deal mentions
    → Tools write directly to Supabase (create/update contacts, log interactions)
→ No response sent back. Pure data ingestion.
```

**Flow 2: User conversation (Tier 2 — user's own chat only)**

```
Gateway POSTs to /api/message (only messages from user's own JID)
→ Auth: verify gateway HMAC signature, resolve clientId
→ Vercel API route triggers Trigger.dev task:
    tasks.trigger("agent-conversation", {
      clientId, message, messageType
    })
→ Returns runId to gateway immediately
→ Gateway subscribes to Trigger.dev Realtime for streaming response

════ INSIDE TRIGGER.DEV (durable, checkpointed, per-client queue) ════

→ Register active run (for cancellation):
    • INSERT INTO active_agent_runs (client_id, run_id, status)
    • If user sends "cancel", /api/cancel looks up this run_id

→ Session boundary check:
    • Time since last message?
      < 2h → SAME SEGMENT: load full recent history
      2-8h → NEW SEGMENT: compact old segment, start fresh with summary
      > 8h → NEW DAY: compact everything, start with memory + today's tasks
    • Explicit reset? ("new topic", "start fresh") → force new segment
    • User says reset → compact current segment → clean slate

→ Context compaction (if triggered):
    • Split old messages into 50-msg chunks
    • Summarize each chunk with Haiku (cheap, pattern-matching)
    • Store summaries in conversation_summaries table
    • Mark original messages as compacted (never delete)
    ── CHECKPOINT after compaction ──

→ Load context:
    • ai_memory (agent's self-written notes about this client)
    • Conversation summaries (compacted history from prior segments/days)
    • Recent conversation messages (current segment, up to 50)
    • Today's tasks + overdue follow-ups + recurring task reminders
    • Quick keyword scan: if message mentions a contact name → pre-load that contact
→ Build system prompt (see SOUL.md for full personality definition):
    LAYER 1: Base personality (from SOUL.md — identity, tone, behavior rules)
    + LAYER 2: Domain knowledge (contact types, deal stages, SG RE specifics)
    + LAYER 3: Client memory (preferences, relationships, avoid-list from ai_memory)
    + LAYER 4: Context (conversation summaries + recent messages + tasks + contacts)
→ OAI Agents SDK: run(agent, message, { maxTurns: 10 })
    Agent model selected by classification: chatAgent (Gemini Flash) or reasoningAgent (Kimi 2.5)
    ── CHECKPOINT after each tool call (state survives crashes) ──
→ Agent loop runs automatically (built into OAI Agents SDK):
    Model calls tools → SDK executes them → feeds results back → model continues
    Until model generates final text response or hits maxTurns limit
→ If model called `draft_message_to_contact`:
    → pending_messages record created (status: awaiting_approval)
    → trigger_token_id stored (for waitpoint resume)
    → Response includes draft preview for user to approve
→ If model called `generate_artifact`:
    → Subtask triggered: "generate-artifact" (separate Trigger.dev task)
    → Sandbox spins up, produces file, uploads to Supabase Storage
    → Artifact URL returned as tool result to model
→ Store interaction (user message + AI response) in Supabase
→ Stream final response text via Trigger.dev Realtime
→ Gateway receives stream → sends to user's WhatsApp

════ END TRIGGER.DEV TASK ════

Why Trigger.dev here:
• Agent tool loops take 10-300s (Vercel times out at 60s)
• Per-client queue (concurrency: 1) prevents interleaved responses
• If server crashes mid-loop, resumes from last checkpoint
• If user sends "cancel", /api/cancel calls runs.cancel() → task gets CancelledError at next checkpoint
• Full trace of every tool call for debugging
```

**Flow 3: Approved send execution (Tier 3 — with waitpoints)**

```
OPTION A: Immediate approval (user replies "yes send it")
→ Gateway POSTs user reply to /api/message
→ Trigger.dev task recognizes approval intent
→ Updates pending_messages.status = 'approved'
→ Calls gateway POST /sessions/:id/send-approved
→ Gateway verifies approval → sends via Baileys → updates status to 'sent'

OPTION B: Draft-then-approve with waitpoint (async approval)
→ During agent-conversation task, model drafts a message
→ Task creates waitpoint token + pending_messages record:

    // Inside the agent-conversation Trigger.dev task:
    import { wait } from "@trigger.dev/sdk/v3";

    const token = await wait.createToken({
      idempotencyKey: `approve-msg-${pendingMessageId}`,
      timeout: "24h",
      tags: [`client-${clientId}`, `pending-${pendingMessageId}`],
    });
    // Store token.id in pending_messages row for later lookup
    await db.updatePendingMessage(pendingMessageId, {
      trigger_token_id: token.id,
    });

→ Task pauses, waiting for token completion:

    const approval = await wait.forToken<{ approved: boolean }>(token);
    // ══ TASK PAUSES HERE (zero compute cost) ══

→ User approves later via WhatsApp or dashboard
→ Vercel API route /api/approve completes the token:

    // In Vercel API route:
    import { wait, configure } from "@trigger.dev/sdk/v3";
    configure({ secretKey: process.env.TRIGGER_SECRET_KEY });

    await wait.completeToken<{ approved: boolean }>(
      tokenId,
      { approved: true }
    );

→ ══ TASK RESUMES from exact state ══

    if (approval.ok && approval.output.approved) {
      await gateway.sendApproved(clientId, pendingMessageId);
      await db.updatePendingMessage(pendingMessageId, { status: "sent" });
    }

Why waitpoints:
• No polling. Task literally sleeps until user acts.
• Zero compute cost during wait (could be minutes or hours).
• If user never approves, token expires after 24h → approval.ok = false → task cleans up.
• idempotencyKey prevents duplicate tokens if user triggers the same draft twice.
```

**Flow 4: Artifact generation (Creator path — E2B + Claude Agent SDK)**

```
Model calls generate_artifact tool during agent-conversation task:
→ Trigger.dev subtask triggered: "generate-artifact"
    ── CHECKPOINT before sandbox call ──
→ E2B sandbox boots from custom template (150ms)
    Template: 'claude-code-sandbox'
    Pre-installed: Claude Agent SDK + Python libs (pandas, matplotlib, reportlab, etc.)
    Env: ANTHROPIC_API_KEY passed at runtime
→ Upload input files from Supabase Storage to /home/user/
→ Claude Agent SDK runs inside sandbox:
    echo '<task prompt>' | claude -p --dangerously-skip-permissions --max-turns 20
    Claude autonomously:
    • Reads input files (Read tool)
    • Writes Python code (Write tool)
    • Executes code (Bash tool)
    • If error → sees error → fixes code → retries (built-in)
    • Saves output to /home/user/output/
    • Budget capped via --max-budget-usd
→ Download files from /home/user/output/
→ Upload to Supabase Storage (scoped to client_id)
    ── CHECKPOINT after sandbox returns ──
→ Storage URL returned as tool result to main agent (OAI Agents SDK)
→ Main agent incorporates link into its response to user
→ E2B sandbox shuts down (ephemeral)

Why Claude Agent SDK inside E2B:
• Claude Agent SDK IS the harness — error recovery, file ops, code execution all built-in
• No DIY retry loops, no custom tool wiring, no pre-flight analysis code
• Claude reads files, writes code, executes, fixes errors autonomously
• Budget caps prevent runaway costs (max_budget_usd parameter)
• Cost tracking: total_cost_usd returned in result

Why E2B (not Vercel Sandbox):
• Custom templates: pre-install Claude Agent SDK + Python libs (zero pip install at runtime)
• 150ms cold start
• Sandbox pause/resume (beta) for warm starts
• ~$0.08/hour per sandbox

Why Trigger.dev wraps the sandbox call:
• Sandbox execution can take 30-120s (fragile, may timeout)
• If sandbox fails, Trigger.dev retries automatically
• Parent task (agent-conversation) checkpointed before/after
• If sandbox crashes, only the sandbox step retries — not the whole conversation
```

**Flow 5: Per-user browser research (Browserbase)**

```
Agent calls browse_property_site tool during agent-conversation task:
→ Trigger.dev subtask triggered: "browser-research"
   ── CHECKPOINT before browser call ──
→ Load Browserbase Context for this client_id (persists cookies/localStorage)
→ If no context exists (first time):
   → Create new Context, send Live View link to user via WhatsApp
   → User authenticates in browser (login to 99.co, PropertyGuru, etc.)
   → Trigger.dev waitpoint pauses until user confirms login complete
→ Connect to Browserbase session with client's Context
→ Stagehand navigates property site, extracts listings/data
→ Results returned as structured JSON tool result
   ── CHECKPOINT after browser returns ──
→ Session disconnects (Context persists cookies for next time)
→ Model incorporates property data into response

Why Browserbase (not Playwright in Vercel Sandbox):
• Contexts API persists cookies/localStorage per user across sessions
  (Vercel Sandbox is ephemeral — cookies lost on shutdown)
• Live View provides embeddable iframe for user to authenticate
  (no way to do this in a headless sandbox)
• Anti-detection built-in (residential proxies, stealth browser)
  (property portals block headless Chrome)
• Stagehand uses accessibility tree (CDP), not screenshots
  (~100x smaller in tokens than screenshot-based automation)
• Native Trigger.dev integration via SDK
```

**Flow 6: Document processing (inbound extraction)**

```
User forwards a PDF/image via WhatsApp (or uploads via dashboard):
→ Gateway detects media attachment in message
→ Gateway POSTs to /api/document { clientId, mediaBuffer, filename, mimeType }
→ Vercel API route:
    1. Uploads file to Supabase Storage (documents/{client_id}/{doc_id}.pdf)
    2. Creates row in documents table (status: 'uploaded')
    3. Triggers Trigger.dev task: "document-processing"
→ Returns immediately (user sees "Processing your document...")

════ INSIDE TRIGGER.DEV (durable, checkpointed, per-client queue) ════

→ Upload to Google Files API (temporary, for Gemini vision)
   ── CHECKPOINT ──

→ Gemini 2.5 Flash: classify + split
   Tag pool = platform tags (8 RE defaults) + client's custom tags (from extraction_schemas)
   Each tag has classificationHint (2-3 sentences)
   Returns: { splits: [{ type, startPage, endPage, identifier, date }] }
   ── CHECKPOINT after classification ──

→ For each split:
   a. If PDF with multiple splits: extract page range as child PDF
   b. Look up extraction schema (platform tag OR client's custom schema)
   c. Route to backend:
      • extraction_backend = 'gemini' → Gemini structured output (free, simple schemas)
      • extraction_backend = 'extend' → ExtendAI processor (per-field confidence + citations)
   d. Store results in document_extractions table
   ── CHECKPOINT after each split ──

→ Auto-link to CRM:
   • Scan extracted data for contact names → fuzzy match contacts table
   • Scan for property addresses → match active deals
   • Set document.contact_id and document.deal_id if confident match

→ Delete from Google Files API (cleanup)

→ Trigger agent-conversation subtask to confirm with user:
   "Filed the OTP for 42 Noriega under Sarah Chen's deal.
    Exercise deadline: Feb 28. Option fee: $5K (1%).
    Want me to create a task for the deadline?"

════ END TRIGGER.DEV TASK ════

Key differences from other flows:
• NO generateText tool loop — deterministic pipeline (classify → split → extract)
• NO sandbox — pure API calls to Gemini + ExtendAI, results to Supabase
• NO LLM conversation during processing — agent only talks to user AFTER extraction
• Uses per-client queue (same concurrencyKey pattern as agent-conversation)
• The only LLM call is Gemini for classification/extraction (not the conversational model)
```

**How document data flows back into the CRM conversation:**

```
Document path WRITES:                     Conversation path READS:
─────────────────────                      ──────────────────────
documents table ──────────────────────────► search_documents tool
  (file metadata, tags, CRM links)            "Find the OTP for Sarah's deal"

document_extractions table ───────────────► search_documents tool
  (structured fields, confidence)              Returns extracted fields

extraction_schemas table ─────────────────► list_extraction_schemas tool
  (user's custom doc types)                    Shows available schemas

documents.contact_id FK ──────────────────► query_crm tool (SQL agent)
  (linked to contacts table)                   "All documents for Sarah Chen"
                                               JOIN documents ON contact_id

documents.deal_id FK ─────────────────────► query_crm tool (SQL agent)
  (linked to deals table)                      "All docs for the Orchard deal"
                                               JOIN documents ON deal_id
```

The document system and CRM conversation are **decoupled but linked through Supabase.** The document path doesn't need to understand conversation context. The conversation path doesn't need to understand extraction pipelines. They share data through tables + foreign keys.

### Tools

```typescript
import { tool } from 'ai'
import { z } from 'zod'

// CRM tools (used by both extraction and conversation)
const crmTools = {
  search_contacts: tool({
    description: 'Query contacts by name, type, status, or other fields',
    inputSchema: z.object({
      query: z.string(),
      type: z.enum(['buyer', 'seller', 'investor', 'referral', 'other']).optional(),
    }),
    execute: async ({ query, type }) => { /* Supabase query */ },
  }),

  create_contact: tool({
    description: 'Create a new contact from extracted or reported data',
    inputSchema: z.object({
      name: z.string(),
      phone: z.string().optional(),
      email: z.string().optional(),
      type: z.string(),
    }),
    execute: async (input) => { /* Supabase insert */ },
  }),

  update_contact: tool({ /* update contact fields, structured data */ }),
  create_interaction: tool({ /* log a call, meeting, showing, text */ }),
  get_follow_ups: tool({ /* today's tasks, overdue items */ }),
  create_task: tool({ /* schedule a follow-up or reminder */ }),
  enrich_lead: tool({ /* call enrichment APIs for a person */ }),
  get_property_comps: tool({ /* comparable sales for an address */ }),
  score_lead: tool({ /* assess lead quality from signals */ }),
  update_deal: tool({ /* move deal stage, update value */ }),

  // Flexible SQL query tool — for ad-hoc CRM queries pre-defined tools can't handle
  query_crm: tool({
    description: 'Run a read-only SQL query against the CRM database. Use when pre-defined tools are insufficient for the question. Examples: "contacts with budget > $1.5M not contacted in 2 weeks", "pipeline value by stage this month vs last month", "all contacts referred by David Tan".',
    inputSchema: z.object({
      query: z.string().describe('SELECT query to execute. Must be SELECT only.'),
      explanation: z.string().describe('What you are trying to find and why'),
    }),
    execute: async ({ query, explanation }) => {
      // Guardrails:
      // 1. SELECT only — reject anything else
      if (!query.trim().toUpperCase().startsWith('SELECT')) {
        return { error: 'Only SELECT queries allowed' };
      }
      // 2. RLS enforces client_id scoping automatically (Supabase)
      // 3. Timeout: 10s max execution time
      // 4. Result limit: cap at 200 rows
      // 5. If result > 50 rows, return summary + stage to Storage for sandbox use

      const result = await db.query(query, { timeout: 10000 });

      if (result.rows.length > 50) {
        // Stage to Supabase Storage for potential sandbox use
        const path = `artifacts/${clientId}/query_${Date.now()}.json`;
        await supabaseStorage.upload('artifacts', path, JSON.stringify(result.rows));
        return {
          summary: `${result.rows.length} rows returned.`,
          schema: Object.keys(result.rows[0] || {}),
          preview: result.rows.slice(0, 10),
          stagedPath: path, // Available for generate_artifact if needed
        };
      }

      return { rows: result.rows, count: result.rows.length };
    },
  }),
}

// Memory tools (model-agnostic — any LLM can call these)
const memoryTools = {
  update_memory: tool({
    description: 'Save or update a note about this client for future reference. Use for preferences, relationships, things to avoid, communication style, or any insight worth remembering.',
    inputSchema: z.object({
      action: z.enum(['add', 'update', 'delete']),
      key: z.string().describe('Category: preferences, relationships, avoid, style, contacts/[name]'),
      content: z.string().describe('The note content in plain text'),
    }),
    execute: async ({ action, key, content }) => {
      // UPSERT/DELETE on ai_memory table, scoped to client_id
      // When pgvector enabled: also generate + store embedding on write
    },
  }),

  recall_memory: tool({
    description: 'Search your memory for information about this client, their contacts, preferences, or any previously saved notes. Use at the start of conversations and when context is needed.',
    inputSchema: z.object({
      query: z.string().describe('Natural language search — e.g. "buyer looking in District 10" or "agent preferences"'),
    }),
    execute: async ({ query }) => {
      // MVP: tsvector FTS (full-text search on key + value)
      // v2: hybrid vector + FTS via Supabase RPC search_memory function
      const results = await db.rpc('search_memory', {
        p_client_id: clientId, p_query: query, p_limit: 10,
      });
      return results.length > 0
        ? results.map(r => `[${r.key}] ${r.value}`).join('\n\n')
        : 'No matching memories found.';
    },
  }),
}

// Scheduling tools (agent can create its own recurring reminders)
const schedulingTools = {
  manage_recurring_task: tool({
    description: 'Create, update, or cancel a recurring task/reminder. Use when the agent wants something to repeat on a schedule (e.g., "remind me every Tuesday to follow up with Sarah").',
    inputSchema: z.object({
      action: z.enum(['create', 'update', 'pause', 'resume', 'cancel', 'list']),
      id: z.string().optional().describe('Task ID (required for update/pause/resume/cancel)'),
      contactId: z.string().optional(),
      description: z.string().optional(),
      scheduleType: z.enum(['daily', 'weekly', 'biweekly', 'monthly']).optional(),
      scheduleDay: z.number().optional().describe('Day of week (0=Sun) or day of month'),
      scheduleTime: z.string().optional().describe('Time in HH:MM format, e.g. "09:00"'),
    }),
    execute: async (input) => {
      // create: INSERT recurring_tasks, calculate next_run_at
      // list: SELECT active recurring tasks for client
      // cancel/pause/resume: UPDATE status
      // Recurring tasks are processed by the existing process-scheduled cron
    },
  }),
}

// Skills (lazy-loading: model reads skill files on demand)
const skillTools = {
  read_skill: tool({
    description: 'Read a skill file to get detailed instructions. Call this BEFORE executing a skill workflow. Use the slug from the Available Skills menu in your system prompt.',
    inputSchema: z.object({
      slug: z.string().describe('Skill slug from Available Skills menu'),
    }),
    execute: async ({ slug }) => { /* See Skills Filesystem Architecture section */ },
  }),

  manage_skill: tool({
    description: 'Create, update, delete, or list user skill files. Use when user teaches a new process, template, or workflow.',
    inputSchema: z.object({
      action: z.enum(['create', 'update', 'delete', 'list']),
      slug: z.string().optional(),
      content: z.string().optional(),
      description: z.string().optional(),
    }),
    execute: async (input) => { /* See Skills Filesystem Architecture section */ },
  }),
}

// Tier 3: Approved messaging (conversation flow only, never extraction)
const messagingTools = {
  draft_message_to_contact: tool({
    description: 'Draft a message to a contact for user approval. NOT sent immediately.',
    inputSchema: z.object({
      contactId: z.string(),
      content: z.string(),
      context: z.string().describe('Why this message is being sent'),
    }),
    execute: async (input) => {
      // Creates pending_messages record with status: awaiting_approval
    },
  }),

  schedule_message: tool({ /* schedule a drafted message for future send */ }),
  list_pending_messages: tool({ /* show user their pending/scheduled messages */ }),
  cancel_pending_message: tool({ /* cancel a scheduled message */ }),
}

// Document tools (inbound extraction — see Document System section)
const documentTools = {
  process_document: tool({ /* classify, split, extract structured data from uploaded doc */ }),
  search_documents: tool({ /* find docs by type, contact, deal, date, or content */ }),
  create_extraction_schema: tool({ /* user defines custom doc type via conversation */ }),
  update_extraction_schema: tool({ /* add/remove fields, change types, archive */ }),
  list_extraction_schemas: tool({ /* platform defaults + user custom schemas */ }),
}

// JIT UI: Ambiguity resolution tools (see JIT UI for Ambiguity Resolution section)
const ambiguityTools = {
  ask_user: tool({
    description: 'Ask the user a scoping question via WhatsApp poll when the request is ambiguous. Use this BEFORE generating artifacts when you are unsure about what the user wants.',
    inputSchema: z.object({
      question: z.string().describe('The poll question'),
      options: z.array(z.string()).max(5).describe('Poll options (max 5)'),
      context: z.string().describe('Why you are asking this — shown as a message before the poll'),
      allowMultiple: z.boolean().default(false).describe('Allow selecting multiple options'),
    }),
    execute: async ({ question, options, context, allowMultiple }) => {
      // 1. Send context message to user's chat (Tier 2)
      // 2. Send WhatsApp poll via Baileys:
      //    sock.sendMessage(clientJid, { poll: { name: question, values: options, selectableCount: allowMultiple ? options.length : 1 } })
      // 3. Create waitpoint token for poll response
      // 4. Task pauses (zero compute) until user votes
      // 5. Poll response forwarded to agent as tool result
    },
  }),

  generate_preview: tool({
    description: 'Generate a visual preview of what you will build. Use after scoping questions are answered. Sends a preview link to the user in WhatsApp.',
    inputSchema: z.object({
      type: z.enum(['comparison', 'pipeline', 'contact_summary', 'report_outline', 'task_list', 'market_snapshot']),
      spec: z.record(z.any()).describe('Structured JSON matching the preview component schema'),
      summary: z.string().describe('1-2 sentence description of what the preview shows — sent as WhatsApp message alongside the link'),
    }),
    execute: async ({ type, spec, summary }) => {
      // 1. Store spec in preview_specs table (nanoid, expires in 24h)
      // 2. Send WhatsApp message: summary + sunder.app/preview/{id} link
      // 3. Create waitpoint token for user confirmation
      // 4. Task pauses until user confirms ("looks good") or requests changes
      // 5. If changes requested: agent modifies spec, generates new preview
      // 6. If confirmed: proceed to generate final output
    },
  }),
}

// Creator path: Artifact generation (triggers sandbox)
const creatorTools = {
  generate_artifact: tool({
    description: 'Generate a file artifact: PDF report, chart, property video, Excel export. Spins up a sandbox to execute code.',
    inputSchema: z.object({
      type: z.enum(['pdf', 'chart', 'video', 'excel', 'image']),
      instructions: z.string().describe('What to generate and how'),
      data: z.any().optional().describe('Structured data (for small payloads <50 rows)'),
      stagedDataPath: z.string().optional().describe('Supabase Storage path from query_crm staging (for large payloads >50 rows). Sandbox downloads directly.'),
    }),
    execute: async ({ type, instructions, data, stagedDataPath }) => {
      // Validation: must have either data or stagedDataPath
      if (!data && !stagedDataPath) {
        return { error: 'Must provide either data or stagedDataPath' };
      }

      // Validate data shape before passing to sandbox
      // (prevents LLM hallucinating/omitting fields from producing wrong artifacts)
      if (data && type === 'pdf') {
        const required = ['title']; // type-specific validation
        const missing = required.filter(f => !(f in data));
        if (missing.length) return { error: `Missing required fields: ${missing.join(', ')}` };
      }

      // Spin up Vercel Sandbox
      // If stagedDataPath: sandbox downloads from Supabase Storage directly
      // If data: pass as JSON payload
      // Execute generation code with pre-installed deps
      // Upload result to Supabase Storage
      // Return { url, type, filename }
    },
  }),

  browse_property_site: tool({
    description: 'Research properties on listing sites (99.co, PropertyGuru) using the user\'s authenticated browser session. Returns structured listing data.',
    parameters: z.object({
      site: z.enum(['99co', 'propertyguru', 'srx']),
      action: z.enum(['search', 'get_listing', 'get_saved']),
      query: z.string().optional(), // search terms, listing URL, etc.
    }),
    execute: async ({ site, action, query }) => {
      // Trigger.dev subtask: browser-research
      // Load Browserbase Context for client_id
      // If no context → prompt user to authenticate via Live View
      // Stagehand navigates site, extracts data
      // Return { listings: [...], source, timestamp }
    },
  }),
}
```

**Critical:** `draft_message_to_contact` creates a `pending_messages` record. It does NOT send. The gateway physically blocks any send without a matching approved record.

### Memory Architecture

The agent maintains its own memory by calling `update_memory`. No filesystem, no Anthropic Memory Tool — just a standard tool backed by Supabase.

**How it works:**

```
Day 1 — empty ai_memory table for this client.

After a week of conversations, the agent has written:

key: "preferences"
value: "Prefers concise updates. Hates long bullet lists.
        Morning briefing at 8am, not 7am. Prices in PSF not total."

key: "relationships"
value: "David at UOB = top referral partner (3 deals).
        Sarah Chen at PropNex = friendly competitor, sometimes co-broke."

key: "avoid"
value: "Don't suggest District 27 properties (bad experience, mentioned Jan 15).
        Don't contact Mike Tan before 10am (gets annoyed)."

key: "style"
value: "Signs off messages with 'Cheers'. Uses 'bro' casually.
        Prefers property prices in PSF, not total."

key: "contacts/sarah-lee"
value: "Buyer, budget $1.5M, looking in District 10. Price-sensitive.
        Worried about lease expiry at 42 Noriega (18 months left)."
```

The agent wrote all of this itself via `update_memory` tool calls. We didn't code detection logic — the model naturally notices things worth remembering.

**Memory is injected into the system prompt every request:**

```typescript
const memories = await db.getMemories(clientId) // SELECT * FROM ai_memory WHERE client_id = ?
const memoryBlock = memories.map(m => `## ${m.key}\n${m.value}`).join('\n\n')

const systemPrompt = `
${BASE_PERSONALITY}
${DOMAIN_KNOWLEDGE}

## Your Memory (notes you've written about this client)
${memoryBlock}

## Today's Context
${todaysTasks}
${recentConversation}
${detectedContacts}
`
```

**Why not Anthropic Memory Tool:** Lock-in. The Memory Tool is Claude-specific beta. Our `update_memory` tool works with any model — Claude, Kimi, DeepSeek, anything with tool calling.

**Memory search — migration path:**

| Phase | Search method | Trigger | What changes |
|-------|-------------|---------|-------------|
| MVP | Full table scan (`SELECT * WHERE client_id = ?`) | Launch | Load all memories into prompt. <50 entries per client. |
| v1.5 | tsvector FTS (exact keyword + stemming) | Any client hits 50 entries | `recall_memory` tool uses `search_memory` RPC. `search_text` tsvector column auto-populates. |
| v2 | Hybrid vector + FTS | Any client hits 100 entries | Add `embedding vector(1536)` column. Embed on every `update_memory` write. `search_memory` RPC combines vector cosine similarity (0.7 weight) + FTS rank (0.3 weight). |

**Schema (designed for v2, works at MVP):**

```sql
-- ai_memory table (v2.3 schema)
ALTER TABLE ai_memory ADD COLUMN embedding vector(1536);  -- nullable, populated when pgvector enabled
ALTER TABLE ai_memory ADD COLUMN search_text tsvector
  GENERATED ALWAYS AS (to_tsvector('english', key || ' ' || value)) STORED;

-- Indexes (create when ready)
CREATE INDEX ON ai_memory USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
CREATE INDEX ON ai_memory USING gin (search_text);
```

**Hybrid search RPC function:**

```sql
CREATE OR REPLACE FUNCTION search_memory(
  p_client_id TEXT, p_query TEXT,
  p_query_embedding vector(1536) DEFAULT NULL, p_limit INTEGER DEFAULT 10
) RETURNS TABLE (key TEXT, value TEXT, similarity FLOAT)
LANGUAGE plpgsql AS $$
BEGIN
  IF p_query_embedding IS NOT NULL THEN
    -- Hybrid: vector cosine + FTS boost
    RETURN QUERY SELECT m.key, m.value,
      (0.7 * (1 - (m.embedding <=> p_query_embedding)) +
       0.3 * ts_rank(m.search_text, plainto_tsquery('english', p_query)))::FLOAT
    FROM ai_memory m WHERE m.client_id = p_client_id AND m.embedding IS NOT NULL
    ORDER BY 3 DESC LIMIT p_limit;
  ELSE
    -- FTS only (MVP/v1.5 mode)
    RETURN QUERY SELECT m.key, m.value,
      ts_rank(m.search_text, plainto_tsquery('english', p_query))::FLOAT
    FROM ai_memory m WHERE m.client_id = p_client_id
      AND m.search_text @@ plainto_tsquery('english', p_query)
    ORDER BY 3 DESC LIMIT p_limit;
  END IF;
END; $$;
```

**Embedding on write (when pgvector enabled):**

```typescript
// Called after every update_memory write
async function embedMemory(memoryId: string, value: string) {
  const { data } = await openai.embeddings.create({
    model: 'text-embedding-3-small', // $0.02/MTok — negligible cost
    input: value,
  });
  await db.updateMemory(memoryId, { embedding: data[0].embedding });
}
```

**Key insight from OpenClaw:** "auth bug" should match "authentication issues." Keyword search breaks with natural language. The pgvector column is nullable from day 1 — zero cost until you populate it.

### System Prompt Construction

The system prompt is assembled from layers, not a monolithic blob. **SOUL.md** (`01_Projects/RE-AI-CRM/SOUL.md`) is the source of truth for Layers 1-2.

```
LAYER 1: Base Personality (~1-2K tokens, from SOUL.md, always loaded)
─────────────────────────────────────────────────────────────────────
Identity, tone, behavior rules, permission awareness.
Defined in SOUL.md — covers: personality traits, Singapore English,
WhatsApp voice, what to always do, what to never do, adaptive tone.
Heartbeat personality (morning briefing, nudge, stale review tone)
also defined in SOUL.md.

LAYER 2a: Domain Knowledge (~2-5K tokens, selectively loaded from Supabase Storage)
───────────────────────────────────────────────────────────────────────────────────
RE-specific knowledge stored as markdown files in Supabase Storage,
indexed in domain_knowledge_index table. Examples: contact types, deal stages,
stamp duty rules (BSD/ABSD/SSD), OTP deadlines, TA terms, viewing prep,
follow-up cadences, lead scoring, HDB regulations, district guides.

Loading per request:
1. always_load=true chunks (~2-3 files: contact classification, deal stages, base RE rules)
2. Keyword-match user message against trigger_keywords → load matched chunks
3. Cap at 5K tokens total. If over budget, rank by keyword hit count.
4. Platform defaults can be overridden per-client (same slug, client_id prefix wins).

See "Domain Knowledge Architecture" section below for full design.

LAYER 2b: Skills Menu (~200-500 tokens, always loaded; full skills loaded on demand)
──────────────────────────────────────────────────────────────────────────────────
Skill files define CAPABILITIES — what the agent can DO, not just what it knows.
Two sources: platform skills (we ship) and user skills (agent creates).
Stored as markdown files in Supabase Storage (bucket: skills),
indexed in skills_index table.

**Lazy-loading pattern (follows OpenClaw + Fintool):**
The system prompt contains a COMPACT MENU only — name + description + slug per skill.
The model decides which skill to use based on the user's message, then reads the
full SKILL.md on demand via the `read_skill` tool.

This is fundamentally different from domain knowledge (Layer 2a) which is PRE-LOADED
into context. Domain knowledge = context the model needs to reason correctly.
Skills = instructions the model follows when executing a workflow. Skills only
need to be loaded when the model decides to act.

What's injected into system prompt:
```
## Available Skills
- **generate-cma** — Generate Comparative Market Analysis report for a property
- **draft-followup** — Draft follow-up message after viewing/meeting/interaction
- **parse-transaction** — Parse OTP/TA/completion documents and extract key terms
- **morning-briefing** — Generate personalized morning briefing summary
- **my-followup-template** [user] — Custom follow-up template for HDB sellers
```

Model reads full skill on demand via `read_skill("generate-cma")` tool call.

See "Skills Filesystem Architecture" section below for full design.

LAYER 3: Client Memory (~1-2K tokens, loaded from ai_memory)
────────────────────────────────────────────────────────────
Agent's self-written notes: preferences, relationships, avoid-list, style.
MVP: full table scan. v1.5: FTS via recall_memory. v2: hybrid vector+FTS.
Loaded fresh every request from Supabase.

LAYER 4: Context (~2-5K tokens, loaded per request)
───────────────────────────────────────────────────
Conversation summaries (compacted prior segments — from conversation_summaries table).
Recent conversation messages (current segment, up to 50 messages).
Today's tasks + overdue items + recurring task reminders.
Detected contact records (if message mentions a name).
Active deal summary.
```

**Total: ~9-18K tokens** — well within any model's context window (Haiku: 200K, Sonnet: 200K). Compaction ensures this stays bounded regardless of conversation length.

**Skills vs Anthropic Skills:** Anthropic Skills = code execution + containers. Our skills are markdown files that define agent capabilities — prompt instructions loaded into context. The Creator path uses actual code execution (via sandbox), but the Reasoner path is pure prompt + tools. Skills are FILES, not code — they live in Supabase Storage and are loaded at prompt-assembly time. See "Skills Filesystem Architecture" below.

### Domain Knowledge Architecture

Domain knowledge chunks are **markdown files in Supabase Storage**, indexed in a **`domain_knowledge_index` Postgres table** for discovery and selective loading. This follows Fintool's pattern (S3 files + `fs_files` SQL index) adapted to our stack.

**Why files instead of content-in-DB:**
- **Human-editable.** Domain knowledge is markdown — edit directly, version in git during development, deploy to Supabase Storage.
- **Versionable.** Supabase Storage supports versioning. See what changed when an extraction starts misfiring.
- **Shadowing-ready.** Same slug at different paths = per-client override. SQL picks the winner.
- **Same pattern as artifacts.** Already using Supabase Storage for `artifacts/{client_id}/`. Domain knowledge uses `knowledge/platform/` and `knowledge/clients/{client_id}/`.

**Storage layout:**

```
Supabase Storage (bucket: knowledge)
├── platform/                              ← platform defaults (always available)
│   ├── contact-classification.md          always_load: true
│   ├── deal-stages.md                     always_load: true
│   ├── follow-up-cadences.md              always_load: true
│   ├── stamp-duty-rules.md                trigger_keywords: ["stamp duty", "BSD", "ABSD", "SSD"]
│   ├── hdb-regulations.md                 trigger_keywords: ["HDB", "BTO", "resale flat"]
│   ├── otp-and-ta.md                      trigger_keywords: ["OTP", "option", "TA", "tenancy"]
│   ├── district-guides/
│   │   ├── district-09-10.md              trigger_keywords: ["District 9", "District 10", "Orchard", "Bukit Timah"]
│   │   └── district-15.md                 trigger_keywords: ["District 15", "East Coast", "Katong"]
│   ├── property-types.md                  trigger_keywords: ["condo", "landed", "HDB", "EC", "penthouse"]
│   ├── viewing-prep.md                    trigger_keywords: ["viewing", "showing", "open house"]
│   └── lead-scoring.md                    trigger_keywords: ["score", "qualify", "hot lead", "cold lead"]
│
└── clients/                               ← per-client overrides (future, not MVP)
    └── {client_id}/
        └── stamp-duty-rules.md            ← wins over platform/stamp-duty-rules.md
```

**Index table:**

```sql
CREATE TABLE domain_knowledge_index (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT NOT NULL,                        -- e.g. "stamp-duty-rules"
  storage_path TEXT NOT NULL,                -- e.g. "knowledge/platform/stamp-duty-rules.md"
  client_id UUID REFERENCES clients(id),     -- NULL = platform default
  tags TEXT[] NOT NULL DEFAULT '{}',         -- e.g. {"financing", "stamp-duty", "buyer"}
  trigger_keywords TEXT[] NOT NULL DEFAULT '{}', -- exact strings to match in user message
  always_load BOOLEAN NOT NULL DEFAULT false,
  token_estimate INTEGER NOT NULL DEFAULT 0, -- rough token count for budget management
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

  UNIQUE (slug, client_id)                   -- one version per slug per client (NULL = platform)
);

-- RLS: platform rows (client_id IS NULL) visible to all; client rows scoped
CREATE POLICY "Platform knowledge visible to all"
  ON domain_knowledge_index FOR SELECT
  USING (client_id IS NULL);
CREATE POLICY "Client knowledge scoped"
  ON domain_knowledge_index FOR SELECT
  USING (client_id = current_setting('app.client_id')::UUID);
```

**Loading logic (runs at start of every agent task):**

```typescript
async function loadDomainKnowledge(clientId: string, userMessage: string): Promise<string> {
  const TOKEN_BUDGET = 5000;

  // 1. Always-load chunks (platform + client overrides)
  const alwaysLoad = await db.query(`
    SELECT DISTINCT ON (slug) slug, storage_path, token_estimate
    FROM domain_knowledge_index
    WHERE always_load = true
      AND (client_id IS NULL OR client_id = $1)
    ORDER BY slug, client_id DESC NULLS LAST  -- client override wins
  `, [clientId]);

  // 2. Keyword-matched chunks
  const messageLower = userMessage.toLowerCase();
  const keywordMatched = await db.query(`
    SELECT DISTINCT ON (slug) slug, storage_path, token_estimate,
      (SELECT COUNT(*) FROM unnest(trigger_keywords) kw
       WHERE $2 ILIKE '%' || kw || '%') AS hit_count
    FROM domain_knowledge_index
    WHERE always_load = false
      AND (client_id IS NULL OR client_id = $1)
      AND EXISTS (
        SELECT 1 FROM unnest(trigger_keywords) kw
        WHERE $2 ILIKE '%' || kw || '%'
      )
    ORDER BY slug, client_id DESC NULLS LAST
  `, [clientId, messageLower]);

  // 3. Budget check — always-load first, then keyword-matched ranked by hits
  const ranked = [
    ...alwaysLoad.rows,
    ...keywordMatched.rows.sort((a, b) => b.hit_count - a.hit_count),
  ];

  let tokensBudget = TOKEN_BUDGET;
  const toLoad: string[] = [];
  for (const row of ranked) {
    if (tokensBudget - row.token_estimate < 0) break;
    toLoad.push(row.storage_path);
    tokensBudget -= row.token_estimate;
  }

  // 4. Fetch file contents from Supabase Storage
  const chunks = await Promise.all(
    toLoad.map(path => supabaseStorage.download('knowledge', path))
  );
  return chunks.map(c => c.text).join('\n\n---\n\n');
}
```

**Scaling path:**

| Phase | Approach | When |
|-------|----------|------|
| MVP | <10 files, keyword matching, always_load covers 80% of queries | Launch |
| Growth | 10-50 files, keyword matching handles the long tail | 10+ clients with diverse needs |
| Scale | Add Haiku tag-classifier for messages with no keyword hits | 50+ knowledge files, keyword matching starts missing |
| Future | Per-client overrides (shadowing). HDB specialist gets different rules than luxury condo agent. | Client segmentation matters |

**Why not embeddings for knowledge retrieval:** Knowledge chunks are static, well-defined domain files — not freeform user-written notes. Keywords are precise, debuggable, and zero-cost. Embeddings make sense for `ai_memory` (freeform, grows unpredictably) but are overkill for 10-50 curated knowledge files where you control the trigger_keywords.

### Skills Filesystem Architecture

Skills are **files** — markdown documents that define what the agent can DO. They live in Supabase Storage (S3-backed), indexed in a `skills_index` Postgres table. The system prompt contains a **compact menu** (name + description per skill). The model **reads the full skill file on demand** via the `read_skill` tool when it decides to execute a workflow. This follows the lazy-loading pattern used by both OpenClaw and Fintool, adapted for B2C (two mount points instead of three — no org/shared layer).

**Why lazy-loading, not keyword pre-loading:**
- Domain knowledge (Layer 2a) is PRE-LOADED because the model needs that context to reason correctly (stamp duty rules, district guides).
- Skills (Layer 2b) are LAZY-LOADED because they're instructions the model follows only when executing a specific workflow. Most skills aren't relevant to any given request.
- At 5-10 skills (MVP), the menu is ~200-500 tokens. At 50+ skills, it's still <2K tokens. The full skill content never enters the prompt unless the model reads it.
- The model self-selects which skill to use based on the user's intent — more accurate than keyword matching ("help me prepare for my viewing" correctly maps to `viewing-prep-guide` without needing exact keyword hits).

**Two mount points:**

| Mount | Path | Permissions | Who creates | Examples |
|---|---|---|---|---|
| **Platform** | `skills/platform/` | Read-only for agent | We ship these | `generate-cma.md`, `draft-followup.md`, `parse-transaction.md`, `morning-briefing.md` |
| **User** | `skills/clients/{client_id}/` | Read-write for agent | Agent creates via `manage_skill` tool, or user teaches | `my-followup-template.md`, `hdb-closing-checklist.md`, `karen-update.md` |

**Why two mount points (not three):**
Fintool has three: private (user), shared (org), public (platform). We drop the shared/org layer because this is B2C — each RE agent is a solo user, not part of an organization. If we ever add team accounts (v2+), we'd add a third mount point (`skills/teams/{team_id}/`).

**Storage layout:**

```
Supabase Storage (bucket: skills)
├── platform/                              ← read-only, we ship these
│   ├── generate-cma.md                    "Generate Comparative Market Analysis report"
│   ├── draft-followup.md                  "Draft follow-up message after interaction"
│   ├── parse-transaction.md               "Parse OTP/TA/completion documents"
│   ├── morning-briefing.md                "Generate personalized morning briefing"
│   ├── viewing-prep-guide.md              "Prepare for property viewing or showing"
│   ├── lead-qualification.md              "Score and qualify a lead"
│   └── property-comparison.md             "Compare properties side by side"
│
└── clients/                               ← read-write, agent creates these
    └── {client_id}/
        ├── my-followup-template.md         "Custom follow-up template for HDB sellers"
        ├── hdb-closing-checklist.md         "7-step HDB closing checklist"
        └── karen-update.md                  "Send daily activity summary to Karen"
```

The descriptions shown above are what appears in the skill menu in the system prompt. The model reads the full file content on demand.

**How skills differ from domain knowledge:**

| | Domain Knowledge (Layer 2a) | Skills (Layer 2b) |
|---|---|---|
| **Purpose** | What the agent KNOWS | What the agent can DO |
| **Examples** | Stamp duty rates, district guides, HDB rules | CMA generation instructions, follow-up templates, closing checklists |
| **Who writes** | We curate (platform only for MVP) | We ship platform defaults + agent creates user skills |
| **Mutability** | Static, updated by us | User skills are dynamic — agent creates/updates them |
| **Loading** | Keyword-matched, pre-loaded into prompt | Menu in prompt, model reads on demand via `read_skill` tool |
| **Storage** | `knowledge/` bucket | `skills/` bucket |
| **Index table** | `domain_knowledge_index` | `skills_index` |

**Index table:**

```sql
CREATE TABLE skills_index (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT NOT NULL,                        -- e.g. "draft-followup"
  storage_path TEXT NOT NULL,                -- e.g. "skills/platform/draft-followup.md"
  client_id UUID REFERENCES clients(id),     -- NULL = platform default
  description TEXT NOT NULL,                 -- shown in skill menu — model uses this to self-select
  tags TEXT[] NOT NULL DEFAULT '{}',         -- e.g. {"messaging", "follow-up"} — for future categorization
  token_estimate INTEGER NOT NULL DEFAULT 0, -- for monitoring context budget when skill is read
  created_by TEXT NOT NULL DEFAULT 'platform', -- 'platform' or 'agent'
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

  UNIQUE (slug, client_id)                   -- one version per slug per client (NULL = platform)
);

-- RLS: platform skills (client_id IS NULL) visible to all; client skills scoped
CREATE POLICY "Platform skills visible to all"
  ON skills_index FOR SELECT
  USING (client_id IS NULL);
CREATE POLICY "Client skills scoped"
  ON skills_index FOR SELECT
  USING (client_id = current_setting('app.client_id')::UUID);
-- Agent can INSERT/UPDATE their own skills
CREATE POLICY "Agent can create client skills"
  ON skills_index FOR INSERT
  WITH CHECK (client_id = current_setting('app.client_id')::UUID);
CREATE POLICY "Agent can update client skills"
  ON skills_index FOR UPDATE
  USING (client_id = current_setting('app.client_id')::UUID);
```

**Shadowing (user overrides platform):**

Same pattern as domain knowledge — `DISTINCT ON (slug) ORDER BY client_id DESC NULLS LAST`. If a user has `skills/clients/{client_id}/draft-followup.md`, it replaces the platform default `skills/platform/draft-followup.md` for that client.

**Skill menu generation (runs at start of every agent task — lightweight, no file reads):**

```typescript
async function getSkillMenu(clientId: string): Promise<string> {
  // Query all available skills for this client (platform + user, with shadowing)
  const skills = await db.query(`
    SELECT DISTINCT ON (slug) slug, description, created_by
    FROM skills_index
    WHERE client_id IS NULL OR client_id = $1
    ORDER BY slug, client_id DESC NULLS LAST  -- client override wins
  `, [clientId]);

  // Format as compact menu for system prompt (~20-50 tokens per skill)
  return skills.rows.map(s =>
    `- **${s.slug}**${s.created_by === 'agent' ? ' [user]' : ''} — ${s.description}`
  ).join('\n');
}

// Injected into system prompt as:
// ## Available Skills
// - **generate-cma** — Generate Comparative Market Analysis report
// - **draft-followup** — Draft follow-up message after interaction
// - **karen-update** [user] — Send daily activity summary to Karen
//
// To use a skill, call read_skill("slug") to load its instructions.
```

**`read_skill` tool (model calls this on demand when it decides to use a skill):**

```typescript
const read_skill = tool({
  description: 'Read a skill file to get detailed instructions. Call this BEFORE executing a skill workflow. Use the slug from the Available Skills menu.',
  inputSchema: z.object({
    slug: z.string().describe('Skill slug from the Available Skills menu, e.g. "generate-cma"'),
  }),
  execute: async ({ slug }) => {
    // Resolve with shadowing (user override > platform default)
    const skill = await db.query(`
      SELECT storage_path FROM skills_index
      WHERE slug = $1 AND (client_id IS NULL OR client_id = $2)
      ORDER BY client_id DESC NULLS LAST
      LIMIT 1
    `, [slug, clientId]);

    if (!skill.rows.length) return { error: `Skill "${slug}" not found` };

    // Fetch full content from Supabase Storage
    const content = await supabaseStorage.download('skills', skill.rows[0].storage_path);
    return { slug, content: content.text };
  },
});
```

**The flow — how the model uses a skill:**

```
System prompt includes:
  "## Available Skills
   - **generate-cma** — Generate Comparative Market Analysis report
   - **draft-followup** — Draft follow-up message after interaction
   ...
   To use a skill, call read_skill("slug") to load its instructions."

User: "Can you prepare a CMA for 42 Noriega?"

Model thinks: "CMA request → I should use the generate-cma skill"

Step 1: Model calls read_skill("generate-cma")
→ Returns full markdown instructions from generate-cma.md

Step 2: Model follows the instructions in the skill file
→ Calls CRM tools (search contacts, get property data)
→ Calls generate_artifact if PDF needed
→ Returns result to user

Total: 1 extra tool call (read_skill). Skill content only in context
when actually needed. No wasted tokens on unused skills.
```

**`manage_skill` tool (agent creates user skills):**

```typescript
const skillTools = {
  manage_skill: tool({
    description: 'Create, update, or delete a user skill file. Use when the user teaches you a new process, template, or workflow they want you to remember and follow.',
    inputSchema: z.object({
      action: z.enum(['create', 'update', 'delete', 'list']),
      slug: z.string().optional().describe('Skill identifier, e.g. "karen-update" (required for create/update/delete)'),
      content: z.string().optional().describe('Markdown content of the skill file (required for create/update)'),
      description: z.string().optional().describe('Short description shown in skill menu — helps model decide when to use this skill'),
    }),
    execute: async ({ action, slug, content, description }) => {
      switch (action) {
        case 'create':
        case 'update': {
          // Upload file to Supabase Storage
          const path = `clients/${clientId}/${slug}.md`;
          await supabaseStorage.upload('skills', path, content, { upsert: true });

          // Upsert index row (description is key — it's what appears in the skill menu)
          await db.query(`
            INSERT INTO skills_index (slug, storage_path, client_id, description, token_estimate, created_by)
            VALUES ($1, $2, $3, $4, $5, 'agent')
            ON CONFLICT (slug, client_id) DO UPDATE SET
              storage_path = EXCLUDED.storage_path,
              description = EXCLUDED.description,
              token_estimate = EXCLUDED.token_estimate,
              updated_at = now()
          `, [slug, path, clientId, description, estimateTokens(content)]);

          return { success: true, action, slug, path };
        }
        case 'delete': {
          await supabaseStorage.remove('skills', [`clients/${clientId}/${slug}.md`]);
          await db.query(`DELETE FROM skills_index WHERE slug = $1 AND client_id = $2`, [slug, clientId]);
          return { success: true, action, slug };
        }
        case 'list': {
          const skills = await db.query(`
            SELECT slug, description, trigger_keywords, created_by
            FROM skills_index
            WHERE client_id IS NULL OR client_id = $1
            ORDER BY created_by, slug
          `, [clientId]);
          return skills.rows;
        }
      }
    },
  }),
}
```

**How "user teaches agent a skill" works end-to-end:**

```
User: "Whenever I say 'send Karen update', email karen@era.sg
       a summary of today's activity"

Agent thinks: This is a reusable workflow. I should save it as a skill.

Agent calls: manage_skill({
  action: "create",
  slug: "karen-update",
  content: "# Karen Update\n\nTrigger: user says 'send Karen update'\n\n## Instructions\n1. Summarize today's activity...\n2. Draft email to karen@era.sg...\n3. Send preview for approval (Tier 3)...",
  description: "Send daily activity summary to Karen at ERA"
})

→ File created: skills/clients/{client_id}/karen-update.md
→ Index row created in skills_index (description shows in skill menu)

Next time user says "send Karen update":
→ Skill menu in system prompt includes: "karen-update [user] — Send daily activity summary to Karen"
→ Model recognizes intent, calls read_skill("karen-update")
→ Gets full instructions, follows them
```

**What goes in a skill file (anatomy):**

```markdown
# Draft Follow-Up Message

## When to use
After a viewing, meeting, or any significant client interaction
where a follow-up would be appropriate.

## Instructions
1. Check interaction history for the contact (last 7 days)
2. Identify the key discussion points from the most recent interaction
3. Draft a warm, concise follow-up message
4. Include any action items or next steps discussed
5. Match the agent's communication style (see memory → style)
6. Present as Tier 3 draft for approval

## Template
Hi {contact_name},

Great {meeting_type} today. Just wanted to follow up on {key_topic}.

{action_items_if_any}

Let me know if you have any questions.

{agent_sign_off}

## Notes
- Keep under 100 words
- Don't use emojis unless agent's style includes them
- If property was discussed, include the address
```

**Scaling path:**

| Phase | Platform skills | User skills | Total |
|-------|----------------|-------------|-------|
| MVP | 5-10 (core workflows) | 0 (agent hasn't learned yet) | 5-10 |
| Month 1 | 5-10 | 2-5 per active client | 10-15 per client |
| Growth | 15-25 (expanded capabilities) | 5-15 per client | 20-40 per client |
| Scale | 25-50 | 10-30 per client | 35-80 per client |

At 80 skill files, the menu is ~1.5K tokens (80 x ~20 tokens per line). The model only reads the 1-2 skills it actually needs per request. Total skill token cost per request: ~200 tokens (menu) + ~500-1000 tokens (one read skill) = well under 2K. Compare: keyword pre-loading would inject ~3-5K tokens of skill content per request regardless of whether it's used.

### Document System (Inbound Extraction)

The document system handles **inbound** documents — files the agent forwards to the AI via WhatsApp (or uploads via dashboard). It classifies, splits, and extracts structured data from documents, linked to CRM contacts and deals. This is the inverse of the Creator path (which generates outbound artifacts).

**Core capability reused from Sunder:** The existing Sunder product already has a battle-tested pipeline: upload → Gemini 2.5 Flash classification → PDF splitting → ExtendAI structured extraction → per-field confidence + citations → validation. We reuse this pipeline wholesale, changing only the input method (WhatsApp-first instead of browser upload) and the tag configuration (RE-specific instead of generic).

**The self-serve idea:** Users can define their own extraction schemas conversationally. "I want to extract data from property brochures — price, floor area, unit mix, TOP date." The AI creates a custom extraction tag, saves it as a per-client config, and from then on any similar document gets auto-classified and extracted.

#### Two Types of Extraction Tags

```
PLATFORM TAGS (we ship, RE-specific defaults)
──────────────────────────────────────────────
We define and maintain these. Available to all clients.

  floor_plan       → { unit_number, sqft, bedrooms, bathrooms, facing, floor_level }
  otp              → { property, price, option_fee, exercise_deadline, conditions[] }
  tenancy_agreement→ { tenant, landlord, property, monthly_rent, start_date, end_date, deposit }
  valuation_report → { property, market_value, forced_sale_value, valuer, date }
  commission_note  → { property, transaction_value, rate, gross_commission, co_broke_split }
  property_brochure→ { development_name, developer, address, unit_mix[], pricing_range, TOP_date }
  receipt          → { vendor, amount, date, category, description }
  other            → { description } (catch-all, no structured extraction)

USER TAGS (agent creates via conversation, per-client)
──────────────────────────────────────────────────────
User teaches the AI what they want extracted from a document type
they encounter regularly. Saved as a per-client extraction schema.

  Examples:
  - Insurance agent's "motor_claim" → { claimant, vehicle_no, accident_date, repair_cost, workshop }
  - Wealth advisor's "portfolio_statement" → { client, NAV, asset_allocation, ytd_return, date }
  - HDB specialist's "hdb_resale_checklist" → { buyer, seller, flat_type, town, resale_price, COV }
```

#### Self-Serve Schema Builder (Conversational)

The self-serve flow replaces the 8-phase developer-driven onboarding from the existing Sunder product. Instead of Claude Code skills + ExtendAI dashboard + manual config, the user defines schemas via WhatsApp conversation.

```
User: "I get a lot of renovation quotations from contractors.
       Can you start extracting data from those?"

Agent: "Sure. What fields do you care about from renovation quotations?"

User: "Contractor name, total cost, itemized breakdown, start date,
       completion date, and warranty period"

Agent: "Got it. I'll create an extraction schema for renovation quotations:

       📄 renovation_quotation
       • contractor_name (text)
       • total_cost (currency)
       • line_items (array: description, quantity, unit_price, subtotal)
       • start_date (date)
       • completion_date (date)
       • warranty_period (text)

       Want to test it? Forward me a sample quotation."

User: [forwards PDF]

Agent: "Here's what I extracted:

       Contractor: HomeStyle Pte Ltd
       Total: $42,800
       Items:
         - Kitchen cabinets: $12,500
         - Flooring (marble): $18,000
         - Painting (3 rooms): $4,800
         - Plumbing: $7,500
       Start: March 15, 2026
       Completion: May 30, 2026
       Warranty: 1 year defects liability

       Looks right? I can adjust the schema if anything's off."

User: "Add a field for payment terms"

Agent: "Added payment_terms (text). Schema updated.
       From now on, any renovation quotation you forward
       will be auto-extracted with these fields."
```

**What happens behind the scenes:**

```
1. User describes document type + desired fields
   → Agent calls `create_extraction_schema` tool

2. Tool creates:
   a. Row in extraction_schemas table (schema definition, per-client)
   b. ExtendAI processor via API (if extraction enabled)
      OR Gemini structured output schema (for simpler extraction)
   c. Classification hint for Gemini (how to recognize this doc type)

3. User sends sample document
   → Same Gemini pipeline: classify → split → extract
   → But now the user's custom tag is in the tag pool
   → ExtendAI (or Gemini structured output) extracts per schema
   → Results shown to user for validation

4. User confirms or adjusts
   → Schema updated, extraction re-run if needed
   → Schema saved permanently for this client

5. Future documents of this type
   → Auto-classified by Gemini (classification hint matches)
   → Auto-extracted with user's schema
   → Linked to contact/deal if identifiable
   → Searchable via search_documents tool
```

#### Extraction Pipeline (reused from Sunder)

```
Document arrives (WhatsApp forward or dashboard upload)
      │
      ▼
Store in Supabase Storage
  documents/{client_id}/{doc_id}.{ext}
      │
      ▼
Trigger.dev task: "document-processing"
(per-client queue, same concurrencyKey pattern)
      │
      ▼
1. Upload to Google Files API (temporary)
      │
      ▼
2. Gemini 2.5 Flash: classify + split
   Tag pool = platform tags + client's custom tags
   Each tag has a classificationHint (2-3 sentences)
   Returns: { splits: [{ type, startPage, endPage, identifier, date }] }
      │
      ▼
3. For each split:
   a. If PDF: extract page range as child PDF
   b. Route to ExtendAI processor (if tag has processorId)
      OR Gemini structured output (for simpler schemas)
   c. Validate extraction (per-field confidence, business rules)
   d. Store results in document_extractions table
      │
      ▼
4. Auto-link to CRM:
   - Scan extracted data for contact names → fuzzy match against contacts table
   - Scan for property addresses → match against active deals
   - Set document.contact_id and document.deal_id if confident match
      │
      ▼
5. Confirm via WhatsApp:
   "Filed the OTP for 42 Noriega under Sarah Chen's deal.
    Exercise deadline: Feb 28. Option fee: $5K (1%).
    Want me to create a task for the deadline?"
      │
      ▼
6. Cleanup: delete from Google Files API
```

**Model routing for extraction:**

| Extraction type | Model | Why |
|---|---|---|
| Simple schemas (<10 fields, no tables) | Gemini 2.5 Flash structured output | Cheap, fast, one API call |
| Complex schemas (tables, nested data, citations needed) | ExtendAI processor | Purpose-built for document extraction, per-field confidence, bounding boxes |
| Classification only (unknown doc, no extraction) | Gemini 2.5 Flash | Just classify + describe, no field extraction |

**Why two extraction backends (Gemini vs ExtendAI):**
- **Gemini structured output** is free for simple extraction (already paying for classification). Good enough for 5-10 flat fields. No citations or confidence scores.
- **ExtendAI** is purpose-built: per-field OCR confidence, bounding box citations, handles messy scans and tables. Worth the cost for complex documents (contracts, invoices, financial statements).
- User's custom schemas start with Gemini. If they need higher accuracy or citation support, upgrade to ExtendAI processor (created via API).

#### Storage Model

```
Supabase Storage (bucket: documents)
└── {client_id}/
    ├── {doc_id}.pdf                    ← original file
    ├── {doc_id}_split_0.pdf            ← child PDFs (if multi-split)
    ├── {doc_id}_split_1.pdf
    └── ...

Supabase Postgres:
  documents table          → file metadata + classification
  document_extractions     → per-split extracted data + confidence
  extraction_schemas       → per-client custom tag definitions
```

**This is the Fintool metadata pattern.** Every document has:
- **Classification** (primary_tag, tags) → what type of document
- **Structured data** (extracted_data JSONB) → normalized fields
- **CRM linkage** (contact_id, deal_id) → who/what it belongs to
- **Searchability** (description, extracted_data) → AI can find it

"Find the floor plan for Parc Clematis" becomes a SQL query with filters, not keyword search over a haystack.

#### New Tables

```sql
-- Inbound documents (files the user sends to the AI)
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  contact_id UUID REFERENCES contacts(id),      -- auto-linked or manually set
  deal_id UUID REFERENCES deals(id),             -- auto-linked or manually set
  storage_path TEXT NOT NULL,                    -- path in Supabase Storage
  original_filename TEXT NOT NULL,
  file_type TEXT NOT NULL,                       -- pdf, jpg, png, etc.
  file_size INTEGER,
  file_hash TEXT,                                -- SHA256 for deduplication
  status TEXT NOT NULL DEFAULT 'uploaded',       -- uploaded, processing, complete, failed
  -- Gemini classification output
  primary_tag TEXT,                              -- most frequent tag from splits
  tags JSONB DEFAULT '{}',                       -- { "floor_plan": 2, "receipt": 1 }
  description TEXT,                              -- Gemini summary
  is_heterogeneous BOOLEAN DEFAULT false,        -- multiple doc types in one file?
  document_date DATE,                            -- extracted date from content
  -- Processing metadata
  processing_error TEXT,
  processed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Per-split extraction results
CREATE TABLE document_extractions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
  split_index INTEGER NOT NULL DEFAULT 0,
  start_page INTEGER,                            -- 1-indexed
  end_page INTEGER,                              -- 1-indexed, inclusive
  tag_id TEXT NOT NULL,                          -- extraction schema slug
  identifier TEXT,                               -- invoice #, unit #, policy #
  document_date DATE,
  -- Extraction output
  extracted_data JSONB DEFAULT '{}',             -- the structured fields
  original_extracted_data JSONB DEFAULT '{}',    -- immutable backup for audit
  extraction_metadata JSONB DEFAULT '{}',        -- per-field confidence, citations, insights
  extraction_status TEXT DEFAULT 'pending',      -- pending, processing, complete, needs_review, failed
  extraction_error TEXT,
  -- Validation
  validation_failures JSONB,                     -- array of { ruleId, message, field }
  low_confidence_fields JSONB,                   -- fields with OCR confidence < 0.85
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- User-defined extraction schemas (custom document types)
CREATE TABLE extraction_schemas (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  slug TEXT NOT NULL,                            -- e.g. "renovation_quotation"
  display_name TEXT NOT NULL,                    -- "Renovation Quotation"
  classification_hint TEXT NOT NULL,             -- 2-3 sentences for Gemini classification
  fields JSONB NOT NULL,                         -- array of { name, type, description, required }
  extraction_backend TEXT DEFAULT 'gemini',      -- 'gemini' (structured output) or 'extend' (ExtendAI)
  extend_processor_id TEXT,                      -- ExtendAI processor ID (if backend = 'extend')
  validate_rules JSONB DEFAULT '[]',            -- array of business rules
  sample_count INTEGER DEFAULT 0,               -- how many docs tested against this schema
  status TEXT DEFAULT 'draft',                   -- draft, active, archived
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),

  UNIQUE (client_id, slug)
);

-- RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_extractions ENABLE ROW LEVEL SECURITY;
ALTER TABLE extraction_schemas ENABLE ROW LEVEL SECURITY;

CREATE POLICY "client_isolation" ON documents FOR ALL
  USING (client_id = current_setting('app.client_id')::TEXT);
CREATE POLICY "client_isolation" ON document_extractions FOR ALL
  USING (document_id IN (SELECT id FROM documents WHERE client_id = current_setting('app.client_id')::TEXT));
CREATE POLICY "client_isolation" ON extraction_schemas FOR ALL
  USING (client_id = current_setting('app.client_id')::TEXT);
```

#### New Tools

```typescript
// Document processing (called automatically when user forwards a file)
const documentTools = {
  process_document: tool({
    description: 'Process an uploaded document — classify, split, extract structured data. Called automatically when user forwards a file via WhatsApp.',
    inputSchema: z.object({
      documentId: z.string(),
      forceTag: z.string().optional().describe('Skip classification, use this tag directly'),
    }),
    execute: async ({ documentId, forceTag }) => {
      // Triggers "document-processing" Trigger.dev task
      // Returns: { splits, extractedFields, suggestedLinks }
    },
  }),

  search_documents: tool({
    description: 'Find documents by type, contact, deal, date, or content. Returns metadata + download URLs.',
    inputSchema: z.object({
      query: z.string().optional(),
      tag: z.string().optional(),
      contactId: z.string().optional(),
      dealId: z.string().optional(),
      dateFrom: z.string().optional(),
      dateTo: z.string().optional(),
    }),
    execute: async (filters) => {
      // Query documents + document_extractions with filters
      // Return: filename, tag, description, key extracted fields, storage URL
    },
  }),

  create_extraction_schema: tool({
    description: 'Create a custom extraction schema for a new document type. Use when the user describes a recurring document they want to extract data from.',
    inputSchema: z.object({
      slug: z.string().describe('Unique identifier, e.g. "renovation_quotation"'),
      displayName: z.string(),
      classificationHint: z.string().describe('2-3 sentences describing how to identify this document type'),
      fields: z.array(z.object({
        name: z.string(),
        type: z.enum(['text', 'number', 'currency', 'date', 'boolean', 'array', 'object']),
        description: z.string(),
        required: z.boolean().default(true),
      })),
    }),
    execute: async (input) => {
      // Insert into extraction_schemas (status: 'draft')
      // Generate Gemini JSON schema from field definitions
      // Return: { schemaId, slug, status: 'draft', message: 'Send a sample to test' }
    },
  }),

  update_extraction_schema: tool({
    description: 'Update an existing custom extraction schema — add/remove fields, change types, update classification hint.',
    inputSchema: z.object({
      slug: z.string(),
      fields: z.array(z.object({
        name: z.string(),
        type: z.string(),
        description: z.string(),
        required: z.boolean().default(true),
      })).optional(),
      classificationHint: z.string().optional(),
      status: z.enum(['draft', 'active', 'archived']).optional(),
    }),
    execute: async (input) => {
      // Update extraction_schemas row
    },
  }),

  list_extraction_schemas: tool({
    description: 'List all extraction schemas (platform defaults + user custom) available for this client.',
    inputSchema: z.object({}),
    execute: async () => {
      // Return platform tags + client's custom schemas
    },
  }),
}
```

#### Scaling Path

| Phase | Platform tags | User custom schemas | Extraction backend |
|---|---|---|---|
| MVP | 8 RE-specific tags (floor_plan, otp, ta, valuation, commission, brochure, receipt, other) | 0 (users haven't defined any yet) | Gemini structured output only (free, simple) |
| Month 1-3 | Same 8 | 1-3 per active client | Gemini for simple, ExtendAI for complex |
| Growth | 15-20 (add insurance, wealth management verticals) | 5-10 per client | ExtendAI for all tags with >50 docs processed |
| Scale | 30+ (multi-vertical) | Unlimited | Per-tag routing based on accuracy metrics |

**Cost:** Gemini structured output extraction is essentially free (already paying for classification call). ExtendAI adds ~$0.10-0.50 per document depending on complexity. At 50 documents/month per client, ~$5-25/mo in extraction costs — well within the $149/mo subscription.

### Sandbox (Creator Path)

The sandbox is a TOOL, not an environment. The model doesn't live in the sandbox. It calls `generate_artifact` when it needs to create something, which spins up an ephemeral sandbox.

**When it fires:**

| Feature | Needs sandbox? | Why |
|---|---|---|
| CRM queries ("what deals do I have?") | No | Structured tools → Supabase |
| Contact management | No | Structured tools → Supabase |
| Follow-up nudges | No | Template text |
| PDF property report | **Yes** | Code execution (reportlab) |
| Market comparison chart | **Yes** | Code execution (matplotlib) |
| Property video/animation | **Yes** | Code execution (Remotion) |
| Excel export | **Yes** | Code execution (xlsx) |
| Deal pipeline visualization | **Yes** | Code execution (charting lib) |

**Sandbox tech:** Vercel Sandbox. Decision resolved: Vercel Sandbox for artifact generation (ephemeral code execution). Firecracker microVMs (<125ms boot, <5MB overhead). Pre-installed dependencies: Python + Node.js + Remotion + matplotlib + reportlab + openpyxl.

**File return flow:**

```
Sandbox produces file
→ Upload to Supabase Storage (bucket: artifacts/{client_id}/)
→ Create row in artifacts table (type, url, created_at)
→ Return URL as tool result to model
→ Model sends link to user: "Here's your property comparison: [link]"
```

### Browser Research (Browserbase)

Browserbase provides cloud browser infrastructure for per-user authenticated browser sessions. Used for property research on listing sites that require login (99.co, PropertyGuru, SRX).

**Core components:**

| Component | What | Why |
|---|---|---|
| **Contexts API** | Persists cookies, localStorage, and session data per user across browser sessions | User logs in once → cookies reused for all future research. No re-auth every time. |
| **Live View** | Embeddable iframe showing the live browser session | User can authenticate (enter credentials, solve CAPTCHAs) without sharing passwords with us. |
| **Stagehand** | AI-driven browser automation framework (by Browserbase) | Uses CDP accessibility tree (~100x smaller than screenshots). Natural-language instructions for navigation. |
| **Trigger.dev integration** | Native SDK support within Trigger.dev tasks | Browser research runs as a durable subtask with checkpointing, retries, and per-client queue. |

**Per-user auth flow (first time):**

```
User asks: "Search 99.co for 3-bedroom condos in District 10"
→ Agent calls browse_property_site tool
→ No Browserbase Context exists for this client_id
→ Create new Context + start session with Live View enabled
→ Send Live View link to user via WhatsApp:
  "I need you to log into 99.co so I can search for you.
  Tap this link and sign in — I'll wait: [Live View URL]"
→ Trigger.dev waitpoint pauses (zero compute cost)
→ User opens link, sees live browser, logs into 99.co
→ User confirms login complete via WhatsApp ("done" / "logged in")
→ Waitpoint completes → task resumes
→ Context now has authenticated cookies → saved for future sessions
```

**Subsequent requests (cookies persisted):**

```
User asks: "Check my saved listings on PropertyGuru"
→ Agent calls browse_property_site tool
→ Browserbase Context exists for this client_id → load it
→ Connect to session with persisted cookies → already authenticated
→ Stagehand navigates to saved listings, extracts data
→ Returns structured JSON: { listings: [...], source: "propertyguru", timestamp }
→ No user interaction needed — cookies still valid
```

**Why not run browsers in Vercel Sandbox:**
- **No cookie persistence.** Vercel Sandbox is ephemeral — cookies lost on shutdown. Users would need to re-authenticate every time.
- **No user auth mechanism.** No way for users to interactively log in to property portals. Live View solves this.
- **No anti-detection.** Property portals block headless Chrome. Browserbase includes residential proxies and stealth browser fingerprinting.
- **Different purpose.** Vercel Sandbox is for code execution (generate files). Browserbase is for web interaction (navigate sites, extract data).

**Implementation pattern (Trigger.dev subtask):**

```typescript
import { task } from "@trigger.dev/sdk/v3";
import { Browserbase } from "@browserbasehq/sdk";
import { Stagehand } from "@browserbasehq/stagehand";

export const browserResearch = task({
  id: "browser-research",
  retry: { maxAttempts: 2 },
  run: async (payload: { clientId: string; site: string; action: string; query?: string }) => {
    const bb = new Browserbase({ apiKey: process.env.BROWSERBASE_API_KEY });

    // Load or create context for this client
    let context = await db.getBrowserbaseContext(payload.clientId, payload.site);
    if (!context) {
      // First time — create context + prompt user to authenticate
      const newContext = await bb.contexts.create({ projectId: process.env.BB_PROJECT_ID });
      await db.saveBrowserbaseContext(payload.clientId, payload.site, newContext.id);

      // Start session with Live View for user auth
      const session = await bb.sessions.create({
        projectId: process.env.BB_PROJECT_ID,
        browserSettings: { context: { id: newContext.id, persist: true } },
      });

      // Send Live View link to user, wait for confirmation
      const liveViewUrl = session.liveUrls.find(u => u.type === 'embedded')?.url;
      await gateway.sendToUser(payload.clientId,
        `I need you to log into ${payload.site}. Tap this link and sign in:\n${liveViewUrl}`
      );

      // Waitpoint — pause until user confirms login
      const token = await wait.createToken({
        idempotencyKey: `browser-auth-${payload.clientId}-${payload.site}`,
        timeout: "10m",
      });
      const confirmation = await wait.forToken(token);
      if (!confirmation.ok) return { error: 'User did not complete authentication' };

      context = newContext;
    }

    // Connect with persisted context
    const session = await bb.sessions.create({
      projectId: process.env.BB_PROJECT_ID,
      browserSettings: { context: { id: context.id, persist: true } },
    });

    const stagehand = new Stagehand({
      browserbaseSessionID: session.id,
      env: "BROWSERBASE",
    });
    await stagehand.init();

    // Execute site-specific research
    const results = await executeResearch(stagehand, payload);

    await stagehand.close();
    return results;
  },
});
```

### Territory Scraper (Nightly Lead Prospecting)

Automated nightly scraper that replaces ~40 hours/week of manual lead prospecting per client. Scrapes real estate listings across a client's territories, extracts lead-qualifying signals, enriches agent profiles, scores leads, and syncs to CRM — all before the client opens their laptop.

**What it demolishes:** Manual Zillow/Realtor.com browsing, copy-pasting agent names into LinkedIn, searching for emails/phone numbers, scoring leads in spreadsheets. All replaced by a 90-minute nightly cron job.

**Architecture:**

| Component | What | Why |
|---|---|---|
| **Browserbase parallel sessions** | 25 concurrent headless browsers scraping listing pages | 314 ZIP codes × ~40 listings each = 12,105 listings. Browserbase handles anti-detection (residential proxies, stealth fingerprinting). Sequential would take 20+ hours; 25 parallel = 90 min. |
| **Signal extraction** | Parse listing data for lead-qualifying signals (configurable per client) | Not all agents are leads. Client-specific signals indicate which agents have problems our client's product solves. Signals stored as scored JSON. |
| **Perplexity API enrichment** | Bulk enrich unique agent profiles with phone, email, brokerage | 12K listings → ~4,446 unique agents after dedup. Perplexity is cheaper than clearbit/apollo for individual lookups. Batch with concurrency control (rate limits). |
| **Lead scoring** | Score each enriched agent based on signal density + recency | Higher signal count + more recent listings = hotter lead. Score stored in `enriched_agents` table. |
| **CRM sync** | Upsert scored leads into client's CRM pipeline | Morning briefing pulls top-scored new leads. Agent wakes up to prioritized, enrichable prospects. |

**Data flow:**

```
2:00 AM — Trigger.dev cron fires
│
├─ Fan out: 1 task per client with active territory config
│
│  Per client:
│  ├─ Load territory config (ZIP codes, target listing sites, signal definitions)
│  ├─ Phase 1: SCRAPE — 25 parallel Browserbase sessions
│  │  ├─ Each session: load listing page for ZIP batch → extract listing cards
│  │  ├─ ~1,429 browser sessions total (314 ZIPs ÷ ~5 ZIPs per session batch)
│  │  └─ Raw listings → scraped_listings table (dedup by listing_id)
│  │
│  ├─ Phase 2: EXTRACT — Parse lead signals from raw listings
│  │  ├─ Apply client-specific signal rules (configurable JSON)
│  │  ├─ Deduplicate agents across listings (same agent, multiple listings)
│  │  └─ ~4,446 unique agent profiles from 12,105 listings
│  │
│  ├─ Phase 3: ENRICH — Perplexity API for contact info
│  │  ├─ Batch requests with concurrency limit (avoid rate limits)
│  │  ├─ Extract: phone, email, brokerage, social profiles
│  │  └─ enriched_agents table (upsert — don't re-enrich known agents)
│  │
│  └─ Phase 4: SCORE + SYNC
│     ├─ Score based on signal density × recency × enrichment completeness
│     ├─ Upsert to CRM (contacts table, tagged as "scraped-lead")
│     └─ Flag top 20 new leads for morning briefing inclusion
│
8:00 AM — Morning briefing includes: "🔥 12 new high-priority leads found overnight"
```

**New tables:**

```sql
-- Territory configuration per client
CREATE TABLE scrape_territories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID REFERENCES clients(id),
  name TEXT NOT NULL,  -- e.g., "Bay Area", "Miami-Dade"
  zip_codes TEXT[] NOT NULL,  -- e.g., '{94102,94103,94104,...}'
  target_sites TEXT[] DEFAULT '{realtor.com}',  -- expandable
  signal_rules JSONB NOT NULL,  -- client-specific lead signals
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Raw scraped listings (deduped by listing_id per site)
CREATE TABLE scraped_listings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID REFERENCES clients(id),
  territory_id UUID REFERENCES scrape_territories(id),
  listing_id TEXT NOT NULL,  -- external ID from listing site
  site TEXT NOT NULL,  -- 'realtor.com', 'zillow.com', etc.
  zip_code TEXT NOT NULL,
  agent_name TEXT,
  agent_info JSONB,  -- raw agent data from listing
  listing_data JSONB,  -- price, address, property type, etc.
  signals JSONB,  -- extracted lead-qualifying signals
  signal_score FLOAT,  -- computed signal density score
  scraped_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(client_id, site, listing_id)  -- dedup key
);

-- Enriched unique agent profiles
CREATE TABLE enriched_agents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID REFERENCES clients(id),
  agent_name TEXT NOT NULL,
  agent_key TEXT NOT NULL,  -- normalized name for dedup
  phone TEXT,
  email TEXT,
  brokerage TEXT,
  social_profiles JSONB,
  listing_count INT DEFAULT 1,  -- how many listings this agent has
  avg_signal_score FLOAT,  -- average across their listings
  lead_score FLOAT,  -- final computed score
  enrichment_source TEXT DEFAULT 'perplexity',
  enriched_at TIMESTAMPTZ,
  synced_to_crm BOOLEAN DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(client_id, agent_key)  -- one profile per agent per client
);
```

**Trigger.dev implementation:**

```typescript
import { schedules, task } from "@trigger.dev/sdk/v3";
import { Browserbase } from "@browserbasehq/sdk";
import { Stagehand } from "@browserbasehq/stagehand";

// Parent: fires nightly, fans out to per-client territory scrapes
export const territoryScrapeSchedule = schedules.task({
  id: "territory-scrape-schedule",
  cron: { pattern: "0 18 * * *", timezone: "UTC" },  // 2am SGT
  run: async () => {
    const clients = await db.getClientsWithActiveTerritories();
    await territoryScrape.batchTrigger(
      clients.map(c => ({
        payload: { clientId: c.id },
        options: {
          queue: { name: "territory-scraper", concurrencyLimit: 3 },
          concurrencyKey: c.id,
          tags: [`client-${c.id}`, "territory-scrape"],
        },
      }))
    );
  },
});

// Child: scrapes one client's territories end-to-end
export const territoryScrape = task({
  id: "territory-scrape",
  retry: { maxAttempts: 2 },
  machine: { preset: "medium-2x" },  // needs memory for 25 parallel sessions
  run: async (payload: { clientId: string }) => {
    const territories = await db.getActiveTerritories(payload.clientId);
    const allZips = territories.flatMap(t => t.zip_codes);
    const signalRules = territories[0].signal_rules;  // client-level rules

    // ── PHASE 1: SCRAPE (25 parallel Browserbase sessions) ──
    const bb = new Browserbase({ apiKey: process.env.BROWSERBASE_API_KEY });
    const zipBatches = chunkArray(allZips, Math.ceil(allZips.length / 25));

    const scrapeResults = await Promise.allSettled(
      zipBatches.map(async (zipBatch) => {
        const session = await bb.sessions.create({
          projectId: process.env.BB_PROJECT_ID,
          browserSettings: {
            fingerprint: { devices: ["desktop"], locales: ["en-US"] },
          },
        });
        const stagehand = new Stagehand({
          browserbaseSessionID: session.id,
          env: "BROWSERBASE",
        });
        await stagehand.init();

        const listings = [];
        for (const zip of zipBatch) {
          const pageListings = await scrapeListingsForZip(stagehand, zip);
          listings.push(...pageListings);
        }

        await stagehand.close();
        return listings;
      })
    );

    const rawListings = scrapeResults
      .filter(r => r.status === "fulfilled")
      .flatMap(r => r.value);

    // Bulk upsert to scraped_listings (dedup by listing_id)
    await db.upsertScrapedListings(payload.clientId, rawListings);

    // ── PHASE 2: EXTRACT SIGNALS ──
    const scoredListings = rawListings.map(listing => ({
      ...listing,
      signals: extractSignals(listing, signalRules),
      signal_score: computeSignalScore(listing, signalRules),
    }));
    await db.updateListingSignals(payload.clientId, scoredListings);

    // ── PHASE 3: ENRICH UNIQUE AGENTS ──
    const uniqueAgents = deduplicateAgents(scoredListings);
    const existingAgents = await db.getEnrichedAgents(payload.clientId);
    const newAgents = uniqueAgents.filter(
      a => !existingAgents.find(e => e.agent_key === a.agent_key)
    );

    // Enrich new agents via Perplexity (concurrency-controlled)
    const enriched = await enrichAgentsBatch(newAgents, {
      concurrencyLimit: 10,  // Perplexity rate limit
      source: "perplexity",
    });
    await db.upsertEnrichedAgents(payload.clientId, enriched);

    // ── PHASE 4: SCORE + SYNC ──
    const allAgents = await db.getEnrichedAgents(payload.clientId);
    const scored = allAgents.map(a => ({
      ...a,
      lead_score: computeLeadScore(a),  // signal_density × recency × enrichment
    }));
    await db.updateLeadScores(payload.clientId, scored);

    // Sync top leads to CRM contacts table
    const topLeads = scored
      .filter(a => a.lead_score > 0.6 && !a.synced_to_crm)
      .sort((a, b) => b.lead_score - a.lead_score)
      .slice(0, 50);  // cap per run
    await db.syncLeadsToCRM(payload.clientId, topLeads);

    // Flag for morning briefing
    await db.flagForBriefing(payload.clientId, {
      newLeadsCount: topLeads.length,
      totalScraped: rawListings.length,
      totalEnriched: enriched.length,
    });

    return {
      listings: rawListings.length,
      uniqueAgents: uniqueAgents.length,
      newEnriched: enriched.length,
      topLeads: topLeads.length,
    };
  },
});

// Helper: scrape listings for a single ZIP code
async function scrapeListingsForZip(stagehand: Stagehand, zip: string) {
  await stagehand.page.goto(
    `https://www.realtor.com/realestateandhomes-search/${zip}`,
    { waitUntil: "networkidle" }
  );

  return await stagehand.extract({
    instruction: "Extract all property listing cards with agent name, price, address, property details, and days on market",
    schema: z.object({
      listings: z.array(z.object({
        listing_id: z.string(),
        agent_name: z.string().optional(),
        price: z.number().optional(),
        address: z.string(),
        property_type: z.string().optional(),
        beds: z.number().optional(),
        baths: z.number().optional(),
        sqft: z.number().optional(),
        days_on_market: z.number().optional(),
      })),
    }),
  });
}

// Helper: enrich agents via Perplexity API
async function enrichAgentsBatch(
  agents: UniqueAgent[],
  opts: { concurrencyLimit: number; source: string }
) {
  const queue = new PQueue({ concurrency: opts.concurrencyLimit });
  return Promise.all(
    agents.map(agent =>
      queue.add(async () => {
        const response = await fetch("https://api.perplexity.ai/chat/completions", {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${process.env.PERPLEXITY_API_KEY}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            model: "llama-3.1-sonar-small-128k-online",
            messages: [{
              role: "user",
              content: `Find contact info for real estate agent "${agent.agent_name}" — phone number, email address, brokerage name, and any social media profiles. Return as JSON.`,
            }],
          }),
        });
        const data = await response.json();
        return { ...agent, ...parseEnrichmentResponse(data) };
      })
    )
  );
}
```

**Cost per nightly run:**

| Component | Usage | Cost |
|---|---|---|
| Browserbase | 25 parallel sessions × ~3.5 min avg = ~87 browser-minutes | ~$0.87 (at $0.01/min) |
| Perplexity API | ~500 new agents/day (incremental) | ~$0.50 (sonar-small) |
| Supabase writes | ~12K listing upserts + ~500 agent upserts | Negligible |
| **Total per client per night** | | **~$1.37** |
| **Monthly per client** | 30 nights | **~$41/mo** |

Worth it: replaces 40 hrs/week of manual prospecting ($2,000+/mo at min wage). Clients wake up to scored, prioritized leads ready for outreach.

**Morning briefing integration:**

The `clientBriefing` task (see Cron section) checks `flagForBriefing` data and includes scraper results:

```
"Good morning! 🏠 Overnight scrape found 12 new high-priority leads:

Top 3:
1. Sarah Chen (RE/MAX) — 8 active listings in your territory, strong signals
2. Mike Rodriguez (Keller Williams) — 5 listings, all match your target profile
3. Jennifer Park (Compass) — 3 new listings this week, high signal density

Full list synced to your pipeline. Want me to draft outreach for the top 5?"
```

**Configurable signal rules (per client):**

```jsonc
// Example: client sells transaction coordination services
{
  "signals": [
    { "field": "days_on_market", "condition": "gt", "value": 30, "weight": 2.0, "reason": "stale listing = overwhelmed agent" },
    { "field": "listing_count", "condition": "gt", "value": 5, "weight": 1.5, "reason": "high volume = needs help" },
    { "field": "price", "condition": "between", "value": [300000, 800000], "weight": 1.0, "reason": "sweet spot for TC services" }
  ],
  "scoring": {
    "min_signals": 2,        // need at least 2 signals to qualify
    "recency_decay": 0.95,   // 5% score decay per day since listing
    "enrichment_boost": 1.3  // 30% boost if we have phone+email
  }
}
```

---

### Context-Aware Data Tiering

Large CRM result sets should return summaries, not full data. The agent uses `query_crm` for detail on demand.

**Tiering rules:**

| Result Size | Behavior | Context Cost |
|---|---|---|
| <20 rows | Return full data in tool response | ~1-2K tokens |
| 20-50 rows | Return full data + warn agent "consider narrowing query" | ~2-5K tokens |
| >50 rows | Return summary + preview (10 rows) + stage to Storage | ~500 tokens |

**Example: "Show me my pipeline"**

```
Agent has 80 active deals.
Without tiering:
  → Load all 80 deals into context (16K+ tokens)

With tiering:
  → query_crm returns:
    { summary: "80 active deals",
      byStage: { viewing: 25, offer: 18, negotiation: 12, closing: 8, nurture: 17 },
      topByValue: [top 5 deals],
      stagedPath: "artifacts/client_abc/query_1707660000.json" }
  → Agent: "You have 80 active deals. 25 in viewing stage, 18 with offers..."
  → User: "Show me the offers over $2M"
  → Agent: query_crm("SELECT * FROM deals WHERE stage='offer' AND value > 2000000")
  → Returns 4 deals (small, full data in context)
```

### Sandbox Data Staging

For multi-step workflows where artifact generation needs large datasets, the data is staged in Supabase Storage rather than passed through tool-call JSON.

**Flow:**

```
Small data (<50 rows):
  query_crm → { rows: [...] }
  generate_artifact({ data: rows }) → Sandbox receives JSON directly

Large data (>50 rows):
  query_crm → stages to Storage → { stagedPath: "artifacts/.../query.json" }
  generate_artifact({ stagedDataPath: "artifacts/.../query.json" })
  → Sandbox downloads from Storage directly
  → No megabytes serialized through tool-call JSON
```

**Why this matters for scale:** Viewing prep packs might query 20 comps + price history + district info = hundreds of rows. Property comparison videos need extensive data. Excel exports of 6 months of interactions across 200 contacts = megabytes. Staging keeps the agent's context clean while giving the sandbox access to full datasets.

### Mid-Workflow Clarification (via Trigger.dev Waitpoints)

Extends the existing Tier 3 waitpoint pattern to support agent asking user clarification questions mid-conversation. Same infrastructure, different use case.

**When it fires:**

- "I see two Sarahs in this conversation — Sarah Lee (buyer) and Sarah Tan (agent). Which one?"
- "This property is listed at $1.2M and $1.35M on different sites. Which price should I use?"
- "Should I include the renovation estimate in the property comparison?"

**Implementation:** Same `waitForToken` pattern as Tier 3 approvals:

```
Agent detects ambiguity during tool loop
→ Agent calls `ask_user_question` tool
→ Tool creates waitpoint token + sends question to user's chat (Tier 2)
→ Task pauses (zero compute cost)
→ User responds via WhatsApp
→ Gateway POSTs to /api/clarification → completes waitpoint token with answer
→ Task resumes with user's answer in context
```

**Difference from Tier 3:** Tier 3 waitpoints are for approval (yes/no/edit). Clarification waitpoints are for open-ended answers. Both use `waitForToken`, both pause with zero compute.

### JIT UI for Ambiguity Resolution

Extends mid-workflow clarification with a visual layer. When the AI can't confidently produce what the user wants, it **scopes first** (WhatsApp polls) then **shows a preview** (web link) before generating the final output. TDD for AI outputs: define the "test" (preview) before the "implementation" (final output).

**The problem:** WhatsApp is text-only. Most CRM operations are simple enough that text works fine. But when the user asks for something open-ended or ambiguous — a report, a comparison, an analysis — the AI guesses wrong. Without a defined output shape, the AI produces something the user didn't want. They iterate painfully, each round costing time and tokens. The user doesn't realize their request is vague ("Compare these properties" — on what dimensions? For what purpose?).

**The pattern: Fintool's AskUserQuestion, adapted for WhatsApp:**

| Function | Fintool (web chat) | RE-AI-CRM (WhatsApp + web) |
|---|---|---|
| **Scoping questions** | Rich UI inline (multiple choice cards) | WhatsApp polls (native Baileys, no typing) |
| **Preview of output** | Rendered inline (Plotly, SpreadJS) | Link to web preview page (phone browser) |
| **Feedback on preview** | Inline interaction | Back in WhatsApp chat |
| **Final output** | Rendered inline + download | Image/PDF/text sent in WhatsApp |

**Decision tree:**

```
User sends a message
    │
    ▼
Is this a clear, unambiguous request?
(CRM update, simple question, defined task)
    │
   YES → Just do it. Text response in WhatsApp.
    │     "Done. Logged your meeting with Sarah."
    │
    NO → The request is ambiguous or underspecified.
    │
    ▼
STEP 1: Scope via WhatsApp polls (ask_user tool)
    │  AI sends 1-3 polls to narrow down intent.
    │  📊 "What should I compare?" → Price & PSF / Size & layout / Everything
    │  📊 "Who is this for?" → The Tan family / Your own reference / To send to client
    │
    ▼
STEP 2: Generate preview → send link (generate_preview tool)
    │  AI: "Here's what I'll put together 👇"
    │  [sunder.app/preview/abc123]
    │  User taps link → phone browser → rendered preview (display-only)
    │
    ▼
STEP 3: User confirms or adjusts in WhatsApp
    │  "Looks good" → AI generates final output
    │  "Add the school district info" → AI updates preview
    │
    ▼
STEP 4: Final output sent in WhatsApp
    │  Image / PDF / text / link to full interactive version
```

**What triggers the ambiguity flow:**
- **Multiple valid interpretations** — "Compare these properties" (on what dimensions?)
- **Missing key parameters** — "Make a report for Sarah" (what kind? what timeframe?)
- **Open-ended creative request** — "Put together something for the Tans" (what is "something"?)
- **High-cost operation** — Anything that will call external APIs, generate artifacts, or take >30 seconds. Preview is cheap insurance against wasted work.

**What does NOT trigger it:** CRM CRUD, direct questions, clear instructions, acknowledgments — just do it.

**WhatsApp polls for scoping (via Baileys):**

Baileys reliably supports polls. They're native, interactive, require zero typing, and feel natural on mobile.

Design rules:
1. Max 3 polls per scoping round. More feels like a survey.
2. Always include an "Other" escape hatch — user can type in chat instead.
3. Keep options to 3-5 per poll. Short, scannable labels.
4. AI explains WHY it's asking: "I want to make sure I build the right thing. Quick question:"
5. Single-select by default. Multi-select only when genuinely needed.

Baileys implementation:

```typescript
await sock.sendMessage(clientJid, {
  poll: {
    name: question,          // "What should I compare?"
    values: options,          // ["Price & PSF", "Size & layout", "Everything"]
    selectableCount: allowMultiple ? options.length : 1,
  }
})
// Poll responses come back through Baileys messages.upsert events
// → forwarded to agent as tool results
```

**Web preview pages:**

Lightweight, mobile-first web pages that show a rendered mockup of what the AI will produce. User taps link in WhatsApp, sees preview in phone browser, goes back to WhatsApp to confirm or adjust.

Design principles:
1. **Mobile-first.** 100% of users open these on their phone from WhatsApp.
2. **Display-only.** No interactive editing, no forms. All feedback happens in chat.
3. **Fast.** Must load in <2 seconds on mobile. No heavy frameworks.
4. **Disposable.** Preview links expire after 24 hours.
5. **Branded but minimal.** Sunder logo, clean layout, no app chrome.

Technical approach — Next.js dynamic routes in the existing Vercel app:

```
/preview/[previewId]    → renders preview from stored JSON
```

Flow:
1. AI generates structured JSON spec (fields, dimensions, sample data)
2. JSON stored in Supabase (`preview_specs` table) with short-lived ID
3. AI sends `sunder.app/preview/{id}` link in WhatsApp
4. Next.js page fetches JSON, renders with React components
5. User views on phone → goes back to WhatsApp

**Preview component library (start small):**

| Component | Use case |
|---|---|
| `ComparisonCard` | Side-by-side property comparison |
| `PipelineView` | Deal stages with counts |
| `ContactSummary` | Contact card with key details |
| `ReportOutline` | Section headers + bullet points showing what the report will cover |
| `TaskList` | Upcoming tasks grouped by date/priority |
| `MarketSnapshot` | Key metrics for an area/property type |

These are NOT the final output — they're preview wireframes. Styled simply, with placeholder/sample data where the real data will go.

**Tambo.co consideration:** Tambo (open-source React toolkit) does exactly this: register React components with Zod schemas, AI selects and populates them. Overkill for MVP (we only need ~6 preview components). Worth evaluating when library grows beyond 10 types. The Zod schema pattern is worth stealing regardless — define props schemas for each preview component even without Tambo.

**Data model:** See `preview_specs` table in Component 4: Supabase section.

**Implementation phases:**
- **Phase 1 (MVP):** Polls only. Implement `ask_user` tool, wire WhatsApp poll sending/response via Baileys. No web preview yet — AI describes what it will build in text after scoping.
- **Phase 2:** Web preview pages. Build `preview_specs` table, `/preview/[id]` route, first 3 components (ComparisonCard, ReportOutline, PipelineView), `generate_preview` tool.
- **Phase 3:** Expand component library based on usage. Evaluate Tambo if >10 components. Add preview analytics.

### Eval Framework

Tier 1 reads ALL WhatsApp conversations autonomously. A bad extraction creates wrong contacts, logs incorrect deals, damages user's real client relationships. Evals are not post-launch polish — they are the foundation. Source: Fintool has ~2,000 test cases, blocks PRs if eval score drops >5%.

**MVP: 20 test cases minimum before launch.**

| Category | Test Cases | What We Validate |
|---|---|---|
| **Tier 1: Extraction accuracy** | 8 | Contact name extraction, phone number parsing, interaction type classification, deal signal detection, follow-up detection |
| **Tier 2: Conversation quality** | 6 | CRM query accuracy, memory recall, appropriate tool selection, Tier 3 drafting (never auto-sends), personality consistency (SOUL.md) |
| **Creator path: Artifact fidelity** | 3 | PDF contains correct data, chart labels match query, Excel export matches source data |
| **Edge cases** | 3 | Ambiguous contact names (two Sarahs), mixed-language messages (English + Mandarin), group chat filtering (should be skipped) |

**Eval-driven development rules:**
- Every new skill gets at least 2 companion test cases
- PR blocked if eval score drops >5%
- Test cases stored in `/evals/` directory alongside the codebase
- Run evals on every model change (switching from Sonnet to Kimi? Run evals first)

**Scaling path:**

| Phase | Test Cases | Trigger |
|---|---|---|
| MVP | 20 | Launch |
| Month 1 | 50 | First 10 users surface edge cases |
| Growth | 100+ | Each bug becomes a test case |
| Scale | 200+ | Per-skill evals, per-vertical evals |

### Session Management & Context Compaction

RE agents chat daily. Without boundaries and compaction, conversation history blows past context windows within weeks. This section defines how conversations are segmented and how history is compressed. (Inspired by OpenClaw's session reset + context compaction patterns.)

**Session boundaries — idle-based segmentation:**

```
Message arrives
      │
      ▼
Time since last message?
      │
      ├── < 2 hours ──► SAME SEGMENT: load full recent history (up to 50 msgs)
      │
      ├── 2-8 hours ──► NEW SEGMENT: compact old segment → summary, start fresh
      │                  Keep last 5 messages as bridge context
      │
      └── > 8 hours ──► NEW DAY: compact everything, start with memory + tasks only
      │
Also: explicit reset triggers ("new topic", "start fresh", "different question")
      └── force new segment regardless of timing
```

**Context compaction — how old messages become summaries:**

```typescript
// Inside agent-conversation Trigger.dev task, before building system prompt
const COMPACTION_THRESHOLD = 100_000; // tokens — trigger compaction above this
const RECENT_MESSAGES_MIN = 20;       // always keep at least this many

async function loadConversationContext(clientId: string, sessionType: string) {
  if (sessionType === 'new_day') {
    // Full compaction — just load summaries + memory
    return {
      messages: [],
      summaries: await db.getConversationSummaries(clientId, { limit: 5 }),
    };
  }

  if (sessionType === 'new_segment') {
    // Compact old segment, keep bridge
    await compactOldMessages(clientId, { keepRecent: 5 });
    return {
      messages: await db.getRecentMessages(clientId, { limit: 5 }),
      summaries: await db.getConversationSummaries(clientId, { limit: 3 }),
    };
  }

  // Same segment — load full recent, compact only if over threshold
  const recent = await db.getRecentMessages(clientId, { limit: 200 });
  if (estimateTokens(recent) > COMPACTION_THRESHOLD) {
    const toKeep = recent.slice(0, RECENT_MESSAGES_MIN);
    const toCompact = recent.slice(RECENT_MESSAGES_MIN);
    await compactMessages(clientId, toCompact);
    return { messages: toKeep, summaries: await db.getConversationSummaries(clientId, { limit: 3 }) };
  }
  return { messages: recent, summaries: [] };
}

async function compactMessages(clientId: string, messages: Message[]) {
  // Split into 50-message chunks, summarize each with Haiku (cheap)
  const chunks = chunkArray(messages, 50);
  for (const chunk of chunks) {
    const summary = await generateText({
      model: registry.languageModel("anthropic:claude-haiku-4-5"),
      system: "Summarize concisely. Preserve: contact names + details, decisions made, open tasks, deal status changes, personal details, budget/timeline info.",
      prompt: formatMessagesForSummary(chunk),
    });
    await db.createConversationSummary({
      clientId,
      summary: summary.text,
      messagesFrom: chunk[chunk.length - 1].created_at,
      messagesTo: chunk[0].created_at,
      messageCount: chunk.length,
    });
    await db.markMessagesCompacted(chunk.map(m => m.id));
  }
}
```

**Key decisions:**
- **Haiku for summarization.** Compaction is pattern-matching. Cheap model. ~$0.001 per compaction.
- **50-message chunks.** Small enough to summarize well, large enough to capture threads.
- **Never delete original messages.** Mark as `compacted` flag. Raw data always recoverable.
- **Summaries are cumulative.** Each compaction creates a new summary row. Builds "session history" over weeks.
- **Compaction runs at the START of a task,** not the end. First message after idle pays the cost.
- **Summaries injected into Layer 4** of the system prompt as `[Previous conversation summary]` blocks.

### Cron Jobs (Trigger.dev Scheduled Tasks)

| Job | Schedule | Trigger.dev task | What it does |
|---|---|---|---|
| Morning briefing | Daily 8am per TZ | `morning-briefing` | Load all active clients → batchTrigger per client → generate summary → send to user's chat (Tier 2) |
| Follow-up nudge | Daily 6pm per TZ | `follow-up-nudge` | Check interactions with no follow-up task → AI suggests next steps → send to user's chat (Tier 2) |
| Stale lead check | Weekly Monday | `stale-lead-check` | Find contacts with no interaction in 14+ days → suggest re-engagement to user (Tier 2) |
| Territory scraper | Daily 2am per TZ | `territory-scrape` | Load active territory configs → batchTrigger per client → scrape listings (Browserbase) → extract signals → enrich agents (Perplexity) → score → sync CRM → flag for briefing |
| Scheduled sends + recurring tasks | Every minute | `process-scheduled` | Check pending_messages where status=approved AND scheduled_at <= now → execute via gateway (Tier 3). **Also:** check recurring_tasks where next_run_at <= now → create one-time task + advance next_run_at. |

**Note:** All cron outputs go to user's own chat (Tier 2). Cron NEVER auto-sends to third parties. Scheduled Tier 3 sends still require prior user approval.

**Why Trigger.dev for cron (not Vercel Cron):**
- **Batch triggering:** Morning briefing for 50 clients = `batchTrigger("morning-briefing", clients.map(...))`. Trigger.dev handles concurrency automatically.
- **Per-client queues:** Each client's briefing runs in their queue. If one client's briefing fails, others are unaffected.
- **Retries:** If a briefing fails (LLM timeout, Supabase hiccup), Trigger.dev retries with backoff. Vercel Cron just fires and forgets.
- **Observability:** See every cron run, per client, with full traces. Vercel Cron gives you nothing.
- **No timeout risk:** Vercel Cron triggers a serverless function (60s limit). Trigger.dev tasks run as long as needed.

```typescript
import { schedules, task } from "@trigger.dev/sdk/v3";
import { generateText } from "ai";

// Parent: fires daily, fans out to per-client briefings
export const morningBriefingSchedule = schedules.task({
  id: "morning-briefing-schedule",
  cron: { pattern: "0 0 * * *", timezone: "Asia/Singapore" }, // midnight UTC = 8am SGT
  run: async (payload) => {
    const clients = await db.getActiveClients();
    // batchTrigger creates one run per client, concurrency-controlled
    await clientBriefing.batchTrigger(
      clients.map(c => ({
        payload: { clientId: c.id },
        options: {
          queue: { name: "agent-conversation", concurrencyLimit: 1 },
          concurrencyKey: c.id, // reuses per-client queue
        },
      }))
    );
  },
});

// Child: generates one client's briefing
export const clientBriefing = task({
  id: "client-briefing",
  retry: { maxAttempts: 3 },
  run: async (payload: { clientId: string }) => {
    const memories = await db.getMemories(payload.clientId);
    const tasks = await db.getTodaysTasks(payload.clientId);
    const overdue = await db.getOverdueTasks(payload.clientId);

    const result = await generateText({
      model: registry.languageModel("anthropic:claude-haiku-4-5"),
      system: buildBriefingPrompt(memories, tasks, overdue),
      prompt: "Generate this agent's morning briefing.",
    });

    // Send to user's WhatsApp via gateway
    await gateway.sendToUser(payload.clientId, result.text);
  },
});
```

### Concurrency (Trigger.dev Per-Client Queues via concurrencyKey)

Per-client queue using `concurrencyKey`. Each client gets their own independent queue with concurrency 1. No in-memory mutex needed.

```typescript
import { task } from "@trigger.dev/sdk/v3";
import { generateText } from "ai";

// Task definition — default queue config
export const agentConversation = task({
  id: "agent-conversation",
  retry: {
    maxAttempts: 3,
    factor: 1.8,
    minTimeoutInMs: 1000,
    maxTimeoutInMs: 30000,
  },
  run: async (payload: { clientId: string; message: string; messageType: string }) => {
    // Agent loop runs here with Vercel AI SDK
    // Per-client concurrency enforced at trigger time (see below)
  },
});
```

```typescript
// Triggering from Vercel API route — concurrencyKey creates per-client queue
import { agentConversation } from "~/trigger/agent-conversation";

export async function POST(request: Request) {
  const { clientId, message, messageType } = await request.json();

  const handle = await agentConversation.trigger(
    { clientId, message, messageType },
    {
      queue: {
        name: "agent-conversation",
        concurrencyLimit: 1,  // max 1 concurrent run per client
      },
      concurrencyKey: clientId,  // ← each client gets their own queue
      tags: [`client-${clientId}`],  // ← for cancel: find queued runs by client
    }
  );

  // Return handle immediately — gateway subscribes to run for streaming
  return Response.json({ runId: handle.id });
}
```

**How concurrencyKey works:**
- `concurrencyKey: "client_abc"` creates queue `agent-conversation:client_abc` (concurrency 1)
- `concurrencyKey: "client_def"` creates queue `agent-conversation:client_def` (concurrency 1)
- Client A and Client B run in parallel (different queues)
- Client A's rapid-fire messages are serialized (same queue)

```
Client A sends 3 messages:     Client B sends 1 message:
  Msg 1 → runs immediately       Msg 1 → runs immediately (different queue)
  Msg 2 → queued behind msg 1
  Msg 3 → queued behind msg 2
```

**Why this is better than in-memory mutex:**
- Vercel serverless functions don't share memory across invocations → in-memory locks don't work
- Trigger.dev queues are durable → survive deployments, crashes, scaling events
- `concurrencyKey` isolates clients → one slow client doesn't block others
- Built-in observability → see queue depth, wait times per client
- No Redis dependency for MVP

### Task Cancellation (Trigger.dev `runs.cancel()`)

WhatsApp has no "stop" button. Users say "stop", "cancel", "nevermind" as natural language. Cancellation must be fast (no LLM routing) and must handle three states: active run, queued runs, and paused waitpoints.

**The problem Fintool solves with Temporal heartbeats:**
> "User clicks 'stop' — what happens? The activity is already running on a different server. Use heartbeats sent every few seconds."

**Our adaptation:** Gateway detects cancel intent via regex (no LLM, <1ms). Vercel API route cancels via Trigger.dev SDK. No heartbeat needed — Trigger.dev cancellation is immediate via API.

**Cancel flow:**

```
User sends "stop" / "cancel" / "nevermind"
      │
      ▼
Gateway regex matches cancel intent (BEFORE routing to /api/message)
      │
      ├── 1. Gateway sends "Got it, cancelled." to user (Tier 2, instant feedback)
      │
      └── 2. Gateway POSTs to /api/cancel { clientId }
                │
                ▼
          Vercel API route /api/cancel:
                │
                ├── a. Look up active run: SELECT run_id FROM active_agent_runs
                │      WHERE client_id = $1 AND status = 'running'
                │
                ├── b. Cancel active run: runs.cancel(runId)
                │      → Trigger.dev cancels the running task immediately
                │      → Task receives CancelledError at next checkpoint/await
                │
                ├── c. Flush queued runs for this client:
                │      List runs with status 'queued' for this concurrencyKey
                │      → Cancel each one (prevents queued messages from executing)
                │
                ├── d. Cancel pending waitpoints (if any):
                │      SELECT trigger_token_id FROM pending_messages
                │      WHERE client_id = $1 AND status = 'awaiting_approval'
                │      → wait.completeToken(tokenId, { approved: false })
                │      → Paused tasks resume and clean up gracefully
                │
                └── e. Update active_agent_runs: SET status = 'cancelled'
```

**Implementation:**

```typescript
// Vercel API route: /api/cancel
import { runs } from "@trigger.dev/sdk/v3";

export async function POST(request: Request) {
  const { clientId } = await request.json();
  verifyGatewayHmac(request); // auth

  // 1. Cancel active run
  const activeRun = await db.getActiveRun(clientId);
  if (activeRun) {
    await runs.cancel(activeRun.run_id);
    await db.updateActiveRun(activeRun.id, { status: 'cancelled' });
  }

  // 2. Flush queued runs for this client
  const queuedRuns = await runs.list({
    status: ["QUEUED"],
    tag: `client-${clientId}`,
  });
  for (const run of queuedRuns.data) {
    await runs.cancel(run.id);
  }

  // 3. Cancel pending waitpoints (Tier 3 drafts, mid-workflow questions)
  const pendingTokens = await db.getPendingWaitpoints(clientId);
  for (const token of pendingTokens) {
    await wait.completeToken(token.trigger_token_id, { approved: false });
    await db.updatePendingMessage(token.id, { status: 'cancelled' });
  }

  return Response.json({ cancelled: true });
}
```

```typescript
// Inside agent-conversation task: track active run for cancel lookups
import { task, context } from "@trigger.dev/sdk/v3";

export const agentConversation = task({
  id: "agent-conversation",
  retry: { maxAttempts: 3 },
  run: async (payload: { clientId: string; message: string; messageType: string }) => {
    // Register this run as active (for cancel lookups)
    await db.upsertActiveRun({
      client_id: payload.clientId,
      run_id: context.run.id,
      status: 'running',
      started_at: new Date(),
    });

    try {
      // ... normal agent loop ...
    } finally {
      // Clean up active run record on completion or cancellation
      await db.updateActiveRunByRunId(context.run.id, { status: 'completed' });
    }
  },
});
```

**`active_agent_runs` table:**

```sql
CREATE TABLE active_agent_runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  run_id TEXT NOT NULL,              -- Trigger.dev run ID
  status TEXT NOT NULL DEFAULT 'running', -- running | completed | cancelled
  started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at TIMESTAMPTZ,
  UNIQUE (client_id, run_id)
);

-- Fast lookup: "what's running for this client?"
CREATE INDEX idx_active_runs_client_status
  ON active_agent_runs(client_id, status)
  WHERE status = 'running';

-- RLS
ALTER TABLE active_agent_runs ENABLE ROW LEVEL SECURITY;
CREATE POLICY client_isolation ON active_agent_runs
  USING (client_id = current_setting('app.client_id')::uuid);
```

**Three states handled:**

| State when user cancels | What happens |
|---|---|
| **Active run** (agent mid-tool-loop) | `runs.cancel(runId)` → task gets `CancelledError` at next checkpoint. Partial work (e.g., contacts already created) persists — cancel doesn't rollback. |
| **Queued runs** (messages waiting behind active) | Each queued run cancelled. Messages effectively dropped. User can re-send if needed. |
| **Paused waitpoint** (Tier 3 approval or mid-workflow question) | Token completed with `{ approved: false }`. Task resumes, sees rejection, cleans up. |

**Design decisions:**
- **Gateway-level detection, not LLM.** Cancel must be instant. Waiting for the agent to "understand" the cancel intent adds 2-10s latency and costs tokens. Regex is free and fast.
- **No rollback on partial work.** If the agent already created a contact before cancel, the contact stays. This is intentional — partial state is better than a complex compensation saga for a CRM.
- **User gets immediate feedback.** Gateway sends "Got it, cancelled." before the API call completes. User doesn't wait.
- **Queued messages are dropped, not deferred.** If user rapid-fired 3 messages then said "stop", all queued messages are cancelled. User can re-send whatever they need after.
- **Tags for queue filtering.** When triggering agent-conversation, include `tags: ["client-${clientId}"]` so `/api/cancel` can find queued runs by client.

### Tier 1 Extraction Idempotency (Message Dedup)

Baileys replays messages on reconnect. Webhooks can fire twice. Trigger.dev retries re-invoke tasks. Without dedup, the same WhatsApp message creates duplicate contacts, duplicate interactions, duplicate deal signals.

**The problem Fintool solves:**
> "The Lambda marks the publication/alert pair as processed, ensuring no re-fire if the document gets reindexed."

**Our adaptation:** Every Baileys message has a globally unique `key.id` (e.g., `3EB0A6170C6B71A9D331`). We use this as an idempotency key at two levels: gateway (fast dedup before API call) and API (Supabase check before extraction).

**Dedup flow:**

```
Baileys fires messages.upsert event
      │
      ▼
For each message:
      │
      ├── Gateway-level dedup (in-memory LRU cache, 10K entries):
      │   messageId in recentlyProcessed? → SKIP (common case: reconnect replay)
      │
      ├── API-level dedup (Supabase check):
      │   POST /api/extract/check { clientId, messageId }
      │   → SELECT 1 FROM processed_messages WHERE message_id = $1 AND client_id = $2
      │   → exists? SKIP (handles: cache miss after gateway restart)
      │
      └── Process message:
          POST /api/extract { clientId, msg, messageId, ... }
          → Extract contacts, interactions, deals
          → INSERT INTO processed_messages (message_id, client_id, chat_jid, processed_at)
          → Add messageId to in-memory cache
```

**Implementation:**

```typescript
// Gateway worker: two-level dedup
import { LRUCache } from 'lru-cache'

const processedCache = new LRUCache<string, true>({ max: 10_000 })

sock.ev.on('messages.upsert', async ({ messages, type }) => {
  for (const msg of messages) {
    const messageId = msg.key.id
    if (!messageId) continue

    // Level 1: In-memory LRU (fast, handles reconnect bursts)
    const cacheKey = `${clientId}:${messageId}`
    if (processedCache.has(cacheKey)) continue

    // Level 2: DB check (handles gateway restart where cache is cold)
    const { duplicate } = await api.post('/api/extract/check', {
      clientId, messageId
    })
    if (duplicate) {
      processedCache.set(cacheKey, true) // warm cache for future
      continue
    }

    // Process
    await api.post('/api/extract', {
      clientId, msg, type,
      fromMe: msg.key.fromMe,
      chatJid: msg.key.remoteJid,
      messageId
    })

    processedCache.set(cacheKey, true)
  }
})
```

```typescript
// Vercel API route: /api/extract/check
export async function POST(request: Request) {
  const { clientId, messageId } = await request.json();
  verifyGatewayHmac(request);

  const { count } = await supabase
    .from('processed_messages')
    .select('*', { count: 'exact', head: true })
    .eq('client_id', clientId)
    .eq('message_id', messageId);

  return Response.json({ duplicate: (count ?? 0) > 0 });
}
```

```typescript
// Vercel API route: /api/extract — mark as processed BEFORE extraction
export async function POST(request: Request) {
  const { clientId, msg, messageId, chatJid, fromMe } = await request.json();
  verifyGatewayHmac(request);

  // Insert first (claim the message). ON CONFLICT = another worker got here first.
  const { error } = await supabase
    .from('processed_messages')
    .insert({
      client_id: clientId,
      message_id: messageId,
      chat_jid: chatJid,
      from_me: fromMe,
      processed_at: new Date().toISOString(),
    })
    .onConflict('client_id, message_id');

  if (error?.code === '23505') {
    // Unique constraint violation — already processed by another request
    return Response.json({ status: 'duplicate' });
  }

  // Proceed with extraction...
  // (existing Tier 1 extraction logic)
}
```

**`processed_messages` table:**

```sql
CREATE TABLE processed_messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID NOT NULL REFERENCES clients(id),
  message_id TEXT NOT NULL,           -- Baileys key.id (globally unique per message)
  chat_jid TEXT NOT NULL,             -- which chat this message came from
  from_me BOOLEAN NOT NULL DEFAULT false,
  processed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  extraction_status TEXT DEFAULT 'processed', -- processed | skipped | error
  UNIQUE (client_id, message_id)      -- dedup constraint
);

-- Fast dedup lookup
CREATE INDEX idx_processed_messages_dedup
  ON processed_messages(client_id, message_id);

-- Cleanup: messages older than 30 days can be pruned (optional cron)
-- The dedup only needs to cover the reconnect window (~24h of message replay)
CREATE INDEX idx_processed_messages_age
  ON processed_messages(processed_at);

-- RLS
ALTER TABLE processed_messages ENABLE ROW LEVEL SECURITY;
CREATE POLICY client_isolation ON processed_messages
  USING (client_id = current_setting('app.client_id')::uuid);
```

**Why two levels of dedup:**

| Level | Speed | Survives gateway restart? | Purpose |
|---|---|---|---|
| **LRU cache** (gateway) | <0.1ms | No | Fast path for reconnect bursts (Baileys replays 100s of messages in seconds) |
| **Supabase check** (API) | ~5ms | Yes | Durable dedup. Handles: gateway restart (cold cache), webhook replay, Trigger.dev task retry |

**Design decisions:**
- **Insert-before-extract (claim pattern).** The `processed_messages` insert happens BEFORE extraction starts. If extraction fails and Trigger.dev retries, the retry hits the unique constraint and skips. This is "at-most-once" extraction — safer than "at-least-once" for a CRM (duplicate contacts are worse than a missed message that gets picked up on the next sync).
- **ON CONFLICT for race conditions.** Two gateway workers processing the same reconnect burst may both pass the LRU cache check. The DB unique constraint is the tiebreaker.
- **30-day TTL.** Baileys reconnect replays recent messages (hours to days). No need to keep dedup records forever. Optional cron prunes old rows.
- **Not on the hot path for Tier 2.** Only Tier 1 (read-all extraction) needs dedup. Tier 2 (user's own messages to AI) is conversational — duplicate messages are harmless (user just asked twice, agent answers twice). Dedup on Tier 2 would add latency to the interactive path for no benefit.

### Tech Stack

- **Runtime:** Node.js / TypeScript
- **Framework:** Next.js (App Router) — dashboard + lightweight API routes
- **Agent SDK:** OpenAI Agents SDK (`@openai/agents`) + Vercel AI SDK adapter (`@openai/agents-extensions`, `@ai-sdk/google`, `@openrouter/ai-sdk-provider`)
- **Providers:** `@ai-sdk/anthropic`, `@ai-sdk/openrouter` (swap models via config)
- **Durable execution:** Trigger.dev v4 — agent tasks, cron, queues, waitpoints, streaming
  - **Alternative: Fly.io Sprite** — Tasks stay alive via API expiration control. Start a task with `POST /v1/tasks {"name": "my-build", "expire_seconds": 3600}` (max 1 hour). Task continues running as long as: (1) holding an HTTP connection, (2) exec session generating stdout, or (3) updated with API call. Delete with `DELETE /v1/tasks/my-build`. Good for keeping background processes alive without external orchestration. Source: [@mrkurt thread Feb 11, 2026](https://twitter.com/mrkurt/status/1759372733)
- **DB client:** Supabase JS SDK
- **Sandbox (artifacts):** Vercel Sandbox (on-demand, called from Trigger.dev tasks)
- **Document extraction:** Gemini 2.5 Flash (classification + simple extraction), ExtendAI (complex extraction with per-field confidence + citations)
- **Browser research:** Browserbase + Stagehand (per-user auth, called from Trigger.dev tasks)
- **Deployment:** Vercel (frontend + CRUD routes), Trigger.dev Cloud (agent tasks)

---

## Component 3: Dashboard

### What it does

Same Next.js app as the API layer. Two views.

### Agent view (app.sunder.ai)

Logged-in RE agent sees their own data. Read-only for MVP.

| Page | Content |
|---|---|
| Pipeline | Deals by stage (kanban or list view) |
| Contacts | All contacts, search/filter, click into detail |
| Contact detail | Interactions history, deals, tasks, AI summary |
| Tasks | Overdue, today, upcoming |
| Activity feed | Recent interactions across all contacts |

- **Auth:** Supabase Auth (email/password). RLS scopes all queries to their client_id.
- **Reads from Supabase directly** — no API routes needed for dashboard queries.

### Admin view (admin.sunder.ai)

Your view. Manages all clients.

| Page | Content |
|---|---|
| Clients | List, status, plan, WhatsApp paired? |
| Gateway health | Calls gateway REST API /sessions — shows connection status per client |
| Usage | API calls, tokens, cost per client (from usage_log table) |
| Billing | Stripe integration, plan management |

- **Auth:** Your login only. Service role or admin-scoped JWT.

### What the dashboard does NOT do (MVP)

- No editing (manage everything via WhatsApp)
- No chat interface (WhatsApp only — future: add via Vercel AI SDK `useChat()` hooks)
- No dashboard-based message approval (MVP approval is WhatsApp-only; dashboard approval is v2+)
- No real-time updates (refresh is fine; add Supabase Realtime later)

### Tech stack

- **Framework:** Next.js (App Router) — same app as API layer
- **Styling:** Tailwind + shadcn/ui
- **Data:** Supabase JS client (direct queries, RLS-scoped)
- **Hosting:** Vercel

---

## Component 4: Supabase

Same schema as v1 architecture doc. See ARCHITECTURE.md Part 4 for full SQL.

**Key points:**
- RLS on every table, filtered by client_id
- Custom JWT with client_id claim (minted by API layer)
- Dashboard uses Supabase Auth (standard email/password flow)
- API layer uses per-client JWT for data isolation

**New tables for v2.4:**

| Table | Purpose | Added in |
|---|---|---|
| `ai_memory` | Agent's self-written notes per client (key-value, text). Includes `embedding vector(1536)` (nullable) + `search_text tsvector` (auto-generated) for semantic search migration. | v2.1 (schema extended v2.3) |
| `artifacts` | Creator path outputs (PDFs, charts, videos) with storage URLs | v2.1 |
| `conversation_summaries` | Compacted conversation history. Each row = one summarized chunk. Fields: `summary TEXT`, `messages_from/to TIMESTAMPTZ`, `message_count INTEGER`, `token_estimate INTEGER`. | v2.3 |
| `recurring_tasks` | Agent-created recurring reminders. Fields: `description TEXT`, `schedule_type` (daily/weekly/biweekly/monthly), `schedule_day INTEGER`, `schedule_time TIME`, `next_run_at TIMESTAMPTZ`, `status` (active/paused/cancelled). Processed by `process-scheduled` cron. | v2.3 |
| `domain_knowledge_index` | Index for domain knowledge files in Supabase Storage. Fields: `slug TEXT`, `storage_path TEXT`, `client_id UUID` (null=platform), `tags TEXT[]`, `trigger_keywords TEXT[]`, `always_load BOOLEAN`, `token_estimate INTEGER`. Unique on (slug, client_id). See Domain Knowledge Architecture section. | v2.4 |
| `skills_index` | Index for skill files in Supabase Storage. Fields: `slug TEXT`, `storage_path TEXT`, `client_id UUID` (null=platform), `description TEXT NOT NULL` (shown in skill menu), `tags TEXT[]`, `token_estimate INTEGER`, `created_by TEXT` ('platform' or 'agent'). Unique on (slug, client_id). Lazy-loading: only `slug` + `description` injected into system prompt as menu; full content read on demand via `read_skill` tool. Same shadowing pattern as domain_knowledge_index. See Skills Filesystem Architecture section. | v2.5 |
| `onboarding_results` | Staging table for onboarding analysis output. Fields: `contacts JSONB`, `deals JSONB`, `style_profile TEXT`, `working_patterns JSONB`, `message_count INTEGER`, `status` (pending_confirmation/confirmed/skipped). User must confirm before data enters CRM. | v2.4 |
| `documents` | Inbound documents (files user sends to AI). Fields: `storage_path TEXT`, `original_filename TEXT`, `file_type TEXT`, `file_hash TEXT` (dedup), `status` (uploaded/processing/complete/failed), `primary_tag TEXT`, `tags JSONB`, `description TEXT`, `is_heterogeneous BOOLEAN`, `document_date DATE`. FK to `contacts`, `deals`. RLS on `client_id`. See Document System section. | v2.8 |
| `document_extractions` | Per-split extraction results. Fields: `split_index INTEGER`, `start_page/end_page INTEGER`, `tag_id TEXT`, `identifier TEXT`, `extracted_data JSONB`, `original_extracted_data JSONB` (immutable audit), `extraction_metadata JSONB` (per-field confidence + citations), `extraction_status`, `validation_failures JSONB`, `low_confidence_fields JSONB`. RLS via parent `documents.client_id`. | v2.8 |
| `extraction_schemas` | User-defined custom extraction schemas. Fields: `slug TEXT`, `display_name TEXT`, `classification_hint TEXT`, `fields JSONB` (array of name/type/description/required), `extraction_backend` (gemini/extend), `extend_processor_id TEXT`, `validate_rules JSONB`, `sample_count INTEGER`, `status` (draft/active/archived). Unique on (client_id, slug). RLS on `client_id`. | v2.8 |
| `active_agent_runs` | Tracks currently running Trigger.dev task per client for cancellation. Fields: `run_id TEXT NOT NULL` (Trigger.dev run ID), `status TEXT` (running/completed/cancelled), `started_at TIMESTAMPTZ`, `ended_at TIMESTAMPTZ`. Unique on (client_id, run_id). Index on (client_id, status) WHERE status='running'. Used by `/api/cancel` to find and cancel active runs. | v2.9 |
| `processed_messages` | Idempotency table for Tier 1 extraction. Fields: `message_id TEXT NOT NULL` (Baileys key.id), `chat_jid TEXT`, `from_me BOOLEAN`, `processed_at TIMESTAMPTZ`, `extraction_status TEXT` (processed/skipped/error). Unique on (client_id, message_id). Prevents duplicate extraction on gateway reconnect, webhook replay, or Trigger.dev retry. 30-day TTL (optional prune cron). | v2.9 |
| `preview_specs` | JIT UI preview specifications. Fields: `id TEXT PRIMARY KEY` (nanoid), `client_id UUID` (FK clients), `type TEXT NOT NULL` (comparison/pipeline/contact_summary/report_outline/task_list/market_snapshot), `spec JSONB NOT NULL` (structured JSON the preview renders), `status TEXT DEFAULT 'pending'` (pending/confirmed/expired), `created_at TIMESTAMPTZ`, `expires_at TIMESTAMPTZ DEFAULT now() + interval '24 hours'`, `confirmed_at TIMESTAMPTZ`. RLS on `client_id`. 24-hour TTL — previews are disposable. See JIT UI for Ambiguity Resolution section. | v3.1 |

---

## Auth & Signup Flow

### Three auth layers

```
LAYER 1: Web (dashboard login)
────────────────────────────────
Standard Supabase Auth. Email/password or magic link.
User logs into dashboard → RLS scopes their data.

LAYER 2: WhatsApp → API (implicit via gateway)
──────────────────────────────────────────────────────
No "WhatsApp login." When you provision a Baileys worker,
you map it to a client_id. Every message from that worker
is already authenticated — the Baileys session IS the auth.

  gateway-manager knows:
    worker_001 → client_abc → phone +6591234567

  When worker_001 forwards a message to API:
    POST /api/message { clientId: "client_abc", text: "..." }
    + HMAC signature proving it came from the gateway

LAYER 3: API → Supabase (per-client JWT)
─────────────────────────────────────────────
API mints a JWT with { client_id: "client_abc" }
for each Supabase query. RLS enforces data isolation.
Even if your code has a bug, Postgres won't return
another client's data.
```

### Signup flow

```
1. LANDING PAGE (sunder.ai)
   └── User clicks "Get Started"

2. SIGNUP (Supabase Auth)
   └── Email + password (or Google OAuth)
   └── Creates auth user in Supabase
   └── Creates row in clients table:
       { id: "client_abc", email, plan: "trial" }

3. PAYMENT (Stripe)
   └── Checkout session (or skip for free trial)
   └── Updates clients.stripe_customer_id

4. ONBOARDING PAGE (app.sunder.ai/setup)
   └── Backend calls: POST gateway/sessions { clientId: "client_abc" }
   └── Gateway spins up Baileys worker
   └── Page polls: GET gateway/sessions/client_abc/qr
   └── Displays QR code to user

5. USER SCANS QR WITH WHATSAPP
   └── Baileys worker detects pairing
   └── Updates clients.whatsapp_paired = true
   └── Gateway notifies API: client_abc is live
   └── Baileys begins syncFullHistory (backfills recent chats)

5.5 HISTORY ANALYSIS (background, automatic — 2-5 min)
    └── History sync completes (or enough messages buffered)
    └── Trigger "onboarding-analysis" Trigger.dev task
    └── Process last 30 days of chat history in batches
    └── Extract: contacts, active deals, communication style
    └── See "Onboarding Analysis" section below for full design

5.7 OPTIONAL: CONNECT SERVICES (prompted in user chat or onboarding page)
    └── AI asks: "Want me to check your Google Calendar too?
        I can find upcoming viewings and client meetings."
    └── User taps OAuth link → Composio handles auth flow
    └── Calendar/Gmail data enriches the initial analysis
    └── More contacts discovered, meetings mapped to deals
    └── See "Connected Services" section below

6. FIRST MESSAGE (personalized from analysis)
   └── AI sends personalized summary instead of generic intro:
       "I've been looking through your recent chats. Here's what I found:

       🔥 Active:
       • Sarah Lee — viewing at 38 Orchard Rd this Thursday
       • David Tan — negotiating 12 Nassim, last msg 2 days ago

       📋 34 contacts detected (12 buyers, 8 sellers, 14 others)
       📅 [if calendar connected] 3 viewings this week

       Does this look right? Reply 'yes' to confirm,
       or tell me what to fix."

   └── Graceful degradation: if history sync is sparse (new phone,
       cleared chats, few messages), fall back to generic intro:
       "Hey! I'm your AI assistant for managing client relationships.
       Tell me about your current clients and I'll start tracking."

7. USER CONFIRMS/CORRECTS
   └── "Yes" → confirmed contacts committed to CRM, style profile
       written to ai_memory, deals created
   └── Corrections → AI updates and learns ("Actually Sarah is a
       seller, not a buyer" → corrects contact type)
   └── User can also ignore — nothing auto-commits without confirmation

8. USER IS LIVE
   └── WhatsApp = primary interface
   └── Dashboard = visibility (app.sunder.ai, same login)
   └── CRM pre-populated (not empty) — cold-start problem solved
```

### Session recovery

If the gateway server restarts:
- Baileys auth state is persisted on disk
- Workers reconnect automatically using stored auth
- Users don't need to re-scan QR
- If auth state is corrupted → user needs to re-scan (rare)

### Security considerations

- **Baileys is unofficial.** WhatsApp doesn't endorse it. Risk of Meta blocking. Mitigation: evaluate WhatsApp Business API at 50+ users.
- **Gateway shared secret** must be rotated and stored securely (env vars, not code).
- **Per-client JWTs** should have reasonable expiry (30-90 days) with rotation.
- **Phone number = identity.** If a user changes their phone number, they need to re-pair.

### Interactive Onboarding Flow

**What it is:** Multi-step setup wizard that runs BEFORE history analysis. Captures user preferences for personality, communication style, model selection, and connected services. Creates personalized agent configuration.

**8-step flow (all optional except step 1):**

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: What's my name?                                         │
│                                                                  │
│          ●─────────○ ○ ○ ○ ○ ○ ○ ○                              │
│                                                                  │
│                      [Agent Avatar]                              │
│                                                                  │
│        Hey! Just spawned in. What's my name?                     │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │ [User enters name]                          │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│                                        [Continue]                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: How should I write?                                     │
│                                                                  │
│          ● ●─────────○ ○ ○ ○ ○ ○ ○                              │
│                                                                  │
│                   [Agent Avatar + Name]                          │
│                                                                  │
│        ┌──────────────────────┐  ┌──────────────────────┐       │
│        │  no caps, no stress  │  │  crisp & polished    │       │
│        └──────────────────────┘  └──────────────────────┘       │
│                                                                  │
│        ┌──────────────────────┐  ┌──────────────────────┐       │
│        │ like texting a friend│  │ delightfully unhinged│       │
│        └──────────────────────┘  └──────────────────────┘       │
│                                                                  │
│        [Back]                              [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: What's my personality?                                  │
│                                                                  │
│          ● ● ●───────○ ○ ○ ○ ○ ○                                │
│                                                                  │
│                   [Agent Avatar + Name]                          │
│                                                                  │
│        ┌──────────────────────┐  ┌──────────────────────┐       │
│        │ your personal        │  │  says what you're    │       │
│        │   cheerleader        │  │    thinking          │       │
│        └──────────────────────┘  └──────────────────────┘       │
│                                                                  │
│        ┌──────────────────────┐  ┌──────────────────────┐       │
│        │  runs on espresso    │  │  down every rabbit   │       │
│        │                      │  │       hole           │       │
│        └──────────────────────┘  └──────────────────────┘       │
│                                                                  │
│        [Back]                              [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: Pick my emoji!                                          │
│          This'll be my signature look                            │
│                                                                  │
│          ● ● ● ●─────○ ○ ○ ○ ○                                  │
│                                                                  │
│              [Agent Avatar with glasses + Name]                  │
│                                                                  │
│        ┌───┬───┬───┬───┬───┬───┬───┬───┐                        │
│        │ 🌙│ ⚡│ 🔥│ 💎│ 🌊│ 🎯│ 🦊│ 🐙│                        │
│        └───┴───┴───┴───┴───┴───┴───┴───┘                        │
│        ┌───┬───┬───┬───┬───┬───┬───┬───┐                        │
│        │ 🦋│ 🐋│ 🦉│ 🐸│ 🚀│ 🎮│ 🎸│ 🎨│                        │
│        └───┴───┴───┴───┴───┴───┴───┴───┘                        │
│        ┌───┬───┬───┬───┬───┬───┬───┬───┐                        │
│        │ 🔮│ 🧠│ ✨│ 🪐│ 🌸│ 🍀│ ☀️│ 🌈│                        │
│        └───┴───┴───┴───┴───┴───┴───┴───┘                        │
│                                                                  │
│        [Back]                              [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: Any more lore for me?                                   │
│          Optional — give me some backstory or special            │
│          instructions                                            │
│                                                                  │
│          ● ● ● ● ●───○ ○ ○ ○                                    │
│                                                                  │
│          [Agent Avatar with emoji + Name 🍀]                     │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │ e.g., You're a time-traveling librarian     │          │
│        │ who speaks in metaphors...                  │          │
│        │                                             │          │
│        │                                             │          │
│        │                                             │          │
│        └─────────────────────────────────────────────┘          │
│                                                       0/500      │
│                                                                  │
│        [Back]                     [Skip]   [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 6: Choose my brain!                                        │
│          Which Claude model should power me?                     │
│                                                                  │
│          ● ● ● ● ● ●──○ ○ ○                                     │
│                                                                  │
│          [Agent Avatar with emoji + Name 🍀]                     │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │  Claude Opus 4.6                       $$$  │          │
│        │  Most capable                               │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │  Claude Sonnet 4.5                      $$  │          │
│        │  Balanced                                   │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│        ┌═════════════════════════════════════════════┐          │
│        ║  Claude Haiku 4.5                        $  ║ ← SELECTED
│        ║  Fast & affordable                          ║          │
│        └═════════════════════════════════════════════┘          │
│                                                                  │
│        You can change this later in settings.                   │
│                                                                  │
│        [Back]                              [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 7: Connect my tools!                                       │
│          These let me work with your favorite services           │
│                                                                  │
│          ● ● ● ● ● ● ●─○ ○                                      │
│                                                                  │
│          [Agent Avatar with emoji + Name 🍀]                     │
│                                                                  │
│        0/3 tools connected, connect another!                     │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │  📧  Gmail                     [Connect] ↗  │          │
│        │      Read and send emails                   │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │  🐙  GitHub                    [Connect] ↗  │          │
│        │      Manage repos and issues                │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│        ┌─────────────────────────────────────────────┐          │
│        │  💬  Slack                     [Connect] ↗  │          │
│        │      Send and read messages                 │          │
│        └─────────────────────────────────────────────┘          │
│                                                                  │
│        I support 1000+ more tools — just ask me in the           │
│        chat later                                                │
│                                                                  │
│        [Back]                     [Skip]   [Continue]            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 8: Chat with me on Telegram!                               │
│          Messages sync with this dashboard                       │
│                                                                  │
│          ● ● ● ● ● ● ● ●─○                                      │
│                                                                  │
│          [Agent Avatar with emoji + Name 🍀]                     │
│                                                                  │
│                                                                  │
│                   ┌──────────────────────┐                       │
│                   │  💬 Link Telegram    │                       │
│                   └──────────────────────┘                       │
│                                                                  │
│                                                                  │
│                                                                  │
│                                                                  │
│        [Back]                                    [Skip]          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 9: All set! (completion)                                   │
│                                                                  │
│          ● ● ● ● ● ● ● ● ●                                      │
│                                                                  │
│          [Agent Avatar with emoji + Name 🍀]                     │
│                                                                  │
│                                                                  │
│               🎉 Ready to go!                                    │
│                                                                  │
│        I'm analyzing your WhatsApp history to learn              │
│        your contacts and communication style.                    │
│        This takes 2-5 minutes.                                   │
│                                                                  │
│        I'll send you a summary when ready!                       │
│                                                                  │
│                                                                  │
│                      [Go to Dashboard]                           │
└─────────────────────────────────────────────────────────────────┘
```

**What gets stored:**

| Setting | Where | Used for |
|---|---|---|
| Agent name | `clients.agent_name` | Message signatures, UI display |
| Writing style | `clients.writing_style` enum | SOUL.md tone preset (casual/formal/friendly/creative) |
| Personality | `clients.personality` enum | SOUL.md behavior preset (cheerleader/direct/energetic/curious) |
| Emoji | `clients.agent_emoji` | UI avatar, message signatures |
| Backstory/lore | `clients.agent_backstory` TEXT | Appended to SOUL.md custom instructions |
| Model preference | `clients.default_model` | Model routing for this client (opus/sonnet/haiku) |
| Connected tools | `client_integrations` table | OAuth tokens for Gmail/GitHub/Slack/etc |
| Chat platform | `clients.chat_platform` enum | WhatsApp vs Telegram gateway routing |

**Implementation notes:**

- **Progressive disclosure:** Each step reveals only what's needed. Back button allows editing.
- **Smart defaults:** Haiku selected by default (cost-conscious). Personality = "says what you're thinking" (balanced for RE agents).
- **Skip-friendly:** Steps 5, 7, 8 are optional. User can complete in 60 seconds (name → style → personality → emoji → done).
- **Visual continuity:** Agent avatar evolves through steps (adds emoji, glasses based on selections).
- **Triggers history analysis:** After step 9, triggers `onboarding-analysis` Trigger.dev task (see next section).

**Why this flow:**

1. **Personalization from day 1** — Fintool-style onboarding adapted for B2C. Agent feels like "your" agent.
2. **Model cost control** — Explicit model selection educates users on cost vs capability trade-offs.
3. **OAuth consent clarity** — Tools shown upfront, not hidden. User knows what they're connecting before OAuth redirect.
4. **Reduces support burden** — Self-serve personality configuration vs hardcoded "one size fits all" tone.

### Onboarding Analysis

**What it does:** After WhatsApp pairing, analyzes the user's recent chat history to pre-populate the CRM. Solves the cold-start problem — the CRM starts with data, not empty.

**Inspired by Fintool:** Fintool reads user-uploaded artifacts (investment memos, Excel models, email threads) to learn investment style, identify companies they cover, and understand thesis structure. We adapt the same principle to a different data source: WhatsApp chat history is already flowing through Baileys (`syncFullHistory: true`), so we analyze it automatically — zero user effort.

**Trigger.dev task: `onboarding-analysis`**

```typescript
import { task } from "@trigger.dev/sdk/v3";
import { generateText } from "ai";

export const onboardingAnalysis = task({
  id: "onboarding-analysis",
  retry: { maxAttempts: 2 },
  run: async (payload: { clientId: string }) => {
    // 1. Fetch last 30 days of messages (already synced by Baileys)
    const messages = await db.getRecentMessages(payload.clientId, {
      limit: 2000,  // cap to control cost
      daysBack: 30,
    });

    if (messages.length < 20) {
      // Sparse history — fall back to generic onboarding
      await db.updateClient(payload.clientId, { onboarding_type: 'generic' });
      return { type: 'generic', reason: 'insufficient_history' };
    }

    // 2. Batch messages by chat JID (one batch per conversation thread)
    const chatThreads = groupByChatJid(messages);

    // 3. Extract contacts + relationships (batch 10-20 msgs per Haiku call)
    const extractedContacts: ExtractedContact[] = [];
    for (const [jid, threadMsgs] of Object.entries(chatThreads)) {
      const batches = chunkArray(threadMsgs, 15);
      for (const batch of batches) {
        const result = await generateText({
          model: registry.languageModel("anthropic:claude-haiku-4-5"),
          system: ONBOARDING_EXTRACTION_PROMPT, // see below
          prompt: formatMessagesForExtraction(batch),
        });
        extractedContacts.push(...parseExtractionResult(result.text));
      }
    }

    // 4. Deduplicate + merge contacts (same name/phone across threads)
    const mergedContacts = deduplicateContacts(extractedContacts);

    // 5. Detect active deals (property mentions + negotiation language)
    const detectedDeals = await detectDeals(payload.clientId, mergedContacts, messages);

    // 6. Analyze communication style (user's OWN messages only)
    const userMessages = messages.filter(m => m.fromMe);
    const styleProfile = await generateText({
      model: registry.languageModel("anthropic:claude-haiku-4-5"),
      system: STYLE_ANALYSIS_PROMPT,
      prompt: formatMessagesForStyleAnalysis(userMessages.slice(0, 100)),
    });

    // 7. Analyze working patterns (no LLM needed — just timestamps)
    const workingPatterns = analyzeTimestamps(userMessages);

    // 8. Store results in staging (NOT committed to CRM yet)
    await db.createOnboardingResults(payload.clientId, {
      contacts: mergedContacts,
      deals: detectedDeals,
      styleProfile: styleProfile.text,
      workingPatterns,
      messageCount: messages.length,
      status: 'pending_confirmation', // user must confirm
    });

    // 9. Mark client ready for personalized first message
    await db.updateClient(payload.clientId, { onboarding_type: 'analyzed' });

    return {
      type: 'analyzed',
      contactCount: mergedContacts.length,
      dealCount: detectedDeals.length,
    };
  },
});
```

**What gets extracted per chat thread:**

| Category | What | Method |
|---|---|---|
| **Contacts** | Names, phone numbers (from JID), relationship type (buyer/seller/referral/colleague) | Haiku extraction per batch |
| **Active deals** | Properties being discussed, rough stage, key dates, price points | Scan for addresses, viewing mentions, negotiation language |
| **Communication style** | Formal vs casual, language mix (English/Singlish/Chinese), emoji usage, sign-off patterns | Haiku analysis of user's own messages (fromMe: true) |
| **Working patterns** | Active hours, response speed, busiest days | Timestamp analysis (no LLM) |
| **Relationship signals** | Who's hot (recent + frequent), who's cold (no reply in 14+ days), ghosted threads | Recency + frequency heuristics |

**Cost:** 30 days of history for an active agent = ~500-2000 messages = 25-100 Haiku API calls. At Haiku pricing (~$0.25/MTok input), ~$0.50-2.00 per onboarding. One-time cost per client.

**Key design decisions:**
- **Nothing auto-commits.** Extracted contacts and deals go to a staging table (`onboarding_results`). User must confirm via WhatsApp before data enters the CRM. This builds trust AND catches extraction errors.
- **Per-client queue reuse.** Onboarding analysis runs in the same `agent-conversation` queue (concurrency: 1) so it doesn't interleave with real-time messages arriving during setup.
- **Style profile → `ai_memory`.** After user confirms, style analysis is written to `ai_memory` as `key: "style"` and `key: "working_patterns"`. Same pattern as self-evolving memory, just seeded from history.
- **Graceful degradation.** If history sync returns <20 messages (new phone, cleared chats), skip analysis and use generic first message. Don't show an empty summary.

### Connected Services (Composio)

**What it does:** During or after onboarding, prompt the user to connect external services for richer context. WhatsApp history is the baseline (free, automatic). Connected services are the upgrade.

**Three tiers of data sources:**

```
TIER 1: WhatsApp history (automatic, everyone gets this)
─────────────────────────────────────────────────────────
• Baileys syncFullHistory — already flowing
• Zero user effort
• Extracts: contacts, deals, style, patterns

TIER 2: Connected services (optional, prompted during onboarding)
────────────────────────────────────────────────────────────────
• Google Calendar → upcoming viewings, client meetings, open houses
• Gmail → email threads with clients, property portal notifications
• Google Contacts → full contact list with phone/email
• Auth via Composio (managed OAuth flows + API wrappers)

TIER 3: Ongoing connected monitoring (future, post-MVP)
───────────────────────────────────────────────────────
• Property portals (PropertyGuru, 99.co) → Browserbase browser sessions with per-user auth
• Notion/OneNote → client notes, property notes
• Continuous sync, not just onboarding
```

**Why Composio:** Managed OAuth flows + pre-built API integrations. Works with Vercel AI SDK as tool providers. No need to build and maintain OAuth redirect handling, token refresh, and API wrappers for each service. Composio provides these as ready-made tool definitions that slot into our existing `generateText` + tools pattern.

**Implementation (MVP: Tier 1 only, Tier 2 as fast-follow):**

```
Onboarding page or WhatsApp prompt:
"Want to connect your Google Calendar?
I can find upcoming viewings and meetings."
    │
    └── User taps link → Composio OAuth flow
        └── Callback stores tokens in Supabase (scoped to client_id)
        └── Enrichment task triggered:
            • Fetch next 30 days of calendar events
            • Match event attendees to extracted WhatsApp contacts
            • Add viewing/meeting dates to detected deals
            • Store as additional onboarding context
```

**Open questions for Composio integration:**
- [ ] Composio vs direct OAuth (Composio adds a dependency; direct OAuth is more work but no middleman)
- [ ] Which services first (Google Calendar is highest-value for RE — viewings, meetings)
- [ ] Token storage and refresh strategy (Composio handles refresh, but where do we store the connection config?)
- [ ] Privacy messaging (user needs to understand what data we access and why)

---

## Infrastructure & Cost

### MVP (1-10 clients)

| Component | Where | Cost |
|---|---|---|
| Gateway | DigitalOcean 2-4GB droplet | $12-24/mo |
| Next.js app (Dashboard + CRUD) | Vercel free tier | $0 |
| Trigger.dev (agent tasks, cron) | Free tier (50K runs/mo) | $0 |
| Supabase | Free tier (500MB DB, 50K rows) | $0 |
| LLM API (Claude/OpenRouter) | ~$5-20/mo per active client | $5-200/mo |
| Document extraction (Gemini) | Included in LLM costs (classification + structured output) | $0 |
| Document extraction (ExtendAI) | ~$0.10-0.50/doc, complex schemas only | $0-50/mo |
| Vercel Sandbox (artifacts) | Included in Vercel plan | $0 |
| Browserbase (browser research) | Developer plan | $20/mo (100 browser hrs) |
| Territory scraper (Browserbase + Perplexity) | ~$1.37/night per active client | $0-41/mo |
| Domain + DNS | Cloudflare | $10/yr |
| **Total** | | **~$45-360/mo** |

### Growth (10-50 clients)

| Component | Where | Cost |
|---|---|---|
| Gateway | DigitalOcean 4-8GB droplet | $24-48/mo |
| Next.js app | Vercel Pro | $20/mo |
| Trigger.dev | Pro ($30/mo + usage) | $30-60/mo |
| Supabase | Pro (8GB DB) | $25/mo |
| LLM API | ~$5-20/mo per client (less with model routing) | $50-500/mo |
| Document extraction (ExtendAI) | ~$5-25/mo per active client (50 docs/mo avg) | $50-500/mo |
| Vercel Sandbox (artifacts) | Included in Vercel Pro | $0 |
| Browserbase (browser research) | Startup plan | $100-200/mo |
| Territory scraper (Browserbase + Perplexity) | ~$41/mo per client with territories | $0-410/mo |
| **Total** | | **~$300-1,770/mo** |

At $149/mo per client with 50 clients = $7,450 MRR. Infra cost = ~$1,770. 76%+ gross margin. Territory scraper is an upsell — not all clients need it, and it pays for itself 50x over (replaces 40 hrs/week of manual prospecting).

**Cost optimization lever:** Route simple queries to Kimi K2.5 ($0.60/MTok input vs Claude's $3.00) or DeepSeek V3.2 ($0.25/MTok) via OpenRouter. Keep Claude Sonnet for complex reasoning only. Potential 70-90% reduction in LLM costs.

---

## Build Order

| Phase | What | Why first |
|---|---|---|
| 1 | Baileys gateway + Next.js app + **Trigger.dev setup** + Vercel AI SDK + basic CRM tools + **SOUL.md personality** | End-to-end: Tier 1 (read all) + Tier 2 (user chat) working. Trigger.dev from day 1 — agent-conversation task with per-client queue. SOUL.md defines personality from day 1. |
| 2 | Supabase schema (including `conversation_summaries`, `recurring_tasks`, `domain_knowledge_index`, `onboarding_results`, pgvector-ready `ai_memory`) + CRM extraction pipeline (Tier 1) + **domain knowledge files in Supabase Storage** | AI passively builds CRM from chat history. Schema includes all v2.4 tables from day 1. Domain knowledge files deployed to Storage. Simple extraction stays on Vercel (Haiku, <10s). |
| 3 | Conversational CRM tools + `update_memory` + `recall_memory` + **session boundaries** + **context compaction** (Tier 2) | User can query/update CRM via WhatsApp. Agent starts building memory. Session segmentation + compaction ensure conversation history stays bounded. |
| 4 | Tier 3 approval flow with **Trigger.dev waitpoints** (draft → preview → approve → send) | Outbound messaging with guardrails. Waitpoints = task pauses until user approves, zero compute cost. |
| 5 | **Trigger.dev scheduled tasks** (morning briefings, follow-up nudges, scheduled sends) + `manage_recurring_task` tool + **heartbeat personality** (from SOUL.md) | Proactive value — the magic moment. Agent can self-schedule recurring reminders. Heartbeat tone defined in SOUL.md. |
| 6 | Dashboard pages (agent view, read-only, pending messages view) + **Trigger.dev Realtime** for live task status | Agents can see what the AI is tracking. Realtime hooks show agent task progress. |
| 7 | **Document system** — `document-processing` Trigger.dev task, Gemini classification + extraction, 8 platform tags (floor_plan, otp, ta, valuation, commission, brochure, receipt, other), document tools (`process_document`, `search_documents`), `documents` + `document_extractions` tables | Inbound extraction — users forward docs via WhatsApp, AI classifies + extracts structured data + links to CRM. Reuses Sunder pipeline. Gemini-only for MVP (free). |
| 8 | **Self-serve schema builder** — `create_extraction_schema` + `update_extraction_schema` tools, `extraction_schemas` table, conversational flow for defining custom doc types | Users teach AI new document types via conversation. ExtendAI integration for complex schemas. |
| 9 | Sandbox / Creator path (`generate_artifact` + Vercel Sandbox), triggered as **Trigger.dev subtask** + Browserbase integration (`browse_property_site`, Contexts API, Live View auth flow) | PDF reports, charts, property videos. Sandbox calls wrapped in durable task for retries. Browser research with per-user auth for property portals. |
| 9.5 | **JIT UI Phase 1:** `ask_user` tool (WhatsApp polls for scoping), poll response capture via Baileys `messages.upsert` → waitpoint completion. **Phase 2:** `preview_specs` table, `/preview/[id]` Next.js route, first 3 preview components (ComparisonCard, ReportOutline, PipelineView), `generate_preview` tool. | Ambiguity resolution before artifact generation. Phase 1 (polls) is cheap and immediately useful — no web preview needed. Phase 2 adds visual preview for complex outputs. Depends on Phase 9 (sandbox/creator path) because previews feed into final artifact generation. |
| 10 | Onboarding flow + **onboarding-analysis task** (history analysis → pre-populated CRM) + admin dashboard + **personalized first-message** | Ready for real users. Onboarding analyzes WhatsApp history, presents summary for confirmation. First-message personality defined in SOUL.md. Cold-start problem solved. |
| 11 | Stripe billing | Ready to charge |
| 12 | **Semantic memory upgrade** (pgvector embeddings on ai_memory writes) + **sub-agent spawning** (parallel research via Trigger.dev triggerAndWait) | Scale features. Flip pgvector switch when any client hits 100 memory entries. Sub-agents for multi-property comparisons. |

---

## Open Questions (Future Sessions)

### Implementation details
- [ ] Exact tool schemas (full zod definitions, validation, error messages)
- [x] ~~System prompt engineering (RE personality, domain knowledge chunks)~~ → **Solved: SOUL.md defines 4-layer prompt construction. Personality, domain knowledge, heartbeat tone, permission awareness all documented.**
- [x] ~~Conversation history management (how much context per request, summarization strategy)~~ → **Solved: Session boundaries (idle-based segmentation at 2h/8h) + context compaction (50-msg chunks → Haiku summaries → conversation_summaries table). See Session Management section.**
- [x] ~~Media handling (voice notes → transcription, photos → vision, documents → parsing)~~ → **Partially solved: Document parsing fully designed (v2.8 Document System — Gemini classification + structured extraction + self-serve schema builder). Voice notes and photos still TBD.**
- [ ] What happens when model hallucinates a tool call
- [x] ~~Vercel serverless concurrency model~~ → **Solved: Trigger.dev per-client queues (concurrency: 1)**
- [ ] Trigger.dev task definitions (exact task IDs, payloads, retry policies, queue configs)
- [ ] Trigger.dev Realtime integration with gateway (how gateway receives streamed responses)
- [x] ~~Task cancellation flow (how user cancels running agent tasks)~~ → **Solved: Gateway regex detects cancel intent → /api/cancel → runs.cancel() + queue flush + waitpoint cleanup. Active runs tracked in `active_agent_runs` table. See Task Cancellation section.**
- [x] ~~Tier 1 extraction idempotency (duplicate message handling)~~ → **Solved: Two-level dedup — gateway LRU cache (fast) + `processed_messages` Supabase table (durable). Insert-before-extract claim pattern with ON CONFLICT. See Tier 1 Extraction Idempotency section.**

### Sandbox
- [x] ~~E2B vs Northflank~~ → **Resolved: Neither. Vercel Sandbox for artifacts (ephemeral code execution). Browserbase for browser sessions (persistent per-user auth).**
- [ ] Pre-installed dependency list and versioning
- [x] ~~Sandbox timeout and error handling~~ → **Solved: Trigger.dev wraps sandbox calls with automatic retries and checkpointing**
- [ ] File size limits for generated artifacts

### Model routing
- [ ] When to introduce cheaper models (Kimi, DeepSeek) for simple queries
- [ ] Thresholds for routing (what makes a query "simple" vs "complex")
- [ ] Eval framework to validate model quality when switching providers

### Integrations
- [ ] Which enrichment APIs to integrate first (and fallback chains)
- [x] ~~Google Calendar read access (Composio or direct OAuth)~~ → **Decided: Composio for managed OAuth. See Connected Services section. Implementation details TBD.**
- [x] ~~Gmail read access~~ → **Decided: Composio. Tier 2 connected service, prompted during onboarding.**
- [ ] Property data sources (MLS, public records)
- [ ] Composio vs direct OAuth (final decision — Composio adds dependency but saves OAuth/refresh implementation)
- [ ] Composio token storage and refresh strategy
- [ ] Privacy messaging for connected services (what data we access and why)

### Operations
- [ ] Baileys reconnection edge cases and session recovery — **Partially mitigated: `processed_messages` dedup table prevents duplicate extraction on reconnect replay. Session auth state persisted to disk. Remaining: graceful reconnection backoff, message ordering guarantees during replay.**
- [x] ~~Monitoring and alerting~~ → **Partially solved: Trigger.dev built-in observability for all agent tasks. Still need gateway health monitoring (separate).**
- [x] ~~Logging strategy~~ → **Partially solved: Trigger.dev provides full tracing per task run. Gateway needs separate logging.**
- [ ] Backup strategy for Supabase

### JIT UI / Ambiguity Resolution
- [ ] Poll response timing — what if user doesn't answer for hours? Remind? Wait silently? Define timeout behavior.
- [ ] Multiple scoping rounds — is one round of polls enough, or might the AI need 2-3 rounds for very ambiguous requests? Cap at 2 to avoid survey fatigue?
- [ ] Preview link in group chats — Tier 2 is fine (user's own chat). Future scenarios where previews might be shared?
- [ ] Offline/slow connection fallback — if user can't load preview page, fall back to text description. Add "Can't load? Reply 'describe' and I'll explain it here."
- [ ] Learning from confirmations — over time, AI should learn user preferences (this agent always wants school info in comparisons) and skip scoping questions it already knows the answer to. Store in `ai_memory`.
- [ ] Preview component Zod schemas — define prop schemas for each preview component (steal Tambo pattern even without Tambo dependency).

### Future features (v2+)
- [ ] Dashboard editing (not just read-only)
- [ ] Dashboard approve/reject pending messages (currently WhatsApp-only approval)
- [ ] Web chat interface via Vercel AI SDK `useChat()` hooks
- [ ] AI-owned email via AgentMail
- [ ] WhatsApp Business API migration (official, at scale)
- [ ] Multi-agent (team accounts)
- [ ] Voice notes → transcription → action
- [ ] **Full-duplex voice conversations** — NVIDIA PersonaPlex-7B changes the economics of voice AI entirely. The traditional pipeline (ASR → LLM → TTS) is three models stitched together with latency at every seam. OpenAI charges $0.06/min input, $0.24/min output for Realtime API. Gemini Live bills 25 tokens/second of audio. Every startup building voice agents is hemorrhaging cash on per-minute fees. PersonaPlex replaces that entire pipeline with one 7B model. Single A100. Open weights, MIT license, commercial use. Response latency: 170ms turn-taking, 240ms interruptions. Scores higher on dialog naturalness than Gemini (2.95 vs 2.80 MOS). Full-duplex — listens and talks simultaneously, no turn-taking pauses. 330K downloads in first month. NVIDIA's play: they don't charge for the model because they sell the GPU. Every company that self-hosts instead of paying per-minute API fees is another A100/H100 sale. Voice AI margin is migrating from application layer to hardware layer. **Implication for us:** self-hosted PersonaPlex on a single GPU could give our agents real-time voice conversations at near-zero marginal cost — no per-minute API dependency. Monitor for when this becomes practical at our scale. Sources: [HuggingFace](https://huggingface.co/nvidia/personaplex-7b-v1), [announcement](https://x.com/HuggingModels/status/2022995332058251548).
- [ ] Allowlist/blocklist: user selects which chats AI should extract from (vs. all)
- [ ] Batch approval: approve multiple scheduled messages at once
- [x] ~~Skill shadowing (platform defaults → per-client overrides, Fintool pattern)~~ → **Solved: Skills Filesystem Architecture (v2.5) + Domain Knowledge Architecture (v2.4). Both use files in Supabase Storage with SQL index tables. Shadowing via DISTINCT ON (slug) ORDER BY client_id DESC NULLS LAST. Skills have two mount points: platform (read-only, we ship) + user (read-write, agent creates via `manage_skill` tool). No org/shared mount (B2C).**
- [ ] Sleep-time memory consolidation (Letta pattern)

### Future features (from OpenClaw gap analysis)
- [ ] **Sub-agent spawning** — parent agent delegates parallel research tasks via Trigger.dev `triggerAndWait`. Pattern: `agent-conversation` spawns `property-research` + `comps-lookup` subtasks, both run in parallel, parent synthesizes results. Build when: agent tool loops regularly exceed 5 steps or users request multi-property comparisons frequently.
- [x] ~~**Browser automation with semantic snapshots**~~ → **Promoted to core architecture: Browserbase + Stagehand for browser research. See Browser Research (Browserbase) section. CDP-based (accessibility tree, not screenshots). Per-user auth via Contexts API + Live View.**
- [ ] **Identity links** (cross-channel session merge) — when adding dashboard web chat (`useChat()`), link WhatsApp identity to dashboard identity so AI knows it's the same agent. Pattern from OpenClaw: `identityLinks: { agent_abc: ["whatsapp:6591234567", "web:user_abc"] }`.
- [ ] **Channel plugin architecture** — abstract gateway into plugin model when adding channels beyond WhatsApp. Each channel = one adapter normalizing to common message format. Not needed while WhatsApp-only.
- [ ] **Configurable heartbeat timing** — AI learns agent's active hours from message patterns and adapts briefing/nudge times. Store preferred times in `ai_memory` under `preferences` key. Currently hardcoded to 8am/6pm SGT.
- [ ] **Autonomous goal board (Dorabot pattern)** — Agent proposes actions on its own, user approves, agent executes. Stolen from Dorabot (`github.com/suitedaces/dorabot`, by @ishanxnagpal / Founding Engineer at Fintool.com). The UX: agent heartbeat fires → reads context (stale deals, upcoming meetings, lead activity) → proposes goals ("Follow up with Sarah at PropNex — last contact 12 days ago", "Draft comparison report for the Tangs — they viewed 3 units this week") → goals land in "Proposed" state → user drags to "Approved" via dashboard or replies "yes" in WhatsApp → agent executes autonomously → reports completion. Four states: **Proposed → Approved → In Progress → Done**. This is the "zero-click CRM" interaction model — the agent does the thinking and proposing, user just approves outputs. Implementation: `proposed_actions` table (id, client_id, action_type, description, context_json, status enum, proposed_at, approved_at, completed_at, result_json). Heartbeat cron generates proposals via `propose_action` tool. Dashboard shows Kanban board. WhatsApp shows numbered list ("I have 3 suggestions for today: 1. Follow up with... 2. Draft report for... Reply with numbers to approve"). Approved items become Trigger.dev tasks. **Key difference from current nudge engine:** current nudges are notifications the user must act on manually. This pattern makes the agent the actor — user just approves/rejects. Build when: nudge engine is live and users consistently act on suggestions (validation that AI judgment is trusted). Related: Dorabot's LinkedIn article "How to Make Your AI Agent Its Own Forward-Deployed Engineer" (Palantir FDE analogy — agent learns domain, proposes work, becomes indispensable). See `OSS-CLAW-ALTERNATIVES.md` for full Dorabot analysis.

---

## Feature Requests — Build or DIY

Here's the deal: we checked. For any feature you want, we can either **build it for you** or you can **DIY it yourself** using the skills/tools system. Your call.

But if you want us to build it — **vote on it.**

### How It Works

1. **Submit** a feature request (WhatsApp or dashboard)
2. It lands on the **public leaderboard** — every user can see and upvote
3. **Most voted idea gets shipped every week.** No exceptions.

That's it. Simple UI, one leaderboard, community decides what gets built next. If your idea is niche and nobody votes for it, you can still DIY it with the skill builder. If it's a banger that everyone wants, we'll ship it for you.

> "We can either build it for you, or you can just DIY. Add it to the leaderboard. Most highly voted idea WILL get shipped every week."

### Implementation (Lightweight)

- **Table:** `feature_requests` (id, client_id, title, description, vote_count, status enum [submitted, voting, building, shipped, diy], created_at, shipped_at)
- **Table:** `feature_votes` (id, feature_id, client_id, unique constraint on feature+client)
- **WhatsApp command:** "feature request: [idea]" → creates entry, returns leaderboard link
- **Dashboard page:** `/features` — list sorted by votes, submit new, upvote existing
- **Weekly cron:** Auto-tag top-voted as "building", notify submitter + voters

---

## Relationship to Other Docs

**ARCHITECTURE.md (v1.1)** remains the reference for:
- **Domain logic:** Contact types, deal stages, interaction model, follow-up engine
- **Database schema:** Full SQL with RLS policies (Part 4)
- **Business model:** Pricing tiers, cost structure, margin analysis
- **Account access phasing:** MVP (read-only) → v2 (AI email) → v3 (full autonomy)

**PRODUCT-VISION.md** is the source of truth for:
- **What we're building:** Problem statement, thesis, target users
- **Feature roadmap:** Full 38-feature list across 6 phases with MVP cut
- **Validation hypotheses:** What to test and kill signals

**SOUL.md** is the source of truth for:
- **Agent personality:** Identity, tone, behavior rules, WhatsApp voice, Singapore English awareness
- **Heartbeat personality:** Morning briefing, evening nudge, weekly stale review, milestone alert tone and structure
- **Memory instructions:** What to remember, when to write, key categories
- **Permission awareness:** How the agent understands and respects Tier 1/2/3
- **Domain knowledge reference:** Contact types, deal stages, interaction types, SG RE specifics

This doc (v3.1) is the source of truth for:
- **How we build it:** Architecture, tech stack, deployment model
- **Deployment model:** Centralized, not per-client VPS
- **Runtime:** OAI Agents SDK + Vercel AI SDK adapter + Next.js, model-agnostic
- **Durable execution:** Trigger.dev for agent tasks, cron, queues, waitpoints
- **Tool calling:** OAI Agents SDK native tools (Zod schemas, works with any provider via adapter)
- **Session management:** Idle-based segmentation + context compaction
- **Memory search:** Keyword (MVP) → FTS (v1.5) → hybrid vector+FTS (v2) migration path
- **Agent self-scheduling:** `recurring_tasks` table + `manage_recurring_task` tool
- **Domain knowledge architecture:** Files in Supabase Storage + `domain_knowledge_index` SQL index. Keyword-based selective loading. Shadowing-ready for per-client overrides.
- **Skills filesystem architecture:** Two mount points (platform read-only + user read-write) in Supabase Storage + `skills_index` SQL index. Agent creates user skills via `manage_skill` tool. Follows Fintool's mount-point pattern adapted for B2C.
- **Onboarding:** History analysis (WhatsApp chat → pre-populated CRM) + connected services (Composio for Google Calendar, Gmail)
- **Infrastructure:** Gateway on DigitalOcean, Vercel for frontend/CRUD, Trigger.dev for agent tasks
- **Why Trigger.dev:** See Fintool article on durable execution (03_Resources/Industry Intel/Fintool - Lessons Building AI Agents for Financial Services.md)
- **JIT UI for ambiguity resolution:** WhatsApp polls for scoping + web preview pages for visual confirmation. Two tools (`ask_user`, `generate_preview`), one table (`preview_specs`), Next.js preview route. Inspired by Fintool's AskUserQuestion pattern adapted for WhatsApp.
- **Fintool gap analysis:** Domain knowledge scaling + onboarding patterns adapted from Fintool articles (03_Resources/Industry Intel/)
- **OpenClaw gap analysis:** See ARCHITECTURE-v2-addendum-openclaw-gaps.md for detailed implementation reference (code samples, SQL, full rationale)
