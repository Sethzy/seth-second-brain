---
type: raw_capture
source_type: x
title: "Sunder sync: Claude Code AI SDK Exploration.md"
url: "https://x.com/boringmarketer/status/2008607337532014709"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Ideas/Claude Code AI SDK Exploration.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "02_Areas/Product/Ideas/Claude Code AI SDK Exploration.md"
sha256: "c962506b268ed7a834ceaac5414f7ab0aabb261751e708eff75b545cf656ab89"
duplicate_of: ""
---

# Sunder sync: Claude Code AI SDK Exploration.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Ideas/Claude Code AI SDK Exploration.md`

Primary URL: https://x.com/boringmarketer/status/2008607337532014709

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-12
tags: [product-idea]
type: feature
priority: none
linear_url:
---

# Claude Code AI SDK Exploration

## Problem
If Claude Code is the best, should use their SDK for building agents.

## Solution
Explore and implement using Claude Agent SDK.

## Resources
- Overview: https://platform.claude.com/docs/en/agent-sdk/overview
- Engineering blog: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- Video: https://www.youtube.com/watch?v=TqC1qOfiVcQ
- Vercel sandbox: https://vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk
- Excel demo: https://github.com/anthropics/claude-agent-sdk-demos/tree/main/excel-demo

## Notes
See PRD for detailed planning.

## Updates

### 2026-01-14
**Excel Collaboration Architecture**

Problems to solve:
1. **Excel in sandbox** - VM starts empty, need file handling strategy
2. **Agent-in-the-loop** - iterative refinement vs one-shot API

Potential approaches:
- **Git-as-filesystem** - agent commits changes, user pulls results, enables branching for comparisons
- Warm container pools for faster iteration
- Preview/diff before applying changes

Current flow is fire-and-forget API → need back-and-forth where user says "make this chart blue" and agent adjusts.

### 2026-01-15
**Sandbox Infrastructure Options (Key Extension)**

Alternatives for running Agent SDK in sandboxed environments:

| Provider | Key Features | Links |
|----------|--------------|-------|
| **Vercel Sandbox** | Ephemeral compute for untrusted code, node24/python3.13, sudo access, OIDC auth | [Docs](https://vercel.com/docs/vercel-sandbox) |
| **Modal Sandboxes** | Runtime container definition, 5min-24hr lifespans, snapshots for state persistence, named discovery | [Docs](https://modal.com/docs/guide/sandboxes) |
| **e2b** | Firecracker microVMs, <200ms cold start, 24hr sessions, LLM-agnostic, open-source | [Site](https://e2b.dev/), [AI Analyst Demo](https://ai-analyst.e2b.dev/), [Repo](https://github.com/e2b-dev/ai-analyst) |

**Comparison:**
- **Vercel** - tightest integration if already on Vercel, managed auth
- **Modal** - most flexible config, good for complex workflows
- **e2b** - purpose-built for AI agents, fastest cold starts, open-source

### 2026-01-15 (2)
**Ad Agent Example (@boringmarketer)**

Real-world Agent SDK use case:
- Finds competitors, learns from their ads
- Prompts and generates on-brand creatives
- Packages in shareable report

Key: runs autonomously OR with prompt. No node-based workflows needed.

Source: https://x.com/boringmarketer/status/2008607337532014709

### 2026-01-15 (3)
**Bash-as-RAG Pattern for RedDoc**

Mental model from @tdinh_me (TypingMind): instead of traditional RAG (chunk → embed → vector search → retrieve), give agent bash tools and let it `grep`, `find`, `jq`, `awk` through files directly.

**Two Architecture Flows:**

| Flow | When to Use |
|------|-------------|
| **SQL/PostgREST** | Reconciliation logic is well-defined, predictable, consistent schemas |
| **Bash/Sandbox** | Format varies by vendor, need iteration, cross-document discovery |

**RedDoc Use Cases for Bash-as-RAG:**
- Three-way matching: `jq` to cross-reference PO ↔ Invoice ↔ Packing list
- Field extraction validation: `grep` patterns to cross-verify OCR
- Anomaly detection: `awk` for arithmetic, `grep -v` for exceptions
- Audit search: `find` + `ripgrep` across hundreds of docs

**Key Insight:** For structured document workflows, often want exact matching not semantic similarity. Bash excels here.

**jq** = command-line JSON query tool (like SQL for JSON):
```bash
jq '.line_items[] | select(.qty > 10)' invoice.json
jq -s '.[0].total - .[1].total' invoice.json po.json
```

---

### 2026-01-15 (4)
**Skills API vs E2B - Don't Need External Sandbox**

Skills API IS the sandbox. From docs:
> Skills integrate with the Messages API through the code execution tool... both require code execution and use the same container structure.

**Code Execution Tool Versions:**

| Version | Capabilities |
|---------|--------------|
| `code_execution_20250522` | Python only |
| `code_execution_20250825` | Python + Bash + file operations |

Current version includes: bash, python, jq, openpyxl, xlsxwriter, python-pptx, python-docx, pypdf, pdfplumber.

**Multi-Turn Conversations:**
```python
# Reuse same container across messages
response2 = client.beta.messages.create(
    container={"id": response1.container.id, ...},
    messages=[...],
)
```
Filesystem persists between turns.

**Long-Running Operations:**
Handle `pause_turn` stop reason - Claude continues from where it stopped, container state preserved.

**Constraint:** No network access. App fetches JSONs from Supabase first, uploads to container.

**Docs:**
- Code Execution: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool
- Skills Guide: https://platform.claude.com/docs/en/build-with-claude/skills-guide
- Bash Tool: https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool
