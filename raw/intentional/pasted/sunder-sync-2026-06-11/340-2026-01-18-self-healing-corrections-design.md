---
type: raw_capture
source_type: pasted
title: "Sunder sync: 2026-01-18-self-healing-corrections-design.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-18-self-healing-corrections-design.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-18-self-healing-corrections-design.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-01-18-self-healing-corrections-design.md"
sha256: "2b371cb3cd246746b21833ace55a959d182749664a7fc0b119b7f3a0c69387f2"
duplicate_of: ""
---

# Sunder sync: 2026-01-18-self-healing-corrections-design.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-18-self-healing-corrections-design.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-18-self-healing-corrections-design.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Self-Healing Corrections: Design Document

**Date:** 2026-01-18
**Status:** Ready for implementation
**Prerequisite:** AI Analyst Part 1 & Part 2 complete

---

## Overview

A lightweight system for capturing user corrections as persistent rules. When the AI detects a user preference that should apply to future analyses, it proposes saving it. User confirms with a button click, rule is logged for manual review.

### Flow

```
User: "For Acme Corp, ignore the tax line - they always bundle it wrong"
                    ↓
AI: [applies correction] + calls propose_rule tool
                    ↓
Frontend: Renders card with rule text + [Yes] [No] buttons
                    ↓
User clicks [Yes]
                    ↓
POST /api/analyst/rules → saves to analyst_rules table
                    ↓
Monthly meeting: Review rules, manually update .claude/templates/maintain-docgen
```

### What We're NOT Building

- No automatic prompt injection at runtime
- No user-facing rule management UI
- No complex scoping (vendor/tag/case hierarchies)

### Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Storage | Supabase table | Persists across devices, works with RLS |
| Scoping | User-level | Rules apply to all user's workflows |
| Trigger | AI-initiated tool call | Model decides when to propose |
| UI | Yes/No buttons | Idiot-proof, no commands to learn |
| Management | No UI | Manual review in monthly meetings |
| Injection | Manual | Update templates after review |

---

## Database Schema

**Table: `analyst_rules`**

```sql
create table analyst_rules (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  case_id uuid not null references cases(id) on delete cascade,
  rule_text text not null,
  created_at timestamptz not null default now()
);

-- RLS: Users can only insert/view their own rules
alter table analyst_rules enable row level security;

create policy "Users can insert own rules"
  on analyst_rules for insert
  with check (auth.uid() = user_id);

create policy "Users can view own rules"
  on analyst_rules for select
  using (auth.uid() = user_id);
```

**Fields:**

| Field | Type | Purpose |
|-------|------|---------|
| `id` | uuid | Primary key |
| `user_id` | uuid | Who created the rule |
| `case_id` | uuid | Which case context it came from |
| `rule_text` | text | The actual rule (e.g., "Acme Corp - ignore tax line items") |
| `created_at` | timestamptz | For sorting in review |

---

## API Endpoint

**File: `api/analyst/rules.ts`**

```typescript
/**
 * POST /api/analyst/rules
 * Saves a user-approved rule to the database.
 * @module api/analyst/rules
 */

import type { VercelRequest, VercelResponse } from "@vercel/node";
import { createClient } from "@supabase/supabase-js";
import { z } from "zod";
import type { Database } from "@/types/database";

const SaveRuleSchema = z.object({
  caseId: z.string().uuid(),
  ruleText: z.string().min(1),
});

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const token = req.headers.authorization?.replace("Bearer ", "");
  if (!token) {
    return res.status(401).json({ error: "Missing authorization token" });
  }

  const supabase = createClient<Database>(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_ANON_KEY!,
    { global: { headers: { Authorization: `Bearer ${token}` } } }
  );

  const { data: { user } } = await supabase.auth.getUser();
  if (!user) {
    return res.status(401).json({ error: "Invalid authentication" });
  }

  const parsed = SaveRuleSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(400).json({ error: "Invalid request", details: parsed.error });
  }

  const { caseId, ruleText } = parsed.data;

  const { error } = await supabase.from("analyst_rules").insert({
    user_id: user.id,
    case_id: caseId,
    rule_text: ruleText,
  });

  if (error) {
    return res.status(500).json({ error: "Failed to save rule" });
  }

  return res.status(201).json({ success: true });
}
```

