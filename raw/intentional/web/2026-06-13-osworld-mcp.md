---
type: raw_capture
source_type: web
title: "OSWorld-MCP"
url: "https://osworld-mcp.github.io"
collected_at: 2026-06-13T10:56:07Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# OSWorld-MCP

Source: https://osworld-mcp.github.io

## Capture Text

# OSWorld-MCP

Original URL: https://osworld-mcp.github.io
Fetched URL: https://osworld-mcp.github.io

## Fetched Content

# OSWorld-MCP Benchmark Leaderboard

## OSWorld-MCP: Benchmarking MCP Tool Invocation in Computer-Use Agents

**Authors:** Hongrui Jia1,2,†, Jitong Liao2,†, Xi Zhang2,†, Haiyang Xu2,\*, Tianbao Xie2, Chaoya Jiang1, Ming Yan2,\*, Si Liu3, Wei Ye1,\*, Fei Huang2

**Affiliations:** 1 Peking University · 2 Tongyi Lab, Alibaba Group · 3 Beijing Zhongguancun Academy

📢 **2025-10-23:** We released our paper and code!
 [Read the Paper](https://arxiv.org/abs/2510.24563) |  [View on GitHub](https://github.com/X-PLUG/OSWorld-MCP)

## Abstract

With advances in decision-making and reasoning capabilities, multimodal agents have shown strong potential in computer application scenarios.
Past evaluations mainly assessed GUI interaction skills, while tool invocation abilities enabled by the Model Context Protocol (MCP) have been largely overlooked.
We present **OSWorld-MCP**, the first comprehensive and fair benchmark for assessing computer-use agents’ tool invocation, GUI operation, and decision-making abilities in a real-world environment.

![Comparison GUI vs MCP](Fig1_thin.jpg)

Figure 1: Task execution via GUI vs MCP Tool

## Highlights

* First benchmark integrating GUI + MCP evaluation in realistic OS environments.
* 158 curated high-quality MCP tools covering 7 common applications.
* New metrics: Accuracy, Tool Invocation Rate (TIR), Average Completion Steps (ACS).
* MCP tools improved success rate up to +15.7% accuracy in some cases.
* Positive relationship between TIR and accuracy validates benchmark challenge.

![Tool Distribution](Fig6.png)

Figure 2: Tool distribution across software ecosystems

## Leaderboard (OSWorld-MCP)

We adopt state-of-the-art **LLM** and **VLM** from open-source representatives such as
Agent-S, Qwen
and closed-source ones from GPT, Gemini, and Claude families on OSWorld-MCP,
as LLM and VLM agent baselines.
  

**Acc**, **TIR**, and **ACS** denote the three evaluation metrics:
*Task Accuracy*, *Tool Invocation Rate*, and *Average Completion Steps*.

---

**Unified Prompt:** To facilitate comparison of performance differences across models,
we standardized our evaluation using the GUI-Owl agent configuration.
This may lead to some performance fluctuations for certain models under their original OSWorld configuration.

**Specific Prompt:** Each model adopts its own unique configuration for OSWorld-MCP evaluation.

---

**We are actively updating** the benchmark with new LLMs, VLMs and methods. Please submit the invocation method and evaluation scripts.
 [Pull requests welcomed!](https://github.com/X-PLUG/OSWorld-MCP/pulls)
  
 For more information, contact:
jiahongrui@stu.pku.edu.cn,
shuofeng.xhy@alibaba-inc.com,
zx443053@alibaba-inc.com.

Filter by Max Steps:

All
15 Steps
50 Steps
100 Steps

All Prompts
Unified Prompt
Specific Prompt

| Rank | Model | Details | Acc | TIR | ACS |
| --- | --- | --- | --- | --- | --- |
|  | Agent-S2.5  OpenAI o3 + UI-TARS-1.5-72B  Simular Research  [Simular Research, '25](https://github.com/simular-ai/Agent-S) | Type: Agentic framework  Max Steps: 15  Runs: 3  Prompt: unified prompt | 42.1 | 30.0 | 10.0 |
|  | Claude 4 Sonnet  claude-sonnet-4-20250514-thinking  Anthropic  [Anthropic, '25](https://www.anthropic.com/news/claude-4) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 36.1 | 27.4 | 10.5 |
|  | Qwen3-VL  qwen3-vl-235b-a22b-thinking  Alibaba Cloud, Qwen Team  [Qwen Team, '25](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 32.8 | 21.5 | 10.0 |
|  | Seed1.5-VL  doubao-1-5-thinking-vision-pro-250428  ByteDance Seed  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 30.7 | 21.0 | 10.1 |
|  | OpenAI o3  o3-2025-04-16  OpenAI  [OpenAI, '25](https://openai.com/index/introducing-o3-and-o4-mini) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 17.6 | 11.6 | 11.9 |
|  | Gemini-2.5-Pro  gemini-2.5-pro  Google DeepMind  [Google DeepMind, '25](https://deepmind.google/models/gemini/pro) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 17.4 | 12.2 | 11.6 |
|  | Qwen2.5-VL  qwen2.5-vl-72b-instruct  Alibaba Cloud, Qwen Team  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl) | Type: General model  Max Steps: 15  Runs: 3  Prompt: unified prompt | 14.5 | 10.1 | 14.0 |
| 8 | Kimi-K2.5  kimi-k2.5  Moonshot AI  [Kimi Team](https://www.kimi.com/ai-models/kimi-k2-5) | Type: General model  Max Steps: 15  Runs: 1  Prompt: specific prompt | 42.8 | 11.9 | 10.9 |
| 9 | Gemini 3.1 Pro  gemini-3.1-pro  Google DeepMind  [Google DeepMind, '26](https://deepmind.google/models/gemini/pro/) | Type: General model  Max Steps: 15  Runs: 1  Prompt: unified prompt | 34.1 | 25.8 | 10.8 |
| 10 | Qwen3.5-Plus  qwen3.5-plus  Alibaba Cloud, Qwen Team  [Qwen Team, '26](https://qwen.ai/blog?id=qwen3.5) | Type: General model  Max Steps: 15  Runs: 1  Prompt: specific prompt | 31.5 | 8.9 | 11.5 |
| 11 | Claude-4-5-Sonnet  claude-sonnet-4-5-20250929  Anthropic  [Anthropic, '25](https://www.anthropic.com/news/claude-4.5-sonnet) | Type: General model  Max Steps: 15  Runs: 1  Prompt: unified prompt | 38.9 | 30.9 | 10.0 |
|  | Agent-S2.5  OpenAI o3 + UI-TARS-1.5-72B  Simular Research  [Simular Research, '25](https://github.com/simular-ai/Agent-S) | Type: Agentic framework  Max Steps: 50  Runs: 3  Prompt: unified prompt | 49.5 | 35.3 | 17.0 |
|  | Claude 4 Sonnet  claude-sonnet-4-20250514-thinking  Anthropic  [Anthropic, '25](https://www.anthropic.com/news/claude-4) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 45.0 | 33.3 | 20.0 |
|  | Qwen3-VL  qwen3-vl-235b-a22b-thinking  Alibaba Cloud, Qwen Team  [Qwen Team, '25](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 39.5 | 26.1 | 18.6 |
|  | Seed1.5-VL  doubao-1-5-thinking-vision-pro-250428  ByteDance Seed  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 38.2 | 25.1 | 22.3 |
|  | Gemini-2.5-Pro  gemini-2.5-pro  Google DeepMind  [Google DeepMind, '25](https://deepmind.google/models/gemini/pro) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 25.7 | 16.8 | 31.0 |
|  | OpenAI o3  o3-2025-04-16  OpenAI  [OpenAI, '25](https://openai.com/index/introducing-o3-and-o4-mini) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 24.1 | 16.0 | 33.0 |
|  | Qwen2.5-VL  qwen2.5-vl-72b-instruct  Alibaba Cloud, Qwen Team  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl) | Type: General model  Max Steps: 50  Runs: 3  Prompt: unified prompt | 15.6 | 9.3 | 39.0 |
| 8 | Kimi-K2.5  kimi-k2.5  Moonshot AI  [Kimi Team](https://www.kimi.com/ai-models/kimi-k2-5) | Type: General model  Max Steps: 50  Runs: 1  Prompt: specific prompt | 56.6 | 18.8 | 21.2 |
| 9 | Gemini 3.1 Pro  gemini-3.1-pro  Google DeepMind  [Google DeepMind, '26](https://deepmind.google/models/gemini/pro/) | Type: General model  Max Steps: 50  Runs: 1  Prompt: unified prompt | 44.2 | 31.0 | 27.6 |
| 10 | Qwen3.5-Plus  qwen3.5-plus  Alibaba Cloud, Qwen Team  [Qwen Team, '26](https://qwen.ai/blog?id=qwen3.5) | Type: General model  Max Steps: 50  Runs: 1  Prompt: specific prompt | 37.6 | 10.2 | 24.9 |
| 11 | Claude-4-5-Sonnet  claude-sonnet-4-5-20250929  Anthropic  [Anthropic, '25](https://www.anthropic.com/news/claude-4.5-sonnet) | Type: General model  Max Steps: 50  Runs: 1  Prompt: unified prompt | 49.5 | 36.6 | 19.8 |

Click headers to sort, use buttons to filter results.
