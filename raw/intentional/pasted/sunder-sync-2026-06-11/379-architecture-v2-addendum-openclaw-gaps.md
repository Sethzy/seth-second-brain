---
type: raw_capture
source_type: x
title: "Sunder sync: ARCHITECTURE-v2-addendum-openclaw-gaps.md"
url: "https://x.com/founder/status/123456789"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/01_Projects/RE-AI-CRM/01-architecture-history/ARCHITECTURE-v2-addendum-openclaw-gaps.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "01_Projects/RE-AI-CRM/01-architecture-history/ARCHITECTURE-v2-addendum-openclaw-gaps.md"
sha256: "8cbadcf445f6086cc89de013866e913ccd040fc4b24208b610c5751caad8eaff"
duplicate_of: ""
---

# Sunder sync: ARCHITECTURE-v2-addendum-openclaw-gaps.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/01_Projects/RE-AI-CRM/01-architecture-history/ARCHITECTURE-v2-addendum-openclaw-gaps.md`

Primary URL: https://x.com/founder/status/123456789

Duplicate of existing source-map entry: `none`

## Capture Text

# RE AI CRM — Architecture v2 Addendum: OpenClaw Gap Analysis

**Status:** Draft v0.1
**Date:** February 11, 2026
**Purpose:** Architectural additions identified from OpenClaw gap analysis. These sections should be merged into ARCHITECTURE-v2-centralized.md.
**Source:** Nader Dabit "You Could've Invented OpenClaw" tutorial + OpenClaw docs (Context7) + feature analysis.

---

## 1. Context Compaction (Conversation History Management)

**Problem solved:** RE agents chat daily. Within weeks, conversation history exceeds context windows. Without compaction, we either truncate (lose context) or fail on token limits.

**OpenClaw approach:** Summarize old messages when context gets too long, split into chunks, summarize each separately. Crash-safe.

**Our implementation:** Compaction runs inside the `agent-conversation` Trigger.dev task, before prompt construction. Supabase-native — no new infra.

### New table: `conversation_summaries`

```sql
CREATE TABLE conversation_summaries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  summary TEXT NOT NULL,              -- AI-generated summary of compacted messages
  messages_from TIMESTAMPTZ NOT NULL, -- earliest message in this chunk
  messages_to TIMESTAMPTZ NOT NULL,   -- latest message in this chunk
  message_count INTEGER NOT NULL,     -- how many messages were compacted
  token_estimate INTEGER,             -- rough token count of the original messages
  created_at TIMESTAMPTZ DEFAULT now()
);

-- RLS
ALTER TABLE conversation_summaries ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON conversation_summaries
  FOR ALL USING (client_id = current_setting('app.client_id'));
```

### Compaction logic (inside Trigger.dev task)

```typescript
// Inside agent-conversation task, before building the system prompt

const CONTEXT_BUDGET = 80_000; // tokens — leave room for system prompt + tools
const RECENT_MESSAGES_MIN = 20; // always keep at least this many recent messages
const COMPACTION_THRESHOLD = 100_000; // trigger compaction above this

async function loadConversationContext(clientId: string) {
  // 1. Load recent messages (interactions table, ordered by created_at DESC)
  const recentMessages = await db.getRecentMessages(clientId, { limit: 200 });

  // 2. Estimate tokens
  const tokenEstimate = estimateTokens(recentMessages);

  if (tokenEstimate < COMPACTION_THRESHOLD) {
    // No compaction needed — return recent messages as-is
    return { messages: recentMessages, summaries: [] };
  }

  // 3. Split: keep recent, compact old
  const recent = recentMessages.slice(0, RECENT_MESSAGES_MIN);
  const old = recentMessages.slice(RECENT_MESSAGES_MIN);

  // 4. Summarize old messages in chunks of ~50
  const chunks = chunkMessages(old, 50);
  const summaries = [];

  for (const chunk of chunks) {
    const summary = await generateText({
      model: registry.languageModel("anthropic:claude-haiku-4-5"), // cheap model for summarization
      system: "Summarize this conversation concisely. Preserve: key facts about contacts (names, preferences, budgets), decisions made, open tasks/follow-ups, deal status changes, personal details mentioned, and anything the agent would want to remember.",
      prompt: formatMessagesForSummary(chunk),
    });

    // 5. Store summary in DB
    await db.createConversationSummary({
      clientId,
      summary: summary.text,
      messagesFrom: chunk[chunk.length - 1].created_at,
      messagesTo: chunk[0].created_at,
      messageCount: chunk.length,
      tokenEstimate: estimateTokens(chunk),
    });

    summaries.push(summary.text);
  }

  // 6. Optionally archive the compacted messages (mark as compacted, don't delete)
  await db.markMessagesCompacted(old.map(m => m.id));

  return { messages: recent, summaries };
}
```

### How summaries are injected into the prompt

```typescript
// In system prompt construction (Layer 4: Context)

const { messages, summaries } = await loadConversationContext(clientId);

const contextBlock = `
## Previous Conversation Summaries
${summaries.length > 0
  ? summaries.map((s, i) => `### Session ${i + 1}\n${s}`).join('\n\n')
  : '(No previous sessions)'}

## Recent Conversation
${formatMessagesForPrompt(messages)}
`;
```

### Key design decisions

- **Haiku for summarization.** Compaction is pattern-matching, not reasoning. Cheap model is fine.
- **50-message chunks.** Small enough to summarize well, large enough to capture threads.
- **Never delete original messages.** Mark as `compacted` in the interactions table. The raw data is always recoverable.
- **Summaries are cumulative.** Each compaction creates a new summary row. Old summaries stay. This builds a "session history" over weeks/months.
- **Compaction runs at the START of a task,** not the end. Agent pays the compaction cost on the first message after history grows — not on every message.

---

## 2. Semantic Memory Search (pgvector Upgrade Path)

**Problem solved:** Keyword search on `ai_memory` breaks with natural language. "That buyer in District 10" won't match a memory keyed as `contacts/sarah-lee`.

**OpenClaw approach:** Hybrid search — vector embeddings for semantic similarity + FTS for exact keyword match. Configurable embedding providers.

**Our implementation:** Schema-ready from day 1. Keyword search for MVP. Flip the switch to pgvector when memory grows past ~100 entries per client.

### Schema update to `ai_memory`

```sql
-- Add embedding column (nullable — populated only when vector search is enabled)
ALTER TABLE ai_memory ADD COLUMN embedding vector(1536);

-- Add full-text search column
ALTER TABLE ai_memory ADD COLUMN search_text tsvector
  GENERATED ALWAYS AS (to_tsvector('english', key || ' ' || value)) STORED;

-- Indexes (create when ready to enable vector search)
CREATE INDEX ON ai_memory USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
CREATE INDEX ON ai_memory USING gin (search_text);
```

### Hybrid search function

```sql
-- Supabase RPC function for hybrid search
CREATE OR REPLACE FUNCTION search_memory(
  p_client_id TEXT,
  p_query TEXT,
  p_query_embedding vector(1536) DEFAULT NULL,
  p_limit INTEGER DEFAULT 10
)
RETURNS TABLE (key TEXT, value TEXT, similarity FLOAT)
LANGUAGE plpgsql AS $$
BEGIN
  IF p_query_embedding IS NOT NULL THEN
    -- Hybrid: vector similarity + FTS boost
    RETURN QUERY
    SELECT m.key, m.value,
      (0.7 * (1 - (m.embedding <=> p_query_embedding)) +
       0.3 * ts_rank(m.search_text, plainto_tsquery('english', p_query)))::FLOAT as similarity
    FROM ai_memory m
    WHERE m.client_id = p_client_id
      AND m.embedding IS NOT NULL
    ORDER BY similarity DESC
    LIMIT p_limit;
  ELSE
    -- Fallback: FTS only (MVP mode)
    RETURN QUERY
    SELECT m.key, m.value,
      ts_rank(m.search_text, plainto_tsquery('english', p_query))::FLOAT as similarity
    FROM ai_memory m
    WHERE m.client_id = p_client_id
      AND m.search_text @@ plainto_tsquery('english', p_query)
    ORDER BY similarity DESC
    LIMIT p_limit;
  END IF;
END;
$$;
```

### Tool update: `memory_search` (new tool alongside `update_memory`)

```typescript
const memoryTools = {
  // Existing: update_memory (unchanged)

  recall_memory: tool({
    description: 'Search your memory for information about this client, their contacts, preferences, or any previously saved notes. Use at the start of conversations and when context is needed.',
    inputSchema: z.object({
      query: z.string().describe('What to search for — natural language, e.g. "buyer looking in District 10" or "agent preferences"'),
    }),
    execute: async ({ query }) => {
      // MVP: keyword search via tsvector
      // Later: embed query → hybrid search
      const results = await db.rpc('search_memory', {
        p_client_id: clientId,
        p_query: query,
        p_limit: 10,
      });
      return results.length > 0
        ? results.map(r => `[${r.key}] ${r.value}`).join('\n\n')
        : 'No matching memories found.';
    },
  }),
};
```

### Embedding pipeline (when ready)

```typescript
// Called after every update_memory write
async function embedMemory(memoryId: string, value: string) {
  const embedding = await openai.embeddings.create({
    model: 'text-embedding-3-small', // $0.02/MTok — negligible cost
    input: value,
  });
  await db.updateMemory(memoryId, {
    embedding: embedding.data[0].embedding,
  });
}
```

### Migration path

| Phase | Search method | When |
|-------|-------------|------|
| MVP | Full table scan (< 50 entries) | Launch |
| v1.5 | tsvector FTS (exact keyword match) | When any client hits 50 entries |
| v2 | Hybrid vector + FTS | When any client hits 100 entries |

**No code change needed for v1.5** — the `search_text` column auto-populates. Just update the tool to use the RPC function.

---

## 3. Agent Self-Scheduling (Dynamic Recurring Tasks)

**Problem solved:** User says "remind me to follow up with Sarah every Tuesday" and the agent can't self-schedule recurring tasks. Only one-time tasks exist.

**OpenClaw approach:** Agents create/modify/remove their own cron jobs via a `cron` tool at runtime.

**Our implementation:** New `recurring_tasks` table + new tool. The existing `process-scheduled` Trigger.dev cron checks this table every run. No new Trigger.dev infra needed.

### New table: `recurring_tasks`

```sql
CREATE TABLE recurring_tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  contact_id UUID REFERENCES contacts(id),
  description TEXT NOT NULL,           -- "Follow up with Sarah about property search"
  schedule_type TEXT NOT NULL,         -- 'daily', 'weekly', 'biweekly', 'monthly', 'custom'
  schedule_day INTEGER,                -- day of week (0=Sun, 1=Mon) for weekly, day of month for monthly
  schedule_time TIME DEFAULT '09:00',  -- preferred time (agent's timezone)
  next_run_at TIMESTAMPTZ NOT NULL,    -- next scheduled execution
  last_run_at TIMESTAMPTZ,
  status TEXT DEFAULT 'active',        -- active, paused, cancelled
  ai_suggested BOOLEAN DEFAULT false,  -- whether AI created this vs agent requested
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- RLS
ALTER TABLE recurring_tasks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON recurring_tasks
  FOR ALL USING (client_id = current_setting('app.client_id'));
```

### New tool: `manage_recurring_task`

```typescript
manage_recurring_task: tool({
  description: 'Create, update, or cancel a recurring task/reminder. Use when the agent wants something to repeat on a schedule (e.g., "remind me every Tuesday to follow up with Sarah").',
  inputSchema: z.object({
    action: z.enum(['create', 'update', 'pause', 'resume', 'cancel', 'list']),
    id: z.string().optional().describe('Task ID (required for update/pause/resume/cancel)'),
    contactId: z.string().optional(),
    description: z.string().optional(),
    scheduleType: z.enum(['daily', 'weekly', 'biweekly', 'monthly']).optional(),
    scheduleDay: z.number().optional().describe('Day of week (0=Sun) or day of month'),
    scheduleTime: z.string().optional().describe('Time in HH:MM format'),
  }),
  execute: async (input) => {
    switch (input.action) {
      case 'create':
        const task = await db.createRecurringTask({
          clientId,
          contactId: input.contactId,
          description: input.description,
          scheduleType: input.scheduleType,
          scheduleDay: input.scheduleDay,
          scheduleTime: input.scheduleTime,
          nextRunAt: calculateNextRun(input),
        });
        return `Recurring task created: "${input.description}" — ${input.scheduleType} at ${input.scheduleTime}. Next run: ${task.nextRunAt}`;

      case 'list':
        const tasks = await db.getRecurringTasks(clientId, { status: 'active' });
        return tasks.length > 0
          ? tasks.map(t => `• ${t.description} (${t.scheduleType}, next: ${t.nextRunAt})`).join('\n')
          : 'No active recurring tasks.';

      case 'cancel':
        await db.updateRecurringTask(input.id, { status: 'cancelled' });
        return 'Recurring task cancelled.';

      // ... pause, resume, update cases
    }
  },
}),
```

### Processing: extend existing `process-scheduled` cron

```typescript
// Add to the existing process-scheduled Trigger.dev task
// (runs every minute, already checks pending_messages)

export const processScheduled = schedules.task({
  id: "process-scheduled",
  cron: { pattern: "* * * * *" },
  run: async () => {
    // Existing: process approved pending_messages
    await processApprovedMessages();

    // NEW: process recurring tasks
    const dueTasks = await db.query(`
      SELECT * FROM recurring_tasks
      WHERE status = 'active' AND next_run_at <= now()
    `);

    for (const task of dueTasks) {
      // Create a one-time task from the recurring template
      await db.createTask({
        clientId: task.client_id,
        contactId: task.contact_id,
        type: 'follow_up',
        description: task.description,
        dueDate: new Date(),
        aiSuggested: true,
        source: `recurring:${task.id}`,
      });

      // Advance next_run_at
      await db.updateRecurringTask(task.id, {
        lastRunAt: new Date(),
        nextRunAt: calculateNextRun(task),
      });

      // Optionally: send a nudge to the agent's chat
      // "Recurring reminder: Follow up with Sarah about property search"
    }
  },
});
```

### Agent experience (AI-initiated)

```
Agent: "Remind me to follow up with Sarah every Tuesday"

AI: Got it. I've set up a weekly reminder:
    📋 "Follow up with Sarah about property search"
    ⏰ Every Tuesday at 9:00am
    Next: Tuesday, Feb 18

    I'll create a task each Tuesday and nudge you in the morning briefing.

[Every Tuesday morning briefing includes:]
    🔁 Recurring: Follow up with Sarah about property search
```

---

### Recurring Tasks UI (Agent-Initiated)

**Problem:** Agents need a UI to proactively create and manage recurring workflows — not just rely on the AI to suggest them. Think morning briefings, weekly pipeline reviews, listing alerts.

**Solution:** A Cron Job Composer (like OpenClaw's) for the agent dashboard.

#### UI Templates

```typescript
const RECURRING_TASK_TEMPLATES = [
  {
    id: 'daily_standup',
    icon: '📅',
    name: 'DAILY STANDUP',
    description: 'Daily summary of new leads, tasks due today, and priority follow-ups.',
    defaultSchedule: { type: 'daily', time: '08:00' },
    promptTemplate: 'Generate my daily standup: new leads from yesterday, tasks due today, deals needing attention.',
  },
  {
    id: 'weekly_pipeline',
    icon: '📋',
    name: 'WEEKLY PIPELINE REVIEW',
    description: 'Review open deals, stalled prospects, and conversion metrics.',
    defaultSchedule: { type: 'weekly', day: 1, time: '09:00' }, // Monday 9am
    promptTemplate: 'Review my pipeline: deals by stage, stalled for >7 days, conversion rate this month.',
  },
  {
    id: 'listing_alert',
    icon: '🏡',
    name: 'LISTING ALERT',
    description: 'Check for new listings matching saved searches or client criteria.',
    defaultSchedule: { type: 'daily', time: '10:00' },
    promptTemplate: 'Check for new listings matching: {search_criteria}',
  },
  {
    id: 'follow_up_reminder',
    icon: '🔔',
    name: 'FOLLOW-UP REMINDER',
    description: 'Weekly or biweekly nudge to follow up with a specific contact or deal.',
    defaultSchedule: { type: 'weekly', day: 2, time: '09:00' }, // Tuesday 9am
    promptTemplate: 'Remind me to follow up with {contact_name} about {context}',
  },
  {
    id: 'inbox_triage',
    icon: '📧',
    name: 'INBOX TRIAGE',
    description: 'Summarize unread messages and prioritize responses.',
    defaultSchedule: { type: 'daily', time: '08:30' },
    promptTemplate: 'Triage my inbox: unread messages, urgent responses needed, low-priority items.',
  },
  {
    id: 'custom',
    icon: '⚙️',
    name: 'CUSTOM',
    description: 'Build your own recurring workflow from scratch.',
    defaultSchedule: { type: 'weekly', day: 1, time: '09:00' },
    promptTemplate: '',
  },
];
```

#### UI Flow (4 Steps)

```
┌─────────────────────────────────────────────────────┐
│  CRON JOB COMPOSER                       [CLOSE]    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Choose a starter template to prefill your cron job │
│                                                      │
│  ┌──────────────────┐  ┌──────────────────┐        │
│  │ 📅 DAILY STANDUP │  │ 🔔 FOLLOW-UP     │        │
│  │ Morning summary  │  │ Timed nudge      │        │
│  └──────────────────┘  └──────────────────┘        │
│                                                      │
│  ┌──────────────────┐  ┌──────────────────┐        │
│  │ 📋 WEEKLY REVIEW │  │ 📧 INBOX TRIAGE  │        │
│  │ Pipeline review  │  │ Message summary  │        │
│  └──────────────────┘  └──────────────────┘        │
│                                                      │
│  ┌──────────────────┐  ┌──────────────────┐        │
│  │ 🏡 LISTING ALERT │  │ ⚙️ CUSTOM        │        │
│  │ New listings     │  │ Blank template   │        │
│  └──────────────────┘  └──────────────────┘        │
│                                                      │
│                          Step 1 of 4                │
│              [BACK]          [NEXT] [CREATE CRON]   │
└─────────────────────────────────────────────────────┘
```

**Step 2:** Configure Schedule
```
┌─────────────────────────────────────────────────────┐
│  Schedule                                            │
├─────────────────────────────────────────────────────┤
│  Frequency: [Daily ▼]  [Weekly ▼]  [Monthly ▼]     │
│  Day:       [Monday ▼]  (if weekly/monthly)         │
│  Time:      [09:00]                                  │
│  Timezone:  [Asia/Singapore ▼]                      │
│                                                      │
│  Next run: Tuesday, Feb 18, 2026 at 9:00am         │
└─────────────────────────────────────────────────────┘
```

**Step 3:** Configure Context (template-specific)
```
┌─────────────────────────────────────────────────────┐
│  Follow-Up Reminder Details                         │
├─────────────────────────────────────────────────────┤
│  Contact:  [Sarah Lee ▼]  (autocomplete contacts)  │
│  Context:  "Property search in District 10"         │
│  Custom instructions (optional):                    │
│  ┌─────────────────────────────────────────────┐   │
│  │ Check if she's still looking, mention the   │   │
│  │ new listings that came in this week.        │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Step 4:** Review & Activate
```
┌─────────────────────────────────────────────────────┐
│  Review & Activate                                   │
├─────────────────────────────────────────────────────┤
│  🔔 Follow-Up Reminder                              │
│  📅 Every Tuesday at 9:00am                         │
│  👤 Contact: Sarah Lee                              │
│  💬 "Follow up about property search in District 10"│
│                                                      │
│  Next run: Tuesday, Feb 18, 2026 at 9:00am         │
│                                                      │
│  [✓] Notify me in morning briefing                 │
│  [✓] Create task automatically                     │
│  [ ] Send WhatsApp reminder (future)               │
│                                                      │
│              [CANCEL]          [CREATE CRON JOB]   │
└─────────────────────────────────────────────────────┘
```

#### Frontend Routes

```typescript
// app/dashboard/recurring-tasks/page.tsx
// List view of all active/paused recurring tasks

export default function RecurringTasksPage() {
  const { data: tasks } = useRecurringTasks();

  return (
    <div>
      <header>
        <h1>Recurring Tasks</h1>
        <Button onClick={() => router.push('/dashboard/recurring-tasks/new')}>
          + New Cron Job
        </Button>
      </header>

      <TaskList tasks={tasks} />
      {/* Table: Name | Schedule | Next Run | Status | Actions */}
    </div>
  );
}
```

```typescript
// app/dashboard/recurring-tasks/new/page.tsx
// 4-step wizard from screenshot

export default function NewRecurringTaskWizard() {
  const [step, setStep] = useState(1);
  const [template, setTemplate] = useState<Template | null>(null);
  const [schedule, setSchedule] = useState<Schedule>({});
  const [context, setContext] = useState<Context>({});

  return (
    <WizardDialog>
      {step === 1 && <TemplateSelector onSelect={setTemplate} />}
      {step === 2 && <ScheduleConfig value={schedule} onChange={setSchedule} />}
      {step === 3 && <ContextConfig template={template} value={context} onChange={setContext} />}
      {step === 4 && <ReviewStep template={template} schedule={schedule} context={context} />}
    </WizardDialog>
  );
}
```

#### Backend API Routes

```typescript
// app/api/recurring-tasks/route.ts

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const status = searchParams.get('status') || 'active';

  const tasks = await db.query.recurring_tasks.findMany({
    where: (t, { eq, and }) => and(
      eq(t.client_id, clientId),
      eq(t.status, status)
    ),
    orderBy: (t, { asc }) => [asc(t.next_run_at)],
  });

  return Response.json({ tasks });
}

