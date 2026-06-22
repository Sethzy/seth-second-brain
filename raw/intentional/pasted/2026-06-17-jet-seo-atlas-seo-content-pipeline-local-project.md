---
type: raw_capture
source_type: pasted
title: "jet-seo Atlas SEO content pipeline local project"
url: "file:///Users/sethlim/Documents/jet-seo/"
collected_at: 2026-06-17T07:53:45Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# jet-seo Atlas SEO content pipeline local project

Source: file:///Users/sethlim/Documents/jet-seo/

## Capture Text

# jet-seo local project snapshot

Source directory: /Users/sethlim/Documents/jet-seo/

## CLAUDE.md

# Atlas SEO Content Pipeline

Ahrefs-driven SEO content workflow for Atlas. Fully machine-executable.

## Quick Start

To run the workflow, provide both files as context:

```
@WORKFLOW.md @MEMORY_STATE.md go
```

## Project Structure

```
.claude/agents/skills/atlas-seo.md   # SEO content generation skill (Step 8)
WORKFLOW.md                           # Master runbook (11 steps, 4 phases)
MEMORY_STATE.md                       # Execution checkpoint (resume state)
docs/marketing/data/                  # CSV trackers (8 files)
docs/marketing/keywords/briefs/       # Content brief files
```

## Skills

| Skill | Location | Used At |
|-------|----------|---------|
| `/atlas-seo` | `.claude/agents/skills/atlas-seo.md` | Step 8: Generate MDX posts |
| `/content-strategy` | (external) | Step A.0: Seed keyword discovery |
| `/programmatic-seo` | (external) | Step 9: Internal linking |

## Workflow Phases

- **Phase A (Research):** Discover seeds, Ahrefs validation, SERP analysis
- **Phase B (Prioritization):** Score, cluster, approve/defer keywords
- **Phase C (Briefs):** SERP analysis, outlines, internal link mapping
- **Phase D (Production):** Generate MDX, add links, validate, commit

One human handoff: Step A.3 (Ahrefs export). Everything else is autonomous.

## State Management

- `MEMORY_STATE.md` is ground truth for workflow position
- CSVs in `docs/marketing/data/` are ground truth for item-level state
- Always read both `WORKFLOW.md` and `MEMORY_STATE.md` before executing any step


## WORKFLOW.md

# Atlas SEO Content Workflow

Machine-executable runbook for the Ahrefs-driven content pipeline. Claude Code reads this document and `MEMORY_STATE.md` — nothing else is needed to execute or resume the full workflow.

---

## 0. How to Execute This Workflow

### 0.1 Cold Start Protocol

```
1. Read this document (WORKFLOW.md) in full.
2. Check if docs/marketing/MEMORY_STATE.md exists.
   - If YES: Read it. Resume from the step indicated in `next_step`.
   - If NO: Begin at Phase A, Step A.0. Create MEMORY_STATE.md per Section 10.
3. Execute steps sequentially. Never skip ahead.
```

### 0.2 Execution Model — Batch-Then-Advance

Each numbered step operates on ALL eligible items before the next step begins. A step is complete ONLY when its completion condition is met for EVERY item in scope. A phase gate blocks ALL steps in the next phase until ALL gate conditions are satisfied.

```
WRONG (per-item waterfall):
  Keyword A: Research → Prioritize → Brief → Draft → Publish
  Keyword B: Research → Prioritize → Brief → Draft → Publish

RIGHT (batch-then-advance):
  Step 5: Score, cluster, and approve ALL validated keywords
  --- GATE: All keywords scored, prioritized, clustered ---
  Step 6: SERP analysis + content strategy for ALL approved keywords
  Step 7: Create briefs + map links + register for ALL keywords
  --- GATE: All briefs created ---
  Step 8: Generate MDX posts for ALL briefs
  ...
```

### 0.3 Step Format Convention

Every step in Phases A–D follows this template:

```
### Step [X.N]: [Name]

**Executor:** AGENT | HUMAN
**Scope:** For every row in `[csv]` where `[column]` = `[value]`
**Action:**
  1. [Exact instruction]
  2. [Exact instruction]
**CSV Update:** Set `[column]` = `[value]` for each processed row
**Skill Call:** `/[skill]` with input: [spec] (or "None")
**Completion Condition:** All rows in `[csv]` where `[column]` was `[old]` now have `[column]` = `[new]`
**MEMORY_STATE Update:** Set `current_phase`, `current_step`, `items_completed`, `items_remaining`
```

For HUMAN steps, the Action section contains:
- **What to do:** Exact human instructions
- **What to produce:** Exact deliverable format
- **Where to put it:** Exact file path(s)
- **Signal completion:** How the user tells Claude Code they are done

### 0.4 Resume Protocol (after `/compact` or new session)

```
1. Read WORKFLOW.md
2. Read MEMORY_STATE.md
3. Check `step_status`:
   a. If `waiting_on_human`: Read `human_handoff` section. Re-present the
      instructions to the user. Ask if they have completed the task. If yes,
      verify deliverable exists and is valid, then proceed.
   b. If `in_progress`: Continue processing `items_remaining` for `current_step`.
   c. If `completed`: Proceed to `next_step`.
4. The `items_remaining` list tells you which items still need processing.
5. Continue from that point. Do NOT re-process items listed in `items_completed`.
6. CRITICAL: After autocompaction or session resume, you MUST re-read BOTH:
   - WORKFLOW.md (at minimum, the current step's section)
   - MEMORY_STATE.md (in full)
   Do NOT rely on conversation context alone. MEMORY_STATE.md is ground truth.
7. Check `items_remaining` in MEMORY_STATE.md to identify which specific
   keywords/briefs/posts still need processing. Do NOT re-process completed items.
```

### 0.5 Context Management Rules

- After completing each step: update MEMORY_STATE.md BEFORE starting the next step.
- If a step involves processing N items and context is running low mid-step: update MEMORY_STATE.md with partial progress (`items_completed` and `items_remaining`), then the resume protocol picks up the remaining items.
- Never hold workflow state in conversation context alone — MEMORY_STATE.md is always the ground truth.
- For long steps (Step 8): update MEMORY_STATE.md after EACH item, not just at step end.

### 0.7 Step Execution Preamble (MANDATORY)

Before executing ANY step, the agent MUST:

1. **Read WORKFLOW.md** for the current step's full specification.
2. **Read MEMORY_STATE.md** to verify current state, items completed, items remaining.
3. **State explicitly:** "I am now executing Step [X.N]: [Name]."
4. **Check Skill Call:** Read the step's "Skill Call" field. If a skill is specified,
   invoke it BEFORE doing any work. State: "This step requires skill /[name]. Invoking now."
   If "None", state: "This step requires no skill call."
5. **Check items in scope:** Verify which items need processing by reading the CSV or
   MEMORY_STATE.md items_remaining list. State the count: "N items to process."
6. **Remind self:** "I must not skip any part of this step. I must follow WORKFLOW.md
   precisely. I must update MEMORY_STATE.md after completing this step."

After completing ANY step, the agent MUST:

1. **Update MEMORY_STATE.md** with step results BEFORE starting the next step.
2. **Verify:** Re-read the updated MEMORY_STATE.md to confirm it was written correctly.
3. **State:** "Step [X.N] complete. Proceeding to Step [X.N+1]."

### 0.8 Self-Containment Rule

This document is self-contained. Do not read FEEDBACK.md, MARKETING.md, or any other documentation to execute this workflow. All required information is included inline. External files are inputs/outputs (CSVs, briefs, drafts, MDX files) — never procedure references.

---

## 1. System Overview

### 1.1 Architecture

```
Ahrefs CSVs → data/*.csv → keywords/briefs/ → content/blog/*.mdx
                  ↑                                            ↓
          MEMORY_STATE.md                              keyword-blog-mapping.csv
          (checkpoint)                                 (published tracking)
```

### 1.2 Data Flow

```
/content-strategy + web research (A.0)
        ↓
keyword-seeds.csv → keywords-validated.csv → serp-analysis.csv
   ↑ (also from                 ↓
   seeds.md)            content-briefs.csv → blog-posts.csv → keyword-blog-mapping.csv
                                                    ↑
                                            ahrefs-exports.csv (registry)
                                            competitor-keywords.csv

Exclusion loop: content/blog/*.mdx primaryKeywords → A.0 exclusion list → prevents duplicate seeds
```

### 1.3 File Map

| Directory | Purpose |
|-----------|---------|
| `WORKFLOW.md` | This document — master runbook (static, never modified during execution) |
| `MEMORY_STATE.md` | Execution checkpoint (written after every step) |
| `.claude/agents/skills/atlas-seo.md` | Atlas SEO content generation skill (invoked at Step 8) |
| `docs/marketing/data/` | 8 CSV trackers (structured data layer) |
| `docs/marketing/keywords/seeds.md` | Legacy seed keywords (read-only reference) |
| `docs/marketing/keywords/prioritized.md` | Legacy prioritized list (read-only reference) |
| `docs/marketing/keywords/briefs/` | Content brief files (`[NN]-[slug].md`) |
| `content/blog/` | Published MDX blog posts |
| `scripts/audit-blog-seo.ts` | SEO + AI writing audit script |
| `scripts/consolidate-ahrefs.ts` | Ahrefs CSV normalizer |

### 1.4 Prerequisites

- Ahrefs Starter account ($29/month, 100 credits). Note: Content Gap and Site Explorer Top Pages (full export) require Ahrefs Lite ($129/month) or higher. This workflow is designed to work within Starter plan limitations.
- Claude Code with skills: `/content-strategy`, `/atlas-seo`, `/programmatic-seo`
- Access to `docs/marketing/` and `content/blog/` directories
- Node.js for running audit scripts (`npm run audit:blog`)

### 1.5 Success Criteria

- All Ahrefs exports consolidated into centralized CSVs
- Keyword status visible at a glance (`not_started` → `ranking`)
- Brief creation references structured SERP data
- Content generation uses documented skill sequences
- Publishing validation catches all AI writing patterns
- Full workflow executable from cold start via this document + MEMORY_STATE.md

---

## 2. Data Layer

All structured data lives in CSVs at `docs/marketing/data/`. CSVs are the source of truth for workflow data. MDX frontmatter is the source of truth for published content. Steps reference CSV status columns to determine scope — if a step says "For every row where status = X", the CSV is the authoritative source.

### 2.1 keyword-seeds.csv

**File:** `docs/marketing/data/keyword-seeds.csv`

| Column | Type | Description |
|--------|------|-------------|
| `seed` | string | The seed keyword text |
| `funnel_stage` | enum | `BOFU` \| `MOFU` \| `TOFU` |
| `source` | string | Where this seed came from. Values: `seeds.md batch N` (legacy), `A.0 competitor gaps`, `A.0 audience pain points`, `A.0 emerging trends`, `A.0 long-tail questions`, `A.0 adjacent topics`, `A.0 content-strategy` (discovered in Step A.0) |
| `date_added` | date | YYYY-MM-DD |
| `status` | enum | `not_started` \| `in_progress` \| `exported` \| `validated` \| `published` |
| `notes` | string | Free text. For A.0-discovered seeds: brief rationale. For published seeds: "Already published: [slug]" |

**Status values:**
- `not_started`: Seed registered, awaiting Ahrefs research
- `in_progress`: Included in current Ahrefs research batch
- `exported`: Ahrefs data obtained, keywords inserted into `keywords-validated.csv`
- `validated`: Keyword fully validated with metrics
- `published`: This seed's keyword already has a published blog post — skip Ahrefs research

**Initial data:** Migrate 6 batches from `keywords/seeds.md` (~60+ seeds across BOFU, MOFU, TOFU, audience-specific, long-tail, thematic) AND register newly discovered seeds from Step A.0 research.

### 2.2 keywords-validated.csv

**File:** `docs/marketing/data/keywords-validated.csv`

