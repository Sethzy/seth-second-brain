---
type: raw_capture
source_type: x
title: "Sunder sync: AI Coding Workflows.md"
url: "https://addyosmani.com/blog/devtools-mcp/"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/04_Archive/AI Coding Workflows.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "04_Archive/AI Coding Workflows.md"
sha256: "b883bd3d1f51587f61f0b5bb6168f8a42ae0c1d8cb8153ffa591f43056f455e5"
duplicate_of: ""
---

# Sunder sync: AI Coding Workflows.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/04_Archive/AI Coding Workflows.md`

Primary URL: https://addyosmani.com/blog/devtools-mcp/

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-12
tags:
  - tool
  - ai-coding
  - workflows
category: ai
---

# AI Coding Workflows

Advice and patterns for AI-assisted development.

---

## Philosophy & Mindset

### Warren

- Prompts are mostly trial and error - don't over-index. More important to be a careful reviewer of the work.
- If you see a coding pattern that works, feed it back to the AI as an example. But this implies you understand it.
- Chrome DevTools MCP for frontend work: https://addyosmani.com/blog/devtools-mcp/
- Use Raycast shortcuts to auto-complete common prompts like `--dangerously-skip-permissions`

### Mudit

**Tool Stack:**
- Claude Code = primary frontend tool (superior to Cursor for most workflows)
- Windsurf = inline editing + basic autocomplete alongside CC

**Key Principles:**
- Manual review required for every AI-generated change
- Review diffs line by line before approval
- Never grant push/delete permissions to AI
- Context window limitations create siloed development (large repos exceed capacity → scattered code)

**Role Shift:**
- Code writer → code reviewer
- 10x productivity through review-based approach
- Architecture research delegated to AI with human oversight

### Simon Willison: Vibe Engineering

**Source:** https://simonwillison.net/2025/Oct/7/vibe-engineering/

Distinguishes "vibe engineering" from "vibe coding" - the former is sophisticated AI-assisted work by experienced professionals who maintain full responsibility for production software.

**Core Insight:**
- AI tools amplify existing expertise
- Senior engineers excel because they already practice the required disciplines
- Working with agents demands operating "at the top of your game"

**Prerequisites for Success:**
- Robust test suites - enables agents to iterate effectively
- Advance planning - improves agent performance substantially
- Comprehensive documentation - helps models access APIs without reading full codebases
- Strong version control habits - facilitates tracking and debugging
- Code review culture - essential for quality assurance
- Manual QA skills - catches edge cases agents miss

**Workflow:**
- Run multiple agents simultaneously on parallel problems
- Invest heavily in code review
- Research approaches, define specs, design loops
- Strong intuition about what to outsource vs handle manually
- Updated estimation skills reflecting AI's variable impact on timelines

### Peter Steinberger: Just Talk To It

**Source:** https://steipete.me/posts/just-talk-to-it

Practical agentic engineering workflow - argues for simplicity over complexity.

**Tool Choice:**
- GPT-5-Codex preferred for speed, efficiency, pragmatic output
- "Just talk to it" beats elaborate prompt engineering frameworks

**Workflow:**
- Multiple parallel agents in same folder with atomic commits
- Faster than branching strategies
- ~20% time on refactoring, all handled by agents

**Against Overcomplexity:**
- Dismisses subagents, elaborate agent frameworks, MCPs as unnecessary overhead
- Most tools add context waste rather than value
- Simpler CLIs (tmux, git) often outperform specialized agentic tools

**Key Insights:**
- Shorter, image-based prompts work better than extensive prompting
- "Blast radius" thinking - scope changes strategically to prevent costly mistakes
- Senior engineering intuition > magical prompts
- Tool proliferation often masks model inefficiencies

---

## Tool-Specific Workflows

### Cursor Agent Workflows

**Source:** https://cursor.com/docs/cookbook/agent-workflows

Cursor's Agent handles autonomous search, code editing, and command execution.