export async function POST(req: Request) {
  const body = await req.json();
  const { template, schedule, context } = body;

  const task = await db.insert(recurring_tasks).values({
    client_id: clientId,
    contact_id: context.contactId,
    description: buildDescription(template, context),
    schedule_type: schedule.type,
    schedule_day: schedule.day,
    schedule_time: schedule.time,
    next_run_at: calculateNextRun(schedule),
    ai_suggested: false, // user-created
    metadata: { template: template.id, context },
  });

  return Response.json({ task });
}
```

```typescript
// app/api/recurring-tasks/[id]/route.ts

export async function PATCH(req: Request, { params }: { params: { id: string } }) {
  const body = await req.json();
  const { status, schedule } = body;

  const task = await db.update(recurring_tasks)
    .set({
      status,
      schedule_type: schedule?.type,
      schedule_day: schedule?.day,
      schedule_time: schedule?.time,
      next_run_at: schedule ? calculateNextRun(schedule) : undefined,
      updated_at: new Date(),
    })
    .where(eq(recurring_tasks.id, params.id));

  return Response.json({ task });
}

export async function DELETE(req: Request, { params }: { params: { id: string } }) {
  await db.update(recurring_tasks)
    .set({ status: 'cancelled' })
    .where(eq(recurring_tasks.id, params.id));

  return Response.json({ success: true });
}
```

#### UI vs AI Tool Comparison

| Aspect | AI Tool (`manage_recurring_task`) | Human UI (Cron Composer) |
|--------|----------------------------------|--------------------------|
| **Trigger** | Agent says "remind me..." | Agent clicks "+ New Cron Job" |
| **Input** | Natural language | Form-based wizard |
| **Templates** | None (AI figures it out) | 6 presets (Daily Standup, etc.) |
| **Flexibility** | High (freeform requests) | Medium (structured options) |
| **Discovery** | Requires agent to know feature exists | Visible in dashboard navigation |
| **Metadata** | `ai_suggested: true` | `ai_suggested: false` |
| **Best for** | Conversational, context-aware reminders | Proactive workflow setup |

Both write to the same `recurring_tasks` table. Processing (in `process-scheduled` task) doesn't care who created it.

#### Example User Journey

```
Agent logs in → Dashboard → "Recurring Tasks" tab

Sees:
  📅 Daily Standup (Active) — Next: Tomorrow 8:00am
  📋 Weekly Pipeline (Active) — Next: Monday 9:00am
  🏡 Listing Alert: District 10 (Active) — Next: Today 10:00am

Clicks "+ New Cron Job"

Chooses "🔔 FOLLOW-UP REMINDER"

Step 2: Sets "Every Tuesday at 9:00am"

Step 3: Selects contact "Sarah Lee", adds context "Property search"

Step 4: Reviews, clicks "CREATE CRON JOB"

Next Tuesday 9am:
  - AI creates a task "Follow up with Sarah about property search"
  - Morning briefing shows: "🔁 Recurring: Follow up with Sarah"
  - Agent sees notification in dashboard
```

#### Build Order

**MVP (Phase 1):**
- List view (`/dashboard/recurring-tasks`)
- Basic create form (no wizard, just a form)
- Pause/resume/cancel actions
- Integration with existing `process-scheduled` task

**Phase 2:**
- 4-step wizard UI (like OpenClaw screenshot)
- 6 preset templates
- Contact/deal autocomplete
- Next run preview

**Phase 3:**
- Edit existing recurring tasks
- Duplicate/clone tasks
- Task execution history (show past runs)
- Advanced scheduling (e.g., "first Monday of month", "weekdays only")

---

## 3b. Mission Control Dashboard

**Problem solved:** The current dashboard (Component 3) is a passive read-only view — Pipeline, Contacts, Tasks. There's no real-time visibility into what the AI is doing, no way to interact with tasks beyond WhatsApp, no activity feed showing AI actions as they happen. Agents have to check WhatsApp to know if the AI extracted a contact, created a task, or is waiting for approval.

**Inspiration:** @pbteja1998's Mission Control for OpenClaw — a shared workspace where you see agent status, task board, activity feed, notifications, and deliverables. Adapted from multi-agent coordination (10 AI agents) to single-agent visibility (1 AI per client).

**Our implementation:** Upgrade Component 3 from passive viewer to active Mission Control. Same Next.js app. Supabase Realtime for live updates. Replaces the "read-only for MVP" constraint.

### Why Mission Control > Basic Dashboard

| Basic Dashboard (current) | Mission Control (upgrade) |
|---|---|
| Static page refresh | Real-time via Supabase Realtime |
| See data, can't act on it | Quick actions (approve, assign, trigger) |
| No visibility into AI state | AI status panel (processing, idle, blocked) |
| Flat task list | Kanban board with comment threads |
| No notification system | Notification center with @mentions |
| Agent has to check WhatsApp | Dashboard is the command center |

### Dashboard Layout

```
┌──────────────────────────────────────────────────────────────────────┐
│  SUNDER MISSION CONTROL                    🔔 3  [Sarah Agent] ▼    │
├──────────┬───────────────────────────────────────────────────────────┤
│          │                                                           │
│  🏠 Home │  ┌─ AI STATUS ────────────────────────────────────────┐  │
│          │  │  🟢 Online — Last active: 2 min ago                │  │
│  📊 Pipe │  │  Currently: Extracting contacts from Group Chat    │  │
│          │  │  Queued: 3 messages  │  Today: 47 actions           │  │
│  👥 Cont │  └────────────────────────────────────────────────────┘  │
│          │                                                           │
│  ✅ Tasks│  ┌─ ACTIVITY FEED ────────────────────────────────────┐  │
│          │  │  2 min ago  📋 Created task: Follow up with Sarah   │  │
│  📡 Feed │  │  5 min ago  👤 New contact: David Tan (buyer)       │  │
│          │  │  12 min ago 💬 AI replied to agent about pricing    │  │
│  🔁 Cron │  │  15 min ago 📊 Updated deal: Riveria #12-08 → LOI │  │
│          │  │  30 min ago ⚠️  APPROVAL NEEDED: Message to Sarah   │  │
│  ⚙️ Set  │  │  1 hr ago   🔁 Recurring: Morning briefing sent    │  │
│          │  └────────────────────────────────────────────────────┘  │
│          │                                                           │
│          │  ┌─ QUICK ACTIONS ────────────────────────────────────┐  │
│          │  │  [📩 Pending Approvals (2)]  [📋 Create Task]      │  │
│          │  │  [💬 Talk to AI]             [🔁 New Cron Job]      │  │
│          │  └────────────────────────────────────────────────────┘  │
└──────────┴───────────────────────────────────────────────────────────┘
```

### Core Panels

#### 1. AI Status Panel

Shows what the AI is doing right now. Real-time via Supabase Realtime subscription on a new `ai_status` table (or column on `clients`).

```typescript
// Real-time AI status component
function AIStatusPanel({ clientId }: { clientId: string }) {
  const status = useRealtimeSubscription('ai_status', clientId);

  return (
    <Card>
      <StatusDot status={status.state} /> {/* 🟢 online, 🟡 processing, 🔴 error, ⚪ idle */}
      <span>{status.state === 'processing' ? status.currentAction : 'Idle'}</span>
      <div className="flex gap-4 text-sm text-muted">
        <span>Queued: {status.queuedMessages}</span>
        <span>Today: {status.actionsToday} actions</span>
        <span>Last active: {timeAgo(status.lastActiveAt)}</span>
      </div>
    </Card>
  );
}
```

States:
- **Online/Idle** — AI is connected, no active tasks
- **Processing** — AI is working (shows what: "Extracting contacts from Group Chat")
- **Waiting for approval** — Tier 3 message blocked, needs agent action
- **Error** — Something failed (gateway down, API error)

Updated by Trigger.dev tasks as they execute:
```typescript
// Inside agent-conversation task
await db.updateAIStatus(clientId, {
  state: 'processing',
  currentAction: 'Analyzing message from Sarah Lee',
  lastActiveAt: new Date(),
});

// ... do work ...

await db.updateAIStatus(clientId, {
  state: 'idle',
  currentAction: null,
  actionsToday: increment(1),
});
```

#### 2. Activity Feed (Real-time)

Stream of everything the AI does. Already have the data in `interactions` + `tasks` tables — just need a unified view.

```typescript
// Supabase Realtime subscription
const activities = useRealtimeQuery(
  supabase
    .from('activity_feed') // view joining interactions + tasks + pending_messages
    .select('*')
    .eq('client_id', clientId)
    .order('created_at', { ascending: false })
    .limit(50)
);
```

Activity types (icons + actions):

| Icon | Activity | Source table |
|------|----------|-------------|
| 👤 | New contact extracted | `contacts` |
| 📊 | Deal stage changed | `deals` |
| 📋 | Task created/completed | `tasks` |
| 💬 | AI conversation (agent chat) | `interactions` |
| 📩 | Message sent to contact | `interactions` |
| ⚠️ | Approval requested (Tier 3) | `pending_messages` |
| ✅ | Approval given/denied | `pending_messages` |
| 🧠 | Memory updated | `ai_memory` |
| 🔁 | Recurring task fired | `recurring_tasks` |
| 📄 | Artifact created | `artifacts` |

Each activity row is clickable — navigates to the relevant contact/deal/task.

```
┌──────────────────────────────────────────────────────────────┐
│  📡 ACTIVITY FEED                              [Filter ▼]   │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  2:15pm  📋 Task created                                     │
│          "Follow up with Sarah about District 10 property"   │
│          Due: Tomorrow  •  Contact: Sarah Lee                │
│          [View Task →]                                       │
│  ─────────────────────────────────────────────────────────── │
│  2:12pm  👤 New contact extracted                            │
│          David Tan — Buyer, Budget $1.5M                     │
│          Source: "PropertyChat SG" group                     │
│          [View Contact →]                                    │
│  ─────────────────────────────────────────────────────────── │
│  2:05pm  ⚠️  APPROVAL NEEDED                                │
│          Draft message to Sarah Lee:                         │
│          "Hi Sarah, 3 new listings in D10 this week..."      │
│          [APPROVE ✓]  [EDIT ✏️]  [REJECT ✗]                 │
│  ─────────────────────────────────────────────────────────── │
│  1:45pm  📊 Deal updated                                    │
│          Riveria #12-08 → LOI stage                          │
│          Auto-detected from WhatsApp conversation            │
│          [View Deal →]                                       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

**Key interaction:** Approval actions inline. Agent sees pending Tier 3 messages in the feed and can approve/edit/reject without going to WhatsApp.

#### 3. Task Board (Kanban)

Upgrade from flat task list to Kanban. Same `tasks` table, different view.

```
┌──────────────────────────────────────────────────────────────┐
│  ✅ TASK BOARD                          [+ New Task] [List ⋮]│
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  OVERDUE (2)    │  TODAY (4)      │  UPCOMING (7)  │  DONE   │
│  ──────────     │  ──────────     │  ──────────    │  ────── │
│  ┌───────────┐  │  ┌───────────┐  │  ┌──────────┐ │         │
│  │Call Sarah  │  │  │Follow up  │  │  │Pipeline  │ │         │
│  │about D10   │  │  │David Tan  │  │  │review    │ │         │
│  │📅 Feb 9   │  │  │📅 Today   │  │  │📅 Mon    │ │         │
│  │🔁 Weekly  │  │  │🤖 AI-made │  │  │🔁 Weekly │ │         │
│  │💬 2 notes │  │  │           │  │  │          │ │         │
│  └───────────┘  │  └───────────┘  │  └──────────┘ │         │
│                  │                 │               │         │
└──────────────────────────────────────────────────────────────┘
```

Task cards show:
- **Title + due date**
- **Source badge:** 🤖 AI-created, 🔁 Recurring, 👤 Manual
- **Comment count** (task has a comment thread)
- **Contact link** (if associated)

Clicking a task opens a detail panel with full context + comment thread:

```
┌──────────────────────────────────────────────────────────────┐
│  ← Back to Board                                              │
│                                                               │
│  📋 Follow up with Sarah about District 10 property          │
│  Status: [Today ▼]  Contact: Sarah Lee  Due: Feb 11          │
│  Source: 🔁 Recurring (weekly, Tue 9am)                      │
│                                                               │
│  ── CONTEXT ──────────────────────────────────────────────── │
│  Sarah is looking for 3BR in District 10, budget $1.8M.     │
│  Last spoke Jan 28 — she wanted to see Riveria and Paya     │
│  Lebar Quarter units.                                        │
│                                                               │
│  ── THREAD ───────────────────────────────────────────────── │
│  🤖 AI (9:00am): Created from recurring task. Sarah hasn't  │
│     been contacted in 14 days. 3 new D10 listings this week. │
│                                                               │
│  👤 You (9:15am): Will call her after lunch. Check if the   │
│     Riveria unit is still available.                          │
│                                                               │
│  🤖 AI (9:16am): Riveria #12-08 is still listed at $1.75M.  │
│     Last transaction in the block: $1,680 PSF (Nov 2025).    │
│                                                               │
│  [Type a note...]                                [Post]      │
│                                                               │
│  ── ACTIONS ──────────────────────────────────────────────── │
│  [Mark Done ✓]  [Snooze →]  [Draft message to Sarah]        │
└──────────────────────────────────────────────────────────────┘
```

**Key interaction:** The comment thread is where agent and AI collaborate on a task. Agent posts notes, AI can respond with context. This is Mission Control's "shared whiteboard" concept — adapted from multi-agent to agent+AI.

#### 4. Notification Center

Bell icon in header. Shows items needing attention.

```typescript
type Notification = {
  id: string;
  type: 'approval_needed' | 'task_overdue' | 'recurring_fired' | 'ai_suggestion' | 'morning_briefing';
  title: string;
  body: string;
  actionUrl: string;    // deep link to relevant page
  read: boolean;
  created_at: string;
};
```

Notification types:
- **⚠️ Approval needed** — Tier 3 message waiting (highest priority)
- **⏰ Task overdue** — follow-up missed
- **🔁 Recurring fired** — cron job created a new task
- **💡 AI suggestion** — AI proactively suggests something ("You haven't contacted David in 2 weeks")
- **📊 Morning briefing** — daily summary ready to view

#### 5. Morning Briefing View

The daily standup concept from pbteja, rendered as a dashboard page instead of Telegram.

