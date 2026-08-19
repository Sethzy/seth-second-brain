---
type: raw_capture
source_type: web
title: "Build Your Own Claude Code Using Langchin: A Deepdive Into LangChain’s Deep Agents"
url: "https://pub.towardsai.net/build-your-own-claude-code-using-langchin-a-deepdive-into-langchains-deep-agents-9ef98d98a69a"
collected_at: 2026-07-02T18:53:25Z
published_at: 2026-06-10
capture_quality: complete
status: raw
trust_lane: intentional
---

# Build Your Own Claude Code Using Langchin: A Deepdive Into LangChain’s Deep Agents

Source: https://pub.towardsai.net/build-your-own-claude-code-using-langchin-a-deepdive-into-langchains-deep-agents-9ef98d98a69a

## Capture Text

Author: Sreejith Sreejayan
Publication: Towards AI / Medium
Canonical URL: https://pub.towardsai.net/build-your-own-claude-code-using-langchin-a-deepdive-into-langchains-deep-agents-9ef98d98a69a
First published: 2026-06-10
Latest published/modified: 2026-06-12
Medium post id: 9ef98d98a69a
Tags: Langchain, Claude Code
Word count: 3977
Reading time: 15 min

## Build Your Own Claude Code Using Langchin: A Deepdive Into LangChain’s Deep Agents

### If you have used Claude Code, you might have walked away thinking, “Wow, this model is incredibly smart at coding.”

But that is actually the wrong mental model. A coding agent is not just a smarter chatbot. The magic of Claude Code is not the model alone; it is the agentic harness wrapped around it.

The harness is the control plane. It is the invisible system that gives the model tools to read files, an environment to run code, memory to remember what it did, and a checklist to stay on track. Without the harness, a language model is just a text generator. With the harness, it becomes a capable, autonomous software engineer.

In this post, we are going to open up the black box. We will look at exactly how Claude Code works behind the curtain. Then, for every piece we uncover, we will rebuild it using LangChain’s deepagents library. By the end, you will understand how coding agents work because you will know how to build one yourself.

## The Architecture of a Coding Agent

Before we dive into the details, here is a map of the system we are exploring:

The whole engine is that cycle, and it starts with you. Everything kicks off from a user question or request — anything from a quick “what files are in this folder?” to a big “refactor the login system and update the tests” — and that single message is what the model reads first before deciding its next step. From there, one of two things happens. If the model needs to act, it calls a tool, the result gets handed back, and it loops — the same loop whether the task takes one step or fifty. The moment it replies with plain text instead of a tool call, the loop exits and you get your answer. That exit condition (“no tool call”) is literally how the agent knows it’s done.

