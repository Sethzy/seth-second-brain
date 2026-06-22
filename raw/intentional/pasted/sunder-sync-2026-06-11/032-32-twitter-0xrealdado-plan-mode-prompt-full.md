---
type: raw_capture
source_type: x
title: "Sunder sync: 32-twitter-0xrealdado-plan-mode-prompt-FULL.md"
url: "https://x.com/0xrealdado/status/2020205261760123056"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/32-twitter-0xrealdado-plan-mode-prompt-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/32-twitter-0xrealdado-plan-mode-prompt-FULL.md"
sha256: "3411d5678ead6130f8343f31b5c85e2191c02f9cfbbf97256ae82f679fb79cc7"
duplicate_of: ""
---

# Sunder sync: 32-twitter-0xrealdado-plan-mode-prompt-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/32-twitter-0xrealdado-plan-mode-prompt-FULL.md`

Primary URL: https://x.com/0xrealdado/status/2020205261760123056

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter - @0xrealdado: Claude Code Plan Mode Prompt Template

**URL:** https://x.com/0xrealdado/status/2020205261760123056
**Author:** Dado (@0xrealdado) - Verified
**Platform:** Twitter/X
**Posted:** 2:37 AM · Feb 8, 2026
**Engagement:** 0 replies, 5 reposts, 97 likes, 210 bookmarks, 5,247 views

## Tweet Summary

Complete markdown prompt template for Claude Code plan mode reviews. Comprehensive framework covering architecture, code quality, testing, and performance with explicit engineering preferences (DRY, well-tested, "engineered enough", edge case handling, explicit over clever).

## Main Tweet Text

"Here it is in markdown format, just copy and paste it:

# Claude Code Prompt for Plan Mode

#prompts

Review this plan thoroughly before making any code changes. For every issue or recommendation, explain the concrete tradeoffs, give me an opinionated recommendation, and ask for my input before assuming a direction.

My engineering preferences (use these to guide your recommendations):
- DRY is important—flag repetition aggressively.
- Well-tested code is non-negotiable; I'd rather have too many tests than too few.
- I want code that's \"engineered enough\" — not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity).
- I err on the side of handling more edge cases, not fewer; thoughtfulness > speed.
- Bias toward explicit over clever.

## 1. Architecture review

Evaluate:
- Overall system design and component boundaries.
- Dependency graph and coupling concerns.
- Data flow patterns and potential bottlenecks.
- Scaling characteristics and single points of failure.
- Security architecture (auth, data access, API boundaries).

## 2. Code quality review

Evaluate:
- Code organization and module structure.
- DRY violations—be aggressive here.
- Error handling patterns and missing edge cases (call these out explicitly).
- Technical debt hotspots.
- Areas that are over-engineered or under-engineered relative to my preferences.

## 3. Test review

Evaluate:
- Test coverage gaps (unit, integration, e2e).
- Test quality and assertion strength.
- Missing edge case coverage—be thorough.
- Untested failure modes and error paths.

## 4. Performance review

Evaluate:
- N+1 queries and database access patterns.
- Memory-usage concerns.
- Caching opportunities.
- Slow or high-complexity code paths.

**For each issue you find**

For every specific issue (bug, smell, design concern, or risk):
- Describe the problem concretely, with file and line references.
- Present 2–3 options, including \"do nothing\" where that's reasonable.
- For each option, specify: implementation effort, risk, impact on other code, and maintenance burden.
- Give me your recommended option and why, mapped to my preferences above.
- Then explicitly ask whether I agree or want to choose a different direction before proceeding.

**Workflow and interaction**

- Do not assume my priorities on timeline or scale.
- After each section, pause and ask for my feedback before moving on.

---

BEFORE YOU START: Ask if I want one of two options:

1/ BIG CHANGE: Work through this interactively, one section at a time (Architecture → Code Quality → Tests → Performance) with at most 4 top issues in each section.

