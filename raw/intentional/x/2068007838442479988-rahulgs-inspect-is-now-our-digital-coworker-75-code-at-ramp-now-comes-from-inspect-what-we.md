---
type: raw_capture
source_type: x
url: https://x.com/rahulgs/status/2068007838442479988
original_url: https://x.com/rahulgs/status/2068007838442479988
author: "rahul"
handle: rahulgs
status_id: 2068007838442479988
captured_at: 2026-06-25T15:11:24+07:00
published_at: "Fri Jun 19 16:27:45 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 24
  reposts: 16
  likes: 681
---

# X post by @rahulgs

## Source

- Original: [https://x.com/rahulgs/status/2068007838442479988](https://x.com/rahulgs/status/2068007838442479988)
- Canonical: [https://x.com/rahulgs/status/2068007838442479988](https://x.com/rahulgs/status/2068007838442479988)
- Author: rahul (@rahulgs)

## Verbatim Text

inspect is now our digital coworker. 75%+ code at ramp now comes from inspect.

what we've invested in:
1. repo setup across every main repo: is every dep installed, every command able to run and is performant, every skill token efficient and installed. are all the tools available - are the unused tools removed? which mcps are bloated? what can we precompute and snapshot in the sandbox fs (mypy, uv deps, bytecode caching, git clone). every additional source of feedback improved the final PR quality: for infra we added terraform plans, for web we added a parallel browser testing agent, for backend we added mypy's new experimental parallel mode, fast enough to run in a sandbox
2. ui polish and closing the loop outside of github - human reviews, ai reviews, diffs, child sessions, stats, fast voice inputs with realtime gpt
3. insane performance obsession (mostly @_dylanga), chasing down every ms across sandbox boot, new prompts, db queries, network round trips
4. try to match or exceed local agent performance across all axes (tools, skills, performance, repo set up)
5. robust api - used for many other automations internally
6. cost optimization: tool bloat, flex api, picking the right model, reasoning level across models
7. making sure prompts are always declarative, and almost never imperative. fix this ✅ implement this feature ✅ use the datadog mcp to fix this ❌ use the db migration skill from this link ❌

it's a moving target but a unending emphasis on speed, defaults, repo setup has allowed us to get as close as we can to "just works" on any knowledge work tasks at ramp - eng, product, data, support, sales, uxr

## Quoted Post

- URL: https://x.com/_dylanga/status/2067999346780524753
- Author: Dylan Garcia (@_dylanga)

Inspect at Scale

Since our [original blog post](https://builders.ramp.com/post/why-we-built-our-background-agent?utm_source=twitter), Inspect's adoption has skyrocketed, the product has matured, and the industry has moved just as fast. What started as an engineer’s tool for writing code is becoming something bigger and so much better.

For some teams, that means going from a feature idea or bug report to a merged PR, reviewed by multiple frontier models and instrumented with monitors and automations that can help catch issues in production.

For others, it means starting with a rough idea and ending with a full web or Slack app, integrated with Snowflake, Slack, Salesforce, Google, Linear, and Notion, all hosted on Ramp’s internal Ramplify platform.

This post is about what we've done to make Inspect work for thousands of daily sessions.

Up next, we will show you how Inspect is evolving from "just" a coding agent into the agentic work environment for the entire software factory at Ramp.

# Inspect by the Numbers

- In the past 6 months, 76.5% of all PRs merged at Ramp were created with Inspect.

- 98.6% of Ramplings in Engineering, Product, Design, and Data have used Inspect at least once, with 58.1% of them creating over 50 sessions per month.

- Over 750 Ramplings use Inspect every day, creating more than 10,000 daily sessions.

# Data, Everywhere

For every Inspect session, we safely extract, sanitize, and store as much signal as we can to power better insights.

With 800k sessions, 30M tool calls, and 100M message parts, we have a rich dataset to learn from. We can identify common access patterns, failure paths, tool rework, and model hallucinations.

That lets us answer questions like: “What are sessions trying to do with our design system’s MCP?” so we can improve it, or “Which tools error the most?” so we can make them more reliable.

# Obsess Over The Experience

The product is the experience. Session data tells us where Inspect is doing well and where it breaks; the work that matters is doubling down on what works and making failures rare before anyone has to ask for help. We obsess over sandboxes, cold starts, and per-repo defaults so using Inspect feels like talking to a coworker who already knows the codebase. Inspect needs to be both powerful _and_ fast.

## Performance

When Inspect feels slow, we want to know exactly where the time went, not guess. Every session is traced end to end: from the first prompt in Slack or the browser, through sandbox boot and repo initialization, down to individual bash commands and tool calls.

Combined with our session data lake, those traces let us find bottlenecks, ship fixes, and verify they actually moved the numbers.

## Rewiring the Sandbox Control Plane

The biggest win in the last few months was rewriting how the Inspect API talks to Modal sandboxes, dubbed Sandboxes V2. The old path routed control commands through a Bun HTTP server running inside each sandbox. It worked, but traces showed it was slow and error-prone, and we spent real effort maintaining it.

We removed the server and replaced it with a direct WebSocket connection through a Cloudflare Durable Object. Start, stop, prompt, and other control messages now flow over the socket instead of bouncing through sandbox-local HTTP. Less connection overhead, less failure surface, fewer moving parts.

The difference showed up immediately in time-to-interactive: sandboxes went from an average of ~6.5 seconds to 2 seconds!

We didn't stop there, and never will. A few other wins stacked on top, with more happening every week:

Smarter compute regions. We fixed an issue where sandboxes were being placed in regions that were far from our users and database, causing unnecessary cross-region round trips.

Faster prompt-to-model. We removed unnecessary work happening in the path from sending a prompt to the model actually starting work, so sessions feel responsive sooner after you hit enter. This removed ~600ms per message.

Faster session fetching. We optimized database queries and loading patterns to make our session UI more responsive and consistent.

## Sandbox Experience

Inspect sessions do not run in a one-size-fits-all container. Every session runs in a sandbox tuned for the repository you are working in. A missing dependency, a slow cold start, or the wrong tool available by default does not just annoy one engineer. It shows up thousands of times a day, and we quickly hear about it.

For every repository we support, we ask the same questions: what commands need to run, what dependencies need to be present, how do we make boot fast, and what tools or MCPs should be available from the first prompt?

The answers differ by repo, and that is the point. In our Python monolith, we prewarm build caches at image creation time so the first real session is not paying for cold-start work. We bake mypy’s incremental cache, prebuilt test databases, and other expensive first-run setup into the image so agents can lint, test, and iterate without waiting on infrastructure. In infra repos, we run `terraform init` during the image build so targeted `terraform plan` is ready when someone asks for it. In microservice repos, we boot with the local stack already running so the agent can hit a live server instead of spending its first ten tool calls figuring out how to start one.

These optimizations, combined with ones discussed further in this post, proved to have a dramatic decrease in our core repository's session times.

We also got deliberate about which tools belong in each environment by default. Some repos need Datadog, Linear, or internal MCPs out of the gate. Others should stay lean until the task actually requires them. The goal is not to load everything everywhere. It is to make the common path feel obvious.

That obsession over per-repo setup is invisible when it works, and painfully obvious when it does not.

## Inspect as a Coworker

Inspect should feel like the coworker who already knows the company: where things live, which team owns what, and how to get started. You bring the problem — a bug report, a screenshot, a vague thread — and Inspect figures out the rest. Sessions start from Slack, the browser, automations, and more. Our goal is to keep the path from that moment to a running session as short as possible, whether you have no idea where to start or you know exactly where the fix lives and just do not want to spend time guiding the agent there.

Slack is where this shows up most. You can @mention Inspect in a thread, or react to a message with the Inspect emoji and let that message become the prompt. We use the reaction path constantly. Someone posts a bug report, a screenshot, or a vague "this feels wrong," and that is often enough to start. The message itself, the surrounding thread, attachments, and even the channel name give us what we need to route the session to the right repository and get the agent moving.

No repo picker, no rewritten spec, no tour of the codebase. Frequently the original message, or a screenshot dropped into the thread, is all it takes.

# Controlling Costs at Scale

As Inspect grew, cost became a product problem, not just an infrastructure problem. We needed Inspect to run more sessions, power more workflows, and support more teams without LLM spend scaling linearly with usage.

## Model Defaults

One of the highest-leverage ways to control cost was improving the Inspect defaults across the board.

We moved Inspect sessions to use GPT-5.5 on medium reasoning by default because it gave us the best balance of quality, speed, and cost. Ramplings can still choose their preferred provider, model, and reasoning level, but the default now works better for the majority of sessions without sending every task to the most expensive settings.

## Automations and Flex Tiers

When we added automations earlier this year, they quickly became a way to turn repeated engineering work into always-on workflows.

Some automations watch production signals from Datadog or Sentry and start investigations the moment something looks wrong. Others monitor Slack, Linear, or code activity to spot patterns, summarize context, route follow-ups, and keep stakeholders aligned.

Adoption grew quickly. In recent weeks, automated sessions grew as much as 30% week over week. It became clear that we could not let frontier-model spend grow at the same rate.

In May 2026, we slowed explosive LLM cost growth and reduced daily spend by roughly 35%. We did it by treating model choice, reasoning level, and service tier as part of the product surface, not as infrastructure defaults or a blanket “use the latest model” policy.

Instead of sending every automation to the most expensive frontier model, at the fastest tier, with the highest reasoning setting, we route each workload to the right execution path. High-priority, user-facing, or latency-sensitive automations can still use the strongest models and fastest routes. Lower-priority background work can run on cheaper models or on the flex tier, where we accept slower completion in exchange for much better unit economics.

Flex is especially useful for the long tail of automation work: recurring checks, summaries, maintenance tasks, background investigations, and follow-ups that need to happen reliably but not instantly.

The result is a system that can absorb more automation volume without spend scaling linearly with usage. We can run more workflows, cover more surfaces, and make Inspect available in more places across Ramp while keeping costs under control.

# Optimizations That Compound

The biggest wins do not always come from one dramatic change. They often come from making the default path cleaner, shorter, and less wasteful across hundreds of thousands of sessions.

## Context Hygiene

We started cutting unnecessary tools and context bloat. Every extra tool description, system instruction, and irrelevant context block gets multiplied across millions of model calls. More context is not always better. Too much of it makes sessions slower, more expensive, and harder for the model to reason through.

We became more deliberate about what the model sees by default: fewer one-off tools, tighter prompts, cleaner context boundaries, and better defaults for the work most sessions are actually trying to do. The goal is simple: give the model what it needs, remove what it does not, and make the common path cheaper and more reliable. We now eagerly load tools and prompts that every session needs, and defer everything else until a task actually requires them.

## Tool Call Optimization

Inspect sessions are tool-heavy. Models constantly search files, read code, run commands, inspect diffs, and call internal systems. Small inefficiencies compound quickly.

One simple example is search. Inspect’s prompt tells models to prefer `rg` over `grep` wherever possible because ripgrep is significantly faster. That may sound small, but models search constantly during coding sessions. Across millions of tool calls, even small latency improvements matter.

In practice, `rg` is about 41% faster at p95 and 80% faster at p99.

This kind of optimization does not reduce the cost of a single token, but it makes sessions shorter, faster, and less wasteful. Better tool choice means fewer retries, less waiting, less duplicated work, and a smoother path from prompt to finished task.

## When Token Savings Backfired

Not every cost-saving attempt worked as cleanly as model routing, flex tiers, or tool optimization.

As Inspect adoption grew, token usage became one of the most important levers to optimize. The question was simple: could we reduce the amount of context we send to models without making sessions worse?

One approach we tested was RTK, a tool that compresses command output before it enters the model’s context. In theory, this was exactly the kind of optimization Inspect should benefit from: agents run tons of shell commands, shell output can be noisy, and compressing it should reduce input tokens.

So we tried it.

For five weeks, we enabled RTK in Inspect’s most-used repositories. It reached roughly 150k sessions, proxied 3.2M shell commands, and reported about 335B input tokens saved. On paper, that translated to around $1M in gross theoretical token savings.

At first, it looked like a huge win. But as we dug deeper, we found a problem.

RTK’s OpenCode integration rewrites tool calls before they execute and proxies them through its binary. That means the model sees the rewritten command, not the original one.

With RTK enabled, the model would ask to run a command and then see a different command executed through `rtk`. It did not know why that happened. That mismatch created confusion: the model would try to bypass the wrapper, adjust flags, escape the command, or retry with a different approach, often multiple times over the course of a session. We were "saving" tokens per command, however ultimately using more of them because commands had to be rerun.

The lesson was that token savings are only useful if they preserve the model’s understanding of the environment. If an optimization makes the agent less predictable, the theoretical savings can disappear into rework.

# What’s Next

All of this has forced us to get serious about the foundations: data, cost, reliability, tool use, model defaults, and the operational details that make agents useful every day.

But those foundations are only the beginning.

Our custom review agents, Review Buddy and Testo, are the first glimpse of what comes next for best-in-class PR reviews and validations. In Review Buddy's beta, it has already reviewed 8,836 PRs in a month. PRs are challenged, checked, and improved by multiple frontier models before it ever reaches production.

We are also bringing Inspect closer to how work actually happens at Ramp: across teams, projects, ownership areas, incidents, planning threads, and long-running initiatives. The goal is for Inspect to understand not just the task in front of it, but the broader context around the work: what a team owns, what a project is trying to accomplish, what decisions have already been made, and what should happen next.

As a final teaser: what happens if we never have to go to GitHub at all?

This is where Inspect is heading. We're taking it from “just” a coding agent to becoming the agentic work environment for the entire software factory at Ramp.

## Capture Note

TweetDetail returned complete normal-post text.
