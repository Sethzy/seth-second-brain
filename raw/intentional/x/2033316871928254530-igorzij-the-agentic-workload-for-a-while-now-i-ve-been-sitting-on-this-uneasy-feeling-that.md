---
type: raw_capture
source_type: x
url: https://x.com/IgorZIJ/status/2033316871928254530
original_url: https://x.com/igorzij/status/2033316871928254530
author: "Igor Zalutski"
handle: IgorZIJ
status_id: 2033316871928254530
captured_at: 2026-06-19T21:44:09+08:00
published_at: "Sun Mar 15 22:58:14 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 4
  reposts: 5
  likes: 9
---

# X post by @IgorZIJ

## Source

- Original: [https://x.com/igorzij/status/2033316871928254530](https://x.com/igorzij/status/2033316871928254530)
- Canonical: [https://x.com/IgorZIJ/status/2033316871928254530](https://x.com/IgorZIJ/status/2033316871928254530)
- Author: Igor Zalutski (@IgorZIJ)

## Verbatim Text

The Agentic Workload

For a while now I’ve been sitting on this uneasy feeling that the code we write when building agents does not fit nicely into any of the existing “kinds” of code that we are used to from the pre-AI era. But I didn’t know why; the only hunch I had was that every time I made another agent, the code that I wrote came out awkward - and it wasn’t Claude’s fault. It took embarrassingly many repetitions of building the same thing over and over again for it to “click”. It feels obvious in hindsight assuming a few plausible priors are true.

# Leading coding agents are CLIs for a reason

Claude Code, Codex, Amp and similar command-line agents are so universally loved because their creators have figured something counterintuitive: for the “right” system design of an agent to become practically useful without disastrous security consequences, most of the existing developer infrastructure needs to be rebuilt for agentic autonomy. You could wait for that to happen - or you could ship something that works today, even if its looks somewhat wrong.

What right design looks like? An agent is basically LLM calls with tools in a loop. It reacts to user input, produces outputs, manages context, and so on. One might naturally design such a thing as a stateless server-side application, running in a container or a serverless function. Tools would be API calls, each tool cleanly abstracting away the internals. On a whiteboard this looks great! Scalability, reliability, all that.

The only problem is this right design doesn’t work. Not because of technical reasons; but because the code that the agent needs to modify doesn’t sit neatly in one github repo waiting to be pulled. It’s not even about the code - it’s about all the countless utilities and services that developers use for building. They are all on their laptops - and no one is going to bother setting up remote development environments just to try this new AI thing.

The wrong design on the other hand solves it beautifully. A CLI meets developers where they are - there’s no need to set up anything else other than installing Claude Code or Codex. If a tool can be used by hand in the terminal, the agent can use it too. This way the actual development environment is fully at harness’s disposal. Also no networking overhead on calling remote services for every step - so it feels snappy, much more so than first-gen cloud-based agents.

# The rise of harness-based agent SDKs

The best coding agents are indeed CLIs - but that does not mean that agentic coding can now only happen on people’s laptops! All sorts of code-generating agents are exploding in popularity, many of which are fully autonomous, or are built for non-technical users. For example apps like Lovable allow anyone to create a fully functional application in a few prompts in the browser; Greptile reviews pull requests for bugs and security; many other agents are built for implementing fixes or entire features in response to Slack mentions or Linear tickets.

All such agents work with code - so if you are building one, which agent framework should you use? Turns out Claude, Codex and other CLI harnesses got so good that if you choose a conventional LLM framework like Langchain or AI SDK you’ll have to put in a lot of work just to match their performance with code, especially on more challenging assignments that might take longer. Anthropic and other coding CLI creators put in a lot of effort into their agents to make them stable in a wide range of coding scenarios; matching that is anything but trivial.

Realising that, people started simply calling Codex or Claude CLIs in their applications - and achieved superior performance compared to a DIY harness. Big labs noticed that pattern, and shipped SDKs that make such usage easier while still relying on the harness CLI under the hood ([Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), [Codex SDK](https://developers.openai.com/codex/sdk/)). Bill Chen from OpenAI [suggests](https://youtu.be/wVl6ZjELpBk?t=712) to “shift your mindset” - stop making direct model calls and treat the harness as the pluggable building block instead.

# So where does my agent live?

Because leading coding agents are CLIs, the most useful SDKs for building coding agents ended up built around those CLIs. So if you are building an agent with Claude Agent SDK, it will shell out to the Claude Code CLI to do its thing. If you are new to building agents but built some web apps or distributed systems before, you might be freaking out - and rightfully so! What do you mean it shells out??? Like, starting another process… on the same host where my application runs? For every request??? Forget scalability or even basic reliability - because it’s going to read and write files also, oh and could also run arbitrary code.

These properties makes the code written with these SDKs much more similar to a CI job in nature than it is to an application. Because every “run” of an agent could potentially overwrite or delete any file if the harness decides so; also its resource consumption profile cannot be known beforehand. But at the same time, it’s clearly an application - an agent might need to respond to user requests, make API calls and so on. However deploying such code to destinations that the application code is traditionally deployed to - like containers or serverless functions - is clearly not a good idea, for the reasons stated above. So what do we do?

# The Agentic Workload

Anthropic wrote a detailed [guide](https://platform.claude.com/docs/en/agent-sdk/hosting) on Agent SDK deployment patterns. Regardless of which pattern you pick for you , you’ll likely end up implementing some of the following in your application:

- creating an ad-hoc sandbox for every agent session (and tracking its lifecycle)

- putting a version of your agent’s code into it

- an always-on gateway service for handling incoming webhooks and requests

- a queue to store incoming messages while the sandbox is being created

Pretty much every agent using Claude Agent SDK or Codex SDK will end up doing something similar, regardless of what the agent does (other than generate some code).

It’s a new type of workload - not a traditional backend service; and not a frontend. This type of workload doesn’t (yet) have an obvious “home” - as in, here are some services I could deploy it to. But that’s strange; because for every piece of code that works locally (and such agents obviously do work locally) there’s typically a range of services they can deployed into. I think this is something that will be solved in near future and we’ll see some new awesome dev platforms emerge.

## Links

- [A thousand ways to sandbox an agent](https://michaellivs.com/blog/sandbox-comparison-2026)

- [The two patterns by which agents connect sandboxes](https://x.com/hwchase17/status/2021261552222158955)

- [Code and Let Live by fly.io](https://fly.io/blog/code-and-let-live/)

## X Article Metadata

- Title: The Agentic Workload
- Preview: For a while now I’ve been sitting on this uneasy feeling that the code we write when building agents does not fit nicely into any of the existing “kinds” of code that we are used to from the pre-AI

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
