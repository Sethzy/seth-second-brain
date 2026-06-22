---
type: raw_capture
source_type: x
title: "Sunder sync: 68-twitter-prukalpa-shared-context-FULL.md"
url: "https://x.com/prukalpa/status/2020250930680328695"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/68-twitter-prukalpa-shared-context-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/68-twitter-prukalpa-shared-context-FULL.md"
sha256: "1c498e878f4d350f412dacbde86b3dfe6beffcdd1fb802ebb3026be272487c1e"
duplicate_of: ""
---

# Sunder sync: 68-twitter-prukalpa-shared-context-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/68-twitter-prukalpa-shared-context-FULL.md`

Primary URL: https://x.com/prukalpa/status/2020250930680328695

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter - @prukalpa: Shared Context Solution for Agent Teams

**URL:** https://x.com/prukalpa/status/2020250930680328695
**Author:** Prukalpa ✨ (@prukalpa) - Verified
**Posted:** 5:38 AM · Feb 8, 2026
**Engagement:** 3 replies, 4 reposts, 23 likes, 34 bookmarks, 5.2K views

## Summary
Prukalpa shares her breakthrough solution for multi-agent shared context. "Shared Context will be the biggest and cost complex problem to solve in the journey to build an autonomous organization." File structure: ACCESS.md (agent permissions), CONTEXT.md (working context), research/ folder. "Last updated by" headers track agent contributions. Eliminates cold starts when initiating agents on projects.

## Full Content

"Shared Context Changed Everything"

> Shared Context will be the biggest and cost complex problem to solve in the journey to build an autonomous organization.

One of my big breakthroughs was treating project context like a shared workspace with a central directory where any agent can read and update.

When one agent learns something, it logs it so the next agent has full context. This eliminated the cold starts when I initiated agents on projects.

The key here is to develop a file structure for your context that makes sense.

### Each project has its own folder with the following structure:

- **ACCESS.md** - outlines which agents have access
- **CONTEXT.md** - the working context for that project
- **research/** - the folder with all supporting documents

Context files have a "Last updated by" header so I know who touched it.

Any agent can read any project unless ACCESS.md denies them, then when an agent learns new context, they update CONTEXT.md

**Quote Tweet:** Kevin Simback's agent teams guide (Item 67)

## Analysis

**Problem Identification:** "Biggest and cost complex problem" - Prukalpa identifies shared context as the fundamental challenge in multi-agent coordination, not tool access or model selection.

**Cold Start Elimination:** The primary value prop is eliminating context re-explanation when spawning agents. Each agent inherits full project state immediately.

**Write Permissions:** Agents can update CONTEXT.md as they learn - this creates a living document that compounds knowledge across agent sessions.

**Access Control:** ACCESS.md provides selective context visibility. Some agents shouldn't see certain projects.

**Attribution:** "Last updated by" headers enable tracking which agent made which changes - important for debugging and understanding agent behavior.

**Research Isolation:** Supporting documents in research/ folder keeps context clean while preserving source materials.

## File Structure Pattern

```
projects/
└── project-name/
    ├── ACCESS.md         ← Permissions (which agents can read)
    ├── CONTEXT.md        ← Living project context (agents update)
    └── research/         ← Supporting documents
        └── ...
```

## Strategic Implications

**Context as Infrastructure:** Prukalpa's insight is that context management IS the infrastructure for autonomous organizations. This is more fundamental than agent coordination patterns or tool integrations.

**Shared Write Access:** Unlike read-only knowledge bases, CONTEXT.md is collaboratively edited by agents. This creates emergent documentation that stays current.

**Permission Model:** ACCESS.md suggests hierarchical or role-based access - not all agents should have full context visibility. Security and information compartmentalization matter even for agents.

**Attribution Layer:** "Last updated by" headers provide accountability and debugging paths. When context is wrong, you can trace it back to the agent that added it.

**Comparison to JUMPERZ (Item 66):** JUMPERZ uses Discord channels for memory. Prukalpa uses file-based context. Both solve the same problem (shared knowledge) with different infrastructure.

## Technical Questions

- **Merge Conflicts:** What happens when two agents update CONTEXT.md simultaneously?
- **Context Versioning:** Is there git-based versioning for CONTEXT.md changes?
- **Context Size:** How large do CONTEXT.md files grow? Is there a token budget?
- **Context Summarization:** Do agents summarize old context to prevent bloat?

## Categories
#shared-context #multi-agent #knowledge-management #context-persistence #agent-memory #file-structure #autonomous-organization

## Related Items
- Item 67: Kevin Simback's agent teams guide (quote tweet)
- Item 66: JUMPERZ's Discord channels as memory (alternative approach)
- Pattern: Context management as core infrastructure
- Pattern: Collaborative knowledge bases edited by agents

