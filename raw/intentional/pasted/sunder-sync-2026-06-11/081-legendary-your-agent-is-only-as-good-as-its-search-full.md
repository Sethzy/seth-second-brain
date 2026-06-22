---
type: raw_capture
source_type: x
title: "Sunder sync: legendary-your-agent-is-only-as-good-as-its-search-FULL.md"
url: "https://x.com/Legendaryy"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/legendary-your-agent-is-only-as-good-as-its-search-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/legendary-your-agent-is-only-as-good-as-its-search-FULL.md"
sha256: "c7a91b57253bab5a0ce9e844721a59c3bf7efe83a081a0f43514166c2c51e8aa"
duplicate_of: ""
---

# Sunder sync: legendary-your-agent-is-only-as-good-as-its-search-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/legendary-your-agent-is-only-as-good-as-its-search-FULL.md`

Primary URL: https://x.com/Legendaryy

Duplicate of existing source-map entry: `none`

## Capture Text

# Your Agent Is Only as Good as Its Search

**Author:** Legendary (@Legendaryy)  
**Source:** X Article  
**Date:** February 13, 2026 (7:25 PM)  
**Views at capture:** 54.4K  
**URL:** https://x.com/Legendaryy  

---

## ASCII Image Recreation

### Image #1 - "Five APIs, five philosophies"

```text
+----------------------------------------------------------------------------------------------+
| Five APIs, five philosophies                                                                 |
+-------------------+-------------------+-------------------+-------------------+--------------+
| BRAVE             | TAVILY            | EXA               | PERPLEXITY        | FIRECRAWL    |
| Own index.        | Agent-native.     | Neural semantic   | Sonar API.        | Extract-first|
| LLM chunks.       | Search + extract  | search by meaning | Answers with      | Scrape any   |
| Privacy-first.    | + crawl.          | over keywords.    | citations built in| site, struct |
+-------------------+-------------------+-------------------+-------------------+--------------+
```

### Image #2 - Brave overview card

```text
+-----------------------------------------------------------------------+
| BRAVE OVERVIEW CARD                                                   |
+------------------------------+----------------------------------------+
| PRICING                      | FREE TIER                              |
| $5 / 1K requests             | $5 credit / month                      |
+------------------------------+----------------------------------------+
| INDEX                        | LATENCY                                |
| 35B+ pages (own index)       | <600ms p90                             |
+------------------------------+----------------------------------------+
| MCP SERVER                   | PRIVACY                                |
| Yes (open source)            | ZDR + SOC 2 Type II                    |
+------------------------------+----------------------------------------+
```

### Image #3 - Tavily overview card

```text
+-----------------------------------------------------------------------+
| TAVILY OVERVIEW CARD                                                  |
+------------------------------+----------------------------------------+
| PRICING                      | FREE TIER                              |
| $0.008 / credit              | 1,000 credits / month                  |
| (~$8 / 1K basic)             |                                        |
+------------------------------+----------------------------------------+
| INDEX                        | ENDPOINTS                              |
| Wraps multiple sources       | Search, Extract, Map, Crawl            |
+------------------------------+----------------------------------------+
| MCP SERVER                   | FRAMEWORKS                             |
| Yes                          | LangChain, LlamaIndex, Vercel          |
+------------------------------+----------------------------------------+
```

### Image #4 - Exa overview card

```text
+-----------------------------------------------------------------------+
| EXA OVERVIEW CARD                                                     |
+------------------------------+----------------------------------------+
| PRICING                      | FREE TIER                              |
| $0.005 / search (neural)     | 1,000 free requests / month            |
+------------------------------+----------------------------------------+
| INDEX                        | LATENCY                                |
| Tens of billions (own index) | Sub-350ms (Fast), <200ms (Instant)     |
+------------------------------+----------------------------------------+
| UNIQUE FEATURE               | PAID PLANS                             |
| Semantic similarity search   | $49/mo Starter, $449/mo Pro            |
+------------------------------+----------------------------------------+
```

### Image #5 - Perplexity overview card

```text
+-----------------------------------------------------------------------+
| PERPLEXITY OVERVIEW CARD                                              |
+------------------------------+----------------------------------------+
| SONAR TOKENS                 | SONAR PRO TOKENS                       |
| $1 / $1 per M + req fee      | $3 / $15 per M + req fee              |
+------------------------------+----------------------------------------+
| SEARCH API                   | DEEP RESEARCH                          |
| $5 / 1K requests             | Tokens + per-search charges            |
| (no token cost)              |                                        |
+------------------------------+----------------------------------------+
| CONTEXT WINDOW               | FREE CREDIT                            |
| 128K (Sonar), 200K (Pro)     | $5/mo with Pro subscription            |
+------------------------------+----------------------------------------+
```

### Image #6 - Firecrawl overview card

