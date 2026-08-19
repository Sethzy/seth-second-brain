---
type: wiki_article
title: LLM Foundations
updated_at: 2026-07-03
status: active
source_count: 11
tags:
  - llm-foundations
  - rag
  - fine-tuning
  - transformers
  - ai-engineering
---

# LLM Foundations

> Sources: Seth interview prompt and source bundle, 2026-06-28; Haggai Roitman arXiv abstract, 2026-06-22; Anatoli Kopadze X Article, 2026-06-20; Khairallah AL-Awady X Article, 2026-06-23; Ramakm/ai-hands-on README, 2026-06-28 capture; Nexu Harness Engineering Guide README, 2026-06-28 capture; Amit Shekhar LLM Internals README, 2026-06-28 capture; Sebastian Raschka, 2026-06-27; Artem Zhutov QMD/X Article, 2026-03-02 capture; Seth pasted GBrain embeddings note, 2026-07-02; Codez X Article, 2026-05-25.
> Raw: [LLM foundations interview prompt and source bundle](../../raw/intentional/pasted/2026-06-28-llm-foundations-interview-prompt-and-source-bundle.md); [arXiv abstract for The Hitchhiker's Guide to Agentic AI](../../raw/intentional/papers/2026-06-28-arxiv-abstract-the-hitchhiker-s-guide-to-agentic-ai.md); [Anatoli Kopadze loops explainer](../../raw/intentional/x/2068328135611822149-anatolikopadze-loops-explained-claude-gpt-mira-and-what-actually-works-ai-has-been-in-ever.md); [Khairallah AI engineer roadmap](../../raw/intentional/x/2069341916798369801-eng-khairallah1-how-to-become-an-ai-engineer-in-2026-without-a-cs-degree-most-people-think.md); [Ramakm ai-hands-on README](../../raw/intentional/web/2026-06-28-github-repo-snapshot-ramakm-ai-hands-on-readme.md); [Nexu Harness Engineering Guide README](../../raw/intentional/web/2026-06-28-github-repo-snapshot-nexu-io-harness-engineering-guide-readm.md); [Amit Shekhar LLM Internals README](../../raw/intentional/web/2026-06-28-github-repo-snapshot-amitshekhariitbhu-llm-internals-readme.md); [Sebastian Raschka Using Local Coding Agents](../../raw/intentional/web/2026-06-28-sebastian-raschka-using-local-coding-agents.md); [Artem Zhutov QMD/X Article](../../raw/intentional/x/2028330693659332615-artemxtech-grep-is-dead-how-i-made-claude-code-actually-remember-things-every-conversation.md); [Seth note on GBrain embeddings and hybrid retrieval](../../raw/intentional/pasted/2026-07-02-seth-note-on-gbrain-embeddings-and-hybrid-retrieval.md); [Codez five-stage LLM pipeline](../../raw/intentional/x/2058911661973454915-0xcodez-how-to-build-your-own-llm-from-scratch-in-5-stages-exact-pipeline-behind-gpt-and-c.md)

## Overview

LLM foundations should be studied as a stack, not as isolated buzzwords. The bottom layer is the model substrate: tokenization, embeddings, transformer attention, feed-forward networks, normalization, position encodings, decoding, KV cache, batching, quantization, MoE, and inference serving. Above that is the adaptation layer: pretraining, supervised fine-tuning, LoRA, RLHF/DPO-style preference tuning, reasoning training, and evaluation. Above that is the context layer: prompting, RAG, memory, retrieval evaluation, citations, and access control. At the top is the product/agent layer: APIs, tool use, loops, harnesses, deployment, monitoring, and human review.

The interview prompt is useful because it tests whether a candidate can separate two concepts that are often mashed together: **RAG changes what the model sees at inference time; fine-tuning changes how the model tends to behave because its weights or adapters were trained**. They are complements, not substitutes.

## Interview Answer: RAG vs Fine-Tuning

A strong answer:

RAG and fine-tuning solve different problems. RAG gives the model fresh, source-backed context at request time. Fine-tuning changes the model's learned behavior, style, task policy, or domain priors. If the problem is "the model does not know this fact" or "the answer must cite current/private documents," start with RAG. If the problem is "the model repeatedly fails the same pattern even when given the right context," "we need a stable output style or task procedure," or "we need lower per-call prompt overhead for a repeated behavior," consider fine-tuning.

RAG is usually better for volatile knowledge, private documents, access control, provenance, auditability, and fast iteration. It lets you update the corpus without retraining and can return citations. Its failure modes are retrieval quality, chunking, stale indexes, irrelevant context, prompt injection, and the model ignoring or misusing retrieved evidence.

Fine-tuning is usually better for stable behavior: format discipline, domain language, classification boundaries, tool-use patterns, style, tone, reasoning procedure, or adapting a smaller/local model to a narrow workflow. Its failure modes are cost, data quality, overfitting, forgotten capabilities, harder updates, weaker citation/provenance, and the temptation to encode facts that should have stayed external.

The best production answer is often both: use RAG for facts and evidence, then fine-tune or LoRA-tune the model to follow the task policy, use retrieved context correctly, produce the desired format, or call tools reliably. Start with prompting plus RAG plus evals; fine-tune only after failures repeat across enough examples that changing the model behavior is cheaper and more reliable than adding more context.

## The Persona Trap

The follow-up about persona is the real test. Retrieved examples can make a model imitate a user's voice for a single request, but that is soft conditioning. It consumes context, can be inconsistent, and may collapse when the retrieval misses the right examples. Fine-tuning can make style or task behavior more consistent because the behavior becomes part of the adapted model distribution.

But fine-tuning is still the wrong place for most personal facts. A user's changing preferences, recent decisions, private notes, current projects, and access-controlled data should live in memory/RAG/systems of record. Fine-tuning can teach "how to sound like Seth" or "how to structure Seth's answers," while retrieval supplies "what Seth currently knows, wants, or decided."

## Decision Rules

| Question | Prefer RAG | Prefer fine-tuning |
|---|---|---|
| Does the information change often? | Yes, retrieve current sources. | No, only if the behavior itself is stable. |
| Do you need citations or audit trail? | Yes. | Usually no. |
| Is the failure bad retrieval or missing evidence? | Fix indexing, chunking, reranking, prompts, or source quality. | Do not train first. |
| Is the failure repeated behavior despite correct context? | Maybe add instructions/evals first. | Yes, especially with many labeled examples. |
| Is the task mostly style, format, classification, or tool policy? | Useful for examples and policy docs. | Often yes. |
| Is latency/token cost dominated by long repeated instructions? | Maybe compress context. | Consider tuning/adapters once stable. |
| Is data access per-user or permissioned? | Yes, retrieve at request time. | Usually avoid baking into weights. |
| Is the target a smaller/local model? | Add retrieval for knowledge. | Tune to recover task behavior or domain language. |

## Core Mental Model

An LLM predicts tokens using patterns learned during training. Tokenization turns text into model-readable pieces; embeddings map tokens to vectors; transformer blocks use attention to mix information across the sequence; feed-forward layers transform features; normalization and positional schemes keep training and inference stable; decoding turns next-token probabilities into output. Inference optimization then decides how fast and cheaply this can run: KV cache avoids recomputing previous keys/values, batching keeps accelerators busy, quantization reduces memory/compute, prompt caching reuses prefixes, and MoE activates only selected expert sub-networks.

RAG sits outside the weights. It retrieves documents, chunks, rows, notes, or tool results, then places selected context into the prompt. A good RAG system is not just "vector DB plus prompt." It needs ingestion quality, chunking strategy, embeddings, lexical search, reranking, permissions, source citations, prompt-injection defenses, and retrieval evals that measure whether the right evidence was found.

Fine-tuning sits inside the model/adaptation layer. Full fine-tuning changes all weights; LoRA trains small low-rank adapter weights; supervised fine-tuning teaches demonstrations; preference/RL methods align choices against human or model feedback. The practical question is not "can we fine-tune?" but "do we have enough high-quality examples and evals to prove the tuned behavior improved without breaking something else?"

Agents add a harness around the model. Tool use lets the model call functions, query systems, or act in an environment. Loops let it plan, execute, verify, and iterate. A harness owns context assembly, memory, tool execution, sandboxing, permissions, state, retries, subagents, and evals. This is why modern AI engineering is not only model knowledge: the system around the model is often where reliability lives.

## LLM-Building Pipeline

Codez's X Article is useful as a high-level study map for building an LLM, not as primary lab documentation. The reusable frame is five stages: pretraining, data, scaling laws, post-training, and evaluation/systems. The memorable lesson for Seth is that the transformer architecture is usually the standardized substrate; leverage tends to come from data quality, compute allocation, preference tuning, eval design, and systems engineering.

- **Pretraining:** next-token prediction over tokenized corpora teaches language, facts, and latent reasoning patterns; transformer choice is mostly table stakes.
- **Data:** crawl extraction, filtering, deduplication, model-based quality scoring, and data-mixture choices shape the ceiling more than architecture tweaks.
- **Scaling laws:** small-run curves and Chinchilla-style tokens-per-parameter tradeoffs guide compute spend; production economics also account for inference cost, not just training cost.
- **Post-training:** SFT teaches instruction/chat behavior, while preference optimization such as RLHF or DPO shifts the model from imitation toward human-preferred answers.
- **Evaluation and systems:** perplexity helps during pretraining but is insufficient after alignment; benchmarks, pairwise comparisons, private evals, precision choices, FlashAttention-style kernels, parallelism, and MoE-style sparsity decide whether a model is usable in practice.

## Hybrid Retrieval: Keyword, Embeddings, And Meaning

Artem Zhutov's QMD article gives a practical mental model for why a serious RAG or LLM-wiki system should not rely on only one search mode. Plain grep finds string matches. BM25 still uses words, but ranks documents by term frequency and rarity, so it is much better for exact terms, filenames, IDs, policy names, product names, and structured notes. Semantic search uses embeddings: chunks and queries become points in a meaning space, so a question about "refunds" can retrieve a page called "chargeback policy" even if the exact word refund never appears.

The GBrain-style upgrade is not that embeddings replace the wiki. The wiki still holds the durable knowledge and citations. Embeddings make that knowledge findable by meaning, especially when the corpus gets large enough that wording mismatch becomes common. Seth's pasted note uses the image of a "map of meaning": nearby points represent similar ideas, even when the words differ. For a small wiki, keyword search may be enough; above thousands or tens of thousands of pages, semantic recall becomes much more valuable.

The best retrieval layer is usually hybrid:

- **BM25 / keyword search:** best for exact anchors, rare terms, titles, commands, error strings, names, dates, product labels, and policy names.
- **Embedding / semantic search:** best for paraphrases, fuzzy memories, transcripts, braindumps, and "I remember the idea but not the words" queries.
- **Metadata filters:** best for permissions, collection boundaries, recency, source type, account, customer, owner, or trust lane.
- **Reranking and source reading:** best for turning candidate chunks into cited evidence rather than trusting the first nearest neighbor.

So the strongest interview answer is: RAG is not "embeddings solve knowledge." RAG is a retrieval-and-grounding architecture. Embeddings help find meaning; keyword/BM25 preserves exactness; metadata preserves scope and permissions; reranking improves ordering; citations, evals, and human review keep the system honest.

## Study Path

1. **Model substrate.** Learn tokenization, embeddings, transformer attention, feed-forward networks, layer/RMS normalization, position encodings, decoding, KV cache, batching, MoE, and quantization. Use the LLM Internals repo as the router.
2. **Hands-on math and code.** Work through enough Python, PyTorch, neural networks, transformers, and RAG notebooks to make the concepts executable. The ai-hands-on repo is the practical spine.
3. **LLM API and tool use.** Build simple scripts that call a model, stream responses, maintain conversation state, enforce structured output, and call one real function/tool.
4. **RAG with evals.** Build a RAG app over a real document set, then measure whether it finds the right chunks before judging generation quality.
5. **Fine-tuning/adapters.** Learn SFT and LoRA after you can explain when not to use them. Treat tuning as behavior adaptation backed by eval data, not as a knowledge-upload button.
6. **Agents and harnesses.** Build a loop with a goal, tools, state, verifier, and stop condition. Then study harness engineering: context assembly, memory, permissions, sandboxing, error handling, and observability.
7. **Deployment and local models.** Learn serving/runtime choices, cost, latency, token budgets, privacy, open-weight models, and local harness tradeoffs. Raschka's local coding-agent article is a good applied example.

## Interview Rubric

A candidate is shallow if they define RAG and fine-tuning correctly but cannot explain the boundary. A stronger candidate says RAG is for external evidence and mutable knowledge, while fine-tuning is for stable behavioral adaptation. A very strong candidate adds evals, data quality, security, citations, permissions, latency, cost, and hybrid architectures.

Red flags:

- "Fine-tune to add company knowledge" as the default answer.
- Treating RAG as solved by embeddings alone.
- No mention of retrieval evaluation.
- No distinction between facts, behavior, style, and tool policy.
- No plan for stale data, citations, permissions, or prompt injection.
- No awareness that fine-tuning can make behavior more consistent but harder to audit.

Green flags:

- Starts with prompt/RAG/evals before training.
- Uses fine-tuning only after repeated failures are observed.
- Separates user memory from model weights.
- Explains that RAG and fine-tuning can be combined.
- Talks about benchmark/eval design before declaring a choice.

## Source Leads

Two LinkedIn links were captured only as public previews, not full source evidence:

- [Sairam Sundaresan LinkedIn preview: courses on Agents, RAG, and real-world LLMs](../../staging/incomplete-captures/web/2026-06-28-linkedin-preview-19-courses-on-agents-rag-and-real-world-llm.md)
- [Andreas Horn LinkedIn preview: visualization of how LLMs work](../../staging/incomplete-captures/web/2026-06-28-linkedin-preview-visualization-of-how-llms-actually-work.md)

Treat these as follow-up capture targets before relying on the full claims. The preview text is useful mainly as a reminder to add curated courses and visual explanations to this learning path.

## Open Questions

- Which three projects should Seth build first: RAG over Second Brain, small tool-using agent, local coding-agent benchmark, or LoRA/fine-tuning demo?
- Should this page later split into child articles for [RAG systems], [fine-tuning and LoRA], [transformer internals], and [agent harnesses], or stay as the single interview-prep router?
- Which evaluation set would prove Seth understands the fundamentals: interview flashcards, coding notebooks, or production-style mini apps?

## See Also

- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Agent Framework Landscape](../agent-frameworks/agent-framework-landscape.md)
- [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
