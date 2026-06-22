---
type: raw_capture
source_type: x
title: "Sunder sync: 2026-01-21-chatbot-onboarding-platform-design.md"
url: "https://x.com/jediahkatz/status/2014805497778733442"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-21-chatbot-onboarding-platform-design.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-01-21-chatbot-onboarding-platform-design.md"
sha256: "68660133608d807c6a56784f759e28beb9df0f101465cc90920e48fffcd08e90"
duplicate_of: ""
---

# Sunder sync: 2026-01-21-chatbot-onboarding-platform-design.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-21-chatbot-onboarding-platform-design.md`

Primary URL: https://x.com/jediahkatz/status/2014805497778733442

Duplicate of existing source-map entry: `none`

## Capture Text

# Chatbot-Driven Onboarding Platform: Design Document

**Date:** 2026-01-21
**Status:** Draft - Pending Approval
**Author:** Claude + Seth

---

## Executive Summary

Transform Sunder from a developer-onboarded SaaS into a **self-serve platform** where users configure their own document-in/document-out workflows through conversational AI.

### The Vision

```
Today:
  Developer runs scripts → TypeScript configs → Redeploy per client

Tomorrow:
  User chats with AI → Config stored in Supabase → Works immediately
```

### Core Insight

The onboarding process (understanding documents, defining schemas, setting up extraction) is fundamentally a **conversation**. Instead of developers translating user requirements into code, let users collaborate directly with AI that can:

- Analyze their sample documents
- Propose configurations
- Test workflows in real-time
- Learn and improve over time

### Key Outcomes

1. **Zero developer involvement** for new client onboarding
2. **No redeployment** - configs are data, not code
3. **Self-healing** - system learns from corrections
4. **Self-serve distribution** - users can "vibe code" any document workflow

---

## It's Orchestration, Not Replacement

The framing matters. If you think of agents as "replacement," you design for autonomy and get frustration. If you think of agents as "orchestration," you design for collaboration and get leverage.

Key patterns that enable effective collaboration:

### Spectrum of Control / Blended Initiative

**The problem:** Treating human-agent interaction as binary—either human is in control or agent is in control—misses the nuanced reality of effective collaboration.

**The solution:** Design for fluid, intentional, reversible control transfer:

- **Human-led:** Human directs, agent executes (e.g., "help me refactor this function")
- **Agent-led:** Agent proposes, human approves (e.g., "I found 10 potential bugs, review them")
- **Blended:** Fluid back-and-forth based on confidence and context

**Implementation:** Agents should explicitly signal confidence levels and when they're crossing control boundaries. Humans should have clear mechanisms to intervene or take back control.

**Key insight:** The goal state isn't fully autonomous or fully manual—it's the dynamic middle where control flows smoothly based on context, confidence, and capability.

### Skill Library Evolution

**The problem:** Agents frequently solve similar problems across different sessions. Without persistence, they must rediscover solutions each time, wasting tokens and time.

**The solution:** Persist working code implementations as reusable skills that evolve over time:

```
Ad-hoc Code → Save Working Solution → Reusable Function → Documented Skill → Agent Capability
```

**Evolution path:**

1. Agent writes code to solve immediate problem
2. If solution works, save to `skills/` directory
3. Refactor for generalization (parameterize hard-coded values)
4. Add documentation (purpose, parameters, returns, examples)
5. Agent discovers and reuses skill in future sessions

**Progressive disclosure optimization:** Instead of loading all skills into context, inject skill descriptions and provide on-demand loading. This achieved 91% token reduction in one implementation (26 tools at 17k tokens → 4 selected tools at 1.5k tokens).

**Key insight:** Organizations want agents to build capability over time, not start from scratch every session. Skills become institutional knowledge.

### Capture Skill Prompt (Reference)

> **Source:** https://x.com/jediahkatz/status/2014805497778733442

The following prompt enables agents to capture learnings, patterns, or workflows from conversations into reusable skills:

```markdown
---
name: capture-skill
description: Capture learnings, patterns, or workflows from the current conversation into a new or existing skill. Use when the user wants to save what was learned, discovered, or built during a conversation as a reusable skill for future sessions.
---

# Capture Skill from Conversation

This skill helps you extract knowledge, patterns, and workflows from the current conversation and persist them as a reusable skill.

## When to Use

- The user says "capture this as a skill" or "save this for next time"
- A useful workflow, pattern, or piece of domain knowledge emerged during the conversation
- The user wants to update an existing skill with new learnings
- The conversation uncovered non-obvious steps, gotchas, or best practices worth preserving

## Capture Process

### Phase 1: Identify What to Capture

Review the conversation for:

1. **Workflows**: Multi-step processes that were figured out through trial and error
2. **Domain knowledge**: Non-obvious facts, configurations, or constraints discovered
3. **Gotchas and fixes**: Problems encountered and their solutions
4. **Patterns**: Code patterns, command sequences, or templates that worked well
5. **Decision rationale**: Why certain approaches were chosen over alternatives

Summarize what you plan to capture and confirm with the user before proceeding.

### Phase 2: Decide Destination

If the user already specified a skill or the destination is obvious from context, just proceed. Otherwise, use the AskQuestion tool (or ask conversationally) to clarify:

1. **New or existing skill?**
   - If existing: Which skill to update? (list relevant skills from `~/.cursor/skills/` and `.cursor/skills/`)
   - If new: What should it be named?

2. **Storage location** (for new skills):
   - Personal (`~/.cursor/skills/`) — available across all projects
   - Project (`.cursor/skills/`) — shared with the repository

### Phase 3: Draft the Skill Content

When capturing into a **new skill**:

1. Choose a descriptive name (lowercase, hyphens, 64 chars)
2. Write a specific description including WHAT and WHEN (third person)
3. Distill the conversation into concise, actionable instructions
4. Include concrete examples drawn from the conversation
5. Add any utility scripts or commands that were used

When updating an **existing skill**:

1. Read the existing SKILL.md
2. Identify where new learnings fit (new section, updated steps, additional examples)
3. Integrate without duplicating existing content
4. Preserve the existing structure and voice

### Phase 4: Distillation Guidelines

The goal is to transform a messy conversation into clean, reusable instructions.

**Do:**
- Extract the final working approach, not the failed attempts (unless gotchas are instructive)
- Generalize from the specific case discussed (replace hardcoded values with placeholders)
- Include the "why" behind non-obvious steps
- Add context the agent wouldn't know without this conversation
- Keep it under 500 lines

**Don't:**
- Include conversation artifacts ("as we discussed", "you mentioned")
- Repeat information the agent already knows
- Include overly specific details that won't transfer to other situations
- Add verbose explanations where a code example suffices

### Phase 5: Write and Verify

1. Create/update the skill file(s)
2. Verify the SKILL.md is under 500 lines
3. Check that the description is specific and includes trigger terms
4. Confirm with the user that the captured content is accurate

## Example: Capturing a Debugging Workflow

If a conversation involved debugging a tricky deployment issue, the captured skill might look like:

\`\`\`markdown
---
name: debug-k8s-deployments
description: Debug Kubernetes deployment failures including CrashLoopBackOff, image pull errors, and resource limits. Use when pods are failing to start or deployments are stuck.
---

# Debug K8s Deployments

## Diagnostic Steps

1. Check pod status: `kubectl get pods -n <namespace> | grep -v Running`
2. Get events: `kubectl describe pod <pod> -n <namespace>`
3. Check logs: `kubectl logs <pod> -n <namespace> --previous`

## Common Issues

### CrashLoopBackOff
- Check if the entrypoint command exists in the container
- Verify environment variables are set (especially secrets)
- Look for OOMKilled in `describe` output → increase memory limits

### ImagePullBackOff
- Verify image tag exists: `docker manifest inspect <image>`
- Check imagePullSecrets are configured for private registries
\`\`\`

Note how this captures the diagnostic sequence and common solutions without any conversation artifacts.

## Handling Edge Cases

**Conversation had multiple topics**: Ask which specific learning to capture, or suggest creating separate skills for distinct topics.

**Learning is too small for a skill**: Suggest creating a Cursor rule (`.cursor/rules/`) instead, which is better suited for single-line or short guidelines.

**Existing skill needs major rewrite**: Confirm with the user whether to restructure the existing skill or create a new one that supersedes it.
```

