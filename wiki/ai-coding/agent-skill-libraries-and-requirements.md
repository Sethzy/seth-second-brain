---
type: wiki_article
title: Agent Skill Libraries And Requirements
updated_at: 2026-07-28
status: draft
source_count: 44
tags:
  - skills
  - requirements
  - legal
  - claude
  - coding-agents
  - codex-skills
  - website-cloning
  - watchlist
---

# Agent Skill Libraries And Requirements

> Sources: forrestchang README, 2026-06-10 capture; Anthropic Claude for Legal README, 2026-06-10 capture; Nurijanian X post, 2026-05-15; AI Engineering From Scratch, 2026-06-10 capture; Seth pasted bundle, 2026-06-10; Sunil Pai X post, 2026-04-18; Shabnam Parveen X post, 2026-04-19; Agency Agents README, 2026-06-11 capture; refreshed Agency Agents repository snapshot, 2026-06-19 capture; Composio Awesome Codex Skills README, 2026-06-11 capture; Matt Pocock Skills README, 2026-06-11 capture; Seth pasted provider/voice/screen bundle, 2026-06-11; iruletheworldmo Anthropic coding agents X post, 2026-04-19; Nick Spisak Karpathy second-brain X Article, 2026-04-04; Farza Karpathy wiki skill X post, 2026-04-05; Farza Karpathy LLM wiki skill gist, 2026-06-11 capture; Eric Siu AI Marketing Skills README, 2026-06-11 capture; Corey Haines marketingskills repository snapshot, 2026-06-19 capture; AgriciDaniel Claude SEO README, 2026-06-11 capture; refreshed AgriciDaniel Claude SEO repository snapshot, 2026-06-19 capture; TheCraigHewitt SEO Machine repository snapshot, 2026-06-19 capture; Eric Siu revenue skills X post, 2026-03-28; Zach Lloyd X Article, 2026-06-11; EveryInc Compound Engineering README, 2026-06-12 capture; obra Superpowers README, 2026-06-12 capture; Karpathy spec-driven development X post, 2026-01-26; David Breunig spec-only library article, 2026-01-08; LangChain Deep Agents overview, 2026-06-12 capture
> Raw: [andrej-karpathy-skills README](../../raw/intentional/web/2026-06-10-andrej-karpathy-skills-readme.md); [Claude for Legal README](../../raw/intentional/web/2026-06-10-claude-for-legal-readme.md); [Nurijanian requirements X post](../../raw/intentional/x/2055333397611077881-nurijanian-my-favorite-ways-to-write-requirements-with-ai-1-grill-me-by-mattpocockuk-https.md); [AI Engineering From Scratch](../../raw/intentional/web/2026-06-10-ai-engineering-from-scratch.md); [HTML artifact skills legal agents bundle](../../raw/intentional/pasted/2026-06-10-html-artifact-skills-legal-agents-and-workflow-tools-bundle.md); [Sunil Pai AI Engineer Europe watchlist X post](../../raw/intentional/x/2045578175426560448-threepointone-you-should-watch-these-2-talks-from-ai-engineer-europe-from-the-vienna-schoo.md); [Shabnam Parveen Anthropic coding agents talk X post](../../raw/intentional/x/2045832146636644628-shabnam-774-head-of-anthropic-coding-agents-just-dropped-a-30-minute-talk-that-will-teach.md); [Agency Agents README](../../raw/intentional/web/2026-06-11-agency-agents-readme.md); [Agency Agents repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-msitarzewski-agency-agents-repository-snapshot-june-2026.md); [Awesome Codex Skills README](../../raw/intentional/web/2026-06-11-awesome-codex-skills-readme.md); [Matt Pocock Skills README](../../raw/intentional/web/2026-06-11-matt-pocock-skills-readme.md); [provider voice screen agents skills and website revamp bundle](../../raw/intentional/pasted/2026-06-11-provider-voice-screen-agents-skills-and-website-revamp-bundle.md); [iruletheworldmo Anthropic coding agents watchlist X post](../../raw/intentional/x/2045804022506852435-iruletheworldmo-a-masterclass-in-coding-agents-from-the-head-of-anthropic-there-s-still-a.md); [Nick Spisak Karpathy second-brain X Article](../../raw/intentional/x/2040448463540830705-nickspisak-how-to-build-your-second-brain-karpathy-dropped-a-post-describing-how-he-uses-a.md); [Farza Karpathy wiki skill X post](../../raw/intentional/x/2040591013648244963-farzatv-karpathy-also-i-ll-here-s-the-skill-i-made-for-the-wiki-if-you-wanna-try-yourself.md); [Farza Karpathy LLM wiki skill gist](../../raw/intentional/web/2026-06-11-farza-karpathy-llm-wiki-skill-gist.md); [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md); [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md); [AgriciDaniel Claude SEO README](../../raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md); [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md); [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md); [Eric Siu revenue skills X post](../../raw/intentional/x/2038039084195807570-ericosiu-open-sourced-our-skills-that-help-grow-revenues-actual-workflows-scripts-scoring.md); [Zach Lloyd spec-driven development X Article](../../raw/intentional/x/2065154860337508577-zachlloydtweets-three-skills-you-need-for-spec-driven-development-if-you-want-to-increase.md); [EveryInc Compound Engineering Plugin README](../../raw/intentional/web/2026-06-12-everyinc-compound-engineering-plugin-readme.md); [obra Superpowers README](../../raw/intentional/web/2026-06-12-obra-superpowers-readme.md); [Karpathy spec-driven development X post](../../raw/intentional/x/2015887154132746653-karpathy-airesearch12-spec-driven-development-it-s-the-limit-of-imperative-gt-declarative.md); [David Breunig spec-only library article](../../raw/intentional/web/2026-06-12-dbreunig-a-software-library-with-no-code.md); [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md)
> Source addendum: JCodesMore ai-website-cloner-template repository snapshot, 2026-06-28 capture; Garry Tan / GBrain "Thin Harness, Fat Skills"; Nicolas Bustamante/Fintool "Lessons from Building AI Agents for Financial Services"; Nicolas Bustamante "LLMs Eat Scaffolding for Breakfast."
> Raw addendum: [JCodesMore ai-website-cloner-template repository snapshot](../../raw/intentional/web/2026-06-28-jcodesmore-ai-website-cloner-template-repository-snapshot-complete.md); [Garry Tan GBrain Thin Harness Fat Skills](../../raw/intentional/web/2026-07-03-garry-tan-gbrain-thin-harness-fat-skills.md); [Fintool lessons from building AI agents](../../raw/intentional/pasted/sunder-sync-2026-06-11/224-nicbustamante-fintool-lessons-building-ai-agents-full.md); [Nicolas Bustamante LLMs Eat Scaffolding For Breakfast](../../raw/intentional/web/2026-07-03-nicolas-bustamante-llms-eat-scaffolding-for-breakfast.md)
> 2026-07-26 addendum: [Jakub Krehel Better skills](../../raw/intentional/x/2080683435153117488-jakubkrehel-i-ve-added-4-new-skills-to-the-better-collection-better-accessibility-finds-ac.md); [Jakub Antalik transitions skill](../../raw/intentional/x/2081036752924352811-jakubantalik-collection-of-33-production-ready-ui-transitions-available-as-css-react-code.md); [Peter Yang no-AI-slop skill](../../raw/intentional/x/2079943830024188105-petergyang-i-m-sick-of-reading-ai-slop-so-today-i-m-open-sourcing-my-no-ai-slop-skill-that.md); [Voxyz skill-versus-sessions audit](../../raw/intentional/x/2080731238554628421-voxyz-ai-compare-a-skill-with-how-you-actually-work-fill-in-skill-path-to-the-skill-md-or.md); [Meng To Three.js game skills](../../raw/intentional/x/2080915786206789733-mengto-i-m-open-sourcing-my-three-js-game-dev-skills-build-an-isometric-action-rpg-with-ca.md)
> 2026-07-28 addendum: [Eric Provencher orchestration-skill post](../../raw/intentional/x/2081351210557145217-pvncher-i-put-the-skill-guidance-from-this-article-together-here-for-anyone-struggling-to.md); [linked orchestrate skill](../../raw/intentional/web/2026-07-28-provencher-codex-orchestrate-skill.md)