```text
+-----------------------------------------------------------------------+
| FIRECRAWL OVERVIEW CARD                                               |
+------------------------------+----------------------------------------+
| PRICING                      | FREE TIER                              |
| 1 credit / page, flat rate   | 500 credits (no card)                  |
+------------------------------+----------------------------------------+
| 100K PAGES                   | SELF-HOST                              |
| $83 / month                  | Yes (fully open source)                |
+------------------------------+----------------------------------------+
| JS RENDERING                 | AGENT FEATURES                         |
| Included, no extra cost      | Pagination, auth, forms                |
+------------------------------+----------------------------------------+
```

### Image #7 - Comparison table snapshot

```text
+--------------------+-------------+----------------+----------------------+--------------------+------------------+
| METRIC             | BRAVE       | TAVILY         | EXA                  | PERPLEXITY         | FIRECRAWL        |
+--------------------+-------------+----------------+----------------------+--------------------+------------------+
| Own Index          | 35B+ pages  | No (wraps)     | Yes                  | Yes                | N/A              |
| Search Type        | Keyword+LLM | Keyword+AI     | Neural embeddings    | LLM + search       | Extract only     |
| Cost / 1K Searches | $5          | ~ $8 basic     | $5                   | $5 + tokens        | N/A              |
| Latency (p50/p90)  | <600ms p90  | ~500ms         | <350ms / <200ms      | ~800ms             | Varies           |
| Extraction Quality | Smart chunks| Basic+advanced | Text + highlights    | Synthesized        | Best-in-class    |
| BYO Model          | Yes         | Yes            | Yes                  | No (bundled)       | Yes              |
| Privacy / ZDR      | SOC2 + ZDR  | Governance     | Standard             | API no logging     | Self-hostable    |
| MCP Server         | Yes         | Yes            | Yes                  | Yes (official)     | Yes              |
| Self-host          | No          | No             | No                   | No                 | Yes (OSS)        |
| Free Tier          | $5 credit   | 1K credits     | 1K requests          | $5 w/ Pro          | 500 credits      |
+--------------------+-------------+----------------+----------------------+--------------------+------------------+
```

### Image #8 - Routing table ("Which API for which use case?")

```text
+--------------------------------------------+-----------------------------------------------+
| General web grounding for agents           | RAG pipelines with LangChain                 |
| -> Brave LLM Context                       | -> Tavily                                    |
| Own index, privacy, MCP-ready              | /research endpoint, governance controls       |
+--------------------------------------------+-----------------------------------------------+
| Finding conceptually similar content       | Quick answers with citations                 |
| -> Exa                                     | -> Perplexity Sonar                           |
| Semantic match over keyword match          | Fast synthesized answers                      |
+--------------------------------------------+-----------------------------------------------+
| Deep extraction from known URLs            | Privacy-critical / regulated industries       |
| -> Firecrawl                               | -> Brave (or Firecrawl self-hosted)           |
| JS rendering, auth, pagination             | ZDR + SOC 2 + data sovereignty                |
+--------------------------------------------+-----------------------------------------------+
| Speed-critical loops (50+ searches)        | Autonomous deep research                      |
| -> Exa Fast / Instant                      | -> Perplexity Deep Research (or Tavily)       |
| Sub-200ms paths for high call volume       | Multi-step query expansion                    |
+--------------------------------------------+-----------------------------------------------+
```

---

## Article Transcript

### Your Agent Is Only as Good as Its Search

Brave just dropped the LLM Context API. Tavily ships agent skills. Exa hit sub-200ms. Perplexity Sonar does multi-step research. Five search APIs, five different philosophies. Here is which one to use for what.

### Search is the bottleneck nobody talks about

Everyone is debating which LLM to use for their agent. Claude vs GPT vs Gemini vs the new open-weights models. But there is a more fundamental question most builders skip: where does your agent get its information?

An agent that cannot search well cannot reason well. It does not matter if you are running Opus 4.6 or M2.5 if the search results feeding your model are stale, shallow, or poorly formatted. The model hallucinates. The agent loops. The user gets garbage.

Microsoft killed the Bing Search API in August 2025. That left a gap. Brave, Tavily, Exa, Perplexity, and Firecrawl all rushed in with different answers to the same question: how do you get the web into an LLM efficiently?

The timing of Brave's announcement is worth noting. They dropped the LLM Context API on February 12, the same day MiniMax released M2.5. When open-weight models hit frontier performance at $0.15/task, the quality of search context feeding those models becomes the actual differentiator. Brave's own research backs this up: they showed that a weaker open-weight model (Qwen3) with high-quality search context outperformed ChatGPT, Perplexity, and Google AI Mode.

In a head-to-head evaluation of 1,500 queries, Ask Brave (powered by Qwen3 + LLM Context API) scored a 4.66/5 absolute category rating, beating ChatGPT (4.32), Google AI Mode (4.39), and Perplexity (4.01). Only Grok (4.71) scored higher. Their conclusion: context quality matters more than model capability.

