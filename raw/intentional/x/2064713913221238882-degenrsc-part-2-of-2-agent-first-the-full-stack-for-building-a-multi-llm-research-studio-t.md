---
type: raw_capture
source_type: x
url: https://x.com/degenrsc/status/2064713913221238882
original_url: https://x.com/i/status/2064713913221238882
author: "Rohit Chauhan"
handle: degenrsc
status_id: 2064713913221238882
captured_at: 2026-06-19T23:58:04+08:00
published_at: "Wed Jun 10 14:18:52 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 4
  likes: 34
---

# X post by @degenrsc

## Source

- Original: [https://x.com/i/status/2064713913221238882](https://x.com/i/status/2064713913221238882)
- Canonical: [https://x.com/degenrsc/status/2064713913221238882](https://x.com/degenrsc/status/2064713913221238882)
- Author: Rohit Chauhan (@degenrsc)

## Verbatim Text

Part 2 of 2: Agent-First: The Full Stack for Building a Multi-LLM Research Studio That Runs Itself

This is part 2 of 2 of the Agent-First: The Full Stack for Building a Multi-LLM Research Studio That Runs Itself article.

The X article system ran out of characters before I could post the whole thing. Read Part 1 first before reading this.

Part 1 of 2 can be found here 👇

[Embedded Tweet: https://x.com/i/status/2064714047241736302]

# The CMC creator post

as a verified creator post after the primary platform and the X cross-post.Token research only. Published on[coinmarketcap.com](https://coinmarketcap.com/)

Format rules:

- Under 2,000 characters, hard limit

- Same voice as the main note, no softening for a broader audience

- Lead with the sharpest data point in the note, not a summary of what the article covers

- Conviction tier at the close: HIGH, MEDIUM, or SPECULATIVE

- Entry zone and stop if there is a trade setup, omit if not

- No em dashes

- Save the draft as `research/outputs/[token]-cmc-post.md` before publishing manually

The CMC post is not a truncated version of the main note. It is the note’s sharpest argument compressed into a standalone piece. A reader who only sees the CMC post should understand the thesis, the key data point, the risk, and the conviction level.

# Publishing stacks by platform

ROCH Labs:

) is the primary record. Every long-form essay publishes there first.Substack ([rochlabs.com](https://rochlabs.com/)

) follows with a screen-share walkthrough of the same article. Not a separate script, a live screen-share with verbal commentary over the written piece. Same content, different medium, different discovery surface.YouTube ([@rochlabs](https://x.com/@rochlabs)

) gets two versions: a native X article (the Substack essay reformatted for X) and a truncated standalone post. The native video from the YouTube walkthrough is uploaded directly to X, never as a YouTube link. X suppresses external links in the algorithm. Native video is treated differently.X ([@degenrsc](https://x.com/@degenrsc)

Coin Bureau:

-feed for equity and macro.CB Discord is the primary channel.[#degen](https://x.com/search?q=%23degen&src=hashtag_click)-shots for token research.[#research](https://x.com/search?q=%23research&src=hashtag_click)

X cross-post goes out the same day, same note, no delay.

CMC creator post goes out for all token research, same day.

The separation between CB and ROCH Labs content is structural. CB content does not automatically become ROCH Labs content. Cross-pollination, taking a CB thesis and developing it into a longer ROCH Labs essay, requires a conscious decision, and the ROCH Labs version is written from scratch rather than republished.

# What the operations layer gives you

A published note with no tracker update is a research event with no institutional memory. Six months later, there is no way to know whether the thesis worked, what the entry and stop were, or whether the system is improving.

The operations layer, call tracker, trade journal, CMC post, cross-posting sequence, is what turns a content operation into a compounding one. The tracker builds a track record that is auditable. The trade journal enforces position discipline. The cross-posting sequence ensures every piece reaches every relevant surface. The CMC post builds a verified creator presence on the platform where retail investors actively research tokens.

None of this is glamorous. All of it is what separates a researcher who produces content from a researcher who runs a research operation.

Section 9 covers where this build goes next: the end state of a fully autonomous research studio, what Phase 3 looks like, and the honest timeline for getting there.

# Section 9: The End State

The build has three phases. Phase 1 is complete. Phase 2 is live as of May 2026. Phase 3 is what the next six to twelve months build toward. The sequence matters more than any individual phase. Reversing it, or skipping ahead, produces an automation layer that runs on top of a workflow no one understands, which is the single most common failure mode in this category.

This section documents what is built, what is being built, and what cannot be built until the prior thing is.

# Phase 1: Systemize. Complete. January to May 2026.

The principle that made Phase 1 necessary is the most important sentence in this entire article for anyone thinking about building something like it.

You cannot automate what you have not first systematized.

This is not obvious advice. The default behavior, for anyone who has watched Hermes deliver a morning brief at 6:30 AM, is to want that experience immediately. To spin up a VPS, install the daemon, schedule a cron, and skip the months of manual workflow that preceded it. Most builds in this category fail there. They fail because automating a messy process makes a messy process run faster. The automation does not clean the process. It compounds the entropy at machine speed, and then the operator has a fast, broken pipeline that fails in ways they cannot diagnose because they never understood the process manually in the first place.

Phase 1 of this build ran for four months and produced no automation. It produced a system. The KMS folder structure. The universal project template. The CLAUDE.md hierarchy across global, KMS root, and project levels. The wiki-first discipline. The kill-my-thesis adversarial layer running manually before any wiki was drafted into a note. The voice references. The call tracker. The trade journal. The publishing sequence. The nine-step research workflow with no-skip rules.

By the time Phase 2 began, every step in the workflow had been run manually dozens of times. The failure modes were documented. The gotchas were named. The boring parts were boring enough to be worth automating, and the non-boring parts (thesis selection, kill condition naming, conviction tier assignment, draft review) were obvious as non-automatable because they had been run manually long enough to feel the parts of the process that resist abstraction.

Phase 1 is the part nobody publishes about because it does not look like a system from the outside. There is no daemon. There is no Telegram bot. There are folders and markdown files and a researcher executing a process by hand. From the inside, it is the part that makes everything else possible.

# Phase 2: Automate. Live as of May 2026.

Phase 2 is the part this article has been documenting throughout. What it actually delivers, in honest terms, is narrower than the surface impression of a fully autonomous research studio. Here is what is automated and what is still manual.

What is automated: the morning brief pipeline runs every day at 6:30 AM IST. Six Hermes workers fire in parallel (Grok x_search for overnight CT (W1), three Gemini Flash data workers for crypto, equities, and macro (W2–W4), one Gemini Flash worker for the curated YouTube transcripts (W5), one Gemini Flash worker for web news (W6)), Gemini 2.5 Pro synthesizes the six outputs into a single brief, a Gemini Flash pass validates the synthesis against the underlying worker data and flags hallucinations, and Telegram delivery lands on the phone before the day starts. The same pipeline then runs three internal phases: quality scoring against a rubric, idea extraction into the idea tracker, and wiki updates delegated to Claude Code via a Hermes subprocess call. The evening position alert runs at 7:00 PM IST on the same daemon, pulls live prices for every Open and Watching position in the trade journal, runs a Grok Tier 1 scan for anything notable on the tracked tickers, saves the brief to disk, and pushes it to Telegram. A monthly skills refresh job runs on the first of every month and reports any new Claude Code skills or Anthropic SDK changes worth knowing about.

What is still manual: Llama AI runs in a browser, requires an authenticated session, and cannot run on a Linux VPS, so every Llama AI pull during a research session is a human opening the browser, typing the prompt, waiting, and exporting the markdown. TradingView MCP requires the Mac desktop application launched in remote debug mode, so all chart analysis is a human Mac session. Research sessions themselves are still human-initiated, because the decision about what is worth researching this week is a judgment call that involves the call tracker, the trade journal, the morning brief, the prior conversations with the CB community, and the operator’s own reading of where the market is misallocating attention. And the publishing decision (draft v1 reads strong enough to ship; voice calibration applied for v2; final review passed; tracker updated; cross-post sent) is a human checkpoint at every step.

The honest Phase 2 picture is this. Hermes runs the intelligence infrastructure. The research pipeline still requires a human to initiate and conclude. The leverage is in the hours reclaimed from data collection, monitoring, and the morning intelligence routine that previously consumed two to three hours per day before any actual research could begin. Phase 2 does not run the research. It clears the runway.

Phase 2 took four months from conception to live automation, January through May 2026. The majority of that time was not building. It was running the manual workflow long enough to understand which steps were worth automating, which steps would break under automation, and which steps belonged to the human regardless of how good the tooling got.

# Phase 3: Scale. Six to twelve months out.

Three components are being built toward, in this order.

The first is Llama AI browser automation. This is the next build and the one that removes the only remaining manual bottleneck in the data collection layer. The architecture is documented in the project plan: Hermes opens a browser session via the browser-use Python library, logs into Llama AI with stored credentials, types the research prompt, polls for completion, exports the markdown to the project’s `research/raw/` folder, and pings Telegram when done. First test runs a single session at a time. Once the single-session loop is reliable, the same pattern runs three parallel instances for sector deep dives that pull from multiple protocols simultaneously. When this ships, Phase 1 and Phase 2 readers alike stop spending five to ten minutes per research session on the Llama AI manual loop.

Toccata catalyst`. Hermes interprets the request, fires the targeted MCPs in parallel, runs Grok CT sentiment with a topic string derived from the request, triggers the Llama AI browser pull, hands the raw data set to the synthesis model for wiki building, runs Grok kill-my-thesis on the resulting wiki, drafts a v1 of the note in Sonnet 4.6, and pings Telegram with a link to the draft. The operator opens the draft. The draft is not blank. It is not a placeholder. It is a coherent v1 that needs voice calibration, conviction tier assignment, and a final review before publishing. The work of producing the draft has been done. The work of judging whether the draft should ship has not. That is the right split. One command from topic to draft.The second is a research orchestration skill. A single command that chains the full pipeline end to end. The command, typed into Telegram: `research Kaspa[$KAS](https://x.com/search?q=%24KAS&src=cashtag_click)

The third is parallel specialist agents. A crypto agent, an equity agent, and a macro agent running simultaneously on their domains. Each one runs its own version of the orchestration skill, focused on its domain, with domain-specific MCPs and a domain-specific voice calibration step. The operator reviews and edits the output across all three. Does not produce it. This is the configuration that turns a solo research operation into something that produces output at a volume previously associated with small research teams, while keeping the editorial judgment in one person.

The timeline for Phase 3 is six to twelve months. The bottleneck is not tooling. The browser-use library exists. Hermes can spawn parallel subprocesses. Multi-agent orchestration patterns are documented in public agent frameworks. The bottleneck is the same one Phase 1 made explicit: the discipline of documenting and systematizing each new step before automating it. Llama AI browser automation cannot ship until the manual Llama AI workflow has been documented to the level of detail required for browser-use to replicate it deterministically. The orchestration skill cannot ship until the manual end-to-end pipeline has been run enough times to know where the model routing breaks, where the kill-my-thesis verdict needs to gate progression versus where it can be reviewed asynchronously, and where the human checkpoint cannot be removed. Phase 1 before Phase 2, always. Phase 2 before Phase 3, always.

# What the agent does not replace

Phase 3 is not a fully autonomous research studio in the sense that the operator becomes optional. The judgment calls that remain human are the calls that determine whether the research is worth doing in the first place: what to research, why now, what thesis to build, what conviction tier the evidence supports, when a kill condition has triggered on an open position, when a thesis is salvageable and when it is directionally wrong. None of these are automatable in any near-term version of this build, and an honest description of the system has to name that limit explicitly rather than imply otherwise.

The leverage Phase 3 adds is the elimination of every hour that was previously going to mechanical work. Data collection. Synthesis. First-draft production. Routine monitoring. Cross-posting. Tracker logging. The reclamation of those hours is not marginal. For a solo operator, it is the difference between producing two notes a week and producing eight. The editorial judgment runs at the same rate either way, because the editorial judgment is the constraint that does not scale through tooling.

The researcher does not get replaced. The hours that were not actually research, that were always overhead masquerading as research, get reclaimed.

# The loop, closed

The opening of this article was a single sentence: every research note you write today starts from zero.

That is the condition the system removes.

The note you write today, with the full build running, starts from a project CLAUDE.md updated at the end of the previous session. From a wiki page that has been refined across three prior research passes on the same token. From a morning brief synthesized four hours ago by Hermes from the curated streams. From a kill-my-thesis verdict produced by a model that was deliberately chosen because it cannot see the wiki the way the model that built the wiki sees it. From a call tracker with 41 prior rows that tell you what your thesis quality looks like under outcome data rather than under self-assessment. From a trade journal that knows what your open positions are without you having to remind it. Nothing in that session starts from zero. Everything compounds.

The researchers who build a structured second brain and a systematized workflow will compound their output measurably faster than the researchers who do not. The gap is small now. Most solo operators are still using AI as a chatbot in a browser tab, paying the re-derivation cost every session, watching their research disappear into chat history every time they close the window. By the time Phase 3 is the baseline expectation for competitive solo research operations, which I believe is the second half of 2027 at the latest, the operators who started building this in 2024 will be eighteen months ahead of the operators who started in 2026, in ways that cannot be closed by working harder. Compounding does not work that way.

Build the second brain first. The compounding starts on day one.

Watching closely.

# Appendix: Cost Breakdown

The full monthly cost of the stack, line by line. These are live figures as of May 2026, pulled from actual invoices and API dashboards, not estimates.

# Complete cost table

# The three entry points

Minimum viable stack: ~$51/month

Claude Code Pro ($20) + X Premium Plus for Grok access (~$16) + TradingView Pro ($15).

This gives you: a persistent identity-aware research agent, CT sentiment analysis via Grok’s native X search (included in your X Premium Plus subscription, no separate API cost), and professional chart analysis via TradingView MCP (the MCP itself is free, you pay for the TradingView Pro subscription). Hermes runs locally on your Mac at no additional cost, though you lose it when the machine is off or asleep. It does not include Llama AI or kill-my-thesis adversarial checks. It is the right starting point for the first month while the KMS and research workflow are being built.

One important note on Grok: X Premium Plus gives you Grok 4 access and, through Hermes’s integration with the xAI API, the ability to run real-time X data research from within the Hermes agent. This is not a separate API subscription, it is the same access you already have from your X subscription, wired into the automation layer.

Core research stack: ~$90/month

Minimum viable stack plus Llama AI Pro ($30-50). Kill-my-thesis uses Grok 4, which runs through your existing X Premium Plus subscription at no additional cost.

This is the version that produces research at production quality. The adversarial layer is live. The deepest on-chain data source is accessible. The win rate improvement from the kill-my-thesis layer pays for the additional cost many times over across a year of publishing. This is the stack to run from month two onward.

Full stack: ~$150-200/month

Core stack plus Hermes full automation, morning brief pipeline (Grok W1 via X Premium Plus, Gemini Flash data workers, Gemini Pro synthesis, Gemini Flash validation), evening position alert, and monthly skills refresh. Add a VPS ($6-12) if you want 24/7 availability independent of your local machine, otherwise Hermes runs on your Mac and the cron jobs miss windows when the machine is off.

This is Phase 2. The intelligence infrastructure runs without you. The research pipeline still requires human initiation and judgment. The cost delta from core to full is primarily the Google AI Studio billing for the Gemini morning brief pipeline and the optional VPS. At 30 research notes per month, the Grok cost across CT sentiment and kill-my-thesis runs is covered by your X Premium Plus subscription. Everything else is fixed.

# The progressive build path

Month 1 (~$51): Install Claude Code. Activate X Premium Plus if not already on it (unlocks Grok). Set up TradingView Pro. Build the KMS folder structure. Write the global CLAUDE.md and run the first five research sessions manually end to end. Do not install Hermes yet. Do not set up the morning brief. Run the workflow by hand, slowly, until every step is understood.

Month 2 ($90): Add Llama AI Pro. Run kill-my-thesis on every wiki before drafting, no exceptions. It uses Grok 4 through your existing X Premium Plus subscription, so there is no additional API cost. Note what the adversarial layer catches and what it misses. The win rate data starts accumulating here.

Month 3+ ($200): Install Hermes. Set up the morning brief pipeline. Configure the evening position alert. The automation layer runs on top of a workflow that has been executed manually enough times to understand where it breaks.

The path is Phase 1 before Phase 2. The cost table is designed to be entered progressively, not all at once.

# What free covers

Five of the eight MCPs in the stack cost nothing: FRED, SEC EDGAR, Financial Datasets, Fear & Greed, and Whale Tracker are fully free. CoinMarketCap and Alpha Vantage are free tier with usage limits (333 calls/day and 500 calls/day respectively) that a solo research operation does not exceed when the data scripts are used correctly. All seven are effectively zero cost in practice.

The real cost of the stack is concentrated in five items: Claude Code / Anthropic API, xAI via X Premium Plus for Grok, Google AI Studio for Gemini, Llama AI Pro subscription, and the optional Hermes VPS. Those five items account for roughly 85% of the total monthly cost at full stack.

TradingView Pro is the only MCP-adjacent cost that requires a paid subscription. The MCP itself is free, it connects to your existing TradingView desktop application via remote debug mode. Pro is the minimum subscription tier that provides the chart capabilities used in this stack. Grok access, if you are already on X Premium Plus, costs nothing additional, it is part of that subscription and wires directly into Hermes.

# Conclusion

This is the entire setup, and how I use claude code + Hermes to turn my research work into a fully agent first workflow.

My end game is to build a one-person agentic research studio with multiple agents with their own unique personas - think a trader agent, a macro agent, a prediction market agent, a fundamental analyst agent, a crypto onchain detective agent, a sales agent, a marketing agent, and an operations agent…not to mention an agent who acts like my Chief of Staff.

Still very early in that vision, and might take months to really fructify but I’m in no hurry. One thing is for sure, the agentic workloads have turned me into a better analyst, and it feels like playing a video game w/ multiple agents as your hands and legs as you navigate the game of markets, investing, and research.

Thanks for reading.

## X Article Metadata

- Title: Part 2 of 2: Agent-First: The Full Stack for Building a Multi-LLM Research Studio That Runs Itself
- Preview: This is part 2 of 2 of the Agent-First: The Full Stack for Building a Multi-LLM Research Studio That Runs Itself article. 
The X article system ran out of characters before I could post the whole

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
