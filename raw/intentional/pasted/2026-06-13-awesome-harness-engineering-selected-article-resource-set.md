---
type: raw_capture
source_type: pasted
title: "Awesome Harness Engineering selected article resource set"
url: "https://github.com/walkinglabs/awesome-harness-engineering#selected-article-resource-set"
collected_at: 2026-06-13T10:49:02Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Awesome Harness Engineering selected article resource set

Source: https://github.com/walkinglabs/awesome-harness-engineering#selected-article-resource-set

## Capture Text

# Awesome Harness Engineering selected article/resource set

Source repository: https://github.com/walkinglabs/awesome-harness-engineering
Repository HEAD inspected: f84f1701974cf1ad67dd774b025b33e613275cee
Selected from attachment: /Users/sethlim/.codex/attachments/1477824e-b26a-4cb9-8933-b7dc0d103e9a/pasted-text.txt
Captured at: 2026-06-13T10:49:02Z

## Selected Entries

- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) - A project-based course repository on making Codex and Claude Code more reliable, centered on an Electron personal knowledge base app with lecture handouts, example artifacts, and practical harness projects.
- [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) - OpenAI's flagship field report on building a large application with Codex using architectural constraints, repo-local instructions, browser validation, and telemetry.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - Anthropic's core article on initializer agents, feature lists, init.sh, self-verification, and handoff artifacts across many context windows.
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) - Anthropic follow-up focused on improving long-running app generation with better task state and evaluator design.
- [The Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) - LangChain's concise framing of an agent as model plus harness, with prompts, tools, middleware, orchestration, and runtime infrastructure.
- [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) - Thoughtworks' framing of harness work into context engineering, architectural constraints, and "garbage collection" against entropy.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) - Anthropic's broader guide to workflows, agents, tools, and when structured systems outperform raw prompting.
- [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) - A practical argument that weak results from coding agents are often harness problems rather than model problems.
- [Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework) - Inngest's case for treating state, retries, traces, and concurrency as first-class infrastructure.
- [Greenfield AI, Brownfield AI, and the Vibecode You Just Inherited](https://sawinyh.com/blog/greenfield-vs-brownfield-ai-codebases) - A three-way taxonomy of codebases agents encounter — agent-native greenfield, true legacy brownfield, and recently-vibecoded inheritance — with playbooks for installing layered CLAUDE.md rules, ratcheted pre-commit hooks, baselined lint violations, and feature-folder refactors so the codebase itself stops being the harness bottleneck.
- [Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime](https://www.preprints.org/manuscript/202603.1756) - A position paper that treats the harness layer as a first-class research object, proposes the control–agency–runtime (CAR) decomposition, and introduces HarnessCard for structured reporting of harness design and evaluation.
- [Many Hands Engineering](https://github.com/mseeks/many-hands-engineering/blob/main/many-hands-engineering.pdf) - A handbook framing the layer above the per-agent harness: how multiple harnessed agents share a commons, where decisions belong on a planned / emergent spectrum, and how human stewardship operates at a different cadence than agent execution. Treats harness engineering as a critical layer of "terrain" the framework sits on top of.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Anthropic's guidance on managing the context window as a working memory budget rather than a dumping ground.
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) - Manus' detailed playbook on KV-cache locality, tool masking, filesystem memory, and keeping useful failures in-context.
- [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) - Thoughtworks guidance on shaping the task environment so coding agents can stay grounded and productive.
- [Advanced Context Engineering for Coding Agents](https://www.humanlayer.dev/blog/advanced-context-engineering) - HumanLayer patterns for reducing context drift and making coding sessions easier to resume.
- [Context-Efficient Backpressure for Coding Agents](https://www.humanlayer.dev/blog/context-efficient-backpressure) - HumanLayer's ideas for preventing agents from burning context on noisy or low-value work.
- [OpenHands Context Condensensation for More Efficient AI Agents](https://openhands.dev/blog/openhands-context-condensensation-for-more-efficient-ai-agents) - OpenHands' design for bounded conversation memory that preserves goals, progress, critical files, and failing tests while keeping long-running coding sessions efficient.
- [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md) - A practical guide to creating durable, repo-local instructions that agents can repeatedly follow.
- [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing) - Anthropic on reducing approval friction without losing control through better sandboxing and policy design.
- [Code execution with MCP: building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp) - Anthropic's approach to giving agents controlled execution power through explicit, inspectable tool boundaries.
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) - Anthropic's guidance on tool interfaces that are easier for models to call correctly and safely.
- [Mitigating Prompt Injection Attacks in Software Agents](https://openhands.dev/blog/mitigating-prompt-injection-attacks-in-software-agents) - OpenHands' practical guide to confirmation mode, analyzers, sandboxing, and hard policies for reducing prompt-injection risk in autonomous coding agents.
- [Assessing internal quality while coding with an agent](https://martinfowler.com/articles/exploring-gen-ai/ccmenu-quality.html) - Thoughtworks on moving quality checks into the loop instead of relying on after-the-fact manual review.
- [Anchoring AI to a reference application](https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html) - Thoughtworks on constraining agents with concrete exemplars so they produce more consistent output.
- [Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) - A clear mental model for where humans should strengthen the harness instead of micromanaging every artifact.
- [Claude Code: Best practices for agentic coding](https://code.claude.com/docs) - Anthropic's practical recommendations for repo structure, checkpoints, validation, and delegation in agentic coding workflows.
- [Lurkr](https://github.com/agentveil-protocol/lurkr) - Static scanner that runs in CI before deploy to surface AI-agent capability risks, including shadow capabilities, credentials into LLM context, eval/subprocess in @tool, direct prompt interpolation, and unverified MCP endpoints.
- [AGENTS.md](https://github.com/agentsmd/agents.md) - A lightweight open format for repo-local instructions that tell agents how to work inside a codebase.
- [agent.md](https://github.com/agentmd/agent.md) - A related standardization effort for machine-readable agent instructions across projects and tools.
- [GitHub Spec Kit](https://github.com/github/spec-kit) - GitHub's toolkit for spec-driven development, useful when you want agents to execute against explicit product and engineering specs.
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) - Thoughtworks on why strong specs make AI-assisted software delivery more dependable.
- [12 Factor Agents](https://www.humanlayer.dev/blog/12-factor-agents) - HumanLayer's operating principles for production agents, including explicit prompts, state ownership, and clean pause-resume behavior.
- [12-Factor AgentOps](https://www.12factoragentops.com/) - An operations-oriented companion focused on context discipline, validation, and reproducible agent workflows.
- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills/) - OpenAI's concrete guide to turning agent traces into repeatable evals with JSONL logs and deterministic checks.
- [How to Evaluate Agent Skills (And Why You Should)](https://openhands.dev/blog/evaluating-agent-skills) - OpenHands' hands-on playbook for measuring whether a skill actually helps using bounded tasks, deterministic verifiers, no-skill baselines, and trace review.
- [Agent evals](https://platform.openai.com/docs/guides/agent-evals) - OpenAI's product guide for measuring agent quality with reproducible task-level and workflow-level evaluations.
- [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices) - OpenAI's general guide to building eval suites that match real-world distributions and catch regressions early.
- [Trace grading](https://platform.openai.com/docs/guides/trace-grading) - OpenAI documentation on grading agent traces directly, which is especially helpful for long multi-step tasks.
- [Inspect AI](https://inspect.aisi.org.uk/) - UK AISI's open-source evaluation framework with solver, scorer, sandboxing, tool-use, MCP, and log-viewer primitives for building reproducible agent eval harnesses.
- [OpenTelemetry Semantic Conventions for Generative AI Systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - Standard span, metric, event, and attribute conventions for instrumenting LLM and agent workflows so harness traces stay portable across observability backends.
- [AgentOps](https://github.com/AgentOps-AI/agentops) - Open-source Python SDK for agent monitoring, session replay, cost tracking, benchmarking, and tracing across common LLM and agent frameworks.
- [agenttrace](https://github.com/luoyuctl/agenttrace) - Local-first TUI/CLI for auditing AI coding-agent session traces, health gates, cost spikes, tool failures, latency gaps, and attempt-to-attempt diffs.
- [Learning to Verify AI-Generated Code](https://openhands.dev/blog/20260305-learning-to-verify-ai-generated-code) - OpenHands' overview of a layered verification stack using trajectory critics trained on production traces for reranking, early stopping, and review-time quality control.
- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) - Anthropic's guidance on what to measure when agents have many possible trajectories to success or failure.
- [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) - Anthropic on how runtime configuration can move coding benchmark scores by more than many leaderboard gaps.
- [Evaluating Deep Agents: Our Learnings](https://blog.langchain.com/evaluating-deep-agents-our-learnings/) - LangChain's practical breakdown of single-step, full-run, and multi-turn eval design for stateful agents.
- [Improving Deep Agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) - LangChain's evidence that harness changes alone can significantly improve benchmark performance.