**Key Patterns:**
- **Test-Driven Development** - Agent runs tests, sees failures, iterates automatically
- **Command Automation** - Store multi-step workflows as Markdown in `.cursor/commands/` (e.g., `/pr`, `/fix-issue`)
- **Codebase Navigation** - Answers architecture/pattern questions via grep + semantic search
- **Visual Processing** - Converts design mockups/screenshots directly into functional components
- **Long-Running Loops** - Hooks enable extended iterations until goals achieved

**Use Cases:**
- Onboarding devs via interactive codebase exploration
- Generating architecture diagrams
- Design-to-code implementation
- Background task delegation (refactoring, bug fixes) to cloud agents
- Visual debugging via screenshot analysis

### Codex Workflows

#### Shipping at Inference Speed

**Source:** https://steipete.me/posts/2025/shipping-at-inference-speed

Peter Steinberger documents how AI coding agents (particularly GPT-5.2 Codex) have transformed development workflow, enabling building software at unprecedented speeds with minimal manual code reading.

**Model Performance:**
- Quality prompts produce working code immediately
- Codex excels at large refactors through deep file analysis (10-15 min reading before writing)
- GPT-5.2's knowledge cutoff (Aug 2024) provides advantage over Claude Opus

**Paradigm Shifts:**
- No longer reads most code—"watches the stream" and focuses on architecture/structure
- Moved away from "plan mode" → collaborative conversations where model explores and builds together
- Language/ecosystem and dependency selection remain highest-value decisions

