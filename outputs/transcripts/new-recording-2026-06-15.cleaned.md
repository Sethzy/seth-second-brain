# New Recording Transcript

- Source audio: `/Users/sethlim/Desktop/New Recording.m4a`
- Transcription model: `mlx-community/whisper-large-v3-turbo` via `mlx-whisper`
- Language hint: English / Singapore English
- Note: Raw TXT/SRT/VTT/TSV/JSON outputs are in the same folder. This cleaned copy removes empty segments and out-of-duration repeated outro artifacts only.

## Transcript

[00:00-00:02] I will be free.
[00:04-00:06] I will be back, but I should be okay.
[00:06-00:11] Okay, okay. Maybe just a quick call up just to find the specification and stuff.
[00:18-00:28] To structure other lines, map product, the inventory, ambiguity, generate, speed, disruptions, confirmation, trading, response.
[00:30-00:34] Transcript.
[00:50-00:52] You just want to dig on Kennedy, I think.
[00:52-00:55] It should be enough to visualize the...
[00:55-01:03] I mean, it's a accurate and very simplified version of what we went through with Mobin.
[01:03-01:05] Yeah, so I guess the...
[01:05-01:09] What I want to know is, if...
[01:09-01:11] Like, what is the complexity?
[01:11-01:14] And like, what do you really want?
[01:14-01:17] Because if you want to do a small slice, right, it's quite simple.
[01:17-01:21] If you want to do like a whole zheng ERP system, right, that's a different story.
[01:21-01:25] No, I don't think we'll be getting an ERP system for this.
[01:25-01:28] Because we'll be using our ERP system for a very long time, really.
[01:28-01:30] So everyone got you very used to this.
[01:30-01:32] I mean, I'm not saying that it shouldn't change.
[01:32-01:33] It should change.
[01:33-01:37] But I think it should be a ramp up from stage one.
[01:37-01:45] So instead of telling you what I need, right, I think you captured my pain points for the whole thing,
[01:45-01:51] which is that it is very time consuming, very tedious, very manual to think all this right now.
[01:51-01:56] So human, human reliance, prone to error and things like that, standard thing.
[01:56-02:00] So I want to make things easier for the night shift.
[02:00-02:03] I'm not cancelling the night shift job position permanently,
[02:03-02:08] because there are still like hotlines, hardlines, you know, coming through.
[02:08-02:14] But I want to simplify its workflow to make sure that whatever that's been captured and sent by our customers
[02:14-02:18] are accurate enough for the morning ops to draw the inventory.
[02:18-02:21] So that's the number one and most important thing.
[02:21-02:24] That is quite simple, to be honest.
[02:24-02:27] Like, I'm your bro, right? I'm not going to lie to you, right?
[02:27-02:29] It's actually quite simple.
[02:29-02:31] Like, most of it is WhatsApp, right?
[02:31-02:34] That's what, you know what, the handwriting, then tweet.
[02:34-02:36] Luckily, yeah, I can read.
[02:36-02:44] I mean, like, I don't think it is difficult to capture text.
[02:44-02:55] I think it's very difficult to capture, first of all, dialects, you know, accents, different mixture of singlish, you know, that kind of thing.
[02:55-02:58] And oversimplified all this.
[02:58-03:03] Like, I explained to Marvin, for example, you say, hey, I want pork, five kilos.
[03:03-03:04] I want to be very low, okay?
[03:04-03:07] But the pork, just that one more, right?
[03:07-03:11] It can be, like, hundreds of possibilities in our inventory.
[03:11-03:17] So I need to map whatever he says according to his historical data and what's in our system.
[03:17-03:19] That kind of thing.
[03:19-03:21] That is the difficult part.
[03:21-03:28] Okay, so, like, I guess, the dialect part, right, it shouldn't be too hard, okay?
[03:28-03:33] The hard part is, like, verifying against a source of truth to create, like, some sort of rule set.
[03:33-03:37] So that when something comes in, right, you validate whether it hits all the criteria.
[03:37-03:41] So, like, pork, weight, which exact pork, like, you know what I mean, right?
[03:41-03:44] Then the question is, like, where does that source of truth live?
[03:44-03:49] Because you can connect it to, once you have that source of truth somewhere, right?
[03:49-03:53] Once you pull that data into, you know, the LOM brain, right?
[03:53-03:56] Then you can actually validate the incoming with the rules.
[03:56-03:59] Then you say, like, fuck you, insufficient.
[03:59-04:00] I need more information, right?
[04:00-04:03] That's basically the triage that needs to happen, right?
[04:03-04:08] I, let's just do, like, a stupid man job, okay?
[04:08-04:13] I can provide you guys with the, for example, Murphy's ordering items.
[04:13-04:15] One to a hundred, okay?
[04:15-04:17] This is everything he's going to order.
[04:17-04:20] That's everything he's going to need for his daily ops, okay?
[04:20-04:26] I'm able to provide to you the whole list of items that our sales has confirmed with him.
[04:26-04:28] This is all the items that you need.
[04:28-04:33] So when he says something or when he inputs something, it can be matched.
[04:33-04:38] Yeah, and then the idea is that, like, is this a source of truth, right?
[04:38-04:40] Is it Excel, I guess?
[04:40-04:43] Or is it like a random PDF?
[04:43-04:44] Not really important, but I'm just kind of curious.
[04:44-04:46] And how often is it updated?
[04:48-04:50] That's the good question.
[04:50-04:53] So it is being updated in our ERP system.
[04:53-04:58] But our ERP system have a three-month validity of historical orders.
[04:58-05:03] So if you order this thing, like, on the 1st of January and you never order for three months,
[05:03-05:09] so from the 1st of April, it will be, like, pushed down, like, away, pushed away from the order history.
[05:09-05:10] Yeah.
[05:10-05:14] So I can generate, I hope I can.
[05:14-05:17] I'll call the IT site to double-check.
[05:17-05:19] I can generate that for you guys.
[05:19-05:27] But the most stupid way is to actually the product descriptions in the WhatsApp group itself.
[05:27-05:30] The WhatsApp group itself meaning, like…
[05:30-05:41] Like, usually our SOPs, whatever sales close with the customer, right, they will create a WhatsApp group from involving the ops, the finance, the customer, and sales, and blah, blah, blah.
[05:41-05:50] And the sales will actually input all the products, information, and specs inside the group chat description.
[05:50-05:53] So this is to check against…
[05:53-05:57] This is for the night shift guys to check against when they don't know what…
[05:57-05:58] Like, exactly what happened.
[05:58-05:59] Hey, pork.
[05:59-06:00] What pork?
[06:00-06:03] You know, then he will open up the group chat description and say,
[06:03-06:04] Oh, actually, he only…
[06:04-06:05] We order one kind of pork.
[06:05-06:08] Then you just write down that pork.
[06:08-06:10] But slowly and slowly, surely,
[06:10-06:14] He doesn't need that anymore because the moment he sees this customer, he knows already,
[06:14-06:16] Oh, this fucker, only the same thing again.
[06:16-06:18] But he just gonna say pork.
[06:18-06:20] Yup, yup, okay.
[06:20-06:22] So, I guess…
[06:22-06:25] So you have your description written.
[06:25-06:28] The WhatsApp group description doesn't get outdated, ah?
[06:28-06:29] Sometimes I guess you will…
[06:29-06:30] Oh…
[06:30-06:31] Yeah, go ahead.
[06:31-06:36] I mean, they will miss out, but it's the job of sales to keep on updating whenever there are changes.
[06:36-06:40] But usually there won't be significant updates to them.
[06:40-06:42] Oh, I would say 90% of the items.
[06:42-06:44] Only like miscellaneous.
[06:44-06:48] For example, like, oh, I actually have one pork belly, one cm.
[06:48-06:50] But, ah…
[06:50-06:52] Last month I ordered like…
[06:52-06:54] Well, I told you I confirmed like 0.1 cm.
[06:54-06:56] You know that kind of thing.
[06:56-06:57] Okay, okay.
[06:57-06:58] The nuance, ah?
[06:58-06:59] The…
[06:59-07:00] Yeah.
[07:00-07:01] So the pain is…
[07:01-07:02] The…
[07:02-07:03] In the day you don't have problems, ah?
[07:03-07:04] Is it?
[07:04-07:06] Because your staff is on duty, ah?
[07:06-07:07] Is that what I'm hearing?
[07:07-07:08] Yes, correct.
[07:08-07:09] So…
[07:09-07:10] So what I'm…
[07:10-07:12] Why the job gets easier in the daytime?
[07:12-07:13] Because when they are trying…
[07:13-07:15] For example, ah…
[07:15-07:16] Let's say Mervin plays a…
[07:16-07:19] Is a customer, plays an order at the night shift.
[07:19-07:21] He's supposed to order one cm thickness.
[07:21-07:22] Okay.
[07:22-07:23] But, ah…
[07:23-07:25] The night shift just wrote 0.1.
[07:25-07:26] Okay.
[07:26-07:31] So, in the daytime, I mean, when I'm keying in the order into my ERP system to generate an invoice,
[07:31-07:33] I was like, hey, cannot be.
[07:33-07:35] He has been ordering…
[07:35-07:41] The correct one, but he's now saying that he needs a 0.1.
[07:41-07:45] So, I will manual correct, or I will go and check with the customer.
[07:45-07:46] Hey, you yesterday ordered 0.1, is it?
[07:46-07:47] But you are actually…
[07:47-07:48] What you've been ordering for months, ah?
[07:48-07:49] It's 1 cm.
[07:49-07:50] That kind of thing.
[07:50-07:54] So, this mistake goes away with the double authentication.
[07:54-07:55] With your staff, lah?
[07:55-07:56] Yes.
[07:56-07:57] And all the…
[07:57-07:58] All the history.
[07:58-08:03] When they check, hey, the order history don't have, you know, this spec.
[08:03-08:04] So, they will check.
[08:04-08:06] They will message, they will call.
[08:06-08:07] Okay, okay.
[08:07-08:08] So, I mean, the…
[08:08-08:09] The only…
[08:09-08:11] The thing that it hinges on, right?
[08:11-08:12] Is your ERP is built by who?
[08:12-08:14] I know you use some dev shop in India, right?
[08:14-08:16] That's what I last remember.
[08:16-08:17] Yup.
[08:17-08:19] Then, there's the ERP API.
[08:19-08:20] No, right?
[08:20-08:21] It's a…
[08:21-08:23] I guess you can only export, right?
[08:23-08:24] Uh…
[08:24-08:25] I…
[08:25-08:26] A…
[08:26-08:27] I…
[08:27-08:29] Think can export.
[08:29-08:30] But because…
[08:30-08:31] Oh, yeah.
[08:31-08:33] One of the thing is that, you know, this kind of, like…
[08:33-08:34] They show in India.
[08:34-08:38] When you are adding something to the system built by them, right?
[08:38-08:39] It's easy.
[08:39-08:40] Because they…
[08:40-08:41] They want to earn that money, man.
[08:41-08:42] So, when you…
[08:42-08:45] Get a third party to try to add something to…
[08:45-08:49] What they have done, and they are not earning the money, they create a lot of problems.
[08:49-08:50] For…
[08:50-08:51] For everyone.
[08:51-08:55] He, this cannot, that cannot, wrong data, you know, push wrong, pull wrong, you know, that…
[08:55-08:56] That kind of shit.
[08:56-08:57] So, we tried a few times, then…
[08:57-08:58] All failed because of this.
[08:58-08:59] Yeah, yeah.
[08:59-09:00] Makes sense.
[09:00-09:01] So, actually…
[09:01-09:02] Cooling data shouldn't be an issue.
[09:02-09:03] Yeah, but you want to take the stupidest version, right?
[09:03-09:04] That will solve your problem, right?
[09:04-09:05] Is that, you just export whatever.
[09:05-09:06] Like, you SKU lists, right?
[09:06-09:07] And then, uh…
[09:07-09:20] Like, if you can export the order history of the customer, it would be even better,
[09:20-09:21] but I guess it's optional.
[09:21-09:27] Then you just match that with the WhatsApp order that comes in, right?
[09:27-09:31] And then, if you can have the order history exported as well, you just match that with…
[09:31-09:34] And then flag any discrepancy and say like, okay, how come most of the time it's like this,
[09:34-09:35] then now this is different.
[09:35-09:41] Then you just flag it as like, oh, you should probably look out for this because it's…
[09:41-09:46] Firstly, uh, doesn't fit any of the SKUs that we have listed, and secondly, or it doesn't
[09:46-09:49] fit the pass order experience that we had with this client.
[09:49-09:53] Then your day shift will just come in and report saying like, okay, fuck, WhatsApp came
[09:53-09:57] in last night, but we flagged these two things and then can you go chase?
[09:57-10:00] But the rest of it should be, if it's all clear, right, it can be a straight-through pass
[10:00-10:01] la.
[10:01-10:02] Does that make sense?
[10:02-10:03] Yes.
[10:03-10:04] Yes.
[10:04-10:05] That can be one of the…
[10:05-10:08] I mean, that's the ideal situation.
[10:08-10:16] So, I'm not sure how physical is this, but maybe you can request for like, weekly pooling
[10:16-10:22] of data from my current ERP system to sync with whatever that you guys are doing, the
[10:22-10:23] order histories.
[10:23-10:30] So, I don't need to be like daily update because I don't know how strenuous it is on the cloud
[10:30-10:32] and servers and things like that.
[10:32-10:39] But, I think weekly or something like that, once in a fortnight, pooling data just to
[10:39-10:44] double, just to update, would be nice also.
[10:44-10:46] Yeah, and there are two ways to do it, right?
[10:46-10:48] One is like, you can do the dummy way, right?
[10:48-10:52] Which is that if your ERP has a big export button, which is export everything, and you
[10:52-10:56] just store everything in like, literally a container in the cloud, right?
[10:56-11:01] And then I can just pull from there, and then once you export again, then you override that
[11:01-11:02] one, you know what I mean?
[11:02-11:03] That's the manual way, right?
[11:03-11:06] But if you want to get fancy, you can do automatic pull, but I don't think it's necessary.
[11:06-11:09] If you're saying weekly basis, then it's, you know what I mean?
[11:09-11:14] You just click one button once a week, then everything comes out, and just pull from there.
[11:14-11:15] You know what I mean?
[11:15-11:18] That's like the real MVP sort of…
[11:18-11:19] Yeah.
[11:19-11:20] Yeah.
[11:20-11:22] Then it's not that deep, you know what I mean?
[11:22-11:26] Then you actually, what you really need to solve is the WhatsApp automation layer.
[11:26-11:29] How about this way?
[11:29-11:39] When you guys are building or designing this, give me like, like access to modify the order
[11:39-11:43] history within your app itself.
[11:43-11:49] So that for example, if this, suddenly I need, I don't know if I need, I need donkey, okay?
[11:49-11:52] I need donkey meat today and see something new.
[11:52-11:56] But when they try to order today, they won't be able to see from the order history because
[11:56-11:58] that will be the first time that they are doing that.
[11:58-12:04] So when this kind of thing happened, I can only imagine is that, okay, I will let my guys, okay,
[12:04-12:11] can you go to whatever that you guys are building, just input donkey, you know, as create like a,
[12:11-12:15] like a pseudo order history like that so that it's able to capture.
[12:15-12:16] Yeah.
[12:16-12:18] Why would donkey come up?
[12:18-12:22] I mean, we brought in new products, okay?
[12:22-12:25] First wave, like the, like the pig's blood, okay?
[12:25-12:28] It just came to Singapore literally just weeks.
[12:28-12:30] So a lot of customers are new to this.
[12:30-12:33] They are starting their first order as pig's blood, new.
[12:33-12:39] Then when they order and they didn't sink in time with my ERP system or whichever cloud,
[12:39-12:42] then it creates a big jam, right?
[12:42-12:43] I suppose.
[12:43-12:44] But these are exceptions, right?
[12:44-12:45] These are not the rule, right?
[12:45-12:47] They're not going to be super frequent, right?
[12:47-12:48] Yeah.
[12:48-12:58] I mean, with a daily order of 200 something, I'm not sure how many new items are being discussed
[12:58-13:00] every day, you know, that's the thing.
[13:00-13:01] Yeah, yeah.
[13:01-13:04] So the, the, I mean, the way you can think of it, right, is that you, what you want to do
[13:04-13:06] is first cut all the bulk volume first.
[13:06-13:07] You don't want a perfect solution, right?
[13:07-13:10] You cut the 250 standard things first.
[13:10-13:12] Then you show the 50 things.
[13:12-13:13] I don't know what the ratio is, right?
[13:13-13:16] And say like, okay, for now we'll do a manual.
[13:16-13:18] I mean, you still need some guy in the morning to check it, right?
[13:18-13:20] You still have someone doing the night shift.
[13:20-13:21] You say you're not going to fire the guy, right?
[13:21-13:26] So the guy can handle the exceptions, but at least he knows like the bulk stuff is being
[13:26-13:27] cleared, right?
[13:27-13:31] And then the, the exceptions can be cleared manually, right?
[13:31-13:34] Then that's the, that's the V1, the, the bare minimum.
[13:34-13:35] Then actually that's the most lift.
[13:35-13:37] You'll solve a lot of pain with that, right?
[13:37-13:42] Then you can slowly turn the system to sort of, you know, take the exceptions and start solving
[13:42-13:44] them one by one, right?
[13:44-13:45] And then there's more work.
[13:45-13:49] But if you want to do like, let's say you want to solve the problem today, it's not that
[13:49-13:50] hard, right?
[13:50-13:54] And I think why I always think, yeah, just solve the big problem first, then you just
[13:54-13:55] follow the stuff.
[13:55-13:56] You can just clear up after that, right?
[13:56-13:57] One by one.
[13:57-13:58] You know what I mean, right?
[13:58-13:59] Yeah.
[13:59-14:02] And I guess like the big problem is really that you have how many WhatsApp groups?
[14:02-14:03] Like 200, 300?
[14:03-14:04] Like thousands.
[14:04-14:05] Huh?
[14:05-14:06] Say again?
[14:06-14:07] Thousands.
[14:07-14:08] Thousands, right?
[14:08-14:09] Yeah.
[14:09-14:12] So the hard part is actually tracking the thousands of WhatsApp and figuring out like what the hell
[14:12-14:17] is coming in every night, making sure that everything is like, like the stuff that is easily
[14:17-14:18] solved is solved, right?
[14:18-14:19] Then I think 80% of your pain will go away.
[14:19-14:20] No?
[14:20-14:21] Yes.
[14:21-14:33] So I think what I can try to map out on my end is actually the export API from my current
[14:33-14:34] ERP system.
[14:34-14:43] So I'll generate, I'll ask the team to try to generate customer names with address with order
[14:43-14:44] history.
[14:44-14:45] Yeah.
[14:45-14:46] That'll be perfect.
[14:46-14:47] Then SKU list, right?
[14:47-14:48] Yeah.
[14:48-14:49] Pack them together.
[14:49-14:50] Yeah.
[14:50-14:51] You pack them together into one single source of truth, right?
[14:51-14:52] And this can be synced weekly for now, right?
[14:52-14:57] We can always move it to daily in future because if your dev shop in India is like anywhere close
[14:57-14:58] to being competent, right?
[14:58-14:59] They can get this done in five minutes, I think.
[14:59-15:00] But let's just do weekly first because like don't talk to them, right?
[15:00-15:01] You really know how it's going to go, right?
[15:01-15:02] You do that weekly.
[15:02-15:03] Once you have that, then what I can do for you is your thousand WhatsApp groups, everything,
[15:03-15:04] whenever the message comes in, right?
[15:04-15:05] You automatically cross references that source of truth, right?
[15:05-15:12] And it comes up with a preliminary answer, which says that, okay, based on the rules that you
[15:12-15:16] say, this order is missing information or it is fucking an exception.
[15:16-15:17] It's not in the sink right now, in the source of truth, right?
[15:17-15:26] But these two things will reflect for either the person, you can also automate the back
[15:26-15:31] and forth, but for now it will reflect to a person and the person will just go to the
[15:31-15:33] guy and say, hey, bro, you're already missing something, bro.
[15:33-15:34] You're already missing something, bro.
[15:34-15:35] You're already missing something, right?
[15:35-15:36] You're already missing something, right?
[15:36-15:37] You're already missing something, right?
[15:37-15:38] You're already missing something, right?
[15:38-15:39] You're already missing something, right?
[15:39-15:40] You're already missing something, right?
[15:40-15:41] You're already missing something, right?
[15:41-15:42] You're missing something, right?
[15:42-15:43] You're missing something, right?
[15:43-15:44] You're missing something, right?
[15:44-15:45] You're already missing something, right?
[15:45-15:46] You're already missing something, right?
[15:46-15:47] You're already missing something, right?
[15:47-15:48] You're already missing something, right?
[15:48-15:49] You're missing something, right?
[15:49-15:52] And with an exception, then the person will just take over and check the ERP manually and
[15:52-15:55] say like, okay, actually, we actually do have this order.
[15:55-15:56] Does it make sense?
[15:56-16:01] Then the bulk cases will be cleared and your team should be quite happy with that.
[16:01-16:05] That's usually how it goes with, I mean, I've done this a few times already, but you
[16:05-16:07] don't try to solve the whole thing at once, you know?
[16:07-16:08] You kill yourself off.
[16:08-16:09] Yeah.
[16:09-16:13] So actually from the WhatsApp side of things, right, it's quite straightforward.
[16:13-16:14] I know how to do it, right?
[16:14-16:18] And then if you sync everything into an Excel for now, right, it's actually probably good
[16:18-16:19] enough.
[16:19-16:20] You don't need to build a fancy dashboard.
[16:20-16:23] I mean, you can, but I don't think it's necessary.
[16:23-16:25] Just put it in an Excel nicely, right?
[16:25-16:27] Everyday you get one sheet, right?
[16:27-16:30] And the sheet will be color coded with like, okay, this is fucked up.
[16:30-16:31] This is not fucked up.
[16:31-16:32] Can't really.
[16:32-16:33] Can't really.
[16:33-16:34] That's one thing, right?
[16:34-16:35] Then it's printable.
[16:35-16:36] Second.
[16:36-16:41] So I do have some requirements on the format.
[16:41-16:44] First of all, it needs to be a printable thing.
[16:44-16:45] All right.
[16:45-16:48] So because after it's being segregated into different routes and things like that, right,
[16:48-16:53] they need to print this shit out and hand over to the inventory team for them to draw
[16:53-16:57] according to the list, according to the sequence of the jobs.
[16:57-16:58] Okay.
[16:58-16:59] This is point number one.
[16:59-17:04] Second, there are certain format I want it to be printed.
[17:04-17:09] For example, like how much space actually you should leave behind every line.
[17:09-17:12] What's the spacing on all these items?
[17:12-17:15] They're very miscellaneous, small, small things, but this is something that actually
[17:15-17:19] is quite important and critical in my operation.
[17:19-17:20] Okay.
[17:20-17:22] This one, 100% can be done.
[17:22-17:24] All I need, okay, what format is it?
[17:24-17:26] PDF or is it a, what do you normally print?
[17:26-17:27] I need a Word Dog.
[17:27-17:28] PDF.
[17:28-17:30] PDF would be okay.
[17:30-17:31] Yup.
[17:31-17:32] Yup.
[17:32-17:35] And then all the exact specifications, the minutiae, right, can be done because like,
[17:35-17:40] you can think of it as like, when you use a computer to do it, everything becomes guaranteed
[17:40-17:41] formatting, right?
[17:41-17:43] You know, human beings make mistakes formatting, right?
[17:43-17:44] Computers don't, because it's rule-based.
[17:44-17:45] You know what I mean?
[17:45-17:48] You write a script and the script will always put it in this format, right?
[17:48-17:53] So the key part here is like, firstly, you need to show me one example, right?
[17:53-17:58] Then I will infer all the formatting that you want and I confirm with you.
[17:58-18:04] And after that, you should always be shut out in the same way every single time in any format
[18:04-18:05] you want.
[18:05-18:09] Because turning Excel into anything is a trivial task, but let's put it this way.
[18:09-18:10] Yeah.
[18:10-18:11] Let me show you something.
[18:11-18:12] Sure.
[18:12-18:13] It should be something like that.
[18:13-18:14] You sign on what?
[18:14-18:15] What's that?
[18:15-18:16] Oh, Tele.
[18:16-18:17] Tele, you say.
[18:17-18:18] Yeah, yeah, yeah, yeah.
[18:18-18:19] No, no, no, no.
[18:19-18:20] But, so how do you normally do this today actually?
[18:20-18:21] That's what I'm curious about.
[18:21-18:37] Because this is actually a prototype from the current, current, current, current, current
[18:37-18:38] IT company.
[18:38-18:45] But we do face a lot of resistance because it's all built in one from ordering all the
[18:45-18:48] way until inventory drawing.
[18:48-18:55] So, but the tricky part is that the customer needs to access to links and passwords and things
[18:55-18:56] like that.
[18:56-19:00] So, a lot of these fuckers are just too lazy to operate on their own.
[19:00-19:02] So, this just dies off.
[19:02-19:05] So, what we are doing now is physical writing.
[19:05-19:12] Like when they take call and take message, they are physically writing items on the list.
[19:12-19:15] Oh, but you, you, the one you sent me is not written, right?
[19:15-19:16] It's printed, right?
[19:16-19:17] This is, this is printed.
[19:17-19:18] This is printed.
[19:18-19:21] Which is the prototype that we are not using.
[19:21-19:22] Oh, okay, okay, okay.
[19:22-19:23] And why are you not using it?
[19:23-19:24] It's because the...
[19:24-19:27] Because, if you try a...
[19:27-19:29] For example, me and Movin are two different customers.
[19:29-19:35] Each of us will have a different unique link for us to access, to place orders.
[19:35-19:38] They need to go into the link and place orders.
[19:38-19:40] But, they are too lazy to do that.
[19:40-19:45] They just want to send like a voice message to make their job easier and make our job hard.
[19:45-19:48] So, that's the, that's the g's of it.
[19:48-19:50] Okay, voice message also can do actually.
[19:50-19:51] That one is under the...
[19:51-19:52] Anything WhatsApp input, right?
[19:52-19:53] Is solvable basically.
[19:53-19:54] As long as it comes in...
[19:54-19:55] WeChat?
[19:55-19:56] WeChat, I'll log into it.
[19:56-19:57] How, how much of it is WeChat?
[19:57-20:01] About WhatsApp, I know, weChat can be done, but I need to go research.
[20:01-20:02] It's the same idea.
[20:02-20:03] You know what I mean?
[20:03-20:05] You, you get the file format.
[20:05-20:06] I think.
[20:06-20:07] Yeah.
[20:07-20:08] But what's the ratio?
[20:08-20:12] I think I would say like a 50-50 or 60 on WeChat, 40 on WhatsApp.
[20:12-20:13] Okay, now I know WeChat.
[20:13-20:16] WeChat confirm that China API is very good one.
[20:16-20:21] WhatsApp is the one that is normally a headache because they are quite anti-automation.
[20:21-20:22] I don't know if you...
[20:22-20:23] Yeah, anyway.
[20:23-20:25] But long story short, both can be done.
[20:25-20:26] It's not a guarantee you, right?
[20:26-20:30] But then, I guess the idea is that you want this form filled up, just without...
[20:30-20:31] Yes.
[20:31-20:35] But then, but in that case, then do you need the password link or all that crap?
[20:35-20:36] No need, right?
[20:36-20:37] No need, no need, no need, no need.
[20:37-20:41] This one is, is, is, is, it need to be plugged into the phone, right?
[20:41-20:45] Or somehow connected to a phone number that we're using.
[20:45-20:50] Or the number, or whichever WhatsApp WeChat account that we need to be linked up.
[20:50-20:53] So, I don't need the customer to access the system.
[20:53-20:56] It's just like auto-capture and generates on the back end.
[20:56-20:58] That, that should do the job.
[20:58-21:03] Okay, then, then like a super simple flow would just be, WhatsApp comes in, right?
[21:03-21:05] You get shared into an Excel sheet.
[21:05-21:07] Your team approves.
[21:07-21:11] Once they approve, it gets shared into a PDF in this format.
[21:11-21:12] Yeah?
[21:12-21:16] That, that would be the, the most basic, you know, without over-engineering or overthinking it, right?
[21:16-21:18] That would probably solve the problem, right?
[21:18-21:19] Yeah.
[21:19-21:22] Then you would just get a very clean PDF in.
[21:22-21:24] I assume you have a template, right?
[21:24-21:25] Just give me a template, though.
[21:25-21:26] Yeah.
[21:26-21:27] And then some examples.
[21:27-21:29] And then, I think that's the entire scope, right?
[21:29-21:30] Yeah.
[21:30-21:32] Cause, I don't know why I even quote you 100K, right?
[21:32-21:35] But that, that is, dude, this is, this is not like that deep, you know what I mean?
[21:35-21:38] It's, if you solve the problem, it's not that deep.
[21:38-21:40] But if you want to go on to expand beyond this, right?
[21:40-21:41] Then it'll be a lot harder, la.
[21:41-21:42] It doesn't make sense, right?
[21:42-21:43] Yeah, bro, it's not code, la.
[21:43-21:45] Because I think you want to do something fancy.
[21:45-21:46] You want to create a platform, la.
[21:46-21:47] Yeah.
[21:47-21:48] So, I mean, these three things, right?
[21:48-21:49] One, what's that in?
[21:49-21:52] Verify against your source of truth, which is the export on a weekly basis of both the
[21:52-21:54] SKU inventory and the customer history, right?
[21:54-21:55] Excel will flag the things that are exceptions.
[21:55-21:58] So, either missing information from the order that is not matching with the SKU, or weird shit
[21:58-21:59] that comes up that doesn't match with the order history.
[21:59-22:00] And then exceptions, which is your blood meat, or your pig blood, right?
[22:00-22:01] That one will just come up as like, okay, not identified.
[22:01-22:02] Then your team will manually do it.
[22:02-22:03] Then once they clean up in the morning, they will just review the Excel.
[22:03-22:06] Then basically they click a button and then it will shit up the correct invoices and
[22:06-22:07] then you can take it from there.
[22:07-22:08] Right?
[22:08-22:09] The correct PDF.
[22:09-22:10] I think that's the flow, right?
[22:10-22:11] Yes, correct.
[22:11-22:12] Okay.
[22:12-22:13] I think that's the flow, right?
[22:13-22:14] Yes, correct.
[22:14-22:15] Okay.
[22:15-22:16] Okay.
[22:16-22:17] Okay.
[22:17-22:18] Okay.
[22:18-22:19] Okay.
[22:19-22:20] Okay.
[22:20-22:21] Okay.
[22:21-22:22] Okay.
[22:22-22:23] Okay.
[22:23-22:24] Okay.
[22:24-22:25] Okay.
[22:25-22:26] Okay.
[22:26-22:27] Okay.
[22:27-22:28] Okay.
[22:28-22:29] Okay.
[22:29-22:30] Okay.
[22:30-22:31] Okay.
[22:31-22:32] Okay.
[22:32-22:33] Okay.
[22:33-22:34] Okay.
[22:34-22:35] Okay.
[22:35-22:36] Okay.
[22:36-22:37] Okay.
[22:37-22:38] Okay.
[22:38-22:39] Okay.
[22:39-22:40] Okay.
[22:40-22:41] Okay.
[22:41-22:42] Okay.
[22:42-22:43] Okay.
[22:43-22:44] Okay.
[22:44-22:45] Okay.
[22:45-22:46] Okay.
[22:46-22:47] Okay.
[22:47-22:48] Okay.
[22:48-22:49] Okay.
[22:49-22:50] Okay.
[22:50-22:51] Okay.
[22:51-22:52] Okay.
[22:52-22:53] Okay.
[22:53-22:54] Okay.
[22:54-22:55] Okay.
[22:55-22:56] Okay.
[22:56-22:57] Okay.
[22:57-22:58] Okay.
[22:58-22:59] Okay.
[22:59-23:00] Okay.
[23:00-23:01] Okay.
[23:01-23:02] Okay.
[23:02-23:03] Okay.
[23:03-23:04] Okay.
[23:04-23:05] Okay.
[23:05-23:06] Okay.
[23:06-23:07] Okay.
[23:07-23:08] Okay.
[23:08-23:09] Okay.
[23:09-23:10] Okay.
[23:10-23:11] Okay.
[23:11-23:12] Okay.
[23:12-23:13] Okay.
[23:13-23:14] Okay.
[23:14-23:15] Okay.
[23:15-23:16] Okay.
[23:16-23:17] Okay.
[23:17-23:18] Okay.
[23:18-23:19] Okay.
[23:19-23:20] Okay.
[23:20-23:21] Okay.
[23:21-23:22] Okay.
[23:22-23:23] Okay.
[23:23-23:24] Okay.
[23:24-23:25] Okay.
[23:25-23:26] Okay.
[23:26-23:27] Okay.
[23:27-23:28] Okay.
[23:28-23:29] Okay.
[23:29-23:30] Okay.
[23:30-23:31] Okay.
[23:31-23:32] Okay.
[23:32-23:33] Okay.
[23:33-23:34] Okay.
[23:34-23:35] Okay.
[23:35-23:36] Okay.
[23:36-23:37] Okay.
[23:37-23:38] Okay.
[23:38-23:39] Okay.
[23:39-23:40] Okay.
[23:40-23:41] Okay.
[23:41-23:42] Okay.
[23:42-23:43] Okay.
[23:43-23:44] Okay.
[23:44-23:45] Okay.
[23:45-23:46] Okay.
[23:46-23:47] Okay.
[23:47-23:48] Okay.
[23:48-23:49] Okay.
[23:49-23:50] Okay.
[23:50-23:51] Okay.
[23:51-23:52] Okay.
[23:52-23:53] Okay.
[23:53-23:54] Okay.
[23:54-23:55] Okay.
[23:55-23:56] Okay.
[23:56-23:57] Okay.
[23:57-23:58] Okay.
[23:58-23:59] Okay.
[23:59-24:00] Okay.
[24:00-24:01] Okay.
[24:01-24:02] Okay.
[24:02-24:03] Okay.
[24:03-24:04] Okay.
[24:04-24:05] Okay.
[24:05-24:06] Okay.
[24:06-24:07] Okay.
[24:07-24:08] Okay.
[24:08-24:09] Okay.
[24:09-24:10] Okay.
[24:10-24:11] Okay.
[24:11-24:12] Okay.
[24:12-24:13] Okay.
[24:13-24:14] Okay.
[24:14-24:15] Okay.
[24:15-24:16] Okay.
[24:16-24:17] Okay.
[24:17-24:18] Okay.
[24:18-24:19] Okay.
[24:19-24:20] Okay.
[24:20-24:21] Okay.
[24:21-24:22] Okay.
[24:22-24:23] Okay.
[24:23-24:24] Okay.
[24:24-24:25] Okay.
[24:25-24:26] Okay.
[24:26-24:27] Okay.
[24:27-24:28] Okay.
[24:28-24:29] Okay.
[24:29-24:30] Okay.
[24:30-24:31] Okay.
[24:31-24:32] Okay.
[24:32-24:33] Okay.
[24:33-24:34] Okay.
[24:34-24:40] So if you give me two kilos of donkey, two kilos of horsey, you know, that kind of thing.
[24:40-24:41] Okay.
[24:41-24:42] Okay.
[24:42-24:43] Horsey.
[24:43-24:44] Okay.
[24:44-24:45] Then you'll be like, what the fuck is a horsey?
[24:45-24:50] So are you able to give me a prompt back to the customer and say, can you clarify what's
[24:50-24:51] !
[24:51-24:54] That thing that you're asking if it doesn't really understand instead of just capturing
[24:54-24:55] and interpreting it on its own.
[24:55-24:56] Yeah.
[24:56-24:57] So I think two things can add, right?
[24:57-24:58] Which is quite simple.
[24:58-25:02] One is that for every order that is captured, we will include the verbatism.
[25:02-25:07] The verbatim transcript or the, what was said.
[25:07-25:08] You know what I mean?
[25:08-25:10] Next to the Excel sheet, you know, in the Excel sheet, there are columns, right?
[25:10-25:11] We'll put in the order.
[25:11-25:14] Then we'll put in the verbatim so that your team can easily scan and say like, oh, actually,
[25:14-25:17] this was the verbatim, right?
[25:17-25:22] Then we can also put the clarifying prompt next to it so that your team can manually feedback.
[25:22-25:26] You can automate this but like, it's not worth it until you see the volume, I guess.
[25:26-25:31] If there's a lot of errors, then you can start saying like, okay, then we want to make a back and forth automation, right?
[25:31-25:32] But, you know what I mean?
[25:32-25:40] I think it would be better for example, I give you like, for example, I ordered 10 items on the list, right?
[25:40-25:42] Then, all done, okay?
[25:42-25:47] Your system captures everything, register everything linked up with the history and blah, blah, blah.
[25:47-25:49] Send a confirmation response.
[25:49-25:51] This is what you ordered.
[25:51-25:54] Then, that's also doable.
[25:54-25:59] Yeah, that will actually eliminate a lot of the back end issues in the morning as well.
[25:59-26:04] So the customer confirms, confirms, like, okay, you confirm really then, like, don't talk about it when it's wrong.
[26:04-26:08] So I think this will help with the whole flow as well.
[26:08-26:17] So basically like a order place, locks in the sheet, sends confirmation in a nice bullet point saying like, you ordered this, this, this, this, this, right?
[26:17-26:23] And then, yeah, with the correct, with the correct decision from my system.
[26:23-26:31] For example, they just say, POC, I'll say, okay, from, is this, POC automatically generate the confirmation, POC barely wants CM cut.
[26:31-26:32] Okay, something like that.
[26:32-26:33] I see.
[26:33-26:34] Okay, okay.
[26:34-26:40] Then, then the only question is like, do you want your team to review first or do you want to automatically send the confirmation?
[26:40-26:42] That's the, they still need to review.
[26:42-26:47] They still need to review, but they, you need to double confirm with the customer.
[26:47-26:51] So sometimes it's like, oh, no, no, no, no, actually I don't want the 1 CM, I changed my mind.
[26:51-26:53] I need 1.5 today.
[26:53-26:54] You know, that kind of thing.
[26:54-26:59] So, but when they see the confirmation, they actually know what they ordered and what they, whichever they said.
[26:59-27:00] I see, I see.
[27:00-27:03] But like, as in, my point is like, you know, the order comes in, right?
[27:03-27:11] Do you want to automatically immediately confirm or do you want to let your team wake up in the morning, check through, and then send the confirmation message if they approve?
[27:11-27:16] Actually, in my operation, this, the moment they place order and my team checks through is confirmed already.
[27:16-27:24] So the really, really confirmation stage, confirm and nail is when they issue invoice, which is the second step of confirmation.
[27:24-27:34] So the first confirmation, I'll put it as a soft confirmation to the customer that we are, we capture your order as such, but this is not what you'll be getting.
[27:34-27:36] For example, some item may be out of stock.
[27:36-27:38] Some item may be missing.
[27:38-27:40] So it's like an auto confirmation.
[27:40-27:44] So the moment they place, they will get a, this is the order that you confirmed.
[27:44-27:46] My team will let you know.
[27:46-27:52] That is the message that we send, immediately after they send something, the customer order something, right?
[27:52-27:54] Yeah, let them check first.
[27:54-27:55] Got it.
[27:55-27:58] Then your team can look at the spreadsheet in the morning and double confirm.
[27:58-27:59] Yes.
[27:59-28:01] Okay, that's just a straight forward.
[28:01-28:03] Because that one will be no risk, you know what I mean?
[28:03-28:04] Because it's just a...
[28:04-28:05] Yeah.
[28:05-28:08] Yeah, okay, okay, makes sense, makes sense.
[28:09-28:10] Yeah.
[28:10-28:11] Yeah.
[28:11-28:12] So yeah, la.
[28:12-28:14] Fuck la, this is giving me a lot of feedback.
[28:14-28:17] Actually why la, is it, is it so much volume is it, or is it like...
[28:17-28:23] Yeah, the, uh, first of all, training a night shift fucker is not easy.
[28:23-28:27] Because he's not, his only job right is actually the night shift.
[28:27-28:32] I cannot fucking work him 20 hours a day by involving him in the day ops.
[28:32-28:37] So, the knowledge that he has is everything on the freaking small screen.
[28:37-28:39] Okay, whichever customer orders, right?
[28:39-28:41] It's just on the screen, he takes it.
[28:41-28:42] He takes the word for it.
[28:42-28:49] So sometimes it's very, very difficult to educate the night shift guys on what the major changes happen during the day.
[28:49-28:54] You know, then he will copy the wrong thing, he will link to the wrong route, you know.
[28:54-28:58] He will, he will, he will, he will commit a lot of mistakes here and there.
[28:58-29:03] So that's, that's, uh, actually some of the mistakes are very, very difficult to...
[29:03-29:04] And why not?
[29:04-29:05] Yeah.
[29:05-29:06] Yeah.
[29:06-29:08] Okay, okay, no, cool.
[29:08-29:10] Then actually, without curiosity, right?
[29:10-29:12] Night shift is like, what time is what time?
[29:12-29:13] I don't know.
[29:13-29:15] But how come your order is at 3am, huh?
[29:15-29:18] Bro, it's 7 to 4.30am.
[29:18-29:24] The last order that they actually cut off is actually when the drivers and the warehouse teams in the office to draw,
[29:24-29:26] then they will cut off the order from there.
[29:26-29:27] So it's about 4 something.
[29:27-29:32] Because they, they, they get off, the, all the, all the chefs get off work around 12 or 1am, right?
[29:32-29:33] Right?
[29:33-29:37] After the cleanup, then they'll start to send order to, they will check in the fridge or whatever missing,
[29:37-29:39] then order for tomorrow's delivery.
[29:39-29:41] So that's why it's all very, very late.
[29:41-29:44] So actually most of your orders come at night, is what I'm hearing.
[29:44-29:47] Yes, most of the order comes at night.
[29:47-29:53] But the daytime orders also quite a bit, also quite a bit, but it's, I would say like 45% comes in the day.
[29:53-29:55] 60% comes in the night.
[29:55-29:59] Oh, okay no la, I was just wondering if it's better actually doing something useful, no?
[29:59-30:02] Cause like, bro, if you tell me like you get 10 orders a night, right?
[30:02-30:03] I tell you, just.
[30:03-30:07] No, I easily put me on the orders, yeah.
[30:07-30:09] Per night, okay la, okay la, then worth solving.
[30:09-30:14] Okay la, okay la, then I think it's worth solving la, I mean,
[30:14-30:17] I mean, the, what I can do for you is like a minimal version.
[30:17-30:22] Cause, I mean, unless, actually how much you willing to pay la, out of curiosity.
[30:23-30:32] I, to be honest, I'm, I'm open for offers la, because this kind of thing, I must match whatever that you guys are giving me as a quotation,
[30:32-30:36] versus, uh, the reality check from the finance side.
[30:36-30:38] So I will try to find a middle ground.
[30:38-30:42] But we are not be, we will not be eligible for any grants la, just, just for your information.
[30:42-31:12] No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no
[31:12-31:21] From all my competitors actually, he did a full scale tech solution for F&B companies all the way until routes and things like that
[31:21-31:30] But it's also subscription basis, it's close to a thousand dollar per, I think 900 something, 900 something per month
[31:30-31:34] So if I want to say this, I would say, let's say 30, 40
[31:34-31:40] That's actually, that's actually what Ivan was trying to do for David
[31:40-31:42] To create a whole system
[31:42-31:46] So for this alone, right, how much are you willing to pay?
[31:46-31:48] What's what I'm trying to figure out?
[31:49-31:52] I'll say, let's cap it in 50
[31:52-32:01] 50, yeah, okay, okay, I mean, look, 50 is gonna be extremely high for what I think it should be, right?
[32:01-32:02] I'll definitely touch you less
[32:02-32:06] Yeah, I mean, Seth, I think it's gonna be
[32:06-32:10] I thought to you what the competitor is doing, it's actually quite detailed
[32:10-32:14] It's like a full solution, including inventory management and everything
[32:14-32:19] I told Marvin, the reason why I'm not using them is because I told the
[32:19-32:21] I'm quite close with the owner
[32:21-32:24] I told him that your system, really, if I'm gonna use it, right
[32:24-32:27] It's gonna benefit me tremendously
[32:27-32:29] But you are my competitor
[32:29-32:35] You know, you get access to all my data, all my historical data, all my customer data and everything like that
[32:35-32:40] I don't, I will not be able to sleep well at night if I'm able to, if I use your system
[32:40-32:45] And although they say, oh, PTBA or whatever, but I don't trust that
[32:45-32:48] So that's the only issue
[32:48-32:55] So I would say, if you quit your distribution and food trading business, I'll onboard with you immediately
[32:55-32:56] But it's impossible
[32:56-33:06] Yeah, I think, I think like, this is going to be, like if you want everything on your own like servers, right
[33:06-33:11] It's quite, it's doable, but the only thing you cannot do is subscribe to someone else's platform, which is
[33:11-33:13] I guess where this project comes in, right
[33:13-33:18] Everything will be on your own like, own like hosted AWS instance, right
[33:18-33:19] Yeah
[33:19-33:20] Then you can sleep well at night, though
[33:20-33:21] I think that's the
[33:21-33:27] Unless, unless you tell me that always, why is by, uh, Entropic or Alibaba, you know, that kind of thing
[33:27-33:32] Okay, I'm able to subscribe, fuck it, that is okay, but, eh, not him, no
[33:32-33:39] Okay, then the last thing is, is like, so wait, I tell you first, ah, say real, right
[33:39-33:43] I have time now, but I don't know about time like in two months, right
[33:43-33:46] Are you willing to do it like now-ish?
[33:46-33:50] Like, how, how, what is your procurement process, ah, is it going to be very long, la
[33:50-34:20] No, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no, no
[34:20-34:23] I put time for you
[34:23-34:26] How about this
[34:26-34:28] Today after this call
[34:28-34:30] You give me
[34:30-34:32] What you need
[34:32-34:34] What you guys will be doing
[34:34-34:36] In a little bit more detail
[34:36-34:38] And also revise your code
[34:38-34:39] Let me know how much it is
[34:39-34:41] I will try to work on it
[34:41-34:42] By this week
[34:42-34:44] Okay, okay, sounds good
[34:44-34:46] The proposal right is that
[34:46-34:47] If let's say you start on the project
[34:47-34:48] Then there's maintenance everything
[34:48-34:50] Then you got no time, right?
[34:50-34:52] Then it's okay, I can get DC deal to do
[34:52-34:55] Maintenance, I'm less worried about that
[34:55-34:56] Because
[34:56-34:58] Yeah, it's a back end work, nothing much
[34:58-35:00] Anyone can do that job, actually
[35:00-35:03] I also don't think there'll be that much maintenance
[35:03-35:04] At least for this scope
[35:04-35:05] You know what I mean
[35:05-35:08] The system should run by itself
[35:08-35:09] After we finish all the iterations
[35:09-35:10] If that makes sense
[35:10-35:12] Unless you change your entire business
[35:12-35:13] Then that's a different story
[35:13-35:15] But it should be
[35:15-35:16] Relatively self-serving
[35:16-35:17] You know what I mean
[35:17-35:19] I don't want to be like
[35:19-35:20] That guy, you know
[35:20-35:21] Who's like fucking three months later
[35:21-35:22] And think break and fuck
[35:22-35:25] Bro, it needs to work la
[35:25-35:27] That's the TRD la
[35:27-35:28] Okay, I think let's do
[35:28-35:28] Go ahead
[35:28-35:30] So I think
[35:30-35:32] I also agree with you that
[35:32-35:34] Maintenance, well actually
[35:34-35:36] I'm not sure how
[35:36-35:38] How regular this is servicing
[35:38-35:39] But
[35:39-35:41] I just want to keep
[35:41-35:43] The first phase of this project
[35:43-35:44] As simple as it is
[35:44-35:45] So that
[35:45-35:46] Like you said
[35:46-35:47] It's more or less automatic on its own
[35:47-35:49] And without much
[35:49-35:51] Too much of processing needed
[35:51-35:52] At the back end
[35:52-35:54] So it doesn't have a lot of cock-ups
[35:54-35:55] Hopefully la
[35:55-35:56] Yeah la
[35:56-35:57] Keep it simple
[35:57-35:58] Keep it light
[35:58-35:59] But make it very useful
[35:59-36:00] And then like
[36:00-36:01] Maintenance
[36:01-36:03] I don't plan to charge you any recurring fee la
[36:03-36:05] Unless you really really really want me to
[36:05-36:06] It should just work
[36:06-36:09] It's a one-off fee
[36:09-36:11] And then it's called a day la
[36:11-36:11] Right
[36:11-36:12] And
[36:12-36:14] Then basically the iteration
[36:14-36:15] Until we call a day
[36:15-36:16] Is unlimited la
[36:16-36:17] Until you feel like
[36:17-36:18] It's like
[36:18-36:18] You know
[36:18-36:20] Right on point with what you're expecting
[36:20-36:21] From your workflow
[36:21-36:22] I think that's kind of like
[36:22-36:23] Normally how I do these kind of things
[36:23-36:25] You know what I mean
[36:25-36:25] So
[36:25-36:26] Fixed fee
[36:26-36:27] Unlimited
[36:27-36:28] Iterations
[36:28-36:28] But
[36:28-36:29] When we cut off
[36:29-36:29] And say like
[36:29-36:30] Okay fuck it
[36:30-36:31] This is working right
[36:31-36:33] Then I don't expect the charge of substitution
[36:33-36:34] Okay
[36:34-36:35] Yeah that's kind of like
[36:35-36:36] What I'm thinking
[36:36-36:37] Because
[36:37-36:38] If I charge subscription
[36:38-36:38] Then
[36:38-36:39] Wow
[36:39-36:40] There's a full ballpark of problems
[36:40-36:41] That come with it
[36:41-36:41] You know what I mean
[36:41-36:42] Which is like
[36:42-36:43] Hey success
[36:43-36:44] I want to upgrade la
[36:44-36:45] Then I'll be fuck you
[36:45-36:46] I mean
[36:46-36:48] If it works well
[36:48-36:49] Of course it will be
[36:49-36:51] I want to upgrade in the future
[36:51-36:51] Correct
[36:51-36:53] Then there will be another scope la
[36:53-36:53] Case by case la
[36:53-36:54] Yeah case by case la
[36:54-36:55] Okay okay cool
[36:55-36:56] So I think that's all I need right
[36:56-36:58] And then I will send you
[36:58-36:58] What I
[36:58-37:00] The requirements that I need
[37:00-37:00] From your side
[37:00-37:02] Which is really mostly the data
[37:02-37:02] I mean
[37:02-37:03] I've been keeping
[37:03-37:03] A transcript la
[37:03-37:04] I'll just send you everything later
[37:04-37:06] Then you pass it back
[37:06-37:07] And then I take a look
[37:07-37:08] After I take a look
[37:08-37:09] I can give you a quote
[37:09-37:09] And then
[37:09-37:11] If it's okay right
[37:11-37:12] Then I can start work like
[37:12-37:13] Basically immediately
[37:13-37:15] Cause I got time
[37:15-37:18] Yeah and you'll be doing me a favor also la
[37:18-37:19] Because I'm damn bored dude
[37:19-37:20] Holy shit
[37:20-37:22] Fuck
[37:22-37:23] I'm applying for a job
[37:23-37:24] But I didn't see you
[37:24-37:24] Fuck
[37:24-37:26] Cause it will take at least like
[37:26-37:27] One two months for me to
[37:27-37:29] Land a good job right
[37:29-37:30] So
[37:30-37:31] Yeah la
[37:31-37:32] Come on and drink la
[37:32-37:32] No choice la
[37:32-37:33] Yeah la
[37:33-37:34] But I mean
[37:34-37:34] Don't wanna drink so much la
[37:34-37:35] So
[37:35-37:36] Do some work la
[37:36-37:37] Okay
[37:37-37:38] Okay okay
[37:38-37:38] We work in the day
[37:38-37:39] And night we come out
[37:39-37:40] Okay okay okay
[37:40-37:41] Okay cool
[37:41-37:41] See you
[37:41-37:42] Alright
[37:42-37:42] Bye
[37:42-37:43] Bye bye
[37:43-37:43] Bye bye
[37:43-37:44] Bye bye
