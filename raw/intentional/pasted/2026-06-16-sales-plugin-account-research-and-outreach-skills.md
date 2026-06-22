---
type: raw_capture
source_type: pasted
title: "Sales plugin account research and outreach skills"
url: "/Users/sethlim/Documents/sales"
collected_at: 2026-06-16T04:58:44Z
published_at: "Unknown"
capture_quality: complete
status: raw
trust_lane: intentional
---

# Sales plugin account research and outreach skills

Source: /Users/sethlim/Documents/sales

## Capture Text

## Sales plugin README

Source file: `/Users/sethlim/Documents/sales/README.md`

```markdown
# Sales Plugin

A sales productivity plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Helps with prospecting, outreach, pipeline management, call preparation, and deal strategy. Works with any sales team — standalone with web search and your input, supercharged when you connect your CRM, email, and other tools.

## Installation

```bash
claude plugins add knowledge-work-plugins/sales
```

## Commands

Explicit workflows you invoke with a slash command:

| Command | Description |
|---|---|
| `/call-summary` | Process call notes or transcript — extract action items, draft follow-up, generate internal summary |
| `/forecast` | Generate a weighted sales forecast — upload CSV or describe your pipeline, set quota, get projections |
| `/pipeline-review` | Analyze pipeline health — prioritize deals, flag risks, get weekly action plan |

All commands work **standalone** (paste notes, upload CSV, or describe your situation) and get **supercharged** with MCP connectors.

## Skills

Domain knowledge Claude uses automatically when relevant:

| Skill | Description |
|---|---|
| `account-research` | Research a company or person — web search for company intel, key contacts, recent news, hiring signals |
| `call-prep` | Prepare for sales calls — account context, attendee research, suggested agenda, discovery questions |
| `daily-briefing` | Prioritized daily sales briefing — meetings, pipeline alerts, email priorities, suggested actions |
| `draft-outreach` | Research-first outreach — research the prospect, then draft personalized email and LinkedIn messages |
| `competitive-intelligence` | Research competitors — product comparison, pricing intel, recent releases, differentiation matrix, sales talk tracks |
| `create-an-asset` | Generate custom sales assets — landing pages, decks, one-pagers, workflow demos tailored to your prospect |

## Example Workflows

### After a Call

```
/call-summary
```

Paste your notes or transcript. Get a structured summary, action items with owners, and a draft follow-up email. If CRM is connected, offers to log the activity and create tasks.

### Weekly Forecast

```
/forecast
```

Upload a CSV export from your CRM (or paste your deals). Tell me your quota and timeline. Get a weighted forecast with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis.

### Pipeline Review

```
/pipeline-review
```

Upload a CSV or describe your pipeline. Get a health score, deal prioritization, risk flags (stale deals, past close dates, single-threaded), and a weekly action plan.

### Researching a Prospect

Just ask naturally:
```
Research Acme Corp before my call tomorrow
```

The `account-research` skill triggers automatically and gives you company overview, key contacts, recent news, and recommended approach.

### Drafting Outreach

```
Draft an email to the VP of Engineering at TechStart
```

The `draft-outreach` skill researches the prospect first, then generates personalized outreach with multiple angles.

### Competitive Intel

```
How do we compare to Competitor X?
```

The `competitive-intelligence` skill researches both companies and builds a differentiation matrix with talk tracks.

## Standalone + Supercharged

Every command and skill works without any integrations:

| What You Can Do | Standalone | Supercharged With |
|-----------------|------------|-------------------|
| Process call notes | Paste notes/transcript | Transcripts MCP (e.g. Gong, Fireflies) |
| Forecast pipeline | Upload CSV, paste deals | CRM MCP |
| Review pipeline | Upload CSV, describe deals | CRM MCP |
| Research prospects | Web search | Enrichment MCP (e.g. Clay, ZoomInfo) |
| Prep for calls | Describe meeting | CRM, Email, Calendar MCPs |
| Draft outreach | Web search + your context | CRM, Email MCPs |
| Competitive intel | Web search | CRM (win/loss data), Docs (battlecards) |

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

Connect your tools for a richer experience:

| Category | Examples | What It Enables |
|---|---|---|
| **CRM** | HubSpot, Close | Pipeline data, account history, contact records |
| **Transcripts** | Fireflies, Gong, Chorus | Call recordings, transcripts, key moments |
| **Enrichment** | Clay, ZoomInfo, Apollo | Company and contact data enrichment |
| **Chat** | Slack, Teams | Internal discussions, colleague intel |

See [CONNECTORS.md](CONNECTORS.md) for the full list of supported integrations, including email, calendar, and additional CRM options.

## Settings

Create a `settings.local.json` file to personalize:

- **Cowork**: Save it in any folder you've shared with Cowork (via the folder picker). The plugin finds it automatically.
- **Claude Code**: Save it at `sales/.claude/settings.local.json`.

```json
{
  "name": "Your Name",
  "title": "Account Executive",
  "company": "Your Company",
  "quota": {
    "annual": 1000000,
    "quarterly": 250000
  },
  "product": {
    "name": "Your Product",
    "value_props": [
      "Key value proposition 1",
      "Key value proposition 2"
    ],
    "competitors": [
      "Competitor A",
      "Competitor B"
    ]
  }
}
```

The plugin will ask you for this information interactively if it's not configured.
```

