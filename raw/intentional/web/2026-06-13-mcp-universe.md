---
type: raw_capture
source_type: web
title: "MCP Universe"
url: "https://mcp-universe.github.io/"
collected_at: 2026-06-13T10:56:05Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# MCP Universe

Source: https://mcp-universe.github.io/

## Capture Text

# MCP Universe

Original URL: https://mcp-universe.github.io/
Fetched URL: https://mcp-universe.github.io/

## Fetched Content

# MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers

MCP-Universe is a comprehensive framework designed for developing, testing, and benchmarking AI agents. It offers a robust platform for building and evaluating both AI agents and LLMs across a wide range of task environments. The framework also supports seamless integration with external MCP servers and facilitates sophisticated agent orchestration workflows.

[Paper](https://arxiv.org/abs/2508.14704)
[Code](https://github.com/SalesforceAIResearch/MCP-Universe)
[Discord](https://discord.gg/t9tU77GF)
[Leaderboard](#results)

Ziyang Luo\*,
[Zhiqi Shen](https://scholar.google.com/citations?user=FYUEZ3wAAAAJ&hl=en)\*,
[Wenzhuo Yang](https://scholar.google.com.sg/citations?user=Ce8uS5IAAAAJ&hl=en)\*,
[Zirui Zhao](https://scholar.google.com/citations?user=sKs2OLUAAAAJ&hl=en),
[Prathyusha Jwalapuram](https://scholar.google.com/citations?user=HH1Daf4AAAAJ&hl=en)  
[Amrita Saha](https://scholar.google.com/citations?user=3Zb5Y2YAAAAJ&hl=en),
[Doyen Sahoo](https://scholar.google.com/citations?user=A61jJD4AAAAJ&hl=en),
[Silvio Savarese](https://scholar.google.com/citations?user=ImpbxLsAAAAJ&hl=en),
[Caiming Xiong](https://scholar.google.com/citations?user=vaSdahkAAAAJ&hl=en),
[Junnan Li](https://scholar.google.com/citations?user=MuUhwi0AAAAJ&hl=en)

\* Equal contribution

Salesforce AI Research

Contact: [zluo@salesforce.com](mailto:zluo@salesforce.com), [cxiong@salesforce.com](mailto:cxiong@salesforce.com), [junnan.li@salesforce.com](mailto:junnan.li@salesforce.com)

![MCP-Universe Overview](intro-mcp-universe.png)

**Figure 1:** Example from MCP-Universe illustrating realistic challenges, including real-world tool usage, long-horizon multi-turn tool calls, long context windows, scattered evidence, and large tool spaces. Unlike prior work, MCP-Universe is grounded in real-world MCP servers connected to actual data sources and environments.

## Leaderboard

Overall Track
LLM (w/ ReAct) Track
LLM (w/ Function Calls) Track
Agent Track

Want to add your model/agent to the leaderboard? [Contact us](mailto:zluo@salesforce.com) to submit new results!

Performance comparison across different LLMs and Agents on MCP-Universe benchmark. Success Rate (SR), Average Evaluator Score, and Average Steps reported.

Proprietary Model

Open-Source Model

**Overall Track:** Combines results from both ReAct and Function Call tracks, showing the best performance achieved by each model across both approaches. Models are ranked by their highest overall success rate from either track.

| Model | Location Navigation | Repository Management | Financial Analysis | 3D Designing | Browser Automation | Web Searching | Average Evaluator Score | Average Steps | Overall Success Rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**LLM (w/ ReAct) Track:** Evaluates large language models using the ReAct (Reasoning and Acting) prompting strategy, in which models alternate between reasoning about the task and taking actions through MCP server function calls. In each step, the LLM can use only one tool.

| Model | Location Navigation | Repository Management | Financial Analysis | 3D Designing | Browser Automation | Web Searching | Average Evaluator Score | Average Steps | Overall Success Rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [GPT-5-High](https://platform.openai.com/docs/models/gpt-5) | 26.67 | 30.30 | 67.50 | 57.89 | 43.59 | 45.45 | 62.82 | 6.84 | 44.16 |
| [GPT-5-Medium](https://platform.openai.com/docs/models/gpt-5) | 33.33 | 30.30 | 67.50 | 52.63 | 35.90 | 45.45 | 60.23 | 8.22 | 43.72 |
| [Grok-4](https://docs.x.ai/docs/models/grok-4-0709) | 28.89 | 12.12 | 40.00 | 26.32 | 41.03 | 41.82 | 49.01 | 7.75 | 33.33 |
| [Claude-4.0-Sonnet-Thinking](https://www.anthropic.com/news/claude-4) | 17.78 | 12.12 | 55.00 | 42.11 | 38.46 | 23.64 | 51.74 | 6.91 | 30.30 |
| [Claude-4.1-Opus](https://www.anthropic.com/news/claude-opus-4-1) | 17.78 | 21.21 | 52.50 | 36.84 | 35.90 | 20.00 | 49.14 | 7.04 | 29.44 |
| [Claude-4.0-Opus](https://www.anthropic.com/news/claude-4) | 15.56 | 15.15 | 55.00 | 31.58 | 38.46 | 18.18 | 46.40 | 7.69 | 28.14 |
| [Claude-4.0-Sonnet](https://www.anthropic.com/news/claude-4) | 22.22 | 12.12 | 55.00 | 26.32 | 38.46 | 21.82 | 50.61 | 7.46 | 29.44 |
| [Grok-4-Fast](https://x.ai/news/grok-4-fast) | 24.44 | 9.09 | 65.00 | 5.26 | 25.64 | 21.82 | 48.95 | 6.54 | 27.27 |
| [Grok-Code-Fast-1](https://x.ai/news/grok-code-fast-1) | 26.67 | 9.09 | 62.50 | 15.79 | 20.51 | 18.18 | 44.72 | 6.87 | 26.41 |
| [o3-Medium](https://platform.openai.com/docs/models/o3) | 26.67 | 6.06 | 40.00 | 26.32 | 25.64 | 29.09 | 38.95 | 4.82 | 26.41 |
| [o4-mini-Medium](https://platform.openai.com/docs/models/o4-mini) | 26.67 | 18.18 | 40.00 | 36.84 | 23.08 | 18.18 | 40.38 | 7.90 | 25.97 |
| [Claude-3.7-Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet) | 13.33 | 18.18 | 40.00 | 36.84 | 23.08 | 21.82 | 40.36 | 7.16 | 24.24 |
| [Gemini-2.5-Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) | 13.33 | 12.12 | 50.00 | 21.05 | 25.64 | 12.73 | 36.93 | 6.98 | 22.08 |
| [Gemini-2.5-Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) | 15.56 | 12.12 | 37.50 | 21.05 | 30.77 | 14.55 | 33.99 | 8.26 | 21.65 |
| [GPT-4.1](https://platform.openai.com/docs/models/gpt-4.1) | 8.89 | 6.06 | 40.00 | 26.32 | 23.08 | 10.91 | 41.32 | 5.24 | 18.18 |
| [GPT-4o-2024-08-06](https://platform.openai.com/docs/models/gpt-4o) | 8.89 | 9.09 | 35.00 | 26.32 | 12.82 | 9.09 | 37.03 | 6.03 | 15.58 |
| [GLM-4.5](https://z.ai/blog/glm-4.5) | 17.78 | 9.09 | 50.00 | 26.32 | 15.38 | 27.27 | 41.16 | 7.33 | 24.68 |
| [GLM-4.6](https://z.ai/blog/glm-4.6) | 15.56 | 9.09 | 55.00 | 31.58 | 25.64 | 21.82 | 43.94 | 8.07 | 25.97 |
| [Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | 13.33 | 3.03 | 57.50 | 31.58 | 30.77 | 9.09 | 41.39 | 7.77 | 22.94 |
| [DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) | 15.56 | 0.00 | 42.50 | 31.58 | 28.21 | 18.18 | 43.23 | 6.31 | 22.08 |
| [DeepSeek-V3.1-Terminus](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus) | 13.33 | 6.06 | 45.00 | 15.79 | 25.64 | 20.00 | 42.68 | 6.44 | 21.65 |
| [DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) | 17.78 | 0.00 | 45.00 | 15.79 | 20.51 | 16.36 | 41.92 | 6.48 | 19.91 |
| [Kimi-K2-0905](https://moonshotai.github.io/Kimi-K2/) | 11.11 | 3.03 | 52.50 | 15.79 | 25.64 | 10.91 | 41.28 | 6.96 | 19.91 |
| [GLM-4.5-Air](https://z.ai/blog/glm-4.5) | 17.78 | 6.06 | 42.50 | 10.53 | 17.95 | 16.36 | 37.42 | 6.42 | 19.48 |
| [Kimi-K2-0711](https://moonshotai.github.io/Kimi-K2/) | 11.11 | 9.09 | 47.50 | 15.79 | 15.38 | 14.55 | 35.10 | 6.07 | 19.05 |
| [Qwen3-Max-Preview (Instruct)](https://modelstudio.console.alibabacloud.com/?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen3-max-preview) | 20.00 | 6.06 | 42.50 | 31.58 | 10.26 | 7.27 | 37.74 | 5.50 | 18.18 |
| [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) | 11.11 | 9.09 | 50.00 | 15.79 | 15.38 | 9.09 | 38.53 | 5.74 | 18.18 |
| [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 11.11 | 6.06 | 30.00 | 26.32 | 12.82 | 7.27 | 35.82 | 5.06 | 14.29 |

**LLM (w/ Function Calls) Track:** Evaluates large language models using native function calling capabilities, where models directly invoke MCP server functions without requiring explicit ReAct-like reasoning steps in their responses. In each step, the LLM can use more than one tool.

| Model | Location Navigation | Repository Management | Financial Analysis | 3D Designing | Browser Automation | Web Searching | Average Evaluator Score | Average Steps | Overall Success Rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Gemini-3-Pro-Preview](https://blog.google/products/gemini/gemini-3/) | 35.56 | 18.18 | 82.50 | 52.63 | 38.46 | 41.82 | 61.67 | 7.80 | 44.59 |
| [GPT-5-Medium](https://platform.openai.com/docs/models/gpt-5) | 35.56 | 30.30 | 60.00 | 52.63 | 43.59 | 36.36 | 59.29 | 7.85 | 41.99 |
| [Grok-4.1-Fast](https://x.ai/news/grok-4-1-fast) | 28.89 | 15.15 | 85.00 | 26.32 | 33.33 | 43.64 | 60.58 | 6.32 | 40.69 |
| [Claude-4.5-Sonnet](https://www.anthropic.com/news/claude-sonnet-4-5) | 26.67 | 12.12 | 80.00 | 52.63 | 28.21 | 21.82 | 54.38 | 9.54 | 35.06 |
| [Grok-4-Fast](https://x.ai/news/grok-4-fast) | 22.22 | 6.06 | 80.00 | 21.05 | 23.08 | 32.73 | 52.20 | 7.25 | 32.47 |
| [Claude-4.0-Sonnet-Thinking](https://www.anthropic.com/news/claude-4) | 24.44 | 6.06 | 72.50 | 47.37 | 35.90 | 14.55 | 50.83 | 9.12 | 31.60 |
| [Claude-4.0-Sonnet](https://www.anthropic.com/news/claude-4) | 22.22 | 6.06 | 77.50 | 36.84 | 35.90 | 21.82 | 52.61 | 9.78 | 32.90 |
| [Kimi-K2-Thinking](https://moonshotai.github.io/Kimi-K2/thinking.html) | 20.00 | 12.12 | 60.00 | 15.79 | 20.51 | 23.64 | 45.23 | 8.15 | 26.41 |
| [Claude-4.5-Haiku](https://www.anthropic.com/news/claude-haiku-4-5) | 22.22 | 12.12 | 60.00 | 21.05 | 20.51 | 20.00 | 44.63 | 8.41 | 26.41 |
| [Grok-Code-Fast-1](https://x.ai/news/grok-code-fast-1) | 17.78 | 12.12 | 57.50 | 26.32 | 15.38 | 20.00 | 43.89 | 7.61 | 24.68 |
| [GPT-4.1](https://platform.openai.com/docs/models/gpt-4.1) | 15.56 | 6.06 | 45.00 | 26.32 | 28.21 | 5.45 | 39.58 | 6.83 | 19.91 |
| [GPT-4o-2024-08-06](https://platform.openai.com/docs/models/gpt-4o) | 8.89 | 6.06 | 35.00 | 10.53 | 12.82 | 7.27 | 32.43 | 6.65 | 13.42 |
| [Qwen3-Max-Preview (Instruct)](https://modelstudio.console.alibabacloud.com/?tab=doc#/doc/?type=model&url=2840914_2&modelId=qwen3-max-preview) | 13.33 | 15.15 | 40.00 | 21.05 | 15.38 | 5.45 | 36.71 | 8.57 | 17.32 |
| [GLM-4.6](https://z.ai/blog/glm-4.6) | 8.89 | 12.12 | 47.50 | 26.32 | 17.95 | 16.36 | 35.87 | 11.79 | 20.78 |
| [GLM-4.5](https://z.ai/blog/glm-4.5) | 22.22 | 9.09 | 37.50 | 26.32 | 10.26 | 16.36 | 37.58 | 10.17 | 19.91 |
| [Kimi-K2-0905](https://moonshotai.github.io/Kimi-K2/) | 17.78 | 6.06 | 42.50 | 15.79 | 23.08 | 10.91 | 38.52 | 10.20 | 19.48 |
| [DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) | 11.11 | 6.06 | 45.00 | 26.32 | 23.08 | 12.73 | 38.88 | 10.74 | 19.91 |
| [DeepSeek-V3.1-Terminus](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus) | 11.11 | 6.06 | 45.00 | 10.53 | 17.95 | 16.36 | 34.55 | 11.33 | 18.61 |
| [DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) | 6.67 | 9.09 | 32.50 | 15.79 | 20.51 | 10.91 | 34.08 | 10.56 | 15.58 |
| [GLM-4.5-Air](https://z.ai/blog/glm-4.5) | 8.89 | 3.03 | 25.00 | 10.53 | 7.69 | 14.55 | 26.47 | 12.21 | 12.12 |
| [GPT-OSS-120B](https://huggingface.co/openai/gpt-oss-120b) | 24.44 | 15.15 | 42.50 | 36.84 | 20.51 | 20.00 | 39.78 | 7.53 | 25.54 |

**Agent Track:** Evaluates complete AI agent systems that combine LLMs with specialized frameworks, tools, and orchestration mechanisms to handle complex multi-step tasks and workflows.

| Agent | Location Navigation | Repository Management | Financial Analysis | 3D Designing | Browser Automation | Web Searching | Overall Success Rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ReAct (GPT-5-Medium) | 33.33 | 30.30 | 67.50 | 52.63 | 35.90 | 45.45 | 43.72 |
| OpenAI Agent SDK (o3-Medium) | 28.89 | 6.06 | 60.00 | 36.84 | 28.89 | 29.09 | 31.60 |
| [HarmonyReAct (GPT-OSS-120B)](https://www.notion.so/Unlocking-the-Potential-of-GPT-OSS-with-a-Co-Designed-Agent-Framework-2718397721c0803fbd7fca65072550a3) | 28.89 | 3.03 | 62.50 | 26.32 | 28.21 | 30.91 | 31.17 |
| ReAct (Claude-4.0-Sonnet) | 22.22 | 12.12 | 55.00 | 26.32 | 38.46 | 21.82 | 29.44 |
| Cursor Agent 1.4.5 (Claude-4.0-Sonnet-Thinking) | 22.22 | 9.09 | 55.00 | 26.32 | 43.59 | 7.27 | 26.41 |
| ReAct (o3-Medium) | 26.67 | 6.06 | 40.00 | 26.32 | 25.64 | 29.09 | 26.41 |
| [HarmonyReAct (GPT-OSS-20B)](https://www.notion.so/Unlocking-the-Potential-of-GPT-OSS-with-a-Co-Designed-Agent-Framework-2718397721c0803fbd7fca65072550a3) | 15.56 | 0.00 | 55.00 | 10.52 | 23.08 | 29.09 | 24.24 |
| OpenAI Agent SDK (GPT-OSS-120B) | 6.67 | 6.06 | 35.00 | 10.53 | 5.13 | 5.45 | 11.26 |

Performance Insights

Even SOTA models show significant limitations, with the best model (GPT-5) achieving only 43.72% overall success rate. This highlights the challenging nature of real-world MCP server interactions and the substantial room for improvement in current LLM agents. The gap between proprietary and open-source models remains substantial.

## Key Findings

### Long-Context Challenge

Token count increases rapidly with interaction steps, often leading to context overflow and degraded performance in multi-step tasks requiring extensive reasoning.

### Unknown-Tools Challenge

LLM agents often lack familiarity with precise usage patterns, parameter specifications, and expected behaviors of diverse MCP servers.

### Cross-Domain Variations

Models show markedly different success rates across application domains, suggesting domain-specific optimization needs and knowledge gaps.
