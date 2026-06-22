---
type: raw_capture
source_type: x
title: "Sunder sync: 80-twitter-vox-agent-company-FULL.md"
url: "https://x.com/voxyz_ai/status/2019914775061270747"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/80-twitter-vox-agent-company-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/80-twitter-vox-agent-company-FULL.md"
sha256: "2422ef2667cfe1e5ece7c3fe6c29e18df33843cfc61e29ef9c8e83cf6401e215"
duplicate_of: ""
---

# Sunder sync: 80-twitter-vox-agent-company-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/80-twitter-vox-agent-company-FULL.md`

Primary URL: https://x.com/voxyz_ai/status/2019914775061270747

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @Voxyz_ai: I Built an AI Company - Two Weeks Later, They Run It Themselves

**URL:** https://x.com/voxyz_ai/status/2019914775061270747
**Author:** Vox (@Voxyz_ai) - Verified
**Posted:** Feb 7, 2026 (inferred)
**Engagement:** 125 replies, 456 reposts, 3.1K likes, 9.2K bookmarks, 998.6K views

## Summary
Epic article: 6 AI agents autonomously run VoxYZ Agent World website. Stack: OpenClaw (VPS), Next.js+Vercel, Supabase. Agents: Minion (decisions), Sage (strategy), Scout (intel), Quill (content), Xalt (social), Observer (QA). Solved 3 pitfalls: (1) Two places fighting over work - VPS sole executor (2) Triggered but nobody picked it up - unified createProposalAndMaybeAutoApprove function (3) Queue growing when quota full - Cap Gates reject at proposal entry. Triggers + Reaction Matrix create spontaneous inter-agent interaction with probability (0.3 = 30% chance Growth analyzes tweet). Self-healing: recoverStaleSteps marks failed after 30min.

## Key Architecture
- Closed loop: Proposal → Auto-approve → Mission → Worker → Event → Trigger → Proposal
- Cap Gates: Reject at entry, don't pile queue
- Reaction Matrix: Probabilistic inter-agent responses  
- VPS=executor, Vercel=control plane
- Cooldowns prevent trigger spam

## Categories
#openclaw #vercel #supabase #6-agents #autonomous-company #closed-loop #cap-gates #reaction-matrix #self-healing

