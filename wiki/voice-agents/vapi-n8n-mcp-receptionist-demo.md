---
type: wiki_article
title: Vapi n8n MCP Receptionist Demo
updated_at: 2026-06-30
status: draft
source_count: 1
tags:
  - voice-agents
  - vapi
  - n8n
  - mcp
  - cx-demo
---

# Vapi n8n MCP Receptionist Demo

> Source: [I Built an AI Voice Receptionist with Vapi and n8n MCP (free template) - YouTube](../../raw/intentional/youtube/2026-06-30-i-built-an-ai-voice-receptionist-with-vapi-and-n8n-mcp.md)

## What The Demo Builds

The video builds a phone-style AI receptionist for "Hercules Detailing." Vapi is the voice-agent front end: it owns the live call, system prompt, model choice, voice behavior, tool selection, knowledge-base query, call transfer, phone number assignment, and end-of-call reporting. n8n is the backend automation layer exposed through an MCP server. The backend workflows update CRM, calendar, appointment logs, and call logs.

The demo proves two customer-CX paths:

- New caller: ask for email, detect no CRM record, collect contact details, create the CRM entry, check appointment availability, book a detailing appointment, update calendar and appointment log, then write a call summary/outcome.
- Returning caller: look up the customer by email, understand a reschedule request, check availability, find the existing appointment/event ID, update the calendar and appointment log, then write a call summary/outcome.

## Architecture Pattern

```text
Caller
  -> Vapi assistant
  -> MCP tool connected to n8n
  -> narrow deterministic n8n workflows
  -> CRM / calendar / appointment log / call log
  -> Vapi speaks the result back to the caller
```

The important design decision is to keep Vapi as the only reasoning agent. The n8n side should not contain another AI agent deciding what to do. In the video, the backend workflows are normal deterministic automations. This reduces duplicated reasoning, latency, cost, and failure surface while a human is waiting on the phone.

## Conversation Flow

The builder starts with a wireframe before configuring Vapi. The flow is:

1. Inbound call starts.
2. Assistant asks for email and uses a CRM lookup tool.
3. If the client exists, welcome them back; if not, gather email, full name, and phone, then create a CRM record.
4. Gather intent.
5. Route to one of several paths: answer a general question from a knowledge base, book/change/delete an appointment, hand off to another assistant, or transfer to a human/team.
6. After the task, log activity and end the call.
7. Send an end-of-call report to an external logger.

For Seth's demo, this is a useful shape because it shows a voice agent doing actual CX work rather than just chatting: identity lookup, stateful business actions, appointment mutation, escalation, and reporting.

## n8n MCP Tools

The MCP server exposes seven custom workflows:

| Tool | Purpose | Main Inputs / Outputs |
|---|---|---|
| Client lookup | Find an existing CRM record by email | Email in; customer record or "new client" style response out |
| New client CRM | Create a new CRM row | Email, name, phone in; created profile out |
| Check availability | Read calendar availability | Start/end range in; busy slots or available-day result out |
| Book event | Create a calendar appointment | Start time, end time, email, event summary in; calendar event and appointment-log row out |
| Update appointment | Move an existing appointment | Event ID and new start/end times in; updated calendar event and sheet row out |
| Lookup appointment | Find the appointment to mutate | Time window and/or customer context in; event ID out |
| Delete appointment | Cancel an appointment | Event ID in; deleted event and cancelled appointment-log row out |

The MCP approach is preferred over hand-wiring many Vapi webhook tools because tool schemas and input requirements live closer to the backend workflows. Otherwise every changed parameter has to be updated in both Vapi and n8n.

## Vapi Configuration

The video configures:

- A model for the assistant, shown as OpenAI GPT-4.1 in the walkthrough because the creator found it followed instructions better than GPT-4 for this flow.
- A first message that asks for the caller's email.
- A system prompt that is heavily iterated through test calls.
- A Vapi tool named for n8n, configured as an MCP integration using the production URL from the n8n MCP server trigger.
- A handoff tool that can route to another internal Vapi assistant, such as customer support.
- A transfer-call tool option for routing to a phone number or human.
- A file-backed knowledge base for FAQs, policies, hours, location, and services, with instructions to use only that source for general questions.
- Server messaging that sends an end-of-call report to an n8n webhook.
- Summary and structured-data extraction, including an `outcome` field for the call log.
- A Vapi phone number assigned to the inbound AI receptionist.

The builder also argues that voice agents should disclose they are AI assistants at the beginning of the call, because interruptions, timing, and etiquette will not be perfect.

## Prompt And Tooling Lessons

- Draw the call flow before writing the prompt.
- Treat the voice-agent prompt like a call-center script with conditional branches.
- Give the assistant explicit rules for each appointment operation.
- For booking, check availability before proposing or confirming a time.
- For changing an appointment, check availability and retrieve the event ID before updating.
- For deleting an appointment, retrieve the event ID first.
- When checking today's availability, use the current time through end of day; for future dates, check the full day.
- Tell the caller available times or busy windows, but do not expose internal calendar event titles.
- Keep each backend tool narrow and well described so MCP/Vapi can select it reliably.
- Keep backend automations deterministic. Do not add a second AI decision-maker unless there is a clear reason.

## CLI-First Rebuild Plan

For a Codex-built version, the n8n pieces can become a small deterministic TypeScript or Python tool service while Vapi keeps phone/voice infrastructure:

1. Define the target CX scenario: order status, appointment scheduling, refund triage, support escalation, or account lookup.
2. Write the call-state flow as a simple state machine or decision table.
3. Create mock business data for CRM, orders, appointments, tickets, and call logs.
4. Implement deterministic tool endpoints: `lookupCustomer`, `createCustomer`, `checkAvailability`, `bookAppointment`, `rescheduleAppointment`, `cancelAppointment`, `createTicket`, `logCall`.
5. Configure the Vapi assistant from files/API rather than from drag-and-drop UI where possible.
6. Attach a small FAQ/policy knowledge base.
7. Configure end-of-call summary and structured outcome extraction.
8. Run two scripted demo calls: a happy-path resolution and a messy customer needing escalation.

This keeps the interview demo aligned with Seth's preference: no low-code drag-and-drop dependency for the core logic, model/provider optionality through Vapi, and zero voice/telephony infra.

## Open Questions

- Should the demo use n8n MCP because the video template does, or replace it with a tiny CLI-managed tool server to make the build feel more engineer-native?
- Which exact CX use case is most interview-legible: appointment scheduling, order lookup, billing/refund triage, or support escalation?
- What is the cheapest acceptable Vapi stack for the demo once model, transcriber, voice, and phone minutes are counted together?
