---
type: raw_capture
source_type: web
title: "Sunder sync: 2026-01-25-just-in-time-ui-design.md"
url: "https://json-render.dev/"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-25-just-in-time-ui-design.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-01-25-just-in-time-ui-design.md"
sha256: "dfaff27a8dcb111d8dcbae39ece93a0db36e2463ecde591ed9829d8e273a7f8a"
duplicate_of: ""
---

# Sunder sync: 2026-01-25-just-in-time-ui-design.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-25-just-in-time-ui-design.md`

Primary URL: https://json-render.dev/

Duplicate of existing source-map entry: `none`

## Capture Text

# Just-in-Time UI for Edge Case Resolution: PRD Draft

**Date:** 2026-01-25
**Status:** Draft
**Author:** Claude + Seth

---

## The Problem

Current Sunder AI Analyst is **just a chat**.

> **Note:** This is analogous to asking Claude Code for ASCII diagrams to explain a complex system. The visual artifact helps you *see* the problem structure, not just read about it. The best AI UIs give you both: the conversation AND the visual representation of what's being solved.

```
┌─────────────────────────────────────────┐
│  [Chat messages]                        │
│  [Chat messages]                        │
│  [Chat messages]                        │
│  [Input box]                            │
└─────────────────────────────────────────┘
```

Users can't **see** what they're working on. When Claude identifies edge cases in document processing, users have to:
1. Read the text description
2. Mentally picture the problem
3. Ask follow-up questions to understand
4. Hope Claude understood their intent

This is friction. Good AI UIs solve this differently.

---

## Inspiration: Chat + Visual Artifact Pattern

### Reference 1: json-render.dev

https://json-render.dev/ 

![json-render edge cases](./assets/json-render-edge-cases.png)

*json-render.dev shows JSON schema on the left, and **live rendered UI** on the right showing "Custom Edge Cases" with CRITICAL/HIGH/MEDIUM severity cards.*

Key insight: The AI generates structured JSON, and a component library renders it instantly. Users see the **actual UI** being built, not just text descriptions.

### Reference 2: Current Sunder AI Analyst

![Current Sunder](./assets/sunder-current-analyst.png)

*Current state: Just a chat with quick action cards (Reconcile, Analyze, Audit). No visual representation of what's being analyzed or the problems found.*

### Reference 3: Origami Agents

![Origami agents](./Screenshot%202026-01-25%20at%2011.21.56%20AM.png)

