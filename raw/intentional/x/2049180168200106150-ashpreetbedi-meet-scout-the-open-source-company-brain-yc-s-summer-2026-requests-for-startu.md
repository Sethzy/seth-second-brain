---
type: raw_capture
source_type: x
url: https://x.com/ashpreetbedi/status/2049180168200106150
original_url: https://x.com/ashpreetbedi/status/2049180168200106150
author: "Ashpreet Bedi"
handle: ashpreetbedi
status_id: 2049180168200106150
captured_at: 2026-06-11T00:17:46+08:00
published_at: "Tue Apr 28 17:33:18 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 31
  reposts: 83
  likes: 1313
---

# X post by @ashpreetbedi

## Source

- Original: [https://x.com/ashpreetbedi/status/2049180168200106150](https://x.com/ashpreetbedi/status/2049180168200106150)
- Canonical: [https://x.com/ashpreetbedi/status/2049180168200106150](https://x.com/ashpreetbedi/status/2049180168200106150)
- Author: Ashpreet Bedi (@ashpreetbedi)

## Verbatim Text

Meet Scout. The open-source company brain

YC's Summer 2026 [Requests for Startups](https://www.ycombinator.com/rfs) named two ideas that point at the same thing from different angles.

[Company Brain](https://www.ycombinator.com/rfs#company-brain): pull knowledge out of fragmented sources (Slack, email, tickets), structure it, keep it current, turn it into something AI can act on.

> "Structure it, keep it current" is the wrong approach. 
The trick is "navigation over search". More on this later.

[Embedded Tweet: https://x.com/i/status/2048834293779378437]

[AI Operating System for Companies](https://www.ycombinator.com/rfs#ai-operating-system-for-companies): the connective layer that makes a company legible to AI by default. Closed-loop systems that watch what happens after a decision and adjust.

[Embedded Tweet: https://x.com/i/status/2048834315539435657]

The brain is the data layer. The OS is what runs on top of it. Neither exists as a finished product today but the pieces are there (model capability, context providers, agentic SQL, MCP, persistent memory, scheduled execution).

Let's see if we can stitch them into something useful. We'll build the company brain together, and see if we can turn it into the AI operating system.

# Meet Scout

[Scout is a open-source context agent](https://github.com/agno-agi/scout). It navigates live information sources to assemble context on demand. It connects the fragmented knowledge living in slack, google drive, linear using proven patterns like "navigation over search", "context providers", and "learning machines".

Scout also builds its own wiki and CRM as it learns about your company. So you can share that "Josh from Anthropic shared this new paper on RLMs" and it'll add a note in the CRM, parse the paper and store it in the company wiki.

You can also share that "a decision on v3 schema migration" is pending and it'll log a follow up in the CRM, ready to surface next time anyone asks what's open. Put follow-up review on a daily cron and the loop gets tighter.

Let's talk through some of the design decisions that make Scout better than dump-everything-in-a-vector-db-and-pray-we-find-the-right-chunks.

# Context Providers

The first issue we run into when building a "company brain" is the ability for one agent to connect all the tools and work across information sources. The three problems that are currently unsolved:

1. Context pollution from too many tools

2. Degrading performance from overlapping scopes

3. Main agent stops working because its context is all tool quirks

The solution which I have found to work is a thin layer between the agent and tools called Context Providers. Each information source (slack, drive, CRM) becomes a context provider and exposes two tools to the main agent:

- query_<source> for natural-language reads

- update_<source> for natural-language writes

The first advantage of this approach is that the main agent doesn't see Slack's twelve tools. It just sees query_slack.

The second advantage, which is the BIG WIN, is that behind the query_slack tool is a sub-agent that owns all of Slack's quirks (look up the user before you DM them, paginate by cursor, prefer conversations.replies for threads). This is extremely important because now the main agent's context is not polluted with instructions on how to use slack, or all the intermediate tool call results.

And no, skills don't solve this. Skills are task-specific instructions ("here's how to use Slack") that the model loads on-demand. Skills move task knowledge out of the always-on prompt and into something more conditional. But when the module is loaded, the Slack tools will still land on the main agent, the intermediate tool call results are still in the main context. Load 2 skills with search capabilities and your agent dies immediately.

Scout's tool surface today:

- Web: query_web

- Slack: query_slack, update_slack

- Google Drive: query_gdrive

- CRM: query_crm, update_crm (writes to contacts / projects / notes / follow-ups)

- Knowledge wiki: query_knowledge, update_knowledge

- Voice wiki: query_voice (read-only)

- MCP servers: query_mcp_<server> (one per registered server)

- Workspace: query_workspace

- Cross-cutting: list_contexts

The payoff:

1. You can actually use multiple context providers together. query_slack finds the discussion, query_gdrive finds the doc.

2. The routing is bare minimum, meaning Scout's instructions stay the same and adding more tools doesn't cause regressions.

You can read a deeper post on Context Providers here:

[Embedded Tweet: https://x.com/i/status/2048817143974613089]

# Navigation over search

The default move when you're building a "company brain" is to ingest everything into a vector db, chunk, embed, and retrieve top-k.

This DOES NOT WORK. The index is always stale. The chunks land at the wrong boundaries. The citations point at fragments that were true last Tuesday. Half the time the relevant content was in the Slack thread that never got indexed because who in their right mind indexes Slack!

Here's the thing the coding agents figured out: dont search, navigate. They `ls` a directory. They `grep` for a function names. They open the file. They follow the import. They walk through the filesystem, just like humans do.

This pattern transfers really well to context agents. Every information source already has the equivalent of ls, grep, and cat. They're exposed behind the context provider.

The payoff:

1. Live State. The Slack message you sent thirty seconds ago is available to the agent. Yesterday's roadmap doc is current because it's the actual doc.

2. Real citations. Every reference is a path you can open. No fragment from an embedding boundary.

3. Permissions stay where they live. Drive enforces who can read what, Slack enforces channel membership. Scout sees what its credentials see.

The trade off is more LLM calls per query. A vector lookup is one round trip; navigation is three or four.

# The wiki, crm, and the closed loop

Some things don't have a natural source home. "Josh from Anthropic shared an RLM paper last week" doesn't live anywhere obvious. It was probably mentioned in Slack, but you don't search Slack for "who is Josh".

That's what the CRM and the knowledge wiki are for. Scout populates these as it learns. Josh becomes a contact in the CRM. The RLM paper becomes a wiki page linked from his contact note.

The CRM ships with four tables: scout_contacts, scout_projects, scout_notes, scout_followups. Beyond those, the write sub-agent creates new scout_* tables on demand. "Track my coffee orders" becomes a scout_coffee_orders table with the right columns. Schema on demand.

> If you think LLMs are good at bash, wait till you see them write SQL.

# Scout in action

[Scout is open-source.](https://github.com/agno-agi/scout) Fork it, customize it, make it your own. [Repo](https://github.com/agno-agi/scout).

## Quickstart

Clone the repo, add your API key and run scout locally using docker.

```shell
git clone https://github.com/agno-agi/scout && cd scout

cp example.env .env             # set OPENAI_API_KEY

docker compose up -d --build
```

By default, scout comes with the web, CRM, knowledge wiki, voice wiki, and workspace context providers. Slack and Google Drive providers are wired up, you just need to set up the credentials.

## AgentOS

Scout runs on Agno's [AgentOS](https://docs.agno.com/). You get a UI, multi-user sessions, scheduled tasks, and a FastAPI app that deploys anywhere Docker runs. Once you have Scout running locally, connect it to the AgentOS UI at [os.agno.com](https://os.agno.com/).

## Slack

Scout is part of your team, and integrating Slack is a ~5 minute setup. Each Slack thread becomes its own session, follow-ups carry the full history.

See the [SLACK_CONNECT.md](https://github.com/agno-agi/scout/blob/main/docs/SLACK_CONNECT.md) file for the setup guide.

Some prompts to test with:

- "Which contexts are you connected to?"

- "Walk me through your codebase"

- "Save a note: Josh from Anthropic shared a new RLM paper this week"

- "The v3 schema migration decision is pending, surface it next Tuesday"

- "Create a runbook for incident response — page on-call first, post status in #incidents, capture timeline as you go"

- "Start tracking my coffee consumption. First one: flat white, extra shot"

# What's next

The roadmap from here:

- Scheduled tasks. Surface pending follow-ups automatically.

- Proactive actions per source. Run update_slack, update_github daily.

- GitHub, Gmail, Calendar providers. Testing on a side branch.

---

Links:

- [Scout](https://github.com/agno-agi/scout)

- [Agno Docs](https://docs.agno.com/)

- [Agno GitHub](https://github.com/agno-agi/agno)

## X Article Metadata

- Title: Meet Scout. The open-source company brain
- Preview: YC's Summer 2026 Requests for Startups named two ideas that point at the same thing from different angles.
Company Brain: pull knowledge out of fragmented sources (Slack, email, tickets), structure

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
