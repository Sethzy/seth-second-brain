---
type: raw_capture
source_type: web
title: "Anchoring AI to a reference application"
url: "https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html"
collected_at: 2026-06-13T10:49:37Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Anchoring AI to a reference application

Source: https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html

## Capture Text

# Anchoring AI to a reference application

Original URL: https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html
Fetched URL: https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html
Awesome Harness summary: Thoughtworks on constraining agents with concrete exemplars so they produce more consistent output.

## Fetched Content

# Anchoring AI to a reference application

[![Photo of Birgitta BÃ¶ckeler](bb.jpg)](https://birgitta.info)

[Birgitta BÃ¶ckeler](https://birgitta.info)

Birgitta is a Distinguished Engineer and AI-assisted delivery
expert at Thoughtworks. She has over 20 years of experience as a software
developer, architect and technical leader.

[![](donkey-card.png)](../exploring-gen-ai.html)

This article is part of [âExploring Gen
AIâ](../exploring-gen-ai.html). A series capturing Thoughtworks technologists' explorations of using gen ai technology for
software development.

25 September 2025

Service templates are a typical building block in the âgolden pathsâ organisations build for their engineering teams, to make it easy to do the right thing. The templates are supposed to be the role models for all the services in the organisation, always representing the most up to date coding patterns and standards.

One of the challenges with service templates though is that once a team instantiated a service with one, itâs tedious to feed template updates back to those services. Can GenAI help with that?

## Reference application as sample provider

As part of a larger experiment that I recently wrote about [here](https://martinfowler.com/articles/pushing-ai-autonomy.html), I created an MCP server that gives a coding assistant access to coding samples for typical patterns. In my case, this was for a Spring Boot web application, where the patterns were repository, service and controller classes. It is a well established prompting practice at this point that providing LLMs with examples of the outputs that we want leads to better results. To put âproviding examplesâ into fancier terms: This is also called â[few-shot prompting](https://martinfowler.com/articles/pushing-ai-autonomy.html)â, or âin-context learningâ.

When I started working with code samples in prompts, I quickly realised how tedious this was, because I was working in a natural language markdown file. It felt a little bit like writing my first Java exams at university, in pencil: You have no idea if the code youâre writing actually compiles. And whatâs more, if youâre creating prompts for multiple coding patterns, you want to keep them consistent with each other. Maintaining code samples in a reference application project that you can compile and run (like a service template) makes it a lot easier to provide AI with compilable, consistent samples.

![Screenshot showing a git commit diff that introduces @Slf4j to a controller, and log.debug statements to each controller method](drift-commit-example.png)

## Detect drift from the reference application

Now back to the problem statement I mentioned at the beginning: Once code is generated (be that with AI, or with a service template), and then further extended and maintained, codebases often drift away from the role model of the reference application.

So in a second step, I wondered how we might use this approach to do a âcode pattern drift detectionâ between the codebase and the reference application. I tested this with a relatively simple example, I added a logger and log.debug statements to the reference applicationâs controller classes:

![Screenshot of a git commit diff in the reference application, showing a controller with an added @Slf4j annotation, and a log.debug statement in one of the endpoint mappings.](drift-mcp-server-samples.png)

Then I expanded the MCP server to provide access to the git commits in the reference application. Asking the agent to first look for the actual changes in the reference gives me some control over the scope of the drift detection, I can use the commits to communicate to AI exactly what type of drift Iâm interested in. Before I introduced this, when I just asked AI to compare the reference controllers with the existing controllers, it went a bit overboard with lots of irrelevant comparisons, and I saw this commit-scoping approach have a good impact.

![An expanded version of the previous diagram, this time showing the setup for the drift detection. The prompt asks the agent to find latest changes, the agent gets the latest commit from the reference application, via MCP server. The agent then looks at the diff and uses it to analyse the target application, and to create a drift report. In a second step, the user can then ask the agent to write code that closes the gaps identified in the report.](drift-mcp-server-commits.png)

In the first step, I just asked AI to generate a report for me that identified all the drift, so I could review and edit that report, e.g. remove findings that were irrelevant. In the second step, I asked AI to take the report and write code that closes the gaps identified.

### When is AI bringing something new to the table?

A thing as simple as adding a logger, or changing a logging framework, can also be done deterministically by codemod tools like [OpenRewrite](https://docs.openrewrite.org/). So bear that in mind before you reach for AI.

Where AI can shine is whenever we have drift that needs coding that is more dynamic than is possible with regular-expression-based codemod recipes. In an advanced form of the logging example, this might be turning non-standardised, rich log statements into a structured format, where an LLM might be better at turning a wide variety of existing log messages into the respective structure.

The example MCP server is included in [the repository that accompanies](https://github.com/birgitta410/pushing-ai-autonomy-article) [the original article](https://martinfowler.com/articles/pushing-ai-autonomy.html).

latest article (Mar 04):

[Humans and Agents in Software Engineering Loops](humans-and-agents.html)

previous article:

[To vibe or not to vibe](to-vibe-or-not-vibe.html)

next article:

[Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](sdd-3-tools.html)

[![](donkey-card.png)](/articles/exploring-gen-ai.html)