```
┌──────────────────────────────────────────────────────────────┐
│  📊 MORNING BRIEFING — February 11, 2026                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  🔥 PRIORITY                                                 │
│  • Sarah Lee hasn't been contacted in 14 days (recurring)    │
│  • 2 pending approvals from yesterday                        │
│  • David Tan asked about pricing — needs response            │
│                                                               │
│  📋 TODAY'S TASKS (6)                                        │
│  • Follow up with Sarah (District 10 search)        🔁      │
│  • Respond to David Tan inquiry                     🤖      │
│  • Review offer terms for Riveria #12-08            📋      │
│  • Call back Mrs. Wong (missed call yesterday)      📋      │
│  • Submit listing photos for Tampines unit          📋      │
│  • Weekly pipeline review                           🔁      │
│                                                               │
│  📊 PIPELINE SNAPSHOT                                        │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Lead: 12  │  Viewing: 5  │  Offer: 3  │  Closed: 1   │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                               │
│  🆕 NEW SINCE YESTERDAY                                     │
│  • 2 new contacts extracted (David Tan, Emily Goh)          │
│  • 4 new listings matching saved searches                   │
│  • Deal: Riveria #12-08 moved to LOI stage                  │
│                                                               │
│  📧 FOLLOW-UP REMINDERS                                     │
│  • James Lim — last contact 7 days ago (was hot lead)       │
│  • Mr. & Mrs. Chen — viewing feedback pending (3 days)      │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

Generated by the existing morning briefing cron (Trigger.dev). Currently sent via WhatsApp — now also persisted and rendered in dashboard.

#### 6. Chat Interface (Post-MVP)

Talk to the AI from the dashboard, not just WhatsApp. Uses Vercel AI SDK `useChat()`.

```typescript
// app/dashboard/chat/page.tsx
import { useChat } from 'ai/react';

export default function DashboardChat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: '/api/chat', // triggers same agent-conversation Trigger.dev task
  });

  return (
    <ChatWindow>
      {messages.map(m => <Message key={m.id} {...m} />)}
      <ChatInput value={input} onChange={handleInputChange} onSubmit={handleSubmit} />
    </ChatWindow>
  );
}
```

This unlocks dashboard-first agents who prefer typing on desktop over WhatsApp. Same AI, same tools, same memory — just different channel.

### New/Modified Tables

```sql
-- AI Status (real-time state for dashboard)
-- Option A: new table
CREATE TABLE ai_status (
  client_id TEXT PRIMARY KEY REFERENCES clients(id),
  state TEXT DEFAULT 'idle',           -- idle, processing, waiting_approval, error
  current_action TEXT,                  -- "Extracting contacts from Group Chat"
  queued_messages INTEGER DEFAULT 0,
  actions_today INTEGER DEFAULT 0,
  last_active_at TIMESTAMPTZ,
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Option B: just add columns to clients table (simpler)
ALTER TABLE clients ADD COLUMN ai_state TEXT DEFAULT 'idle';
ALTER TABLE clients ADD COLUMN ai_current_action TEXT;
ALTER TABLE clients ADD COLUMN ai_last_active_at TIMESTAMPTZ;

-- Activity Feed (materialized view or DB view)
CREATE VIEW activity_feed AS
  SELECT 'contact_created' as type, id, created_at, client_id,
    jsonb_build_object('name', name, 'category', category) as data
  FROM contacts
  UNION ALL
  SELECT 'task_created' as type, id, created_at, client_id,
    jsonb_build_object('description', description, 'due_date', due_date) as data
  FROM tasks
  UNION ALL
  SELECT 'deal_updated' as type, id, updated_at, client_id,
    jsonb_build_object('property', property_address, 'stage', stage) as data
  FROM deals
  UNION ALL
  SELECT 'approval_needed' as type, id, created_at, client_id,
    jsonb_build_object('to_contact', to_name, 'draft', draft_text) as data
  FROM pending_messages WHERE status = 'pending'
  ORDER BY created_at DESC;

-- Notifications
CREATE TABLE notifications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  type TEXT NOT NULL,          -- approval_needed, task_overdue, recurring_fired, ai_suggestion, morning_briefing
  title TEXT NOT NULL,
  body TEXT,
  action_url TEXT,             -- deep link: /dashboard/tasks/abc123
  read BOOLEAN DEFAULT false,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE notifications ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON notifications
  FOR ALL USING (client_id = current_setting('app.client_id'));

-- Task comments (thread on each task)
CREATE TABLE task_comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID NOT NULL REFERENCES tasks(id),
  client_id TEXT NOT NULL REFERENCES clients(id),
  author_type TEXT NOT NULL,    -- 'agent' or 'ai'
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE task_comments ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON task_comments
  FOR ALL USING (client_id = current_setting('app.client_id'));

-- Morning briefings (persist for dashboard view)
CREATE TABLE morning_briefings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  date DATE NOT NULL,
  content JSONB NOT NULL,       -- structured: { priority, tasks, pipeline, new_items, follow_ups }
  rendered_text TEXT,           -- markdown version (for WhatsApp)
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE(client_id, date)
);
```

### Frontend Routes (Updated Component 3)

| Route | Page | Panel |
|---|---|---|
| `/dashboard` | **Home / Mission Control** | AI Status + Activity Feed + Quick Actions |
| `/dashboard/pipeline` | Pipeline | Kanban deals by stage |
| `/dashboard/contacts` | Contacts | List + search/filter |
| `/dashboard/contacts/[id]` | Contact detail | Interactions, deals, tasks, AI notes |
| `/dashboard/tasks` | **Task Board** | Kanban (Overdue / Today / Upcoming / Done) |
| `/dashboard/tasks/[id]` | Task detail | Context + comment thread + actions |
| `/dashboard/feed` | **Full Activity Feed** | Filterable stream of all AI actions |
| `/dashboard/recurring-tasks` | Recurring Tasks | List + manage cron jobs |
| `/dashboard/recurring-tasks/new` | Cron Composer | 4-step wizard |
| `/dashboard/briefing` | **Morning Briefing** | Today's generated briefing |
| `/dashboard/briefing/[date]` | Historical Briefing | Past briefings |
| `/dashboard/chat` | **AI Chat** | Dashboard chat interface (post-MVP) |
| `/dashboard/approvals` | **Pending Approvals** | All Tier 3 messages awaiting action |
| `/dashboard/settings` | Settings | Preferences, notification settings |

### Real-time Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌───────────────────┐
│ Trigger.dev      │     │  Supabase     │     │  Next.js Frontend  │
│ (agent tasks)    │────▶│  (tables)     │────▶│  (Realtime sub)    │
│                  │     │              │     │                    │
│ On each action:  │     │ INSERT/UPDATE │     │ useRealtimeQuery() │
│ - Update ai_stat │     │ triggers      │     │ Auto-refreshes UI  │
│ - Insert activity│     │ Realtime      │     │ No polling needed  │
│ - Create notif   │     │ broadcast     │     │                    │
└─────────────────┘     └──────────────┘     └───────────────────┘
```

Uses Supabase Realtime (built-in, free tier supports it). Frontend subscribes to:
- `ai_status` changes (AI State panel)
- `activity_feed` view (Activity Feed)
- `notifications` inserts (Bell icon badge)
- `task_comments` inserts (Task detail thread)

### Mission Control vs pbteja's Multi-Agent Setup

| Concept | pbteja (10 agents) | Sunder (1 AI per client) |
|---------|-------------------|--------------------------|
| **Agent Cards** | 10 agent status cards | 1 AI status panel |
| **Task Board** | Agents pick up tasks | Agent + AI collaborate on tasks |
| **Comment Threads** | Agents discuss with each other | Agent + AI discuss |
| **Activity Feed** | Multi-agent actions | Single AI actions on behalf of agent |
| **Notifications** | @mention between agents | AI → Agent notifications |
| **Heartbeat** | Agents check in every 15 min | AI processes queued messages |
| **Daily Standup** | Compiled from all agents | Compiled from one AI's actions |
| **SOUL.md** | Per-agent personality | Per-client AI personality (already in SOUL.md) |
| **Shared Database** | Convex (agents coordinate) | Supabase (AI + dashboard sync) |

The mental model shift: pbteja's Mission Control coordinates **agents talking to agents**. Ours coordinates **an agent and their AI assistant** — the dashboard is the "office" where the agent watches and directs their AI.

### Build Order

**Phase 1 (MVP Dashboard Upgrade):**
- AI Status panel (simple: idle/processing/error)
- Activity Feed (read-only, using existing tables)
- Inline approval actions (approve/reject Tier 3 from dashboard)
- Notifications table + bell icon
- Supabase Realtime for AI status + notifications

**Phase 2 (Task Board):**
- Kanban task view (drag-and-drop optional)
- Task detail panel with comment thread
- Task creation from dashboard
- Task comments (agent posts notes, AI responds)

**Phase 3 (Briefing + Chat):**
- Morning Briefing page (persist + render)
- Historical briefings archive
- Dashboard chat interface (Vercel AI SDK `useChat()`)
- Notification preferences (email/push future)

**Phase 4 (Power Features):**
- Custom activity feed filters
- Saved views / pinned tasks
- Keyboard shortcuts (j/k navigation, a to approve)
- Mobile-responsive Mission Control
- Browser push notifications

---

## 4. Session Boundaries & Reset

**Problem solved:** Agent asks about Sarah at 9am, then a completely different deal at 3pm. Without boundaries, the 3pm context is polluted with 9am context — wasting tokens and potentially confusing the model.

**OpenClaw approach:** Reset triggers (`/new`, `/reset`), idle-based auto-reset, daily resets at configurable hour. Per-session-type reset policies.

**Our implementation:** Lightweight session segmentation. Conversations are split into segments; compaction handles the rest. No new infra — integrates with the compaction system.

### How it works

```
Message arrives for agent-conversation task
      │
      ▼
Check: time since last message?
      │
      ├── < 2 hours ──► SAME SEGMENT: load full recent history
      │
      ├── 2-8 hours ──► NEW SEGMENT: compact old segment, start fresh with summary
      │
      └── > 8 hours ──► NEW DAY: compact everything, start with just memory + today's tasks
      │
Also check: does message contain reset trigger?
      │
      ├── "new topic" / "start fresh" / "reset" ──► force new segment
      │
      └── No trigger ──► continue as above
```

### Implementation (inside agent-conversation task)

```typescript
const IDLE_THRESHOLD_MINUTES = 120; // 2 hours
const DAY_THRESHOLD_MINUTES = 480;  // 8 hours

async function resolveSessionContext(clientId: string, newMessage: string) {
  const lastMessage = await db.getLastInteraction(clientId, { type: 'ai_conversation' });
  const minutesSinceLastMessage = lastMessage
    ? differenceInMinutes(new Date(), lastMessage.created_at)
    : Infinity;

  // Check for explicit reset triggers
  const resetTriggers = ['new topic', 'start fresh', 'reset', 'different question'];
  const isReset = resetTriggers.some(t => newMessage.toLowerCase().includes(t));

  if (isReset || minutesSinceLastMessage > DAY_THRESHOLD_MINUTES) {
    // NEW DAY or EXPLICIT RESET: compact everything, start clean
    await triggerCompaction(clientId, { compactAll: true });
    return {
      recentMessages: [],
      summaries: await db.getConversationSummaries(clientId, { limit: 3 }),
      sessionType: 'new_day',
    };
  }

  if (minutesSinceLastMessage > IDLE_THRESHOLD_MINUTES) {
    // NEW SEGMENT: compact old, keep a bridge summary
    await triggerCompaction(clientId, { keepRecent: 5 }); // keep last 5 as bridge
    return {
      recentMessages: await db.getRecentMessages(clientId, { limit: 5 }),
      summaries: await db.getConversationSummaries(clientId, { limit: 3 }),
      sessionType: 'new_segment',
    };
  }

  // SAME SEGMENT: load full recent history
  return {
    recentMessages: await db.getRecentMessages(clientId, { limit: 50 }),
    summaries: [],
    sessionType: 'continuation',
  };
}
```

### Agent experience

Transparent. The agent doesn't see session boundaries. They just notice:
- Morning conversations are crisp (no leftover context from yesterday)
- Switching topics mid-day doesn't confuse the AI
- The AI always remembers important things (they're in memory, not in conversation history)

The agent CAN say "start fresh" or "new topic" to force a clean slate if the AI seems confused.

### Configurable per-client (future)

Store idle threshold in `ai_memory` under `preferences`:
```
key: "preferences"
value: "... Session idle timeout: 60 minutes (agent prefers quick context resets)."
```

The agent-conversation task reads this from memory and adjusts thresholds.

---

## 5. Sub-Agent Spawning (Medium Priority — Design Now, Build Post-MVP)

**Problem solved:** Complex requests like "Compare these 3 properties, check recent sales, and draft a message to Sarah" require sequential tool calls that burn time and context. Parallel sub-tasks would be faster.

**OpenClaw approach:** `sessions_spawn` — parent spawns child agent with its own context, timeout, model. Child returns results.

**Our implementation:** Maps directly to Trigger.dev `triggerAndWait`. The parent `agent-conversation` task spawns child tasks that run in parallel and return results.

### Architecture sketch

```
agent-conversation (parent task)
│
├── Model decides it needs parallel research
│
├── triggerAndWait([
│     { task: "property-research", payload: { properties: [...] } },
│     { task: "comps-lookup", payload: { addresses: [...] } },
│   ])
│
├── Both run in parallel as separate Trigger.dev tasks
│   ├── property-research: uses Haiku, fetches property data
│   └── comps-lookup: uses Haiku, searches comparable sales
│
├── Results returned to parent
│
└── Parent model synthesizes results + drafts message to Sarah
```

### Task definition pattern

```typescript
export const propertyResearch = task({
  id: "property-research",
  retry: { maxAttempts: 2 },
  run: async (payload: { clientId: string; properties: string[] }) => {
    const results = [];
    for (const property of payload.properties) {
      const data = await generateText({
        model: registry.languageModel("anthropic:claude-haiku-4-5"),
        tools: { search_property: propertySearchTool },
        prompt: `Research this property: ${property}. Return: address, price, PSF, tenure, floor area, district, last transaction.`,
      });
      results.push(data.text);
    }
    return results;
  },
});
```

### When to spawn sub-agents

The parent model doesn't decide — we add a tool:

```typescript
parallel_research: tool({
  description: 'Run multiple research tasks in parallel when the user needs information about several properties, contacts, or topics at once. Faster than doing them one by one.',
  inputSchema: z.object({
    tasks: z.array(z.object({
      type: z.enum(['property-research', 'comps-lookup', 'contact-enrichment']),
      query: z.string(),
    })),
  }),
  execute: async ({ tasks }) => {
    const handles = await Promise.all(
      tasks.map(t => subtaskMap[t.type].triggerAndWait({ clientId, query: t.query }))
    );
    return handles.map((h, i) => `## ${tasks[i].type}: ${tasks[i].query}\n${h}`).join('\n\n');
  },
}),
```

### Build order

Not MVP. Build when:
- Agent tool loops regularly exceed 5 steps
- Users request multi-property comparisons frequently
- Sequential execution becomes a noticeable bottleneck

---

## 6. Browser Automation — Web Data Operations (Medium Priority — Future)

**Problem solved:** Platforms without direct API integration (LinkedIn, X/Twitter, MLS portals, competitor listing sites) require browser control. Property research, lead intelligence, competitor monitoring, and social media operations all need robust, anti-detection-capable browser automation.

**Core principle:** Our users are non-technical RE agents. They will never write Playwright scripts or debug browser selectors. The browser layer must be **fully managed** — natural language in, structured data out.

**Previous approach (Section 6 v1):** DIY Playwright + semantic snapshots inside Trigger.dev. Discarded — too much maintenance burden, no anti-detection, brittle on adversarial sites like LinkedIn.

### Platform Evaluation (Feb 2026)

Evaluated 5 platforms for browser automation. Key finding: the market has split into **infrastructure** (you write the code, they run the browsers) vs **outcomes** (you describe what you want, they handle everything).

| | **TinyFish** | **Browserbase** | **OpenClaw Browser** | **Playwright (local)** | **Vercel agent-browser** |
|---|---|---|---|---|---|
| **Abstraction** | Highest (NL → data) | Mid (you code, they run) | Mid (CDP + AI) | Lowest (raw code) | Low (CLI for AI) |
| **Anti-detection** | All-in (proxies, fingerprints, anti-bot) | Stealth mode, captchas, proxies | None built-in | None (need playwright-stealth) | None |
| **LinkedIn viability** | Medium-High | High (with Advanced stealth) | Low-Medium | Low | Low |
| **Our users can use it** | Yes (API call) | No (need Playwright code) | No (need CDP knowledge) | No | No |
| **Pricing** | $0.015/step, $150/mo Pro | $99/mo Startup | Free (OSS) + LLM costs | Free | Free |

### Decision: TinyFish Primary + Browserbase Fallback

```
Browser Automation Strategy
├── Layer 1: TinyFish (PRIMARY — 90% of use cases)
│   ├── Natural language goal → structured data
│   ├── All infra managed (browsers, proxies, anti-bot, LLM inference)
│   ├── $0.015/step all-in, ~$150-270/mo at our scale
│   ├── 1,000 parallel operations, 98.7% success rate
│   ├── Claude MCP native integration
│   └── Used for: lead research, listing scraping, competitor monitoring,
│       conference data, social media extraction
│
├── Layer 2: Browserbase + Stagehand (FALLBACK — 10% edge cases)
│   ├── When TinyFish can't handle it (complex multi-step auth flows,
│   │   LinkedIn deep sessions, custom interaction sequences)
│   ├── Playwright-native — we write the specific automation
│   ├── Session persistence (Contexts API) for login state
│   ├── Trigger.dev integration (first-class)
│   ├── $99/mo for 500 browser hours
│   └── Used for: LinkedIn authenticated sessions, MLS portal logins,
│       complex form submissions that need precise control
│
└── Layer 3: OpenClaw Browser (INTERNAL ONLY — dev/debug)
    ├── Chrome extension mode for leveraging existing login state
    ├── Remote CDP mode can connect TO Browserbase
    ├── No anti-detection — only for internal tools
    └── Used for: debugging, testing, one-off scrapes during development
```

### Why TinyFish Primary

**1. Architecture matches our "better harness = dumber model" pattern:**

TinyFish internally splits browser operations into:
- **Reasoning steps (~20-30%)** — Large LLMs (GPT-4, Gemini) for ambiguous decisions
- **Execution steps (~70-80%)** — Small specialized models for mechanical actions (click, type, paginate) at millisecond speed

This is exactly our cost optimization pattern. They've applied it to browser automation.

**2. AgentQL under the hood — semantic selectors, not DOM positions:**

TinyFish is built on AgentQL, their open-source query language. It parses both HTML structure AND the accessibility tree (dual input), pre-processes to strip noise, then routes to different LLMs based on task complexity. Selectors are semantic and self-healing — same query works across UI changes.

```
How AgentQL works:
HTML + Accessibility Tree → Pre-processing (strip noise)
  → Pipeline selection (scraping vs automation)
    → LLM routing (simple → small model, complex → GPT-4/Gemini)
      → Grounding + validation against actual DOM
        → Verified result