## Account research skill

Source file: `/Users/sethlim/Documents/sales/skills/account-research/SKILL.md`

```markdown
---
name: account-research
description: Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Trigger with "research [company]", "look up [person]", "intel on [prospect]", "who is [name] at [company]", or "tell me about [company]".
---

# Account Research

Get a complete picture of any company or person before outreach. This skill always works with web search, and gets significantly better with enrichment and CRM data.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ACCOUNT RESEARCH                             │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone via web search)                        │
│  ✓ Company overview: what they do, size, industry               │
│  ✓ Recent news: funding, leadership changes, announcements      │
│  ✓ Hiring signals: open roles, growth indicators                │
│  ✓ Key people: leadership team from LinkedIn                    │
│  ✓ Product/service: what they sell, who they serve              │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Enrichment: verified emails, phone, tech stack, org chart    │
│  + CRM: prior relationship, past opportunities, contacts        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

Just tell me who to research:

- "Research Stripe"
- "Look up the CTO at Notion"
- "Intel on acme.com"
- "Who is Sarah Chen at TechCorp?"
- "Tell me about [company] before my call"

I'll run web searches immediately. If you have enrichment or CRM connected, I'll pull that data too.

---

## Connectors (Optional)

Connect your tools to supercharge this skill:

| Connector | What It Adds |
|-----------|--------------|
| **Enrichment** | Verified emails, phone numbers, tech stack, org chart, funding details |
| **CRM** | Prior relationship history, past opportunities, existing contacts, notes |

> **No connectors?** No problem. Web search provides solid research for any company or person.

---

## Output Format

```markdown
# Research: [Company or Person Name]

**Generated:** [Date]
**Sources:** Web Search [+ Enrichment] [+ CRM]

---

## Quick Take

[2-3 sentences: Who they are, why they might need you, best angle for outreach]

---

## Company Profile

| Field | Value |
|-------|-------|
| **Company** | [Name] |
| **Website** | [URL] |
| **Industry** | [Industry] |
| **Size** | [Employee count] |
| **Headquarters** | [Location] |
| **Founded** | [Year] |
| **Funding** | [Stage + amount if known] |
| **Revenue** | [Estimate if available] |

### What They Do
[1-2 sentence description of their business, product, and customers]

### Recent News
- **[Headline]** — [Date] — [Why it matters for your outreach]
- **[Headline]** — [Date] — [Why it matters]

### Hiring Signals
- [X] open roles in [Department]
- Notable: [Relevant roles like Engineering, Sales, AI/ML]
- Growth indicator: [Hiring velocity interpretation]

---

## Key People

### [Name] — [Title]
| Field | Detail |
|-------|--------|
| **LinkedIn** | [URL] |
| **Background** | [Prior companies, education] |
| **Tenure** | [Time at company] |
| **Email** | [If enrichment connected] |

**Talking Points:**
- [Personal hook based on background]
- [Professional hook based on role]

[Repeat for relevant contacts]

---

## Tech Stack [If Enrichment Connected]

| Category | Tools |
|----------|-------|
| **Cloud** | [AWS, GCP, Azure, etc.] |
| **Data** | [Snowflake, Databricks, etc.] |
| **CRM** | [e.g. Salesforce, HubSpot] |
| **Other** | [Relevant tools] |

