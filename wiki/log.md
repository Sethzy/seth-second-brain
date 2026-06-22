# Wiki Log

Append-only operation log.

## 2026-06-19 | ingest | Agency Agents repository snapshot refresh

- Captured a refreshed repository snapshot for `msitarzewski/agency-agents`, preserving repository URL, latest commit hash/date, GitHub metadata, tracked file tree, README, division registry, and install/convert scripts.
- Updated: Agent Skill Libraries And Requirements with the current Agency Agents shape: 232 specialist agents across 16 divisions, multi-tool installs, and division/agent filtering as the safe trial path.
- Updated source-map provenance for the compiled capture.

## 2026-06-19 | ingest | SEO Machine, Claude SEO refresh, and X content research agent

- Captured repository snapshots for TheCraigHewitt's SEO Machine and AgricIDaniel's refreshed Claude SEO repo, preserving repository URL, commit hash/date, file tree, and selected workflow/plugin docs.
- Captured Seth's pasted JAZII X article on a content research agent that tracks creators/keywords, extracts hook/topic/format/emotion patterns, and generates angles after market scanning.
- Updated: SEO/AEO/GEO Content Systems with SEO Machine as a content-production workspace and refreshed Claude SEO as a specialist audit/plugin architecture.
- Updated: Content Ops And Editorial Systems with SEO Machine context/command structure and the "research first, patterns second, writing third" social/editorial loop.
- Updated: Agentic Marketing Workflows with research-before-generation as a core marketing workflow principle.
- Updated: Agent Skill Libraries And Requirements with workspace-style skill packs alongside plugin-style domain packs.
- Updated source-map provenance for the compiled captures.

## 2026-06-14 | ingest | OpenAI, Claude, and Cursor vendor-blog six-month sweep

- Scraped OpenAI Developers Blog, Claude Blog, and Cursor Blog for posts published from 2025-12-14 through 2026-06-14.
- Captured extracted Markdown raw snapshots for 160 article posts after excluding Cursor topic/category pages; reused 3 existing captures for already-saved URLs.
- Created the raw sweep manifest at `raw/intentional/pasted/2026-06-14-vendor-blog-six-month-sweep-manifest.md`.
- Compiled: Vendor Agentic Engineering Blogs, Last Six Months.
- Updated source-map provenance for the new raw captures.

## 2026-06-12 | ingest | AI Engineer: Structuring a modern AI team

- Captured the YouTube transcript for "Structuring a modern AI team - Denys Linkov, Wisedocs" as complete raw evidence from English auto-captions.
- Updated: AI Engineering Talks On Agentic Coding.
- Updated: Agentic Engineering Practices.
- Updated source-map provenance for the compiled YouTube capture.

## 2026-06-12 | ingest | OpenAI codex-plugin-cc and cross-model adversarial review

- Captured the OpenAI `codex-plugin-cc` README as complete raw GitHub evidence.
- Logged the key concept: adversarial review is strongest when the checker is a different model/runtime from the maker, because same-model review can share training-distribution blind spots.
- Updated: Agentic Engineering Practices.
- Updated source-map provenance for the compiled README capture.

## 2026-06-12 | ingest | LangChain Deep Agents overview

- Captured the LangChain Deep Agents overview as complete raw web evidence.
- Used Context7 current documentation lookup for the Deep Agents package/docset before compiling.
- Updated: Agentic Engineering Practices.
- Updated: Agent Skill Libraries And Requirements.
- Updated source-map provenance for the compiled docs capture.

## 2026-06-12 | ingest | Spec-only libraries, loop engineering, and harness captures

- Captured Karpathy's spec-driven development X post and David Breunig's spec-only `whenwords` article as complete raw evidence.
- Captured complete X Articles/posts from Lance Martin, Addy Osmani, Nicholas Charrière, zodchiii, Sairahul, and Sydney Runkle on loop engineering, harness engineering, custom harnesses, Claude Code/Shopify-style infrastructure, and product convergence.
- Confirmed `systematicls/status/2028814227004395561` was already captured and compiled.
- Staged `0xCodez`, `calcsam`, and `akshay_pachaar` X URLs as incomplete because the authenticated TweetDetail capture failed with JSON parsing errors and no verbatim text was confirmed.
- Updated: Agentic Engineering Practices.
- Updated: Agent Skill Libraries And Requirements.
- Updated: AI Engineering Talks On Agentic Coding.
- Updated: Agent Goals And Dynamic Workflows.

## 2026-06-10 | init | V1 scaffold

- Created retrieval-first second-brain structure.
- Added raw, wiki, staging, qmd, and Last30Days workflow conventions.

## 2026-06-10 | ingest | First second-brain ingestion test, strict raw rerun

- Captured Seth's pasted bundle as complete raw evidence.
- Staged external web, YouTube, LinkedIn, Glassdoor, and X links as incomplete captures because full verbatim source text was not confirmed.
- Created: AI GTM Opportunity Leads.
- Created: Warm Intro Pathfinding With AI.

## 2026-06-10 | ingest | Authenticated X capture fix

- Replaced oEmbed X capture with Last30Days-inspired authenticated Bird/TweetDetail capture using Chrome Profile 3 cookies.
- Promoted the JUMPERZ `/goal` post to complete raw X evidence.
- Kept Thariq, Dominik Kundel, and Matt Van Horn X Article links in incomplete staging because TweetDetail returned article metadata/preview, not full article body.
- Created: Agent Goals And Dynamic Workflows.

