---
type: raw_capture
source_type: web
title: "CodeRabbit Agent"
url: "https://www.coderabbit.ai/agent"
collected_at: 2026-06-10T16:01:15Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# CodeRabbit Agent

Source: https://www.coderabbit.ai/agent

## Capture Text

Extracted readable page text from HTML.

Agent | CodeRabbit | Try for Free
Agent
Enterprise
Customers
Pricing
Blog
Resources
Docs
Trust Center
Contact Us
FAQ
Reports & Guides
Log In
Get a free trial
C
o
d
e
R
a
b
b
i
t
A
g
e
n
t
f
o
r
S
l
a
c
k
Your team's second brain
One agent for your entire Software Development Lifecycle. Right in Slack.
Try for free
Get $50/user free agent minutes.
Threads
Huddles
Channels
eng-backend
eng-incidents
eng-builds
eng-support
Add channels
Apps
GitHub
Notion
Linear
Add apps
#
eng-incidents
Datadog
2:38 AM 🔴
Alert: checkout-service p99 latency > 10s
checkout-service
p99 latency spiked from 380ms to 12.4s at 02:38 UTC.
Nadia K.
2:41 AM
@CodeRabbit pull the Datadog traces for checkout-service and figure out where the bottleneck is.
CodeRabbit
2:41 AM
Pulled APM traces since 02:15 UTC. Every slow trace is stuck on the same downstream call,
POST /api/inventory/reserve
to
inventory-service
.
Checked GCP Cloud Run logs for
inventory-service
. Instance count dropped from 8 to 1 at 02:35 UTC. Autoscaler shows a config change pushed at 02:34 UTC that set
maxInstances
to 1. That came from PR #3301 merged earlier tonight. It was supposed to update env vars but accidentally included a Terraform change to the scaling config.
Marcus J.
2:43 AM
Just saw the page. Nadia, you need a hand?
Nadia K.
2:43 AM
CodeRabbit already found it. Accidental scaling change in #3301.
@CodeRabbit open a revert for just the scaling config
, don't touch the env var update.
CodeRabbit
2:44 AM
Done.
PR #3315
opened:
fix: revert inventory-service maxInstances to 12
Isolated just the scaling revert. The env var update from #3301 is untouched. Once merged, Cloud Run will scale back up within ~90 seconds.
Marcus J.
2:45 AM
Merging. Nadia, watch the dashboard.
Nadia K.
2:47 AM
Latency dropping. Back under 500ms. We're good.
Marcus J.
2:48 AM
@CodeRabbit draft a postmortem and file it. SEV-2.
CodeRabbit
2:48 AM
Done.
ENG-4120
created in Linear: "SEV-2 Postmortem: inventory-service scaling regression" with timeline, root cause, and remediation. Linked to PR #3301 and PR #3315.
Threads
Huddles
Channels
eng-backend
eng-incidents
eng-builds
eng-support
Add channels
Apps
GitHub
Notion
Linear
Add apps
#
eng-incidents
Datadog
2:38 AM 🔴
Alert: checkout-service p99 latency > 10s
checkout-service
p99 latency spiked from 380ms to 12.4s at 02:38 UTC.
Nadia K.
2:41 AM
@CodeRabbit pull the Datadog traces for checkout-service and figure out where the bottleneck is.
CodeRabbit
2:41 AM
Pulled APM traces since 02:15 UTC. Every slow trace is stuck on the same downstream call,
POST /api/inventory/reserve
to
inventory-service
.
Checked GCP Cloud Run logs for
inventory-service
. Instance count dropped from 8 to 1 at 02:35 UTC. Autoscaler shows a config change pushed at 02:34 UTC that set
maxInstances
to 1. That came from PR #3301 merged earlier tonight. It was supposed to update env vars but accidentally included a Terraform change to the scaling config.
Marcus J.
2:43 AM
Just saw the page. Nadia, you need a hand?
Nadia K.
2:43 AM
CodeRabbit already found it. Accidental scaling change in #3301.
@CodeRabbit open a revert for just the scaling config
, don't touch the env var update.
CodeRabbit
2:44 AM
Done.
PR #3315
opened:
fix: revert inventory-service maxInstances to 12
Isolated just the scaling revert. The env var update from #3301 is untouched. Once merged, Cloud Run will scale back up within ~90 seconds.
Marcus J.
2:45 AM
Merging. Nadia, watch the dashboard.
Nadia K.
2:47 AM
Latency dropping. Back under 500ms. We're good.
Marcus J.
2:48 AM
@CodeRabbit draft a postmortem and file it. SEV-2.
CodeRabbit
2:48 AM
Done.
ENG-4120
created in Linear: "SEV-2 Postmortem: inventory-service scaling regression" with timeline, root cause, and remediation. Linked to PR #3301 and PR #3315.
From the team that pioneered AI code reviews
2M
code reviews every week
6M
repos under review
15K
customers
Smart isn't enough
Reasoning without context is a reflex. Context without reasoning is a lookup.
Best agent combines both.
C
o
n
n
e
c
t
o
r
s
Connect your stack,
get answers in Slack
The agent reaches into your tools — Jira, Sentry, Linear, Datadog and more — to fetch context, surface insights, and take action, all without leaving Slack.
Monitoring
Project Tracking
Knowledge
Design
Support
Sentry
Datadog
PagerDuty
CircleCI
AWS
PostHog
Monitoring
Sentry
Datadog
PagerDuty
CircleCI
AWS
PostHog
Project Tracking
Jira
Linear
Asana
Knowledge
Notion
Google Drive
Design
Figma
Canva
Support
HubSpot
Intercom
Zendesk
Gong
Pylon
prod-alerts
Debug the failure
Sentry
APP
10:42 AM
checkout.charge
error rate: 0.4% → 7.1% since 02:08 UTC.
C
o
d
e
R
a
b
b
i
t
A
g
e
n
t
f
o
r
S
l
a
c
k
Built for Agentic SDLC Workflows
Context
Your org's operating context
The agent pulls your org's context together — across every tool and team conversation — into one place.
Code
·
the repo, recent changes and opened PRs
Tickets
·
Jira, Linear or wherever your team tracks work
Docs
·
Notion pages, Confluence wikis, internal runbooks
Monitoring
·
Datadog, PostHog, Sentry & your observability stack
Cloud
·
AWS, GCP, and the infra that runs under it all.
Your org's operating context
The agent pulls your org's context together — across every tool and team conversation — into one place.
Code
–
the repo, recent changes and opened PRs
Tickets
–
Jira, Linear or wherever your team tracks work
Docs
–
Notion pages, Confluence wikis, internal runbooks
Monitoring
–
Datadog, PostHog, Sentry & your observability stack
Cloud
–
AWS, GCP, and the infra that runs under it all.
Memory
A living memory of your team
The agent builds a knowledge base from Slack and your systems. Decisions, fixes, and patterns are captured as they happen and refined through daily use, so it reflects how your team actually works.
Team knowledge
·
Org-wide know-how, shared across teams, channels, and repos
Channel memory
·
retains team-specific patterns, runbooks and conventions
Thread memory
·
carries forward everything from the current task
A living memory of your team
The agent builds a knowledge base from Slack and your systems. Decisions, fixes, and patterns are captured as they happen and refined through daily use, so it reflects how your team actually works.
Team knowledge
–
Org-wide know-how, shared across teams, channels, and repos
Channel memory
–
retains team-specific patterns, runbooks and conventions
Thread memory
–
carries forward everything from the current task
Multi-Player
Built for team collaboration
Work happens in Slack. The agent works in a shared thread alongside your team. Anyone can guide, contribute, and move tasks forward. It learns from team conversations and stays aligned as work evolves.
Synchronous
·
the agent lives in the Slack thread.
Steerable
·
redirect or expand the work mid-task.
Resumable
·
stop, switch devices, come back tomorrow.
Built for team collaboration
Work happens in Slack. The agent works in a shared thread alongside your team. Anyone can guide, contribute, and move tasks forward. It learns from team conversations and stays aligned as work evolves.
Synchronous
–
the agent lives in the Slack thread.
Steerable
–
redirect or expand the work mid-task.
Resumable
–
stop, switch devices, come back tomorrow.
Governance
Guardrails in place
Access, knowledge, and spend, scoped to the channel and user. Every run is explainable and attributed, so you see what the agent did, for whom, and what it cost
Access
·
scoped to who you are and what you do.
Knowledge
·
scoped to the channel where it belongs.
Tool control
·
decide which integrations are available where.
Cost control
·
attributed by team and channel, not individual keys.
Guardrails in place
Access, knowledge, and spend, scoped to the channel and user. Every run is explainable and attributed, so you see what the agent did, for whom, and what it cost
Access
–
scoped to who you are and what you do.
Knowledge
–
scoped to the channel where it belongs.
Tool control
–
decide which integrations are available where.
Cost control
–
attributed by team and channel, not individual keys.
C
u
s
t
o
m
i
z
e
d
Built into the agent
Add skill files and custom sandboxes to suit your needs.
Your agent’s skills
Custom sandboxes
T
r
i
g
g
e
r
s
&
A
u
t
o
m
a
t
i
o
n
s
Work that completes on its own
Beyond @mentions, the agent runs work for you on a schedule or on a signal — investigating, summarizing and posting results in the channel or thread where the team already looks.
#
engineering-standup
Daily · 9:25 AM
CodeRabbit
9:25 AM
Yesterday's merges
·
auth-service: JWT refresh · Ahmad
·
dashboard: chart performance · Maya
·
payments: retry logic · Carlos
Blocked tickets
·
JIRA-1234 — missing design approval
·
JIRA-1456 — waiting on infra team
Overnight Sentry
·
2 new issues · payment timeout +12%
Today's deploys
·
14:00 UTC — api-gateway v2.4.1
Scheduled
#
dev
Every hour · PRs idle >24h
CodeRabbit
10:00 AM
Found
2 stale PRs
in need of attention
#847
26h
+142
3 comments
Add rate limiting to public API
@sarah
@mike
Awaiting security review
#851
31h
+89
7 comments
Migrate legacy auth endpoints
@chen
@alex
Test failures on CI
On signal
See how it works
Typical AI pricing
Input tokens
$3.00 / M
Output tokens
$15.00 / M
Model tier multiplier
1× – 5×
Tool calls
per-call
Context window surcharge
tiered
Your bill
unpredictable
CodeRabbit
Active agent minutes
$0.50 / min
Your bill
minutes × rate
The math
$0.50/minute is roughly
$30/hour
— a fraction of what a senior engineer costs. Except this one runs in parallel, overnight, and on demand.
Pay for time. Not tokens.
Most AI tools bill you across a moving target — model tier, token count, tool calls, context size. You can't forecast it, and your finance team hates it.
CodeRabbit charges one thing: the seconds an agent is actively working. At $0.50/minute, that's roughly $30/hour — a bargain compared to what a senior engineer costs. Except the agent runs in parallel, overnight, and on demand.
We meter every run down to the second and sum it across your team for the billing period. That's the whole model.
Typical AI pricing
Input tokens
$3.00 / M
Output tokens
$15.00 / M
Model tier multiplier
1× – 5×
Tool calls
per-call
Context window surcharge
tiered
Your bill
unpredictable
CodeRabbit
Active agent minutes
$0.50 / min
Your bill
minutes × rate
The math
$0.50/minute is roughly
$30/hour
— a fraction of what a senior engineer costs. Except this one runs in parallel, overnight, and on demand.
FAQ
What is CodeRabbit Agent for Slack?
CodeRabbit Agent for Slack
is built for agentic SDLC workflows. It pulls your org’s operating context together from across every tool and team conversation - code, tickets, docs, monitoring, cloud - and reasons over it to move work forward in the channel or thread where it’s already happening. It investigates, plans, opens PRs, captures team knowledge, and keeps everyone aligned as work evolves.
What is Agentic SDLC?
Agentic SDLC is a software delivery practice where AI agents participate meaningfully across the complete software development lifecycle - planning, requirement analysis, design, coding, testing, deployment, and maintenance. Instead of your team bouncing between point tools, the CodeRabbit Agent works alongside you, carrying context across phases, taking action on your behalf, capturing what the team learns, and staying accountable for its actions.
What Agentic SDLC actually needs?
To effectively implement the Agentic Software Development Lifecycle (SDLC), you need four key elements: a clear context of your organization's operations across code, issue trackers, and tools; a long-term, durable team knowledge; support for collaboration in existing communication channels; and proper governance with scoped access to tools and spend controls.
How to start using CodeRabbit Agent for Slack?
Sign in with Slack to establish the workspace identity. Then connect GitHub by linking your Slack workspace to the GitHub org. Install the CodeRabbit GitHub App to grant repository access. Optionally, you can edit the base scope - the default repositories, connections, and spend baseline for the workspace. Finally, start using CodeRabbit Agent for Slack, just mention @coderabbit in any channel or DM.
What tools does it integrate with?
CodeRabbit Agent for Slack connects with all the SDLC tools, such as Jira, Linear, Notion, Asana, Intercom, Zendesk, AWS, Datadog, CircleCI, PostHog, Sentry, PagerDuty, Figma, Canva, Google Drive, Gong, Pylon, OneDrive, and HubSpot. You can also plug in your own through MCP servers and APIs.
What are agent minutes, and how does pricing work for this product?
Agent minutes are the amount of active CodeRabbit runtime spent completing a task. The runtime measures elapsed sandbox time, from command start to run finish, and bills for minutes used.
Can I control what the CodeRabbit Agent can access?
Governance is integrated through scopes, which define everything the agent can do in a given context: accessible repositories, usable connections, user groups and users authorized to invoke it, and applicable spend limits. Every workspace starts with a default base scope, and additional scopes can be created that inherit from it and impose narrower restrictions.
How does knowledge base work with CodeRabbit Agent for Slack?
The knowledge base stores durable facts that it learned by working with your team. Knowledge respects Slack’s privacy boundaries, so public channels and shared surfaces use the global workspace knowledge base, private channels use a private conversation knowledge base, while DMs and group DMs use a private conversation knowledge base.
How can I monitor the usage of CodeRabbit Agent for Slack?
Just go to the
Usage tab
of your CodeRabbit Agent for Slack dashboard and monitor it from there.
Who can use and manage it?
CodeRabbit Agent for Slack responds only to workspace members. External users (guests) are blocked by default, and channels marked as externally shared are fully unsupported. For now, you can set up roles using the Workspace users section in
your settings
. Currently, you can pick between primary user, CodeRabbit admin, and scope admin (which requires a custom scope).
Where can I find more technical guidance regarding CodeRabbit Agent for Slack?
The most effective resource that will allow you to grasp all the technical concepts around CodeRabbit Agent for Slack would be our
docs
.
I already use CodeRabbit for code review. Is this the same thing?
Code review runs automatically on your pull requests. CodeRabbit Agent for Slack is built for agentic SDLC workflows. It lives in the channel or thread where your team already works, pulls your org’s operating context from across code, tickets, docs, monitoring, cloud, and reasons over it to investigate, plan, open PRs, and carry your team’s knowledge forward, all within guardrails you control. The two products share the same underlying engine.
Does this replace my engineers?
CodeRabbit Agent for Slack is designed to amplify your team, not replace it. It remembers what your team knows, handles the repeatable work, and surfaces context so engineers can focus on the hard decisions. Your team steers the agent in real time, reviews its work, and makes the calls that matter. The hard parts of engineering stay with the engineers.
Try it today
One agent for your entire Software Development Lifecycle. Right in Slack.
Try for free
Get $50/user free agent minutes.
Products
Agent
Pull Request Reviews
IDE Reviews
CLI Reviews
Plan
OSS
Navigation
About Us
Features
FAQ
System Status
Careers
DPA
Startup Program
Vulnerability Disclosure
Resources
Blog
Docs
Changelog
Case Studies
Trust Center
Brand Guidelines
Reports & Guides
Contact
Support
Sales
Pricing
Partnerships
Subscribe
By
signing up
you agree to our
Terms of Use
and authorize CodeRabbit to provide occasional updates about products and solutions. You understand that you can opt out at any time and that your data will be handled in accordance with
CodeRabbit Privacy Policy
Select language
English
日本語
Terms of Service
Privacy Policy
CodeRabbit, Inc. ©  2026
Products
Agent
Pull Request Reviews
IDE Reviews
CLI Reviews
Plan
OSS
Navigation
About Us
Features
FAQ
System Status
Careers
DPA
Startup Program
Vulnerability Disclosure
Resources
Blog
Docs
Changelog
Case Studies
Trust Center
Brand Guidelines
Reports & Guides
Contact
Support
Sales
Pricing
Partnerships
Select language
English
日本語
Subscribe
By
signing up
you agree to our
Terms of Use
and authorize CodeRabbit to provide occasional updates about products and solutions. You understand that you can opt out at any time and that your data will be handled in accordance with
CodeRabbit Privacy Policy
