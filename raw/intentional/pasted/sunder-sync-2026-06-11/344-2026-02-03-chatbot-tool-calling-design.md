---
type: raw_capture
source_type: web
title: "Sunder sync: 2026-02-03-chatbot-tool-calling-design.md"
url: "https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-02-03-chatbot-tool-calling-design.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-02-03-chatbot-tool-calling-design.md"
sha256: "8828eb8a92b2a87260d39fc76eb048f77938b509c0f6ebdc6a486ee25baa779d"
duplicate_of: ""
---

# Sunder sync: 2026-02-03-chatbot-tool-calling-design.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-02-03-chatbot-tool-calling-design.md`

Primary URL: https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage

Duplicate of existing source-map entry: `none`

## Capture Text

# Chatbot Tool Calling: Database Query & File Exploration

**Date:** 2026-02-03
**Status:** Draft - Idea Stage
**Author:** Claude + Seth

---

## Executive Summary

Add tool calling capabilities to the chatbot so users can **query the database** and **explore raw files** when the AI can't figure something out from extracted data alone.

### The Vision

```
Today:
  AI can't find data → User is stuck → Opens Supabase/downloads file manually

Tomorrow:
  AI can't find data → AI uses tools → Queries DB / reads file → Answers user
```

### Core Insight

Extraction isn't perfect. When users ask "why is this field empty?" or "what's actually in document X?", the chatbot should be able to **investigate** rather than just apologize. This transforms the chatbot from a Q&A interface into an **agentic assistant** that can self-serve context.

### Key Outcomes

1. **Self-debugging** - Users can ask "what's in the raw file?" when extractions seem wrong
2. **Ad-hoc queries** - "Show me all documents from last week with missing fields"
3. **Transparent reasoning** - Tool invocations are visible, building trust
4. **Reduced support load** - Users self-serve instead of asking developers

---

## Inspiration: Claude Agent SDK Tool Patterns

The Claude Agent SDK provides clean patterns for tool definition and execution streaming.

### Tool Definition Pattern

```typescript
import { tool } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// Tools are defined with:
// 1. Name - unique identifier
// 2. Description - helps model decide when to use it
// 3. Input schema - Zod validation
// 4. Execute function - async implementation

const queryDatabase = tool(
  "query_database",
  "Query the database to find records, check extracted data, or investigate missing fields",
  {
    sql: z.string().describe("SQL query (SELECT only, no mutations)"),
    explanation: z.string().describe("Why this query helps answer the user's question")
  },
  async (args) => {
    // Validate SQL is read-only
    // Execute against Supabase
    // Return formatted results
  }
);
```

### Streaming Tool Execution (UI Pattern)

From the Claude Agent SDK docs - tracking tool lifecycle for UI display:

```typescript
// Track tool state for UI
let currentTool: string | null = null;
let toolInput = "";

for await (const message of query({ prompt, options })) {
  if (message.type === "stream_event") {
    const event = message.event;

    if (event.type === "content_block_start") {
      if (event.content_block.type === "tool_use") {
        // Show: [Using query_database...]
        currentTool = event.content_block.name;
        toolInput = "";
      }
    } else if (event.type === "content_block_delta") {
      if (event.delta.type === "input_json_delta") {
        // Accumulate input for display
        toolInput += event.delta.partial_json;
      }
    } else if (event.type === "content_block_stop") {
      if (currentTool) {
        // Show: query_database completed ✓
        currentTool = null;
      }
    }
  }
}
```

---

## Proposed Tools

### 1. `query_database` - SQL Query Tool

**Purpose:** Let users ask data questions the AI can't answer from context alone.

**Use Cases:**
- "How many documents did we process last week?"
- "Show me all records where company_name is empty"
- "What's the extraction status for document ID xyz?"

**Schema:**
```typescript
const queryDatabase = tool(
  "query_database",
  "Query the Supabase database to find records, check extracted data, or investigate issues. Use this when you need to look up specific records or aggregate data that isn't in the current context.",
  {
    sql: z.string().describe("Read-only SQL query (SELECT only)"),
    reason: z.string().describe("Brief explanation of why this query helps")
  },
  async ({ sql, reason }) => {
    // 1. Validate SQL is SELECT-only (no INSERT/UPDATE/DELETE/DROP)
    // 2. Add row limit if not present (LIMIT 100)
    // 3. Execute via Supabase client
    // 4. Format results as markdown table
    return {
      content: [{
        type: "text",
        text: formatAsMarkdownTable(results)
      }]
    };
  }
);
```

