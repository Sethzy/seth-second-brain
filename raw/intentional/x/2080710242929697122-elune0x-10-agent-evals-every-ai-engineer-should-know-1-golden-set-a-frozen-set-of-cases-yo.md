---
type: raw_capture
source_type: x
url: https://x.com/elune0x/status/2080710242929697122
original_url: https://x.com/elune0x/status/2080710242929697122
author: "elune"
handle: elune0x
status_id: 2080710242929697122
captured_at: 2026-07-26T15:15:15+08:00
published_at: "Fri Jul 24 17:42:34 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 29
  reposts: 131
  likes: 1012
---

# X post by @elune0x

## Source

- Original: [https://x.com/elune0x/status/2080710242929697122](https://x.com/elune0x/status/2080710242929697122)
- Canonical: [https://x.com/elune0x/status/2080710242929697122](https://x.com/elune0x/status/2080710242929697122)
- Author: elune (@elune0x)

## Verbatim Text

10 agent evals every AI engineer should know

1) golden set

a frozen set of cases you run after every prompt model or tool change

use it as your baseline to see whether the system improved or quietly broke

OpenAI Evals helps you build repeatable benchmark sets and compare model changes

→ https://t.co/dr1GZlC75R

2) llm as judge

a second model scores open ended answers against a written rubric

use it when there is no exact output to compare against

OpenEvals provides ready made evaluators for LLM applications

→ https://t.co/S2yhnByFIP

3) rubric scoring

score correctness tone safety and cost separately

one quality number hides the problem

DeepEval helps you create custom metrics and score every dimension independently

→ https://t.co/q9Z6Xmixia

4) trajectory eval

grade the path the agent took

not only the final answer

AgentEvals checks agent actions decisions and tool calls across the full trajectory

→ https://t.co/0oziAl54az

5) tool unit tests

test every tool with fixed inputs and outputs

no model in the loop

MCP Inspector helps you inspect and test MCP servers tools and responses separately

→ https://t.co/IVmt5qpWIN

6) regression suite

replay previous runs against every new prompt model or toolset

then compare the results

Promptfoo helps you run repeatable eval suites catch regressions and add checks to CI

→ https://t.co/zxi2PuWuhe

7) a b in prod

split real traffic between two versions and compare actual outcomes

GrowthBook provides feature flags controlled experiments and product analytics

→ https://t.co/DGlE3JjDD3

8) human review

sample real runs and let a person grade them honestly

use it to calibrate your automated judge

Argilla helps teams collect human feedback review outputs and build better datasets

→ https://t.co/QHWb7skWjr

9) shadow run

let the candidate run on real traffic while its output is shown to nobody

use it before a risky rollout

Langfuse helps you trace production runs compare candidates and monitor eval results

→ https://t.co/IrhDf38tRn

10) red team

attack the system before somebody else does

jailbreaks prompt injection data leaks and tool abuse

Garak scans LLM systems for vulnerabilities and unsafe behavior

→ https://t.co/w8ObyW4ZKv

offline evals tell you it works

online evals tell you it still works

you probably do not need all ten today

start with the two that would have caught your last outage

bookmark this

## Quoted Post

- URL: https://x.com/elune0x/status/2079923329633313196
- Author: elune (@elune0x)

Loop Engineering: How to Build Agents That Improve Their Own Work

# From manual prompting to engineered loops

Most people still operate AI agents by hand

They enter one task

Wait for one response

Review the result themselves

Correct the mistakes themselves

Then send another prompt

The human is still doing the looping

The next stage looks different

You stop prompting the agent step by step

You build a loop around it

The loop gives instructions

Checks the output

Chooses the next action

And keeps running until the result meets the standard

That is loop engineering

The idea is simple

Stop spending your time prompting agents manually

Start designing the systems that prompt them for you

> "You should not be prompting coding agents anymore You should be designing loops that prompt your agents"

Boris Cherny leads Claude Code at Anthropic

He described the same shift through his own workflow:

> "I do not prompt Claude anymore I have loops running that prompt Claude and figure out what to do My job is to write loops"

---

# Why most people still do not build real loops

Loops sound incredible until you see the token bill

A normal agent loop can consume context extremely fast:

- A medium-sized coding loop can use 50K-200K tokens

- A fleet with an orchestrator and specialists can use 500K-2M tokens

- A loop scheduled to run daily can consume millions of tokens every week

Every retry costs tokens

Every correction costs tokens

Every verification step costs tokens

Every subagent adds another bill

That is the hidden limitation people rarely discuss

Loop engineering is not difficult because the concept is hard to understand

It is difficult because most users cannot afford unlimited agent runs

The obvious response is:

> "Easy for you to say, you have unlimited OpenAI access"

And that criticism is fair

