---
type: raw_capture
source_type: x
url: https://x.com/cyrilXBT/status/2056186353029722587
original_url: https://x.com/cyrilxbt/status/2056186353029722587
author: "CyrilXBT"
handle: cyrilXBT
status_id: 2056186353029722587
captured_at: 2026-06-10T23:50:42+08:00
published_at: "Mon May 18 01:33:23 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 25
  reposts: 43
  likes: 260
---

# X post by @cyrilXBT

## Source

- Original: [https://x.com/cyrilxbt/status/2056186353029722587](https://x.com/cyrilxbt/status/2056186353029722587)
- Canonical: [https://x.com/cyrilXBT/status/2056186353029722587](https://x.com/cyrilXBT/status/2056186353029722587)
- Author: CyrilXBT (@cyrilXBT)

## Verbatim Text

How to Build a Claude Agent That Manages Your Entire Business While You Sleep

Most business owners spend their days reacting.

Emails pile up. Project statuses go stale. Client briefs need compiling. Reports need generating. Content needs drafting. Revenue needs tracking. Follow-ups get missed.

Not because they are disorganized.

Because they are the operational layer of their own business.

Every piece of information that moves from one place to another moves through them. Every status update requires their attention. Every recurring task waits for them to initiate it.

The business does not run without them in the loop.

This guide is about changing that equation permanently.

A Claude agent connected to your tools, configured with your business context, and running automated workflows via N8N does not wait for you to initiate anything.

It monitors. It processes. It acts. It reports.

While you sleep.

## The Mental Model Shift

Before the build, the concept.

Most people who try to automate their business build automations.

A Zap that sends an email when a form is submitted. A workflow that creates a task when a Slack message is pinged. Individual automations for individual triggers.

These are useful. They are not a business management agent.

The difference is intelligence and context.

An automation executes a fixed sequence when a trigger fires.

An agent reads the situation, applies business context, makes a judgment, and takes the appropriate action.

When a new lead comes in, an automation sends a templated email.

When a new lead comes in, an agent reads the lead's details, checks your CRM for any existing relationship, researches the company, drafts a personalized first message based on their specific situation, schedules it for the optimal send time, and creates a follow-up task for three days later.

Same trigger. Completely different output.

The agent does what a smart human employee would do.

The automation does what a dumb script does.

This guide builds the agent.

## The Architecture

Four components make a business management agent work.

Claude is the intelligence layer. It reads context, makes decisions, generates outputs, and determines what action to take in any given situation.

CLAUDE.md is the business context layer. It tells Claude everything about your business before any workflow runs. Your clients. Your standards. Your voice. Your rules. Your current priorities.

MCP Servers are the connection layer. They give Claude direct access to your actual business tools. Email. Calendar. CRM. Project management. Database. Communication tools.

N8N is the automation layer. It schedules workflows, fires triggers, passes data between systems, and makes the entire operation run without you initiating anything.

Together these four components create an agent that manages your business continuously rather than responding to your prompts on demand.

## Building the Business Context Layer

The CLAUDE.md file is the foundation everything else rests on.

Every workflow the agent runs reads this file first. It is the briefing document that turns generic Claude capability into business-specific intelligence.

A poorly written CLAUDE.md produces generic outputs that require significant editing.

A precisely written CLAUDE.md produces outputs that could have come from a senior employee who has worked with you for years.

# Business Management Agent — CLAUDE.md

## Business Identity
Name: [YOUR BUSINESS NAME]
What you do: [SPECIFIC ONE-SENTENCE DESCRIPTION]
Who you serve: [SPECIFIC CUSTOMER DESCRIPTION]
Revenue model: [HOW THE BUSINESS MAKES MONEY]
Stage: [EARLY / GROWTH / ESTABLISHED]
Monthly revenue: [CURRENT NUMBER — UPDATE MONTHLY]

## Active Clients
[CLIENT NAME]: [SERVICE TYPE] | Value: $[MRR] | 
Status: [CURRENT STATUS] | Next action: [SPECIFIC NEXT STEP]
[Repeat for every active client]

## Current Projects
[PROJECT NAME]: [DESCRIPTION] | Deadline: [DATE] | 
Status: [STATUS] | Blocker: [IF ANY]
[Repeat for every active project]

## Communication Standards
Email tone: [PROFESSIONAL / FRIENDLY / DIRECT]
Response time commitment: [YOUR STANDARD]
What you never say: [SPECIFIC PHRASES TO AVOID]
How you open emails: [YOUR PATTERN]
How you close emails: [YOUR PATTERN]

## Decision Authority
Agent can act autonomously on:
- Scheduling non-urgent internal tasks
- Drafting communications for review
- Generating reports and summaries
- Updating internal records
- Routing information between systems

Agent must escalate to human before:
- Any external communication sent
- Any financial transaction
- Any client commitment made
- Any contract or agreement
- Any public-facing content published

## Quality Standards
[WHAT GOOD WORK LOOKS LIKE IN YOUR BUSINESS]

## This Week's Focus
[UPDATE EVERY MONDAY — current priorities that weight every decision]

The Decision Authority section is the most important part of this file.

It defines the boundary between what the agent does autonomously and what it flags for human review.

Get this wrong in either direction and you either have an agent that does nothing useful or one that makes decisions it should not make.

## The MCP Stack for Business Management

The right MCP connections depend on your specific business tools. These are the highest-value connections for most operators.

Gmail MCP — Read incoming emails. Categorize by type and urgency. Draft responses. Flag items requiring human review. Monitor for specific triggers like payment notifications or client escalations.

Google Calendar MCP — Read your schedule. Create events. Set reminders. Identify scheduling conflicts. Prepare briefings for upcoming calls.

Notion or Airtable MCP — Read and update project databases. Update client records. Track task completion. Generate status reports from live data.

Stripe MCP — Monitor revenue. Flag payment failures. Track MRR trends. Generate financial summaries.

Slack MCP — Post automated updates to channels. Send notifications when workflows complete. Read mentions requiring response.

Filesystem MCP — Read and write your local files. Access your Obsidian vault. Save reports and generated content to the right folders.

Your claude_desktop_config.json connecting the core stack:

{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/your/business/vault"
      ]
    },
    "gmail": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GMAIL_CLIENT_ID": "your-client-id",
        "GMAIL_CLIENT_SECRET": "your-client-secret"
      }
    },
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_KEY": "your-key"
      }
    },
    "gcal": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-calendar"],
      "env": {
        "GCAL_CLIENT_ID": "your-client-id",
        "GCAL_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}

## The Six Business Management Workflows

These six workflows cover the core functions of running a business. Each one runs automatically via N8N without you initiating anything.

Workflow 1: Morning Business Briefing

Trigger: Every weekday at 6AM

What it does:

Read CLAUDE.md for full business context.

Compile the morning briefing from these sources:

EMAIL: Read all emails received since yesterday 5PM.
Categorize each as: CLIENT, PROSPECT, VENDOR, ADMIN, or URGENT.
Summarize any requiring response today.

CALENDAR: Read today's schedule from Google Calendar.
For any external meetings: pull the contact from the CRM,
summarize recent communications, prepare 3 agenda items.

PROJECTS: Read all project records in Notion.
Flag any projects with overdue tasks or approaching deadlines.

REVENUE: Check Stripe for any transactions or alerts since yesterday.

OUTPUT FORMAT:
URGENT (requires action before 10AM): [LIST]
TODAY'S SCHEDULE: [WITH PREP NOTES FOR EACH MEETING]
EMAIL PRIORITIES: [WHAT NEEDS A RESPONSE TODAY]
PROJECT ALERTS: [ANYTHING NEEDING ATTENTION]
REVENUE UPDATE: [KEY NUMBERS]
ONE FOCUS: [The single most important thing to accomplish today]

Save to: /vault/daily-briefings/[DATE]-briefing.md
Send summary to Slack #daily-briefing channel.

Why it matters: You open your laptop to a complete operational picture. No scrambling through email, calendar, and Slack to understand where you stand. The briefing is waiting.

Workflow 2: Email Triage and Draft Generator

Trigger: Every 2 hours during business hours

What it does:

Read all unread emails received in the last 2 hours.

For each email:

STEP 1: Categorize
- CLIENT URGENT: Requires response within 2 hours
- CLIENT STANDARD: Requires response within 24 hours  
- PROSPECT: New potential client inquiry
- VENDOR/ADMIN: Does not require urgent response
- AUTOMATED: No response needed

STEP 2: For CLIENT URGENT and PROSPECT emails:
Read the sender's record from the CRM.
Read any previous email thread with this sender.
Draft a response that:
- Addresses every point raised in their email
- Matches the communication standards in CLAUDE.md
- Includes a specific next step or clear answer
- Does NOT commit to anything in the Decision Authority 
  escalation list

STEP 3: Save drafts to /vault/email-drafts/[DATE]-drafts.md
STEP 4: Send Slack notification listing emails requiring review
with draft locations

Do not send any email. Prepare drafts for human review only.

Why it matters: Email triage that used to take 45 minutes happens automatically. You arrive at your review queue with drafts already written. You approve or edit. You send. The back-and-forth of writing from scratch is eliminated.

Workflow 3: Client Relationship Monitor

Trigger: Every Monday at 7AM

What it does:

Read all active client records from CLAUDE.md and the CRM.

For each client:

COMMUNICATION HEALTH CHECK:
- When was the last communication?
- Is there any open item without a response?
- Is any deliverable overdue?

RELATIONSHIP SCORE:
Rate the relationship health as: HEALTHY, ATTENTION NEEDED, or AT RISK
Based on: recency of contact, open issues, delivery status

ACTION REQUIRED:
For ATTENTION NEEDED: Draft a check-in message
For AT RISK: Flag as urgent and summarize the situation

UPSELL OPPORTUNITY:
Based on the client's usage and stated goals, identify if there
is a natural expansion opportunity worth raising

Save weekly CRM report to: /vault/crm-reports/[DATE]-crm.md
Send Slack alert for any AT RISK clients immediately.

Why it matters: Client churn is expensive. The relationship monitor catches problems before they become cancellations. An at-risk client flagged Monday morning can be saved with a well-timed conversation. The same client flagged after they have already decided to leave cannot.

Workflow 4: Revenue and Financial Tracking

Trigger: First day of every month at 8AM

What it does:

Read all Stripe transactions from the previous month.
Read expense records from the business folder.
Read revenue target from CLAUDE.md.

Generate monthly financial report:

REVENUE SUMMARY:
- Total MRR
- New MRR (new clients started)
- Expansion MRR (upsells)
- Churned MRR (cancellations)
- Net new MRR
- Total vs target (percentage)

CLIENT BREAKDOWN:
- Revenue by client
- Clients at risk of churning based on engagement signals

EXPENSE SUMMARY:
- Total expenses by category
- Month over month comparison
- Largest expense categories

PROJECTION:
- Current run rate
- Projected quarterly total
- Gap to annual target

RECOMMENDATIONS:
- One action to increase revenue this month
- One cost reduction opportunity if any exists

Save to: /vault/finances/[YEAR]-[MONTH]-financial-report.md
Update the revenue figure in CLAUDE.md.

Why it matters: Financial clarity without a manual process. You start every month knowing exactly where you stand without spending an hour pulling numbers from Stripe and spreadsheets.

Workflow 5: Project Status Auto-Updater

Trigger: Continuous — fires when you log completions in your daily note

What it does:

When you write DONE: [project] — [task] in your daily note:

Read the completion entry from today's daily note.
Find the corresponding project record in Notion.
Mark the specified task as complete with today's timestamp.
Check if this completion triggers any dependent tasks.
If yes: update dependent task status to READY.
Check if all tasks in the current phase are complete.
If yes: advance the project to the next phase.
Update the project overview with current completion percentage.
Send Slack notification: "[Project] — [Task] completed. 
Project is now [X]% complete."

Why it matters: Project management that updates itself. You log what you did once. The project database reflects reality automatically. The stakeholder notification goes out automatically. You never manually update a project status again.

Workflow 6: Weekly Business Review

Trigger: Every Sunday at 7PM

What it does:

Read all daily notes from the past 7 days.
Read all project status changes this week.
Read the email triage logs from this week.
Read the financial transactions from this week.
Read the client relationship report from Monday.

Generate the weekly business review:

WHAT MOVED FORWARD:
Specific projects, clients, and metrics that improved
The cause of each improvement

WHAT DID NOT MOVE:
Honest assessment of what stalled
The most likely reason for each

THE PATTERN THIS WEEK:
One theme that appeared repeatedly across the week
Whether it is positive or needs addressing

NEXT WEEK'S PRIORITIES:
Three specific priorities ranked by business impact
For each: why it matters and the specific next action

ONE DECISION TO MAKE:
The most important decision sitting on the table
The information you have to make it
What happens if you delay it one more week

Save to: /vault/weekly-reviews/[DATE]-review.md

Why it matters: The weekly review is the highest-leverage hour in any business. Done well it surfaces patterns that daily operations obscure and identifies the decisions that compound. Done automatically it requires 15 minutes of reading instead of 90 minutes of manual compilation.

## Setting Up the N8N Orchestration Layer

All six workflows run via N8N. Self-hosted on a $5 DigitalOcean droplet.

Each workflow follows the same N8N structure:

Trigger Node → Read CLAUDE.md → Prepare context prompt → 
Claude API call → Process output → Write to vault → 
Send notification → Log operation

The Claude API call always passes the CLAUDE.md contents as system context. This is what makes every automated output business-specific rather than generic.

For the email triage workflow the structure has an additional branch:

Gmail webhook → Filter non-automated emails → 
Read sender CRM record → Prepare draft context → 
Claude API call → Save draft → Slack notification

The Gmail webhook requires a configured Gmail API connection in N8N. This is the most technically involved setup step and typically takes 30 to 45 minutes the first time.

## The First 30 Days

The agent does not run perfectly from day one.

The first week surfaces gaps in your CLAUDE.md. The email triage uses language that does not match your voice. The morning briefing prioritizes the wrong things. The project updater misses a workflow.

Each gap is a two-minute CLAUDE.md edit.

By day 14 the outputs require less editing than they did in week one.

By day 30 the morning briefing is accurate enough that you make decisions from it without checking the sources. The email drafts sound like you wrote them on your best day. The weekly review captures things you would have missed in a manual review.

The compounding starts at day one.

It becomes visible at day 30.

It becomes indispensable at day 90.

## What Changes When It Works

The shift that happens when a business management agent is running correctly is not that you work less.

It is that the work you do is different.

Before the agent: You start every day reacting to email, manually updating project statuses, compiling information that already exists in your tools, and handling the administrative coordination that keeps everything from falling behind.

After the agent: You start every day reading a briefing that is already compiled, reviewing drafts that are already written, seeing project statuses that are already updated, and making decisions about things that actually require your judgment.

The administrative coordination layer of your business runs itself.

What remains is the work only you can do.

Strategy. Relationships. Creative decisions. The judgment calls that make the difference between a good business and a great one.

That is what the agent frees you to focus on.

Build it this weekend.

Start with the morning briefing workflow.

Add one workflow per week.

By month two your business manages itself while you sleep.

Follow @cyrilXBT for the exact N8N workflows, CLAUDE.md templates, and MCP configurations that power this entire system.

## X Article Metadata

- Title: How to Build a Claude Agent That Manages Your Entire Business While You Sleep
- Preview: Most business owners spend their days reacting.
Emails pile up. Project statuses go stale. Client briefs need compiling. Reports need generating. Content needs drafting. Revenue needs tracking.

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
