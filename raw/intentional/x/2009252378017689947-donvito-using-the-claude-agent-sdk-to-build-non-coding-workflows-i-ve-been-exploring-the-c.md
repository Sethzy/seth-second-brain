---
type: raw_capture
source_type: x
url: https://x.com/donvito/status/2009252378017689947
original_url: https://x.com/donvito/status/2009252378017689947
author: "Melvin Vivas"
handle: donvito
status_id: 2009252378017689947
captured_at: 2026-06-19T19:57:54+08:00
published_at: "Thu Jan 08 13:14:31 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 25
  reposts: 111
  likes: 1164
---

# X post by @donvito

## Source

- Original: [https://x.com/donvito/status/2009252378017689947](https://x.com/donvito/status/2009252378017689947)
- Canonical: [https://x.com/donvito/status/2009252378017689947](https://x.com/donvito/status/2009252378017689947)
- Author: Melvin Vivas (@donvito)

## Verbatim Text

Using the Claude Agent SDK to build non-coding workflows

I’ve been exploring the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview) which powers Claude Code, one of the best coding tools out there right now.

I had this idea — why not use it for non-coding workflows instead of relying on other agent frameworks like CrewAI or LangChain?

To validate the idea, I built a simple example: a news researcher agent that finds the latest AI news and translates it into Korean.

## The Setup

Here’s an initial script do demonstrate the idea

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition
from claude_agent_sdk.types import McpHttpServerConfig
import os

async def main():
    firecrawl_api_key = os.environ['FIRECRAWL_API_KEY']
    firecrawl_mcp = McpHttpServerConfig(
        type="http",
        url="https://mcp.firecrawl.dev/v2/mcp",
        headers={"Authorization": f"Bearer {firecrawl_api_key}"}
    )
    translator_agent = AgentDefinition(
        description="Translate the content from any language to any other language.",
        prompt="You are an expert language translator.",
        tools=["Read", "Edit", "Bash", "Grep"],
        model="sonnet"
    )
    options = ClaudeAgentOptions(
        model="glm-4.6",
        system_prompt="You are an expert news researcher.",
        permission_mode='bypassPermissions',
        cwd="/Users/melvin/PycharmProjects/ClaudeCodeSDK/output",
        mcp_servers={"firecrawl_mcp": firecrawl_mcp},
        agents={"translator-agent": translator_agent}
    )
    async for message in query(
        prompt=(
            "What are the latest news topics in AI? "
            "Write the results to a markdown file with URLs as references. "
            "Then use the translator-agent to translate the content to Korean "
            "and save it to a separate markdown file."
        ),
        options=options
    ):
        print(message)
asyncio.run(main())
```

## Concept 1: Using MCPs for Data Retrieval

I used the [Firecrawl MCP](https://docs.firecrawl.dev/mcp-server) to fetch the latest AI news.

The agent gathered data, summarised it, and wrote the results into a Markdown file, all autonomously.

This shows how an MCP can act like an API plugin layer, enabling agents to perform real-world data collection beyond simple prompts.

## Concept 2: Sub-Agents for Specialized Tasks

After gathering the news, I wanted a translated version.

Instead of hardcoding translation logic, I created a sub-agent the translator-agent specifically for that purpose.

The main agent then delegated the translation task to the sub-agent.

[The output](https://firecrawl.dev/):

- ai_news_en.md — English summary

- ai_news_ko.md — Korean translation

## A more elaborate example

I made different sub-agents in this more complex example to demonstrate the power of the Claude Agent SDK which powers Claude Code.

This script wires up a small “news research” workflow. It shows how to chain multiple specialised sub-agents so that a single run can:

• Research a topic on the web
• Extract highlights
• Translate the content
• Build a simple webpage
• Generate social posts

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition
from claude_agent_sdk.types import McpHttpServerConfig, AssistantMessage, UserMessage
import os

async def main():

    firecrawl_api_key = os.environ['FIRECRAWL_API_KEY']
    firecrawl_mcp = McpHttpServerConfig(
        type="http",
        url="https://mcp.firecrawl.dev/v2/mcp",
        headers={
            "Authorization": f"Bearer {firecrawl_api_key}"
        }
    )

    translator_agent = AgentDefinition(
        description="Translate the content from any language to any other language.",
        prompt="You are an expert language translator.",
        tools=["Read", "Edit", "Bash", "Grep"]
    )

    highlights_extractor_agent = AgentDefinition(
        description="Extract key highlights from researched news and create a markdown file with the highlights.",
        prompt="You are an expert at extracting and summarizing key highlights from news articles. Extract the most important points, insights, and takeaways, then create a well-structured markdown file.",
        tools=["Read", "Write", "Edit"]
    )

    website_developer_agent = AgentDefinition(
        description="Create and develop webpages with HTML, CSS, and JavaScript.",
        prompt="You are an expert web developer. Create modern, responsive, and well-structured webpages using HTML, CSS, and JavaScript.",
        tools=["Read", "Write", "Edit"]
    )

    social_media_creator_agent = AgentDefinition(
        description="Create engaging LinkedIn and Twitter posts from news content.",
        prompt="You are an expert social media content creator. Create compelling, engaging LinkedIn and Twitter posts that capture key insights and drive engagement. Use appropriate hashtags and formatting for each platform.",
        tools=["Read", "Write", "Edit"],
    )

    options = ClaudeAgentOptions(
        model="glm-4.6",
        system_prompt="You are an expert news researcher.",
        permission_mode='bypassPermissions',
        cwd="/Users/melvin/PycharmProjects/ClaudeCodeSDK/output",
        mcp_servers= {"firecrawl_mcp": firecrawl_mcp},
        agents={
            "translator-agent": translator_agent,
            "highlights-extractor-agent": highlights_extractor_agent,
            "website-developer-agent": website_developer_agent,
            "social-media-creator-agent": social_media_creator_agent
        }
    )

    async for message in query(
        prompt="What are the latest news topics in the philippines about flood control projects and dpwh. "
               "Write the results to a markdown file. Add urls as references "
               "as sources in the markdown file. "
               "Also write a translation of the news to Korean using the translator-agent. "
               "Write the translation to a separate markdown file. "
               "Extract highlights and write to a separate markdown file. "
               "Then use the website-developer-agent to create an HTML webpage displaying the AI news "
               "with proper styling and save it to a file. "
               "Finally, use the social-media-creator-agent to create LinkedIn and Twitter posts "
               "based on the AI news and save them to a markdown file.",
        options=options
    ):
        print(message)


asyncio.run(main())
```

## Here’s sample output of this workflow

It creates a twitter post and a webpage together plus markdown files produced by each sub-agent

## Why This Matters

The Claude Agent SDK already supports:

- Tools (Read, Edit, Bash, etc.)

- MCPs (external capability servers)

- Skills

- Sub-agents

These are the same components other AI agent frameworks build from scratch, but here, it’s all native to Claude’s ecosystem.

With what Claude AI has built, developers and researchers can rapidly compose workflows that go beyond chat — from document generation to automated pipelines.

I used the GLM 4.6 model in this example, but of course, it works [perfectly with](https://firecrawl.dev/) Claude models like Haiku and Sonnet.

## A Great Alternative to AI Agent Frameworks

Frameworks like CrewAI and LangChain are excellent for building complex agent systems — but sometimes, simplicity wins.

The Claude Agent SDK gives you the same building blocks — tools, sub-agents, and external connectors — in a lightweight package that integrates naturally with Claude’s ecosystem.

## X Article Metadata

- Title: Using the Claude Agent SDK to build non-coding workflows
- Preview: I’ve been exploring the Claude Agent SDK which powers Claude Code, one of the best coding tools out there right now.
I had this idea — why not use it for non-coding workflows instead of relying on

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
