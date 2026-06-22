---
type: raw_capture
source_type: x
url: https://x.com/ryancarson/status/2020931274219594107
original_url: https://x.com/ryancarson/status/2020931274219594107
author: "Ryan Carson"
handle: ryancarson
status_id: 2020931274219594107
captured_at: 2026-06-19T20:17:24+08:00
published_at: "Mon Feb 09 18:42:17 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 113
  reposts: 111
  likes: 1322
---

# X post by @ryancarson

## Source

- Original: [https://x.com/ryancarson/status/2020931274219594107](https://x.com/ryancarson/status/2020931274219594107)
- Canonical: [https://x.com/ryancarson/status/2020931274219594107](https://x.com/ryancarson/status/2020931274219594107)
- Author: Ryan Carson (@ryancarson)

## Verbatim Text

How to setup a team of agents in OpenClaw - in just one command

This article will show you how to install an entire team of agents into your OpenClaw setup with one simple command.

Your lobster will then be able to manage an agent team and have them execute repeatable, deterministic workflows to ship real PRs.

Say hello to [Antfarm](https://www.antfarm.cool) - built right on top of @openclaw.

1. It's [free and open source](https://github.com/snarktank/antfarm).

2. You get a dashboard to visualize what's happening ...

And you can click into a task to see all the details, including the user stories (with acceptance criteria) that your agent team is cranking through ...

## TL;DR

- One command installs a full agent team into your existing @openclaw  setup

- Deterministic workflows — same steps, same order, every time

- Agents verify each other's work

- Each agent gets fresh context

- YAML-defined, so you can build your own workflows

- Zero infrastructure — no Docker, no Redis, no Kafka

## Install

Tell your OpenClaw agent ...

```bash
install github.com/snarktank/antfarm
```

That's it.

One command provisions everything: agent workspaces, cron polling, subagent permissions.

No Docker, no queues, no external services.

## Agent team workflows included

1. feature-dev (7 agents)

Drop in a feature request. Get back a tested PR. The planner decomposes your task into stories. Each story gets implemented, verified, and tested in isolation. Failures retry automatically.

```plaintext
plan → setup → implement → verify → test → PR → review
```

2. security-audit (7 agents)

Point it at a repo. Get back a security fix PR with regression tests. Scans for vulnerabilities, ranks by severity, patches each one, re-audits after all fixes are applied.

```plaintext
scan → prioritize → setup → fix → verify → test → PR
```

3. bug-fix (6 agents)

Paste a bug report. Get back a fix with a regression test. Triager reproduces it, investigator finds root cause, fixer patches, verifier confirms. Zero babysitting.

```plaintext
triage → investigate → setup → fix → verify → PR
```

## Quick example

```bash
$ antfarm workflow install feature-dev
✓ Installed workflow: feature-dev

$ antfarm workflow run feature-dev "Add user authentication with OAuth"
Run: a1fdf573
Workflow: feature-dev
Status: running

$ antfarm workflow status "OAuth"
Run: a1fdf573
Workflow: feature-dev
Steps:
  [done   ] plan (planner)
  [done   ] setup (setup)
  [running] implement (developer)  Stories: 3/7 done
  [pending] verify (verifier)
  [pending] test (tester)
  [pending] pr (developer)
  [pending] review (reviewer)
```

## Why it works

Deterministic workflows

Same workflow, same steps, same order. Not "hopefully the agent remembers to test."

Agents verify each other

The developer doesn't mark their own homework. A separate verifier checks every story against acceptance criteria.

Fresh context, every step

Each agent gets a clean session using Ralph loops. No context window bloat. No hallucinated state from 50 messages ago.

Retry and escalate

Failed steps retry automatically. If retries exhaust, it escalates to you. Nothing fails silently.

## How it works

1. Define

Agents and steps in YAML. Each agent gets a persona, workspace, and strict acceptance criteria. No ambiguity about who does what.

2. Install

One command provisions everything: agent workspaces, cron polling, subagent permissions. No Docker, no queues, no external services.

3. Run

Agents poll for work independently. Claim a step, do the work, pass context to the next agent. SQLite tracks state. Cron keeps it moving.

## Minimal by design

YAML + SQLite + cron. That's it.

No Redis, no Kafka, no container orchestrator.

Antfarm is a TypeScript CLI with zero external dependencies. It runs wherever OpenClaw runs.

## Built on the Ralph loop

Each agent runs in a fresh session with clean context. Memory persists through git history and progress files — the same autonomous loop pattern from [Ralph](https://github.com/snarktank/ralph), scaled to multi-agent workflows.

## Add your own workflows

The bundled workflows are starting points. Define your own agents, steps, retry logic, and verification gates in plain YAML and Markdown. If you can write a prompt, you can build a workflow.

```yaml
id: my-workflow
name: My Custom Workflow
agents:
  - id: researcher
    name: Researcher
    workspace:
      files:
        AGENTS.md: agents/researcher/AGENTS.md

steps:
  - id: research
    agent: researcher
    input: |
      Research {{task}} and report findings.
      Reply with STATUS: done and FINDINGS: ...
    expects: "STATUS: done"
```

Full guide: [docs/creating-workflows.md](https://github.com/snarktank/antfarm/blob/main/docs/creating-workflows.md)

## Security

You're installing agent teams that run code on your machine. That's scary and we take that seriously.

- Curated repo only — Antfarm only installs workflows from the official snarktank/antfarm repository. No arbitrary remote sources.

- Reviewed for prompt injection — Every Antfarm workflow is reviewed for prompt injection attacks and malicious agent files before merging.

- Community contributions welcome — Want to add a workflow? Submit a PR. All submissions go through careful security review before they ship.

- Transparent by default — Every workflow is plain YAML and Markdown. You can read exactly what each agent will do before you install it.

## Dashboard

Monitor runs, track step progress, and view agent output in real time with:

```bash
antfarm dashboard
```

## Commands

Lifecycle

Install all bundled workflows

```bash
antfarm install
```

Full teardown (agents, crons, DB)

```bash
antfarm uninstall
```

Workflows

Start a run

```bash
antfarm workflow run <id> <task>
```

Check run status

```bash
antfarm workflow status <query>
```

List all runs

```bash
antfarm workflow runs
```

Resume a failed run

```bash
antfarm workflow resume <run-id>
```

Management

List available workflows

```bash
antfarm workflow list
```

Install a single workflow

```bash
antfarm workflow install <id>
```

Remove a single workflow

```bash
antfarm workflow uninstall <id>
```

Start the web dashboard

```bash
antfarm dashboard
```

View recent log entries

```bash
antfarm logs
```

---

Try it out: tell your OpenClaw agent ...

```bash
install github.com/snarktank/antfarm
```

... and run your first workflow. I'd love to hear how it goes — what works, what breaks, what workflows you'd want to see. DM me or open an issue on the [Antfarm repo](https://github.com/snarktank/antfarm).

## Why I built this

I've been working on building reliable, repeatable agentic dev processes for a while now.

It started with [ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) (now at 7,500 stars) — a tightly guardrailed system for getting consistent output from AI agents. Models were less capable back then, so those tight guardrails were required. Every step had to be explicitly defined and checked. The github repo went nuts after my interview with @clairevo.

[Embedded Tweet: https://x.com/i/status/1946306085557809361]

Then Opus 4.5 and Gemini 3 came out and everything changed. Models were finally capable enough to run (mostly) autonomously, so [Ralph](https://github.com/snarktank/ralph) (just hit 9,800 stars) became possible — an autonomous agent loop that picks up tasks and executes them until complete.

People seemed to like the Ralph guide and it rocketed to 1.8m views on X.

[Embedded Tweet: https://x.com/i/status/2008548371712135632]

Then @openclaw hit.

I realized I needed to take everything I'd learned and build a team of agents that my OpenClaw could manage. But they needed repeatable, deterministic workflows and the Ralph loop pattern — fresh context every session, memory through git, automatic retries.

So I built [Antfarm](https://www.antfarm.cool) for my own needs and decided to open source it. I'd love for people to submit PRs with new workflows. We'll vet every submission for security and prompt injection before merging, and hopefully build a library of community workflows that everyone can use.

Hope you like it and find it useful :)

## X Article Metadata

- Title: How to setup a team of agents in OpenClaw - in just one command
- Preview: This article will show you how to install an entire team of agents into your OpenClaw setup with one simple command. 
Your lobster will then be able to manage an agent team and have them execute

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