---

## Architecture Overview

### Three Chatbots, Clear Boundaries

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           SUNDER PLATFORM                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────┐                                                   │
│  │   ONBOARDING     │  Full-screen, mandatory for new orgs              │
│  │   CHATBOT        │  Blocks dashboard until complete                  │
│  │                  │  Then disappears forever                          │
│  │  [Sandbox: ON]   │                                                   │
│  └────────┬─────────┘                                                   │
│           │ completes                                                   │
│           ▼                                                             │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │                         DASHBOARD                               │    │
│  │  ┌─────────────┐    ┌─────────────────────────────────────┐   │    │
│  │  │ MAINTENANCE │    │              CASES                   │   │    │
│  │  │ CHATBOT     │    │  ┌─────────────────────────────┐    │   │    │
│  │  │             │    │  │  Case Container              │    │   │    │
│  │  │ [Sidebar]   │    │  │  ┌───────────────────────┐  │    │   │    │
│  │  │             │    │  │  │   ANALYST CHATBOT     │  │    │   │    │
│  │  │ Sandbox:    │    │  │  │                       │  │    │   │    │
│  │  │ on-demand   │    │  │  │   [Case-scoped]       │  │    │   │    │
│  │  │             │    │  │  │   Sandbox: on-demand  │  │    │   │    │
│  │  └─────────────┘    │  │  └───────────────────────┘  │    │   │    │
│  │                      │  └─────────────────────────────┘    │   │    │
│  │                      └─────────────────────────────────────┘   │    │
│  └────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

| Chatbot | Location | Lifecycle | Scope | Sandbox |
|---------|----------|-----------|-------|---------|
| **Onboarding** | Full-screen overlay | One-time, mandatory | Org setup | Always on |
| **Maintenance** | Sidebar | Always accessible | Org config updates | On-demand |
| **Analyst** | Inside case container | Per-case | Documents in that case | On-demand |

### Data Flow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Onboarding    │     │    Supabase     │     │   Claude API    │
│   Chatbot       │────▶│   org_configs   │────▶│   Skills API    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │ generates             │ stores                │ hosts
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   SKILL.md      │     │  skill_content  │     │    skill_id     │
│   (content)     │     │  skill_id       │     │   (runtime)     │
└─────────────────┘     │  preferences    │     └─────────────────┘
                        └─────────────────┘
                                │
                                │ loaded by
                                ▼
                ┌───────────────────────────────┐
                │  Analyst / DocGen at runtime  │
                └───────────────────────────────┘
```

---

## Data Model

### Supabase Schema

```sql
-- =============================================================================
-- INDUSTRY TEMPLATES
-- Pre-built skill templates for common use cases.
-- Accelerates onboarding by providing starting points.
-- =============================================================================
CREATE TABLE templates (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Identity
  name text NOT NULL,                    -- "PI Law Firm Starter"
  slug text NOT NULL UNIQUE,             -- "pi-law-firm"
  industry text NOT NULL,                -- "law", "insurance", "accounting"
  sub_industry text,                     -- "personal-injury", "workers-comp"

  -- Content
  skill_content text NOT NULL,           -- The template SKILL.md
  description text,                      -- User-facing description
  document_types jsonb,                  -- ["medical-bill", "income-statement", ...]

  -- Metadata
  created_by text NOT NULL DEFAULT 'sunder',  -- 'sunder' or 'derived'
  usage_count int NOT NULL DEFAULT 0,    -- Track popularity
  is_active boolean NOT NULL DEFAULT true,

  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

-- Templates are public (read-only for all authenticated users)
ALTER TABLE templates ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Templates are readable by all authenticated users"
  ON templates FOR SELECT
  USING (auth.role() = 'authenticated' AND is_active = true);


-- =============================================================================
-- ORGANIZATION CONFIGS
-- One row per organization. Stores the complete workflow configuration.
-- =============================================================================
CREATE TABLE org_configs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id uuid NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,

  -- Skill storage
  skill_content text,                    -- SKILL.md content (source of truth)
  skill_id text,                         -- Claude API skill_id (for runtime)
  skill_version text,                    -- Version tracking

  -- Template reference
  template_id uuid REFERENCES templates(id),  -- NULL if started from scratch

  -- Metadata
  industry text,                         -- "law", "insurance", "accounting"
  onboarding_completed_at timestamptz,   -- NULL if still onboarding
  onboarding_progress jsonb,             -- Partial progress for resume

  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),

  UNIQUE(org_id)
);

-- RLS: Org members can read/write their own config
ALTER TABLE org_configs ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Org members can manage their config"
  ON org_configs FOR ALL
  USING (org_id IN (SELECT org_id FROM org_members WHERE user_id = auth.uid()));


-- =============================================================================
-- ORGANIZATION PREFERENCES
-- Learned preferences captured from Analyst corrections.
-- Batched into skill during Maintenance interactions.
-- =============================================================================
CREATE TABLE org_preferences (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id uuid NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,

  preference_text text NOT NULL,         -- Plain English rule
  source_case_id uuid REFERENCES cases(id) ON DELETE SET NULL,  -- Where it came from
  incorporated_at timestamptz,           -- When baked into skill (NULL if pending)

  created_at timestamptz NOT NULL DEFAULT now()
);

-- RLS: Org members can read/write their preferences
ALTER TABLE org_preferences ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Org members can manage preferences"
  ON org_preferences FOR ALL
  USING (org_id IN (SELECT org_id FROM org_members WHERE user_id = auth.uid()));

-- Index for finding unincorporated preferences
CREATE INDEX idx_org_preferences_pending
  ON org_preferences (org_id)
  WHERE incorporated_at IS NULL;
```

### Config Loader (with Migration Support)

```typescript
/**
 * Fetches org config from Supabase, falls back to legacy TypeScript config.
 * Enables gradual migration from hardcoded configs to data-driven.
 */
export async function getOrgConfig(orgId: string): Promise<OrgConfig> {
  // Try Supabase first
  const { data } = await supabase
    .from('org_configs')
    .select('*')
    .eq('org_id', orgId)
    .single();

  if (data?.skill_id) {
    return {
      skillId: data.skill_id,
      skillContent: data.skill_content,
      industry: data.industry,
      source: 'supabase',
    };
  }

  // Fallback to legacy TypeScript config
  const legacyConfig = await getLegacyConfig(orgId);
  if (legacyConfig) {
    return {
      skillId: legacyConfig.skillId,
      skillContent: null,  // Not available for legacy
      industry: legacyConfig.industry,
      source: 'legacy',
    };
  }

  throw new Error(`No config found for org: ${orgId}`);
}
```

---

## Industry Templates

### Purpose

Pre-built skill templates that accelerate onboarding. Instead of building from scratch, users start with a proven template and customize from there.

### Why Templates Matter

| Without Templates | With Templates |
|-------------------|----------------|
| Upload 5+ sample docs | Upload 1-2 docs to verify |
| AI discovers doc types from scratch | Doc types pre-defined |
| 20-30 min onboarding | 5-10 min onboarding |
| Higher chance of missing fields | Battle-tested field coverage |
| User must explain everything | User only explains differences |

### Template Selection Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Industry Selection                                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "What industry are you in?"                                            │
│                                                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │  Law Firm   │ │  Insurance  │ │  Accounting │ │    Other    │       │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (if Law Firm)
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1b: Sub-Industry (if applicable)                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "What type of law does your firm practice?"                            │
│                                                                          │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐           │
│  │ Personal Injury │ │ Workers' Comp   │ │ Family Law      │           │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (if template exists)
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Template Offer                                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "Great! We have a starter template for PI law firms."                  │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ 📋 PI Law Firm Starter                                           │   │
│  │                                                                   │   │
│  │ Includes document types:                                         │   │
│  │ • Medical Bills (with GST validation, provider extraction)       │   │
│  │ • Income Statements (lost wages calculation)                     │   │
│  │ • Police Reports (incident details, parties involved)            │   │
│  │ • Medical Records (treatment timeline)                           │   │
│  │                                                                   │   │
│  │ Output: Excel summary with expense breakdown by category         │   │
│  │                                                                   │   │
│  │ Used by 47 law firms                                             │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌────────────────────────┐  ┌────────────────────────┐                │
│  │  Start with template   │  │  Start from scratch    │                │
│  │     (Recommended)      │  │                        │                │
│  └────────────────────────┘  └────────────────────────┘                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
        ┌───────────────────┐           ┌───────────────────┐
        │  WITH TEMPLATE    │           │  FROM SCRATCH     │
        ├───────────────────┤           ├───────────────────┤
        │ Skip doc upload   │           │ Full onboarding   │
        │ → Refinement      │           │ flow as designed  │
        │ → Quick test      │           │                   │
        │ → Done            │           │                   │
        └───────────────────┘           └───────────────────┘
```