![Medium image 1*B2UEAAJ9EPMbhKbGbOwDww.png](https://miro.medium.com/v2/resize:fit:1400/1*B2UEAAJ9EPMbhKbGbOwDww.png)

That “decides the next step” box is really the three blended phases from the research: the model is constantly gathering context (reading files), taking action (editing, running commands), and verifying results (running tests), all flowing through the same loop. There are no separate “modes” for those — they’re just different tool calls.

There is, however, one deliberate gear-shift worth calling out: plan mode. Normally the agent plans and acts in the same breath. Plan mode puts a gate in front of the loop — you ask the agent to investigate and propose a plan without changing anything, so it reads files and thinks but holds off on edits and commands until you approve. Then the normal loop takes over and executes. It’s a safety valve for big or risky tasks. This is different from the automatic to-do list (which the agent writes for itself on every task); plan mode is a user-triggered pause that you explicitly approve.

What the diagram still leaves out is the rest of the machinery wrapped around the loop — context compaction when memory fills up, subagents running their own private loops, and the permission/sandbox layer between “Run a tool” and the actual system. Those don’t change the loop; they wrap it.

![Medium image 1*fcBtc4UX2fyeYk4h6MR4Yw.png](https://miro.medium.com/v2/resize:fit:1400/1*fcBtc4UX2fyeYk4h6MR4Yw.png)

The four pieces inside the harness are the capabilities that make the loop reliable instead of flaky. Planning makes the agent think before it acts. Tools give it hands. Context management keeps it from drowning in its own memory on long jobs. Subagents let it spin off side-quests in their own private loops so the main conversation stays clean. None of these change the loop — they feed it.

Now the part that matters most: the bottom layer. When the agent decides to actually do something in the real world — edit a file, run a shell command, hit the network — that action does not go straight to your machine. It has to pass through the permissions and sandbox layer first. This is the single most important safety idea in the whole system.

The trap is thinking you can keep the agent safe by writing “please don’t delete anything important” in its instructions. That’s not a wall — it’s a sticky note the model can ignore, misread, or be talked out of. Real safety lives in this layer, outside the model, where a permission rule can flat-out block a tool call and a sandbox can stop a dangerous command at the operating-system level no matter what the model wants.

Enough theory. Let’s build it.

## Part 0: The loop from scratch — no framework, no magic

Before reaching for any library, look at the whole engine bare. This is a complete, working agent loop:

```
def run_agent_loop(client, user_message, tools, tool_functions, max_turns=20):
    messages = [{"role": "user", "content": user_message}]
    for _ in range(max_turns):
        # 1. Ask the model what to do next.
        response = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=1024, tools=tools, messages=messages
        )
        messages = [*messages, {"role": "assistant", "content": response.content}]

        # 2. Plain text and no tool request? The job is done.
        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            return "".join(b.text for b in response.content if b.type == "text")
        # 3. Run each requested tool and hand the results back. 4. Repeat.
        results = [
            {"type": "tool_result", "tool_use_id": call.id,
             "content": tool_functions[call.name](**call.input)}
            for call in tool_uses
        ]
        messages = [*messages, {"role": "user", "content": results}]
    raise RuntimeError(f"agent loop did not finish within {max_turns} turns")
```

That’s it. Around thirty lines, and every concept in the rest of this post is this loop with batteries: better tools plugged into `tool_functions`, a planner that writes itself notes into `messages`, a compactor that shrinks `messages` when it bloats, subagents that are just this same function called recursively with a fresh `messages` list, and a permission check inserted between the model asking for a tool and the line that calls it. The `max_turns` backstop is the one piece of paranoia no real harness skips — a model that loops forever burns money forever.

## Part 1: The loop — the engine that drives everything

Every coding agent has a beating heart called the agent loop. It is the cycle that turns “talking” into “doing.” It is also almost embarrassingly simple:

1. Ask the model what to do next.
1. The model either replies with normal text, or it asks to use a tool.
1. If it asked for a tool, the system runs that tool and hands the result back to the model.
1. Repeat from step 1.
1. When the model replies with plain text and no tool request, the job is done. Stop and show the user the answer.

That is the entire engine. Read a file, run a command, edit some code — every single action flows through this exact same cycle.

Think of it like a contractor: You hand them a job and a checklist. They look at what is next, do it, check the result, and decide what to do next. They only come back to talk to you when there is nothing left on the list. The agent loop is that contractor’s brain.

One elegant detail worth appreciating is that this loop naturally grows or shrinks to fit the task. A quick question (“What files are in this folder?”) might take a single turn. A massive request (“Refactor the login system”) might chain dozens of tool calls across many turns. Nobody has to hard-code how many steps a task needs.

Building it with Deep Agents

Here is the good news: you do not have to write this while loop yourself. When you create a Deep Agent, you get a fully working loop for free.

First, install the library and a model provider:

```
pip install deepagents langchain-anthropic
```

Then, create the simplest possible agent:

```
from deepagents import create_deep_agent

def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"It's always sunny in {city}!"
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant.",
)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
```

That create_deep_agent call returns a ready-to-run agent with the loop already wired up. When you call .invoke(), it runs the exact cycle we just described. The harness doesn’t care which model you plug in — OpenAI, Google, or Anthropic — the loop remains the same.

## Part 2: The tools — giving the agent hands

If the loop is the engine, tools are the hands. A model with no tools can only talk. A model with good tools can read your codebase, change it, and check its work. Real coding tools sort into four families:

Reading tools — look around without changing anything:

- `read_file` to open a file.
- `glob` to find files by name pattern (e.g. every file ending in `.py`).
- `grep` to search inside files for specific text.
- (A common beginner confusion: glob finds files by name; grep finds files by contents.)

Editing tools — change things safely: `write_file` for new files, `edit_file` to change part of an existing file.

An execute tool — runs shell commands, the same ones you’d type in a terminal.

A delegate tool — `task`, which hands a sub-task off to a helper agent.

### Why not just let the model run any command?

Couldn’t the agent just `cat` to read and `sed` to edit? It could, but dedicated tools are vastly better for two reasons:

- Token budgeting: a purpose-built read tool can measure a file’s size before dumping it into memory and trim it if needed. A raw `cat` floods everything in and can blow the context window.
- Cleaner permissions: when the agent uses a known `edit_file` tool, the harness knows exactly what's happening and can apply safety rules. A free-form shell command is a dangerous black box.

There’s a funny real-world quirk: the model learned from the public internet, full of Stack Overflow answers using `cat` and `sed`. So even advanced models keep reaching for raw shell out of habit. Your system prompt has to firmly remind it to use its real tools, not the shell shortcuts.

### Building it with Deep Agents

Deep Agents ships the whole suite built-in — planning, filesystem tools, execute, and delegation. You add custom tools on top with a decorated function:

```
import subprocess
from langchain_core.tools import tool

MAX_OUTPUT_CHARS = 20_000  # roughly 5k tokens
@tool
def run_tests(path: str = ".") -> str:
    """Run the project's pytest suite and return its output.
    Output is truncated to the last 20k characters (failures appear at the
    end). The run is killed after 5 minutes.
    """
    try:
        result = subprocess.run(["pytest", path], capture_output=True,
                                text=True, check=False, timeout=300)
    except subprocess.TimeoutExpired:
        return "pytest timed out after 300s"
    output = result.stdout + result.stderr
    if len(output) > MAX_OUTPUT_CHARS:
        return ("[... output truncated to the last 20,000 characters ...]\n"
                + output[-MAX_OUTPUT_CHARS:])
    return output
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[run_tests],            # merged in alongside the built-ins
    system_prompt="You are a coding assistant. Always run tests after editing.",
)
```

The `@tool` decorator turns a plain function into something the model can call. That docstring is crucial — the model reads it like an instruction manual to know when and how to use the tool.Part 3: Planning — thinking before doing

## Part 3: Planning — thinking before doing

Drop a complex request on a bare model, and it tends to flail. It makes one tool call, then another, with no overall plan, sometimes going in circles. A good coding agent avoids this by planning first.

Before touching any code, the agent writes a structured to-do list. It breaks the task into clear steps, then works through that list, marking items as “in-progress” and “completed” as it goes.

Think of it like a cook: A good cook reads the entire recipe before turning on the stove. They aren’t figuring out step four while step three is burning.

There is a clever engineering trick hiding behind this. In a long session, models lose track of their original goal because their instructions get buried under pages of tool output. To fix this, the harness quietly re-injects the current to-do list back into the conversation after tool calls. It is like a colleague gently sliding the checklist back in front of you so you don’t forget the point.

Building it with Deep Agents

This feature is called the write_todos tool, and in Deep Agents, it is built in. You don’t configure anything — the default system prompt automatically teaches the agent to plan before acting and keeps the to-do list updated across the loop.

## Part 4: Context management — beating the memory limit

This is where the hardest engineering lives. Every model has a context window — a hard limit on its short-term memory. Read a few large files, run some commands, and you fill it fast. When it overflows, the agent forgets things, including your original instructions.

Coding agents solve this with a two-part strategy:

1. Files as external memory: Instead of cramming a giant search result into the conversation, the agent saves it to a file and just remembers the filename. If it needs the details later, it reads the file.
1. Compaction: When the conversation gets dangerously close to filling the window, the harness automatically pauses the loop. It summarizes the older parts of the conversation, tucks those important facts into long-term storage, and clears the bloated short-term memory.

Think of it like researching a massive report: You don’t try to hold every book in your head. You take notes, file the books away, and keep a one-page summary on your desk.

### Building it with Deep Agents

Both halves are built in. Deep Agents ships a virtual filesystem to offload large results, plus automatic summarization middleware. You get this memory management for free the moment you create the agent.

## Part 5: Subagents — divide and conquer

Some tasks are too big for one conversation. Searching a giant codebase might involve reading fifty files — and you do not want fifty files clogging your main agent’s clean memory.

The solution is subagents. The main agent spins up a helper, hands it one highly specific job (“search the codebase and tell me where the auth logic lives”), and the helper does that work in its own separate, blank context window. When done, it reports back a concise summary.

Think of it like a manager: A manager delegates a research task to a junior employee. The junior reads a stack of documents and comes back with a one-paragraph summary. The manager’s desk stays clean.

The safety rail: Subagents are strictly forbidden from spawning their own subagents. If they could, a confused agent might create an infinite loop of nested helpers, creating a runaway process that burns your API budget. A strict depth limit keeps delegation safe.

Building it with Deep Agents

Deep Agents has a built-in task tool for spawning helpers. You can create specialized helpers — like a dedicated code searcher — by describing them as simple dictionaries:

```
code_searcher = {
    "name": "code-searcher",
    "description": "Searches the codebase to find where specific logic lives. "
                   "Use this for any open-ended 'where is X?' question.",
    # ⚠️ NOTE: the key is `system_prompt`, NOT `prompt` (see correction below).
    "system_prompt": "You are an expert at navigating codebases. Use the grep "
                     "and glob tools to locate relevant files, then report a "
                     "concise summary of what you found and where. Do not make "
                     "any edits.",
}

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[run_tests],
    system_prompt="You are a coding assistant.",
    subagents=[code_searcher],
)
```

The main agent now knows it has a specialist available, keeping its own memory pristine for the actual coding work.

## Part 6: Safety and human-in-the-loop — the brakes

We have now built an agent that can edit files and run shell commands on your machine. Pause and let that sink in. An overeager agent could delete the wrong files or run something highly destructive. Power without brakes is a massive liability.

Coding agents add control in two layers:

1. Allowlists and deny rules: Safe tools (reading files) run automatically. Destructive tools (deleting files) require approval.
1. Approval prompts (Human-in-the-loop): For risky actions, the agent pauses and asks you. You approve, edit, or reject the action, and then the loop continues.

The golden rule of agent security: A prompt is not a security boundary.

Telling the model “Please don’t delete anything important” is a polite suggestion, not a wall. The model can hallucinate and bypass it entirely. Real safety is enforced outside the model, inside the harness. A permission rule can flat-out block a tool call. A sandbox can stop a dangerous shell command at the operating-system level, no matter how badly the model wants to run it. This is why the execute tool requires a proper backend. Asking nicely is not security.

### Building it with Deep Agents

Deep Agents enforces limits in the harness. It requires a backend for shell access, and it uses LangGraph’s native interrupt feature to pause before risky operations.

```
from deepagents import create_deep_agent
# Import path for backends can vary by version - check the current
# "Backends" page in the Deep Agents docs.
from deepagents.backends import LocalShellBackend

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a coding assistant working inside this project.",
    backend=LocalShellBackend(),   # enables the `execute` shell tool
)
```

When a gated tool is requested, the loop interrupts and the result contains an `__interrupt__` payload describing the pending action and the decisions you can make (`approve`, `edit`, `reject`, `respond`). Then you resume:

```
from langgraph.types import Command

result = agent.invoke({"messages": [...]}, config)
result["__interrupt__"]   # the pending action + allowed decisions — show your user

# You decide; the loop picks up exactly where it paused:
agent.invoke(Command(resume={"decisions": [{"type": "approve"}]}), config)
# ... or {"type": "reject"} — the tool is never run, and the model is told so.
```

Always configure your real limits in the harness, never just in the prompt.

## Part 7: Memory and persistence — remembering across sessions

By default, an agent forgets everything the second a conversation ends. But a real assistant should remember your project’s coding conventions, your preferences, and what it was doing yesterday.

Two capabilities handle this:

- Checkpointing: Saves the agent’s exact state so a long task can survive an interruption and pick up right where it left off.
- Long-term memory: Stores facts that persist across completely separate conversations (e.g., “This project uses 4-space indentation”).

### Building it with Deep Agents

Because Deep Agents runs on LangGraph, you get persistence simply by plugging in a checkpointer:

```
from deepagents import create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[run_tests],
    system_prompt="You are a coding assistant.",
    checkpointer=InMemorySaver(),   # remembers state within a session
)
# A "thread_id" ties messages together into one ongoing conversation.
config = {"configurable": {"thread_id": "project-alpha"}}
agent.invoke(
    {"messages": [{"role": "user", "content": "Start refactoring the auth module."}]},
    config=config,
)
# Later, same thread_id - the agent remembers the earlier turn:
agent.invoke(
    {"messages": [{"role": "user", "content": "Now update the tests too."}]},
    config=config,
)
```

InMemorySaver works for the life of your program. For real persistence that survives reboots, you just swap it for a database-backed checkpointer.

## Putting it all together

Let’s assemble everything into one agent that has all seven parts: the loop, custom tools, planning, context management, a subagent, shell access, and persistence.

```
from deepagents import create_deep_agent
from deepagents.backends import LocalShellBackend
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

# --- A custom tool (Part 2) — token-budgeted, see Part 2 for the full body ---
@tool
def run_tests(path: str = ".") -> str:
    """Run the project's pytest suite and return its (truncated) output."""
    import subprocess
    try:
        result = subprocess.run(["pytest", path], capture_output=True,
                                text=True, check=False, timeout=300)
    except subprocess.TimeoutExpired:
        return "pytest timed out after 300s"
    output = result.stdout + result.stderr
    return output if len(output) <= 20_000 else "[... truncated ...]\n" + output[-20_000:]

# --- A specialized subagent (Part 5) — note the `system_prompt` key ---
code_searcher = {
    "name": "code-searcher",
    "description": "Finds where specific logic lives in the codebase. "
                   "Use for open-ended 'where is X?' questions.",
    "system_prompt": "You navigate codebases using grep and glob, then report a "
                     "concise summary of what you found. You never make edits.",
}

# --- A system prompt that teaches good behavior (Parts 2 & 3) ---
SYSTEM_PROMPT = """You are a careful coding assistant.
Workflow:
1. Plan the task as a to-do list before doing anything.
2. Use your built-in read, grep, and glob tools to explore - never the raw shell
   equivalents like cat or grep.
3. Make focused edits.
4. ALWAYS run the tests after editing, and fix anything that breaks.
5. Delegate broad codebase searches to the code-searcher subagent.
"""

# --- Assemble the agent (Parts 1, 4, 6, 7 handled by the harness) ---
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",                  # Part 1: the loop, model-agnostic
    tools=[run_tests],                                     # Part 2: custom hands
    system_prompt=SYSTEM_PROMPT,                           # Parts 2 & 3: behavior + planning
    subagents=[code_searcher],                             # Part 5: delegation
    backend=LocalShellBackend(root_dir=".", virtual_mode=False),  # Part 6: shell access
    interrupt_on={"execute": True,                         # Part 6: the brakes —
                  "write_file": True, "edit_file": True},  #   approval before anything destructive
    checkpointer=InMemorySaver(),                          # Part 7: memory across turns
)
# Part 4 (context management) and built-in planning come on automatically.

config = {"configurable": {"thread_id": "my-project"}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "The login tests are failing. Fix them."}]},
    config=config,
)
print(result["messages"][-1].content)
```

In under a hundred lines of code, you have a coding agent that plans, explores, edits, runs tests, delegates to helpers, respects a sandbox, and remembers its context. That is the exact same anatomy as Claude Code.

## The honest part: what’s easy and what’s hard

It would be misleading to end on “and that’s all there is to it.” Here is the honest engineering reality.

What the harness gives you for free (~80%): The loop, the tool suite, planning, context management, delegation, persistence, and streaming. A few years ago, building this from scratch was a massive project. Today, it is a library call.

What is still on you (the hard 20%):

- The system prompt: This dictates the agent’s reliability. Teaching it exactly when to use which tool and how to recover from mistakes takes serious, iterative tuning.
- The sandbox: Safe shell execution is non-negotiable. Setting up proper OS-level isolation takes deep care.
- The right tools: An agent is only as good as its tools. If your code searcher or test runner is flaky, your agent will be flaky too.

The limitations to keep in mind:

- It costs money: Planning, subagents, and looping mean a lot of API calls. Complex tasks rack up real costs.
- It is bound by the model: The best harness in the world cannot make a weak language model reason well.
- It can fail: Agents misunderstand instructions and make bad edits. The brakes exist precisely because mistakes are a reality.
- It can be overkill: For a quick question, a standard chatbot is faster and cheaper. Only spin up an agent when the task actually requires one.

## Wrapping up

The big takeaway is the one we started with: the magic was never just the model.

A capable coding agent is an ordinary language model wrapped inside a powerful harness. It is a loop that turns talk into action, tools that give it hands, planning that keeps it focused, context management that beats its memory limits, subagents that divide the work, brakes that keep it safe, and memory that makes it durable.

Once you see these parts clearly, the black box opens up. With a library like Deep Agents, you can assemble all of them yourself in a single afternoon. The best way to truly understand how Claude Code ticks is to build a small version of it and watch it run. Here is the [github repo](https://github.com/the-Sreejith/langclaude) to the project
