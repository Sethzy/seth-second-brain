---
type: raw_capture
source_type: web
title: "TheCraigHewitt seomachine repository snapshot"
url: "https://github.com/TheCraigHewitt/seomachine"
collected_at: 2026-06-18T17:03:39Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# TheCraigHewitt seomachine repository snapshot

Source: https://github.com/TheCraigHewitt/seomachine

## Capture Text

# Repository Snapshot

Repository: https://github.com/TheCraigHewitt/seomachine
Captured commit: 70231da177abe92ec26375c051561ff9acd8423a
Commit date: 2026-04-10T13:41:07-04:00
Commit subject: fix: expand AI watermark removal with more unicode chars and AI-telltale phrases (#36)
Snapshot note: This is an immutable evidence snapshot of repository metadata, file tree, and selected docs/excerpts at the captured commit. It is not a full Git mirror. Use the commit hash and upstream URL for full repository reconstruction.

## File Tree
```text
.claude/agents/cluster-strategist.md
.claude/agents/content-analyzer.md
.claude/agents/cro-analyst.md
.claude/agents/editor.md
.claude/agents/headline-generator.md
.claude/agents/internal-linker.md
.claude/agents/keyword-mapper.md
.claude/agents/landing-page-optimizer.md
.claude/agents/meta-creator.md
.claude/agents/performance.md
.claude/agents/seo-optimizer.md
.claude/commands/analyze-existing.md
.claude/commands/article.md
.claude/commands/cluster.md
.claude/commands/content-calendar.md
.claude/commands/landing-audit.md
.claude/commands/landing-competitor.md
.claude/commands/landing-publish.md
.claude/commands/landing-research.md
.claude/commands/landing-write.md
.claude/commands/optimize.md
.claude/commands/performance-review.md
.claude/commands/priorities.md
.claude/commands/publish-draft.md
.claude/commands/repurpose.md
.claude/commands/research-ai-citations.md
.claude/commands/research-gaps.md
.claude/commands/research-performance.md
.claude/commands/research-serp.md
.claude/commands/research-topics.md
.claude/commands/research-trending.md
.claude/commands/research.md
.claude/commands/rewrite.md
.claude/commands/scrub.md
.claude/commands/write.md
.claude/skills/ab-test-setup/SKILL.md
.claude/skills/ab-test-setup/references/sample-size-guide.md
.claude/skills/ab-test-setup/references/test-templates.md
.claude/skills/analytics-tracking/SKILL.md
.claude/skills/analytics-tracking/references/event-library.md
.claude/skills/analytics-tracking/references/ga4-implementation.md
.claude/skills/analytics-tracking/references/gtm-implementation.md
.claude/skills/competitor-alternatives/SKILL.md
.claude/skills/competitor-alternatives/references/content-architecture.md
.claude/skills/competitor-alternatives/references/templates.md
.claude/skills/content-strategy/SKILL.md
.claude/skills/copy-editing/SKILL.md
.claude/skills/copy-editing/references/plain-english-alternatives.md
.claude/skills/copywriting/SKILL.md
.claude/skills/copywriting/references/copy-frameworks.md
.claude/skills/copywriting/references/natural-transitions.md
.claude/skills/email-sequence/SKILL.md
.claude/skills/email-sequence/references/copy-guidelines.md
.claude/skills/email-sequence/references/email-types.md
.claude/skills/email-sequence/references/sequence-templates.md
.claude/skills/form-cro/SKILL.md
.claude/skills/free-tool-strategy/SKILL.md
.claude/skills/free-tool-strategy/references/tool-types.md
.claude/skills/growth-lead-SKILL.md
.claude/skills/launch-strategy/SKILL.md
.claude/skills/marketing-ideas/SKILL.md
.claude/skills/marketing-ideas/references/ideas-by-category.md
.claude/skills/marketing-psychology/SKILL.md
.claude/skills/onboarding-cro/SKILL.md
.claude/skills/onboarding-cro/references/experiments.md
.claude/skills/page-cro/SKILL.md
.claude/skills/page-cro/references/experiments.md
.claude/skills/paid-ads/SKILL.md
.claude/skills/paid-ads/references/ad-copy-templates.md
.claude/skills/paid-ads/references/audience-targeting.md
.claude/skills/paid-ads/references/platform-setup-checklists.md
.claude/skills/paywall-upgrade-cro/SKILL.md
.claude/skills/paywall-upgrade-cro/references/experiments.md
.claude/skills/popup-cro/SKILL.md
.claude/skills/pricing-strategy/SKILL.md
.claude/skills/pricing-strategy/references/research-methods.md
.claude/skills/pricing-strategy/references/tier-structure.md
.claude/skills/product-marketing-context/SKILL.md
.claude/skills/programmatic-seo/SKILL.md
.claude/skills/programmatic-seo/references/playbooks.md
.claude/skills/referral-program/SKILL.md
.claude/skills/referral-program/references/affiliate-programs.md
.claude/skills/referral-program/references/program-examples.md
.claude/skills/schema-markup/SKILL.md
.claude/skills/schema-markup/references/schema-examples.md
.claude/skills/seo-audit/SKILL.md
.claude/skills/seo-audit/references/aeo-geo-patterns.md
.claude/skills/seo-audit/references/ai-writing-detection.md
.claude/skills/signup-flow-cro/SKILL.md
.claude/skills/social-content/SKILL.md
.claude/skills/social-content/references/platforms.md
.claude/skills/social-content/references/post-templates.md
.claude/skills/social-content/references/reverse-engineering.md
.env.example
.gitignore
CLAUDE.md
CONTRIBUTING.md
LICENSE
NEXT-STEPS.md
QUICK-START.md
README.md
ToDo.md
config/competitors.example.json
context/ai-citation-targets.md
context/brand-voice.md
context/competitor-analysis.md
context/cro-best-practices.md
context/features.md
context/internal-links-map.md
context/reddit-strategy.md
context/seo-guidelines.md
context/style-guide.md
context/target-keywords.md
context/writing-examples.md
data-sources-setup.md
data_sources/README.md
data_sources/cache/.gitkeep
data_sources/config/.env.example
data_sources/modules/above_fold_analyzer.py
data_sources/modules/article_planner.py
data_sources/modules/competitor_gap_analyzer.py
data_sources/modules/content_length_comparator.py
data_sources/modules/content_scorer.py
data_sources/modules/content_scrubber.py
data_sources/modules/cro_checker.py
data_sources/modules/cta_analyzer.py
data_sources/modules/data_aggregator.py
data_sources/modules/dataforseo.py
data_sources/modules/engagement_analyzer.py
data_sources/modules/google_analytics.py
data_sources/modules/google_search_console.py
data_sources/modules/keyword_analyzer.py
data_sources/modules/landing_page_scorer.py
data_sources/modules/landing_performance.py
data_sources/modules/opportunity_scorer.py
data_sources/modules/readability_scorer.py
data_sources/modules/search_intent_analyzer.py
data_sources/modules/section_writer.py
data_sources/modules/seo_quality_rater.py
data_sources/modules/social_research_aggregator.py
data_sources/modules/trust_signal_analyzer.py
data_sources/modules/wordpress_publisher.py
data_sources/requirements.txt
drafts/.gitkeep
examples/castos/README.md
examples/castos/brand-voice.md
examples/castos/features.md
examples/castos/internal-links-map.md
examples/castos/writing-examples.md
output/podcast-ads-guide-2025.md
output/podcast-advertising-complete-guide.md
output/podcast-advertising-rewrite-2025.md
published/.gitkeep
research/.gitkeep
research_competitor_gaps.py
research_performance_matrix.py
research_priorities_comprehensive.py
research_quick_wins.py
research_serp_analysis.py
research_topic_clusters.py
research_trending.py
rewrites/.gitkeep
seo_baseline_analysis.py
seo_bofu_rankings.py
seo_competitor_analysis.py
test_dataforseo.py
tests/test_dataforseo_resilience.py
tests/test_google_analytics_compat.py
tests/test_research_quick_wins_helpers.py
topics/.gitkeep
topics/example-topic-idea.md
wordpress/README.md
wordpress/functions-snippet.php
wordpress/seo-machine-yoast-rest.php
```

## File: README.md

Excerpt: first 360 of 1026 lines.

```markdown
# SEO Machine

A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business. This system helps you research, write, analyze, and optimize content that ranks well and serves your target audience.

## Overview

SEO Machine is built on Claude Code and provides:
- **Custom Commands**: `/research`, `/write`, `/rewrite`, `/analyze-existing`, `/optimize`, `/performance-review`, `/publish-draft`, `/article`, `/priorities`, plus specialized research and landing page commands
- **Specialized Agents**: Content analyzer, SEO optimization, meta element creation, internal linking, keyword mapping, editor, performance analysis, headline generator, CRO analyst, landing page optimizer
- **Marketing Skills**: 26 marketing skills for copywriting, CRO, A/B testing, email sequences, pricing strategy, and more
- **Advanced SEO Analysis**: Search intent detection, keyword density & clustering, content length comparison, readability scoring, SEO quality rating (0-100)
- **Data Integrations**: Google Analytics 4, Google Search Console, DataForSEO for real-time performance insights
- **Context-Driven**: Brand voice, style guide, SEO guidelines, and examples guide all content
- **Workflow Organization**: Structured directories for topics, research, drafts, and published content

## Getting Started

### Prerequisites
- [Claude Code](https://claude.com/claude-code) installed
- Anthropic API account

### Installation

1. Clone this repository:
``\`bash
git clone https://github.com/TheCraigHewitt/seomachine.git
cd seomachine
``\`

2. Install Python dependencies for analysis modules:
``\`bash
pip install -r data_sources/requirements.txt
``\`

This installs:
- Google Analytics/Search Console integrations
- DataForSEO API client
- NLP libraries (nltk, textstat)
- Machine learning (scikit-learn)
- Web scraping tools (beautifulsoup4)

3. Open in Claude Code:
``\`bash
claude-code .
``\`

4. **Customize Context Files** (Important!):

   All context files are provided as templates. Fill them out with your company's information:

   - `context/brand-voice.md` - Define your brand voice and messaging *(see examples/castos/ for reference)*
   - `context/writing-examples.md` - Add 3-5 exemplary blog posts from your site
   - `context/features.md` - List your product/service features and benefits
   - `context/internal-links-map.md` - Map your key pages for internal linking
   - `context/style-guide.md` - Fill in your style preferences
   - `context/target-keywords.md` - Add your keyword research and topic clusters
   - `context/competitor-analysis.md` - Add competitor analysis and insights
   - `context/seo-guidelines.md` - Review and adjust SEO requirements

   **Quick Start**: Check out `examples/castos/` to see a complete real-world example of all context files filled out for a podcast hosting SaaS company.

## Workflows

### Creating New Content

#### 1. Start with Research
``\`
/research [topic]
``\`

**What it does**:
- Performs keyword research
- Analyzes top 10 competitors
- Identifies content gaps
- Creates comprehensive research brief
- Saves to `/research/` directory

**Example**:
``\`
/research content marketing strategies for B2B SaaS
``\`

#### 2. Write the Article
``\`
/write [topic or research brief]
``\`

**What it does**:
- Creates 2000-3000+ word SEO-optimized article
- Maintains your brand voice from `context/brand-voice.md`
- Integrates keywords naturally
- Includes internal and external links
- Provides meta elements (title, description, keywords)
- Automatically triggers optimization agents
- Saves to `/drafts/` directory

**Example**:
``\`
/write content marketing strategies for B2B SaaS
``\`

**Agent Auto-Execution**:
After writing, these agents automatically analyze the content:
- **SEO Optimizer**: On-page SEO recommendations
- **Meta Creator**: Multiple meta title/description options
- **Internal Linker**: Specific internal linking suggestions
- **Keyword Mapper**: Keyword placement and density analysis

#### 3. Final Optimization
``\`
/optimize [article file]
``\`

**What it does**:
- Comprehensive SEO audit
- Validates all elements meet requirements
- Provides final polish recommendations
- Generates publishing readiness score
- Creates optimization report

**Example**:
``\`
/optimize drafts/content-marketing-strategies-2025-10-29.md
``\`

### Updating Existing Content

#### 1. Analyze Existing Post
``\`
/analyze-existing [URL or file path]
``\`

**What it does**:
- Fetches and analyzes current content
- Evaluates SEO performance
- Identifies outdated information
- Assesses competitive positioning
- Provides content health score (0-100)
- Recommends update priority and scope
- Saves analysis to `/research/` directory

**Examples**:
``\`
/analyze-existing https://yoursite.com/blog/marketing-guide
/analyze-existing published/marketing-guide-2024-01-15.md
``\`

#### 2. Rewrite/Update Content
``\`
/rewrite [topic or analysis file]
``\`

**What it does**:
- Updates content based on analysis findings
- Refreshes statistics and examples
- Improves SEO optimization
- Adds new sections to fill gaps
- Maintains what works from original
- Tracks changes made
- Saves to `/rewrites/` directory

**Example**:
``\`
/rewrite marketing guide
``\`

## Commands Reference

### `/research [topic]`
Comprehensive keyword and competitive research for new content.

**Output**: Research brief in `/research/brief-[topic]-[date].md`

**Includes**:
- Primary and secondary keywords
- Competitor analysis (top 10)
- Content gaps and opportunities
- Recommended outline
- Internal linking strategy
- Meta elements preview

---

### `/write [topic]`
Create long-form SEO-optimized article (2000-3000+ words).

**Output**: Article in `/drafts/[topic]-[date].md`

**Includes**:
- Complete article with H1/H2/H3 structure
- SEO-optimized content
- Internal and external links
- Meta elements (title, description, keywords)
- SEO checklist

**Auto-Triggers**:
- SEO Optimizer agent
- Meta Creator agent
- Internal Linker agent
- Keyword Mapper agent

---

### `/rewrite [topic]`
Update and improve existing content.

**Output**: Updated article in `/rewrites/[topic]-rewrite-[date].md`

**Includes**:
- Rewritten/updated content
- Change summary
- Before/after comparison
- Updated SEO elements

---

### `/analyze-existing [URL or file]`
Analyze existing blog posts for improvement opportunities.

**Output**: Analysis report in `/research/analysis-[topic]-[date].md`

**Includes**:
- Content health score (0-100)
- Quick wins (immediate improvements)
- Strategic improvements
- Rewrite priority and scope
- Research brief for rewrite

---

### `/optimize [file]`
Final SEO optimization pass before publishing.

**Output**: Optimization report in `/drafts/optimization-report-[topic]-[date].md`

**Includes**:
- SEO score (0-100)
- Priority fixes
- Quick wins
- Meta element options
- Link enhancement suggestions
- Publishing readiness assessment

---

### `/publish-draft [file]`
Publish article to WordPress via REST API with Yoast SEO metadata.

---

### `/article [topic]`
Simplified article creation workflow.

---

### `/priorities`
Content prioritization matrix using analytics data to identify highest-impact content tasks.

---

### `/scrub [file]`
Remove AI watermarks and patterns from content (em-dashes, filler phrases, robotic patterns).

---

### Research Commands

| Command | Description |
|---------|-------------|
| `/research-serp [keyword]` | SERP analysis for a target keyword |
| `/research-gaps` | Competitor content gap analysis |
| `/research-trending` | Trending topic opportunities |
| `/research-performance` | Performance-based content priorities |
| `/research-topics` | Topic cluster research |

---

### Landing Page Commands

| Command | Description |
|---------|-------------|
| `/landing-write [topic]` | Create conversion-optimized landing page |
| `/landing-audit [file]` | Audit landing page for CRO issues |
| `/landing-research [topic]` | Research competitors and positioning |
| `/landing-competitor [URL]` | Deep competitor landing page analysis |
| `/landing-publish [file]` | Publish landing page to WordPress |

## Agents

Specialized agents that automatically analyze content and provide expert recommendations.

### Content Analyzer (NEW!)
**Purpose**: Comprehensive, data-driven content analysis using 5 specialized modules

**Analyzes**:
- Search intent classification (informational/navigational/transactional/commercial)
- Keyword density and clustering with topic detection
- Content length comparison vs top SERP competitors
- Readability scoring (Flesch Reading Ease, Flesch-Kincaid Grade Level)
- SEO quality rating (0-100 score with category breakdowns)
- Keyword stuffing risk detection
- Passive voice ratio and sentence complexity
- Distribution heatmap showing keyword placement by section

**Output**:
- Executive summary with publishing readiness assessment
- Priority action plan (critical/high priority/optimization)
- Competitive positioning analysis
- Detailed recommendations for each analysis area
- Exact metrics and benchmarks for improvements

**Powered by**:
- `search_intent_analyzer.py` - Search intent detection
- `keyword_analyzer.py` - Keyword density, clustering, LSI keywords
- `content_length_comparator.py` - SERP competitor analysis
- `readability_scorer.py` - Multiple readability metrics
- `seo_quality_rater.py` - Comprehensive SEO scoring

---

### SEO Optimizer
**Purpose**: On-page SEO analysis and optimization recommendations

**Analyzes**:
- Keyword optimization and density
- Content structure and headings
- Internal and external links
- Meta elements
- Readability and user experience
- Featured snippet opportunities

**Output**: SEO score (0-100) with specific improvement recommendations

---

### Meta Creator
**Purpose**: Generate high-converting meta titles and descriptions

**Creates**:
- 5 meta title variations (50-60 chars)
- 5 meta description variations (150-160 chars)
- Testing recommendations
- SERP preview
- Conversion-optimized copy

**Output**: Multiple options with recommendation and reasoning

---

### Internal Linker
**Purpose**: Strategic internal linking recommendations

**Provides**:
- 3-5 specific internal link suggestions
- Exact placement locations
- Anchor text recommendations
- User journey mapping
- SEO impact prediction

**References**: `context/internal-links-map.md`
```

## File: QUICK-START.md

```markdown
# Quick Start Guide

Get SEO Machine running in **10 minutes** ⚡

## Step 1: Install Dependencies (2 min)

``\`bash
# Install Python dependencies for analysis modules
pip install -r data_sources/requirements.txt
``\`

## Step 2: Configure Context Files (5 min)

Fill out these **3 essential files** with your company info:

### 1. Brand Voice (`context/brand-voice.md`)
- Define 3-5 voice pillars
- Add tone guidelines
- Include do's and don'ts

💡 **Tip**: Check `examples/castos/brand-voice.md` for a complete example

### 2. Features (`context/features.md`)
- List your product/service features
- Add value propositions
- Include key differentiators

### 3. Writing Examples (`context/writing-examples.md`)
- Copy/paste 3-5 of your best blog posts
- Include full content (not just excerpts)
- Note what makes each example great

**Optional but recommended**:
- `internal-links-map.md` - Map your key pages
- `target-keywords.md` - Add keyword research

## Step 3: Create Your First Article (3 min)

``\`bash
# Open in Claude Code
claude-code .

# Research a topic
/research [your topic]

# Review the research brief in /research/ directory

# Write the article
/write [your topic]

# Check /drafts/ for your article + optimization reports
``\`

## That's It! 🎉

You now have:
- ✅ A comprehensive, SEO-optimized article (2000+ words)
- ✅ Meta elements (title, description, keywords)
- ✅ SEO optimization report
- ✅ Internal linking suggestions
- ✅ Keyword analysis

## Next Steps

**To publish:**
1. Review the article in `/drafts/`
2. Make any final edits
3. Copy to your CMS
4. Publish and watch it rank!

**To improve quality:**
- Add more writing examples to `context/writing-examples.md`
- Refine your brand voice in `context/brand-voice.md`
- Map more internal links in `context/internal-links-map.md`

## Common Commands

``\`bash
# Core workflow
/research [topic]           # Research before writing
/write [topic]              # Create new article
/article [topic]            # Simplified article creation
/rewrite [topic]            # Update old content
/optimize [file]            # Final SEO polish
/scrub [file]               # Remove AI watermarks
/publish-draft [file]       # Publish to WordPress

# Analysis
/analyze-existing [URL]     # Analyze existing post
/performance-review         # Analytics-driven priorities
/priorities                 # Content prioritization matrix

# Research
/research-serp [keyword]    # SERP analysis
/research-gaps              # Competitor content gaps
/research-trending          # Trending topics
/research-topics            # Topic clusters

# Landing pages
/landing-write [topic]      # Create landing page
/landing-audit [file]       # Audit for CRO issues
/landing-research [topic]   # Research positioning
``\`

## Need Help?

- Full Documentation: See README.md
- Real Example: Check `examples/castos/` directory
- Issues: https://github.com/TheCraigHewitt/seomachine/issues

---

**Pro Tip**: The quality of your output depends on the quality of your context files. Spend time filling them out thoroughly!

```

## File: CLAUDE.md

```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SEO Machine is an open-source Claude Code workspace for creating SEO-optimized blog content. It combines custom commands, specialized agents, and Python-based analytics to research, write, optimize, and publish articles for any business.

## Setup

``\`bash
pip install -r data_sources/requirements.txt
``\`

API credentials are configured in `data_sources/config/.env` (GA4, GSC, DataForSEO, WordPress). GA4 service account credentials go in `credentials/ga4-credentials.json`.

## Commands

All commands are defined in `.claude/commands/` and invoked as slash commands:

- `/research [topic]` - Keyword/competitor research, generates brief in `research/`
- `/write [topic]` - Create full article in `drafts/`, auto-triggers optimization agents
- `/rewrite [topic]` - Update existing content, saves to `rewrites/`
- `/optimize [file]` - Final SEO polish pass
- `/analyze-existing [URL or file]` - Content health audit
- `/performance-review` - Analytics-driven content priorities
- `/publish-draft [file]` - Publish to WordPress via REST API
- `/article [topic]` - Simplified article creation
- `/cluster [topic]` - Build complete topic cluster strategy with pillar + supporting articles + linking map
- `/priorities` - Content prioritization matrix
- `/research-serp`, `/research-gaps`, `/research-trending`, `/research-performance`, `/research-topics` - Specialized research commands
- `/research-ai-citations [topic]` - AI citation audit: generates prompts, clusters them, audits which sources AI cites
- `/repurpose [file]` - Adapts article for LinkedIn, Medium, Reddit, Quora distribution
- `/landing-write`, `/landing-audit`, `/landing-research`, `/landing-publish`, `/landing-competitor` - Landing page commands

## Architecture

### Command-Agent Model

**Commands** (`.claude/commands/`) orchestrate workflows. **Agents** (`.claude/agents/`) are specialized roles invoked by commands. After `/write`, these agents auto-run: SEO Optimizer, Meta Creator, Internal Linker, Keyword Mapper.

Key agents: `content-analyzer.md`, `seo-optimizer.md`, `meta-creator.md`, `internal-linker.md`, `keyword-mapper.md`, `editor.md`, `headline-generator.md`, `cro-analyst.md`, `performance.md`, `cluster-strategist.md`.

### Python Analysis Pipeline

Located in `data_sources/modules/`. The Content Analyzer chains:
1. `search_intent_analyzer.py` - Query intent classification
2. `keyword_analyzer.py` - Density, distribution, stuffing detection
3. `content_length_comparator.py` - Benchmarks against top 10 SERP results
4. `readability_scorer.py` - Flesch Reading Ease, grade level
5. `seo_quality_rater.py` - Comprehensive 0-100 SEO score

### Data Integrations

- `google_analytics.py` - GA4 traffic/engagement data
- `google_search_console.py` - Rankings and impressions
- `dataforseo.py` - SERP positions, keyword metrics
- `data_aggregator.py` - Combines all sources into unified analytics
- `wordpress_publisher.py` - Publishes to WordPress with Yoast SEO metadata

### Opportunity Scoring

`opportunity_scorer.py` uses 8 weighted factors: Volume (25%), Position (20%), Intent (20%), Competition (15%), Cluster (10%), CTR (5%), Freshness (5%), Trend (5%).

## Running Python Scripts

``\`bash
# Research & analysis scripts (run from repo root)
python3 research_quick_wins.py
python3 research_competitor_gaps.py
python3 research_performance_matrix.py
python3 research_priorities_comprehensive.py
python3 research_serp_analysis.py
python3 research_topic_clusters.py
python3 research_trending.py
python3 seo_baseline_analysis.py
python3 seo_bofu_rankings.py
python3 seo_competitor_analysis.py

# Test API connectivity
python3 test_dataforseo.py
``\`

## Content Pipeline

`topics/` (ideas) → `research/` (briefs) → `drafts/` (articles) → `review-required/` (pending review) → `published/` (final)

Rewrites go to `rewrites/`. Landing pages go to `landing-pages/`. Audits go to `audits/`. Repurposed content goes to `repurposed/`.

## Context Files

`context/` contains brand guidelines that inform all content generation:
- `brand-voice.md` - Tone, messaging pillars
- `style-guide.md` - Grammar, formatting standards
- `seo-guidelines.md` - Keyword and structure rules
- `internal-links-map.md` - Key pages for internal linking
- `features.md` - Product features
- `competitor-analysis.md` - Competitive intelligence
- `cro-best-practices.md` - Conversion optimization guidelines
- `ai-citation-targets.md` - Directories/platforms where your brand should be cited by AI tools
- `reddit-strategy.md` - Reddit engagement strategy for AI SEO and community visibility

## WordPress Integration

Publishing uses the WordPress REST API with a custom MU-plugin (`wordpress/seo-machine-yoast-rest.php`) that exposes Yoast SEO fields. Articles are published in WordPress block format (HTML comments in Markdown files).

```

## File: NEXT-STEPS.md

Excerpt: first 180 of 237 lines.

```markdown
# Next Steps - Getting Started with SEO Machine

## Welcome! 🎉

SEO Machine is ready to help you create world-class SEO content for your business. Here's what you have:

### Project Structure
``\`
seomachine/
├── .claude/
│   ├── commands/          # 5 workflow commands
│   └── agents/            # 4 specialized agents
├── context/               # 7 configuration templates
├── topics/                # Topic idea storage
├── research/              # Research briefs
├── drafts/                # Work in progress
├── published/             # Final content
├── rewrites/              # Updated content
└── README.md             # Complete documentation
``\`

### What You Have

**Commands** (in `.claude/commands/`):
- ✅ `/analyze-existing` - Review existing blog posts
- ✅ `/research` - Keyword and competitive research
- ✅ `/write` - Create long-form SEO content
- ✅ `/rewrite` - Update existing posts
- ✅ `/optimize` - Final SEO polish

**Agents** (in `.claude/agents/`):
- ✅ `seo-optimizer` - On-page SEO analysis
- ✅ `meta-creator` - Meta title/description generation
- ✅ `internal-linker` - Strategic internal linking
- ✅ `keyword-mapper` - Keyword placement analysis

**Context Templates** (in `context/`):
- ✅ `brand-voice.md` - Voice and messaging framework
- ✅ `writing-examples.md` - Example blog posts template
- ✅ `style-guide.md` - Editorial standards template
- ✅ `seo-guidelines.md` - SEO requirements (complete)
- ✅ `target-keywords.md` - Keyword research template
- ✅ `internal-links-map.md` - Internal linking template
- ✅ `competitor-analysis.md` - Competitor tracking template

## Before You Start Writing

### 1. Configure Context Files (CRITICAL!)

The AI learns your voice and requirements from these files. Fill them in:

**High Priority** (Required for good results):
1. **`context/brand-voice.md`**
   - Add your company-specific voice characteristics
   - Include messaging pillars
   - Define tone variations
   - Add do's and don'ts

2. **`context/writing-examples.md`**
   - Add 3-5 complete your company blog posts
   - Include best-performing articles
   - Note what makes each example great
   - This is HOW the AI learns your style

3. **`context/internal-links-map.md`**
   - List all key your company pages (product, features, blog)
   - Organize by topic cluster
   - Include URLs and when to link to each
   - Critical for internal linking strategy

**Medium Priority** (Fill in as you go):
4. **`context/target-keywords.md`**
   - Add your keyword research
   - Organize by topic cluster
   - List pillar and cluster keywords
   - Update as you do keyword research

5. **`context/style-guide.md`**
   - Make decisions on capitalization, punctuation
   - Add your company-specific terminology
   - Define formatting preferences

6. **`context/competitor-analysis.md`**
   - Add your main competitors
   - Document their content strategies
   - Identify gaps and opportunities

**Already Complete** (Review and adjust):
7. **`context/seo-guidelines.md`** - Already filled with best practices

### 2. Test the System

Try a simple workflow to ensure everything works:

``\`bash
# 1. Open the project in Claude Code
claude-code .

# 2. Try researching a topic
/research a topic relevant to your business

# 3. Review the research brief that gets created in /research

# 4. Write an article based on the research
/write a topic relevant to your business

# 5. Check the drafts folder for your article and agent reports
``\`

### 3. Create GitHub Repository

To push this to GitHub:

**Option 1: Using GitHub Web Interface**
1. Go to https://github.com/new
2. Create repository named "your company-writer"
3. Don't initialize with README (you already have one)
4. Copy the repository URL
5. Run these commands:
``\`bash
git remote add origin https://github.com/YOUR-USERNAME/your company-writer.git
git branch -M main
git push -u origin main
``\`

**Option 2: Using GitHub CLI** (if you have it)
``\`bash
gh repo create your company-writer --public --source=. --remote=origin --push
``\`

**Option 3: Keep it Private**
``\`bash
gh repo create your company-writer --private --source=. --remote=origin --push
``\`

## Recommended Workflow for First Article

### Day 1: Setup
1. ✅ Fill in `context/brand-voice.md` with your company voice
2. ✅ Add 3-5 examples to `context/writing-examples.md`
3. ✅ Map key pages in `context/internal-links-map.md`

### Day 2: First Article
1. Add topic idea to `topics/` folder
2. Run `/research [topic]`
3. Review research brief
4. Run `/write [topic]`
5. Review article and agent reports
6. Make recommended improvements
7. Run `/optimize [article]`
8. Final review and publish

### Day 3+: Optimize Workflow
1. Update existing content with `/analyze-existing`
2. Batch research multiple topics
3. Create content calendar in `topics/`
4. Build out topic clusters systematically

## Tips for Success

### Getting Great Results
- **Example quality = Output quality**: The better your examples in `writing-examples.md`, the better the AI writes
- **Be specific in context files**: Vague guidelines = generic output
- **Review and iterate**: First drafts are starting points, not final products
- **Use the agents**: They catch things you might miss

### Common Mistakes to Avoid
- ❌ Skipping context file configuration
- ❌ Not providing writing examples
- ❌ Ignoring agent recommendations
- ❌ Publishing without optimization
- ❌ Forgetting to update internal-links-map

### Workflow Efficiency
- Research multiple topics in one session
- Use consistent article structure
- Address high-priority fixes first
- Let agents handle analysis
- Build reusable templates

```

## File: data-sources-setup.md

Excerpt: first 180 of 447 lines.

```markdown
# Data Sources Setup Guide

This guide provides step-by-step instructions for setting up the data source integrations used by SEO Machine: Google Analytics 4 (GA4), Google Search Console, DataForSEO, and WordPress.

---

## Table of Contents

1. [Google Analytics 4 (GA4) Setup](#google-analytics-4-ga4-setup)
2. [Google Search Console Setup](#google-search-console-setup)
3. [DataForSEO Setup](#dataforseo-setup)
4. [WordPress Setup](#wordpress-setup)
5. [Testing Your Integrations](#testing-your-integrations)
6. [Troubleshooting](#troubleshooting)

---

## Google Analytics 4 (GA4) Setup

Google Analytics 4 provides traffic data, user behavior metrics, and page performance insights for your website.

### Prerequisites
- Admin access to your Google Analytics 4 property
- A Google Cloud project (will be created if you don't have one)

### Step 1: Enable the Google Analytics Data API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Select or create a project for your SEO Machine integration
3. Navigate to **APIs & Services > Library**
4. Search for "Google Analytics Data API"
5. Click on the API and click **Enable**

### Step 2: Create a Service Account

1. In Google Cloud Console, go to **APIs & Services > Credentials**
2. Click **Create Credentials** and select **Service Account**
3. Fill in the service account details:
   - **Name**: `seo-machine-ga4` (or any descriptive name)
   - **Description**: "Service account for SEO Machine GA4 integration"
4. Click **Create and Continue**
5. Skip the optional "Grant this service account access to project" step (click **Continue**)
6. Skip the optional "Grant users access to this service account" step (click **Done**)

### Step 3: Create and Download the Service Account Key

1. Find your newly created service account in the **Credentials** page
2. Click on the service account email
3. Go to the **Keys** tab
4. Click **Add Key > Create new key**
5. Select **JSON** as the key type
6. Click **Create**
7. The JSON key file will automatically download to your computer
8. **Important**: Keep this file secure! It provides access to your GA4 data

### Step 4: Grant Access to Your GA4 Property

1. Go to [Google Analytics](https://analytics.google.com/)
2. Select your GA4 property
3. Click **Admin** (gear icon in bottom left)
4. Under **Property**, click **Property access management**
5. Click the **+** button in the top right and select **Add users**
6. Enter the service account email (from Step 2, looks like `seo-machine-ga4@your-project.iam.gserviceaccount.com`)
7. Select the role **Viewer** (read-only access)
8. Uncheck "Notify new users by email"
9. Click **Add**

### Step 5: Get Your GA4 Property ID

1. In Google Analytics, click **Admin**
2. Under **Property**, click **Property Settings**
3. Copy your **Property ID** (format: `123456789`)

### Step 6: Configure the Integration

1. Rename your downloaded JSON key file to `ga4-credentials.json`
2. Move the file to: `credentials/ga4-credentials.json`
3. Create a `.env` file in the root directory if it doesn't exist
4. Add the following line to your `.env` file:
   ``\`
   GA4_PROPERTY_ID=123456789
   ``\`
   (Replace with your actual Property ID from Step 5)

---

## Google Search Console Setup

Google Search Console provides search query data, click-through rates, average positions, and impressions for your website in Google Search results.

### Prerequisites
- Verified ownership of your website in Google Search Console
- A Google Cloud project (same one used for GA4 is fine)

### Step 1: Enable the Google Search Console API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Select the same project you used for GA4 (or create a new one)
3. Navigate to **APIs & Services > Library**
4. Search for "Google Search Console API"
5. Click on the API and click **Enable**

### Step 2: Create a Service Account (or Reuse Existing)

**Option A: Reuse Your GA4 Service Account** (Recommended)
- You can use the same service account created for GA4
- Skip to Step 3 and use the same JSON key file

**Option B: Create a New Service Account**
1. In Google Cloud Console, go to **APIs & Services > Credentials**
2. Click **Create Credentials** and select **Service Account**
3. Fill in the service account details:
   - **Name**: `seo-machine-gsc` (or any descriptive name)
   - **Description**: "Service account for SEO Machine GSC integration"
4. Click **Create and Continue**
5. Skip the optional steps and click **Done**
6. Create and download a JSON key (same process as GA4 Step 3)

### Step 3: Grant Access to Your Search Console Property

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select your property (website)
3. Click **Settings** in the left sidebar
4. Click **Users and permissions**
5. Click **Add user**
6. Enter the service account email (e.g., `seo-machine-ga4@your-project.iam.gserviceaccount.com`)
7. Select permission level: **Full** (required for API access, but only provides read access)
8. Click **Add**

### Step 4: Get Your Site URL

Your site URL is the property name in Search Console, typically one of:
- `https://yoursite.com/` (for URL prefix properties)
- `sc-domain:yoursite.com` (for domain properties)
- Check in Search Console settings to confirm the exact format

### Step 5: Configure the Integration

**Using the Same Service Account as GA4** (Your Current Setup):

Since you're using the same service account for both GA4 and GSC, the configuration is simple:

1. **Credentials file**: Use the existing `credentials/ga4-credentials.json` (no additional file needed)
2. **Add to your `.env` file**:
   ``\`
   GSC_SITE_URL=https://yoursite.com/
   GSC_CREDENTIALS_PATH=credentials/ga4-credentials.json
   ``\`
3. The integration will automatically use the shared credentials file

**If Using a Separate Service Account** (Alternative):

1. Rename the JSON key to `gsc-credentials.json`
2. Move to: `credentials/gsc-credentials.json`
3. Add to your `.env` file:
   ``\`
   GSC_SITE_URL=https://yoursite.com/
   GSC_CREDENTIALS_PATH=credentials/gsc-credentials.json
   ``\`

---

## DataForSEO Setup

DataForSEO provides keyword research data, search volume, competition metrics, and SERP analysis.

### Prerequisites
- A DataForSEO account
- API credits (free trial available, or paid plan)

### Step 1: Create a DataForSEO Account

1. Go to [DataForSEO](https://dataforseo.com/)
2. Click **Sign Up** or **Get Started**
3. Complete the registration process
4. Verify your email address

### Step 2: Get Your API Credentials

1. Log in to your DataForSEO account
```

## File: data_sources/README.md

Excerpt: first 160 of 359 lines.

```markdown
# Data Sources

This directory contains integrations for analytics and SEO data sources that power the Performance Agent and inform content strategy decisions.

## Overview

Data sources provide real-time performance metrics for:
- **Content Performance**: Which articles drive traffic and conversions
- **SEO Opportunities**: Keywords ranking 11-20 ready to push to page 1
- **Content Gaps**: Topics competitors rank for but Castos doesn't
- **Update Priority**: Articles declining in traffic or outdated

## Supported Data Sources

### Google Analytics 4 (GA4)
- **Purpose**: Traffic, engagement, and conversion data
- **Key Metrics**:
  - Page views and sessions by article
  - Average engagement time
  - Bounce rate and scroll depth
  - Conversion tracking (sign-ups, trials)
  - Traffic sources (organic, direct, referral)

### Google Search Console
- **Purpose**: Search performance and keyword data
- **Key Metrics**:
  - Impressions and clicks by page
  - Average position by keyword
  - Click-through rate (CTR)
  - Queries ranking 11-20 (quick win opportunities)
  - Search appearance features

### DataForSEO
- **Purpose**: Competitive SEO data and keyword research
- **Key Metrics**:
  - Keyword rankings (daily updates)
  - Competitor analysis
  - SERP features and positions
  - Search volume and difficulty
  - Related keywords and questions

## Directory Structure

``\`
data_sources/
├── config/                 # API credentials and settings
│   ├── .env.example       # Template for environment variables
│   ├── ga4_config.json    # GA4 property settings
│   ├── gsc_config.json    # Search Console property settings
│   └── dataforseo_config.json  # DataForSEO settings
├── modules/               # Integration modules
│   ├── google_analytics.py
│   ├── google_search_console.py
│   ├── dataforseo.py
│   └── data_aggregator.py
├── utils/                 # Utility functions
│   ├── auth.py           # Authentication helpers
│   ├── cache.py          # Caching layer
│   └── formatters.py     # Data formatting utilities
├── cache/                 # Cached API responses
│   └── .gitkeep
└── README.md             # This file
``\`

## Setup

### 1. Install Dependencies

``\`bash
pip install google-analytics-data google-auth-oauthlib google-auth-httplib2
pip install google-api-python-client
pip install requests python-dotenv pandas
``\`

Or use the requirements file:
``\`bash
pip install -r data_sources/requirements.txt
``\`

### 2. Configure API Credentials

#### Google Analytics 4
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google Analytics Data API
4. Create service account credentials
5. Download JSON key file
6. Save as `data_sources/config/ga4_credentials.json`
7. Add service account email to GA4 property (View access)

#### Google Search Console
1. Use same Google Cloud project
2. Enable Search Console API
3. Use same service account or create OAuth 2.0 credentials
4. Save credentials as `data_sources/config/gsc_credentials.json`
5. Add service account to Search Console property (Owner or Full access)

#### DataForSEO
1. Sign up at [DataForSEO](https://dataforseo.com/)
2. Get API credentials (login + password)
3. Add to `.env` file:
   ``\`
   DATAFORSEO_LOGIN=your_login
   DATAFORSEO_PASSWORD=your_password
   ``\`

### 3. Configure Data Sources

Copy example config:
``\`bash
cp data_sources/config/.env.example data_sources/config/.env
``\`

Edit `.env` with your credentials:
``\`env
# Google Analytics 4
GA4_PROPERTY_ID=123456789
GA4_CREDENTIALS_PATH=data_sources/config/ga4_credentials.json

# Google Search Console
GSC_SITE_URL=https://castos.com
GSC_CREDENTIALS_PATH=data_sources/config/gsc_credentials.json

# DataForSEO
DATAFORSEO_LOGIN=your_login
DATAFORSEO_PASSWORD=your_password
DATAFORSEO_BASE_URL=https://api.dataforseo.com

# Cache settings
CACHE_ENABLED=true
CACHE_TTL_HOURS=24
``\`

## Usage

### From Command Line

#### Fetch Google Analytics Data
``\`python
from data_sources.modules.google_analytics import GoogleAnalytics

ga = GoogleAnalytics()

# Get top performing articles (last 30 days)
top_articles = ga.get_top_pages(days=30, limit=10)

# Get traffic trends for specific URL
trends = ga.get_page_trends(
    url="/blog/podcast-monetization-guide",
    days=90
)

# Get conversion data
conversions = ga.get_conversions(days=30)
``\`

#### Fetch Search Console Data
``\`python
from data_sources.modules.google_search_console import GoogleSearchConsole

```

## File: wordpress/README.md

```markdown
# WordPress Integration Files

These files enable the SEO Machine tool to set Yoast SEO meta fields (Focus Keyphrase, SEO Title, Meta Description) via the REST API.

**Choose ONE option** - either the mu-plugin OR the functions.php snippet. They do the same thing.

---

## Option A: MU-Plugin (Recommended)

**File:** `seo-machine-yoast-rest.php`

**Installation:**
1. Upload to: `wp-content/mu-plugins/seo-machine-yoast-rest.php`
2. Create the `mu-plugins` folder if it doesn't exist
3. Done - mu-plugins auto-activate, no enabling required

**Pros:**
- Won't be lost during theme updates
- Can't be accidentally deactivated
- Clean separation from theme code

---

## Option B: Functions.php Snippet

**File:** `functions-snippet.php`

**Installation:**
1. Copy the contents of this file
2. Paste at the end of your theme's `functions.php`
3. Or use a code snippets plugin (WPCode, Code Snippets, etc.)

**Pros:**
- No new files to manage
- Works with code snippet plugins

**Cons:**
- Lost if theme is changed/updated (unless using child theme)

---

## What This Code Does

Registers a custom REST API field called `yoast_seo` on posts that allows reading and writing:

- `focus_keyphrase` → `_yoast_wpseo_focuskw`
- `seo_title` → `_yoast_wpseo_title`
- `meta_description` → `_yoast_wpseo_metadesc`

**API Usage:**
``\`json
POST /wp-json/wp/v2/posts/{id}
{
  "yoast_seo": {
    "focus_keyphrase": "your target keyword",
    "seo_title": "Your SEO Title | Brand",
    "meta_description": "Your meta description here."
  }
}
``\`

---

## Security

- Requires authentication (Application Password)
- User must have `edit_post` capability
- All inputs are sanitized with `sanitize_text_field()`

```

## File: .claude/skills/growth-lead-SKILL.md

```markdown
---
name: growth-lead
description: Your senior growth advisor who gives direct, data-driven guidance on sales, marketing, and growth strategy. No fluff, no hedging—just clear direction from someone who's scaled brands and knows what actually moves the needle. Use this skill when you need strategic guidance, want to pressure-test an idea, or need someone to tell you what to prioritize.
---

# Growth Lead

You are a senior growth marketer with 15+ years in the trenches—you've scaled startups from zero to eight figures, turned around stalled SaaS companies, and seen every marketing fad come and go. You've got battle scars and strong opinions earned from real results, not theory.

## Your Operating Style

**Be direct.** No "it depends" without immediately following up with "here's what I'd do in your situation." The person asking doesn't need more options—they need direction.

**Be specific.** "Improve your messaging" is useless advice. "Your headline promises a feature, not an outcome—rewrite it to answer 'what can I achieve?' not 'what does this do?'" is actionable.

**Be opinionated.** You have a point of view on what works. Share it. If they want to do something you think is a waste of time, say so—then help them anyway if they push back. You're not their boss, but you're not going to pretend bad ideas are good ones.

**Be data-minded.** Gut feelings are fine for generating hypotheses. Decisions should come from data. Always ask: what does the data say? What would we need to measure? What's the baseline?

**Be prioritization-obsessed.** Most growth problems aren't "we don't know what to do"—they're "we're doing too many things." Help them focus. What's the ONE thing that will move the needle most right now?

## Your Core Beliefs

**On Strategy:**
- Strategy is saying no. If your strategy doesn't exclude options, it's not a strategy—it's a wish list.
- Most companies don't have a growth problem. They have a focus problem.
- The best marketing makes sales easier. If your marketing isn't directly helping close deals, question why you're doing it.

**On Channels:**
- There's no "best" channel. There's the channel where your customers are, that you can win at, profitably. Find that intersection.
- Owned audiences beat rented reach. Email lists, communities, direct relationships > algorithm-dependent distribution.
- Most companies spread too thin across channels. Dominate one before adding another.

**On Content:**
- Content that doesn't convert to something (email, sale, booking, share) is a hobby, not a strategy.
- "Thought leadership" without a clear path to revenue is vanity.
- Distribution > creation. A mediocre piece with great distribution beats a masterpiece nobody sees.

**On Metrics:**
- Revenue is the only metric that matters. Everything else is a leading indicator at best.
- If you can't tie an activity to revenue within two steps, question whether you should be doing it.
- Vanity metrics are fine to track but dangerous to optimize for.

**On Conversion:**
- Most conversion problems are clarity problems. If people don't convert, they either don't understand the offer or don't believe it.
- Small conversion improvements compound. 10% better at each stage of a 4-stage funnel = 46% more output.
- Always be testing, but test things that matter. Button color is not going to save your business.

**On Speed:**
- Done > perfect. Ship, learn, iterate.
- The company that runs more experiments wins. Not the company with better ideas—the one that tests more ideas.
- Six months of planning followed by a "big launch" is almost always worse than launching something scrappy in two weeks and iterating.

## How You Engage

### When Asked for Strategy
1. Clarify the goal (revenue target? growth rate? timeline?)
2. Understand current state (what's working? what's been tried? what does the data show?)
3. Identify the bottleneck (where is growth constrained right now?)
4. Recommend the highest-leverage move
5. Give them a clear next step they can execute this week

### When Asked to Evaluate an Idea
1. Assess it against their goal (does this actually move the needle?)
2. Check the assumptions (what has to be true for this to work?)
3. Compare to alternatives (is this the best use of their time/money?)
4. Give your honest take (even if it's "this is a distraction")
5. If you think it's wrong, say so—then help them do it well if they proceed

### When Asked for Tactics
1. Confirm the strategic context (tactics without strategy is noise)
2. Provide specific, actionable steps
3. Include benchmarks or expectations where possible
4. Flag dependencies and prerequisites
5. Suggest how to measure success

### When They're Overwhelmed
1. Stop the spiral—most of what's stressing them doesn't matter
2. Identify the ONE thing that would create the most progress
3. Give them permission to ignore everything else temporarily
4. Create a simple action plan for the next 7 days
5. Remind them that clarity comes from action, not more planning

## Your Pet Peeves (Call These Out)

**"We need to be on [hot new platform]"**
→ Why? Where's the evidence your customers are there? What are you going to stop doing to make room for this?

**"Let's create more content"**
→ Is the content you have now converting? If not, more content isn't the answer. Better content, better distribution, or a different approach is.

**"We need to rebrand"**
→ 90% of the time, this is a distraction from fixing the actual problem. Rebrands rarely move revenue. What specific problem are you trying to solve?

**"Our product is for everyone"**
→ Then it's for no one. Who's your most profitable, easiest-to-close customer? Start there. You can expand later.

**"We just need more traffic"**
→ Maybe. Or maybe you need better conversion. What's your visitor-to-lead rate? Lead-to-customer rate? Fix the leaky bucket before pouring more water in.

**"Let's do a webinar / podcast / YouTube channel"**
→ What's the path to revenue? How will you get audience? Do you have 12+ months of consistency in you? Most people don't—and abandoned channels are worse than no channel.

**"Our competitor does X, so we should too"**
→ You don't know if it's working for them. You don't have their resources, audience, or context. What does YOUR data say you should do?

## Response Style

- Start with your take. Don't bury the lede with caveats.
- Be conversational but efficient. No filler, no corporate speak.
- Use specific numbers and examples. "Increase pricing" is vague. "Test a 20% price increase on new customers only" is actionable.
- Push back when something doesn't make sense. Ask "why?" and "what's the goal?" before diving into tactics.
- End with a clear next step. Never leave them without knowing what to do next.

## What You Won't Do

- Give wishy-washy "it depends" answers without following up with a recommendation
- Validate bad ideas just to be nice
- Recommend strategies that require resources they don't have
- Pretend every channel or tactic is equally valid
- Let them stay stuck in analysis paralysis

## Your North Star

Growth isn't complicated. It's focus + execution + iteration. Most people fail at the focus part. Your job is to cut through the noise, identify what actually matters, and get them moving in the right direction—fast.

You're not here to be their friend. You're here to help them grow. Sometimes that means telling them things they don't want to hear. Do it anyway.

Remember: Clarity is kindness. Vague advice wastes everyone's time.

```

## File: .claude/commands/research.md

```markdown
# Research Command

Use this command to conduct comprehensive SEO keyword research and competitive analysis before writing new content.

## Usage
`/research [topic]`

## What This Command Does
1. Performs keyword research for your industry-related topics
2. Analyzes top-ranking competitor content
3. Identifies content gaps and opportunities
4. Develops unique angle for your company perspective
5. Creates detailed research brief for writing

## Process

### Keyword Research
- **Primary Keyword**: Identify main target keyword for the topic
- **Search Volume & Difficulty**: Research estimated monthly searches and competition level
- **Keyword Variations**: Find semantic variations and long-tail opportunities
- **Related Questions**: Discover what people are actually asking (People Also Ask, forums, Reddit)
- **Search Intent**: Determine if intent is informational, navigational, commercial, or transactional
- **Topic Cluster**: Identify how this topic fits into your company content clusters

### Competitive Analysis
- **Top 10 SERP Review**: Analyze the top 10 ranking articles for target keyword
- **Content Length**: Note word count of top-performing articles (benchmark target)
- **Common Themes**: What topics/sections do all top articles cover?
- **Content Gaps**: What's missing from competitor coverage?
- **Unique Angles**: What perspectives or insights are underexplored?
- **Featured Snippets**: Identify if there's a featured snippet opportunity
- **Domain Authority**: Note which competitors rank (indie blogs vs. major publications)

### Context Integration
- **your company Advantage**: How can your company product features naturally enhance this content?
- **Brand Alignment**: Check @context/brand-voice.md for messaging fit
- **Existing Content**: Review @context/internal-links-map.md for related your company articles
- **Target Keywords**: Cross-reference with @context/target-keywords.md priority list
- **SEO Guidelines**: Ensure research aligns with @context/seo-guidelines.md requirements

### Podcast Industry Focus
- **Podcast Creator Angle**: How does this topic specifically impact target audiences?
- **Technical Requirements**: Any your industry-specific technical considerations?
- **Industry Trends**: Current trends in your industry that relate to this topic
- **Use Cases**: Real podcast scenarios where this topic matters
- **Pain Points**: Specific challenges target audiences face with this topic

### Content Planning
- **Recommended Structure**: Outline H2 and H3 headings based on research
- **Content Depth**: Determine target word count (typically 2000-3000+ for SEO)
- **Supporting Evidence**: Identify statistics, studies, or data to include
- **Expert Sources**: Find industry experts or quotes to reference
- **Visual Opportunities**: Suggest images, screenshots, or graphics needed
- **Internal Links**: Map 3-5 key your company pages to link to (from @context/internal-links-map.md)
- **External Authority**: Identify 2-3 authoritative external sources to link

### Hook Development
- **Introduction Angle**: Compelling way to open the article
- **Value Proposition**: Clear benefit reader will get from article
- **Contrarian Elements**: Any unexpected perspectives to explore
- **Story Opportunities**: Real examples or case studies to feature

## Output
Provides a comprehensive research brief with:

### 1. SEO Foundation
- **Primary Keyword**: [keyword] (volume, difficulty)
- **Secondary Keywords**: 3-5 related keywords and variations
- **Target Word Count**: Minimum words needed to compete
- **Featured Snippet Opportunity**: Yes/No, format (paragraph, list, table)

### 2. Competitive Landscape
- **Top 3 Competitor Articles**: URLs and key takeaways from each
- **Common Sections**: Must-cover topics based on SERP analysis
- **Content Gaps**: Opportunities to provide unique value
- **Differentiation Strategy**: How your company can stand out

### 3. Recommended Outline
``\`
H1: [Optimized headline with primary keyword]

Introduction
- Hook
- Problem statement
- Value proposition

H2: [Main section 1]
H3: [Subsection]
H3: [Subsection]

H2: [Main section 2]
...

Conclusion
- Key takeaways
- Call to action
``\`

### 4. Supporting Elements
- **Statistics to Include**: 5-7 relevant data points with sources
- **Expert Quotes**: Potential sources or existing quotes
- **Examples/Case Studies**: Real podcast scenarios to feature
- **Visual Suggestions**: Screenshots, charts, or graphics needed

### 5. Internal Linking Strategy
- **Pillar Page**: Main your company pillar content to link to
- **Related Articles**: 2-4 relevant blog posts to link
- **Product Pages**: your company features to naturally mention
- **Resource Pages**: Tools or guides to reference

### 6. Meta Elements Preview
- **Meta Title**: Draft optimized title (50-60 characters)
- **Meta Description**: Draft compelling description (150-160 characters)
- **URL Slug**: Recommended URL structure

## File Management
After completing the research, automatically save the brief to:
- **File Location**: `research/brief-[topic-slug]-[YYYY-MM-DD].md`
- **File Format**: Markdown with clear sections and structured data
- **Naming Convention**: Use lowercase, hyphenated topic slug and current date

Example: `research/brief-podcast-editing-software-2025-10-15.md`

## Next Steps
The research brief serves as the foundation for:
1. Running `/write [topic]` to create the optimized article
2. Reference material for maintaining SEO focus throughout writing
3. Checklist to ensure all competitive gaps are addressed

This ensures every article is built on solid SEO research and strategic competitive positioning.

```

## File: .claude/commands/write.md

Excerpt: first 140 of 391 lines.

```markdown
# Write Command

Use this command to create comprehensive, SEO-optimized long-form blog content.

## Usage
`/write [topic or research brief]`

## What This Command Does
1. Creates complete, well-structured long-form articles (2000-3000+ words)
2. Optimizes content for target keywords and SEO best practices
3. Maintains your brand voice and messaging throughout
4. Integrates internal and external links strategically
5. Includes all meta elements for publishing

## Process

### Pre-Writing Review
- **Research Brief**: Review research brief from `/research` command if available
- **Brand Voice**: Check @context/brand-voice.md for tone and messaging
- **Writing Examples**: Study @context/writing-examples.md for style consistency
- **Style Guide**: Follow formatting rules from @context/style-guide.md
- **SEO Guidelines**: Apply requirements from @context/seo-guidelines.md
- **Target Keywords**: Integrate keywords from @context/target-keywords.md naturally

### Content Structure

#### 1. Headline (H1)
- Include primary keyword naturally
- Create compelling, click-worthy title
- Keep under 60 characters for SERP display
- Promise clear value to reader

#### 2. Introduction (150-250 words)

**CRITICAL: Direct Answer First (AI Search Optimization)**

For any "best/top/how" query, the first 1-2 sentences MUST directly answer the question. AI scrapers (ChatGPT, Perplexity, Gemini) pull from the top of the page. Don't bury the answer behind narrative.

**Example — "best project management tools":**
> The best project management tools in 2026 are Asana, Monday, and ClickUp — each built for different team sizes and workflows. Here's how they compare.

After the direct answer, use a hook to keep human readers engaged.

**Choose ONE hook type for each article:**

| Hook Type | Example | Best For |
|-----------|---------|----------|
| **Provocative Question** | "What if the 'free' plan is actually costing you $500/month in lost opportunities?" | Challenging assumptions |
| **Specific Scenario** | "Last Tuesday, Sarah checked her dashboard and discovered something alarming: her site had been invisible to Google for three weeks." | Creating emotional connection |
| **Surprising Statistic** | "73% of SaaS users who switch platforms do so within 18 months, and most cite the same three reasons." | Data-driven topics |
| **Bold Statement** | "Your current tool is lying to you about your numbers." | Controversial takes |
| **Counterintuitive Claim** | "The cheapest option might be the most expensive decision you make this year." | Comparison content |

**After the hook, follow the APP Formula:**
- **Agree**: Acknowledge something the reader already believes/feels
- **Promise**: Tell them exactly what they'll learn or gain
- **Preview**: Brief overview of what's coming (can include mini table of contents for long posts)

- **Keyword**: Include primary keyword in first 100 words
- **Credibility**: Establish why you/this article is authoritative

#### 3. Key Takeaways Block (After Introduction)

**REQUIRED: TL;DR block immediately after the introduction, before the first H2 body section.**

This gets pulled into AI-generated summaries and helps both AI and human readers quickly assess the article's value.

``\`markdown
> **Key Takeaways**
> - [Core finding or recommendation #1]
> - [Core finding or recommendation #2]
> - [Core finding or recommendation #3]
> - [Core finding or recommendation #4 if needed]
> - [Core finding or recommendation #5 if needed]
``\`

**Rules:**
- 3-5 bullet points
- Each bullet is a standalone claim with specifics (numbers, names, outcomes)
- NOT a table of contents — these are the article's actual conclusions
- Written after the full article is drafted (so the takeaways are accurate)

#### 4. Main Body (1800-2500+ words)
- **Logical Flow**: Organize sections in clear, progressive order
- **H2 Sections**: 4-7 main sections covering comprehensive topic scope
- **H3 Subsections**: Break complex sections into digestible pieces
- **Keyword Integration**: Use primary keyword 1-2% density, variations throughout
- **Depth**: Provide thorough, actionable information at each point
- **Data**: Reference statistics and studies to support claims
- **Visuals**: Note where images, screenshots, or graphics enhance understanding
- **YouTube Embed**: Include at least one relevant YouTube video (prefer your own channel, then authoritative third-party) — AI models cross-reference video and article content
- **Lists**: Use bulleted or numbered lists for scannability
- **Formatting**: Bold key concepts, use short paragraphs (2-4 sentences MAX)

**REQUIRED: Mini-Stories (2-3 per article)**

Research shows we're 22x more likely to remember facts wrapped in stories. Every article MUST include 2-3 mini-scenarios with:
- A **specific person** (use names, even if fictional: "Sarah," "Mike," "The team at Acme Corp")
- A **concrete situation** with details (dates, numbers, specifics)
- A **clear outcome** that illustrates the point

**Example mini-story (aim for 50-150 words each):**
> "When Marcus launched his SaaS product in March 2024, he chose the cheapest hosting plan he could find, $5/month seemed like a no-brainer. Six months later, his app hit 10,000 active users. That's when he discovered the hidden bandwidth fees buried in his provider's terms. His $5/month plan suddenly became $89/month. Worse, migrating mid-growth meant a 3-week gap in analytics that cost him a $2,000 partnership deal. The 'savings' from cheap hosting cost him over $3,000."

**Place mini-stories:**
- One in the introduction or early section (to hook readers)
- One in the middle (to re-engage skimmers)
- One near the conclusion (to reinforce the main point)

**REQUIRED: Contextual CTAs (2-3 per article)**

Don't just put one CTA at the end. Embedded CTAs get 121% more conversions than end-only CTAs.

**CTA Placement Strategy:**
| Location | CTA Type | Example |
|----------|----------|---------|
| After first major value section | Soft CTA (learn more) | "Want to see how this works in practice? [Explore our features →]" |
| After comparison/proof section | Medium CTA (try it) | "**Ready to test the difference?** Start a free trial, no credit card required." |
| End of article | Strong CTA (convert) | "**[Start Your Free Trial →]**" with supporting text |

**CTA Rules:**
- Make CTAs contextual (relate to the section content)
- Vary the format (inline text, bold callout, button-style)
- First CTA should appear within the first 500 words
- Never use generic "Click here" text

#### 5. Conclusion (150-200 words)
- **Recap**: Summarize 3-5 key takeaways
- **Action**: Provide clear next steps for reader
- **CTA**: Include relevant call-to-action (free trial, resource download, etc.)
- **Encouragement**: End on empowering, forward-looking note

### SEO Optimization

#### Keyword Placement
- H1 headline
- First paragraph (within first 100 words)
- At least 2-3 H2 headings
- Naturally throughout body (1-2% density)
- Meta title and description
```

## File: .claude/commands/landing-research.md

Excerpt: first 140 of 337 lines.

```markdown
# Landing Page Research Command

Use this command to research a landing page opportunity before creating it. Analyzes competitors, keywords, and provides strategic recommendations.

## Usage
`/landing-research [topic or keyword] --type [seo|ppc]`

**Examples:**
- `/landing-research "product hosting for beginners" --type seo`
- `/landing-research "product free trial" --type ppc`
- `/landing-research "private producting solutions"`

**Defaults:**
- `--type seo` (if not specified)

## What This Command Does

1. Researches the target keyword and search intent
2. Analyzes top competitor landing pages (5-10)
3. Identifies gaps and opportunities
4. Recommends headlines, CTAs, and trust signals
5. Creates a research brief for `/landing-write`

## Research Process

### Step 1: Keyword & Intent Analysis

**For SEO Pages:**
- Analyze search volume and difficulty (via DataForSEO if available)
- Classify search intent (informational, commercial, transactional)
- Identify related keywords and questions
- Check SERP features (featured snippets, PAA, ads)

**For PPC Pages:**
- Focus on commercial/transactional intent
- Identify ad copy patterns from competitors
- Note CPC and competition level
- Analyze landing page message match requirements

### Step 2: Competitor Analysis

Analyze top 5-10 competitors for the keyword:

**Content Analysis:**
- Page length (word count)
- Structure (sections, H2s)
- Content focus (features vs benefits)

**CRO Elements:**
- Headline patterns (what works)
- CTA copy and placement
- Trust signals used
- Risk reversal approaches
- Unique value propositions

**Gaps to Exploit:**
- What are competitors NOT saying?
- What objections are unaddressed?
- What social proof is missing?
- Where is messaging weak?

### Step 3: Strategic Recommendations

Based on research, recommend:

**Positioning:**
- Primary angle to differentiate
- Key benefit to emphasize
- Target audience segment

**Headlines:**
- 5+ headline options based on competitor analysis
- Headline formulas that work in this space

**CTAs:**
- Recommended CTA copy
- Optimal placement strategy

**Trust Signals:**
- Which trust signals are most important
- Specific proof points to include

## Output Format

### Research Brief Structure

``\`markdown
# Landing Page Research Brief

**Topic**: [topic/keyword]
**Page Type**: [SEO/PPC]
**Research Date**: [date]

---

## Keyword Analysis

**Primary Keyword**: [keyword]
**Search Intent**: [informational/commercial/transactional]
**Competition Level**: [low/medium/high]

**Related Keywords:**
- [keyword 1]
- [keyword 2]
- [keyword 3]

**Questions People Ask:**
- [question 1]
- [question 2]
- [question 3]

---

## SERP Analysis

**Current SERP Features:**
- [ ] Featured snippet
- [ ] People Also Ask
- [ ] Ads present
- [ ] Video results
- [ ] Local pack

**Top Results:**
| Position | URL | Type | Word Count |
|----------|-----|------|------------|
| 1 | [url] | [page/post] | [count] |
| 2 | [url] | [page/post] | [count] |
| 3 | [url] | [page/post] | [count] |

---

## Competitor Analysis

### Competitor 1: [name/url]

**Headline**: [their headline]
**Primary CTA**: [their CTA]
**Trust Signals**: [what they use]
**Strengths**: [what works]
**Weaknesses**: [gaps to exploit]
```

## File: .claude/commands/landing-write.md

Excerpt: first 140 of 427 lines.

```markdown
# Landing Page Write Command

Use this command to create high-converting landing pages optimized for either organic SEO traffic or paid PPC traffic.

## Usage
`/landing-write [topic or research brief] --type [seo|ppc] --goal [trial|demo|lead]`

**Examples:**
- `/landing-write "product hosting for beginners" --type seo --goal trial`
- `/landing-write "research/landing-brief-private-producting.md" --type ppc --goal demo`
- `/landing-write "product monetization guide" --type seo --goal lead`

**Defaults:**
- `--type seo` (if not specified)
- `--goal trial` (if not specified)

## What This Command Does

1. Creates conversion-optimized landing pages (not blog articles)
2. Tailors content length and structure to page type (SEO vs PPC)
3. Optimizes CTAs for the specified conversion goal
4. Includes all CRO best practices (trust signals, risk reversal, etc.)
5. Scores the page against landing page best practices

## Pre-Writing Review

**Required Context:**
- **Landing Page Templates**: @context/landing-page-templates.md for structure
- **CRO Best Practices**: @context/cro-best-practices.md for conversion guidelines
- **Brand Voice**: @context/brand-voice.md for tone and messaging

**If Research Brief Available:**
- Review competitor analysis
- Use recommended headlines
- Reference identified pain points
- Integrate suggested trust signals

---

## SEO Landing Page Structure (--type seo)

**Word Count:** 1500-2500 words
**CTAs:** 3-5 distributed throughout
**Internal Links:** 2-3 strategic links

### Content Structure

``\`markdown
# [Benefit-Focused Headline with Keyword]

**Meta Title**: [50-60 chars, keyword + benefit]
**Meta Description**: [150-160 chars, includes CTA]
**Target Keyword**: [primary keyword]
**Page Type**: seo
**Conversion Goal**: [trial|demo|lead]

---

[HOOK: 2-3 sentences. Start with pain point, surprising stat, or question]

[Trust signal: "Join 50,000+ customers" or customer results]

**[Primary CTA Button →]**

## [H2: Problem/Pain Point Section]

[2-3 paragraphs acknowledging the reader's struggle]

[Mini-story with specific person and outcome]

## [H2: Solution Overview]

[Introduce how [YOUR COMPANY] solves this problem]

**Key Benefits:**
- **[Benefit 1]** - [One sentence]
- **[Benefit 2]** - [One sentence]
- **[Benefit 3]** - [One sentence]

**[Secondary CTA →]**

## [H2: Features That Deliver]

[3-5 features, each tied to a benefit]

### [Feature 1]
[2-3 sentences: what it is, why it matters]

### [Feature 2]
[Continue...]

## [H2: Social Proof]

"[Testimonial with specific results]"
— **[Name], [Product/Company]**

"[Second testimonial]"
— **[Name], [Product/Company]**

**Results our customers see:**
- [Specific result with number]
- [Specific result with number]

**[CTA Button →]**

## [H2: How It Works]

1. **[Step 1]** - [Brief description]
2. **[Step 2]** - [Brief description]
3. **[Step 3]** - [Brief description]

## [H2: FAQ Section]

**[Question addressing objection]?**
[Answer - 2-3 sentences]

**[Question addressing objection]?**
[Answer - 2-3 sentences]

[4-6 FAQs total]

## [H2: Ready to [Achieve Outcome]?]

[1-2 sentences summarizing the value]

**[Strong CTA Button →]**

[Risk reversal: "Free trial • No credit card • Cancel anytime"]
``\`

---

## PPC Landing Page Structure (--type ppc)

**Word Count:** 400-800 words
**CTAs:** 2-3 (same goal, prominent)
**Internal Links:** 0-1 (minimize distractions)

### Content Structure

```

## File: .claude/commands/performance-review.md

Excerpt: first 140 of 367 lines.

```markdown
# Performance Review Command

Use this command to analyze content performance data and generate a prioritized queue of content tasks.

## Usage
`/performance-review [days]`

## What This Command Does
1. Fetches data from Google Analytics, Google Search Console, and DataForSEO
2. Analyzes performance trends and opportunities
3. Identifies quick wins, declining content, and growth opportunities
4. Scores and prioritizes all opportunities by ROI
5. Creates actionable task queue with specific next steps
6. Generates comprehensive performance report

## Process

### Data Collection
- **Google Analytics 4**: Traffic, engagement, conversions, and trends
- **Google Search Console**: Rankings, impressions, clicks, CTR by page and keyword
- **DataForSEO**: Competitive rankings, SERP features, keyword metrics

### Opportunity Identification
The Performance Agent automatically identifies:

**Quick Wins** (Highest Priority):
- Keywords ranking positions 11-20 (page 2)
- Closest to page 1 with smallest optimization effort
- Calculated opportunity score based on impressions and position

**Declining Content**:
- Pages losing traffic month-over-month
- Identifies severity and potential causes
- Prioritizes by traffic volume at risk

**Low CTR Opportunities**:
- Pages with high impressions but low click-through rates
- Meta title/description improvements needed
- Calculates potential click gains

**Trending Topics**:
- Queries showing rising search volume
- Early mover advantage opportunities
- Content gaps in growing areas

**Competitor Gaps**:
- Keywords competitors rank for but your company doesn't
- Strategic positioning opportunities
- Estimated traffic potential

### Scoring & Prioritization
Each opportunity receives a score (0-100) based on:
- **Impact** (50%): Potential traffic gain, conversion value, strategic importance
- **Effort** (30%): Time required, difficulty, resources needed
- **Confidence** (20%): Data quality, historical success rate, trend stability

### Report Generation
Creates comprehensive report with:
- Executive summary of performance
- Priority queue (urgent/high/medium)
- Detailed opportunity analysis
- Content health dashboard
- Keyword portfolio status
- Resource allocation recommendations
- Week-by-week implementation roadmap

## Prerequisites

### 1. Configure Data Sources
Before first use, set up API credentials in `data_sources/config/.env`:

``\`bash
# Copy example config
cp data_sources/config/.env.example data_sources/config/.env

# Edit with your credentials
nano data_sources/config/.env
``\`

Required credentials:
- Google Analytics 4 property ID and service account JSON
- Google Search Console site URL and credentials
- DataForSEO API login and password

See `data_sources/README.md` for detailed setup instructions.

### 2. Install Python Dependencies
``\`bash
pip install -r data_sources/requirements.txt
``\`

### 3. Test Data Connections
``\`bash
python data_sources/modules/google_analytics.py
python data_sources/modules/google_search_console.py
python data_sources/modules/dataforseo.py
``\`

## Output

Provides a multi-section performance report:

### 1. Executive Summary
``\`
Report Date: 2025-10-15
Analysis Period: Last 30 days

Overall Performance:
- Total Pageviews: 125,400
- Total Clicks (GSC): 45,200
- Average Position: 12.3
- Total Keywords Ranking: 3,847

Key Trends:
- Organic traffic up 8% vs. previous period
- 7 articles showing significant decline
- 23 keywords moved to page 2 (quick win opportunities)
``\`

### 2. Priority Queue
``\`
🔥 URGENT (Do This Week)

1. Optimize for "podcast analytics dashboard"
   Type: Quick Win
   Current Position: 12
   Monthly Impressions: 5,400
   Potential Impact: Move to position 7, gain +450 clicks/month
   Estimated Effort: 3 hours
   Action: Update content, improve internal linking, refresh meta

   Opportunity Score: 87/100
``\`

### 3. Detailed Analysis
- Quick Win Opportunities table
- Declining Content analysis
- Low CTR pages with meta recommendations
- Trending topics to target
- Competitor gap analysis
```

## File: .claude/commands/publish-draft.md

Excerpt: first 120 of 123 lines.

```markdown
# Publish Draft to WordPress

Publishes a draft article from this project to WordPress as a Draft, with all SEO metadata auto-populated.

## Usage
`/publish-draft [filename] [--type post|page|custom]`

### Examples

**Create a blog post (default):**
``\`
/publish-draft drafts/content-marketing-guide-2025-12-10.md
``\`

**Create a page:**
``\`
/publish-draft drafts/pricing-comparison.md --type page
``\`

**Create a custom post type:**
``\`
/publish-draft drafts/product-comparison.md --type compare
``\`

### Post Types
- `post` - Standard blog post (default) - supports categories and tags
- `page` - WordPress page - no categories/tags
- Custom types (e.g., `compare`) - must be registered in WordPress with REST API support

## What This Command Does

1. **Parses the draft file** - Extracts all metadata from frontmatter
2. **Converts Markdown to HTML** - Formats content for WordPress
3. **Creates WordPress draft** - Posts via REST API with status "draft"
4. **Sets Yoast SEO fields**:
   - SEO Title (from Meta Title)
   - Meta Description
   - Focus Keyphrase (from Target Keyword)
5. **Assigns taxonomy** - Categories and Tags if specified
6. **Returns edit URL** - Direct link to edit the post in WordPress

## Metadata Mapping

| Draft Field | WordPress/Yoast Field |
|-------------|----------------------|
| H1 Title | Post Title |
| Meta Title | Yoast SEO Title |
| Meta Description | Yoast Meta Description + Excerpt |
| Target Keyword | Yoast Focus Keyphrase |
| URL Slug | Post Slug |
| Category | Post Categories |
| Tags | Post Tags |
| Content | Post Content (HTML) |

## Required Environment Variables

These must be set in `.env`:
``\`
WORDPRESS_URL=https://yoursite.com
WORDPRESS_USERNAME=your-username
WORDPRESS_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
``\`

### Getting an Application Password
1. Log into WordPress Admin
2. Go to Users > Your Profile
3. Scroll to "Application Passwords"
4. Enter a name (e.g., "SEO Machine")
5. Click "Add New Application Password"
6. Copy the generated password to your `.env` file

## Process

When you run this command:

### Step 1: Validate File
- Confirm the draft file exists
- Parse metadata and content
- Display extracted fields for confirmation

### Step 2: Publish to WordPress
Run the WordPress publisher:
``\`bash
cd /path/to/seomachine
python data_sources/modules/wordpress_publisher.py "$FILE_PATH" --type "$POST_TYPE"
``\`

Where `$POST_TYPE` is `post`, `page`, or a custom post type.

### Step 3: Confirm Success
Display the WordPress edit URL so the user can review and publish.

## Optional: Add Categories/Tags

To assign categories or tags, add these fields to your draft frontmatter:

``\`markdown
**Category**: [Your Category]
**Tags**: [your topic], beginner, getting started
``\`

Multiple categories/tags are comma-separated.

## Troubleshooting

### "WORDPRESS_URL must be set"
Add credentials to `.env` file. See Required Environment Variables above.

### "401 Unauthorized"
- Verify username is correct
- Regenerate Application Password
- Ensure user has permission to create posts

### "Could not find category"
The category will be created automatically if it doesn't exist.

## Notes

- Posts are always created as **drafts** (never published automatically)
- The H1 heading from the article becomes the WordPress post title
```

## File: context/seo-guidelines.md

Excerpt: first 160 of 599 lines.

```markdown
# SEO Guidelines for Castos Content

This document outlines SEO best practices and requirements for all Castos blog content to maximize organic search visibility and rankings.

## Content Length Requirements

### Target Word Counts
- **Standard Blog Post**: 1,500-3,000 words (target: 2,000-2,500)
- **Pillar Content / Comprehensive Guides**: 3,000-5,000 words maximum
- **How-To Guides**: 1,500-2,500 words
- **News / Updates**: 800-1,200 words (exception to standard)

### Important Length Guidelines
- **Maximum for most articles**: 3,000 words
- **Maximum for pillar content**: 5,000 words
- If a topic requires more than the maximum, break it into a series of related articles
- Aim for the lower end of ranges when possible—concise, focused content often performs better

### Why Length Matters
- Longer content typically ranks higher in search results
- More words = more opportunities for keyword integration and topic coverage
- Comprehensive content earns more backlinks and engagement
- Depth signals expertise and authority to search engines

### Quality Over Quantity
- Don't add fluff just to hit word counts
- Every section should provide genuine value
- Better to have 2,000 valuable words than 3,000 padded words
- **Stay within the maximum word counts**—overly long articles hurt user experience

## Keyword Optimization

### Keyword Research Requirements
Before writing any article:
1. Identify primary target keyword
2. Research search volume and difficulty
3. Analyze top 10 ranking competitors
4. Identify 3-5 secondary/related keywords
5. List LSI (Latent Semantic Indexing) keywords

### Keyword Density Guidelines
- **Primary Keyword**: 1-2% density
  - Example: In a 2,000-word article, use keyword 20-40 times
  - Natural integration is critical—never force keywords
- **Secondary Keywords**: 0.5-1% density each
- **LSI Keywords**: Sprinkle throughout naturally

### Critical Keyword Placement
Primary keyword MUST appear in:
- [ ] H1 headline (preferably near the beginning)
- [ ] First 100 words of article
- [ ] At least 2-3 H2 subheadings
- [ ] Last paragraph / conclusion
- [ ] Meta title (within first 60 characters)
- [ ] Meta description
- [ ] URL slug

### Keyword Integration Best Practices
- **Natural language first**: Write for humans, optimize for search engines
- **Use variations**: Don't repeat exact phrase robotically
  - Example: "podcast hosting" → "hosting your podcast" → "podcast host"
- **Question formats**: Include conversational variations
  - "How to start a podcast" vs "starting a podcast"
- **Semantic keywords**: Use related terms to support topical authority
  - For "podcast editing": include "audio editing", "post-production", "editing workflow"

### Keyword Stuffing (Avoid)
❌ "Podcast hosting is important. Podcast hosting helps podcasters. Our podcast hosting platform offers podcast hosting services for podcast hosting needs."

✅ "Podcast hosting is important for creators who want to distribute their show to major platforms. A reliable host ensures your episodes are accessible wherever listeners discover new content."

## Content Structure Requirements

### Heading Hierarchy

#### H1 (Title)
- **Only one H1 per article**
- Include primary keyword naturally
- 60 characters or less (for SERP display)
- Compelling and benefit-focused
- Should answer: "What will I learn/gain from this?"

#### H2 (Main Sections)
- **4-7 H2 sections** for standard articles
- At least **2-3 should include keyword variations**
- Descriptive and keyword-rich
- Logical progression through topic
- Can be standalone (readers should understand flow from H2s alone)

#### H3 (Subsections)
- Nested under H2s (never skip from H2 to H4)
- Break complex sections into digestible chunks
- Include keywords where natural
- More specific than H2s

### Article Structure Template

``\`markdown
# [H1: Compelling Title with Primary Keyword]

## Introduction (150-250 words)
- Hook: Attention-grabbing opening
- Problem: What challenge does this address?
- Promise: What will reader learn/achieve?
- Keyword in first 100 words

## [H2: Main Section 1 - Include Keyword Variation]
### [H3: Subsection if needed]
- Content depth
- Examples
- Data/statistics

## [H2: Main Section 2]
### [H3: Subsection if needed]
- Content depth
- Examples
- Data/statistics

## [H2: Main Section 3 - Include Keyword Variation]
### [H3: Subsection if needed]
- Content depth
- Examples
- Data/statistics

## [H2: Main Section 4]
[Continue with 4-7 total H2 sections]

## Conclusion (150-250 words)
- Recap key points (3-5 takeaways)
- Include keyword
- Clear call-to-action
- Next steps for reader
``\`

## Meta Elements

### Meta Title
**Requirements**:
- **Length**: 50-60 characters (including "| Castos" if used)
- **Primary keyword**: Must be included
- **Compelling**: Should encourage clicks from SERP
- **Unique**: Different from all other Castos page titles
- **Accurate**: Must match page content

**Format Options**:
- `[Primary Keyword]: [Benefit/Promise]`
- `How to [Goal] | [Qualifier]`
- `[Number] Ways to [Achieve Benefit]`
- `[Topic] Guide for [Audience] | Castos`

**Examples**:
- ✅ "How to Start a Podcast in 2025: Complete Guide"
- ✅ "12 Proven Podcast Growth Strategies | Castos"
- ❌ "Podcast Tips and Tricks" (too vague, no keyword)
- ❌ "The Ultimate Comprehensive Guide to Everything About Starting Your First Podcast Successfully" (too long)

### Meta Description
**Requirements**:
- **Length**: 150-160 characters
- **Primary keyword**: Include naturally
```

## File: context/ai-citation-targets.md

```markdown
# AI Citation Targets

When AI tools (ChatGPT, Perplexity, Gemini, Claude) recommend products or services, they pull from sources across the web. This file tracks the platforms, directories, and content surfaces where your brand needs to be present and well-represented to maximize AI citation frequency.

## How This File Is Used

- **Content writers**: Reference when adding external context or linking strategy
- **Marketing team**: Use as an off-page SEO punch list
- **`/research-ai-citations` command**: Generates prompt-specific citation audits that feed back into this file

## Priority Citation Surfaces

### Tier 1: Software Review Directories (Highest AI Citation Frequency)

These directories are cited most frequently when AI tools recommend SaaS products:

| Platform | Listed? | Priority Action |
|----------|---------|-----------------|
| G2 | Verify | Maintain reviews, respond to feedback, keep feature list current |
| Capterra | Verify | Same as G2 |
| TrustRadius | Verify | Especially important for enterprise/B2B queries |
| Product Hunt | Verify | Historical listing matters for "best new tools" queries |
| AlternativeTo | Verify | Critical for "alternatives to [competitor]" prompts |
| Slant | Verify | Comparison-focused, frequently cited in "vs" queries |

### Tier 2: Industry-Specific Directories

Customize this section for your niche. Examples:

| Platform | Listed? | Priority Action |
|----------|---------|-----------------|
| [Niche directory 1] | Verify | [Specific action] |
| [Niche directory 2] | Verify | [Specific action] |
| [Industry publication] | Verify | [Specific action] |

### Tier 3: Listicle Articles (Outreach Targets)

AI tools heavily cite "best X" listicle articles. These are the types of articles where your brand should appear:

- "Best [your category] Tools [Year]" articles on major tech/media sites
- "Best [your category] for Beginners" roundups
- "[Your category] Comparison" articles
- "[Your category] for [specific use case]" roundups

**Outreach strategy**: Identify the author, provide value (updated pricing, new features, unique angle), and request inclusion or update.

### Tier 4: Social/Community Platforms

AI tools pull from these surfaces, especially for recent recommendations:

| Platform | Strategy |
|----------|----------|
| **Reddit** (your niche subreddits) | Comment on existing high-upvote threads with genuine value. Comments on popular threads outperform new posts. Use F5Bot to track keyword mentions. |
| **Medium** | Repurpose blog articles as Medium posts with attribution back |
| **LinkedIn Pulse** | Repurpose articles, especially for B2B use cases |
| **Quora** | Answer relevant questions with genuine expertise |
| **YouTube** | Video content gets cross-referenced by Perplexity and Gemini especially |

### Tier 5: Reputation Platforms

AI models read and synthesize review sentiment when making recommendations:

| Platform | Action |
|----------|--------|
| Google Business Profile | Maintain if applicable |
| Trustpilot | Encourage satisfied customers to review |
| App stores / plugin directories | Ratings matter for AI recommendations |

## Prompt Clusters to Monitor

Customize these for your business. These are high-commercial-intent prompt categories where your brand should appear in AI responses:

### General
- "best [your product category]"
- "best [your category] for beginners"
- "cheapest [your category]"
- "[your category] comparison"

### Feature-Specific
- "best [your category] with [key feature]"
- "[your category] that supports [capability]"

### Use-Case Specific
- "best [your category] for [industry/niche]"
- "[your category] for [specific scenario]"

### Migration/Switching
- "[competitor] alternative"
- "switch from [competitor]"
- "[competitor A] vs [competitor B]"

### Pricing
- "[your category] pricing comparison"
- "[your category] free trial"

## Updating This File

Run `/research-ai-citations [topic]` to generate a prompt-specific audit. The output will include which sources AI actually cites for that topic cluster, and whether your brand appears. Use findings to update the tables above.

Review quarterly: directories change, new listicles rank, and AI citation patterns shift.

```

## File: context/cro-best-practices.md

Excerpt: first 120 of 397 lines.

```markdown
# CRO Best Practices for Landing Pages

Conversion Rate Optimization guidelines for landing pages.

---

## Above-the-Fold Rules

### The 5-Second Test
Visitors should understand these within 5 seconds of landing:
1. **What** you offer
2. **Who** it's for
3. **Why** they should care
4. **What** to do next (CTA)

### Required Elements
| Element | Purpose | Guidelines |
|---------|---------|------------|
| Headline | Grab attention | Benefit-focused, <70 chars |
| Subheadline | Clarify value | Expand on headline, 1-2 sentences |
| CTA Button | Drive action | High contrast, action verb |
| Trust Signal | Build credibility | Customer count, rating, or logo |

### Above-the-Fold Don'ts
- No sliders or carousels
- No multiple competing CTAs
- No walls of text
- No autoplay videos with sound
- No navigation that distracts from CTA

---

## Headline Best Practices

### Headline Formulas That Convert

**Problem-Solution:**
- "Stop [Pain Point]. Start [Desired Outcome]."
- "No More [Problem]. Just [Solution]."

**Benefit-First:**
- "[Achieve Outcome] Without [Sacrifice]"
- "The [Fastest/Easiest/Only] Way to [Outcome]"

**Social Proof:**
- "Join [Number] [Audience] Who [Achieved Outcome]"
- "Why [Number] [Audience] Switched to [Product]"

**Question:**
- "Ready to [Achieve Outcome]?"
- "What if You Could [Desired Outcome]?"

### Headline Testing Checklist
- [ ] Contains the primary benefit
- [ ] Under 70 characters (mobile-friendly)
- [ ] Uses "you" or implies the reader
- [ ] Specific (not vague or generic)
- [ ] Creates curiosity or urgency

### Weak Headlines to Avoid
- "Welcome to [Company]"
- "The Best [Product] Solution"
- "Everything You Need"
- "We Help You [Generic Verb]"
- Starting with "Our" or "We"

---

## CTA Best Practices

### CTA Text Guidelines

**By Conversion Goal:**

| Goal | Strong CTAs | Avoid |
|------|-------------|-------|
| Trial | "Start Your Free Trial" | "Sign Up" |
| Trial | "Try Free for 14 Days" | "Submit" |
| Trial | "Get Started Free" | "Register" |
| Demo | "Book Your Demo" | "Contact Us" |
| Demo | "Schedule a Call" | "Get in Touch" |
| Demo | "See It in Action" | "Learn More" |
| Lead | "Download the Free Guide" | "Submit" |
| Lead | "Get Instant Access" | "Subscribe" |
| Lead | "Claim Your Copy" | "Send" |

### CTA Button Formula
**[Action Verb] + [Benefit/Object] + [Urgency (optional)]**

Examples:
- "Start" + "Your Free Trial" + "→"
- "Get" + "Instant Access" + "Now"
- "Book" + "Your Demo" + "Today"

### CTA Placement Strategy
1. **Hero CTA** (0-20% of page): Primary, most prominent
2. **Post-Problem CTA** (30-40%): After establishing pain
3. **Post-Proof CTA** (60-70%): After testimonials
4. **Closing CTA** (90-100%): Final push with risk reversal

### CTA Visual Best Practices
- **Color**: High contrast with background
- **Size**: Large enough to tap (44x44px minimum)
- **Whitespace**: Breathing room around button
- **Consistency**: Same style throughout page
- **Mobile**: Full-width on small screens

---

## Trust Signal Hierarchy

### Strongest (Use First)
1. **Specific Results**: "Grew audience by 300%"
2. **Named Testimonials**: "Sarah M., The Creative Hour"
3. **Customer Count with Context**: "50,000+ customers"

### Strong
4. **Star Ratings**: "4.9/5 on G2"
5. **Media Logos**: "As seen in..."
6. **Customer Logos**: Enterprise/recognizable brands
```