```

**3. Production-proven at scale (not a demo):**

| Customer | Use Case | Scale |
|---|---|---|
| **Google Hotels** | Convert hotel websites → structured availability data | 40,000+ properties |
| **DoorDash** | Authenticated checkout data across competitor platforms | 20+ countries, 3x daily |
| **ClassPass** | Venue data collection and operational workflows | 835 venues daily, 98.6% time reduction |
| **Jobright.ai** | Navigate and complete job applications across platforms | 1M+ professionals served |
| **Amplemarket** | Extract lead data from conference websites | Dozens of events/mo, zero custom code |

**4. Mind2Web benchmarks (Feb 12, 2026) — not close:**

Online-Mind2Web: 300 tasks across 136 live websites, 3 difficulty levels.

| Agent | Easy | Medium | Hard | **Total** |
|---|---|---|---|---|
| **TinyFish** | 97.5% | 89.9% | 81.9% | **89.9%** |
| OpenAI Operator | 83.1% | 58.0% | 43.2% | 61.3% |
| Claude Computer Use 3.7 | 90.4% | 49.0% | 32.4% | 56.3% |
| Browser Use | 55.4% | 26.6% | 8.1% | 30.0% |

Key: Every other agent falls off a cliff on hard tasks (40-58 point drop). TinyFish only drops 15 points. That's the gap between "cool demo" and "production-ready." They published all 300 execution traces including failures.

**5. $47M raised** (ICONIQ Capital), $0.015/step all-in pricing:**

No separate bills for browsers ($0/hr), proxies ($0/GB), AI inference (included), or infrastructure. Usage-based, decreasing as operations get codified. At our scale (~30K steps/mo = ~$270/mo Pro plan).

### Architecture: How It Integrates

```
agent-conversation task (Trigger.dev)
│
├── Model decides it needs web data
│   (e.g., "research this company on LinkedIn", "check listing prices")
│
├── Calls `browse_web` tool
│   │
│   ├── SIMPLE (TinyFish — default):
│   │   POST https://agent.tinyfish.ai/v1/automation/run-sse
│   │   { "url": "...", "goal": "...", "proxy_config": { "enabled": true } }
│   │   → Returns structured data via SSE stream
│   │   → No browser management, no Playwright, no cleanup
│   │
│   └── COMPLEX (Browserbase — fallback):
│       const browser = await chromium.connectOverCDP(
│         `wss://connect.browserbase.com?apiKey=${KEY}&enableProxy=true`
│       );
│       → Full Playwright control for multi-step auth flows
│       → Session context persisted for LinkedIn login state
│       → Manual cleanup, but precise control
│
└── Structured data returned as tool result to parent model
```

### Tool Definitions

```typescript
// Primary: TinyFish — natural language web operations
browse_web: tool({
  description: 'Browse a website to extract data or perform actions. Use for: property lookups, LinkedIn research, competitor monitoring, conference lead extraction. Describe what you need in plain English.',
  inputSchema: z.object({
    url: z.string().describe('Target URL'),
    goal: z.string().describe('What to extract or do, in plain English'),
    useProxy: z.boolean().optional().default(true)
      .describe('Enable residential proxy for anti-detection (default: true)'),
  }),
  execute: async ({ url, goal, useProxy }) => {
    const response = await fetch('https://agent.tinyfish.ai/v1/automation/run-sse', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': process.env.TINYFISH_API_KEY!,
      },
      body: JSON.stringify({
        url,
        goal,
        proxy_config: { enabled: useProxy },
      }),
    });

    // Stream SSE response, collect final result
    const result = await collectSSEResult(response);
    return result;
  },
}),

// Fallback: Browserbase — when TinyFish can't handle it
browse_web_advanced: tool({
  description: 'Advanced browser session for complex multi-step flows requiring login state, precise element interaction, or long-running sessions. Only use when browse_web fails or when the task requires authenticated session persistence (e.g., LinkedIn deep profile access with existing login).',
  inputSchema: z.object({
    instructions: z.string().describe('Step-by-step instructions for the browser session'),
    sessionContextId: z.string().optional()
      .describe('Reuse a previous session context (for login persistence)'),
  }),
  execute: async ({ instructions, sessionContextId }) => {
    // Triggers a Trigger.dev subtask with Browserbase
    const result = await browserResearchTask.triggerAndWait({
      clientId,
      instructions,
      sessionContextId,
    });
    return result;
  },
}),
```

### Browserbase Subtask (for fallback)

```typescript
export const browserResearch = task({
  id: "browser-research",
  retry: { maxAttempts: 2 },
  run: async (payload: {
    clientId: string;
    instructions: string;
    sessionContextId?: string;
  }) => {
    const { chromium } = await import('playwright-core');

    // Connect to Browserbase with stealth + proxy
    const browser = await chromium.connectOverCDP(
      `wss://connect.browserbase.com?apiKey=${process.env.BROWSERBASE_API_KEY}&enableProxy=true`
      + (payload.sessionContextId ? `&contextId=${payload.sessionContextId}` : '')
    );

    const context = browser.contexts()[0];
    const page = context.pages()[0];

    try {
      // Use Stagehand for AI-driven navigation
      // or manual Playwright steps based on instructions
      const result = await executeInstructions(page, payload.instructions);
      return result;
    } finally {
      await browser.close();
    }
  },
});
```

### Use Cases Mapped to Tools

| Use Case | Tool | Why |
|---|---|---|
| **Property listing lookup** | `browse_web` (TinyFish) | Simple extraction, public site |
| **LinkedIn company research** | `browse_web` (TinyFish) | Natural language, anti-detection included |
| **LinkedIn deep profile + connections** | `browse_web_advanced` (Browserbase) | Needs auth session persistence |
| **Competitor price monitoring (batch)** | `browse_web` (TinyFish) | Parallel operations across sites |
| **MLS portal login + search** | `browse_web_advanced` (Browserbase) | Multi-step auth, form submission |
| **Conference lead extraction** | `browse_web` (TinyFish) | Amplemarket pattern — proven |
| **X/Twitter profile scraping** | `browse_web` (TinyFish) | Anti-detection handles X's bot protection |
| **Fill external CRM forms** | `browse_web_advanced` (Browserbase) | Precise element targeting needed |

### Cost Estimate

| Component | Monthly Cost | Notes |
|---|---|---|
| TinyFish Pro | $150 | 16,500 steps included |
| TinyFish overage | ~$120 | ~13,500 extra steps at $0.009/step |
| Browserbase Startup | $99 | 500 hours, fallback only |
| **Total** | **~$370/mo** | vs DIY: $200 infra + $500+ LLM + maintenance time |

For comparison: manual research by a human VA costs $2,000-4,000/mo for similar throughput.

### Risks & Mitigations

| Risk | Mitigation |
|---|---|
| **LinkedIn blocks TinyFish** | Fallback to Browserbase with session persistence. LinkedIn is the hardest site — test early. |
| **TinyFish rate limits at scale** | Enterprise plan ($custom) unlocks unlimited. Or batch via Trigger.dev to throttle. |
| **TinyFish goes down** | Browserbase fallback. Both tools are independent — no single point of failure. |
| **Data quality from NL extraction** | Validate outputs against schema. TinyFish's grounding layer helps but add our own validation. |
| **Anti-bot arms race** | Both TinyFish and Browserbase invest heavily in this. Their problem, not ours. |

### When to build

Not MVP. Build when:
- Property data APIs are insufficient
- Sales pipeline needs LinkedIn/X intelligence at scale
- Agents request "check this listing for me" or "research this company"
- Competitor monitoring feature (Listing Stalker, #15) is prioritized

**Phase 1:** TinyFish integration only (`browse_web` tool). Test against LinkedIn, property sites, conference pages.
**Phase 2:** Browserbase fallback (`browse_web_advanced` tool) for authenticated multi-step flows.
**Phase 3:** Batch operations via Trigger.dev — parallel TinyFish calls for bulk research (e.g., "research all 50 companies in my pipeline").

---

## 7. AI Scratch Pad — Knowledge Capture UI

**Problem solved:** Agents discover relevant content constantly — articles, tweets, listings, competitor intel — but capturing it into the system is friction-heavy. Current options: manually file into folders (librarian work) or lose the context entirely. The scraping problem compounds this — platforms like X.com paywall content, making even link-based capture unreliable.

**Core insight:** The less UI, the better. Agents aren't librarians. The AI should infer *why* something is interesting based on knowing the user — their active deals, current interests, and past behavior. But interests evolve, so the system needs a way to capture new signal without making the user explain themselves.

**Design principle:** Thin UI layer + tremendous signal value. Even a single tap of confirmation ("Is this for your sandbox madness?" → Yes) gives the AI enough to categorize, tag, and file correctly. The ratio of user effort to system value is extremely high.

### UX Flow: Link + Notes → AI Categorizes → User Confirms

```
┌──────────────────────────────────────────────────────┐
│  📋 SCRATCH PAD                             [CLOSE]   │
├──────────────────────────────────────────────────────┤
│                                                        │
│  Paste a link or drop some notes:                     │
│  ┌──────────────────────────────────────────────┐    │
│  │ https://x.com/founder/status/123456789       │    │
│  └──────────────────────────────────────────────┘    │
│                                                        │
│  Quick notes (optional):                              │
│  ┌──────────────────────────────────────────────┐    │
│  │ interesting agent architecture, multi-model   │    │
│  │ routing pattern                               │    │
│  └──────────────────────────────────────────────┘    │
│                                                        │
│                               [Save to Inbox →]       │
└──────────────────────────────────────────────────────┘

        ↓ AI processes (scrape + infer) ↓

┌──────────────────────────────────────────────────────┐
│  🤖 AI thinks this is for:                            │
├──────────────────────────────────────────────────────┤
│                                                        │
│  ┌─────────────────────┐  ┌─────────────────────┐   │
│  │ 🏗️ CRM Architecture │  │ 💰 Cost Optimization │   │
│  │ (Recommended)        │  │                      │   │
│  └─────────────────────┘  └─────────────────────┘   │
│                                                        │
│  ┌─────────────────────┐  ┌─────────────────────┐   │
│  │ 🤖 Agent Patterns   │  │ 📊 Competitor Intel  │   │
│  └─────────────────────┘  └─────────────────────┘   │
│                                                        │
│  Summary: "Thread about multi-model routing saving    │
│  94% on agent costs. Author uses Gemini Flash for     │
│  daily chat, escalates to Sonnet for complex tasks."  │
│                                                        │
│  Tags: #model-routing #cost-savings #agent-arch       │
│                                                        │
│              [✓ Looks good]    [✏️ Edit]               │
└──────────────────────────────────────────────────────┘
```

### Three Layers of Intelligence

| Layer | What it does | User effort |
|-------|-------------|-------------|
| **1. Scrape + Extract** | Fetch link content, handle paywalls/fallbacks, extract key points | Zero — automatic |
| **2. Infer Intent** | AI reads user's memory/OS (active projects, interests, past captures) to guess *why* this matters | Zero — automatic |
| **3. Confirm Signal** | 2-4 buttons: AI's best guesses for category. User taps one. | One tap — but extremely high value |

### Why User Signal > Pure Inference

Jet's insight: *"The OS is always a snapshot of your interests in the past. You always change. Anything new needs to be captured."*

Pure inference from memory works ~70% of the time (user is interested in X because they've always been interested in X). But the 30% — new interests, pivots, adjacent curiosity — is exactly where categorization fails and where a single tap of user signal is worth more than 10 rounds of AI reasoning.

The buttons aren't a form. They're a **poll**. The AI proposes, the user confirms. This is agentic UI at its thinnest — maximum value from minimum interaction.

### Implementation

```typescript
// POST /api/scratchpad — receives link + optional notes
export async function POST(req: Request) {
  const { url, notes } = await req.json();

  // Layer 1: Scrape + Extract
  const content = await scrapeUrl(url); // handles paywalls, fallbacks to cached/archive
  const summary = await generateText({
    model: registry.languageModel("google:gemini-2.5-flash"), // cheap
    prompt: `Summarize this content in 2-3 sentences. Extract key tags.\n\n${content}`,
  });

  // Layer 2: Infer Intent (read user's current interests from memory)
  const userContext = await db.rpc('search_memory', {
    p_client_id: clientId,
    p_query: 'current projects interests priorities',
    p_limit: 10,
  });

  const inference = await generateText({
    model: registry.languageModel("google:gemini-2.5-flash"),
    prompt: `Given the user's current context:\n${userContext}\n\nAnd this new content:\n${summary.text}\n\nSuggest 2-4 categories this might belong to. Return as JSON array of { id, label, confidence }.`,
  });

  // Return for Layer 3: user confirmation UI
  return Response.json({
    summary: summary.text,
    suggestedCategories: inference.parsed,
    tags: extractTags(summary.text),
    rawContent: content,
  });
}

// POST /api/scratchpad/confirm — user taps a category
export async function confirmCapture(req: Request) {
  const { captureId, selectedCategory, summary, tags, url } = await req.json();

  // File to the right place
  await db.createCapture({
    clientId,
    url,
    summary,
    category: selectedCategory,
    tags,
    source: 'scratchpad',
    userConfirmed: true, // this signal is gold
  });

  // Update user interest model (memory)
  await db.updateMemory(clientId, {
    key: `interests/${selectedCategory}`,
    value: `User captured content about ${selectedCategory}. Latest: ${summary}`,
    operation: 'append',
  });
}
```

### Scraping Fallback Chain

Platforms like X.com actively block scraping. The system needs a graceful degradation chain:

```
1. Direct fetch (works for blogs, docs, open sites)
     ↓ fails
2. Cached/archive version (Google Cache, Wayback Machine, archive.today)
     ↓ fails
3. User-provided notes only (extract what we can from their description)
     ↓ always works
4. Ask user to paste content ("Couldn't access this link — paste the key content?")
```

The point: never block capture because scraping failed. The user's notes alone are often enough for the AI to categorize correctly.

### Where This Lives in the Product

- **Dashboard:** Quick-access scratch pad button (floating action or header shortcut)
- **WhatsApp:** Agent sends a link → AI auto-captures to scratch pad, asks for confirmation via quick reply buttons
- **Mobile:** Optimized for phone — the primary capture use case is "I'm scrolling and found something interesting"

### Build Order

**Phase 1 (MVP):**
- Simple capture form: URL + notes → save to inbox
- No AI inference yet — just structured storage
- Dashboard list view of captures

**Phase 2 (AI Inference):**
- Auto-scraping with fallback chain
- AI summarization (Gemini Flash — cheap)
- Category inference from user memory
- 2-4 button confirmation UI

**Phase 3 (Smart Capture):**
- WhatsApp integration (send link → auto-capture)
- Interest model updates from confirmations
- "Related captures" — surface past saves when new content matches
- Browser extension for one-click capture

---

## 8. Agent Filesystem — Structured Knowledge Home

**Problem solved:** The AI generates and accumulates content constantly — meeting notes, research, memory logs, artifacts, scratchpad captures, deal docs. Without a structured filesystem, everything ends up in flat DB rows with no spatial organization. The agent (human) can't browse, and the AI can't reason about "where things are."

**OpenClaw approach:** A literal folder tree on disk (`~/clawd/`). The agent's single home directory with organized drawers. Domain separation (business vs personal), daily memory logs in `memory/`, skills in `skills/`, root-level identity files (MEMORY.md, SOUL.md, USER.md, TOOLS.md).

**Why it works (OpenClaw's rationale):**
1. **Domain separation** — `business/` and `personal/` keep work and life apart. AI knows where to file without asking.
2. **Memory system** — `memory/` holds raw daily logs (YYYY-MM-DD.md). `MEMORY.md` holds distilled long-term memory. Agent wakes up fresh every session and reads these to know who it is.
3. **Skills are local** — custom skills in `skills/` so the agent can reference and extend them.
4. **It grows with you** — start with top-level folders, add subfolders as topics deepen. Structure upfront keeps things organized from day one.

### OpenClaw's Folder Structure (Reference)

```
~/clawd/
├── business/           # Work stuff — projects, sales, research, team docs
│   ├── AgentZero/
│   ├── assets/
│   ├── coding/
│   ├── comms/
│   ├── metrics/
│   ├── paid-ads/
│   ├── research/
│   ├── sales/
│   └── team/
├── docs/               # Documentation and references
├── downloads/          # Temporary files, downloads, exports
├── memory/             # Daily memory logs (YYYY-MM-DD.md files)
├── personal/           # Life stuff — health, finance, travel, etc.
│   ├── Christianity/
│   ├── dating/
│   ├── finance/
│   ├── health/
│   ├── productivity/
│   ├── research/
│   └── travel/
├── skills/             # Custom skills your agent can use
│   ├── apify/
│   └── todoist/
└── vps/                # Server management notes and configs
    ├── mistakes/
    ├── security/
    └── vps-stats/

Key root files:
  MEMORY.md   — long-term memory (curated, persistent)
  SOUL.md     — personality and behavior rules
  USER.md     — info about you so the agent can help better
  TOOLS.md    — notes about your specific tool setup
```

### Deeper Pattern: Knowledge = Code (PKM References)

**Sources:**
- Heinrich (@arscontexta) — ["obsidian + claude code 101"](https://x.com/arscontexta) (Jan 2026) — year-long experiment running Claude Code on Obsidian vaults as an "operating system for thinking"
- [ballred/obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm) — Obsidian + Claude Code PKM starter kit with agents, skills, hooks, and goal alignment

**Core thesis:** *Knowledge bases and codebases have a lot in common. They're both folders of text files with relationships between them, they both have conventions and patterns, and they both benefit from agents that can navigate and operate them.*

The shift: **You don't take notes anymore. You operate a system that takes notes.** The human role evolves from writer to editor, from creator to curator. The AI handles implementation (filing, linking, structuring) while the human provides judgment (what matters, what connects).

#### Key Patterns We Should Adopt

**1. Agent Orientation Layers — How the AI Finds Things Fast**

Heinrich's system uses layered discovery so the AI doesn't have to read every file:

```
Layer 1: Tree structure (folder layout)         — "what exists?"
Layer 2: Index file (one-line per note)          — "what's each thing about?"
Layer 3: Topic pages / MOCs (maps of content)    — "how do things relate?"
Layer 4: Follow links within notes               — "deep dive into connections"
```

The AI starts broad, narrows to what's relevant, then follows links. For us: the AI scans the `client_files` tree → reads an index → follows metadata links to related files.

**Our implementation:** Auto-generated `INDEX.md` at each folder level:

```markdown
# /business/deals/ — Index

