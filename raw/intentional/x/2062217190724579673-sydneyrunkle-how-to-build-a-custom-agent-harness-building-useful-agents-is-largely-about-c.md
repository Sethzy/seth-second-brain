---
type: raw_capture
source_type: x
url: https://x.com/sydneyrunkle/status/2062217190724579673
original_url: https://x.com/sydneyrunkle/status/2062217190724579673
author: "Sydney Runkle"
handle: sydneyrunkle
status_id: 2062217190724579673
captured_at: 2026-06-12T21:20:09+08:00
published_at: "Wed Jun 03 16:57:47 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 12
  reposts: 89
  likes: 612
---

# X post by @sydneyrunkle

## Source

- Original: [https://x.com/sydneyrunkle/status/2062217190724579673](https://x.com/sydneyrunkle/status/2062217190724579673)
- Canonical: [https://x.com/sydneyrunkle/status/2062217190724579673](https://x.com/sydneyrunkle/status/2062217190724579673)
- Author: Sydney Runkle (@sydneyrunkle)

## Verbatim Text

How to Build a Custom Agent Harness

Building useful agents is largely about customization: connecting your agent to the right context, data, and environment(s) for the task at hand.

At its core, an agent is a model calling tools in a loop until it completes a task and returns a result:

You can also define an agent as:

> agent = model + harness

The harness is the scaffolding around the model that connects it to the real world.

The remainder of this post assumes the following:

1. An agent is only as good as the context provided to the model

2. The job of a harness is to provide context to the model at every step

So, to build a useful agent, you need a harness that’s great at delivering the right context for the given task to the model.

# The base harness

create_agent is LangChain's primitive for building a harness. Pass in a model, tools, and a system prompt, and you have a working agent:

```python
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=tools,
    system_prompt="you are a helpful assistant..."
)
```

Harnesses like [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) and the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) come pre-assembled with an opinionated middleware (explained below) stack: memory, context management, sandboxing, and more. They're designed to get you to a production-ready agent fast, and they work well for most cases. But many agents need finer grained customization than these harnesses support: custom prompting, business logic, guardrails, etc.

`create_agent` takes a different approach: it’s purposefully minimalistic. Our philosophy is similar to that of [Pi](https://pi.dev/), a highly configurable coding agent harness. create_agent just implements the core agent loop, and it exposes middleware as a primitive for customization.

# Middleware: how you customize the harness

Middleware hooks into the agent loop at each step: before and after model calls, before and after tool calls, at agent startup and teardown. Each piece handles one concern and composes freely with any other:

Middleware allows you to add capabilities to your agent via a few levers that often work together:

Deterministic Logic. Business logic, policy enforcement, dynamic agent control — anything that needs to fire at a specific point in the loop. This includes runtime control over the agent itself: swapping the model based on task complexity, adjusting the prompt, and updating the agent’s message history (during compaction, for example). The right place for anything that can't (or shouldn't) live in a prompt.

Tools. Rather than registering tools directly on the agent, middleware can handle the full lifecycle — setup, teardown, registration — and hand the agent a clean set of tools to work with. This matters when tools have dependencies, require initialization, or need to be torn down cleanly at the end of a run. It also keeps tool configuration close to the logic that governs it, rather than scattered across the agent definition.

Custom state. If your middleware needs to track state across hooks, middleware can extend the agent’s state with custom properties. This enables middleware to track state throughout execution (maintain counters, flags, or other values that persist throughout agent runs) and share data between hooks.

Stream handlers. Middleware can intercept and transform the agent's output stream — filtering events, injecting metadata, routing different event types to different consumers. Useful when different parts of your stack need to react to different things the agent does: a UI consuming token deltas, an audit log capturing tool calls, a monitoring system tracking latency.

The beauty of middleware is that it:

1. Enables customization at any point in the agent loop

2. Bundles related logic in composable, sharable units of code

LangChain ships [prebuilt middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in) for the most common patterns. Anything bespoke to your use case is one [custom middleware](https://docs.langchain.com/oss/python/langchain/middleware/custom) away. Because each piece is isolated, the same middleware can be reused across every agent in an organization so that new agents inherit battle-tested behavior without rebuilding it.

# Harness capabilities

The job of a harness is to get the model the right context at the right time for the given task.

The table below maps common capabilities to middleware that support them. Most production agents end up using several together, depending on the agent’s needs (is it long running? how complex are the tasks? how sensitive are the agent’s actions?, etc):

See the full list of prebuilt middleware [here](https://docs.langchain.com/oss/python/langchain/middleware/built-in).

# Task-harness fit

Task-harness fit is how well your harness matches the actual demands of the task: the context it needs, the failures it'll encounter, the policies it must enforce, the environment it operates in. A harness for a customer service agent looks very different from one built for a long-running coding agent.

Every agent we build at LangChain, including our [GTM agent](https://www.langchain.com/blog/how-we-built-langchains-gtm-agent), [asynchronous coding agent](https://github.com/langchain-ai/open-swe), and our [no-code agent builder](https://www.langchain.com/langsmith/fleet), is built on create_agent with a middleware stack tailored to that agent’s mission.

The best agents aren't just built with capable models, they're built with harnesses that tightly fit the task. The easiest way to build a custom harness is with create_agent.

# References

## Get Started

- [Quickstart: build your first agent with create_agent](https://docs.langchain.com/oss/python/langchain/quickstart)

- [create_agent guide](https://docs.langchain.com/oss/python/langchain/agents)

- [Middleware reference](https://docs.langchain.com/oss/python/langchain/middleware/built-in)

- [Custom middleware guide](https://docs.langchain.com/oss/python/langchain/middleware/custom)

- [Deep Agents: a production harness built on create_agent](https://docs.langchain.com/oss/python/deepagents/overview)

## Acknowledgements

Thanks to @hwchase17, @huntlovell, @masondrxy, and @Vtrivedy10  for their thoughtful review and feedback.

## X Article Metadata

- Title: How to Build a Custom Agent Harness
- Preview: Building useful agents is largely about customization: connecting your agent to the right context, data, and environment(s) for the task at hand.
At its core, an agent is a model calling tools in a

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
