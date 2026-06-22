---
type: raw_capture
source_type: x
url: https://x.com/fluixoo/status/2065436839821852945
original_url: https://x.com/fluixoo/status/2065436839821852945
author: "Fluixo"
handle: fluixoo
status_id: 2065436839821852945
captured_at: 2026-06-19T23:58:47+08:00
published_at: "Fri Jun 12 14:11:31 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 1
  likes: 10
---

# X post by @fluixoo

## Source

- Original: [https://x.com/fluixoo/status/2065436839821852945](https://x.com/fluixoo/status/2065436839821852945)
- Canonical: [https://x.com/fluixoo/status/2065436839821852945](https://x.com/fluixoo/status/2065436839821852945)
- Author: Fluixo (@fluixoo)

## Verbatim Text

ONE AI AGENT FAILS. A TEAM OF AGENTS PERFORMS BETTER.

Most people try to build a single, large AI agent.

They try to make it do everything at once:

- research

- writing

- coding

- design

- analytics

- publishing

- verification

- memory

- browser interaction

- API interaction

Then the agent does something strange.

It loses context.
It confuses the task.
It writes a weak draft.
It doesn’t check the facts.
It breaks down the steps.

And people conclude:

“AI agents aren’t ready yet.”

It seems to me that the problem often isn’t with the agents.

The problem is in the architecture.

One agent with a massive task is like hiring a single person and asking them to be a researcher, editor, developer, designer, manager, and reviewer all at once.

Sometimes it works.

But with complex tasks, everything falls apart.

---

## The major shift

You shouldn’t be thinking, “What kind of agent should I create?”

But rather, “What kind of workflow do I need?”

And then break it down into smaller roles.

Not just one Content Agent.

But:

- Research Agent

- Brief Agent

- Writer Agent

- Editor Agent

- Critic Agent

- Publisher Agent

Not just one Coding Agent.

But:

- Planner

- Implementer

- Test Runner

- Security Reviewer

- Browser Checker

- Release Assistant

Each agent performs a small, clear task.

That’s exactly what makes the system more reliable.

---

## Why does one agent lose?

An agent almost always faces three problems.

1. The task is too broad

If we were to say:

```
Build me a full product.
```

The agent must decide for themselves:

- what to build

- where to start

- which files to modify

- how to test

- what constitutes completion

and what risks are involved.

That’s too much freedom.

Freedom seems powerful, but it often leads to chaos.

2. Too many tools

If an agent is given 15 tools, they will use them in unpredictable ways.

It’s better to provide 2–3 tools tailored to a specific task.

The Research Agent gets search/fetch.
The Writer Agent doesn’t get any tools at all.
The Browser Checker gets a browser.
The Security Reviewer gets access to the code and a checklist.

Fewer tools.

More stability.

3. No quality gate

The most dangerous part.

People often pass output on without checking it.

Research is weak, but the Writer writes anyway.
The draft is poor, but the Publisher formats it anyway.
The code is broken, but the deployment proceeds anyway.

In a multi-agent system, there must be a gate between steps:

```
Is this good enough for the next step?
If not, send it back with specific feedback.
```

Without this, the pipeline simply speeds up the errors.

---

## Basic Architecture

I would start with the simplest diagram:

```
Input -> Research -> Brief -> Draft -> Review -> Final
```

This is a sequential pipeline.

It’s boring.

But that’s exactly why it’s good.

You always know:

- where the task is right now

- which agent is working on it

- what output is needed

- where it went wrong

- what needs to be fixed

For my first multi-agent system, I wouldn’t build a complex hierarchy.

You don’t need a CEO Agent, 5 managers, and 20 specialists.

At first, three agents are enough:

1. Research Agent.

2. Writer/Builder Agent.

3. Critic Agent.

And one Orchestrator, who decides when to send the task back.

---

## Research Agent

Research Agent doesn't write articles.

It doesn't draw conclusions.

It doesn't try to sound fancy.

Its job is to compile information in a structured format.

Example output:

```
TOPIC:
ANGLE:
KEY INSIGHTS:
TOOLS:
RISKS:
SOURCES:
OPEN QUESTIONS:
```

This is important.

If the Research Agent starts writing prose, the downstream agents will begin to interpret its style rather than its structure.

It’s better to stick to dry notes.

Then the Writer will generate the text.

---

## Writer or Builder Agent

The second agent does the bulk of the work.

If it’s content, they write a draft.

If it’s code, they handle the implementation.

If it’s a product, they compile the specifications.

The main rule:

They must receive a good brief.

Not just “write an article.”

But:

- topic

- angle

- audience

- structure

- constraints

- style

- what not to do

- what output is needed

A good agent is not a magical worker.

It is a specific role in a normal workflow.

---

## Critic Agent

This is a role that almost everyone underestimates.

A Critic Agent doesn’t have to be polite.

They have to be helpful.

Their job is to:

- find weaknesses

- point out unsourced claims

- check the structure

- catch repetitions

- point out where the logic breaks down

- identify risks

- suggest specific fixes

A bad critic:

```
The text is good, but it could be improved.
```

Normal critic:

```
The main point doesn’t appear until the fourth paragraph.
Move it to the first sentence.

The section on tools is too general.
Add a specific example of a pipeline.

The claim about 5,000 hours seems risky.
Either remove it or specify that it’s the author’s claim.
```

Now that's helpful.

---

## Orchestrator

Orchestrator is a manager.

It shouldn’t do all the work itself.

It should:

- Accept a task

- Break it down into steps

- Assign each step to the right agent

- Check the output

- Send it back for revision if it’s not good

- Compile the final result

If the Orchestrator writes, researches, reviews, and publishes on its own, it turns back into one big agent.

And that’s exactly what we’re trying to avoid.

---

## Where is OpenClaw here?

OpenClaw is interesting as a platform for experimenting with AI agents.

Based on my notes, I have a separate deployment guide:

- Ubuntu server

- Telegram bot token

- OpenClaw gateway

- Google AI via plugin

- Telegram pairing

- health check

- logs

In other words, the idea isn’t just to “talk to the model.”

It’s about setting up an agent gateway, connecting Telegram, and starting to work with the agent as a separate service.

I like this approach.

Because the AI agent isn’t just a browser tab.

It becomes a workflow endpoint.

I sent a message to the bot.
I received a response.
The task went into the pipeline.
There are logs.
There’s a health check.
You can connect more tools.

This is closer to real automation.

---

## But you have to start slowly

I wouldn't start with production automation.

First, you need to put together a small team of agents dedicated to a single task.

For example, a content research team:

```
Topic -> Research Agent -> Brief Agent -> Writer Agent -> Critic Agent -> Final Draft
```

And only then should you make it more complex.

Check:

- where the research is weak

- where the Writer produces generic content

- where the Critic is too lenient

- where the Orchestrator misses errors

- how much a single run costs

- how long it takes

- which outputs need to be logged

Until the pipeline is stable on a simple task, there’s no point in adding 10 new tools.

---

## Five Rules for a Reliable Agent Team

1. Structured outputs

Each agent must return output in a clear format.

Not “whatever works.”

But strictly:

```
SUMMARY:
FINDINGS:
RISKS:
NEXT STEP:
```

Otherwise, the next agent will have to guess every time.

2. Quality gates

Don’t pass on poor output.

If the research is weak, send it back to the researcher.

If the draft is weak, send it back to the writer.

If the code fails the tests, don’t proceed.

3. Minimal tools

Don’t give every agent everything.

Give each agent only what they need for their task.

This reduces chaos.

4. Retry with feedback

If an agent makes a mistake, don’t just run it again.

Provide specific feedback.

Don’t:

```
try again
```

But:

```
Find 3 concrete examples.
Remove generic claims.
Add risks.
Return only structured notes.
```

5. Logs

If there are no logs, you won’t know where things went wrong.

In production, every step should include:

- input

- output

- tools used

- time

- errors

- retry reason

It’s tedious.

But without this, it’s impossible to properly improve the agent system.

---

## Real-world use cases

Content

The Research Agent gathers data.
The Writer drafts the content.
The Editor polishes it.
The Publisher formats it.

B2B Prospecting

The Prospecting Agent identifies companies.
The Research Agent gathers context.
The Personalization Agent crafts the opening line.
The Sequencer Agent handles follow-ups.

Vibe coding

Planner builds a plan.
Coder makes changes.
Test Agent runs tests.
Browser Agent checks the UI.
Security Agent looks for risks.

Obsidian workflow

Inbox Agent sorts through notes.
Linking Agent adds connections.
Content Agent suggests posts.
Review Agent checks the style.

This is what a normal agency system looks like.

Not a single all-powerful agent.

But a small team where everyone does their part.

---

## What I would put together first

I’d start with the content agent team, because that’s closest to my workflow.

Minimal setup:

1. I provide a topic.

2. The Research Agent gathers structured notes.

3. The Brief Agent turns the notes into an outline.

4. The Writer Agent writes X Article.

5. The Critic Agent cuts out generic sections.

6. The Final Agent creates X post + a Telegram version.

7. Everything is saved in Obsidian.

This can already be tested on real articles.

And if it works for content, the same principle can be applied to:

- coding

- marketing

- lead research

- project planning

- Web3 monitoring

- Telegram bots

---

## My conclusion

The future of AI agents does not lie in a single massive agent that does everything.

The future lies in small systems.

Where there are:

- narrow roles

- intuitive tools

- structured outputs

- quality gates

- critic

- logs

- human approval

A single agent with a big task looks impressive in a demo.

But a team of small agents more often wins in real-world work.

Because it’s understandable.

It can be tested.

It can be fixed.

It can be improved one step at a time.

And this is my main mental model:

Don’t build an “AI employee.”

Build a workflow where AI agents handle specific, well-defined tasks.

Follow me @fluixoo for more AI, Web3, and automation content. Hope this was useful.

## X Article Metadata

- Title: ONE AI AGENT FAILS. A TEAM OF AGENTS PERFORMS BETTER.
- Preview: Most people try to build a single, large AI agent.
They try to make it do everything at once:
research
writing
coding
design
analytics
publishing
verification
memory
browser interaction
API

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
