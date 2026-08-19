---
type: raw_capture
source_type: web
title: "What Pipeline Coverage Means with a 30-day Sales Cycle"
url: "https://www.kellblog.com/what-do-pipeline-coverage-and-forecast-mean-when-your-sales-cycle-is-30-days/"
collected_at: 2026-07-26T07:18:04Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# What Pipeline Coverage Means with a 30-day Sales Cycle

Source: https://www.kellblog.com/what-do-pipeline-coverage-and-forecast-mean-when-your-sales-cycle-is-30-days/

## Capture Text

Forecasting
What Do "Pipeline Coverage" and "Forecast" Mean When Your Sales Cycle is 30 Days?
Dave Kellogg
26 Jul 2023
—
7 min read
Share
layered sales fc featured
I grew up in enterprise.  I have already written a post on the tricky problem of
mapping one’s mindset from enterprise to velocity SaaS
, meaning smaller deals, shorter contract durations (e.g., month-to-month), and/or monthly-varying pricing [1].  That
post
was focused on what, if anything, “annual recurring revenue” (ARR) means such an environment, and how that impacts metrics that rely on ARR as part of their definition (e.g.,
CAC ratio
).
In this post, I’ll continue in the velocity SaaS direction by exploring short average sales cycles (ASC), as opposed to short contracts.  Specifically, what does it mean in short ASC companies when you discuss common concepts like
pipeline coverage
and the
sales forecast
?
Let’s demonstrate the problem.
In enterprise, quarterly pipeline (defined as the sum of the values of opportunities with a close date in the quarter) is somewhat intertwined the notion of long sales cycles.  Meaning that in a company with 9–12-month sales cycles, virtually every deal that has a chance of closing within the quarter is
already in the pipeline
at the start of the quarter.  Thus, you can meaningfully calculate “coverage” for the quarter by dividing the quarterly starting pipeline by the quarterly sales target.  Most sales VPs like a
3x ratio
[2].
Thus, the concept of pipeline coverage implicitly assumes a sales cycle (significantly) longer than the coverage period.  That’s why most companies don’t look at out-quarter pipeline coverage much (though
they should
) and if they do, they expect a much lower coverage ratio.
Now, let’s imagine an average sales cycle of 30 days and -- rather than futzing with cohorts, statistics, and distributions [3] -- let’s assume that all oppties are won or lost in
exactly
30 days [4].
In this scenario, at the start of the quarter, what is the pipeline coverage ratio?  It’s 1.0x.  Why?  We have zero pipeline for months 2 and 3 of the quarter.  If we assume that we have 3.0x coverage for month one and that the quarterly goal is evenly distributed across months, then we’d have 3.0x, 0.0x, and 0.0x for the three months of the quarter, or 1.0x overall [5].
In this example, quarterly pipeline coverage is basically
meaningless
because two-thirds of the pipeline you need to close during the quarter hasn’t been created yet
.  Assuming a 30-day
MQL
-to-opportunity lag, one-third is working its way through the high funnel and the other third is still a wink in marketing’s eye.
If quarterly pipeline coverage is basically meaningless in short ASC companies, then what
is
meaningful?
Examining monthly pipeline coverage. Instead of week-3 quarterly pipeline coverage [6], we should look at day-3 monthly pipeline coverage -- dividing the starting monthly pipeline by the monthly sales target.  (After that, you can use
to-go pipeline coverage
to get continuous insight.)
Treating months 2 and 3 the way you’d treat next-quarter and the quarter thereafter in enterprise. Using a
pipeline progression chart
to see how the out-month pipeline is shaping up.
Getting
marketing to forecast starting pipeline
for month 2 and month 3, based on what they have already generated in the high funnel and their current pipeline generation plans for month 2.
Inherent in my point of view is that the definition of “coverage” is based on opportunities that
already exist
in the pipeline. Call me untrusting, but somehow I can’t feel covered by something that hasn’t been created yet.  Some might define quarterly coverage in this environment using month 1 pipeline plus month 2 pipeline forecast and month 3 pipeline plan.  But to me, that’s not coverage.  And it’s objectively not the same thing as pipeline coverage when we use the term in enterprise.
Now, let’s zip back to reality for a minute.  In the velocity companies that I work with, ASC is closer to 60 days and with a pretty broad distribution where maybe 90% of the deals close within 30 and 120 days.  Happily, this means you will have month 2 and month 3 opportunities in the starting quarter pipeline, but it nevertheless also means you will be increasingly reliant on to-be-generated opportunities across the months of the quarter.
In this case, I would make a three-layer forecast:
Sales (from existing opportunities).  Forecast month 1, 2, and 3 sales using the normal sales forecasting process.
Marketing, from the high funnel.  Use existing MQLs and your standard conversion rates, ideally time-based
time-based
(not just the total rate, but the rate split by time period)
Marketing, from planned demandgen.  Forecast responses, then use standard conversion rates and ideally time-based.  (Ideally you can start with your
inverted funnel model
.)
This approach is preferable to looking only at pipeline generation (pipegen) because a pipegen approach:
Tends to ignore the oppties that are already there
Almost always ignores that
time-based nature of close rates
Uses an average sales price (ASP) as the proxy value for an opportunity [7].
In the example above you can clearly see how much of the forecast comes from existing opportunities (51%), how much from the existing high funnel (36%), and how much from planned demandgen activities (13%).
Finally, I have the same problem with the word "forecast" as I do with "coverage" in the short ASC world.   They're not quite the same thing as they are in enteprise.  First, let me define "forecast," along with its cousins, "plan" and "model."
The
plan
is about accountability. It’s what we signed up for and accountable to.  Budget is a synonym [8].
The
model
is a
driver-based model
of the business. It’s a calculated output (e.g., opportunities generated) given assumptions for a number of inputs and the way they interact (e.g., demandgen spend, MQLs generated, conversion rates).
The
forecast
is about prediction. It’s someone’s latest prediction for an output (e.g., bookings) given all available information at the time it’s made.
The plan is what we were willing to sign up for last December (when we received board approval).  The forecast is what we think is going to happen now.  We used models to help build the original plan and we can certainly
re-run those models
today using actuals as inputs to see what they produce.
In enterprise, the sales forecast is all about the deals in play.  What if Mike closes deals A, B, and either C or D.  The buyer at deal E promised me they’d give us the order.  Given everything we know about Sally’s deal F, what value do we think it will close at?  Sales VPs spend hours in Excel (or a modern forecasting tool like Clari) running scenarios to arrive a number.  It’s usually more about different combinations of deals than it is about probabilities and expected values.
In the velocity world, as discussed above, the forecast cannot be only about existing deals.  If you want to forecast a quarter, you'll need to include results from the high-funnel and planned demangen.  I'd still call it a forecast, but I'd know that it's not quite the same thing as a forecast in enterprise.  And by presenting in the three layers above, you can remind everyone of that.
# # #
Notes
[1] Monthly-varying SaaS is a different concept, which I used in that post, featuring short contracts (e.g., month-to-month) where the spend can vary every month, usually as the result of a flexible user-based pricing model, a consumption-based pricing model, or a hybrid pricing model (e.g., base + overage).  In such environments, simple SaaS concepts like ARR can quickly lose meaning, as do the metrics that rely on them (e.g., CAC ratio).
[2] Which I think had its ancient origins in the idea that you win 33%, lose 33%, and 33% slip.  (Thus assuming a 50% competitive win rate.)  Regardless of its roots, 3x (starting) coverage is a widely accepted norm, so much so that I fear it's often a
self-fufilling prophecy
.
[3] We’re ignoring the distribution of average sales cycle length for closed/won deals, its standard deviation, and the fact the three different outcomes (i.e., win, loss, slip) will likely have three different average opportunity cycle lengths (e.g., you usually lose faster than you win), each with its own distribution.
[4] And, most unrealistically, that deals never slip to a subsequent period.  We're also assuming that all opportunities are generated on the first day of month, an exactly 30-day lag from MQL to opportunity, and that all MQLs are generated on the first day of month, and convert in exactly 30 days.  (And, for the detail-oriented, that every month is 30 days.)  Overall, with these simplifying assumptions, you start every month with only the opportunities generated from MQLs generated the prior month and only those opportunities.  There is no leftover pipeline sloshing around to confuse things.
[5] The reality is likely somewhat less than 1.0x because we’d normally expected to some backloading ("linearity") of the quarterly target across the months of the quarter.  In enterprise, that backloading is severe (e.g., most enterprise cash models assume a 10/20/70 distribution).  In velocity SaaS, I've seen from 30/30/40 (i.e., pretty flat) to 10/20/70 (i.e., as backloaded as enterprise), typically reflecting a quarterly (as opposed to a monthly) sales cadence which is usually a mistake in a velocity model.
[6] To intelligently compare pipeline across quarters we need to fix a point in time to snapshot it.  In enterprise, I prefer day one of week three because it’s early enough to take actions (e.g., reducing expenses), but late enough so sales can no longer credibly claim they need more time for
pipeline cleanup (aka, scrubbing)
.
[7] In enterprise, this is a major sin because deal sizes vary significantly and values should be inserted only after discovery and price-point socialization (e.g., “you do know that this costs $150K?”)  In velocity, it’s a lesser sin because the deal sizes tend to be more similar.  Either way, if all we’re doing is counting opportunities and multiplying by a constant, then why not just admit it and count opportunities directly?  The more sophisticated the proxy, the more I like it (e.g., using $10K for SMB, $25K for MM, and $75K for ENT).
[8] Technically, I'd say budget is a synonym for the financial part of the plan.  That is, a budget is only one part of a plan.  A plan would also include strategic goals, objectives for attaining them, and organization structure.