## 2026-06-10 | ingest | X Article field toggles and wiki compilation

- Enabled X Article field toggles in TweetDetail capture and promoted Thariq, Dominik Kundel, and Matt Van Horn X Articles to complete raw X evidence.
- Updated: Agent Goals And Dynamic Workflows.
- Updated source-map provenance for the newly compiled X Article captures.

## 2026-06-10 | sweep | Last30Days: Fable Mythos Claude Code release

- Ran Last30Days for "Fable Mythos Claude Code release".
- Fixed the repo wrapper to pass `--save-dir` so sweep output persists under `raw/sweeps/last30days/`.
- Saved raw sweep output and staged a digest. No durable wiki pages were promoted from this sweep.

## 2026-06-10 | debug | Last30Days Serper web results

- Debugged Web: 0 behavior in Last30Days Serper backend.
- Found Serper returned fresh results with relative dates such as "22 hours ago"; the local Last30Days parser treated those dates as unparseable and filtered them out.
- Patched the local GTM Last30Days copy to parse common relative dates and reran the Fable/Mythos sweep with Web, X, and YouTube coverage.
- Staged the corrected sweep digest. No durable wiki pages were promoted.

## 2026-06-10 | ingest | Agent workflow links: goals, classifiers, browser outreach, self-improvement

- Captured exact X links for Alvin Sng classifier and VB self-improvement prompts through the authenticated X path.
- Captured complete raw snapshots for the OpenAI Cookbook Goals notebook, Claude browser-use best practices, ECC README, and Seth's pasted batch.
- Staged the Every guide as partial because the page is subscriber-gated after the preview.
- Staged the Claude YouTube video as partial because no transcript or captions were available through `yt-dlp`.
- Updated: Agent Goals And Dynamic Workflows.
- Created: Agentic Classifiers.
- Created: Browser Outreach Delegation.

## 2026-06-10 | ingest | GTM API, waterfall enrichment, and agentic engineering stack

- Captured Deepline as a complete web snapshot for agent-native GTM API and waterfall enrichment positioning.
- Captured exact X links for Alok Bishoyi autoresearch, Nicolas Bustamante personal agent stack, and sysls agentic engineering through the authenticated X path.
- Captured Seth's pasted Deepline/X note as complete raw evidence.
- Created: GTM Waterfall Enrichment APIs.
- Created: Agentic Engineering Practices.
- Created: Personal Agent Ops Stack.
- Updated: Agent Goals And Dynamic Workflows.

## 2026-06-10 | ingest | Codex maxxing, artifact surfaces, and GTM campaign bundle

- Captured Seth's attached Codex maxxing/GTM bundle as complete pasted raw evidence.
- Captured exact X links for Codex maxxing, implementation notes, business agents, Obsidian dashboard, OpenHuman, second-brain structure, and related leads through the authenticated X path.
- Captured complete web/raw snapshots for Jason Liu's Codex-maxxing article, HTML Anything README, Presenton README, and two YouTube transcripts.
- Created: Agentic GTM Campaign Workflows.
- Created: Agentic Artifact Surfaces.
- Updated: Agent Goals And Dynamic Workflows.
- Updated: Agentic Engineering Practices.
- Updated: GTM Waterfall Enrichment APIs.
- Updated: Personal Agent Ops Stack.

## 2026-06-10 | ingest | Finance workflows repo radar

- Captured exact X link for wincy.eth finance GitHub repo roundup through the authenticated X path.
- Created: Agentic Finance Workflows.

## 2026-06-10 | ingest | HTML artifacts, skill libraries, legal agents, and work surfaces

- Captured Seth's pasted bundle as complete raw evidence.
- Captured exact X links for HTML artifacts, app flow maps, Claude outcomes, PDF redesign, Hermes/agent platform leads, requirements prompts, and self-improving agents where available.
- Staged Garry Tan and Akshay Pachaar X links as partial because authenticated X capture returned malformed TweetDetail JSON.
- Captured complete web/raw snapshots for fireworks-tech-graph, andrej-karpathy-skills, clawchief, Claude for Legal, Sentry Junior, CodeRabbit Agent, Onyx docs, SimpleWords, AI Engineering From Scratch, Raycast, and Tolaria.
- Created: Agent Skill Libraries And Requirements.
- Created: Agent Platforms And Work Surfaces.
- Updated: Agentic Artifact Surfaces.
- Updated: Agent Goals And Dynamic Workflows with outcomes, dreaming, and self-improving agent loops from Lance Martin and Joao Moura.
- Added root `CLAUDE.md` with compact Karpathy-style Claude Code guidance and repo-specific Second Brain reminders.
- Updated source-map provenance for the compiled raw captures; left Sarah Fim's shortened-link-only X capture raw-only.

## 2026-06-11 | ingest | Provider swap, voice, screen artifacts, agents, skills, and website revamp leads

