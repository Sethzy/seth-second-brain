---
type: raw_capture
source_type: pasted
title: "Sunder sync: SKILL.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/nanoclaw-skills/skills/customize/SKILL.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/nanoclaw-skills/skills/customize/SKILL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/nanoclaw-skills/skills/customize/SKILL.md"
sha256: "9501939b1a0dd339713e14956a822e211850e712688d2a80f12272ca17211c32"
duplicate_of: ""
---

# Sunder sync: SKILL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/nanoclaw-skills/skills/customize/SKILL.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/nanoclaw-skills/skills/customize/SKILL.md

Duplicate of existing source-map entry: `none`

## Capture Text

---
name: customize
description: Add new capabilities or modify NanoClaw behavior. Use when user wants to add channels (Telegram, Slack, email input), change triggers, add integrations, modify the router, or make any other customizations. This is an interactive skill that asks questions to understand what the user wants.
---

# NanoClaw Customization

This skill helps users add capabilities or modify behavior. Use AskUserQuestion to understand what they want before making changes.

## Workflow

1. **Understand the request** - Ask clarifying questions
2. **Plan the changes** - Identify files to modify
3. **Implement** - Make changes directly to the code
4. **Test guidance** - Tell user how to verify

## Key Files

| File | Purpose |
|------|---------|
| `src/index.ts` | Orchestrator: state, message loop, agent invocation |
| `src/channels/whatsapp.ts` | WhatsApp connection, auth, send/receive |
| `src/ipc.ts` | IPC watcher and task processing |
| `src/router.ts` | Message formatting and outbound routing |
| `src/types.ts` | TypeScript interfaces (includes Channel) |
| `src/config.ts` | Assistant name, trigger pattern, directories |
| `src/db.ts` | Database initialization and queries |
| `src/whatsapp-auth.ts` | Standalone WhatsApp authentication script |
| `groups/CLAUDE.md` | Global memory/persona |

## Common Customization Patterns

### Adding a New Input Channel (e.g., Telegram, Slack, Email)

Questions to ask:
- Which channel? (Telegram, Slack, Discord, email, SMS, etc.)
- Same trigger word or different?
- Same memory hierarchy or separate?
- Should messages from this channel go to existing groups or new ones?

Implementation pattern:
1. Create `src/channels/{name}.ts` implementing the `Channel` interface from `src/types.ts` (see `src/channels/whatsapp.ts` for reference)
2. Add the channel instance to `main()` in `src/index.ts` and wire callbacks (`onMessage`, `onChatMetadata`)
3. Messages are stored via the `onMessage` callback; routing is automatic via `ownsJid()`

### Adding a New MCP Integration

Questions to ask:
- What service? (Calendar, Notion, database, etc.)
- What operations needed? (read, write, both)
- Which groups should have access?

Implementation:
1. Add MCP server config to the container settings (see `src/container-runner.ts` for how MCP servers are mounted)
2. Document available tools in `groups/CLAUDE.md`

### Changing Assistant Behavior

Questions to ask:
- What aspect? (name, trigger, persona, response style)
- Apply to all groups or specific ones?

Simple changes → edit `src/config.ts`
Persona changes → edit `groups/CLAUDE.md`
Per-group behavior → edit specific group's `CLAUDE.md`

### Adding New Commands

Questions to ask:
- What should the command do?
- Available in all groups or main only?
- Does it need new MCP tools?

Implementation:
1. Commands are handled by the agent naturally — add instructions to `groups/CLAUDE.md` or the group's `CLAUDE.md`
2. For trigger-level routing changes, modify `processGroupMessages()` in `src/index.ts`

### Changing Deployment

Questions to ask:
- Target platform? (Linux server, Docker, different Mac)
- Service manager? (systemd, Docker, supervisord)

Implementation:
1. Create appropriate service files
2. Update paths in config
3. Provide setup instructions

## After Changes

Always tell the user:
```bash
# Rebuild and restart
npm run build
launchctl unload ~/Library/LaunchAgents/com.nanoclaw.plist
launchctl load ~/Library/LaunchAgents/com.nanoclaw.plist
```

## Example Interaction

User: "Add Telegram as an input channel"

1. Ask: "Should Telegram use the same @Andy trigger, or a different one?"
2. Ask: "Should Telegram messages create separate conversation contexts, or share with WhatsApp groups?"
3. Create `src/channels/telegram.ts` implementing the `Channel` interface (see `src/channels/whatsapp.ts`)
4. Add the channel to `main()` in `src/index.ts`
5. Tell user how to authenticate and test

