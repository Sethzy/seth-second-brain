---
type: raw_capture
source_type: web
title: "How a $100M ARR Company Runs RevOps on GitHub; Inside Hightouch's Agent Repo"
url: "https://www.thesignal.club/p/how-a-100m-arr-company-runs-revops"
original_url: "https://www.thesignal.club/p/how-a-100m-arr-company-runs-revops"
author: "Brendan J Short"
captured_at: 2026-07-28T15:10:00+08:00
published_at: 2026-07-21
capture_quality: complete
status: raw
trust_lane: intentional
---

# How a $100M ARR Company Runs RevOps on GitHub; Inside Hightouch's Agent Repo

## Source

- Original: https://www.thesignal.club/p/how-a-100m-arr-company-runs-revops
- Subtitle: Skills for every rep. A four-layer repo for RevOps. And three AI experiments that got pulled. With Nikko Georgantonis, Head of GTM AI & Systems at Hightouch.

## Verbatim Text

If you’ve spent any time on LinkedIn this year, you’ve seen a post claiming “your sales team needs to put all your sales context in a GitHub repo!” Routing logic, field definitions, playbooks, all versioned, all readable by agents. But, often, the person making this claim is a one-man agency owner. So, I’ve been on the hunt to find scale companies running this playbook. Today, we explore one such company.

I first met Tejas, CEO of Hightouch, when we both lived in the Mission district in San Francisco; I was working at Zoom Video, and he had a new little startup and was trying to sell me (I tried to buy, but couldn’t get through procurement with my dinky title). It’s been a blast to see them absolutely ripping over the last 6 years.

Hightouch crossed $100M ARR in April (they’ve grown more than 100% in each of the past two years) and raised a $150M Series D at a $2.75B valuation in March.

I recently sat down with a legend, Nikko Georgantonis, the Head of GTM AI & Systems at Hightouch. What they’ve built is one of the more sophisticated GTM systems I’ve seen. And this is not an agency guy who did a Claude Code project over a weekend. This is what AI adoption looks like inside a revenue org that’s scaling fast enough to have real stakes.

Here’s what we cover in today’s post:

- The two-pillar setup
- Pillar 1: Skills for every rep
- Pillar 2: The four-layer agent repo
- Why a repo instead of a tool
- What’s working for them right now
- What they tried that got pulled back
- RevOps becomes the agent wrangler

Nikko describes his job in two parts.

Part one is adoption. He’s going to QBRs and teaching the revenue org what skills are and why they matter. The deliverable is a library of packaged skills that reps actually use.

Part two is automation. His team has historically owned the system admin work of RevOps (data cleaning, lead list uploads, field hygiene, answering “can you update this account” requests in Slack). He’s handing that work to agents.

What caught my attention is how differently he architected each pillar. The rep-facing stuff is deliberately simple. The RevOps stuff is where the sophistication lives.

### The two-pillar setup

#### Pillar 1: Skills for every rep

The skills pillar isn’t overly complex. The highest-usage skills are things like account research. What makes them work is how prescriptive they are. Every skill follows the same formula: Here’s where to look, what to do, what good looks like, what you shouldn’t do.

A few things stood out to me about how he runs this:

Skills are overlaid onto the customer engagement process. He’s not building random one-off prompts. Each skill maps to a stage of how Hightouch engages customers, and it covers the whole revenue org: AEs, SEs, post-sales.

Reps choose their tool. Skills run in Claude or Glean, whichever the rep prefers. Nikko manages both. Either way, the skill taps into Hightouch’s internal brain through Glean’s MCP, which gives it access to Gong calls and internal docs.

Forking is the point. He ships the prescriptive version, and reps fork it to fit their own workflow.

The BI unlock for leaders. Skills can call Omni (their BI tool) to pull live metrics. That opens up manager and CRO use cases: scheduled skills that send weekly pacing reports without anyone asking for them.

#### Pillar 2: The four-layer agent repo

All of the logic for his RevOps agents lives in a GitHub repo. Execution happens in n8n. The repo has four layers:

1. Context. The documentation that used to live in Notion, made machine-readable.

Their customer engagement process. Lead routing logic. How territories get cut. Forecasting definitions. Every opportunity and account field, audited and defined. Any agent can reference any of it.

2. Coordination. The routing layer.

Example: Hightouch has an internal RevOps Slack channel where people ask for account updates, flag duplicate leads, request list uploads, etc. The number of possible request types is too large for one prompt. So the first agent is a router. It classifies the request and hands it to the right specialist agent, passing notes along with it. Longer-term, this layer is how lead routing and scoring move from rule-based to probabilistic.

3. Memory. Agent history.

The example that made this click for me: Nikko has an agent that sends sales managers a report on each AE’s milestones, how they’re pacing, and a recommendation for what to fix. When it runs again two weeks later, it reads the recommendation it gave last time and factors that in. Some memory belongs in the warehouse. Recommendation history belongs in the repo.

4. Prompts. The actual prompts.

Most people would let these live inside n8n. Nikko keeps a skeleton in n8n that calls the prompt files in the repo instead.