**Best Practices:**
1. **Start with CLIs first** before UI—agents verify output efficiently
2. **Structure codebases for agent efficiency** rather than human readability
3. **Use documentation strategically**: maintain docs/*.md files for consistency
4. **Embrace linear development**: commit to main directly; ongoing refactoring
5. **Cross-reference existing solutions** across projects
6. **Pair images with minimal text** for UI iteration
7. **Configure appropriately**: increase token limits and auto-compact thresholds

**Critical Point:**
Agent-assisted development still requires understanding "where things are and how systems connect"—architectural thinking remains essential.

#### OpenAI ExecPlans Framework

**Source:** https://cookbook.openai.com/articles/codex_exec_plans

ExecPlans are comprehensive design documents enabling Codex to tackle multi-hour, complex tasks. One case: "seven hours from a single prompt."

**Core Principles:**
- **Self-Containment:** Plans must include all knowledge needed—no external references
- **Living Documents:** Continuous updates required. "It should always be possible to restart from only the ExecPlan."
- **Observable Outcomes:** Success = demonstrable behavior, not mere code changes

**Essential Sections:**
Every ExecPlan needs:
- **Progress:** Timestamped checkbox tracking
- **Surprises & Discoveries:** Unexpected findings with evidence
- **Decision Log:** Rationale for changes
- **Outcomes & Retrospective:** Lessons and remaining work

**Best Practices:**
- Define terminology in plain language immediately
- Prioritize user-visible effects over implementation details
- Include concrete test commands and expected transcripts
- Write prose-first narratives (not checklists except Progress)
- Provide recovery paths for risky operations
- Validate comprehensively before completion

**Philosophy:**
"A single, stateless agent—or human novice—can read your ExecPlan from top to bottom and produce a working, observable result."

#### Dual-Agent Workflow: Codex + Claude Code

**Source:** https://x.com/alexfinn/status/2012653446349131953

**Setup:**
- **Left screen:** Codex 5.2 xhigh
- **Right screen:** Claude Code Opus 4.5

**Workflow:**
1. **Start with Claude Code in plan mode** — let it design the approach
2. **Validate plans with Codex** — copy/paste every plan, get critical feedback, feed back to CC
3. **Use Codex to fix CC mistakes** — when Claude messes up, have Codex diagnose and fix
4. **Cross-review all changes** — every change either agent makes, have the other review it
5. **Let the cleaner win** — primarily use whichever agent is last to clean up the other's mess

**Benefits:**
- 10x faster app production
- Feels like managing a team of engineers
- Each agent catches the other's blind spots

### Claude Code Workflows

#### Claude 4 Best Practices

**URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices

**General Principles:**
- Be explicit with instructions - Claude 4.x follows precisely, so request "above and beyond" behavior explicitly
- Add context/motivation behind instructions - explain *why* for better results
- Examples matter - Claude pays close attention, ensure they align with desired behavior

**Long-Horizon & State Tracking:**
- Claude 4.5 excels at multi-context-window workflows with incremental progress
- Use structured formats (JSON) for state data, unstructured text for progress notes
- Use git for state tracking across sessions
- First context window: set up framework (tests, scripts). Future windows: iterate on todo-list

**Tool Usage:**
- Be explicit about taking action vs suggesting ("Change this function" not "Can you suggest changes")
- For proactive action: "implement changes rather than only suggesting them"
- Claude 4.x aggressive with parallel tool calls - steerable with prompts
- Reduce "CRITICAL/MUST" language - Claude 4.5 more responsive, may overtrigger

**Key Prompting Patterns:**

Reduce overengineering:
```
Avoid over-engineering. Only make changes that are directly requested or clearly necessary. Keep solutions simple and focused.
```

Code exploration:
```
ALWAYS read and understand relevant files before proposing code edits. Do not speculate about code you have not inspected.
```

Minimize hallucinations:
```
Never speculate about code you have not opened. Give grounded and hallucination-free answers.
```

Parallel tool calls:
```
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in parallel.
```

#### Subagent Orchestration

- Claude 4.5 recognizes when to delegate to subagents proactively
- Ensure well-defined subagent tools available
- Steerable if needed: "Only delegate when task clearly benefits from separate agent"

---

## Evaluation & Testing

### Evaluating AI Agents (Anthropic)

**Source:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

**Key Takeaways:**
- Combine evaluation methods: code-based graders (fast), model-based graders (flexible), human graders (highest quality)
- Track pass@k (at least one success) and pass^k (all trials succeed) for non-deterministic outputs
- Start with 20-50 realistic test cases from actual failures
- Grade outputs, not execution paths - agents find valid solutions evaluators didn't anticipate
- Read transcripts regularly to distinguish agent failures from flawed eval logic

**Practical Advice:**
- Start immediately with manual checks already performed during dev
- Build balanced test suites testing both when behaviors should/shouldn't occur
- Design isolated environments preventing cross-trial contamination
- Treat eval maintenance as routine engineering work

---

## Community Resources

### Skills & Tools

#### Beads (Steve Yegge)
- **URL:** https://github.com/steveyegge/beads
- Git-backed graph issue tracker for AI agents
- Replaces messy markdown plans with dependency-aware graph
- Hash-based IDs (bd-a1b2) prevent merge conflicts
- Semantic summarization preserves token budget

#### Agent Templates (AITMPL)
- **URL:** https://www.aitmpl.com/agents
- Ready-made configs: Agents, Commands, Settings, Hooks, MCPs, Plugins, Skills
- Pre-built stacks for OpenAI, Stripe, Salesforce, Shopify, AWS, GitHub
- Free, MIT licensed

#### Notion Skills
- **URL:** https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0
- Official Notion integration skills

### Guides & Tutorials

#### Nader's Agent Guide
- **URL:** https://nader.substack.com/p/the-complete-guide-to-building-agents
- Complete walkthrough building code review agent
- Covers: streaming, structured output, permissions, subagents, MCP, cost tracking

#### Training
- **Skilljar:** https://anthropic.skilljar.com/claude-code-in-action

#### Simon Willison on Claude Skills
- **URL:** https://simonwillison.net/2025/Oct/16/claude-skills/

### Key Repos

- **Reconciliation template:** https://github.com/Sethzy/template-workflow-extract-reconcile-invoice
- **Agent SDK Overview:** https://platform.claude.com/docs/en/agent-sdk/overview
- **Building Agents:** https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- **Agent SDK Demos:** https://github.com/anthropics/claude-agent-sdk-demos/tree/main/excel-demo
- **Vercel Sandbox Guide:** https://vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk

### Video Resources

- https://www.youtube.com/watch?v=TqC1qOfiVcQ
- https://youtu.be/CEvIs9y1uog (Workflow dev kit + AI SDK)

### X/Twitter Links

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

