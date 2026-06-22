---
type: raw_capture
source_type: x
title: "Sunder sync: SKILL.md"
url: "https://twitter.com/x/123"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/phone/SKILL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/phone/SKILL.md"
sha256: "54569638e4d5eee5de13857bdbeff0babcf9ded5ba4e2a53ebfb242327b54a86"
duplicate_of: ""
---

# Sunder sync: SKILL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/phone/SKILL.md`

Primary URL: https://twitter.com/x/123

Duplicate of existing source-map entry: `none`

## Capture Text

---
name: phone
description: Capture ideas and notes to the Obsidian vault inbox with proper formatting. Use when the user says "I'm on mobile", "I'm on my phone", "use phone skill", "capture this", "inbox", "save this idea", "quick note", or shares rambling thoughts/links they want saved for later processing.
---

# Phone Capture

## Execution

**Announce at start:** "Capturing to inbox."

**Tone:** Direct, results-focused. Extremely concise, sacrifice grammar for brevity.

## Instructions

**NEVER ask for clarification. Auto-detect and route.**

1. **Detect type** from user input (use best judgment, never ask):
   | Type | Triggers | Tag |
   |------|----------|-----|
   | product-idea | "product idea", "feature", "build this", "ship this", product concepts | `product-idea` |
   | sales-idea | "sales idea", "segment", "outreach", "referral", "partnership", client feedback on sales | `sales-idea` |
   | marketing-idea | "marketing idea", "content idea", "campaign", marketing concepts | `marketing-idea` |
   | demo-video | "demo video", "demo script", "video script" | `demo-video` |
   | contract | "contract", "agreement", "legal template" | `contract` |
   | proposal-template | "proposal email", "email template", "outreach template" | `proposal-template` |
   | competitor | specific company news/features, "they launched", "[Company] just..." | `competitor` |
   | intel | general market trends, industry news, articles (not about specific competitor) | `intel` |
   | tool | "library", "tool", "framework", open source, dev tools | `tool` |
   | general | anything else | `inbox` |

   **Competitor vs Intel:** If about a *specific company* → competitor. If about *general trends* → intel.

   **Sales Assets (demo-video, contract, proposal-template):** These go to inbox for later processing via `/general-inbox` which routes to `02_Areas/Sales/Proposals/` subfolders.

2. Extract the core idea from user's input
3. If URLs are provided, fetch and summarize the content
4. Create note at `00_Inbox/YYYY-MM-DD - Note - [Brief Title].md` using the template below
5. Branch and push (merge happens on desktop via `/git`):
   ```bash
   BRANCH="inbox/$(date +%Y%m%d-%H%M%S)"
   git checkout -b $BRANCH
   git add .
   git commit -m "add: inbox - [brief description]"
   git push -u origin $BRANCH
   ```
6. Confirm: filename + type tag + "pushed to inbox/[branch], will merge on desktop"

**Link-only input:** If user just drops a link with minimal context, use WebFetch to read the full content, then generate the title and summary from the article. The Idea section becomes a summary of what the article is about, and Reference Material contains key takeaways.

## Note Template

```markdown
---
created: YYYY-MM-DD
tags: [inbox, TYPE_TAG]
source: [URL if provided, otherwise omit]
status: captured
---

# [Clear Title]

## Idea

[2-3 sentence summary of the core idea]

## Details

[Bullet points with additional context, if any]

## Reference Material

[If URLs provided, include for each link:]
- **[Page Title](URL)**
  - [2-3 bullet summary of the content]
  - [Key takeaways relevant to the idea]

[Omit this section if no links provided]

## Next Steps

- [ ] Review and process
```

## Example

**Input:** "I'm on my phone - saw cool AI invoice thing on twitter might be good for sunder https://twitter.com/x/123"

**Output:** `00_Inbox/2026-01-11 - Note - AI Invoice Processing Idea.md`

```markdown
---
created: 2026-01-11
tags: [inbox, product-idea]
source: https://twitter.com/x/123
status: captured
---

# AI Invoice Processing Idea

## Idea

Potential feature opportunity - AI invoice processing could be relevant to Sunder's product.

## Details

- Saw example on Twitter of company automating invoice processing
- Worth exploring as a product feature

## Reference Material

- **[Thread: How we automated 10k invoices/month](https://twitter.com/x/123)**
  - Company reduced invoice processing time by 80% using AI
  - Key tech: OCR + LLM for data extraction
  - Integration with existing ERP systems

## Next Steps

- [ ] Review and process
```