| Column | Type | Description |
|--------|------|-------------|
| `keyword` | string | Validated keyword text |
| `parent_topic` | string | Parent topic from Ahrefs |
| `kd` | integer | Keyword difficulty (0-100) |
| `volume` | integer | Monthly search volume |
| `traffic_potential` | integer | Total traffic potential |
| `business_value` | integer | 1-5 score (see Phase B rubric) |
| `bv_rationale` | string | One-sentence justification for BV score |
| `priority_score` | float | `(business_value * traffic_potential) / (kd + 1)` |
| `funnel_stage` | enum | `BOFU` \| `MOFU` \| `TOFU` |
| `search_intent` | enum | `commercial` \| `informational` \| `comparison` |
| `content_type` | enum | `listicle` \| `guide` \| `comparison` \| `how-to` |
| `pillar` | string | One of 4 pillars (see Section 3) |
| `cluster` | string | Topic cluster within pillar |
| `status` | enum | `validated` \| `scored` \| `prioritized` \| `approved_for_brief` \| `deferred` |
| `status_changed_at` | date | YYYY-MM-DD — updated whenever `status` changes |
| `date_researched` | date | YYYY-MM-DD |
| `brief_id` | string | Link to content-briefs.csv |
| `blog_slug` | string | Link to published MDX |

**Initial data:** Migrate 30+ keywords from `keywords/prioritized.md`.

### 2.3 serp-analysis.csv

**File:** `docs/marketing/data/serp-analysis.csv`

| Column | Type | Description |
|--------|------|-------------|
| `keyword` | string | Target keyword |
| `date_analyzed` | date | YYYY-MM-DD |
| `top_10_urls` | string | Pipe-separated URLs of top 10 results |
| `top_10_titles` | string | Pipe-separated titles |
| `opportunity_type` | string | E.g., "weak competition", "content gap", "format opportunity" |
| `content_format` | string | What format Google rewards (listicle, guide, comparison) |
| `competitor_strengths` | string | Key strengths of top-ranking content |
| `data_source` | enum | `web_search` \| `training_knowledge` |
| `notes` | string | Free text |

### 2.4 competitor-keywords.csv

**File:** `docs/marketing/data/competitor-keywords.csv`

| Column | Type | Description |
|--------|------|-------------|
| `competitor_domain` | string | Domain name |
| `keyword` | string | Keyword they rank for |
| `position` | integer | Their ranking position |
| `date_exported` | date | YYYY-MM-DD |
| `kd` | integer | Keyword difficulty |
| `volume` | integer | Monthly search volume |
| `traffic_potential` | integer | Total traffic potential |
| `notes` | string | Free text |

**Initial data:** Merge 5 competitor CSVs: `CONSENSUS_AHREFS.csv`, `ELICIT_AHREFS.csv`, `NOTEBOOKLM_AHREFS.csv`, `OBSIDIAN_AHREFS.csv`, `SCITEAI_AHREFS.csv`.

### 2.5 content-briefs.csv

**File:** `docs/marketing/data/content-briefs.csv`

| Column | Type | Description |
|--------|------|-------------|
| `brief_id` | string | Matches brief filename (e.g., "01-second-brain-app") |
| `keyword` | string | Primary keyword |
| `date_created` | date | YYYY-MM-DD |
| `outline_status` | enum | `draft` \| `complete` |
| `internal_links_mapped` | boolean | true/false |
| `competitor_benchmarks` | boolean | true/false |
| `status` | enum | `brief_created` \| `serp_analyzed` \| `outline_approved` |
| `assigned_to` | string | Agent or user |

**Initial data:** Register 10 existing briefs in `keywords/briefs/` (01 through 10).

### 2.6 blog-posts.csv

**File:** `docs/marketing/data/blog-posts.csv`

| Column | Type | Description |
|--------|------|-------------|
| `slug` | string | MDX filename without extension |
| `primary_keyword` | string | From keywords-validated.csv |
| `brief_id` | string | Link to content-briefs.csv |
| `word_count` | integer | Published word count |
| `ai_violations` | integer | Count of critical AI writing violations |
| `skills_used` | string | Comma-separated skill names used |
| `date_published` | date | YYYY-MM-DD |
| `date_updated` | date | YYYY-MM-DD |
| `ranking_position` | integer | Current Google position (updated manually) |
| `monthly_traffic` | integer | Monthly organic sessions |
| `conversions` | integer | Sign-ups attributed |
| `status` | enum | `reviewed` \| `published` \| `indexed` \| `ranking` \| `optimizing` \| `archived` |
| `status_changed_at` | date | YYYY-MM-DD — updated whenever `status` changes |

**Initial data:** Populate from 42 published MDX posts and `blog-keyword-map.json` (45 entries).

### 2.7 keyword-blog-mapping.csv

**File:** `docs/marketing/data/keyword-blog-mapping.csv`

| Column | Type | Description |
|--------|------|-------------|
| `keyword` | string | Keyword text |
| `blog_slug` | string | MDX slug |
| `relationship_type` | enum | `primary` \| `secondary` \| `supporting` |

**Cannibalization rule:** Only one post should be `primary` per keyword. The audit script flags multiple `primary` entries for the same keyword.

**Cannibalization remediation:** When a duplicate `primary` mapping is detected:
1. **Differentiate intent:** If the two posts target different search intents (e.g., one commercial, one informational), change the lower-priority post's `relationship_type` to `secondary` and update its `primaryKeyword` to a more specific variant.
2. **Consolidate:** If both posts cover the same intent and overlap significantly, merge the weaker post's unique content into the stronger post, then archive the weaker post (set `status` = `archived` in `blog-posts.csv`).
3. **Redirect:** If the weaker post has external backlinks or indexed traffic, set up a 301 redirect from its slug to the stronger post before archiving.

### 2.8 ahrefs-exports.csv

**File:** `docs/marketing/data/ahrefs-exports.csv`

| Column | Type | Description |
|--------|------|-------------|
| `export_id` | string | Unique identifier |
| `export_type` | enum | `keyword_research` \| `competitor_analysis` \| `serp_overview` |
| `source_keyword` | string | Seed keyword or blank |
| `source_domain` | string | Competitor domain or blank |
| `date_exported` | date | YYYY-MM-DD |
| `rows_imported` | integer | Number of rows processed |
| `status` | enum | `unprocessed` \| `processed` \| `error` |
| `file_path` | string | Relative path to CSV file |

**Initial data:** Register existing Ahrefs CSV files (count may vary — scan `docs/marketing/keywords/` for `AHREFS_*.csv` and `*_AHREFS.csv` patterns to determine actual count).

### 2.9 Internal Link Tracking

Internal links are tracked via two mechanisms — no separate link graph CSV is needed:
1. **`relatedLinks` in MDX frontmatter** — each post declares its `blog`, `useCases`, `comparisons`, and `personas` links.
2. **Brief files** (`keywords/briefs/[NN]-[slug].md`) — the "Internal Links" section records both outbound ("link TO") and inbound ("link FROM") targets with anchor text.

Together these provide the equivalent of a `from_slug → to_slug` link graph. A dedicated `internal-links.csv` with columns `from_slug`, `to_slug`, `anchor_text`, `context` is a future enhancement for when the blog exceeds 100 posts and link auditing at scale becomes necessary.

### 2.10 CSV-to-Frontmatter Sync Rules

On publish, validate that frontmatter matches CSV:
- `primaryKeyword` must exist in `keywords-validated.csv`
- `searchIntent` must match CSV `search_intent` value
- `cluster` must match CSV `cluster` value
- `slug` must match CSV `blog_slug` value

---

## 3. Content Hierarchy & Taxonomy

### 3.1 Hierarchy

```
Pillar → Cluster → Keyword → Brief → Post
```

### 3.2 Pillars and Clusters

| Pillar | Clusters | Blog Category |
|--------|----------|---------------|
| AI Research Tools | Literature Review, Citation Management | `research-synthesis`, `ai-learning` |
| Second Brain & PKM | Second Brain Apps, Connected Notes | `knowledge-compounding` |
| NotebookLM Alternatives | Direct Alternatives, Competitor Comparisons | `ai-learning` |
| Visual Knowledge | Mind Mapping, Concept Visualization | `visual-thinking` |

Additional blog category: `professional-knowledge` (professional workflows, knowledge management at work).

### 3.3 Mapping Rules

- `pillar` column in `keywords-validated.csv` maps to one of the 4 pillars above.
- `cluster` column maps to a cluster within that pillar.
- Blog frontmatter `cluster` field matches the `cluster` column value.
- Blog frontmatter `category` field maps to the blog category for that pillar (see table above).
- Parent Topic from Ahrefs is used as a suggestion for cluster assignment but requires confirmation, not auto-assignment.

---

## 4. Phase A: Research

**Goal:** Discover new keyword opportunities through strategic research, then validate them with Ahrefs data.

**Input:** Atlas product context, competitor landscape, existing published content (42 blog posts in `content/blog/`), existing seeds in `keywords/seeds.md`, and competitor domains.

**Output:** Populated `keyword-seeds.csv`, `keywords-validated.csv`, `serp-analysis.csv`, `competitor-keywords.csv`, and `ahrefs-exports.csv`.

### Step A.0: Discover New Seed Keywords via Strategic Research

**Executor:** AGENT
**Scope:** The entire Atlas keyword landscape — existing blog posts, competitor content, market trends, and audience needs.
**Action:**

This step uses `/content-strategy` and deep web research to discover high-potential seed keywords that are NOT already covered by existing blog posts or existing seeds. This is the creative, strategic discovery step that feeds the rest of the pipeline.

**A.0.0 — Assess pillar balance:**

1. Count published posts per category in `content/blog/`.
2. For each pillar, calculate:
   - Total published posts
   - Aggregate traffic potential of published posts (from `keywords-validated.csv`)
   - Aggregate traffic potential of deferred keywords (from `keywords-validated.csv`)
   - Remaining opportunity = deferred TP / (published TP + deferred TP)
3. Calculate a "pillar priority score" for each pillar:
   `pillar_priority = remaining_opportunity × (deferred_keyword_count / total_keyword_count)`
4. Surface pillars with:
   - Fewer than 25% of total posts but >25% of total keyword traffic potential → "underserved"
   - More than 40% of total posts but <40% of total keyword traffic potential → "saturated"
5. Use these signals when generating seeds in A.0.2 and A.0.3:
   - Weight seed generation toward underserved pillars.
   - For saturated pillars, only generate seeds with traffic_potential > median of
     existing published keywords in that pillar (i.e., only add high-value keywords).
6. Record pillar balance assessment in MEMORY_STATE.md.

**A.0.1 — Build the exclusion list (keywords already used):**

1. Scan all MDX files in `content/blog/` and extract `primaryKeyword` from each file's frontmatter. These are **published keywords** — do NOT generate seeds that duplicate them.
2. Read `data/keyword-seeds.csv` (if it exists). These are **pipeline keywords** — do NOT generate seeds that duplicate them.
3. Read `keywords/seeds.md` (if it exists). These are **legacy seeds** — do NOT generate seeds that duplicate them.
4. Read `data/keywords-validated.csv` (if it exists). Extract all `keyword` values. These are **validated keywords** — do NOT generate seeds that duplicate them.
5. Compile a single **exclusion list** of all keywords from steps 1-4. This list prevents the workflow from researching keywords that are already covered or in the pipeline.

**A.0.2 — Research new seed keywords using `/content-strategy`:**

1. Call `/content-strategy` with input:
   - Atlas product context: AI-powered knowledge workspace for researchers and knowledge workers (search, citation management, visual knowledge mapping, connected notes)
   - The 5 primary competitor domains: `notebooklm.google.com`, `elicit.com`, `scite.ai`, `notion.so`, `obsidian.md`
   - The 4 content pillars (Section 3.2): AI Research Tools, Second Brain & PKM, NotebookLM Alternatives, Visual Knowledge
   - The exclusion list from A.0.1
   - Request: Identify gaps in current content coverage. What topics, angles, and audiences are underserved? What content opportunities exist in each pillar? What emerging trends or new competitor features create keyword opportunities?

2. From the `/content-strategy` output, extract candidate seed keywords organized by funnel stage and pillar.

**A.0.3 — Deep web research for keyword discovery:**