**Integration Opportunity:** [How your product fits with their stack]

---

## Prior Relationship [If CRM Connected]

| Field | Detail |
|-------|--------|
| **Status** | [New / Prior prospect / Customer / Churned] |
| **Last Contact** | [Date and type] |
| **Previous Opps** | [Won/Lost and why] |
| **Known Contacts** | [Names already in CRM] |

**History:** [Summary of past relationship]

---

## Qualification Signals

### Positive Signals
- ✅ [Signal and evidence]
- ✅ [Signal and evidence]

### Potential Concerns
- ⚠️ [Concern and what to watch for]

### Unknown (Ask in Discovery)
- ❓ [Gap in understanding]

---

## Recommended Approach

**Best Entry Point:** [Person and why]

**Opening Hook:** [What to lead with based on research]

**Discovery Questions:**
1. [Question about their situation]
2. [Question about pain points]
3. [Question about decision process]

---

## Sources
- [Source 1](URL)
- [Source 2](URL)
```

---

## Execution Flow

### Step 1: Parse Request

```
Identify what to research:
- "Research Stripe" → Company research
- "Look up John Smith at Acme" → Person + company
- "Who is the CTO at Notion" → Role-based search
- "Intel on acme.com" → Domain-based lookup
```

### Step 2: Web Search (Always)

```
Run these searches:
1. "[Company name]" → Homepage, about page
2. "[Company name] news" → Recent announcements
3. "[Company name] funding" → Investment history
4. "[Company name] careers" → Hiring signals
5. "[Person name] [Company] LinkedIn" → Profile info
6. "[Company name] product" → What they sell
7. "[Company name] customers" → Who they serve
```

**Extract:**
- Company description and positioning
- Recent news (last 90 days)
- Leadership team
- Open job postings
- Technology mentions
- Customer base

### Step 3: Enrichment (If Connected)

```
If enrichment tools available:
1. Enrich company → Firmographics, funding, tech stack
2. Search people → Org chart, contact list
3. Enrich person → Email, phone, background
4. Get signals → Intent data, hiring velocity
```

**Enrichment adds:**
- Verified contact info
- Complete org chart
- Precise employee count
- Detailed tech stack
- Funding history with investors

### Step 4: CRM Check (If Connected)

```
If CRM available:
1. Search for account by domain
2. Get related contacts
3. Get opportunity history
4. Get activity timeline
```

**CRM adds:**
- Prior relationship context
- What happened before (won/lost deals)
- Who we've talked to
- Notes and history

### Step 5: Synthesize

```
1. Combine all sources
2. Prioritize enrichment data over web (more accurate)
3. Add CRM context if exists
4. Identify qualification signals
5. Generate talking points
6. Recommend approach
```

---

## Research Variations

### Company Research
Focus on: Business overview, news, hiring, leadership

### Person Research
Focus on: Background, role, LinkedIn activity, talking points

### Competitor Research
Focus on: Product comparison, positioning, win/loss patterns

### Pre-Meeting Research
Focus on: Attendee backgrounds, recent news, relationship history

---

## Tips for Better Research

1. **Include the domain** — "research acme.com" is more precise
2. **Specify the person** — "look up Jane Smith, VP Sales at Acme"
3. **State your goal** — "research Stripe before my demo call"
4. **Ask for specifics** — "what's their tech stack?" after initial research

---

## Related Skills

- **call-prep** — Full meeting prep with this research plus context
- **draft-outreach** — Write personalized message based on research
- **prospecting** — Qualify and prioritize research targets
```

## Draft outreach skill

Source file: `/Users/sethlim/Documents/sales/skills/draft-outreach/SKILL.md`