---

## Tool Definition

**Add to `src/lib/analyst/types.ts`:**

```typescript
/** Tool definition for propose_rule */
export const PROPOSE_RULE_TOOL = {
  name: "propose_rule",
  description: `Propose saving a user correction as a persistent rule.
Call this when the user provides a preference that should apply to ALL future analyses,
not just this session. Do NOT call for one-off adjustments.`,
  parameters: {
    type: "object",
    properties: {
      rule: {
        type: "string",
        description: "The rule to save, written as a clear instruction (e.g., 'For Acme Corp invoices, ignore tax line items during matching')",
      },
    },
    required: ["rule"],
  },
};
```

**System prompt addition:**

```typescript
export const SYSTEM_PROMPT = `You are an AI analyst...

## Saving User Preferences
When a user provides a correction that sounds like a GENERAL preference (not a one-off),
call the propose_rule tool. Examples:
- "Acme always bundles shipping into line 1" → call propose_rule
- "Skip row 5 for now" → do NOT call (one-off)
- "Vendor X invoices never have tax" → call propose_rule
`;
```

---

## Frontend Component

**File: `src/components/analyst/propose-rule-card.tsx`**

```tsx
/**
 * Renders Yes/No buttons when AI proposes saving a rule.
 * @module components/analyst/propose-rule-card
 */
import { useState } from "react";
import { Check, X, Lightbulb, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { supabase } from "@/lib/supabase";

interface ProposeRuleCardProps {
  /** The rule text proposed by the AI */
  rule: string;
  /** Case ID for context */
  caseId: string;
}

/**
 * Card component that appears when AI proposes saving a rule.
 * User can click Yes to save or No to dismiss.
 */
export function ProposeRuleCard({ rule, caseId }: ProposeRuleCardProps) {
  const [status, setStatus] = useState<"pending" | "saving" | "saved" | null>("pending");

  const handleSave = async () => {
    setStatus("saving");
    const { data: { session } } = await supabase.auth.getSession();

    const res = await fetch("/api/analyst/rules", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${session?.access_token}`,
      },
      body: JSON.stringify({ caseId, ruleText: rule }),
    });

    setStatus(res.ok ? "saved" : "pending");
  };

  if (status === "saved") {
    return (
      <div className="flex items-center gap-2 p-3 bg-green-50 border border-green-200 rounded-lg text-green-700 text-sm">
        <Check className="h-4 w-4" />
        <span>Rule saved for review</span>
      </div>
    );
  }

  if (status === null) return null;

  return (
    <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg space-y-2">
      <div className="flex items-start gap-2">
        <Lightbulb className="h-4 w-4 text-blue-600 mt-0.5" />
        <div className="flex-1">
          <p className="text-sm font-medium text-blue-900">Remember this for future analyses?</p>
          <p className="text-sm text-blue-800 mt-1">"{rule}"</p>
        </div>
      </div>
      <div className="flex gap-2 ml-6">
        <Button size="sm" onClick={handleSave} disabled={status === "saving"}>
          {status === "saving" ? <Loader2 className="h-4 w-4 animate-spin" /> : <Check className="h-4 w-4 mr-1" />}
          Yes
        </Button>
        <Button size="sm" variant="ghost" onClick={() => setStatus(null)}>
          <X className="h-4 w-4 mr-1" />
          No
        </Button>
      </div>
    </div>
  );
}
```

---

## ChatMessage Integration

**Update `src/components/analyst/chat-message.tsx`:**

```tsx
// Add import
import { ProposeRuleCard } from "./propose-rule-card";