### Template-Accelerated Onboarding

When user selects a template, the flow shortcuts:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TEMPLATE FLOW (shortened)                                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. Industry → Template Selected                                        │
│     ↓                                                                   │
│  2. "Here's what the template includes. What's different for you?"      │
│     ↓                                                                   │
│  3. User: "We also process demand letters" or "Looks good"              │
│     ↓                                                                   │
│  4. If additions needed → brief doc upload + analysis                   │
│     ↓                                                                   │
│  5. "Upload one document to test the workflow"                          │
│     ↓                                                                   │
│  6. Test run → verify → done                                            │
│                                                                          │
│  Total time: 5-10 minutes vs 20-30 minutes                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Refinement Conversation (Template Mode)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Onboarding Chat (Template Selected)                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  AI: "The PI Law Firm template includes:                                │
│                                                                          │
│       📋 Medical Bills - provider, date, amounts, GST, line items       │
│       📋 Income Statements - employer, period, gross/net income         │
│       📋 Police Reports - report number, date, officer, description     │
│       📋 Medical Records - provider, dates, treatments                  │
│                                                                          │
│       Is there anything you process that's not on this list?"           │
│                                                                          │
│  User: "We also process demand letters and settlement offers"           │
│                                                                          │
│  AI: "Got it! Upload a sample demand letter and I'll add that           │
│       document type to your config."                                    │
│                                                                          │
│  [User uploads demand-letter.pdf]                                       │
│  [Sandbox analyzes - but only this new doc type]                        │
│                                                                          │
│  AI: "Added Demand Letters with fields: recipient, claim_amount,        │
│       deadline, case_reference. Want to add Settlement Offers too,      │
│       or should we test what we have?"                                  │
│                                                                          │
│  User: "Let's test first"                                               │
│                                                                          │
│  AI: "Upload any document and I'll process it with your config."        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Initial Templates (V1)

Hand-crafted from existing clients. Starting set:

| Template | Industry | Sub-Industry | Based On |
|----------|----------|--------------|----------|
| **PI Law Firm Starter** | Law | Personal Injury | hoh-law |
| **Workers' Comp Firm** | Law | Workers' Comp | (to create) |
| **Insurance Claims** | Insurance | General | (to create) |
| **Small Business Accounting** | Accounting | General | (to create) |

### Template Creation Process

```typescript
/**
 * Create a template from an existing successful org config.
 * Strips org-specific rules, keeps universal patterns.
 */
async function createTemplateFromOrg(
  orgId: string,
  templateName: string,
  templateSlug: string,
): Promise<string> {
  const orgConfig = await getOrgConfig(orgId);

  // Strip org-specific learned preferences
  const genericSkill = stripOrgSpecificRules(orgConfig.skillContent);

  // Insert template
  const { data } = await supabase.from('templates').insert({
    name: templateName,
    slug: templateSlug,
    industry: orgConfig.industry,
    skill_content: genericSkill,
    description: `Starter template for ${templateName}`,
    document_types: extractDocumentTypes(genericSkill),
    created_by: 'sunder',
  }).select().single();

  return data.id;
}

/**
 * Load template as starting point for new org.
 */
async function initOrgFromTemplate(
  orgId: string,
  templateId: string,
): Promise<void> {
  const { data: template } = await supabase
    .from('templates')
    .select('*')
    .eq('id', templateId)
    .single();

  // Create org config with template skill as starting point
  await supabase.from('org_configs').insert({
    org_id: orgId,
    skill_content: template.skill_content,
    template_id: templateId,
    industry: template.industry,
    // skill_id is NULL - will be created when onboarding completes
  });

  // Increment usage count
  await supabase.rpc('increment_template_usage', { template_id: templateId });
}
```

### Future: Derived Templates

Once we have N successful orgs in an industry, we can analyze patterns:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ DERIVED TEMPLATE PIPELINE (Future)                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  10+ PI law firms onboarded                                             │
│           ↓                                                             │
│  Analyze common document types, fields, validation rules                │
│           ↓                                                             │
│  Identify patterns (90% have medical bills with these 8 fields)         │
│           ↓                                                             │
│  Generate candidate template (anonymized)                               │
│           ↓                                                             │
│  Human review → approve → publish                                       │
│           ↓                                                             │
│  New PI firms get even better starting point                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

This creates a **flywheel**: more clients → better templates → faster onboarding → more clients.

---

## Onboarding Chatbot

### Purpose

Guide new organizations through complete workflow setup. Must be completed before dashboard access is granted.

### Completion Criteria

Onboarding is "done" when the **full workflow has been tested successfully**:
1. At least one document type defined
2. Sample document uploaded and extracted correctly
3. DocGen produces valid output

### Conversation Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Welcome + Industry Selection                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "Welcome to Sunder! Let's set up your document workflow."              │
│                                                                          │
│  "What industry are you in?"                                            │
│                                                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │  Law Firm   │ │  Insurance  │ │  Accounting │ │    Other    │       │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘       │
│                                                                          │
│  [Industry selection helps AI ask better follow-up questions]           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Sample Document Upload                                           │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "Now I need to see what documents you work with."                      │
│                                                                          │
│  "Upload 3-5 sample documents you typically process."                   │
│  "(Medical bills, invoices, reports - whatever you deal with daily)"    │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │                    📄 Drop files here                            │   │
│  │                    or click to browse                            │   │
│  │                                                                   │   │
│  │            Supported: PDF, images, Excel, Word                   │   │
│  │                                                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ━━━━━━━━━━━━━━━━ SANDBOX SPINS UP HERE ━━━━━━━━━━━━━━━━               │
│  (Show nice animation: "Setting up your workspace...")                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 3: AI Analysis                                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  [Claude Code analyzes documents in sandbox]                            │
│  - Identifies document types                                            │
│  - Extracts field patterns                                              │
│  - Detects validation rules                                             │
│                                                                          │
│  "I found 3 types of documents:"                                        │
│                                                                          │
│  📋 Medical Bills (2 samples)                                           │
│     Fields: provider_name, date, total_amount, gst, items[]             │
│                                                                          │
│  📋 Income Statements (2 samples)                                       │
│     Fields: employer, period, gross_income, deductions, net_income      │
│                                                                          │
│  📋 Police Reports (1 sample)                                           │
│     Fields: report_number, date, officer, description                   │
│                                                                          │
│  "Does this look right? Anything I missed?"                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 4: Conversational Refinement                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User: "You missed the case number field on medical bills"              │
│  AI: "Got it - added case_number to Medical Bills. Anything else?"      │
│                                                                          │
│  User: "For income statements, we need to flag if tax seems wrong"      │
│  AI: "I'll add a validation: flag if tax_deducted doesn't match         │
│       expected rate. What rate should I use?"                           │
│                                                                          │
│  User: "15%"                                                            │
│  AI: "Done. I'll flag any income statement where tax isn't ~15%         │
│       of gross income. What else?"                                      │
│                                                                          │
│  User: "That's all for now"                                             │
│  AI: "Great! Now let's define what output you need."                    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 5: Output Definition                                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "What should the final output look like?"                              │
│                                                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                       │
│  │Excel Report │ │PDF Summary  │ │    Both     │                       │
│  └─────────────┘ └─────────────┘ └─────────────┘                       │
│                                                                          │
│  User: [Excel Report]                                                   │
│                                                                          │
│  "What columns/sections do you need? You can describe it or             │
│   show me an example of what you currently produce."                    │
│                                                                          │
│  User: "I need a summary of all medical expenses grouped by provider,   │
│         with a total at the bottom. Flag any that seem duplicated."     │
│                                                                          │
│  AI: "Got it. The Excel will have:                                      │
│       - Summary sheet: totals by provider                               │
│       - Details sheet: all line items                                   │
│       - Flags column for potential duplicates                           │
│       Sound right?"                                                     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 6: Test Run                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "Let's test the full workflow. Upload one more document."              │
│                                                                          │
│  [User uploads test document]                                           │
│                                                                          │
│  "Processing..."                                                        │
│  ✓ Document classified as: Medical Bill                                 │
│  ✓ Fields extracted: provider=SGH, amount=$1,500, gst=$135...           │
│  ✓ Validation passed                                                    │
│  ✓ Excel generated                                                      │
│                                                                          │
│  [Download: test-report.xlsx]                                           │
│                                                                          │
│  "Here's your report. Does everything look correct?"                    │
│                                                                          │
│  ┌─────────────┐ ┌─────────────────────────┐                           │
│  │  Looks good │ │ Something needs fixing  │                           │
│  └─────────────┘ └─────────────────────────┘                           │
│                                                                          │
│  [If "needs fixing" → return to Step 4 refinement loop]                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 7: Completion                                                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  "Your workflow is ready!"                                              │
│                                                                          │
│  Summary:                                                                │
│  • 3 document types configured                                          │
│  • Validation rules set up                                              │
│  • Excel report format defined                                          │
│                                                                          │
│  "You can update these anytime from the Settings menu."                 │
│                                                                          │
│  ┌─────────────────────────────┐                                        │
│  │     Go to Dashboard →       │                                        │
│  └─────────────────────────────┘                                        │
│                                                                          │
│  [Behind the scenes:]                                                   │
│  1. Generate final SKILL.md                                             │
│  2. Upload to Claude Skills API → get skill_id                          │
│  3. Save skill_content + skill_id to Supabase                          │
│  4. Set onboarding_completed_at = now()                                 │
│  5. Destroy sandbox                                                     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Sandbox Lifecycle (Onboarding)

