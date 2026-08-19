---
type: wiki_article
title: Sandbox Filesystem Agent Architecture
updated_at: 2026-06-28
status: active
source_count: 11
tags:
  - agent-frameworks
  - sandboxes
  - filesystems
  - bash
  - eve
  - openclaw
  - tasklet
  - fintool
---

# Sandbox Filesystem Agent Architecture

> Sources: Vercel "How to build agents with filesystems and bash", 2026-01-09; LangChain/Harrison Chase "The two patterns by which agents connect sandboxes", 2026-02-10; Harrison Chase X article capture, 2026-06-27; Nicolas Bustamante/Fintool lessons capture; Tasklet state/tool architecture captures; Sunder sandbox architecture playbook captures; Vercel Eve Concepts docs; Vercel Introducing Eve.
> Raw: [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md); [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md); [Harrison Chase X Article](../../raw/intentional/x/2021261552222158955-hwchase17-the-two-patterns-by-which-agents-connect-sandboxes-tl-dr-more-and-more-agents-ne.md); [Fintool Lessons Building AI Agents](../../raw/intentional/pasted/sunder-sync-2026-06-11/224-nicbustamante-fintool-lessons-building-ai-agents-full.md); [Tasklet State Surfaces](../../raw/intentional/pasted/sunder-sync-2026-06-11/240-02-state-surfaces-system-vs-agent.md); [Tasklet Tool System And Execution Flow](../../raw/intentional/pasted/sunder-sync-2026-06-11/241-03-tool-system-and-execution-flow.md); [Tasklet/Fintool Pattern Spectrum](../../raw/intentional/pasted/sunder-sync-2026-06-11/380-key-architecture-v2-centralized.md); [Final Sandbox Architecture Playbook](../../raw/intentional/pasted/sunder-sync-2026-06-11/387-final-sandbox-architecture-playbook.md); [Vercel Testing Bash Is All You Need](../../raw/intentional/pasted/sunder-sync-2026-06-11/080-vercel-testing-bash-is-all-you-need-full.md); [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md); [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md)

## Core Model

The clean mental model is:

- **Files are the interface.**
- **Storage is the memory.**
- **The sandbox is the blast wall.**
- **Tools are the doors.**
- **The model/tool loop is the worker that walks through the doors.**

The important question is not "does the agent have a filesystem?" The better question is "which filesystem?"

## Four Filesystems

There are usually four different file-like surfaces:

| Surface | What It Means | Durable? | Example |
|---|---|---|---|
| Agent definition filesystem | The committed files that define behavior | Yes, through Git/deploy | Eve `agent/instructions.md`, `agent/tools/`, `agent/skills/` |
| Persistent workspace filesystem | Agent-readable memory and artifacts | Yes, through S3/database/object storage or a persistent volume | `/agent/home`, user memories, generated reports |
| Sandbox filesystem | Isolated execution workspace | Often temporary, sometimes session-stateful | Vercel Sandbox, E2B, Daytona, Docker, VM |
| Projected business filesystem | A file-shaped view of real app data | Regenerated from source systems | CRM accounts as folders, transcripts as markdown, `meta.json` per document |

Vercel's filesystem/bash article argues that LLMs are already strong at directory navigation, `grep`, `find`, `cat`, scripts, and codebase-style exploration. So for support tickets, sales transcripts, CRM records, documents, or call notes, you can project the domain into files and let the agent use the same habits it uses in code.

That does not mean the filesystem becomes the only database. It means the filesystem becomes a model-friendly work surface.

## Sandbox Patterns

LangChain's article gives the key architecture split.

| Pattern | Where The Agent Runs | Where Code Runs | Main Benefit | Main Risk |
|---|---|---|---|---|
| Agent in sandbox | Inside the Docker/VM/sandbox | Same place | Mirrors local development and gives direct filesystem access | Agent code, prompts, credentials, and tool permissions sit inside the sandbox boundary |
| Sandbox as tool | App/server/local harness | Remote sandbox called by API | Keeps agent state and API keys outside; isolates only execution | More network hops and state-sync decisions |

This distinction matters because it separates **agent state** from **execution state**.

In Pattern 1, the sandbox is the agent's home. In Pattern 2, the sandbox is a tool the agent can rent for dangerous or code-heavy work.

## Where Bash Fits

Shell commands are the agent's low-level way of operating a filesystem. `bash` is one common shell that can run commands such as:

```bash
ls
find . -name "*.md"
grep -R "pricing objection" transcripts/
cat account/acme/summary.md
python analyze.py
```

The Vercel article's point is not "bash is magic." It is that shell-style operations give the model precise, inspectable retrieval:

- `grep` finds exact phrases.
- `find` discovers files.
- `cat` reads only what is needed.
- scripts transform files into new artifacts.
- the transcript or CRM dump does not have to be stuffed into the prompt upfront.

For semi-structured data, this is often better than only vector search. Fintool's captured lessons point toward a hybrid: use SQL/metadata for structured lookup and bash/filesystem exploration to inspect and verify messy documents.

## Durable Storage Is Still Required

For an AI CRM, durable storage is not optional.

The CRM database or CRM API owns:

- accounts
- contacts
- deals
- messages
- permissions
- approvals
- audit events
- normalized metadata

Object storage or persistent workspace storage owns:

- transcripts
- uploaded PDFs/spreadsheets
- generated reports
- account briefs
- working artifacts
- user/team memories
- reusable skill files

The sandbox owns:

