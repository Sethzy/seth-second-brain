---
type: raw_capture
source_type: web
title: "Context Engineering for Coding Agents"
url: "https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html"
collected_at: 2026-06-13T10:49:23Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Context Engineering for Coding Agents

Source: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html

## Capture Text

# Context Engineering for Coding Agents

Original URL: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
Fetched URL: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
Awesome Harness summary: Thoughtworks guidance on shaping the task environment so coding agents can stay grounded and productive.

## Fetched Content

# Context Engineering for Coding Agents

[![Photo of Birgitta BÃ¶ckeler](bb.jpg)](https://birgitta.info)

[Birgitta BÃ¶ckeler](https://birgitta.info)

Birgitta is a Distinguished Engineer and AI-assisted delivery
expert at Thoughtworks. She has over 20 years of experience as a software
developer, architect and technical leader.

[![](donkey-card.png)](../exploring-gen-ai.html)

This article is part of [âExploring Gen
AIâ](../exploring-gen-ai.html). A series capturing Thoughtworks technologists' explorations of using gen ai technology for
software development.

05 February 2026

The number of options we have to configure and enrich a coding agentâs context has exploded over the past few months. Claude Code is leading the charge with innovations in this space, but other coding assistants are quickly following suit. Powerful context engineering is becoming a huge part of the developer experience of these tools.

Context engineering is relevant for all types of agents and LLM usage of course. My colleague [Bharani Subramaniamâs simple definition](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/talking-context-engineering) is: âContext engineering is curating what the model sees so that you get a better result.â

For coding agents, there is an emerging set of context engineering approaches and terms. The foundation of it are the configuration features offered by the tools (e.g. ârulesâ, âskillsâ), and then the nitty gritty of part is how we conceptually use those features (âspecsâ, various workflows).

This memo is a primer about the current state of context configuration features, using Claude Code as an example at the end.

## What is context in coding agents?

âEverything is contextâ - however, these are the main categories I think of as context configuration in coding agents.

### Reusable Prompts

Almost all forms of AI coding context engineering ultimately involve a bunch of markdown files with prompts. I use âpromptâ in the broadest sense here, like itâs 2023: A prompt is text that we send to an LLM to get a response back. To me there are two main categories of intentions behind these prompts, I will call them:

* **Instructions**: Prompts that tell an agent to do something, e.g. âWrite an E2E test in the following way: â¦â
* **Guidance**: (aka rules, guardrails) General conventions that the agent should follow, e.g. âAlways write tests that are independent of each other.â

These two categories often blend into each other, but Iâve still found it useful to distinguish them.

### Context interfaces

I couldnât really find an established term for what Iâd call **context interfaces**: Descriptions for the LLM of how it can get even more context, should it decide to.

* **Tools**: Built-in capabilities like calling bash commands, searching files, etc.
* **MCP Servers**: Custom programs or scripts that run on your machine (or on a server) and give the agent access to data sources and other actions.
* **Skills**: These newest entrants into coding context engineering are descriptions of additional resources, instructions, documentation, scripts, etc. that the LLM can load on demand when it thinks itâs relevant for the task at hand.

The more of these you configure, the more space they take up in the context. So itâs prudent to think strategically about what context interfaces are necessary for a particular task.

![Coding context visual overview, showing system prompt, context interfaces, instructions and guidance, conversation history](coding-context-overview.png)

**Files in your workspace**

The most basic and powerful context interfaces in coding agents are file reading and searching, to understand your current codebase, so Iâm giving them a special mention here. Itâs worth reflecting on how well your existing code serves as context, basically if you have [AI-friendly codebase design](https://www.thoughtworks.com/radar/techniques/ai-friendly-code-design).

## If and when: Who decides to load context?

* **LLM**: Allowing the LLM to decide when to load context is a prerequisite for running agents in an unsupervised way. But there always remains some uncertainty (dare I say non-determinism) *if* the LLM will actually load the context when we would expect it to. Example: Skills
* **Human**: A human invocation of context gives us control, but reduces the level of automation overall. Example: Slash commands
* **Agent software**: Some context features are triggered by the agent software itself, at deterministic points in time. Example: Claude Code hooks

## How much: Keeping the context as small as possible

One of the goals of context engineering is to balance the amount of context given - not too little, not too much. Even though context windows have technically gotten really big, that doesnât mean that itâs a good idea to indiscriminately dump information in there. An agentâs effectiveness goes down when it gets too much context, and too much context is a cost factor as well of course.

Some of this size management is up to the developer: How much context configuration we create, and how much text we put in there. My recommendation would be to build context like rules files up gradually, and not pump too much stuff in there right from the start. The models have gotten quite powerful, so what you might have had to put into the context half a year ago might not even be necessary anymore.

Transparency about how full the context is, and what is taking up how much space, is a crucial feature in the tools to help us navigate this balance.

![Example of Claude Code's /context command result, giving transparency about what is taking up how much space in the context](claude-code-context.png)

But itâs not all up to us, some coding agent tools are also better at optimising context under the hood than others. They compact the conversation history periodically, or optimise the way tools are represented (like [Claude Codeâs Tool Search Tool](https://www.anthropic.com/engineering/advanced-tool-use)).

## Example: Claude Code

Here is an overview of Claude Codeâs context configuration features as of January 2026, and where they fall in the dimensions described above:

### [CLAUDE.md](http://Claude.md)

**What:** Guidance

**Who decides to load:** Claude Code - Always used at start of a session

**When to use:** For most frequently repeated general conventions that apply to the whole project

**Example use cases:**

* âwe use yarn, not npmâ
* âdonât forget to activate the virtual environment before running anythingâ
* âwhen we refactor, we donât care about backwards compatibilityâ

**Other coding assistants:** Basically all coding assistants have this feature of a main ârules fileâ; There are attempts to standardise it as [`AGENTS.md`](https://agents.md/)

### [Rules](https://code.claude.com/docs/en/memory#modular-rules-with-claude/rules/)

**What:** Guidance

**Who decides to load:** Claude Code, when files at the configured paths have been loaded

**When to use:** Helps organise and modularise guidance, and therefore limit size of the always loaded CLAUDE.md. Rules can be scoped to files (e.g. \*.ts for all TypeScript files), which means they will then only be loaded when relevant.

**Example use cases:** âWhen writing bash scripts, variables should be referred to as ${var} not $var.â paths: \*\*/\*.sh

**Other coding assistants:** More and more coding assistants allow this path-based rules configuration, e.g. GH Copilot and Cursor

### [Slash commands](https://code.claude.com/docs/en/slash-commands)

**What:** Instructions

**Who decides to load:** Human

**When to use:** Common tasks (review, commit, test, â¦) that you have a specific longer prompt for, and that you want to trigger yourself, inside the main context *DEPRECATED in Claude Code, superceded by Skills*

**Example use cases:** `/code-review` Â· `/e2e-test` Â· `/prep-commit`

**Other coding assistants:** Common feature, e.g. GH Copilot and Cursor

### [Skills](https://code.claude.com/docs/en/skills)

**What:** Guidance, instructions, documentation, scripts, â¦

**Who decides to load:** LLM (based on skill description) or Human

**When to use:** In its simplest form, this is for guidance or instructions that you only want to âlazy loadâ when relevant for the task at hand. But you can put whatever additional resources and scripts you want into a skillâs folder, and reference them from the main `SKILL.md` to be loaded.

**Example use cases:**

* JIRA access (skill e.g. describes how agent can use CLI to access JIRA)
* âConventions to follow for React componentsâ
* âHow to integrate the XYZ APIâ

**Other coding assistants:** Cursorâs âApply intelligentlyâ rules were always a bit like this, but theyâre now also switching to Claude Code style Skills

### [Subagents](https://code.claude.com/docs/en/sub-agents)

**What:** Instructions + Configuration of model and set of available tools; Will run in its own context window, can be parallelised

**Who decides to load:** LLM or Human

**When to use:**

* Common larger tasks that are suitable for and worth running in their own context for efficiency (to improve results with more intentional context), or to reduce costs).
* Tasks for which you usually want to use a model other than your default model
* Tasks that need specific tools / MCP servers that you donât want to always have available in your default context
* Orchestratable workflows

**Example use cases:**

* Create an E2E test for everything that was just built
* Code review done by a separate context and with a different model to give you a âsecond opinionâ without the baggage of your original session
* subagents are foundational for swarm experiments like claude-flow or Gas Town

**Other coding assistants:** [Roo Code has had subagents for quite a while](https://martinfowler.com/articles/pushing-ai-autonomy.html#MultipleAgents), they call them âmodesâ; [Cursor just got them](https://cursor.com/docs/context/subagents); [GH Copilot allows agent configuration](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents), but they can only be triggered by humans for now

### [MCP Servers](https://code.claude.com/docs/en/mcp)

**What:** A program that runs on your machine (or on a server) and gives the agent access to data sources and other actions via the Model Context Protocol

**Who decides to load:** LLM

**When to use:** Use when you want to give your agent access to an API, or to a tool running on your machine. Think of it as a script on your machine with lots of options, and those options are exposed to the agent in a structured way. Once the LLM decides to call this, the tool call itself is usually a deterministic thing. There is a trend now to supercede some MCP server functionality with skills that describe how to use scripts and CLIs.

**Example use cases:** JIRA access (MCP server that can execute API calls to Atlassian) Â· Browser navigation (e.g. Playwright MCP) Â· Access to a knowledge base on your machine

**Other coding assistants:** All common coding assistants support MCP servers at this point

### [Hooks](https://code.claude.com/docs/en/hooks-guide)

**What:** Scripts

**Who decides to load:** Claude Code lifecycle events

**When to use:** When you want something to happen deterministically every single time you edit a file, execute a command, call an MCP server, etc.

**Example use cases:**

* Custom notifications
* After every file edit, check if itâs a JS file and if so, then run prettier on it
* Claude Code observability use cases, like logging all executed commands somewhere

**Other coding assistants:** Hooks are a feature that is still quite rare. Cursor has just started supporting them.

### [Plugins](https://code.claude.com/docs/en/plugins)

**What:** A way to distribute all or any of these things

**Example use cases:** Distribute a common set of commands, skills and hooks to teams in an organisation

This is quite a long list! However, weâre in a âstormingâ phase right now and will surely converge on a simpler set of features. I expect e.g. Skills to not only absorb slash commands, but also rules, which would reduce this list by two entries.

## Sharing context configurations

As I said in the beginning, these features are just the foundation for humans to do the actual work and filling these with reasonable context. It takes quite a bit of time to build up a good setup, because you have to use a configuration for a while to be able to say if itâs working well or not - there are no unit tests for context engineering. Therefore, people are keen to share good setups with each other.

Challenges for sharing:

* The context of the sharer and the receiver has to be as similar as possible - it works a lot better inside of a team than between strangers on the internet
* There is a tendency to overengineer the context with unnecessary, copied & pasted instructions up front, in my experience itâs best to build this up iteratively
* Different experience levels might need different rules and instructions
* If you have low awareness of whatâs in your context because you copied a lot from a stranger, you might inadvertently repeat instructions or contradict existing ones, or blame the poor coding agent for being useless when itâs just following *your* instructions

## Beware: Illusion of control

In spite of the name, ultimately this is not *really* engineeringâ¦ Once the agent gets all these instructions and guidance, execution still depends on how well the LLM interprets them! Context engineering can definitely make a coding agent more effective and increase the probability of useful results quite a bit. However, sometimes people talk about these features with phrases like âensure it does Xâ, or âprevent hallucinationsâ. But as long as LLMs are involved, we can never be *certain* of anything, [we still need to think in probabilities](/articles/exploring-gen-ai/to-vibe-or-not-vibe.html) and choose the right level of human oversight for the job.

latest article (Mar 04):

[Humans and Agents in Software Engineering Loops](humans-and-agents.html)

previous article:

[Assessing internal quality while coding with an agent](ccmenu-quality.html)

next article:

[Harness Engineering - first thoughts](harness-engineering-memo.html)

[![](donkey-card.png)](/articles/exploring-gen-ai.html)