- Captured Seth's pasted provider/voice/screen/agents/skills/website-revamp bundle as complete raw evidence.
- Captured exact X links for xAI voice APIs, LLM Wiki, agentic-coding talks, screen recording, AI slides, GTM campaign motions, sales call intelligence, AI flyers, managed agents, and Codex website/app building.
- Captured complete web/raw snapshots for OpenScreen, Agency Agents, Composio Awesome Codex Skills, and Matt Pocock Skills.
- Staged the Instagram AI flyers link as partial because only the URL was captured, not full post text/media.
- Updated: Personal Agent Ops Stack with xAI voice provider evaluation, Cloudflare interactive voice as an experiment, and LLM Wiki as second-brain mechanics.
- Updated: Agentic Artifact Surfaces with OpenScreen, AI slides, editable AI images/flyers, and design-to-web-app loops.
- Updated: Agent Skill Libraries And Requirements with Agency Agents, Awesome Codex Skills, Matt Pocock Skills, and watchlist-only agentic-coding talks.
- Updated: Agentic GTM Campaign Workflows with six outbound campaign motions and Architect Mode-style call-intelligence loops.
- Updated: Agent Platforms And Work Surfaces with Jess Yan's managed-agent/product-role lead.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Harness engineering, company research, Scout, video workflow, and Clay MCP leads

- Captured Seth's pasted harness/Codex/company-research/video-workflow/Clay MCP bundle as complete raw evidence.
- Captured exact X links for Codex/Cowork harness design, Gooseworks GTM data access, Browserbase company research, and Scout/company brain.
- Staged the Trae AI harness-engineering X link as partial because authenticated X capture returned malformed TweetDetail JSON.
- Captured the Browserbase `company-research` skill page as complete raw web evidence.
- Captured the YouTube auto-caption transcript for "Codex Just Replaced 1,000 Hours of Video Editing Tutorials" as complete raw YouTube evidence.
- Updated: Agentic Engineering Practices with harness engineering, FastMCP wrappers, and context-provider architecture.
- Updated: GTM Waterfall Enrichment APIs with Gooseworks, Browserbase company-research skill structure, Clay MCP as a lead to verify, and provider comparison questions.
- Updated: Agentic Artifact Surfaces with a coded-video workflow and Remotion versus Hyperframes evaluation questions.
- Updated: Agent Platforms And Work Surfaces with Scout as an open-source company-brain/context-provider lead.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Acme GTM OS, company brain, agentic marketing, and design system bundle

- Captured Seth's Acme/eGiro GTM OS pasted bundle as complete raw evidence.
- Captured exact X links for company brains, proposal agents, Remotion/HyperFrames/Editframe video, Claude/Open Design, image-to-code website workflows, design resources, calculators, Cursor/Codex app surfaces, cold DM basics, and Replit slides.
- Captured complete web/raw snapshots for Actively AI, LangChain's GTM agent blog, Browserbase GTM page, Open Design README, Refero, Jiro, Aura, shadcn UI kit illustrations, Anthropic's growth marketing article, and Grainient.
- Staged Instagram and LinkedIn links as partial because full post text/media was not fetched; Seth's pasted API-tool notes remain preserved in the raw pasted bundle.
- Created: Acme Agentic GTM OS.
- Updated: Agentic Artifact Surfaces with Acme brand-machine, Open Design, Remotion/HyperFrames/Editframe, and image-to-code website workflow leads.
- Updated: Agent Platforms And Work Surfaces with company-brain/Slackbot architecture and contribution loops.
- Updated: GTM Waterfall Enrichment APIs with Acme TAM scraping, trigger monitors, provider map, Trigger.dev-style scheduled scrapers, and account-data pipe questions.
- Updated: Agentic GTM Campaign Workflows with proposal agents, per-account artifacts, and daily researched outreach cadence.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Anthropic coding agents, LinkedIn MCP outreach, and Cloudflare agent platform leads

- Captured exact X links for an Anthropic coding-agents watchlist item, Roman's Claude MCP + LinkedIn/Gojiberry outreach workflow, and Rita/Alan's Cloudflare Agents Week platform breakdown.
- Updated: Agent Skill Libraries And Requirements with the Anthropic coding-agents talk as another watchlist-only source.
- Updated: Agentic GTM Campaign Workflows with the Gojiberry LinkedIn outreach loop, including ICP, high-intent lead discovery, enrichment, personalized messages, campaign launch, and weekly optimization.
- Updated: Personal Agent Ops Stack with Cloudflare's agent infrastructure lane across Dynamic Workers, Sandboxes, durable execution, browser HITL, voice, email, AI Gateway, Mesh, and memory.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Vercel AI SDK, Slack agents, sandbox, call-summary, and lead-processing templates

- Captured Seth's pasted Vercel AI SDK sandbox agent templates batch as complete raw evidence.
- Captured complete web/raw snapshots for the Vercel Slack Agent Template README and template page, Call Summary Agent with Sandbox README and template page, and Lead Agent README plus Lead Processing Agent template page.
- Staged the av1dlive X link as partial because authenticated X capture returned malformed TweetDetail JSON.
- Created: Vercel Agent Templates And Sandboxes.
- Updated: Agent Platforms And Work Surfaces with the Vercel Slack Agent Template as an implementation skeleton for Slack-native agents.
- Updated: Agentic GTM Campaign Workflows with call-summary and inbound lead-processing reference architectures.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Browserbase bb, sandboxed internal agents, and GTM tab-work automation