One important note: reps never touch the repo. They see the outputs (a Slack reply, a field in the CRM, a report, a human-review step in the sequencer/dialer). Skills are how reps build. The repo is how RevOps builds.

### Why a repo instead of a tool

Notably, Nikko told me he can’t make tooling bets right now.

Is n8n the right workflow tool today? Yes. Will it be in six months? No idea. Eight months ago, his “skills” were Glean agents. Then the technology moved. He’s watched his own stack rotate underneath him fast enough that betting the logic layer on any single vendor feels reckless.

So the investment goes into the layer that survives tool churn. Context, coordination logic, memory, and prompts, written crisply enough that they can be connected to whatever executes next. When something better than n8n shows up, the migration is re-pointing an execution layer, not rebuilding a brain. This aligns with the thinking Kyle Norton shared on “owning your intelligence” (ie: you should not buy your gtm brain)—you want control, portability, and compounding advantage.

Because everything is documented in one repo, he can point an LLM at it and ask where the redundancy is, where logic is duplicated, and how he should restructure. The system becomes legible to the tools that maintain it. To me, this is the obvious/inevitable future.

And the endgame, in Nikko’s words, is that his job just becomes Claude Code. n8n has an MCP now, so he can do the development in Claude Code and have the documentation write itself back to GitHub. Salesforce admin changes that document themselves. Agents checking the outputs of other agents. His team’s old admin backlog, from data cleaning to lead list uploads, handed off. He says they’re system is starting to compound.

One aside: Cursor skipped the repo entirely and fetches everything live. Different problem. ChatGTM serves reps operational data that goes stale in hours; Nikko’s repo holds business rules that should outlive any tool. Live data gets fetched. Business logic gets committed.

### What’s working for them right now

Territory planning on a digital maturity score. This one predates the agent repo and Nikko was almost dismissive of it, but it might be the most valuable thing he showed me.

He built a Clay workflow that enriches every account with a digital maturity score: does this company run a data warehouse, does it do omnichannel marketing, does it operate a loyalty program, plus other boolean attributes. “Financial services” is a broad industry, and the “digital maturity score” is the next layer down. This bespoke scoring system separates the Chimes of the world from a credit union down the street. And it’s how Hightouch cuts territories today.

The manager pacing reports. Covered above, but it’s a pattern you can steal pretty easily: scheduled skill, pulls defined metrics from BI, gives each manager a per-AE diagnosis and recommendation, remembers what it said last time.

Betting on AI-native vendors. One example: Hightouch is replacing a legacy sales engagement platform with Nooks’ sequencer. A Series D company swapping a legacy sales engagement platform for a smaller, AI-native vendor is atypical, but the reasoning maps to everything above: he wants tools with real MCP workflows built in, not APIs with MCP slapped in front of them. As Nikko told me, “It’s easy to tell the difference.”

### What they tried that got pulled back

1. Black-box reports. Hightouch built agents for proactive analytics: check the dashboards, diagnose what changed, recommend what to do. That works. But, where it broke was mixing in net-new metrics that nobody had defined before. Users didn’t trust them. People are pessimistic toward AI output by default, and an undefined metric inside an AI-generated report reads as a black box. The lesson he took is that agents can diagnose metrics your team already trusts. They shouldn’t invent new ones.

2. The asset-building skill. The team at Hightouch shipped a skill that helps sellers build customer-facing assets, but he’s rolling it back (for now, at least). The failure mode is subtle. The skill does 40-50% of the work. Experienced sellers know exactly what bad looks like, so they finish the remaining half with no problem. But new hires can’t identify which half is theirs to do. So for the people who needed help most, the skill amplified slop instead of raising the floor.

3. Fully automated outbound. For enterprise sales, Nikko isn’t bullish on “automated outbound”, and Hightouch didn’t find success with it. Where automation does work for them is inbound: handling demo-request follow-ups. Nikko clarified this one:

> 100% automated outbound we are bearish on, but agent-assisted we are bullish (and why we bought Nooks).

### RevOps becomes the agent wrangler

Look at what’s actually left for his team once this system matures. The admin work is delegated to agents. The tribal knowledge is codified in the context layer. The reactive Slack-channel work gets triaged by a router. What remains is designing the system: deciding what context agents get, how they hand off, what they remember, and checking their work.

That’s a real answer to the question I keep chasing: who should own AI inside the GTM org? At Cursor, it was a growth leader who built a product. At the 11 growth-stage companies I profiled, it was usually a GTM engineer, RevOps, or a technical founder. At Hightouch, it’s RevOps with engineering habits: version control, documentation, composability.

The tools will keep rotating. Nikko is planning for that instead of fighting it. Six months from now, the executor might not be n8n, and the retrieval layer might not be Glean, and for Hightouch, it won’t matter much, because none of the logic lives there.

RevOps is evolving. And I suspect the early-adopter hacker/tinkerer-type builders, like Nikko at Hightouch, will be the people running systems for AI-native GTM teams in the coming years.

## Capture Note

Complete article body captured from the public source. Sponsorship copy, subscription boilerplate, comments, and footer navigation were omitted. Company metrics and case-study outcomes are source-reported.