// Update interface
interface ChatMessageProps {
  /** The message to render */
  message: UIMessage;
  /** Case ID for rule saving */
  caseId: string;
}

// In the parts.map switch statement, add propose_rule case:
if (part.toolName === "propose_rule") {
  const args = part.args as { rule: string };
  return (
    <ProposeRuleCard
      key={key}
      rule={args.rule}
      caseId={caseId}
    />
  );
}
```

**Update `src/components/analyst/analyst-section.tsx`:**

```tsx
// Pass caseId to ChatMessage:
{messages.map((message) => (
  <ChatMessage
    key={message.id}
    message={message}
    caseId={caseId}
  />
))}
```

---

## Implementation Tasks

| Task | Component | File | Action |
|------|-----------|------|--------|
| 1 | Database migration | `supabase/migrations/xxx_analyst_rules.sql` | CREATE |
| 2 | API endpoint | `api/analyst/rules.ts` | CREATE |
| 3 | Tool definition | `src/lib/analyst/types.ts` | MODIFY |
| 4 | System prompt | `src/lib/analyst/types.ts` | MODIFY |
| 5 | ProposeRuleCard | `src/components/analyst/propose-rule-card.tsx` | CREATE |
| 6 | ProposeRuleCard test | `src/components/analyst/propose-rule-card.test.tsx` | CREATE |
| 7 | ChatMessage update | `src/components/analyst/chat-message.tsx` | MODIFY |
| 8 | AnalystSection update | `src/components/analyst/analyst-section.tsx` | MODIFY |
| 9 | Chat API tool registration | `api/chat.ts` | MODIFY |
| 10 | Barrel export | `src/components/analyst/index.ts` | MODIFY |

---

## Unresolved Questions

1. **Chat API tool registration** - Need to verify how to register `propose_rule` as a client-side tool that doesn't execute server-side. May just need to include in tools array without a server handler.

---

## Success Criteria

- [ ] AI proposes saving rules when user gives persistent preferences
- [ ] ProposeRuleCard renders with Yes/No buttons
- [ ] Clicking Yes saves to `analyst_rules` table
- [ ] Clicking No dismisses the card
- [ ] Saved confirmation shows after successful save
- [ ] Rules visible in Supabase for monthly review
- [ ] One-off corrections do NOT trigger propose_rule

---
---
---

# Reference Architecture: How to Make Your AI Agent Its Own Forward-Deployed Engineer

> Source: Fintool (Fintool.com)
> Added: 2026-01-29

---

## Introduction

Palantir invented the Forward Deployed Engineer. Embed a technical person with the customer. Learn their domain, customize the product, make it indispensable.

The key thing FDEs do that most software doesn't: they notice patterns in how you work and build automation around them. They don't wait for you to ask. They watch, learn, propose, and implement.

That's what we, at Fintool, automated.

---

## Where Agents are at today

Skills are the hot primitive. Claude introduced them. Cursor added them in January. Agent Skills is becoming an open standard.

A skill is a SKILL.md file that teaches the agent how to do something. Anthropic calls them "executable knowledge packages." The key innovation: progressive disclosure. Agent sees skill metadata upfront, only loads full instructions when relevant. Scales without bloating context.

Claude Code and even the infamous clawdebot have Skill Creator skills now. You tell the agent "save this as a skill" and it writes the file.

But that's reactive. You have to ask.

---

## Reactive skill creation v/s Proactive skill creation

```
+------------------------------------+-------------------------------------+
|             REACTIVE               |             PROACTIVE               |
+------------------------------------+-------------------------------------+
|                                    |                                     |
|                                    |           +---------------+         |
|                                    |      +--->|    Detects    |---+     |
|                                    |      |    |   patterns    |   |     |
|    +-----------+    +-----------+  |      |    +---------------+   |     |
|    |           |    |   Agent   |  |      |                        v     |
|    |   User    |--->|  creates  |  |  +--------+            +----------+ |
|    |   asks    |    |   skill   |  |  | Agent  |            | Proposes | |
|    |           |    |           |  |  | watches|            |  skill   | |
|    +-----------+    +-----------+  |  +--------+            +----------+ |
|                                    |      ^                        |     |
|                                    |      |    +---------------+   |     |
|                                    |      +----+     Skill     |<--+     |
|                                    |           |     saved     |         |
|                                    |           +---------------+         |
|                                    |                   ^                 |
|                                    |                   |                 |
|                                    |           +---------------+         |
|                                    |           |     User      |         |
|                                    |           |   approves    |         |
|                                    |           +---------------+         |
|                                    |                                     |
|       "You have to ask"            |     "Agent notices before you ask"  |
|                                    |                                     |
|    - 'make me a skill for X'       |    - Weekly pattern detection       |
|    - 'save this as a template'     |      across all conversations       |
|                                    |                                     |
+------------------------------------+-------------------------------------+
|    'Claude, Cursor, Clawdbot'      |         'FDE Agent' (the future)    |
|        (current tools)             |                                     |
+------------------------------------+-------------------------------------+
```

---

## What an FDE Actually Does

An FDE doesn't wait for you to ask for automation. They watch how you work. They notice you do the same analysis every quarter. They notice you always check the same five metrics. They notice you uploaded the same Excel template three times.

Then they say: "I noticed you keep doing this. Want me to automate it?"

That's the difference between a tool and a coworker.

The agent actually has an advantage over a human FDE: it can hold your entire history in context. Every conversation, every watchlist, every document you've created. A human forgets. The agent doesn't. More context means better pattern detection, better proactive suggestions.

---

## Here's what we built..

Two trigger types feed the same agent:

**Scheduled triggers** run on cron. A Lambda checks schedules every 10 minutes, matches alerts, queues workflows.

**Publication triggers** fire on events. New SEC filing drops, hits event queue, Lambda matches alerts, queues workflow.

Both paths converge on the same AI agent with full context: user filesystem, conversation history, email delivery. Same agent that handles chat. No separate system.

### System Architecture Diagram

```
+=============================================================================+
|                            TRIGGER ARCHITECTURE                              |
+=============================================================================+

