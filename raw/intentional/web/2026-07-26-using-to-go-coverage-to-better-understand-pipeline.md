---
type: raw_capture
source_type: web
title: "Using To-Go Coverage to Better Understand Pipeline"
url: "https://www.kellblog.com/using-to-go-coverage-to-better-understand-pipeline-and-improve-forecasting/"
collected_at: 2026-07-26T07:18:07Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Using To-Go Coverage to Better Understand Pipeline

Source: https://www.kellblog.com/using-to-go-coverage-to-better-understand-pipeline-and-improve-forecasting/

## Capture Text

Forecasting
Using To-Go Coverage to Better Understand Pipeline and Improve Forecasting
Dave Kellogg
29 Apr 2021
—
6 min read
Share
This is the second in a three-part series focused on forecasting and pipeline.  In
part I
, we examined
triangulation forecasts
with a detailed example.  In this, part II, we'll discuss to-go pipeline coverage, specifically using it in conjunction with what we covered in part I.  In part III, we'll look at this/next/all-quarter pipeline analysis as a simple way to see what's happening overall with your pipeline.
Pipeline coverage is a simple enough notion:  take the pipeline in play and divide it by the target and get a coverage ratio.  Most folks say it should be around 3.0, which isn't a bad rule of thumb.
Before diving in further, let's quickly remind ourselves of the definition of pipeline:
Pipeline for a period is the sum of the value of all opportunities with a close date in that period.
This begs questions around definitions for opportunity, value, and close date which I won't review here, but you can find discussed
here
.  The most common mistakes I see thinking about the pipeline are:
Turning 3.0x into a
self-fulfilling prophecy
by bludgeoning reps until they have 3.0x coverage, instead of using coverage as an unmanaged indicator
Not periodically scrubbing the pipeline according to a defined process and rules, deluding yourself into thinking "
we're always scrubbing the pipeline
" (which usually means you never are).
Applying hidden filters to the pipeline, such as "oh, sorry, when we say pipeline around here we mean stage-4+ pipeline."  Thus executives often don't even understand what they're analyzing and upstream stages turn into pipeline landfills full of junk opportunities that are left unmanaged.
Pausing sales hiring until the pipeline builds, effectively
confusing cause and effect
in how the pipeline gets built [1].
Creating opportunities with placeholder values that pollute the pipeline with fake news [1A], instead of creating them with $0 value until a salesrep socializes price with the customer [2].
Conflating
milestone-based and cohort-based
conversion rates in analyzing the pipeline.
Doing analysis primarily on either an annual or
rolling four-quarter pipeline
, instead of focusing first on this-quarter and next-quarter pipeline.
Judging the size of the all-quarter pipeline by looking at dollar value instead of
opportunity count
and
the distribution of oppties across reps
[2A].
In this post, I'll discuss another common mistake, which is not analyzing pipeline on a to-go basis within a quarter.
The idea is simple:
Many folks run around thinking, "we need 3.0x pipeline coverage at all times!"  This is ambiguous and begs the questions "of what?" and "when?" [3]
With a bit more rigor you can get people thinking, "we need to
start
the quarter with 3.0x pipeline coverage" which is not a bad rule of thumb.
With even a bit more rigor that you can get people thinking, "at all times during the quarter I'd like to have 3.0x coverage of what I have left to sell to hit plan." [4]
And that is the concept of to-go pipeline coverage [5].  Let's look at the spreadsheet in the prior post with a new to-go coverage block and see what else we can glean.
Looking at this, I observe:
We started this quarter with $12,500 in pipeline and a pretty healthy 3.2x coverage ratio.
We started last quarter in a tighter position at 2.8x and we are running behind plan on the year [6].
We have been bleeding off pipeline faster than we have been closing business.  To-go coverage has dropped from 3.2x to 2.2x during the first 9 weeks of the quarter.  Not good.  [7]
I can easily reverse engineer that we've sold only $750K in New ARR to date [8], which is also not good.
There was a big drop in the pipeline in week 3 which makes me start to wonder what the gray shading means.
The
gray shading
is there to remind us that sales management is supposed to
scrub the pipeline
in weeks 2, 5, and 8 so that the pipeline data presented in weeks 3, 6, and 9 is scrubbed.  The benefits of this are:
It eliminates the "
always scrubbing means never scrubbing"
problem.
It draws a deadline for how long sales has to clean up after the end of a quarter:  the end of week 2.  That's enough time to close out the quarter, take a few days rest, and then get back at it.
It provides a basis for snapshotting analytics.  Because pipeline conversion rates vary by week things can get confusing fast.  Thus, to keep it simple I base a lot of my pipeline metrics on week 3 snapshots (e.g., week 3 pipeline conversion rate) [9]
It provides an easy way to see if the scrub was actually done.  If the pipeline is flat in weeks 3, 6, and 9, I'm wondering if anyone is scrubbing anything.
It lets you see how dirty things got.  In this example, things were pretty dirty:  we bled off $3,275K in pipeline during the week 2 scrub which I would not be happy about.
Thus far, while this quarter is not looking good for SaaSCo, I can't tell what happened to all that pipeline and what that means for the future.  That's the subject of the
last post
in this three-part series.
A link to the spreadsheet I used in the example is
here
.
# # #
Notes
[1]  In enterprise SaaS at least, you should look at it the other way around:  you don't build pipeline and then hire reps to sell it, you hire reps and then they build the pipeline, as the linked post discusses.
[1A]  The same is true of close dates.  For example, if you create opportunities with a close date that is 18+ months out, they can always be moved into the more current pipeline.  If you create them 9 months out and automatically assign a $150K value to each, you can end up with a lot air (or fake news/data) in your pipeline.
[2]  For benchmarking purposes, this creates the need for "implied pipeline" which replaces the $0 with a segment-appropriate average sales price (ASP) as most people tend to create oppties with placeholder values.  I'd rather see the "real" pipeline and then inflate it to "implied pipeline" -- plus it's hard to know if $150K is assigned to an oppty as a placeholder that hasn't been changed or if that's the real value assigned by the salesrep.
[2A] If you create oppties with a placeholder value then dollar pipeline is a proxy for the oppty count, but a far less intuitive one -- e.g., how much dollar volume of pipeline can a rep handle?  Dunno.  How many oppties can they work on effectively at one time?  Maybe 15-20, tops.
[3] "Of what" meaning of what number?  If you're looking at all-quarters pipeline you may have oppties that are 4, 6, or 8+ quarters out (depending on your rules) and you most certainly don't have an operating plan number that you're trying to cover, nor is coverage even meaningful so far in advance.  "When" means when in the quarter?  3.0x plan coverage makes sense on day 1; it makes no sense on day 50.
[4] As it turns out, 3.0x to-go coverage is likely an excessively high bar as you get further into the quarter.  For example, by week 12, the only deals still forecast within the quarter should be very high quality.  So the rule of thumb is always 3.0x, but you can and should watch how it evolves at your firm as you get close to quarter's end.
[5]  In times when the forecast is materially different from the plan, separating the concepts of to-go to forecast and to-go to plan can be useful.  But, by default, to-go should mean to-go to plan.
[6] I know this from the extra columns presented in the screenshot from the same sheet in the previous post.  We started this quarter at 96% of the ARR plan and while the never explicitly lists our prior-quarter plan performance, it seems a safe guess.
[7]  If to-go coverage increases, we are closing business faster than we are losing it.  If to-go coverage decreases we are "losing" (broadly defined as slip, lost, no decision) business faster than we are closing it.  If the ratio remains constant we are closing business at the same ratio as we started the quarter at.
[8]  A good sheet will list this explicitly, but you can calculate it pretty fast.  If you have a pipeline of $7,000, a plan of $3,900, and coverage of 2.2x then:  7,000/2.2 (rounded) = 3,150 to go, with a plan of 3,900 means you have sold 750.
[9] An important metric that can be used as an
additional triangulation forecast
and is New ARR / Week 3 Pipeline.
