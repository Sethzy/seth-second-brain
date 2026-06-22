---
type: raw_capture
source_type: web
title: "Built-in memory for Claude Managed Agents"
url: "https://claude.com/blog/claude-managed-agents-memory/"
canonical_url: "https://claude.com/blog/claude-managed-agents-memory/"
vendor_blog: claude
published_at: 2026-04-23
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Built-in memory for Claude Managed Agents

Original URL: https://claude.com/blog/claude-managed-agents-memory/
Published: 2026-04-23
Captured: 2026-06-14T02:32:25+00:00

Description: Memory on Claude Managed Agents lets you build agents that learn from every task, user, and session, with no memory infrastructure to maintain.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

# Built-in memory for Claude Managed Agents

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  April 23, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-managed-agents-memory

Memory on [Claude Managed Agents](https://claude.com/blog/claude-managed-agents) is available today in public beta. Your agents can now learn from every session, using an intelligence-optimized memory layer that balances performance with flexibility. Because memories are stored as files, developers can export them, manage them via the API, and keep full control over what agents retain.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e911b25f02df256c8cba87_Claude-Blog-CMA-Memory.png)

## Agents that learn across sessions

Managed Agents pairs production infrastructure with a harness tuned for performance. Memory extends that: it’s optimized against internal benchmarks for long-running agents that improve across sessions and share what they've learned with each other.

We've found that agents are most effective with memory when it builds on the tools they already use. Memory on Managed Agents mounts directly onto a filesystem, so Claude can rely on the same bash and code execution capabilities that make it effective at agentic tasks. With filesystem-based memory, [our latest models](https://www.anthropic.com/news/claude-opus-4-7#:~:text=Memory.%20Opus%204.7%20is%20better%20at%20using%20file%20system%2Dbased%20memory.%20It%20remembers%20important%20notes%20across%20long%2C%20multi%2Dsession%20work%2C%20and%20uses%20them%20to%20move%20on%20to%20new%20tasks%20that%2C%20as%20a%20result%2C%20need%20less%20up%2Dfront%20context.) save more comprehensive, well-organized memories and are more discerning about what to remember for a given task.

## Portable memories for production-grade agents

Memory is built for enterprise deployments, with scoped permissions, audit logs, and full programmatic control. Stores can be shared across multiple agents with different access scopes. For example, an org-wide store might be read-only, while per-user stores allow reads and writes. Multiple agents can work concurrently against the same store without overwriting each other.

Memories are files that can be exported and independently managed via the API, giving developers full control. All changes are tracked with a detailed audit log, so you can tell which agent and session a memory came from. You can roll back to an earlier version or redact content from history. Updates also surface in the [Claude Console](https://platform.claude.com/) as session events, so developers can trace what an agent learned and where it came from.

## **What teams are building**

Teams have been using memory to close feedback loops, speed up verification, and replace custom retrieval infrastructure:

* **Netflix** agents carry context across sessions, including insights that took multiple turns to uncover and corrections from a human mid-conversation, instead of manually updating prompts and skills.
* **Rakuten's** task-based long-running agents use memory to learn from every session and avoid repeating past mistakes, cutting first-pass errors by 97%, all within workspace-scoped, observable boundaries.
* **Wisedocs** built their document verification pipeline on Managed Agents, using cross-session memory to spot and remember recurring document issues, speeding up verification by 30%.**‍**
* **Ando** is building their workplace messaging platform on Managed Agents, capturing how each organization interacts instead of building memory infrastructure themselves.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Memory in Claude Managed Agents lets us put continuous learning into production at scale. Our agents distill lessons from every session, delivering 97% fewer first-pass errors at 27% lower cost and 34% lower latency, so users spend less time nudging agents to fix mistakes the system has already learned to avoid. And because memory is workspace-scoped and observable, continuous learning stays under our control.

Yusuke Kaji, General Manager, AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcd77828fd211e8ca469_ando-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcdb9e60b6c1a29d80cb_ando-dark.svg)

A lot of our work at Ando is making sense of fast-moving, messy conversations between teams and their agents. Memory lets us stop building memory infra and focus on the product itself.

Sara Du, Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2b010f3f3d0c408c6ec5_wisedocs-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2afe43c6e63a42d7d5ce_wisedocs-dark.svg)

A good memory API gets rid of many infrastructure headaches, especially when building across agents and sessions. In our document verification pipeline on Claude Managed Agents, we used cross-session memory to let our agents identify and remember common issues — including ones we didn't think about. It's sped verification up 30%.

Denys Linkov, Head of Machine Learning

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

Memory on Managed Agents is now available in public beta on the Claude Platform. Visit the [Claude Console](https://platform.claude.com/) or use our new CLI to deploy your first agent with memory. Explore the [documentation](https://platform.claude.com/docs/en/managed-agents/memory) to learn more.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

Apr 14, 2026

### Introducing routines in Claude Code

Product announcements

[Introducing routines in Claude Code](#)Introducing routines in Claude Code

[Introducing routines in Claude Code](/blog/introducing-routines-in-claude-code)Introducing routines in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

May 28, 2026

### Introducing dynamic workflows in Claude Code

Product announcements

[Introducing dynamic workflows in Claude Code](#)Introducing dynamic workflows in Claude Code

[Introducing dynamic workflows in Claude Code](/blog/introducing-dynamic-workflows-in-claude-code)Introducing dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

Jun 9, 2026

### New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

Product announcements

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](#)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](/blog/whats-new-in-claude-managed-agents)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jun 8, 2026

### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Product announcements

[Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](#)Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

[Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](/blog/claude-for-foundation-models)Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