This is why cheap models with large context windows matter so much

To run useful loops every day, you need:

- Affordable input tokens

- Affordable output tokens

- Large context windows

- Reliable tool calling

- Structured JSON output

- High concurrency

- Enough context to remember earlier steps

Without those things, loops remain expensive experiments

With them, loops become practical systems that can run real work

---

# The old workflow vs the new workflow

For the last two years, most people have used agents like this:

You prompt

The agent responds

You review the answer

You notice a problem

You prompt again

It works, but it does not scale

The old workflow:

- You write the prompt

- The agent creates an output

- You inspect the output

- You repair the weak parts

- You manually repeat the process

The new workflow:

- You define the outcome

- The loop discovers what is required

- The loop creates a plan

- The agent executes the work

- A checker evaluates the result

- The loop corrects failures

- The system stops when the goal is complete

A prompt gives an agent a single instruction

A loop gives the agent an entire job

---

# What loop engineering actually means

Loop engineering means building repeatable feedback cycles around AI agents

The objective is straightforward:

Move from an initial attempt to a verified result

Without a human controlling every step

The basic loop contains five stages:

1. Discover

2. Plan

3. Execute

4. Verify

5. Iterate

If the result passes the check, ship it

If the result fails, return it to the loop

That is the entire concept

You are not trying to write one flawless prompt

You are creating a system

One that improves imperfect outputs until they meet the requirement

---

# Single-agent loops

Loops generally come in two sizes

The smaller version uses one agent to complete the whole cycle

It discovers what needs to happen

Plans the work

Performs the task

Reviews the result

And tries again when something fails

It is similar to one person editing their own draft until it is ready

Single-agent loops work well for:

- Focused tasks

- Limited scopes

- Clear goals

- Content drafts

- Bug fixes

- Research summaries

One agent

One feedback cycle

Continuous self-improvement

---

# Fleet loops

A fleet loop operates at a larger scale

One orchestrator receives the main objective

It divides the objective into smaller pieces

Those pieces are assigned to specialist agents

Each specialist can also delegate narrow tasks to smaller subagents

Example:

```
Goal: Build a productivity app

Orchestrator owns the mission
        ↓              ↓              ↓
    Research       Engineering        QA
    Specialist     Specialist         Specialist
        ↓              ↓              ↓
 Web Researcher   Code Writer      Test Writer
                  + Debugger       + Bug Tracker
```

This is no longer one agent working by itself

It is closer to a small autonomous team running a project from beginning to end

---

# Open loops vs closed loops

This is the most important practical difference

Not every loop works the same way

## Open loops

Open loops are exploratory

You provide a broad goal and allow the agent to discover its own path

The agent may discover useful things you never specified

But it can also become expensive and chaotic

Open loops can:

- Explore too many directions

- Waste large amounts of tokens

- Generate low-quality work at high speed

- Drift away from the actual objective

- Become difficult to control

Open loops are exciting

But they are usually not the best starting point

## Closed loops

Closed loops have clear boundaries

The human defines the path first

The loop still operates independently, but it stays inside explicit rules

A closed loop includes:

- A clear objective

- Defined stages

- Evaluation after every stage

- A stop condition

- A human handoff if the system gets stuck

This is the version that creates value today

It costs less

It is easier to trust

It produces cleaner results

Start with closed loops

Make them more open only after your checks are strong enough

---

# The 6 building blocks of an effective loop

Every loop follows the same five-stage cycle conceptually

In practice, six building blocks make that cycle useful

## 1 Automations

Automation is the heartbeat of the loop

It starts the process without requiring you to remember to launch it manually

Examples:

- Run every morning

- Run whenever a PR opens

- Run after a file changes

- Run when a new ticket appears

- Continue until every test passes

If you still start every action yourself, the loop is not doing enough

## 2 Worktrees

Worktrees become important when several agents edit code at the same time

Without isolation, agents collide

Two agents may change the same file

One agent may overwrite another agent's work

A worktree gives every agent a separate workspace and branch

That lets multiple agents work in parallel

Without turning the repository into a mess

## 3 Skills

Skills store reusable knowledge about the project

Stop explaining the same context during every run

Write the important information once

Let every future loop reuse it

Useful skill files can contain:

- Product vision

- Architecture

- Project rules

- Build instructions

- Testing instructions

- Actions the agent must never take

Without skills, every loop begins from a cold start

With skills, every run begins with knowledge accumulated from earlier work

## 4 Plugins and connectors

A loop that can only read local files has limited value

Connectors allow it to interact with the tools where your real work happens

Examples:

- GitHub

- Slack

- Linear

- Jira

- Gmail

- Google Drive

- Databases

- Staging APIs

This is the difference between:

"Here is a possible fix"

