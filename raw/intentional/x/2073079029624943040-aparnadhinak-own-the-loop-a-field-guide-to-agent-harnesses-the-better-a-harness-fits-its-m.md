---
type: raw_capture
source_type: x
url: https://x.com/aparnadhinak/status/2073079029624943040
original_url: https://x.com/aparnadhinak/status/2073079029624943040
author: "Aparna Dhinakaran"
handle: aparnadhinak
status_id: 2073079029624943040
captured_at: 2026-07-04T12:46:28+08:00
published_at: "Fri Jul 03 16:18:51 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 2
  reposts: 13
  likes: 96
---

# X post by @aparnadhinak

## Source

- Original: [https://x.com/aparnadhinak/status/2073079029624943040](https://x.com/aparnadhinak/status/2073079029624943040)
- Canonical: [https://x.com/aparnadhinak/status/2073079029624943040](https://x.com/aparnadhinak/status/2073079029624943040)
- Author: Aparna Dhinakaran (@aparnadhinak)

## Verbatim Text

Own the Loop: A Field Guide to Agent Harnesses

The better a harness fits its model, the less of it is yours. The most capable coding agents today are model-native pairs: a frontier lab matches its best model to its own harness. Claude Code is strongest on Anthropic's models, Codex on OpenAI's.

But that fit comes at a cost: the same coupling that makes a harness feel magical also ties your workflow to one vendor's models, prices, and product surfaces. When a model gets too expensive, goes down, or [gets pulled from use entirely](https://www.google.com/url?q=https://www.anthropic.com/news/fable-mythos-access&sa=D&source=editors&ust=1783098969986591&usg=AOvVaw27Df3YCAcaoOoFIOxeft-f), your workflow breaks with it.

And as the best models show less improvement with every release, and [open-weight models have exploded in capability](https://www.google.com/url?q=https://llm-stats.com/blog/research/glm-5-2-vs-claude-opus-4-8&sa=D&source=editors&ust=1783098969986914&usg=AOvVaw3vUT3_Qb6BhY9bAzyZvXFu), models are becoming a commodity, which is why it's the harness, not the model, that now makes or breaks your agent.

So the real choice isn't which model, but how much of the harness to own. We answer this by mapping the field, comparing harnesses on:

- Capability: how well the model fits the harness, plus the ecosystem around it: the tooling, skills, and integrations it can draw on.

- Freedom: how easily you can switch models, and how much of your workflow you own.

- Workflow: which job, and which user, does each harness actually serve?

All of this analysis assumes we know what we're comparing; let's establish a baseline: what is a harness?

# Every harness is a loop

A harness is a while loop the model runs. Alone, the model answers once and stops. In the loop it edits files, runs tests, reads failures, fixes code, and repeats until the work is done.

The major harnesses all arrived here independently, converging on the same set of parts. They differ by who controls that loop once it's running: two harnesses can share the same basic cycle and feel nothing alike, depending on whether you can read what happened, wire in your own tools, and carry the workflow forward. That gap is what the rest of this guide maps.

# The harness map

We placed the field on two axes and graded each harness out of ten: how capable it is, and how free you are.

Capability is graded on how well the model fits the harness, and the ecosystem around it: how much tooling it brings, and the skills, integrations, and support it can draw on. Freedom is how well your setup survives change: how easily you can switch and mix models, and how little of your loop is trapped on one vendor's platform.

Open source and freedom are not the same thing. Droid and Cursor are closed, but run almost any model. Codex is open source and tries to pull you toward OpenAI's conventions and services whenever possible.

Model-native pairs lead in capability, followed by open-agnostic tools, Pi, and assist-first agents. Choose a closed, vendor-optimized performance or move toward swappable, portable workflows.

# Freedom: how hard is it to leave?

With model choice no longer defining the edge, the true test of a harness is portability. It comes down to two questions: Can you audit and fork the code? And does your workflow (the rules, integrations, and configurations you’ve built) stay with you, or is it trapped in the vendor's ecosystem?

Vendors are actively widening this gap by migrating your daily loop onto their own services, letting you carry a live session between browser and terminal, run a sibling agent inside a desktop app, and [hand a design mockup straight to the coding agent](https://www.google.com/url?q=https://www.anthropic.com/news/claude-design-anthropic-labs&sa=D&source=editors&ust=1783098969991351&usg=AOvVaw2PX0pOPfCwahzhRLkFWBp7), all fluidly across surfaces only they run. These features are powerful, but built to keep you on the platform.

Community tools have no such retention motive. Because they are forkable, they cannot be repriced, quietly degraded, or restricted without your consent. In a field that reinvents itself monthly, the robust move is to keep your model swappable and your workflow somewhere you own so that your compounding knowledge stays with you.

# Capability: the same model, a better agent

Run identical tasks through different harnesses using the same model, and the results diverge sharply; models often score [several points higher](https://www.google.com/url?q=https://www.tbench.ai/leaderboard/terminal-bench/2.1&sa=D&source=editors&ust=1783098969992573&usg=AOvVaw1IkeQYLqwdAl98i9ZI7vIn) when running in their own lab’s harness.

These high-performance defaults are tempting, but the native advantage is diminishing. Any edge in complex tasks can be reclaimed by routing the right step to the right model.

Orchestration, not raw model performance, is the new capability. Models have distinct temperaments; some excel at planning, others at execution. The future isn't a tool attached to one model, but rather it’s a manager that orchestrates across them. This requires a harness that switches models without friction, allowing you to use a frontier model for high-level planning and cheaper open-weights for mechanical lifting.

# Which one to use

The right harness depends on the job at hand.

The best, at a cost. Use Claude Code for the strongest model-native coding loop, the richest extension surface, or Codex if your work already lives in OpenAI's terminal, IDE, and cloud. These are the tightest model-harness pairs and the right default for most people. The cost is in the name: the better the fit, the less of your workflow is portable, so keep your instructions and knowledge in a form you can own, and stay shallow on the cloud-only surfaces.

Own the harness. Use OpenCode for the open-source Claude Code feel with provider choice built in, OpenHands for a self-hostable SWE-agent platform, Goose for a vendor-neutral general agent, and Pi to build up from the minimum loop. Open, model-agnostic, and yours to assemble. More control means more setup, and this is the tier that pays off as models commoditize and routing each task to the right one becomes the point.

Staying in the IDE. Use Cursor for the best day-to-day IDE surface with model choice underneath, Copilot when GitHub-native features are enough, Antigravity for an agent-first IDE with orchestration built in, and Cline for an open agent that approves every edit before it runs. These optimize for the surface you work in rather than control of the loop.

Hand off or assist. A different shape of work focused on delegating. Devin is a fully autonomous cloud engineer. Droid is an agent across terminal, IDE, desktop, that runs any model. OpenClaw and Hermes are always-on personal assistants on your chat surfaces, with memory, schedules, and long-running routines. OpenClaw reaches you across many surfaces, and Hermes carries its memory and skills across model providers, which is this whole argument built into an assistant.

Renting the frontier is right where cost matters less and peak out-of-the-box performance matters most. Keeping an open, model-agnostic escape is a bet on where a fast-moving field is heading, as cheap, powerful models have closed the gap in capability.

The future of harnesses

The trends point in the same direction: toward the dominance of the loop and the vendor's platform.

- A layer is forming above the harness.[ ](https://www.google.com/url?q=https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents&sa=D&source=editors&ust=1783098969997993&usg=AOvVaw2PhJEKTTFQ9Rs0N4mFSHUE)[Meta-harnesses now compose several coding agents behind one interface](https://www.google.com/url?q=https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents&sa=D&source=editors&ust=1783098969998325&usg=AOvVaw2dhW4yyKQ73zDd6q9Sf8er), enforcing budgets and permissions above the loop instead of inside it, and[ ](https://www.google.com/url?q=https://openai.com/index/open-source-codex-orchestration-symphony/&sa=D&source=editors&ust=1783098969998538&usg=AOvVaw0Q6ME-Wg2oiJhFhV9DrgmB)[the issue tracker is becoming a control plane for fleets of agents](https://www.google.com/url?q=https://openai.com/index/open-source-codex-orchestration-symphony/&sa=D&source=editors&ust=1783098969998704&usg=AOvVaw0CNTO6nDktTo5bVYrC51Wh). This does to harnesses what routers did to models: it relocates the ownership question rather than answering it. Whether your routing policies live in an open runtime or a managed console decides whether your orchestration is portable, or trapped on one more platform you can't export.

- The matched pair goes stale.[ ](https://www.google.com/url?q=https://www.anthropic.com/engineering/harness-design-long-running-apps&sa=D&source=editors&ust=1783098969999251&usg=AOvVaw2xrA4OPrlZIzgj1FDrRHT4)[Every component encodes an assumption about what the model can't do alone](https://www.google.com/url?q=https://www.anthropic.com/engineering/harness-design-long-running-apps&sa=D&source=editors&ust=1783098969999452&usg=AOvVaw324iWV4fRXIBUhuuvuh3Oi), and the assumptions rot.[ ](https://www.google.com/url?q=https://cognition.com/blog/devin-sonnet-4-5-lessons-and-challenges&sa=D&source=editors&ust=1783098969999555&usg=AOvVaw1p-on-Ickq2YeAcSA6fZ7m)[One harness built elaborate compaction and checkpointing around a model that cut corners near its context limit](https://www.google.com/url?q=https://cognition.com/blog/devin-sonnet-4-5-lessons-and-challenges&sa=D&source=editors&ust=1783098969999756&usg=AOvVaw2UdpH0UnUiqmAMfAfOk1jF). The next release didn’t need the crutch, and the scaffolding became dead weight. Some argue the endpoint is a[ ](https://www.google.com/url?q=https://arxiv.org/abs/2604.21003&sa=D&source=editors&ust=1783098970000002&usg=AOvVaw0dDU8aygMrNwU7m2xCgINJ)[minimal harness](https://www.google.com/url?q=https://arxiv.org/abs/2604.21003&sa=D&source=editors&ust=1783098970000094&usg=AOvVaw0TAtC9txKXN94pmpO7UXOA), as owning the loop means owning the ability to re-fit it when the model moves under you.

- The harness is starting to improve itself. Harnesses can now improve from their own[ ](https://www.google.com/url?q=https://arxiv.org/abs/2606.09498&sa=D&source=editors&ust=1783098970000547&usg=AOvVaw0JiGviKoD4xmN5-bc9NlVL)[execution traces](https://www.google.com/url?q=https://arxiv.org/abs/2606.09498&sa=D&source=editors&ust=1783098970000647&usg=AOvVaw1FEUMJ2SOP9ZKnbC4M93b3), though[ ](https://www.google.com/url?q=https://arxiv.org/abs/2605.30621&sa=D&source=editors&ust=1783098970000834&usg=AOvVaw3xkQ0cXVG-oIqC6ODuAtDu)[the gains land unevenly](https://www.google.com/url?q=https://arxiv.org/abs/2605.30621&sa=D&source=editors&ust=1783098970000932&usg=AOvVaw0a4U62iQL3F50wLRI81n7s). If the loop evolves from what it records, the trace becomes the asset, and you keep it only if you own the loop.

# Own the loop

The durable asset is the loop you build and refine, where human and token capital compound.

The model is rented capability, and it's getting cheaper. The harness is the control loop, and the lock-in. We pick the model first and let the harness come along with it, but the model turns over every few months while the harness is what you keep. So is the skill of running it: what you learn about any one model resets with the next release, while what you learn about your loop compounds across all of them. Own the loop, because the model was never yours to keep.

## X Article Metadata

- Title: Own the Loop: A Field Guide to Agent Harnesses
- Preview: The better a harness fits its model, the less of it is yours. The most capable coding agents today are model-native pairs: a frontier lab matches its best model to its own harness. Claude Code is

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
