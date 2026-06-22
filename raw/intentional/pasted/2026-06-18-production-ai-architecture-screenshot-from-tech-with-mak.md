---
type: raw_capture
source_type: pasted
title: "Production AI architecture screenshot from Tech with Mak"
url: "Unknown"
collected_at: 2026-06-18T14:43:27Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Production AI architecture screenshot from Tech with Mak

Source: Unknown

## Capture Text

Transcribed from user-provided screenshot: raw/intentional/pasted/assets/2026-06-18-production-ai-architecture-x-screenshot.png

Visible X post metadata:
- Author: Tech with Mak
- Handle: @techNmak
- Published/displayed time: 12:03 AM · Jun 18, 2026
- Visible views: 27.3K
- Original URL: not visible in screenshot
- Visible external domain: academy[.]neosage[.]io

Tweet text:

Someone just dropped a 9-layer production AI architecture and it's the most honest breakdown I've seen.

services/ - RAG pipeline, semantic cache, memory, query rewriter, router. Not one file. Five.

agents/ - document grader, decomposer, adaptive router. Self-correcting by design.

prompts/ - versioned, typed, registered. Never hardcoded.

security/ - input, content, output. Three guards not one.

evaluation/ - golden dataset, offline eval, online monitor. Most people skip this entire layer and ship blind.

observability/ - per-stage tracing, feedback linked to traces, cost per query.

.claude/ - agent context so your AI coding assistant knows the codebase before it touches a file.

The demo is one file. Production is this.

Check: academy[.]neosage[.]io

Image transcript:

production-ai-app/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── Dockerfile
│   ├── components/
│   │   ├── hybrid_retriever.py
│   │   └── reranker.py
│   ├── services/
│   │   ├── rag_pipeline.py
│   │   ├── semantic_cache.py
│   │   ├── conversation.py
│   │   ├── query_rewriter.py
│   │   └── query_router.py
│   ├── prompts/
│   │   ├── templates.py
│   │   └── registry.py
│   ├── agents/
│   │   ├── document_grader.py
│   │   ├── query_decomposer.py
│   │   ├── adaptive_router.py
│   │   └── tools/vector_search.py
│   │       ├── web_search.py
│   │       └── code_search.py
│   ├── security/
│   │   ├── input_guard.py
│   │   ├── content_filter.py
│   │   └── output_filter.py
│   ├── evaluation/
│   │   ├── golden_dataset.json
│   │   ├── offline_eval.py
│   │   ├── online_monitor.py
│   │   └── eval_results/
│   ├── observability/
│   │   ├── tracer.py
│   │   ├── feedback.py
│   │   └── cost_tracker.py
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── index_config/
│   ├── scripts/
│   │   ├── seed.py
│   │   ├── migrate.py
│   │   └── healthcheck.py
│   ├── frontend/
│   │   ├── app.py
│   │   ├── static/
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── tests/
│   │   ├── test_retrieval.py
│   │   ├── test_cache.py
│   │   └── test_routing.py
│   ├── docs/
│   │   ├── architecture.md
│   │   ├── api-reference.md
│   │   └── deployment.md
│   └── .claude/
│       └── rules/
│           ├── code-style.md
│           └── testing.md
├── CLAUDE.md
├── AGENTS.md
├── docker-compose.yml
├── pyproject.toml
└── README.md

Image side annotations:
- app/: FastAPI entry, config, schemas, containerized
- components/: Custom retrieval: hybrid search + reranking
- services/: Core business logic: pipeline, cache, memory, rewriting, routing
- prompts/: Versioned, type-specific, hot-swappable
- agents/: Intelligence layer: self-correcting retrieval, LLM-driven source selection
- tools/: Pluggable tool definitions
- security/: Three guard layers: input, content, output
- evaluation/: Golden test set, offline + online pipelines, tracked history
- observability/: Per-stage tracing, feedback capture, cost breakdown
- data/: Raw -> processed -> index config
- scripts/: Seed, migrate, healthcheck
- frontend/: UI, containerized separately
- tests/: Retrieval, cache, routing tests. CI-ready.
- docs/: Architecture, API ref, deployment guide
- .claude/: AI coding agent context, rules, project memory

User instruction: "replicate and add this please"
