---
type: raw_capture
source_type: x
url: https://x.com/VibeMarketer_/status/2020142441769156678
original_url: https://x.com/vibemarketer_/status/2020142441769156678
author: "J.B."
handle: VibeMarketer_
status_id: 2020142441769156678
captured_at: 2026-06-19T20:16:28+08:00
published_at: "Sat Feb 07 14:27:45 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 15
  reposts: 35
  likes: 533
---

# X post by @VibeMarketer_

## Source

- Original: [https://x.com/vibemarketer_/status/2020142441769156678](https://x.com/vibemarketer_/status/2020142441769156678)
- Canonical: [https://x.com/VibeMarketer_/status/2020142441769156678](https://x.com/VibeMarketer_/status/2020142441769156678)
- Author: J.B. (@VibeMarketer_)

## Verbatim Text

claude code just shipped agent teams. here's how to build your own marketing department inside it.

i've been using it on every major project and the results have been kind of ridiculous. here's how it works:

now, first of all - this isn't another prompt trick. it's a new way to run multiple claude instances that actually work together.

one lead coordinating, multiple teammates executing in parallel, all communicating with each other in real time.

it's experimental right now, and you have to enable it manually. but if you're running any kind of marketing operation, this changes the game.

here's what's actually happening under the hood:

you tell claude to create a team and define the roles. it spawns separate instances - each with their own context window, and they get to work. the lead coordinates. teammates claim tasks from a shared list. and unlike subagents (which just report back), teammates can message each other directly.

that last part is the unlock. they don't just work in parallel, they collaborate, challenge each other, and build on each other's findings.

here's how i'm using it for marketing:

campaign research sprint:

"create an agent team to research the launch strategy for [product]. spawn three teammates: one on competitor ad analysis, one on customer voice mining from reviews and reddit, one stress-testing our current positioning against what they find. have them share findings and challenge each other."

they work simultaneously. when the competitor researcher finds a gap, the positioning teammate pressure-tests whether we can actually own it. the voice-of-customer teammate validates whether real buyers even care. the lead synthesizes into a strategy doc.

landing page builds:

"create an agent team to build the landing page for [offer]. one teammate on copy and messaging, one on conversion structure and CRO, one running adversarial review as a skeptical buyer. require plan approval before any implementation."

the plan approval piece is key - each teammate has to outline their approach before executing. the lead reviews and either approves or sends back with feedback. catches bad directions before they waste cycles.

ad creative exploration:

"spawn 4 teammates to explore different hook angles for [product]. have them each develop one direction, then debate which is strongest. update findings doc with consensus."

the debate structure is the secret sauce. one agent exploring alone tends to anchor on the first decent idea. four agents actively trying to disprove each other? the angle that survives is actually battle-tested.

content production:

"create a team for this week's content. one teammate on search intent and competitive gaps, one drafting based on findings, one running the recursive quality loop on every piece before it ships."

parallel processing instead of sequential bottleneck. research and production happen at the same time, with built-in QA.

you get the idea.. these are just a couple of examples but imagination is the limit in terms of how far you want to take this.

now, here’s how to actually set agent swarm up inside claude code:

1. enable agent teams - add this to your settings.json:

2. {

3. "env": {

4. "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"

5. }

}

1. tell claude to create a team in natural language. be specific about roles. "one teammate on X, one on Y, one playing devil's advocate" works. "make a team to help with marketing" doesn't.

2. use delegate mode if you want the lead to only coordinate. press Shift+Tab after starting the team. this prevents the lead from doing the work itself - it only spawns, assigns, and synthesizes.

3. require plan approval for high-stakes work. add "require plan approval before they make any changes" to your prompt. each teammate outlines their approach, the lead reviews, and only approved plans get executed.

4. talk to teammates directly when needed. Shift+Up/Down to select a teammate, then type. you can redirect anyone without going through the lead.

5. use the shared task list. the lead creates tasks, teammates claim them. you can check status anytime with Ctrl+T. if something's stuck, nudge the teammate or reassign.

6. let them argue. when you tell teammates to "challenge each other" or "debate," they actually do. don't flatten this - the friction is where the insight lives.

some mistakes to avoid:

- don't use agent teams for simple tasks. single deliverables, quick copy tweaks, sequential work - just use one session. the coordination overhead isn't worth it.

- don't let teammates edit the same files. two agents writing to the same doc = overwrites. break work so each owns different pieces.

- don't spawn too many teammates. 3-5 is usually right. more than that and coordination overhead kills you.

- don't let them run unattended too long. check in, redirect, synthesize as they go. the longer they run without input, the higher the risk of wasted work.

- don't forget context. teammates don't inherit the lead's conversation history. include relevant context in your spawn prompts.

- don't skip plan approval on complex work. it feels slower but catches bad directions before they burn cycles.

and a few things to keep in mind:

- teammates each have their own context window. they load project context (CLAUDE.md, skills, MCP servers) but not the lead's conversation history.

- token usage scales with team size. each teammate is a separate claude instance. worth it for complex work, overkill for simple tasks.

- task dependencies work automatically. when a teammate completes a task that others depend on, blocked tasks unblock.

- you can specify models. "use sonnet for each teammate" if you want to manage costs.

- shutdown can be slow. teammates finish their current work before stopping.

- clean up through the lead. when you're done, tell the lead to clean up. don't have teammates do it - can leave things in a broken state.

now, again, this isn't for everything. quick copy tweaks, single deliverables, sequential work - just use one session and keep it simple.

but for anything that benefits from parallel research, multiple perspectives, and built-in pressure-testing? agent teams compound fast.

if you’re interested in more AI marketing news like this, feel free to follow me @VibeMarketer_

I'll keep dropping updates like these as often as possible. thanks for reading :)

## X Article Metadata

- Title: claude code just shipped agent teams. here's how to build your own marketing department inside it.
- Preview: i've been using it on every major project and the results have been kind of ridiculous. here's how it works:
now, first of all - this isn't another prompt trick. it's a new way to run multiple claude

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