## Overview

This cluster is about improving agent behavior through reusable skill libraries, better requirement-shaping prompts, and domain-specific packs. The most actionable lead is `andrej-karpathy-skills`, which packages Karpathy-style guidance into a `CLAUDE.md` file: surface assumptions, manage confusion, avoid overbuilt abstractions, protect user changes, and ask clarifying questions when needed.

The Nurijanian post points to requirement-writing workflows such as `/grill-me` and `/shaping`: using AI to pressure-test requirements before implementation. Claude for Legal is the domain-pack version of the same pattern: reference agents, skills, and data connectors for legal workflows, available as Claude Cowork/Code plugins or Managed Agents API deployments.

Zach Lloyd's spec-driven development article gives the requirements lane a concrete skill chain: use `/write-product-spec` to create a user-facing `PRODUCT.md`, use `/write-tech-spec` to create an implementation-strategy `TECH.md` in the same `specs/<issue>` directory, implement against both, then run `/validate-changes-match-specs` plus computer-use UX validation for visual/desktop flows. The important pattern is that specs are markdown files checked into the implementation PR, so teammates and agents can review the contract together.

Karpathy and David Breunig add the extreme case: a requirement artifact can sometimes become the library. Karpathy frames spec-driven development as fully declarative development. Breunig's `whenwords` repo ships no implementation, only a spec, language-agnostic tests, and install instructions that tell a coding agent to generate the local implementation and run tests. This is not a replacement for serious dependency engineering, but it is a strong example of requirements and tests becoming portable executable intent.