TOP PATH: SCHEDULED ALERTS
--------------------------

  +----------+         +----------+         +----------+         +----------+
  |   [*]    |  Every  |    /\    |  Check  |    __    |  Match  |   (T)    |
  |  Stats   |-------->|  Lambda  |-------->|   |  |   |-------->|   Time   |---+
  |  Chart   |  10 min |    \/    |  sched  |   |__|   |  alerts |          |   |
  +----------+         +----------+         +----------+         +----------+   |
                                                                                |
                                                                                |
BOTTOM PATH: PUBLICATION ALERTS                                                 |
-------------------------------                                                 |
                                                                                |
  +----------+         +----------+         +----------+         +----------+   |
  |   ___    |   New   |   [X]    |  Event  |    __    |  Match  |   (T)    |   |
  |  |   |   |-------->|  Target  |-------->|   |  |   |-------->|   Time   |---+
  |  |___|   |  filing |  Queue   |  queue  |   |__|   |  alerts |          |   |
  +----------+         +----------+         +----------+         +----------+   |
                                                                                |
                                                                                |
                                        +---------------------------------------+
                                        |
                                        v
                          +-----------------------------+
                          |                             |       +----------------+
                          |        +-----------+        |------>|  Email sent    |
                          |        |   {o_o}   |        |       +----------------+
                          |        |  AI Agent |        |
                          |        +-----------+        |       +----------------+
                          |                             |------>| Skill created  |
                          |    Same agent, full tool    |       +----------------+
                          |          access             |
                          |                             |       +----------------+
                          +-----------------------------+------>|    Content     |
                                        ^                       |   published    |
                                        |                       +----------------+
                        +---------------+---------------+
                        |               |               |
                  +-----+-----+   +-----+-----+   +-----+-----+
                  |   User    |   |Conversation|  |   Email   |
                  | filesystem|   |   history  |  |  delivery |
                  +-----------+   +-----------+   +-----------+