```typescript
/**
 * Onboarding sandbox stays alive for entire session.
 * One cold start at the beginning, then snappy interactions throughout.
 */
async function startOnboardingSession(orgId: string) {
  // 1. Create sandbox (5-10s cold start - show animation)
  const sandbox = await Sandbox.create({
    runtime: 'python3.13',
    timeout: 1800000,  // 30 minutes initial
  });

  // 2. Store sandbox ID in session for reconnection
  await saveSessionState(orgId, { sandboxId: sandbox.sandboxId });

  // 3. Set up sandbox with analysis tools
  await sandbox.runCommand('pip', ['install', 'pdfplumber', 'openpyxl']);

  return sandbox;
}

/**
 * Extend timeout if session is still active.
 */
async function keepAlive(sandbox: Sandbox) {
  const remaining = sandbox.timeout;
  if (remaining < 300000) {  // Less than 5 min left
    await sandbox.extendTimeout(900000);  // Add 15 min
  }
}

/**
 * Complete onboarding - save everything, destroy sandbox.
 */
async function completeOnboarding(
  orgId: string,
  sandbox: Sandbox,
  skillContent: string
) {
  // 1. Upload skill to Claude API
  const skillId = await uploadSkillToClaude(skillContent);

  // 2. Save to Supabase
  await supabase.from('org_configs').upsert({
    org_id: orgId,
    skill_content: skillContent,
    skill_id: skillId,
    onboarding_completed_at: new Date().toISOString(),
    onboarding_progress: null,  // Clear partial progress
  });

  // 3. Destroy sandbox
  await sandbox.stop();
}
```

### Partial Progress & Resume

```typescript
/**
 * Auto-save progress after each step.
 * Enables "Continue where you left off" on next login.
 */
async function saveProgress(orgId: string, progress: OnboardingProgress) {
  await supabase.from('org_configs').upsert({
    org_id: orgId,
    onboarding_progress: {
      current_step: progress.step,
      industry: progress.industry,
      document_types: progress.documentTypes,
      field_schemas: progress.fieldSchemas,
      output_format: progress.outputFormat,
      sandbox_id: progress.sandboxId,
      updated_at: new Date().toISOString(),
    },
  });
}

/**
 * Check if org has partial progress on app load.
 */
async function checkOnboardingStatus(orgId: string): Promise<OnboardingStatus> {
  const { data } = await supabase
    .from('org_configs')
    .select('onboarding_completed_at, onboarding_progress')
    .eq('org_id', orgId)
    .single();

  if (data?.onboarding_completed_at) {
    return { status: 'completed' };
  }

  if (data?.onboarding_progress) {
    return {
      status: 'in_progress',
      progress: data.onboarding_progress,
    };
  }

  return { status: 'not_started' };
}
```

---

## Maintenance Chatbot

### Purpose

Handle ongoing config updates. Lives in sidebar, accessible anytime after onboarding.

### Capabilities

| Action | Sandbox Needed? | Example |
|--------|-----------------|---------|
| View config | No | "What document types do I have?" |
| Simple field changes | No | "Change GST rate to 9%" |
| Add validation rule | No | "Flag invoices over $10,000" |
| Add document type | Yes | "We now process police reports" |
| Test changes | Yes | "Let me upload a doc to test" |
| Regenerate skill | Yes | "Rebuild with my pending preferences" |
| Undo last change | No | "Undo the last change" |

### Conversation Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Maintenance Chat (Sidebar)                                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  AI: "How can I help with your workflow?"                               │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  SIMPLE CHANGE (No sandbox):                                            │
│                                                                          │
│  User: "Change the GST rate from 8% to 9%"                              │
│  AI: "Updated. GST validation now uses 9%."                             │
│      [Regenerates skill in background, uploads to Claude API]           │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  COMPLEX CHANGE (Sandbox spins up):                                     │
│                                                                          │
│  User: "Add police reports as a new document type"                      │
│  AI: "I'll need to see a sample. Upload one?"                           │
│                                                                          │
│  [User uploads] → [Sandbox spins up] → [Analysis]                       │
│                                                                          │
│  AI: "Found these fields: report_number, date, officer, description.    │
│       Look right?"                                                      │
│  User: "Add incident_type too"                                          │
│  AI: "Added. Want to test with another document?"                       │
│  User: "No, that's fine"                                                │
│  AI: "Done. Police reports are now configured."                         │
│      [Updates skill, destroys sandbox]                                  │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  PREFERENCE INCORPORATION:                                              │
│                                                                          │
│  AI: "I noticed you have 3 pending preferences from recent work.        │
│       Want me to incorporate them into your workflow?"                  │
│                                                                          │
│  - "Ignore shipping lines for Acme Corp"                                │
│  - "Flag any invoice from Vendor X over $5000"                          │
│  - "Medical bills from SGH always have bundled GST"                     │
│                                                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐                   │
│  │  Add all    │ │ Review each │ │  Skip for now   │                   │
│  └─────────────┘ └─────────────┘ └─────────────────┘                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Skill Regeneration

```typescript
/**
 * Regenerate skill after config changes.
 * Updates both Supabase and Claude API.
 */
async function regenerateSkill(orgId: string, newContent: string) {
  // 1. Get existing config
  const { data: config } = await supabase
    .from('org_configs')
    .select('skill_id')
    .eq('org_id', orgId)
    .single();

  // 2. Create new version (if skill exists) or new skill
  let skillId: string;
  if (config?.skill_id) {
    // Update existing skill with new version
    await createSkillVersion(config.skill_id, newContent);
    skillId = config.skill_id;
  } else {
    // Create new skill
    skillId = await createNewSkill(newContent);
  }

  // 3. Update Supabase
  await supabase.from('org_configs').update({
    skill_content: newContent,
    skill_id: skillId,
    updated_at: new Date().toISOString(),
  }).eq('org_id', orgId);

  // 4. Mark incorporated preferences
  await supabase.from('org_preferences').update({
    incorporated_at: new Date().toISOString(),
  }).eq('org_id', orgId).is('incorporated_at', null);
}
```

---

## Analyst Chatbot

### Purpose

Analyze documents within a specific case. Loads the org's skill to understand their workflow.

### Integration with Org Config

```typescript
/**
 * Initialize Analyst with org's skill loaded.
 */
async function initAnalyst(caseId: string, orgId: string) {
  // 1. Get org config
  const config = await getOrgConfig(orgId);

  // 2. Get case data
  const caseData = await getCaseData(caseId);

  // 3. Build system prompt with skill
  const systemPrompt = buildAnalystPrompt(config.skillContent, caseData);

  // 4. Initialize chat with skill context
  return {
    systemPrompt,
    skillId: config.skillId,  // For Claude API calls
    tools: [
      { type: 'code_execution' },
      // Other tools...
    ],
  };
}
```

