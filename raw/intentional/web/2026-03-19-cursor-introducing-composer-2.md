---
type: raw_capture
source_type: web
title: "Introducing Composer 2"
url: "https://cursor.com/blog/composer-2/"
canonical_url: "https://cursor.com/blog/composer-2/"
vendor_blog: cursor
published_at: 2026-03-19
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Introducing Composer 2
Original URL: https://cursor.com/blog/composer-2/
Published: 2026-03-19
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [research](/blog/topic/research)

Mar 19, 2026·[research](/blog/topic/research)

# Introducing Composer 2

3 min read

Composer 2 is now available in Cursor.

It's frontier-level at coding and priced at $0.50/M input and $2.50/M output tokens, making it a new, optimal combination of intelligence and cost. We also released a [technical report](https://arxiv.org/abs/2603.24477) on how we trained it.

![Composer 2 efficiency and quality on CursorBench](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-2-scatter-r4.png&w=1920&q=70)![Composer 2 efficiency and quality on CursorBench](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-2-scatter-r4-dark.png&w=1920&q=70)

## [#](#frontier-level-coding-intelligence)Frontier-level coding intelligence

We're rapidly improving the quality of our model. Composer 2 delivers large improvements on all [benchmarks we measure](/blog/cursorbench), including Terminal-Bench 2.0[1](#fn-1) and SWE-bench Multilingual:

![Composer 2 Terminal-Bench 2.0 results](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-2-terminal-bench-score-r9.png&w=1920&q=70)![Composer 2 Terminal-Bench 2.0 results](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-2-terminal-bench-score-r9-dark.png&w=1920&q=70)

| Model | CursorBench | Terminal-Bench 2.0 | SWE-bench Multilingual |
| --- | --- | --- | --- |
| Composer 2 | 61.3 | 61.7 | 73.7 |
| Composer 1.5 | 44.2 | 47.9 | 65.9 |
| Composer 1 | 38.0 | 40.0 | 56.9 |

These quality improvements come from our first continued pretraining run, which provides a far stronger base to scale our reinforcement learning.

From this base, we train on [long-horizon](/blog/self-driving-codebases) coding tasks through [reinforcement learning](/blog/self-summarization). Composer 2 is able to solve challenging tasks requiring hundreds of actions.

## [#](#try-composer-2)Try Composer 2

Composer 2 is priced at $0.50/M input and $2.50/M output tokens.

There is also a **faster variant with the same intelligence** at $1.50/M input and $7.50/M output tokens, which has a lower cost than other fast models[2](#fn-2). We're making fast the default option. See our [model docs](/docs/models/cursor-composer-2) for full details.

![Composer 2 fast variant speed and cost compared to other models](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-speed-cost-r12.png&w=1920&q=70)![Composer 2 fast variant speed and cost compared to other models](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcomposer-speed-cost-r12-dark.png&w=1920&q=70)

On individual plans, Composer usage is part of a [standalone usage pool](https://cursor.com/docs/models-and-pricing#usage-pools) with generous usage included. Try Composer 2 today in Cursor or in the early alpha of our [new interface](https://cursor.com/glass).

---

1. Terminal-Bench 2.0 is an agent evaluation benchmark for terminal use maintained by the Laude Institute. Anthropic model scores use the Claude Code harness and OpenAI model scores use the Simple Codex harness. Our Cursor score was computed using the official [Harbor evaluation framework](https://github.com/laude-institute/harbor) (the designated harness for Terminal-Bench 2.0) with default benchmark settings. We ran 5 iterations per model-agent pair and report the average. More details on the benchmark can be found at the official [Terminal Bench website](https://www.tbench.ai/). For other models besides Composer 2, we took the max score between the [official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) score and the score recorded running in our infrastructure. [↩](#fnref-1)
2. Tokens per second (TPS) for all models are from a snapshot of Cursor traffic on March 18th, 2026. Token sizing for Composer and GPT models are similar. Anthropic tokens are ~15% smaller and the TPS number is normalized to reflect that. Similarly, output token price for non-Anthropic models was scaled to match the same ~15% change. Speed may vary depending on provider capacity and improvements over time. [↩](#fnref-2)

Filed under: [research](/blog/topic/research)

Author: Cursor Team
