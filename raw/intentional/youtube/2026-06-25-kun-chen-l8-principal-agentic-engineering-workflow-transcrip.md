---
type: raw_capture
source_type: youtube
title: "Kun Chen L8 Principal Agentic Engineering Workflow Transcript"
url: "https://www.youtube.com/watch?v=iQyg-KypKAA"
collected_at: 2026-06-25T08:20:51Z
published_at: "2026-06-20"
capture_quality: complete
status: raw
trust_lane: intentional
---

# Kun Chen L8 Principal Agentic Engineering Workflow Transcript

Source: https://www.youtube.com/watch?v=iQyg-KypKAA

## Capture Text

Title: L8 Principal's Agentic Engineering Workflow
Channel: Kun Chen
Published: 2026-06-20
Duration: 45:46
Source URL: https://www.youtube.com/watch?v=iQyg-KypKAA

## Description

Tools mentioned: WezTerm, tmux, Neovim, npx skills CLI, OpenSuperWhisper, AXI, lavish, no-mistakes, gnhf, treehouse, firstmate. Chapters include terminal workflow, memory files, skills, voice input, agent ergonomics, planning with interactive artifacts, validating work, and task splitting.

## Transcript

[00:00:00] Hi everyone.
[00:00:01] Welcome to this video
[00:00:02] and this will be a full
[00:00:03] walkthrough of my agent
[00:00:05] engineering workflow.
[00:00:06] My name is Kun.
[00:00:07] I was previously an late
[00:00:09] principal engineer,
[00:00:10] worked at meta, Microsoft, and assassin
[00:00:13] on many large scale systems
[00:00:14] like the Bing search engine,
[00:00:16] windows, and Facebook games.
[00:00:18] In the recent couple of years,
[00:00:19] I have been building frontier
[00:00:21] coding agents at Atlassian
[00:00:22] and helped many engineering teams
[00:00:24] figure out how to use them effectively.
[00:00:27] and I have been building heavily
[00:00:28] with agents myself
[00:00:29] and shipping 40 to 50
[00:00:32] almost every day, sometimes more.
[00:00:34] And these are all well tested
[00:00:36] and shipped production.
[00:00:37] not those Minecraft demos.
[00:00:38] You see people wipe code on social media.
[00:00:40] I have shaped my workflow
[00:00:42] to be both highly
[00:00:43] productive and enjoyable.
[00:00:45] Many people recently asked me
[00:00:47] what it looks like,
[00:00:48] be honest,
[00:00:48] I did debate a lot with myself
[00:00:51] whether I should make this video
[00:00:52] a paid course
[00:00:53] because it does
[00:00:54] have that level of value,
[00:00:56] but ultimately
[00:00:57] I decided to just share it here
[00:00:58] with everyone
[00:00:59] because I want to stay focused
[00:01:00] on building products as my main business.
[00:01:03] you can see
[00:01:03] this is a bit of a long video,
[00:01:05] because I'm going to walk through
[00:01:06] many fundamental
[00:01:07] concepts of agent engineering
[00:01:09] that's not only show you how I do it,
[00:01:11] but also the why
[00:01:13] and how things really work
[00:01:14] under the hood.
[00:01:15] These are not gimmicks that look cool
[00:01:17] but can't actually be used for real work.
[00:01:19] These are all real workflows
[00:01:21] that professionals like myself
[00:01:23] use to get real work done.
[00:01:25] By the end of this video,
[00:01:26] I want you to feel like
[00:01:27] a captain
[00:01:28] that can sail a large ship
[00:01:30] with a crew of agents
[00:01:31] working for you,
[00:01:32] and do so
[00:01:33] in a stress free and satisfying way.
[00:01:36] Largely speaking,
[00:01:37] we will be walking
[00:01:37] through these chapters.
[00:01:39] We'll start with assembling our ship,
[00:01:42] where I will introduce the core setup.
[00:01:45] We will then talk through
[00:01:46] how we recruit and ramp up
[00:01:48] our crewmates
[00:01:49] with the right usage of memory
[00:01:51] and skills.
[00:01:52] I will then demonstrate
[00:01:54] how we work
[00:01:54] with a single crewmate effectively.
[00:01:57] Then we'll upgrade
[00:01:58] to working with multiple crewmates
[00:02:00] all at the same time.
[00:02:01] And lastly, we will recruit a first mate
[00:02:04] that manages
[00:02:05] a lot of the overhead for us
[00:02:07] so we can stay focused
[00:02:08] on the big picture.
[00:02:09] As a captain,
[00:02:10] the very first level
[00:02:12] is to gather our gears
[00:02:13] and build our ship.
[00:02:14] Now, as we get into my workflow,
[00:02:17] something that's going to be really hard
[00:02:19] to miss
[00:02:19] is that I do
[00:02:20] almost everything in my terminal.
[00:02:22] I know there are a lot of people
[00:02:24] who will tell you
[00:02:25] that the graphical user interface
[00:02:26] is better.
[00:02:27] It allows richer
[00:02:28] interactions and better visuals,
[00:02:30] but I think by the end of this video,
[00:02:32] I might just be able to convince you
[00:02:34] that terminal is not quite that yet.
[00:02:37] I use the terminal mostly
[00:02:39] for two very real reasons.
[00:02:41] One is to allow my hands to almost
[00:02:43] never have to leave the keyboard.
[00:02:45] This is actually a much bigger deal
[00:02:47] than most people think,
[00:02:48] because when your hands
[00:02:50] stay on the keyboard,
[00:02:51] you stay in the flow.
[00:02:52] But if you have to move your hand
[00:02:55] to the mouse every couple of seconds,
[00:02:57] it breaks the flow and forces
[00:02:58] your brain to contact switch.
[00:03:01] I know there are some guy apps
[00:03:02] that also have great key points
[00:03:04] that allow you to do most things
[00:03:05] with the keyboard as well,
[00:03:07] but that's just not
[00:03:08] the primary interaction
[00:03:09] paradigm for guy apps,
[00:03:11] And it's hard to build the discipline
[00:03:13] of hands on keyboard
[00:03:15] when every once in a while
[00:03:16] you still have to use the mouse
[00:03:18] terminal apps.
[00:03:19] On the other hand,
[00:03:20] are all designed for the keyboard,
[00:03:22] so there is no reason for your hands
[00:03:24] to move anywhere else.
[00:03:25] The other
[00:03:26] very important factor
[00:03:27] that drives me to use
[00:03:28] the terminal is that
[00:03:29] I can keep the exact same workflow
[00:03:32] everywhere, even on my phone.
[00:03:33] but if you really don't
[00:03:35] like the terminal, that's okay too.
[00:03:37] I designed this video to be more
[00:03:38] about the fundamental
[00:03:40] concepts behind
[00:03:41] agent engineering
[00:03:42] rather than the mechanics.
[00:03:43] So most of the things that I talk about
[00:03:46] should be applicable
[00:03:47] to GUI based workflows as well. Now.
[00:03:50] Since we are looking at a terminal here,
[00:03:52] let me share what it is
[00:03:53] I'm using this
[00:03:55] beautiful, clean and elegant
[00:03:56] terminal emulator
[00:03:57] you are looking at
[00:03:58] here is called Western.
[00:04:01] Western is a highly performance
[00:04:03] terminal emulator built by a guy
[00:04:05] named West.
[00:04:06] It's got 26
[00:04:07] k GitHub stars and has existed
[00:04:09] for many years.
[00:04:10] I like it mostly for two reasons.
[00:04:13] One is that it's truly cross-platform.
[00:04:15] It's pretty much
[00:04:16] the only terminal emulator I can find
[00:04:18] that can work on windows
[00:04:20] exactly the same way
[00:04:21] it works on Mac and Linux.
[00:04:23] Right now
[00:04:23] I mostly only work on Mac,
[00:04:25] but it was a big lifesaver
[00:04:27] when I was working for Microsoft
[00:04:28] and was forced to use windows for work.
[00:04:32] The other reason is that it's
[00:04:33] highly customizable.
[00:04:34] You can write Lua scripts to configure
[00:04:36] pretty much everything. Here.
[00:04:38] Let me show you my config in my dot
[00:04:40] files.
[00:04:41] It's all in this file
[00:04:42] called Western dot lua.
[00:04:44] It's a lower script.
[00:04:45] So it's not just static values.
[00:04:47] You can actually set conditions
[00:04:48] and write various
[00:04:49] kind of
[00:04:50] logic to make your config
[00:04:51] very dynamic and flexible.
[00:04:54] If I change some settings
[00:04:55] here, let's say
[00:04:56] I change the color scheme to chalk.
[00:05:00] You will see that
[00:05:00] it does a hot reload instantly,
[00:05:02] which is super handy.
[00:05:04] But I still like my rose pine moon,
[00:05:06] so let's come back to it.
[00:05:07] I can't use anything else.
[00:05:09] Inside of West
[00:05:10] term, I run something called tmux.
[00:05:13] It's short for terminal multiplexer.
[00:05:16] If you haven't come across this yet,
[00:05:17] it's probably easiest
[00:05:18] to just show you what this does.
[00:05:20] so I'm
[00:05:20] typing this command here
[00:05:21] to start a session.
[00:05:24] Now I'm inside of t max.
[00:05:26] You can see
[00:05:26] not much is different except for that.
[00:05:29] There is a bar at the top
[00:05:30] showing some information,
[00:05:32] and I still get a shell
[00:05:34] where I can type commands,
[00:05:35] But now I can split my terminal
[00:05:37] into multiple panes,
[00:05:39] as many of them as I like.
[00:05:41] This is super useful
[00:05:42] because I can spin up an agent
[00:05:44] in one pain and spin up
[00:05:46] an editor in another,
[00:05:47] and still have a pain to myself
[00:05:50] so I can just run commands.
[00:05:52] I can also spin up
[00:05:53] multiple tabs
[00:05:54] and they are also called windows in.
[00:05:57] This is very useful
[00:05:58] for running multiple
[00:05:59] agent sessions in parallel.
[00:06:01] The other cool thing is
[00:06:02] that tmux
[00:06:03] sessions are persistent in the server.
[00:06:06] So if I use a keyboard shortcut here
[00:06:08] to detach from tmux, you can see
[00:06:11] I'm back in the normal shell
[00:06:12] without the status bar at the top.
[00:06:14] But if I type the same command to launch
[00:06:17] tmux again,
[00:06:19] I get back to the exact same state
[00:06:21] I was in So I can continue my work here.
[00:06:24] What's even more useful
[00:06:25] is that I can connect
[00:06:26] to this same session
[00:06:27] from another device,
[00:06:28] like my laptop or my phone.
[00:06:30] that's a real game changer.
[00:06:32] That's very hard to replicate
[00:06:34] without this terminal centric workflow.
[00:06:36] If you just install tmux by default,
[00:06:39] it doesn't have the same experience
[00:06:40] while showing here,
[00:06:42] like the tab bar and the metadata.
[00:06:44] You will probably need to
[00:06:45] do a bit of configuration
[00:06:46] and customize it.
[00:06:48] Let me show you my team config.
[00:06:52] Here it is.
[00:06:53] Most of these settings are key points
[00:06:55] that I have been using
[00:06:56] for many years,
[00:06:57] and built into my muscle memory.
[00:07:00] Some of these are for styling and various
[00:07:02] kind of behaviors.
[00:07:03] There are many
[00:07:04] YouTube videos
[00:07:05] that go into more details
[00:07:06] about tmux configuration.
[00:07:08] So I'm not going to go down the rabbit
[00:07:09] hole here. For now.
[00:07:11] You just need to know
[00:07:12] that you are likely
[00:07:13] want to spend some time
[00:07:15] configuring your t mux for it.
[00:07:17] Look good and work
[00:07:18] well for This text editor here is Nuvem.
[00:07:21] It's basically the modern version of vim.
[00:07:23] It's my favorite text editor.
[00:07:25] If you are not familiar with vim yet,
[00:07:27] it's an editor
[00:07:28] whose main purpose
[00:07:29] is to keep your hands on the keyboard.
[00:07:31] So if you watch my keystrokes here,
[00:07:34] I can move the cursor
[00:07:35] up and down, left and right with keys.
[00:07:38] I can also scroll up or scroll down.
[00:07:42] If I have to make edits,
[00:07:43] I can go into insert
[00:07:44] mode and start to type anything I like.
[00:07:48] There are a ton of keyboard shortcuts
[00:07:50] for doing everything you need.
[00:07:51] For example,
[00:07:52] let's say
[00:07:52] I want to delete the current line.
[00:07:54] I can just type dd and it's gone.
[00:07:56] I can undo it by typing you.
[00:07:59] And if you look at the left hand side
[00:08:01] I have relative line numbers.
[00:08:03] This line number 238
[00:08:06] is the current line number.
[00:08:07] And the line above
[00:08:09] shows one,
[00:08:09] which means it's one line
[00:08:11] above the current line
[00:08:12] and the lines below as well.
[00:08:14] So let's say
[00:08:15] I want to jump to the line
[00:08:16] that says set environment.
[00:08:19] That's 11 lines above the current line.
[00:08:21] So I can just type 11 k.
[00:08:23] And I'm here.
[00:08:24] So once you have enough muscle memory,
[00:08:27] you can just navigate around
[00:08:28] much more quickly than using a mouse.
[00:08:31] I also have a bunch of plugins
[00:08:32] that help me get around in as well.
[00:08:35] And I have key points for all of them.
[00:08:38] Like space S
[00:08:39] allows me to search
[00:08:40] or grep for the code base,
[00:08:41] so I can just type rows
[00:08:43] and it will find all the occurrences
[00:08:45] of rows in the current code base.
[00:08:48] I can type space F
[00:08:50] to find files by their names,
[00:08:51] like if I type flake
[00:08:53] I'll get to the flake file immediately.
[00:08:56] Working with them
[00:08:57] has a learning curve for sure.
[00:08:59] But once you get used to it,
[00:09:00] it just feels really, really good.
[00:09:03] Whenever I'm
[00:09:03] in, I'm just flying like a bird
[00:09:06] and it's awesome okay?
[00:09:07] I have to stop here before
[00:09:08] this turns into a vim tutorial.
[00:09:10] You can find a lot of great
[00:09:12] YouTube videos
[00:09:12] that will help
[00:09:13] you get started on them
[00:09:14] and become a master.
[00:09:16] Maybe one last tip for me
[00:09:18] is just how to exit.
[00:09:20] Here you go.
[00:09:21] All right.
[00:09:22] Our ship is ready to sail,
[00:09:23] but we have no crewmates yet.
[00:09:25] Where? The captain.
[00:09:27] We can't do everything by ourselves.
[00:09:28] We need to bring in agents
[00:09:30] as our crewmates.
[00:09:31] I use four different
[00:09:32] agent harnesses regularly.
[00:09:34] There is cloud,
[00:09:35] which is cloud code,
[00:09:37] which is basically
[00:09:37] the only practical choice
[00:09:39] if you are using the subscription
[00:09:40] from anthropic.
[00:09:42] Generally speaking, though,
[00:09:43] it's a pretty good harness.
[00:09:45] I think
[00:09:45] it has the most sensible
[00:09:47] default experience out of the box.
[00:09:49] It's also got a pretty rich feature set.
[00:09:51] The downside
[00:09:52] is that sometimes it's a little
[00:09:54] bit buggy,
[00:09:54] and it's not as customizable
[00:09:57] as some of the other options.
[00:09:58] The next one I use a lot is Codex COI.
[00:10:02] It's written in rust,
[00:10:03] and you can feel
[00:10:04] it's a little bit smoother
[00:10:05] than cloud code when you use it.
[00:10:07] It's also open source,
[00:10:09] so if you run into some problems,
[00:10:10] You can often
[00:10:11] just have Codex
[00:10:12] inspect its own source code
[00:10:14] and figure out a workaround by itself.
[00:10:17] It's a bit
[00:10:17] lacking in terms of bells and whistles,
[00:10:19] and it's also not very customizable.
[00:10:22] And then there is the Pi coding agent.
[00:10:25] And this whole philosophy
[00:10:27] is to be minimal and highly extensible.
[00:10:29] It's great
[00:10:30] if you don't want any bloat
[00:10:31] and you'd like to tinker around
[00:10:33] and kind of make it your own.
[00:10:35] and lastly, there is open code.
[00:10:38] I like it a lot.
[00:10:40] It's got a battery smooth t UI,
[00:10:42] And it's got
[00:10:43] good integration
[00:10:44] with pretty much
[00:10:45] every model you can find.
[00:10:46] It's also got a more complete
[00:10:48] out of the box feature set than Pi.
[00:10:50] So if you want to use an agent harness
[00:10:52] that is model agnostic
[00:10:54] and one that you can just grab
[00:10:56] from the shelf and just go.
[00:10:57] Open code is a pretty good choice.
[00:10:59] For the rest of this video though.
[00:11:01] I'm going to use cloud code
[00:11:02] because I know
[00:11:03] many people are already familiar with it,
[00:11:05] but I have been very strict
[00:11:07] about making my workflow
[00:11:08] agent agnostic
[00:11:09] because the landscape is changing very,
[00:11:11] very fast.
[00:11:12] who knows which model or agents
[00:11:14] will be the best
[00:11:15] performing one next month?
[00:11:16] Right.
[00:11:16] So everything I show here in
[00:11:18] the video is agent agnostic
[00:11:20] and should be applicable
[00:11:21] regardless of which model or harness
[00:11:23] you use.
[00:11:25] The problem with this crewmates
[00:11:27] is that they are fresh recruits,
[00:11:28] and they have no idea how we run our ship
[00:11:30] or how we like to work.
[00:11:32] We need a proper onboarding process
[00:11:34] to ramp them up.
[00:11:35] We will do this mostly through
[00:11:37] two ways memory files and skills.
[00:11:40] There are few types of memory
[00:11:41] files, global memory
[00:11:43] files, and project level memory files.
[00:11:45] The global memory
[00:11:46] file for cloud code is at this location,
[00:11:51] and every other
[00:11:52] agent
[00:11:53] uses the other standard location here.
[00:11:56] So what I do is that I use this command
[00:11:59] Which made MD a symbolic link to MD.
[00:12:04] So they both exist,
[00:12:05] but under the hood
[00:12:06] they point to the same file.
[00:12:08] Here's
[00:12:08] the content of my actual global memory
[00:12:11] file. You can see it's pretty minimal.
[00:12:14] There is only 27 lines.
[00:12:16] Because everything in this file
[00:12:17] gets loaded into the system
[00:12:19] prompt of every single agent session
[00:12:21] across all our projects.
[00:12:23] If we have too much content in this file,
[00:12:26] it will silently use a lot of our tokens.
[00:12:29] I mostly write down
[00:12:30] my personal preferences here,
[00:12:31] like never use em.
[00:12:34] Somehow AI models are trained
[00:12:36] to use
[00:12:36] em by default instead of a plain dash.
[00:12:39] So now whenever I see em,
[00:12:41] I just feel like it's robotic.
[00:12:43] And I don't like that
[00:12:44] when I need the agent
[00:12:45] to write something for me.
[00:12:46] Like PR descriptions.
[00:12:48] Oh, and this is a good one.
[00:12:49] When making technical decisions,
[00:12:51] don't give too much weight
[00:12:52] to development cost.
[00:12:54] Here is something interesting
[00:12:55] that you may not know. Let me show you.
[00:12:58] If we ask a frontier model
[00:13:00] to estimate the development
[00:13:01] cost of a project,
[00:13:03] let's say
[00:13:04] I want to build a 3D
[00:13:06] first person shooting game
[00:13:08] that I can play locally with AI enemies.
[00:13:12] How long do you think that will take?
[00:13:16] Let's see what cloud will say.
[00:13:18] Okay, here it is.
[00:13:19] See, the estimate is in days
[00:13:21] and weeks and months.
[00:13:23] But if we ask the agents to
[00:13:25] actually build it now,
[00:13:26] I can guarantee
[00:13:27] it will come back with a playable version
[00:13:29] in just a few minutes.
[00:13:31] Because I have done this so many times.
[00:13:33] This mismatch is happening
[00:13:35] because the models
[00:13:36] were trained from human data,
[00:13:38] and that is what
[00:13:39] a typical human developer
[00:13:40] would give as the estimate.
[00:13:43] AI doesn't seem to know it
[00:13:44] can code much faster than humans yet.
[00:13:47] When AI is making technical decisions,
[00:13:50] it's implicitly
[00:13:51] assuming the development cost
[00:13:52] for some of the options are much higher
[00:13:55] than they actually are.
[00:13:56] This biases the model to choose
[00:13:59] cheap solutions
[00:14:00] that are often low quality,
[00:14:02] not scalable, or hard to maintain.
[00:14:04] So I have this rule here to
[00:14:06] correct that bias.
[00:14:09] I also said when
[00:14:10] doing bug fixes
[00:14:12] always starts
[00:14:13] with reproducing the bug
[00:14:14] in an end to end setting
[00:14:16] as closely aligned
[00:14:17] with how an end user
[00:14:19] would experience it as possible.
[00:14:21] AI models today by default
[00:14:23] like to write unit tests,
[00:14:25] which are often not sufficient
[00:14:26] and not really covering
[00:14:28] the product behaviors we want to guard.
[00:14:30] I found that leaning into end to end
[00:14:32] testing is a lot more reliable.
[00:14:34] Besides these preferences,
[00:14:35] I also have
[00:14:36] some interesting stuff opinions,
[00:14:39] which is super useful.
[00:14:41] That's a slightly different
[00:14:42] topic though,
[00:14:42] so I won't go into too much detail here,
[00:14:44] but I do have a blog post
[00:14:46] explaining how that works,
[00:14:47] which I'll link here
[00:14:48] in case you're interested.
[00:14:49] Besides the global memory
[00:14:51] file, each project
[00:14:52] can also have a project level memory
[00:14:54] file.
[00:14:54] Let me show you
[00:14:55] one example here by going into
[00:14:57] this project called High Bit.
[00:14:59] This is an AI Twitter app
[00:15:00] I have been working on.
[00:15:01] The project level memory file
[00:15:03] is typically stored as cloud or agents,
[00:15:07] depending on which agent you use.
[00:15:09] I do the same thing here
[00:15:10] with a symbolic link.
[00:15:11] So the same file is shared
[00:15:13] for both cloud and other agents.
[00:15:15] This one we are looking at
[00:15:16] here is a little bit verbose.
[00:15:18] I would say
[00:15:19] I will probably clean this up after this,
[00:15:21] but let me show you on a high level
[00:15:23] what I put into this file.
[00:15:24] It has some context on what
[00:15:26] this project is,
[00:15:27] how the repo is laid out,
[00:15:30] some terminology,
[00:15:32] how some of the most important
[00:15:34] components work,
[00:15:35] and how to do end to end testing,
[00:15:37] and some conventions at the bottom.
[00:15:40] This file is a lot more verbose
[00:15:42] than the global memory file,
[00:15:44] because this is basically the collective
[00:15:46] learning of all the agent sessions
[00:15:48] in this project.
[00:15:49] The way I built
[00:15:49] this file is not by writing
[00:15:51] everything by hand,
[00:15:52] but rather that every time
[00:15:54] I saw the agent doing something wrong,
[00:15:56] I would correct it
[00:15:57] and ask it to remember
[00:15:58] to not make the same mistake again
[00:16:00] by storing the learning
[00:16:01] into this memory file.
[00:16:03] So over time,
[00:16:04] our crewmates working on this project
[00:16:06] get smarter and more experienced.
[00:16:08] You don't need any fancy memory system
[00:16:10] to do that.
[00:16:10] This markdown file is all
[00:16:12] it takes over time.
[00:16:13] It does tend to get more
[00:16:15] and more bloated though.
[00:16:16] One way
[00:16:17] I reduce the size of this file
[00:16:19] is by moving
[00:16:20] some conditional information
[00:16:21] that is not always needed into a skill.
[00:16:24] For example,
[00:16:25] the end to end
[00:16:26] testing instruction here is only needed
[00:16:29] if the agent is making changes, right?
[00:16:31] So if I just ask the agent a question,
[00:16:34] this whole section is totally useless
[00:16:36] and would be wasting tokens.
[00:16:38] The way to improve efficiency
[00:16:40] here is by converting
[00:16:42] this kind of
[00:16:43] conditionally useful information
[00:16:44] from the memory file into skills.
[00:16:47] I typically just
[00:16:48] ask the agent to do this.
[00:16:49] Here, let me do it alive.
[00:16:52] I will say let's extract the end to end
[00:16:56] testing instructions
[00:16:58] junctions in our agents
[00:17:01] and file into a project level skill.
[00:17:07] Cloud already knew how
[00:17:09] to do this,
[00:17:10] what skills mean and how to create them,
[00:17:12] but other agent
[00:17:13] harnesses may not understand
[00:17:15] how to do that out of the box.
[00:17:17] To teach your agent how to create skills,
[00:17:20] you can install a skill called
[00:17:22] Skill Creator which
[00:17:24] which was written by anthropic.
[00:17:26] You can do that by running this command.
[00:17:28] This NPC's skills thing
[00:17:31] is a call from Vercel that is very handy.
[00:17:34] It's basically my main tool
[00:17:36] for installing and managing skills.
[00:17:38] It supports pretty much any agent.
[00:17:41] Once this skill is installed,
[00:17:42] your agent will be able
[00:17:43] to follow the rules and create
[00:17:45] new skills for you moving forward.
[00:17:48] cloud has done its work.
[00:17:49] Let's look at what cloud created for us.
[00:17:53] It basically removed
[00:17:56] a large chunk of the content
[00:17:58] from our agents MD file and move
[00:18:02] that into this this skill file.
[00:18:05] This is a good thing about skills
[00:18:07] is that it's designed
[00:18:08] for progressive disclosure,
[00:18:10] which means when your agent starts,
[00:18:12] it only loads this tiny description
[00:18:14] field from your skills into the system
[00:18:16] prompt to know what these skills do,
[00:18:18] and only when it actually decides
[00:18:21] that it needs to use a certain skill.
[00:18:23] It will then reads the rest of this file.
[00:18:25] This allows you to store
[00:18:27] a lot of the knowledge
[00:18:28] about how to do various
[00:18:29] kinds of things
[00:18:30] without blowing up your system.
[00:18:32] Prompt and memory file
[00:18:33] with a ton of contents
[00:18:34] that uses your tokens
[00:18:35] for every single request,
[00:18:37] whether the request actually
[00:18:38] needs those skills or not.
[00:18:40] One thing
[00:18:40] I do want you to know about skills
[00:18:42] is that you should generally avoid
[00:18:45] installing random skills
[00:18:46] from the internet.
[00:18:47] Even the ones that have a lot of
[00:18:49] GitHub stars.
[00:18:50] First of all,
[00:18:51] these skills
[00:18:52] can instruct your agents to run
[00:18:53] pretty much anything on your machine.
[00:18:56] This is a very risky thing to do,
[00:18:57] because the agent can lick your API keys
[00:19:00] or even credentials to your bank
[00:19:02] account to untrusted
[00:19:03] third parties without you knowing.
[00:19:06] even if we put aside
[00:19:07] the security problem,
[00:19:08] some of the skills
[00:19:09] actually degrade your agents performance.
[00:19:12] Look at this repo
[00:19:13] here called Android Skills, which has
[00:19:16] 177,000 GitHub stars.
[00:19:20] That's like massive.
[00:19:21] So it must be really good, right?
[00:19:23] I actually evaluated a skill in this repo
[00:19:26] with Program Bench,
[00:19:28] which tests
[00:19:29] the agent's ability to build
[00:19:30] programs end to end.
[00:19:32] And the result shows
[00:19:34] that by using this skill,
[00:19:36] the agent will use
[00:19:37] 5% more tokens
[00:19:38] while making the results worse.
[00:19:40] And if you look closely, this skill is
[00:19:44] not even written by André
[00:19:45] Karpathy himself.
[00:19:47] I'm not here to criticize
[00:19:48] the author of this repo, though.
[00:19:50] I'm mainly saying
[00:19:51] that being popular
[00:19:52] is not the same as actually being good.
[00:19:55] A lot of the skills
[00:19:56] being widely shared today
[00:19:58] have not been rigorously evaluated,
[00:20:00] and are typically just some random guy
[00:20:03] who found something
[00:20:04] that worked for themselves and
[00:20:06] and somehow got it to go viral.
[00:20:08] Their GitHub stars
[00:20:10] only tell you how popular they are
[00:20:11] and not
[00:20:12] whether they are actually helpful.
[00:20:14] So as a general rule of thumb,
[00:20:16] I recommend that you do not install
[00:20:18] any skill
[00:20:19] from the internet
[00:20:20] that claims to magically
[00:20:22] make your agent perform better,
[00:20:23] but hasn't published anything
[00:20:25] rigorous that proves its claim.
[00:20:27] All right.
[00:20:28] Now that we have memory files
[00:20:30] and skills to help ramp up
[00:20:31] crewmates, it's
[00:20:32] finally time
[00:20:33] to actually start working
[00:20:34] with the crewmates and set sail.
[00:20:36] The first thing about working with
[00:20:38] the crewmate is how you talk to them.
[00:20:40] I have pretty much completely moved
[00:20:42] to voice input now, So.
[00:20:44] Instead of typing,
[00:20:45] I will just say, explain this
[00:20:47] repo in a concise way
[00:20:48] and give me a recap of what
[00:20:50] the recent press have been working on.
[00:20:53] This is just so easy.
[00:20:54] There is an actual paper from Stanford
[00:20:57] that seriously compared the efficiency.
[00:20:59] And basically
[00:21:01] talking is three times
[00:21:02] faster than typing.
[00:21:04] So this is a very big boost
[00:21:05] in productivity.
[00:21:07] I also want to show you something
[00:21:08] interesting here.
[00:21:09] If we go to the references of this paper
[00:21:13] look who's here.
[00:21:15] It's our guy Dario.
[00:21:17] What is the CEO of anthropic doing here?
[00:21:20] Apparently if we follow this link
[00:21:23] Dario was doing some speech recognition
[00:21:26] stuff back in 2016.
[00:21:28] Now we're using speech recognition
[00:21:29] technology to talk to cloud
[00:21:31] which is also created by Dario.
[00:21:33] What a small world.
[00:21:35] The voice input.
[00:21:36] We just did
[00:21:37] was actually transcribed
[00:21:38] locally using this app called Open
[00:21:41] Super Whisper.
[00:21:43] It's completely free and open source,
[00:21:45] which is what I think
[00:21:46] this type of software should be.
[00:21:47] It runs the whisper model
[00:21:49] locally on your machine
[00:21:50] and do the transcription.
[00:21:51] And the quality is like
[00:21:53] really, really good.
[00:21:54] So this is how I do most of my prompts.
[00:21:56] Now, the only case
[00:21:58] where I fall back to typing
[00:22:00] is when I need to give the agent a URL
[00:22:03] or a file path, or something like that.
[00:22:05] Trust me,
[00:22:06] you don't want to speak a URL out loud,
[00:22:09] whether it's by yourself or
[00:22:10] with other humans around.
[00:22:13] If we
[00:22:13] come back to this prompt
[00:22:15] and let the agent run,
[00:22:16] you will see that
[00:22:17] because we asked the agent
[00:22:19] to look at recent polls,
[00:22:20] it will need to call GitHub
[00:22:22] to fetch the data.
[00:22:24] This is an important thing
[00:22:25] to pay attention to,
[00:22:26] because agents
[00:22:27] rely on external tools
[00:22:29] like GitHub to do its tasks.
[00:22:31] The design of these external tools
[00:22:33] can greatly affect
[00:22:34] your agents performance.
[00:22:35] Take GitHub as an example.
[00:22:37] Many people use the GitHub MCP
[00:22:39] server for accessing GitHub.
[00:22:41] However, I ran this benchmark here
[00:22:44] that measured various
[00:22:45] kinds of ways
[00:22:46] to access GitHub For the exact same tasks
[00:22:50] using GitHub, MCP
[00:22:51] server will cost you to spend three times
[00:22:54] more on token cost,
[00:22:56] and more than double
[00:22:57] the latency compared to using the CLI.
[00:23:00] If you are using the GitHub MCP,
[00:23:01] you are pretty much wasting
[00:23:03] both time and money
[00:23:04] for no clear benefits.
[00:23:06] Now you can see there's
[00:23:07] this thing called axi,
[00:23:09] which has the lowest cost
[00:23:10] but highest success rate.
[00:23:12] So what is it? Let me show you.
[00:23:16] Axi is a set of
[00:23:18] design standards
[00:23:19] I authored
[00:23:19] after discovering the huge upside
[00:23:21] we can have by designing our tools
[00:23:24] to treat agents as a first class citizen
[00:23:27] and optimize for agent ergonomics.
[00:23:30] I created ten principles
[00:23:32] for how to make a tool
[00:23:33] highly efficient for agents.
[00:23:35] For example,
[00:23:37] using token efficient output
[00:23:38] format can save about 40%
[00:23:40] tokens compared to using JSON.
[00:23:42] And then I built a few axes with
[00:23:45] Besides the GitHub axis I showed earlier,
[00:23:47] I also built Chrome dev tools actually,
[00:23:49] and benchmarked
[00:23:51] it against other various browser tools.
[00:23:54] And Here you can see
[00:23:56] the agents taking less turns
[00:23:58] and using less tokens
[00:23:59] to get the same tasks done with the ax.
[00:24:02] The main point here
[00:24:03] is when you give tools to your agents,
[00:24:05] do some research on their efficiency
[00:24:07] because they can greatly affect
[00:24:09] how much mileage
[00:24:10] you get out of your agents.
[00:24:12] If you want to use the axes
[00:24:14] I mentioned earlier,
[00:24:15] you can just go to this site called axis
[00:24:18] and find them in this catalog.
[00:24:20] You can just go to the repo
[00:24:22] and find instructions
[00:24:23] for how to start using them.
[00:24:25] Speaking of this catalog,
[00:24:27] there is something called
[00:24:28] lavish axi here.
[00:24:30] This is a very important tool
[00:24:32] in my setup.
[00:24:33] I pretty much rely on this tool
[00:24:35] for planning any kind of complex work.
[00:24:37] Let's do a real feature live
[00:24:39] and I'll show you how it works.
[00:24:40] Let me first launch high bit
[00:24:42] to show you
[00:24:43] what I'm trying to work on here.
[00:24:45] Hybrid is an AI Twitter
[00:24:46] I'm building for kids.
[00:24:48] I'll just create a test profile here.
[00:24:53] You can see here
[00:24:54] at the top I
[00:24:55] have these two buttons,
[00:24:56] what I can do and my progress.
[00:24:59] They are showing very similar content
[00:25:01] right now which is a problem.
[00:25:03] So and also the UI is not very exciting
[00:25:07] or fun.
[00:25:08] So let me go back and talk to cloud.
[00:25:14] I'll still use voice input here.
[00:25:16] I'll just say
[00:25:18] I'd like to consolidate
[00:25:19] the what I can do
[00:25:21] and my progress buttons,
[00:25:23] because their functionality
[00:25:25] is very similar
[00:25:25] and I'd like to revamp the experience
[00:25:28] there to be something
[00:25:29] more fun
[00:25:30] and exciting,
[00:25:31] like in an achievement system.
[00:25:33] Come up with some options
[00:25:35] and let's discuss.
[00:25:36] Don't use lavish.
[00:25:39] Okay, the reason I said don't use
[00:25:41] lavish is that I wanted to show you
[00:25:44] what's the default workflow today.
[00:25:45] Looks like for many people.
[00:25:47] And then I'm going to show you
[00:25:48] the difference lavish makes.
[00:25:50] Because I already have leverage
[00:25:52] skills installed.
[00:25:53] My cloud will automatically use lavish
[00:25:55] for this type of question,
[00:25:56] which is why I had to tell
[00:25:58] it not to do that right now.
[00:26:00] Okay, cloud is doing this work.
[00:26:02] Now. Cloud has come back with a response.
[00:26:05] Sometimes it will use its plan mode,
[00:26:07] or sometimes I will ask you
[00:26:09] to write down the plan
[00:26:09] in the markdown file,
[00:26:10] but it's more or less the same.
[00:26:13] It's a wall of text
[00:26:14] I now have to read through.
[00:26:15] It's not very easy to understand
[00:26:17] what what
[00:26:18] each option
[00:26:20] is actually going to look like,
[00:26:22] and if I'm not happy
[00:26:23] with some parts of it,
[00:26:24] I can't very easily tell cloud
[00:26:27] which parts I'm talking about.
[00:26:28] I can select a piece of text
[00:26:30] in the plan and say, this is wrong.
[00:26:32] Now let's try
[00:26:33] the exact same prompt with lavish.
[00:26:35] Here it goes again.
[00:26:36] I actually don't have to say
[00:26:37] use lavish
[00:26:38] because the agent already
[00:26:40] has the lavish skill
[00:26:41] that tells the agent
[00:26:42] for this type of planning
[00:26:44] it should establish, for demo purpose,
[00:26:46] I just wanted to be explicit.
[00:26:48] Cloud would roughly do the same things
[00:26:50] to figure out the options,
[00:26:52] except at the end
[00:26:53] it would not print out that wall of text.
[00:26:56] Again,
[00:26:56] it will launch the browser
[00:26:58] and show me this page. Now look at this.
[00:27:01] This is the lavish editor.
[00:27:03] The reason I named it lavish
[00:27:04] is that it's richer than a rich editor.
[00:27:07] I almost named it filthy
[00:27:09] rich editor,
[00:27:09] but that's just not the best
[00:27:11] sounding name.
[00:27:12] Lavish editor basically
[00:27:14] instructed the agent
[00:27:15] to create an HTML artifact
[00:27:17] to visualize what we need to discuss.
[00:27:19] It always uses the same design system
[00:27:22] as the current project being worked on,
[00:27:24] so this is consistent
[00:27:25] with how the app actually looks.
[00:27:28] This makes it very easy
[00:27:29] to reveal concepts and prototypes.
[00:27:32] See the option is laid out here.
[00:27:33] This is so much easier to understand
[00:27:36] than the huge wall of text
[00:27:37] we were looking at
[00:27:38] in the terminal, right?
[00:27:40] I can also annotate
[00:27:41] and make comments
[00:27:43] on specific parts of the artifacts
[00:27:45] to give feedback to the agent.
[00:27:47] This is something
[00:27:47] that's really hard
[00:27:48] to do with the wall of
[00:27:49] text, or a markdown file
[00:27:52] And at the bottom, there
[00:27:54] are things for me to decide on,
[00:27:56] and I can just click on these options
[00:27:59] to make the decisions.
[00:28:00] I just sent this feedback back
[00:28:02] to the agents inside of lavish
[00:28:04] without even having to go back
[00:28:05] to the terminal.
[00:28:06] Honestly, I can never go back
[00:28:08] to reading text in the terminal anymore.
[00:28:10] This is just way too much more efficient.
[00:28:12] Now the agent has made updates to the and
[00:28:15] I feel happy about this,
[00:28:16] so I'll just tell the agent
[00:28:18] to start building.
[00:28:19] Start building and we'll end
[00:28:22] the session.
[00:28:23] We can
[00:28:24] then go back to the terminal now and see.
[00:28:27] The agent will start to work
[00:28:28] on the implementation,
[00:28:30] because we already clarified
[00:28:31] all the requirements
[00:28:32] in the planning phase.
[00:28:33] I typically don't
[00:28:34] need to interfere at all
[00:28:35] during this implementation phase.
[00:28:37] I only come back to this
[00:28:38] when the agent has done.
[00:28:39] And when the agent says it's done,
[00:28:42] that's actually
[00:28:42] when things get really tricky.
[00:28:45] This is where a lot of people
[00:28:46] will spin up
[00:28:47] their editor
[00:28:48] and start reviewing the diff.
[00:28:51] The problem is, AI writes code so fast,
[00:28:54] and if every piece of code requires
[00:28:57] your review,
[00:28:57] then you are creating a big
[00:28:59] bottleneck on yourself
[00:29:00] because you can only review so many
[00:29:02] every day.
[00:29:03] Your velocity will be hard capped by it.
[00:29:06] And even more importantly, reviewing diff
[00:29:09] is just not fun.
[00:29:11] No one says I became an engineer
[00:29:13] because I love reviewing diffs all day.
[00:29:15] My advice
[00:29:16] here is that
[00:29:18] in order to
[00:29:18] really scale ourselves with AI,
[00:29:21] we have to think of ourselves
[00:29:22] more as an engineering manager
[00:29:24] or engineering director.
[00:29:26] Your directors
[00:29:27] most likely don't review any place yet.
[00:29:30] They can influence the quality
[00:29:31] of their team's software
[00:29:32] by creating good culture
[00:29:34] and processes, and rely on the team
[00:29:37] to carry them out.
[00:29:38] That's what we should do with AI.
[00:29:40] What I do here,
[00:29:41] when the agent says the work is
[00:29:43] done, is not to start
[00:29:44] reviewing the dips or start
[00:29:46] manually testing the changes.
[00:29:48] That's too much overhead.
[00:29:49] On myself,
[00:29:50] I sense the change into a pipeline
[00:29:52] I built called No Mistakes.
[00:29:57] No mistakes is also free and open source.
[00:30:00] It orchestrates your agent
[00:30:01] to execute a series of steps
[00:30:03] that takes this first pass code
[00:30:05] all the way through to a clean PR.
[00:30:07] It would first create a branch
[00:30:09] if one doesn't exist yet,
[00:30:10] and then create a commit
[00:30:12] and then take it through a pipeline
[00:30:14] in an isolated work tree,
[00:30:16] so nothing during the validation
[00:30:18] would affect your current repo.
[00:30:19] It would first understand
[00:30:20] your real intent behind the change
[00:30:22] by analyzing
[00:30:23] your agent session,
[00:30:24] then rebase the change
[00:30:26] on top of the latest main branch
[00:30:28] on remote
[00:30:28] origin and resolve merge
[00:30:30] conflicts up front,
[00:30:31] then starts
[00:30:32] an adversarial review
[00:30:34] in its own fresh context window.
[00:30:36] This is where most problems get caught,
[00:30:38] and obvious problems
[00:30:40] will get self corrected,
[00:30:41] but ambiguous ones
[00:30:43] that have product
[00:30:44] implications will be escalated
[00:30:46] to us humans for a decision after review.
[00:30:49] It also tries to test
[00:30:51] the change end to end
[00:30:52] against the original intent,
[00:30:53] and this step will
[00:30:55] actually record evidence that proves
[00:30:57] the change is working that we can.
[00:30:58] Then later on
[00:30:59] look at to gain more confidence.
[00:31:02] It will then do a documentation pass
[00:31:04] of updating all relevant documentation
[00:31:06] to reflect the latest change.
[00:31:08] And also finally,
[00:31:09] make sure there is no linting problems
[00:31:11] before pushing the branch
[00:31:13] to remote and raise a PR.
[00:31:15] The no mistakes
[00:31:16] pipeline will also keep babysitting
[00:31:18] the PR
[00:31:19] until it's merged,
[00:31:20] because during the PR phase,
[00:31:22] we can still have merge conflicts
[00:31:23] that come in, or CI pipeline failures
[00:31:26] that are very annoying as well,
[00:31:28] with no mistakes doing the babysitting.
[00:31:30] We don't have to waste our own time
[00:31:31] at all.
[00:31:32] Another way to trigger
[00:31:33] no mistakes is as a skill.
[00:31:36] I can just type no mistakes in the agent
[00:31:39] and it will do the same pipeline
[00:31:41] as This may seem very slow,
[00:31:43] but in practice
[00:31:44] I never stare at this screen.
[00:31:46] I would go spin up other tasks.
[00:31:47] I come back only when no mistake says
[00:31:50] all checks passed
[00:31:51] that's when I go to the PR
[00:31:53] and apply my judgment.
[00:31:54] Here's the PR
[00:31:55] from the change we just did.
[00:31:57] We can see here
[00:31:58] it summarized the original intent.
[00:32:00] What's changed,
[00:32:02] how it's tested,
[00:32:03] and what happened
[00:32:04] during the normal stakes pipeline.
[00:32:06] We can click to see the evidence
[00:32:09] from its testing
[00:32:10] to know
[00:32:11] whether it's really done
[00:32:12] what we asked for,
[00:32:14] depending on what the change is,
[00:32:16] the evidence
[00:32:17] could be a screenshot like this
[00:32:19] a video demo,
[00:32:20] a log file, or something else.
[00:32:22] It's designed
[00:32:22] to give you the most direct way
[00:32:24] to see the change
[00:32:25] working as you intended.
[00:32:26] We can also see that
[00:32:27] the pipeline discovers
[00:32:29] some problems
[00:32:29] and fix them before raising the PR.
[00:32:32] This is a good time to audit
[00:32:34] whether these changes
[00:32:35] are actually what we need.
[00:32:36] If anything doesn't look right,
[00:32:38] we can go back to the agent
[00:32:39] and ask for more changes
[00:32:40] before merging this PR.
[00:32:42] This risk assessment
[00:32:43] here is also very useful.
[00:32:45] I basically look at this to decide
[00:32:47] how much time
[00:32:47] I should spend on reviewing
[00:32:49] this change in more detail.
[00:32:51] For low risk changes,
[00:32:52] I don't really look at the diff at all
[00:32:54] Because I have validated
[00:32:56] time and time again for low risk changes.
[00:32:58] Any problem I could catch
[00:33:00] is very likely
[00:33:01] already caught by the pipeline
[00:33:03] only more
[00:33:03] risky changes are worth my
[00:33:05] This is how I scale up
[00:33:06] the volume of code changes
[00:33:07] I do every day through
[00:33:09] a large crew of agents,
[00:33:10] without losing control on quality.
[00:33:12] One thing we are starting to see
[00:33:14] now is that the place where I spend
[00:33:16] time is towards the beginning
[00:33:18] and the end of the task.
[00:33:20] At the beginning
[00:33:21] I would spend time in lavish to plan
[00:33:23] the requirements more clearly.
[00:33:25] At the end
[00:33:26] I would come in and hold
[00:33:27] a bar on quality.
[00:33:29] All these parts in the middle
[00:33:31] is done by AI,
[00:33:32] which frees me up to spin up other tasks.
[00:33:35] This is a core aspect of how I work,
[00:33:37] and you can see the more time
[00:33:39] I can free up in the middle,
[00:33:41] the more work I can go do in parallel.
[00:33:43] So an interesting question
[00:33:45] now is
[00:33:46] how do we get the agents
[00:33:47] to work for longer
[00:33:48] and longer in the middle?
[00:33:50] That depends on us
[00:33:51] giving them more and more complex tasks
[00:33:53] that take longer to complete.
[00:33:55] But more complex tasks are often
[00:33:58] not as easy for our agents
[00:33:59] to complete autonomously.
[00:34:02] An extreme version of this is
[00:34:03] when I go to bed,
[00:34:04] I sleep for 7 to 8 hours every night.
[00:34:07] How do I keep the agents busy
[00:34:09] for eight hours?
[00:34:10] This is where I say good night.
[00:34:13] Have fun.
[00:34:13] It's another free and open source tool
[00:34:15] I built specifically
[00:34:17] for long running tasks.
[00:34:18] It's becoming quite popular.
[00:34:20] It's that simple to use.
[00:34:22] Just give it an objective
[00:34:23] and it will keep going
[00:34:24] until it meets some stop condition
[00:34:26] you defined.
[00:34:27] Let me show you a real example
[00:34:29] that I often do.
[00:34:30] This is again in the hybrid repo
[00:34:32] I will run.
[00:34:33] Good night.
[00:34:33] Have fun and give a prompt.
[00:34:36] Pretend you are a seven year
[00:34:38] old kid and use the high bit
[00:34:40] app end to end.
[00:34:41] Don't mind
[00:34:42] the profile
[00:34:42] creation step
[00:34:43] which is designed for parents
[00:34:45] in the rest of the app.
[00:34:46] Try to do different things
[00:34:47] and find the first usability problem
[00:34:50] that will confuse you as a kid,
[00:34:52] or stop you from knowing how to proceed.
[00:34:54] If you find a problem, stop and fix it,
[00:34:57] then rinse and repeat.
[00:35:00] Here he goes.
[00:35:01] Good night. Have fun.
[00:35:02] Is now running in the loop.
[00:35:03] To execute on what I just asked for.
[00:35:06] I can monitor token usage here
[00:35:08] or how many iterations have been done.
[00:35:10] The iterations will be showing up
[00:35:12] as the moons in this row,
[00:35:13] and I can see how many commits
[00:35:15] have been made as well.
[00:35:16] Or I can just go to bed
[00:35:17] knowing the agents won't stop
[00:35:19] until there is no more problem
[00:35:20] to be found.
[00:35:21] When I wake up,
[00:35:22] I can reveal a list of commits
[00:35:24] made on this new branch and decide
[00:35:26] which ones I want.
[00:35:28] I typically use goodnight.
[00:35:29] Have fun for improving
[00:35:31] on some verifiable objectives
[00:35:33] or objectives,
[00:35:34] where I trust the agent
[00:35:36] to have the reasonable judgment over,
[00:35:38] like the one we just did.
[00:35:39] Verifiable objectives
[00:35:41] are more like reducing page load
[00:35:43] time, improving
[00:35:44] end to end test coverage
[00:35:45] or like Android hypothesis auto research.
[00:35:48] Keep experimenting different hypotheses
[00:35:51] to improve on the metric.
[00:35:52] These are all
[00:35:53] well suited for a long running loop.
[00:35:55] To tackle
[00:35:56] the recently introduced
[00:35:57] slash goal
[00:35:58] command in Codex and Cloud
[00:36:00] code can also do something similar,
[00:36:02] good night.
[00:36:03] Have fun
[00:36:03] still gives me a better experience.
[00:36:05] Because I can set a token cap or
[00:36:08] iteration cap or stop condition
[00:36:10] more precisely,
[00:36:12] whereas in Cloud Code and Codex,
[00:36:14] if I set a goal before I go to bed,
[00:36:16] I might wake up realizing my weekly
[00:36:19] quota is all Good night.
[00:36:20] Have fun.
[00:36:21] Solved a very important problem,
[00:36:23] which is to keep the agents
[00:36:24] running for a long time.
[00:36:26] So when the agents are running,
[00:36:28] I'm freed up to do more things.
[00:36:30] This is when we level up
[00:36:32] and start working with multiple crewmates
[00:36:34] in parallel.
[00:36:34] So let's spin up another tab in teams
[00:36:37] and get more work started.
[00:36:39] Now here's the problem.
[00:36:40] In this directory I already have.
[00:36:42] Good night.
[00:36:43] Have fun running.
[00:36:44] So if I spin up another agent
[00:36:46] working in the same directory,
[00:36:47] they will step on each other's
[00:36:49] toes and cause conflicts.
[00:36:51] The default solution
[00:36:52] here is git work tree.
[00:36:54] For those of you
[00:36:54] who aren't familiar with it,
[00:36:56] a guitar work
[00:36:57] tree is basically creating
[00:36:58] a clone of your report directory.
[00:37:00] I can create one by typing git work tree
[00:37:03] add and give a path here.
[00:37:07] Now we have to think about a name.
[00:37:09] This is when you waste five minutes
[00:37:11] and eventually give up and just say hi.
[00:37:13] Bit two.
[00:37:15] Now we have a work tree
[00:37:16] and we can navigate to it.
[00:37:18] So let's go find it.
[00:37:20] It's in high bit two.
[00:37:21] This is a separate directory
[00:37:23] on the file system.
[00:37:24] So we can have an agent
[00:37:25] doing anything here.
[00:37:26] And it won't conflict
[00:37:27] with good night to have fun,
[00:37:29] which is running in the original report
[00:37:31] directory.
[00:37:31] The problem with work trees
[00:37:33] is that we now have something
[00:37:35] to maintain in our head.
[00:37:36] I need to remember.
[00:37:38] Oh, I have hybrid two here.
[00:37:40] Next time I come into this hybrid
[00:37:42] two directory
[00:37:43] I would wonder
[00:37:44] what was I doing in this work
[00:37:45] tree last time?
[00:37:47] Is there still an agent running or is it
[00:37:49] All of
[00:37:50] that has to
[00:37:50] exist in my head,
[00:37:52] and there is no way I'm
[00:37:53] going to remember all that.
[00:37:54] So this work tree
[00:37:56] basically becomes a debt.
[00:37:57] To get rid of it.
[00:37:58] I need to run this remove command.
[00:38:02] Remove.
[00:38:05] This is just a lot of overhead.
[00:38:07] My solution to
[00:38:08] that is another tool
[00:38:09] I built called Treehouse.
[00:38:11] It's very simple.
[00:38:12] I just come into this
[00:38:13] repo and I run Treehouse.
[00:38:16] It would drop me into a fresh work tree
[00:38:18] where I can start doing whatever I want.
[00:38:21] I can keep spinning up
[00:38:22] more and more of this work trees
[00:38:24] by running Treehouse again.
[00:38:27] And if I want, I can see a list
[00:38:30] of all the work trees
[00:38:32] by typing Treehouse status.
[00:38:34] So I can see
[00:38:35] which ones are being used versus not.
[00:38:37] When I'm done,
[00:38:38] I can just close this tab
[00:38:39] and Treehouse knows that I'm done,
[00:38:42] so it will free up
[00:38:43] that work tree for future use.
[00:38:45] Next time I ask for work tree,
[00:38:47] it will try to reuse one of the idol
[00:38:50] work trees
[00:38:50] instead of creating a brand new
[00:38:52] So let's start some real work.
[00:38:54] I have a bunch of user feedback
[00:38:56] from my son's last round of playtesting,
[00:38:58] so let me use this
[00:38:59] first worksheet
[00:39:00] we created and launch
[00:39:01] cloud, and I will say,
[00:39:04] I remember it's hard for the kid
[00:39:06] to realize
[00:39:06] they can press and hold
[00:39:08] the voice input button to talk.
[00:39:10] By default
[00:39:10] they just click it
[00:39:11] and then they will see a popover.
[00:39:13] Maybe in the popover,
[00:39:14] we add a label that tells them
[00:39:16] they can also press and hold
[00:39:19] and I'll enter.
[00:39:21] Then I'll spin up a new tab
[00:39:23] Treehouse Cloud, and this time I will say
[00:39:28] the Image attachment dropdown
[00:39:29] menu should have an action
[00:39:31] that takes a screenshot
[00:39:32] of the current app
[00:39:33] and use that as the attachment.
[00:39:37] All right, one more tab.
[00:39:39] Treehouse cloud.
[00:39:44] Our agent status bar right above the chat
[00:39:46] input is not always showing bot activity.
[00:39:49] Look into
[00:39:50] what happened
[00:39:51] there and make sure
[00:39:52] when any bots are in progress,
[00:39:54] it always displays
[00:39:55] something that reflects
[00:39:56] the latest activity.
[00:39:59] Boom!
[00:40:00] We now have three
[00:40:00] sessions running in parallel.
[00:40:02] Now I can keep going
[00:40:03] because none of these sessions
[00:40:05] will need my attention anytime soon,
[00:40:07] especially if I tell them to run.
[00:40:09] No mistakes after implementation.
[00:40:11] I know
[00:40:11] whether they need me
[00:40:13] by looking at the top status bar,
[00:40:15] and I can switch
[00:40:16] between the tabs using keyboard
[00:40:17] shortcuts like this.
[00:40:19] That's very important
[00:40:20] for managing a lot of parallel
[00:40:21] sessions efficiently.
[00:40:23] That said,
[00:40:24] after doing this for a while,
[00:40:26] you will discover that
[00:40:27] juggling between all these sessions,
[00:40:29] it's quite exhausting.
[00:40:31] The constant context switch
[00:40:32] and having to remind yourself
[00:40:34] what each session was even doing
[00:40:36] just doesn't feel like an ideal end
[00:40:38] game experience.
[00:40:39] So I kept pushing the boundary on this
[00:40:42] and I discovered that
[00:40:44] I needed a first mate,
[00:40:46] someone I can talk to as a captain
[00:40:48] that will carry out
[00:40:49] all my directions and manage
[00:40:51] all the crewmates for me
[00:40:53] so I can focus on the big picture
[00:40:55] like where should we go next?
[00:40:56] not playing whack
[00:40:57] a mole
[00:40:58] with this
[00:40:58] increasingly high number of crewmates,
[00:41:00] this is how I level up
[00:41:02] and truly become a captain.
[00:41:04] My First mate is another free
[00:41:06] and open source project
[00:41:07] and it's very new.
[00:41:08] The way to use it is by just cloning it.
[00:41:14] And then I can run
[00:41:17] an agent in this repository.
[00:41:19] Now I just talk to it
[00:41:21] and ask it to work on any projects
[00:41:23] I like.
[00:41:24] Let's say
[00:41:25] I'd like to work on lavish
[00:41:27] access, GitHub, Axi and Chrome dev tools.
[00:41:29] Actually They are all GitHub projects
[00:41:31] I own.
[00:41:32] first mate is starting up
[00:41:33] and the first time we run it
[00:41:35] it will do some setup
[00:41:36] and ask for some preferences,
[00:41:38] but it's also just talking to it,
[00:41:39] which is pretty easy.
[00:41:41] you might wonder
[00:41:42] why is the transcription so good?
[00:41:44] Because it's
[00:41:45] recognizing this project names.
[00:41:47] Let me show you.
[00:41:49] Open Silver Whisper actually supports
[00:41:52] this customization
[00:41:54] through a system prompt.
[00:41:56] So what we can do
[00:41:57] here is in this model menu
[00:42:00] in the transcription menu
[00:42:01] there is an initial prompt.
[00:42:03] And we can put in some common vocabulary
[00:42:05] that we use into this system prompt.
[00:42:08] this prompt is
[00:42:09] what makes the transcription really good.
[00:42:10] First mate here is asking how strict
[00:42:13] I want to be
[00:42:13] with the code changes in this repos,
[00:42:15] and I want to select full gates to PR.
[00:42:19] This is basically going
[00:42:20] to be using no mistakes
[00:42:21] as the pipeline to validate its change
[00:42:25] and first task.
[00:42:26] Yeah, I'll describe it. Right now.
[00:42:29] A real thing I want to do
[00:42:30] is for all three
[00:42:32] projects, I'd like to add an update
[00:42:34] command on the CLI
[00:42:36] that will update their
[00:42:37] version to the latest on npm.
[00:42:41] And let's see what First Mate does.
[00:42:43] It realizes that this is not one task,
[00:42:46] but three parallel tasks,
[00:42:47] and it's now spinning up
[00:42:49] these tabs in timox,
[00:42:51] just like we be the scenes.
[00:42:53] It would also call tree House
[00:42:54] to create work trees,
[00:42:56] and then run an agent in that work
[00:42:58] tree to get the work done,
[00:42:59] and then it will run.
[00:43:00] No mistakes to validate the change
[00:43:02] and get the PR ready for us to review.
[00:43:04] Now you can see
[00:43:05] it's first made that
[00:43:07] it's doing the juggling.
[00:43:08] I don't need to worry
[00:43:09] about any of this now.
[00:43:10] I can just keep giving it more work.
[00:43:13] Hey first mate,
[00:43:14] let's also look at the most recent
[00:43:16] three open issues in lavish axillary
[00:43:19] and let's discuss which
[00:43:20] ones are actionable.
[00:43:23] Boom!
[00:43:24] First mate
[00:43:25] now is pulling the open
[00:43:26] issues from the repo
[00:43:27] while waiting for the three background
[00:43:29] agents working in parallel.
[00:43:31] All right,
[00:43:31] first mate said number 87 is cleanest.
[00:43:35] It's very actionable.
[00:43:36] And let me just see.
[00:43:38] What is this?
[00:43:39] Don't toggle in annotation mode.
[00:43:42] Okay.
[00:43:44] That's the clear bug.
[00:43:46] All right, first mate, let's address
[00:43:49] number 87.
[00:43:52] Look, now first mate is struggling
[00:43:54] a lot of tasks for me
[00:43:56] that I otherwise
[00:43:57] would have to manage by myself.
[00:43:59] Watching it
[00:43:59] context switch is actually
[00:44:01] an oddly satisfying experience,
[00:44:03] because I know that's what
[00:44:04] I would have to do otherwise.
[00:44:06] First mate is basically all my tools
[00:44:08] coming together
[00:44:09] as one cohesive workflow,
[00:44:11] and I have been really happy with it.
[00:44:13] It's been a pretty
[00:44:14] significant improvement
[00:44:15] to my overall experience
[00:44:17] working with agents.
[00:44:18] I highly recommend trying it out
[00:44:19] if you are still directly talking
[00:44:21] to every single agent session one by one,
[00:44:23] it will be a pretty massive upgrade.
[00:44:26] Something you start to notice
[00:44:27] after having a first mate.
[00:44:28] Is that because first mate took care
[00:44:31] of so many things for you,
[00:44:32] you start to run out of ideas
[00:44:34] for what to ask you to do.
[00:44:36] This is a good thing because it indicates
[00:44:38] the bottleneck is shifting,
[00:44:40] but it also means you,
[00:44:41] as the captain, needs to keep up.
[00:44:44] This requires a mindset shift
[00:44:46] of focusing more of your energy
[00:44:48] on understanding what matters
[00:44:50] by talking to your users,
[00:44:52] understanding the competitive landscape,
[00:44:54] and crafting a good treasure
[00:44:56] map that can lead your crew
[00:44:58] to a good direction.
[00:45:00] Once you started doing
[00:45:01] that, congratulations!
[00:45:03] You have successfully transitioned
[00:45:04] from a sailor into a great captain.
[00:45:07] All right.
[00:45:08] We have gone from not having a ship
[00:45:10] to being a captain
[00:45:11] that has a first mate and a big crew
[00:45:14] that sailed together.
[00:45:15] This is a pretty good time
[00:45:17] to wrap up this video.
[00:45:18] All my tools can be found on my GitHub
[00:45:20] and will be linked
[00:45:21] in the description below.
[00:45:23] They are all free and open source.
[00:45:25] I built them
[00:45:26] because I just want
[00:45:26] to see more people learning
[00:45:28] how to do
[00:45:28] a genetic engineering
[00:45:29] effectively and doing it
[00:45:31] in an enjoyable way,
[00:45:32] and that's what I hope
[00:45:34] you can get out of this video.
[00:45:36] I will continue to share
[00:45:37] more of my workflow
[00:45:38] and things
[00:45:38] I find useful
[00:45:39] on my channel,
[00:45:40] so don't forget to subscribe
[00:45:41] if you don't want to miss anything.
[00:45:43] Thank you for watching
[00:45:44] and see you next time!
