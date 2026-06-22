---
type: raw_capture
source_type: x
title: "Sunder sync: Code Sandbox UI.md"
url: "https://x.com/tdinh_me/status/2011289471241826767"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/01_Projects/Code Sandbox UI.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "01_Projects/Code Sandbox UI.md"
sha256: "88c069f606010358230e8b9223314488fcdf8ba74cb1f07a9b6e61bdb848a6a7"
duplicate_of: ""
---

# Sunder sync: Code Sandbox UI.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/01_Projects/Code Sandbox UI.md`

Primary URL: https://x.com/tdinh_me/status/2011289471241826767

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-14
tags: [project]
status: active
target: 2026-01-19
linear_url:
---

# Code Sandbox UI

## Problem
Need code execution/sandbox capability in our product. TypingMind just shipped this - we need parity.

## Solution
Add Code Sandbox UI that leverages built-in sandbox from providers:
- OpenAI API (20min persistent container, file persistence)
- Gemini
- Claude

## Why This Matters
Extraction alone is trivial. The "wow moment" is AI doing the actual work:

| Level | What it does | Impact |
|-------|--------------|--------|
| **Extraction** | AI extracted information for you | User still reviews, finds patterns |
| **Reconciliation** | AI is doing your work for you | User reviews output, not inputs |

The value isn't "here's the data" - it's "here's what matches, here's what doesn't, here's the exceptions." That's most of the job.

## The Pattern
Same as web scraping skill - minimal instruction, let AI figure it out:

| Before | After |
|--------|-------|
| "here is directory, do not stop until done" | "here's my messy data, here is ur sandbox" |

That's the future of work.

## Weekend Scope (Jan 18-19)
1. **Fix UI** → make it a chatbot
2. **Multi-turn** → use provider's container persistence, not custom sandbox
3. **Streaming** → implement their streaming pattern
4. **Skill** → iterate on output format (markdown vs JSON)

## Notes
- TypingMind approach: use provider-native sandboxes first, 3rd party (Vercel, E2B) later
- OpenAI's persistent container is most feature-rich (accepts file input)
- Reference: https://x.com/tdinh_me/status/2011289471241826767

## Updates

### 2026-01-15
**Claude Code Execution - Streaming Pattern**

Server-side code execution with streaming events:

```
content_block_start → server_tool_use (code_execution)
content_block_delta → input_json_delta (code streams in)
[pause while code executes]
content_block_start → code_execution_tool_result (stdout/stderr)
```

Key event types:
- `server_tool_use` with `name: "code_execution"` - signals code block starting
- `input_json_delta` - streams the code being written
- `code_execution_tool_result` - returns `stdout` and `stderr` after execution

Docs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool

---

### 2026-01-16
**Bash-as-RAG Pattern**

Mental model from @tdinh_me: instead of traditional RAG (chunk → embed → vector search → retrieve), give agent bash tools and let it `grep`, `find`, `jq`, `awk` through files directly.

**Two Architecture Flows:**

| Flow | When to Use |
|------|-------------|
| **SQL/PostgREST** | Reconciliation logic well-defined, predictable, consistent schemas |
| **Bash/Sandbox** | Format varies by vendor, need iteration, cross-document discovery |

**Use Cases:**
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

### 2026-01-16 (2)
**Skills API = The Sandbox (No E2B Needed)**

From docs:
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

**Constraint:** No network access. App fetches data first, uploads to container.

**Docs:**
- Code Execution: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool
- Skills Guide: https://platform.claude.com/docs/en/build-with-claude/skills-guide
- Bash Tool: https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool

---

### 2026-01-16 (3)
**Excel Editing - Can Modify Existing Files**

Yes, Claude can edit existing Excel files, not just create new ones.

```python
from openpyxl import load_workbook

# Load existing file
wb = load_workbook('existing.xlsx')
sheet = wb.active  # or wb['SheetName']

# Work with multiple sheets
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]

# Modify cells
sheet['A1'] = 'New Value'
sheet.insert_rows(2)
sheet.delete_cols(3)

# Add new sheet
new_sheet = wb.create_sheet('NewSheet')
new_sheet['A1'] = 'Data'

wb.save('modified.xlsx')
```

**Capabilities:**

| Action | Supported |
|--------|-----------|
| Load existing .xlsx | ✅ |
| Modify cell values | ✅ |
| Preserve formulas | ✅ |
| Preserve formatting | ✅ |
| Insert/delete rows/columns | ✅ |
| Add new sheets | ✅ |
| Work with multiple sheets | ✅ |

**Caveat:** Excel files modified by openpyxl contain formulas as strings but not calculated values. Use `recalc.py` script or open in Excel to recalculate.

**For RedDoc:** Can upload reconciliation template, have Claude populate with match results, get back modified file with formatting intact.

---

### 2026-01-16 (4)
**Real-World Testimonials - Non-Coders Using Claude Code**

#### @vinnynguyen1194 (Big 4 Accountant)
> "I tried claude code and cowork for a non-coding task after building a relevant skill for my line of work. After it ran for an hour, it came back with an output that I thought was one of the best outputs i have read in 10 years of working at big 4."

> "It was at the Manager level and it is scary! It was able to get me excel analysis, well formated document and above all, quality content that shows great reasoning, highly contextual. This task usually takes my team a full week to produce, and the quality is not even near the quality that CC can produce in an hour."

**Key insight:** Week-long Big 4 task → 1 hour with manager-level quality.

#### @harshagrawal004 (Claude Code Workflow)
**How it works:**
- Give Claude access to one specific folder
- Tell it what you need: "Create an expense report from these receipts"
- Claude makes a plan and executes
- You review results
- Nothing outside that folder gets touched

**Built-in skills for:**
- Word documents (proper formatting)
- PowerPoint presentations (structured slides)
- Excel spreadsheets (formulas included)
- Pair with Claude in Chrome for browser-based tasks

**Availability:** Claude Max subscribers on macOS, research preview

**Takeaway:** The sandbox model + skills = safe autonomous execution for non-technical users.