And:

"I opened the PR and connected it to the ticket"

"Then I monitored CI and posted the final update"

## 5 Subagents

The maker and the checker should not always be the same agent

An agent that wrote the code may be too forgiving when reviewing it

An agent that drafted an article may overlook the same weak sections twice

Use separate agents for:

- Exploration

- Implementation

- Review

- Testing

- Fact-checking

- Final summaries

Quality improves when the reviewer is independent

The creator should not be the only one checking the work

## 6 Memory

Memory allows the loop to continue across multiple runs

The model forgets

The repository does not

The notes do not

The project log does not

Memory can be stored in:

- Markdown files

- Project logs

- Linear tickets

- GitHub issues

- Obsidian vaults

- Databases

- Claude Projects

A long-running loop must remember what has already been attempted

What worked

What failed

And what still needs to be completed

Without persistent memory, the loop starts from zero every time

---

# Real examples of loops

These workflows make the idea concrete

## Coding loop

```
Read VISIONmd + ARCHITECTUREmd
↓
Plan the next change
↓
Edit the code
↓
Run the tests
↓
If tests fail → inspect the error → fix → test again
↓
If tests pass → summarize the changes
↓
Stop
```

A human does not need to drive every stage

The agent writes, tests, corrects, and verifies its own work

## Research loop

```
Define the research question
↓
Find relevant sources
↓
Summarize the evidence
↓
Verify every claim against the sources
↓
Compare conflicting information
↓
Create the final synthesis
↓
Stop when the confidence threshold is reached
```

This produces a much stronger result than asking for one quick summary

## Content loop

```
Define the topic + audience + objective
↓
Create the first draft
↓
Send it to a critique agent
↓
Rewrite using the critique
↓
Score it against the success criteria
↓
If it passes → publish
↓
If it fails → rewrite again
```

The loop turns one idea into a repeatable content system

## Sales outreach loop

```
Define the ICP
↓
Find leads that match the profile
↓
Enrich each lead with company data
↓
Qualify them against the criteria
↓
Personalize the message
↓
Run a quality review
↓
Send or escalate to a human
```

Every example uses the same skeleton:

Goal

Action

Check

Fix

Repeat until the job is complete

---

# Prompt engineer vs loop engineer

This is the new skill gap opening in 2026

## Prompt engineer

A prompt engineer concentrates on better instructions

They improve the wording

They produce a stronger single response

But after the agent finishes, a human still has to review everything

The human remains the feedback loop

## Loop engineer

A loop engineer builds the feedback system itself

They determine:

- What launches the loop

- What context the agent receives

- Which tools it can access

- What qualifies as success

- Who verifies the result

- When the process must stop

- Where the final output is stored

A prompt engineer says:

"Write a function for me"

A loop engineer says:

"Write the function"

"Test it and fix it until every test passes"

"Then summarize the change"

The tools may be identical

The mindset is completely different

The highest-leverage AI builders are moving beyond better instructions

They are creating systems that discover and plan

Execute and verify

Then stop at the correct moment

---

# The short version

Loop engineering is the move from manual prompts to automated feedback cycles

The shift:

- Old way: Give an agent one task at a time

- New way: Build a loop that manages the complete cycle

The 6 things you build:

- Automations: Start the loop automatically

- Worktrees: Let agents work in parallel without file conflicts

- Skills: Reuse project knowledge in every run

- Plugins and connectors: Give the loop access to real tools

- Subagents: Separate makers from reviewers

- Memory: Preserve knowledge between runs

The 2 sizes:

- Single-agent loop: One agent repeatedly improves its own work

- Fleet loop: An orchestrator coordinates specialists and subagents

The 2 types:

- Open loop: Flexible, exploratory, and expensive

- Closed loop: Bounded, reliable, and affordable

The 5 stages:

1. Discover

2. Plan

3. Execute

4. Verify

5. Iterate

The real cost problem:

- Loops consume tokens quickly

- Cheap long-context models make them practical

- Without affordable tokens, most users never move beyond experiments

The mindset change:

- Prompt engineers request outputs from AI

- Loop engineers build systems that deliver verified outcomes

That is the real unlock

Stop searching for one perfect prompt

Build a loop that keeps making imperfect outputs better

A dependable loop will beat a perfect prompt

---

# If you read this far

Follow @elune0x and bookmark this article

Come back to it when you're ready to build your own loops

## Media

- video: https://pbs.twimg.com/amplify_video_thumb/2080659759661768704/img/IAlO9I16I4KjI8xD.jpg
- video: https://video.twimg.com/amplify_video/2080659759661768704/vid/avc1/992x1404/yqo32pBSqJgEcNSX.mp4?tag=29

## Capture Note

TweetDetail returned complete normal-post text.