- temporary code execution
- package installs
- scratch files
- risky user-provided files
- generated scripts
- isolated document processing

The agent definition owns:

- instructions
- tools
- skills
- channel config
- schedules
- evals
- sandbox config

Fintool's lesson is the strongest production version of this: S3 can be the source of truth for user files, skills, memories, uploads, and artifacts; Postgres/SQL indexes the metadata for fast retrieval; the sandbox sees scoped mounts such as private, shared, and public areas.

## Eve Interpretation

Eve should be read as a filesystem-first agent definition and runtime, not as "put the whole company in a folder."

For Eve:

- `agent/` is the deployable agent definition.
- Vercel Workflows gives durable session/turn execution.
- AI SDK and AI Gateway handle the model loop and model routing.
- tools and connections touch business systems.
- skills are on-demand procedural context.
- the sandbox is the isolated bash/file/code environment.

Eve looks closer to LangChain Pattern 2 for most product work: the agent runtime and product systems remain outside the sandbox, while sandbox work is called when the agent needs isolated execution. The sandbox can still have files, but those files are a workspace/projection, not necessarily the permanent source of truth.

## OpenClaw And Local Codex Comparison

Codex on a local repo and self-hosted OpenClaw can feel like the filesystem and sandbox are the same thing because the agent can read and mutate a workspace directly.

That is convenient for personal knowledge work:

- `grep` searches the actual wiki/repo.
- files are both memory and workbench.
- shell commands operate where the data already lives.

For a production AI CRM, that coupling becomes risky. The better pattern is to decouple:

- durable CRM data stays in databases and APIs.
- durable artifacts stay in object storage or persistent workspace storage.
- the sandbox gets a scoped copy, projection, or mount.
- tools mediate every external mutation.
- approvals gate risky writes.

So OpenClaw-on-a-VPS can combine workspace, runtime, storage, and sandbox in one machine. Eve/Vercel-style production architecture tends to split them into separate layers.

## AI CRM Flow

Plain-language end to end:

1. A teammate messages the bot in Slack or the app.
2. The agent runtime resumes the durable session.
3. The runtime loads the agent definition: instructions, tools, skills, connections, approvals, schedules, evals, and sandbox config.
4. The model thinks through the model/tool loop.
5. If it needs CRM facts, it calls trusted CRM/search/database tools.
6. If it needs file-shaped context, the app projects relevant CRM records, call transcripts, docs, or account history into a workspace.
7. If it needs risky execution, parsing, scripts, package installs, spreadsheets, PDFs, or generated code, it calls the sandbox.
8. The sandbox reads/writes its own isolated files and returns results.
9. The agent decides next steps from the tool results.
10. If it wants to mutate CRM, send email, post externally, or save durable memory, a tool does that behind permission checks and approval gates.
11. The durable workflow records state so the run survives waits, crashes, and redeploys.
12. Observability/evals inspect whether the agent used tools correctly.

## Design Rules

- Use files when the model needs to browse, inspect, compare, transform, or create artifacts.
- Use databases when the app needs permissions, queries, joins, auditing, dedupe, and durable truth.
- Use vector search when the query is semantic and fuzzy.
- Use `grep`/bash when the query is exact, structured, or file-local.
- Use a sandbox when code execution or untrusted files could hurt the host runtime.
- Use tools for every real-world mutation.
- Use approvals for irreversible or externally visible writes.
- Do not confuse "agent folder" with "customer data store."

## Open Questions

- For Seth's first AI CRM prototype, should account briefs live as persisted markdown files, database rows rendered into markdown on demand, or both?
- Should sandbox sessions be ephemeral per task, stateful per customer/account, or stateful per user?
- What is the minimum metadata index needed so the agent can find account artifacts without needing to `grep` the whole world every time?
- Can Eve's built-in sandbox and connection model replace a custom OpenClaw-style VPS workbench, or should Eve be treated as the hosted product path and OpenClaw as the local/self-hosted path?

## Sources

- [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md)
- [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md)
- [Harrison Chase X Article](../../raw/intentional/x/2021261552222158955-hwchase17-the-two-patterns-by-which-agents-connect-sandboxes-tl-dr-more-and-more-agents-ne.md)
- [Fintool Lessons Building AI Agents](../../raw/intentional/pasted/sunder-sync-2026-06-11/224-nicbustamante-fintool-lessons-building-ai-agents-full.md)
- [Tasklet State Surfaces](../../raw/intentional/pasted/sunder-sync-2026-06-11/240-02-state-surfaces-system-vs-agent.md)
- [Tasklet Tool System And Execution Flow](../../raw/intentional/pasted/sunder-sync-2026-06-11/241-03-tool-system-and-execution-flow.md)
- [Tasklet/Fintool Pattern Spectrum](../../raw/intentional/pasted/sunder-sync-2026-06-11/380-key-architecture-v2-centralized.md)
- [Final Sandbox Architecture Playbook](../../raw/intentional/pasted/sunder-sync-2026-06-11/387-final-sandbox-architecture-playbook.md)
- [Vercel Testing Bash Is All You Need](../../raw/intentional/pasted/sunder-sync-2026-06-11/080-vercel-testing-bash-is-all-you-need-full.md)
- [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md)
- [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md)

## See Also

- [Vercel Eve Framework](vercel-eve-framework.md)
- [Agent Framework Landscape](agent-framework-landscape.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [OpenClaw Architecture And Operating Model](../openclaw/openclaw-architecture-and-operating-model.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