```markdown
---
name: draft-outreach
description: Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]".
---

# Draft Outreach

Research first, then draft. This skill never sends generic outreach - it always researches the prospect first to personalize the message. Works standalone with web search, supercharged when you connect your tools.

## Connectors (Optional)

| Connector | What It Adds |
|-----------|--------------|
| **Enrichment** | Verified email, phone, background details |
| **CRM** | Prior relationship context, existing contacts |
| **Email** | Create draft directly in your inbox |

> **No connectors?** Web research works great. I'll output the email text for you to copy.

---

## How It Works

```
+------------------------------------------------------------------+
|                      DRAFT OUTREACH                               |
|                                                                   |
|  Step 1: RESEARCH (always happens first)                         |
|  - Web search (default)                                           |
|  - + Enrichment (if enrichment tools connected)                  |
|  - + CRM (if CRM connected)                                      |
|                                                                   |
|  Step 2: DRAFT (based on research)                               |
|  - Personalized opening (from research)                          |
|  - Relevant hook (their priorities)                              |
|  - Clear CTA                                                      |
|                                                                   |
|  Step 3: DELIVER (based on connectors)                           |
|  - Email draft (if email connected)                              |
|  - Copy for LinkedIn (always)                                    |
|  - Output to user (always)                                        |
+------------------------------------------------------------------+
```

---

## Output Format

```markdown
# Outreach Draft: [Person] @ [Company]
**Generated:** [Date] | **Research Sources:** [Web, Enrichment, CRM]

---

## Research Summary

**Target:** [Name], [Title] at [Company]
**Hook:** [Why reaching out now - the personalized angle]
**Goal:** [What you want from this outreach]

---

## Email Draft

**To:** [email if known, or "find email" note]
**Subject:** [Personalized subject line]

---

[Email body]

---

**Subject Line Alternatives:**
1. [Option 2]
2. [Option 3]

---

## LinkedIn Message (if no email)

**Connection Request (< 300 chars):**
[Short, no-pitch connection request]

**Follow-up Message (after connected):**
[Value-first message]

---

## Why This Approach

| Element | Based On |
|---------|----------|
| Opening | [Research finding that makes it personal] |
| Hook | [Their priority/pain point] |
| Proof | [Relevant customer story] |
| CTA | [Low-friction ask] |

---

## Email Draft Status

[Draft created - check ~~email]
[Email not connected - copy email above]
[No email found - use LinkedIn approach]

---

## Follow-up Sequence (Optional)

**Day 3 - Follow-up 1:**
[Short, new angle]

**Day 7 - Follow-up 2:**
[Different value prop]

**Day 14 - Break-up:**
[Final attempt]
```

---

## Execution Flow

### Step 1: Parse Request

```
Input patterns:
- "draft outreach to John Smith at Acme" → Person + company
- "write cold email to Acme's CTO" → Role + company
- "reach out to sarah@acme.com" → Email provided
- "LinkedIn message to [LinkedIn URL]" → Profile provided
```

### Step 2: Research First (Always)

**Use research-prospect skill internally:**
```
1. Web search for company + person
2. If Enrichment connected: Get verified contact info, background
3. If CRM connected: Check for prior relationship
```

**Must find before drafting:**
- Who they are (title, background)
- What the company does
- Recent news or trigger
- Personalization hook

### Step 3: Identify Hook

```
Priority order for hooks:
1. Trigger event (funding, hiring, news) → Most timely
2. Mutual connection → Social proof
3. Their content (post, article, talk) → Shows you did research
4. Company initiative → Relevant to their priorities
5. Role-based pain point → Least personal but still relevant
```

### Step 4: Draft Message

**Email Structure (AIDA):**
```
SUBJECT: [Personalized, <50 chars, no spam words]

[Opening: Personal hook - shows you researched them]

[Interest: Their problem/opportunity in 1-2 sentences]

[Desire: Brief proof point - similar company result]

[Action: Clear, low-friction CTA]

[Signature]
```

**LinkedIn Connection Request (<300 chars):**
```
Hi [Name], [Mutual connection/shared interest/genuine compliment].
Would love to connect. [No pitch]
```

**LinkedIn Follow-up Message:**
```
Thanks for connecting! [Value-first: insight, article, observation]

[Soft transition to why you reached out]

[Question, not pitch]
```

### Step 5: Create Email Draft

```
If email connector available:
1. Create draft with to, subject, body
2. Return draft link
3. Note: "Draft created - review and send"

If not available:
1. Output email text
2. Note: "Copy to your email client"
```

---

## Capability by Connector

| Capability | Web Only | + Enrichment | + CRM | + Email |
|------------|----------|--------------|-------|---------|
| Personalized opening | Basic | Deep | With history | Same |
| Verified email | No | Yes | Yes | Yes |
| Background details | Public only | Full | Full | Full |
| Prior relationship | No | No | Yes | Yes |
| Auto-create draft | No | No | No | Yes |

---

## Message Templates by Scenario

### Cold Outreach (No Prior Relationship)

```
Subject: [Their initiative] + [your angle]