2/ SMALL CHANGE: Work through interactively ONE question per review section

FOR EACH STAGE OF REVIEW: output the explanation and pros and cons of each stage's questions AND your opinionated recommendation and why, and then use AskUserQuestion.

Also NUMBER issues and then give LETTERS for options and when using AskUserQuestion make sure each option clearly labels the issue NUMBER and option LETTER so the user doesn't get confused.

Make the recommended option always the 1st option."

## Full Prompt Template (Formatted)

### Engineering Preferences

1. **DRY (Don't Repeat Yourself)**
   - Importance: High
   - Instruction: Flag repetition aggressively

2. **Testing**
   - Philosophy: Well-tested code is non-negotiable
   - Bias: Rather have too many tests than too few

3. **Engineering Balance**
   - Target: "Engineered enough"
   - Avoid: Under-engineered (fragile, hacky)
   - Avoid: Over-engineered (premature abstraction, unnecessary complexity)

4. **Edge Cases**
   - Philosophy: Handle more, not fewer
   - Priority: Thoughtfulness > speed

5. **Code Style**
   - Principle: Explicit over clever

### Review Framework: 4 Sections

#### Section 1: Architecture Review

**Evaluate:**
- Overall system design and component boundaries
- Dependency graph and coupling concerns
- Data flow patterns and potential bottlenecks
- Scaling characteristics and single points of failure
- Security architecture (auth, data access, API boundaries)

#### Section 2: Code Quality Review

**Evaluate:**
- Code organization and module structure
- DRY violations (be aggressive)
- Error handling patterns and missing edge cases (explicit callouts)
- Technical debt hotspots
- Over/under-engineered areas (relative to preferences)

#### Section 3: Test Review

**Evaluate:**
- Test coverage gaps (unit, integration, e2e)
- Test quality and assertion strength
- Missing edge case coverage (be thorough)
- Untested failure modes and error paths

#### Section 4: Performance Review

**Evaluate:**
- N+1 queries and database access patterns
- Memory-usage concerns
- Caching opportunities
- Slow or high-complexity code paths

### Issue Reporting Format

For every specific issue (bug, smell, design concern, risk):

1. **Describe problem concretely**
   - Include file and line references

2. **Present 2-3 options**
   - Include "do nothing" where reasonable

3. **For each option, specify:**
   - Implementation effort
   - Risk
   - Impact on other code
   - Maintenance burden

4. **Give recommended option**
   - Map to engineering preferences above
   - Explain why

5. **Ask for confirmation**
   - Explicitly ask if user agrees
   - Don't proceed without confirmation

### Workflow Rules

**Constraints:**
- Do not assume priorities on timeline or scale
- After each section, pause for feedback before moving on

**Initial choice:**
- Ask user: BIG CHANGE or SMALL CHANGE?

**BIG CHANGE:**
- Work through interactively, one section at a time
- Order: Architecture → Code Quality → Tests → Performance
- Max 4 top issues per section

**SMALL CHANGE:**
- Work through interactively
- ONE question per review section

**For each stage:**
1. Output explanation
2. Output pros/cons of each stage's questions
3. Output opinionated recommendation and why
4. Use AskUserQuestion tool

**Labeling convention:**
- NUMBER issues (Issue #1, Issue #2, etc.)
- LETTER options (Option A, Option B, Option C)
- AskUserQuestion must clearly label issue NUMBER and option LETTER
- Recommended option always listed first

## Key Insights

### 1. Engineering Philosophy Codification
**Value:** Explicit engineering preferences guide all recommendations
**Impact:** Consistent code review aligned with personal values

**Core values:**
- DRY (aggressive repetition flagging)
- Testing (non-negotiable, more is better)
- Balance (not too fragile, not too complex)
- Edge cases (thoughtful > fast)
- Clarity (explicit > clever)

### 2. Structured Review Process
**4 sections:** Architecture → Code Quality → Tests → Performance
**Why sequential:** Each builds on previous understanding

### 3. Decision-Making Framework
**For every issue:**
- Concrete description + file references
- 2-3 options (including "do nothing")
- Trade-off analysis (effort, risk, impact, maintenance)
- Opinionated recommendation mapped to preferences
- Explicit approval required

**Why this works:** Balances AI expertise with human judgment

### 4. Scalable Approach
**BIG CHANGE:** 4 issues per section (16 total max)
**SMALL CHANGE:** 1 question per section (4 total)

**Adaptability:** Same framework scales to project size

### 5. Interactive Workflow
**Pattern:** Output → Recommend → Ask → Wait for approval
**Tool:** AskUserQuestion (explicit in prompt)
**Benefit:** Human-in-loop throughout

### 6. Labeling Convention
**Issues:** Numbered (#1, #2, #3)
**Options:** Lettered (A, B, C)
**In AskUserQuestion:** "Issue #2, Option B"

**Why:** Prevents confusion in multi-issue reviews

### 7. Recommended Option First
**Rule:** Make recommended option always 1st
**Psychology:** Reduces cognitive load, establishes default

## Use Cases

### For Individual Developers
- Code review before PR
- Refactoring planning
- Technical debt assessment

### For Teams
- Standardize code review practices
- Align on engineering preferences
- Onboard new team members to coding standards

### For AI Pair Programming
- Guide Claude Code plan mode
- Ensure consistent review quality
- Balance AI suggestions with human values

## Comparison to Default Claude Code Behavior

| Aspect | Default Behavior | With This Prompt |
|--------|------------------|------------------|
| **DRY focus** | General | Aggressive flagging |
| **Testing** | Balanced | More tests preferred |
| **Edge cases** | Pragmatic | Thorough (thoughtfulness > speed) |
| **Code style** | Varies | Explicit over clever |
| **Issue format** | Narrative | Structured (2-3 options + trade-offs) |
| **Workflow** | Continuous | Pause after each section |
| **Recommendations** | Neutral | Opinionated (mapped to preferences) |

## Engineering Preferences Breakdown

### 1. DRY (Don't Repeat Yourself)
**Quote:** "DRY is important—flag repetition aggressively."
**Intensity:** High (aggressive)
**Application:** Code quality review section

### 2. Testing
**Quote:** "Well-tested code is non-negotiable; I'd rather have too many tests than too few."
**Philosophy:** More tests > fewer tests
**Entire section:** Test review (Section 3)

### 3. "Engineered Enough"
**Quote:** "I want code that's 'engineered enough' — not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity)."

**Avoid:**
- Under-engineered: fragile, hacky
- Over-engineered: premature abstraction, unnecessary complexity

**Target:** Goldilocks zone

### 4. Edge Cases
**Quote:** "I err on the side of handling more edge cases, not fewer; thoughtfulness > speed."
**Bias:** More coverage
**Priority:** Thoughtfulness over speed

### 5. Explicit Over Clever
**Quote:** "Bias toward explicit over clever."
**Style:** Clear, readable code > concise "clever" code

## Category

Claude Code, Plan Mode, Prompts, Code Review, Engineering Preferences, DRY, Testing, Architecture, Prompt Templates

## Related

- **Author:** Dado (@0xrealdado) - Verified
- **Subject:** Claude Code plan mode prompt template
- **Format:** Copy-paste markdown prompt
- **Hashtag:** #prompts
- **Engagement:** 97 likes, 210 bookmarks (high bookmark:like ratio = utility)
- **Date:** February 8, 2026
- **Framework:** 4-section review (Architecture, Code Quality, Tests, Performance)
- **Philosophy:** DRY, well-tested, "engineered enough", edge cases, explicit over clever
- **Workflow:** Interactive with AskUserQuestion tool
- **Labeling:** Numbered issues + lettered options
- **Use case:** Code review, refactoring, technical debt assessment

