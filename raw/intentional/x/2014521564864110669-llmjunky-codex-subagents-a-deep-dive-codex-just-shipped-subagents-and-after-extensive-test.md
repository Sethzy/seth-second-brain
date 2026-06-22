---
type: raw_capture
source_type: x
url: https://x.com/LLMJunky/status/2014521564864110669
original_url: https://x.com/LLMJunky/status/2014521564864110669
author: "am.will"
handle: LLMJunky
status_id: 2014521564864110669
captured_at: 2026-06-19T19:58:41+08:00
published_at: "Fri Jan 23 02:12:23 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 9
  reposts: 34
  likes: 339
---

# X post by @LLMJunky

## Source

- Original: [https://x.com/LLMJunky/status/2014521564864110669](https://x.com/LLMJunky/status/2014521564864110669)
- Canonical: [https://x.com/LLMJunky/status/2014521564864110669](https://x.com/LLMJunky/status/2014521564864110669)
- Author: am.will (@LLMJunky)

## Verbatim Text

Codex Subagents: A Deep Dive

Codex just shipped subagents, and after extensive testing, I've learned what works, what doesn't, and how to actually get the most out of them.

Buckle up. This is going to be a deep dive.

## The Learning Curve

After posting about this feature earlier this week, I received a load of questions and comments (thank you!), and I figured this would be a good opportunity to address those questions, as well as provide some insights to the power users who are familiar with how they work in other agent harnesses.

Let me get this out of the way right now: subagents are not perfect. In these early stages, it's no surprise that there are quirks. Codex subagents behave differently than what you might expect from Claude Code, and understanding these differences is key to unlocking their potential.

My first lesson: While you don't need to explicitly tell Codex when to use subagents, I've found that if you have tasks in mind that are ideal candidates, it's worth being direct. Tell Codex to use subagents for those tasks.

One key difference between Codex and Claude Code is that Claude tends to make more assumptions, creating a more "hands-free" experience. Codex, by contrast, often requires very explicit instructions to get the outcomes you want. If you're used to Claude's subagents, Codex might feel quirky at first. Sometimes you have to get very specific about expected behavior where Claude wouldn't need such strict guidance.

Don't worry though. You can accomplish all the same things with Codex's agents that you can with Claude. These are just things to keep in mind.

With that out of the way, let's talk about how Codex subagents work under the hood.

## The Two Types of Agents

## The Orchestrator

The Orchestrator (I'll call it "Orc" from here on) is not technically a subagent. It's a mode. Think of it as your main agent who coordinates and prompts subagents to handle an array of tasks. The Orc decides when and how to deploy "Workers," which are the actual subagents.

Orcs are explicitly instructed not to complete tasks themselves. Instead, they organize and employ as many workers as needed to complete a given task. As the documentation puts it, Orcs "coordinate execution, monitor progress, resolve conflicts, and integrate results into a coherent outcome."

Think of Orcs as literal managers. They do the high-level research, understand the scope and vision of the task (or plan), and then hire workers to complete the individual tasks required for success.

It's the Orc's job to ensure each worker has its own set of explicit instructions, constraints, and expected outcomes. When a worker finishes, the Orc is required to verify and check their work.

This is especially crucial with multi-agent workflows to ensure everyone is working towards a common goal. OpenAI has explicit instructions in their documentation for this, and the Orc will often make workers aware of one another: "You are not alone in this environment. Do not impact or overwrite the work of the others."

If the Orc finds a problem after launching a multi-agent task, it can simply assign fixes to workers to clear up any conflicts caused by parallelism.

That's how it is supposed to work anyway. In practice, I have found that it wasn't quite so hands-free. But, I have no doubt these are refinements that will improve as Subagents head towards a GA release.

## Workers

Workers inherit the rights, permissions, and tools of the parent, including skills and the ability to launch other subagents (though they're explicitly directed not to unless the user requests it).

Workers operate in interactive mode. They can come back to the Orc with questions or receive follow-up instructions. This is where they differ from codex exec functions, which operate in non-interactive mode.

## When Subagents Launch Automatically

You shouldn't need to explicitly request subagents. I have been using them for days now, and I have had them intelligently spawn on their own on numerous occasions. They are intended launch on their own in scenarios like:

- Very large tasks with multiple well-defined scopes that can run in parallel

- When the agent wants a second opinion from another agent (yes, really! It can call for a "self-review" from a worker, or even debate with itself)

- Running and fixing tests in the background, or reading large log files

- Long-running or blocking tasks in the background

- Isolation for risky changes (sandboxing)

## The Context Window Strategy

Second Lesson: Even when Codex doesn't automatically call an agent, you should be thinking about how intermediate steps affect your main agent's context window during any long-horizon task.

Subagents are ideal candidates for any task where you only care about the final output, especially if the research or file-reading phase is likely to consume a lot of tokens.

Think tasks like:

- Extensive web searches like reading Github repositories

- Reading log files

- Writing documentation

- Library Discovery

The second primary use case, as previously mentioned, is parallel tasks. Also known as swarms.

## Getting the Most Out of Subagents

As I mentioned, Codex can be steerable to a fault. Sometimes you really need hyper-specific prompting to get the desired result. My recommendation: create a skill for any workflow involving subagents so you can generate highly repeatable outcomes.

Third Lesson: Avoid assuming the subagent is returning useful information. Also avoid assuming the Orc is providing correct context to your subagents. At least for now. While you can see an excerpt of the prompt the Orc gives a worker, as well as an excerpt of a worker's output, they're heavily truncated and not particularly useful.

To get around this, just ask:

- "What was your prompt to the worker(s)?"

- "Please show me the entire output of the worker(s)"

This gives you visibility into how well the Orc and Worker are behaving according to expectations.

If you want to employ swarms effectively, you must be sure your subagents are getting the right context and outputting actually useful work.

The Orc should be very explicit about expectations for both the work required and the output on the other side of the task. Ambiguity of ANY kind invites drift. You really don't want drift when swarming.

It is supposed to do all this on its own, and I'm sure it will improve over time, but for now...

Know what goes in, and know what comes out. Validation is easy. You can just ask.

## A Real Example: Building My Own Plan Mode

Earlier this week, the Codex team introduced new collaboration modes (and yes, that's different from "collab" mode). Among these is a native Plan mode. I've had time to play with it.

I was very happy to find that OpenAI released plan mode, but with all of these new toys to play with, I had a thought: what if I could create my own Plan mode? How could I leverage subagents to get the outcomes I was really looking for?

So I created a skill that generates my own custom plan type. It first does extensive research in my repo, then uses the brand new request_user_input tool to ask clarifying questions before proceeding to write a plan.

I thought: since Codex has this "debate an idea with a subagent" feature, why not have my plan skill send the completed plan to a subagent for review and feedback? It's almost always helpful to have agents review their work. So I instructed it to spin up a worker to check its work.

The result was a lie.

It told me it completed successfully and generated a plan, but it finished far too quickly. I knew something was up.

So I asked: "What was your prompt?"

It hadn't even provided the plan to the worker. Nor did the worker output its expected answer. Ultimately, I had to explicitly instruct the Orc to provide the filepath to the plan and a detailed overview prompt, including what we expected the Worker output to look like.

After that? Voilà. Magic.

Fourth Lesson: Don't assume. Validate.

Note: If you want to review a Worker's prompt & output, you can also use /resume

## Mastering Swarms

To utilize swarms effectively, I use my "plan skill" to write plans with Phases and Tasks where each Phase/Task lists its dependencies. When we run the plan, the Orc can look at the entirety of it and know exactly which tasks are unblocked at any given moment.

If Task 1.2 relies on 1.1, it won't start yet. But once Task 1.1 is complete, Tasks 1.2 through 2.2 can all be done in parallel, it can launch four subagents in tandem without needing further research or worrying about conflicts.

To make this work, I created a parallel-task agent that directs the Orc on how to prompt subagents for the highest degree of success. You don't need this skill for swarms to work, but I've found that the more control you have over context, the better the outcomes.

The parallel skill provides clear instructions and a template for swarms. Here's how it expects the Orc to prompt a Worker:

## Providing a subagent with this type of explicit context has two main benefits:

1. Token efficiency.

The less context you give, the more research the worker needs to do. The Orc already did this research. No need to do it twice.

2. Dramatically reduced drift.

It tells the agent who, what, where, and when, and provides a clear framework with explicit expectations.

Once the first set of tasks complete, the Orc is instructed to re-review the plan, identify newly unblocked tasks, and repeat until tasks remaining = 0.

## The Power of Orchestration

The beauty of the Orc really surfaces here. What makes it so powerful is that your agent now acts as a true conductor: always tracking and managing the state of your project, ensuring workers perform as expected, and pushing the project toward successful completion. All without ever needing to compact. Or rarely.

This enables even longer-horizon tasks without drift.

Final Lesson: You can just ask it to launch subagents for any reason. You don't have to be fancy with the above techniques. In fact, you don't need subagents at all! You can go the rest of your days without ever touching them. These are just productivity unlocks, another tool in your belt. If you learn them, you can build even faster, that's all!

## Get the Skills

These are my current learnings on how to unlock subagents and get the most out of them using Codex.

If you're interested in using my skills for swarms, [they're available on my GitHub:](https://github.com/am-will/codex-skills)

- planner: For generating normal plans

- plan-harder: For using the planning agent that launches a subagent for a second opinion and further refinement

- parallel-task: Uses Orchestration Mode to Implement tasks from a plan

Note: To use these features, you need the following in your config.toml:

[features]
collab = true
collaboration_modes = true

Without these, the "request_user_input" tool won't work.

If you want to use swarms, I recommend you use one of my planner skills in "pair programming mode" (use Shift+Tab) because it creates phased plans with task dependencies that are more explicitly outlined for swarms.

Alternatively, you can just ask the official Plan Mode to list every task's dependencies, and it will oblige. Either way works just fine.

If you made it this far, you're a legend! I hope you learned something today. Feel free to leave questions below. Happy Swarming!

PS. Look at this funny experimental prompt in the Codex repo. LOL.

## X Article Metadata

- Title: Codex Subagents: A Deep Dive
- Preview: Codex just shipped subagents, and after extensive testing, I've learned what works, what doesn't, and how to actually get the most out of them.
Buckle up. This is going to be a deep dive.
The Learning

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
