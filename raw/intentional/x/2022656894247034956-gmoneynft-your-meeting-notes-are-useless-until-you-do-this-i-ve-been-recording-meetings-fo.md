---
type: raw_capture
source_type: x
url: https://x.com/gmoneyNFT/status/2022656894247034956
original_url: https://x.com/gmoneyNFT/status/2022656894247034956
author: "gmoney.eth"
handle: gmoneyNFT
status_id: 2022656894247034956
captured_at: 2026-06-19T20:45:11+08:00
published_at: "Sat Feb 14 12:59:17 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 23
  reposts: 10
  likes: 139
---

# X post by @gmoneyNFT

## Source

- Original: [https://x.com/gmoneyNFT/status/2022656894247034956](https://x.com/gmoneyNFT/status/2022656894247034956)
- Canonical: [https://x.com/gmoneyNFT/status/2022656894247034956](https://x.com/gmoneyNFT/status/2022656894247034956)
- Author: gmoney.eth (@gmoneyNFT)

## Verbatim Text

your meeting notes are useless until you do this

i've been recording meetings for the last couple of years. every call, every zoom, every sync. i always said i was going to do something with them. review them, extract the value, turn them into something useful.

yada yada yada. life gets in the way. i never do anything with them. the recordings just pile up in some folder i never open. all those good ideas, all those insights, all that ip - gone.

here's what changed.

## the problem

in the middle of a call, i'll have an idea. something worth sharing. something that would make a good tweet, or a blog post, or just something to remember. and i think "oh, that's a good one. i should turn that into content."

and then the call ends. i move on to the next thing. and i forget. every single time. it's not that i don't care. it's that the gap between "having the idea" and "doing something with it" is too big. by the time i remember, the context is gone. the energy is gone. the momentum is gone.

## the system

1. every night at 8pm, my ai pulls the day's meeting transcripts.
granola records everything. the api exports to markdown. my agent grabs all of it automatically. no manual work.

2. i review action items.
what did i agree to? what did i commit to? what needs following up? all extracted and organized. the alternative was relying on memory. i don't do that anymore.

3. i turn meeting insights into content.
this is the part that surprised me. my ai scans the transcript for "contentable" moments — things i said that are worth sharing. hot takes. observations. lessons. it drafts 10 tweet pitches in my voice. i pick the best ones and post them.

the gap between "having the idea" and "doing something with it" went from "never" to "every night."

## how to set this up (step by step)

step 1: get an ai note-taking app.
i use granola. it sits on your mac, records audio from meetings (without joining as a bot), and merges your human notes with the ai transcript. [@ksc called it the ai note-taking app that actually works](https://x.com/ksc/status/1917643621320515756) and they're right. alternatives: otter, fireflies, tldv.

step 2: get an ai agent framework.
i use openclaw. it's what runs my agents 24/7. you can also use claude code directly. the key is: you need something that can run on a schedule and process your notes automatically.

step 3: connect the two.
granola has an api. grab your auth token from ~/Library/Application Support/Granola/supabase.json. set up a cron job (or use your agent's heartbeat) to pull transcripts every night.

step 4: define what you want.
don't automate everything at once. start with one output:

- action items → slack/notion

- content ideas → draft tweets

- meeting summary → email to yourself

step 5: build the skill.
write instructions for your agent. include: your voice (how you write), what makes something "content-worthy," formatting preferences. save it as a skill or playbook that runs automatically.

step 6: cron it.
set it to run every night at a time that works for you. 8pm works for me. the point is: consistency. every night. no manual triggering.

## why this matters

[@rahul_j_mathur said it best](https://x.com/Rahul_J_Mathur/status/1896077640223899774): the transcript is not the valuable part. the summary is not the valuable part. what you do with it afterward is where the value is.

your meetings are generating ip constantly. good ideas, decisions, insights, content. and it's all disappearing into a black hole of apps you never check. the fix isn't a better note-taking app. it's connecting your notes to something that actually does something with them.

save this. share it with your agents. set it up tonight.

## X Article Metadata

- Title: your meeting notes are useless until you do this
- Preview: i've been recording meetings for the last couple of years. every call, every zoom, every sync. i always said i was going to do something with them. review them, extract the value, turn them into

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