- Captured exact X links for Kyle Jeong's Browserbase `bb` internal-agent architecture and Prathit Joshi's GTM agent post through the authenticated X path.
- Captured Seth's pasted note preserving "instead of Viktor.ai" and `claude --dangerously-skip-permissions` as retrieval hooks and safety context.
- Updated: Agent Platforms And Work Surfaces with Browserbase `bb` as the stronger company-OS/Slackbot baseline candidate.
- Updated: Agentic Engineering Practices with sandbox, credential-brokering proxy, scoped permissions, skill routing, and a caution that permission-skip modes belong only behind compensating controls.
- Updated: Agentic GTM Campaign Workflows with parallel GTM research threads for Reddit trends, leads, analytics, and tool-connected tab work.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Clawchief v2, Karpathy wiki skills, and coding-agent components

- Captured exact X links for Ryan Carson's Clawchief v2 update, Nick Spisak's Karpathy second-brain article, Farza's wiki-skill post, and Sebastian Raschka's coding-agent-components post through the authenticated X path.
- Captured complete web/raw snapshots for the refreshed Clawchief README, Farza's Karpathy LLM wiki skill gist, and Raschka's Components of a Coding Agent article page.
- Updated: Agent Platforms And Work Surfaces with Clawchief v2's source-of-truth files, task archive, heartbeat orchestrator, cron templates, and assistant/business-development skills.
- Updated: Personal Agent Ops Stack with the Karpathy flat-file second-brain pattern and Farza's ingest/absorb/query/cleanup skill model.
- Updated: Agent Skill Libraries And Requirements with the knowledge-base-specific skill lane and provenance cautions for adapting Farza's wiki skill.
- Updated: Agentic Engineering Practices with Raschka's coding-agent component framing: repo context, tools, memory, delegation, sandboxing, permissions, and verification.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | OpenClaw CRM assistant and AI marketing skill library

- Captured exact X link for Ryan Carson's original Clawchief/OpenClaw assistant article through the authenticated X path.
- Captured complete web/raw snapshot for Eric Siu's AI Marketing Skills README.
- Updated: Agent Platforms And Work Surfaces with the OpenClaw CRM/outreach assistant use case, tracker source of truth, cron sweeps, and validation checklist.
- Updated: Agentic GTM Campaign Workflows with AI Marketing Skills categories and trial candidates for Acme/eGiro.
- Updated: Agent Skill Libraries And Requirements with AI Marketing Skills as a domain-specific executable skill pack.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | 10xapp Core OSS productivity surface

- Captured complete web/raw snapshot for the 10xapp Core OSS README.
- Updated: Agent Platforms And Work Surfaces with Core OSS as an open-source all-in-one productivity substrate for email, calendar, AI chat/tool use, messages, files, docs, projects, workspaces, and dashboard.
- Updated source-map provenance for the compiled capture.

## 2026-06-11 | ingest | Codex Security, sandbox loop, and SEO skills

- Captured exact X link for Romain Huet's Codex Security pointer through the authenticated X path.
- Resolved the linked setup URL to OpenAI's Codex Security setup docs and captured the official setup page as raw evidence; the linked OpenAI blog URL returned 403 from terminal fetch.
- Captured complete web/raw snapshot for AgriciDaniel's Claude SEO README using a safe literal fallback because `scripts/new-raw-capture.sh` expands untrusted README text in its heredoc.
- Updated: Agentic Engineering Practices with the Codex Security scan loop: repo/branch/environment/history window, generated threat model, findings, validation output, and remediation PRs.
- Updated: Agent Skill Libraries And Requirements with Claude SEO as a specialist marketing skill pack and Codex SEO as the likely Codex-native evaluation target.
- Updated: Agentic GTM Campaign Workflows with SEO audits, GEO/citability, programmatic SEO, comparison pages, and drift monitoring as recurring GTM operations.
- Updated source-map provenance for the compiled captures.

## 2026-06-11 | ingest | Devin platform choice and Ramp Inspect background agent

- Captured exact X link for Ryan Carson's Devin/platform note through the authenticated X path.
- Captured Ramp's "Why We Built Our Own Background Agent" article from the public compiled MDX bundle; created a corrected second raw capture after the first extraction had mojibake punctuation, and marked the first capture superseded in source-map.
- Updated: Agentic Engineering Practices with Devin versus custom harness buy/build framing and Ramp Inspect's hosted sandbox architecture.
- Updated: Agent Platforms And Work Surfaces with Devin as managed code-factory platform lead and Ramp Inspect as a custom internal coding-agent surface.
- Updated source-map provenance for compiled and superseded captures.

## 2026-06-11 | ingest | smux, Codex use cases, enterprise agent diffusion, and revenue skills

- Captured ShawnPana's smux README as complete raw web evidence.
- Captured exact X links for Romain Huet's Codex use-cases post, Aaron Levie's capability-overhang article, and Eric Siu's revenue-skill post through the authenticated X path.
- Captured OpenAI's official Codex use-cases page as complete raw web evidence.
- Staged the Bloggersarvesh X link as failed/incomplete because authenticated TweetDetail returned malformed JSON.
- Updated: Agentic Engineering Practices with smux/tmux-bridge local agent orchestration and Codex use-case starter prompts as task-contract references.
- Updated: Personal Agent Ops Stack with smux as a local Claude+Codex workbench candidate.
- Updated: Agent Platforms And Work Surfaces with Levie's enterprise agent adoption, context-gap, permissioning, and diffusion framing.
- Updated: Agent Skill Libraries And Requirements and Agentic GTM Campaign Workflows with Eric Siu's revenue skill-pack framing.
- Updated source-map provenance for compiled and incomplete captures.

## 2026-06-11 | ingest | Frontend Slides HTML presentation skill

