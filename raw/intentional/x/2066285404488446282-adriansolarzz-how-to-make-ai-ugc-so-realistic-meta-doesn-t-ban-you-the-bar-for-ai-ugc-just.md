---
type: raw_capture
source_type: x
url: https://x.com/adriansolarzz/status/2066285404488446282
original_url: https://x.com/adriansolarzz/status/2066285404488446282
author: "Adrian Solarz"
handle: adriansolarzz
status_id: 2066285404488446282
captured_at: 2026-06-19T23:59:22+08:00
published_at: "Sun Jun 14 22:23:24 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 2
  likes: 32
---

# X post by @adriansolarzz

## Source

- Original: [https://x.com/adriansolarzz/status/2066285404488446282](https://x.com/adriansolarzz/status/2066285404488446282)
- Canonical: [https://x.com/adriansolarzz/status/2066285404488446282](https://x.com/adriansolarzz/status/2066285404488446282)
- Author: Adrian Solarz (@adriansolarzz)

## Verbatim Text

How to Make AI UGC So Realistic Meta Doesn't Ban You

the bar for AI UGC just moved.

it used to be "does this look good."

now it's "does this look real enough that Meta's systems don't flag it and a skeptical viewer doesn't clock it in the first 2 seconds."

type shi.

Meta leaned hard into AI moderation this year, and the false bans have been catching legit creators and businesses, not just spam.

at the same time Instagram started pushing reach toward content that reads as authentic and original, and away from anything that looks templated or machine-made.

so realism stopped being just a quality concern and turned into a survival requirement.

---

## The Test Everything Else Serves

before any specific technique, there's one rule the whole checklist exists to pass:

would you believe it's a real video in the first 2 seconds?

be honest with yourself. if you hesitate even slightly, the moderation system hesitates too, and so does the viewer. a clip you have to talk yourself into believing is a clip that's going to get clocked, reported, or flagged. every technique below is just a way of getting a clip to pass this test cleanly, with no hesitation.

run it on every video before it posts. if it doesn't pass, it doesn't ship.

---

## Kill the Fake Background Blur

this is the single most common tell, and almost nobody talks about it.

AI video models love cinematic depth of field, the soft, dreamy, blurred-out background that makes a shot look produced. and that's exactly the problem. real UGC is filmed on a phone, in a bedroom or a car or a kitchen, and phone cameras hold most of the frame in focus. the background is usually sharp, or only naturally soft, not melted into creamy bokeh.

so when your AI clip has that beautiful blurred background, it doesn't read as "someone filmed this on their phone." it reads as "a camera crew made this," which is the exact opposite of UGC, and increasingly the exact thing that gets flagged as synthetic or inauthentic.

prompt against it directly. casual phone framing, background in focus, no artificial depth of field, no cinematic blur. this one change alone moves a clip from "ad" to "real," and it's the first thing i'd fix on anything that's getting clocked.

quick way to spot it: pause on any frame and look at the background. if it's smoothly melted into soft color the way a $2,000 camera with a fast lens would render it, that's the tell. real phone footage keeps the edges of objects behind the subject readable, you can still make out the doorframe, the shelf, the stuff on the counter. when the background is too pretty, it's too fake.

---

## Skin Texture Is the Whole Game on Faces

AI defaults to smooth, poreless, filtered skin. it's the fastest way to get a clip clocked as fake, because no real human face looks like that on a phone camera.

real skin has pores, slight unevenness, texture, the occasional blemish or redness. the imperfections are what make it read as real. a flawless face is a synthetic face.

the clause goes on every slide and every clip with a human in it, no exceptions:

> realistic skin texture, visible pores around the nose and cheeks, natural slight unevenness, no filter quality, no smoothing.

if you fix nothing else on the face, fix this. smooth skin is the tell that survives even when everything else is right.

---

## Lighting That Looks Like a Room, Not a Set

studio lighting gives it away. when the light is even, soft, and flattering from every direction, the brain reads "produced" instantly, because real life doesn't light you evenly from all sides.

in real footage, the light is directional and imperfect. one main source, usually a window or a lamp, casting natural shadows, with some unevenness across the face. that's what a real room looks like.

treat lighting as its own dedicated clause in the prompt, not something buried in a list:

> soft warm light from a window at left, natural shadows across the face, no harsh highlights, skin lit without overexposing.

lighting controls how real a clip feels more than almost any other variable. get it looking like an actual room and half the realism battle is already won.

---

## Watch the Motion and the Eyes

a clip can have a perfect still frame and still fall apart the second it moves. motion is where most AI video gets caught.

the tells to hunt for: dead eyes that don't focus or have any life in them, lip-sync drift where the mouth doesn't quite track the audio, floaty or too-smooth motion that no real person moves with, and robotic or repetitive gestures that loop unnaturally. these are exactly what a skeptical viewer catches, and exactly what a vision-based moderation system is built to catch.

worth knowing what each one looks like so you can spot it fast. dead eyes are the worst offender, the face is technically moving but there's nobody home behind the eyes, no micro-focus, no blinking rhythm that feels human.

lip-sync drift usually shows up at the start and end of sentences, where the mouth keeps moving a beat after the audio stops or starts late. floaty motion is the head and shoulders gliding instead of carrying the small natural shakes and weight changes a real person has. and looping gestures are the same hand movement repeating on a cycle, which the eye picks up even when it can't name it.

the fix is selection, not repair.

generate several versions of any clip with a person in it, and kill the ones with eye, sync, or motion problems instead of trying to salvage them. keep the one out of the batch that already moves right. a clip that's fighting you on motion is rarely worth saving when the next generation might just land clean.

---

## Anti-Polish: Casual, Not Produced

the overall vibe has to say someone filmed this on their phone, not a brand produced this.

that means casual framing, slightly off-center, not perfectly composed. a real environment, a room that looks lived in, with some clutter and normal background detail, not a clean staged set. and an organic, not studio feel across the whole thing.

a little imperfection is the entire point. the slightly crooked angle, the ordinary room, the framing that's a little off, those are what make it believable. polished is a tell. real life is a bit messy, and your AI UGC should be too.

> casual phone framing, real lived-in environment, not a professional set, organic not studio quality, slightly imperfect composition.

---

## Put Premium Rendering on Anything Getting Reach

here's a principle that matters more now than it used to: the more views a clip gets, the higher the realism bar it has to clear.

a clip that reaches 500 people can be decent and get away with it. a clip that's about to reach 500,000 is going to be scrutinized by thousands of skeptical viewers, and the more reach it gets, the more likely someone reports it or the moderation system takes a closer look. the small tells that slide by on a low-view clip get obvious at scale.

so your high-reach clips get the premium treatment. run Seedance 2.0 at $0.168/s on anything you're actually pushing, the proven winners getting real distribution or spend. premium rendering is what keeps a clip looking real on the 10th viewing, which is exactly when it matters, because that's when the eyes and the risk both pile up.

the routing logic stays the same as always: cheap models for the testing volume, premium for anything that's going to be seen a lot. you don't need every test clip to be flawless, you need every high-reach clip to be.

---

## QC Every Clip Before It Posts

at any real volume you can't eyeball every video, so the realism check has to be automated, or quality falls apart the moment you scale and one bad clip becomes the one that gets you flagged.

run every clip through a vision-capable model, Claude, or Fable 5 now that it's out and the vision is stronger, against a fixed checklist: does it pass the 2-second test, is the skin texture there, are the eyes alive, does the lip movement track, is there any fake blur, does the motion read natural. anything that fails gets flagged and regenerated with the prompt tightened at whatever broke. anything that passes ships.

this QC layer is the filter between your generation and your account. it's what makes sure the clip that goes live is the one that passes as real, not the one that quietly tanks your account integrity. at scale, this is the difference between a system that stays up and one that gets clapped.

the regeneration loop matters as much as the check itself. a flagged clip doesn't just get thrown out, it goes back through with the prompt adjusted at the specific thing that failed, fake blur gets the anti-blur clause reinforced, a plastic face gets the skin texture clause pushed harder, a motion problem gets a fresh batch to select from.

so the system isn't just catching bad clips, it's converting them into good ones automatically. and because the check is consistent every time instead of depending on whether a tired human caught it on review, the catch rate stays high across hundreds of clips a week, which is exactly where manual review falls apart.

---

## Stop Recycling, Instagram Is Specifically Watching for It

Instagram moved reach toward original creators and away from aggregators and recycled content. they've been clear about it, authenticity is the thing they're rewarding, and templated or automated-looking content is the thing they're pushing down.

so reposting the same video across accounts, or pumping out content that's obviously the same template with the words swapped, does 2 bad things at once. it gets you deprioritized in reach, and it makes your account look automated, which is exactly the footprint the moderation system flags.

the fix is real variation. unique content per account, genuinely different videos, not cosmetic reskins of one clip. when you produce winners and want to scale them, the variations have to actually differ, new angles, new cuts, new openings, not the same render with a new caption.

the volume's fine, the duplication is what kills you.

---

## The Honest Label Option

Instagram rolled out an optional AI creator label. it's voluntary, and turning it on doesn't reduce your reach, which makes it a legitimate compliance path rather than a penalty.

so in niches where the audience genuinely doesn't care that the content is AI, supplements for older demographics, plenty of practical product categories, running the label honestly is a clean, safe way to operate. the content still converts as long as the video itself is good, and you've taken the "is this hiding something" risk off the table entirely.

in the skeptical, younger, realism-obsessed niches, you lean on the realism checklist instead and let the content pass on its own merits.

the bigger point: the label existing at all means Meta is giving AI content a compliant lane to operate in, not trying to wipe it out. they're handing you a path to stay clean. use whichever version of it fits your niche.

---

## Realism Isn't Only the Video

your video can be flawless and you can still get banned on account behavior, so the realism has to cover the whole footprint, not just the pixels.

warm up new accounts before running them at volume. an account that's days old and suddenly posting at high frequency looks automated no matter how real the videos are. ramp it, profile and light engagement first, then build the posting volume over a few weeks.

don't add your link too early. slapping a link on while an account is blowing up is one of the classic triggers for a shadowban or an ID verification wall. wait until real traffic is actually flowing, a few hundred thousand views on the account, before you add links and start routing people off-platform.

post at a human cadence. stagger your posting times, don't publish across accounts at the same minute, don't behave in the patterns that scream coordinated network.

the account has to look like a real person ran it, the same way the video has to look like a real person filmed it. it's one continuous realism, and the weakest link is what gets you.

---

## Why This Is Actually an Edge

most guys are going to read about the ban wave and do one of 2 things, panic and stop, or ignore it and keep posting sloppy content until they get clapped. both of those clear out of your way.

the realism bar is a filter, and filters are good for whoever's on the right side of them. when the platform starts removing the content that doesn't pass, the content that does pass gets less competition for the same reach. the guys who build the realism discipline into their production now aren't just avoiding bans, they're inheriting the distribution that used to go to everyone posting obvious AI slop.

so the move isn't to fear the crackdown. it's to be the operation that's already producing content clean enough that the crackdown works in your favor.

## X Article Metadata

- Title: How to Make AI UGC So Realistic Meta Doesn't Ban You
- Preview: the bar for AI UGC just moved.
it used to be "does this look good."
now it's "does this look real enough that Meta's systems don't flag it and a skeptical viewer doesn't clock it in the first 2

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
