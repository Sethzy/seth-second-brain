---
type: raw_capture
source_type: x
url: https://x.com/0xTria/status/2063952648533897291
original_url: https://x.com/0xTria/status/2063952648533897291
author: "0xTria"
handle: 0xTria
status_id: 2063952648533897291
captured_at: 2026-06-19T23:50:56+08:00
published_at: "Mon Jun 08 11:53:52 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 8
  reposts: 39
  likes: 232
---

# X post by @0xTria

## Source

- Original: [https://x.com/0xTria/status/2063952648533897291](https://x.com/0xTria/status/2063952648533897291)
- Canonical: [https://x.com/0xTria/status/2063952648533897291](https://x.com/0xTria/status/2063952648533897291)
- Author: 0xTria (@0xTria)

## Verbatim Text

I Built an AI Influencer for $0 and Started Monetizing Her in the First Week.

Most AI avatar tutorials stop at one pretty face. That is not a business. I wanted to build a repeatable system: same person, same style, same voice, product videos, lifestyle clips, and a workflow anyone can copy without paying for an AI avatar platform.

The goal was simple: not to create one image, but to create a character I could use again and again. If she looked different in every post, the whole thing was useless. If the videos felt like AI demos, nobody would watch them. If the workflow required a paid avatar platform, it was not worth copying.

So I built the system from zero: face, identity, voice, photos, product clips, short videos, and final edits.

Here is the exact workflow.

## Step 1 — Don’t start with a prompt. Start with identity.

Most AI influencers fail because they are built from one vague prompt:

```
pretty realistic ai girl, influencer, 9:16
```

That gives you the same average face everyone else gets.

Instead, build the person from references.

Use Pinterest to collect 2–3 faces, then decide what each reference is responsible for:

- Reference 1: hair color and haircut

- Reference 2: face shape and eyes

- Reference 3: lips, style, vibe, or expression

The goal is not to copy a real person.

The goal is to mix separate traits into a new, consistent synthetic character.

## Step 2 — Make ChatGPT analyze before it writes.

This is the trick most people skip.

Do not ask ChatGPT to write the final image prompt immediately.

First, upload the references and force ChatGPT to describe each girl separately: face shape, hair, eyes, brows, lips, skin, style.

Then ask it to number them: Girl 1, Girl 2, Girl 3.

Only after that, decide which features you want from each reference.

This prevents random “AI beauty” and turns the avatar into something controlled.

```
You are an expert in visual description and prompt creation for image generation.
Your task: when the user uploads photos of girls, you must:
1. First, analyze the appearance of each girl in detail: face shape, facial features, hair color and texture, eyes, eyebrows, lips, skin, and overall style. Briefly describe each one in 2–3 sentences per photo and number them as “Girl 1”, “Girl 2”, “Girl 3”.
2. Do not create the final prompt immediately. Instead, ask the user clarifying questions: which exact features they want to take from each girl, such as eyes, nose, lips, face shape, hair, and style. Suggest your own recommended mix, but wait for the user’s final answer before creating the prompt.
3. After the user answers, create a hybrid prompt that combines the selected features into one unified character description.
The final prompt must be a detailed English text, no longer than 150 words, and must include:
- the character’s physical appearance;
- a white studio background;
- clothing: black T-shirt;
- soft professional lighting;
- photorealistic style, visible skin texture, high detail.
```

The final image prompt should be in English, under 150 words, and include:

- physical features

- white studio background

- black T-shirt

- soft professional lighting

- photorealism and visible skin texture

## Step 3 — Generate the base portrait.

Once the hybrid prompt is ready, generate the first vertical 9:16 portrait.

Do not move forward until the face works.

If the hair, face structure, skin, and overall vibe are wrong at this stage, everything later becomes harder: body shots, outfits, videos, lip sync, and motion transfer.

When you get a good result, save it as the main identity reference.

This image becomes the “source of truth” for the entire character.

## Step 4 — Build a mini character sheet.

One portrait is not enough.

The model needs to understand the same person from different angles.

In Google Flow, upload the portrait and generate:

1. a waist-up shot

2. a full-body shot

3. any extra angle you will use later

Do not expect the first generation to be perfect.

A good result may take 3–6 attempts. That is normal.

Your goal is not quantity. Your goal is identity consistency.

## Step 5 — Lock the identity before every new scene.

When you place the avatar into a new location, AI models love to “improve” her.

They change the hair, smooth the skin, alter the face, fix asymmetry, or accidentally make her a different person.

So every scene prompt starts with an identity lock:

```
Use exactly the same synthetic person from the attached reference image. Preserve the exact facial structure, body proportions, natural skin tone, and authentic asymmetry. Do not beautify or change the appearance. Hair must remain identical in color and haircut.
```

After the lock, describe the scene:

- what she is doing

- where she is

- what she wears

- how the camera sees her

- what the lighting feels like

- what should stay static

## Step 6 — Create scenes like a mini-vlog, not random images.

The workflow builds three lifestyle shots:

1. city selfie-vlog

2. skincare / face cream shot

3. TikTok-style dance setup

The mindset is simple:

You are not generating one pretty image.

You are building a sequence that can be edited into a story.

Morning routine → outfit → TikTok → city walk.

## Step 7 — Write video prompts like a director.

For animation, a pretty prompt is not enough.

Use this structure:

1. Subject

2. Action

3. Location

4. Camera / angle

5. Lighting / atmosphere

6. Visual style

7. Small movements

[SCREENSHOT 10: Lesson 2, 01:20–03:41 — the 7-part video prompt formula.]

Bad prompt:

```
Girl walking in the city.
```

Better prompt:

```
A young woman walks down a sunny city street while filming herself on the front camera of an iPhone. Vertical handheld selfie-vlog shot, natural walking motion, subtle head movements, blinking, realistic lip sync, soft daylight, casual lifestyle vlog style.
```

One important rule: give the model one main action.

If she walks, jumps, laughs, turns, waves, and talks in one prompt, the model gets confused.

## Step 8 — Animate the shots.

In Google Flow, switch from image mode to video mode, use vertical 9:16, and generate the city selfie-vlog.

The result should feel like a normal front-camera iPhone video: handheld, imperfect, casual, and alive.

For the cream scene, repeat “static camera” twice.

Why?

Because video models sometimes ignore “static shot” if it only appears once.

```
Static front-camera iPhone shot. The camera remains completely static.
```

That one detail can save failed generations.

## Step 9 — Use Motion Control for TikTok.

For TikTok-style content, do not invent movement from scratch.

Use a reference video.

Upload:

- the reference dance video

- your AI character image

- the matching starting frame

Then enable Character Orientation Match Video and generate in 720p.

The closer the pose, silhouette, and outfit are to the reference, the fewer artifacts you get.

## Step 10 — Voice and music make it feel real.

Without sound, it is just a synthetic montage.

The final layer is ElevenLabs:

1. Write a short voiceover

2. Pick a soft female voice

3. Use Enhance for emotional direction

4. Add pauses, whispers, and mood tags manually

5. Generate instrumental background music

The voiceover turns random clips into a character.

The music glues the scenes together.

The final output is a short “My Day” AI lifestyle vlog with face, body, motion, voice, and mood working together.

## The full funnel

References → ChatGPT identity prompt → base portrait → character sheet → scene images → video animation → Motion Control → ElevenLabs voiceover → instrumental music → final edit.

The real lesson:

AI influencers are not made by one magic prompt.

They are made by a system that protects identity at every step.

## X Article Metadata

- Title: I Built an AI Influencer for $0 and Started Monetizing Her in the First Week.
- Preview: Most AI avatar tutorials stop at one pretty face. That is not a business. I wanted to build a repeatable system: same person, same style, same voice, product videos, lifestyle clips, and a workflow

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