*[app.origamiagents.com](https://app.origamiagents.com) - Chat/reasoning on left, live data table on right. As AI works, the table populates with status (Qualified/Disqualified/Pending). Left panel shows **Qualification Conditions** - the rules being applied. User sees both the logic AND the results.*

Key insight: The left panel isn't just chat history - it's a **visual explanation of the problem structure**. Like asking Claude for ASCII diagrams to explain a concept, except the diagram is interactive and updates in real-time.

---

## The Opportunity

When processing documents, Claude often encounters edge cases:
- Low confidence extractions
- Ambiguous classifications
- Missing required fields
- OCR quality issues
- Duplicate detection
- Date format ambiguities

Today: Claude describes these in text. User has to parse and respond.

**Tomorrow: Surface edge cases as visual cards/panels that user can interact with.**

---

## Proposed UI: Chat + Edge Case Panel

```
┌──────────────────────────────────────────────────────────────────────┐
│  Files (18)  │  Rules  │  AI Analyst ✨  │  Reports (60)            │
├──────────────────────────────────────────────────────────────────────┤
│                         │                                            │
│  CHAT PANEL             │  VISUAL ARTIFACT PANEL                    │
│                         │                                            │
│  ┌───────────────────┐  │  ┌────────────────────────────────────┐   │
│  │ Claude: Found 12  │  │  │ Edge Cases (12)     Filter ▾      │   │
│  │ edge cases that   │  │  │                                    │   │
│  │ need your input   │  │  │ ┌────────────────────────────────┐│   │
│  └───────────────────┘  │  │ │ CRITICAL  Invoice #INV-2024    ││   │
│                         │  │ │ Amount: $1,234 or $12,340?     ││   │
│  ┌───────────────────┐  │  │ │ [View Doc] [Pick $1,234]       ││   │
│  │ User: The one     │  │  │ │ [Pick $12,340] [Skip]          ││   │
│  │ from ABC Corp     │  │  │ └────────────────────────────────┘│   │
│  │ should be $12,340 │  │  │                                    │   │
│  └───────────────────┘  │  │ ┌────────────────────────────────┐│   │
│                         │  │ │ HIGH  Receipt_Old_Scan.jpg     ││   │
│  ┌───────────────────┐  │  │ │ Low DPI (72). Confidence: 76%  ││   │
│  │ Claude: Got it.   │  │  │ │ [View Doc] [Accept Anyway]     ││   │
│  │ Updated. 11 more. │  │  │ │ [Request Re-scan]              ││   │
│  └───────────────────┘  │  │ └────────────────────────────────┘│   │
│                         │  │                                    │   │
│  [Input: Ask or assign] │  │ ┌────────────────────────────────┐│   │
│                         │  │ │ MEDIUM  Medical Report pg 3-7  ││   │
│                         │  │ │ Overlapping date ranges found  ││   │
│                         │  │ │ [View Doc] [Merge] [Keep Both] ││   │
│                         │  │ └────────────────────────────────┘│   │
│                         │  │                                    │   │
└──────────────────────────┴──────────────────────────────────────────┘
```

---

## Edge Case Types to Surface

| Severity | Type | Visual Treatment |
|----------|------|------------------|
| CRITICAL | Amount ambiguity ($1,234 vs $12,340) | Red card, must resolve |
| CRITICAL | Missing required field | Red card, suggest sources |
| HIGH | Low OCR confidence (<85%) | Orange card, show preview |
| HIGH | Classification uncertainty | Orange card, suggest options |
| MEDIUM | Duplicate detection | Yellow card, show both |
| MEDIUM | Date format ambiguity (01/02/24) | Yellow card, pick format |
| LOW | Minor spelling variations | Gray card, auto-resolve option |

---

## Interaction Patterns

### 1. Direct Card Actions
User clicks button on card → resolved immediately
- "Pick $12,340" → updates extraction, card disappears
- "Accept Anyway" → marks as accepted, moves on
- "Skip" → defers for later

### 2. Chat + Card Coordination
User mentions card in chat → AI responds with context
- User: "The ABC Corp one" → AI knows which card, provides reasoning
- User: "Resolve all duplicates by keeping the newer one" → batch action

### 3. Card → Document Deep Dive
"View Doc" → opens PDF viewer with citation highlighted
User can verify source before deciding

### 4. Bulk Actions
Filter cards → Select multiple → Apply same resolution
"Accept all LOW severity items"

---

## Technical Approach: Just-in-Time UI

Inspired by json-render.dev:

1. **AI generates structured JSON** for edge cases:
```json
{
  "edgeCases": [
    {
      "id": "ec-001",
      "severity": "critical",
      "type": "amount_ambiguity",
      "documentId": "doc-123",
      "field": "amount",
      "options": ["$1,234", "$12,340"],
      "context": "OCR detected comma, could be decimal separator",
      "citation": { "page": 2, "bbox": [...] }
    }
  ]
}
```

2. **React component renders cards** from this JSON
3. **User actions update the JSON** → mutations back to DB
4. **Chat has access to the same JSON** → can reference and modify

This is the "Generative UI" pattern - AI produces structured data, UI components render it dynamically.

---

## What About Excel?

User said: *"The excel is just an excel, i don't think the user really cares. He can just download it."*

Options:
1. **Keep Excel as download-only** - Don't show in panel, just download button
2. **Show Excel preview** - Read-only embedded view when relevant
3. **Show Excel with edge cases highlighted** - Cells that need attention are marked

Recommendation: **Start with edge cases panel.** Excel preview can be added later if users ask. The value is in surfacing problems, not showing the output.

---

## Comparison: Before vs After

### Before (Chat Only)
```
Claude: I found 12 issues with the extraction:
1. Invoice INV-2024 has an ambiguous amount - could be $1,234 or $12,340
2. Receipt_Old_Scan.jpg has low DPI...
3. ...

User: [reads wall of text, tries to remember which is which]
```

### After (Chat + Visual Panel)
```
Claude: Found 12 edge cases. I've surfaced them in the panel -
        2 critical, 4 high, 6 medium. Start with the red ones?

User: [sees cards, clicks "View Doc" on first one, makes decision]
```

---

## Implementation Phases

### Phase 1: Edge Case Panel MVP
- Add right panel to AI Analyst tab
- AI generates edge cases as structured JSON
- Render as cards with severity badges
- Basic actions: View Doc, Accept, Skip

### Phase 2: Chat + Panel Coordination
- Chat can reference cards ("resolve the ABC Corp one")
- Card actions reflected in chat history
- Bulk actions via chat ("accept all low severity")

### Phase 3: More Artifact Types
- Extraction summary table
- Document comparison view
- Timeline visualization for date issues
- Excel preview when generating reports

---

## Open Questions

1. **How does AI generate the edge case JSON?**
   - During processing? On-demand when user opens Analyst?
   - Tool call that returns structured data?

2. **Persistence?**
   - Store edge cases in DB (new table)?
   - Or generate fresh each session?

3. **What if user resolves via chat only?**
   - Panel should update to reflect resolutions
   - Bidirectional sync needed

4. **Mobile?**
   - Stack panels vertically?
   - Or hide panel, show only on demand?

---

## References

- [json-render.dev](https://json-render.dev/) - Just-in-time UI rendering from JSON
- [Vercel AI SDK Generative UI](https://sdk.vercel.ai/docs/ai-sdk-rsc/generative-ui) - React Server Components for AI
- Clay/Similar tools - Chat + data table pattern

---

## Screenshots (Referenced Above)

1. **json-render-edge-cases.png** - json-render.dev showing JSON→UI pattern with edge case cards (CRITICAL/HIGH/MEDIUM severity) *(description only - temp file lost)*
2. **sunder-current-analyst.png** - Current Sunder AI Analyst: chat-only with quick action cards *(description only - temp file lost)*
3. **Screenshot 2026-01-25 at 11.21.56 AM.png** - Origami Agents (app.origamiagents.com): Chat/rules on left, live data table on right with Qualified/Disqualified/Pending statuses

