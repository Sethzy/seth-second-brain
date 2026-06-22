---
type: raw_capture
source_type: web
title: "12-Factor AgentOps"
url: "https://www.12factoragentops.com/"
collected_at: 2026-06-13T10:49:43Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# 12-Factor AgentOps

Source: https://www.12factoragentops.com/

## Capture Text

# 12-Factor AgentOps

Original URL: https://www.12factoragentops.com/
Fetched URL: https://www.12factoragentops.com/
Awesome Harness summary: An operations-oriented companion focused on context discipline, validation, and reproducible agent workflows.

## Fetched Content

// 12-FACTOR AGENTOPS

# Don't run production on vibes.

Agents generate code with no record of what was tried, no gate it had to pass, no proof it works. 12-Factor AgentOps is the operating model that closes that gap. Twelve factors that make agent-built software something a team can stand behind, in the tradition of the Twelve-Factor App.

[Read the 12 factors →](/factors)[Run it in your agent →](/install)[GitHub ↗](https://github.com/boshu2/agentops)

LAYER 1

BOOKKEEPING

Record attempts, decisions, verdicts in .agents/.

Never wonder what the agent already tried.

LAYER 2

CONTEXT COMPILER

Compile the right slice into the next run.

No re-explaining your codebase each session.

LAYER 3

VALIDATION GATES

Fresh-context review before plans & code ship.

Catch broken work before it hits your branch.

LAYER 4

KNOWLEDGE FLYWHEEL

Promote learnings into durable constraints.

Solved once, stays solved.

├ cold start↺ THE CORPUS COMPOUNDS — NEXT SESSION STARTS LOADEDcompounding ┤

// the 12 factors[all 12 →](/factors)

The operating rules the site is named for: twelve, in four phases.

![The 12 factors as a four-phase loop: Prepare, Bound, Select, Govern — Govern feeds back into Prepare](/media/factor-loop.svg)

[IPREPARE

Context

Put only task-relevant context in the window.](/factors/01-context-is-everything)[II

Track

Keep work state, decisions, and learnings in git.](/factors/02-track-everything-in-git)[III

Scope

Give each agent one bounded job and a fresh window.](/factors/03-one-agent-one-job)[IVBOUND

Privilege

Act inside a least-privilege envelope untrusted input cannot widen.](/factors/04-enforce-least-privilege)[V

Research

Inspect the integration surface before writing code.](/factors/05-research-before-you-build)[VI

Isolate

Separate concurrent workers by workspace, context, and state.](/factors/06-isolate-workers)[VIISELECT

Validate

The worker reports evidence; an independent checker writes the verdict.](/factors/07-validate-externally)[VIII

Lock

Turn validated work into the new baseline.](/factors/08-lock-progress-forward)[IX

Extract

Record what the session learned, not only what it changed.](/factors/09-extract-learnings)[XGOVERN

Compound

Wire learnings — positive and negative — back into future work.](/factors/10-compound-knowledge)[XI

Supervise

Escalate up a clear tree; a stuck job goes to a fresh agent.](/factors/11-supervise-hierarchically)[XII

Measure

Track fitness toward goals, not agent activity.](/factors/12-measure-outcomes)

// see it work

A skill loads the corpus before writing a line of code; a mixed-model council reviews before it ships.

> /research add rate limiting to /login

// loading context from .agents/ …

3 prior auth decisions cited · 2 planning rules · 1 learning

plan: token bucket, 5/min per IP, Redis-backed, jittered

// recorded → .agents/runs/2026-05-08-rate-limit/research.md

> /council --mixed validate this PR

// evidence packet sealed → 6 judges across Claude Code + Codex

claude · WARN rate limiting missing on /login

codex · WARN token-bucket refill lacks jitter

consensus: WARN — fix before shipping

// the bet

THE WAGER — Vendors will ship managed memory, review councils, and overnight learning loops natively; they will lock them to their runtime. Your corpus stays in .agents/ in your repo, runs on whichever harness you already pay for, and is portable across whichever frontier model wins next quarter.

Good architecture principles outlive every tool that implements them.

[see the proof →](/sovereignty-proof)

// the three gaps it closes

The failure modes that make agent work unreliable, each closed by a named surface.

G1JUDGMENTPressure-test plans before code.closed by /pre-mortem · /vibe · /council

G2DURABLE LEARNINGSolved problems stay solved.closed by /retro · /forge · ao lookup

G3LOOP CLOSUREShipped work informs the next session.closed by /post-mortem · finding compiler · /evolve

// pages

[/factorsthe twelve, in four phases→](/factors)[/cdlcthe context development lifecycle→](/cdlc)[/comparisonshow it stacks up against alternatives→](/comparisons)[/journeydoctrine evolution as a devlog arc→](/journey)[/skillsthe catalog, enforced in your runtime→](/skills)[/installrun the loop in your harness→](/install)

// the standard for software you can trust an agent to build.

the corpus stays yours
