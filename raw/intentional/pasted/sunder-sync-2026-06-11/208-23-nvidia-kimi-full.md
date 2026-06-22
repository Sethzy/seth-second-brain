---
type: raw_capture
source_type: web
title: "Sunder sync: 23-nvidia-kimi-FULL.md"
url: "https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/23-nvidia-kimi-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/23-nvidia-kimi-FULL.md"
sha256: "a552ce090b2682c313b7dea20de6f0e91680996096038cb8029d1bf81718e6f1"
duplicate_of: ""
---

# Sunder sync: 23-nvidia-kimi-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/23-nvidia-kimi-FULL.md`

Primary URL: https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard

Duplicate of existing source-map entry: `none`

## Capture Text

# NVIDIA - Kimi K2.5 Model Card

**URL:** https://build.nvidia.com/moonshotai/kimi-k2.5/modelcard
**Developer:** Moonshot AI
**Platform:** NVIDIA NIM
**Released:** January 26, 2026
**Type:** Model card / Technical documentation

## Title

"kimi-k2.5 Model by Moonshotai | NVIDIA NIM"

## Overview

1T parameter native multimodal MoE model for high-capacity video and image understanding with efficient inference. Supports advanced agentic capabilities including swarm execution and thinking modes.

## One-Line Description

"1T multimodal MoE for high-capacity video and image understanding with efficient inference."

## Full Description

Kimi K2.5 is an open-source, native multimodal agentic model built through continual pretraining on approximately **15 trillion mixed visual and text tokens** atop Kimi-K2-Base. It seamlessly integrates vision and language understanding with advanced agentic capabilities, supporting both **instant and thinking modes**, as well as **conversational and agentic paradigms**.

**Status:** Ready for commercial/non-commercial use.

## Model Architecture

### Core Specs

| Specification | Value |
|--------------|-------|
| **Architecture Type** | Transformer |
| **Network** | Mixture-of-Experts (MoE) |
| **Total Parameters** | 1T (1 trillion) |
| **Activated Parameters** | 32B per token |
| **Number of Layers** | 61 (including 1 Dense layer) |
| **Attention Hidden Dim** | 7168 |
| **MoE Hidden Dim** | 2048 per expert |
| **Attention Heads** | 64 |
| **Number of Experts** | 384 |
| **Selected per Token** | 8 experts |
| **Shared Experts** | 1 |
| **Vocabulary Size** | 160K |
| **Attention Mechanism** | MLA (Multi-head Latent Attention) |
| **Activation Function** | SwiGLU |
| **Vision Encoder** | MoonViT |
| **Vision Parameters** | 400M |

### Technical Highlights

- **Sparse activation:** Only 32B of 1T parameters active per token
- **Large expert pool:** 384 experts, selecting best 8 per token
- **Native multimodal:** Vision-language co-trained from scratch
- **INT4 quantization:** Native weight-only quantization (Group size 32)
- **Optimized for:** NVIDIA Hopper Architecture (H100, H200)

## Input Specifications

### Input Types
- **Modalities:** Image, Video, Text
- **Formats:** RGB (images/video), String (text)
- **Parameters:** 2D (visual), 1D (text)
- **Context Length:** 256K tokens

### Input Properties
- Supports image, video, PDF, and text inputs
- **Video input:** Experimental feature (official API only)
- **Visual compression:** Spatial-temporal pooling before projection into LLM
- Multi-modal inputs can be interleaved

## Output Specifications

### Output Types
- **Modality:** Text only
- **Format:** String
- **Parameters:** 1D

### Output Modes

#### 1. Thinking Mode
- Includes reasoning traces
- Response contains `reasoning_content`
- **Recommended temperature:** 1.0
- **Recommended top_p:** 0.95
- Shows intermediate reasoning steps

#### 2. Instant Mode
- Direct responses without reasoning traces
- **Recommended temperature:** 0.6
- **Recommended top_p:** 0.95
- Faster responses

