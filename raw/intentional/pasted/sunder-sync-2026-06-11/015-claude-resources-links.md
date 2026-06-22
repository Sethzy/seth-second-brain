---
type: raw_capture
source_type: x
title: "Sunder sync: Claude Resources & Links.md"
url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/04_Archive/Claude Resources & Links.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "04_Archive/Claude Resources & Links.md"
sha256: "79f8feacdd5f01f4cc9001b77ae3c966c560629dc96cb44d01f0ea5a2bf688c0"
duplicate_of: ""
---

# Sunder sync: Claude Resources & Links.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/04_Archive/Claude Resources & Links.md`

Primary URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-16
tags:
  - tool
  - ai
  - claude
  - resources
category: ai
status: unsorted
---

# Claude Resources & Links

> Unsorted collection of Claude-related resources, guides, and links. To be organized later.

---

## Claude 4 Best Practices

**URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

### General Principles
- Be explicit with instructions - Claude 4.x follows precisely, so request "above and beyond" behavior explicitly
- Add context/motivation behind instructions - explain *why* for better results
- Examples matter - Claude pays close attention, ensure they align with desired behavior

### Long-Horizon & State Tracking
- Claude 4.5 excels at multi-context-window workflows with incremental progress
- Use structured formats (JSON) for state data, unstructured text for progress notes
- Use git for state tracking across sessions
- First context window: set up framework (tests, scripts). Future windows: iterate on todo-list

### Tool Usage
- Be explicit about taking action vs suggesting ("Change this function" not "Can you suggest changes")
- For proactive action: "implement changes rather than only suggesting them"
- Claude 4.x aggressive with parallel tool calls - steerable with prompts
- Reduce "CRITICAL/MUST" language - Claude 4.5 more responsive, may overtrigger

### Key Prompting Patterns

**Reduce overengineering:**
```
Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.
```

**Code exploration:**
```
ALWAYS read and understand relevant files before proposing code edits. Do not speculate about code you have not inspected.
```

**Minimize hallucinations:**
```
Never speculate about code you have not opened. Give grounded and hallucination-free answers.
```

**Parallel tool calls:**
```
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in parallel.
```

### Subagent Orchestration
- Claude 4.5 recognizes when to delegate to subagents proactively
- Ensure well-defined subagent tools available
- Steerable if needed: "Only delegate when task clearly benefits from separate agent"

---

## Example: Frontend Design Skill

**Source:** https://claude.com/blog/improving-frontend-design-through-skills

### Problem
Claude generates generic "AI slop" frontends (Inter fonts, purple gradients, minimal animations) due to distributional convergence.

### Solution
Use Skills to provide targeted design guidance on-demand:

1. **Frontend Aesthetics Skill** (~400 tokens)
   - Typography: distinctive fonts from Google Fonts
   - Color/theme: avoid generic purple gradients
   - Motion: meaningful animations
   - Backgrounds: patterns, gradients, visual interest

2. **Web-Artifacts-Builder Skill**
   - React + Tailwind CSS + shadcn/ui
   - Bundle into single HTML via Parcel

### Key Insight
Prompt at the right "altitude" - "use distinctive fonts from Google Fonts" works better than specific hex codes. Skills deliver specialized knowledge on-demand without bloating system prompts.

**Pattern:** Any domain where Claude produces generic output is a candidate for Skill development.

---

## Community Skills & Tools

### Design Skill (Dammyjay93)
- **URL:** https://github.com/Dammyjay93/claude-design-skill
- Enterprise-grade UI design guidance
- 6 design personalities: Precision, Warmth, Sophistication, Boldness, Utility, Data
- Anti-patterns: dramatic shadows, asymmetric padding, decorative gradients
- Install to `~/.claude/skills/design-principles/`

### Beads (Steve Yegge)
- **URL:** https://github.com/steveyegge/beads
- Git-backed graph issue tracker for AI agents
- Replaces messy markdown plans with dependency-aware graph
- Hash-based IDs (bd-a1b2) prevent merge conflicts
- Semantic summarization preserves token budget

### Agent Templates (AITMPL)
- **URL:** https://www.aitmpl.com/agents
- Ready-made configs: Agents, Commands, Settings, Hooks, MCPs, Plugins, Skills
- Pre-built stacks for OpenAI, Stripe, Salesforce, Shopify, AWS, GitHub
- Free, MIT licensed

### Notion Skills
- **URL:** https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0
- Official Notion integration skills

---

## Guides & Tutorials

### Nader's Agent Guide
- **URL:** https://nader.substack.com/p/the-complete-guide-to-building-agents
- Complete walkthrough building code review agent
- Covers: streaming, structured output, permissions, subagents, MCP, cost tracking

### Training
- **Skilljar:** https://anthropic.skilljar.com/claude-code-in-action

### Simon Willison on Claude Skills
- **URL:** https://simonwillison.net/2025/Oct/16/claude-skills/

---

## Key Repos

- **Reconciliation template:** https://github.com/Sethzy/template-workflow-extract-reconcile-invoice
- **Agent SDK Overview:** https://platform.claude.com/docs/en/agent-sdk/overview
- **Building Agents:** https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- **Agent SDK Demos:** https://github.com/anthropics/claude-agent-sdk-demos/tree/main/excel-demo
- **Vercel Sandbox Guide:** https://vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk

---

## Video Resources

- https://www.youtube.com/watch?v=TqC1qOfiVcQ
- https://youtu.be/CEvIs9y1uog (Workflow dev kit + AI SDK)

---

## X/Twitter Links (Unsorted)

- https://x.com/ryancarson/status/2008548371712135632
- https://x.com/aidenybai/status/2008222086830191053
- https://x.com/housecor/status/2008306060193370509
- https://x.com/ryancarson/status/2008950489904472501
- https://x.com/dabit3/status/2009131298250428923
- https://x.com/donvito/status/2009252378017689947
- https://x.com/rlancemartin/status/2009683038272401719
- https://x.com/bcherny/status/2009450715081789767
- https://x.com/rohit4verse/status/2009663737469542875
- https://x.com/jarrodwatts/status/2009451357758214256
- https://x.com/vercel/status/2009769470194266327
- https://x.com/danshipper/status/2009651408144835021
- https://x.com/danshipper/status/2009652998075474153
- https://x.com/anthropicai/status/2009696515061911674
- https://x.com/jerryjliu0/status/2009784608590873075 (structured extraction)
- https://x.com/ryancarson/status/2002478402414973194

---

*To be organized and consolidated later.*

