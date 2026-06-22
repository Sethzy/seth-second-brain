---
type: raw_capture
source_type: x
url: https://x.com/JackCulpan/status/2029478582352003150
original_url: https://x.com/jackculpan/status/2029478582352003150
author: "Jack Culpan"
handle: JackCulpan
status_id: 2029478582352003150
captured_at: 2026-06-19T21:42:54+08:00
published_at: "Thu Mar 05 08:46:14 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 22
  reposts: 76
  likes: 1323
---

# X post by @JackCulpan

## Source

- Original: [https://x.com/jackculpan/status/2029478582352003150](https://x.com/jackculpan/status/2029478582352003150)
- Canonical: [https://x.com/JackCulpan/status/2029478582352003150](https://x.com/JackCulpan/status/2029478582352003150)
- Author: Jack Culpan (@JackCulpan)

## Verbatim Text

Here's the prompt:

## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately – don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff your behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes – don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests – then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

### 7. Task Management
1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

### Core Principles
- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

## Quoted Post

- URL: https://x.com/bcherny/status/2017742741636321619
- Author: Boris Cherny (@bcherny)

I'm Boris and I created Claude Code. I wanted to quickly share a few tips for using Claude Code, sourced directly from the Claude Code team. The way the team uses Claude is different than how I use it. Remember: there is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!

## Capture Note

TweetDetail returned complete normal-post text.