- Captured the Frontend Slides README as complete raw web evidence.
- Updated: Agentic Artifact Surfaces with Frontend Slides as a deck-specific HTML artifact skill: single-file slides, PowerPoint conversion, visual style previews, anti-generic template presets, and progressive template loading.
- Updated source-map provenance for the compiled capture.

## 2026-06-11 | ingest | Desktop Archive markdown batch

- Captured 74 markdown files from `/Users/sethlim/Desktop/Archive/` one by one as raw pasted evidence under `raw/intentional/pasted/archive-2026-06-11/`.
- Copied 22 files from `/Users/sethlim/Desktop/Archive/Attachments/` into the archive raw capture folder as an attachment backup.
- Created: Desktop Archive Saved Inputs, a one-by-one wiki digest with category, original filename, raw capture link, and retrieval summary for every note.
- Updated: Agentic Engineering Practices with archive leads for Claude Code tooling, harness engineering, evals, dogfooding, browser automation, compaction, and sandboxes.
- Updated: Agent Platforms And Work Surfaces with archive leads for OpenClaw-adjacent systems, CoWork-OS, Core, Junior, Voicebox, ChatAvocado, OpenViktor, and Telegram wrappers.
- Updated: Agentic Artifact Surfaces with archive leads for Figma MCP, Excalidraw/draw.io MCP, Remotion, VEO, Pencil, TikTok slide shows, and Frontend Slides.
- Updated: Agentic GTM Campaign Workflows with archive leads for AI CRM, GTM coworkers, Salesforce/AI sales startups, LangChain GTM agent, directory SEO, UGC, and web automation stacks.
- Updated: Personal Agent Ops Stack with archive leads for deep research, observability, Obsidian commands, workflows.io, and personal-system triage.
- Updated source-map provenance for all 74 raw note captures and the archive ingest manifest.

## 2026-06-11 | ingest | Sunder Workspace and migration source sync

- Ported 439 article/scrape/text captures from `/Users/sethlim/Documents/Sunder Workspace/` and `/Users/sethlim/Documents/sunder-next-migration-20260225/` into `raw/intentional/pasted/sunder-sync-2026-06-11/`, including 64 supplemental candidates added during the verification pass.
- Ported 68 CSV/XLSX/TSV data snapshots into `raw/intentional/pasted/sunder-sync-2026-06-11-data/`.
- Created: Sunder Sync Source Captures, a one-by-one retrieval digest for X/Twitter captures, web scrapes, local scrape outputs, and data files.
- Updated: Agent Platforms And Work Surfaces, Agentic Engineering Practices, Agentic GTM Campaign Workflows, GTM Waterfall Enrichment APIs, and Agentic Artifact Surfaces with Sunder sync retrieval pointers.
- Updated source-map provenance for all 507 raw captures plus the Sunder sync manifests.
- Did not delete or alter the original files in either source folder.

## 2026-06-11 | capture+sweep | Remotion product-demo video collateral

- Captured exact X link for Thariq/Fable launch-video workflow through the authenticated X path.
- Ran Last30Days sweep for Remotion, AI video editors, Fable-style launch collateral, and founder-speaking product demo videos.
- Staged digest for job-application product demo collateral; left it uncompiled pending manual capture of HyperFrames/Vex/related sources or Seth's own workflow experiment.
- Updated source-map provenance for the captured X post and staged Last30Days sweep.

## 2026-06-11 | ingest | browser-use video-use

- Captured exact X link for Gregor Zunic's video-use pointer through the authenticated X path.
- Captured the browser-use/video-use README as complete raw web evidence.
- Updated: Agentic Artifact Surfaces with transcript-first agentic video editing for founder/product demo collateral: raw footage, transcript pack, timeline views, EDL/cut plan, FFmpeg render, subtitles/color/audio fades, HyperFrames/Remotion overlays, and rendered-boundary self-eval.
- Updated the Remotion product-demo Last30Days digest with video-use as the concrete repo lead.
- Updated source-map provenance for both captures.

## 2026-06-11 | ingest | Remotion vs HyperFrames routing

- Captured Matt Van Horn's Remotion-vs-HyperFrames X Article through the authenticated X path.
- Updated: Agentic Artifact Surfaces with the routing rule: video-use as upstream transcript-first editing, HyperFrames for fast agent-authored HTML launch reels/product clips, and Remotion for React-native compositions, code review, and scale.
- Updated the Remotion product-demo Last30Days digest to mark the HyperFrames comparison lead as captured and compiled.
- Updated source-map provenance for the captured X Article.

## 2026-06-11 | ingest | GTM Context OS GitHub repository

- Staged: GTM Context OS GitHub repository partial capture.
- Updated: Agentic GTM Campaign Workflows.

## 2026-06-12 | ingest | Peter Wang vertical-agent context hierarchy

- Captured exact X Article link through the authenticated X path.
- Updated: Agentic Engineering Practices with vertical agents as faithful compression of task distributions, using L1/L2/L3 context tiers, deferred specs/tools, raw-reference escape hatches, and token-compressed domain operations.
- Updated source-map provenance for the compiled capture.

## 2026-06-12 | ingest | Zach Lloyd spec-driven development skills

