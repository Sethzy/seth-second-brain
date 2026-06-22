---
type: raw_capture
source_type: pasted
title: "Vox Claude Code Codex prompt templates screenshots"
url: "https://x.com/Voxyz_ai/status/2067237707483337118"
collected_at: 2026-06-18T14:45:53Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Vox Claude Code Codex prompt templates screenshots

Source: https://x.com/Voxyz_ai/status/2067237707483337118

## Capture Text

Source context: user-provided screenshots of the Vox thread attached in Codex on 2026-06-18. These screenshots supplement the previously captured X post at https://x.com/Voxyz_ai/status/2067237707483337118.

Screenshot files:
- /var/folders/dm/273c39x9321bmnr710y7xdhm0000gn/T/TemporaryItems/NSIRD_screencaptureui_CDvw8K/Screenshot 2026-06-18 at 10.39.19 PM.png
- /var/folders/dm/273c39x9321bmnr710y7xdhm0000gn/T/TemporaryItems/NSIRD_screencaptureui_gB8ofN/Screenshot 2026-06-18 at 10.39.26 PM.png
- /var/folders/dm/273c39x9321bmnr710y7xdhm0000gn/T/TemporaryItems/NSIRD_screencaptureui_p9EBBT/Screenshot 2026-06-18 at 10.39.33 PM.png
- /var/folders/dm/273c39x9321bmnr710y7xdhm0000gn/T/TemporaryItems/NSIRD_screencaptureui_CX5zqn/Screenshot 2026-06-18 at 10.39.37 PM.png

## Verbatim Prompt Templates

### 1. the goal template i run on everything

goal: {your task / the full spec you already agreed on}. keep going until the architecture and result meet the bar, not just until it runs.
after every meaningful step: real-time test the real thing (full end-to-end, plus computer use, browser, keystrokes, whatever it needs), auto review then commit, write progress somewhere sensible in the project.
finish: one dedicated review pass over everything.
done = every dimension at 100%, production-grade, a real user can walk in and use it.

swap out {your task} and go. new feature, refactor, all the same.
tip: don't hardcode the progress path. tell it to write somewhere sensible and it finds the right spot on its own.

this is the wrapper for everything below. drop a task prompt into the {your task} slot, use #2 for big jobs, and it runs end-to-end instead of stopping at the first thing that compiles.

### 2. parallel + end-to-end goal (for big tasks)

For this task, write yourself a new end-to-end /goal: complete the whole plan, not just the next step, until the architecture, implementation, tests, review, and final result meet the standard. Split that goal into independent pieces, spawn as many parallel agents as needed to do it better and faster, and give each agent its own dedicated /goal that includes its expected deliverable, verification, and completion standard.

Dispatch them concurrently, keep tracking progress in the right place, synthesize results as they return, resolve conflicts, continue implementation, run real-time validation after important steps, and finish with review, submission/commit when appropriate, and a final summary. Validation should cover the real end-to-end path, including browser/computer use, clicks, keyboard actions, and any necessary operation. Do not stop after partial progress unless blocked by missing credentials, destructive ambiguity, or conflicting requirements.

### 3. build something production-grade

Act as a senior engineer shipping something production-ready, whether it's a single feature or a full app.

Don't jump to code. First analyze the requirements, list the edge cases, design the architecture, lay out a plan. Build the minimal version that's still scalable and maintainable.

Then deliver: architecture overview, folder structure, data flow, database schema and API design where relevant, full implementation, edge case and error handling, performance notes.

Design it like a real startup MVP, not a demo.

### 4. understand an unfamiliar repo + refactor

Act as a senior engineer who just inherited a large, unfamiliar codebase.
First understand the architecture and data flow.

Then find: structural problems, duplicated code, performance bottlenecks, maintainability risks.

Deliver: architecture overview, problem areas, refactor strategy, improved architecture and code.

### 5. senior debugging engineer

Act as a senior engineer chasing a bug in production.

Read the code carefully, reason step by step, find the root cause, give a robust fix. Account for edge cases and performance.

Your answer should cover three things: the cause, the fix plan, and production-ready code.

### 6. performance optimization

Optimize this code as a performance engineer.

Targets: speed, memory, scalability.

Find: bottlenecks, inefficient logic, unnecessary re-renders.

Return the explanation plus the optimized code.

### 7. production-grade UI components

As a senior frontend engineer, build reusable, accessible, production-ready UI components.

Cover: loading states, edge cases, responsive layout, accessibility.

Deliver the component architecture, props design, and full implementation.

### 8. publishable APIs

As an experienced backend engineer, design and build clean, production-ready APIs.

Include: validation, error handling, clean architecture.

Deliver the route design, validation, controller logic, and full implementation.