Seth's current high-trust AI-coding trio is Matt Pocock Skills, EveryInc Compound Engineering, and obra Superpowers. Matt Pocock is the lightweight engineering-fundamentals pack: grill requirements, build shared language, use TDD, diagnose systematically, and improve architecture. Compound Engineering is the compounding-work loop: strategy, ideation, brainstorm, plan, work, debug, multi-agent review, product pulse, and compound notes so each engineering unit makes later work easier. Superpowers is the stricter methodology layer: automatic skill checks, brainstorming before code, approved design, worktrees, tiny implementation tasks, true red/green TDD, subagent-driven development, two-stage review, and verification before completion.

The AI Engineer transcript batch upgrades earlier watchlist leads into source evidence. Matt Pocock's talks give the detailed workflow behind `grill-me`, PRDs, vertical slices, TDD, shared language, and deep-module design. Anthropic's skills talk frames skills as progressively disclosed folders of procedural knowledge, scripts, assets, and dependencies that can be versioned, tested, evaluated, and shared across an organization. Kiro's spec-driven-development talk adds the stronger requirements lane: structured natural-language requirements, acceptance criteria, property-based tests, requirement verification, and spec artifacts that can be customized with mocks, test cases, and MCP-sourced context.

LangChain's Deep Agents overview adds a framework-native version of the same skill idea: reusable skills can supply specialized workflows, domain knowledge, and custom instructions inside a broader harness. The distinction is useful: skills are not the whole agent system; they are one loadable context/expertise layer alongside tools, MCP, filesystem state, memory, permissions, human approval, and subagents.

Garry Tan's GBrain note sharpens this into the "thin harness, fat skills" design rule. The harness should run the loop, load context, read and write files, and enforce safety, while reusable skills carry procedure, judgment, examples, output shape, and domain context. The durable asset is not a giant always-on instruction file or a custom runtime; it is the business procedure made explicit enough that the model can call it like a method with task-specific parameters.

Fintool's agent-building notes add the enterprise product version: skills are powerful because non-engineers can read, edit, audit, and own them without a full deploy cycle. They can be private, shared, or public, discovered lazily instead of all mounted at once, and paired with evals when the workflow matters. A good business skill should encode the SOP, source-of-truth map, rubric, examples, approval rules, failure modes, and success criteria.

