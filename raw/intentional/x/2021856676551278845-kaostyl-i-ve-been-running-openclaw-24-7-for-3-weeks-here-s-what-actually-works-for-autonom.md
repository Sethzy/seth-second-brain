---
type: raw_capture
source_type: x
url: https://x.com/kaostyl/status/2021856676551278845
original_url: https://x.com/kaostyl/status/2021856676551278845
author: "Kaostyl"
handle: kaostyl
status_id: 2021856676551278845
captured_at: 2026-06-19T20:18:22+08:00
published_at: "Thu Feb 12 07:59:30 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 59
  reposts: 95
  likes: 1348
---

# X post by @kaostyl

## Source

- Original: [https://x.com/kaostyl/status/2021856676551278845](https://x.com/kaostyl/status/2021856676551278845)
- Canonical: [https://x.com/kaostyl/status/2021856676551278845](https://x.com/kaostyl/status/2021856676551278845)
- Author: Kaostyl (@kaostyl)

## Verbatim Text

I've been running OpenClaw 24/7 for 3 weeks. Here's what actually works for autonomous agents (not theory — battle-tested patterns):

🧠 Memory architecture matters more than prompts

Don't dump everything in https://t.co/Be5Xdc9UsF. Split it:

• memory/active-tasks.md → your "save game" (crash recovery)
• memory/YYYY-MM-DD.md → daily raw logs
• memory/projects.md, https://t.co/htttxcZsvo, https://t.co/XlwgyR8GUs → thematic long-term
Why? Your agent wakes up fresh every session. These files ARE its brain. The split means it loads only what it needs.

⚡ Sub-agents are your 10x multiplier

Stop doing things sequentially. I spawn 3-5 sub-agents in parallel for any big task. Example: deploying 11 websites simultaneously — 4 agents, each handling a batch, all running at once.

The trick: define clear success criteria BEFORE spawning. Each agent must validate its own work, then YOU verify before announcing "done."

⏰ Cron > Heartbeats for specific tasks

Heartbeats are great for batching periodic checks (email + calendar + mentions in one turn).

But for precise schedules? Use cron jobs:

• Daily content ideas at 6am
• Overnight research scout at 2am
• Tech watch at 8am
Each runs in isolation with its own context. No token waste from loading the full conversation history.

🔄 The crash recovery pattern nobody talks about

Your agent WILL crash/restart. https://t.co/OrzLkm5r0r is the safety net:

• When you START a task → write it
• When you SPAWN a sub-agent → note session key
• When it COMPLETES → update
On restart, agent reads this file first and resumes autonomously. No "what were we doing?" — it figures it out.

🛡️ Security rule that saved me

Use your strongest model (Opus) for ANY task that reads external web content. Weaker models are more vulnerable to prompt injection from hostile websites.

Internal tasks (file reading, reminders, local work) → Sonnet is fine.
External content (tweets, articles, emails) → Opus only.

📝 https://t.co/snp6Guwnlv should be tiny

I see people stuffing 200 lines in their https://t.co/snp6Guwnlv. Bad idea — it runs every ~30min and burns tokens.

Keep it under 20 lines. Just a checklist:

• Check active tasks freshness
• Session health (archive bloated sessions)
• Self-review every ~4h
Heavy work goes in cron jobs, not heartbeats.

🎯 The real unlock: Skills with routing logic

If you have multiple skills, add "Use when / Don't use when" in each description. Without this, the agent misfires ~20% of the time picking the wrong skill.

Think of it as if/else logic for your agent's decision-making.

The bottleneck isn't AI capability anymore. It's YOUR speed reviewing what the agents produce. Build systems that close the loop automatically, and you'll 10x your output.

#openclaw #autonomous #ai

## Capture Note

TweetDetail returned complete normal-post text.
