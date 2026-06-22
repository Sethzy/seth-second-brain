---
type: raw_capture
source_type: web
title: "Redesigning Claude Code on desktop for parallel agents"
url: "https://claude.com/blog/claude-code-desktop-redesign/"
canonical_url: "https://claude.com/blog/claude-code-desktop-redesign/"
vendor_blog: claude
published_at: 2026-04-14
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Redesigning Claude Code on desktop for parallel agents

Original URL: https://claude.com/blog/claude-code-desktop-redesign/
Published: 2026-04-14
Captured: 2026-06-14T02:32:25+00:00

Description: Today, we're releasing a redesign of the Claude Code desktop app, built to help you run more Claude Code tasks at once.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Redesigning Claude Code on desktop for parallel agents

Today, we're releasing a redesign of the Claude Code desktop app, built to help you run more Claude Code tasks at once.

Download app

[Download app](https://claude.com/download)Download app

Read documentation

[Read documentation](https://docs.claude.com/claude-code)Read documentation

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code
* Date

  April 14, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-code-desktop-redesign

It includes a new sidebar for managing multiple sessions, a drag-and-drop layout for arranging your workspace, an integrated terminal and file editor, plus performance and quality-of-life improvements.

## The new desktop experience

For many developers, the shape of agentic work has changed. You're not typing one prompt and waiting. You're kicking off a refactor in one repo, a bug fix in another, and a test-writing pass in a third, checking on each as results come in, steering when something drifts, and reviewing diffs before you ship.

The new app is built for how agentic coding actually feels now: many things in flight, and you in the orchestrator seat.

## Run sessions in parallel

The new sidebar puts every active and recent session in one place. Kick off work across multiple repos and move between them as results arrive.

You can filter by status, project, or environment, or group the sidebar by project to find and resume sessions faster. When a session's PR merges or closes, it archives itself so the sidebar stays focused on what's live.

When you need to ask a question mid-task, you can open a side chat (⌘ + ; or Ctrl + ;) to branch off a conversation. Side chats pull context from the main thread, but don’t add anything back to the thread, to avoid misdirecting your tasks.

## Review and ship without leaving the app

The redesign brings more commonly-used tools into the app, so you can review, tweak, and ship Claude's work without bouncing to your editor:

* **Integrated terminal**: Run tests or builds alongside your session.
* **In-app file editor**: Open files, make spot edits directly, and save changes.
* **Faster diff viewer**: Rebuilt for performance on large changesets.
* **Expanded preview**: Open HTML files or PDFs in-app, in addition to running local app servers in the preview pane.

Every pane is drag-and-drop. Arrange the terminal, preview, diff viewer, and chat in whatever grid matches how you work.

## Fits your stack

The desktop app now has parity with CLI plugins. If your org manages Claude Code plugins centrally, or you've installed your own locally, they work in the desktop app exactly the way they do in your terminal.

You can still run sessions locally or in the cloud. SSH support now extends to Mac alongside Linux, so you can point sessions at remote machines from either platform.

## Customize for how you work

Three view modes—Verbose, Normal, and Summary—let you dial the interface from full transparency into Claude's tool calls to just the results. New keyboard shortcuts cover session switching, spawning, and navigation; press `⌘ + /` (or `Ctrl + /`) to see the full list. A new usage button shows both your context window and session usage at a glance.

Under the hood, the app has been rebuilt for reliability and speed, and now streams responses as Claude generates them.

## Getting started

The redesigned desktop app is available now for all Claude Code users on Pro, Max, Team, and Enterprise plans, and via the Claude API.

[Download the app](https://claude.com/download), or update and restart if you already have it. Explore the [documentation](https://docs.claude.com/claude-code) to learn more.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

Get Claude Code

* [Desktop](/download)
* [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
* [On the web](https://claude.ai/code)
* [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Oct 8, 2025

### Beyond permission prompts: making Claude Code more secure and autonomous

Claude Code

[Beyond permission prompts: making Claude Code more secure and autonomous](#)Beyond permission prompts: making Claude Code more secure and autonomous

[Beyond permission prompts: making Claude Code more secure and autonomous](/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous)Beyond permission prompts: making Claude Code more secure and autonomous

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

Apr 14, 2026

### Introducing routines in Claude Code

Product announcements

[Introducing routines in Claude Code](#)Introducing routines in Claude Code

[Introducing routines in Claude Code](/blog/introducing-routines-in-claude-code)Introducing routines in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

May 28, 2026

### Introducing dynamic workflows in Claude Code

Product announcements

[Introducing dynamic workflows in Claude Code](#)Introducing dynamic workflows in Claude Code

[Introducing dynamic workflows in Claude Code](/blog/introducing-dynamic-workflows-in-claude-code)Introducing dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

Jun 9, 2026

### New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

Product announcements

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](#)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](/blog/whats-new-in-claude-managed-agents)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