| File | Summary | Last Updated |
|------|---------|-------------|
| riveria-1208/ | 3BR condo, Sarah Lee buyer, LOI stage | Feb 12 |
| tampines-blk42/ | HDB listing, pending photos | Feb 10 |
| paya-lebar-quarter/ | Mixed-use, David Tan interested | Feb 8 |
```

Generated automatically by a Trigger.dev cron or on file changes. Cheap — Gemini Flash scans new/changed files and updates the one-liner. The AI reads the index first, then drills into specific files only when needed.

**2. Agent Breadcrumbs — AI Leaves Notes for Future Sessions**

Heinrich: *"When Claude discovers something useful about navigating a topic, it records that in the topic page. Future sessions read those notes and learn from past navigation."*

This is cross-session learning without fine-tuning. The AI annotates its own filesystem:

```markdown
<!-- AI Navigation Note (2026-02-15): Sarah's deal folder has comps in
/artifacts/ not here — check both locations when asked about pricing. -->
```

**Our implementation:** A `_notes.md` file per deal/contact folder where the AI leaves breadcrumbs. Cheap to generate, extremely valuable for context across sessions.

**3. Notes as Claims, Not Topics**

Heinrich: *"Instead of 'thoughts on ai slop' you write 'quality is the hard part'. When you link to it, the title becomes part of your sentence naturally."*

For RE context: instead of `market-analysis.md`, name it `district-10-prices-peaked-q4-2025.md`. When the AI references it in a message, the filename IS the insight.

**4. Links as Reasoning Paths**

Heinrich: *"The network is the knowledge. A note with many incoming links is more valuable than an isolated note."*

Our `metadata.linkedContactId` and `metadata.linkedDealId` already enable this, but we should also support **cross-file links** in content — `[[/business/contacts/sarah-lee]]` syntax that the AI can follow. The dashboard renders these as clickable navigation.

**5. Vault Philosophy Per Client (from ballred/obsidian-claude-pkm)**

The ballred starter kit reinforces that every vault needs its own `CLAUDE.md` philosophy — and it shows a practical implementation with:
- **Agents** (`.claude/agents/`) — specialized AI modes (note-organizer, weekly-reviewer, goal-aligner, inbox-processor)
- **Skills** (`.claude/skills/`) — auto-discovered capabilities
- **Hooks** — auto-commit on save, session initialization (tree view at start)
- **Commands** — `/daily`, `/weekly`, `/push`, `/onboard`
- **Rules** — path-specific conventions (different markdown rules per folder)

For our RE CRM, the per-client `SOUL.md` already covers personality, but we should consider **per-folder conventions** — e.g., files in `/business/deals/` follow deal-doc conventions, files in `/captures/` follow scratch pad format, files in `/memory/` follow daily log format. The AI reads these conventions from a folder-level `.rules` file or from the client's SOUL.md.

#### The Obsidian Analogy for Our Product

| Obsidian Vault Pattern | Our RE CRM Equivalent |
|----------------------|---------------------|
| `CLAUDE.md` (teaches AI the system) | `SOUL.md` + `PREFERENCES.md` (root files) |
| `00_inbox/` (capture zone) | Scratch Pad → `/captures/` |
| `01_thinking/` (synthesis) | `/business/research/` |
| `02_reference/` (external knowledge) | `/captures/articles/`, `/captures/competitors/` |
| `memory/` daily logs | `/memory/YYYY-MM-DD.md` |
| `MEMORY.md` (distilled long-term) | `ai_memory` table + `MEMORY.md` root file |
| Topic pages / MOCs | Auto-generated `INDEX.md` per folder |
| `[[wiki links]]` | Cross-file links + metadata `linkedContactId`/`linkedDealId` |
| Hooks (tree at session start) | AI orientation: scan tree → read index → drill in |
| Skills (auto-discovered) | AI tools (`save_file`, `read_file`, etc.) |
| Agents (note-organizer, inbox-processor) | Trigger.dev tasks (compaction, filing, enrichment) |
| `/onboard` command | Client onboarding: create default folders + root files |

### Search Layer: QMD Pattern (Hybrid Search for Knowledge)

**Source:** [tobi/qmd](https://github.com/tobi/qmd) — Tobi Lütke's on-device search engine for markdown notes. *"Index your markdown notes, meeting transcripts, documentation, and knowledge bases. Search with keywords or natural language."*

A folder structure is useless without search. As files accumulate (meeting notes, captures, dossiers, artifacts), the AI can't read everything on every turn. QMD solves this with a hybrid search pipeline that combines keyword matching, semantic understanding, and LLM reranking — all running locally.

**QMD's architecture (what we're adapting):**

```
Query ──► LLM Query Expansion ──► [Original + 2 Variants]
                                        │
                     ┌──────────────────┼──────────────────┐
                     ▼                  ▼                  ▼
               BM25 (FTS5)       BM25 (FTS5)        BM25 (FTS5)
               Vector Search     Vector Search       Vector Search
                     │                  │                  │
                     └──────────────────┼──────────────────┘
                                        ▼
                              RRF Fusion (combine all lists)
                                        ▼
                              LLM Re-ranking (top 30)
                                        ▼
                              Position-Aware Blend
                                        ▼
                                  Final Results
```

**Key QMD concepts we adopt:**

| QMD Concept | What It Does | Our Supabase Equivalent |
|-------------|-------------|------------------------|
| **Collections** | Named sets of files (`~/notes`, `~/meetings`) | Folder-scoped queries on `client_files` (`/business/deals/`, `/captures/`) |
| **Context** | Folder-level descriptions that help search understand content | `metadata` on folder rows + folder `INDEX.md` files |
| **BM25 (FTS5)** | Fast keyword search | Supabase `tsvector` + `to_tsvector()` (already in Section 2) |
| **Vector search** | Semantic similarity via embeddings | Supabase `pgvector` (already in Section 2) |
| **Hybrid + Reranking** | Query expansion + RRF fusion + LLM rerank | Supabase RPC function combining FTS + vector + Gemini Flash reranking |
| **Content-addressable docids** | 6-char hash IDs for quick reference (`#abc123`) | `id` column shortcodes — AI can reference files by short ID |
| **Virtual paths** | `qmd://collection/path` for collection-scoped refs | Our existing `/business/deals/riveria-1208/` paths |
| **MCP Server** | Exposes search/get/multi-get tools to AI agents | Our `search_files`, `read_file`, `list_folder` tools |

**Why this matters for our product:** The RE agent's filesystem will accumulate hundreds of files per client within months — meeting notes, daily logs, captures, deal docs, contact dossiers, artifacts. Without hybrid search, the AI is blind to its own knowledge. With it, the agent can ask *"what did we discuss about D10 pricing?"* and get semantically relevant results from across the entire file tree, not just keyword matches.

#### Our Implementation: Hybrid File Search

```sql
-- Add to client_files table (extends Section 8 schema)

-- Full-text search column (auto-populated)
ALTER TABLE client_files ADD COLUMN search_text tsvector
  GENERATED ALWAYS AS (
    to_tsvector('english', coalesce(name, '') || ' ' || coalesce(content, ''))
  ) STORED;

-- Vector embedding column (populated async, like Section 2)
ALTER TABLE client_files ADD COLUMN embedding vector(1536);

-- Folder-level context description (QMD's "context" concept)
ALTER TABLE client_files ADD COLUMN context_description TEXT;
  -- e.g. folder '/business/deals/' has context "Active real estate deals and transaction docs"

-- Indexes
CREATE INDEX ON client_files USING gin (search_text);
CREATE INDEX ON client_files USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

```sql
-- Hybrid file search function (adapts QMD's pipeline for Supabase)
CREATE OR REPLACE FUNCTION search_client_files(
  p_client_id TEXT,
  p_query TEXT,
  p_query_embedding vector(1536) DEFAULT NULL,
  p_folder TEXT DEFAULT NULL,        -- scope to folder, e.g. '/business/deals/'
  p_limit INTEGER DEFAULT 10
)
RETURNS TABLE (
  id UUID, path TEXT, name TEXT, snippet TEXT,
  fts_score FLOAT, vec_score FLOAT, combined_score FLOAT
)
LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  WITH
  -- BM25 keyword results
  fts AS (
    SELECT f.id, f.path, f.name,
      ts_headline('english', f.content, plainto_tsquery('english', p_query),
        'MaxWords=60, MinWords=20') as snippet,
      ts_rank(f.search_text, plainto_tsquery('english', p_query)) as score
    FROM client_files f
    WHERE f.client_id = p_client_id
      AND f.type = 'file'
      AND f.search_text @@ plainto_tsquery('english', p_query)
      AND (p_folder IS NULL OR f.path LIKE p_folder || '%')
    ORDER BY score DESC
    LIMIT 30
  ),
  -- Vector semantic results (if embedding provided)
  vec AS (
    SELECT f.id, f.path, f.name,
      substring(f.content, 1, 200) as snippet,
      (1 - (f.embedding <=> p_query_embedding)) as score
    FROM client_files f
    WHERE f.client_id = p_client_id
      AND f.type = 'file'
      AND f.embedding IS NOT NULL
      AND p_query_embedding IS NOT NULL
      AND (p_folder IS NULL OR f.path LIKE p_folder || '%')
    ORDER BY f.embedding <=> p_query_embedding
    LIMIT 30
  ),
  -- RRF Fusion (simplified — QMD uses k=60)
  combined AS (
    SELECT
      COALESCE(fts.id, vec.id) as id,
      COALESCE(fts.path, vec.path) as path,
      COALESCE(fts.name, vec.name) as name,
      COALESCE(fts.snippet, vec.snippet) as snippet,
      COALESCE(fts.score, 0) as fts_score,
      COALESCE(vec.score, 0) as vec_score,
      -- Weighted combination: 0.4 FTS + 0.6 vector (semantic wins for natural language)
      (0.4 * COALESCE(fts.score, 0) + 0.6 * COALESCE(vec.score, 0)) as combined_score
    FROM fts
    FULL OUTER JOIN vec ON fts.id = vec.id
  )
  SELECT c.id, c.path, c.name, c.snippet, c.fts_score, c.vec_score, c.combined_score
  FROM combined c
  ORDER BY c.combined_score DESC
  LIMIT p_limit;
END;
$$;
```

#### Updated `search_files` Tool (with Hybrid Search)

```typescript
search_files: tool({
  description: 'Search across all files by content, natural language, or tags. Uses hybrid keyword + semantic search for best results.',
  inputSchema: z.object({
    query: z.string().describe('What to search for — natural language, keywords, or a question'),
    folder: z.string().optional().describe('Limit search to a folder path, e.g. /business/deals/'),
    mode: z.enum(['fast', 'deep']).optional().default('fast')
      .describe('fast = keyword only (FTS), deep = hybrid FTS + vector + optional reranking'),
  }),
  execute: async ({ query, folder, mode }) => {
    if (mode === 'fast') {
      // BM25 only — cheap, no embedding needed
      const results = await db.rpc('search_client_files', {
        p_client_id: clientId,
        p_query: query,
        p_folder: folder,
        p_limit: 10,
      });
      return formatSearchResults(results);
    }

    // Deep: embed query → hybrid search
    const queryEmbedding = await openai.embeddings.create({
      model: 'text-embedding-3-small',
      input: query,
    });

    const results = await db.rpc('search_client_files', {
      p_client_id: clientId,
      p_query: query,
      p_query_embedding: queryEmbedding.data[0].embedding,
      p_folder: folder,
      p_limit: 10,
    });

    return formatSearchResults(results);
  },
}),
```

#### Folder Context (QMD's Best Idea)

QMD lets you annotate paths with descriptions that help search understand your content:

```sh
qmd context add qmd://meetings "Meeting notes and summaries"
qmd context add qmd://journals/2025 "Daily notes from 2025"
```

We do the same with `context_description` on folder rows:

```typescript
// Auto-set on folder creation
const DEFAULT_FOLDER_CONTEXTS: Record<string, string> = {
  '/business/deals/':     'Active real estate deals, transaction documents, offer terms, comps',
  '/business/contacts/':  'Contact dossiers — buyer/seller profiles, preferences, interaction history',
  '/business/research/':  'Market research, pricing analysis, district reports',
  '/captures/':           'Scratch pad captures — articles, ideas, competitor intel from web',
  '/captures/articles/':  'Saved articles and threads about tech, AI, real estate',
  '/captures/competitors/': 'Competitor analysis and intel',
  '/memory/':             'Daily AI activity logs and session records',
  '/memory/briefings/':   'Morning briefing summaries',
  '/artifacts/':          'AI-generated deliverables — comps reports, decks, PDFs',
};
```

When the AI searches, folder context is included in results — so "API docs" found in `/captures/articles/` gets context "Saved articles and threads" vs the same match in `/business/research/` getting "Market research, pricing analysis." The AI can disambiguate.

#### Embedding Pipeline (Async, Cheap)

```typescript
// Trigger.dev task: runs after file create/update
export const embedFile = task({
  id: "embed-client-file",
  retry: { maxAttempts: 2 },
  run: async ({ clientId, fileId }: { clientId: string; fileId: string }) => {
    const file = await db.getFile(fileId);
    if (!file.content || file.content.length < 50) return; // skip tiny files

    const embedding = await openai.embeddings.create({
      model: 'text-embedding-3-small', // $0.02/MTok — negligible
      input: `${file.name}\n\n${file.content}`.slice(0, 8000), // cap at ~2K tokens
    });

    await db.updateFile(fileId, {
      embedding: embedding.data[0].embedding,
    });
  },
});
```

Triggered on every `save_file` call. Cost is negligible — even 1,000 files/month = ~$0.04.

### Our Adaptation: Per-Client Virtual Filesystem

OpenClaw runs on a VPS with real disk access. Our agents run in Supabase + Trigger.dev — no persistent disk. We need the same organizational benefit stored in the database.

**Design:** A `client_files` table that mirrors a filesystem. The AI reads/writes to "paths" that feel like folders. The dashboard renders a file browser. Artifacts, captures, notes — everything has a location.

### Schema

```sql
CREATE TABLE client_files (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  path TEXT NOT NULL,               -- '/business/deals/riveria-1208/offer-terms.md'
  name TEXT NOT NULL,               -- 'offer-terms.md'
  type TEXT NOT NULL,               -- 'file' or 'folder'
  content_type TEXT,                -- 'markdown', 'json', 'pdf', 'image', 'artifact'
  content TEXT,                     -- file content (markdown, text, JSON)
  storage_url TEXT,                 -- for binary files (PDFs, images) → Supabase Storage
  metadata JSONB DEFAULT '{}',     -- tags, source, category, linked_contact_id, etc.
  parent_path TEXT,                 -- '/business/deals/riveria-1208/'
  size_bytes INTEGER,
  created_by TEXT DEFAULT 'ai',     -- 'ai' or 'agent'
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),

  UNIQUE(client_id, path)
);

-- Fast lookups
CREATE INDEX ON client_files (client_id, parent_path);  -- list folder contents
CREATE INDEX ON client_files (client_id, path);          -- direct path access
CREATE INDEX ON client_files USING gin (metadata);       -- tag/metadata search

-- RLS
ALTER TABLE client_files ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON client_files
  FOR ALL USING (client_id = current_setting('app.client_id'));
```

### Default Folder Structure (Created Per Client on Onboarding)

```typescript
const DEFAULT_FOLDERS = [
  // Work
  '/business/',
  '/business/deals/',           // Active deal folders (auto-created per deal)
  '/business/contacts/',        // Contact dossiers
  '/business/research/',        // Market research, comps, analysis
  '/business/listings/',        // Active listing materials
  '/business/templates/',       // Message templates, scripts

  // Knowledge capture (ties into Section 7: Scratch Pad)
  '/captures/',                 // Scratch pad items land here
  '/captures/articles/',
  '/captures/competitors/',
  '/captures/ideas/',

  // AI system files
  '/memory/',                   // Daily memory logs (YYYY-MM-DD.md)
  '/artifacts/',                // AI-generated deliverables (reports, decks, comps)

  // Agent identity (maps to SOUL.md, USER.md concept)
  // These are stored as root-level files, not folders
];