### Output Capabilities
- Text generation
- Reasoning and analysis
- Code generation
- Tool orchestration commands
- Multi-step agentic workflows

## Key Capabilities

### 1. Native Multimodality
- Pre-trained on vision-language tokens (not bolted on)
- Excels in visual knowledge
- Cross-modal reasoning
- Agentic tool use grounded in visual inputs

### 2. Coding with Vision
- Generates code from visual specifications
  - UI designs → code
  - Video workflows → code
- Autonomously orchestrates tools for visual data processing
- Advanced web development capabilities

### 3. Agent Swarm 🔥
**Major innovation:** Transitions from single-agent scaling to self-directed, coordinated swarm execution

**How it works:**
- Decomposes complex tasks into parallel sub-tasks
- Dynamically instantiates domain-specific agents
- Coordinates execution across swarm
- Self-directed task distribution

**Use case example:** Building an e-commerce site
- One agent handles frontend
- Another handles backend
- Third handles database schema
- Fourth handles testing
- All coordinated by K2.5

### 4. Multi-modal Agents
Building general agents tailored for scenario-specific automation:
- Visual analysis applications
- Tool-augmented agentic workflows
- Complex task decomposition
- Autonomous image search and processing

### 5. Advanced Web Development
- Autonomous image search for assets
- Dynamic layout refinement
- Iterative design improvement
- Visual specification to code

### 6. Visual Analysis
- High-level comprehension of images
- Video understanding (experimental)
- PDF processing
- Reasoning over visual data

### 7. Complex Tool Use
- Agentic search
- Multi-step tool chains
- Tool selection based on visual context
- Interleaved thinking and tool calls

## Inference

### Hardware Requirements
**Supported:**
- NVIDIA H100 (Hopper)
- NVIDIA H200 (Hopper)

**Not yet:**
- Blackwell Architecture (separate NVIDIA development)

### Runtime Engines
- **vLLM** (primary)
- **SGLang**
- **KTransformers**

**Preferred OS:** Linux

### Quantization
- Native INT4 weight-only quantization
- Group size: 32
- Compressed tensors format
- Optimized for Hopper Architecture

### Acceleration
**Test hardware:** H200
**Acceleration engine:** vLLM

## Training Data

### Scale
**Total:** ~15 trillion mixed visual and text tokens

### Modalities
- Image
- Video
- Text

### Method
Continual pretraining on Kimi-K2-Base

### Details
- Collection: 15T tokens
- Labeling: Undisclosed
- Source: Undisclosed

## Evaluation

### Methodology
- **Tool:** Kimi Vendor Verifier
- **Benchmarks:** Standard multi-modal benchmarks
- **Mode:** Thinking mode enabled
- **Temperature:** 1.0
- **Top-p:** 0.95
- **Context length:** 256K tokens
- **Labeling:** Human-evaluated

### Results
(Benchmark scores section present but specific numbers not extracted from snapshot)

## Interleaved Thinking and Multi-Step Tool Call

K2.5 shares same design as K2 Thinking:
- Reasoning interleaved with tool calls
- Multi-step agentic workflows
- Tool selection during thinking process

**Documentation:** See K2 Thinking guide (platform.moonshot.ai)

## API Usage

### Chat Completion
Standard OpenAI-compatible chat API

### Chat with Visual Content
Supports image, video, PDF in messages array

### Configuration

**For Thinking Mode:**
```json
{
  "temperature": 1.0,
  "top_p": 0.95
}
```

**For Instant Mode:**
```json
{
  "temperature": 0.6,
  "top_p": 0.95,
  "extra_body": {
    "chat_template_kwargs": {"thinking": false}
  }
}
```

### Notes
- Video chat: Experimental, official API only (not vLLM/SGLang yet)
- Tool calls: Same pattern as K2 Thinking
- Context: Up to 256K tokens

## Use Cases