### Self-Improvement Loop

When Analyst detects a user preference that should persist:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Analyst Chat (Inside Case)                                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User: "For Acme Corp, always ignore the tax line - they bundle wrong"  │
│                                                                          │
│  AI: [Applies correction to current analysis]                           │
│      [Calls propose_rule tool]                                          │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ 💡 Remember this for future analyses?                            │   │
│  │                                                                   │   │
│  │ "For Acme Corp invoices, ignore tax line items"                  │   │
│  │                                                                   │   │
│  │ ┌─────────┐  ┌─────────┐                                        │   │
│  │ │   Yes   │  │   No    │                                        │   │
│  │ └─────────┘  └─────────┘                                        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  [User clicks Yes]                                                      │
│  → Saves to org_preferences table                                       │
│  → Batched into skill on next Maintenance interaction                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Tool Definition

```typescript
/**
 * Tool for Analyst to propose saving a preference.
 */
export const PROPOSE_RULE_TOOL = {
  name: "propose_rule",
  description: `Propose saving a user correction as a persistent preference.
Call when user provides a preference that should apply to ALL future analyses.
Do NOT call for one-off adjustments.`,
  parameters: {
    type: "object",
    properties: {
      rule: {
        type: "string",
        description: "The preference in plain English (e.g., 'For Acme Corp invoices, ignore tax line items')",
      },
    },
    required: ["rule"],
  },
};
```

---

## Self-Healing Rules System

> **Original Design:** `docs/new roadmap/2026-01-18-self-healing-corrections-design.md`

### The Core Idea

Like your Codex Agent file - a living document that accumulates "rules" over time and makes the AI work better. Each org builds up their own "organizational memory" through natural usage.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     SELF-HEALING LOOP                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User corrects Analyst ──▶ "Should I remember this?" ──▶ User clicks Yes│
│                                                                │         │
│                                                                ▼         │
│                                                         org_preferences  │
│                                                         (pending rules)  │
│                                                                │         │
│                                                                ▼         │
│  User opens Maintenance ──▶ "You have 3 pending rules" ──▶ Incorporate  │
│                                                                │         │
│                                                                ▼         │
│                                                         Skill updated    │
│                                                         (rules baked in) │
│                                                                │         │
│                                                                ▼         │
│  Next Analyst session ──▶ Skill loaded ──▶ Rules automatically applied  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### What Gets Captured

| Type | Example | How Detected |
|------|---------|--------------|
| **Vendor-specific rules** | "Acme Corp always bundles shipping into line 1" | User correction about specific vendor |
| **Validation overrides** | "Ignore GST mismatch for overseas invoices" | User dismisses a validation flag |
| **Field interpretations** | "When SGH says 'consultation', that's a medical expense" | User re-categorizes extracted data |
| **Output preferences** | "Always put the summary column first" | User feedback on generated reports |
| **Domain knowledge** | "In PI cases, lost wages include CPF" | User provides context during analysis |

### User Experience

**Step 1: Correction happens naturally in Analyst**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Analyst Chat                                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User: "The tax line for Acme is wrong - they always bundle it into     │
│         the shipping line, just ignore it"                              │
│                                                                          │
│  AI: "Got it - I'll ignore the tax line for this Acme invoice."         │
│                                                                          │
│      [AI detects this sounds like a GENERAL rule, not one-off]          │
│      [AI calls propose_rule tool]                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**Step 2: Simple confirmation (Yes/No only)**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │ 💡 Remember this for future analyses?                              │  │
│  │                                                                     │  │
│  │ "For Acme Corp invoices, ignore the tax line item                  │  │
│  │  (they bundle it into shipping)"                                   │  │
│  │                                                                     │  │
│  │ ┌─────────────┐  ┌─────────────┐                                  │  │
│  │ │     Yes     │  │     No      │                                  │  │
│  │ └─────────────┘  └─────────────┘                                  │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  [No text input, no complexity - just two buttons]                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**Step 3: Rules accumulate silently**

```
org_preferences table:
┌────────────────────────────────────────────────────────────────────────┐
│ preference_text                                    │ incorporated_at   │
├────────────────────────────────────────────────────┼───────────────────┤
│ "For Acme Corp invoices, ignore tax line items"   │ NULL (pending)    │
│ "SGH consultation fees are medical expenses"      │ NULL (pending)    │
│ "Ignore GST mismatch for overseas invoices"       │ NULL (pending)    │
│ "PI lost wages include CPF contributions"         │ 2026-01-15 (done) │
└────────────────────────────────────────────────────┴───────────────────┘
```

**Step 4: Batched incorporation via Maintenance**

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Maintenance Chat (Sidebar)                                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  AI: "You have 3 preferences from recent work that haven't been         │
│       added to your workflow yet:"                                      │
│                                                                          │
│       • For Acme Corp invoices, ignore tax line items                   │
│       • SGH consultation fees are medical expenses                      │
│       • Ignore GST mismatch for overseas invoices                       │
│                                                                          │
│       "Want me to add these to your workflow?"                          │
│                                                                          │
│  ┌─────────────┐ ┌─────────────────┐ ┌─────────────────┐               │
│  │   Add all   │ │  Review each    │ │  Skip for now   │               │
│  └─────────────┘ └─────────────────┘ └─────────────────┘               │
│                                                                          │
│  [If "Add all" or "Review each" → regenerate skill with rules]          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why Batched (Not Immediate)

| Approach | Pros | Cons |
|----------|------|------|
| **Immediate** | Rules apply instantly | Constant skill regeneration, API costs, potential bad rules slip through |
| **Batched** | Natural review moment, lower costs, user sees what's being added | Slight delay before rules take effect |

**Decision: Batched** - incorporates naturally when user next touches Maintenance. Creates a lightweight review moment without requiring manual rule management.

### Detection Heuristics

How does Analyst know when to propose a rule vs. treat it as one-off?

```typescript
/**
 * Heuristics for detecting persistent preferences.
 * Encoded in Analyst system prompt.
 */
const PROPOSE_RULE_HEURISTICS = `
## When to Propose Saving a Rule

PROPOSE a rule when user says:
- "Always..." or "Never..." (explicit permanence)
- "[Vendor X] always does..." (vendor-specific pattern)
- "For all [document type]..." (category-wide rule)
- "That's how we do it" / "That's our policy" (org practice)
- "Remember that..." / "Keep in mind..." (explicit memory request)

DO NOT propose when user says:
- "For now..." / "Just this once..." (explicit one-off)
- "Skip this one" / "Ignore that" (instance-specific)
- "Let me check" / "I'm not sure" (uncertainty)
- Correcting an obvious AI error (not a preference, just a fix)

When uncertain: DO NOT propose. Err on the side of not cluttering
the rules with one-off corrections.
`;
```

### Skill Integration

When rules are incorporated, they're woven into the SKILL.md:

**Before:**
```markdown
## Constraints

- Never hallucinate data not in source documents
- Ask user if confidence < 70%
```

**After:**
```markdown
## Constraints

- Never hallucinate data not in source documents
- Ask user if confidence < 70%

## Learned Preferences

These are org-specific rules learned from user feedback:

- For Acme Corp invoices, ignore the tax line item (they bundle it into shipping)
- SGH consultation fees should be categorized as medical expenses
- Ignore GST mismatch for overseas invoices (different tax jurisdictions)
- For PI cases, lost wages calculations include CPF contributions
```

### Viewing & Managing Rules

**Principle: No direct editing.** Users don't manage rules manually - they just confirm or skip when proposed.

But they should be able to **see** what the system has learned:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ Maintenance Chat                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User: "What rules have I set up?"                                      │
│                                                                          │
│  AI: "Here's what I've learned about your workflow:                     │
│                                                                          │
│       **Vendor Rules:**                                                 │
│       • Acme Corp - ignore tax line items                               │
│       • SGH - consultation fees are medical expenses                    │
│                                                                          │
│       **Validation Rules:**                                             │
│       • Ignore GST mismatch for overseas invoices                       │
│                                                                          │
│       **Domain Knowledge:**                                             │
│       • PI lost wages include CPF contributions                         │
│                                                                          │
│       Want to remove any of these?"                                     │
│                                                                          │
│  User: "Remove the Acme one, we fixed that with them"                   │
│                                                                          │
│  AI: "Done - removed the Acme Corp rule."                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Data Model (Rules-Specific)