Nicolas Bustamante's "LLMs Eat Scaffolding for Breakfast" is the cleanup warning. Some scaffolding is real product work today but obsolete tomorrow as the model absorbs PDF parsing, structured output, reasoning patterns, or retrieval shortcuts. Skill libraries should therefore be easy to shorten, delete, and replace. The compounding advantage is not brittle glue; it is the organization's domain context, source systems, evals, workflow taste, and ability to revise the procedure quickly.

Anthropic's Claude Code steering article is now the clearest official routing rule for where instructions belong. Root `CLAUDE.md` is high-context-cost global project memory, subdirectory `CLAUDE.md` is local convention memory, rules are constraints, skills are procedural workflows loaded on demand, subagents isolate heavy side tasks, hooks are deterministic lifecycle automation, output styles change the assistant role, and appended system prompts are invocation-scoped add-ons. The Vox audit prompt turns that table into an actionable cleanup loop: inventory every rule, skill, hook, and subagent; decide which mechanism fits; show the migration plan; move the instructions; validate the real paths; and confirm always-on context is not burning tokens unnecessarily.

Jakub Krehel's `make-interfaces-feel-better` skill is a small but useful example of a narrow taste/procedure skill. It does not try to become a design system; it loads when the task is UI polish and focuses the agent on typography, hover states, optical alignment, concentric border radius, shadows, micro-interactions, font smoothing, tabular numbers, and image outlines. The sdrzn "20-line markdown" post is only a link lead, but it reinforces the same pattern as Karpathy's minimal prompts: a short well-shaped instruction file can carry a surprising amount of behavior if it routes the model to the right habits.

JCodesMore's `ai-website-cloner-template` is the strongest captured lead for a local `clone-website` skill. It is not just a prompt; it is a Next.js 16, React 19, shadcn, and Tailwind v4 scaffold with `.claude/skills/clone-website/SKILL.md` as the source of truth, a generated `.codex/skills/clone-website/SKILL.md`, and synchronized command/instruction surfaces for GitHub Copilot, Cursor, Windsurf, Gemini, OpenCode, Augment, Continue, Amazon Q, and Aider. The workflow requires browser automation, desktop/mobile screenshots, computed-style extraction, asset download, behavior sweeps, page topology, per-component spec files, parallel builders in worktrees, build checks, and visual QA diffs. For Seth, the reusable idea is a permission-gated Codex/browser skill for rebuilding owned or permitted sites from evidence, not a generic page generator or a license to clone deceptive copies.

The newer skill-library captures split into two useful lanes. Composio's Awesome Codex Skills is a broad catalog of Codex skill bundles, including productivity, collaboration, data, app connections, and engineering workflows. Agency Agents is a role library: many prebuilt specialist agents that can be installed or adapted across Claude Code, Codex, Cursor, OpenClaw, and other tools. The refreshed June 2026 Agency Agents snapshot preserves commit `93f3c5f81837cb784e225c3cebe5c3620d7d3cd4`, the complete tracked file tree, README, division registry, and install/convert scripts. Its useful retrieval shape is "232 specialized agents across 16 divisions," with selection flags such as `--division`, `--agent`, and `--agents-file`; that matters because the repo itself warns some runtimes have agent-count limits and because Seth should mine narrow role contracts rather than drop the whole library into global context.

Eric Siu's AI Marketing Skills repo adds a domain-specific operations lane: skills can include scripts, scoring rubrics, automation pipelines, telemetry, and team workflows for sales and marketing, not just prose instructions. His X post frames the pack as actual workflows for resurrecting deals, expert-panel content, visitor-to-pipeline conversion, autonomous marketing experiments, and finance-ops recovery. The repo is worth mining selectively for repeated GTM tasks, but not installing wholesale into global context.