```

---

## The Proactive Skill Creator

Our FDE at Fintool is our **Proactive skill creator**, which is a scheduled trigger. Runs weekly. The prompt:

> "Review this user's last week of conversations. If patterns exist, draft skill recommendations and email them. If nothing, stay silent."

---

## The Filesystem

Each user gets their own filesystem rooted at their **{user_uuid}**. System skills live in **/public/**. Agent reads both.

```
FILESYSTEM STRUCTURE
====================

/{user_uuid}/
|-- memories/
|   |-- UserMemories.md
|
|-- skills/              # their custom skills
|
|-- watchlists/
|
|-- artifacts/


/public/
|-- skills/              # system skills (everyone gets these)
|-- ...
```

What you see is what the agent sees. No hidden state. You can grep your entire knowledge base like a codebase.

### Why filesystem?

LLMs already know how to use them. It's in the pretraining. Vercel found they could replace most custom tooling with a filesystem tool and a bash tool. Cost dropped 75%. Letta's benchmark showed filesystem-based agents scored 74% on memory tasks, beating specialized memory tools.

The filesystem is all you need for continual learning. Files accumulate. The agent navigates, searches, understands structure.

---

## The FDE Loops

The filesystem enables three loops:

### 1. Learning Loop

User signs up. Agent asks what they do, how they invest. Writes to **UserMemories.md**. Every session, reads it first. Doesn't ask "what do you care about" again.

```
LEARNING LOOP FLOW
==================

+------------------+      +-------------------+      +--------------------+
|   User signs up  |----->|  Agent asks       |----->|  Writes to         |
|                  |      |  onboarding Qs    |      |  UserMemories.md   |
+------------------+      +-------------------+      +--------------------+
                                                              |
          +---------------------------------------------------+
          |
          v
+------------------+      +-------------------+      +--------------------+
|  Every session   |----->|  Agent reads      |----->|  Personalized      |
|  starts          |      |  UserMemories.md  |      |  experience        |
+------------------+      +-------------------+      +--------------------+

Example onboarding questions:
  - "What sectors do you focus on?"
      -> Technology, Financials
  - "What market cap range do you typically focus on?"
      -> Mid caps ($2B-$10B)
  - "What's your investment orientation?"
      -> Long-only / Long-short / Just researching
```

---

### 2. Automation Loop

Runs weekly. Agent reviews your conversations, spots repeated templates, repeated document structures, repeated workflows. Emails recommendations. User replies yes. Agent writes **SKILL.md**. The product customizes itself to how they work.

```
AUTOMATION LOOP FLOW
====================

+------------------+      +-------------------+      +--------------------+
|  Weekly cron     |----->|  Agent reviews    |----->|  Detects patterns  |
|  trigger fires   |      |  conversations    |      |  in user behavior  |
+------------------+      +-------------------+      +--------------------+
                                                              |
          +---------------------------------------------------+
          |
          v
