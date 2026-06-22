---
type: raw_capture
source_type: x
url: https://x.com/utpalnadiger/status/2033370292945658185
original_url: https://x.com/utpalnadiger/status/2033370292945658185
author: "Utpal Nadiger"
handle: utpalnadiger
status_id: 2033370292945658185
captured_at: 2026-06-19T21:44:10+08:00
published_at: "Mon Mar 16 02:30:30 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 4
  likes: 33
---

# X post by @utpalnadiger

## Source

- Original: [https://x.com/utpalnadiger/status/2033370292945658185](https://x.com/utpalnadiger/status/2033370292945658185)
- Canonical: [https://x.com/utpalnadiger/status/2033370292945658185](https://x.com/utpalnadiger/status/2033370292945658185)
- Author: Utpal Nadiger (@utpalnadiger)

## Verbatim Text

Sunday doomscroll report: everything I found on sandbox infra

Yesterday I hiked the twin peaks (i've attached a picture from the hike) and did a hectic lower body workout to follow that. 

It's particularly sunny in SF this weekend and I'd like to think I made good use of it. 

But the soreness and laziness that comes with the weekend hit me today, and made me go into doom scroll hell.

Thankfully though, this weekend's doomscrolling sesh was actually productive.

I'll explain haha, this isn't cope I promise. 

Since we've been onboarding users onto opencomputer.dev starting this week, I ended up putting myself in the shoes of users who would want something like this. 

What would they be searching for? 

Basically wanted to trace what the journey was from "hey I want to build an agent" to "Hey here's what I want to use for infra for my agent"

Fair warning: I don't claim for this to be thorough, I also don't claim for any of this to be without bias as I am a founder of a vendor in the space, but I am certain that it'll help more folks who are tracing the same path so here goes:

## What my elaborate, intentional doomscrolling process looked like

I first stumbled on the [awesome sandbox](https://github.com/restyler/awesome-sandbox) repo, it breaks down the main isolation approaches ie, MicroVMs, application kernels, language runtimes, containers, and maps out which vendors use what. It was honestly great for building a mental model of the space before you start comparing.

Another banger resource, for me (mind you I was specifically trying to look for resources to help me pick infra for a background agent, a bit like ramp's [inspect](https://x.com/rahulgs/status/2010734250203455862))  was this [article](https://background-agents.com/), which, honestly, is an absolute work of art. Likely Opus 4.6 as the artist, but just goes to show how good opus is haha (Sorry @loujaybee if this is not true)

And then I stepped into the maze of vendors - each incredible in their own way, but obviously, as an (early) vendor in the space, I was keen to do more digging.

I was aware of the [compute sdk benchmarks](https://github.com/computesdk/benchmarks) from my previous doomscrolling so that's where I first went, and honestly, they are INCREDIBLY thorough. Looking at how they make money (as a sandbox "gateway" if I understand correctly), I don't think they are incentivised to be partial to any one vendor, even if one of them ended up sponsoring the benchmarks. So if I were a user, I'd go to their open source benchmark repo for sure! (and probably run them myself just to be sure)

I kept scrolling (mostly out of interest at this point) and kept finding more  folks that probably went through the same rabbit hole:

- @gm_mertd  (founder of banker.so) did a solid feature by feature [comparison](https://sandbox-comparison.pages.dev/) which kinda goes beyond just benchmarks if that's your thing.

- @nilesh_agarwal2 (ex-CTO of Inferless, currently at Baseten) [went deep](https://github.com/nickaggarwal/sandbox-test/blob/main/FULL_BENCHMARK_REPORT) on benchmarks - dude clearly knows his infra!

- @kajogo777  (founder of stakpak.dev)  built a [taxonomy of sandbox types](https://github.com/kajogo777/the-agent-sandbox-taxonomy). Honestly helpful for figuring out what you even need before comparing

- @NathanFlurry  - the creator of sandboxagent.dev and founder of @rivet_dev -  put together a [cost comparison](https://claude.ai/public/artifacts/5a2a8a9d-4af3-4524-a04f-92f4f92629a7) across providers  - which is pretty thorough but he himself mentions he's not very sure about the accuracy, I added it anyways.

- Honourable mention to @ryanvogel's [thread](https://x.com/ryanvogel/status/2024266375825363207). I didn't actually find this one doomscrolling, but it comes up on almost every user call we've been on. At this point it's basically required reading in the space.

I put all the exploits from this effort into an awesome repo, so that users going through the same rabbit hole may benefit from it (and learn about opencomputer.dev in the process too? we'll take all the attention we can get!)

Check it out [here](https://github.com/diggerhq/awesome-sandbox-benchmarks). Feel free to create a PR if you find any more!

## X Article Metadata

- Title: Sunday doomscroll report: everything I found on sandbox infra
- Preview: Yesterday I hiked the twin peaks (i've attached a picture from the hike) and did a hectic lower body workout to follow that. 

It's particularly sunny in SF this weekend and I'd like to think I made

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