Hi [Name],

[Personal hook based on research - news, content, mutual connection].

[1 sentence on their likely challenge based on role/company].

[Brief proof: "We helped [Similar Company] achieve [Result]".]

Worth a 15-min call to see if relevant?

[Signature]
```

### Warm Outreach (Have Met / Mutual Connection)

```
Subject: Following up from [context]

Hi [Name],

[Reference to how you know them / who connected you].

[Why reaching out now - their trigger].

[Specific value you can offer].

[CTA]
```

### Re-Engagement (Went Dark)

```
Subject: [Short, curiosity-driven]

Hi [Name],

[Acknowledge time passed without being guilt-trippy].

[New reason to reconnect - their news or your news].

[Simple question to re-open dialogue].

[Signature]
```

### Post-Event Follow-up

```
Subject: Great meeting you at [Event]

Hi [Name],

[Specific memory from conversation].

[Value-add: article, intro, resource related to what you discussed].

[Soft CTA for next conversation].
```

---

## Email Style Guidelines

1. **Be concise but informative** — Get to the point quickly. Busy people skim.
2. **No markdown formatting** — Never use asterisks, bold (**text**), or other markdown. Write plain text that looks natural in any email client.
3. **Short paragraphs** — 2-3 sentences max per paragraph. White space is your friend.
4. **Simple lists** — If listing items, use plain dashes. No fancy formatting.

**Good:**
```
Here's what I can share:
- Case study from a similar company
- 15-min intro call this week
- Quick demo if helpful
```

**Bad:**
```
**What I Can Offer:**
- **Case study** from a similar company
- **Intro call** this week
```

---

## What NOT to Do

**Generic openers:**
- "I hope this email finds you well"
- "I'm reaching out because..."
- "I wanted to introduce myself"

**Feature dumps:**
- Long paragraphs about your product
- Multiple value props at once
- No clear CTA

**Fake personalization:**
- "I noticed you work at [Company]" (obviously)
- "Congrats on your role" (without context)

**Markdown in emails:**
- Using **bold** or *italic* asterisks
- Headers or formatted lists that won't render

**Instead:**
- Lead with something specific you learned
- One clear value prop
- One clear ask
- Plain text formatting only

---

## Channel Selection

```
IF verified email available:
  → Email preferred (higher response rate)
  → Also provide LinkedIn backup

IF no email:
  → LinkedIn connection request
  → Follow-up message template for after connection

IF warm intro possible:
  → Suggest mutual connection outreach first
```

---

## Company Configuration [CUSTOMIZE]

```markdown
## Outreach Settings

- My name: [Your Name]
- My title: [Your Title]
- My company: [Company Name]
- Value prop: [One sentence - what you help with]

## Signature
[Your preferred email signature]

## Proof Points
- [Customer 1]: [Result]
- [Customer 2]: [Result]
- [Customer 3]: [Result]

## CTA Options
- Default: "Worth a 15-min call?"
- Softer: "Open to learning more?"
- Specific: "Can I send over a quick demo?"

## Tone
- [Professional / Casual / Direct]
- Industry-specific language: [Yes/No]
```

---

## Example

**Input:** "draft outreach to the Head of Engineering at Notion"

**Research finds:**
- Name: David Tibbitts
- Recent news: Notion launched AI features
- Hiring: 5 ML engineer roles open
- Background: Ex-Facebook, Stanford CS

**Output:**

```markdown
# Outreach Draft: David Tibbitts @ Notion

## Research Summary
**Target:** David Tibbitts, Head of Engineering at Notion
**Hook:** They're scaling AI features and hiring ML talent
**Goal:** Intro call about AI infrastructure

---

## Email Draft

**To:** david@notion.so
**Subject:** Notion's AI scaling + a thought

---

Hi David,

Saw Notion's AI rollout is gaining serious traction - congrats.
With 5 ML roles open, seems like you're scaling fast.

Curious how you're thinking about inference infrastructure
as usage grows. We helped [Similar Company] cut their AI
serving costs 40% while improving latency.

Worth a 15-min call to see if relevant to your roadmap?

Best,
[Name]

---

**Subject Alternatives:**
1. Notion AI + scaling question
2. Quick thought on Notion's ML hiring

---

## Email Draft Status
Draft created - check ~~email
```
```
