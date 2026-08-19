# Auditable Structured Document Extraction

> Sources: Google LangExtract, repository snapshot at commit `0dff5479`, 2026-07-02; Chayenne Zhao, 2026-02-13; Asad Naveed, 2026-02-12
> Raw: [Google LangExtract repository README snapshot](../../raw/intentional/web/2026-07-20-google-langextract-repository-readme-snapshot.md); [Chayenne Zhao on source-grounded extraction](../../raw/intentional/x/2022232965582045420-genai-is-real-people-calling-langextract-a-nothingburger-clearly-haven-t-dealt-with-the-ha.md); [Asad Naveed on LangExtract](../../raw/intentional/x/2021854163567624444-dr-asadnaveed-breaking-google-just-took-away-your-research-asssitant-s-job-google-has-laun.md)
> Status: active
> Updated: 2026-07-20

## Overview

Structured document extraction becomes materially more useful when every output can be traced back to the exact evidence that produced it. Google LangExtract is a concrete implementation of this pattern: it turns unstructured text into typed extractions, aligns them to character intervals in the source, scales across long documents through chunking and repeated passes, and provides an interactive review surface. The reusable lesson is broader than this library: extraction systems should return evidence coordinates and review artifacts alongside JSON, rather than asking downstream users to trust model output in isolation.

## What LangExtract Does

LangExtract is a Python library for extracting structured information from unstructured text using user instructions and few-shot examples. Its core workflow is:

1. Define the extraction classes, rules, and desired attributes in a prompt.
2. Supply high-quality example text with expected extractions.
3. Run `lx.extract` against text, documents, or supported URLs.
4. Persist annotated results as JSONL.
5. Generate a self-contained HTML visualization for human review in source context.

The library supports cloud and local model providers, including Gemini, OpenAI models, and Ollama-backed local models. It can also accept explicit output schemas for stronger attribute constraints with supported providers.

## Why Source Grounding Matters

Each extraction is aligned to an exact character interval in the source text. This makes the output inspectable, highlightable, and easier to verify. An extraction that cannot be located receives no character interval, which creates a practical filter for separating grounded spans from unsupported model output.

This changes the product contract from “the model returned structured data” to “the model returned structured data plus evidence coordinates.” That distinction is especially valuable in research, healthcare, legal, financial, operational, and knowledge-base workflows where a reviewer must understand where a field came from.

The social framing around LangExtract called this a response to the “hallucination tax” of long-context extraction. That is a useful intuition, but source alignment should not be treated as proof that every inferred attribute is correct. A span can be grounded while its classification or attached attributes remain wrong.

## Long-Document Strategy

LangExtract addresses long inputs with three composable controls:

- **Chunking:** split the document into smaller buffers so the extraction task stays focused.
- **Parallel processing:** process chunks concurrently to reduce wall-clock time.
- **Multiple extraction passes:** trade additional model calls for higher recall on sparse or difficult entities.

The result is a tunable precision, recall, latency, and cost system rather than a single giant-context prompt. Smaller chunks may improve local extraction accuracy but can lose cross-chunk context; repeated passes may improve recall but also increase duplication and cost. Production use therefore needs task-specific evaluation rather than assuming the default settings transfer across domains.

## Schema And Prompt Discipline

Few-shot examples function as an executable extraction specification. Example spans should be verbatim, ordered by source appearance, and consistent with the task rules. LangExtract warns when prompt examples do not align cleanly to their example text.

For durable workflows, the extraction contract should define:

- entity or field classes;
- exact-span versus inferred-value policy;
- allowed attribute values and null behavior;
- overlap and ordering rules;
- duplicate resolution;
- evidence requirements;
- acceptance thresholds and human-review triggers.

Explicit schemas are useful for structural consistency, but they do not by themselves guarantee semantic correctness. The prompt, examples, provider behavior, and evaluation set remain part of the effective schema.

## Practical Evaluation Checklist

Evaluate the full pipeline on representative documents, including messy and adversarial cases:

- span precision and recall;
- field-level accuracy;
- percentage of outputs with valid source intervals;
- unsupported or example-leaked extractions;
- duplicates across chunks or passes;
- missed entities at chunk boundaries;
- latency and model cost per document;
- reviewer time saved by the visualization;
- consistency across model and library upgrades.

Keep the original document, prompt, examples, model identifier, extraction settings, and library version with every production run. Evidence coordinates are most valuable when the entire extraction decision can be reproduced.

## Caveats And Corrections

One captured X post described LangExtract as requiring no API keys or usage limits. That is only true for suitable local-model paths. Cloud-hosted Gemini and OpenAI models require provider credentials and remain subject to their rate limits and pricing. The library is open source, but the selected inference backend determines runtime economics and data-handling constraints.

Character alignment also cannot validate facts inferred from model world knowledge. Prompts may deliberately request inferred attributes, but those attributes should be labeled separately from verbatim evidence and reviewed under a different confidence policy.

## Second Brain Relevance

LangExtract is a candidate primitive for turning long source captures into machine-readable entities while retaining links to the exact passage. Potential uses include:

- extracting people, companies, tools, claims, dates, and relationships from saved sources;
- producing reviewable candidate metadata before wiki compilation;
- attaching evidence spans to CRM or research records;
- generating structured training and evaluation sets from manually verified captures.

It should augment rather than replace raw snapshots. The immutable source remains the evidence layer; LangExtract-style output is a derived, versioned annotation layer that can accelerate compilation and retrieval.

## See Also

- [Agentic Classifiers](agentic-classifiers.md)
- [Agentic Artifact Surfaces](agentic-artifact-surfaces.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
