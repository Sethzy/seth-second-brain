---
type: raw_capture
source_type: web
title: "How CodeRabbit used Claude to build an agent orchestration system"
url: "https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system/"
canonical_url: "https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system/"
vendor_blog: claude
published_at: 2026-05-27
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# How CodeRabbit used Claude to build an agent orchestration system

Original URL: https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system/
Published: 2026-05-27
Captured: 2026-06-14T02:32:25+00:00

Description: CodeRabbit built a layer on Claude that sits between a coding request and a coding agent, producing a structured coding plan the team can review before any code gets generated.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

# How CodeRabbit used Claude to build an agent orchestration system

CodeRabbit built a layer on Claude that sits between a coding request and a coding agent, producing a structured coding plan the team can review before any code gets generated.

Watch the webinar

[Watch the webinar](https://www.anthropic.com/webinars/how-coderabbit-orchestrates-agents-to-strengthen-ai-generated-code)Watch the webinar

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  May 27, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system

*In our series,* ***How startups build with Claude***, we highlight how startups are transforming their industries with AI. In this article, we share how CodeRabbit built an agent orchestration layer that plans before AI generates code.

| The quick pitch | |
| --- | --- |
| Name | CodeRabbit |
| Founded | 2023 |
| Founders | Harjot Gill, CEO |
| Stack | Claude Platform, Claude Code |
| Scale | Reviews 2 million PRs per week across 15,000+ customers |

AI coding tools have collapsed the time between idea and working prototype. CodeRabbit, an AI code review platform, has noticed a different trend climbing alongside that throughput: code that compiles and passes tests but doesn't do what the team actually meant to build.

David Loker, VP of AI at CodeRabbit, locates the cause upstream of the model. Experienced developers often assume coding agents understand the same context they do, so they don’t write down requirements that feel obvious to them. The coding agent then fills the gaps with whatever it considers plausible.

To close that gap, CodeRabbit used Claude to design and build an agent orchestration system that runs a structured planning phase before any code is generated. The team's working thesis is that planning quality determines output quality, and the cheaper code generation gets, the more expensive it becomes to move in the wrong direction.

## **Addressing the internal knowledge gap in AI coding**

When the CodeRabbit team studied AI-generated pull requests across their customer base, the most frequent failure mode was code that compiled and passed tests, yet still didn't solve the problem it was built to solve.

"As we gain experience as developers, we internalize knowledge," Loker says. "All those things are in our head, and we assume other developers know them too. But then we make that assumption of the AI system as well, that it also implicitly understands. We're not even aware that we're assuming those things."

Vague prompts force the underlying system to fill gaps with whatever it considers plausible. That guess often diverges from what the developer had in mind.

Loker offers a personal example. While building a memory system on a side project, he spent hours iterating with a coding agent until everything ran. When he asked the agent how to use it, the instructions told him to pass in a user token. There was no login page. He had specified that the system required users but never said users needed a way to sign in. The agent filled the gap, and hours of work landed in a product missing a front door.

"What ends up happening is you build a lot more stuff on top of it, then much later you find there's a problem," Loker says. "In AI workflows, late validation can be very expensive."

## **An orchestration layer that runs before AI coding solutions**

CodeRabbit's response was to insert a planning system in front of code generation. It coordinates multiple Claude models to analyze requirements and surface assumptions before producing a structured execution plan that defines what should be built and what constraints it needs to satisfy.

"This planning system is not meant to replace Claude Code's Plan Mode," Loker says. "It's a higher level orchestration that happens before Claude Code, to point it in a really narrow and right direction where everything that needs to be explicit is made explicit, and we are aware of all assumptions that are being made."

The output is a collaborative product requirements document (PRD): a plan created with full context, validated by stakeholders across the team, and reviewed before implementation starts. Claude Code picks up that plan and uses it to generate a fine-grained implementation plan. The plan becomes a shared artifact that captures what was decided and why, which not only helps teams avoid rework and validate later that the output matched the original intent, but also onboard new engineers.

## **Routing across the Claude model family**

CodeRabbit matches each model tier to task complexity to optimize for cost and latency. Opus drives the orchestration loop and the higher-level strategic work of understanding the problem and setting overall direction. Sonnet takes that output and sequences it into structured planning steps. Haiku handles narrowly scoped operations like context distillation and targeted tool use, where the question is specific enough that a smaller model can answer it well.

"If Haiku does as well as Sonnet on a given task, we use Haiku," Loker says. "If the evaluation harness tells us the plan quality improves when we give Opus more room, we give it more room. We don't guess."

## **Building an eval harness for plan quality**

CodeRabbit had a mature evaluation system for code review, but nothing for evaluating planning output. Building that infrastructure became its own project.

The system started with hand-tuned examples and manual inspection. The team developed a library of LLM judges that scored specific dimensions of plan quality. Because plans eventually produce code, the team could also measure whether the generated code worked, whether it contained extra scope, and how many tokens it took to get there. Running the same task with and without the planning step gave them a way to isolate the value of planning itself.

"We didn't realize what the right level of detail was going to be for that plan," Loker says. Plans that were too granular went stale the moment the codebase shifted. Plans that were too high-level left room for the agent to fill in assumptions, which was the original problem the planning layer was meant to solve. Finding the working level of abstraction took iteration, which is what the eval harness made possible.

## **Catching errors before any code gets written**

In an AI-native coding workflow, many of the decisions that used to surface during code review are now made earlier, in the planning layer. Building a plan that the team can review and align on before code generation starts catches mistakes early.

"What we've built, using the Claude ecosystem, is a team-wide planning system," Loker says. "The plan itself becomes a quality gate. If we can make sure the quality of that plan is really good upfront, the downstream effect is very pronounced. You end up with a lot better code at the end of it."

| Best practices from the CodeRabbit team | |
| --- | --- |
| What outcome are you actually trying to create, and how do you measure? | Be explicit not just in specifications to the AI but also define what you want in the MPP (maximum possible product). |
| What assumptions are still implicit? | Ask Claude: what is missing? Are there any parts of the plan that are coming out as implicit assumptions instead of explicit specifications? |
| What workflows or edge cases are easy to forget? | Ask Claude to help identify places or cases that you may not have taken into account. |
| How will you know the output matches intent before rollout? | Create a record of work: a chronicle of planning artifacts that is saved and reused. |

**Build your startup on the** [**Claude Platform**](https://platform.claude.com/login?returnTo=%2F%3F)**.**

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Oct 8, 2025

### Beyond permission prompts: making Claude Code more secure and autonomous

Claude Code

[Beyond permission prompts: making Claude Code more secure and autonomous](#)Beyond permission prompts: making Claude Code more secure and autonomous

[Beyond permission prompts: making Claude Code more secure and autonomous](/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous)Beyond permission prompts: making Claude Code more secure and autonomous

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Jun 5, 2026

### How one Anthropic seller rebuilt his team's workflows with Claude Code

Claude Code

[How one Anthropic seller rebuilt his team's workflows with Claude Code](#)How one Anthropic seller rebuilt his team's workflows with Claude Code

[How one Anthropic seller rebuilt his team's workflows with Claude Code](/blog/how-anthropic-uses-claude-gtm-engineering)How one Anthropic seller rebuilt his team's workflows with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jun 3, 2026

### Lessons from building Claude Code: How we use skills

Claude Code

[Lessons from building Claude Code: How we use skills](#)Lessons from building Claude Code: How we use skills

[Lessons from building Claude Code: How we use skills](/blog/lessons-from-building-claude-code-how-we-use-skills)Lessons from building Claude Code: How we use skills

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

Jun 2, 2026

### A harness for every task: dynamic workflows in Claude Code

Claude Code

[A harness for every task: dynamic workflows in Claude Code](#) A harness for every task: dynamic workflows in Claude Code

[A harness for every task: dynamic workflows in Claude Code](/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) A harness for every task: dynamic workflows in Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
