---
type: raw_capture
source_type: web
title: "Sunder sync: 15-vercel-labs-just-bash-FULL.md"
url: "https://github.com/vercel-labs/just-bash"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/15-vercel-labs-just-bash-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/15-vercel-labs-just-bash-FULL.md"
sha256: "77b783c2170d9e08418fca5e5246e347439bec3e822696c99834f14d71ae25b0"
duplicate_of: ""
---

# Sunder sync: 15-vercel-labs-just-bash-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/15-vercel-labs-just-bash-FULL.md`

Primary URL: https://github.com/vercel-labs/just-bash

Duplicate of existing source-map entry: `none`

## Capture Text

# Vercel Labs - just-bash: Bash for Agents

**Repository:** vercel-labs/just-bash
**URL:** https://github.com/vercel-labs/just-bash
**Website:** https://justbash.dev/
**License:** Apache-2.0

## Overview

**Bash for Agents** - A specialized bash environment designed for AI agent execution

## Repository Stats

- **Stars:** 519
- **Forks:** 40
- **Latest commit:** "Add agent to the website (#73)" by cramforce - Feb 1, 2026
- **License:** Apache-2.0

## Key Features

### Network Access

- **Optional network access** with secure-by-default URL filtering
- Network enabled via:
  - URL prefix allow-lists
  - HTTP-method allow-lists
- Secure by default (network disabled unless explicitly allowed)

### Security Model

- **Secure-by-default** architecture
- Optional network access (not enabled by default)
- URL filtering for allowed network calls
- HTTP method restrictions

### Limitations

- **Beta software** - use at your own risk
- **Binaries/WASM inherently unsupported**
  - Use alternative tools for full VM requirements

## Repository Structure

### Key Files

- **AGENTS.md** - Agent configuration and documentation
- **AGENTS.npm.md** - NPM-specific agent docs
- **CLAUDE.md** - Claude-specific integration docs
- **README.md** - Main documentation
- **LICENSE** - Apache-2.0 license

### Directories

- **examples/** - Example agent implementations
- **src/** - Source code

## Use Cases

### For AI Agents

- Execute bash commands in controlled environment
- Secure command execution with network restrictions
- Agent-friendly bash interface

### Security-Conscious Applications

- Run untrusted bash with network controls
- Sandbox bash execution
- Controlled external access

### Development & Testing

- Test agent bash interactions
- Validate agent command execution
- Safe experimentation environment

## Technical Details

### Security Features

1. **Network isolation** by default
2. **Allowlist-based** network access
3. **URL filtering** for network calls
4. **HTTP method restrictions**
5. **No binary/WASM execution**

### Agent Integration

- **AGENTS.md** - Agent configuration
- **CLAUDE.md** - Claude Code integration
- **NPM support** - Package management for agents

## Key Takeaways

1. **Purpose-built for agents** - not general-purpose bash
2. **Security first** - network disabled by default
3. **Controlled access** - allowlist-based network
4. **Beta status** - production use at own risk
5. **Vercel Labs project** - experimental/research

## Comparison to Standard Bash

### Differences

| Feature | just-bash | Standard Bash |
|---------|-----------|---------------|
| Network | Optional, restricted | Unrestricted |
| Binary execution | Not supported | Supported |
| WASM | Not supported | Via tools |
| Security model | Allowlist-based | Open |
| Primary use case | AI agents | General purpose |

## Installation & Usage

See:
- **Website:** https://justbash.dev/
- **Repository:** https://github.com/vercel-labs/just-bash
- **Docs:** AGENTS.md, CLAUDE.md, README.md

## Context in Agent Ecosystem

### Why This Matters

AI agents need to execute bash commands, but:
- Standard bash is too permissive
- Unrestricted network access is dangerous
- Binary execution expands attack surface

### just-bash Solution

Provides **secure-by-default bash** specifically designed for agent use cases:
- Network optional and controlled
- No binary execution
- URL/method filtering
- Agent-friendly interface

## Category

Agent Infrastructure, Security, Developer Tools, Bash

## Related

- **Company:** Vercel Labs (experimental projects)
- **Integration:** Vercel Sandbox, Claude Code
- **Security:** Allowlist-based, secure-by-default
- **Status:** Beta (use at own risk)
- **Alternatives:** Full VM for binary/WASM needs

