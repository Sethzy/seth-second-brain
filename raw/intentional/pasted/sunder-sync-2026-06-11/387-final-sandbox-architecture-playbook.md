---
type: raw_capture
source_type: x
title: "Sunder sync: final-sandbox-architecture-playbook.md"
url: "https://x.com/dabit3/status/2009131298250428923"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/03_Resources/Playbooks/Engineering/final-sandbox-architecture-playbook.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "03_Resources/Playbooks/Engineering/final-sandbox-architecture-playbook.md"
sha256: "28f38648dc2f315dea87b87f74bf4480b4b70c5612bc790e57e77633cf352a4c"
duplicate_of: ""
---

# Sunder sync: final-sandbox-architecture-playbook.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/03_Resources/Playbooks/Engineering/final-sandbox-architecture-playbook.md`

Primary URL: https://x.com/dabit3/status/2009131298250428923

Duplicate of existing source-map entry: `none`

## Capture Text

# Sandbox Architecture Playbook

> **Purpose**: Unified guide for building AI agents with sandboxed execution environments.
>
> **Status**: Active
> **Created**: 2026-01-18
> **Based on**: Comprehensive research (2026-01-16) + Sunder hybrid architecture design

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Core Architectural Patterns](#2-core-architectural-patterns)
3. [Sunder's Hybrid Architecture](#3-sunders-hybrid-architecture)
4. [Sandbox Provider Reference](#4-sandbox-provider-reference)
5. [Reference Implementations](#5-reference-implementations)
6. [Integration Patterns](#6-integration-patterns)
7. [Decision Framework](#7-decision-framework)
8. [Implementation Playbook](#8-implementation-playbook)
9. [Open Questions & Future Work](#9-open-questions--future-work)
10. [Sources & References](#10-sources--references)
11. [Appendix: Quick Start Template](#11-appendix-quick-start-template)
12. [Philosophy & Strategic Notes](#12-philosophy--strategic-notes)
13. [Claude Agent SDK Deep Dive](#13-claude-agent-sdk-deep-dive)

---

## 1. Executive Summary

### The Core Insight

Modern AI agents perform better with **fewer, more powerful tools** rather than many specialized ones. The industry is converging on a pattern where:

- **Filesystems replace vector databases** for context retrieval
- **Bash commands replace custom tools** for data exploration
- **Sandboxed microVMs provide isolation** for untrusted code execution

### Key Metrics (from Vercel's d0 agent)

| Metric | Before (Many Tools) | After (Minimal Tools) | Improvement |
|--------|--------------------|-----------------------|-------------|
| Execution Time | 274.8s | 77.4s | **3.5x faster** |
| Success Rate | 80% | 100% | **+20%** |
| Token Usage | ~102k | ~61k | **37% fewer** |
| Steps Required | ~12 | ~7 | **42% fewer** |

### Sunder's Strategic Decision

We adopt a **Hybrid Sandbox Architecture**: keep the simple Anthropic container path for basic analysis, add E2B (or similar) for power-user flows requiring network access, MCP tools, or custom packages.

### TL;DR Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Your Application                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   AI SDK    │───▶│   Agent     │───▶│   Sandbox   │     │
│  │  (Claude)   │    │  (Minimal   │    │ (Firecracker│     │
│  │             │    │   Tools)    │    │   microVM)  │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│                            │                   │            │
│                            ▼                   ▼            │
│                    ┌─────────────┐    ┌─────────────┐      │
│                    │ExecuteCommand│   │ Filesystem  │      │
│                    │ (bash tool)  │   │  (context)  │      │
│                    └─────────────┘    └─────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Core Architectural Patterns

### 2.1 The "80% Tools Removal" Philosophy

**Source**: [vercel.com/blog/we-removed-80-percent-of-our-agents-tools](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)

#### The Problem

Vercel's internal text-to-SQL agent (d0) was built with many specialized tools:
- Schema lookup tools
- Query validation systems
- Error recovery mechanisms
- Entity join finders
- Catalog search functions
- Analysis planning tools

**Result**: 80% success rate, 274 seconds average execution, fragile, high maintenance.

#### The Solution

Stripped down to **two tools**:
1. `ExecuteCommand` - bash access (grep, cat, find, ls)
2. `ExecuteSQL` - query execution

```typescript
const agent = new ToolLoopAgent({
  model: "anthropic/claude-opus-4.5",
  tools: {
    ExecuteCommand: toolLoopAgent(sandbox),
    ExecuteSQL,
  },
});
```

#### Why It Works

1. **LLMs are trained on code navigation** - grep, cat, find are native capabilities
2. **Good documentation > smart tooling** - Well-structured files enable discovery
3. **Model capability improvements** - Larger context windows eliminate need for constraints
4. **Debugging transparency** - File reads and commands are visible and traceable

#### Key Quote

> "We were constraining reasoning because we didn't trust the model to reason. The best agents might be the ones with the fewest tools. Every tool is a choice you're making for the model."

---

### 2.2 Filesystem-Based Agent Pattern

**Source**: [vercel.com/blog/how-to-build-agents-with-filesystems-and-bash](https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash)

#### Core Insight

Replace custom retrieval tools with filesystem navigation:

```
Agent receives task → ls/find to explore → grep/cat for content
→ Send context to LLM → Return structured output
```

#### Why Filesystems Work

| Advantage | Explanation |
|-----------|-------------|
| **Natural domain mapping** | Customer records, transcripts, CRM data have inherent hierarchies |
| **Precise retrieval** | `grep -r "keyword"` returns exact matches vs semantic approximations |
| **On-demand loading** | Files loaded when needed, reducing token consumption |
| **Native model capability** | LLMs extensively trained on code navigation |
| **Debuggable** | File reads and commands are visible |

#### Directory Structure Pattern

```
context/
├── gong-calls/
│   ├── demo-call-001.md
│   ├── metadata.json
│   └── previous-calls/
├── salesforce/
│   ├── account.md
│   └── opportunity.md
├── research/
│   └── company-research.md
└── playbooks/
    └── sales-playbook.md
```

#### Implementation Example

```typescript
import { Sandbox } from '@vercel/sandbox';
import { bashTool } from 'bash-tool';

// Create sandbox with context files
const sandbox = await Sandbox.create({ runtime: 'node24' });
await sandbox.writeFiles([
  { path: 'context/transcript.md', content: transcriptBuffer },
  { path: 'context/metadata.json', content: metadataBuffer },
]);

// Agent uses bash to explore
const tools = {
  bash: bashTool(sandbox),
};

// Agent prompt includes:
// - ls to see available files
// - grep to search content
// - cat to read specific files
```

---

### 2.3 Files as Universal Interface (LlamaIndex Perspective)

**Source**: [llamaindex.ai/blog/files-are-all-you-need](https://www.llamaindex.ai/blog/files-are-all-you-need)

#### Core Thesis

Files and filesystems are emerging as the **primary abstraction for agent context management**, replacing:
- Naive RAG patterns
- Explicit MCP tool definitions
- Hardcoded retrieval logic

#### Three Use Cases

**1. Long-Context Storage**
```
Problem: Context window limitations during extended tasks
Solution: Store conversation history in searchable files (Claude.md, research.md)
Pattern: Agents dynamically retrieve previous context when needed
```

**2. External Context Retrieval**
```
Problem: Vector databases require upfront embedding, scale poorly
Solution: Filesystem CLI + semantic search for flexible discovery
Pattern: ls, grep, find combined with targeted reading
Key Insight: File search outperforms naive semantic search on small-medium collections
```

**3. Skills as Files**
```
Problem: MCP tools are complex to build, bloat context
Solution: Store "skills" as markdown files (API specs, procedures)
Advantages:
  - Easier than MCP development
  - Natural context window management
  - Enable arbitrary code execution
```

#### The Minimal Toolset

~5-10 tools is as capable as 100+ specialized tools:
- CLI filesystem navigation
- Code interpreter
- Web fetch
- Semantic search (when needed)

#### Known Gaps

| Gap | Workaround |
|-----|------------|
| Non-plaintext parsing (PDF, Word, Excel) | LlamaCloud Parse/Extract tools |
| Scaling beyond 1k-1M+ documents | External search infrastructure |
| Complex file editing (presentations, images) | Specialized tools |

---

## 3. Sunder's Hybrid Architecture

### 3.1 Problem Statement

Anthropic's built-in container provides excellent code execution but has a critical limitation: **no network access**. This blocks three capabilities we need for advanced use cases:

1. **Full Claude Agent SDK** - Subagents, plan mode, multi-agent orchestration
2. **Network Access** - MCP server calls, external API integrations
3. **Custom Packages** - Arbitrary pip/npm packages beyond Anthropic's curated skills

### 3.2 Solution: Two-Path Architecture

Keep the simple Anthropic container path for basic analysis, add E2B (or similar) for power-user flows.

```
┌─────────────────────────────────────────────────────────────────────┐
│                         AI Analyst Request                          │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │     Route Decision       │
                    │   (based on task type)   │
                    └──────────────────────────┘
                          │              │
              ┌───────────┘              └───────────┐
              ▼                                      ▼
┌─────────────────────────┐          ┌─────────────────────────────────┐
│   SIMPLE PATH           │          │   POWER PATH                    │
│   Anthropic Container   │          │   E2B Sandbox                   │
├─────────────────────────┤          ├─────────────────────────────────┤
│ ✓ Code execution        │          │ ✓ Code execution                │
│ ✓ File I/O              │          │ ✓ File I/O                      │
│ ✓ Pre-loaded skills     │          │ ✓ Network access                │
│ ✗ No network            │          │ ✓ MCP server calls              │
│ ✗ No custom packages    │          │ ✓ Claude Agent SDK (subagents)  │
│                         │          │ ✓ Custom pip/npm packages       │
├─────────────────────────┤          ├─────────────────────────────────┤
│ Cost: Included in API   │          │ Cost: ~$0.05/min (~$3/hr)       │
│ Latency: Fast           │          │ Latency: +5-10s cold start      │
│ Session: 30 days        │          │ Session: Configurable           │
└─────────────────────────┘          └─────────────────────────────────┘
```

### 3.3 Use Case Routing

| Use Case | Route | Rationale |
|----------|-------|-----------|
| Document summarization | Simple | No network needed |
| Data extraction → JSON | Simple | File I/O only |
| Reconciliation analysis | Simple | Pandas/jq in container |
| Generate Excel/PDF reports | Simple | Skills handle this |
| Query external database | **Power** | Network access required |
| Call MCP tools (Supabase, etc.) | **Power** | MCP = HTTP calls |
| Multi-agent orchestration | **Power** | Agent SDK subagents |
| Install custom Python package | **Power** | Arbitrary pip install |
| Web scraping / API calls | **Power** | Network access required |

---

## 4. Sandbox Provider Reference

### 4.1 Provider Comparison

| Provider | Network | Custom Pkgs | Persistence | Pricing | Best For |
|----------|---------|-------------|-------------|---------|----------|
| **Anthropic Container** | ❌ | Limited (skills) | 30 days | Included | Simple analysis |
| **E2B** | ✅ | ✅ | 1hr default | $0.05/min | Agentic workloads (recommended for Power Path) |
| **Vercel Sandbox** | ✅ | ✅ | 5min-5hr | Included w/ Vercel | Vercel-native apps |
| **Modal** | ✅ | ✅ | Per-request | $0.192/hr | Serverless-first |
| **Fly Machines** | ✅ | ✅ | Persistent | ~$5/mo min | Full VM control |
| **Vercel Edge Runtime** | ⚠️ | ❌ | None | Included | Limited runtime |

**Sunder Recommendation**: Start with **E2B** for Power Path - best developer experience for agentic workloads, well-documented, used by Jerry Liu and others in the space.

---

### 4.2 Vercel Sandbox - Core Technology

**Source**: [vercel.com/docs/vercel-sandbox](https://vercel.com/docs/vercel-sandbox)

Vercel Sandbox is an **ephemeral compute primitive** built on Firecracker microVMs. It provides:

- **Isolated execution** for untrusted/AI-generated code
- **Full Linux environment** with sudo access
- **Short-lived instances** (default 5 min, max 5 hours on Pro)
- **Network isolation** with allowlisting capabilities

#### System Specifications

| Property | Value |
|----------|-------|
| Base OS | Amazon Linux 2023 |
| Default User | `vercel-sandbox` |
| Working Directory | `/vercel/sandbox` |
| Sudo Access | Available |

**Available Runtimes**:

| Image | Runtime Path | Package Managers |
|-------|--------------|------------------|
| `node24` (default) | `/vercel/runtimes/node24` | npm, pnpm |
| `node22` | `/vercel/runtimes/node22` | npm, pnpm |
| `python3.13` | `/vercel/runtimes/python` | pip, uv |

**Pre-installed Packages**: git, tar, openssl, bind-utils, bzip2, findutils, gzip, iputils, libicu, libjpeg, libpng, ncurses-libs, procps, unzip, which, whois, zstd

**Install Additional Packages**:
```typescript
await sandbox.runCommand({
  cmd: 'dnf',
  args: ['install', '-y', 'golang'],
  sudo: true,
});
```

#### Timeout Limits

| Plan | Default | Maximum |
|------|---------|---------|
| Hobby | 5 minutes | 45 minutes |
| Pro/Enterprise | 5 minutes | 5 hours |

---

### 4.3 Vercel Sandbox SDK (`@vercel/sandbox`)

**Source**: [vercel.com/docs/vercel-sandbox/sdk-reference](https://vercel.com/docs/vercel-sandbox/sdk-reference)

#### Installation

```bash
pnpm i @vercel/sandbox
```

#### Authentication

```bash
# Link project and pull OIDC tokens
vercel link
vercel env pull
```

> **Note**: Development tokens expire after 12 hours. Production tokens are auto-managed.

#### Core Classes

| Class | Purpose |
|-------|---------|
| `Sandbox` | Creates/manages isolated microVM environments |
| `Command` | Handles running commands inside sandbox |
| `CommandFinished` | Contains results after command completes |

#### Sandbox Lifecycle

```typescript
import { Sandbox } from '@vercel/sandbox';

// 1. Create sandbox
const sandbox = await Sandbox.create({
  runtime: 'node24',
  ports: [3000],           // Expose ports for preview
  timeout: 300000,         // 5 minutes
});

// 2. Access properties
console.log(sandbox.sandboxId);  // Unique identifier
console.log(sandbox.status);     // "pending" | "running" | "stopping" | "stopped" | "failed"
console.log(sandbox.timeout);    // Remaining ms
console.log(sandbox.createdAt);  // Date object

// 3. Run commands
const result = await sandbox.runCommand('node', ['--version']);
console.log(result.exitCode);         // 0
console.log(await result.stdout());   // v24.x.x

// 4. Cleanup
await sandbox.stop();
```

#### Sandbox.create() Options

```typescript
const sandbox = await Sandbox.create({
  // Runtime selection
  runtime: 'node24' | 'node22' | 'python3.13',

  // Source options (mutually exclusive)
  source: {
    // Option A: Clone git repo
    type: 'git',
    url: 'https://github.com/user/repo.git',
    username: 'git-user',      // For private repos
    password: 'token',
    depth: 1,                  // Shallow clone
    revision: 'main',
  },
  // OR
  source: {
    // Option B: Mount tarball
    type: 'tarball',
    url: 'https://example.com/archive.tar.gz',
  },

  // Resources
  resources: { vcpus: 2 },

  // Networking
  ports: [3000, 8080],        // Ports to expose

  // Lifecycle
  timeout: 300000,            // Initial timeout (ms)
  signal: AbortSignal,        // Cancellation
});
```

#### Running Commands

```typescript
// Simple execution (blocks until complete)
const result = await sandbox.runCommand('npm', ['install']);

// With options
const result = await sandbox.runCommand({
  cmd: 'npm',
  args: ['run', 'build'],
  cwd: '/vercel/sandbox/app',
  env: { NODE_ENV: 'production' },
  sudo: false,
  stdout: process.stdout,     // Stream output
  stderr: process.stderr,
});

// Detached execution (returns immediately)
const command = await sandbox.runCommand({
  cmd: 'npm',
  args: ['run', 'dev'],
  detached: true,
});

// Later: wait for completion
const finished = await command.wait();

// Or stream logs in real-time
for await (const log of command.logs()) {
  if (log.stream === 'stdout') {
    process.stdout.write(log.data);
  }
}

// Kill detached command
await command.kill('SIGTERM');
```

#### File Operations

```typescript
// Create directory
await sandbox.mkDir('tmp/assets');

// Write files
await sandbox.writeFiles([
  { path: 'config.json', content: Buffer.from('{"key": "value"}') },
  { path: 'src/index.ts', content: Buffer.from('console.log("hi")') },
]);

// Read file (returns ReadableStream or null)
const stream = await sandbox.readFile({ path: 'package.json' });

// Read file to buffer
const buffer = await sandbox.readFileToBuffer({ path: 'output.json' });

// Download file to local filesystem
const localPath = await sandbox.downloadFile(
  { path: 'dist/bundle.js', cwd: '/vercel/sandbox' },
  { path: 'bundle.js', cwd: '/tmp' },
  { mkdirRecursive: true }
);
```

#### Networking & Preview

```typescript
// Create sandbox with exposed port
const sandbox = await Sandbox.create({
  runtime: 'node24',
  ports: [3000],
});

// Start dev server (detached)
await sandbox.runCommand({
  cmd: 'npm',
  args: ['run', 'dev'],
  detached: true,
});

// Get public preview URL
const previewUrl = sandbox.domain(3000);
// Returns: https://<sandbox-id>.vercel.sh
```

#### Lifecycle Management

```typescript
// List all sandboxes for a project
const { sandboxes, pagination } = await Sandbox.list({
  projectId: 'prj_xxx',
  limit: 10,
  since: Date.now() - 86400000,  // Last 24 hours
});

// Reconnect to existing sandbox
const sandbox = await Sandbox.get({ sandboxId: 'sbx_xxx' });

// Extend timeout (up to plan max)
await sandbox.extendTimeout(60000);  // Add 60 seconds

// Stop sandbox
await sandbox.stop();
```

#### Command Result Properties

```typescript
const result = await sandbox.runCommand('npm', ['test']);

result.exitCode;     // number: 0 = success
result.cmdId;        // string: unique command ID
result.cwd;          // string: working directory
result.startedAt;    // number: Unix timestamp (ms)

await result.stdout();        // string: stdout content
await result.stderr();        // string: stderr content
await result.output('both');  // string: combined output
```

---

## 5. Reference Implementations

### 5.1 OSS Data Analyst

**Repository**: [github.com/vercel-labs/oss-data-analyst](https://github.com/vercel-labs/oss-data-analyst)

#### What It Does

AI agent that explores a semantic layer in sandbox to answer natural language questions with SQL. **Key innovation**: Agent dynamically discovers schema rather than having it hardcoded.

#### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Question                             │
│              "How many companies in Tech?"                   │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                 Sandbox Instantiation                        │
│     Copies semantic YAML files into /vercel/sandbox          │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                 Schema Exploration                           │
│  Agent runs: cat catalog.yml                                 │
│  Agent runs: cat entities/companies.yml                      │
│  Agent runs: grep -r "industry" .                            │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                 SQL Construction                             │
│  SELECT COUNT(*) FROM companies WHERE industry = 'Tech'      │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                 SQLite Execution + Response                  │
│  "There are 42 companies in the Technology industry..."     │
└─────────────────────────────────────────────────────────────┘
```

#### Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Next.js |
| AI Orchestration | Vercel AI SDK |
| Execution | Vercel Sandbox |
| Database | SQLite |
| Language | TypeScript (97.4%) |

#### Key Files

| File | Purpose |
|------|---------|
| `src/lib/agent.ts` | Agent definition + system prompt |
| `src/lib/tools/sandbox.ts` | Sandbox provisioning |
| `src/lib/tools/shell.ts` | Shell command execution |
| `src/lib/tools/execute-sqlite.ts` | SQL query execution |

#### Semantic Layer Structure

```yaml
# src/semantic/catalog.yml
entities:
  - name: companies
    description: "Company records with industry and size"
  - name: people
    description: "Employee records with department and salary"

# src/semantic/entities/companies.yml
sql_table_name: companies
fields:
  - name: id
    sql: "${TABLE}.id"
  - name: industry
    sql: "${TABLE}.industry"
joins:
  - name: employees
    sql: "${TABLE}.id = people.company_id"
example_questions:
  - "How many companies are in each industry?"
```

#### Setup

```bash
git clone https://github.com/vercel-labs/oss-data-analyst.git
cd oss-data-analyst
pnpm install
cp env.local.example .env.local
# Add VERCEL_AI_GATEWAY_API_KEY to .env.local
pnpm initDatabase
pnpm dev
```

#### Why This Matters

- **No hardcoded schema**: Agent discovers structure dynamically
- **Self-healing**: Schema changes don't require code updates
- **Extensible**: Add new entities by creating YAML files

---

### 5.2 Call Summary Agent

**Template**: [vercel.com/templates/ai/call-summary-agent](https://vercel.com/templates/ai/call-summary-agent)

#### What It Does

AI-powered system for analyzing sales calls, generating structured summaries with tasks, objections, and insights.

#### Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Webhook   │───▶│  Durable    │───▶│   Sandbox   │
│   (Gong)    │    │  Workflow   │    │  Creation   │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                   ┌─────────────────────────────────┐
                   │        Agent Exploration         │
                   │  grep -r 'pricing' context/      │
                   │  cat context/transcript.md       │
                   │  cat context/metadata.json       │
                   └─────────────────────────────────┘
                                             │
                                             ▼
                   ┌─────────────────────────────────┐
                   │      Structured Output           │
                   │  { summary, tasks, objections }  │
                   └─────────────────────────────────┘
```

#### Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Next.js |
| AI | Vercel AI SDK + Claude |
| Execution | Vercel Sandbox |
| Durability | Vercel Workflow DevKit |
| Shell Access | bash-tool (npm) |

#### Output Schema

```typescript
interface CallSummary {
  summary: string;
  tasks: Array<{
    taskDescription: string;
    taskOwner: string;
    ownerCompany: 'internal' | 'customer' | 'partner';
  }>;
  objections: Array<{
    description: string;
    quote: string;
    speaker: string;
    speakerCompany: string;
    handled: boolean;
    handledScore: number;  // 0-100
  }>;
}
```

#### Key Pattern: Transcript as Codebase

Instead of processing entire transcript:
```typescript
// Agent explores like debugging code
await bash('grep -r "pricing" context/');
await bash('cat context/metadata.json');
await bash('cat context/transcript.md | head -100');
```

#### Setup

```bash
git clone https://github.com/vercel-labs/call-summary-agent
cd call-summary-agent
pnpm install
vercel link
vercel env pull
pnpm dev

# Test with mock data
curl -X POST http://localhost:3000/api/gong-webhook
```

#### Production Configuration

```bash
# Environment variables
GONG_ACCESS_KEY=xxx
GONG_SECRET_KEY=xxx
COMPANY_NAME=Acme Corp  # Optional

# Webhook endpoint
POST https://your-app.vercel.app/api/gong-webhook
```

---

### 5.3 Vibe Coding Platform (v0)

> **⭐ CORE REFERENCE** — This is the primary example to clone when building Sunder's sandbox architecture. Production-grade patterns, minimal tooling, multi-model support.

**Repository**: [github.com/vercel/examples/tree/main/apps/vibe-coding-platform](https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform)

#### What It Is

Full-stack text-to-app generation platform (the technology behind v0.dev). **Key innovation**: Demonstrates the minimal-tool philosophy in production — only 4 tools drive the entire code generation workflow.

#### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Prompt                             │
│         "Build a Pokemon search app with Next.js"            │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    AI Gateway Layer                          │
│  ├── Model routing (GPT-5.2, Claude 4.5, Gemini)            │
│  ├── Provider-specific config (reasoning, cache, headers)    │
│  └── Bot detection                                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│               Agentic Loop (max 20 steps)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ streamText() + stepCountIs(20) + tools              │   │
│  └──────────────────────────────────────────────────────┘   │
│            │           │           │           │             │
│            ▼           ▼           ▼           ▼             │
│     ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│     │ create   │ │ generate │ │   run    │ │   get    │     │
│     │ Sandbox  │ │  Files   │ │ Command  │ │ Sandbox  │     │
│     │          │ │          │ │          │ │   URL    │     │
│     └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   Vercel Sandbox                             │
│  Ephemeral microVM, ports exposed, npm/python available      │
└─────────────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    Live Preview                              │
│            https://<sandbox-id>.vercel.sh                    │
└─────────────────────────────────────────────────────────────┘
```

#### Tech Stack

| Layer | Technology |
|-------|------------|
| Framework | Next.js 16 + React 19 |
| AI SDK | Vercel AI SDK 6.0 (`ai`, `@ai-sdk/gateway`, `@ai-sdk/openai`) |
| Sandbox | `@vercel/sandbox` (0.0.17) |
| State | Zustand |
| UI | Radix UI + Tailwind v4 |
| Validation | Zod |

#### The 4-Tool Pattern

The entire code generation workflow uses only **4 tools** — a canonical example of the "80% tools removal" philosophy:

| Tool | Purpose | When Used |
|------|---------|-----------|
| `createSandbox` | Initialize ephemeral Linux container | Once per session, at start |
| `generateFiles` | Create/write files to sandbox | When scaffolding or fixing code |
| `runCommand` | Execute npm/node/python commands | Installing deps, running dev server |
| `getSandboxURL` | Get live preview URL | After starting dev server |

#### Key Files

| File | Purpose |
|------|---------|
| `ai/gateway.ts` | Multi-model routing with provider-specific config |
| `ai/tools/index.ts` | Tool factory — creates 4 tools with writer dependency |
| `ai/tools/create-sandbox.ts` | Sandbox lifecycle management |
| `ai/tools/generate-files.ts` | File generation with streaming progress |
| `ai/tools/run-command.ts` | Command execution (blocking or detached) |
| `ai/tools/*.md` | LLM instructions for each tool |
| `app/api/chat/route.ts` | Agentic loop with 20-step limit |

#### Tool Implementation Pattern

Each tool follows a consistent pattern with streaming UI updates:

```typescript
// ai/tools/create-sandbox.ts
import { tool } from "ai";
import { Sandbox } from "@vercel/sandbox";
import { z } from "zod";

export function createSandbox(writer: UIMessageWriter) {
  return tool({
    description: "Initialize an ephemeral Linux container...",
    parameters: z.object({
      timeout: z.number().min(600000).max(2700000).default(600000),
      ports: z.array(z.number()).max(2).optional(),
    }),
    execute: async ({ timeout, ports }) => {
      // 1. Write loading state for streaming UI
      writer.write({ type: "sandbox", status: "loading" });

      try {
        // 2. Create sandbox
        const sandbox = await Sandbox.create({ timeout, ports });

        // 3. Write success state
        writer.write({
          type: "sandbox",
          status: "created",
          sandboxId: sandbox.sandboxId,
        });

        return { sandboxId: sandbox.sandboxId };
      } catch (error) {
        // 4. Write error state
        writer.write({
          type: "sandbox",
          status: "error",
          error: getRichError(error),
        });
        throw error;
      }
    },
  });
}
```

#### Agentic Loop Configuration

```typescript
// app/api/chat/route.ts
import { streamText, stepCountIs } from "ai";
import { gateway } from "@/ai/gateway";
import { tools } from "@/ai/tools";

export async function POST(request: Request) {
  const { messages, modelId } = await request.json();

  // Transform error reports into text for context
  const processedMessages = messages.map(transformErrorParts);

  const result = streamText({
    model: gateway(modelId),
    messages: processedMessages,
    tools: tools(modelId, writer),  // Inject model + writer
    system: systemPrompt,           // From markdown file
    stopWhen: stepCountIs(20),      // Cap at 20 tool calls
    sendReasoning: true,            // Include thinking
  });

  return result.toDataStreamResponse();
}
```

#### Multi-Model Gateway

Provider-specific configuration for optimal performance:

```typescript
// ai/gateway.ts
export function gateway(modelId: string) {
  const provider = createGatewayProvider();

  if (modelId.includes("gpt-5")) {
    return provider(modelId, {
      providerOptions: {
        openai: {
          reasoningEffort: "high",
          encryptedReasoningContent: true,
        },
      },
    });
  }

  if (modelId.includes("claude")) {
    return provider(modelId, {
      headers: { "anthropic-beta": "fine-grained-tool-streaming" },
      providerOptions: {
        anthropic: { cacheControl: { type: "ephemeral" } },
      },
    });
  }

  return provider(modelId);
}
```

#### LLM Tool Instructions (Markdown Files)

Each tool has a `.md` file with explicit LLM instructions:

```markdown
<!-- ai/tools/create-sandbox.md -->
Use this tool ONCE per session when starting a new coding task.

**When to use:**
- User requests a new app or feature
- Need fresh environment after reset

**When NOT to use:**
- Sandbox already exists
- Only need file uploads or command execution
```

#### Setup

```bash
git clone https://github.com/vercel/examples.git
cd examples/apps/vibe-coding-platform
pnpm install

# Link to Vercel project (required for sandbox auth)
vercel link
vercel env pull

# Run dev server
pnpm dev
```

#### Why This Matters

1. **Minimal tools, maximum capability**: 4 tools generate full-stack apps
2. **Streaming-first UX**: Status updates for every operation
3. **Multi-model flexibility**: Same tools work across GPT/Claude/Gemini
4. **Step limits**: `stopWhen: stepCountIs(20)` prevents runaway loops
5. **LLM-readable instructions**: `.md` files guide tool usage without bloating schemas
6. **Production-grade patterns**: This is actual v0.dev architecture

---

## 6. Integration Patterns

### 6.1 Claude Agent SDK + Vercel Sandbox

**Source**: [vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk](https://vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk)

#### Basic Setup

```typescript
import { Sandbox } from '@vercel/sandbox';
import Anthropic from '@anthropic-ai/sdk';

// 1. Create sandbox
const sandbox = await Sandbox.create({
  runtime: 'node22',
});

// 2. Install Claude Code
await sandbox.runCommand({
  cmd: 'npm',
  args: ['install', '@anthropic-ai/claude-code'],
});

// 3. Configure network allowlist
// Only allow: api.anthropic.com, github.com, etc.
```

#### Architecture Components

| Component | Purpose |
|-----------|---------|
| Vercel Sandbox | Ephemeral microVM execution |
| Claude Agent SDK | Multi-step reasoning, tool orchestration |
| Persistent Shell | Maintains conversational state |
| MCP | Custom tool integration (GitHub, APIs) |

#### Security Model

```typescript
// Network allowlisting
const allowedDomains = [
  'api.anthropic.com',
  'github.com',
  'registry.npmjs.org',
];

// Permission system for tools
const permissions = {
  fileSystem: { read: true, write: '/vercel/sandbox' },
  network: { allowlist: allowedDomains },
  shell: { allowSudo: false },
};
```

---

### 6.2 Running AI-Generated Code Safely

**Source**: [vercel.com/kb/guide/running-ai-generated-code-sandbox](https://vercel.com/kb/guide/running-ai-generated-code-sandbox)

#### Safety Patterns

```typescript
// 1. Ephemeral environments
const sandbox = await Sandbox.create({
  timeout: 60000,  // Auto-destroy after 1 minute
});

// 2. Resource limits
const sandbox = await Sandbox.create({
  resources: { vcpus: 1 },
});

// 3. Network isolation
// Sandbox has no network by default
// Explicitly allowlist required domains

// 4. Filesystem isolation
// All changes are ephemeral
// No access to host filesystem

// 5. Artifact extraction
const output = await sandbox.readFileToBuffer({ path: 'output.json' });
await sandbox.stop();  // Destroy immediately after
```

---

### 6.3 E2B Integration (Power Path)

For Sunder's Power Path requiring network access:

```typescript
// lib/e2b-sandbox.ts
import { Sandbox } from '@e2b/code-interpreter';

interface SandboxSession {
  sandboxId: string;
  createdAt: Date;
  lastUsed: Date;
}

export async function getOrCreateSandbox(userId: string): Promise<Sandbox> {
  // Check for existing session in DB
  const existing = await db.sandboxSessions.findFirst({
    where: { userId, lastUsed: { gte: oneHourAgo } }
  });
  
  if (existing) {
    return Sandbox.connect(existing.sandboxId);
  }
  
  // Create new sandbox with pre-installed dependencies
  const sandbox = await Sandbox.create({
    template: 'sunder-agent',  // Custom template
    timeout: 60 * 60,          // 1 hour
  });
  
  // Persist session
  await db.sandboxSessions.create({
    data: { userId, sandboxId: sandbox.sandboxId }
  });
  
  return sandbox;
}
```

#### Custom E2B Template

Pre-bake dependencies to reduce cold start:

```dockerfile
# e2b-template/Dockerfile
FROM e2b/code-interpreter:latest

RUN pip install \
  anthropic \
  mcp \
  pandas \
  openpyxl \
  supabase \
  httpx

# Pre-configure MCP connections
COPY mcp-config.json /home/user/.mcp/config.json
```

#### MCP Integration Inside Sandbox

```python
# Runs INSIDE E2B sandbox
from anthropic import Anthropic
from mcp import StdioServerParameters, ClientSession
from mcp.client.stdio import stdio_client

async def run_agent_with_mcp(user_message: str, files: list[str]):
    # Connect to MCP servers (network access!)
    async with stdio_client(StdioServerParameters(
        command="npx",
        args=["-y", "@anthropic/mcp-supabase"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            # Get available tools from MCP
            tools = await session.list_tools()
            
            # Run Claude with MCP tools
            client = Anthropic()
            response = client.messages.create(
                model="claude-sonnet-4-5-20250514",
                messages=[{"role": "user", "content": user_message}],
                tools=[convert_mcp_tool(t) for t in tools],
            )
            
            return response
```

---

## 7. Decision Framework

### 7.1 When to Use Which Sandbox

| Use Case | Simple Path (Anthropic) | Power Path (E2B) | Vercel Sandbox |
|----------|-------------------------|------------------|----------------|
| Running untrusted/AI-generated code | ✅ | ✅ | ✅ |
| Interactive code playgrounds | ⚠️ Limited | ✅ | ✅ |
| Agent-based data exploration | ✅ | ✅ | ✅ |
| MCP/external API calls | ❌ | ✅ | ✅ |
| CI/CD pipelines | ❌ | ⚠️ | ⚠️ Ephemeral |
| Long-running services | ✅ 30 days | ⚠️ 1hr default | ❌ Max 5 hours |
| High-volume batch processing | ✅ Included | ⚠️ Cost | ⚠️ Cost |

### 7.2 Minimal vs Complex Tooling

| Scenario | Recommendation |
|----------|----------------|
| Text-to-SQL agents | Minimal: bash + SQL execution |
| Code generation | Minimal: filesystem + interpreter |
| Document analysis | Minimal: bash exploration |
| Multi-API orchestration | Consider: targeted MCP tools |
| Complex workflows | Consider: Workflow DevKit + minimal tools |

### 7.3 Filesystem vs RAG

| Scenario | Use Filesystem | Use RAG |
|----------|----------------|---------|
| < 1000 documents | ✅ | ⚠️ |
| 1000-10000 documents | ⚠️ | ✅ |
| > 10000 documents | ❌ | ✅ |
| Hierarchical data | ✅ | ⚠️ |
| Exact match retrieval | ✅ | ❌ |
| Semantic similarity | ⚠️ | ✅ |

### 7.4 Cost Considerations

#### E2B Pricing Model
- **Per-minute billing**: $0.05/min
- **Typical session**: 5-15 minutes = $0.25-$0.75
- **Heavy user (1hr/day)**: ~$90/month

#### Cost Control Strategies
1. **Timeout limits**: Auto-terminate idle sandboxes
2. **User quotas**: Limit power-path minutes per user/org
3. **Warm pool**: Keep 1-2 sandboxes warm for fast starts
4. **Usage alerts**: Notify on unusual consumption

#### Break-even Analysis

| Scenario | E2B Cost | Value Delivered |
|----------|----------|-----------------|
| 10 min power session | $0.50 | Saved 2hr manual work |
| External API integration | $1.00 | Enabled new use case |
| Multi-agent orchestration | $2.00 | 10x quality improvement |

**Verdict**: Cost is negligible compared to value if used for genuinely complex tasks.

---

## 8. Implementation Playbook

### Phase 1: Ship Current Plan (No Change)
**Timeline**: As planned
**Goal**: Get AI Analyst live with Anthropic container

- Complete Part 1 (Backend) and Part 2 (UI)
- Ship to users
- Gather feedback on limitations hit in practice

### Phase 2: Add Power Path Toggle
**Timeline**: 1-2 weeks after Phase 1
**Goal**: Allow explicit opt-in to E2B sandbox

**Changes**:
1. Add E2B SDK to Vercel functions
2. Create "Power Mode" toggle in UI
3. Route requests based on toggle
4. Session management for E2B sandbox IDs
5. Cost tracking/alerts

```typescript
// api/chat.ts - routing logic
if (request.powerMode) {
  return handlePowerPath(request);  // E2B
} else {
  return handleSimplePath(request); // Anthropic container
}
```

### Phase 3: Intelligent Auto-Routing
**Timeline**: Future / As needed
**Goal**: Automatically detect when Power path is needed

**Signals for auto-upgrade**:
- User mentions "call API", "fetch from", "connect to"
- Task requires MCP tool not available in container
- User explicitly requests package not in skills
- Claude requests network access and fails

---

## 9. Open Questions & Future Work

### Technical Questions

| Question | Options | Status |
|----------|---------|--------|
| Session handoff | Can we migrate mid-conversation from Simple → Power path? | Open |
| File sync | How do we sync files between Anthropic container and E2B? | Open |
| Credential management | How do we securely pass API keys to E2B sandbox? | Open |
| MCP server hosting | Where do MCP servers run? (Sidecar in E2B? Separate service?) | Open |
| Fallback behavior | What happens if E2B is down? | Open |

### Decision Points (Before Phase 2)

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Sandbox provider | E2B, Modal, Fly | E2B (best DX for agents) |
| Auto vs manual routing | Auto-detect, manual toggle, or hybrid | Start with manual toggle |
| MCP server location | In-sandbox, separate service | In-sandbox (simpler) |
| Cost model | Pass-through, bundled, freemium | Bundled in enterprise tier |

---

## 10. Sources & References

### Official Documentation

| Resource | URL |
|----------|-----|
| Vercel Sandbox Docs | https://vercel.com/docs/vercel-sandbox |
| Sandbox SDK Reference | https://vercel.com/docs/vercel-sandbox/sdk-reference |
| Sandbox Pricing | https://vercel.com/docs/vercel-sandbox/pricing |
| E2B Documentation | https://e2b.dev/docs |
| Claude Agent SDK | https://docs.anthropic.com/en/docs/agents-and-tools/claude-agent-sdk |
| MCP Protocol | https://modelcontextprotocol.io |

### Blog Posts & Guides

| Resource | URL |
|----------|-----|
| 80% Tools Removal | https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools |
| Filesystem-Based Agents | https://vercel.com/blog/how-to-build-agents-with-filesystems-and-bash |
| Claude Agent SDK Guide | https://vercel.com/kb/guide/using-vercel-sandbox-claude-agent-sdk |
| AI-Generated Code Safety | https://vercel.com/kb/guide/running-ai-generated-code-sandbox |
| Files Are All You Need | https://www.llamaindex.ai/blog/files-are-all-you-need |

### Case Studies & Field Reports

| Resource | Description |
|----------|-------------|
| [Fintool - Lessons Building AI Agents for Financial Services](../../../03_Resources/Industry%20Intel/Fintool%20-%20Lessons%20Building%20AI%20Agents%20for%20Financial%20Services.md) | Nicolas Bustamante's battle-tested insights from 2 years building AI agents for professional investors. Covers: sandbox architecture with ABAC, S3-first data layer, skill shadowing systems, Temporal for long-running tasks, domain-specific evals. **Highly recommended.** |

### Reference Implementations

| Resource | URL |
|----------|-----|
| OSS Data Analyst | https://github.com/vercel-labs/oss-data-analyst |
| Call Summary Agent | https://vercel.com/templates/ai/call-summary-agent |
| Vibe Coding Platform | https://github.com/vercel/examples/tree/main/apps/vibe-coding-platform |
| Jerry Liu's Form Filler | https://github.com/jerryjliu/form_filling_app |

### NPM Packages

| Package | Purpose |
|---------|---------|
| `@vercel/sandbox` | Sandbox SDK |
| `bash-tool` | Generic shell access for AI SDK |
| `@anthropic-ai/claude-code` | Claude Code integration |
| `@e2b/code-interpreter` | E2B Code Interpreter SDK |

---

## 11. Appendix: Quick Start Template

```typescript
/**
 * Minimal AI Agent with Vercel Sandbox
 *
 * Pattern: Filesystem-based exploration with minimal tooling
 */
import { Sandbox } from '@vercel/sandbox';
import { generateText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

async function runAgent(question: string) {
  // 1. Create sandbox with context
  const sandbox = await Sandbox.create({ runtime: 'node24' });

  try {
    // 2. Write context files
    await sandbox.writeFiles([
      { path: 'context/data.json', content: Buffer.from(JSON.stringify(data)) },
      { path: 'context/schema.yml', content: Buffer.from(schemaYaml) },
    ]);

    // 3. Define minimal tools
    const tools = {
      bash: {
        description: 'Execute bash commands in sandbox',
        parameters: { command: { type: 'string' } },
        execute: async ({ command }) => {
          const result = await sandbox.runCommand('bash', ['-c', command]);
          return await result.stdout();
        },
      },
    };

    // 4. Run agent loop
    const response = await generateText({
      model: anthropic('claude-sonnet-4-20250514'),
      tools,
      system: `You are a data analyst. Use bash commands (ls, cat, grep, find)
               to explore the context/ directory and answer questions.`,
      prompt: question,
    });

    return response.text;
  } finally {
    await sandbox.stop();
  }
}
```

---

## 12. Philosophy & Strategic Notes

> *Added: 2026-01-18 — Raw thinking on the future of agentic work*

### Code Is the Final Action Space Abstraction Layer

**The final frontier of agents is solved** — and it's code execution.

Excel generation is just *one skill* among many that Claude Code could learn and execute. With MCP + network access, there's **no theoretical limit** to what Claude Code could do. Every action in the digital world can be expressed as code.

### The Role of Human Steering

For **local execution** (no untrusted code, developer workflows), you don't need a VM — Claude Code runs directly.

However, a complex set of auto-invoked skills and instructions can lead to **random/unpredictable outcomes** without human steering. This is why humans still exist in coding workflows (for how long, we don't know 🤷).

But here's the insight:

> **If work is a fixed, repeatable workflow** (e.g., Excel generation → Fill up ERP → Send email), you can isolate each step to a VM and chain them together deterministically.

### Multi-Skill VM Architecture

**Key realization**: You can have different folders/repos within a single VM.

```
/vercel/sandbox/
├── skills/
│   ├── excel-generator/      # Skill 1
│   ├── erp-integration/      # Skill 2
│   └── email-sender/         # Skill 3
├── workflows/
│   └── reconciliation-pipeline/
└── context/
    └── user-data/
```

### Strategic Implication for Sunder

Once we nail **Excel generation** as a skill, the next move is:

1. **Keep the same VM infrastructure** (E2B / Vercel Sandbox)
2. **Add new "work types"** as skills (ERP data entry, email drafting, report generation, etc.)
3. **Chain skills into workflows** for fixed, repeatable admin tasks

The VM infra becomes a **platform for automating knowledge work** — not just a one-off feature.

### The Vision

```
┌────────────────────────────────────────────────────────────┐
│                    SUNDER SKILL PLATFORM                    │
├────────────────────────────────────────────────────────────┤
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌─────────┐ │
│  │  Excel   │──▶│   ERP    │──▶│  Email   │──▶│  Done!  │ │
│  │   Gen    │   │  Upload  │   │  Draft   │   │         │ │
│  └──────────┘   └──────────┘   └──────────┘   └─────────┘ │
│       ▲              ▲              ▲                      │
│       └──────────────┴──────────────┘                      │
│              Human steering (when needed)                   │
└────────────────────────────────────────────────────────────┘
```

---

---

## 13. Claude Agent SDK Deep Dive

> *Added: 2026-01-19 — Comprehensive guide based on official docs and Nader Dabit's tutorial*
>
> **Sources:**
> - [Hosting](https://platform.claude.com/docs/en/agent-sdk/hosting)
> - [File Checkpointing](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)
> - [Secure Deployment](https://platform.claude.com/docs/en/agent-sdk/secure-deployment)
> - [TypeScript SDK Reference](https://platform.claude.com/docs/en/agent-sdk/typescript)
> - [Nader Dabit's Complete Guide](https://x.com/dabit3/status/2009131298250428923)

### 13.1 What the SDK Gives You

The Claude Agent SDK is the same engine behind Claude Code, exposed as a library. It handles:

- **The agent loop** — no more manual tool execution cycles
- **Built-in tools** — Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
- **Context management** — session persistence, file checkpointing
- **Subagent orchestration** — delegate tasks to specialized agents

```typescript
// Without the SDK: You manage the loop
let response = await client.messages.create({...});
while (response.stop_reason === "tool_use") {
  const result = yourToolExecutor(response.tool_use);
  response = await client.messages.create({ tool_result: result, ... });
}

// With the SDK: Claude manages it
for await (const message of query({ prompt: "Fix the bug in auth.py" })) {
  console.log(message); // Claude reads, finds bugs, edits code
}
```

### 13.2 Installation & Setup

```bash
# Install Claude Code CLI (required runtime)
npm install -g @anthropic-ai/claude-code

# Install SDK
npm install @anthropic-ai/claude-agent-sdk

# Set API key
export ANTHROPIC_API_KEY=your-api-key
```

### 13.3 Basic Agent Pattern

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

async function main() {
  for await (const message of query({
    prompt: "What files are in this directory?",
    options: {
      model: "opus",
      allowedTools: ["Glob", "Read"],
      maxTurns: 250
    }
  })) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text);
        }
      }
    }

    if (message.type === "result") {
      console.log("\nDone:", message.subtype);
    }
  }
}
```

### 13.4 Message Stream Types

| Message Type | Description |
|--------------|-------------|
| `system` | Session initialization (session_id, tools, model) |
| `assistant` | Claude's responses and tool calls |
| `user` | User messages (with checkpoint UUIDs) |
| `result` | Final result with cost, usage, success/error |
| `stream_event` | Partial messages (if `includePartialMessages: true`) |

### 13.5 Structured Output

Force JSON schema output for programmatic consumption:

```typescript
const reviewSchema = {
  type: "object",
  properties: {
    issues: {
      type: "array",
      items: {
        type: "object",
        properties: {
          severity: { type: "string", enum: ["low", "medium", "high", "critical"] },
          category: { type: "string", enum: ["bug", "security", "performance", "style"] },
          file: { type: "string" },
          line: { type: "number" },
          description: { type: "string" },
          suggestion: { type: "string" }
        },
        required: ["severity", "category", "file", "description"]
      }
    },
    summary: { type: "string" },
    overallScore: { type: "number" }
  },
  required: ["issues", "summary", "overallScore"]
};

const response = query({
  prompt: "Review this codebase",
  options: {
    outputFormat: { type: "json_schema", schema: reviewSchema }
  }
});
```

### 13.6 Permission Modes

| Mode | Description |
|------|-------------|
| `default` | Standard permission behavior (prompts for approval) |
| `acceptEdits` | Auto-accept file edits |
| `bypassPermissions` | Skip all permission checks (requires `allowDangerouslySkipPermissions: true`) |
| `plan` | Planning mode — no execution |

**Custom permission handler:**

```typescript
options: {
  canUseTool: async (toolName, input) => {
    if (["Read", "Glob", "Grep"].includes(toolName)) {
      return { behavior: "allow", updatedInput: input };
    }
    if (toolName === "Write" && input.file_path?.includes(".env")) {
      return { behavior: "deny", message: "Cannot modify .env files" };
    }
    return { behavior: "allow", updatedInput: input };
  }
}
```

### 13.7 Subagents

Delegate complex tasks to specialized agents:

```typescript
options: {
  allowedTools: ["Read", "Glob", "Grep", "Task"], // Task enables subagents
  agents: {
    "security-reviewer": {
      description: "Security specialist for vulnerability detection",
      prompt: `You are a security expert. Focus on:
- SQL injection, XSS, CSRF vulnerabilities
- Exposed credentials and secrets
- Insecure data handling`,
      tools: ["Read", "Grep", "Glob"],
      model: "sonnet"
    },
    "test-analyzer": {
      description: "Test coverage and quality analyzer",
      prompt: `Analyze test coverage gaps and quality`,
      tools: ["Read", "Grep", "Glob"],
      model: "haiku" // Faster model for simpler tasks
    }
  }
}
```

### 13.8 Hooks

Intercept and customize agent behavior:

```typescript
const auditLogger: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse") {
    console.log(`[AUDIT] ${new Date().toISOString()} - ${input.tool_name}`);
  }
  return {};
};

const blockDangerousCommands: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse" && input.tool_name === "Bash") {
    const command = input.tool_input?.command || "";
    if (command.includes("rm -rf") || command.includes("sudo")) {
      return {
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "deny",
          permissionDecisionReason: "Dangerous command blocked"
        }
      };
    }
  }
  return {};
};

options: {
  hooks: {
    PreToolUse: [
      { hooks: [auditLogger] },
      { matcher: "Bash", hooks: [blockDangerousCommands] }
    ]
  }
}
```

**Available hooks:** `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `Notification`, `UserPromptSubmit`, `SessionStart`, `SessionEnd`, `Stop`, `SubagentStart`, `SubagentStop`, `PreCompact`, `PermissionRequest`

### 13.9 Custom MCP Tools

Extend Claude with custom tools:

```typescript
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

const customServer = createSdkMcpServer({
  name: "code-metrics",
  version: "1.0.0",
  tools: [
    tool(
      "analyze_complexity",
      "Calculate cyclomatic complexity for a file",
      { filePath: z.string().describe("Path to the file to analyze") },
      async (args) => {
        const complexity = calculateComplexity(args.filePath);
        return {
          content: [{
            type: "text",
            text: `Cyclomatic complexity for ${args.filePath}: ${complexity}`
          }]
        };
      }
    )
  ]
});

const response = query({
  prompt: "Analyze complexity of main.ts",
  options: {
    mcpServers: { "code-metrics": customServer },
    allowedTools: ["Read", "mcp__code-metrics__analyze_complexity"]
  }
});
```

### 13.10 File Checkpointing

Track file changes and rewind to any previous state:

```typescript
const opts = {
  enableFileCheckpointing: true,
  permissionMode: "acceptEdits",
  extraArgs: { 'replay-user-messages': null }, // Required for checkpoint UUIDs
  env: { ...process.env, CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING: '1' }
};

let checkpointId: string | undefined;
let sessionId: string | undefined;

const response = query({ prompt: "Refactor auth module", options: opts });

for await (const message of response) {
  // Capture first user message UUID as checkpoint
  if (message.type === 'user' && message.uuid && !checkpointId) {
    checkpointId = message.uuid;
  }
  if ('session_id' in message && !sessionId) {
    sessionId = message.session_id;
  }
}

// Later: rewind to checkpoint
if (checkpointId && sessionId) {
  const rewindQuery = query({
    prompt: "",
    options: { ...opts, resume: sessionId }
  });
  for await (const msg of rewindQuery) {
    await rewindQuery.rewindFiles(checkpointId);
    break;
  }
}
```

**Limitations:**
- Only tracks Write, Edit, NotebookEdit tools (not Bash file operations)
- Checkpoints tied to the session that created them
- File content only (not directory operations)

### 13.11 Session Management

Resume conversations and fork sessions:

```typescript
// Initial query
let sessionId: string;
for await (const message of query({ prompt: "Review this codebase" })) {
  if (message.type === "system" && message.subtype === "init") {
    sessionId = message.session_id;
  }
}

// Continue conversation
for await (const message of query({
  prompt: "Now fix the most critical issue",
  options: { resume: sessionId }
})) {
  // Claude remembers previous context
}

// Fork to new session (preserves history, new ID)
for await (const message of query({
  prompt: "Try an alternative approach",
  options: { resume: sessionId, forkSession: true }
})) {
  // Creates new session branched from original
}
```

### 13.12 Hosting Patterns

#### Pattern 1: Ephemeral Sessions
Create container per task, destroy when complete.

**Best for:** One-off tasks, bug investigation, invoice processing, translation

#### Pattern 2: Long-Running Sessions
Persistent containers running multiple Claude processes.

**Best for:** Proactive agents, site builders, high-frequency chat bots

#### Pattern 3: Hybrid Sessions
Ephemeral containers hydrated with history/state from database or session resumption.

**Best for:** Intermittent interaction, deep research, customer support spanning multiple interactions

#### Pattern 4: Single Containers
Multiple Claude processes in one global container.

**Best for:** Agent simulations, closely collaborating agents

### 13.13 Secure Deployment

#### Isolation Technologies

| Technology | Isolation Strength | Performance | Complexity |
|------------|-------------------|-------------|------------|
| Sandbox runtime | Good | Very low | Low |
| Containers (Docker) | Setup dependent | Low | Medium |
| gVisor | Excellent | Medium/High | Medium |
| VMs (Firecracker) | Excellent | High | Medium/High |

#### Credential Management: The Proxy Pattern

Run a proxy **outside** the agent's security boundary that injects credentials:

```
┌─────────────────────────────────────────┐
│  Agent Container (no credentials)       │
│  ┌─────────────────────────────────────┐│
│  │ Claude sends request without creds  ││
│  └──────────────┬──────────────────────┘│
└─────────────────┼───────────────────────┘
                  │ Unix socket / HTTP
┌─────────────────┼───────────────────────┐
│  Proxy (outside │ security boundary)    │
│  ├── Validates │ request                │
│  ├── Injects credentials                │
│  ├── Forwards to external API           │
│  └── Logs for audit                     │
└─────────────────────────────────────────┘
```

**Configure Claude to use proxy:**
```bash
# Option 1: Sampling API only
export ANTHROPIC_BASE_URL="http://localhost:8080"

# Option 2: System-wide
export HTTP_PROXY="http://localhost:8080"
export HTTPS_PROXY="http://localhost:8080"
```

#### Docker Security Hardening

```bash
docker run \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  --network none \
  --memory 2g \
  --cpus 2 \
  --pids-limit 100 \
  --user 1000:1000 \
  -v /path/to/code:/workspace:ro \
  -v /var/run/proxy.sock:/var/run/proxy.sock:ro \
  agent-image
```

**Key flags:**
- `--cap-drop ALL` — Remove dangerous Linux capabilities
- `--network none` — No network interfaces; communicate via Unix socket only
- `--read-only` — Immutable root filesystem
- `-v ...:/workspace:ro` — Mount code read-only

⚠️ **Never mount:** `~/.ssh`, `~/.aws`, `~/.config`, `~/.docker/config.json`, `*.pem`, `*.key`

#### Sandbox Settings (Programmatic)

```typescript
options: {
  sandbox: {
    enabled: true,
    autoAllowBashIfSandboxed: true,
    excludedCommands: ['docker'], // Always bypass sandbox
    allowUnsandboxedCommands: false, // Model can't escape
    network: {
      allowLocalBinding: true, // For dev servers
      allowUnixSockets: ['/var/run/docker.sock']
    }
  }
}
```

### 13.14 Cost Tracking

```typescript
for await (const message of query({ prompt: "..." })) {
  if (message.type === "result" && message.subtype === "success") {
    console.log("Total cost:", message.total_cost_usd);
    console.log("Token usage:", message.usage);

    // Per-model breakdown (useful with subagents)
    for (const [model, usage] of Object.entries(message.modelUsage)) {
      console.log(`${model}: $${usage.costUSD.toFixed(4)}`);
    }
  }
}
```

### 13.15 Production Code Review Agent (Complete Example)

```typescript
import { query, AgentDefinition } from "@anthropic-ai/claude-agent-sdk";

interface ReviewResult {
  issues: Array<{
    severity: "low" | "medium" | "high" | "critical";
    category: "bug" | "security" | "performance" | "style";
    file: string;
    line?: number;
    description: string;
    suggestion?: string;
  }>;
  summary: string;
  overallScore: number;
}

async function runCodeReview(directory: string): Promise<ReviewResult | null> {
  let result: ReviewResult | null = null;

  for await (const message of query({
    prompt: `Perform a thorough code review of ${directory}.
Analyze all source files for bugs, security vulnerabilities,
performance issues, and code quality.`,
    options: {
      model: "opus",
      allowedTools: ["Read", "Glob", "Grep", "Task"],
      permissionMode: "bypassPermissions",
      allowDangerouslySkipPermissions: true,
      maxTurns: 250,
      outputFormat: {
        type: "json_schema",
        schema: reviewSchema
      },
      agents: {
        "security-scanner": {
          description: "Deep security analysis",
          prompt: `Scan for injection vulnerabilities, auth flaws,
                   sensitive data exposure, insecure dependencies`,
          tools: ["Read", "Grep", "Glob"],
          model: "sonnet"
        } as AgentDefinition
      }
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      result = message.structured_output as ReviewResult;
      console.log(`✅ Review complete! Cost: $${message.total_cost_usd.toFixed(4)}`);
    }
  }

  return result;
}
```

---

*Document consolidated from research conducted on 2026-01-16 and Sunder hybrid architecture design on 2026-01-18. Claude Agent SDK section added 2026-01-19. All links verified at time of creation.*
