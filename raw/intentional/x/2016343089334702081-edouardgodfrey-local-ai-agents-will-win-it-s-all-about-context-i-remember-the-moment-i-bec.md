---
type: raw_capture
source_type: x
url: https://x.com/EdouardGodfrey/status/2016343089334702081
original_url: https://x.com/EdouardGodfrey/status/2016343089334702081
author: "Edouard Godfrey"
handle: EdouardGodfrey
status_id: 2016343089334702081
captured_at: 2026-06-19T19:58:52+08:00
published_at: "Wed Jan 28 02:50:28 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 5
  reposts: 5
  likes: 43
---

# X post by @EdouardGodfrey

## Source

- Original: [https://x.com/EdouardGodfrey/status/2016343089334702081](https://x.com/EdouardGodfrey/status/2016343089334702081)
- Canonical: [https://x.com/EdouardGodfrey/status/2016343089334702081](https://x.com/EdouardGodfrey/status/2016343089334702081)
- Author: Edouard Godfrey (@EdouardGodfrey)

## Verbatim Text

Local AI agents will win. It's all about context.

I remember the moment I became Cursor-pilled.

On the surface, it did exactly what I was already doing with ChatGPT. Write code with an LLM. Copy code in, get suggestions, paste them back. Cursor seemed like a nicer wrapper around the same workflow.

Then I stopped copy-pasting. And everything changed.

The model wasn't smarter. But it could see my codebase. It stopped asking "what framework are you using?" It stopped hallucinating import paths. The friction vanished - not because the model improved, but because it found its own context.

At [Fintool](https://fintool.com), we build AI agents for financial research. Our architecture works fine: users upload documents, our agent runs in a remote sandbox with Bash access, results come back. It's robust. It scales.

But when Claude Cowork launched, I felt that Cursor feeling again.

The agent runs locally. It sees your browser - authenticated, with your sessions, your tabs. It sees your entire file system. No more janky MCP connectors to Sharepoint that barely work and can't manage context. No more uploading. No more describing what you're looking at.

Everything a human can do on their machine, the agent can do.

That's not the paradigm we have in the cloud. In a cloud sandbox, the agent only sees what you curate - what you copy-paste, drag-drop, upload, describe in your prompt. It can't check your Google Calendar to tell someone you're running five minutes late. It can't pull up that PDF you downloaded last week. It waits for you to provide context instead of finding it.

Then I realized what makes [Cowork](https://claude.com/blog/cowork-research-preview) work for knowledge workers: it's the sandbox.

The agent runs in a VM - a full Linux filesystem inside Apple's virtualization framework. It can rm -rf / all day. Nothing on your real machine is affected.

This seemed worth diving into. What does it actually take to contain an agent? I built a prototype to find out: [https://github.com/edouard-blocktool/local-agent](https://github.com/edouard-blocktool/local-agent)

## The Prototype

```
┌───────────────────────────────────────────────────────────┐
│                      HOST (macOS)                         │
│                                                           │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐     │
│  │  Client  │    │  Chrome  │◄──►│  Playwright MCP  │     │
│  │   CLI    │    │  Browser │    │ (browser control)│     │
│  └────┬─────┘    └──────────┘    └────────┬─────────┘     │
│       │                                   │               │
│       │ TCP :9999                         │               │
│       │            ~/Desktop              │               │
│       │                │                  │               │
│ ══════│════════════════│══════════════════│═══════════════│
│       │                │ mount            │               │
│       ▼                ▼                  ▼               │
│  ┌────────────────────────────────────────────────────┐   │
│  │               LIMA VM (Ubuntu)                     │   │
│  │                                                    │   │
│  │   /mnt/desktop ◄── ~/Desktop (read-write)         │   │
│  │   /opt/agent   ◄── agent code (read-only)         │   │
│  │                                                    │   │
│  │   ┌────────────────────────────────────────────┐   │   │
│  │   │             Agent Server                   │   │   │
│  │   │        (Claude + Bash/Read/Write)          │   │   │
│  │   └────────────────────────────────────────────┘   │   │
│  │                                                    │   │
│  └────────────────────────────────────────────────────┘   │
│                                                           │
└───────────────────────────────────────────────────────────┘

```

There are three risks to manage with a local agent: destruction (deleting your files), exfiltration (leaking your data), and unintended action (sending emails you didn't approve). This prototype focuses on the first.

The agent runs in a [Lima](https://lima-vm.io/) VM - a lightweight Linux virtual machine on macOS. It has its own filesystem, its own process space. Complete isolation from the host.

But complete isolation defeats the purpose. The agent needs to see something. So I added controlled mounts:

> /mnt/desktop  →  ~/Desktop    (read-write)
/opt/agent    →  agent code   (read-only)

The agent can read and write files on my Desktop. That's it. Not my Documents folder. Not my SSH keys. Not my browser cookies. Just one folder, explicitly shared.

This is the core pattern: default deny, explicit allow.

My filesystem is invisible to the agent. I choose what to expose. The mental model flips from "what can the agent damage?" to "what have I shared with the agent?"

For browser control, I connected the agent to [Playwright MCP](https://github.com/anthropics/claude-code/tree/main/packages/playwright-mcp) via a Chrome extension. The agent can navigate, click, fill forms - anything you'd do in a browser. This runs on the host, outside the VM, which is a security tradeoff I haven't fully addressed.

That's the whole prototype. VM for filesystem isolation. Playwright for browser. No network filtering, no action approval. Just enough to test the core idea.

## What can it do?

> ./client prompt "Browse Google News and draft me a summary in my Desktop folder"

The agent opens Chrome, navigates to Google News, reads the headlines, and writes a markdown file to /mnt/desktop/news-summary.md - which appears on my actual Desktop.

This is the Cowork experience in miniature. The agent browses the web as me (authenticated, with my sessions). It writes to my filesystem (through a controlled mount). I didn't copy-paste anything. I didn't upload anything. I just asked, and it did the work.

The same pattern scales:

- Create an Excel model with revenue projections based on this earnings transcript

- Pull AAPL and MSFT stock data using yfinance and create a comparison chart

- Review my Google Calendar for the week - which meetings do I need to prep for?

- Go to my Gmail and summarize any urgent emails from the last 24 hours

Browser plus filesystem covers a surprising amount of knowledge work. No MCP connector needed for Gmail - the browser just works. No special integration for Excel - the agent installs openpyxl and writes the file.

## What's Next

The prototype works, but it's minimal. A few things I want to add:

- Dynamic mounts. Right now, mounts are fixed at VM startup. If I want to share a new folder mid-session, I restart the VM. That's not how real work flows. You're in a conversation, the agent needs access to something, you want to say "here, look at this folder" without breaking context. Hot-mounting is essential.

- Artifacts. The agent creates files inside the sandbox. Getting them out is clunky - I have to know where they landed and copy them manually. Need a cleaner pattern where artifacts the agent produces surface automatically to the user. Cowork does this well with its artifact panel.

- Network proxy. The prototype handles destruction (filesystem isolation) but not exfiltration. The agent has unrestricted internet access. It could post my files anywhere. A proxy layer would help - route all traffic through it, log what's being sent, maybe allowlist specific domains. This also helps with prompt injection: you can inspect what the agent is receiving from the web.

- Desktop control. This is the nuclear option. Right now the agent controls Chrome through Playwright. But what about apps that don't run in a browser? Slack desktop, Excel native, Figma, your IDE. One answer is VNC - let the agent see and control the full desktop via screen sharing. Everything a human can do, the agent can do. This is dangerous. It's also the endgame for true automation. Cowork doesn't do this yet. But someone will.

## Why This Matters

Local agents will win. Context wins, and context lives locally.

Think about all the integrations that will never exist. There's no MCP connector for your company's obscure HR portal. No one's building one for that legacy financial research system. Salesforce has an API, but your compliance tool doesn't. The long tail of enterprise software will never be covered.

But the browser just works. The agent logs in the same way you do. It clicks through the same UI. The integration problem disappears - the agent uses the same interface you use.

And your filesystem has everything. Most enterprises are only just thinking about migrating to the cloud - so a Sharepoint connector, cool, but what about the years of spreadsheets sitting on local drives? The presentations. The documents. The PDFs you downloaded and forgot about. It's all there, accessible - if the agent can see it.

That's the last mile of context. Not what you remembered to upload. Not what you copy-pasted into a prompt. Everything.

This is why the runtime is moving local. Not for performance. Not for cost. Not even for privacy - though that matters a lot in enterprise. For context.

## X Article Metadata

- Title: Local AI agents will win. It's all about context.
- Preview: I remember the moment I became Cursor-pilled.
On the surface, it did exactly what I was already doing with ChatGPT. Write code with an LLM. Copy code in, get suggestions, paste them back. Cursor

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