const ROOT_FILES = [
  { path: '/MEMORY.md', content: '# Long-Term Memory\n\n(AI-curated, persistent across sessions)' },
  { path: '/SOUL.md', content: '# AI Personality\n\n(Generated from onboarding — tone, style, boundaries)' },
  { path: '/PREFERENCES.md', content: '# Agent Preferences\n\n(Communication style, working hours, notification prefs)' },
];
```

### AI Tools for Filesystem

```typescript
const fileTools = {
  save_file: tool({
    description: 'Save content to the agent\'s file system. Use for meeting notes, research, drafts, or any content worth keeping. AI auto-selects the right folder based on content type.',
    inputSchema: z.object({
      path: z.string().describe('File path, e.g. /business/deals/riveria-1208/meeting-notes-feb11.md'),
      content: z.string(),
      metadata: z.object({
        tags: z.array(z.string()).optional(),
        source: z.string().optional(),       // 'scratchpad', 'meeting', 'whatsapp', 'ai-generated'
        linkedContactId: z.string().optional(),
        linkedDealId: z.string().optional(),
      }).optional(),
    }),
    execute: async ({ path, content, metadata }) => {
      // Auto-create parent folders if they don't exist
      await ensureParentFolders(clientId, path);
      await db.upsertFile({ clientId, path, name: basename(path), content, metadata });
      return `Saved to ${path}`;
    },
  }),

  read_file: tool({
    description: 'Read a file from the agent\'s file system.',
    inputSchema: z.object({ path: z.string() }),
    execute: async ({ path }) => {
      const file = await db.getFile(clientId, path);
      return file ? file.content : `File not found: ${path}`;
    },
  }),

  list_folder: tool({
    description: 'List contents of a folder in the agent\'s file system.',
    inputSchema: z.object({ path: z.string() }),
    execute: async ({ path }) => {
      const items = await db.listFolder(clientId, path);
      return items.map(i => `${i.type === 'folder' ? '📁' : '📄'} ${i.name}`).join('\n');
    },
  }),

  search_files: tool({
    description: 'Search across all files by content or metadata tags.',
    inputSchema: z.object({
      query: z.string(),
      folder: z.string().optional().describe('Limit search to a folder path'),
    }),
    execute: async ({ query, folder }) => {
      const results = await db.searchFiles(clientId, query, { folder });
      return results.map(r => `${r.path} — ${r.snippet}`).join('\n\n');
    },
  }),
};
```

### How Existing Features Map to Folders

| Feature | Creates files in | Example path |
|---------|-----------------|-------------|
| **Scratch Pad capture** (Section 7) | `/captures/{category}/` | `/captures/articles/multi-model-routing.md` |
| **Meeting notes** (post-meeting skill) | `/business/deals/{deal}/` | `/business/deals/riveria-1208/meeting-feb11.md` |
| **AI artifacts** (sandbox output) | `/artifacts/` | `/artifacts/comps-report-d10-feb2026.pdf` |
| **Daily memory logs** | `/memory/` | `/memory/2026-02-15.md` |
| **Contact dossiers** | `/business/contacts/` | `/business/contacts/sarah-lee.md` |
| **Deal folders** (auto-created) | `/business/deals/` | `/business/deals/riveria-1208/` |
| **Morning briefings** | `/memory/briefings/` | `/memory/briefings/2026-02-15.md` |

### Dashboard: File Browser

```
┌──────────────────────────────────────────────────────────────┐
│  📂 FILES                                    [+ New] [Search]│
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  📁 business/                                    12 items     │
│    📁 deals/                                     5 items      │
│      📁 riveria-1208/                            3 items      │
│        📄 meeting-notes-feb11.md           Feb 11 • AI       │
│        📄 offer-terms-draft.md             Feb 12 • AI       │
│        📄 comps-report.pdf                 Feb 10 • AI       │
│    📁 contacts/                                  28 items     │
│    📁 research/                                  7 items      │
│                                                               │
│  📁 captures/                                    15 items     │
│    📁 articles/                                  8 items      │
│    📁 competitors/                               4 items      │
│    📁 ideas/                                     3 items      │
│                                                               │
│  📁 memory/                                      45 items     │
│  📁 artifacts/                                   12 items     │
│                                                               │
│  📄 MEMORY.md                              Today • AI        │
│  📄 SOUL.md                                Feb 1 • Setup     │
│  📄 PREFERENCES.md                         Feb 5 • Agent     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Auto-Filing: AI Knows Where Things Go

The key insight from OpenClaw: *"When you say 'save this,' it knows where. When you say 'find that thing from last week,' it knows where to look."*

The folder structure gives the AI spatial reasoning about information. Instead of flat tags on DB rows, the AI thinks in paths:

```
Agent: "Save these meeting notes from the Sarah call"
AI: → saves to /business/deals/riveria-1208/meeting-feb15.md
     (knows the deal, knows the contact, picks the right folder)

Agent: "What did we discuss about D10 pricing last week?"
AI: → searches /business/deals/ for D10-related files from last week
     → also checks /memory/ daily logs for that date range
     → synthesizes from multiple sources
```

### Relationship to Existing Memory System

The filesystem doesn't replace `ai_memory` — it complements it:

| System | Purpose | Analogy |
|--------|---------|---------|
| `ai_memory` table | Key-value facts the AI needs instantly | Your brain's working memory |
| `MEMORY.md` root file | Curated long-term summary | Your journal's summary page |
| `/memory/` daily logs | Raw daily activity records | Your daily journal entries |
| `client_files` tree | Organized documents and artifacts | Your filing cabinet |

The AI reads `ai_memory` + `MEMORY.md` at conversation start (fast context). It reaches into `client_files` when it needs specific documents (tool call).

### Build Order

**Phase 1 (MVP):**
- `client_files` table + basic CRUD API
- Default folder creation on onboarding
- `save_file` and `read_file` tools for AI
- Deal folders auto-created when deals are created
- FTS search via `tsvector` (keyword-only `search_files` tool, mode: fast)
- Folder context descriptions on default folders

**Phase 2 (Dashboard + Search):**
- File browser UI in dashboard
- Click to view file content
- Manual file upload (agent adds docs)
- Search bar in file browser (FTS)
- Async embedding pipeline (Trigger.dev task on file create/update)
- Hybrid search: FTS + pgvector (`search_files` tool, mode: deep)

**Phase 3 (Smart Filing + PKM Patterns):**
- AI auto-files scratch pad captures into correct folders
- Auto-generated contact dossiers from conversation history
- Deal folder auto-populates (meeting notes, comps, messages)
- File linking (connect files to contacts/deals in metadata)
- Auto-generated `INDEX.md` per folder (orientation layer)
- AI breadcrumbs (`_notes.md` per folder — cross-session learning)
- Cross-file `[[links]]` rendered as clickable navigation in dashboard
- Per-folder conventions (deal-doc format, capture format, memory log format)
- LLM reranking on search results (Gemini Flash — cheap, QMD-style quality boost)

---

## 9. Skill Generation — Non-Technical Skill Authoring via Chat

**Problem solved:** Creating OpenClaw skills currently requires understanding SKILL.md structure, YAML frontmatter, prompt engineering, reference files, and script integration. Non-technical users (teammates, clients, future self on mobile) can't author skills through Telegram/WhatsApp — the chat interface provides zero visibility into the structured artifact being built.

