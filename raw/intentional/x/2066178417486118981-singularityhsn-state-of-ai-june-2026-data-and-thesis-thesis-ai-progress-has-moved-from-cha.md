---
type: raw_capture
source_type: x
url: https://x.com/singularityHSN/status/2066178417486118981
original_url: https://x.com/singularityHSN/status/2066178417486118981
author: "Habanero"
handle: singularityHSN
status_id: 2066178417486118981
captured_at: 2026-06-19T23:59:17+08:00
published_at: "Sun Jun 14 15:18:17 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 0
  likes: 1
---

# X post by @singularityHSN

## Source

- Original: [https://x.com/singularityHSN/status/2066178417486118981](https://x.com/singularityHSN/status/2066178417486118981)
- Canonical: [https://x.com/singularityHSN/status/2066178417486118981](https://x.com/singularityHSN/status/2066178417486118981)
- Author: Habanero (@singularityHSN)

## Verbatim Text

State of AI, June 2026: data and thesis

Thesis: AI progress has moved from chatbot assistance to expert technical agents. The reliable unit of work is moving upward: from short prompts to tool use, codebases, exploit chains, research loops, production workflows, and bounded AI-R&D tasks.

The central measurement is how long can an agent operate across tools, context, verification, and feedback before reliability collapses?

1. Timeline implied by the evidence

2025–2026: AI coworker / collaborator era
 2026: expert technical agent era
 2027–2028: narrow automated AI-R&D loops become plausible
 2027–2029: major structured digital-work disruption
 2028–2030: broad AI-R&D acceleration becomes plausible
 2028–2031: most structured digital work becomes technically automatable under sufficient tooling, context, inference, and verification
 2029–2032: AI-heavy BG3-like production pipeline becomes plausible
 2029–2032: GTA6-like vertical slice becomes plausible
 2033–2040+: true GTA6-scale solo/director project remains harder
 2030–2035: economy and institutions reorganize

Sources behind timeline: OpenAI GPT-5.5 data [1], OpenAI automated researcher plan [2], OpenAI math result [3], Anthropic Glasswing / Mythos [4], Anthropic Fable/Mythos 5 [5], AISI cyber autonomy [7], METR task horizons [10], ARC-AGI-3 [11], ProgramBench [13], FrontierCode [14], Anthropic recursive self-improvement data [18], Epoch AI trends [23], IEA data-center projections [24].

2. GPT-5.5: OpenAI public frontier data

OpenAI announced GPT-5.5 on April 23, 2026. OpenAI describes it as strong at coding/debugging, online research, data analysis, documents/spreadsheets, software operation, tool use, planning, ambiguity handling, and continuing until a task is finished. [1]

Reported GPT-5.5 results:

Terminal-Bench 2.0: 82.7%
 Expert-SWE internal: 73.1%
 GDPval wins/ties: 84.9%
 OSWorld-Verified: 78.7%
 Toolathlon: 55.6%
 BrowseComp: 84.4%
 FrontierMath Tiers 1–3: 51.7%
 FrontierMath Tier 4: 35.4%
 CyberGym: 81.8%
 SWE-Bench Pro: 58.6% [1]

OpenAI reports that more than 85% of OpenAI uses Codex weekly across software engineering, finance, communications, marketing, data science, and product. [1]

OpenAI reports that Codex reviewed 24,771 K-1 tax forms across 71,637 pages and accelerated the finance process by 2 weeks versus the prior year. [1]

OpenAI reports that one go-to-market employee automated weekly reports with Codex, saving 5–10 hours per week. [1]

OpenAI states that the goal is to build an automated AI researcher. Its plan says that by March 2028, a significant fraction of OpenAI research may be done by AI systems alongside human researchers. [2]

OpenAI also reported that an internal general-purpose reasoning model disproved a long-standing Erdős planar unit-distance conjecture first posed in 1946, with the proof checked by external mathematicians. [3]

3. Claude Mythos Preview / Project Glasswing

Anthropic announced Project Glasswing on April 7, 2026. Partners included AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks. [4]

Anthropic describes Claude Mythos Preview as a general-purpose, unreleased frontier model that can surpass all but the most skilled humans at finding and exploiting software vulnerabilities. [4]

Reported Mythos Preview results:

CyberGym: 83.1%
 SWE-Bench Pro: 77.8%
 Terminal-Bench 2.0: 82.0%
 Terminal-Bench 2.1 with longer timeout: 92.1%
 SWE-Bench Multimodal: 59.0%
 SWE-Bench Multilingual: 87.3%
 SWE-Bench Verified: 93.9%
 GPQA Diamond: 94.6%
 Humanity’s Last Exam, no tools: 56.8%
 Humanity’s Last Exam, with tools: 64.7%
 BrowseComp: 86.9%
 OSWorld-Verified: 79.6% [4]

Anthropic says Mythos Preview found thousands of high-severity vulnerabilities, including in every major OS and browser. It also reports a 16-year-old FFmpeg vulnerability that automated testing had hit 5 million times without catching. [4]

Anthropic committed up to $100M in usage credits for Mythos Preview and $4M in direct donations to open-source security organizations. [4]

Anthropic says it does not plan to make Mythos Preview generally available. [4]

4. Claude Fable 5 / Mythos 5

Anthropic positions Claude Fable 5 as the general-release Mythos-class model and Claude Mythos 5 as the same underlying model with some safeguards lifted for trusted cyber/bio users. [5]

Pricing: $10 per million input tokens and $50 per million output tokens. [5]

Reported / discussed Fable-Mythos 5 values:

SWE-Bench Pro: 80.3%
 FrontierCode Diamond: 29.3% xhigh
 Terminal-Bench 2.1: 88.0%
 OSWorld-Verified: 85.0%
 HLE no tools: 59.0%
 HLE with tools: 64.5%
 ExploitBench Cap%: 78.0%
 HealthBench Professional: 66.0% [5]

Anthropic reports that more than 95% of Fable sessions involve no fallback; in those sessions, performance is effectively the same as Mythos 5. [5]

Stripe reported that Fable 5 performed a 50-million-line Ruby codebase migration in 1 day that would otherwise have taken a whole team more than 2 months by hand. [5]

Anthropic reports that internal protein-design experts accelerated aspects of drug design by about 10× using Mythos 5. It also reports that Mythos 5 with tools and no human assistance matched or beat skilled human operators, and that 9 of 14 protein targets yielded strong drug-design candidates under investigation. [5]

The US government directive forced Anthropic to suspend all Fable 5 / Mythos 5 access by foreign nationals; Anthropic disabled the models for all customers to ensure compliance. [6]

5. Cyber autonomy: strongest current near-term signal

AISI reports that the length of cyber tasks frontier models can complete has been doubling every few months. The February 2026 estimate was 4.7 months, accelerated from an 8-month estimate in November 2025. [7]

AISI caps runs at 2.5M tokens per task for comparability and states this understates frontier capabilities. [7]

With the 2.5M-token cap, GPT-5.5 succeeded 100% on 5 of 6 tasks estimated over 8 hours and solved the sixth on every uncapped attempt. Mythos Preview completed all 6 long tasks 100% under the cap. [7]

In cyber ranges, a newer Mythos checkpoint solved “The Last Ones” 6/10 and “Cooling Tower” 3/10. GPT-5.5 solved “The Last Ones” 3/10. [7]

AISI states that without the 2.5M-token cap, success rates become high enough that time horizons become difficult to calculate. It also reports that up to 100M tokens were used in a cyber range experiment and performance likely improved beyond that. [7]

Anthropic’s Glasswing update reports scanning 1,000+ open-source projects with Mythos and finding 23,019 estimated vulnerabilities, including 6,202 estimated high/critical vulnerabilities. [8]

Of 1,752 high/critical candidates assessed, Anthropic reports 1,587 true positives, a 90.6% true-positive rate. 1,094 were confirmed high/critical, equal to 62.4%. [8]

Anthropic’s red-team N-day exploit work reports:

8 working Firefox code-execution exploits from 18 recent SpiderMonkey security patches
 First Firefox exploit in under 1 hour
 8 exploits in roughly 12 hours
 18 PoCs from 21 Windows kernel patches
 8 full Windows privilege-escalation chains to SYSTEM
 Total Windows run cost: $15,700
 Approximate cost per exploit chain: $2,000
 PoCs for 13 of 14 Windows bugs Microsoft rated “Exploitation Less Likely” or “Unlikely” [9]

Thesis: cyber is the clearest current domain where AI agents are moving from assistance into high-value autonomous execution, because the work is digital, testable, tool-mediated, and feedback-rich.

6. Software engineering: fast acceleration, not full replacement

METR defines task-completion time horizon as the human-expert task duration at which an AI agent succeeds with a given reliability. METR’s current suite is mostly software engineering, ML, and cybersecurity. METR warns that measurements above 16 hours are unreliable with its current task suite. [10]

Anthropic reports that task horizons have been doubling roughly every 4 months. It places Opus 4.6 around 12-hour tasks and says week-scale tasks could come into range in 2027 if the trend holds. [18]

Anthropic reports that as of May 2026, more than 80% of code merged into Anthropic’s codebase was authored by Claude. It also reports that typical Anthropic engineers merged 8× as much code per day in Q2 2026 as in 2024. [18]

FrontierCode tests whether coding agents produce mergeable production-quality PRs. Reported Diamond scores:

Claude Opus 4.8: 13.4%
 GPT-5.5: 6.3%
 Gemini 3.1 Pro: 4.7%
 Fable 5 discussed value: 29.3% xhigh [14][5]

ProgramBench tests whether agents can rebuild software from only executable plus documentation, without source code or tests. [13]

ProgramBench dataset:

200 tasks
 Median code lines: 8,635
 Max code lines: 2,701,283
 Median files: 50
 Max files: 5,342
 Median tests: 770
 Max tests: 14,645 [13]

ProgramBench result:

No model fully resolved any task
 Best model passed 95%+ tests on 3.0% of tasks
 Claude Opus 4.7: 0.0% resolved, 3.0% almost
 Claude Opus 4.6: 0.0% resolved, 2.5% almost
 Claude Sonnet 4.6: 0.0% resolved, 1.6% almost [13]

Thesis: models are already strong in implementation loops, debugging, migration, testing, and tool-mediated repo work. High-level architecture, open-ended decomposition, and production-quality mergeability remain bottlenecks.

7. AI-R&D acceleration

OpenAI states that AI doing AI research may become a determining factor of progress within the next few years, with March 2028 as an explicit milestone for significant AI contribution to research. [2]

Anthropic recursive-self-improvement data:

Claude-authored merged code at Anthropic: >80% as of May 2026
 Engineer code/day output: 8× Q2 2026 versus 2024
 Task-horizon doubling: roughly every 4 months
 Training-code optimization: Claude Opus 4 in May 2025 averaged ~3× speedup over starting code
 Training-code optimization: Claude Mythos Preview in April 2026 achieved ~52×
 Human researcher comparison: 4–8 hours to reach 4×
 Open-ended safety research task: agents recovered 97% of a performance gap over 800 cumulative hours and ~$18k compute
 Human comparison: two researchers recovered 23% in about a week [18]

PostTrainBench tested whether LLM agents can automate LLM post-training. Best agent result discussed: ~23.2% weighted average versus 51.1% for official instruct-tuned models. [17]

CORE-Bench Hard tested computational reproducibility of scientific papers. Result discussed: Claude Code + Opus 4.5 reached 77.78% verified and 95.5% with manual validation. [16]

FrontierMath data discussed:

GPT-5.5 xhigh: 85% on Tiers 1–3
 Google AI Co-Mathematician: 76% on Tier 4
 FrontierMath audit addressed errors in 42% of problems [21][22]

Thesis: AI-R&D is not fully autonomous, but bounded AI-R&D loops are already measurable. The hinge is whether agents can reliably generate, test, evaluate, and improve systems across long loops.

8. Broad-autonomy counterweights

ARC-AGI-3 evaluates novel long-horizon interactive environments. ARC analyzed 160 replays and reasoning traces from GPT-5.5 and Opus 4.7. [11]

Scores discussed:

GPT-5.5: 0.43%
 Opus 4.7: 0.18%
 Opus 4.8 update discussed: 1.5% [11]

ARC failure modes: models notice local effects but form false world models, over-map new environments to familiar abstractions, solve individual levels without extracting transferable mechanics. [11]

Agents’ Last Exam measures long-horizon economically valuable professional workflows with verifiable outcomes. [12]

Scale:

55 targeted sub-industries
 1.5K+ tasks collected toward 5K target
 300+ experts [12]

Domains include After Effects motion/VFX, Siemens NX 3D modeling, Unreal Engine scene setup and rendering, Moldex3D mold-flow analysis, Rhino urban design/energy analysis, and FSLeyes neuroimaging. [12]

Hard-tier result discussed: average full pass rate around 2.6% across mainstream harness/backbone setups. [12]

No-CoT “Think Fast” data:

30,000+ questions
 43 benchmarks
 No-CoT task-completion horizon doubled roughly yearly over the prior six years
 GPT-5.5 no-CoT 50% task horizon: >3 minutes
 GPT-5.5 no-CoT reasoning-token equivalent: >1,500 o3-mini reasoning tokens
 Median forecast: >7 minutes by 2028, ~25 minutes by 2030 [20]

Thesis: scaffolded agents are advancing faster than raw no-CoT reasoning, but broad general autonomy is not solved. Novel adaptation, long-horizon world-model formation, architecture, and cross-domain professional workflows remain major bottlenecks.

9. Infrastructure and economics

Epoch data:

Frontier language-model training compute grew 5× per year since 2020
 Training compute doubled every 5.2 months
 Top-5 training compute trend grew ~10,000× since 2020
 Pretraining compute efficiency improved ~3.0× per year
 Pretraining efficiency doubled every 7.6 months
 Training cost grew 3.5× per year since 2020
 Training cost doubled every 7 months
 Context windows grew 30× per year since 2023
 Context windows doubled every 2.4 months
 AI-chip compute stock grew 3.4× per year since 2022
 AI-chip compute stock doubled about every 7 months
 Frontier AI labs raised more than $170B
 US holds about 75% of global GPU cluster performance
 AI chip performance per dollar improved ~37–40% per year
 GPU energy efficiency improved 34% per year since 2008
 Memory bandwidth grew 28% per year since 2008 [23]

Epoch data-center estimates:

Meta Prometheus: 600 MW IT power, $24B capex, 800k H100-equivalent
 Meta Hyperion expected by January 2028: 3.7M H100-equivalent
 1GW AI data-center cost: ~$38B capex
 Gigawatt-scale AI data-center build time: ~2.1 years [23]

IEA data:

Global data-center electricity consumption projected to roughly double from 485 TWh in 2025 to 950 TWh in 2030
 Major tech capex exceeded $400B in 2025
 Major tech capex expected to rise another 75% in 2026
 AI-factory capacity more than tripled in 18 months
 HBM shortage expected to persist through at least end-2027 [24]

Thesis: AI capability is being pushed by training compute, inference/test-time compute, and compute efficiency. Energy, chips, HBM, power, and data-center construction are now direct AI capability variables.

10. Labor exposure

Anthropic Economic Index:

1M Claude.ai conversations analyzed
 1M first-party API conversations analyzed
 Computer & Mathematical tasks accounted for 35% of Claude.ai conversations in the March 2026 report
 Users choose Opus more for higher-wage tasks
 Opus was used 4 percentage points more than average for coding among paying Claude.ai users [25]

Anthropic labor-market data:

Claude currently covers 33% of tasks in Computer & Math
 Computer Programmers: 75% coverage
 Data Entry Keyers: 67% coverage
 Customer service and data entry among highly exposed occupations
 No clear unemployment effect yet in high-exposure occupations
 Tentative slowed hiring for young workers in exposed occupations [26]

Dario Amodei statements:

Powerful AI could arrive as early as 2026
 Powerful AI definition: smarter than Nobel Prize winner across fields, can act through human digital interfaces, can complete hours/days/weeks tasks autonomously, can run millions of independent copies
 Powerful AI could be 1–2 years away
 AI may disrupt 50% of entry-level white-collar jobs over 1–5 years
 Long-term income support, UBI, or universal capital accounts may be needed if labor demand falls permanently [27][28][29]

Thesis: the first exposed labor zone is structured digital work: coding, analytics, support, back-office workflows, document-heavy work, testable engineering, cyber, and AI-native operations.

11. Applied-work datapoint

One applied AI engineer reported building 2 MCP servers in one day, deploying through GitOps repo, Jenkins, Quay, Argo CD, and VDI, with complex terminal commands and thousands of lines of code/config.

Estimated normal enterprise effort: ~30 person-days.

Task category: MCP servers, RAG apps, SDLC agents, orchestration/glue code, deployment/config, enterprise AI engineering.

Thesis: this matches the high-exposure zone: digital, structured, tool-mediated, log/test/deploy feedback loops, reproducible artifacts, and large amounts of boilerplate/integration work.

12. Bottom line

The evidence shows a transition from assistant tools to expert agents in structured digital domains.

Strongest current signals:

GPT-5.5 and Mythos/Fable benchmark jumps [1][4][5]
 AISI/METR task-horizon trends [7][10]
 Anthropic’s >80% Claude-authored code datapoint [18]
 Glasswing vulnerability discovery at scale [8]
 Fable 5 code migration and drug-design examples [5]
 OpenAI’s March 2028 automated researcher target [2]
 AI-R&D loop evidence from Anthropic, CORE-Bench, PostTrainBench, and FrontierMath [16][17][18][21]
 Infrastructure scaling from Epoch and IEA [23][24]
 Counterweights from ARC-AGI-3, ProgramBench, FrontierCode, Agents’ Last Exam, and no-CoT horizon work [11][12][13][14][20]

Final thesis:

AI progress is moving upward in abstraction.

2024: assistants
 2025: collaborators
 2026: expert agents
 2027–2028: narrow automated AI-R&D loops
 2028–2031: broad structured digital-work automation
 2030–2035: institutional and labor-market reorganization

The transition is:

AI systems are becoming reliable enough to operate inside increasingly large verified loops.

References

[1] OpenAI — Introducing GPT-5.5
 https://openai.com/index/introducing-gpt-5-5/

[2] OpenAI — Built to benefit everyone: our plan
 https://openai.com/index/built-to-benefit-everyone-our-plan/

[3] OpenAI — An OpenAI model has disproved a central conjecture in discrete geometry
 https://openai.com/index/model-disproves-discrete-geometry-conjecture/

[4] Anthropic — Project Glasswing
 https://www.anthropic.com/glasswing

[5] Anthropic — Claude Fable 5 and Claude Mythos 5
 https://www.anthropic.com/news/claude-fable-5-mythos-5

[6] Anthropic — Statement on the US government directive to suspend access to Fable 5 and Mythos 5
 https://www.anthropic.com/news/fable-mythos-access

[7] UK AI Security Institute — How fast is autonomous AI cyber capability advancing?
 https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing

[8] Anthropic — Project Glasswing: An initial update
 https://www.anthropic.com/research/glasswing-initial-update

[9] Anthropic Red Team — N-days
 https://red.anthropic.com/2026/n-days/

[10] METR — Task-Completion Time Horizons of Frontier AI Models
 https://metr.org/time-horizons/

[11] ARC Prize — Analyzing GPT-5.5 & Opus 4.7 with ARC-AGI-3
 https://arcprize.org/blog/arc-agi-3-gpt-5-5-opus-4-7-analysis

[12] Agents’ Last Exam
 https://agents-last-exam.org/

[13] ProgramBench — Can Language Models Rebuild Programs From Scratch?
 https://arxiv.org/html/2605.03546v1

[14] Cognition — Introducing FrontierCode
 https://cognition.ai/blog/frontier-code

[15] DeepSWE GitHub
 https://github.com/datacurve-ai/deep-swe

[16] CORE-Bench Hard Leaderboard
 https://hal.cs.princeton.edu/corebench_hard

[17] PostTrainBench — Can LLM Agents Automate LLM Post-Training?
 https://arxiv.org/html/2603.08640v2

[18] Anthropic — When AI builds itself
 https://www.anthropic.com/institute/recursive-self-improvement

[19] Anthropic — Paving the way for agents in biology
 https://www.anthropic.com/research/agents-in-biology

[20] Think Fast — Estimating No-CoT Task-Completion Time Horizons of Frontier Models
 https://arxiv.org/abs/2606.07157

[21] Epoch AI — FrontierMath Open Problems
 https://epoch.ai/frontiermath/open-problems

[22] Epoch AI — Data on AI Capabilities and Benchmarking
 https://epoch.ai/benchmarks

[23] Epoch AI — Trends in Artificial Intelligence
 https://epoch.ai/trends

[24] IEA — Key Questions on Energy and AI
 https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

[25] Anthropic — Economic Index March 2026 Report
 https://www.anthropic.com/research/economic-index-march-2026-report

[26] Anthropic — Labor market impacts of AI
 https://www.anthropic.com/research/labor-market-impacts

[27] Dario Amodei — Machines of Loving Grace
 https://www.darioamodei.com/essay/machines-of-loving-grace

[28] Dario Amodei — The Adolescence of Technology
 https://darioamodei.com/essay/the-adolescence-of-technology

[29] Dario Amodei — Policy on the AI Exponential
 https://darioamodei.com/post/policy-on-the-ai-exponential

## X Article Metadata

- Title: State of AI, June 2026: data and thesis
- Preview: Thesis: AI progress has moved from chatbot assistance to expert technical agents. The reliable unit of work is moving upward: from short prompts to tool use, codebases, exploit chains, research loops,

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
