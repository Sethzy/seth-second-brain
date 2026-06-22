# AI Engineering Big Shifts Research Ledger

Date window: roughly December 2025 through June 14, 2026.

This ledger supports `index.html`. It replaces the earlier exact-date chronology with a scan-first map of broad industry shifts.

## Retrieval Pass

- Used QMD first across Seth Second Brain.
- Retrieved full local sources before rewriting: `wiki/personal-systems/agent-platforms-and-work-surfaces.md`, `wiki/ai-coding/agentic-engineering-practices.md`, `wiki/ai-coding/vendor-agentic-engineering-blogs-2026.md`, OpenClaw/Clawchief captures, Codex use-case/security captures, Cursor third-era/Cursor 3 captures, and Claude context-engineering captures.
- Used external primary pages for current vendor/product details where local raw captures were not present, especially OpenAI Codex changelog, Anthropic model/system-card pages, Cognition verification/Desktop posts, and LangChain Deep Agents docs.
- Treated `staging/incomplete-captures/` and Last30Days sweeps as lead material only. No core milestone depends on incomplete captures.

## Shift Source Map

| Shift | Claim boundary | Key sources |
| --- | --- | --- |
| Frontier coding models crossed into agent territory | High-level synthesis that model capability unlocked longer, more autonomous, tool-using workflows. Exact model comparisons vary by vendor and source; the artifact phrases this as an Opus/Codex/Composer-era model jump rather than one exact model point release. | Cursor third era: `raw/intentional/web/2026-02-26-cursor-the-third-era-of-ai-software-development.md`; Anthropic Opus/system-card pages |
| Codex-style app surfaces became real workbenches | Codex app is treated as a work surface because Goal mode, Appshots, remote computer use, plugin sharing, browser annotations, and use-case galleries make the agent operate across apps and tasks. | OpenAI Codex changelog; `raw/intentional/web/2026-06-11-openai-codex-use-cases.md` |
| OpenClaw made the local agent OS legible | OpenClaw is an emerging/local-agent-OS signal, not proof of the whole market. The claim is that it made the file-state, heartbeat, skills, multi-channel, provider-abstraction pattern easy to name. | `wiki/personal-systems/agent-platforms-and-work-surfaces.md`; `raw/intentional/web/2026-06-10-clawchief-readme.md`; `raw/intentional/pasted/sunder-sync-2026-06-11/390-openclaw-pi-agent-vercel-sdk-deep.md` |
| The harness became the product | Strongest cross-source synthesis: reliability comes from tools, state, permissions, context, subagents, evals, and observability around the model. | `wiki/ai-coding/agentic-engineering-practices.md`; `raw/intentional/web/2026-04-30-cursor-continually-improving-our-agent-harness.md`; LangChain Deep Agents docs |
| Skills and workflows replaced one-off prompting | Broad vendor convergence: skills, workflows, plugins, routines, and playbooks package reusable procedure and domain knowledge. | `raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md`; `raw/intentional/web/2026-06-02-claude-a-harness-for-every-task-dynamic-workflows-in-claude-code.md`; Codex changelog |
| Context engineering became the new backend | Claim is about retrieval, compaction, memory, and subagent routing becoming core engineering work. | `raw/intentional/web/2026-01-06-cursor-dynamic-context-discovery.md`; `raw/intentional/web/2026-02-11-openai-shell-skills-compaction-tips-for-long-running-agents-that-do-real-work-o.md`; `raw/intentional/web/2026-06-13-effective-context-engineering-for-ai-agents.md` |
| Verification moved inside the agent loop | Cross-source claim that agents need tests, screenshots, traces, evals, review, and automatic remediation to be useful in production. | `raw/intentional/web/2026-01-15-cursor-building-a-better-bugbot.md`; `raw/intentional/web/2026-06-13-testing-agent-skills-systematically-with-evals.md`; `raw/intentional/web/2026-06-11-openai-codex-security-setup-docs.md`; Cognition testing-development |
| Cloud, desktop, Slack, and browser converged | Claim that work surfaces converged across IDE, desktop, web, Slack, cloud VMs, browser, mobile, GitHub, and Linear. | `raw/intentional/web/2026-04-02-cursor-meet-the-new-cursor.md`; Cognition Devin Desktop; `wiki/personal-systems/agent-platforms-and-work-surfaces.md` |
| Security and governance became design constraints | Strong vendor/local convergence around sandboxes, secure indexing, hooks, threat models, vaults, and least-privilege production access. | `raw/intentional/web/2025-12-22-cursor-hooks-for-security-and-platform-teams.md`; `raw/intentional/web/2026-02-18-cursor-implementing-a-secure-sandbox-for-local-agents.md`; `raw/intentional/web/2026-05-27-claude-zero-trust-for-ai-agents.md`; `raw/intentional/web/2026-06-11-openai-codex-security-setup-docs.md` |

## Why This Is Less Granular

The prior version had 73 dated entries. That was useful as a source audit, but too dense for scanning. This version deliberately uses nine timeline milestones and a four-phase progression rail. The citations remain attached, but the first read should answer: "what changed in the industry, and how did the stack form over time?"

## Claim Audit

| Claim class | Treatment |
| --- | --- |
| Confirmed facts | Source titles, local raw paths, vendor feature names, product docs, and broad launch details. |
| Synthesis | Shift names, phase labels, and why a source matters. These are interpretive but grounded in multiple sources. |
| Emerging signal | OpenClaw/local-agent-OS material is high-signal for Seth's corpus, but it is labeled emerging rather than industry-wide proof. |
| Excluded | Detailed release chronology, noisy sweep-only claims, and exact model-name claims that were not needed for the scan-level story. |

## QMD Retrieval Examples

Commands run during this pass included:

```bash
qmd search "OpenClaw openclaw Claw Claude Code open agent OS" -n 20 --full-path
qmd search "Codex app Codex goals appshots remote computer use plugin sharing Codex use cases" -n 20 --full-path
qmd search "Opus 4.5 Opus 4.6 Claude Opus Sonnet 4.6 Fable Mythos" -n 20 --full-path
qmd query $'intent: Find synthesized local sources that identify big industry-wide shifts in AI engineering and agentic software development...'
qmd get qmd://wiki/personal-systems/agent-platforms-and-work-surfaces.md:1:220 --full-path
qmd get qmd://wiki/ai-coding/agentic-engineering-practices.md:1:230 --full-path
qmd get qmd://wiki/ai-coding/vendor-agentic-engineering-blogs-2026.md:1:380 --full-path
qmd get qmd://intentional/web/2026-06-10-clawchief-readme.md:1:120 --full-path
qmd get qmd://intentional/web/2026-06-11-openai-codex-use-cases.md:1:120 --full-path
qmd get qmd://intentional/web/2026-02-26-cursor-the-third-era-of-ai-software-development.md:50:45 --full-path
```

## External Primary Checks

- OpenAI Codex changelog for Appshots, Goal mode, remote computer use, plugin sharing, and browser annotation details.
- Anthropic model/system-card and Claude blog pages for Opus/Sonnet/Fable model-line context.
- Cognition posts for Devin Desktop and verification framing.
- LangChain Deep Agents overview for a library-level harness reference.