AgriciDaniel's Claude SEO repo is the strongest captured example of a specialist marketing skill pack. It packages a `/seo` command surface, 25 sub-skills, 18 specialist agents, Google-aligned methodology, parallel site audits, schema/content/technical/local/e-commerce/international/GEO workflows, drift monitoring, and falsifiable recommendations. The refreshed June 2026 repository snapshot shows the surrounding plugin architecture too: marketplace metadata, plugin manifest, command docs, architecture docs, MCP extensions, hooks, tests, and per-domain skills. It also points to a Codex SEO port, which is the likely better fit if Seth wants this inside Codex rather than Claude Code.

SEO Machine is the workspace-style counterpart to Claude SEO's plugin-style pack. It organizes a Claude Code project around commands, specialist agents, context files, data-source modules, output folders, and WordPress publishing. For skill-library design, its key contribution is not one skill file; it is the whole repo as a reusable content machine where brand voice, target keywords, competitor context, CRO heuristics, and publishing integrations are first-class context.

Corey Haines' `marketingskills` repo is the broad cross-agent marketing pack. It follows the Agent Skills spec, installs through `npx skills`, SkillKit, or Claude plugin marketplace, and centers every downstream marketing task on a reusable `.agents/product-marketing.md` context file. Its important contribution is coverage and routing: 45 skills across product marketing, SEO/AEO, content, copy, CRO, analytics, ads, lifecycle, RevOps, social, video, pricing, offers, launch, referrals, and sales enablement, plus eval JSON files and a registry of marketing APIs, MCPs, CLIs, and integration guides. For Seth, it is a better source of reusable marketing workflow contracts than a thing to dump into global context wholesale.

Nick Spisak and Farza add a knowledge-base-specific skill lane: a skill can scaffold and operate a Karpathy-style LLM wiki with raw entries, compiled wiki pages, query commands, cleanup, backlinks, and health checks. This is directly relevant to Seth Second Brain, but should be adapted carefully because this repo already has a stronger trust-lane split between immutable raw captures, staging, compiled wiki pages, source-map provenance, and append-only logs.

The watchlist posts should not be treated as source evidence for the talks themselves yet, but they identify recurring agentic-coding study items: the AI Engineer Europe "Vienna school of agentic coding" talks and Anthropic coding-agents talks that multiple people flagged as high-signal.

## Key Ideas

