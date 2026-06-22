---
type: raw_capture
source_type: web
title: "Lessons from building Claude Code: Prompt caching is everything"
url: "https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything/"
canonical_url: "https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything/"
vendor_blog: claude
published_at: 2026-04-30
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Lessons from building Claude Code: Prompt caching is everything

Original URL: https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything/
Published: 2026-04-30
Captured: 2026-06-14T02:32:25+00:00

Description: Best practices for optimizing prompt caching in Claude Code, including how to most effectively structure your prompt, use tools, and layer on compaction.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

# Lessons from building Claude Code: Prompt caching is everything

We share best practices for optimizing prompt caching in Claude Code, including how to most effectively structure your prompt, use tools, and layer on compaction.

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  April 30, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything

It is often said in engineering that "cache rules everything around me", and the same rule holds for agents.

Long running agentic products like Claude Code are made feasible by [**prompt caching**](https://x.com/RLanceMartin/status/2024573404888911886) which allows us to reuse computation from previous roundtrips and significantly decrease latency and cost.

At Claude Code, we build our entire harness around prompt caching. A high prompt cache hit rate decreases costs and helps us create more generous rate limits for our subscription plans, so we run alerts on our prompt cache hit rate and declare SEVs if they're too low.

These are the (often unintuitive) lessons we've learned from optimizing prompt caching at scale.

## **Lay out your prompt for caching**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f2f39fa10dea4e26853e8c_2371721a.png)

Claude Code's system prompt is organized so the stable pieces stay cached and only the conversation itself grows turn by turn.

Prompt caching works by prefix matching—the API caches everything from the start of the request up to each `cache_control` breakpoint. This means the order you put things in matters enormously, you want as many of your requests to share a prefix as possible.

The best way to do this is static content first, dynamic content last. For Claude Code this looks like:

1. **Static system prompt** & Tools (globally cached)
2. **CLAUDE.md** (cached within a project)
3. **Session context** (cached within a session)
4. **Conversation messages**

This way we maximize how many sessions share cache hits.

But this approach can be surprisingly fragile. We’ve broken this ordering before for a variety of reasons, including: putting an in-depth timestamp in the static system prompt, shuffling tool order definitions non-deterministically, and updating parameters of tools (e.g., what agents the Agent tool can call).

## **Use messages for updates**

There may be times when the information you put in your prompt becomes out of date, for example if you have the time or if the user changes a file. It may be tempting to update the prompt, but that would result in a cache miss and could end up being quite expensive for the user.

Consider if you can pass in this information via messages in the agent’s next turn instead. In Claude Code, we add a <system-reminder> tag in the next user message or tool result with the updated information for the model, which helps preserve the cache.

## **Don't change models mid-session**

Prompt caches are unique to models and this can make the math of prompt caching quite unintuitive.

For example, if you're 100k tokens into a conversation with Opus and want to ask a question that is fairly easy to answer, it would actually be more expensive to switch to Haiku than to have Opus answer, because we would need to rebuild the prompt cache for Haiku.

If you need to switch models, the best way to do it is with subagents; extending the above example, you could deploy a subagent that prompts Opus to prepare a "hand-off" message to another model on the task that it needs to get done. We do this often with the Claude Code’s Explore agents, which use Haiku.

## **Never add or remove tools mid-session**

Changing the tool set in the middle of a conversation is one of the most common ways people break prompt caching. It seems intuitive—you should only give the model tools you think it needs right now. But because tools are part of the cached prefix, adding or removing a tool invalidates the cache for the entire conversation.

**Using Plan Mode to design around the cache**

[Plan Mode](https://code.claude.com/docs/en/common-workflows) is a great example of designing features around caching constraints. The intuitive approach would be: when the user enters plan mode, swap out the tool set to only include read-only tools, but that would break the cache.

Instead, we keep *all* tools in the request at all times and use EnterPlanMode and ExitPlanMode as tools themselves. When the user toggles Plan Mode on, the agent gets a system message explaining that it's in Plan Mode and what the instructions are:  explore the codebase, don't edit files, and call ExitPlanMode when the plan is complete. The tool definitions never change.

This has a bonus benefit: because EnterPlanMode is a tool the model can call itself, it can autonomously enter plan mode when it detects a hard problem, without any cache break.

**Use tool search to defer instead of remove**

The same principle applies to our [tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool). Claude Code can have dozens of MCP tools loaded, and including all of them in every request would be expensive, but removing them mid-conversation would break the cache.

Our solution: `defer_loading`. Instead of removing tools, we send lightweight stubs ( just the tool name, with `defer_loading: true`) that the model can "discover" via tool search when needed. The full tool schemas are only loaded when the model selects them. This keeps the cached prefix stable because the same stubs are always present in the same order.

You can also use the [tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) through our API to simplify this.

## **Compacting without breaking the cache**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f2f39fa10dea4e26853e8f_9e1aba00.png)

When the context window fills up, Claude Code forks a cached call to summarize the conversation, then resumes with the summary in place of the original messages.

[Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) is what happens when you run out of the context window. We summarize the conversation so far and continue a new session with that summary.

Compaction interacts with prompt caching in ways that are easy to get wrong. To compact a conversation, you have to send the full conversation to the model so it can write a summary. The simplest way to do that is a separate API call with its own system prompt (something like "summarize this") and no tools attached, but that's exactly where the cost trap is. Prompt caching only applies when a request's prefix matches what's already cached, byte for byte, from the start. Your main conversation is cached under one system prompt and tool set; the summarization call uses a different system prompt and no tools, so the prefixes diverge at the very first token and none of the cache applies. You end up paying the full, uncached input rate for the entire conversation you're sending in — and the longer the conversation (i.e., the more you need compaction in the first place), the more expensive that one call becomes.

**The solution: cache-safe forking**

When we run compaction, we use the *exact same* system prompt, user context, system context, and tool definitions as the parent conversation. We prepend the parent's conversation messages, then append the compaction prompt as a new user message at the end.

From the API's perspective, this request looks nearly identical to the parent's last request—same prefix, same tools, same history—so the cached prefix is reused. The only new tokens are the compaction prompt itself.

This does mean however that we need to save a "compaction buffer" so that we have enough room in the context window to include the compact message and the summary output tokens.

Compaction is tricky but luckily, you don't need to learn these lessons yourself—based on our learnings from Claude Code we built [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction#prompt-caching) directly into the API, so you can apply these patterns in your own applications.

## **Lessons learned**

Here are a few patterns we’ve found useful for optimizing prompt caching when building an agent:

1. **Prompt caching is a prefix match.** Any change anywhere in the prefix invalidates everything after it. Design your entire system around this constraint. Get the ordering right and most of the caching works for free.
2. **Use messages instead of system prompt changes**. You may be tempted to edit the system prompt to do things like entering plan mode, changing the date, etc. but it would actually be better to insert these into messages during the conversation.
3. **Don't change tools or models mid-conversation.** Use tools to model state transitions (like plan mode) rather than changing the tool set. Defer tool loading instead of removing tools.
4. **Monitor your cache hit rate like you monitor uptime.** We alert on cache breaks and treat them as incidents. A few percentage points of cache miss rate can dramatically affect cost and latency.
5. **Fork operations need to share the parent's prefix.** If you need to run a side computation (compaction, summarization, skill execution), use identical cache-safe parameters so you get cache hits on the parent's prefix.

Claude Code is built around prompt caching from day one; for the best results when building an agent, we suggest you do, too.

[*Get started*](https://code.claude.com/docs/en/overview) *with Claude Code today.*

*This article was written by Thariq Shihipar, a member of technical staff on the Claude Code team.*

‍

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Oct 8, 2025

### Beyond permission prompts: making Claude Code more secure and autonomous

Claude Code

[Beyond permission prompts: making Claude Code more secure and autonomous](#)Beyond permission prompts: making Claude Code more secure and autonomous

[Beyond permission prompts: making Claude Code more secure and autonomous](/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous)Beyond permission prompts: making Claude Code more secure and autonomous

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Jun 5, 2026

### How one Anthropic seller rebuilt his team's workflows with Claude Code

Claude Code

[How one Anthropic seller rebuilt his team's workflows with Claude Code](#)How one Anthropic seller rebuilt his team's workflows with Claude Code

[How one Anthropic seller rebuilt his team's workflows with Claude Code](/blog/how-anthropic-uses-claude-gtm-engineering)How one Anthropic seller rebuilt his team's workflows with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jun 3, 2026

### Lessons from building Claude Code: How we use skills

Claude Code

[Lessons from building Claude Code: How we use skills](#)Lessons from building Claude Code: How we use skills

[Lessons from building Claude Code: How we use skills](/blog/lessons-from-building-claude-code-how-we-use-skills)Lessons from building Claude Code: How we use skills

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

Jun 2, 2026

### A harness for every task: dynamic workflows in Claude Code

Claude Code

[A harness for every task: dynamic workflows in Claude Code](#) A harness for every task: dynamic workflows in Claude Code

[A harness for every task: dynamic workflows in Claude Code](/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) A harness for every task: dynamic workflows in Claude Code

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