**Security:**
- Whitelist of allowed tables (no auth/billing tables)
- SELECT-only validation
- Row limit enforcement
- Query timeout
- RLS still applies (user can only see their org's data)

### 2. `read_raw_file` - File Content Tool

**Purpose:** Let users inspect source documents when extractions seem off.

**Use Cases:**
- "What's actually in document ABC123?"
- "Show me the raw text from page 2"
- "Why couldn't you extract the invoice number?"

**Schema:**
```typescript
const readRawFile = tool(
  "read_raw_file",
  "Read the raw content of an uploaded document. Use this when the user questions an extraction result or wants to see what's actually in a file.",
  {
    fileId: z.string().describe("The document/file ID to read"),
    pageNumber: z.number().optional().describe("Specific page to read (for multi-page docs)")
  },
  async ({ fileId, pageNumber }) => {
    // 1. Verify user has access to this file (RLS)
    // 2. Fetch from Supabase storage
    // 3. Extract text content (handle PDF, images via OCR cache)
    // 4. Return content (with truncation if too long)
    return {
      content: [{
        type: "text",
        text: truncate(fileContent, 10000) // Limit context size
      }]
    };
  }
);
```

### 3. `search_documents` - Semantic Search Tool (Future)

**Purpose:** Find relevant documents across the user's corpus.

```typescript
const searchDocuments = tool(
  "search_documents",
  "Search across all documents using semantic similarity. Use when the user asks about topics that might span multiple documents.",
  {
    query: z.string().describe("Natural language search query"),
    limit: z.number().default(5).describe("Max results to return")
  },
  async ({ query, limit }) => {
    // Vector similarity search via pgvector
  }
);
```

---

## UI Design

Based on the screenshot reference, tool invocations should be:

### Collapsible Tool Cards

```
┌─────────────────────────────────────────────┐
│ ▶ QueryDatabase  "SELECT * FROM docs..."    │
└─────────────────────────────────────────────┘
```

Expanded:
```
┌─────────────────────────────────────────────┐
│ ▼ QueryDatabase                             │
│                                             │
│   Query: SELECT id, name, status            │
│          FROM documents                      │
│          WHERE org_id = 'abc'               │
│          LIMIT 10                           │
│                                             │
│   Results: 10 rows                          │
│   ┌─────────────────────────────────────┐   │
│   │ id  │ name        │ status          │   │
│   │ 1   │ Invoice.pdf │ extracted       │   │
│   │ ... │ ...         │ ...             │   │
│   └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

### State Indicators

- `⏳ Running...` - Tool executing
- `✓ Completed` - Tool finished successfully
- `✗ Error` - Tool failed (show error message)

### "Agent" Toggle

Bottom of chat input - toggle to enable/disable tool use:
- **Off:** Standard chat, no tool calling
- **On:** AI can use tools to investigate

---

## Implementation with Vercel AI SDK

Since we're using Vercel AI SDK, here's how this maps:

### Server-Side (API Route)

```typescript
// api/chat/route.ts
import { streamText, tool } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
import { z } from 'zod';

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = await streamText({
    model: anthropic('claude-sonnet-4-20250514'),
    messages,
    tools: {
      queryDatabase: tool({
        description: 'Query the database to find records or investigate data issues',
        parameters: z.object({
          sql: z.string().describe('Read-only SQL query'),
          reason: z.string().describe('Why this query helps'),
        }),
        execute: async ({ sql, reason }) => {
          // Validate and execute
          const results = await executeReadOnlyQuery(sql);
          return formatResults(results);
        },
      }),
      readRawFile: tool({
        description: 'Read raw content from an uploaded document',
        parameters: z.object({
          fileId: z.string(),
          pageNumber: z.number().optional(),
        }),
        execute: async ({ fileId, pageNumber }) => {
          const content = await fetchFileContent(fileId, pageNumber);
          return content;
        },
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

### Client-Side (useChat)

```typescript
// components/chatbot.tsx
import { useChat } from 'ai/react';

export function Chatbot() {
  const { messages, input, handleSubmit, setInput } = useChat({
    api: '/api/chat',
  });

  return (
    <div>
      {messages.map((message) => (
        <div key={message.id}>
          {message.role === 'assistant' && message.parts?.map((part, i) => {
            // Render tool invocations
            if (part.type === 'tool-invocation') {
              return (
                <ToolCard
                  key={i}
                  name={part.toolInvocation.toolName}
                  args={part.toolInvocation.args}
                  state={part.toolInvocation.state}
                  result={part.toolInvocation.result}
                />
              );
            }
            // Render text
            if (part.type === 'text') {
              return <Markdown key={i}>{part.text}</Markdown>;
            }
          })}
        </div>
      ))}
      {/* Input */}
    </div>
  );
}
```

---

## Security Considerations

### SQL Injection Prevention
- Parameterized queries where possible
- Strict SELECT-only validation (regex + AST parsing)
- Table whitelist
- Column blacklist (exclude sensitive fields)

### Access Control
- RLS enforced at database level
- File access validated against user's org
- Audit logging of all tool invocations

### Rate Limiting
- Max queries per minute per user
- Query complexity limits (no expensive JOINs)
- Result size limits

---

## Rollout Plan

### Phase 1: Read-Only Database Queries
- Implement `query_database` tool
- Table whitelist: `documents`, `extractions`, `files`
- Basic UI for tool invocation display
- Internal testing only

### Phase 2: File Content Reading
- Implement `read_raw_file` tool
- Handle PDF text extraction (use cached OCR)
- Truncation for large files

### Phase 3: Polish & Launch
- Agent toggle in UI
- Expanded tool cards with copy functionality
- User feedback collection
- Docs/help content

### Phase 4: Advanced (Future)
- Semantic search across documents
- Write tools (with approval flow)
- Custom tool definitions per org

---

## Open Questions

1. **Should tool results be persisted?** Useful for debugging, but storage cost.
2. **Query complexity limits?** Need to balance usefulness vs. DB load.
3. **Approval flow for certain queries?** Or fully automatic?
4. **How to handle tool errors gracefully?** Retry? Fall back to explanation?

---

## References

- [Vercel AI SDK - Chatbot Tool Usage](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage)
- [Vercel AI SDK - Tools and Tool Calling](https://ai-sdk.dev/docs/ai-sdk-core/tools-and-tool-calling)
- [Claude Agent SDK - Custom Tools](https://platform.claude.com/docs/en/agent-sdk/custom-tools)
- [Claude Agent SDK - Streaming Output](https://platform.claude.com/docs/en/agent-sdk/streaming-output)