- Captured exact X Article link through the authenticated X path.
- Updated: Agent Skill Libraries And Requirements with the Warp common-skills product-spec, tech-spec, spec-match validation, and computer-use UX validation chain.
- Updated: Agentic Engineering Practices with checked-in product/tech specs as reviewable task contracts for implementation PRs.
- Updated source-map provenance for the compiled capture.

## 2026-06-12 | ingest | Superpowers and Compound Engineering core AI-coding repos

- Captured: EveryInc Compound Engineering Plugin README.
- Captured: obra Superpowers README.
- Updated: Agent Skill Libraries And Requirements with Seth's high-trust AI-coding trio: Matt Pocock Skills, Compound Engineering, and Superpowers.
- Updated: Agentic Engineering Practices with Compound Engineering's compounding plan/review/learning loop and Superpowers' strict design/TDD/subagent/review/verification methodology.
- Fixed `scripts/new-raw-capture.sh` so arbitrary raw body text is written inertly instead of being interpolated by the shell heredoc.
- Updated source-map provenance for both captures.

## 2026-06-12 | ingest | AI Engineer agentic-coding talks

- Captured complete YouTube transcripts for twelve AI Engineer talks on AI coding, harness engineering, skills, spec-driven development, Claude Code internals, agent lifecycle, reliable agents, and knowledge-work automation.
- Created: AI Engineering Talks On Agentic Coding with one summary per talk and an updated spec-driven-development draft.
- Updated: Agentic Engineering Practices with the synthesis that serious AI coding is an end-to-end SDLC loop spanning requirements, architecture, context, verification, review, release, and learning.
- Updated: Agent Skill Libraries And Requirements with transcript-backed support for Matt Pocock workflows, Anthropic skills, and Kiro-style structured requirements.
- Updated source-map provenance for all twelve YouTube captures.

## 2026-06-12 | ingest | Cognition Devin managed-agent workflows

- Captured: How Cognition Uses Devin to Build Devin.
- Captured: Closing the Agent Loop: Devin Autofixes Review Comments.
- Captured: Cognition Coding Agents 101 pointer page and the linked Devin Agents 101 guide.
- Created: Devin Managed Agent Workflows.
- Updated: Agentic Engineering Practices with Devin managed-platform loops, review/autofix systems, and operator practices for autonomous coding agents.
- Updated: Agent Platforms And Work Surfaces with Devin's multi-surface platform shape: Slack/Linear/Jira/web/CLI/API, codebase Q&A, review, DeepWiki, playbooks, MCPs, session insights, and automated triggers.
- Updated source-map provenance for all four web captures.

## 2026-06-12 | ingest | YC context-engineering talks

- Captured complete YouTube transcripts for Context Engineering for Engineers and Advanced Context Engineering for Agents.
- Updated: AI Engineering Talks On Agentic Coding with Chroma's gather/glean context model and HumanLayer's research-plan-implement workflow for large codebases.
- Updated: Agentic Engineering Practices with context curation, intentional compaction, subagent search, research/plan artifacts, and the claim that bad research/plans are higher-leverage failures than individual bad code lines.
- Updated source-map provenance for both YouTube captures.

## 2026-06-13 | ingest | walkinglabs Awesome Harness Engineering selected set

- Captured Seth's selected subset of `walkinglabs/awesome-harness-engineering`: 48 selected resources from Courses/Learning, Foundations, Context/Memory/Working State, Constraints/Guardrails/Safe Autonomy, Specs/Agent Files/Workflow Design, and Evals/Observability.
- Captured the selected-list manifest as raw pasted evidence and 47 source pages/repo READMEs/PDF text extractions as raw or staged captures; the OpenAI harness article was already present and skipped.
- Staged one incomplete preprints.org position-paper capture because the page/PDF blocked local fetches; kept it as incomplete evidence only.
- Updated: Agentic Engineering Practices with the walkinglabs harness canon: work definition, runtime control, and measurement as the three-layer operating map for reliable agents.
- Updated source-map provenance for the new capture cluster.

## 2026-06-13 | ingest | walkinglabs Awesome Harness Engineering full repo remainder

- Captured the remaining `walkinglabs/awesome-harness-engineering` README links after the selected-set import, including Benchmarks and Runtimes/Harnesses/Reference Implementations.
- Added a remaining-links manifest plus 57 resource captures; 7 JS-heavy/blocked benchmark pages were staged as partial/incomplete captures rather than promoted as full evidence.
- Updated: Agentic Engineering Practices with the benchmark/runtime map for Terminal-Bench, SWE-bench, WebArena, OSWorld, MCP benchmarks, security benchmarks, Deep Agents, SWE-agent, SWE-ReX, browser harnesses, Harbor, Harness Evolver, Ralph loops, and portable skills.
- Updated source-map provenance for the full-repo remainder.

## 2026-06-15 | ingest | Workflow Hustle While Job Hunting

- Captured: Seth's pasted vertical-agent startup note and scaling discussion as complete raw pasted evidence.
- Created: Workflow Hustle While Job Hunting as a new wiki lane for building small workflow businesses and proof-of-work artifacts while applying for jobs.
- Updated: Knowledge Base Index with the Workflow Hustle domain.
- Updated source-map provenance for the compiled raw capture.

## 2026-06-15 | ingest | Zhao OrderOps PRD

