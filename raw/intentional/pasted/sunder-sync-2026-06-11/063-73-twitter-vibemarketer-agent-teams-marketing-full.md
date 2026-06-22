---
type: raw_capture
source_type: x
title: "Sunder sync: 73-twitter-vibemarketer-agent-teams-marketing-FULL.md"
url: "https://x.com/vibemarketer_/status/2020142441769156678"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/73-twitter-vibemarketer-agent-teams-marketing-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/73-twitter-vibemarketer-agent-teams-marketing-FULL.md"
sha256: "78b14039ca35bd4abf1850d82d32eb6404cc76a4adee8e94ac1f7831d2fec437"
duplicate_of: ""
---

# Sunder sync: 73-twitter-vibemarketer-agent-teams-marketing-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/73-twitter-vibemarketer-agent-teams-marketing-FULL.md`

Primary URL: https://x.com/vibemarketer_/status/2020142441769156678

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @VibeMarketer_: Build Your Marketing Department in Claude Code Agent Teams

**URL:** https://x.com/vibemarketer_/status/2020142441769156678
**Author:** J.B. (@VibeMarketer_) - Verified
**Posted:** 10:27 PM · Feb 7, 2026
**Engagement:** 15 replies, 36 reposts, 530 likes, 1.5K bookmarks, 48.3K views

## Summary
Comprehensive guide to Claude Code's new agent teams feature for marketing operations. "Claude code just shipped agent teams. Here's how to build your own marketing department inside it." Covers setup (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS), use cases (campaign research, landing pages, ad creative, content), best practices (delegate mode, plan approval, 3-5 teammates), and common mistakes. Teams collaborate in real time, challenge each other, share findings - not just parallel execution.

## Key Content

### Setup
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### Marketing Use Cases

**Campaign Research Sprint:** 3 teammates (competitor ad analysis, customer voice mining, positioning stress-test) work simultaneously, challenge findings, lead synthesizes strategy.

**Landing Page Builds:** Copy + messaging, conversion/CRO, adversarial review as skeptical buyer. Plan approval required before implementation.

**Ad Creative Exploration:** 4 teammates explore hook angles, debate which is strongest, consensus survives battle-testing.

**Content Production:** Search intent/gaps, drafting, recursive quality loop. Parallel research + production with built-in QA.

### Best Practices
- Delegate mode (Shift+Tab): Lead coordinates only, doesn't execute
- Plan approval: Outlines reviewed before execution
- 3-5 teammates optimal: More = coordination overhead
- Let them argue: Friction drives insight
- Shift+Up/Down: Talk to teammates directly

### Mistakes to Avoid
- Simple tasks don't need teams
- Same-file edits = overwrites
- Too many teammates kills coordination
- Unattended runs risk wasted work
- Teammates lack lead's conversation history
- Skip plan approval = burn cycles on bad directions

## Analysis
**Collaboration vs. Parallelization:** "They don't just work in parallel, they collaborate, challenge each other, and build on each other's findings." This is peer debate, not just fan-out/fan-in.

**Battle-Testing:** "One agent exploring alone tends to anchor on the first decent idea. Four agents actively trying to disprove each other? The angle that survives is actually battle-tested."

**Token Economics:** Each teammate = separate Claude instance. Worth it for complex work, overkill for simple tasks.

## Categories
#agent-teams #claude-code #marketing-automation #multi-agent #delegate-mode #plan-approval #parallel-execution #battle-testing

## Related Items
- Item 67: Kevin Simback agent teams guide (complementary)
- Item 68: Prukalpa shared context (coordination pattern)
- Pattern: Agent teams for specialized workflows