### Designed For
- **Developers:** Building multi-modal AI agents
- **Enterprises:** Scenario-specific automation
- **Applications:**
  - Visual analysis platforms
  - Advanced web development (autonomous asset search, layout iteration)
  - Coding assistance with visual specs
  - Tool-augmented agentic workflows
  - Agent swarm coordination

### Example Scenarios
1. **E-commerce site builder:**
   - Show UI mockup
   - K2.5 generates code + coordinates sub-agents
   - Handles frontend/backend/DB in parallel

2. **Data analysis pipeline:**
   - Point at dashboard screenshot
   - K2.5 writes scraping + processing code
   - Orchestrates tools to execute

3. **Video workflow automation:**
   - Describe process in video
   - K2.5 generates automation script
   - Handles visual verification

## Known Limitations

1. **Hardware:** Trained for Hopper; Blackwell support separate effort
2. **Quantization:** Native INT4 (not fp16/bf16 by default)
3. **Video:** Experimental feature, limited support in third-party deployments
4. **Third-party APIs:** Some features (video, specific modes) require official API

## Release Information

### Dates
- **NVIDIA build.nvidia.com:** January 26, 2026
- **HuggingFace:** January 26, 2026

### Version
Kimi K2.5 v1.0

### Deployment
**Geography:** Global

## Licensing

### Primary Licenses
1. **NVIDIA API Trial Terms of Service** (for API usage)
2. **NVIDIA Open Model License Agreement** (for model)
3. **Modified MIT License** (additional - see HuggingFace)

**Commercial use:** Permitted

## References

- **Company:** Moonshot AI (https://www.moonshot.ai/)
- **HuggingFace:** moonshotai/Kimi-K2.5
- **Platform:** NVIDIA NIM / build.nvidia.com

## Ethical Considerations

### NVIDIA Guidelines
- Trustworthy AI is shared responsibility
- Developers must ensure model meets industry requirements
- Address unforeseen product misuse
- Ensure proper rights/permissions for input content

### User Responsibilities
- Responsible for model inputs and outputs
- Must implement guardrails before deployment
- Must ensure safe integration
- Responsible for compliance with safety/ethical standards

### Privacy Notes
- If images include people, PHI, or IP, outputs may reflect
- No automatic blurring or proportion maintenance
- Users must have proper rights to all input content

### Reporting
Security vulnerabilities and AI concerns: nvidia.com/support/submit-security-vulnerability

## V-Model Methodology

**Important:** Integration requires additional testing
- Use case-specific data validation
- Unit and system level testing
- Iterative validation
- Mitigate risks before deployment
- Ensure compliance with safety/ethical standards

## Technical Innovation Highlights

### 1. Agent Swarm Architecture
**Unique:** Self-directed task decomposition and parallel execution
- Not just single-agent scaling
- Dynamic agent instantiation
- Coordinated swarm behavior
- Domain-specific sub-agents

### 2. Native Multimodal Training
**Different from:** Bolted-on vision modules
- Vision-language co-trained from start
- 15T mixed tokens (not separate stages)
- Visual reasoning deeply integrated

### 3. Efficient 1T Model
**Sparse activation:** 32B active per token
- 384 experts, select 8
- 97% of parameters idle per inference
- Cost of 32B model, capacity of 1T

### 4. Thinking + Instant Modes
**Flexibility:** Same model, different behaviors
- Thinking: Reasoning traces visible
- Instant: Direct answers
- Temperature tuning per mode

## Category

Multimodal AI, Mixture-of-Experts, Agent Swarm, Vision-Language Models, Agentic AI, NVIDIA NIM

## Related

- **Developer:** Moonshot AI
- **Platform:** NVIDIA NIM (build.nvidia.com)
- **Model family:** Kimi K2 series (K2-Base → K2.5)
- **Competing with:** GPT-4V, Claude Opus 4 Multimodal, Gemini Ultra
- **Innovation:** Agent swarm execution (first major model with this capability)
- **Timing:** Released during OpenClaw agent wave (Jan 2026)
- **Hardware:** NVIDIA Hopper (H100/H200)

