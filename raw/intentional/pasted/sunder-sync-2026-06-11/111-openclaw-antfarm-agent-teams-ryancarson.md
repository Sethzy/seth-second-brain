---
type: raw_capture
source_type: x
title: "Sunder sync: openclaw-antfarm-agent-teams-ryancarson.md"
url: "https://x.com/ryancarson/status/2020931274219594107"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-antfarm-agent-teams-ryancarson.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/openclaw-antfarm-agent-teams-ryancarson.md"
sha256: "0e14c5d8c31d841b91d7d77de89d359ced70d1627ad9ad59d035b421fa65affb"
duplicate_of: ""
---

# Sunder sync: openclaw-antfarm-agent-teams-ryancarson.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-antfarm-agent-teams-ryancarson.md`

Primary URL: https://x.com/ryancarson/status/2020931274219594107

Duplicate of existing source-map entry: `none`

## Capture Text

# How to setup a team of agents in OpenClaw - in just one command

**Author:** Ryan Carson (@ryancarson) - Verified
**Date:** Feb 10, 2026
**URL:** https://x.com/ryancarson/status/2020931274219594107
**Type:** X Article (long-form)
**Engagement:** 83 replies, 70 reposts, 761 likes, 2,292 bookmarks, 175K views
**Tags:** openclaw, agent-teams, antfarm, multi-agent, workflows

---

## Summary

Article showing how to install an entire team of agents into your OpenClaw setup with one command using **Antfarm** (built on top of OpenClaw). Your lobster can then manage an agent team and have them execute repeatable, deterministic workflows to ship real PRs.

**Product:** [Antfarm](https://www.antfarm.cool)
**Repo:** [github.com/snarktank/antfarm](https://github.com/snarktank/antfarm)

---

## Key Points

- **Free and open source**
- Dashboard to visualize what's happening
- Click into tasks to see details including user stories with acceptance criteria

## TL;DR

- One command installs a full agent team into your existing OpenClaw setup
- Deterministic workflows — same steps, same order, every time
- Agents verify each other's work
- Each agent gets fresh context
- YAML-defined, so you can build your own workflows
- Zero infrastructure — no Docker, no Redis, no Kafka

## Install

Tell your OpenClaw agent:
```bash
install github.com/snarktank/antfarm
```

That's it. One command provisions everything: agent workspaces, cron polling, subagent permissions. No Docker, no queues, no external services.

## Agent team workflows included

### 1. feature-dev (7 agents)
Drop in a feature request. Get back a tested PR. The planner decomposes your task into stories. Each story gets implemented, verified, and tested in isolation. Failures retry automatically.

```
plan → setup → implement → verify → test → PR → review
```

### 2. security-audit (7 agents)
Point it at a repo. Get back a security fix PR with regression tests. Scans for vulnerabilities, ranks by severity, patches each one, re-audits after all fixes are applied.

```
scan → prioritize → setup → fix → verify → test → PR
```

### 3. bug-fix (6 agents)
Paste a bug report. Get back a fix with a regression test. Triager reproduces it, investigator finds root cause, fixer patches, verifier confirms. Zero babysitting.

```
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
  [done ] plan (planner)
  [done ] setup (setup)
  [running] implement (developer) Stories: 3/7 done
  [pending] verify (verifier)
  [pending] test (tester)
  [pending] pr (developer)
  [pending] review (reviewer)
```

## Why it works

- **Deterministic workflows** — Same workflow, same steps, same order. Not "hopefully the agent remembers to test."
- **Agents verify each other** — The developer doesn't mark their own homework. A separate verifier checks every story against acceptance criteria.
- **Fresh context, every step** — Each agent gets a clean session using Ralph loops. No context window bloat. No hallucinated state from 50 messages ago.
- **Retry and escalate** — Failed steps retry automatically. If retries exhaust, it escalates to you. Nothing fails silently.

## How it works

1. **Define** — Agents and steps in YAML. Each agent gets a persona, workspace, and strict acceptance criteria.
2. **Install** — One command provisions everything: agent workspaces, cron polling, subagent permissions.
3. **Run** — Agents poll for work independently. Claim a step, do the work, pass context to the next agent. SQLite tracks state. Cron keeps it moving.

## Minimal by design

YAML + SQLite + cron. That's it. No Redis, no Kafka, no container orchestrator. Antfarm is a TypeScript CLI with zero external dependencies. It runs wherever OpenClaw runs.

## Built on the Ralph loop

Each agent runs in a fresh session with clean context. Memory persists through git history and progress files — the same autonomous loop pattern from [Ralph](https://github.com/snarktank/ralph), scaled to multi-agent workflows.

## Add your own workflows

Define your own agents, steps, retry logic, and verification gates in plain YAML and Markdown.

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

- **Curated repo only** — Antfarm only installs workflows from the official snarktank/antfarm repository
- **Reviewed for prompt injection** — Every workflow is reviewed before merging
- **Community contributions welcome** — Submit PRs, all go through security review
- **Transparent by default** — Every workflow is plain YAML and Markdown

## Commands

```bash
# Lifecycle
antfarm install              # Install all bundled workflows
antfarm uninstall            # Full teardown (agents, crons, DB)

# Workflows
antfarm workflow run <id> <task>      # Start a run
antfarm workflow status <query>       # Check run status
antfarm workflow runs                 # List all runs
antfarm workflow resume <run-id>      # Resume a failed run

# Management
antfarm workflow list                 # List available workflows
antfarm workflow install <id>         # Install a single workflow
antfarm workflow uninstall <id>       # Remove a single workflow
antfarm dashboard                     # Start web dashboard
antfarm logs                          # View recent log entries
```

## Backstory

- Started with [ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) (7,500 stars) — tightly guardrailed system for consistent AI agent output
- Then Opus 4.5 and Gemini 3 made autonomous agents viable → [Ralph](https://github.com/snarktank/ralph) (9,800 stars) — autonomous agent loop
- Ralph guide hit 1.8M views on X
- Then OpenClaw hit → needed to take everything learned and build multi-agent team management
- Built Antfarm for own needs, open sourced it

## Related repos

- [github.com/snarktank/antfarm](https://github.com/snarktank/antfarm)
- [github.com/snarktank/ralph](https://github.com/snarktank/ralph)
- [github.com/snarktank/ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks)

