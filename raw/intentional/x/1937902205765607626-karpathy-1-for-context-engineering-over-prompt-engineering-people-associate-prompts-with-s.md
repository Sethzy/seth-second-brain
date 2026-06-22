---
type: raw_capture
source_type: x
url: https://x.com/karpathy/status/1937902205765607626
original_url: https://x.com/karpathy/status/1937902205765607626
author: "Andrej Karpathy"
handle: karpathy
status_id: 1937902205765607626
captured_at: 2026-06-19T19:39:12+08:00
published_at: "Wed Jun 25 15:54:24 +0000 2025"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 529
  reposts: 2051
  likes: 14338
---

# X post by @karpathy

## Source

- Original: [https://x.com/karpathy/status/1937902205765607626](https://x.com/karpathy/status/1937902205765607626)
- Canonical: [https://x.com/karpathy/status/1937902205765607626](https://x.com/karpathy/status/1937902205765607626)
- Author: Andrej Karpathy (@karpathy)

## Verbatim Text

+1 for "context engineering" over "prompt engineering".

People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step. Science because doing this right involves task descriptions and explanations, few shot examples, RAG, related (possibly multimodal) data, tools, state and history, compacting... Too little or of the wrong form and the LLM doesn't have the right context for optimal performance. Too much or too irrelevant and the LLM costs might go up and performance might come down. Doing this well is highly non-trivial. And art because of the guiding intuition around LLM psychology of people spirits.

On top of context engineering itself, an LLM app has to:
- break up problems just right into control flows
- pack the context windows just right
- dispatch calls to LLMs of the right kind and capability
- handle generation-verification UIUX flows
- a lot more - guardrails, security, evals, parallelism, prefetching, ...

So context engineering is just one small piece of an emerging thick layer of non-trivial software that coordinates individual LLM calls (and a lot more) into full LLM apps. The term "ChatGPT wrapper" is tired and really, really wrong.

## Quoted Post

- URL: https://x.com/tobi/status/1935533422589399127
- Author: tobi lutke (@tobi)

I really like the term “context engineering” over prompt engineering. 

It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM.

## Capture Note

TweetDetail returned complete normal-post text.