+------------------+      +-------------------+      +--------------------+
|  Emails skill    |----->|  User approves    |----->|  Agent writes      |
|  recommendation  |      |  (or declines)    |      |  SKILL.md          |
+------------------+      +-------------------+      +--------------------+
```

#### Example Email - Skill Recommendation

```
+------------------------------------------------------------------------+
| Subject: I found a workflow I can automate for you                     |
+------------------------------------------------------------------------+
|                                                                        |
| Hi,                                                                    |
|                                                                        |
| I reviewed your conversations from the past week and noticed a pattern.|
|                                                                        |
| +--------------------------------------------------------------------+ |
| | DCF Valuation Template                                             | |
| |                                                                    | |
| | You've run 4 DCF valuations this month (CRWD, PANW, FTNT, ZS)     | |
| | and they all use the same assumptions:                             | |
| |                                                                    | |
| | - 10-year projection period                                        | |
| | - Revenue growth fading from current to 3% terminal                | |
| | - WACC: 10-12% for software companies                              | |
| | - Terminal multiple: 15-20x FCF based on growth profile            | |
| | - Three scenarios: base, bull (+20% to terminal), bear (-20%)      | |
| | - Output as Excel with sensitivity tables                          | |
| +--------------------------------------------------------------------+ |
|                                                                        |
| Want me to save this as a reusable skill?                              |
|                                                                        |
| Once saved, you can just say "run a DCF on DDOG" and I'll pull the    |
| financials, apply your assumptions, build the three scenarios, and     |
| generate the Excel with sensitivity tables. Same structure every time. |
|                                                                        |
| [Yes, create this skill]  [Not now]                                    |
|                                                                        |
+------------------------------------------------------------------------+
```

---

### 3. Outreach Loop

User goes quiet. Trigger fires. Agent checks their watchlists, sees something happened. Sends personalized email with research attached. Not a drip campaign. Actual relevance.

```
OUTREACH LOOP FLOW
==================

+------------------+      +-------------------+      +--------------------+
|  User inactive   |----->|  Trigger fires    |----->|  Agent checks      |
|  for N days      |      |                   |      |  their watchlists  |
+------------------+      +-------------------+      +--------------------+
                                                              |
          +---------------------------------------------------+
          |
          v
+------------------+      +-------------------+      +--------------------+
|  Identifies      |----->|  Generates        |----->|  Sends personalized|
|  relevant events |      |  research/summary |      |  email with data   |
+------------------+      +-------------------+      +--------------------+
```

#### Example Email - Re-engagement

```
+------------------------------------------------------------------------+
| Subject: You haven't been back in a while                              |
+------------------------------------------------------------------------+
|                                                                        |
| Hi,                                                                    |
|                                                                        |
| I noticed you haven't logged in for a few weeks. A few things          |
| happened in your Technology watchlist that might be worth catching     |
| up on:                                                                 |
|                                                                        |
| +--------------------------------------------------------------------+ |
| | INTC filed an 8-K announcing CEO departure                         | |
| | Pat Gelsinger out. Stock down 8% on the news. Interim co-CEOs      | |
| | appointed.                                                         | |
| +--------------------------------------------------------------------+ |
|                                                                        |
| +--------------------------------------------------------------------+ |
| | AMD raised guidance at CES                                         | |
| | MI350 chips shipping ahead of schedule. Data center revenue guide  | |
| | raised to $8B for 2026.                                            | |
| +--------------------------------------------------------------------+ |
|                                                                        |
| +--------------------------------------------------------------------+ |
| | ASML missed bookings estimates                                     | |
| | Q4 orders EUR2.6B vs EUR4.0B expected. China restrictions cited.   | |
| | Stock -12% in two sessions.                                        | |
| +--------------------------------------------------------------------+ |
|                                                                        |
| Based on your watchlist, you might want to try:                        |
|                                                                        |
| +--------------------------------------------------------------------+ |
| | "Screen my Technology watchlist for companies that beat estimates  | |
| |  and raised guidance this quarter"                                 | |
| +--------------------------------------------------------------------+ |
|                                                                        |
| [Open Fintool]                                                         |
|                                                                        |
+------------------------------------------------------------------------+
```

Three things happened in their watchlist. INTC CEO departure. AMD raised guidance. ASML missed bookings. Plus a suggested prompt tailored to their coverage.

That's specific to their data. A different user gets different events, different suggestions.

---

## Skills That Matter

Skills load on-demand. The agent sees skill metadata upfront but only loads the full content when relevant. There are 2 types of skills that'll be relevant no matter your vertical:

### 1. System Skills

Ship with the product. Data sources, workflows, document generators. Engineers and non-engineers collaborate to write them. Domain expertise encoded in markdown.

### 2. User Skills

Don't exist until the agent creates them. Patterns detected, skill proposed, user approves, skill saved.

---

## Skills Compound Over Time

```
SKILL ACCUMULATION TIMELINE
===========================

                          Skills Compound Over Time

         Week 1               Month 1               Month 3
           |                    |                     |
           v                    v                     v
     +-----------+        +-----------+         +-----------+
     |    ___    |        |    ___    |         |   ___  *  |
     |   |   |   |        |   |===|   |         |  |===|    |
     |   |___|   |        |   |___|   |         |  |___|    |
     +-----------+        +-----------+         +-----------+
           |                    |                     |
           v                    v                     v
     +-----------+        +-----------+         +-----------+
     |  0 skills |        |  2 skills |         | 5+ skills |
     +-----------+        +-----------+         +-----------+
           |                    |                     |
           v                    v                     v
      Agent knows          Earnings memo,        LLM gets caught
      nothing about        quarterly model       up on your style
      how you work                               instantly
