---
type: raw_capture
source_type: x
url: https://x.com/meghanatweets/status/2065575795746336926
original_url: https://x.com/meghanatweets/status/2065575795746336926
author: "Meghana Harishankara"
handle: meghanatweets
status_id: 2065575795746336926
captured_at: 2026-06-19T23:58:55+08:00
published_at: "Fri Jun 12 23:23:40 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 0
  likes: 7
---

# X post by @meghanatweets

## Source

- Original: [https://x.com/meghanatweets/status/2065575795746336926](https://x.com/meghanatweets/status/2065575795746336926)
- Canonical: [https://x.com/meghanatweets/status/2065575795746336926](https://x.com/meghanatweets/status/2065575795746336926)
- Author: Meghana Harishankara (@meghanatweets)

## Verbatim Text

The ‘AI loops’ fight isn’t about AI loops

Last weekend, I found myself thumbing past [Peter Steinberger’s monthly reminder](https://x.com/steipete/status/2063697162748260627) for what felt like the fourth time. It’s the post on X that says you shouldn’t be prompting coding agents anymore, you should be designing loops that prompt your agents. My usual approach to a tweet that wants to retire my job (scroll past, do not engage) was failing me, because by then it had cleared 2.2 million views and the replies had turned into a polite-ish brawl. The eye-roll surfaced. So did a second thought.

That second thought is what landed me here. The first thing I want to say is that the eye-roll is correct (anyone who’s written a CI pipeline, an autoscaler, or a Kubernetes reconciliation loop has been “designing loops” for years, and the framing is half-rebrand). The second thing I want to say is that the eye-roll is also incomplete. There’s something here, just not the thing the slogan claims, and I don’t think the existing skepticism, which is loud and reasonable, has named it cleanly yet.

So this is a post that concedes most of what the skeptics say, then argues hard about the part nobody on either side seems to be talking about. The structure of the loop is old. What changed is what we put inside it. That’s the actual conversation worth having.

## Yes, it’s a while loop

Let’s get the receipts out of the way. The pattern this whole discourse is rediscovering has a name and a date. Geoffrey Huntley posted [“Ralph Wiggum as a software engineer”](https://ghuntley.com/ralph/) in July 2025, and the “ralph loop” is a literal one-line bash:

while :; do cat PROMPT.md | claude-code ; done

That’s it. A coding agent in a while : with state on disk and a fresh context every iteration. By January 2026 it had spawned an open-source community ([ralph-wiggum](https://github.com/fstandhartinger/ralph-wiggum), [ralph-loop](https://github.com/sebastianspicker/ralph-loop), a deterministic harness with replayable trajectories), and Anthropic shipped an [official ](https://claude.com/plugins/ralph-loop)[/ralph-loop](https://claude.com/plugins/ralph-loop)[ plugin](https://claude.com/plugins/ralph-loop) for Claude Code that's cleared 178k installs as of writing. So when someone tells you in 2026 that you should be "designing loops" instead of prompting, the technique they're describing is approaching its first birthday.

It’s also not coming from outside the building. Boris Cherny, the person who built Claude Code, [went on stage at the WorkOS Acquired Unplugged event](https://www.youtube.com/watch?v=RkQQ7WEor7w) on June 2, 2026 (last week) and gave the cleanest definition I’ve heard:

> Now it’s actually leveled up, I think, again, to the next wave of abstraction where I don’t prompt Claude anymore. I have loops that are running. They’re the ones that are prompting Claude and figuring out what to do. My job is to write loops.

He has the receipt to back it. As of late December 2025, 100% of his contributions to Claude Code in the prior 30 days were written by Claude Code. He landed 259 PRs. He deleted his IDE in November 2025 and hasn’t opened it since. Steinberger sloganized it. Boris is shipping it.

Sure, ok. Now the easy objection.

## Cron with a decision-maker

The sharpest skeptic line I’ve seen this week is four words: “cronjobs have funny re-branding rn.” Half of that’s correct. The scheduling layer of every “loop” you’ll see in production is, in fact, cron. Boris literally runs his on cron. The /loop slash command in Claude Code is calling cron under the hood. If your whole definition of an AI loop is "a thing that runs on a timer," then yes, we invented that in 1975 and you can put your phone down.

But the punchline ducks half the question. A cron job runs a fixed script. A loop, in the way Boris and Steinberger mean it, runs a model that looks at the current state, decides what to do next, does it, checks whether it worked, and decides whether to keep going. The decision is the agent’s, not yours, and not a hardcoded branch. That’s the part cron never had: a body. Stack those, let one loop dispatch and supervise others, give them durable shared state, and cron stops being able to express what’s happening. The interesting engineering is everything you wrap around that body so it doesn’t run off a cliff.

This isn’t a new shape, by the way. Kubernetes calls them [“control loops.”](https://kubernetes.io/docs/concepts/architecture/controller/) The official docs use a thermostat as the example. Every CI pipeline that re-runs flaky tests, every autoscaler that watches a metric and adjusts, every TCP congestion-control implementation: they’re all the same trick at different altitudes. I’m not a control-systems person (I read the Kubernetes docs the same way you do), but the rhyme is hard to miss. The thing that changes between a thermostat and an agent isn’t the loop. It’s what’s in the loop’s body.

## What actually changed

Now the harder concession. The “agents are just a while loop with an LLM call” line is the loudest skeptical take going — 1,800-plus Hacker News comments and a whole site ([extra-steps.dev](https://extra-steps.dev/)) dedicated to mapping AI buzzwords to CS primitives. They're right that the shape's old. What changed is what we put inside it, and that's the part the slogan keeps skipping. Worth naming, otherwise this post reads like one more "this is just X" dunk.

The first thing that’s different is what’s in the controller slot. A thermostat picks “on” or “off.” An autoscaler picks an integer. The LLM in an agent loop picks an action over a space orders of magnitude larger than the thermostat or autoscaler controllers it’s being compared to: the cross-product of the codebase, every tool you’ve wired up, and the prompts of all the loops that came before. The structure is the same. The space the controller chooses over is genuinely new. That’s not nothing.

The bigger shift is one layer up. Single-agent ralph is old hat by now. The thing that’s actually new in the last six months is multi-agent supervision: one loop dispatching and supervising others, with durable shared state in git, and crash recovery so the system survives a restart. [Steve Yegge’s Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) is the deep end of this. Twenty to thirty Claude Code instances coordinated by a Mayor agent, patrol agents running continuous loops, state in git so work survives a crash. It’s open source. That’s the part the slogan is gesturing at, even if Steinberger’s six words don’t quite reach it.

And there are good-faith counter-arguments that go further than my position. The Netflix Conductor creator wrote [“Late-Bound Sagas: Why Your Agent Is Not an LLM in a Loop”](https://news.ycombinator.com/item?id=47766445) arguing that the while-loop primitive itself is the wrong one: planning and execution should be separated, signal-driven cancellation is a real new requirement, runtime-synthesized graphs are too. I think they’re more right than wrong. Once you’re past a single agent fixing tests in a tight loop and into multi-agent supervision with long-running goals, the bash one-liner isn’t expressive enough. You need a planner, you need cancellation, you need something that survives a restart. That’s still arguing about what’s inside the body, not whether the loop itself is the wrong shape. Which control plane belongs there is the real question. But it’s the version of that argument that matters most, and any honest take has to concede it.

We’ve been in this kind of argument before. RAG was “just search” until people put work into making it more than that. Chain-of-thought was “just prompting” until people built around it. I don’t think the precedent predicts anything about loops. That would be cheap induction. But it does say something about the shape of the conversation: the “it’s just X” line is usually correct, and the part it skips is usually where the new engineering ends up living. Worth keeping that pattern in mind without leaning on it.

## The conversation we should be having

All of that is the surface argument, and I think the surface argument is mostly settled. Yes, it’s a while loop. No, it’s not just cron. The controller is genuinely new in some ways. The interesting engineering is one layer down, and that’s the conversation everyone keeps skipping past.

The practitioners already use the right word. Anthropic’s own Claude Code blog has a post called [“Feedback loops: Help Claude Code complete ambitious tasks with less babysitting.”](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) They take the loop’s existence as given. What they emphasize is the quality of the feedback inside it: “Claude already self-verifies against deterministic signals like type errors, lint errors, failing tests, and runtime errors.” Those deterministic signals are sensors. The two-layer pattern they recommend (in-loop verification while the agent works, plus a second-agent review before the merge) is feedback design at two altitudes. Their own framing line is the one I keep coming back to:

> “When checks depend on you, coding sessions become a turn-based game, and you lose what makes agents useful: autonomy.”

That sentence is doing real work. It’s the difference between a loop that closes (the agent observes, decides, acts, observes again) and one that’s just a while-true around a stranger. It’s also why the chatter on X feels off. Steinberger’s “design loops” slogan is shouting one layer above where Anthropic’s own engineers are quietly using control-systems vocabulary. The marketing layer is louder than the engineering layer, which is, well, normal.

The pattern is so commoditized at this point that there’s a marketplace selling pre-built ones. [loops.elorm.xyz](https://loops.elorm.xyz/) opens with "Stop prompting. Start looping." and sells reusable loops with names like "Ship PR Until Green", "Coverage Until Threshold", "Build Until Green". Each one's a literal while error > threshold: observe; correct; with an LLM in the controller slot (how cool is that!). The patterns are SKUs now.

And the failure mode of a badly-designed loop has stopped being a philosophical problem and become a finance problem, which is when most things start getting real attention. [Uber capped its engineers at $1,500 per person per tool per month](https://finance.yahoo.com/sectors/technology/articles/uber-caps-monthly-employee-ai-180342247.html) for Claude Code and Cursor after burning through its annual AI budget in four months. The receipt that should be in every “design loops” thread is the boring one: without halt conditions, you get infinite loops and billing surprises orders of magnitude over budget. Every serious 2026 write-up I read converges on the same three hard stops: a max iteration count, no-progress detection, and a token or dollar ceiling. That’s the actual engineering. Not the loop. Not the rebrand. The body of the loop, the feedback inside it, and the conditions under which it stops.

## Verdict: argue about the inside

So here’s where I land. Yes, it’s a while loop. The structure is old. What changed is what we put inside it: the LLM in the controller slot, the multi-agent supervision around it, the deterministic feedback signals, the halt conditions that stop it from becoming an Anthropic-bill-shaped hole in your runway. That’s where the engineering lives. That’s where the arguments worth having are.

Stop arguing whether AI loops are a new shape. They aren’t, exactly. Argue about the controller, the feedback, the halt condition. That’s the conversation worth showing up for. Everything else is plumbing.

## X Article Metadata

- Title: The ‘AI loops’ fight isn’t about AI loops
- Preview: Last weekend, I found myself thumbing past Peter Steinberger’s monthly reminder for what felt like the fourth time. It’s the post on X that says you shouldn’t be prompting coding agents anymore, you

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