**Source:** Reverse-engineered from [Refly](https://github.com/refly-ai/refly) (Apache 2.0) — specifically their "Vibe Mode" / Copilot-led Builder architecture. We extract the *pattern*, not the code. Their stack (NestJS + Prisma + PostgreSQL + Redis + Elasticsearch + BullMQ + ReactFlow) is a 15-package monorepo we don't need. The valuable IP is the agent architecture and compilation pipeline.

### What Refly Actually Does (Under the Hood)

Refly's "Vibe Mode" is **not** a compiler or DSL parser. It's a well-prompted LLM that outputs structured JSON, rendered on a ReactFlow canvas. The "Model-Native DSL" is marketing speak for "structured output schema."

**Two-Level Agent Architecture:**

```
User (natural language)
  → Copilot Agent (skill/workflow designer — canvas level)
    → Node Agents (individual task executors — task level)
```

**Copilot Agent** = a system-prompted LLM with 3 tools:
- `generate_workflow` — creates a complete WorkflowPlan from scratch
- `patch_workflow` — edits an existing plan (add/remove/update tasks, variables)
- `get_workflow_summary` — retrieves current plan structure for context in multi-turn

**Behavior loop (from `copilot-agent-system.md`):**
1. Understand user intent from natural language
2. Ask clarifying questions if requirements are ambiguous
3. Call `generate_workflow` with structured output conforming to WorkflowPlan schema
4. Present result, iterate on feedback via `patch_workflow`
5. Error handling: on tool failure, read error, fix, retry without user intervention

**WorkflowPlan Schema (Refly's internal representation):**

```typescript
interface WorkflowPlan {
  title: string;
  tasks: WorkflowTask[];
  variables: WorkflowVariable[];
}

interface WorkflowTask {
  id: string;                  // unique task ID
  title: string;               // "Research company LinkedIn"
  prompt: string;              // the actual instruction for this task's Node Agent
  toolsets: string[];          // what tools this task can use
  dependentTasks?: string[];   // task IDs that must run first (forms a DAG)
}

interface WorkflowVariable {
  variableId: string;
  variableType: "string" | "resource" | "option";
  name: string;                // "company_name"
  description: string;         // "The target company to research"
  required: boolean;
  options?: string[];          // for option type: predefined choices
  resourceTypes?: string[];    // for resource type: ["document", "image", "audio", "video"]
  value?: any;                 // default value
}
```

**Execution pipeline:**

```
Natural language query
  → CopilotAutogenService (orchestrator)
    → SkillService.sendInvokeSkillTask() (invokes Copilot Agent)
      → Copilot Agent generates WorkflowPlan
        → generateCanvasDataFromWorkflowPlan() converts to ReactFlow nodes + edges
          → CanvasService creates/updates the visual canvas
            → Optional: CLI `refly skill create` packages into redistributable skill
```

**Key insight:** The canvas is just a visualization layer. The actual skill is the WorkflowPlan JSON. For chat-based interfaces (WhatsApp/Telegram), we replace the canvas with a formatted text preview + approve/edit/cancel buttons.

### Our Adaptation: Skill Copilot Agent

We extract the pattern and map it onto our existing stack:

| Refly Component | Our Equivalent | Notes |
|---|---|---|
| `CopilotAutogenService` | OpenAI Agents SDK agent with `generate_skill` tool | Runs in E2B sandbox or direct API |
| `WorkflowPlan` schema | SKILL.md frontmatter + body | Already 80% there — our skills are richer (have references, scripts) |
| `copilot-agent-system.md` | Skill Copilot system prompt | Adapted for our SKILL.md format |
| ReactFlow canvas | WhatsApp/Telegram formatted preview message | Text-based, with approve/edit/cancel buttons |
| PostgreSQL + Prisma | Supabase `skill_drafts` table | Store in-progress skill authoring sessions |
| BullMQ execution | Trigger.dev (if complex) or direct (if simple) | Most skills don't need queues |
| Skill registry | Git repo `.claude/skills/` directory | OpenClaw's native discovery mechanism |

### Skill Copilot System Prompt (Core)

The Skill Copilot is a single agent with structured output tools. It runs as a conversational agent on WhatsApp/Telegram.

**System prompt structure:**

```markdown
You are the Skill Copilot — you help users create OpenClaw skills through conversation.

## Your Role
You design skills by understanding what the user wants to automate, then generating
a structured SKILL.md file. You are the "Copilot Agent" — you design, you don't execute.

## Behavior Mode: Guided Skill Design
1. UNDERSTAND: Parse the user's natural language description of what they want
2. CLARIFY: Ask 2-3 targeted questions if requirements are ambiguous:
   - What triggers this skill? (keywords, slash commands)
   - What inputs does the user provide vs what gets looked up?
   - What's the output? (file, message, API call, etc.)
   - What tools/integrations are needed?
3. GENERATE: Call `generate_skill` with the structured output
4. PRESENT: Show a formatted preview for approval
5. ITERATE: If user wants changes, call `patch_skill` (don't regenerate from scratch)

## Tool Selection Guide
- New skill or major restructure → `generate_skill`
- Minor edits (change a trigger, update a prompt section) → `patch_skill`
- User asks "what does it look like now?" → `get_skill_summary`

## Constraints
- Always ask at least 1 clarifying question before generating
- Never generate a skill with zero triggers
- Always include a description that explains WHEN to use the skill
- Reference files should only be included if the skill genuinely needs domain knowledge
- Keep prompt bodies concise — the skill prompt is a system prompt, not a novel
- Respond in the user's language
```

### `generate_skill` Tool Schema

This is the structured output tool the Skill Copilot calls. Maps directly to our SKILL.md format:

```typescript
interface GenerateSkillInput {
  // SKILL.md frontmatter
  name: string;                     // kebab-case skill name
  displayName: string;              // human-readable name
  description: string;              // when and why to use this skill
  triggers: string[];               // keywords/phrases that activate it
  category: "sales" | "research" | "ops" | "creative" | "general";

  // Execution config
  model?: string;                   // default: "gemini-2.5-flash" (cheap)
  escalationModel?: string;         // fallback: "kimi-k2" or "claude-sonnet"
  tools?: string[];                 // MCP tools or built-in tools needed

  // Variables (user inputs)
  variables: SkillVariable[];

  // Skill body (the actual prompt)
  systemPrompt: string;             // the instruction set
  outputFormat?: string;            // expected output structure

  // Optional: reference files
  references?: {
    filename: string;
    description: string;            // what this reference contains
    source: "url" | "file" | "inline";
    content?: string;               // for inline references
    url?: string;                   // for URL references to fetch
  }[];

  // Optional: steps (for multi-step skills)
  steps?: {
    id: string;
    title: string;
    prompt: string;
    tools?: string[];
    dependsOn?: string[];           // step IDs — forms DAG
  }[];
}

interface SkillVariable {
  name: string;                     // variable name (snake_case)
  type: "string" | "url" | "file" | "choice";
  description: string;
  required: boolean;
  default?: string;
  choices?: string[];               // for choice type
}
```

### `patch_skill` Tool Schema

For incremental edits without regenerating the whole skill:

```typescript
interface PatchSkillInput {
  operations: PatchOperation[];
}

type PatchOperation =
  | { op: "update_field"; field: string; value: any }           // update any top-level field
  | { op: "add_trigger"; trigger: string }                      // add a trigger phrase
  | { op: "remove_trigger"; trigger: string }                   // remove a trigger phrase
  | { op: "add_variable"; variable: SkillVariable }             // add an input variable
  | { op: "remove_variable"; name: string }                     // remove a variable
  | { op: "update_variable"; name: string; updates: Partial<SkillVariable> }
  | { op: "add_step"; step: SkillStep; after?: string }         // add a step (optionally after another)
  | { op: "remove_step"; id: string }                           // remove a step
  | { op: "update_step"; id: string; updates: Partial<SkillStep> }
  | { op: "add_reference"; reference: SkillReference }
  | { op: "remove_reference"; filename: string }
  | { op: "update_prompt"; systemPrompt: string };              // rewrite the main prompt
```

### WhatsApp/Telegram Preview Format

When the Copilot Agent generates a skill, it's rendered as a chat message (replaces Refly's ReactFlow canvas):

```
📋 *New Skill: LinkedIn → Cold Email*

_Researches a company on LinkedIn, identifies decision makers,
and drafts a personalized cold outreach email._

*Triggers:* "research and email", "outreach to [company]"

*Inputs:*
  • `company_name` (required) — Target company name
  • `tone` (optional) — casual | formal | friendly [default: friendly]
  • `product_angle` (optional) — Which product benefit to emphasize

*Steps:*
  1️⃣ Research company LinkedIn → web-search, linkedin-scraper
  2️⃣ Find decision makers → linkedin-scraper
  3️⃣ Draft personalized email → llm (depends on 1, 2)

*Model:* gemini-2.5-flash (escalates to kimi-k2 on failure)

*References:*
  • `cold-email-templates.md` — proven email frameworks

✅ Approve   ✏️ Edit   ❌ Cancel
```

User taps **Approve** → SKILL.md gets written to `.claude/skills/{name}/SKILL.md` and reference files are created alongside it.

User taps **Edit** → Copilot enters edit mode: "What would you like to change?"

### Authoring Session Persistence

Multi-turn skill authoring sessions need to survive disconnects (WhatsApp drops, Telegram timeouts). Store in-progress drafts:

```sql
CREATE TABLE skill_drafts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  skill_name TEXT,
  status TEXT DEFAULT 'drafting',  -- drafting | preview | approved | cancelled
  current_plan JSONB NOT NULL,     -- the GenerateSkillInput as JSON
  conversation_history JSONB,      -- messages in this authoring session
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
```

### Compilation: SKILL.md Generation

When approved, the structured JSON gets compiled to the actual SKILL.md file:

```typescript
function compileSkillMd(plan: GenerateSkillInput): string {
  const frontmatter = [
    '---',
    `name: ${plan.name}`,
    `description: ${plan.description}`,
    `triggers:`,
    ...plan.triggers.map(t => `  - "${t}"`),
    plan.model ? `model: ${plan.model}` : null,
    plan.tools?.length ? `tools:\n${plan.tools.map(t => `  - ${t}`).join('\n')}` : null,
    plan.variables?.length ? `variables:` : null,
    ...(plan.variables || []).map(v =>
      `  ${v.name}:\n    type: ${v.type}\n    description: "${v.description}"\n    required: ${v.required}`
    ),
    '---',
  ].filter(Boolean).join('\n');

  const body = plan.systemPrompt;

  return `${frontmatter}\n\n${body}`;
}
```

Reference files are written to the same skill directory:

```
.claude/skills/{skill-name}/
  SKILL.md              ← generated from plan
  references/
    cold-email-templates.md   ← fetched or inline content
    industry-knowledge.md     ← optional domain context
```

### Integration with Existing Architecture

**Entry points (where Skill Copilot gets invoked):**
- WhatsApp: user says "create a skill" or "I want to automate X" → routes to Skill Copilot agent
- Telegram: same trigger detection
- Dashboard (future): `/dashboard/skills/new` → web form that calls same backend
- CLI: `claude /1-skill-creator` → existing flow (for technical users)

**Execution pattern:** Basic skill — direct API call (no sandbox needed). The Skill Copilot is a lightweight conversational agent, not a code executor.

**Model routing:** Skill Copilot itself runs on Gemini 2.5 Flash (conversational, low-cost). The `generate_skill` tool output is structured JSON — doesn't need a frontier model. Escalate to Sonnet only if the user's description is highly complex or ambiguous.

### What We DON'T Take from Refly

| Refly Feature | Why We Skip It |
|---|---|
| ReactFlow canvas + drag-and-drop | Our users are on mobile chat, not desktop. **Voice is the correct replacement medium** (see note below). |
| NestJS + Prisma + PostgreSQL stack | Already have Supabase. One table (`skill_drafts`) vs their entire ORM. |
| BullMQ execution queues | Skills are authored conversationally, not queued. Execution uses our existing 3 patterns. |
| LangGraph skill engine | We have OpenAI Agents SDK. Skills execute through OpenClaw's native mechanism. |
| Elasticsearch full-text search | Supabase full-text search is enough for skill discovery. |
| YJS real-time collaboration | Single-user skill authoring. No collaboration needed. |
| Skill marketplace / registry | Git-based `.claude/skills/` directory. Share via repo, not a marketplace. |
| Credit/billing system | Not relevant — we're self-hosted. |

### Key Insight: Voice Is the Correct Medium (Not Visual, Not Text Chat)

> **The canvas is Refly's answer to "how do non-technical users author structured artifacts?" The correct answer for *our* users is an AI voice interviewer.**

Refly replaced code with a visual canvas. We need to go one step further and replace the canvas with **voice conversation**. The reasoning:

1. **Our users are non-technical and mobile-first.** They're on WhatsApp/Telegram, often on their phone. Typing structured requirements into a chat box is nearly as painful as writing YAML — it's just a different flavor of "staring at a blank page."

2. **Voice is the natural interface for requirements gathering.** A product manager doesn't fill out a form to describe a feature — they *talk through it*. Skill authoring is requirements gathering. The best requirements come from a guided interview, not a text prompt.

3. **The Copilot Agent pattern maps perfectly to a voice interviewer.** The behavior loop (understand → clarify → generate → present → iterate) is literally what a good interviewer does. The only difference is the transport: voice-to-text on input, text-to-voice on output.

**How this changes the architecture:**

```
Current Refly:    User types → Copilot reads → Canvas renders
Our text flow:    User types → Copilot reads → Chat preview renders
Our voice flow:   User speaks → STT → Copilot reads → TTS → User hears summary
                                                      → Text preview sent as confirmation
```

**The voice layer is thin — it wraps the same Skill Copilot agent:**
- **Input:** Whisper / Deepgram / Gemini STT transcribes voice messages → feeds into the same `generate_skill` / `patch_skill` pipeline
- **Output:** The Copilot's clarifying questions and preview summaries get spoken back via TTS (ElevenLabs / Chatterbox / Gemini TTS)
- **Confirmation:** The final skill preview is still sent as a formatted text message (the user needs to *see* the structure before approving — voice alone isn't enough for verification)

**Why this is better than a canvas for our users:**
- Zero learning curve — everyone knows how to answer questions out loud
- Works while driving, walking, or between meetings
- The AI interviewer *pulls structure out of rambling* — the user doesn't need to think in terms of "triggers" and "variables," the interviewer extracts those from natural speech
- Still produces the same SKILL.md artifact at the end

**Voice interviewer prompt additions (append to Skill Copilot system prompt):**

```markdown
## Voice Mode Adaptations
When the user is speaking (voice messages), adapt your behavior:
- Keep your questions SHORT — one question at a time, max 2 sentences
- Summarize back what you heard before moving on: "OK so you want X, and it should Y. Right?"
- Don't ask about implementation details (model, tools) — infer those from the description
- Focus on WHAT and WHEN, not HOW:
  - "What should this do?"
  - "When would you use this — what would you say to trigger it?"
  - "What information do you need to give it for it to work?"
  - "What should the output look like?"
- After 3-4 questions, generate the skill and read back a SHORT summary
- Send the full text preview as a follow-up message for visual confirmation
```

**Build implication:** Voice support slots into Week 3-4 of the build order. The Skill Copilot agent is the same — we just add STT on input and TTS on output. The `skill_drafts` table already stores conversation history, so voice sessions persist the same way.

### Build Order

1. **Week 1: Skill Copilot system prompt + `generate_skill` tool** — test in Claude Code first (cheapest iteration loop). Validate that natural language → SKILL.md generation works reliably.
2. **Week 2: `patch_skill` tool + multi-turn editing** — handle "change the triggers" / "add a variable" / "rewrite step 3" without regenerating.
3. **Week 3: WhatsApp/Telegram integration** — wire Skill Copilot as a route in the agent conversation handler. Add preview formatting + approve/edit/cancel buttons. Add `skill_drafts` table for session persistence.
4. **Week 4: Reference file handling** — auto-fetch URLs, create reference files alongside SKILL.md. Test end-to-end: user describes skill on WhatsApp → skill appears in `.claude/skills/` → skill is usable.
5. **Future: Dashboard UI** — web form at `/dashboard/skills/new` for users who prefer visual input. Calls the same `generate_skill` / `patch_skill` backend.

---

## 10. Execution Environments: Shell Sandbox vs Computer Use

**Core principle:** Two different tools for different jobs. Most tasks don't need a full graphical computer — they just need to crunch data or run a script. We always pick the lightest-weight environment that gets the job done.

| | Shell Sandbox | Computer Use |
|---|---|---|
| **What it is** | Lightweight Linux terminal (E2B) | Full remote computer with display |
| **Speed** | Fast (milliseconds) | Slower (renders UI, takes screenshots) |
| **Cost** | Cheap | 3-5x more expensive |
| **Best for** | Scripts, data processing, file ops, code execution | Websites requiring login, clicking buttons, visual tasks |
| **Access** | CLI tools only | Browser, desktop apps, anything with a GUI |

**Why separate environments?** Efficiency. Spinning up a whole virtual machine with a display just to run `python analyze.py` is overkill.

**Mental model:**
- Shell sandbox = quick calculator on your desk
- Computer Use = driving to a fully-equipped office

**Routing rule:** Default to shell sandbox. Only provision Computer Use when the task requires a browser with login state, visual interaction (clicking, scrolling), or desktop GUI applications. Examples:
- SVG/PDF generation with Python → **Shell sandbox**
- Scraping a public API → **Shell sandbox**
- Logging into Figma to edit a design → **Computer Use**
- Filling out a web form that requires session auth → **Computer Use**
- Running data analysis or file transformations → **Shell sandbox**

**Implementation note:** This maps to our existing architecture — E2B sandbox (shell) is the default execution environment for all three execution patterns (cron, workflows, platform tasks). Computer Use is a separate, on-demand capability provisioned only when explicitly needed.

---

## Summary: Merge Plan

| Section | Merge into | Location in ARCHITECTURE-v2 |
|---------|-----------|---------------------------|
| Context Compaction | Flow 2 (User conversation) | After "Store interaction" step, add compaction logic |
| Semantic Memory | Memory Architecture section | Expand with pgvector schema + migration path |
| Self-Scheduling | Tools section + Supabase schema | New tool `manage_recurring_task` + new table |
| Recurring Tasks UI | Frontend Architecture section | New dashboard route + 4-step wizard UI |
| **Mission Control** | **Component 3: Dashboard** | **Replace passive dashboard with real-time Mission Control** |
| Session Boundaries | New subsection after "Data Flows" | "Session Management & Context Boundaries" |
| Sub-Agent Spawning | Open Questions → Future Features | Move from open question to designed pattern |
| **Browser Automation** | **Open Questions → Future Features** | **TinyFish primary (NL→data) + Browserbase fallback (Playwright auth flows). Replaces DIY Playwright approach.** |
| **AI Scratch Pad** | **Component 3: Dashboard + WhatsApp** | **New capture flow — thin UI, AI inference, user signal confirmation** |
| **Agent Filesystem** | **New: Data Architecture** | **Per-client virtual filesystem — `client_files` table, folder tree, auto-filing** |
| **Skill Generation** | **New: Skill Authoring** | **Copilot Agent pattern from Refly — NL → SKILL.md via chat. `skill_drafts` table, WhatsApp/Telegram preview + approve flow** |

### New Supabase tables (add to schema)

1. `conversation_summaries` — compacted conversation history
2. `recurring_tasks` — agent-created recurring reminders (supports both AI tool + human UI)
3. `ai_status` — real-time AI state for dashboard (or columns on `clients` table)
4. `notifications` — agent notifications (approvals, overdue tasks, AI suggestions)
5. `task_comments` — comment threads on tasks (agent + AI collaborate)
6. `morning_briefings` — persisted daily briefings (structured JSON + rendered markdown)
7. `client_files` — per-client virtual filesystem (folder tree, documents, artifacts)
8. `skill_drafts` — in-progress skill authoring sessions (Copilot multi-turn state)

### New tools (add to Tools section)

1. `recall_memory` — semantic/keyword search on ai_memory
2. `manage_recurring_task` — create/update/cancel recurring tasks (AI-initiated)
3. `parallel_research` — spawn parallel sub-tasks (post-MVP)
4. `browse_web` — TinyFish natural language web operations (primary)
5. `browse_web_advanced` — Browserbase Playwright sessions for complex auth flows (fallback)
5. `save_file` / `read_file` / `list_folder` / `search_files` — virtual filesystem CRUD
6. `generate_skill` / `patch_skill` / `get_skill_summary` — Skill Copilot tools (NL → SKILL.md authoring)

### Updated tools

1. `update_memory` — add embedding generation on write (when pgvector enabled)

### New frontend routes (add to Dashboard)

**Recurring Tasks:**
1. `/dashboard/recurring-tasks` — List view of all recurring tasks
2. `/dashboard/recurring-tasks/new` — 4-step Cron Job Composer wizard
3. `/dashboard/recurring-tasks/[id]` — Edit/manage existing task

**Mission Control (replaces basic dashboard):**
4. `/dashboard` — Home: AI Status + Activity Feed + Quick Actions
5. `/dashboard/tasks` — Kanban Task Board (upgraded from flat list)
6. `/dashboard/tasks/[id]` — Task detail with comment thread
7. `/dashboard/feed` — Full filterable Activity Feed
8. `/dashboard/briefing` — Today's Morning Briefing
9. `/dashboard/briefing/[date]` — Historical briefings
10. `/dashboard/chat` — AI Chat interface (post-MVP, uses `useChat()`)
11. `/dashboard/approvals` — Pending Tier 3 approvals
12. `/dashboard/scratchpad` — AI Scratch Pad capture + history
13. `/dashboard/files` — File browser (virtual filesystem)
14. `/dashboard/files/[...path]` — Folder/file detail view

**Skill Authoring:**
15. `/dashboard/skills` — List all skills (installed + custom)
16. `/dashboard/skills/new` — Skill Copilot web form (calls same `generate_skill` backend)
17. `/dashboard/skills/[name]` — View/edit existing skill

### New API routes

**Recurring Tasks:**
1. `GET /api/recurring-tasks` — Fetch all recurring tasks for client
2. `POST /api/recurring-tasks` — Create new recurring task (from UI)
3. `PATCH /api/recurring-tasks/[id]` — Update schedule/status
4. `DELETE /api/recurring-tasks/[id]` — Cancel recurring task

**Mission Control:**
5. `GET /api/activity-feed` — Unified activity feed (or use Supabase view directly)
6. `GET /api/notifications` — Fetch unread notifications
7. `PATCH /api/notifications/[id]` — Mark notification read
8. `POST /api/tasks/[id]/comments` — Post comment on task thread
9. `GET /api/tasks/[id]/comments` — Fetch task comment thread
10. `GET /api/briefing/[date]` — Fetch morning briefing for date
11. `POST /api/chat` — Dashboard chat endpoint (triggers agent-conversation task)

**AI Scratch Pad:**
12. `POST /api/scratchpad` — Submit URL + notes, returns AI summary + category suggestions
13. `POST /api/scratchpad/confirm` — User confirms category, files the capture
14. `GET /api/scratchpad` — Fetch capture history

**Agent Filesystem:**
15. `GET /api/files?path=` — List folder contents
16. `GET /api/files/content?path=` — Read file content
17. `POST /api/files` — Create file/folder
18. `DELETE /api/files?path=` — Delete file/folder
19. `GET /api/files/search?q=` — Search across files

### New SOUL.md (separate file)

Created at `01_Projects/RE-AI-CRM/SOUL.md` — defines Layer 1 + Layer 2 of the system prompt (personality + domain knowledge). Ready for implementation as the `system` parameter in `generateText` calls.

---

## Self-Hosted OSS Infrastructure Layer

**Core insight:** The product is the agent. Everything else is infrastructure the user never sees. Instead of integrating with third-party SaaS (where each user needs their own account), we self-host OSS platforms and the agent calls them directly. Users interact with the agent via WhatsApp — they never know Cal.com or Formbricks or any of these exist.

**Why this is powerful:**
- **Zero onboarding friction** — no "create your Cal.com account", no "connect your Tally". The agent just works.
- **Auth is ours** — we manage all API keys, all accounts. One auth layer in Supabase, not N scattered SaaS logins.
- **Can't churn the infrastructure** — if we own their scheduling, their forms, their documents, their email... they're locked into the ecosystem. The switching cost isn't "cancel a subscription" — it's "rebuild your entire business workflow."
- **Cost control** — self-hosted = no per-seat SaaS fees. Host on a single VPS, scale when needed.
- **Data ownership** — everything stays in our infra. No third-party data processing concerns.

### Architecture pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    USER (WhatsApp)                           │
│         "Schedule a viewing for the Riveria unit"           │
│         "Send Sarah a feedback form after the viewing"      │
│         "Send the LOI for signing"                          │
│         "Email market update to all D10 buyers"             │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    AI AGENT                                  │
│              (the product layer)                             │
│                                                              │
│   MCP tools:                                                │
│   ├── create_booking_link()   → Cal.com                     │
│   ├── create_feedback_form()  → Formbricks                  │
│   ├── send_for_signing()      → DocuSeal                    │
│   ├── send_campaign()         → Listmonk                    │
│   ├── create_short_link()     → Shlink                      │
│   ├── generate_pdf()          → Gotenberg                   │
│   ├── publish_brief()         → Outline                     │
│   ├── update_crm()            → Twenty / Supabase           │
│   └── send_whatsapp()         → Baileys gateway             │
└──────────────────────┬──────────────────────────────────────┘
                       │
    ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
    ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
  Cal.com Formbr DocuSeal Listmnk Shlink Gotenb Outline Twenty Supa
  (sched) (forms) (esign) (email) (links) (pdf)  (wiki) (crm) (data)
    └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
                       │
              All Docker Compose on single VPS
              (Hetzner / sprites.dev)
```

**Key: the user never creates an account on any of these platforms.** We provision everything server-side. The agent is the only interface.

---

### OSS Platform Registry

Every platform below is self-hostable via Docker, has a REST API the agent can call, and replaces a SaaS subscription the user would otherwise need.

---

#### 1. Cal.com — Scheduling

| | |
|---|---|
| **Replaces** | Calendly, Acuity, Doodle |
| **Repo** | https://github.com/calcom/cal.com |
| **License** | AGPLv3 |
| **Deploy** | Docker / Docker Compose / Vercel |
| **Auth** | Bearer token (`cal_` prefixed API key) or OAuth |
| **API docs** | https://cal.com/docs/api-reference/v2/introduction |
| **GitHub stars** | 40k+ |

**What the agent does with it:**
- Creates booking links on the fly for viewings, follow-ups, discovery calls
- Checks available slots and suggests times in WhatsApp chat
- Books directly when contact picks a time
- Receives webhooks: `BOOKING_CREATED`, `BOOKING_CANCELLED`, `BOOKING_RESCHEDULED`, `BOOKING_NO_SHOW`
- Auto-sends pre-meeting briefings and triggers post-meeting feedback forms

**Key endpoints:** `POST /v2/event-types`, `GET /v2/slots`, `POST /v2/bookings`, `POST /v2/event-types/:id/webhooks`

**MCP tools:** `create_booking_link`, `get_available_slots`, `book_meeting`

---

#### 2. Formbricks — Forms & Surveys

| | |
|---|---|
| **Replaces** | Typeform, Tally, Google Forms |
| **Repo** | https://github.com/formbricks/formbricks |
| **License** | AGPLv3 |
| **Deploy** | Docker / Docker Compose / Kubernetes (Helm) |
| **Auth** | API Key (Management API) |
| **API docs** | https://formbricks.com/docs/api-v2-reference/introduction |

**What the agent does with it:**
- Creates post-viewing feedback forms, NPS surveys, client satisfaction surveys
- Generates questions dynamically from deal/contact context
- Sends shareable form links via WhatsApp
- Receives webhook on submission → updates deal sentiment, contact notes, creates follow-up tasks

**MCP tools:** `create_feedback_form`

> Originally considered Tally.so, but Tally **cannot be self-hosted**. Formbricks is the #1 OSS alternative.

---

#### 3. DocuSeal — Document Signing

| | |
|---|---|
| **Replaces** | DocuSign, PandaDoc, HelloSign |
| **Repo** | https://github.com/docusealco/docuseal |
| **License** | AGPLv3 |
| **Deploy** | Docker |
| **Auth** | API Key |
| **API docs** | https://www.docuseal.com/docs/api |
| **Users** | 138,000+ businesses |

**What the agent does with it:**
- Sends LOIs, contracts, and agreements for e-signature via WhatsApp link
- Uploads PDF/DOCX templates, pre-fills fields from deal data (price, address, parties)
- Tracks signing status — who's signed, who hasn't
- Webhook on completion → updates deal stage to "LOI Signed" / "Contract Executed"
- Legally binding (ESIGN, UETA, eIDAS compliant)

**Why DocuSeal over Documenso:** DocuSeal has 138k+ users, battle-tested API, simpler setup. Documenso is younger and less production-proven.

**MCP tools:** `send_for_signing`, `check_signing_status`, `create_template`

**This is a money feature.** Closing deals without leaving WhatsApp.

---

#### 4. Listmonk — Email Campaigns & Newsletters

| | |
|---|---|
| **Replaces** | Mailchimp, ConvertKit, SendGrid Marketing |
| **Repo** | https://github.com/knadh/listmonk |
| **License** | AGPLv3 |
| **Deploy** | Docker (single Go binary + PostgreSQL) |
| **Auth** | API token |
| **API docs** | https://listmonk.app/docs/apis/apis/ |
| **GitHub stars** | 19k+ |

**What the agent does with it:**
- Manages segmented subscriber lists (buyers by district, sellers by property type, investors by budget range)
- Creates and sends campaigns: weekly market updates, new listing alerts, deal anniversaries
- Sends transactional emails: meeting confirmations, document receipts
- Supports not just email but **WhatsApp, SMS, and any medium** via Messenger webhook interfaces
- A/B testing, scheduled sending, campaign analytics

**Key endpoints:** `POST /api/campaigns`, `POST /api/subscribers`, `GET /api/campaigns/:id/stats`, `POST /api/tx` (transactional)

**MCP tools:** `send_campaign`, `add_subscriber`, `send_transactional_email`

**Why Listmonk over Mautic:** Listmonk is a single binary. Mautic is a full PHP application with 10x the complexity. For agent-driven email where the AI composes everything, Listmonk's simplicity is a feature.

---

#### 5. Shlink — Link Shortening & Click Tracking

| | |
|---|---|
| **Replaces** | Bitly, Dub.co, Short.io |
| **Repo** | https://github.com/shlinkio/shlink |
| **License** | MIT |
| **Deploy** | Docker |
| **Auth** | API Key |
| **API docs** | https://shlink.io/documentation/api-docs/ |
| **GitHub stars** | 4.7k |

**What the agent does with it:**
- Wraps every link it sends (booking pages, forms, listings) in a tracked short URL
- Monitors click analytics: who clicked, when, how many times, from where (geolocation)
- Detects intent signals: "Sarah clicked the Riveria listing 4x this week" → agent proactively follows up
- Custom slugs for branding: `links.sunder.sg/riveria-viewing`
- Multi-domain support — different short domains per client or campaign

**Key endpoints:** `POST /rest/v3/short-urls`, `GET /rest/v3/short-urls/:shortCode/visits`

**MCP tools:** `create_short_link`, `get_link_analytics`

**This is an intelligence feature.** Every link becomes a sensor. The agent knows what contacts are interested in before they say it.

---

#### 6. Gotenberg — PDF Generation & Conversion

| | |
|---|---|
| **Replaces** | Adobe PDF services, PDF.co, wkhtmltopdf |
| **Repo** | https://github.com/gotenberg/gotenberg |
| **License** | MIT |
| **Deploy** | Docker (`gotenberg/gotenberg:8`) |
| **Auth** | None (internal service, not exposed publicly) |
| **API docs** | https://gotenberg.dev/ |
| **Docker pulls** | 50M+, 11k+ GitHub stars |

**What the agent does with it:**
- Generates property fact sheets from HTML templates → PDF
- Converts proposals, market reports, and briefs from Markdown/HTML to polished PDFs
- Merges multiple documents (floor plan + fact sheet + pricing) into single PDF packages
- Converts Word/Excel/PowerPoint files clients send into PDFs
- Renders custom sales decks from templates with deal-specific data

**Key capabilities:** Chromium engine (HTML/URL → PDF), LibreOffice engine (DOCX/XLSX/PPTX → PDF), PDF merge, PDF/A conversion, S3 presigned URL support

**API style:** HTTP form-based routes (20+), called via simple POST requests

**MCP tools:** `generate_pdf`, `convert_document`, `merge_pdfs`

---

#### 7. Outline — Knowledge Base & Wiki

| | |
|---|---|
| **Replaces** | Notion (shared docs), Confluence, GitBook |
| **Repo** | https://github.com/outline/outline |
| **License** | BSL 1.1 (free for self-hosting) |
| **Deploy** | Docker (recommended) |
| **Auth** | API Key (Bearer token) |
| **API docs** | https://www.getoutline.com/developers |

**What the agent does with it:**
- Creates and maintains client-facing knowledge bases: "Your Property Search Brief" updated daily
- Publishes deal summaries, market reports, and meeting notes as clean, shareable docs
- Organizes internal team knowledge: playbooks, scripts, market intel
- Full API = the agent programmatically creates, updates, and organizes documents
- Collections + templates = consistent structure across all client portals
- 20+ integrations (Slack, Figma, etc.) for when Mission Control expands

**Key endpoints:** `POST /api/documents.create`, `POST /api/documents.update`, `POST /api/collections.create`, `POST /api/documents.search`

**MCP tools:** `publish_brief`, `update_client_portal`, `search_knowledge_base`

**Client portal play:** Each client gets a collection in Outline. Agent curates it — meeting summaries, shortlisted properties, market snapshots. Client sees a clean, branded wiki. No logins needed if shared via public link.

---

#### 8. Twenty — CRM

| | |
|---|---|
| **Replaces** | Salesforce, HubSpot, Pipedrive |
| **Repo** | https://github.com/twentyhq/twenty |
| **License** | AGPLv3 |
| **Deploy** | Docker / Docker Compose / AWS / GCP / Azure |
| **Auth** | Bearer token (API Key) |
| **API docs** | https://docs.twenty.com/developers/extend/capabilities/apis |
| **GitHub stars** | 25k+ |

**What the agent does with it:**
- Full CRM with people, companies, deals, notes, tasks — all via REST + GraphQL API
- Core API (CRM data) + Metadata API (custom fields, object definitions)
- Webhooks for real-time CRM events
- Could replace our raw Supabase tables as the CRM layer evolves — gives us a proper UI for when agents/admins need to manually inspect data
- Customizable: add RE-specific fields (property type, district, budget range) via Metadata API

**When to adopt:** Not day 1. Supabase tables + agent are sufficient initially. Twenty becomes relevant when we need a **visual CRM dashboard for human agents** to browse alongside the AI — or when a client wants to "see their pipeline" beyond what WhatsApp shows.

**Key endpoints:** `POST /rest/people`, `POST /rest/companies`, `PATCH /rest/opportunities/:id`, `GET /rest/tasks`

**MCP tools:** `update_contact`, `update_deal`, `create_task`, `search_crm`

---

#### 9. Supabase — Data Layer (already in stack)

| | |
|---|---|
| **Replaces** | Firebase, custom backend |
| **Repo** | https://github.com/supabase/supabase |
| **License** | Apache 2.0 |
| **Deploy** | Docker / self-hosted / cloud |

Already the backbone. Auth, Realtime subscriptions, PostgreSQL, RLS, Edge Functions. Everything else connects back to Supabase as the source of truth.

---

### Hosting strategy

All platforms run as Docker containers on the same infra:

```yaml
# docker-compose.yml (simplified)
services:
  calcom:
    image: calcom/cal.com
    ports: ["3001:3000"]

  formbricks:
    image: formbricks/formbricks
    ports: ["3002:3000"]

  docuseal:
    image: docuseal/docuseal
    ports: ["3003:3000"]

  listmonk:
    image: listmonk/listmonk
    ports: ["3004:9000"]

  shlink:
    image: shlinkio/shlink
    ports: ["3005:8080"]

  gotenberg:
    image: gotenberg/gotenberg:8
    ports: ["3006:3000"]

  outline:
    image: outlinewiki/outline
    ports: ["3007:3000"]

  twenty:
    image: twentycrm/twenty
    ports: ["3008:3000"]

  supabase:
    # already in our stack

  caddy:
    image: caddy:2
    ports: ["80:80", "443:443"]
    # Reverse proxy — routes *.sunder.sg subdomains to each service
    # cal.sunder.sg → calcom, forms.sunder.sg → formbricks, etc.
```

**Cost estimate:** Hetzner CX41 (~$20/mo) or dedicated AX42 (~$45/mo) handles all 9 platforms for dozens of users. Each platform is lightweight individually — the bottleneck is PostgreSQL, which they can share.

---

### Future expansion candidates

| Capability | OSS Platform | Replaces | Notes |
|-----------|-------------|----------|-------|
| Analytics | **Plausible** | Google Analytics | Track booking page / form conversion rates |
| Notifications | **Novu** / **Apprise** | OneSignal, Courier | Unified notification layer across WhatsApp/email/SMS/push |
| File storage | **MinIO** | S3 / Dropbox | S3-compatible object storage for property photos, contracts |
| Live chat | **Chatwoot** | Intercom | If we add a web widget alongside WhatsApp |
| Invoicing | **Invoice Ninja** | QuickBooks | Agent generates invoices for commission tracking |
| Automation | **n8n** | Zapier | Alternative to Trigger.dev for some workflows |
| Social media | **Postiz** | Buffer, Hootsuite | Agent manages listing posts across platforms |

---

**The play:** Every piece of software the user would normally buy a subscription for, we self-host and the agent manages. The user's "SaaS stack" is just... talking to an agent on WhatsApp.

---

## Architecture Decision: Built-in CRM

**Status:** Decided
**Date:** February 16, 2026

### Context

The product promises "Built-in CRM — every lead, every deal, tracked. Ready from day one." The user never creates a CRM account or configures anything. The agent manages their CRM via WhatsApp; the dashboard is an "occasionally glance" layer.

We evaluated three approaches:
- **(A) Centralized Supabase + custom Mission Control UI** — one database, all clients, RLS isolation, lightweight custom CRM screens
- **(B) Twenty CRM per container** — self-host Twenty in each client's sprites.dev sandbox, use its built-in UI
- **(C) Local Postgres per container + custom UI** — each client gets their own database and CRM app in their sandbox

### Decision: Approach A — Centralized Supabase + Mission Control

**Rationale:**
1. **Business control** — all data in one place, one backup, one monitoring endpoint
2. **Lean containers** — sprites.dev containers run the agent + skills only, no Postgres, no web server. Cheaper, faster boot.
3. **One deployment** — Mission Control is one Next.js app on Vercel serving all clients, not N deployments
4. **Supabase gives us Auth, Realtime, RLS for free** — activity feed, live pipeline updates, login, tenant isolation are already built
5. **Cross-client analytics trivial** — one `SELECT` to see all deals, revenue, health across the platform
6. **Schema customization is a config problem, not an infrastructure problem** — JSONB custom fields + `crm_config` table, not separate databases

**Why not B (Twenty per container):**
- ~1-2GB RAM per container for Twenty + Postgres = real compute cost at scale
- Twenty is a full CRM product — massive overkill for "occasionally glance" dashboard usage
- Dependency on Twenty's roadmap, update cycle, breaking changes
- No centralized data visibility without building a sync layer

**Why not C (local Postgres per container):**
- Scattered data across N containers — backups, monitoring, analytics all harder
- Need to roll our own websockets (no Supabase Realtime)
- Need to roll our own auth (no Supabase Auth)
- Container disk bloat for marginal benefit
- Network latency concern is irrelevant — 50ms DB call vs 2-3s LLM inference

### Architecture

```
Client A's sprites container     Client B's sprites container
  └── Agent + Skills               └── Agent + Skills
        │                                │
        └────────────┬───────────────────┘
                     ▼
           Centralized Supabase
           ├── contacts, deals, tasks (RLS by client_id)
           ├── crm_config (per-client schema definitions)
           ├── interactions (conversation history)
           ├── Realtime (live updates to Mission Control)
           └── Auth (Mission Control login)
                     │
                     ▼
           Mission Control (Next.js on Vercel)
           └── Dynamic CRM views (reads crm_config to render per-client fields)
```

### Per-client schema customization

Every client gets the same base tables. Customization lives in two places: a `crm_config` table (defines what fields and stages exist) and JSONB columns on the data tables (stores the values).

#### `crm_config` table

```sql
CREATE TABLE crm_config (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id) UNIQUE,

  -- Deal pipeline config
  deal_stages JSONB NOT NULL DEFAULT '[
    {"key": "inquiry", "label": "Inquiry", "color": "#3B82F6"},
    {"key": "viewing", "label": "Viewing", "color": "#F59E0B"},
    {"key": "offer", "label": "Offer", "color": "#8B5CF6"},
    {"key": "negotiation", "label": "Negotiation", "color": "#EC4899"},
    {"key": "closed_won", "label": "Closed Won", "color": "#10B981"},
    {"key": "closed_lost", "label": "Closed Lost", "color": "#EF4444"}
  ]',

  -- Custom field definitions per entity
  contact_fields JSONB NOT NULL DEFAULT '[
    {"key": "source", "label": "Source", "type": "select", "options": ["WhatsApp", "Referral", "Walk-in", "Online"]},
    {"key": "budget", "label": "Budget", "type": "currency"},
    {"key": "notes", "label": "Notes", "type": "text"}
  ]',

  deal_fields JSONB NOT NULL DEFAULT '[
    {"key": "property_address", "label": "Property", "type": "text"},
    {"key": "district", "label": "District", "type": "select", "options": ["D1","D2","D9","D10","D11","D15"]},
    {"key": "psf_price", "label": "PSF Price", "type": "currency"},
    {"key": "tenure", "label": "Tenure", "type": "select", "options": ["Freehold","99-year","999-year"]}
  ]',

  -- UI preferences
  pipeline_view JSONB DEFAULT '{"default_view": "kanban", "visible_stages": "all"}',

  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- RLS