```sql
-- Already defined in main schema, but highlighting here:
CREATE TABLE org_preferences (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id uuid NOT NULL REFERENCES organizations(id),

  preference_text text NOT NULL,         -- Plain English rule
  source_case_id uuid,                   -- Which case it came from
  incorporated_at timestamptz,           -- NULL = pending, timestamp = in skill

  created_at timestamptz NOT NULL DEFAULT now()
);

-- Useful queries:

-- Get pending rules for an org
SELECT * FROM org_preferences
WHERE org_id = $1 AND incorporated_at IS NULL
ORDER BY created_at;

-- Get all active rules (incorporated into skill)
SELECT * FROM org_preferences
WHERE org_id = $1 AND incorporated_at IS NOT NULL
ORDER BY incorporated_at DESC;

-- Mark rules as incorporated
UPDATE org_preferences
SET incorporated_at = now()
WHERE org_id = $1 AND incorporated_at IS NULL;
```

### The End State

Over time, each org accumulates a rich set of rules that make the AI increasingly effective:

```
Month 1:  3 rules  → AI works okay, needs frequent corrections
Month 3:  15 rules → AI handles most cases correctly
Month 6:  30 rules → AI feels like it "knows" the org
Month 12: 50 rules → AI is essentially a trained team member
```

**This is the moat.** The longer an org uses the platform, the better it gets for them specifically. Switching costs become high because they'd lose all this accumulated knowledge.

---

## Execution Architecture

### Two Different Execution Environments

**Critical architectural decision:** Onboarding/Maintenance use a different execution model than Analyst.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    EXECUTION ARCHITECTURE SPLIT                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ONBOARDING + MAINTENANCE CHATBOTS                                      │
│  ════════════════════════════════                                       │
│                                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────────┐ │
│  │   useChat   │───▶│  API Route  │───▶│     VERCEL SANDBOX          │ │
│  │  (AI SDK)   │    │ streamText  │    │   (Firecracker microVM)     │ │
│  └─────────────┘    └─────────────┘    │                             │ │
│                                         │  • Full Linux environment   │ │
│                                         │  • Install any packages     │ │
│                                         │  • Run Claude Code agent    │ │
│                                         │  • Filesystem as context    │ │
│                                         │  • Long-running sessions    │ │
│                                         └─────────────────────────────┘ │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  ANALYST CHATBOT (unchanged)                                            │
│  ═══════════════════════════                                            │
│                                                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────────┐ │
│  │   useChat   │───▶│  API Route  │───▶│   ANTHROPIC CONTAINER       │ │
│  │  (AI SDK)   │    │ streamText  │    │   (Code Execution)          │ │
│  └─────────────┘    └─────────────┘    │                             │ │
│                                         │  • Python sandbox           │ │
│                                         │  • Skills (xlsx, pdf, etc.) │ │
│                                         │  • Container persistence    │ │
│                                         │  • Built-in file gen        │ │
│                                         └─────────────────────────────┘ │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why Different Environments?

| Capability | Vercel Sandbox | Anthropic Container |
|------------|----------------|---------------------|
| **Full OS access** | ✅ Yes (Amazon Linux) | ❌ No (Python only) |
| **Install packages** | ✅ Any (dnf, pip, npm) | ⚠️ Limited |
| **Long sessions** | ✅ Up to 5 hours | ⚠️ Request-scoped |
| **File persistence** | ✅ Across calls in session | ✅ Within container |
| **Claude Code agent** | ✅ Can run inside | ❌ Not available |
| **Built-in skills** | ❌ Must implement | ✅ xlsx, pdf, docx |
| **Network access** | ✅ Configurable allowlist | ⚠️ Limited |
| **Cost** | Per-second billing | Per-token |

**Decision:**
- **Onboarding/Maintenance** need full power: analyze arbitrary docs, run scripts, potentially interact with ExtendAI, generate skills. → **Vercel Sandbox**
- **Analyst** needs focused execution: run Python on case data, generate Excel/PDF. → **Anthropic Container** (already works well)

---

## Onboarding/Maintenance: Vercel Sandbox Architecture

> **Implementation References:**
> - Sandbox SDK & patterns: `docs/architecture/final-sandbox-research.md`
> - AI SDK useChat/streamText: `docs/architecture/ai-sdk-patterns-cheatsheet.md`
> - External: [vibe-coding-platform](https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform)

### Reference: vibe-coding-platform Pattern

Based on [vercel/examples/apps/vibe-coding-platform](https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform) and patterns documented in `docs/architecture/final-sandbox-research.md`.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Frontend (React)                                                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  const { messages, sendMessage, status } = useChat({                    │
│    transport: new DefaultChatTransport({                                │
│      api: '/api/onboarding/chat',                                       │
│      body: () => ({ orgId, sandboxId }),                                │
│    }),                                                                   │
│  });                                                                     │
│                                                                          │
│  // Render message.parts including tool-bash, tool-analyze, etc.        │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  API Route: /api/onboarding/chat                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  export async function POST(req: Request) {                             │
│    const { messages, orgId, sandboxId } = await req.json();             │
│                                                                          │
│    // Get or create sandbox                                             │
│    const sandbox = sandboxId                                            │
│      ? await Sandbox.get({ sandboxId })                                 │
│      : await Sandbox.create({ runtime: 'python3.13', timeout: 1800000 });│
│                                                                          │
│    const result = streamText({                                          │
│      model: anthropic('claude-sonnet-4-5'),                             │
│      system: ONBOARDING_SYSTEM_PROMPT,                                  │
│      messages: await convertToModelMessages(messages),                  │
│      tools: {                                                            │
│        bash: bashTool(sandbox),                                         │
│        analyze_document: analyzeDocTool(sandbox),                       │
│        propose_config: proposeConfigTool(),                             │
│        test_extraction: testExtractionTool(sandbox),                    │
│      },                                                                  │
│    });                                                                   │
│                                                                          │
│    // Return stream + sandbox ID in headers                             │
│    return result.toUIMessageStreamResponse({                            │
│      headers: { 'X-Sandbox-Id': sandbox.sandboxId },                    │
│    });                                                                   │
│  }                                                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Vercel Sandbox (Firecracker microVM)                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  /vercel/sandbox/                                                       │
│  ├── uploads/                    # User-uploaded documents              │
│  │   ├── medical-bill-1.pdf                                             │
│  │   ├── invoice-sample.pdf                                             │
│  │   └── income-statement.xlsx                                          │
│  ├── analysis/                   # AI-generated analysis                │
│  │   ├── document-types.json                                            │
│  │   └── field-schemas.json                                             │
│  ├── skill/                      # Generated skill                      │
│  │   └── SKILL.md                                                       │
│  └── scripts/                    # Analysis scripts                     │
│      ├── extract_fields.py                                              │
│      └── validate_config.py                                             │
│                                                                          │
│  Agent can:                                                              │
│  • ls, cat, grep to explore                                             │
│  • pip install pdfplumber, openpyxl                                     │
│  • Run Python scripts for document analysis                             │
│  • Write files (skill, config, etc.)                                    │
│  • Call external APIs (ExtendAI, Supabase)                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Tool Definitions (Onboarding)

```typescript
import { tool } from 'ai';
import { z } from 'zod';
import { Sandbox } from '@vercel/sandbox';

/**
 * Bash tool - allows agent to run commands in sandbox.
 * Core tool for filesystem exploration and script execution.
 */
export function bashTool(sandbox: Sandbox) {
  return tool({
    description: `Execute bash commands in the sandbox.
Use for: exploring files (ls, cat, grep), running scripts (python, node),
installing packages (pip install, npm install), file manipulation.`,
    inputSchema: z.object({
      command: z.string().describe('Bash command to execute'),
    }),
    execute: async ({ command }) => {
      const result = await sandbox.runCommand('bash', ['-c', command]);
      const stdout = await result.stdout();
      const stderr = await result.stderr();
      return {
        exitCode: result.exitCode,
        stdout,
        stderr,
        output: stdout + (stderr ? `\nSTDERR: ${stderr}` : ''),
      };
    },
  });
}

/**
 * Document analysis tool - analyzes uploaded documents.
 * Writes results to sandbox filesystem for agent to explore.
 */
export function analyzeDocTool(sandbox: Sandbox) {
  return tool({
    description: `Analyze an uploaded document to identify its type and extract field patterns.