- Captured: Zhao workflow sketches as raw image attachments plus an interpretive raw manifest.
- Created: Zhao OrderOps PRD with Mermaid diagrams for channel intake, order normalization, route/load sequencing, and order state transitions.
- Published: Zhao OrderOps HTML artifact to https://civic-oasis-aq2d.here.now/ using Here Now authenticated hosting.
- Updated: Workflow Hustle While Job Hunting with a project cross-link.
- Updated: Knowledge Base Index with the Zhao OrderOps project page.
- Updated source-map provenance for the compiled sketch manifest.

## 2026-06-16 | ingest | Enterprise sales knowledge dump consolidation

- Added an authenticated X profile timeline sweep interface and captured 100-post snapshots for `@AlfieJCarter`, `@fivosaresti`, `@chrispisarski`, and `@BrianLaManna_`.
- Staged: Enterprise sales X profile digest.
- Captured: enterprise-sales transcript, Cher Hao WhatsApp excerpt, Acme/eGiro first-10-day goals, career-ops enterprise sales playbook, Salescraft Patrick Spychalski/Eric Nowoslawski LinkedIn corpus subset, sales plugin account-research/outreach skills, and GTM workspace agentic outbound/Acme OS docs.
- Created: High-Signal Enterprise Sales.
- Created: AI-Native Account Intelligence.
- Updated: Acme Agentic GTM OS.
- Updated: Agentic GTM Campaign Workflows.
- Updated: GTM Waterfall Enrichment APIs.
- Updated: Knowledge Base Index and source-map provenance for the new raw, staging, and compiled wiki pages.

## 2026-06-16 | ingest | Hamburger Rule enterprise sales note

- Captured: Shyam Sankar/Palantir Hamburger Rule enterprise-sales note as intentional pasted raw evidence.
- Updated: High-Signal Enterprise Sales with the bureaucratic-friction principle that the desired next action must be easier than stalling or doing nothing.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-16 | ingest | Backdated enterprise sales X profile sweep

- Extended the X profile timeline scraper with `--offset` support for backdated profile snapshots.
- Captured: Alfie Carter posts 101-200, Fivos Aresti posts 101-190, and Chris Pisarski posts 101-200 as sweep evidence.
- Blocked: Brian LaManna posts 101-200 were not captured because X returned HTTP 429 rate limits after multiple retries.
- Staged: Enterprise sales X profile backdated digest.
- Updated: High-Signal Enterprise Sales with buyer-defined demos, champion enablement, discovery questions, and CRM note quality.
- Updated: AI-Native Account Intelligence with signal routing and closed-won/closed-lost feedback loops.
- Updated: Agentic GTM Campaign Workflows with content-to-CRM loops, shared GTM skill context, personalized microsites/decks, and the GTM engineer role shape.
- Updated: Acme Agentic GTM OS with daily deal review, demo prep, champion packages, CRM note quality, and skill bootstrap constraints.
- Updated: GTM Waterfall Enrichment APIs with signal routing-table requirements.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-17 | ingest | Marketing domain and Last30Days synthesis

- Captured: Stripe Forward Deployed AI Accelerator Marketing job posting as complete pasted raw evidence.
- Captured: jet-seo Atlas SEO content pipeline local project as a complete local-project raw snapshot.
- Captured: Hesamation X post about Anthropic growth marketing via the authenticated X capture path.
- Staged: LinkedIn post lead for the Anthropic Claude marketing guide as incomplete evidence only.
- Ran and staged eight Last30Days marketing sweeps: workflow transformation, SEO/AEO/GEO, performance creative ops, autonomous landing pages, AI UGC, content/editorial ops, lifecycle CRM/marketing ops, and marketing analytics/FDA enablement.
- Created: Agentic Marketing Workflows.
- Created: SEO/AEO/GEO Content Systems.
- Created: Performance Marketing Creative Ops.
- Created: Autonomous Websites And Landing Pages.
- Created: UGC And Creator Systems.
- Created: Content Ops And Editorial Systems.
- Created: Lifecycle CRM And Marketing Ops.
- Created: Marketing Analytics And FDA Enablement.
- Updated: Knowledge Base Index with the Marketing domain and article router.
- Updated: source-map provenance for the new raw captures, staged digests, promoted Marketing pages, and existing seed captures compiled into Marketing.

## 2026-06-18 | ingest | OpenClaw canonical architecture section

- Created: OpenClaw Architecture And Operating Model as the canonical wiki section for OpenClaw/Clawdbot architecture, sessions, multi-agent routing, isolation, Pi/runtime nuance, tools, plugins, and tool policy.
- Updated: Knowledge Base Index with the OpenClaw domain.
- Updated source-map provenance for the compiled OpenClaw source cluster.

## 2026-06-18 | ingest | Z.ai GLM-5.2 X post

- Captured: Z.ai GLM-5.2 launch post as complete intentional X raw evidence.
- Updated: Agentic Engineering Practices with GLM-5.2 as an open-weight model-layer watch item for coding/agentic tasks, long context, reasoning effort, cost, and license evaluation.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-18 | ingest | Vox prompt-shaping X post

- Captured: Vox's Claude Code/Codex prompt-shaping post as complete intentional X raw evidence.
- Updated: Agentic Engineering Practices with the prompt-contract reminder that senior coding agents should receive goals, context, constraints, and verification expectations rather than one-line imperatives.
- Updated: Knowledge Base Index and source-map provenance.

## [2026-06-18] ingest | Agent Framework Landscape

- Created: Agent Framework Landscape.
- Added: Agent Frameworks domain to index.
- Staged partial: Vercel eve announcement partial reader capture.