### Five APIs, five philosophies

### Search API overview

### Brave LLM Context API

This is the big one that triggered this breakdown. @brave is not wrapping Google or Bing. They own an independent search index of 35+ billion pages, refreshed with 100+ million daily changes. The new LLM Context endpoint goes beyond standard web results. It performs a full search, then extracts "smart chunks" from each page in real-time: clean text, structured data, JSON-LD schemas, table extraction, code context, forum discussions, YouTube captions. These chunks get ranked by relevance and compiled into a token-efficient format optimized for LLM consumption.

Latency: under 600ms at p90 for the full pipeline (search + extraction + ranking), with less than 130ms overhead on top of normal search. You can set a token budget to control costs at the request level. Goggles support lets you filter, boost, or downrank results by domain. SOC 2 Type II attested. Zero Data Retention. No conflicts of interest: they do not train their own LLMs on your queries.

### Brave Overview Card

- Pricing: $5/1K requests
- Free tier: $5 credit/month
- Index: 35B+ pages (own index)
- Latency: <600ms p90
- MCP server: Yes (open source)
- Privacy: ZDR + SOC 2 Type II

### Tavily

@tavilyai has become the default search API in the LangChain/LlamaIndex ecosystem, used by 800,000+ developers. It is purpose-built for AI agents with four endpoints: Search (web discovery), Extract (pull content from URLs), Map (understand site structure), and Crawl (navigate and extract from entire sites). In January 2026 they shipped agent skills, a Vercel AI SDK integration, the /research endpoint for multi-step automated research, and domain governance controls for regulated industries.

The credit-based pricing takes some understanding. Basic search costs 1 credit, advanced costs 2. Crawling stacks mapping + extraction costs. The /research endpoint uses dynamic pricing with min/max boundaries. Credits do not roll over month to month.

### Tavily Overview Card

- Pricing: $0.008/credit (~$8/1K basic)
- Free tier: 1,000 credits/month
- Index: Wraps multiple sources
- Endpoints: Search, Extract, Map, Crawl
- MCP server: Yes
- Frameworks: LangChain, LlamaIndex, Vercel

### Exa

@ExaAILabs (formerly Metaphor) is the contrarian play. While everyone else does keyword matching or wraps Google, Exa uses neural embeddings trained on their own index of tens of billions of pages. You search by meaning, not words. Ask "find articles explaining quantum computing like I am five" and it understands the intent. In October 2025 they launched Exa 2.0 with three tiers: Exa Fast (sub-350ms p50, fastest at the time), Exa Auto (default, balances latency and quality), and Exa Deep (agentic multi-search, ~3.5s p50, highest quality). Then on February 12, 2026 they shipped Exa Instant, pushing latency below 200ms for real-time applications.

The index is refreshed every minute. They built an in-house vector database to serve embeddings at low latency, trained for over a month on a 144x H200 cluster. For research agents making 50+ search calls, the 200ms savings per call from Exa Instant adds up to 10+ seconds of total savings.

### Exa Overview Card

- Pricing: $0.005/search (neural, 1-25)
- Free tier: 1,000 free requests/month
- Index: Tens of billions (own index)
- Latency: Sub-350ms (Fast), <200ms (Instant)
- Unique feature: Semantic similarity search
- Paid plans: $49/mo (Starter), $449/mo (Pro)

### Perplexity

Perplexity's API bundles search and LLM together. You do not just get results, you get synthesized answers with citations. The lineup: Sonar (fast, $1/M in+out tokens), Sonar Pro (deeper reasoning, $3/M input + $15/M output), Sonar Reasoning Pro (chain-of-thought with separate reasoning token costs), and Sonar Deep Research (autonomous multi-step, charges per search query made). On top of token costs, each model charges a per-request fee that varies by search context size (Low/Medium/High). The raw Search API is $5/1K requests with no token costs.

The trade-off is clear: you give up control over the LLM layer in exchange for a complete answer pipeline. If you want to use your own model (like running M2.5 or Opus), Perplexity is the wrong choice. If you want the fastest path to grounded answers, it might be the right one. Citation tokens are now free on standard Sonar and Sonar Pro, which meaningfully reduces per-query costs. But total cost per query depends on model choice + context size + token volume, making it harder to predict than flat-rate APIs.

### Perplexity Overview Card

- Sonar tokens: $1/$1 per M + request fee varies
- Sonar Pro tokens: $3/$15 per M + request fee varies
- Search API: $5/1K requests (no token cost)
- Deep Research: Tokens + per-search charges
- Context window: 128K (Sonar), 200K (Pro)
- Free credit: $5/mo with Pro subscription

### Firecrawl

