---
title: Vendor Agentic Engineering Blogs, Last Six Months
status: active
updated: 2026-06-14
---

# Vendor Agentic Engineering Blogs, Last Six Months

> Window: 2025-12-14 through 2026-06-14.
> Raw manifest: [Vendor Blog Six-Month Sweep Manifest](../../raw/intentional/pasted/2026-06-14-vendor-blog-six-month-sweep-manifest.md).
> Scope: OpenAI Developers Blog, Claude Blog, and Cursor Blog only. Captures are extracted Markdown snapshots with original URLs and dates preserved.

## Executive Read

The last six months of official vendor writing strongly supports the idea that serious AI coding is becoming a full software-development loop, not a prompt trick. The strongest posts are about harnesses, skills, context, evals, review, sandboxing, long-running agents, cloud environments, and enterprise rollout. That is exactly the distinction Seth wants to make: not lazy vibe coding, but an AI-native engineering workflow where the human shapes requirements, the agent executes bounded work, and the system verifies behavior with tests, traces, diffs, screenshots, review, and production controls.

The three vendor blogs converge on the same operating model:

- OpenAI emphasizes Codex as a long-horizon engineering worker, skills as packaged expertise, evals for agent skills, and multimodal/front-end/product-building workflows.
- Claude emphasizes Claude Code as an engineering workbench with skills, dynamic workflows, subagents, routines, session management, MCP, managed agents, and enterprise/security patterns.
- Cursor emphasizes the agent harness itself: context discovery, long-running agents, Bugbot review/autofix, cloud agents, sandboxes, model/harness co-design, CursorBench, and enterprise SDLC rollout.

## What This Adds To Seth’s Narrative

These sources make the state-of-art story more concrete:

- Agentic engineering is an SDLC: discover context, write a plan/spec, execute through agents, inspect diffs, run tests, use browser/computer verification where relevant, invite adversarial review, and ship behind safety controls.
- The scarce skill is no longer typing every line by hand. The scarce skill is shaping the problem, selecting the harness/tooling, providing source-grounded context, choosing verification loops, and knowing when the agent output is unsafe or low quality.
- The best current teams are building loops around agents: harness changes are measured, review agents produce fixes, cloud agents run in controlled environments, skills package repeatable expertise, and MCP/connectors expose systems safely.
- This is credible language for Sunder: Seth was not claiming traditional senior full-stack authorship; he was operating as an AI-native product engineer/founder who used agents to convert customer discovery into working workflow software.

## Highest-Signal Reading List

### Openai - High Signal

