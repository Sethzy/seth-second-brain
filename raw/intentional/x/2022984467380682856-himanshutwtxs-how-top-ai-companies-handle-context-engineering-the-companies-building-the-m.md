---
type: raw_capture
source_type: x
url: https://x.com/himanshutwtxs/status/2022984467380682856
original_url: https://x.com/Hxlfed14/status/2022984467380682856
author: "Himanshu"
handle: himanshutwtxs
status_id: 2022984467380682856
captured_at: 2026-06-19T20:45:19+08:00
published_at: "Sun Feb 15 10:40:56 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 12
  likes: 92
---

# X post by @himanshutwtxs

## Source

- Original: [https://x.com/Hxlfed14/status/2022984467380682856](https://x.com/Hxlfed14/status/2022984467380682856)
- Canonical: [https://x.com/himanshutwtxs/status/2022984467380682856](https://x.com/himanshutwtxs/status/2022984467380682856)
- Author: Himanshu (@himanshutwtxs)

## Verbatim Text

How Top AI Companies Handle Context Engineering

The companies building the most capable AI agents today: @Manus , @cursor_ai , @AnthropicAI , @OpenAI , @GoogleDeepMind , @LangChain  are all solving the same problem: what information should an LLM see, when should it see it, and how should it be structured?

What is interesting is that these companies have been publishing their approaches openly through detailed blog posts, SDK cookbooks, research papers.

Each started from different constraints and arrived at different solutions. Some of those solutions converge. Some directly contradict each other.

I went through all of it. This article breaks down what each company does, compares their strategies head-to-head, and maps the techniques that are emerging as industry standard versus those that remain experimental.

Sources analyzed (All sources listed at the end of the article):

---

## The Core Problem

Every company here faces the same constraint: context windows are finite, and agents generate tokens exponentially.

A typical @ManusAI task involves ~50 tool calls. Each appends observations to the context. Without intervention, the window fills and performance degrades: "context rot."

The companies frame this differently, Anthropic calls it an "attention budget" problem, LangChain uses the "context window = RAM" analogy but all converge on the same conclusion: smarter context management beats bigger context windows.

---

## How Each Company Does It

> @ManusAI : "Six Principles from Production"

Context: Manus serves millions of users. A typical task averages 50 tool calls with a 100:1 input-to-output token ratio.

They have rewritten their agent framework four times each time after discovering a better way to shape context. They call this process "Stochastic Gradient Descent"

Six principles, condensed:

- KV-Cache is sacred. Cached tokens cost $0.30/MTok vs $3/MTok uncached (10x). Keep the prompt prefix stable, logs append-only. Even reordered JSON keys invalidate the cache.

- Logit masking over tool removal. All tools stay loaded permanently. Availability per step is controlled by constraining output token probabilities during decoding. Context stays stable; only behavioral constraints change.

- File system as extended memory. Large observations go to files; only lightweight references stay in context. Compression is fine as long as it is reversible.

- Attention manipulation via recitation. A living todo.md is updated and re-read every step, placing the current objective in the high-attention zone (end of context).

- Errors preserved, not cleaned. Failed actions stay in context for implicit belief updating, reducing repeated mistakes.

- Structured variation against fixation. Different serialization templates and phrasing across iterations prevent the model from falling into rigid, repetitive patterns.

---

> @cursor_ai : "Dynamic Context Discovery"

Context: Their Jan 2026 research blog describes five techniques they developed after observing that as models improved, providing fewer details up front and letting the agent pull its own context produced better results. They back this with A/B test data.

Five techniques, condensed:

- Files as tool output interface. Large JSON responses get written to files. Agent reads incrementally via tail/grep. No unnecessary summarization.

- Chat history files for lossless compression. Full history is saved to a file before summarization. Agent can restore any lost detail- lossy compression becomes lossless.

- Skills as discoverable files. Domain capabilities stored as files, discovered via search, not pre-loaded in the system prompt.

- Lazy MCP tool loading. Only tool names loaded upfront. Full definitions fetched on-demand. 46.9% token reduction in A/B tests.

- Terminal sessions as files. Shell history becomes a searchable file and agent greps for what it needs

Key assumption: This works because models are now good enough to know what context they need.

---

> @AnthropicAI : "The Attention Budget Framework"

Context: Anthropic published what many consider the foundational framing for context engineering (September 2025), followed by a deep dive on long-running agent harnesses (January 2026) and MCP-based code execution (November 2025). Their work is grounded in building Claude Code

Core strategies, condensed:

- The Goldilocks Zone for system prompts. Anthropic found two failure modes: over-engineered system prompts with 2K+ words of if-else logic that break on edge cases, and vague prompts like "be helpful" that give the model nothing to work with. 

Their fix: organize prompts into clear sections (XML tags or markdown headers), use canonical examples to show expected behavior, and let the model handle edge cases instead of hard-coding them.

- Just-in-time retrieval. Agent retrieves context at runtime based on what it actually needs is shifting from pre-inference RAG to in-loop retrieval.

- Lean tools with no overlap. If a human engineer cannot say which tool to use in a given situation, neither can the model. Tools should be self-contained and unambiguous.

- Compaction at 95%. Claude Code auto-summarizes when the window hits 95% capacity. For long-running agents, an initializer agent writes a comprehensive requirements file (200+ features) that persists across windows.

- Code execution over direct tool calls. For MCP with many servers, agents write code that calls tools rather than invoking them directly. Definitions stay in the filesystem.

Two failure patterns discovered: Agents "one-shot" complex projects (run out of context mid-implementation), and compaction transfers information imperfectly across windows. Solution: structured planning files in the filesystem

---

> @OpenAI : "Session Memory as Infrastructure"

Context: OpenAI's approach is documented through their Agents SDK and two detailed cookbooks- one on short-term session memory (September 2025) and one on long-term context personalization (December 2025).

Their contribution is framework-oriented: structured patterns developers can adopt directly.

Three patterns, condensed:

- Trimming. Drop older turns, keep last N. Simple, deterministic, zero latency  but causes "amnesia" for earlier constraints.

- Compression. Summarize older history with a separate model call. Summaries act as "clean rooms" that can correct prior mistakes. Risk: summary drift.

- State-based long-term memory. Structured state objects (profile + notes) persist across sessions. Each run: 
distill memories → consolidate notes → inject state with precedence (latest input → session → global defaults).

Key distinction: OpenAI contrasts retrieval-based memory (searching past interactions as documents) with state-based memory (structured fields with precedence). State-based supports belief updates over fact accumulation is more reliable, more deterministic.

---

> @GoogleDeepMind : "The Long Context Bet"

Context: Google's approach is distinct from everyone else on this list. While other companies focus on fitting the right tokens into a limited window, Google bets on abundance as Gemini models offer up to 2M tokens of context, with research testing up to 10M. Their ReadAgent paper (2024) adds a complementary research angle on memory compression.

Approach, condensed:

- "Just put it all in." Default to filling the context window. RAG and summarization are workarounds for limited context models. Evidence: Gemini learned to translate Kalamang (<200 speakers) from in-context materials alone.

- Context caching. Up to 75% cost reduction via caching APIs, analogous to Manus's KV-cache optimization.

- Progressive truncation. Compress older context while maintaining the logical thread.

- ReadAgent- Gist Memory (research). Compress interactions into episodic "gist memories," look up originals when needed. Increases effective context by 20x. Modeled on how humans read long documents.

- Many-shot in-context learning. Unique leverage of massive windows hundreds/thousands of examples in-context, matching fine-tuned model performance.

The tension: Long context doesn't eliminate context engineering but it changes what it looks like. Research still shows 15–47% performance drops as context length increases.

---

> @LangChain : "The Framework Taxonomy"

Context:  Their contribution is taxonomic- organizing what others are doing into a coherent framework, backed by their LangGraph implementation and "Deep Agents" analysis.

- Write - save context outside the window. Scratchpads, persistent state objects, filesystem storage. Example: Anthropic's multi-agent researcher saves plans to memory because context exceeding 200K tokens gets truncated.

- Select - pull relevant context in. RAG, semantic search, filesystem traversal with grep/glob. The challenge is retrieving the right context at the right time, not just the most semantically similar.

- Compress - retain only essential tokens. Conversation summarization, tool output compression. LangChain measured a reduction from 115K to 60K tokens through end-to-end summarization in their tests.

- Isolate - split context across agents. Multi-agent architectures where sub-agents get their own context windows, preventing "context pollution" from irrelevant details accumulating in a shared window.

- No-op tools as context engineering. Their "Deep Agents" analysis revealed that Claude Code's todo list tool does nothing functionally but it is purely a context strategy that forces the agent to articulate its plan, keeping it on track over long trajectories.

---

## The Technique Matrix

Quick-reference mapping techniques to companies based on public documentation.

Legend: 
[C] = Core differentiator 
[Y] = Yes, uses/advocates 
[--] = Not discussed publicly 
[alt] = Different approach to same problem

Context Window Management:

Information Retrieval:

Planning & Coherence:

Multi-Agent & Isolation:

Memory & Robustness:

---

## Where The Industry Agrees (and Where It Doesn't)

The technique matrix tells most of the story, but here is the short version.

Near-consensus: File system as extended memory. Dynamic over static retrieval. Persistent plan files for long-running tasks. Error traces kept, not cleaned.

Active disagreement: How to handle tool overload (Manus's logit masking vs Cursor's lazy loading- opposite strategies, both work). Long context vs lean context (Google vs everyone else). Whether to use frameworks or raw primitives.

Unsolved: Session memory; no two companies do it the same way. Context engineering evaluation; no standard benchmarks exist. Cursor's 46.9% token reduction is one of the few published numbers. When to isolate sub-agent context vs share it is still purely empirical.

One pattern worth noting: the teams shipping the best agents keep simplifying. Manus has been rewritten five times. Each rewrite removed things. If your agent harness is getting more complex while models get better, something is wrong.

---

## Open Questions

Long context vs. smart compression- which wins at scale?

Should sub-agents share context or communicate results?

How do you evaluate context engineering quality?

---

Based entirely on publicly available blogs, documentation, and research papers from the companies referenced.

References

1. Manus — ["Context Engineering for AI Agents: Lessons from Building Manus"](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) (Jul 2025)

2. Cursor — ["Dynamic Context Discovery"](https://cursor.com/blog/dynamic-context-discovery) (Jan 2026)

3. Anthropic — ["Effective Context Engineering for AI Agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (Sep 2025)

4. Anthropic — ["Effective Harnesses for Long-Running Agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Jan 2026)

5. Anthropic — ["Code Execution with MCP"](https://www.anthropic.com/engineering/code-execution-with-mcp) (Nov 2025)

6. OpenAI — ["Context Engineering - Short-Term Memory Management with Sessions"](https://cookbook.openai.com/examples/agents_sdk/session_memory) (Sep 2025)

7. OpenAI — ["Context Engineering for Personalization"](https://cookbook.openai.com/examples/agents_sdk/context_personalization) (Dec 2025)

8. Google DeepMind — ["A Human-Inspired Reading Agent with Gist Memory"](https://deepmind.google/research/publications/74917/) (2024)

9. Google — [Long Context Documentation](https://ai.google.dev/gemini-api/docs/long-context) (2025)

10. LangChain — ["Context Engineering for Agents"](https://blog.langchain.com/context-engineering-for-agents/) (Jul 2025)

11. LangChain — ["The Rise of Context Engineering"](https://blog.langchain.com/the-rise-of-context-engineering/) (Jun 2025)

12. LangChain — ["How Agents Can Use Filesystems for Context Engineering"](https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/) (Nov 2025)

13. LangChain — ["Deep Agents"](https://blog.langchain.com/deep-agents/) (Jul 2025)

14. Phil Schmid — ["Context Engineering for AI Agents: Part 2"](https://www.philschmid.de/context-engineering-part-2) (Dec 2025)

15. Lance Martin — ["Context Engineering in Manus"](https://rlancemartin.github.io/2025/10/15/manus/) (Oct 2025)

## X Article Metadata

- Title: How Top AI Companies Handle Context Engineering
- Preview: The companies building the most capable AI agents today: @Manus , @cursor_ai , @AnthropicAI , @OpenAI , @GoogleDeepMind , @LangChain  are all solving the same problem: what information should an LLM

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