@firecrawl is the extraction specialist. Where the others start with search, Firecrawl starts with "give me a URL and I will get you everything on that page." Their Agent handles JavaScript rendering, pagination, authentication, CAPTCHAs, and multi-page workflows automatically. Open source and self-hostable. In Firecrawl's own comparison testing, they reported 77.2% coverage and 0.638 F1 quality versus Exa's 69.2% coverage and 0.508 F1. (Note: these are vendor-published benchmarks, not independently audited.)

It is not a search engine. It is what you use after your search engine finds the right URLs. The pricing is flat and predictable: one credit per page, always. No depth multipliers, no variable consumption. At 100K pages monthly, Firecrawl costs $83 versus Tavily's $500-800 for equivalent extraction.

### Firecrawl Overview Card

- Pricing: 1 credit/page, flat rate
- Free tier: 500 credits (no card)
- 100K pages: $83/month
- Self-host: Yes (fully open source)
- JS rendering: Included, no extra cost
- Agent features: Pagination, auth, forms

### The comparison table

For the humans reading this, here is everything you need to know in one table.

### The Big Overview

See ASCII Image #7 above.

### Which API for which use case?

The smart move is not picking one. It is routing different query types to different APIs based on what each does best. Here is the routing table I would use if I were building an agent stack today.

### Decisions

See ASCII Image #8 above.

### Why the Brave announcement matters specifically

Brave's LLM Context API is interesting because of what it is not. It is not a wrapper around Google or Bing (like SerpAPI, which Google is suing). It is not bundled with an LLM you are forced to use (like Perplexity). It is not just a search endpoint (like their previous API).

What it is: a purpose-built pipeline that takes a query, searches an independent 35B-page index, extracts smart chunks from each result page in real-time, ranks those chunks for relevance, and delivers them in a token-budget-controlled format ready for any LLM. All in under 600ms.

Three things stand out in the announcement:

1. Skills for developer environments. They open-sourced Brave Search API Skills that work in Cursor, OpenCode, ClaudeCode, and OpenClaw. This is not an accident. The 200,000+ developers who signed up through the OpenClaw release are exactly the target audience.
2. The pricing simplification. Everything under Search (Web, LLM Context, Images, News, Videos) is $5/1K requests with $5 free monthly credit. No per-token costs on the search side. Answers plan is separate at $4/1K searches + $5/M tokens. This is meaningfully simpler than Tavily's credit system or Perplexity's token + request + search stacking.
3. The independence argument. Brave's blog makes the case that scrapers are legally risky (Google v. SerpAPI), can be shut off arbitrarily, and cannot offer true Zero Data Retention since queries pass through a third party. As the only western independent search index at scale outside Big Tech, they are positioning as the safe infrastructure choice for enterprise AI.

### What this means for agent builders

#### 1) The search layer is becoming the real moat

LLMs are commoditizing. Brave's evaluation showed an open-weight model with good search context beating frontier models with worse context. As model performance converges (M2.5 is 0.6 points from Opus), the quality of information flowing into those models becomes the primary differentiator. The search API you choose is now a product decision, not just an infrastructure one.

#### 2) The hybrid approach is winning

The most effective agent stacks are routing different query types to different APIs. Simple factual lookups go to Brave (cheap, fast, high quality context). Research discovery goes to Exa (semantic understanding). Deep extraction goes to Firecrawl (best quality, self-hostable). Quick synthesized answers go to Sonar (no model integration needed). This multi-API approach reduces costs 40-60% compared to using one provider for everything.

#### 3) Privacy and independence actually matter now

Enterprise AI teams are asking where their queries go. Wrapped APIs send queries to Google or Bing. Brave's ZDR policy and SOC 2 attestation are not just compliance checkboxes. They are competitive advantages for regulated industries where query content is sensitive. Firecrawl's open-source self-hosting option is the nuclear option for teams that need full data sovereignty.

### The OpenClaw connection

Brave specifically mentioned the 200,000+ developers who signed up through OpenClaw. Brave Search MCP server is already integrated. For anyone running agents on OpenClaw, the LLM Context API is the path of least resistance for high-quality web grounding. But do not sleep on combining it with Exa for research tasks and Firecrawl for deep extraction. The stack is more powerful than any single tool.

### The search API cheat sheet

- If you pick one: Brave LLM Context API. Independent index, LLM-optimized chunks, clean pricing, ZDR, MCP server ready. The best general-purpose search for agents in February 2026.
- If you pick two: Add Exa for semantic research discovery. Brave handles factual grounding. Exa handles "find me things like this." Together they cover 90% of agent search needs.
- If you go all-in: Brave for grounding + Exa for discovery + Firecrawl for extraction + Perplexity Sonar for quick answers. Route by query type. Budget $50-100/month for a comprehensive search stack that outperforms any single provider.

Your agent is only as good as its search. The LLM handles reasoning. The search handles reality. Get both right.

