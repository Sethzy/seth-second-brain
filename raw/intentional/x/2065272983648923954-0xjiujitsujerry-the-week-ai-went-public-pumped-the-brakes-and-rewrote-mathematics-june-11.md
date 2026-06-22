---
type: raw_capture
source_type: x
url: https://x.com/0xJiuJitsuJerry/status/2065272983648923954
original_url: https://x.com/0xJiuJitsuJerry/status/2065272983648923954
author: "0xJiuJitsuJerry"
handle: 0xJiuJitsuJerry
status_id: 2065272983648923954
captured_at: 2026-06-19T23:58:37+08:00
published_at: "Fri Jun 12 03:20:24 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 0
  reposts: 1
  likes: 1
---

# X post by @0xJiuJitsuJerry

## Source

- Original: [https://x.com/0xJiuJitsuJerry/status/2065272983648923954](https://x.com/0xJiuJitsuJerry/status/2065272983648923954)
- Canonical: [https://x.com/0xJiuJitsuJerry/status/2065272983648923954](https://x.com/0xJiuJitsuJerry/status/2065272983648923954)
- Author: 0xJiuJitsuJerry (@0xJiuJitsuJerry)

## Verbatim Text

The Week AI Went Public, Pumped the Brakes, and Rewrote Mathematics

June 11, 2026

Picture this: it's Monday morning. You pour your coffee. You open your feed. And in the span of five days, the company that brought you ChatGPT files to go public at a potential trillion-dollar valuation, its biggest rival begs the world to slow down before humans lose control, NVIDIA drops a foundation model for robots that actually move things in the real world, Apple finally makes Siri useful, and a machine disproves a math problem that has stumped the brightest minds for eighty years.

That was the week of June 4–10, 2026. Let's walk through it together — first in plain English anyone can understand, then with the technical depth that builders, architects, and AI creators actually need.

## The Simple Version: What Just Happened

The Money Moment

@OpenAI — the company behind ChatGPT — filed secret paperwork to go public. Going public means anyone could soon buy a piece of the company on the stock market, just like you can buy Apple or Tesla stock. This is a big deal because OpenAI was last valued at $852 billion. Yes, billion. For context, that's more than the entire economies of most countries. They're making about $2 billion every month from ChatGPT subscriptions and advertising. Their competitor, Anthropic (makers of Claude), filed a week earlier and is valued even higher — around $965 billion.

Why should you care? Because when companies this big and this important go public, they have to open their books. For the first time, we'll see how much it actually costs to build frontier AI.

The Warning Bell

That same competitor — @AnthropicAI — published something extraordinary on June 4: a public call asking the entire AI industry to consider hitting pause. Not because they're losing. Because they're scared of what they're seeing.

Their AI assistant, Claude, now writes roughly 80% of all the code Anthropic produces. In April, Claude agents completed an entire AI safety research project — coming up with hypotheses, running experiments, iterating on results — with humans only picking the topic. The worry is something called "recursive self-improvement": AI systems that can design and build even smarter AI systems, without humans in the loop. Once that feedback loop starts, it may be very hard to stop.

Anthropic isn't saying "shut it all down forever." They're saying: let's coordinate — globally, verifiably — so no country or company secretly races ahead while others pause. It's the most detailed slowdown proposal ever to come from inside a top AI lab.

The Robot Brain

@nvidia, the company whose chips power most of the AI revolution, unveiled Cosmos 3: a single AI model that can understand text, images, video, sound, and robot movements all at once. Think of it as a foundation model — like #GPT for language — but for the physical world. It can watch a video of a factory floor and predict what should happen next. It can generate training data for robots that need to learn how to pick up objects they've never seen before.

NVIDIA made it fully open. Anyone can download the weights, study the code, and build on top of it. That's a big deal in a world where most powerful AI models are locked behind APIs and paywalls.

The Personal AI Computer

#NVIDIA also announced #RTXSpark — a new kind of computer chip designed to run powerful AI entirely on your device, with no internet connection needed. It has 128GB of memory shared between the CPU and GPU, so it can load massive AI models without breaking a sweat. The first laptops and desktops with RTX Spark arrive this fall, from ASUS, Dell, @Microsoft, Lenovo, and others. Expect to pay $4,500 and up.

The pitch: your own personal AI agent, running locally, fully private, no monthly subscription. For anyone who's been building AI on Mac Minis and Raspberry Pi clusters, this is the next rung on the hardware ladder.

The Apple Intelligence Shift

At WWDC 2026, @Apple finally showed its cards. Siri got a complete overhaul — now called Siri AI — and it's powered by Google's Gemini models under the hood. That's right: Apple partnered with Google on AI. The new Siri has a dedicated app, remembers your conversations across devices via iCloud, and can actually understand what's on your screen.

Image Playground now generates photorealistic images, and the Photos app can reframe your pictures as if you'd taken them from a different angle. Every AI-generated or AI-edited image gets a SynthID watermark — an invisible tag that says "an AI made this." Apple is the first major platform to build that labeling into the operating system itself.

The Math Problem That Fell

Here's the one that should make you pause. In 1946, the legendary mathematician Paul Erdős posed a puzzle about points on a plane and distances between them. For eighty years, the brightest minds assumed the answer involved square grids. They were wrong.

OpenAI's reasoning model looked at the problem and — drawing on a branch of mathematics called algebraic number theory that no human had connected to this puzzle — found a completely different approach. It produced a valid disproof in about five days. External mathematicians, including Fields Medalist Tim Gowers, verified it.

At almost the same moment, Google DeepMind's AlphaProof Nexus solved nine Erdős problems using formal verification — mathematical proofs checked by a system called Lean, which guarantees there are no hidden errors.

But nearly 2,000 mathematicians responded by signing the Leiden Declaration: a warning that AI threatens research integrity, that AI-generated proofs can look right but be wrong, and that we need new rules for how math gets done. Even Terence Tao — widely considered one of the greatest living mathematicians — has become an advocate for AI-assisted mathematics.

## The Technical Layer: What Builders Need to Know

OpenAI's IPO and the Economics of Frontier AI

OpenAI's S-1 (still confidential) will be the single most important document in AI economics when it drops. Here's what matters technically:

- Revenue mix: ~$2B/month appears split between ChatGPT subscriptions (Plus/Pro/Go tiers), enterprise API usage, and the ads pilot. The ads pilot hit $100M annual run rate in under 6 weeks — that's the fastest monetization velocity I've seen in enterprise AI. If ad revenue scales, it changes the incentive structure: optimizing for attention, not just capability.

- Compute costs: Projected >$100B cash burn by 2029 implies massive infrastructure investment. OpenAI is developing custom silicon to reduce dependence on cloud providers (likely NVIDIA). The chip strategy will determine gross margins.

- The Anthropic parallel: Anthropic filed first and carries a higher current valuation ($965B vs $852B). Anthropic's enterprise-focused strategy (Claude writes 80% of their code, deployed in enterprise, safety-first positioning) may look more sustainable to institutional investors. OpenAI's consumer-advertising pivot introduces volatility.

- The AGI timeline: Altman's "automated AI researcher by 2028" goal is either visionary or wildly optimistic. For context: Claude agents completing an AI safety research project autonomously suggests the capability is closer than skeptics think, but scaling from a single domain to general research is a different beast entirely.

Anthropic's Pause Proposal: Technical Signals

The June 4 blog post is worth reading in full. The technical landmarks:

- Code throughput: Claude generates ~80% of Anthropic's production code. That's not code completion — that's agentic software engineering. The remaining 20% is likely architecture, review, and integration. If your AI isn't writing most of your code yet, know that the frontier labs are already there.

- Autonomous research: The April 2026 safety research project is a milestone. Claude agents proposed hypotheses, designed experiments, ran tests, and iterated — all in parallel. The human role was setting the topic and scoring rubric. This is the "automated AI researcher" capability that OpenAI is targeting for 2028, already working (in a narrow domain) at Anthropic.

- Recursive self-improvement: The term is precise. It's not just "AI helping build AI" — that's been happening for years with chip design, code generation, and hyperparameter tuning. Recursive self-improvement means an AI system that can design, train, and deploy a successor system that is more capable than itself, without human intervention in the loop. Anthropic believes they're approaching that threshold.

- Verification challenge: The hardest part of a coordinated pause is verifying compliance. Training runs are easier to conceal than missile silos. Anthropic proposes building verification infrastructure first, then pausing. This is a "trust but verify" framework that acknowledges the enforcement problem directly.

Cosmos 3: Architecture Notes for Physical AI Builders

Cosmos 3's Mixture-of-Transformers architecture deserves attention:

- Dual-mode design: An autoregressive transformer for reasoning (perception, planning, world modeling) and a diffusion transformer for generation (images, video, audio, action trajectories). This separation lets the model think before it acts — it reasons about physics first, then generates output.

- 3D mRoPE: A shared 3D rotary position embedding across modalities. This is the secret sauce for consistent spatial reasoning across text, video, and action spaces. If you're working on embodied AI, this is the embedding technique to study.

- Open weights: No API gate. Download, fine-tune, deploy. The 16B Nano variant runs on consumer GPUs. The 64B Super variant is for training pipelines and offline synthetic data generation. Edge (coming soon) targets real-time on-device inference for robots.

- Training data advantage: Cosmos 3 was trained on multimodal data that includes physics simulations, robot trajectories, and real-world video. The synthetic data generation capabilities mean you can bootstrap robot learning with far less real-world data than before.

RTX Spark: Local AI Infrastructure

For those running local AI clusters (Mac Mini M4, Raspberry Pi, custom rigs), RTX Spark changes the math:

- Unified memory architecture: 128GB shared between CPU and GPU via NVLink-C2C, eliminating PCIe bottlenecks. This means you can load very large models (Llama 4-class, large diffusion models) without quantization compromises. No more splitting models across devices or settling for 4-bit quantized versions.

- On-device agents: The AI Hosting Runtime manages deployment across CPU, GPU, and NPU tiles. Agents run locally, sandboxed, with no cloud dependency. This is the privacy-first AI compute model that Apple Intelligence gestures toward but NVIDIA is building the hardware for.

- Price point: $4,500-$6,500 is steep for hobbyists but competitive for professional workstations. The question is whether the software ecosystem (Windows on Arm, AI agent frameworks) matures fast enough to justify the premium over a Mac Studio or Mac Mini cluster.

Apple's Foundation Model Strategy

Apple's WWDC reveals are technically nuanced:

- Gemini partnership: Apple is using @Google's Gemini models to power Siri AI, not their own on-device models for the heavy lifting. This is a concession that Apple's foundation model development has lagged. The privacy story (Private Cloud Compute) means Apple is acting as a trusted intermediary between your device and Google's cloud — a complex architecture that's either brilliant or brittle.

- SynthID watermarking: Apple is embedding Google DeepMind's SynthID into all AI-generated and AI-edited images at the OS level. This is invisible to users but detectable by tools. It's the first platform-level content authenticity mandate. Expect this to become standard across ecosystems.

- AFM 3 family: Apple's own foundation models (AFM 3, Cloud Pro variants) run on Apple Silicon for on-device tasks and NVIDIA GPUs in Apple's cloud for server-side generation. The hybrid inference architecture is similar to what Microsoft is building with Project Solara — push what you can to the edge, burst to cloud for heavy lifts.

AI Mathematics: Disproof and Its Discontents

The Erdős unit-distance disproof is technically fascinating:

- The approach: The model didn't use geometry at all — it applied algebraic number theory, specifically infinite class field towers and Golod-Shafarevich theory, to construct point configurations with more unit-distance pairs than any grid arrangement. This cross-domain leap is something human mathematicians describe as "creative" — and is exactly the kind of reasoning that traditional ML benchmarks don't test for.

- The verification gap: Google DeepMind's AlphaProof Nexus took a different path — formal verification via Lean, which produces machine-checkable proofs that are guaranteed correct. OpenAI's approach produced a result validated by human experts but without formal verification. The Leiden Declaration signatories are worried about the former: plausible outputs that pass human review but contain hidden errors.

- The Tao inflection: Terence Tao's evolution from skeptic to advocate is the human story here. He sees AI as a tool for "decomposable" problems — break a big conjecture into thousands of small subproblems, let AI handle those, and have humans tackle the irreducible core. Formal verification (Lean) is the bridge that makes this trustworthy.

## What This Week Means

We're in a moment where the money, the hardware, the software, and the governance debate are all accelerating in parallel — but not at the same speed. The money is moving fastest (two mega-IPOs in a month). The hardware is close behind (Cosmos 3, RTX Spark shipping this fall). The capabilities are unnerving even their creators (Anthropic's pause call). And the governance is… a declaration signed by mathematicians and a blog post from a company that also wants to go public.

The gap between what we can build and what we've agreed to be careful about is the widest it's ever been. For those of us building in this space — whether on Mac Minis, Raspberry Pi clusters, or RTX Sparks — that gap is also where the most important work lives.

This article was researched and written by the Morning Intel Swarm (Research → Code → Creative Agents) for @0xJiuJitsuJerry on June 11, 2026. It's designed to be useful whether you're just getting into AI or you're already running your own models at home.

## X Article Metadata

- Title: The Week AI Went Public, Pumped the Brakes, and Rewrote Mathematics
- Preview: June 11, 2026
Picture this: it's Monday morning. You pour your coffee. You open your feed. And in the span of five days, the company that brought you ChatGPT files to go public at a potential

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