Returns structured analysis that can be used to build configuration.`,
    inputSchema: z.object({
      filename: z.string().describe('Name of file in uploads/ directory'),
    }),
    execute: async ({ filename }) => {
      // Write analysis script to sandbox
      await sandbox.writeFiles([{
        path: 'scripts/analyze.py',
        content: Buffer.from(ANALYZE_SCRIPT),
      }]);

      // Run analysis
      const result = await sandbox.runCommand('python', [
        'scripts/analyze.py',
        `uploads/${filename}`,
      ]);

      return {
        success: result.exitCode === 0,
        output: await result.stdout(),
        error: result.exitCode !== 0 ? await result.stderr() : null,
      };
    },
  });
}

/**
 * Propose config tool - presents extracted config for user approval.
 * Client-side tool that renders approval UI.
 */
export function proposeConfigTool() {
  return tool({
    description: `Propose a document type configuration for user review.
Call this when you've analyzed documents and want user to confirm the config.`,
    inputSchema: z.object({
      documentType: z.string().describe('Name of document type'),
      fields: z.array(z.object({
        name: z.string(),
        type: z.string(),
        description: z.string(),
      })).describe('Extracted fields'),
      validationRules: z.array(z.string()).optional(),
    }),
    // No execute - renders as UI component on client
  });
}

/**
 * Test extraction tool - tests config against a document.
 */
export function testExtractionTool(sandbox: Sandbox) {
  return tool({
    description: `Test the current configuration against a document.
Use to verify extraction works before completing onboarding.`,
    inputSchema: z.object({
      filename: z.string().describe('Document to test'),
      configPath: z.string().describe('Path to config file'),
    }),
    execute: async ({ filename, configPath }) => {
      const result = await sandbox.runCommand('python', [
        'scripts/test_extraction.py',
        `uploads/${filename}`,
        configPath,
      ]);

      return {
        success: result.exitCode === 0,
        results: await result.stdout(),
        errors: result.exitCode !== 0 ? await result.stderr() : null,
      };
    },
  });
}
```

### Sandbox Lifecycle Management

```typescript
/**
 * Onboarding session state - persisted to enable resume.
 */
interface OnboardingSession {
  orgId: string;
  sandboxId: string | null;
  status: 'active' | 'completed' | 'abandoned';
  progress: OnboardingProgress;
  createdAt: Date;
  lastActiveAt: Date;
}

/**
 * Start or resume onboarding session.
 */
async function getOrCreateOnboardingSession(orgId: string): Promise<{
  session: OnboardingSession;
  sandbox: Sandbox;
}> {
  // Check for existing session
  const existing = await getOnboardingSession(orgId);

  if (existing?.sandboxId && existing.status === 'active') {
    try {
      // Try to reconnect to existing sandbox
      const sandbox = await Sandbox.get({ sandboxId: existing.sandboxId });
      if (sandbox.status === 'running') {
        return { session: existing, sandbox };
      }
    } catch {
      // Sandbox expired, create new one
    }
  }

  // Create new sandbox
  const sandbox = await Sandbox.create({
    runtime: 'python3.13',
    timeout: 1800000,  // 30 minutes
    resources: { vcpus: 2 },
  });

  // Install common packages
  await sandbox.runCommand({
    cmd: 'pip',
    args: ['install', 'pdfplumber', 'openpyxl', 'python-docx'],
  });

  // Create directory structure
  await sandbox.mkDir('uploads');
  await sandbox.mkDir('analysis');
  await sandbox.mkDir('skill');
  await sandbox.mkDir('scripts');

  // Save session
  const session = await saveOnboardingSession({
    orgId,
    sandboxId: sandbox.sandboxId,
    status: 'active',
    progress: { step: 'welcome', documentTypes: [], fieldSchemas: {} },
    createdAt: new Date(),
    lastActiveAt: new Date(),
  });

  return { session, sandbox };
}

/**
 * Keep sandbox alive during active session.
 */
async function extendSandboxIfNeeded(sandbox: Sandbox) {
  if (sandbox.timeout < 300000) {  // Less than 5 min left
    await sandbox.extendTimeout(900000);  // Add 15 min
  }
}

/**
 * Complete onboarding - save config, destroy sandbox.
 */
async function completeOnboarding(
  orgId: string,
  sandbox: Sandbox,
) {
  // Read generated skill from sandbox
  const skillContent = await sandbox.readFileToBuffer({ path: 'skill/SKILL.md' });

  // Upload to Claude Skills API
  const skillId = await uploadSkillToClaude(skillContent.toString());

  // Save to Supabase
  await supabase.from('org_configs').upsert({
    org_id: orgId,
    skill_content: skillContent.toString(),
    skill_id: skillId,
    onboarding_completed_at: new Date().toISOString(),
    onboarding_progress: null,
  });

  // Destroy sandbox
  await sandbox.stop();

  // Update session
  await updateOnboardingSession(orgId, { status: 'completed', sandboxId: null });
}
```

### File Upload Handling

```typescript
/**
 * API route for uploading documents to onboarding sandbox.
 */
export async function POST(req: Request) {
  const formData = await req.formData();
  const file = formData.get('file') as File;
  const sandboxId = formData.get('sandboxId') as string;

  if (!file || !sandboxId) {
    return Response.json({ error: 'Missing file or sandboxId' }, { status: 400 });
  }

  // Get sandbox
  const sandbox = await Sandbox.get({ sandboxId });

  // Write file to sandbox
  const buffer = Buffer.from(await file.arrayBuffer());
  await sandbox.writeFiles([{
    path: `uploads/${file.name}`,
    content: buffer,
  }]);

  return Response.json({
    success: true,
    filename: file.name,
    path: `uploads/${file.name}`,
  });
}
```

---

## Analyst: Anthropic Container Architecture (Unchanged)

> **Implementation References:**
> - Anthropic code execution: `docs/architecture/ai-sdk-patterns-cheatsheet.md` (Section 3)
> - Skills API: `docs/architecture/Final-Claude Skills SDK.md`

The Analyst chatbot keeps its current architecture using Anthropic's built-in code execution.

### Why Keep It?

1. **Already works well** - No need to change what's working
2. **Built-in skills** - xlsx, pdf, docx generation out of the box
3. **Container persistence** - Files persist across turns with `prepareStep`
4. **Lower complexity** - No sandbox management needed
5. **Cost efficient** - Per-token, not per-second

### Architecture

```typescript
// api/analyst/chat/route.ts
import { streamText, convertToModelMessages, stepCountIs } from 'ai';
import {
  anthropic,
  forwardAnthropicContainerIdFromLastStep,
} from '@ai-sdk/anthropic';