1. Use web search to research each of the following discovery angles. For EACH angle, generate 5-15 candidate seed keywords:

   **Angle 1: Competitor content gaps (agent-driven competitor analysis)**
   - Read existing competitor top pages exports in `docs/marketing/keywords/` (if any exist from prior runs). Extract non-branded keywords with volume > 50.
   - Use web search to analyze competitor blogs, product pages, and documentation for the 5 primary competitor domains (Notion, Obsidian, Elicit, Scite.ai, NotebookLM).
   - Identify topics competitors cover that Atlas does not. Focus on non-branded keywords and content themes.
   - Look for "vs" and "alternative" queries competitors rank for.
   - Extract keyword opportunities from competitor content analysis and feed into the seed pipeline.
   - This replaces the manual Ahrefs Competitor Top Pages session (which yielded mostly branded keywords with limited actionable discovery on the Starter plan's 25-row export cap).

   **Angle 2: Audience pain points**
   - Search Reddit, Twitter/X, and academic forums for complaints about research workflows, note-taking, literature review, and knowledge management
   - Identify recurring pain points expressed in user language (not marketing language)
   - Look for "how do I..." and "what's the best way to..." patterns

   **Angle 3: Emerging trends**
   - Search for new developments in AI research tools, PKM, and knowledge management
   - Identify new tool categories, workflows, or use cases that have emerged recently
   - Look for trending topics in the knowledge work / research space

   **Angle 4: Long-tail and question keywords**
   - Search "People Also Ask" patterns for core topics (second brain, literature review, research tools, mind mapping)
   - Identify specific, actionable question keywords with clear search intent
   - Look for niche audience segments (e.g., "for medical researchers", "for law students", "for journalists")

   **Angle 5: Adjacent topic expansion**
   - Identify topics adjacent to Atlas's core pillars that could attract relevant traffic
   - Look for workflow-related keywords (e.g., "research workflow automation", "academic writing pipeline")
   - Explore cross-pillar opportunities (e.g., "mind map your literature review")

2. For each candidate keyword from web research, verify it is NOT in the exclusion list.

**A.0.4 — Classify and register discovered seeds:**

1. Compile all unique candidate seeds from A.0.2 and A.0.3.
2. Remove any that appear in the exclusion list (exact match or close semantic match — e.g., "second brain apps" duplicates existing "second brain app").
3. For each surviving candidate, classify:
   - `funnel_stage`: BOFU (buying intent, tool search, comparisons) / MOFU (solution-aware, evaluating approaches) / TOFU (problem-aware, learning)
   - `pillar`: one of the 4 pillars from Section 3.2, or "Adjacent" if it doesn't fit neatly
4. Save the classified seeds to a temporary working list for A.1 to register.

**CSV Update:** None directly (A.1 handles CSV registration).
**Skill Call:** `/content-strategy` with input: product context + competitor domains + content pillars + exclusion list. Output: content gap analysis and seed keyword recommendations.
**Completion Condition:** A classified list of new seed keywords exists, all verified against the exclusion list. Minimum target: 20 new seed keywords across at least 3 pillars.
**MEMORY_STATE Update:** Record count of seeds discovered per angle, count of duplicates removed, set `current_step: A.0`, `step_status: completed`, `next_step: A.1`.

### Step A.1: Register ALL Seed Keywords

**Executor:** AGENT
**Scope:** All seeds from TWO sources: (1) `keywords/seeds.md` (legacy seeds) and (2) A.0 research output (newly discovered seeds) — excluding any already in `data/keyword-seeds.csv`.
**Action:**

1. Read `data/keyword-seeds.csv` (create if not exists).

2. **Register legacy seeds from `keywords/seeds.md`:**
   a. Read `keywords/seeds.md`. Parse all seed keywords with their funnel stage (BOFU/MOFU/TOFU) and batch source.
   b. For each seed NOT already in the CSV, add a row with:
      - `seed`: keyword text
      - `funnel_stage`: BOFU/MOFU/TOFU as identified in seeds.md
      - `source`: "seeds.md batch N" (where N is the batch number)
      - `date_added`: today's date
      - `status`: `not_started`
      - `notes`: empty

3. **Register newly discovered seeds from A.0:**
   a. Read the classified seed list from A.0.
   b. For each seed NOT already in the CSV (check both `seed` column and exclusion list from A.0.1), add a row with:
      - `seed`: keyword text
      - `funnel_stage`: BOFU/MOFU/TOFU as classified in A.0.4
      - `source`: discovery angle that produced it (e.g., "A.0 competitor gaps", "A.0 audience pain points", "A.0 emerging trends", "A.0 long-tail questions", "A.0 adjacent topics", "A.0 content-strategy")
      - `date_added`: today's date
      - `status`: `not_started`
      - `notes`: brief context on why this seed was selected (e.g., "Reddit users frequently ask about this", "New tool category emerging in 2026")

4. **Flag seeds whose keywords already have published posts:**
   - For any seed in CSV whose keyword text matches a `primaryKeyword` in an existing blog post, set `status` = `published` and `notes` = "Already published: [slug]". These seeds should not proceed to Ahrefs research.

**CSV Update:** New rows added to `keyword-seeds.csv` with `status` = `not_started` (new seeds) or `published` (already covered).
**Skill Call:** None.
**Completion Condition:** Every seed keyword from `seeds.md` AND from A.0 research has a corresponding row in `keyword-seeds.csv`.
**MEMORY_STATE Update:** Record count of seeds registered (legacy vs new), count flagged as published, set `current_step: A.1`, `step_status: completed`, `next_step: A.2`.

### Step A.2: Prepare Ahrefs Research Instructions

**Executor:** AGENT
**Scope:** All rows in `keyword-seeds.csv` where `status` = `not_started`.
**Action:**
1. Group seed keywords by `funnel_stage` (BOFU, MOFU, TOFU).
2. Write seed keyword groups to `docs/marketing/data/seed-groups.csv` instead of presenting as conversation text. Schema:
   ```
   seed,funnel_stage,group_label,workflow_run,date_generated,status
   "second brain app",BOFU,"BOFU Group 1","run-YYYY-MM-DD","YYYY-MM-DD","not_started"
   ```
   Set `status` = `not_started` for new seeds, `exported` after user completes Ahrefs session, `validated` after A.4 processing.
3. Present the user with: the CSV file path, instructions to open the file, and which column to copy-paste into Ahrefs per session.
4. Prepare a structured instruction document for the user describing 2 Ahrefs sessions:

**Session 1: Keywords Explorer (55 credits)**
- Open `docs/marketing/data/seed-groups.csv` and copy seeds grouped by funnel stage
- Enter seeds into Ahrefs Keywords Explorer
- Apply filters: KD 0-30, Volume 50+, Traffic Potential 200+
- Export CSV with columns: Keyword, Volume, KD, Traffic Potential, Parent Topic

**Optional Session 2: SERP Exports (up to 45 credits)**
- For seeds the human finds particularly interesting, click SERP overview in Keywords Explorer
- Note DR of top 10 results for each keyword
- Identify weak spots (forums, Medium, outdated content in top positions)
- Record which keywords have winnable SERPs vs brand-heavy SERPs
- Export SERP overview CSVs for these keywords
- This is optional — the agent can do equivalent SERP analysis via web search at zero credit cost

Total: 55 credits required, up to 100 with optional SERP exports. 45+ credits in reserve for ad-hoc research.

**Note:** Competitor Top Pages and Content Gap analysis have been moved to agent-driven steps (A.0.3 Angle 1) because:
- Content Gap is unavailable on Ahrefs Starter plan ($29/mo) — requires Lite ($129/mo) or higher.
- Competitor Top Pages exports on Starter are limited to 25 rows, yielding mostly branded keywords with limited actionable discovery.
- Agent-driven competitor analysis via web search provides equivalent or better keyword discovery at zero credit cost.

5. Present the instruction document to the user.

**CSV Update:** Set `status` = `in_progress` for all seeds included in the instructions. Update `seed-groups.csv` status accordingly.
**Skill Call:** None (content strategy analysis was performed in A.0).
**Completion Condition:** Instruction document prepared and presented to user. `seed-groups.csv` created with all seeds.
**MEMORY_STATE Update:** Record instruction set prepared, seed-groups CSV path, set `current_step: A.2`, `step_status: completed`, `next_step: A.3`.

### Step A.3: User Executes Ahrefs Research

**Executor:** HUMAN
**Scope:** All seed keyword batches from A.2 instructions.
**Action:**

**What to do:** Log into Ahrefs. Execute the research protocol described in Step A.2:
- Session 1 (required): Keywords Explorer — open `docs/marketing/data/seed-groups.csv`, copy seeds by funnel stage, enter into Keywords Explorer, apply filters (KD 0-30, Volume 50+, TP 200+), export CSV (55 credits)
- Session 2 (optional): SERP Exports — for seeds that look particularly promising, export SERP overview CSVs (up to 45 credits). The agent can do SERP analysis via web search at zero credit cost, so this is optional.

**What to produce:**
- 1-3 CSV files from Ahrefs Keywords Explorer exports
- (Optional) SERP overview CSV exports for high-interest keywords
- (Optional) A text summary of SERP validation findings: which keywords have winnable SERPs, which are brand-heavy, which have weak spots

**Where to put it:**
- Save CSVs to `docs/marketing/keywords/` with naming pattern `AHREFS_[topic].csv`
- Save SERP notes as `docs/marketing/data/serp-notes.md`

**Signal completion:** Tell Claude Code "Ahrefs exports complete" and list the filenames saved.

**CSV Update:** None (user action).
**Skill Call:** None.
**Completion Condition:** User confirms, Claude Code verifies CSV files exist at expected paths.
**MEMORY_STATE Update:** Set `step_status: waiting_on_human`, record which sessions are expected. On user confirmation: set `step_status: completed`, `next_step: A.4`.

### Step A.4: Consolidate and Normalize Exports

**Executor:** AGENT
**Scope:** All new CSV files the user placed + all rows in `ahrefs-exports.csv` where `status` = `unprocessed`.
**Action:**

**Pre-step:** If `scripts/consolidate-ahrefs.ts` exists, run it (`npx ts-node scripts/consolidate-ahrefs.ts`) to auto-normalize exports. If the script does not exist or fails, perform normalization manually as described below.

1. Scan `docs/marketing/keywords/` for new `AHREFS_*.csv` and `*_AHREFS.csv` files not yet registered in `ahrefs-exports.csv`.
2. Register each new export in `ahrefs-exports.csv` with `status` = `unprocessed`.
3. For each unprocessed export:
   a. Parse the CSV. Note: Ahrefs exports may contain CSS class-name columns from HTML-table format. Normalize column names by stripping CSS class prefixes (e.g., `.keyword` → `keyword`, `.kd` → `kd`).
   b. Determine export type from filename pattern: `AHREFS_*` = keyword research, `*_AHREFS` = competitor analysis.
   c. For keyword research exports: insert validated keywords into `keywords-validated.csv` with `status` = `validated`, `date_researched` = today. Deduplicate against existing rows by `keyword` (update metrics if keyword already exists).
   d. For competitor exports: insert into `competitor-keywords.csv`. Deduplicate by `competitor_domain` + `keyword`.
   e. Mark export as `processed` in `ahrefs-exports.csv`, record `rows_imported`.
4. If `data/serp-notes.md` exists (from user's SERP validation in A.3):
   a. Parse SERP notes.
   b. For each keyword mentioned, add or update a row in `serp-analysis.csv` with the user's findings (opportunity type, weak spots, DR notes). Set `data_source` = `web_search`.
5. **Agent-driven SERP analysis (replaces human Session 4):**
   a. After consolidation, identify top 20 candidates by priority score (calculated in Step 5, or estimated here as `traffic_potential / (kd + 1)` for pre-scoring).
   b. For each top candidate, use web search to analyze SERP difficulty:
      - Check top-ranking domains and note DR of top 10 results for each keyword.
      - Identify weak spots (forums, Medium, outdated content in top positions).
      - Classify each keyword as: `winnable` (weak competition, achievable DR gap), `competitive` (strong domains but content gaps exist), or `brand_heavy` (dominated by branded results — deprioritize).
   c. Record findings in `serp-analysis.csv` with `data_source` = `web_search`. Include `opportunity_type` classification from step b.
   d. If the human also provided SERP exports from optional Session 2, merge both data sources (human Ahrefs exports take priority for overlapping keywords).
6. Update `keyword-seeds.csv`: set `status` = `exported` for seeds that now have corresponding validated keywords. (Seeds with `status` = `published` are already terminal — do not modify them.)
7. Update `seed-groups.csv`: set `status` = `exported` for seeds whose keywords are now in `keywords-validated.csv`.

**CSV Update:** New rows in `keywords-validated.csv` (status = `validated`), `competitor-keywords.csv`, `ahrefs-exports.csv` (status = `processed`), `serp-analysis.csv` (agent SERP analysis + any human SERP notes), `keyword-seeds.csv` (status = `exported`), `seed-groups.csv` (status = `exported`).
**Skill Call:** None.
**Completion Condition:** All exports processed, all keywords in `keywords-validated.csv`, SERP analysis recorded in `serp-analysis.csv` for top 20 candidates.
**MEMORY_STATE Update:** Record count of keywords validated, count of exports processed, count of SERP analyses completed, set `current_step: A.4`, `step_status: completed`, `next_step: 5`.

**Phase A Gate:** `keyword-seeds.csv` has all seeds registered (from both legacy and A.0 discovery) AND `keywords-validated.csv` has rows with `status` = `validated` AND `serp-analysis.csv` has entries for top candidates. Cannot proceed to Phase B until all A steps (A.0 through A.4) are complete.

---

## 5. Phase B: Prioritization

**Goal:** Score, cluster, and approve/defer all validated keywords in a single pass.

**Input:** `keywords-validated.csv` with status = `validated`.

**Output:** All keywords scored, prioritized, clustered, and classified as `approved_for_brief` or `deferred`.

### Step 5: Score, Cluster, and Approve ALL Validated Keywords

**Executor:** AGENT
**Scope:** Every row in `keywords-validated.csv` where `status` = `validated`.
**Action:**

For EACH keyword, perform all of the following in a single pass. One CSV read at the start, one CSV write at the end.

**5a. Assign Business Value (1-5)**

Reason about each keyword's business value using the scoring rubric. Consider the keyword text, its funnel stage, search intent signals, and relevance to Atlas features. Record the score AND a one-sentence rationale.

**Business Value Rubric (1-5):**

| Score | Criteria | Signal Examples |
|-------|----------|-----------------|
| **5** | Direct product search, competitor comparison, high buying intent | "notebooklm alternative", "second brain app", "best ai research tool" |
| **4** | Solution-aware, evaluating tools in the category | "ai for literature review", "research paper organizer", "connected notes app" |
| **3** | Problem-aware, seeking solutions but not yet tool-shopping | "how to organize research papers", "too many browser tabs research" |
| **2** | Informational, tangentially relevant to Atlas domain | "how to write literature review", "what is zettelkasten" |
| **1** | Broad awareness, only indirectly connected to knowledge work | "productivity tips for students", "best study habits" |

**No heuristic auto-assign.** Every keyword gets prompt-based reasoning. Read the keyword, consider what a searcher wants, assess how directly Atlas solves that need, and assign a score with rationale.

Set `business_value` (1-5) and `bv_rationale` (one-sentence justification).

**5b. Calculate Priority Score**

```
priority_score = (business_value × traffic_potential) ÷ (kd + 1)
```

Example:
- Keyword: "second brain app"
- Business Value: 5, Traffic Potential: 800, KD: 3
- Priority Score: (5 × 800) ÷ (3 + 1) = 1000.0

**5c. Assign Cluster and Pillar**

Group by `parent_topic` (from Ahrefs data) and assign `cluster` and `pillar` per the taxonomy in Section 3.2:
- If parent_topic relates to literature review, citations, research tools → Pillar: "AI Research Tools"
- If parent_topic relates to second brain, PKM, note-taking → Pillar: "Second Brain & PKM"
- If parent_topic relates to NotebookLM, specific tool alternatives → Pillar: "NotebookLM Alternatives"
- If parent_topic relates to mind maps, visual organization → Pillar: "Visual Knowledge"

Within each pillar, assign the most specific cluster (see Section 3.2 for cluster names).

**5d. Apply Decision Thresholds**

| Threshold | Condition | Status | Notes |
|-----------|-----------|--------|-------|
| **Immediate** | priority_score > 150 AND kd < 20 | `approved_for_brief` | High priority, proceed to brief |
| **Secondary** | priority_score 75-150 AND kd 15-30 | `approved_for_brief` | Add note: "secondary priority" |
| **Long-term** | priority_score < 75 | `deferred` | Monitor for opportunity changes |

**CSV Update:** Set `business_value`, `bv_rationale`, `priority_score`, `cluster`, `pillar`, and `status` = `approved_for_brief` or `deferred` for each row.
**Skill Call:** None.
**Completion Condition:** Every keyword in `keywords-validated.csv` has `business_value`, `priority_score`, `cluster`, `pillar`, and a status of `approved_for_brief` or `deferred`.
**MEMORY_STATE Update:** Record counts (approved vs deferred), set `current_step: 5`, `step_status: completed`, `next_step: 6`.

**Phase B Gate:** Every keyword in `keywords-validated.csv` has `business_value`, `priority_score`, `cluster`, `pillar`, and a status of `approved_for_brief` or `deferred`. Cannot proceed to Phase C until Step 5 is complete.

---

## 6. Phase C: Briefs

**Goal:** Create detailed content briefs with SERP analysis, outlines, and internal linking strategy for all approved keywords.

**Input:** `keywords-validated.csv` with status = `approved_for_brief`.

**Output:** Brief files in `keywords/briefs/`, populated `content-briefs.csv` and `serp-analysis.csv`.

### Step 6: SERP Analysis + Content Strategy for ALL Approved Keywords

**Executor:** AGENT
**Scope:** Every row in `keywords-validated.csv` where `status` = `approved_for_brief`.
**Action:**

For each keyword, perform SERP analysis and content strategy determination in a single pass:

**6a. SERP Analysis**

1. Use web search to analyze top 10 SERP results.
2. Record in `serp-analysis.csv`:
   - `keyword`: the target keyword
   - `date_analyzed`: today
   - `top_10_urls`: pipe-separated URLs of top 10 results
   - `top_10_titles`: pipe-separated titles
   - `opportunity_type`: e.g., "weak competition — forums and Medium in top 5", "content gap — no comprehensive listicle", "format opportunity — no comparison table"
   - `content_format`: what format Google rewards (listicle, guide, comparison, how-to)
   - `competitor_strengths`: key strengths of top content (e.g., "deep methodology", "visual examples", "brand authority")
   - `data_source`: `web_search` or `training_knowledge`
   - `notes`: what's missing, differentiation opportunities
3. If web search is unavailable or returns insufficient data: use training knowledge of typical SERP patterns for the topic area. Record `data_source` = `training_knowledge`.

**6b. Content Strategy**

From the SERP analysis, determine:
- `search_intent`: `commercial` (buying/comparing), `informational` (learning/how-to), or `comparison` (X vs Y)
- `content_type`: `listicle` (ranked list of items), `guide` (step-by-step educational), `comparison` (head-to-head), `how-to` (process-focused)
- Target word count based on SERP data: match or exceed top-ranking content (typically 2,000-4,000 words)

Update `keywords-validated.csv` with `search_intent` and `content_type`.

**CSV Update:** New or updated rows in `serp-analysis.csv`. Set `search_intent` and `content_type` in `keywords-validated.csv`.
**Skill Call:** None (uses web search directly for SERP data).
**Completion Condition:** Every approved keyword has a row in `serp-analysis.csv` and `search_intent` + `content_type` populated in `keywords-validated.csv`.
**MEMORY_STATE Update:** Record count analyzed, set `current_step: 6`, `step_status: completed`, `next_step: 7`.

### Step 7: Create Briefs + Map Links + Register for ALL Approved Keywords

**Executor:** AGENT
**Scope:** Every approved keyword with `search_intent` and `content_type` set.
**Action:**

For each keyword, create brief, map internal links, and register in CSV in a single pass:

**7a. Create Brief File**

1. Determine the next brief number (check existing files in `keywords/briefs/`).
2. Create brief file at `docs/marketing/keywords/briefs/[NN]-[slug].md`.
3. Populate the brief using the template below, selecting the outline structure based on `content_type`.

**Brief Template:**

```markdown
## Target Keyword
**Primary:** [keyword from CSV]
**Secondary:** [2-3 related keywords from same cluster]

## Metrics
| Metric | Value |
|--------|-------|
| Volume | [from CSV] |
| KD | [from CSV] |
| Traffic Potential | [from CSV] |
| Business Value | [from CSV] |
| Priority Score | [from CSV] |
| Funnel Stage | [from CSV] |

## Search Intent
[search_intent] — [one-sentence description of what the searcher wants]

## SERP Analysis
[Summarize from serp-analysis.csv: top sites, content types, what's missing, opportunity]

## Content Format
**Type:** [content_type]
**Target Length:** [word count]
**Target URL:** `/blog/[slug]`

## Outline
[Use format-specific outline below]

## Internal Links
**Link TO (from this article):**
- [slug]: /blog/[slug] or /use-cases/[slug]

**Link FROM (add links to this article):**
- [slug]: /blog/[slug]

## Competitor Benchmarks
| Competitor | Word Count | Key Strength | What to Beat |
|------------|-----------|--------------|--------------|
| [name] | [count] | [strength] | [strategy] |
```

**Outline by Content Type:**

**Listicle / Comparison (content_type = `listicle` or `comparison`):**
```
### Introduction (150-200 words)
- Hook: Pain point or problem statement
- Define the concept
- Preview: What readers will learn

### What to Look For in [Category] (300-400 words)
- Criteria for evaluation
- Key features that matter
- What to avoid

### Top [N] [Category] (1,500-2,500 words)
1. **Atlas** — [Atlas positioning: AI-powered knowledge workspace]
   - Who it's for
   - Key strengths (4-5 bullet points)
   - Pricing
2. **Competitor 1** — [Same structure]
3-7. **Competitors 2-6** — [Same structure]

### Comparison Table
[Feature comparison matrix]

### How to Choose the Right [Tool] (200-300 words)
- Decision framework
- Use case recommendations

### FAQs (400-600 words)
- 4-6 questions from "People Also Ask"
- Address common objections

### Conclusion (100-150 words)
- Summary
- Recommendation
- CTA to try Atlas
```

**Guide / How-to (content_type = `guide` or `how-to`):**
```
### Introduction (150-200 words)
- Hook: Problem statement
- Why this matters
- What you'll learn

### What Is [Concept] (200-300 words)
- Definition
- Why it matters
- Brief history or context

### Step-by-Step Process (1,500-2,500 words)
- Step 1: [Action] (300-400 words)
  - Explanation
  - Example
  - Tips
- Step 2-N: [Same structure]

### Tools and Resources (300-400 words)
- Atlas positioning
- Alternative tools

### Common Mistakes to Avoid (200-300 words)
- Mistake 1 + fix
- Mistake 2 + fix

### FAQs (400-600 words)
- 4-6 questions

### Conclusion (100-150 words)
- Summary
- Next steps
- CTA to try Atlas
```

**Headline Formula Reference:**

Use these formulas as starting points when crafting titles and H2 headings (the `/atlas-seo` skill has the full set):

| # | Formula | Example |
|---|---------|---------|
| 1 | **[Number] Best [Category] for [Audience] in [Year]** | "7 Best Second Brain Apps for Researchers in 2026" |
| 2 | **How to [Achieve Goal] (Step-by-Step Guide)** | "How to Build a Second Brain (Step-by-Step Guide)" |
| 3 | **[Tool A] vs [Tool B]: [Differentiator]** | "NotebookLM vs Obsidian: Which Handles Research Better?" |
| 4 | **What Is [Concept]? (And Why It Matters for [Audience])** | "What Is Zettelkasten? (And Why It Matters for Writers)" |
| 5 | **[Number] [Adjective] Ways to [Solve Problem]** | "5 Proven Ways to Organize Research Papers" |
| 6 | **The Complete Guide to [Topic] in [Year]** | "The Complete Guide to AI Literature Review in 2026" |
| 7 | **[Topic]: Everything You Need to Know** | "Connected Notes Apps: Everything You Need to Know" |
| 8 | **Why [Common Approach] Fails (And What to Do Instead)** | "Why Folder-Based Note Systems Fail (And What to Do Instead)" |
| 9 | **[Audience]'s Guide to [Topic]** | "The PhD Student's Guide to AI Research Tools" |
| 10 | **[Number] [Topic] Mistakes That [Negative Outcome]** | "5 Literature Review Mistakes That Tank Your Paper" |

**7b. Map Internal Links**

For each brief:
1. Scan existing blog posts in `content/blog/` by reading frontmatter (`primaryKeyword`, `cluster`, `relatedLinks`).
2. Identify 3-5 **link-to** targets: existing posts that the new article should link to (same cluster, related topics, use case pages).
3. Identify 2-3 **link-from** sources: existing posts that should add a link back to the new article.
4. Populate the brief file's "Internal Links" section with specific slugs and anchor text suggestions.

**7c. Register in CSV**

For each brief:
1. Add row to `content-briefs.csv`:
   - `brief_id`: filename without extension (e.g., "01-second-brain-app")
   - `keyword`: primary keyword from brief
   - `date_created`: today
   - `outline_status`: `complete`
   - `internal_links_mapped`: `true`
   - `competitor_benchmarks`: `true` if benchmarks section is populated
   - `status`: `outline_approved`
   - `assigned_to`: "claude-code"
2. Update `keywords-validated.csv`: set `brief_id` for the corresponding keyword row.

**CSV Update:** New rows in `content-briefs.csv` with `status` = `outline_approved`. Updated `brief_id` in `keywords-validated.csv`.
**Skill Call:** None.
**Completion Condition:** Every approved keyword has a brief file in `keywords/briefs/` with outline, internal links, and competitor benchmarks populated. All briefs registered in `content-briefs.csv`.
**MEMORY_STATE Update:** Record count of briefs created, set `current_step: 7`, `step_status: completed`, `next_step: 8`.

**Phase C Gate:** Every approved keyword has a brief in `content-briefs.csv` with `status` = `outline_approved`, a brief file in `keywords/briefs/`, SERP data in `serp-analysis.csv`, and internal linking mapped. Cannot proceed to Phase D until Steps 6-7 are complete.

---

## 7. Phase D: Content Production + Publishing

**Goal:** Generate publication-ready MDX posts, add internal links, validate everything, and commit.

**Input:** `content-briefs.csv` with status = `outline_approved`.

**Output:** Published MDX files in `content/blog/`, all CSVs updated, local git commit.

### Step 8: Generate MDX Posts (`/atlas-seo`)

**Executor:** AGENT
**Scope:** Every row in `content-briefs.csv` where `status` = `outline_approved`.
**Action:**

For each brief, generate a publication-ready blog post in a single pass using the `/atlas-seo` skill. Output goes directly to `content/blog/[slug].mdx` with full YAML frontmatter. No intermediate draft files.

1. Read the brief file from `keywords/briefs/[brief_id].md`.
2. Invoke `/atlas-seo` with the brief as input. The skill handles:
   - Draft generation using the prompt template (see `/atlas-seo` SKILL.md Section 4)
   - All 7 copy-editing sweep criteria applied during generation
   - Persuasion principles applied during generation
   - AI-avoidance rules enforced during generation
   - AEO/GEO structural requirements built into content
   - YAML frontmatter with all required fields
   - MDX formatting
3. Save output to `content/blog/[slug].mdx`.
4. Add row to `blog-posts.csv`:
   - `slug`: URL-friendly slug (lowercase, hyphens, includes primary keyword, 3-6 words)
   - `primary_keyword`: from brief
   - `brief_id`: from brief
   - `word_count`: actual word count
   - `ai_violations`: 0
   - `skills_used`: "/atlas-seo"
   - `status`: `reviewed`
   - `date_published`: (empty — set in Step 11)
5. **Update MEMORY_STATE.md immediately** after each post (this step is most likely to hit context limits).

**CSV Update:** New rows in `blog-posts.csv` with `status` = `reviewed`.
**Skill Call:** `/atlas-seo` per post. **⚠️ BLOCKING: The `/atlas-seo` skill MUST be invoked BEFORE generating any post content. Do NOT proceed with content generation until the skill has been loaded and the MEMORY_STATE.md skill checklist has been updated.**
**Completion Condition:** All approved briefs have corresponding MDX files in `content/blog/` and `blog-posts.csv` entries with `status` = `reviewed`.
**MEMORY_STATE Update:** **Critical — update after EACH post**, not just at step end. Record which posts are generated, which remain. Set `current_step: 8`, update skill checklist (Step 8 → /atlas-seo → YES).

### Step 9: Internal Links (`/programmatic-seo`)

**Executor:** AGENT
**Scope:** Every new MDX file generated in Step 8.
**Action:**

For each post:
1. Read the brief's internal linking section (from Step 7b).
2. Add 3-5 outbound internal links within the article content:
   - Link to related use case pages: `/use-cases/[slug]`
   - Link to related blog posts: `/blog/[slug]`
   - Link to comparison pages: `/vs/[competitor]`
   - Use descriptive anchor text (not "click here")
   - Place links contextually where they add value
3. Update existing related posts to add backlinks to this new post:
   - Open each target post from the "link FROM" list in the brief
   - Find relevant anchor text in the existing post
   - Add markdown link to the new post
   - Save the modified existing post

**CSV Update:** None.
**Skill Call:** `/programmatic-seo` for hub-spoke linking strategy across the cluster. **⚠️ BLOCKING: The `/programmatic-seo` skill MUST be invoked BEFORE implementing any internal links. Do NOT proceed with link insertion until the skill has been loaded and the MEMORY_STATE.md skill checklist has been updated.**
**Completion Condition:** All new posts have 3-5 internal links. Reciprocal links added to existing posts.
**MEMORY_STATE Update:** Record count with links, update skill checklist (Step 9 → /programmatic-seo → YES), set `current_step: 9`, `step_status: completed`, `next_step: 10`.

### Step 10: Validate + Fix ALL Posts

**Executor:** AGENT
**Scope:** Every new MDX file.
**Action:**

Run ALL validation checks in a single pass per post:

**10a. AI Writing Detection**

Scan each post for:

1. **Em-dashes (—):** Count all occurrences. Any em-dash is a violation.
2. **Overused verbs (15):** `delve`, `leverage`, `optimize`, `utilize`, `facilitate`, `foster`, `bolster`, `underscore`, `unveil`, `navigate`, `streamline`, `enhance`, `endeavor`, `ascertain`, `elucidate`
3. **Overused adjectives (14):** `robust`, `comprehensive`, `pivotal`, `crucial`, `vital`, `transformative`, `cutting-edge`, `groundbreaking`, `innovative`, `seamless`, `intricate`, `nuanced`, `multifaceted`, `holistic`
4. **AI transitions (6):** `furthermore`, `moreover`, `notwithstanding`, `that being said`, `at its core`, `to put it simply`
5. **Opening red flags (3):** `In today's fast-paced world`, `In an era of`, `Let's delve into`
6. **Filler words (21):** `absolutely`, `actually`, `basically`, `certainly`, `clearly`, `definitely`, `essentially`, `extremely`, `fundamentally`, `incredibly`, `interestingly`, `obviously`, `quite`, `really`, `significantly`, `simply`, `surely`, `truly`, `ultimately`, `undoubtedly`, `very`
7. **Academic tells (6):** `shed light on`, `pave the way for`, `a myriad of`, `a plethora of`, `paramount`, `pertaining to`

Prompt-based detection: formulaic structures, hedged language, AI transition patterns, unnaturally balanced paragraphs, generic conclusions.

**Severity Classification:**

| Severity | Condition | Blocking? |
|----------|-----------|-----------|
| **Critical** | 2+ em-dashes; 3+ overused verbs total; any opening red flag | YES |
| **Warning** | 1 em-dash; 1-2 overused verbs; 3+ filler words | NO (should fix) |
| **Info** | Academic tells; formal language with plain-English alternatives | NO (optional) |

**10b. SEO Audit**

Run `npm run audit:blog` (or `npx ts-node scripts/audit-blog-seo.ts`):

| Check | Severity | Criteria |
|-------|----------|----------|
| Title length | Warning | 50-60 characters |
| Description length | Warning | 150-160 characters |
| Primary keyword in title | Critical | Must be present |
| Primary keyword in description | Warning | Should be present |
| Primary keyword in first 100 words | Warning | Should be present |
| Keyword density | Warning | 1-2% for primaryKeyword |
| All frontmatter fields present | Critical | title, description, slug, keywords, category, cluster, primaryKeyword, searchIntent, author, publishedAt, updatedAt, faqs, relatedLinks |
| FAQ count | Warning | 4-6 Q&A pairs |
| Heading hierarchy | Warning | Single H1 (title only), proper H2/H3 nesting |
| Word count | Warning | 2,000-4,000 words |
| Internal links present | Warning | Minimum 3 |
| Broken internal links | Critical | All /blog/[slug] links must resolve |
| Duplicate primaryKeyword | Critical | No two posts share the same primaryKeyword |
| Image alt text | Info | All `![](...)` images should have descriptive alt text |
| External link validation | Info | All external URLs well-formed (https://) and reputable |
| Content freshness | Info | Flag if updatedAt > 6 months old |

**10c. AEO/GEO Validation**

Based on `searchIntent` from frontmatter:

**Commercial Intent posts (`searchIntent` = `commercial` or `comparison`) require:**
- 1+ comparison table (markdown table with 4+ rows)
- 4+ FAQ entries (in frontmatter)
- 2+ statistics citing a named source

**Informational Intent posts (`searchIntent` = `informational`) require:**
- Definition in first 200 words
- Step-by-step structure (if how-to content type)
- 3+ evidence-backed claims

**AEO/GEO Scoring:** Each requirement met = 33 points (0-99 scale). Blocking threshold: score >= 99 (all 3 met).

AEO-specific: self-contained answer blocks, FAQ answers 50-100 words, listicle items with justifications.
GEO-specific: authoritative claims format, evidence sandwich, specific numbers and timeframes.

**10d. Frontmatter-CSV Sync**

For each post, verify:
1. `primaryKeyword` in frontmatter must exist as a `keyword` in `keywords-validated.csv`.
2. `searchIntent` in frontmatter must match `search_intent` in `keywords-validated.csv`.
3. `cluster` in frontmatter must match `cluster` in `keywords-validated.csv`.
4. `slug` in frontmatter must match the intended `blog_slug` in `keywords-validated.csv`.

**Fix Loop:**

If ANY issues found across 10a-10d:
1. Fix all issues in one pass (use replacement tables from Section 8 for AI violations, auto-fix for SEO/AEO/GEO/sync issues).
2. Revalidate all checks.
3. Repeat until all checks pass.

**Safety valve:** If the same violation persists unchanged after 5 consecutive fix attempts, record in `blocking_issues` and proceed.

**CSV Update:** Set `ai_violations` in `blog-posts.csv`. Update `blog_slug` in `keywords-validated.csv` if needed.
**Skill Call:** None.
**Completion Condition:** All posts pass all checks with zero critical issues and `ai_violations` = 0.
**MEMORY_STATE Update:** Record validation results, AEO/GEO scores, set `current_step: 10`, `step_status: completed`, `next_step: 11`.

### Step 11: Update CSVs and Commit

**Executor:** AGENT
**Scope:** Every validated post.
**Action:**

1. Update `blog-posts.csv` for each post:
   - Set `status` = `published`
   - Set `date_published` = today
   - Set `word_count` = actual word count of published MDX content
2. Add rows to `keyword-blog-mapping.csv`:
   - Primary keyword → `relationship_type` = `primary`
   - Secondary keywords (from frontmatter `keywords[]` array) → `relationship_type` = `secondary`
   - Any supporting keywords mentioned in content → `relationship_type` = `supporting`
3. Update `keywords-validated.csv`: set `blog_slug` for each keyword that now has a published post.
4. Stage and commit:
   ```
   git add content/blog/[new-slugs].mdx
   git add docs/marketing/data/*.csv
   git add docs/marketing/keywords/briefs/*
   git add docs/marketing/MEMORY_STATE.md
   git add [any modified existing blog posts with new backlinks]
   git commit -m "Add blog posts: [comma-separated list of slugs]"
   ```
   **Do NOT push.** The user will push when ready.

**CSV Update:** `blog-posts.csv` status = `published`, `keyword-blog-mapping.csv` new rows, `keywords-validated.csv` blog_slug updated.
**Skill Call:** None.
**Completion Condition:** All CSVs updated, all files committed locally.
**MEMORY_STATE Update:** Record final counts, set `current_step: 11`, `step_status: completed`, `current_phase: complete`.

**Phase D Gate:** Every post has a committed MDX file in `content/blog/`, all CSVs updated, all internal links reciprocal, all validation checks passing (AI detection, SEO audit, AEO/GEO, frontmatter-CSV sync). Workflow complete for this batch. User pushes to deploy at their discretion.

---

## 8. Validation Rules Reference

Consolidated reference of all validation checks. The actual validation logic is specified inline at Step 10 where it executes. This section exists for human review and script development.

### 8.1 AI Writing Detection (Step 10)

**Overused Verbs (15):**
`delve`, `leverage`, `optimize`, `utilize`, `facilitate`, `foster`, `bolster`, `underscore`, `unveil`, `navigate`, `streamline`, `enhance`, `endeavor`, `ascertain`, `elucidate`

**Overused Adjectives (14):**
`robust`, `comprehensive`, `pivotal`, `crucial`, `vital`, `transformative`, `cutting-edge`, `groundbreaking`, `innovative`, `seamless`, `intricate`, `nuanced`, `multifaceted`, `holistic`

**AI Transitions (6):**
`furthermore`, `moreover`, `notwithstanding`, `that being said`, `at its core`, `to put it simply`

**Opening Red Flags (3):**
`In today's fast-paced world`, `In an era of`, `Let's delve into`

**Filler Words (21):**
`absolutely`, `actually`, `basically`, `certainly`, `clearly`, `definitely`, `essentially`, `extremely`, `fundamentally`, `incredibly`, `interestingly`, `obviously`, `quite`, `really`, `significantly`, `simply`, `surely`, `truly`, `ultimately`, `undoubtedly`, `very`

**Academic Tells (6):**
`shed light on`, `pave the way for`, `a myriad of`, `a plethora of`, `paramount`, `pertaining to`

**Severity Rules:**

| Severity | Condition | Blocks Publishing? |
|----------|-----------|-------------------|
| Critical | 2+ em-dashes; 3+ overused verbs total; any opening red flag | YES |
| Warning | 1 em-dash; 1-2 overused verbs; 3+ filler words | NO (should fix) |
| Info | Academic tells; formal language | NO (optional) |

### 8.2 AEO/GEO Requirements (Step 10)

**Commercial Intent (`commercial` or `comparison`):**
- 1+ comparison table (markdown table with 4+ rows) — 33 points
- 4+ FAQ entries (in frontmatter) — 33 points
- 2+ statistics with sources — 33 points

**Informational Intent (`informational`):**
- Definition in first 200 words — 33 points
- Step-by-step structure (if how-to) — 33 points
- 3+ evidence-backed claims — 33 points

**Scoring:** Each requirement met = 33 points (0-99 scale). Blocking threshold: score ≥ 99 (all 3 met).

### 8.3 SEO Checks (Step 10)

| Check | Severity | Criteria |
|-------|----------|----------|
| Title length | Warning | 50-60 characters |
| Description length | Warning | 150-160 characters |
| Primary keyword in title | Critical | Must be present |
| Primary keyword in first 100 words | Warning | Should be present |
| Keyword density | Warning | 1-2% |
| Frontmatter completeness | Critical | All required fields |
| FAQ count | Warning | 4-6 |
| Heading hierarchy | Warning | Single H1, proper H2/H3 nesting |
| Word count | Warning | 2,000-4,000 |
| Internal links | Warning | Minimum 3 per post, max 1 per 200 words |
| Broken internal links | Critical | All must resolve |
| Duplicate primaryKeyword | Critical | One post per keyword |
| Image alt text | Info | All images should have descriptive alt text |
| External link validation | Info | All external URLs well-formed (https://) and reputable |
| Content freshness | Info | Flag if > 6 months old |

### 8.4 Internal Linking Rules (Steps 7, 9)

- Minimum 3 internal links per post
- Maximum 1 link per 200 words (avoid over-optimization)
- All cluster siblings should link to each other
- Pillar pages should link to all cluster posts
- Use descriptive anchor text (not "click here")
- All links must be reciprocal where possible

### 8.5 Frontmatter-CSV Consistency (Step 10)

- `primaryKeyword` must exist in `keywords-validated.csv`
- `searchIntent` must match CSV value
- `cluster` must match CSV value
- `slug` must match CSV `blog_slug` value
- Only one post `primary` per keyword in `keyword-blog-mapping.csv`

---

## 9. Skill Integration Map & Human Handoff Inventory

### 9.1 Skill-to-Step Map

| Step | Executor | Skill | Input | Output |
|------|----------|-------|-------|--------|
| A.0 | AGENT | `/content-strategy` + web search | Product context + competitor domains + pillars + exclusion list | New seed keywords (20+ across 3+ pillars) |
| Step 6 | AGENT | web search (no skill) | Target keyword | SERP analysis + content strategy |
| Step 8 | AGENT | `/atlas-seo` | Brief file | Publication-ready MDX with frontmatter |
| Step 9 | AGENT | `/programmatic-seo` | Post + cluster data | Internal linking plan |

### 9.2 Human Handoff Inventory

There is exactly ONE human handoff in the entire workflow:

| Step | Type | What User Does | Deliverable | Blocks |
|------|------|---------------|-------------|--------|
| A.3 | HUMAN | Log into Ahrefs, run 1 required session (Keywords Explorer, 55 credits) + 1 optional session (SERP exports, up to 45 credits), export CSVs | 1-3 CSV files from Keywords Explorer + optional SERP exports | Phase A cannot complete without Ahrefs data |

All other steps — including seed keyword discovery (A.0), business value scoring, keyword prioritization, brief creation, content generation, validation, internal linking, and git commit — are fully autonomous AGENT steps.

The user pushes to remote and deploys at their own discretion after the workflow completes.

---

## 10. MEMORY_STATE.md Specification

### 10.1 Schema

```markdown
# MEMORY_STATE
---
workflow_version: "3.0"
workflow_run_id: "run-YYYY-MM-DD"
last_updated: "YYYY-MM-DD HH:MM"
seed_groups_csv_path: "docs/marketing/data/seed-groups.csv"
---

## Execution State

current_phase: [A|B|C|D|complete]
current_step: [e.g., "8"]
next_step: [e.g., "9"]
step_status: [in_progress|completed|waiting_on_human]
step_executor: [AGENT|HUMAN]

## Current Step Progress

### Items Completed (in current step)
- [keyword-or-slug-1]: [status after processing]
- [keyword-or-slug-2]: [status after processing]

### Items Remaining (in current step)
- [keyword-or-slug-3]
- [keyword-or-slug-4]

### Items Tracking (for multi-item steps: Step 8, Step 9)

completed_items:
  - [slug-1] (brief NN)
  - [slug-2] (brief NN)

remaining_items:
  - [slug-3] (brief NN)
  - [slug-4] (brief NN)

total: [N]
completed: [N]
remaining: [N]

Note: The agent MUST update completed_items and remaining_items after processing
EACH item in multi-item steps, not just at step completion. This enables accurate
resume after autocompaction.

## Skill Checklist (current step)

| Step | Required Skill | Invoked? | Timestamp |
|------|---------------|----------|-----------|
| Step 8 | /atlas-seo | NO |           |
| Step 9 | /programmatic-seo | NO |    |

The agent MUST populate this table at the start of each step and mark "YES" with
timestamp only AFTER actually invoking the skill. This creates an audit trail.
The skill call check in Section 0.7 is a BLOCKING requirement — the agent must NOT
proceed with step work until the required skill has been invoked and this table updated.

## Pillar Balance Snapshot (updated in A.0.0)

| Pillar | Published Posts | Published TP | Deferred TP | Remaining Opportunity | Priority |
|--------|----------------|-------------|-------------|----------------------|----------|
| AI Research Tools | [N] | [N] | [N] | [%] | [underserved/balanced/saturated] |
| Second Brain & PKM | [N] | [N] | [N] | [%] | [underserved/balanced/saturated] |
| NotebookLM Alternatives | [N] | [N] | [N] | [%] | [underserved/balanced/saturated] |
| Visual Knowledge | [N] | [N] | [N] | [%] | [underserved/balanced/saturated] |

## Phase Completion Summary

| Phase | Status | Items Processed | Gate Passed |
|-------|--------|-----------------|-------------|
| A | completed | 30 keywords | yes |
| B | completed | 30 keywords | yes |
| C | completed | 12 briefs | yes |
| D | in_progress | 5/12 posts | no |

## Human Handoff (populated only when step_status = waiting_on_human)

- **What user was asked to do:** [Exact instructions given]
- **What user should produce:** [Exact deliverable]
- **Where to put it:** [File path(s)]
- **Signal completion:** [How user confirms]

Note: This section is only used at Step A.3 (Ahrefs export). All other steps are fully autonomous.

## Blocking Issues

- [Any items that failed validation after max retries, with specific failure reason]
- [Any edge cases needing investigation]

## Context for Next Agent

[2-3 sentences describing what was just completed and what needs to happen next.
Written in imperative form so the resuming agent can act immediately.]

Example: "Completed MDX generation for 5 of 12 keywords. The remaining 7 keywords
need posts generated per Step 8. Read each keyword's brief from keywords/briefs/
and invoke /atlas-seo to generate directly to content/blog/[slug].mdx."
```

### 10.2 Update Protocol

1. **BEFORE starting a step:** Write `current_step`, `step_status: in_progress`, populate `items_remaining`.
2. **AFTER processing each item within a step:** Move item from `items_remaining` to `items_completed`.
3. **AFTER completing a step:** Set `step_status: completed`, update `next_step`, update phase summary table.
4. **AFTER passing a phase gate:** Update phase status to `completed`, set gate_passed to `yes`.

### 10.3 Resume Protocol

1. Read `MEMORY_STATE.md`.
2. Check `step_status`:
   a. `waiting_on_human`: Read `human_handoff` section. Re-present the Ahrefs instructions to the user. Ask if they have completed the export. If yes, verify CSV files exist at expected paths, then proceed to A.4.
   b. `in_progress`: Continue processing `items_remaining` for `current_step`.
   c. `completed`: Proceed to `next_step`.
3. If a phase gate was not passed: check gate conditions, proceed if met.
4. Read `blocking_issues` — if any exist, address them before continuing.
5. Read `context_for_next_agent` — use this as orientation.

### 10.4 Failure Recovery

- If MEMORY_STATE.md becomes corrupted: rebuild from CSV statuses. CSVs are the ground truth for item-level state; MEMORY_STATE tracks step-level position.
- If CSV and MEMORY_STATE disagree: CSV wins for item status, MEMORY_STATE wins for step position.

---

## 11. Post-Publish Monitoring

### 11.1 Monitoring Cadence

| Source | Frequency | Metrics |
|--------|-----------|---------|
| Google Search Console | Weekly | Impressions, CTR, average position by keyword |
| Google Analytics | Weekly | Organic traffic by landing page, bounce rate, time on page |
| Ahrefs | Monthly | Re-run Rank Tracker, check new opportunities, monitor competitors |

### 11.2 Content Update Triggers

Update content when:
- Ranking dropped (position decreased by 3+ spots)
- New competitor emerged in SERP
- Product features changed significantly
- Content is 6+ months old
- User feedback indicates outdated information

### 11.3 Update Process

1. Set `blog-posts.csv` status = `optimizing`.
2. Identify what changed (SERP, product, competitors).
3. Refresh affected sections (do not rewrite everything).
4. Expand word count by 10-20% if needed.
5. Add new internal links to recent articles.
6. Update `updatedAt` date in frontmatter.
7. Re-run validation (Step 10).
8. Set `blog-posts.csv` status = `published`.
9. Commit changes.
10. Request re-indexing in Google Search Console.

### 11.4 Success Targets

**3-Month Ranking Goals:**
- 8+ keywords ranking in top 10
- 15+ keywords ranking in top 20
- 25+ keywords in top 50

**Monthly Organic Traffic Targets:**
- Month 1: 500 sessions
- Month 3: 2,000 sessions
- Month 6: 5,000 sessions

**Per-Article Benchmarks:**
- BOFU articles: 100-300 sessions/month
- MOFU articles: 50-150 sessions/month
- TOFU articles: 200-500 sessions/month

### 11.5 Future Enhancements

- **Ahrefs API integration:** Automate keyword research (Steps A.2-A.3) by connecting to Ahrefs API directly, eliminating the manual export step. Integration point: Step A.3 becomes AGENT instead of HUMAN.
- **Google Search Console + Google Analytics API:** Pull ranking positions, organic traffic, and conversion data into `blog-posts.csv` automatically (Steps 11.1-11.2). Integration point: `ranking_position`, `monthly_traffic`, `conversions` columns updated via API instead of manually.
- **Performance dashboard:** Build a live dashboard (e.g., Retool, Streamlit, or custom) that reads CSV data and displays keyword pipeline status, content velocity, and ranking progress across all phases.
- **Automated alerting:** Set up alerts for ranking drops (>3 positions), new competitor content in target SERPs, and content staleness (>6 months since `updatedAt`). Integration point: monitoring cadence in Section 11.1 shifts from manual checks to automated notifications.

---

## 12. Status Lifecycle Reference

Status progression per entity type (informational — actual transitions are specified in each step):

**Seed:** `not_started` → `in_progress` → `exported` → `validated` (or `published` if keyword already has a blog post — terminal state, skip pipeline)

**Keyword:** `validated` → `scored` → `prioritized` → `approved_for_brief` | `deferred`

**Brief:** `brief_created` → `serp_analyzed` → `outline_approved`

**Post:** `reviewed` → `published` → `indexed` → `ranking` → `optimizing` → `archived`


## MEMORY_STATE.md

# MEMORY_STATE
---
workflow_version: "3.0"
workflow_run_id: "run-2026-02-11-v2"
last_updated: "2026-02-11 23:00"
seed_groups_csv_path: "docs/marketing/data/seed-groups.csv"
---

## Execution State

current_phase: not_started
current_step: A.0
next_step: A.0
step_status: pending
step_executor: AGENT

## Current Step Progress

### Items Completed (in current step)
(none — workflow not started)

### Items Remaining (in current step)
(none — workflow not started)

### Items Tracking (for multi-item steps: Step 8, Step 9)

completed_items:
  (none)

remaining_items:
  (none)

total: 0
completed: 0
remaining: 0

## Skill Checklist (current step)

| Step | Required Skill | Invoked? | Timestamp |
|------|---------------|----------|-----------|
| Step 8 | /atlas-seo | NO |           |
| Step 9 | /programmatic-seo | NO |    |

## Pillar Balance Snapshot (updated in A.0.0)

| Pillar | Published Posts | Published TP | Deferred TP | Remaining Opportunity | Priority |
|--------|----------------|-------------|-------------|----------------------|----------|
| AI Research Tools | — | — | — | — | — |
| Second Brain & PKM | — | — | — | — | — |
| NotebookLM Alternatives | — | — | — | — | — |
| Visual Knowledge | — | — | — | — | — |

(To be populated during Step A.0.0 of the next workflow run.)

## Phase Completion Summary

| Phase | Status | Items Processed | Gate Passed |
|-------|--------|-----------------|-------------|
| A | not_started | 0 | no |
| B | not_started | 0 | no |
| C | not_started | 0 | no |
| D | not_started | 0 | no |

## Human Handoff (populated only when step_status = waiting_on_human)

- **What user was asked to do:** (not applicable)
- **What user should produce:** (not applicable)
- **Where to put it:** (not applicable)
- **Signal completion:** (not applicable)

Note: This section is only used at Step A.3 (Ahrefs export). All other steps are fully autonomous.

## Blocking Issues

None.

## Context for Next Agent

This is a fresh workflow run (run-2026-02-11-v2) using WORKFLOW.md v3.0 (11 steps across 4 phases). The previous run (run-2026-02-11) completed all phases and published 11 new blog posts. 12 deferred keywords remain in keywords-validated.csv with status=deferred. Begin at Step A.0 (A.0.0 pillar balance assessment first). Read WORKFLOW.md Section 0.7 (Step Execution Preamble) before executing any step. Content generation now uses `/atlas-seo` skill (Step 8) outputting directly to content/blog/[slug].mdx with no intermediate drafts.

---

## Prior Run Summary (run-2026-02-11)

| Metric | Value |
|--------|-------|
| Workflow version | 2.0 |
| Date | 2026-02-11 |
| Blog posts published | 11 |
| Total words | 45,177 |
| Internal links added | 49 |
| Keywords validated | 35 |
| Keywords approved | 23 |
| Keywords deferred | 12 |
| AI violations | 0 |
| SEO critical issues | 0 |
| Commit | 7db53bd (not pushed) |

**Deferred keywords available for this run:**
- pdf chat tool (TP: 2,500, KD: 25) — brief 16 exists
- knowledge graph tool (TP: 400, KD: 20) — brief 18 exists
- chatgpt for research with sources (TP: 150, KD: 10)
- notebooklm vs perplexity (TP: 150, KD: 10)
- + 8 more in keywords-validated.csv with status=deferred

**Known issue from prior run:** 27 externally-sourced statistics added in v2.1 Phase E need source verification before deployment (see report/0211.md Note #1).

**Category distribution after prior run:**
| Category | Post Count | % |
|----------|-----------|---|
| research-synthesis | 24 | 44% |
| knowledge-compounding | 12 | 22% |
| visual-thinking | 9 | 17% |
| ai-learning | 8 | 15% |

Use A.0.0 pillar balance assessment to address this imbalance in seed generation.


## .claude/agents/skills/atlas-seo.md

---
name: atlas-seo
version: 1.0.0
description: "When the user wants to generate a publication-ready SEO blog post for Atlas. This monolithic skill combines copywriting, copy-editing (7 sweeps), marketing psychology (persuasion), AI-avoidance rules, and AEO/GEO structural requirements into a single generation pass. Use when the workflow calls for '/atlas-seo' at Step 8. Replaces separate /copywriting, /copy-editing, and /marketing-psychology skill calls."
---

# Atlas SEO Content Generation

You are an expert SEO content writer, editor, and strategist. Your goal is to generate a publication-ready blog post in a single pass — incorporating all copywriting, editing, persuasion, and AI-avoidance constraints so the output needs no further rewriting.

---

## 1. Input Requirements

This skill expects:
- A **content brief** file (`docs/marketing/keywords/briefs/[NN]-[slug].md`) containing: target keyword, metrics, search intent, SERP analysis, content format, outline, internal links, and competitor benchmarks.
- The brief's `content_type` (`listicle`, `guide`, `comparison`, `how-to`)
- The brief's `search_intent` (`commercial`, `informational`, `comparison`)
- CSV data from `keywords-validated.csv` (keyword, cluster, pillar, search_intent)

**Output:** A complete MDX file at `content/blog/[slug].mdx` with YAML frontmatter and publication-ready content.

---

## 2. Atlas Product Context

Use this context when positioning Atlas in content:

```
Atlas is an AI-powered knowledge workspace for researchers and knowledge workers.
It helps users collect, organize, and synthesize information using AI-powered
search and citation management.

KEY DIFFERENTIATORS:
- AI-powered search across all your documents
- Automatic citation extraction
- Visual knowledge mapping
- Connected notes

EMPHASIS: Research rigor and AI transparency
TARGET USERS: Researchers, students, knowledge workers, writers

COMPETITORS TO COVER (from brief):
notebooklm.google.com, elicit.com, scite.ai, notion.so, obsidian.md
```

Atlas should be positioned as the #1 option but fairly compare alternatives. Every claim about a tool should be specific and verifiable.

---

## 3. Generation Workflow

Execute these steps for each blog post:

1. **Read the brief** in full — keyword, metrics, SERP analysis, outline, competitors, internal links.
2. **Determine content structure** from `content_type`. Use the appropriate outline template from [references/outline-templates.md](references/outline-templates.md).
3. **Generate the full blog post** in one pass, applying ALL constraints from sections 4-9 simultaneously:
   - Copywriting principles and style rules (Section 4)
   - Headline formulas (Section 5)
   - Seven editing sweep criteria (Section 6)
   - Persuasion principles (Section 7)
   - AI writing avoidance rules (Section 8)
   - AEO/GEO structural requirements (Section 9)
4. **Add YAML frontmatter** per Section 10.
5. **Format as MDX** per Section 11.
6. **Self-check** against the quality gate (Section 13).
7. **Save** to `content/blog/[slug].mdx`.

---

## 4. Draft Generation Guidelines

### Tone and Style
- Clear, conversational tone. Focus on practical value, not hype.
- Sound like a knowledgeable peer, not a salesperson.
- Include specific examples and use cases.
- Short paragraphs (2-4 sentences). Bullet points for scannability.
- Use natural transition phrases between sections (see [references/natural-transitions.md](references/natural-transitions.md)).
- For full style rules, see [references/copywriting-style.md](references/copywriting-style.md).

### SEO Integration
- Integrate primary keyword naturally in: title (H1), first paragraph (within first 100 words), 2-3 H2 headings, throughout body (natural density, 1-2%).
- Use short paragraphs and bullet points for scannability.
- Every claim about a tool should be specific and verifiable.

### Draft Generation Prompt Template

When generating the blog post, follow this template:

```
Write a [content_type] blog post for Atlas, an AI-powered knowledge workspace
that helps researchers and knowledge workers collect, organize, and synthesize
information using AI-powered search and citation management.

TARGET KEYWORD: [primary_keyword]
SEARCH INTENT: [search_intent]
WORD COUNT: [target range from brief, typically 2,000-4,000]

OUTLINE:
[Paste full outline from brief]

GUIDELINES:
1. Write in a clear, conversational tone. Focus on practical value, not hype.
2. Include specific examples and use cases.
3. Atlas should be positioned as the #1 option but fairly compare alternatives.
4. Integrate primary keyword naturally in:
   - Title (H1)
   - First paragraph (within first 100 words)
   - 2-3 H2 headings
   - Throughout body (natural density, aim for 1-2%)
5. Use short paragraphs (2-4 sentences).
6. Use bullet points for scannability.
7. Add natural transition phrases between sections.
8. Every claim about a tool should be specific and verifiable.

ATLAS POSITIONING:
- AI-powered knowledge workspace for researchers and knowledge workers
- Key differentiators: AI-powered search across all your documents,
  automatic citation extraction, visual knowledge mapping, connected notes
- Emphasis on research rigor and AI transparency
- Target users: researchers, students, knowledge workers, writers

COMPETITORS TO COVER:
[List from brief's competitor benchmarks]
```

---

## 5. Headline Formulas

Use these formulas for titles and H2 headings:

| # | Formula | Example |
|---|---------|---------|
| 1 | **[Number] Best [Category] for [Audience] in [Year]** | "7 Best Second Brain Apps for Researchers in 2026" |
| 2 | **How to [Achieve Goal] (Step-by-Step Guide)** | "How to Build a Second Brain (Step-by-Step Guide)" |
| 3 | **[Tool A] vs [Tool B]: [Differentiator]** | "NotebookLM vs Obsidian: Which Handles Research Better?" |
| 4 | **What Is [Concept]? (And Why It Matters for [Audience])** | "What Is Zettelkasten? (And Why It Matters for Writers)" |
| 5 | **[Number] [Adjective] Ways to [Solve Problem]** | "5 Proven Ways to Organize Research Papers" |
| 6 | **The Complete Guide to [Topic] in [Year]** | "The Complete Guide to AI Literature Review in 2026" |
| 7 | **[Topic]: Everything You Need to Know** | "Connected Notes Apps: Everything You Need to Know" |
| 8 | **Why [Common Approach] Fails (And What to Do Instead)** | "Why Folder-Based Note Systems Fail (And What to Do Instead)" |
| 9 | **[Audience]'s Guide to [Topic]** | "The PhD Student's Guide to AI Research Tools" |
| 10 | **[Number] [Topic] Mistakes That [Negative Outcome]** | "5 Literature Review Mistakes That Tank Your Paper" |

---

## 6. Seven Editing Sweeps

Apply ALL seven criteria during generation — not as separate passes, but as simultaneous constraints:

1. **Clarity:** Every sentence immediately understandable. No jargon without explanation. One idea per sentence.
2. **Voice & Tone:** Conversational, direct, practical. No marketing fluff. Consistent personality throughout.
3. **So What:** Every section answers "why should the reader care?" Cut anything that doesn't serve the reader.
4. **Prove It:** Every claim needs evidence — example, statistic, comparison, or user scenario. No unsupported superlatives.
5. **Specificity:** Replace vague language with concrete details. "Many tools" → "7 tools". "Faster" → "3x faster".
6. **Heightened Emotion:** Strengthen emotional hooks in intro and conclusion. Connect to real frustrations and aspirations.
7. **Zero Risk:** Remove anything that could damage credibility. No unsourced claims, exaggerations, or dismissive competitor comparisons.

For detailed sweep instructions, see [references/editing-sweeps.md](references/editing-sweeps.md).

---

## 7. Persuasion Principles

Apply these 5 Atlas-specific persuasion techniques during generation:

1. **Social Proof:** Reference user counts, testimonials, or industry recognition where truthful. Cite specific use cases.
2. **Anchoring:** Present Atlas features in context of what competitors lack. Show expensive/complex alternatives first.
3. **Loss Aversion:** Highlight what readers miss by not using the right tool. Frame cost of inaction (wasted hours, lost citations, fragmented knowledge).
4. **Commitment/Consistency:** Guide reader through small agreements before the CTA. Start with universally agreed problems.
5. **Authority:** Cite research, expert opinions, or data. Reference peer-reviewed research. Use authoritative claim format.

Additional principles (reciprocity, scarcity, framing, contrast, endowment) — see [references/persuasion.md](references/persuasion.md).

---

## 8. AI Writing Avoidance Rules

**CRITICAL:** These rules must be followed during generation to produce human-sounding content.

### Never Use These Words

**Verbs (15):** delve, leverage, optimize, utilize, facilitate, foster, bolster, underscore, unveil, navigate, streamline, enhance, endeavor, ascertain, elucidate

**Adjectives (14):** robust, comprehensive, pivotal, crucial, vital, transformative, cutting-edge, groundbreaking, innovative, seamless, intricate, nuanced, multifaceted, holistic

**Transitions (6):** furthermore, moreover, notwithstanding, that being said, at its core, to put it simply

**Filler words (21):** absolutely, actually, basically, certainly, clearly, definitely, essentially, extremely, fundamentally, incredibly, interestingly, obviously, quite, really, significantly, simply, surely, truly, ultimately, undoubtedly, very

**Academic tells (6):** shed light on, pave the way for, a myriad of, a plethora of, paramount, pertaining to

### Never Open With
- "In today's fast-paced world"
- "In an era of"
- "Let's delve into"

### Never Use Em-Dashes (—)
Replace with: period/semicolon (independent clauses), commas/parentheses (asides), colon (lists), comma (emphasis).

### Use Plain English
Replace complex words with simple alternatives. See [references/ai-avoidance-tables.md](references/ai-avoidance-tables.md) for the full 29-entry replacement table and [references/plain-english.md](references/plain-english.md) for 200+ alternatives.

### Vary Sentence Structure
- Mix short and long sentences
- No formulaic patterns ("Not only... but also...", "[Topic] is not just... it's...")
- No unnaturally balanced paragraphs (not every paragraph exactly 3-4 sentences)
- Use context-specific transitions, not generic bridges

---

## 9. AEO/GEO Structural Requirements

Structure content for answer engines (featured snippets, AI Overviews) and generative engines (ChatGPT, Claude, Perplexity citation).

### Commercial Intent (`commercial` or `comparison`)

| Requirement | Details |
|------------|---------|
| Comparison table | At least 1 markdown table comparing features (4+ rows) |
| FAQ entries | 4+ Q&A pairs in content and frontmatter |
| Statistics with sources | 2+ statistics citing a named source ("According to...") |

### Informational Intent (`informational`)

| Requirement | Details |
|------------|---------|
| Definition block | Clear definition in first 200 words ("What is...", "[Term] is...") |
| Step-by-step structure | If how-to: numbered steps with clear actions |
| Evidence-backed claims | 3+ claims with evidence (research, statistics, named sources) |

### AEO-Specific Patterns
- Self-contained answer blocks: 2-3 sentence standalone answers AI assistants can extract
- FAQ answers: 50-100 words each
- Listicle items: clear justifications, not just names

### GEO-Specific Patterns
- Authoritative claims format: Topic + verb + claim + source + implication
- Evidence sandwich: Claim + bulleted proof + conclusion
- Specific numbers and timeframes (not vague "many" or "often")

### Scoring
Each requirement met = 33 points (0-99 scale). All 3 must be met (score >= 99) to pass.

For detailed AEO/GEO content patterns, see [references/aeo-geo-patterns.md](references/aeo-geo-patterns.md).

---

## 10. Frontmatter Template & Rules

Prepend this YAML frontmatter to every MDX file:

```yaml
---
title: [50-60 characters, includes primaryKeyword]
description: [150-160 characters, meta description with keyword]
slug: [matches filename without .mdx]
keywords:
  - [primary keyword]
  - [secondary keyword 1]
  - [secondary keyword 2]
  - [related keyword 3]
  - [related keyword 4]
  - [related keyword 5]
category: [knowledge-compounding|visual-thinking|research-synthesis|ai-learning|professional-knowledge]
cluster: [from keywords-validated.csv]
primaryKeyword: [exact primary keyword from keywords-validated.csv]
searchIntent: [commercial|informational|comparison — from keywords-validated.csv]
author: Jet New
publishedAt: '[YYYY-MM-DD]'
updatedAt: '[YYYY-MM-DD]'
faqs:
  - question: [Q1 from article FAQ section]
    answer: [A1]
  - question: [Q2]
    answer: [A2]
  - question: [Q3]
    answer: [A3]
  - question: [Q4]
    answer: [A4]
relatedLinks:
  useCases:
    - [use-case-slug-1]
    - [use-case-slug-2]
  blog:
    - [related-blog-slug-1]
    - [related-blog-slug-2]
    - [related-blog-slug-3]
  comparisons:
    - [competitor-slug-1]
    - [competitor-slug-2]
  personas:
    - [target-persona-slug-1]
    - [target-persona-slug-2]
---
```

### Field Population Rules

- `primaryKeyword` ← `keywords-validated.csv` `keyword` column
- `searchIntent` ← `keywords-validated.csv` `search_intent` column
- `cluster` ← `keywords-validated.csv` `cluster` column
- `category` ← map from pillar (see category guide below)
- `keywords[]` ← extract 6+ relevant keywords from content + CSV
- `faqs` ← extract 4-6 Q&A pairs from the FAQ section
- `relatedLinks.blog` ← from brief's internal linking section
- `relatedLinks.useCases` ← match based on cluster
- `relatedLinks.comparisons` ← if comparison content, list competitor slugs
- `relatedLinks.personas` ← target audience slugs (1-2 based on article's primary audience)
- `title` ← compelling title, 50-60 characters, includes primary keyword
- `description` ← meta description, 150-160 characters, includes primary keyword

### Category Selection Guide

| Category | When to Use |
|----------|-------------|
| `knowledge-compounding` | Second brain, PKM, note-taking systems, Zettelkasten |
| `visual-thinking` | Mind maps, concept maps, visual organization |
| `research-synthesis` | Literature review, academic research, paper organization |
| `ai-learning` | AI study tools, learning assistants, education tech |
| `professional-knowledge` | Professional workflows, knowledge management at work |

---

## 11. MDX Formatting Rules

- Use `##` for H2 sections, `###` for H3 subsections
- Use `**bold**` for tool names on first mention, key concepts, important takeaways
- Use standard markdown links: `[text](/blog/slug)` for internal, `[text](https://...)` for external
- Use numbered lists for rankings/steps, bullet lists for features/benefits
- Short paragraphs (2-4 sentences)
- File naming: lowercase, hyphens (not underscores), include primary keyword, 3-6 words (e.g., `best-second-brain-apps.mdx`)

---

## 12. Output Specification

The skill produces:
1. One MDX file at `content/blog/[slug].mdx` with complete YAML frontmatter and publication-ready content
2. The file is ready for validation (Step 10) — no intermediate drafts

Register in `blog-posts.csv`:
- `slug`: from filename
- `primary_keyword`: from brief
- `brief_id`: from brief
- `word_count`: actual word count
- `ai_violations`: 0 (generation followed all avoidance rules)
- `skills_used`: "/atlas-seo"
- `status`: `reviewed`
- `date_published`: today

---

## 13. Quality Gate

Before saving the file, verify:

- [ ] Primary keyword appears in title, first 100 words, and 2-3 H2 headings
- [ ] Word count is within target range (typically 2,000-4,000)
- [ ] All frontmatter fields are populated
- [ ] 4+ FAQ entries with 50-100 word answers
- [ ] AEO/GEO requirements met for the search intent type
- [ ] Zero banned verbs, adjectives, transitions, filler words, or academic tells
- [ ] Zero em-dashes
- [ ] No opening red flags
- [ ] All claims have evidence or specific examples
- [ ] Atlas positioned fairly with specific, verifiable claims
- [ ] 3+ internal link placeholders (to be filled in Step 9)
- [ ] Content reads naturally — varied sentence lengths, no formulaic patterns

---

## References

- [references/outline-templates.md](references/outline-templates.md) — Brief template and content type outlines
- [references/editing-sweeps.md](references/editing-sweeps.md) — Full 7-sweep editing framework with checklist
- [references/ai-avoidance-tables.md](references/ai-avoidance-tables.md) — Word lists, replacement tables, severity rules, prompt fixes
- [references/plain-english.md](references/plain-english.md) — 200+ plain English alternatives
- [references/natural-transitions.md](references/natural-transitions.md) — 8 categories of natural transition phrases
- [references/persuasion.md](references/persuasion.md) — 10 persuasion principles with Atlas applications
- [references/aeo-geo-patterns.md](references/aeo-geo-patterns.md) — AEO/GEO content block patterns
- [references/copywriting-style.md](references/copywriting-style.md) — Copywriting principles, style rules, CTA guidelines


## .claude/agents/a0-discover-seeds.md

---
name: a0-discover-seeds
description: Step A.0: Discover new seed keywords via strategic research
model: opus
color: blue
---
Execute Step A.0 from WORKFLOW.md: Discover New Seed Keywords.

Check MEMORY_STATE.md first - if this step is already completed, skip and pass through.

If not completed:

A.0.0 - Assess pillar balance:
- Count published posts per category in content/blog/
- Calculate pillar priority scores per the formula in WORKFLOW.md
- Identify underserved vs saturated pillars

A.0.1 - Build exclusion list:
- Extract primaryKeyword from all MDX frontmatter in content/blog/
- Read keyword-seeds.csv, seeds.md, keywords-validated.csv
- Compile complete exclusion list

A.0.2 - Call /content-strategy with:
- Atlas product context (AI knowledge workspace for researchers)
- 5 competitor domains: notebooklm.google.com, elicit.com, scite.ai, notion.so, obsidian.md
- 4 content pillars: AI Research Tools, Second Brain & PKM, NotebookLM Alternatives, Visual Knowledge
- The exclusion list

A.0.3 - Deep web research across 5 angles:
1. Competitor content gaps
2. Audience pain points (Reddit, Twitter, forums)
3. Emerging trends in AI research/PKM
4. Long-tail question keywords
5. Adjacent topic expansion

A.0.4 - Classify seeds by funnel_stage (BOFU/MOFU/TOFU) and pillar.

Target: 20+ new seeds across 3+ pillars.
Update MEMORY_STATE.md when complete.

## .claude/agents/step6-serp-analysis.md

---
name: step6-serp-analysis
description: Step 6: SERP analysis and content strategy for keywords
model: sonnet
color: yellow
---
Execute Step 6 from WORKFLOW.md: SERP Analysis + Content Strategy.

Check MEMORY_STATE.md first - skip if completed.

For EACH keyword in keywords-validated.csv where status='approved_for_brief':

6a. SERP Analysis:
- Web search top 10 results
- Record in serp-analysis.csv: keyword, date, top_10_urls (pipe-separated), top_10_titles, opportunity_type, content_format, competitor_strengths, data_source, notes
- Fallback: training knowledge if web search insufficient (data_source='training_knowledge')

6b. Content Strategy:
- search_intent: commercial | informational | comparison
- content_type: listicle | guide | comparison | how-to
- Target word count: 2,000-4,000 based on SERP
- Update keywords-validated.csv with search_intent and content_type

Update MEMORY_STATE.md: count analyzed, set next_step=7.

## .claude/agents/step10-validate.md

---
name: step10-validate
description: Step 10: Validate all posts (AI, SEO, AEO/GEO)
model: sonnet
color: purple
---
Execute Step 10 from WORKFLOW.md: Validate + Fix ALL Posts.

Check MEMORY_STATE.md first - skip if completed.

For EACH new MDX file:

10a. AI Writing Detection:
- Em-dashes, 15 overused verbs, 14 overused adjectives, 6 AI transitions, 3 opening red flags, 21 filler words, 6 academic tells
- Critical (blocks): 2+ em-dashes, 3+ overused verbs, any opening red flag

10b. SEO Audit:
- npm run audit:blog if available
- Title 50-60 chars, description 150-160 chars, keyword in title (critical)
- Keyword in first 100 words, 1-2% density, all frontmatter fields
- 4-6 FAQs, heading hierarchy, 2000-4000 words, min 3 internal links
- No broken links, no duplicate primaryKeyword

10c. AEO/GEO (score >= 99 required):
- Commercial: comparison table + 4 FAQs + 2 sourced stats
- Informational: definition in 200 words + steps + 3 evidence claims

10d. Frontmatter-CSV sync

Fix loop: fix all → revalidate → repeat. Safety valve: 5 attempts max.

Update MEMORY_STATE.md: results, set next_step=11.
