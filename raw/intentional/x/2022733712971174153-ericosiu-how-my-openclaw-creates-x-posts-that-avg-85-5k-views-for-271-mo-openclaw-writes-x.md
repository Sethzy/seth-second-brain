---
type: raw_capture
source_type: x
url: https://x.com/ericosiu/status/2022733712971174153
original_url: https://x.com/ericosiu/status/2022733712971174153
author: "ericosiu"
handle: ericosiu
status_id: 2022733712971174153
captured_at: 2026-06-19T20:45:16+08:00
published_at: "Sat Feb 14 18:04:32 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 25
  reposts: 39
  likes: 547
---

# X post by @ericosiu

## Source

- Original: [https://x.com/ericosiu/status/2022733712971174153](https://x.com/ericosiu/status/2022733712971174153)
- Canonical: [https://x.com/ericosiu/status/2022733712971174153](https://x.com/ericosiu/status/2022733712971174153)
- Author: ericosiu (@ericosiu)

## Verbatim Text

How My OpenClaw Creates X Posts That Avg 85.5k Views

For $271/mo, OpenClaw writes X articles that generate 85,547 views per post OpenClaw while replacing $15,000/mo in business/marketing costs.

Everyone's talking about 'AI agents'. Nobody shows the receipts.

Here are mine.

This article was largely written by the system it describes.

I told my AI assistant: "Write a comprehensive X article based on the coolest thing we accomplished this week." It gave me a few angles and then pulled a skill that matches my writing voice from a style guide it built by studying my previous posts. Drafted it. Sent it to my Telegram as 3 messages with approve/edit buttons.

I made minor edits to the hook, and Nano Banana made the thumbnail.

That's not the impressive part. The impressive part is that while it was writing this article, the same system was simultaneously:

• Replacing annoying 'chores' that our client services team has to do

• Scanning my CRM for deals that sales can revive

• Preparing recruiting candidates for review (with outreach angles)

The article was a side task. One of dozens.

I run an AI-native marketing agency called @singlegrain. I built these 4 agents that wake up before I do. They scan my pipeline, analyze my SEO/AEO, score content angles, and source candidates.

By 8 AM, I have a Telegram full of decisions. I tap buttons. Approve. Reject. Next.

Here's what runs every morning:

```
5 AM  ─ Quote Mining
6 AM  ─ Content Angles
7 AM  ─ SEO Actions
7:30  ─ Strategic Brief
8 AM  ─ Deal of the Day
8:45  ─ Agent Roundtable
9 AM  ─ Recruiting Drop
10:30 ─ Product Pulse
11 AM ─ Connection of Day
```

34 cron jobs. 71 scripts. Zero humans involved until I open my phone.

The cost breakdown surprised me.

```
Weekly Cost:
Infra       ████████████ $37
SEO Agent   ████         $5
Content     ████         $5
Deals       ███          $4
Recruiting  ███          $3
Other       ████████     $9
            ─────────────────
Total       $63/week ($271/mo)
```

60% of my spend goes to infrastructure. Not the agents doing real work. The memory systems, the context injection, the anti-amnesia layer.

Nobody tells you that part.

The agents aren't one system. They're four specialists with a shared brain.

```
┌────────┐  ┌────────┐
│ Oracle │  │ Flash  │
│  SEO   │  │Content │
└───┬────┘  └───┬────┘
    │           │
    ▼           ▼
┌──────────────────┐
│   Shared Brain   │
│ priorities, KPIs │
│ feedback, signals│
└──────────────────┘
    ▲           ▲
    │           │
┌───┴────┐  ┌───┴────┐
│ Alfred │  │ Cyborg │
│Strategy│  │Recruit │
└────────┘  └────────┘
```

Oracle finds a keyword gap. Flash sees it and suggests content for that exact topic. I reject a deal. All four agents learn — nobody resurfaces it.

Before the shared brain, they were repeating each other. Contradicting each other. Wasting my time with the same recommendation from three different agents.

One symlinked directory fixed 80% of that.

Here's what broke. Because it always breaks.

My content agent didn't fire a single job for 48 hours. No error. No warning. Just silence. Had to rebuild the delivery pipeline from scratch.

Caught an agent claiming it "successfully analyzed" data that didn't exist yet. It fabricated a report. Confidently. With numbers.

Fix: every agent runs the script first, reads the output file, then reports. Trust nothing.

Deal of the Day kept showing the same prospect. Three days in a row. Same person. Same pitch.

Fix: dedup checks against 14 days of outputs and all feedback history.

The worst one. Three infrastructure crons were burning $37 a week on the most expensive model. They were running simple Python scripts. Didn't need the big model at all.

```
Before optimization:
Memory    ████████ $11/wk (Opus)
Compactor ████████ $11/wk (Opus)
Vector    ████████ $14/wk (Opus)

After:
Memory    ██       $2/wk (Sonnet)
Compactor ██       $2/wk (Sonnet)
Vector    ███      $3/wk (Sonnet)

Saved: $30/week
```

Nobody audits their agent costs. I didn't for two weeks. It adds up.

The system that watches the system.

Agents break. Crons fail silently. Costs drift. So I built agents that monitor agents.

```
Monthly:
┌────────────────┐
│ Elon Algorithm │
│ Question.      │
│ Delete.        │
│ Simplify.      │
└───────┬────────┘
        ▼
Weekly:
┌────────────────┐
│ Self-Healing   │
│ Auto-fix fails │
│ Bump timeouts  │
│ Force retries  │
└───────┬────────┘
        ▼
Weekly:
┌────────────────┐
│ System Janitor │
│ Prune files    │
│ Track costs    │
│ Flag duplicates│
└────────────────┘
```

Every month: Question every system. Delete ruthlessly. Simplify what survives.

If an agent's recommendations go ignored for 3 weeks, it gets flagged for deletion. No sacred cows.

Everyone's excited about building agents. Nobody talks about maintaining them. After 2 weeks of 34 daily crons I had 84 data files, 53 agent outputs accumulating, and feedback logs that every agent reads on every run — burning tokens for no reason.

Garbage collection has to be as automated as the building. Or you drown in 90 days.

This morning I told my system to build six things at once. Attribution tracking. Client dashboard. Multi-tenancy. Cost modeling. Regression testing. Data moat analysis.

Six sub-agents. Running in parallel. All six finished in 8 minutes.

```
7:40 AM — spawned 6 agents
7:43 AM — cost model done
7:44 AM — data moat done
7:46 AM — attribution done
7:47 AM — dashboard done
7:47 AM — regression done
7:48 AM — multi-tenancy done
```

8 minutes. Six production systems. Each one would take a human team a week.

That's not a flex. That's the uncomfortable truth about where this is going.

The uncomfortable truth.

This system isn't smart. It's consistent.

It wakes up at 5 AM. It never skips the SEO audit because it's "too busy." It never forgets to check the pipeline. It never calls in sick.

$271 a month. Does the work of a $15,000/month team.

But it took two weeks of debugging to get here. Most of those two weeks were fixing things that broke, not building new things. Silent failures. Fabricated outputs. Cost bloat. Recommendation loops.

The real moat isn't the AI. It's the feedback loop. Every approval teaches. Every rejection teaches. The system compounds.

Two weeks in, my competitive moat score is 19 out of 100. Minimal. But it grows every day. In six months, a competitor would need months to replicate what I have. In a year, they can't catch up.

Most people will read this, think "cool," and go back to manually checking their dashboards.

The few who actually build it will wonder why they waited.

325K of you read my last 4 posts about this setup.

Worth it? You tell me.

For more like this, level up your AI + marketing with 14,000+ marketers and founders in my Leveling Up newsletter here for free: https://levelingup.beehiiv.com/subscribe

## X Article Metadata

- Title: How My OpenClaw Creates X Posts That Avg 85.5k Views
- Preview: For $271/mo, OpenClaw writes X articles that generate 85,547 views per post OpenClaw while replacing $15,000/mo in business/marketing costs.
Everyone's talking about 'AI agents'. Nobody shows the

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
