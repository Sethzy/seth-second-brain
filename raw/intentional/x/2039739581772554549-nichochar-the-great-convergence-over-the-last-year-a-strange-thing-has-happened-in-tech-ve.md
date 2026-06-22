---
type: raw_capture
source_type: x
url: https://x.com/nichochar/status/2039739581772554549
original_url: https://x.com/nichochar/status/2039739581772554549
author: "Nicholas Charriere"
handle: nichochar
status_id: 2039739581772554549
captured_at: 2026-06-12T21:20:01+08:00
published_at: "Thu Apr 02 16:19:47 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 25
  reposts: 68
  likes: 612
---

# X post by @nichochar

## Source

- Original: [https://x.com/nichochar/status/2039739581772554549](https://x.com/nichochar/status/2039739581772554549)
- Canonical: [https://x.com/nichochar/status/2039739581772554549](https://x.com/nichochar/status/2039739581772554549)
- Author: Nicholas Charriere (@nichochar)

## Verbatim Text

The Great Convergence

Over the last year, a strange thing has happened in tech: very different companies have started moving towards the same product shape, and it feels like everyone is building the same thing.

Linear [announced](https://linear.app/next) last week that they're building coding agents. OpenAI is [deprecating Sora](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation) and focusing entirely on Codex. Anthropic is obviously all-in on claude code and cowork. Notion is building agents for work. So are Google, Microsoft, Meta (Manus), Lovable, Retool and many others.

These companies have different histories, customers and product categories, but they're starting to converge on the same idea: software that can take a goal, use tools, and do work on your behalf.

This convergence is not hard to explain: the market is enormous. This is so much more than a new feature. The prize is enterprise knowledge work.

## What changed

The important shift is not just that models got better (although that's a major part of it working), it's the invention of the general harness.

Claude Code was a massive breakthrough. Although initially invented for coding use cases, it turns out that a smart looping agent generalizes incredibly well towards any computer based task if you give it the right tools. (claude code -> claude cowork)

So this new technique emerges and turns out to be a general problem solving machine. It also scales on a very unique dimension: it can keep running for a long time (autonomy level is theoretically a configuration of the system).

This is the holy grail of software: a conceptually simple system that can solve many problems.

It takes the shape of a model harness + a goal + a set of tools. It runs in a loop calling tools until it stops and produces a result.

I'm simplifying a little and there is a lot of execution craft in doing these things well, but if you build this and then throw tokens at it there seems to be very little theoretical ceiling to what it can achieve. More tools, more tokens, more greedy approaches all seem to scale, and models will only ever get better from this point out.

In the last couple of years, it has become evident that LLMs are incredible at writing code. They're so good that coding is the current best assumed path to AGI. And these harnesses as well as their tools are all just code.

Because the harness + model = code + intelligence, they have the ability to reflect and improve themselves over time. Andrej Karpathy went viral with this idea in his recent prototype AutoResearch:

[Embedded Tweet: https://x.com/i/status/2030371219518931079]

## The opportunity

The prize is not one more AI feature; it's automating enterprise knowledge work. If you can sell this to other companies, you're selling labor itself. There is probably no ceiling to the demand.

This is such a large opportunity that it makes "personal AI use cases", the B2C motions like Sora or chatGPT, seem trivial. In this light, it makes perfect sense for openAI to [refocus away from B2C](https://www.wired.com/story/openai-shuts-down-sora-ipo-ai-superapp/) towards enterprise use cases. Everyone should and probably will, it's the economically rational thing to do.

## Continuous Learning

When I was working on self-driving cars at Cruise, the vision was the concept of a “Continuously Learning Machine” (CLM). The goal was to have the cars drive around, gather experience and then improve, and it guided all of engineering’s efforts.

This was of course never quite achieved, there were always humans in the loop. It was nonetheless a very useful north star: over time humans steered less, and they did so only in the highest leverage areas (tough labeling, model tuning, deploy decision).

We massively compressed the feedback cycle, and in the 4 years I was there we went from deploying new models on the car ~quarterly to ~weekly. That pace of iteration was incredible and led Cruise to deploying autonomous vehicles first in SF, ahead of Waymo.

This idea of continuous learning is about to spread everywhere in these agentic products. Building software factories that are as autonomous as possible is happening everywhere. Just like the CLM, humans will always be somewhat involved[1][2].

The competition will be across this new dimension of where your product places itself against the autonomy slider.

At Cruise, the feedback loop was drive -> collect data -> retrain the model -> deploy. For LLM agents, the loop is run -> monitor -> improve the harness code and context engineering -> run again. The difference is that the agent itself can close this loop. It can reflect on its own performance and use its coding ability to implement better approaches.

Stanford Researcher @yoonholeee recently announced exactly this idea, that he coins as "Meta-Harness":

[Embedded Tweet: https://x.com/i/status/2038640635482456118]

## The app layer convergence

The pattern is everywhere:

- new agent in the calendar app

- new agent in the travel booking app

- new agent in the house listing website

- new agent in the maps app

- new agent in the email client

- ...

All of these just use a harness looping agent architecture with the right tools and context management.

Many teams are adding agents to their offerings, and by doing so they're building agent harnesses. After going through this, they immediately feel how generalizable they are and unlock the common vision.

Whether you're a system of record, a productivity tool or a communication platform, you have a very strong motive and now the capability to build an agent platform for knowledge work.

In the past, different app layer companies owned different parts of the knowledge work value chain. They produced a lot of value around one specific workflow or problem. Notion was optimized for text knowledge and simple databases, Zapier helped connecting APIs into workflows, Microsoft produced an office suite helping knowledge workers work with documents or spreadsheets.

Systems-of-record companies (Salesforce, Notion) are pulled here because they already own the data, the workflow and have deep penetration with other enterprises. All they have to do is productize the harness, connect it to that data, and package it as a generalist productivity solution.

Model companies (@AnthropicAI , @OpenAI ) are pulled here because they own the intelligence layer and the cost curve. But the model layer is very competitive, commoditizing fast and doesn't have great margins. They are naturally moving up the stack into applications, and the killer application is the general harness.

Communication platform companies (Slack, Meta, Teams) are pulled here because agents need to communicate (with each other and with humans) and they've solved this problem already. They are the natural home for managing agents in a hybrid agent/human world.

Finally, some companies already do multiple of these things (Microsoft, Google) so have compounding reasons to build a vertically integrated solution.

Ultimately every business wants to solve as many problems for the customer as they can within their scope of expertise. With this new technology, they can zoom out and focus on solving outcomes rather than tasks.

The vision is to give an outcome (a KPI or other long horizon business goal) to an agentic system which will then proceed to become a software factory, building itself and self-improving towards that outcome over a long period of time.

Everyone is converging: they are building self-improving agents which do knowledge work.

## The infrastructure convergence

Infrastructure serves the application layer, so the convergence follows.

Given the size of the agent application layer demand, I expect all infra companies to reposition as "infrastructure for agents".

Databricks, Vercel, Cloudflare, AWS, Supabase, all of them. The opportunity is incredibly large and it's pretty horizontal. You won't need to build 200 separate optimal services like AWS. By providing the basic building blocks (sandboxes, virtual computers for computer use, storage, file-systems, version control), you can cover a massive market.

In order to build the self-improving agent we discussed above, you need the following blocks:

- Sandbox for writing and executing code

- Computer use infra to enable the agent to use the web (not well solved today)

- Monitoring (spans, traces, and eval tooling)

- Orchestration infrastructure

You still need the classic building blocks, I'm focusing here on agent specific requirements.

The infrastructure convergence is that companies want to own the full loop: monitoring and traces, sandboxes and computers agents use, agent orchestration, and coding environments.

There are obvious advantages in serving the entire infrastructure needs of the agent lifecycle. Both in how deeply you can integrate things together (which leads to a better feedback loop for improvement) and for economical and practical reasons (it's easier to buy from one vendor than multiple vendors).

Once you have all of these pieces, you can build long running, heavily monitored agents performing long-horizon and economically viable tasks. You use the feedback from the final result + all of the monitoring into the next run and ask the agent to improve itself. It writes code and manipulates its own context using the scientific method "observation, hypothesis, experiment", and it keeps going.

## Prediction

My prediction is simple: by the end of 2026, many software companies will look like they are selling the same thing.

That is the great convergence: app companies, model companies, and infrastructure companies are all starting to build towards the same thing.

It's not because the industry lost imagination, but because the architecture and economics are pushing everyone towards the same destination: self-improving software systems that can take a goal, use tools, and produce business outcomes.

The harness explains the convergence. The self-improvement explains the acceleration. Once agents can be monitored, evaluated, orchestrated and improved by changing their own code and context, the companies that own more of that loop will improve faster and their progress will compound.

The winners will not just have better models. They will have distribution, trusted workflow positioning, proprietary context, and the shortest path from observation to improvement.

---

[1] Notion recently counter positioned for humans to be part of things: Think Together https://x.com/ivanhzhao/status/2038670159259619644

[2] Elon famously [admitted](https://www.businessinsider.com/elon-musk-says-model-3-production-mistake-was-using-robots-2018-4) that he tried to over-automate the Tesla factories and learned the lesson that some things should be done by humans

## X Article Metadata

- Title: The Great Convergence
- Preview: Over the last year, a strange thing has happened in tech: very different companies have started moving towards the same product shape, and it feels like everyone is building the same thing.
Linear

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
