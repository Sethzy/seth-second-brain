---
type: raw_capture
source_type: x
url: https://x.com/alokbishoyi97/status/2059610305408462898
original_url: https://x.com/alokbishoyi97/status/2059610305408462898
author: "Alok Bishoyi"
handle: alokbishoyi97
status_id: 2059610305408462898
captured_at: 2026-06-10T23:45:52+08:00
published_at: "Wed May 27 12:18:57 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 21
  reposts: 90
  likes: 961
---

# X post by @alokbishoyi97

## Source

- Original: [https://x.com/alokbishoyi97/status/2059610305408462898](https://x.com/alokbishoyi97/status/2059610305408462898)
- Canonical: [https://x.com/alokbishoyi97/status/2059610305408462898](https://x.com/alokbishoyi97/status/2059610305408462898)
- Author: Alok Bishoyi (@alokbishoyi97)

## Verbatim Text

Using Autoresearch to improve harness skills ( with detailed example run )

## self-improving agents are here

The most interesting shift in AI right now is that agents are now improving themselves. You point one at a problem, leave it alone, and come back to find it has run experiments on its own behavior, kept what worked, discarded what didn't, and produced a version of itself that scores meaningfully higher on the task you cared about. The underlying model never changed. The wrapper around it did.

## what's actually changing

The thing being optimized is the layer between you and the model. Most agent harnesses now expose some of their capabilities as a Skill. a Skill is a markdown file with a short description (of when this Skill is relevant) and a body (what the agent should do once it's loaded).

Claude Code has Skills. Codex has them. Cursor exposes a similar surface. so does OpenClaw and a handful of other harnesses. The implementation details differ, but the idea is the same: the agent's procedure for a class of tasks is a plain markdown file. Anyone - including another agent  - can read it, edit it, and ship a new version.

This is what makes self-improvement tractable. The parameter space isn't model weights, which require a training run, a GPU cluster, and a labeled dataset. The parameter space is markdown in this case. An LLM can write markdown. Another LLM can grade it.

we used a Claude Code harness and Claude Skills in the run below, but nothing about the approach is Claude-specific. Point the same loop at a Codex skill or a Cursor agent definition and you get the same machine.

## what evo is

evo is the loop.

You give it a codebase, a definition of "better", and a budget. It sets up a benchmark (or uses one you already have), generates hypotheses about what to change, runs each hypothesis in its own isolated workspace, scores the result, and keeps a tree of attempts.

The branches that score higher get extended. The branches that don't get pruned. An auditor checks each accepted change for cheating - verifying the optimizer isn't smuggling test answers into the parameter file.

Three things make evo different from a single greedy hill-climb thats typical in autoresearch implementations :

- parallel exploration - Multiple agents run at the same time, each in its own sandbox, each trying a different hypothesis. They don't have to wait their turn.

- tree search, not linear - evo doesn't only keep the single highest-scoring branch. It keeps branches that win on different slices of the task - specialists alongside generalists. When those specialists can be merged, the result is usually better than either parent alone.

- gates - any pass/fail check you can write (a regression test, a held-out slice, a no-cheating audit) is a gate. An experiment that fails a gate gets discarded even if its score is the best so far. Without gates, optimization loops find ways to game the metric.

evo is open source. We use it ourselves. It's also the engine underneath the autoresearch platform that we are launching ( details below )

## how you use evo

setup is two commands:

```bash
uv tool install evo-hq-cli  # the optimizer
evo install claude-code # wires them together
```

that's the full install. swap claude-code for codex, cursor, openclaw, hermes, pi or whichever host you already use.

then two commands run the loop.

/evo:discover : is the one-time setup. You point it at a codebase and tell it what you want better. It explores the repo, figures out a benchmark (or instruments one if none exists), proposes the optimization target, and registers any gates that should run on every experiment.

/evo:optimize is the loop. It orchestrates agent runs in parallel, the per-agent budget, and the stopping condition (usually: stop when N consecutive rounds produce no improvement)

From user's POV that's it. The dashboard streams scores and traces as experiments complete. You can leave it running for an hour or a week.When it's done, you get back the parameter file (Skill, prompt, config, whatever the target was) that scored highest, plus the full record of every hypothesis it tried

It works on Claude Code, Codex, Cursor, OpenClaw, and a few others. Runs locally by default; you can swap to a cloud sandbox provider if you want experiments running in parallel without burning your laptop.

## what we did

To make this concrete we pointed evo at a hard benchmark ( SealQA  )and let it run. The target was a public set of 20 fact-seeking questions where the obvious search results disagree, and the right answer takes some reasoning to extract. The kind of question where a vanilla agent confidently answers wrong: "which country joined the EU most recently that also borders Russia" - the joint condition trips up most single-shot searches. "how many active volcanoes are currently erupting" - the answer depends on whether you mean today, this month, or this year, and the top sources disagree.

Baseline: Claude Code with web search, no custom Skills. 5/20 right

We set evo loose on the `.claude/skills/` directory. 50 experiments later, ending state: one 145-line Skill file with five trigger-gated sub-protocols, one for each question shape evo discovered the agent was systematically getting wrong.

Score: 11/20. More than doubled.

The underlying model did not change. The loop produced the wrapper.

## why this matters

here is the how we model the leverage of an agentic system :

> model capability × good harness × tight verification loops

Until recently only the first factor moved on a regular cadence. New model, new behavior.  Now the other two factors are moving too. and they're moving on a schedule you control, against an objective you defined, in a parameter space that anyone can update. And these are optimized against your benchmark, over your dataset

This is what i mean when i say AI's 4-minute mile is here. The breakthrough isn't a bigger model. It's a tighter loop around the one we already have.

We are building the [evo platform ](https://evo-hq.com)to make this loop available to anyone, not just teams who can build the orchestration themselves.

You define what "better" means for your AI. You point the platform at your repo, your agent stack, or your Skills directory. It builds the harness, runs the experiments in parallel, scores them honestly, and returns the version that scored highest along with the full audit trail of how it got there.

The longer arc is continuous tuning. Users don't actually want a one-time autoresearch run -  they want their systems to stay tuned as the problem drifts, as the model updates, as new failure modes appear. The goal is for the loop to run 24/7, watching the benchmark and keeping the configuration current. Systems, code, agents, Skills, models -  anything where "better" has a definition.

The full record of the SealQA run - every experiment, the final Skill, every hypothesis evo tried, the live dashboard - [is here](https://evo-hq.com/shared/x/9k3b8t2qhr/) . So is the way to register if you want this loop running on something of yours.

## X Article Metadata

- Title: Using Autoresearch to improve harness skills ( with detailed example run )
- Preview: self-improving agents are here
The most interesting shift in AI right now is that agents are now improving themselves. You point one at a problem, leave it alone, and come back to find it has run

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
