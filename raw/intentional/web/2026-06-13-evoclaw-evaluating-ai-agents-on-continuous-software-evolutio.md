---
type: raw_capture
source_type: web
title: "EvoClaw: Evaluating AI Agents on Continuous Software Evolution"
url: "https://openhands.dev/blog/evoclaw-benchmark"
collected_at: 2026-06-13T10:55:56Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# EvoClaw: Evaluating AI Agents on Continuous Software Evolution

Source: https://openhands.dev/blog/evoclaw-benchmark

## Capture Text

# EvoClaw: Evaluating AI Agents on Continuous Software Evolution

Original URL: https://openhands.dev/blog/evoclaw-benchmark
Fetched URL: https://openhands.dev/blog/evoclaw-benchmark

## Fetched Content

[← Back to Blog](/blog)

# EvoClaw: Evaluating AI Agents on Continuous Software Evolution

![](/assets/webflow/blog/evoclaw-benchmark/202603-evoblog-1.webp)

Written by

Gangda Deng and Zhaoling Chen

Published on

March 23, 2026

*This is a guest blog by *[*Gangda Deng*](https://hydrapse.github.io/)* and *[*Zhaoling Chen*](https://czlll.github.io/)*, introducing EvoClaw—a benchmark built with OpenHands to move beyond isolated coding tasks and toward continuous software evolution.*

AI coding has entered a new phase. In early 2026, stronger LLMs and projects like [OpenClaw](https://github.com/openclaw/openclaw) started pushing agents toward long-running, iterative workflows instead of one-off conversational task solving.

Most benchmarks still evaluate isolated tasks. Agents are getting good at those. But real engineering work is not one isolated task. Teams continuously extend an existing codebase while preserving behavior, managing dependencies, and paying down technical debt.

![](/assets/webflow/blog/evoclaw-benchmark/cover.webp)

Continuous development is where software engineering really begins. Early implementation choices constrain later work, regressions accumulate, and the real question becomes: can an agent keep solving the next task without degrading the system in the process?

That is what [EvoClaw](https://evo-claw.com/) is designed to measure. It evaluates agents on **continuous software evolution** by asking them to complete a sequence of dependent milestone tasks extracted from real repository history.

## From isolated tasks to continuous evolution

EvoClaw is built around a simple observation: one-shot code generation is not how most software is developed. Requirements arrive over time, each change depends on earlier decisions, and the system has to stay healthy while it evolves.

The benchmark captures that setting by reconstructing milestone trajectories from real repositories and evaluating agents across those trajectories instead of on isolated bug-fix prompts.

![](/assets/webflow/blog/evoclaw-benchmark/benchmark-overview.webp)

## Why milestones matter

Milestone-level task granularity is the key design choice in EvoClaw.

‍

A single commit is often too small and too noisy to serve as a meaningful development objective. At the other extreme, release-level changes are too coarse and hide the dependency structure that makes long-horizon maintenance difficult. EvoClaw works at the milestone level: semantically and functionally coherent units that are still executable and testable.

To build those trajectories at scale, the authors introduce **DeepCommit**. Starting from real open-source history, DeepCommit aggregates related commits into milestones, infers temporal dependencies, and validates the resulting task graph at runtime.

![](/assets/webflow/blog/evoclaw-benchmark/milestone-dag.webp)

## What EvoClaw measures

EvoClaw covers repositories across **five programming languages**. For each repository, it selects a real development window spanning multiple releases, sometimes across as much as 750 days of history.

The benchmark focuses on two complementary dimensions:

* **Recall**: how much of the newly required functionality the agent implements
* **Precision**: how much existing functionality the agent preserves without introducing regressions

Those two signals are then combined into a milestone-level score using an F1-style aggregation.

This framing matters because the hard part of real software evolution is often not adding new code. It is keeping the existing system from breaking while the codebase gets more complicated.

## The headline result

The results drop sharply once evaluation moves from isolated tasks to continuous evolution.

![](/assets/webflow/blog/evoclaw-benchmark/202603-evoblog-1.webp)

On isolated-task settings, frontier agents can often score above 80%. But under EvoClaw's continuous setting, the best system in the initial release reaches only **38.03% overall score**: **Claude Opus 4.6 + OpenHands**. The highest resolve rate is **13.37%**, achieved by **Gemini 3 Pro + Gemini CLI**.

![](/assets/webflow/blog/evoclaw-benchmark/main-results.webp)

That gap is the central point of the benchmark: isolated-task performance still overestimates how well an agent will behave once earlier choices, regressions, and dependency chains start to matter.

## Evolution eventually stalls

A natural question is whether a strong coding agent could eventually finish the whole project if you simply gave it enough iterations.

EvoClaw suggests the answer is no.

![](/assets/webflow/blog/evoclaw-benchmark/evolution-plateau.webp)

Even the strongest system, Opus 4.6, plateaus at roughly **45% overall score** under saturation-based extrapolation. The differences across model families are also revealing: GPT and Claude improve steadily across versions, while Gemini variants often start faster in the early milestones but show much less long-horizon improvement.

A more interesting pattern appears when the overall score is decomposed into recall and precision.

![](/assets/webflow/blog/evoclaw-benchmark/recall-vs-percision.webp)

Recall keeps rising almost linearly. Even as the codebase becomes messier and more fragile, agents remain fairly good at implementing new requested functionality. The bottleneck is precision: models struggle to preserve existing behavior, and regressions accumulate faster than they can be repaired.

That is what ultimately causes long-horizon development to stall.

## Technical debt compounds faster than agents can repair it

To understand how failures compound over time, the benchmark introduces an **error chain** analysis that tracks how problems propagate across milestones.

![](/assets/webflow/blog/evoclaw-benchmark/error-chain-analysis.webp)

The pattern is clear. Agents do sometimes repair earlier mistakes, but unresolved regressions accumulate faster than they can be fixed. Those failures then propagate downstream through dependency chains, creating a snowball effect that eventually stalls further progress.

## From code generation to system governance

If EvoClaw makes one thing clear, it is that code generation alone is not enough. The real entry point for AI systems into software engineering is whether they can follow evolving requirements while also keeping the larger system stable.

Today's frontier models still behave more like on-demand code generators than like senior engineers maintaining a living codebase. They are much better at local implementation than at system-level judgment.

That points to where the next breakthroughs need to happen: proactive refactoring, long-term memory, better planning, and much stronger awareness of architectural state. It is the same shift described in [The Second Half](https://ysymyth.github.io/The-Second-Half/): moving from passive code generation toward active system governance.

If you want to dig deeper, the full project is available here:

* [Leaderboard](https://evo-claw.com/)
* [Paper (arXiv)](https://arxiv.org/abs/2603.13428)
* [Dataset](https://huggingface.co/datasets/hyd2apse/EvoClaw-data)
* [Code](https://github.com/Hydrapse/EvoClaw)

Citation![](/assets/webflow/icons/chevrondown.svg)![](/assets/webflow/icons/copy.svg)

[![](/assets/notion-blog/model-choice-llm-profiles/llm-profiles.png)

Simple, In-conversation Model Choice in OpenHands](/blog/model-choice-llm-profiles)[![](/assets/notion-blog/openhands-for-customer-success/cover.png)

OpenHands for Customer Success: You Don't Have to Be a Developer to Use Coding Agents](/blog/openhands-for-customer-success)[![](/assets/webflow/blog/openhands-product-update-may-2026/69a8470f9d00e34ff3c8d8df_openhands_product_update_v3.png)

OpenHands Product Update - May 2026](/blog/openhands-product-update---may-2026)

# Get useful insights in our blog

Insights and updates from the OpenHands team

Sign up for our newsletter for updates, events, and community insights.

By submitting your email you agree to our [Privacy Policy](/privacy)

### Thank you for your submission!

![](/assets/webflow/backgrounds/6908d170831c19b2b6976323_ascii-art_(16)_1.svg)

Building the open standard for autonomous software development.

OpenHands is the foundation for secure, transparent, model-agnostic coding agents - empowering every software team to build faster with full control.

Build with SDK

[Build with SDK](https://docs.openhands.dev/sdk)

Try it live

[Try it live](https://app.all-hands.dev/)

[![](/assets/webflow/misc/6908d21b2270590dedae7f30_Frame48095725.svg)](/joinslack)

[![](/assets/webflow/misc/6908d21bd2a1305f4f77161b_Frame48095723.svg)](https://x.com/OpenHandsDev)

[![](/assets/webflow/misc/6908d21a36dee3e7147b3d21_Frame48095724.svg)](https://github.com/OpenHands/OpenHands)

[Home](/)[Product](/product)[Enterprise](/enterprise)[Pricing](/pricing)[About](/about)

[Resources](#footer-resources)[Community](/community)[Manifesto](/manifesto)[Docs](https://docs.openhands.dev/)[Blog](/blog)[Press](/press)[Careers](https://jobs.ashbyhq.com/OpenHands)

[Contact](/contact)

© 2026 OpenHands - All rights reserved

[Privacy Policy](/privacy)

![](/assets/webflow/backgrounds/openhands_logo_black.svg)