ALTER TABLE crm_config ENABLE ROW LEVEL SECURITY;
CREATE POLICY "client_isolation" ON crm_config
  FOR ALL USING (client_id = current_setting('app.client_id'));
```

#### Data tables (universal, with JSONB custom fields)

```sql
-- Contacts — universal across all verticals
CREATE TABLE contacts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),

  -- Universal fields (every client has these)
  name TEXT NOT NULL,
  phone TEXT,
  email TEXT,
  company TEXT,
  tags TEXT[] DEFAULT '{}',

  -- Per-client custom fields (defined by crm_config.contact_fields)
  custom_fields JSONB DEFAULT '{}',
  -- e.g. {"source": "WhatsApp", "budget": 1500000, "notes": "Looking in D10"}

  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Deals — universal pipeline with custom fields
CREATE TABLE deals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),
  contact_id UUID REFERENCES contacts(id),

  -- Universal fields
  title TEXT NOT NULL,
  stage TEXT NOT NULL DEFAULT 'inquiry',  -- maps to crm_config.deal_stages[].key
  value NUMERIC,
  currency TEXT DEFAULT 'SGD',

  -- Per-client custom fields (defined by crm_config.deal_fields)
  custom_fields JSONB DEFAULT '{}',
  -- e.g. {"property_address": "Riveria #12-08", "district": "D10", "psf_price": 2100}

  closed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Activities — unified timeline for any entity
CREATE TABLE activities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id TEXT NOT NULL REFERENCES clients(id),

  -- Polymorphic: can be linked to contact, deal, or both
  contact_id UUID REFERENCES contacts(id),
  deal_id UUID REFERENCES deals(id),

  type TEXT NOT NULL,  -- 'note', 'call', 'meeting', 'whatsapp', 'email', 'stage_change', 'task_created', 'form_submitted'
  content TEXT,        -- human-readable description
  metadata JSONB,      -- structured data (e.g. old_stage, new_stage for stage_change)

  -- Who did this
  actor TEXT NOT NULL DEFAULT 'agent',  -- 'agent', 'user', 'system', 'contact'

  created_at TIMESTAMPTZ DEFAULT now()
);

-- RLS on all tables
ALTER TABLE contacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE deals ENABLE ROW LEVEL SECURITY;
ALTER TABLE activities ENABLE ROW LEVEL SECURITY;

CREATE POLICY "client_isolation" ON contacts FOR ALL USING (client_id = current_setting('app.client_id'));
CREATE POLICY "client_isolation" ON deals FOR ALL USING (client_id = current_setting('app.client_id'));
CREATE POLICY "client_isolation" ON activities FOR ALL USING (client_id = current_setting('app.client_id'));
```

### How skills interact with the CRM

The agent's skills read `crm_config` to understand the client's CRM structure, then write to the universal tables.

```typescript
// Inside a skill: "Extract contact from WhatsApp message"
const config = await supabase
  .from('crm_config')
  .select('contact_fields, deal_stages')
  .eq('client_id', clientId)
  .single();

// Agent knows what fields are valid for this client
// Generates structured data matching the config
const contact = await supabase
  .from('contacts')
  .insert({
    client_id: clientId,
    name: 'Sarah Lee',
    phone: '+6591234567',
    custom_fields: {
      source: 'WhatsApp',        // field defined in crm_config
      budget: 1500000,
      notes: 'Looking for 3BR in D10, freehold preferred'
    }
  });
```

```typescript
// skill: crm-setup (runs once during client onboarding)
// Agent calls this to configure the CRM for a new client

const defaultREConfig = {
  deal_stages: [
    { key: 'inquiry', label: 'Inquiry', color: '#3B82F6' },
    { key: 'viewing', label: 'Viewing', color: '#F59E0B' },
    { key: 'offer', label: 'Offer', color: '#8B5CF6' },
    { key: 'negotiation', label: 'Negotiation', color: '#EC4899' },
    { key: 'closed_won', label: 'Closed Won', color: '#10B981' },
    { key: 'closed_lost', label: 'Closed Lost', color: '#EF4444' },
  ],
  contact_fields: [
    { key: 'source', label: 'Source', type: 'select', options: ['WhatsApp', 'Referral', 'Walk-in', 'Online'] },
    { key: 'budget', label: 'Budget', type: 'currency' },
    { key: 'buyer_type', label: 'Buyer Type', type: 'select', options: ['First-time', 'Upgrader', 'Investor', 'Downsizer'] },
  ],
  deal_fields: [
    { key: 'property_address', label: 'Property', type: 'text' },
    { key: 'district', label: 'District', type: 'select', options: ['D1','D2','D9','D10','D11','D15'] },
    { key: 'psf_price', label: 'PSF Price', type: 'currency' },
    { key: 'tenure', label: 'Tenure', type: 'select', options: ['Freehold', '99-year', '999-year'] },
  ],
};

// Agent can also modify this config conversationally:
// User: "Add a field for property type — condo, landed, HDB"
// Agent: updates crm_config.deal_fields, adds { key: 'property_type', ... }
```

### Mission Control screens (5 total)

Built with Refine + shadcn/ui on top of Supabase. One Next.js app, deployed once on Vercel, serves all clients.

```
┌─────────────────────────────────────────────────────────────┐
│  MISSION CONTROL                                            │
│                                                              │
│  ┌─────────┐ ┌──────────┐ ┌────────┐ ┌──────┐ ┌──────────┐│
│  │Pipeline │ │ Contacts │ │ Detail │ │ Feed │ │   Chat   ││
│  │ (kanban)│ │  (table) │ │ (view) │ │      │ │          ││
│  └─────────┘ └──────────┘ └────────┘ └──────┘ └──────────┘│
│                                                              │
│  All views read crm_config to know which fields/stages      │
│  to render. Same codebase, different UI per client.         │
└─────────────────────────────────────────────────────────────┘
```

1. **Pipeline** — Kanban board. Columns from `crm_config.deal_stages`. Cards show deal title + value + contact name. Drag to change stage.
2. **Contacts** — Table with search, sort, filter. Columns from universal fields + `crm_config.contact_fields`. Click to open detail.
3. **Deal/Contact detail** — Fields rendered dynamically from `crm_config`. Activity timeline below (from `activities` table). Conversation history from `interactions` table.
4. **Activity feed** — Real-time stream via Supabase Realtime. Everything the agent did. Filterable by type.
5. **Chat** — Talk to the agent from the dashboard (same agent, different channel alongside WhatsApp).

### Key design principles

1. **The agent is the primary interface.** Mission Control is secondary. If a feature can be done via WhatsApp chat, it doesn't need a dedicated UI screen.
2. **Dynamic, not hardcoded.** Every field, stage, and view reads from `crm_config`. No code changes needed to customize a client's CRM — just update the config (agent does this via skills).
3. **Activities are the source of truth.** Every action (agent or human) creates an activity. The timeline is the audit log. No separate audit system needed.
4. **JSONB over schema changes.** Custom fields live in JSONB columns. This trades query performance (can't index individual custom fields as easily) for flexibility (no migrations when a client adds a field). For the volume of data per client (hundreds of contacts, not millions), this is the right tradeoff.
5. **Skills define the schema, not the infrastructure.** The `crm-setup` skill knows what an RE agent's CRM should look like. A future `crm-setup-insurance` skill knows what an insurance broker needs. Same tables, different config.
