---
type: raw_capture
source_type: x
url: https://x.com/davep/status/2081746878119678414
original_url: https://x.com/davep/status/2081746878119678414
author: "David Pan"
handle: davep
status_id: 2081746878119678414
captured_at: 2026-07-28T14:52:16+08:00
published_at: "Mon Jul 27 14:21:47 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 17
  reposts: 16
  likes: 161
---

# X post by @davep

## Source

- Original: [https://x.com/davep/status/2081746878119678414](https://x.com/davep/status/2081746878119678414)
- Canonical: [https://x.com/davep/status/2081746878119678414](https://x.com/davep/status/2081746878119678414)
- Author: David Pan (@davep)

## Verbatim Text

Stripe and Sierra built their own coding agent systems. You probably don't need to.

[Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) built minions, a homegrown agent system that merges 1,300+ pull requests every week with no human-written code. [Sierra's Pinecone](https://x.com/neilrahilly/status/2075290325757608148?s=20) opens 70% of their PRs. The write-ups are excellent. If you haven't read them, you should. If you have, you've probably wondered whether you should build your own.

For most teams, I think the answer is no. Not because Stripe and Sierra got it wrong. They were early to these ideas and they have the teams to pull this off. But you can now buy (nearly) everything they had to build. Most orgs should be optimizing for something else: speed to value. I work at Cursor, so I have my own biases, but here are my reasons:

## 1. The differentiated part is portable anyway

The part of a cloud agent system that makes it feel like yours is the context layer. Rules that encode your conventions. Skills to codify reusable instructions. MCP access to your internal systems. Workflows to verify what agents have written. When Stripe's minions read the same rule files their engineers write for Cursor and Claude Code, and pull context from the same internal MCP tools, that's context doing the work.

Here's the thing about this layer: it's the most differentiated part of the system, and it's also the most portable. A rule file, a skill, and an MCP config all work the same anywhere, and none of them tie you to a vendor. Stripe proved the point by standardizing on Cursor's rule format, so one set of rules guides their minions, Cursor, and Claude Code alike. So the usual fear, "if we buy the platform, we give up our differentiation," is just not a concern. You keep the differentiated part no matter what. Buying means you skip everything underneath it.

## 2. The build is way bigger than it looks

Getting an agent running in a VM? That's a weekend. Getting to four nines of reliability and sub-10-second environment startups? That's a multi-quarter infrastructure project. We've been building cloud agents at Cursor for 18 months and we believe it will be an indefinite area of investment.

There's a polish problem too. Even a working internal build rarely gets the attention to detail that makes people actually use it. An internal tool that's 80% as good gets 20% of the usage. Most teams ship a Slack bot and stop there, because integrating the same agent into the IDE, CLI, web, mobile, Jira, etc. is way too much surface area. And then there's governance: user management, token analytics, budget controls, audit trails. All of it is mandatory, none of it is differentiating.

Accountability is another cost that never makes it into the build estimate. Agents do things. Eventually one of them does the wrong thing. When that happens, everyone looks at the team that built the system, and now that team owns the incident, the postmortem, and the remediation. Buying doesn't make incidents impossible, but it does put a vendor with a security team on the hook next to you.

## 3. The state of the art won't sit still

Every month or so, some forward-thinking team invents a better way to automate the SDLC, and whatever you built three months ago looks dated. Fine-tuned code models got lapped by the next frontier release. The RAG stacks everyone built lost to long context and agentic search. Custom integrations became MCP configs overnight. Even Sierra started with parallel agents in git worktrees and built past them within months.

At Cursor's scale, we can lean into that churn. We’re happy to rebuild because the cost spreads across thousands of customers, and the math still works. The same scale buys negotiated cloud contracts and multi-tenant bin packing that no internal deployment can match. For an in-house devex team, the same churn is a tax. Every reinvention lands on a roadmap that's already full of internal customers. You don't want to be on the permanent R&D treadmill. You want a scaled partner who runs it for you.

## 4. Buying doesn't mean giving up control

The last objection is control. Most build decisions are really lock-in fears in disguise, so get specific about where you actually need options. Models are the obvious one: token spend is turning into a real line item, and the pareto frontier of capability versus cost moves every few weeks. With a model-neutral platform, you’ll always have access to the very best no matter who is leading the race this week.

The other one is the agent execution layer. Run it however you want, from fully Cursor-hosted to fully self-hosted in your own network, where agents can reach internal endpoints and test infra like any service account would. Your security posture becomes a deployment choice, not a reason to build.

## When building makes sense

There are a few things that tip the scales toward building. The more of these that describe you, the stronger the case.

Your product is agent infrastructure. Sierra sells AI agents for a living. Building agent systems is in their DNA and dogfooded by a few hundred employees every day. They certainly have the expertise to build a coding agent system as well.

You already own the hard parts. Stripe ran minions on devboxes they'd spent a decade perfecting. For them, building an agent system around those devboxes is probably less work than bending them to fit the shape of an off-the-shelf product. If your dev infrastructure is that mature and that bespoke, the math can flip the same way for you.

You'll fund it like a product, indefinitely. A staffed team with a roadmap, on-call, and a budget that survives reorgs. Even then, don't start from zero: building blocks like the [Cursor SDK](https://cursor.com/sdk) give you a model-agnostic agent harness that’s ready to go, so your team's effort goes into the parts that are unique to you.

## Credit where it's due

I have huge respect for Stripe, Sierra, and the other teams pushing the limits of agentic engineering. Their eng teams are second to none. But most orgs don't need to follow in their footsteps. They need speed to value and a partner whose whole job is staying at the cutting edge on their behalf. For almost everyone, that's worth more than full customization.

Get AI-native asap. Then decide which pieces to bring in-house, one at a time.

## X Article Metadata

- Title: Stripe and Sierra built their own coding agent systems. You probably don't need to.
- Preview: Stripe built minions, a homegrown agent system that merges 1,300+ pull requests every week with no human-written code. Sierra's Pinecone opens 70% of their PRs. The write-ups are excellent. If you

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
