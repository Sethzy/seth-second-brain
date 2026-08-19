---
type: raw_capture
source_type: web
title: "Cuelume — interaction sounds for the web"
url: "https://cuelume-site.pages.dev/"
collected_at: 2026-07-26T07:17:32Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Cuelume — interaction sounds for the web

Source: https://cuelume-site.pages.dev/

## Capture Text

Cuelume — interaction sounds for the web
cuelume
agents.md
copied
v0.1.2 · 14 cues · 0 deps
Tiny interaction sounds that make interfaces feel alive.
Cuelume synthesizes every cue live with Web Audio — no files, no runtime
    dependencies. Everything below runs on the real library.
Sound palette
press a cue, or use 1–0 + Q–R
idle
— Hz · — s
chime
sparkle
droplet
bloom
whisper
tick
press
release
toggle
success
error
page
loading
ready
Interaction patterns
live
data-cuelume-hover
fine-pointer hover
Docs
Examples
Changelog
data-cuelume-press
+ data-cuelume-release
Save
Saved
data-cuelume-toggle
Why cuelume
every card plays
mp3
cuelume
<5 kB
Tiny
No audio files, no dependencies. All fourteen sounds together are smaller than one MP3 click.
Live
Every cue is synthesized with Web Audio the moment it plays. There are no recordings to load.
data-cuelume-press
Save
Declarative
One attribute per behavior. Add it to your markup and bind() does the rest.
Curated
Fourteen cues, each with its own shape: chimes, glides, clicks and blooms. Not fourteen tweaks of one click.
Install
click the command to switch package manager
$
npm install cuelume
Usage
index.html
app.ts
<!-- one attribute per behavior -->
<button
data-cuelume-press data-cuelume-release
>Save</button>
<a
data-cuelume-hover="tick"
>Docs</a>
<button
data-cuelume-toggle
>Dark mode</button>
import
{ bind, play }
from
"cuelume"
;

bind();
// wires every data-cuelume-* attribute
play(
"success"
);
// or play imperatively
MIT © Daniel White
npm
· curated interaction sounds for the web
