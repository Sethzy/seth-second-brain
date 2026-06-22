---
type: raw_capture
source_type: x
url: https://x.com/ysu_nlp/status/1754365367294562680
original_url: https://x.com/ysu_nlp/status/1754365367294562680
author: "Yu Su"
handle: ysu_nlp
status_id: 1754365367294562680
captured_at: 2026-06-19T19:38:36+08:00
published_at: "Mon Feb 05 04:44:32 +0000 2024"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 35
  likes: 156
---

# X post by @ysu_nlp

## Source

- Original: [https://x.com/ysu_nlp/status/1754365367294562680](https://x.com/ysu_nlp/status/1754365367294562680)
- Canonical: [https://x.com/ysu_nlp/status/1754365367294562680](https://x.com/ysu_nlp/status/1754365367294562680)
- Author: Yu Su (@ysu_nlp)

## Verbatim Text

Thanks @_akhaliq for sharing our work. So, let's talk about planning. 

Planning is a hallmark of human intelligence. It is an evolutionary feat built upon numerous other capacities: 
> using various tools to iteratively collect information and make decisions
> recording intermediate plans (in working memory or on a physical device) for deliberation
> exploring alternative plans by running simulations, which in turn depends on a world model
> and many others (trial-and-error learning, case-based reasoning, backtracking, etc.)

For decades, researchers have been attempting to develop AI agents to mimic humans’ planning capability, but often in constrained settings because many of the cognitive substrates necessary for human-level planning have been lacking. AI agents that can work robustly in the largely unconstrained settings in which humans operate remain a distant goal.

Here entered language agents, the new superstar in town
Language agents (aka LLM/AI/autonomous agents) powered by LLMs were one of the keywords of 2023, and they are poised to see many real-world applications in 2024. They are characterized by their use of language as a vehicle for thought and communication. Language agents have shown many interesting capabilities such as tool use and various forms of reasoning, which potentially fulfill the role of some of the cognitive substrates that were lacking in earlier AI agents. So, are they capable of more complex planning tasks that were out of reach of prior agents?

TravelPlanner
> To advance this investigation, we propose TravelPlanner, a new planning benchmark that focuses on a common real-world planning scenario—travel planning. This is a challenging, time-consuming task even for humans, but most people can do it successfully, with the right tools and enough time. 
> Travel planning is also interesting in that it's hard for humans to generate a good plan (e.g., our trained annotators take avg 12 mins to annotate a plan), but it's relatively easy for us to judge whether an AI-generated plan is satisfactory. So, if an AI agent can do this, it could become a very useful tool to save us time, in a verifiable and trustworthy way!
> TravelPlanner provides a rich sandbox environment with around 4 million data entries crawled from the Internet that can be accessed via 6 tools. We also meticulously curate 1,225 diverse user queries (along with their reference plans), each imposing a different combination of constraints.

So, can current language agents plan travels?
> TL;DR: not yet. We comprehensively evaluated SOTA LLMs (GPT-4/Gemini/Mixtral/etc.) and planning strategies (ReAct/Reflexion/etc.), but the best success rate we can get is only 0.6% (6 out of 1000) :( 
> Language agents struggle to stay on task, use the right tools to collect information, or keep track of multiple constraints simultaneously. 
> However, we note that the mere possibility for language agents to tackle such a complex problem is in itself non-trivial progress. We hope that TravelPlanner provides a challenging yet meaningful testbed for future language agents to hill-climb towards human-level planning in complex settings.

📌 https://t.co/A12YzLSBxq
📌 Paper: https://t.co/wnLmKcZEuu
📌 Code: https://t.co/aMJitYx5M2
📌 Data: https://t.co/mkv2Pq0JMB

Work from @osunlp led by my amazing students @jianxie_ @DrogoKhal4, joint with @jiangjie_chen @DarthZhu_ @Reza20000722 @tydsh Yanghua Xiao

## Quoted Post

- URL: https://x.com/_akhaliq/status/1754353852155879549
- Author: AK (@_akhaliq)

TravelPlanner

A Benchmark for Real-World Planning with Language Agents

paper page: https://t.co/Eujgifzguo

Planning has been part of the core pursuit for artificial intelligence since its conception, but earlier AI agents mostly focused on constrained settings because many of the cognitive substrates necessary for human-level planning have been lacking. Recently, language agents powered by large language models (LLMs) have shown interesting capabilities such as tool use and reasoning. Are these language agents capable of planning in more complex settings that are out of the reach of prior AI agents? To advance this investigation, we propose TravelPlanner, a new planning benchmark that focuses on travel planning, a common real-world planning scenario. It provides a rich sandbox environment, various tools for accessing nearly four million data records, and 1,225 meticulously curated planning intents and reference plans. Comprehensive evaluations show that the current language agents are not yet capable of handling such complex planning tasks-even GPT-4 only achieves a success rate of 0.6%. Language agents struggle to stay on task, use the right tools to collect information, or keep track of multiple constraints. However, we note that the mere possibility for language agents to tackle such a complex problem is in itself non-trivial progress. TravelPlanner provides a challenging yet meaningful testbed for future language agents.

## Media

- video: https://pbs.twimg.com/ext_tw_video_thumb/1754358248784683008/pu/img/rbNHxq87S_8_XAVC.jpg
- video: https://video.twimg.com/ext_tw_video/1754358248784683008/pu/vid/avc1/1280x720/9rJM5kLIqiCYFBRU.mp4?tag=12

## Capture Note

TweetDetail returned complete normal-post text.
