---
type: raw_capture
source_type: x
url: https://x.com/romainhuet/status/2049597180474970179
original_url: https://x.com/romainhuet/status/2049597180474970179
author: "Romain Huet"
handle: romainhuet
status_id: 2049597180474970179
captured_at: 2026-06-11T00:25:59+08:00
published_at: "Wed Apr 29 21:10:22 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 13
  reposts: 23
  likes: 367
---

# X post by @romainhuet

## Source

- Original: [https://x.com/romainhuet/status/2049597180474970179](https://x.com/romainhuet/status/2049597180474970179)
- Canonical: [https://x.com/romainhuet/status/2049597180474970179](https://x.com/romainhuet/status/2049597180474970179)
- Author: Romain Huet (@romainhuet)

## Verbatim Text

GPT-5.5 + GPT-Image-2 is becoming one of the best combos for building apps!

@dkundel breaks down why it works so well. We built those learnings into the Build Web Apps plugin, so Codex can handle the design-to-app loop for you. 👌

## Quoted Post

- URL: https://x.com/dkundel/status/2049591675518165134
- Author: dominik kundel (@dkundel)

The Most Fun I’ve Had Building Apps: GPT-5.5 + GPT-Image-2

Last week, [we released GPT-5.5](https://openai.com/index/introducing-gpt-5-5/), our most intelligent model yet. In combination with the recent Codex app feature launches it has in many ways [changed how I work](https://x.com/dkundel/status/2046297434205430130).

One of the things that blew my mind though was GPT-5.5’s increase in coding capabilities, especially its focus on details and instruction following and how it translates into better, more creative apps. Combining GPT-5.5’s attention to detail with GPT-Image-2’s capability of rendering high quality UIs lets you create more creative high fidelity apps.

Try out the Build Web Apps plugin to see them come together by having Codex design and implement your front end apps!

## From screenshot to interactive app

One of the biggest wow moments I had in the early testing phases of GPT-5.5 was when @jxnlco sent me a picture of an app he had been working on. I pasted the screenshot into the Codex app and asked Codex to implement it with real mission data from the Artemis II mission.

Codex reviewed the image, pulled real mission data from the @NASA website and started implementing the app.

What surprised me the most is that it noticed and solved some challenges that I hadn’t even realized. The screenshot had a visible ratio between moon and earth that was unrealistic for the mission data. To solve for that Codex, went and interpolated the data around the earth and moon to account for that while preserving a more realistic flight path between the two planets.

For a more complete view I then asked Codex to also add a “true scale” option to better see the full flight based on the real data.

[Embedded Tweet: https://x.com/i/status/2047377234806374756]

## GPT-Image-2 for the design

GPT-5.5 is especially strong at implementing a design once it has something clear to build toward. But what do you do when you do not have a design spec yet?

That’s where the GPT-Image-2 launch could not have come at a better time. The model is a big step up in image generation overall but it’s especially good at generating user interfaces and rendering text.

So you can ask Codex or ChatGPT to first generate a design for you using GPT-Image-2 and then hand it as the implementation guidance to GPT-5.5 to turn it into reality.

In fact many of you have already figured this out and have built some fun and impressive things with it!

[Embedded Tweet: https://x.com/i/status/2047637933948109105]

[Embedded Tweet: https://x.com/i/status/2047112052213203034]

[Embedded Tweet: https://x.com/i/status/2047625152121180533]

## Bringing things together

Together with last week’s addition of browser use inside the Codex app we shipped an update to our “Build Web Apps” plugin inside the Codex app. Once installed Codex automatically uses the new “Frontend App Builder” skill inside the plugin to use image gen with GPT-Image-2 to generate the concept before passing the implementation to GPT-5.5 and uses the new in-app browser for validation of the app.

It will also use GPT-Image-2 to generate the assets inside the app that are necessary to polish the app.

You can also combine it with plan mode using /plan to have Codex work through more complex apps like building a 3D modeling software.

Big shout also to @LexnLin who updated his taste-skill with a similar approach!

[Embedded Tweet: https://x.com/i/status/2046706461573579064]

## Improved design accuracy

One thing we noticed was that there could be a difference in polish and implementation accuracy depending on how you used GPT-Image-2 with Codex. If you manually combined image generation and implementation in a single prompt, Codex could sometimes treat the generated design more as inspiration than as a strict spec, especially on longer or more complex tasks.

[Embedded Tweet: https://x.com/i/status/2047449896039657652]

That’s part of why we shipped the updated Build Web Apps plugin. It gives Codex a more structured workflow that includes explicitly revisiting and comparing the GPT-5.5 implemented design with the original design from GPT-Image-2. In practice, that tighter loop helps preserve design intent and improves accuracy.

If you’re doing this manually, a good trick is to explicitly ask Codex to revisit the design image and do a side-by-side critique against the implementation or screenshot of the app.

## Let your creativity loose!

This approach is not limited to web apps either. Ask Codex to design and implement your next mobile or native app. It’s been a lot of fun to have GPT-Image-2 to visualize ideas and have Codex turn them into reality. Whether it’s games, utility apps or even entire operating systems, let your creativity loose!

[Embedded Tweet: https://x.com/i/status/2048845170746294666]

If you build something impressive, share it below or [submit it for our showcase](https://developers.openai.com/showcase).

## Capture Note

TweetDetail returned complete normal-post text.