- Skills are best when they encode recurring procedures or judgment patterns, not vague preferences.
- "Thin harness, fat skills" means the generic runtime should stay narrow while procedures, rubrics, examples, and domain judgment live in explicit skills.
- A skill is strongest when it behaves like a method call: reusable process plus task-specific parameters, not an all-purpose prompt blob.
- Business skills should be editable and auditable by the domain team when possible; requiring a code deploy for every SOP tweak slows down the learning loop.
- Skill routing matters. A useful skill that the resolver never selects is effectively invisible, so trigger conditions and negative examples are part of the asset.
- As models improve, delete scaffolding that the model has absorbed. Keep deterministic tools, source-of-truth systems, evals, and human review gates; avoid preserving glue because it used to be necessary.
- Requirement skills should force sharper inputs: scope, constraints, acceptance criteria, edge cases, unknowns, and tradeoffs.
- Spec-driven development should split "what" from "how": product specs capture user behavior, mocks/screenshots, stories, and product invariants; tech specs capture architecture, code locations, constraints, and implementation strategy.
- For tiny, well-bounded utilities, a `SPEC.md` plus language-agnostic tests can be a distributable agent-era artifact; for complex foundations, reference implementations and community bug-fixing still matter.
- Validation skills are a separate artifact from implementation skills. Ask an agent to compare the PR against the checked-in specs and report inconsistencies before relying on the change.
- Strong spec workflows should let external context enter before implementation: MCP/documentation/task-tracker context can improve requirements, design, mocks, test cases, and task lists.
- Skills should be treated like software when they become important: version them, test/evaluate them, track dependencies, and retire obsolete ones.
- In a full harness such as Deep Agents, skills sit beside tools, memory, filesystem context, permissions, and subagents; they should not become a dumping ground for every concern.
- Instruction-routing matters: always-on project memory, path-scoped rules, procedural skills, deterministic hooks, isolated subagents, output styles, and appended prompts have different context cost and authority.
- A cleanup pass over `CLAUDE.md`/`AGENTS.md` should move rarely used procedures into skills, deterministic behavior into hooks, heavy investigations into subagents, and path-specific constraints into scoped rules.
- UI-polish skills are best when they encode concrete taste checks rather than vague "make it better" preferences.
- Website-cloning skills should be extraction-first: browser automation, screenshots, computed styles, real assets, interaction sweeps, component specs, build checks, and visual QA before declaring done.
- Cross-agent skill packs need a canonical source plus sync scripts. `ai-website-cloner-template` keeps the clone workflow in `.claude/skills/clone-website/SKILL.md` and regenerates Codex, Copilot, Cursor, Windsurf, Gemini, OpenCode, Augment, Continue, and Amazon Q surfaces from it.
- A local website-cloner skill should include allowed-use checks: owned sites, migration/recovery/learning, or explicit permission; exclude phishing, impersonation, passing off another brand's design, and terms-of-service-violating scraping.
- Seth's default coding-skill stack should treat Matt Pocock as the compact engineering-principles layer, Compound Engineering as the compounding planning/review/learning loop, and Superpowers as the stricter autonomous implementation/TDD/review methodology.
- Compound Engineering's most reusable idea is that planning, review, and knowledge capture are the compounding surface: brainstorms sharpen plans, plans shrink execution, reviews catch patterns, and compound notes prevent rediscovery.
- Superpowers' most reusable idea is mandatory process over ad hoc prompting: brainstorm, approve design, create a worktree, write bite-sized tasks, use red/green TDD, run subagent review, and verify before declaring completion.
- A good `CLAUDE.md`/`AGENTS.md` should act as a router to relevant skills and rules, not a giant context dump.
- Domain packs such as Claude for Legal suggest a future where high-stakes workflows are distributed as curated skills, agents, and connectors.
- Broad business-domain packs need a context spine. `marketingskills` uses product-marketing context as the shared memory so channel skills inherit the same product, ICP, positioning, customer language, proof, and goals.
- AI Engineering From Scratch is a curriculum lead for deeper technical grounding: build from math and primitives before relying on frameworks.
- Broad skill catalogs are useful for discovery, but Seth should only install skills that map to repeated workflows, have clear trigger conditions, and do not bloat global context.
- Engineering skills worth trying first are requirement grilling, shared-language docs, TDD, diagnosis/debugging, code review, and CI/review-comment loops.
- Knowledge-base skills are worth trying when they preserve provenance: ingest should save raw evidence, absorb should compile meaningfully into wiki pages, query should be read-only by default, and cleanup should flag contradictions instead of silently rewriting history.
- Role-agent libraries are best treated as templates to borrow from, not automatic delegation truth. Each agent needs a narrow contract, expected output, and verification gate.
- Large role-agent catalogs need a selection layer before installation. Agency Agents' own installer supports division/agent filters; use those filters to trial a small set of roles before adding any library-wide surface to Codex or Claude.
- Domain skill packs can encode real business workflows: expert-panel scoring, pipeline routing, deal resurrection, ICP learning, content operations, conversion audits, and deck generation.
- Specialist skills should bring their own acceptance tests and evidence model. Claude SEO's useful pattern is not just "audit SEO"; it is commands, sub-skills, agents, source-grounded checks, scores, dependency relationships, and falsifiability criteria.
- Workspace-style skill packs can be just as valuable as installable plugins when the workflow depends on local project state, context folders, output directories, and publishing hooks.
- Watchlist-only posts belong in the queue until the actual video/transcript/article is captured.

## Skills Need Behavioral Evidence

The July 26 batch adds a useful quality loop: compare what a skill says to what the agent actually did across real sessions. A skill is not validated because its prose is polished. It should change observable behavior on representative tasks without adding more context, rigidity, or failure modes than it removes.

This suggests four evaluation layers:

1. **Capability:** can the skill reliably enable the target result, such as accessible layouts, coherent transitions, non-generic writing, or a playable Three.js vertical slice?
2. **Selection:** does the agent load the skill only when relevant?
3. **Transfer:** does it work across projects rather than only the original demo?
4. **Regression:** do session traces and golden tasks show improvement against the no-skill baseline?

The Better collection, UI-transition packages, no-AI-slop writing rules, and game-development skills are different domains but the same product pattern: specialized craft becomes an inspectable, testable instruction-and-tool bundle.

Eric Provencher's `orchestrate` skill is a compact coordination example: keep the parent agent available to the user, delegate narrow and distinct work, prevent overlapping ownership and recursive delegation, use lower reasoning effort for read-only scouts, and retain approvals with the user. Its usefulness depends on scope; automatic multi-agent delegation for every non-trivial task can add coordination cost when the work is not genuinely parallel.

## Open Questions

- Which parts of `andrej-karpathy-skills` should be adapted into Seth's `AGENTS.md` versus kept as a separate skill?
- Should "write requirements" become a reusable Second Brain workflow before any large app/build task?
- Should Seth adapt Warp's common-skills spec chain into a local Codex workflow: `specs/<issue>/PRODUCT.md`, `TECH.md`, implementation, spec-match validation, and screenshot/computer-use validation?
- Should Seth install Superpowers and Compound Engineering in Codex as first-class coding workflows, or mine their best practices into local Second Brain skills first?
- How should Matt Pocock, Compound Engineering, and Superpowers be routed to avoid overlap: lightweight requirement/TDD work, compounding project loops, and strict autonomous implementation respectively?
- Which legal workflows matter enough to evaluate Claude for Legal: contract review, privacy, AI governance, or employment?
- Which Codex productivity skills should be installed first: meeting notes/actions, issue triage, Notion capture, app connections, or spreadsheet/report workflows?
- Which Agency Agents roles are worth adapting into Seth's setup first via a narrow `--division` or `--agent` trial: frontend, code review, technical writing, GTM, research, operations, security, or testing?
- Should Farza's `wiki` skill be forked into a Seth-specific skill, or should its best ideas be merged into the existing `seth-second-brain`/`karpathy-llm-wiki` skills?
- Which Eric Siu marketing skill should be adapted first as a local Codex/Claude workflow: Sales Pipeline, Outbound Engine, Autoresearch, Deck Generator, or Revenue Intelligence?
- Which Corey Haines `marketingskills` subset should Seth trial first as a local workflow pack: product-marketing, AI SEO/content strategy, CRO/copywriting, analytics, RevOps, or marketing-plan?
- Should Seth install/evaluate Codex SEO rather than Claude SEO so the SEO workflow lives in the same Codex skill/plugin surface as the rest of this repo?
- Should the AI Engineer Europe and Anthropic coding-agents talks be captured as full transcripts before being compiled into agentic-engineering claims?
- Should Seth port `ai-website-cloner-template` into a local Codex `clone-website` skill using Browser/Chrome/Playwright inspection, screenshot comparison, and explicit allowed-use checks?

## Sources