```

Skills accumulate. Week 1, the agent knows nothing specific to you. Month 3, it has five skills tailored to how you work.

---

## Conclusion? Or the beginning..

Palantir-esque FDEs cost millions. They don't scale.

We built one that runs on cron. It watches every user, learns their patterns, and builds automation before they think to ask. The longer someone uses the product, the more it customizes itself to how they work.

**That's the difference between a tool and a coworker.**

---

## Application to Sunder: Self-Healing Corrections

### Key Concepts to Apply

| Fintool Concept | Sunder Application |
|-----------------|-------------------|
| User filesystem `/{user_uuid}/` | Each user gets memories, skills, watchlists, artifacts |
| System skills in `/public/` | Shared correction rules across all users |
| **Learning loop** | Onboarding -> UserMemories.md -> personalization |
| **Automation loop** | Weekly pattern detection -> skill proposals -> user approval |
| **Outreach loop** | Re-engagement based on user's data |
| **Scheduled triggers** | Cron-based, every 10 min check |
| **Event triggers** | Publication/filing triggers |
| Convergence on single agent | All paths lead to same AI agent with full context |
| Progressive disclosure | Agent sees skill metadata upfront, loads full content when relevant |

### Implementation Considerations for Document Corrections

1. **Correction patterns**: Agent detects repeated manual corrections users make
2. **Skill proposals**: "I noticed you always correct [X] to [Y]. Want me to automate this?"
3. **Memory files**: Track user correction preferences in UserMemories.md
4. **Self-healing**: Agent proactively applies learned corrections before user reviews

### Architecture Mapping

```
SUNDER SELF-HEALING ARCHITECTURE (Based on Fintool FDE)
=======================================================

USER DATA LAYER
---------------
/{user_uuid}/
|-- memories/
|   |-- UserMemories.md        <-- Correction preferences
|   |-- CorrectionPatterns.md  <-- Detected patterns
|
|-- skills/
|   |-- vendor-specific/       <-- "Acme Corp: ignore tax lines"
|   |-- document-type/         <-- "Invoices: always check date format"
|
|-- correction-history/        <-- Raw correction log for pattern mining

/public/
|-- skills/
|   |-- default-corrections/   <-- System-wide correction rules
|-- ...


TRIGGER ARCHITECTURE
--------------------

+------------------+      +-------------------+      +--------------------+
| User makes       |----->| AI detects        |----->| Proposes saving    |
| correction       |      | persistent        |      | as rule (Yes/No)   |
| (real-time)      |      | preference        |      |                    |
+------------------+      +-------------------+      +--------------------+
                                                              |
                                                              v
+------------------+      +-------------------+      +--------------------+
| Weekly cron      |----->| Reviews all       |----->| Emails batch       |
| runs             |      | correction logs   |      | recommendations    |
+------------------+      +-------------------+      +--------------------+
                                                              |
                                                              v
                                                     +--------------------+
                                                     | Agent writes       |
                                                     | SKILL.md or        |
                                                     | updates rules      |
                                                     +--------------------+
```

---

*Source: Fintool.com - Made on Fintool*

