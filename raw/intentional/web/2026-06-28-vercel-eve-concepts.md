---
type: raw_capture
source_type: web
title: "Vercel Eve Concepts"
url: "https://vercel.com/docs/eve/concepts"
collected_at: 2026-06-28T08:13:08Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Vercel Eve Concepts

Source: https://vercel.com/docs/eve/concepts

## Capture Text

Search
Docs
⌘ K
Start
Getting started
Fundamentals
Frameworks
Incremental Migration
Production Checklist
Build AI apps
AI Gateway
AI SDK
MCP
Vercel Connect
beta
eve
beta
Agent Resources
Run agents and backends
Functions
Fluid Compute
Routing Middleware
Cron Jobs
Queues
beta
Workflows
Sandbox
Ship and scale
Projects
Git
Drop
new
CLI
Monorepos
Builds
Deployments
Domains
Vercel for Platforms
Routing
CDN
Microfrontends
Storage
Integrations
Vercel Agent
Observe and improve
Observability
Vercel Toolbar
Feature Flags
Rolling Releases
Instant Rollback
Secure and govern
Firewall
Bot Management
BotID
Deployment Protection
Passport
beta
Identity & Access
Networking
Security & Compliance
Manage
Pricing
Plans
Spend Management
Limits
Notifications
Support Center
Reference
Project Configuration
REST API
Vercel SDK
Build Output API
Webhooks
Marketplace APIs
Checks
Errors
Glossary
eve
beta
Overview
Concepts
Pricing and Limits
Observability
Copy page
Concepts
Copy page
eve turns a filesystem project into a durable backend AI agent. You author the agent under an
agent/
directory, and eve discovers those files, validates them, compiles a manifest, and serves
the runtime as a deployable app.
Agent project
An eve agent is a set of named files and directories under
agent/
. Directories are
auto-discovered by name, so adding a capability is usually as simple as adding a file:
agent/instructions.md
: the always-on system prompt.
agent/agent.ts
: runtime config, such as model and options, through
defineAgent
.
agent/tools/*.ts
: one typed tool per file; the filename becomes the runtime tool name.
agent/skills/*
: optional, on-demand procedures the model loads only when relevant.
agent/subagents/*
: optional child agents the model delegates focused subtasks to.
agent/channels/*
: platform entry points such as HTTP and Slack.
agent/connections/*
: typed integrations with external services.
agent/sandbox/*
: the agent's isolated compute environment.
agent/instrumentation.ts
: optional OpenTelemetry setup for AI SDK spans.
Runtime config
The
agent/agent.ts
file defines the agent runtime. The most important setting is the model:
agent/agent.ts
import
{ defineAgent }
from
'eve'
;
export
default
defineAgent
({
model
:
'openai/gpt-5.4-mini'
,
});
Model strings resolve through
AI Gateway
on Vercel, so deployed agents can use
Vercel OIDC instead of managing provider API keys directly.
Sessions and turns
A session is the durable conversation or task started by a channel or HTTP request. Each user
message or external event creates a turn. During a turn, the agent can call tools, load skills, read
or write sandbox files, delegate to
subagents
, and stream lifecycle events back to the
client.
eve exposes HTTP routes for creating a session and attaching to its stream:
curl
-X
POST
http://127.0.0.1:
3000
/eve/v1/session
\
-H
'content-type: application/json'
\
-d
'{"message":"Summarize this repository"}'
The response includes an
x-eve-session-id
header. Use that id to reattach to the stream:
curl
http://127.0.0.1:
3000
/eve/v1/session/
<
sessionI
d
>
/stream
Durability
eve sessions run on top of
Vercel Workflows
. Workflows persist progress as an
event log and deterministically replay it to reconstruct state, so a session can survive cold
starts, redeploys, and long pauses while it waits for the next message or a tool result.
On Vercel, the compiled agent runs from
Vercel Functions
. Because agent turns are
long-running and stream incrementally, eve benefits from
Fluid Compute
,
which is enabled by default for new projects.
Channels
Channels are entry points into the same agent runtime. A channel can start sessions, route platform
events into turns, and apply platform-specific authentication or formatting. eve agents can expose
HTTP routes and can add channel files for platforms such as Slack.
Route-auth secrets, preview-protection bypass secrets, and other channel-specific configuration live
in project
environment variables
.
Tools and skills
Tools are typed actions the model can call during a turn. Each file in
agent/tools/
defines one
tool, and the filename becomes the tool name the model sees. Learn more about
adding tools to your eve agent
.
Skills are larger procedures or reference material that the model loads on demand. Use skills for
repeatable workflows, multi-step instructions, or domain knowledge that should not be part of the
always-on prompt. Keeping skills separate helps the model use the right context only when it is
relevant.
Install skills into
agent/skills/
with the
skills CLI
from your eve project directory.
Subagents
A subagent is a child agent that the model delegates a focused subtask to. Use one to run work in
parallel, give a child a narrower set of tools, or give a specialist its own identity. Unlike a
skill, which adds instructions to the running agent, a subagent runs as a separate agent with fresh
conversation history and state. eve offers two kinds: the built-in
agent
tool delegates to a copy
of the current agent, and declared subagents live under
agent/subagents/*
with their own config.
Learn more about
using subagents with eve
.
Connections
Connections describe typed integrations with external services. Use them to keep provider-specific
configuration and credential access outside the model prompt and tool implementation details.
For delegated user or team credentials, pair eve tools with
Vercel Connect
. For
model access, use
AI Gateway
model strings in the agent config.
Sandbox
Every eve agent has one sandbox: an isolated, bash-style compute environment with its own
filesystem. Framework tools such as
bash
,
read_file
, and
write_file
target it, and authored
tools can target it too.
On Vercel, the sandbox can run on
Vercel Sandbox
, using ephemeral microVMs for
untrusted or model-generated commands.
Observability
Every eve project gets Agent Runs in the Vercel dashboard. Agent Runs shows sessions, turns, tool
calls, reasoning, timing, and token usage without an
instrumentation.ts
file.
As the deployer, where your agent processes personal, sensitive, or regulated data, you may be
required to disclose this capture as required by applicable laws and in your privacy materials.
If you also want AI SDK spans in an external OpenTelemetry backend, add
agent/instrumentation.ts
.
See
eve observability
for the dashboard view and OpenTelemetry setup.
Next steps
Getting started
: create your first eve project.
Pricing and Limits
: understand the Vercel resources eve uses.
Observability
: inspect Agent Runs and optional OpenTelemetry spans.
Last updated
June 19, 2026
Previous
eve
Next
Pricing and Limits
Was this helpful?
supported.
Send
On this page
Agent project
Runtime config
Sessions and turns
Durability
Channels
Tools and skills
Subagents
Connections
Sandbox
Observability
Next steps