export async function POST(req: Request) {
  const { messages, caseId, containerId } = await req.json();

  // Load org config for skill
  const orgConfig = await getOrgConfig(caseId);

  const result = streamText({
    model: anthropic('claude-sonnet-4-5'),
    system: buildAnalystPrompt(orgConfig.skillContent),
    messages: await convertToModelMessages(messages),
    stopWhen: stepCountIs(10),
    tools: {
      code_execution: anthropic.tools.codeExecution_20250825(),
      propose_rule: proposeRuleTool(),  // For self-healing
    },
    providerOptions: {
      anthropic: {
        container: containerId ? { id: containerId } : {
          skills: [
            { type: 'anthropic', skillId: 'xlsx', version: 'latest' },
            { type: 'anthropic', skillId: 'pdf', version: 'latest' },
            { type: 'custom', skillId: orgConfig.skillId, version: 'latest' },
          ],
        },
      },
    },
    prepareStep: forwardAnthropicContainerIdFromLastStep,
  });

  return result.toUIMessageStreamResponse();
}
```

---

## Sandbox Lifecycle Summary

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     SANDBOX LIFECYCLE BY CHATBOT                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ONBOARDING (Vercel Sandbox - Always On):                               │
│                                                                          │
│  User starts ──▶ Sandbox created ──▶ Multiple chat turns ──▶ Completed  │
│  onboarding      (one cold start)    (same sandbox, extend              │
│                   ~5-10 seconds)      timeout as needed)      │         │
│                                                                ▼         │
│                                                          Save to Supabase│
│                                                          Upload skill    │
│                                                          Destroy sandbox │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  MAINTENANCE (Vercel Sandbox - On Demand):                              │
│                                                                          │
│  Simple change ──▶ No sandbox ──▶ Update config via chat API            │
│                                                                          │
│  Complex change ──▶ Sandbox created ──▶ Test/Analysis ──▶ Destroy       │
│  ("test my config")   (on-demand)                                       │
│                                                                          │
│  ─────────────────────────────────────────────────────────────────────  │
│                                                                          │
│  ANALYST (Anthropic Container - Request Scoped):                        │
│                                                                          │
│  Chat turn ──▶ Container auto-created ──▶ Code execution ──▶ Response   │
│                (by Anthropic)              Files persist     │           │
│                                            across turns      │           │
│                                            via prepareStep   │           │
│                                                              ▼           │
│                                                   Container managed     │
│                                                   by Anthropic          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Error Handling

### Onboarding Errors

| Scenario | Handling |
|----------|----------|
| Unsupported file type | "I can't process .xyz files. Try PDF, images, or Excel." |
| Can't identify document | "I'm not sure what this document is. Can you describe it?" |
| Sandbox timeout | Save progress, offer "Resume where you left off" |
| Test run fails | "Something went wrong. Let's adjust..." (stay in loop) |
| User abandons | Save partial progress, show "Continue setup" on next login |
| Skill upload fails | Retry with exponential backoff, alert if persistent |

### Maintenance Errors

| Scenario | Handling |
|----------|----------|
| Invalid change request | "I don't understand. Can you rephrase?" |
| Sandbox fails to start | "Having trouble testing. Try again in a moment." |
| Skill regeneration fails | Keep old skill active, notify user |
| Concurrent edits | Last-write-wins with conflict notification |

### Recovery Patterns

```typescript
/**
 * Wrap sandbox operations with automatic recovery.
 */
async function withSandboxRecovery<T>(
  orgId: string,
  operation: (sandbox: Sandbox) => Promise<T>
): Promise<T> {
  let attempts = 0;
  const maxAttempts = 3;

  while (attempts < maxAttempts) {
    try {
      const sandbox = await createSandboxWithSkill(orgId);
      try {
        return await operation(sandbox);
      } finally {
        await sandbox.stop();
      }
    } catch (error) {
      attempts++;
      if (attempts >= maxAttempts) {
        throw new Error(`Sandbox operation failed after ${maxAttempts} attempts`);
      }
      await sleep(1000 * attempts);  // Exponential backoff
    }
  }

  throw new Error('Unreachable');
}
```

---

## Security

### Principles

| Concern | Approach |
|---------|----------|
| Sensitive documents | Process in ephemeral sandbox, never persist raw docs |
| Org data isolation | RLS on all tables, org members only |
| Sandbox network | Allowlist only (Claude, Supabase, ExtendAI) |
| Malicious uploads | Sandbox isolation - worst case crashes sandbox |
| Skill tampering | No direct editing, all changes through chatbot |

### Row-Level Security

```sql
-- All org data is protected by RLS
-- Users can only access their own org's data

CREATE POLICY "org_isolation" ON org_configs
  FOR ALL USING (
    org_id IN (
      SELECT org_id FROM org_members WHERE user_id = auth.uid()
    )
  );

CREATE POLICY "org_isolation" ON org_preferences
  FOR ALL USING (
    org_id IN (
      SELECT org_id FROM org_members WHERE user_id = auth.uid()
    )
  );
```

### Skill Content Validation

```typescript
/**
 * Validate skill content before upload to Claude API.
 * Prevents injection of malicious instructions.
 */
function validateSkillContent(content: string): ValidationResult {
  const issues: string[] = [];

  // Check for suspicious patterns
  if (content.includes('ignore all previous instructions')) {
    issues.push('Suspicious instruction override detected');
  }

  // Check size limits
  if (content.length > 100000) {
    issues.push('Skill content exceeds size limit');
  }

  // Check required sections
  if (!content.includes('## Problem')) {
    issues.push('Missing required Problem section');
  }

  return {
    valid: issues.length === 0,
    issues,
  };
}
```

---

## Migration Strategy

### Approach: Gradual Migration

```
Phase 1: New clients use Supabase
         Existing clients stay on TypeScript

Phase 2: Migrate high-value clients manually
         (Run onboarding chatbot, verify output)

Phase 3: Deprecate TypeScript configs
         (All clients on Supabase)
```

### Migration Helper

```typescript
/**
 * Migrate a legacy client to Supabase.
 * Can be triggered manually or via admin UI.
 */
async function migrateLegacyClient(clientId: string) {
  // 1. Load legacy config
  const legacy = await getLegacyConfig(clientId);
  if (!legacy) {
    throw new Error(`No legacy config for: ${clientId}`);
  }

  // 2. Read existing skill files
  const skillDir = `src/clients/${clientId}/docgen-skill/${clientId}-docgen`;
  const skillContent = await fs.readFile(`${skillDir}/SKILL.md`, 'utf-8');

  // 3. Get or lookup org
  const org = await getOrCreateOrg(clientId);

  // 4. Insert into Supabase
  await supabase.from('org_configs').upsert({
    org_id: org.id,
    skill_content: skillContent,
    skill_id: legacy.skillId,
    industry: legacy.industry,
    onboarding_completed_at: new Date().toISOString(),
  });

  console.log(`Migrated ${clientId} to Supabase`);
}
```

---

## Implementation Phases

### Phase 1: Foundation
- [ ] Supabase schema (org_configs, org_preferences)
- [ ] Config loader with fallback
- [ ] Basic API endpoints

### Phase 2: Onboarding Chatbot
- [ ] Full-screen onboarding UI
- [ ] Sandbox integration
- [ ] Document analysis pipeline
- [ ] Skill generation
- [ ] Progress persistence

### Phase 3: Maintenance Chatbot
- [ ] Sidebar UI
- [ ] Simple change handling
- [ ] On-demand sandbox for complex changes
- [ ] Preference incorporation

### Phase 4: Analyst Integration
- [ ] Load org skill into Analyst
- [ ] propose_rule tool
- [ ] Preference capture flow

### Phase 5: Migration & Polish
- [ ] Migration tooling
- [ ] Error handling refinement
- [ ] Monitoring & observability

---

## Unresolved Questions

1. **Skill versioning UI** - Should users be able to see/rollback to previous skill versions? (Leaning: no, keep simple)

2. **Multi-user editing** - What happens if two users from same org edit config simultaneously? (Leaning: last-write-wins with notification)

3. **Sandbox cost monitoring** - How do we track/limit sandbox usage per org? (Needs investigation)

4. **Skill size limits** - What's the max skill size Claude API accepts? (Needs testing)

5. **Offline/degraded mode** - What if Claude API is down during onboarding? (Leaning: show error, retry later)

---

## Success Criteria

- [ ] New org can complete onboarding without developer involvement
- [ ] No code deployment required for new client configs
- [ ] Analyst correctly uses org-specific skill
- [ ] Preferences captured and incorporated into skill
- [ ] Existing clients continue working during migration
- [ ] Average onboarding time < 30 minutes
- [ ] User satisfaction with self-serve experience

---

## References & Inspiration

### Twin.so - Conversational Agent Builder

**URL:** https://twin.so/

**Screenshot:** [self-onboarding.png](assets/self-onboarding.png)

**What's interesting:**
- Conversational onboarding flow that progressively gathers user context through natural Q&A
- Uses clickable button options alongside free-text input (e.g., "Email (Gmail/Outlook)", "LinkedIn messages", "Both email and LinkedIn")
- Sequential, focused questions: lead sources → CRM → outreach methods
- Each answer informs the next question contextually ("Got it—LinkedIn leads into Notion. Now for the outreach side.")
- "My Agents" sidebar suggests users can create multiple workflow agents
- Minimal chrome, conversation-first UI

**Relevance to Sunder:** This pattern could inform how we design the onboarding chatbot - conversational discovery with clickable options reduces friction and guides users through complex configuration without overwhelming them.

---

*Document generated through collaborative brainstorming session, 2026-01-21*

