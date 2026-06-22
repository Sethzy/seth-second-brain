---
type: raw_capture
source_type: pasted
title: "Archive note: Must do tmr.md"
url: "file:///Users/sethlim/Desktop/Archive/Must%20do%20tmr.md"
collected_at: 2026-06-11T02:20:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Desktop/Archive/Must do tmr.md"
sha256: "fee59bda03a71c88e092df472599d5245662373c5a05ac48e5b90e9f9700d2e8"
---

# Archive note: Must do tmr.md

Source file: `/Users/sethlim/Desktop/Archive/Must do tmr.md`

## Capture Text

# Must do tmr    
# [https://docs.devin.ai/work-with-devin/deepwiki-mcp](https://docs.devin.ai/work-with-devin/deepwiki-mcp)   To view keyboard shortcuts, press question mark  
[View keyboard shortcuts](https://x.com/i/keyboard_shortcuts)  
  
## Post  
See new posts  
Conversation  
  
  
  
  
**[Andrej Karpathy](https://x.com/karpathy)**  
[@karpathy](https://x.com/karpathy)  
On DeepWiki and increasing malleability of software.  
  
This starts as partially a post on appreciation to DeepWiki, which I routinely find very useful and I think more people would find useful to know about. I went through a few iterations of use:  
  
Their first feature was that it auto-builds wiki pages for github repos (e.g. nanochat here) with quick Q&A:  
[https://](https://t.co/DQHXagUwK0)  
[deepwiki.com/karpathy/nanoc](https://t.co/DQHXagUwK0)  
[hat](https://t.co/DQHXagUwK0)  
Just swap "github" to "deepwiki" in the URL for any repo and you can instantly Q&A against it. For example, yesterday I was curious about "how does torchao implement fp8 training?". I find that in *many* cases, library docs can be spotty and outdated and bad, but directly asking questions to the code via DeepWiki works very well. The code is the source of truth and LLMs are increasingly able to understand it.  
  
But then I realized that in many cases it's even a lot more powerful not being the direct (human) consumer of this information/functionality, but giving your agent access to DeepWiki via MCP. So e.g. yesterday I faced some annoyances with using torchao library for fp8 training and I had the suspicion that the whole thing really shouldn't be that complicated (wait shouldn't this be a Function like Linear except with a few extra casts and 3 calls to torch._scaled_mm?) so I tried:  
  
*"Use DeepWiki MCP and Github CLI to look at how torchao implements fp8 training. Is it possible to 'rip out' the functionality? Implement nanochat/fp8.py that has identical API but is fully self-contained"*  
*"Use DeepWiki MCP and Github CLI to look at how torchao implements fp8 training. Is it possible to 'rip out' the functionality? Implement nanochat/fp8.py that has identical API but is fully self-contained"*  
  
Claude went off for 5 minutes and came back with 150 lines of clean code that worked out of the box, with tests proving equivalent results, which allowed me to delete torchao as repo dependency, and for some reason I still don't fully understand (I think it has to do with internals of torch compile) - this simple version runs 3% faster. The agent also found a lot of tiny implementation details that actually do matter, that I may have naively missed otherwise and that would have been very hard for maintainers to keep docs about. Tricks around numerics, dtypes, autocast, meta device, torch compile interactions so I learned a lot from the process too. So this is now the default fp8 training implementation for nanochat  
[https://](https://t.co/3i5cv6grWm)  
[github.com/karpathy/nanoc](https://t.co/3i5cv6grWm)  
[hat/commit/e569b59f92aea06bf8fc1c48489b3cc2e57189f4](https://t.co/3i5cv6grWm)  
  
Anyway TLDR I find this combo of DeepWiki MCP + GitHub CLI is quite powerful to "rip out" any specific functionality from any github repo and target it for the very specific use case that you have in mind, and it actually kind of works now in some cases. Maybe you don't download, configure and take dependency on a giant monolithic library, maybe you point your agent at it and rip out the exact part you need. Maybe this informs how we write software more generally to actively encourage this workflow - e.g. building more "bacterial code", code that is less tangled, more self-contained, more dependency-free, more stateless, much easier to rip out from the repo (  
Anyway TLDR I find this combo of DeepWiki MCP + GitHub CLI is quite powerful to "rip out" any specific functionality from any github repo and target it for the very specific use case that you have in mind, and it actually kind of works now in some cases. Maybe you don't download, configure and take dependency on a giant monolithic library, maybe you point your agent at it and rip out the exact part you need. Maybe this informs how we write software more generally to actively encourage this workflow - e.g. building more "bacterial code", code that is less tangled, more self-contained, more dependency-free, more stateless, much easier to rip out from the repo (  
[https://](https://x.com/karpathy/status/1941616674094170287)  
[x.com/karpathy/statu](https://x.com/karpathy/status/1941616674094170287)  
[s/1941616674094170287](https://x.com/karpathy/status/1941616674094170287)  
)   
There's obvious downsides and risks to this, but it is fundamentally a new option that was not possible or economical before (it would have cost too much time) but now with agents, it is. Software might become a lot more fluid and malleable. "Libraries are over, LLMs are the new compiler" :). And does your project really need its 100MB of dependencies?  
  
  
[From deepwiki.com](https://t.co/DQHXagUwK0)  
[From deepwiki.com](https://t.co/DQHXagUwK0)  
[1:12 AM · Feb 12, 2026](https://x.com/karpathy/status/2021633574089416993)  
·  
·  
**[95.6K](https://x.com/karpathy/status/2021633574089416993/analytics)**  
**[95.6K](https://x.com/karpathy/status/2021633574089416993/analytics)**  
[ Views](https://x.com/karpathy/status/2021633574089416993/analytics)  
Relevant  
[View quotes](https://x.com/karpathy/status/2021633574089416993/quotes)  
  
  
  
  
##   
  
  
  
  
  
**[Mark Saroufim](https://x.com/marksaroufim)**  
[@marksaroufim](https://x.com/marksaroufim)  
·  
[2h](https://x.com/marksaroufim/status/2021636675039113612)  
FWIW the torchao team is quite happy you're ripping out just what you need, that's exactly why we created the project!  
  
  
  
  
**[Andrej Karpathy](https://x.com/karpathy)**  
[@karpathy](https://x.com/karpathy)  
·  
[2h](https://x.com/karpathy/status/2021637660532764999)  
Good to hear! Almost every code base is suddenly half "useful library code" (legacy) and half "docs++". i.e. with LLMs in hand, the torchao repo is *significantly* better docs on how to do fp8 training in PyTorch than official fp8 training docs. This is new & interesting.  
  
  
  
Show replies  
  
  
  
  
  
**[Enes Poyraz](https://x.com/ens_pyrz)**  
[@ens_pyrz](https://x.com/ens_pyrz)  
·  
[2h](https://x.com/ens_pyrz/status/2021635165806854211)  
Great Insight. But, as a Software Engineer, i find this "getting of dependencies"-trend quite concerning. Dependencies, such as libraries are "good abstractions". It's Code that gets "updated" and "security patched" while i can focus on solving my problem.  
  
  
  
  
**[Andrej Karpathy](https://x.com/karpathy)**  
[@karpathy](https://x.com/karpathy)  
·  
[2h](https://x.com/karpathy/status/2021636275120583096)  
So that's why I mentioned risks. But imo it easily cuts both ways - libraries and dependencies can be a source of risks and vulnerabilities in the first place, e.g. supply chain attacks. They also change and impose maintenance burden. There's a lot more.  
  
  
  
  
  
**[Eddie](https://x.com/pussymonious)**  
[@pussymonious](https://x.com/pussymonious)  
·  
[1h](https://x.com/pussymonious/status/2021641143780569487)  
I love how most of the replies to this post are AI written   
![1f923.svg](Attachments/CA30E5AF-F5F2-4578-806D-FC14F3940F59.svg)  
  
  
  
  
**[Andrej Karpathy](https://x.com/karpathy)**  
[@karpathy](https://x.com/karpathy)  
·  
[1h](https://x.com/karpathy/status/2021642321100677434)  
It's so obvious and annoying isn't it.  
  
Sometimes I try to block the accounts which is just a total waste of time.  
  
  
  
Show replies  
  
  
  
  
  
**[Daniel Hensley](https://x.com/dw_hensley)**  
[@dw_hensley](https://x.com/dw_hensley)  
·  
[1h](https://x.com/dw_hensley/status/2021649993677885663)  
Beyond your specific point about dependencies and to the broader pre-computed information in-the-loop for agents point here: This is exactly the thesis we have.  
  
We pre-compute context for codebases to make it impossible for agents to “not know what they don’t know” when working  
Show more  
  
  
  
  
  
**[Xirtam Esrevni](https://x.com/XirtamEsrevni)**  
[@XirtamEsrevni](https://x.com/XirtamEsrevni)  
·  
[51m](https://x.com/XirtamEsrevni/status/2021658341605556542)  
hmm, so whats better for use with Cursor agent:  
  
1. give them the deepwiki link to a repo  
2. give them the output from   
[https://](https://t.co/cB3Jum9nFG)  
[gitingest.com](https://t.co/cB3Jum9nFG)  
[gitingest.com](https://t.co/cB3Jum9nFG)  
  
  
  
  
  
**[Anoop Mehendale](https://x.com/aprateem)**  
[@aprateem](https://x.com/aprateem)  
·  
[2h](https://x.com/aprateem/status/2021637117592707315)  
[@grok](https://x.com/grok)  
[@grok](https://x.com/grok)  
 can you dumb this down, explain in simple terms and talk about potential implications?  
  
  
  
  
  
**[yrzhe.top](https://x.com/yrzhe_top)**  
  
![9KKzNslR_bigger.jpg](Attachments/8732C0DB-41C9-4733-A3B3-4A6C805B7B4E.jpg)  
[@yrzhe_top](https://x.com/yrzhe_top)  
·  
[1h](https://x.com/yrzhe_top/status/2021652761968804215)  
Seeing this from the consumer product side. We build "skills" - self-contained modules, <200 lines, zero deps - that agents compose at runtime for non-technical users.  
When an agent hits tangled dependencies, it doesn't crash. It hallucinates a workaround that looks correct.  
Show more  
  
  
  
  
  
**[Sebastian Sigl](https://x.com/sesigl)**  
[@sesigl](https://x.com/sesigl)  
·  
[1h](https://x.com/sesigl/status/2021652826724655237)  
The part I keep thinking about: this works beautifully when you're a solo researcher who understands exactly what they extracted and why. The team version of this is where it gets interesting.  
  
When 5 engineers on a team each rip out their own version of the same library  
Show more  
  
* **		Relevant people**  [   ](https://x.com/karpathy)    **[Andrej Karpathy ](https://x.com/karpathy)**[@karpathy ](https://x.com/karpathy)I like to train large deep neural nets. Previously Director of AI @ Tesla, founding team @ OpenAI, PhD @ Stanford.  
Trending now  
  
## What’s happening  
Trending in Singapore  
**KENGNAMPING AT OneDynasty 2026**  
Politics · Trending  
**Zionism**  
Business & finance · Trending  
**#AlgoTrading**  
Trending in Singapore  
**wts lfb**  
[Show more](https://x.com/explore/tabs/for-you)  
[Terms of Service](https://x.com/tos)  
 |  
[Privacy Policy](https://x.com/privacy)  
[Privacy Policy](https://x.com/privacy)  
 |  
[Cookie Policy](https://support.x.com/articles/20170514)  
 |  
[Accessibility](https://help.x.com/resources/accessibility)  
[Accessibility](https://help.x.com/resources/accessibility)  
 |  
[Ads info](https://business.x.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo)  
 |  
More  
© 2026 X Corp.  
  
  
![Attachment.png](Attachments/9B44C89D-F063-458F-9229-910A84A2E1A9.png)  
   

