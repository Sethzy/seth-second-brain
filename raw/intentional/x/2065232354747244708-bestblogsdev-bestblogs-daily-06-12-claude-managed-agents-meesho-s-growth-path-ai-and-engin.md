---
type: raw_capture
source_type: x
url: https://x.com/BestBlogsDev/status/2065232354747244708
original_url: https://x.com/BestBlogsDev/status/2065232354747244708
author: "BestBlogs"
handle: BestBlogsDev
status_id: 2065232354747244708
captured_at: 2026-06-19T23:58:36+08:00
published_at: "Fri Jun 12 00:38:58 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 0
  reposts: 1
  likes: 7
---

# X post by @BestBlogsDev

## Source

- Original: [https://x.com/BestBlogsDev/status/2065232354747244708](https://x.com/BestBlogsDev/status/2065232354747244708)
- Canonical: [https://x.com/BestBlogsDev/status/2065232354747244708](https://x.com/BestBlogsDev/status/2065232354747244708)
- Author: BestBlogs (@BestBlogsDev)

## Verbatim Text

BestBlogs Daily · 06-12 · Claude Managed Agents, Meesho's Growth Path, AI and Engineering Jobs

[Read this brief online](https://www.bestblogs.dev/en/explore/brief/2026-06-12)

## Intro

Three threads worth following today. The first is about agent infrastructure: Anthropic is rethinking how production agents should be built by separating the reasoning loop from the sandbox where code actually runs. The second is a founder's story of radical pivots: how Meesho rebuilt itself three times on the way to becoming India's biggest shopping app, including a contrarian bet that nearly broke its own network in order to grow it. The third pushes back on a popular narrative — that AI is quietly replacing software engineers — by looking at what the layoff data actually shows. Beyond these three deep reads, today's quick takes cover an agent-harness conversation with Google DeepMind's Logan Kilpatrick, a new way to detect hidden "sleeper agent" behaviors in language models, a rocky launch for Google's Antigravity 2.0, engineering teams rethinking their AI spend, a hands-on cost comparison of agentic coding setups, a CEO's case for owning AI transformation personally, and a fresh take on what business intelligence needs next.

## Deep Dive 1: The evolution of agentic surfaces: building with Claude Managed Agents | Claude

When Anthropic first opened the Claude API to developers in 2023, the contract was simple: you sent a prompt, Claude returned a completion, and your application decided what happened next. That was enough for single-turn work like summarizing documents or classifying tickets. But over time, people wanted Claude to carry a task all the way through — look something up, act on it, see what changed, and decide what to do next, ideally operating inside the systems work already runs on, like a codebase or a ticketing system. Doing that with the raw API meant building your own loop: ask the model what to do, run the tool, feed the result back, repeat. Claude Code, the agentic coding tool Anthropic launched in 2025, packaged that loop — tool execution, subagents, context management — into a working harness, and the Claude Agent SDK later let developers build on the same machinery instead of maintaining a homegrown one.

Even with a tuned harness, though, moving an agent into production raises a separate set of problems: where does it run, how does a multi-hour task survive an interruption, what happens to its filesystem between runs, what's the blast radius if the code it writes goes wrong, how does it reach your credentials without exposing them to generated code, and can you reconstruct what it did after the fact. Anthropic's read is that many of these problems trace back to one architectural choice — agent harnesses that run inside the same container as the filesystem they operate on, so the container has to spin up before Claude can even start thinking, and the agent sits right next to your credentials.

Claude Managed Agents addresses this by decoupling the harness that calls Claude from the sandbox where code executes, connecting the two through a resumable, append-only session log of every model call, tool call, and result. Claude can start reasoning before any sandbox exists, credentials live in a separate vault that generated code never sees directly — protected with envelope encryption and released only against a signed request token — and a run can be reconstructed from its session log at any point. In Anthropic's own testing, this cut time-to-first-token by roughly 60% in the median case and by more than 90% in the slowest cases, because sessions that never need a tool can skip spinning up a sandbox entirely.

The system is built around three resources: an agent (model, prompt, tools, and guardrails), an environment (the sandbox, its networking rules, and pre-installed packages, hosted on Anthropic's cloud or your own infrastructure), and a session (a single run pairing an agent with an environment, with its full event history and outputs persisted server-side). That persistence is also what powers features like Memory and Dreaming, a scheduled process that reviews past sessions to curate memories so agents improve over recurring tasks. For teams that want tool execution to stay inside their own network, self-hosted sandboxes and MCP tunnels let the code, filesystem, and network egress never leave their environment while Anthropic still manages the harness.

This connects to a pattern showing up across today's other stories: infrastructure choices that look like implementation details — where state lives, what a harness assumes about a model's behavior — end up shaping how fast a team can ship and how safely they can scale. If you're evaluating agent platforms or trying to decide how much custom harness work is worth maintaining in-house, this is a useful primer on what "production-ready" actually requires beyond a good prompt. Read it on [BestBlogs](https://www.bestblogs.dev/article/8e6ddfdf).

## Deep Dive 2: How Meesho Became India’s Biggest Shopping App

In a live interview with Y Combinator, Meesho co-founder Vidit Aatrey traces the company's path from a failed local-store directory to processing roughly 2.5 billion orders a year for 250 million consumers and nearly a million independent merchants. The story is less about a single insight than about three full product rebuilds, each forced by watching what users actually did rather than what they said they wanted.

The founders started in 2015 after noticing a stark gap: corporate India assumed e-commerce was a solved problem dominated by Amazon and Flipkart, but 85% of the country's GDP ran through small local retail shops that were completely outside the digital economy. Their first product, "Fashion Nearby," let brick-and-mortar clothing vendors list inventory for a neighborhood radius — and it died within three months, because the founders had only interviewed store owners and never validated demand with consumers. A restricted local directory offered neither the selection of e-commerce nor the immediacy of walking into a store.

The second version came from watching rather than asking: the founders spent weeks sitting quietly in retail storefronts and noticed shopkeepers were already running informal e-commerce through manual WhatsApp groups. Meesho — short for "Meri Shop," or "My Shop" — became a plugin to manage inventory and payments inside those WhatsApp loops. It onboarded hundreds of thousands of storefronts and got the company into Y Combinator, but hit a wall: traditional merchants wouldn't pay a recurring SaaS fee for logistics software. The data, however, revealed a different power-user group — online drop-shippers with no physical storefront, often homemakers building zero-capital businesses from home. Meesho pivoted again into Meesho Supply, a marketplace connecting these drop-shippers directly to wholesale vendors, and transaction volume doubled monthly without any marketing spend.

Between 2016 and 2020, this WhatsApp-based model was also a deliberate response to India's expensive mobile data: standard shopping apps with heavy image-loading drained data plans and got uninstalled, while WhatsApp's compressed, text-first format kept costs low enough for budget-conscious rural users to stay engaged. By 2020, Meesho had scaled to 10 million active sales groups reaching an estimated 100 million buyers.

Then, in 2021, the conditions that justified that whole model disappeared: data costs collapsed toward zero and pandemic lockdowns forced rural users online directly. Aatrey made what he describes as a highly controversial call — cannibalizing Meesho's own reseller network to go direct-to-consumer, fully aware that "all these drop shippers are going to hate you because you're intermediating them" and that a half-hearted experiment would be lose-lose. Despite board skepticism, Meesho launched its standalone consumer app on July 5, 2021, hit #1 in the Play Store's shopping category within 48 hours, and grew from 10 million sellers to 100 million end-consumer monthly active users in five months.

Looking ahead, as Meesho targets India's full billion-consumer base, Aatrey frames generative AI as a transformation on the scale of that 2021 pivot. The company has built Wani, a voice-first AI shopping agent aimed at users who find typed search, star ratings, and digital checkouts intimidating — letting people browse, choose, and pay entirely by speaking in their regional dialect. The throughline across all four versions is the same: Meesho kept its mission constant (bringing commerce to underserved consumers) while being willing to discard the product, and even the customer segment, whenever the evidence pointed elsewhere. Watch the full conversation on [BestBlogs](https://www.bestblogs.dev/video/d607641).

## Deep Dive 3: Why AI hasn’t replaced software engineers， and won’t

This essay from AI as Normal Technology takes direct aim at one of the most repeated claims of 2026 — that AI is already causing mass layoffs of software engineers — by checking it against the cases most often cited as evidence, and finding the narrative doesn't hold up.

Start with three headline stories. In February, fintech company Block cut 4,000 jobs, with founder Jack Dorsey framing it around AI "enabling a new way of working" with "smaller and flatter teams." But subsequent reporting told a different story: Block had tripled headcount during the pandemic and was under heavy financial pressure, and an employee who refused a 75% retention raise to quit said the company had "shoved AI down everyone's throats" with "very limited gains in productivity." In April, Snap laid off about 1,000 people, with CEO Evan Spiegel citing AI and noting that AI generated 65% of new code — but the cuts followed a campaign from an activist investor demanding cost reductions, and the roles cut (including 150 in augmented reality) didn't track the pattern you'd expect from AI-driven cuts. In May, Intuit cut 3,000 roles alongside new deals with Anthropic and OpenAI, and press coverage connected the two — but Intuit's CEO explicitly pushed back, saying "none of it had to do with AI" and that the cuts targeted "coordination-heavy roles" and excess management layers.

The essay calls this pattern "AI washing," and argues it's economy-wide: 59% of U.S. hiring managers admit they cite AI for layoffs because it plays better with stakeholders than financial constraints, and a Forrester analyst notes that when companies announcing AI-driven layoffs are asked if they actually have a mature AI system ready to fill the gap, the answer is no nine times out of ten. The hardest data point comes from New York's WARN Act filings, which added an AI-disclosure checkbox in March 2025: in the first full year, of roughly 25,000 laid-off workers in the state, only 46 — about two-tenths of a percent — were tied to AI.

The essay's explanation for why this keeps happening rests on what it calls the "decide-execute-deliver sandwich." Software engineering work breaks into deciding what to build, executing the implementation, and being accountable for delivering it — with deep understanding of the codebase and business underlying all three. AI has compressed the execute layer dramatically: one study across 100,000 GitHub developers found AI agents led to an eight-fold increase in lines of code written, but only a 30% increase in releases, because the decide and deliver layers remain bottlenecks that don't move at the same pace. The essay also draws a sharp line between "vibe coding" (telling an agent what to do without supervising or reviewing it) and "agentic engineering" (using agents as tools while staying accountable for output) — noting that in one dataset, only 44% of agent-produced code survived into user commits, and vibe-coded commits introduced security vulnerabilities at nine times the human-only rate.

The piece lands on cautious optimism: because software is highly responsive to price (cheaper software means people build more of it), and because AI doesn't substitute well for human decision-making and accountability, demand for software engineers may grow rather than shrink even as AI reshapes how the work gets done — much like how cheaper compute didn't shrink the need for engineers, it expanded what they could build. Read the full piece on [BestBlogs](https://www.bestblogs.dev/article/28a90882).

## Quick Takes

[Google DeepMind's Logan Kilpatrick: Why the Model Eats the Harness](https://www.bestblogs.dev/video/568d29c) — In this Sequoia Capital conversation, the lead of Google AI Studio and the Gemini API explains why Google is rebuilding its product lineup around what he calls an "anti-gravity agent harness" — a shared layer spanning IDE, web, CLI, and SDK that lets consumer and developer tools run long-horizon agentic workflows. The bigger theme is that capabilities developers used to build themselves keep getting absorbed into the model and its harness over time, and Kilpatrick discusses where that leaves room for startups to differentiate as that boundary keeps moving.

[You Can Catch Sleeper Agents by Teaching Another Model to Imitate Them](https://www.bestblogs.dev/article/86a5e7ba) — This LessWrong write-up of a new preprint introduces "activation-matched finetuning": train a clean reference model to match a suspect model's internal activations on ordinary, benign prompts, and whatever the reference can't reproduce is where hidden behavior lives. The leftover signal spikes sharply on trigger prompts and even on prompts that are merely related to the trigger, which the authors show can make it possible to search for the trigger itself rather than just confirming a backdoor exists.

[The Pulse: Antigravity 2.0 takes 'IDE' out of its new IDE](https://www.bestblogs.dev/article/bca3a4c2) — The Pragmatic Engineer's Gergely Orosz reviews Google's relaunch of Antigravity, the AI IDE Google built after acquiring most of the Windsurf team. The new "Antigravity 2.0" drops the IDE interface entirely in favor of something that resembles Codex's desktop app, while a separate "Antigravity IDE" still exists — creating confusing dual installations, an update flow that silently switches users between the two, and what Orosz describes as a rushed, sloppily reviewed launch that raises questions about Google's ability to ship credible developer tools.

[The Pulse: a trend of trying to cut back on AI spend within eng departments?](https://www.bestblogs.dev/article/3d0b654a) — Also from The Pragmatic Engineer, this piece tracks a growing pattern of engineering leaders scrutinizing and trimming AI tooling budgets, because the link between heavy AI tool usage and actual shipped features remains hard to demonstrate. The timing is notable: shortly after this analysis circulated, OpenAI's CEO separately acknowledged that AI costs have become a serious budgeting issue for some companies, echoing the same concern from the other side of the table.

[Fable vs Fable+Subagents vs Fable+Chinese Models: A Cost-Benefit Experiment](https://www.bestblogs.dev/status/2065154347730710783) — A detailed hands-on experiment compares three approaches to using Claude Fable for building a Minecraft clone: plain Fable, Fable with subagents, and Fable paired with cheaper Chinese-developed models for routine work. The results show a clear quality gradient where more expensive setups produce better code, but also make the case that cheaper alternatives are good enough for the bulk of everyday tasks — useful framing for anyone trying to manage agentic coding costs without sacrificing output on the parts that matter most.

[The CEO Must Be the Chief AI Officer](https://www.bestblogs.dev/video/03f412f) — On Y Combinator's The Light Cone, Brex co-founder and CEO Pedro Franchesci argues that AI transformation can't be delegated — it has to be driven by the CEO directly, because it requires rethinking how the whole organization works, not just bolting a chatbot onto existing processes. He shares how Brex built and open-sourced Crab Trap, a tool for securing enterprise agents at the network level, and lays out a three-tier framework — Product AI, Operational AI, and Corporate AI — for thinking about where AI investment should go.

[BI Is Dead, Long Live BI](https://www.bestblogs.dev/article/96bb500d) — This Towards Data Science piece argues that the long-standing bottleneck in data-driven decision-making was never query speed or dashboard availability — it was knowing which questions to ask in the first place. The author proposes a "business intent layer," powered by AI agents that sit between raw data and decision-makers, translating business questions into the right analyses automatically. It's a useful frame for anyone whose org has plenty of dashboards but still struggles to turn data into decisions.

## More Reads

Today's slate is concentrated in three deep reads and seven quick takes above, which together cover the day's most substantive threads — agent infrastructure, a founder's growth story, and the AI-jobs debate, plus a cluster of shorter pieces on agent harnesses, AI safety research, developer tooling, and AI spending discipline. Start with the Intro and Quick Takes above for the fuller picture of today's news.

## Reading Path

If you only have time for three things today: start with Deep Dive 3 (Why AI hasn't replaced software engineers, and won't) for the clearest counter-narrative to the AI-jobs panic, then read Deep Dive 1 (Claude Managed Agents) to see the infrastructure thinking behind the agents that essay is talking about, and finish with Deep Dive 2 (How Meesho Became India's Biggest Shopping App) as a grounding case study in how a real company navigates exactly this kind of platform shift — repeatedly rebuilding itself rather than betting everything on one idea. If you have a few more minutes, the Quick Takes on Antigravity 2.0 and AI spending add useful context on how the rest of the industry is reacting to the same pressures.

BestBlogs is an AI-powered personal reading assistant that helps you build a stable, trusted, and personalized flow of high-quality information. It helps you decide what is worth reading, understand it faster, and gradually learn what you care about.

## X Article Metadata

- Title: BestBlogs Daily · 06-12 · Claude Managed Agents, Meesho's Growth Path, AI and Engineering Jobs
- Preview: Read this brief online
Intro
Three threads worth following today. The first is about agent infrastructure: Anthropic is rethinking how production agents should be built by separating the reasoning

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