## 2026-06-18 | ingest | Ivan Falco ads-skills and paid-ads Claude Code transcript

- Captured: `ivangfalco/ads-skills` repository snapshot at commit `926bf75e20a833012ca1c7aeb514209411541fd6`.
- Captured: How To Get Unlimited Leads Using Claude Code For Paid Ads transcript as complete intentional YouTube raw evidence.
- Updated: Performance Marketing Creative Ops with the paid-ads agent workflow: audience/list builder, ad generator, ICP matrix, audience intelligence, enrichment, brand/template creative generation, ad-platform APIs, paused campaign staging, and human approval.
- Updated: Agentic Marketing Workflows with ads-skills as a concrete public implementation of AI-native marketing operations.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-18 | ingest | Vox prompt templates screenshots

- Captured: user-provided screenshots with the eight Vox Claude Code/Codex prompt templates as complete intentional pasted raw evidence.
- Updated: Agentic Engineering Practices with the full prompt-template pattern: role, goal, deliverables, architecture/edge cases, verification, review loop, and completion standard.
- Preserved: the earlier Vox X raw capture remains immutable; the screenshot prompt text is stored as a separate raw source linked back to the same X post.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-18 | ingest | Production AI architecture screenshot

- Captured: Tech with Mak production AI architecture screenshot as intentional pasted raw evidence, with the temp screenshot preserved as a repo-local asset.
- Updated: Agentic Engineering Practices with the production AI/RAG app repo-layer checklist: retrieval components, services, prompts, agents/tools, security, evals, observability, data/index config, tests, docs, and coding-agent context.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-18 | ingest | Ploy website-centered marketing platform launch

- Captured: Bryant Chou's Ploy launch X conversation as intentional raw evidence from user-pasted text; exact status URL was not provided.
- Updated: Autonomous Websites And Landing Pages with Ploy as a website-centered growth-system example spanning ABM pages, programmatic SEO, ad-specific landing pages, site slurping, daily reports, and approval-gated shipping.
- Updated: Agentic Marketing Workflows with the broader pattern that AI marketing moves from asset generation to a connected website/CMS/CRM/campaign/analytics/SEO/AEO operating loop.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-19 | ingest | Corey Haines marketingskills

- Captured: `coreyhaines31/marketingskills` repository snapshot at commit `8bfcdffb655f16e713940cd04fb08891899c47db`.
- Updated: Agentic Marketing Workflows with `marketingskills` as a broad cross-agent marketing skill-library pattern centered on shared product-marketing context.
- Updated: SEO/AEO/GEO Content Systems with `seo-audit`, `ai-seo`, `programmatic-seo`, schema, site architecture, content strategy, analytics, and product-marketing as portable SEO/content workflow contracts.
- Updated: Content Ops And Editorial Systems with `marketingskills` as a source for product-marketing, content strategy, copywriting, copy editing, social, email, video, image, customer research, and analytics routes.
- Updated: Agent Skill Libraries And Requirements with `marketingskills` as a broad domain pack using Agent Skills, evals, plugin marketplace install paths, and a marketing tool registry.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-19 | ingest | AI operator and Stripe FDA role framing

- Captured: Rish Gupta's AI operator essay as complete intentional web raw evidence.
- Captured: Andrew Yeung's Stripe Forward Deployed AI Accelerator X post through the authenticated X capture path.
- Updated: Agentic Marketing Workflows with the AI-operator/FDA category: embedded workflow redesign, short-cycle build/buy, IC education, adoption, reusable playbooks, and handoff.
- Updated: Knowledge Base Index and source-map provenance.

## 2026-06-19 | ingest | Startup Funding Signal Job Search

- Captured: Newly funded startup job-search and Singapore GTM lead strategy as complete intentional pasted raw evidence.
- Created: Job Apps domain.
- Created: Startup Funding Signal Job Search with verified/caveated target pipeline, Singapore/APAC GTM lead wedge, outreach principles, weekly job-apps loop, and links to GTM/account-intelligence support pages.
- Updated: Knowledge Base Index and source-map provenance.

## [2026-06-22] query | Archived: OpenAI And Codex Context Dossier For Strategic BDR APAC

- Created: OpenAI And Codex Context Dossier For Strategic BDR APAC.
- Updated: Knowledge Base Index archive section.

## [2026-06-22] query | Re-audited: OpenAI And Codex Context Dossier For Strategic BDR APAC

- Expanded the archive with an OpenAI-vs-Claude/Anthropic comparison section, competitive talk tracks, and a larger Claude/Anthropic source index.
- Rechecked coverage with QMD retrieval plus exact `rg` term and path searches across `wiki/`, `raw/`, and `staging/`.

## [2026-06-22] query | Amended: Codex Agentic-Coding Narrative

- Added an Evolution Of Agentic Coding section to the OpenAI/Codex dossier.
- Added the concise selling narrative: Codex proves the shift from AI answering questions to agents completing bounded, verifiable work.
- Added agentic-coding evolution sources to the archive source index.

## [2026-06-22] maintenance | Removed true duplicate raw captures

- Deleted duplicate OpenAI Cookbook Goals captures `raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex-2.md` and `raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex-3.md`.
- Kept canonical capture `raw/intentional/web/2026-06-10-openai-cookbook-using-goals-in-codex.md`.
- Updated source-map provenance and archive source links to reference only the canonical capture.