- **2026-03-09 - Using skills to accelerate OSS maintenance | OpenAI Developers** ([raw](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md), [source](https://developers.openai.com/blog/skills-agents-sdk/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-02-11 - Shell + Skills + Compaction: Tips for long-running agents that do real work | OpenAI Developers** ([raw](../../raw/intentional/web/2026-02-11-openai-shell-skills-compaction-tips-for-long-running-agents-that-do-real-work-o.md), [source](https://developers.openai.com/blog/skills-shell-tips/))
  - Why it matters: Long-running task design: delegation, context retention, checkpoints, and human review.
- **2026-02-04 - 15 lessons learned building ChatGPT Apps | OpenAI Developers** ([raw](../../raw/intentional/web/2026-02-04-openai-15-lessons-learned-building-chatgpt-apps-openai-developers.md), [source](https://developers.openai.com/blog/15-lessons-building-chatgpt-apps/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-22 - Testing Agent Skills Systematically with Evals | OpenAI Developers** ([raw](../../raw/intentional/web/2026-06-13-testing-agent-skills-systematically-with-evals.md), [source](https://developers.openai.com/blog/eval-skills/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-01-11 - Supercharging Codex with JetBrains MCP at Skyscanner | OpenAI Developers** ([raw](../../raw/intentional/web/2026-01-11-openai-supercharging-codex-with-jetbrains-mcp-at-skyscanner-openai-developers.md), [source](https://developers.openai.com/blog/skyscanner-codex-jetbrains-mcp/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.

### Claude - High Signal

- **2026-06-10 - The evolution of agentic surfaces: building with Claude Managed Agents** ([raw](../../raw/intentional/web/2026-06-10-claude-the-evolution-of-agentic-surfaces-building-with-claude-managed-agents.md), [source](https://claude.com/blog/building-with-claude-managed-agents/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-06-09 - New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults** ([raw](../../raw/intentional/web/2026-06-09-claude-new-in-claude-managed-agents-run-agents-on-a-schedule-and-store-environm.md), [source](https://claude.com/blog/whats-new-in-claude-managed-agents/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-06-08 - Observability for developers building connectors** ([raw](../../raw/intentional/web/2026-06-08-claude-observability-for-developers-building-connectors.md), [source](https://claude.com/blog/observability-for-developers-building-connectors/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code** ([raw](../../raw/intentional/web/2026-06-05-claude-how-one-anthropic-seller-rebuilt-his-team-s-workflows-with-claude-code.md), [source](https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-06-03 - Running an AI-native engineering org** ([raw](../../raw/intentional/web/2026-06-03-claude-running-an-ai-native-engineering-org.md), [source](https://claude.com/blog/running-an-ai-native-engineering-org/))
  - Why it matters: State-of-the-market framing for how software engineering is changing.
- **2026-06-03 - Lessons from building Claude Code: How we use skills** ([raw](../../raw/intentional/web/2026-06-03-claude-lessons-from-building-claude-code-how-we-use-skills.md), [source](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-06-03 - Best practices for getting started with Claude Cowork** ([raw](../../raw/intentional/web/2026-06-03-claude-best-practices-for-getting-started-with-claude-cowork.md), [source](https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork/))
  - Why it matters: Practical workflow guidance for agentic coding discipline.
- **2026-06-02 - A harness for every task: dynamic workflows in Claude Code** ([raw](../../raw/intentional/web/2026-06-02-claude-a-harness-for-every-task-dynamic-workflows-in-claude-code.md), [source](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/))
  - Why it matters: Harness engineering: context, tools, instrumentation, and iteration around the model.
- **2026-05-28 - Introducing dynamic workflows in Claude Code** ([raw](../../raw/intentional/web/2026-05-28-claude-introducing-dynamic-workflows-in-claude-code.md), [source](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-27 - Zero Trust for AI agents** ([raw](../../raw/intentional/web/2026-05-27-claude-zero-trust-for-ai-agents.md), [source](https://claude.com/blog/zero-trust-for-ai-agents/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-05-21 - Claude now works with more security and compliance tools** ([raw](../../raw/intentional/web/2026-05-21-claude-claude-now-works-with-more-security-and-compliance-tools.md), [source](https://claude.com/blog/compliance-api-security-partners/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-05-20 - Using Claude Code: The unreasonable effectiveness of HTML** ([raw](../../raw/intentional/web/2026-05-20-claude-using-claude-code-the-unreasonable-effectiveness-of-html.md), [source](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-19 - New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels** ([raw](../../raw/intentional/web/2026-05-19-claude-new-in-claude-managed-agents-self-hosted-sandboxes-and-mcp-tunnels.md), [source](https://claude.com/blog/claude-managed-agents-updates/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-05-15 - Deploying Claude across the legal industry** ([raw](../../raw/intentional/web/2026-05-15-claude-deploying-claude-across-the-legal-industry.md), [source](https://claude.com/blog/deploying-claude-across-the-legal-industry/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-14 - How Claude Code works in large codebases: Best practices and where to start** ([raw](../../raw/intentional/web/2026-05-14-claude-how-claude-code-works-in-large-codebases-best-practices-and-where-to-sta.md), [source](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start/))
  - Why it matters: Context engineering: discover, index, retrieve, and preserve codebase facts.
- **2026-05-12 - How Anthropic's cybersecurity team built a threat detection platform with Claude Code** ([raw](../../raw/intentional/web/2026-05-12-claude-how-anthropic-s-cybersecurity-team-built-a-threat-detection-platform-wit.md), [source](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-05-12 - Claude for the legal industry** ([raw](../../raw/intentional/web/2026-05-12-claude-claude-for-the-legal-industry.md), [source](https://claude.com/blog/claude-for-the-legal-industry/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-11 - Agent view in Claude Code** ([raw](../../raw/intentional/web/2026-05-11-claude-agent-view-in-claude-code.md), [source](https://claude.com/blog/agent-view-in-claude-code/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks** ([raw](../../raw/intentional/web/2026-05-01-claude-how-a-non-technical-project-manager-built-and-shipped-a-stress-managemen.md), [source](https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-30 - Lessons from building Claude Code: Prompt caching is everything** ([raw](../../raw/intentional/web/2026-04-30-claude-lessons-from-building-claude-code-prompt-caching-is-everything.md), [source](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-30 - Claude Security is now in public beta** ([raw](../../raw/intentional/web/2026-04-30-claude-claude-security-is-now-in-public-beta.md), [source](https://claude.com/blog/claude-security-public-beta/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-04-30 - Building AI agents for the enterprise** ([raw](../../raw/intentional/web/2026-04-30-claude-building-ai-agents-for-the-enterprise.md), [source](https://claude.com/blog/building-ai-agents-for-the-enterprise/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-29 - Product development in the agentic era** ([raw](../../raw/intentional/web/2026-04-29-claude-product-development-in-the-agentic-era.md), [source](https://claude.com/blog/product-development-in-the-agentic-era/))
  - Why it matters: State-of-the-market framing for how software engineering is changing.
- **2026-04-29 - Deploying agentic AI across the enterprise with Claude Cowork** ([raw](../../raw/intentional/web/2026-04-29-claude-deploying-agentic-ai-across-the-enterprise-with-claude-cowork.md), [source](https://claude.com/blog/new-guide-deploying-claude-across-the-enterprise-with-claude-cowork/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-29 - Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp** ([raw](../../raw/intentional/web/2026-04-29-claude-claude-api-skill-now-in-coderabbit-jetbrains-resolve-ai-and-warp.md), [source](https://claude.com/blog/claude-api-skill/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-04-28 - Onboarding Claude Code like a new developer: Lessons from 17 years of development** ([raw](../../raw/intentional/web/2026-04-28-claude-onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-dev.md), [source](https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-22 - Building agents that reach production systems with MCP** ([raw](../../raw/intentional/web/2026-04-22-claude-building-agents-that-reach-production-systems-with-mcp.md), [source](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon** ([raw](../../raw/intentional/web/2026-04-20-claude-meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon.md), [source](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-16 - Best practices for using Claude Opus 4.7 with Claude Code** ([raw](../../raw/intentional/web/2026-04-16-claude-best-practices-for-using-claude-opus-4-7-with-claude-code.md), [source](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code/))
  - Why it matters: Practical workflow guidance for agentic coding discipline.
- **2026-04-15 - Using Claude Code: session management and 1M context** ([raw](../../raw/intentional/web/2026-04-15-claude-using-claude-code-session-management-and-1m-context.md), [source](https://claude.com/blog/using-claude-code-session-management-and-1m-context/))
  - Why it matters: Context engineering: discover, index, retrieve, and preserve codebase facts.
- **2026-04-14 - Redesigning Claude Code on desktop for parallel agents** ([raw](../../raw/intentional/web/2026-04-14-claude-redesigning-claude-code-on-desktop-for-parallel-agents.md), [source](https://claude.com/blog/claude-code-desktop-redesign/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-10 - Seeing like an agent: how we design tools in Claude Code** ([raw](../../raw/intentional/web/2026-04-10-claude-seeing-like-an-agent-how-we-design-tools-in-claude-code.md), [source](https://claude.com/blog/seeing-like-an-agent/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-08 - Claude Managed Agents: get to production 10x faster** ([raw](../../raw/intentional/web/2026-04-08-claude-claude-managed-agents-get-to-production-10x-faster.md), [source](https://claude.com/blog/claude-managed-agents/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor** ([raw](../../raw/intentional/web/2026-04-08-claude-how-carta-healthcare-gets-ai-to-reason-like-a-clinical-abstractor.md), [source](https://claude.com/blog/carta-healthcare-clinical-abstractor/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-07 - How and when to use subagents in Claude Code** ([raw](../../raw/intentional/web/2026-04-07-claude-how-and-when-to-use-subagents-in-claude-code.md), [source](https://claude.com/blog/subagents-in-claude-code/))
  - Why it matters: Multi-agent decomposition: split work by role, context, and verification surface.
- **2026-04-02 - Harnessing Claude’s intelligence** ([raw](../../raw/intentional/web/2026-04-02-claude-harnessing-claude-s-intelligence.md), [source](https://claude.com/blog/harnessing-claudes-intelligence/))
  - Why it matters: Harness engineering: context, tools, instrumentation, and iteration around the model.
- **2026-03-24 - Auto mode for Claude Code** ([raw](../../raw/intentional/web/2026-03-24-claude-auto-mode-for-claude-code.md), [source](https://claude.com/blog/auto-mode/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-19 - Product management on the AI exponential** ([raw](../../raw/intentional/web/2026-03-19-claude-product-management-on-the-ai-exponential.md), [source](https://claude.com/blog/product-management-on-the-ai-exponential/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-11 - Advancing Claude for Excel and PowerPoint** ([raw](../../raw/intentional/web/2026-03-11-claude-advancing-claude-for-excel-and-powerpoint.md), [source](https://claude.com/blog/claude-excel-powerpoint-updates/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-09 - Bringing Code Review to Claude Code** ([raw](../../raw/intentional/web/2026-03-09-claude-bringing-code-review-to-claude-code.md), [source](https://claude.com/blog/code-review/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-03-05 - Common workflow patterns for AI agents—and when to use them** ([raw](../../raw/intentional/web/2026-03-05-claude-common-workflow-patterns-for-ai-agents-and-when-to-use-them.md), [source](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-03 - Improving skill-creator: Test, measure, and refine Agent Skills** ([raw](../../raw/intentional/web/2026-03-03-claude-improving-skill-creator-test-measure-and-refine-agent-skills.md), [source](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-02-24 - Cowork and plugins for finance** ([raw](../../raw/intentional/web/2026-02-24-claude-cowork-and-plugins-for-finance.md), [source](https://claude.com/blog/cowork-plugins-finance/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-02-24 - Cowork and plugins for teams across the enterprise** ([raw](../../raw/intentional/web/2026-02-24-claude-cowork-and-plugins-for-teams-across-the-enterprise.md), [source](https://claude.com/blog/cowork-plugins-across-enterprise/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-02-20 - Bringing automated preview, review, and merge to Claude Code on desktop** ([raw](../../raw/intentional/web/2026-02-20-claude-bringing-automated-preview-review-and-merge-to-claude-code-on-desktop.md), [source](https://claude.com/blog/preview-review-and-merge-with-claude-code/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-01-30 - Customize Cowork with plugins** ([raw](../../raw/intentional/web/2026-01-30-claude-customize-cowork-with-plugins.md), [source](https://claude.com/blog/cowork-plugins/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-01-29 - Understand Claude Code’s impact with contribution metrics** ([raw](../../raw/intentional/web/2026-01-29-claude-understand-claude-code-s-impact-with-contribution-metrics.md), [source](https://claude.com/blog/contribution-metrics/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-29 - A complete guide to building skills for Claude** ([raw](../../raw/intentional/web/2026-01-29-claude-a-complete-guide-to-building-skills-for-claude.md), [source](https://claude.com/blog/complete-guide-to-building-skills-for-claude/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2026-01-26 - Your favorite work tools are now interactive connectors inside Claude** ([raw](../../raw/intentional/web/2026-01-26-claude-your-favorite-work-tools-are-now-interactive-connectors-inside-claude.md), [source](https://claude.com/blog/interactive-tools-in-claude/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-01-26 - How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code** ([raw](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md), [source](https://claude.com/blog/how-anthropic-uses-claude-marketing/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-22 - Building agents with Skills: Equipping agents for specialized work** ([raw](../../raw/intentional/web/2026-01-22-claude-building-agents-with-skills-equipping-agents-for-specialized-work.md), [source](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2025-12-19 - Extending Claude’s capabilities with skills and MCP servers** ([raw](../../raw/intentional/web/2025-12-19-claude-extending-claude-s-capabilities-with-skills-and-mcp-servers.md), [source](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.
- **2025-12-18 - Skills for organizations, partners, the ecosystem** ([raw](../../raw/intentional/web/2025-12-18-claude-skills-for-organizations-partners-the-ecosystem.md), [source](https://claude.com/blog/organization-skills-and-directory/))
  - Why it matters: Skills as reusable agent capability packs: instructions, scripts, domain knowledge, and tests.

### Cursor - High Signal

- **2026-06-03 - Introducing organizations for Cursor Enterprise** ([raw](../../raw/intentional/web/2026-06-03-cursor-introducing-organizations-for-cursor-enterprise.md), [source](https://cursor.com/blog/organizations/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-06-02 - What we’ve learned building cloud agents** ([raw](../../raw/intentional/web/2026-06-02-cursor-what-we-ve-learned-building-cloud-agents.md), [source](https://cursor.com/blog/cloud-agent-lessons/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-05-26 - Faire doubles PR throughput with Cursor Cloud Agents** ([raw](../../raw/intentional/web/2026-05-26-cursor-faire-doubles-pr-throughput-with-cursor-cloud-agents.md), [source](https://cursor.com/blog/faire/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-05-22 - Cursor named a Leader in the 2026 Gartner® Magic Quadrant™ for Enterprise AI Coding Agents** ([raw](../../raw/intentional/web/2026-05-22-cursor-cursor-named-a-leader-in-the-2026-gartner-magic-quadrant-for-enterprise.md), [source](https://cursor.com/blog/cursor-leads-gartner-mq-2026/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-18 - Introducing Composer 2.5** ([raw](../../raw/intentional/web/2026-05-18-cursor-introducing-composer-2-5.md), [source](https://cursor.com/blog/composer-2-5/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-05-13 - Development environments for your cloud agents** ([raw](../../raw/intentional/web/2026-05-13-cursor-development-environments-for-your-cloud-agents.md), [source](https://cursor.com/blog/cloud-agent-development-environments/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-05-11 - Beyond efficiency: PayPal expands what's possible to build with AI** ([raw](../../raw/intentional/web/2026-05-11-cursor-beyond-efficiency-paypal-expands-what-s-possible-to-build-with-ai.md), [source](https://cursor.com/blog/paypal/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-05-11 - Updates to Bugbot for Teams and Individuals** ([raw](../../raw/intentional/web/2026-05-11-cursor-updates-to-bugbot-for-teams-and-individuals.md), [source](https://cursor.com/blog/may-2026-bugbot-changes/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-05-06 - Bootstrapping Composer with autoinstall** ([raw](../../raw/intentional/web/2026-05-06-cursor-bootstrapping-composer-with-autoinstall.md), [source](https://cursor.com/blog/bootstrapping-composer-with-autoinstall/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-04-30 - Continually improving our agent harness** ([raw](../../raw/intentional/web/2026-04-30-cursor-continually-improving-our-agent-harness.md), [source](https://cursor.com/blog/continually-improving-agent-harness/))
  - Why it matters: Harness engineering: context, tools, instrumentation, and iteration around the model.
- **2026-04-29 - Build programmatic agents with the Cursor SDK** ([raw](../../raw/intentional/web/2026-04-29-cursor-build-programmatic-agents-with-the-cursor-sdk.md), [source](https://cursor.com/blog/typescript-sdk/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-23 - National Australia Bank accelerates legacy migrations with Cursor** ([raw](../../raw/intentional/web/2026-04-23-cursor-national-australia-bank-accelerates-legacy-migrations-with-cursor.md), [source](https://cursor.com/blog/nab/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-21 - Cursor partners with SpaceX on model training** ([raw](../../raw/intentional/web/2026-04-21-cursor-cursor-partners-with-spacex-on-model-training.md), [source](https://cursor.com/blog/spacex-model-training/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-21 - Keeping the Cursor app stable** ([raw](../../raw/intentional/web/2026-04-21-cursor-keeping-the-cursor-app-stable.md), [source](https://cursor.com/blog/app-stability/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-15 - Interact with agent-created visualizations in canvases** ([raw](../../raw/intentional/web/2026-04-15-cursor-interact-with-agent-created-visualizations-in-canvases.md), [source](https://cursor.com/blog/canvas/))
  - Why it matters: Frontend/browser verification loop: design input, visual inspection, screenshots, and iteration.
- **2026-04-15 - Better AI models enable more ambitious work** ([raw](../../raw/intentional/web/2026-04-15-cursor-better-ai-models-enable-more-ambitious-work.md), [source](https://cursor.com/blog/better-models-ambitious-work/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-15 - Amplitude ships 3x more production code with Cursor** ([raw](../../raw/intentional/web/2026-04-15-cursor-amplitude-ships-3x-more-production-code-with-cursor.md), [source](https://cursor.com/blog/amplitude/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-14 - Speeding up GPU kernels by 38% with a multi-agent system** ([raw](../../raw/intentional/web/2026-04-14-cursor-speeding-up-gpu-kernels-by-38-with-a-multi-agent-system.md), [source](https://cursor.com/blog/multi-agent-kernels/))
  - Why it matters: Multi-agent decomposition: split work by role, context, and verification surface.
- **2026-04-08 - Bugbot now self-improves with learned rules** ([raw](../../raw/intentional/web/2026-04-08-cursor-bugbot-now-self-improves-with-learned-rules.md), [source](https://cursor.com/blog/bugbot-learning/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-04-06 - Better MoE model inference with warp decode** ([raw](../../raw/intentional/web/2026-04-06-cursor-better-moe-model-inference-with-warp-decode.md), [source](https://cursor.com/blog/warp-decode/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-04-02 - Meet the new Cursor** ([raw](../../raw/intentional/web/2026-04-02-cursor-meet-the-new-cursor.md), [source](https://cursor.com/blog/cursor-3/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-27 - A technical report on Composer 2** ([raw](../../raw/intentional/web/2026-03-27-cursor-a-technical-report-on-composer-2.md), [source](https://cursor.com/blog/composer-2-technical-report/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-03-26 - Improving Composer through real-time RL** ([raw](../../raw/intentional/web/2026-03-26-cursor-improving-composer-through-real-time-rl.md), [source](https://cursor.com/blog/real-time-rl-for-composer/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-03-25 - Run cloud agents in your own infrastructure** ([raw](../../raw/intentional/web/2026-03-25-cursor-run-cloud-agents-in-your-own-infrastructure.md), [source](https://cursor.com/blog/self-hosted-cloud-agents/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-03-23 - Fast regex search: indexing text for agent tools** ([raw](../../raw/intentional/web/2026-03-23-cursor-fast-regex-search-indexing-text-for-agent-tools.md), [source](https://cursor.com/blog/fast-regex-search/))
  - Why it matters: Context engineering: discover, index, retrieve, and preserve codebase facts.
- **2026-03-19 - Introducing Composer 2** ([raw](../../raw/intentional/web/2026-03-19-cursor-introducing-composer-2.md), [source](https://cursor.com/blog/composer-2/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-03-18 - Money Forward brings Cursor’s coding agents to product, design, and QA** ([raw](../../raw/intentional/web/2026-03-18-cursor-money-forward-brings-cursor-s-coding-agents-to-product-design-and-qa.md), [source](https://cursor.com/blog/money-forward/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-17 - Training Composer for longer horizons** ([raw](../../raw/intentional/web/2026-03-17-cursor-training-composer-for-longer-horizons.md), [source](https://cursor.com/blog/self-summarization/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-03-16 - Securing our codebase with autonomous agents** ([raw](../../raw/intentional/web/2026-03-16-cursor-securing-our-codebase-with-autonomous-agents.md), [source](https://cursor.com/blog/security-agents/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-11 - Over 30 new plugins join the Cursor Marketplace** ([raw](../../raw/intentional/web/2026-03-11-cursor-over-30-new-plugins-join-the-cursor-marketplace.md), [source](https://cursor.com/blog/new-plugins/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-03-11 - How we compare model quality in Cursor** ([raw](../../raw/intentional/web/2026-03-11-cursor-how-we-compare-model-quality-in-cursor.md), [source](https://cursor.com/blog/cursorbench/))
  - Why it matters: Verification/eval loop: measure agent behavior instead of trusting demos.
- **2026-03-05 - Build agents that run automatically** ([raw](../../raw/intentional/web/2026-03-05-cursor-build-agents-that-run-automatically.md), [source](https://cursor.com/blog/automations/))
  - Why it matters: Background/cloud agent operations: schedules, environments, vaults, and async execution.
- **2026-03-04 - Cursor is now available in JetBrains IDEs** ([raw](../../raw/intentional/web/2026-03-04-cursor-cursor-is-now-available-in-jetbrains-ides.md), [source](https://cursor.com/blog/jetbrains-acp/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-03 - How technical support at Cursor uses Cursor** ([raw](../../raw/intentional/web/2026-03-03-cursor-how-technical-support-at-cursor-uses-cursor.md), [source](https://cursor.com/blog/cursor-support/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-03-02 - PlanetScale protects production reliability with Bugbot** ([raw](../../raw/intentional/web/2026-03-02-cursor-planetscale-protects-production-reliability-with-bugbot.md), [source](https://cursor.com/blog/planetscale/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-02-26 - The third era of AI software development** ([raw](../../raw/intentional/web/2026-02-26-cursor-the-third-era-of-ai-software-development.md), [source](https://cursor.com/blog/third-era/))
  - Why it matters: State-of-the-market framing for how software engineering is changing.
- **2026-02-26 - Closing the code review loop with Bugbot Autofix** ([raw](../../raw/intentional/web/2026-02-26-cursor-closing-the-code-review-loop-with-bugbot-autofix.md), [source](https://cursor.com/blog/bugbot-autofix/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-02-24 - Cursor agents can now control their own computers** ([raw](../../raw/intentional/web/2026-02-24-cursor-cursor-agents-can-now-control-their-own-computers.md), [source](https://cursor.com/blog/agent-computer-use/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-02-18 - Implementing a secure sandbox for local agents** ([raw](../../raw/intentional/web/2026-02-18-cursor-implementing-a-secure-sandbox-for-local-agents.md), [source](https://cursor.com/blog/agent-sandboxing/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-02-17 - How Stripe rolled out a consistent Cursor experience for 3,000 engineers** ([raw](../../raw/intentional/web/2026-02-17-cursor-how-stripe-rolled-out-a-consistent-cursor-experience-for-3-000-engineers.md), [source](https://cursor.com/blog/stripe/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-02-17 - Extend Cursor with plugins** ([raw](../../raw/intentional/web/2026-02-17-cursor-extend-cursor-with-plugins.md), [source](https://cursor.com/blog/marketplace/))
  - Why it matters: Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- **2026-02-13 - Box chooses Cursor for enterprise-grade quality, security, and control** ([raw](../../raw/intentional/web/2026-02-13-cursor-box-chooses-cursor-for-enterprise-grade-quality-security-and-control.md), [source](https://cursor.com/blog/box/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-02-12 - Expanding our long-running agents research preview** ([raw](../../raw/intentional/web/2026-02-12-cursor-expanding-our-long-running-agents-research-preview.md), [source](https://cursor.com/blog/long-running-agents/))
  - Why it matters: Long-running task design: delegation, context retention, checkpoints, and human review.
- **2026-02-11 - Increased usage for agents** ([raw](../../raw/intentional/web/2026-02-11-cursor-increased-usage-for-agents.md), [source](https://cursor.com/blog/increased-agent-usage/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-02-09 - Introducing Composer 1.5** ([raw](../../raw/intentional/web/2026-02-09-cursor-introducing-composer-1-5.md), [source](https://cursor.com/blog/composer-1-5/))
  - Why it matters: Model/product co-design: model behavior, harness, and UX evolve together.
- **2026-02-06 - NVIDIA commits 3x more code across 30,000 developers with Cursor** ([raw](../../raw/intentional/web/2026-02-06-cursor-nvidia-commits-3x-more-code-across-30-000-developers-with-cursor.md), [source](https://cursor.com/blog/nvidia/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-02-05 - Towards self-driving codebases** ([raw](../../raw/intentional/web/2026-02-05-cursor-towards-self-driving-codebases.md), [source](https://cursor.com/blog/self-driving-codebases/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-27 - Securely indexing large codebases** ([raw](../../raw/intentional/web/2026-01-27-cursor-securely-indexing-large-codebases.md), [source](https://cursor.com/blog/secure-codebase-indexing/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2026-01-26 - Dropbox uses Cursor to index over 550,000 files and build an AI-native SDLC** ([raw](../../raw/intentional/web/2026-01-26-cursor-dropbox-uses-cursor-to-index-over-550-000-files-and-build-an-ai-native-s.md), [source](https://cursor.com/blog/dropbox/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-21 - Salesforce accelerates velocity by over 30% and ships higher-quality code with Cursor** ([raw](../../raw/intentional/web/2026-01-21-cursor-salesforce-accelerates-velocity-by-over-30-and-ships-higher-quality-code.md), [source](https://cursor.com/blog/salesforce/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- **2026-01-15 - Building a better Bugbot** ([raw](../../raw/intentional/web/2026-01-15-cursor-building-a-better-bugbot.md), [source](https://cursor.com/blog/building-bugbot/))
  - Why it matters: Review loop: agent finds, explains, fixes, and learns from defects.
- **2026-01-14 - Scaling long-running autonomous coding** ([raw](../../raw/intentional/web/2026-01-14-cursor-scaling-long-running-autonomous-coding.md), [source](https://cursor.com/blog/scaling-agents/))
  - Why it matters: Long-running task design: delegation, context retention, checkpoints, and human review.
- **2026-01-09 - Best practices for coding with agents** ([raw](../../raw/intentional/web/2026-01-09-cursor-best-practices-for-coding-with-agents.md), [source](https://cursor.com/blog/agent-best-practices/))
  - Why it matters: Practical workflow guidance for agentic coding discipline.
- **2026-01-06 - Dynamic context discovery** ([raw](../../raw/intentional/web/2026-01-06-cursor-dynamic-context-discovery.md), [source](https://cursor.com/blog/dynamic-context-discovery/))
  - Why it matters: Context engineering: discover, index, retrieve, and preserve codebase facts.
- **2025-12-22 - Hooks for security and platform teams** ([raw](../../raw/intentional/web/2025-12-22-cursor-hooks-for-security-and-platform-teams.md), [source](https://cursor.com/blog/hooks-partners/))
  - Why it matters: Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- **2025-12-19 - Graphite is joining Cursor** ([raw](../../raw/intentional/web/2025-12-19-cursor-graphite-is-joining-cursor.md), [source](https://cursor.com/blog/graphite/))
  - Why it matters: Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.

## Useful Supporting Posts

### Openai - Supporting

- 2026-03-25 - [How Perplexity Brought Voice Search to Millions Using the Realtime API | OpenAI Developers](../../raw/intentional/web/2026-03-25-openai-how-perplexity-brought-voice-search-to-millions-using-the-realtime-api-o.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-03-20 - [Designing delightful frontends with GPT-5.4 | OpenAI Developers](../../raw/intentional/web/2026-03-20-openai-designing-delightful-frontends-with-gpt-5-4-openai-developers.md) - Frontend/browser verification loop: design input, visual inspection, screenshots, and iteration.
- 2026-03-11 - [From prompts to products: One year of Responses | OpenAI Developers](../../raw/intentional/web/2026-03-11-openai-from-prompts-to-products-one-year-of-responses-openai-developers.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-02-26 - [Building frontend UIs with Codex and Figma | OpenAI Developers](../../raw/intentional/web/2026-02-26-openai-building-frontend-uis-with-codex-and-figma-openai-developers.md) - Frontend/browser verification loop: design input, visual inspection, screenshots, and iteration.
- 2026-02-23 - [Run long horizon tasks with Codex | OpenAI Developers](../../raw/intentional/web/2026-02-23-openai-run-long-horizon-tasks-with-codex-openai-developers.md) - Long-running task design: delegation, context retention, checkpoints, and human review.
- 2025-12-30 - [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.

### Claude - Supporting

- 2026-06-05 - [The Claude Cowork product guide](../../raw/intentional/web/2026-06-05-claude-the-claude-cowork-product-guide.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-06-03 - [How Anthropic enables self-service data analytics with Claude](../../raw/intentional/web/2026-06-03-claude-how-anthropic-enables-self-service-data-analytics-with-claude.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-05-27 - [Using LLMs to secure source code](../../raw/intentional/web/2026-05-27-claude-using-llms-to-secure-source-code.md) - Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- 2026-05-21 - [How our partners are putting Opus to work for cybersecurity](../../raw/intentional/web/2026-05-21-claude-how-our-partners-are-putting-opus-to-work-for-cybersecurity.md) - Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- 2026-05-20 - [How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book](../../raw/intentional/web/2026-05-20-claude-how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-05-13 - [Best practices for computer and browser use with Claude](../../raw/intentional/web/2026-06-10-claude-best-practices-for-computer-and-browser-use-with-clau.md) - Practical workflow guidance for agentic coding discipline.
- 2026-05-11 - [Introducing the Claude Platform on AWS](../../raw/intentional/web/2026-05-11-claude-introducing-the-claude-platform-on-aws.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-05-06 - [New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](../../raw/intentional/web/2026-05-06-claude-new-in-claude-managed-agents-dreaming-outcomes-and-multiagent-orchestrat.md) - Background/cloud agent operations: schedules, environments, vaults, and async execution.
- 2026-05-05 - [Deploying Claude across financial services](../../raw/intentional/web/2026-05-05-claude-deploying-claude-across-financial-services.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-04-30 - [How Kepler built verifiable AI for financial services with Claude](../../raw/intentional/web/2026-04-30-claude-how-kepler-built-verifiable-ai-for-financial-services-with-claude.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-04-23 - [New connectors in Claude for everyday life](../../raw/intentional/web/2026-04-23-claude-new-connectors-in-claude-for-everyday-life.md) - Tooling layer: MCP/plugins/connectors turn external systems into agent-readable interfaces.
- 2026-04-23 - [Built-in memory for Claude Managed Agents](../../raw/intentional/web/2026-04-23-claude-built-in-memory-for-claude-managed-agents.md) - Background/cloud agent operations: schedules, environments, vaults, and async execution.
- 2026-04-14 - [Introducing routines in Claude Code](../../raw/intentional/web/2026-04-14-claude-introducing-routines-in-claude-code.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-04-10 - [Preparing your security program for AI-accelerated offense](../../raw/intentional/web/2026-04-10-claude-preparing-your-security-program-for-ai-accelerated-offense.md) - Production safety: sandboxing, least privilege, secure indexing, and agent controls.
- 2026-04-10 - [Multi-agent coordination patterns: Five approaches and when to use them](../../raw/intentional/web/2026-04-10-claude-multi-agent-coordination-patterns-five-approaches-and-when-to-use-them.md) - Multi-agent decomposition: split work by role, context, and verification surface.
- 2026-04-09 - [Making Claude Cowork ready for enterprise](../../raw/intentional/web/2026-04-09-claude-making-claude-cowork-ready-for-enterprise.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-03-30 - [Audit Claude Platform activity with the Compliance API](../../raw/intentional/web/2026-03-30-claude-audit-claude-platform-activity-with-the-compliance-api.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-03-23 - [Put Claude to work on your computer](../../raw/intentional/web/2026-03-23-claude-put-claude-to-work-on-your-computer.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-03-13 - [1M context is now generally available for Opus 4.6 and Sonnet 4.6](../../raw/intentional/web/2026-03-13-claude-1m-context-is-now-generally-available-for-opus-4-6-and-sonnet-4-6.md) - Context engineering: discover, index, retrieve, and preserve codebase facts.
- 2026-02-17 - [Increase web search accuracy and efficiency with dynamic filtering](../../raw/intentional/web/2026-02-17-claude-increase-web-search-accuracy-and-efficiency-with-dynamic-filtering.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-02-12 - [Claude Enterprise, now available self-serve](../../raw/intentional/web/2026-02-12-claude-claude-enterprise-now-available-self-serve.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.
- 2026-01-23 - [Building multi-agent systems: When and how to use them](../../raw/intentional/web/2026-01-23-claude-building-multi-agent-systems-when-and-how-to-use-them.md) - Multi-agent decomposition: split work by role, context, and verification surface.

### Cursor - Supporting

- 2026-06-01 - [Improvements to Teams Pricing](../../raw/intentional/web/2026-06-01-cursor-improvements-to-teams-pricing.md) - Supporting evidence for current vendor direction, enterprise adoption, or adjacent AI product workflows.

## Captured But Probably Not Central

These were captured because they were inside the requested six-month vendor window, but they are less central to Seth’s agentic-engineering proof-of-work narrative. They may still be useful for adjacent product, legal, finance, customer, security, or enterprise-adoption examples.

### Openai - Archive

- 2025-12-22 - [Updates for developers building with voice | OpenAI Developers](../../raw/intentional/web/2025-12-22-openai-updates-for-developers-building-with-voice-openai-developers.md)

### Claude - Archive

- 2026-06-08 - [Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](../../raw/intentional/web/2026-06-08-claude-building-intelligent-apps-for-apple-platforms-with-claude-in-the-foundat.md)
- 2026-05-27 - [How CodeRabbit used Claude to build an agent orchestration system](../../raw/intentional/web/2026-05-27-claude-how-coderabbit-used-claude-to-build-an-agent-orchestration-system.md)
- 2026-05-26 - [Code w/ Claude London 2026: Rethinking how we build](../../raw/intentional/web/2026-05-26-claude-code-w-claude-london-2026-rethinking-how-we-build.md)
- 2026-05-22 - [How Anthropic's finance team uses Claude to shape the narrative behind the numbers](../../raw/intentional/web/2026-05-22-claude-how-anthropic-s-finance-team-uses-claude-to-shape-the-narrative-behind-t.md)
- 2026-05-14 - [The founder's playbook: Building an AI-native startup](../../raw/intentional/web/2026-05-14-claude-the-founder-s-playbook-building-an-ai-native-startup.md)
- 2026-05-12 - [Code w/ Claude SF 2026 recap: Building on the AI exponential](../../raw/intentional/web/2026-05-12-claude-code-w-claude-sf-2026-recap-building-on-the-ai-exponential.md)
- 2026-05-07 - [Collaborate with Claude across Excel, PowerPoint, Word and Outlook](../../raw/intentional/web/2026-05-07-claude-collaborate-with-claude-across-excel-powerpoint-word-and-outlook.md)
- 2026-04-09 - [The advisor strategy: Give agents an intelligence boost](../../raw/intentional/web/2026-04-09-claude-the-advisor-strategy-give-agents-an-intelligence-boost.md)
- 2026-03-18 - [Code with Claude comes to San Francisco, London, and Tokyo](../../raw/intentional/web/2026-03-18-claude-code-with-claude-comes-to-san-francisco-london-and-tokyo.md)
- 2026-03-12 - [Claude now creates interactive charts, diagrams and visualizations](../../raw/intentional/web/2026-03-12-claude-claude-now-creates-interactive-charts-diagrams-and-visualizations.md)
- 2026-02-23 - [How AI helps break the cost barrier to COBOL modernization](../../raw/intentional/web/2026-02-23-claude-how-ai-helps-break-the-cost-barrier-to-cobol-modernization.md)
- 2026-02-09 - [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](../../raw/intentional/web/2026-02-09-claude-behind-the-model-launch-what-customers-discovered-testing-claude-opus-4.md)
- 2026-02-05 - [Advancing finance with Claude Opus 4.6](../../raw/intentional/web/2026-02-05-claude-advancing-finance-with-claude-opus-4-6.md)
- 2026-01-28 - [How leading retailers are turning AI pilots into enterprise-wide transformation](../../raw/intentional/web/2026-01-28-claude-how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transfo.md)
- 2026-01-28 - [Updates to Claude Team](../../raw/intentional/web/2026-01-28-claude-updates-to-claude-team.md)
- 2026-01-21 - [Eight trends defining how software gets built in 2026](../../raw/intentional/web/2026-01-21-claude-eight-trends-defining-how-software-gets-built-in-2026.md)

## Patterns To Reuse In Interviews

- **Spec-to-execution loop:** Claude/Codex/Cursor all now frame agent work as task contracts, not chat. Start with requirements, constraints, repo context, acceptance criteria, and verification plan.
- **Harness loop:** Treat the model as one component inside a harness: tools, context, memory, sandboxes, evals, logs, and reviewer agents determine whether it can reliably finish work.
- **Context loop:** Codebase indexing, dynamic context discovery, 1M context/session management, and MCP/connectors are now first-class engineering concerns.
- **Verification loop:** Tests, evals, Bugbot/code review, CursorBench, OpenAI skill evals, screenshots, logs, and traces are what separate production agentic engineering from vibe coding.
- **Safety loop:** Sandboxes, hooks, vaults, Zero Trust, audit APIs, secure indexing, and production-system MCP controls are part of the actual modern AI coding stack.
- **Org loop:** AI-native engineering orgs are adopting background agents, cloud agents, managed agents, and plugin/skill libraries to turn repeated workflows into shared infrastructure.

## Suggested Interview Language

The strongest concise formulation is:

> I use AI agents as part of an engineering loop, not as a replacement for judgment. I start by turning product/customer context into a scoped spec, ask a model to challenge the plan, use another agent to implement, then verify with tests, logs, browser screenshots, traces, code review, and a human diff pass. The latest vendor writing from OpenAI, Claude, and Cursor all points in this direction: the real work is harness, context, evals, review, and production controls.

## Counts

- OpenAI: 12 in-window posts selected; 11 new captures, 1 existing capture reused.
- Claude: 91 in-window posts selected; 89 new captures, 2 existing captures reused.
- Cursor: 57 in-window article posts selected after excluding topic/category pages.
- Total article posts retained: 160.

## Open Questions

- Should the career artifact cite only the highest-signal posts, or should it include a broader appendix with all 160 vendor captures?
- Should Seth maintain this vendor-blog sweep monthly so the narrative stays current?
- Which Sunder feature examples should explicitly cite each workflow pattern: context loop, frontend verification loop, eval/QA loop, database/RLS loop, adversarial review loop, and product-spec loop?