- [andrej-karpathy-skills README](../../raw/intentional/web/2026-06-10-andrej-karpathy-skills-readme.md)
- [Claude for Legal README](../../raw/intentional/web/2026-06-10-claude-for-legal-readme.md)
- [Nurijanian requirements X post](../../raw/intentional/x/2055333397611077881-nurijanian-my-favorite-ways-to-write-requirements-with-ai-1-grill-me-by-mattpocockuk-https.md)
- [AI Engineering From Scratch](../../raw/intentional/web/2026-06-10-ai-engineering-from-scratch.md)
- [HTML artifact skills legal agents bundle](../../raw/intentional/pasted/2026-06-10-html-artifact-skills-legal-agents-and-workflow-tools-bundle.md)
- [Sunil Pai AI Engineer Europe watchlist X post](../../raw/intentional/x/2045578175426560448-threepointone-you-should-watch-these-2-talks-from-ai-engineer-europe-from-the-vienna-schoo.md)
- [Shabnam Parveen Anthropic coding agents talk X post](../../raw/intentional/x/2045832146636644628-shabnam-774-head-of-anthropic-coding-agents-just-dropped-a-30-minute-talk-that-will-teach.md)
- [Agency Agents README](../../raw/intentional/web/2026-06-11-agency-agents-readme.md)
- [Agency Agents repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-msitarzewski-agency-agents-repository-snapshot-june-2026.md)
- [Awesome Codex Skills README](../../raw/intentional/web/2026-06-11-awesome-codex-skills-readme.md)
- [Matt Pocock Skills README](../../raw/intentional/web/2026-06-11-matt-pocock-skills-readme.md)
- [Provider voice screen agents skills and website revamp bundle](../../raw/intentional/pasted/2026-06-11-provider-voice-screen-agents-skills-and-website-revamp-bundle.md)
- [iruletheworldmo Anthropic coding agents watchlist X post](../../raw/intentional/x/2045804022506852435-iruletheworldmo-a-masterclass-in-coding-agents-from-the-head-of-anthropic-there-s-still-a.md)
- [Nick Spisak Karpathy second-brain X Article](../../raw/intentional/x/2040448463540830705-nickspisak-how-to-build-your-second-brain-karpathy-dropped-a-post-describing-how-he-uses-a.md)
- [Farza Karpathy wiki skill X post](../../raw/intentional/x/2040591013648244963-farzatv-karpathy-also-i-ll-here-s-the-skill-i-made-for-the-wiki-if-you-wanna-try-yourself.md)
- [Farza Karpathy LLM wiki skill gist](../../raw/intentional/web/2026-06-11-farza-karpathy-llm-wiki-skill-gist.md)
- [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md)
- [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md)
- [AgriciDaniel Claude SEO README](../../raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md)
- [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md)
- [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md)
- [Eric Siu revenue skills X post](../../raw/intentional/x/2038039084195807570-ericosiu-open-sourced-our-skills-that-help-grow-revenues-actual-workflows-scripts-scoring.md)
- [Zach Lloyd spec-driven development X Article](../../raw/intentional/x/2065154860337508577-zachlloydtweets-three-skills-you-need-for-spec-driven-development-if-you-want-to-increase.md)
- [EveryInc Compound Engineering Plugin README](../../raw/intentional/web/2026-06-12-everyinc-compound-engineering-plugin-readme.md)
- [obra Superpowers README](../../raw/intentional/web/2026-06-12-obra-superpowers-readme.md)
- [Karpathy spec-driven development X post](../../raw/intentional/x/2015887154132746653-karpathy-airesearch12-spec-driven-development-it-s-the-limit-of-imperative-gt-declarative.md)
- [David Breunig spec-only library article](../../raw/intentional/web/2026-06-12-dbreunig-a-software-library-with-no-code.md)
- [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md)
- [Anthropic Steering Claude Code Skills Hooks Rules Subagents](../../raw/intentional/web/2026-06-25-anthropic-steering-claude-code-skills-hooks-rules-subagents.md)
- [Voxyz Claude Code setup audit prompt X post](../../raw/intentional/x/2068813763248324753-voxyz-ai-the-article-shows-the-tradeoffs-you-can-use-this-prompt-to-audit-your-config-fast.md)
- [Jakub Krehel Make Interfaces Feel Better Skill](../../raw/intentional/web/2026-06-25-jakub-krehel-make-interfaces-feel-better-skill.md)
- [sdrzn 20-line markdown prompt lead X post](../../raw/intentional/x/2068808565389959345-sdrzn-honestly-impressive-this-20-line-markdown-file-has-45k-stars-on-github-shows-how-muc.md)
- [JCodesMore ai-website-cloner-template repository snapshot](../../raw/intentional/web/2026-06-28-jcodesmore-ai-website-cloner-template-repository-snapshot-complete.md)

## See Also

- [Agentic Engineering Practices](agentic-engineering-practices.md)
- [AI Engineering Talks On Agentic Coding](ai-engineering-talks-on-agentic-coding.md)
- [Agent Goals And Dynamic Workflows](../personal-systems/agent-goals-and-dynamic-workflows.md)
