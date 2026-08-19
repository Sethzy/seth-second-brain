---
type: raw_capture
source_type: web
title: "Speech-to-Speech AI Models with Zach Koh Voice AI Newsletter Transcript"
url: "https://voice-ai-newsletter.krisp.ai/p/speech-to-speech-ai-models-zach-koch?showTranscript=true"
collected_at: 2026-07-02T18:37:36Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Speech-to-Speech AI Models with Zach Koh Voice AI Newsletter Transcript

Source: https://voice-ai-newsletter.krisp.ai/p/speech-to-speech-ai-models-zach-koch?showTranscript=true

## Capture Text


Voice AI Newsletter
Voice AI Newsletter


Playback speed
1×
Share post
Share post at current time
Share from 0:00



0:49
/
29:18






Search
Welcome to the next episode of Voice AI Podcast, where we discuss the future of Voice AI. Today, I'm really super excited to host Zach Koh, who is the co-founder and CEO at Fixie AI. Welcome, Zach. Thank you for having me. Yeah, let me sort of try to summarize what Fixy AI is doing.
So you guys, and correct me if I say anything wrong. It's going to be a good test. It'll be a good test. We'll see. Yeah, yeah. No, actually, I just took it from your website. So you guys are building AIs that can communicate as naturally as humans. I mean, I think that's your mission statement, right?
Yeah, that's the goal. Yeah, but in practice, actually, you're building UltraVox, which is an open source, state of art, speech to speech model, right? Think like everyone, I guess, knows about OpenAI's voice mode, and you have built a very impressive model that is open source, right? And actually, we at CRISP have tried it.
We are so impressed by that. It's like super fast. and very high quality, so we just loved it. And the second thing, like you say on the website, you're building the world's best tech for handling real-time communication with LLMs over WebRTC. I would definitely like to dig into that as well.
You are experimenting with AI-human interaction at something called Town. I don't know what it is, so... Yeah, happy to talk about it, yeah. And the last thing is you're tracking the latency of models and providers over at the fastest AI, the fastest.ai, which I find to be an amazing resource. I check regularly for the fastest running LAMs.
I guess that's the core of what you guys have been doing. How many years have you been around?
We started the company in mid-2022. So we like to say we were like before the chat GPT craze sort of emerged. We made sort of an early bet on LLMs. But the voice thing was sort of like a pivot for us. Like we started in a different space.
We actually sort of started off as like a multi-agent framework. uh orchestration platform so uh we built like the entire way for agents to talk to each other in in english back and forth or for http but this was all back in the
days where the best model was gpt3 right so there was no tool there was no tool calling yet there was no rag yet like we sort of had just had to build all this up from scratch and so um
True visionaries, huh? Nobody was talking about that back then.
Got lucky is how I put it. I think we stumbled into some things and we sort of had our, what I call our holy crap moments on LLMs in early 2022 with the GPT-3 playground. And again, there were no chat models yet. There were only completion models.
But it was just so amazing that you could few shot these things and it was like, So here we are a couple of years later.
Yeah, yeah. Zach, tell me more about your team. How is it constructed in terms of your experience, right? It seems like you guys are big into WebRTC and you have that experience and then you take LLMs and then you build these speech-to-speech models and you have some secret, not secret, but very unique source, I guess,
to make it fast, smart, and so on. What does it need to build these models?
Well, yeah, I think there's two parts to... I should correct one thing, by the way, for the record, is that we are... The model itself is aspirationally speech-to-speech. Right now, we are speech-in-text-out. And then, like, our platform that we sort of, like, call UltraVox Real-Time has a speech component, but it's not digged into the model yet.
So that's, like, something that we are... working on and trying to produce for next year, which is a true fully speech in speech out. But, you know, as a small team, it was important that we pick like one problem to focus on first. And we chose to focus on the problem of speech understanding.
How can we get the model to understand speech really well, understand dialogue very well, understand things like turn taking intonation? These are the things that are really hard. And then we'll sort of like add the the the the speech generation a bit later.
Right now, probably in the early part of next year, that'll be part of the open source model.
Do you mean that it's like speech to text? So the LLM is text, but then you do TTS? Because it's so fast. I mean, it feels like very, very natural. It feels like speech to speech.
It does. I think the trick with all these things is you kind of get a latency budget, right? Is how I think about it. And you get to choose, like, if you save over here, you get to spend more for here. And so I think that the reality is that we judge the quality of these voice agents
or speech systems by the quality of the speech on the other end, because that's like the easiest thing for us as humans to reason about. Like, do you sound plausible? It's like the legibility test, right? Like what makes the system much more legible? And so for us,
it was always important that we don't skimp on the quality of voice on the other side. Even though there are faster TTS models out there than what we use by default, the quality matters a lot. But we don't have an ASR step. And we've also optimized the entire stack for low latency. So by saving latency over here,
we're able to spend it more on the quality of the speech on the other side. And this is why I think if you do apples to apples comparisons on speech quality, we tend to be faster than others for that reason.
And by embedding the TTS into the model, it will make it faster. Is that the idea?
Yeah, I think there's two things that you want to buy. I think like, yes, it will make it faster. I think latency is always like a thing that's top of mind. But I don't think like latency right now is the biggest barrier to feel like natural feeling conversations. Yeah, so I was saying is like,
I think that like, I don't think latency is like the number one barrier right now. Like, we can keep driving latency down and we will. But even latency itself is not like, there's no like, like singular right answer for what appropriate response speed is. Like if you think about in everyday human interactions, like there was,
if you and I were friends for 15 years and we're at a bar, like the, the, the latency like between our turns would be very, very low. But like, if we had just met and this was like a very formal environment, the latency would be much higher because we'd be erring on the side of respect.
And so the truth is that like latency is always a little bit of a fungible thing. But the thing we really care about is the naturalness and the feeling of naturalness of the dialogue. And like ultimately want speech to speech, because I think you want like a singular model where you're leveraging the full
power of the transformer and a large model to reason about what's happening in the dialogue. How should I respond? Like what's the what's the tone I'm getting and how does that affect the tone that I should generate on the other side? And so ultimately, you want as much as you can, I think,
to move these all into a singular model, because that's the only way that we think you're going to be able to actually get the level of naturalness that will sort of make you think as though, oh, this dialogue feels correct.
Yeah. And, um, so correct in terms of humanness, right? Like, so the, like a Turing test for Turing test for like human interaction is this like a person or.
Yeah. Exactly. Exactly. And not that we're trying to trick people, of course, but just that, like, um, like the expectation is that you should be able to, what I would say is you don't want to have to change the way you as a human speak, uh, to make the computer understand you,
which is what still has to happen today. Um, so.
And then can you decompose this into different components? What is it? How do you guys think about the humanness? Obviously, we have our own system. Humans have their own systems to filter noise or... you know, understand emotion. Is emotion part of this? Should we have like built-in emotion recognition, like audio based so that, you know,
the model is robust? How do you think about that?
Yeah, I mean, I think ultimately you have to. I think that the interesting question is like, are these discrete components? Are they all part of the same model? I think that's sort of like an interesting sort of empirical question that we sort of navigate as we make progress. But like, as you know, like,
Humans have decent built-in noise cancellation, it seems, but the models don't much. So, of course, we use crisp noise cancellation models, which are a great help to the model. And so I think that if tools exist, we should leverage those tools to help the models increase understanding. But at the same time,
the models themselves clearly need to become more robust in terms of their ability to handle adverse conditions, multiple speakers, background noise, and stuff like that. And so I think it's always going to be like a combination effort. And as much as we can, we're trying to sort of like, how do humans work?
Like, well, humans don't have an ASR step, right? As I'm talking, you're not like transcribing into text.
Well, sometimes I do because like English is not my first language. It is true. It is true.
Like when you're speaking a foreign language, sometimes like you go through a translation process. I have subtitles, yeah. But for the most part, like, And we then can use context to help us, even when there's gaps in understanding, like it's a loud environment or chaotic,
we as humans use context to help us drive the words that we might have missed. So our chief belief when we started UltraVox was we had to stop the transcript stage. We had to get to the point where the model was being fed the audio directly.
That way it can reason about the audio with the full power of the model. And I think that's sort of where we are today. It's like there's no ASR stage. The model consumes speech embeddings directly. And now the model can reason across those speech embeddings and fill in the gaps
better than it can in just an ASR stage. And of course, we get latency wins. So it's a combination of like, yeah, you want to be faster, but you also want the system to be smarter. And like the way we humans work is like the more context that we can take in,
the better we are able to reason about like how to respond, if I should respond, when I should respond. And that's kind of like what's driving our current strategy and thinking.
Very cool. Yeah. And when you think about the use cases for this, right? What are the top three use cases coming to mind like that you see from customers and others?
Yeah, I think there's the present world use cases, which is where almost all the attention is. And then there's also the world that we're also excited about in the future. And the future world, I think, needs more progress on the core modeling side. So we need smarter LLMs, for example.
And then we also need better voice AIs as well, better speech language models. And so the combination of these two will hopefully unlock new use cases as we evolve. I think humanoid robots, for example, more AI employees, group collaborations inside of Meets, all that good stuff. I think like right now,
I think the trend that we see is the same trend I think a lot of folks see, which is like our number one sort of incoming request is typically is like customer support, like outbound or inbound sort of phone call handling. We also see a number of, I would call them like sort of AI native companies.
They're trying to think about voice as like a primitive that they should have from the very beginning. um and uh one that i'm sort of particularly excited by uh just because it's like really fun to build is we partnered a little bit with like this uh toy company and
had this like sort of really fun sort of thing coming out next year they're doing almost all the toy work we just kind of like offer the the service that we have but i think it's a pretty magical experience that they've been sort of able to build um
for uh for for kids and stuff like that um but uh so yeah the bulk of the business is definitely in those first two categories for sure
Yeah, if you think about how kids are going to talk to toys, it really needs to be smart and be tuned to that. That's a really interesting use case. I know a company called Moxie. There is a Moxie robot that does it, but I'm not sure what AI they're using. Yeah, I'm not sure either.
And there's going to be called Hey Curio 2 that builds a really fun stuffed animal called Grok, I think that is about. So I think we're starting to see some really fun ideas in this space that aren't just like the very strict classic sort of mold here.
Zach, like you mentioned, so one of the things you're building is the best tech stack for real-time communication, LLM, and WebRTC, right? Can you elaborate what that means? What's that ideal tech stack of the future?
Yeah, well, the ideal tech stack is probably the one that works the best. So we have two things that we spend a lot of our days on, right? The model itself, that's the UltraVox model. But then we also productionize a SaaS offering, which we call UltraVox real time. which is where we sort of are running the model,
expose it as APIs, has built in things for like tools and all the stuff you sort of need to build productionized voice AI systems, right? Most people like that are paying that if people pay us, like we give the model away for free, of course, it's on Hugging Face, anyone can go use it.
We also contribute to VLLM, which is like probably the largest open source inference framework. We added in like the support for like audio input as the modality in VLLM. And we'll continue to push that forward. So all that we sort of give into the open source community for free.
And then ultra box real time is sort of like our opinionated stack on how all these pieces compose in a low latency way to sort of solve and like meet like real world customer problems. and so like what's the ideal stack i think it depends i mean so uh we clearly love
web rtc like a number of our like people on our team are from google and like the stadia teams and like the real-time teams where like how do you like eke out every last millisecond of latency from a system uh and like we've spent lots of time like
deep in the weeds about like um how do you be smart across every single stage of the problem um and so we spend a lot of time there But it's also about how do you efficiently route to the GPU? Here's a simple example. When you go to do inference, inference is stateless, right?
So when you actually go to ask the model to produce a response. And so for most systems, when you submit your request in, it gets routed to whatever GPU is available. And because all the context is passed in, it can be used to generate a response. But for us, like audio is the source of truth, right?
So like, we don't, we don't use the transcript ever. It's like the transcript is more just like a user facing accessibility feature. So audio embeddings are the, are what the model reasons about. But as those audio embeddings grow, the size gets larger. So if you were to do a completely stateless inference, your latency would be pretty bad.
So we instead have to do this best effort thing, that's very good best effort, where we try to lock a call to a particular GPU so we can make heavy use of the cache, for example, to drive down latency.
so like but yeah we spend a lot of time in our days in like web rtc land uh and uh you know gpu efficiencies like we try to remove any middlemen from that thing because like a lot of like providers also add these like proxies and every proxy is
just like 20 or 30 milliseconds here and and no one individually is terrible but when you start to like sum them up like it really eats at you and so a lot of like driving latency out is just being very meticulous about saying are you necessary is this necessary can we get rid of this
um and that's what we sort of spend our our time on and that's kind of what makes the demo possible um and we have more work to do here i feel i still think we can drive out another couple hundred milliseconds here with work and i guess like
supporting different languages different frameworks different platforms is going to be part of the roadmap right so that to make it like really easy for developers to use the api yeah yeah exactly exactly yeah
Yeah, and this is where we haven't done a phenomenal job, if I'm fully honest. I think we have a base set of APIs that are pretty low-level primitive. And so I think they're the right primitives, but they can be a little bit difficult to compose if you're not like... too difficult sometimes.
And so we're sort of like reworking things a little bit right now to make them a little bit more accessible. We've got SDKs for the primary languages, but again, like I wouldn't give them, I wouldn't give us an A plus for like a devX and usability.
And so these are sort of things that we're like very actively trying to lower the barrier to entry on.
Yeah. Look, let's switch the gears a bit. Like OpenAI yesterday announced about some improvements in their voice mode, right? A couple of things that caught my eye. Like first, like they introduced the mini model, right? Which is going to be... like way, way cheaper. I guess like it's just like a smaller LLM behind it.
So it's maybe it's going to be less smart. I don't know. We haven't tested it yet.
We also haven't, I was going to ask you if you had a chance to test it yet. And I think this is sort of what's really interesting is like, what's the parameter size, but I don't know yet.
Yeah. Yeah. Yeah. No, no idea yet. And the second thing is like this native WebRTC support was very interesting to see. So basically you can, they provide from what I understand like web RTC connection from the API so that you can like You don't need other providers in the middle, I guess. I think that's what it removes.
And you can just talk to OpenAI through WebRTC. What are your thoughts on this? I mean, obviously, the biggest competitor, right? How do you think about them? And Google has announced something.
I think Jim and I also did live... what's it, what's it called? Anyway, but they're, they're equivalent as well.
Yeah. Yeah. Yeah. I think like, I guess everyone is going to get in, like anthropic is probably going to get into there as well. So how do you think about the competition there? It must be hard when all these big companies are there, but I think it's the default intuition, but startups, if you just follow default intuition,
that's not how startups work. There is always a niche, and then if you do something way better, you win, right?
Yeah, yeah. I mean, my thoughts on this are always evolving because the space is evolving so rapidly. I think I'll say at a high level, the more people talking about voice AI is good for us, right? I think that we remain pretty convicted that voice is a really great modality. It's the way humans prefer to interact.
And so therefore, it's the way we've always... We don't have a better mechanism as humans for rapidly exchanging ideas than voice. It's the best. So like the more that we can align that to like the computer systems that we use, I think the better for everyone.
Um, I think the, uh, for open AI and web RTC support, I think it was completely expected. Uh, you know, when they first launched it, it was only, it was only web sockets. Um, and web sockets of course is great for server to server, but it's really bad, uh, when you're going down to client side devices.
And so to us, our, our bet was, that was only because like web sockets are TCP, right? Uh, whereas like you know webrtc is is a udp and like um i think that uh so to us it was very expected and makes sense uh it also makes sense that if you are open ai uh
you want to own as much of like the stack yourself as opposed to depending on third-party providers uh i think for the average person it doesn't make that much of a difference uh like whether it's like their webrtc stack or like someone else's webrtc stack i don't think that really matters like
it's just a glorified pipe between a client and some other some other peer um and i think it's more about for them an ownership mentality um and uh i think the pricing thing is interesting for sure uh like you know and that's where i think where um
i'm with you like what the key question is how how smart is that model like how like the mini model can it do like real world scenarios how's tool calling support that i need to go experiment with maybe over the break uh and then um
And for Gemini, I also think it was a great default experience, I think, out of the box. I think our view is that, again, we play in the domain of open source. And we chose open source, I think, A, from a philosophical perspective.
We think that we very heavily align with Lama and Mistral and how they think about the world and what openness gives us. But also, I think it's just from a practical business standpoint, I think that we're sort of really interested in the companies who are also interested in open source overall and the ability, therefore,
to run these stacks completely on-prem. So we also license our stack to run. So if you're a larger regulated company, the idea of trusting your entire strategy to a black box in the proprietary ecosystem is a little bit alarming. And sort of our bet was always gonna be that open source will continue to converge
with the capabilities of proprietary and faced with the optionality of like, do I put all of my confidence into the black box or do I go with the option set? I think larger enterprises I think are more and more um looking at things like llama and mistral because they like they present that
optionality that isn't necessarily present in the proprietary solutions and so like again net net i think it's good for us it's great to see more competition and sort of see um i'll sort of say what i've said before it's like none of us are still great yet
um i think uh oh yeah a lot of no one really has no one really has speech on like real speech understanding everyone is still dependent on silence and vad is like your indicator so like we're all still like kind of like hovering around the same
spots and i think our mission is like um we're only doing one thing we only focus on building the fastest most reliable best speech understanding system out there and so all of our time and energy goes into this one problem and so i think the
question is like if we just do this one thing can we do it really well for businesses i'm like Time will tell. We should do, like, a follow-up in six months and see, like, where we're at. But, like, that's – at least that's a strategy that we're taking.
No, I think that makes sense. Like, the open source angle and the enterprise angle is, I think, a very valid point. So – and, like, just to clarify for myself, do you guys – Like when you build like a speech, speech model, like speech, speech to speech or speech to, I don't know, speech to LLM, I guess.
Speech attacks. Yeah. Speech attacks. Yeah. Yeah. Not speech attacks, but speech to LLM, right? LLM. Oh, I see. I see what you're saying. I see what you're saying. Yeah. Got it. But do you have to like, if you want to change the, replace the, the underlying model, you need to do like full training again.
Is that how it works?
Yes, if the model is completely different, yeah, we will retrain. But there's a couple of nuanced points there.
Can you do, like, a checkpoint and then, like, fine-tune? Or it's just impossible? Yeah,
if it's in, like, the same embedding space, but, like, you cannot, for example, take an UltraVox adapter trained on Llama and expect it to apply to the world of Mistral. Like, those are two different. But, for example, like, when 3.3 came out with Llama, like, that was just a fine-tune of our projector.
uh and and that was that was very short and easy and so we upgraded our model behind the scenes from ultra box to 3.3 like overnight basically oh and we can also like reapply the same adapter to any fine tune as well like particularly laura's
all work out of the box uh without any need to retrain but yeah like if like a brand new but yeah you cannot use a projector like mistral to make it work with like jimma from google like that won't work because like they're in embedding spaces of course completely completely separate
Yeah. No, I love it. Look, let's talk about two years in. My last question always, how do you imagine the voice AI space in two years? I mean, it's a big, difficult, difficult one. But it's a fun one. Yeah, I mean, I used to say five years, but I'm down to two now because it's just...
Exactly. I feel like I got asked this question from a candidate. He's like, so what do you see the world like in five years? And I was like, I don't even know. Like if I think about when we started the company in 2022, like the best model was GPT-3.
And like, and now here we are in late 2024 and like GPT-3 is like, haha, what a dumb model. And the pace is insane. And so it's always a little bit hard. But I think from our vantage point, I think what we're really hoping to get to over the next couple of years are AIs
that are real collaborators. And I think that if you think about if you work in a company right it's in the larger the company the more time you spend in meetings because like uh the hard part of getting stuff done uh oftentimes it's not like the work
itself it's like the coordination around the work oh yeah um and uh i think what i like what the future i'm imagining is where like a lot of the like those collaborations are like always joint collaborations between humans and ais uh and so we've got ais like in the video call for example
And like right now, like all we get are like glorified note takers, right? Because we can't, they're not capable of participating in the dialogue yet. They don't understand multiple speakers. They don't understand like, like the rules of multi-person dialogue and when to interject. But like,
so like this bridge from like where we are now into the real world is like what I'm the most excited by and I think is totally possible. you know, you've got like, you've got more investment in humanoid robots over the last like nine months than like, I feel like the decade previously. So everyone's excited by this,
but like, but if you think about what it's going to take to make those robots be able to actually like dialogue in the real world, like a retail store where there's all these different speakers and like, like all the systems right now would completely fall flat. So I think like over the next couple of years,
I think we go from these things as like largely behind the scenes actors who you don't really trust with anything super important and get easily confused into like primary collaborators that we like look to more and more as like to help us refine ideas, lead meetings, like empathize a little bit.
I think these are sort of what's possible at the current trend lines and like think what, and like that's what I'm like most excited by. And so I sort of view it as These days, we're sort of plucking the low-hanging fruit of voice AI. But the real future, I think, is really around this deep collaboration concept.
And that's really where voice is best served. Because, like, again, whenever we have a complex problem, like if you and I were debating something on, like, crisp models, for example, we would almost guaranteed want to get in a meeting, right? Because going back and forth on Slack and text, this doesn't allow you to, like,
have the richness and speed of dialogue. Exactly. So, like, that's what I'm excited by.
we lose context and it's just like way more natural. And I think the moment you start to imagine this like collaborative meeting where there are like three agents and two people talking to each other, there are so many problems to solve there from tech perspective. And so there's a lot of value to be created and so on.
Yeah, I love that. I think that makes a lot of sense.
Yeah. And I feel like a lot of people sort of, I think like we fall into the trap of thinking like, oh, like voice AI is salt. Like we we've got, and it's like, and if you think about like how many, you know, I live in this space every day.
So I think it's a little bit different for us, but. Like it's like I have a list of like a hundred problems that have to be like addressed before we can even come even close to like making those things possible, right? Right now, our models still get confused.
Like if my daughter comes up and like ask me a question and the AI hears it, the AI like responds back to her. It's like, no, no, no, clearly that's my daughter and not me. Like, why don't you know that? And so we have so many obvious things to go off and solve on the speech
understanding side first, I think. But rich problem space.
Very cool, Zach. I think this was great. I really would like to follow up in six months, nine months and see where you guys, I'm like very fascinated in this technology. And yeah, thanks so much for your insights and time.
Yeah, no, thank you. And thanks to Chris for like the great models that we're already working with. And so thanks for what you guys do as well. Sounds great. Thanks, Zach. Thanks. Thanks.


54


1






Welcome to the next episode of Voice AI Podcast, where we discuss the future of Voice AI. Today, I'm really super excited to host Zach Koh, who is the co-founder and CEO at Fixie AI. Welcome, Zach. Thank you for having me. Yeah, let me sort of try to summarize what Fixy AI is doing.
So you guys, and correct me if I say anything wrong. It's going to be a good test. It'll be a good test. We'll see. Yeah, yeah. No, actually, I just took it from your website. So you guys are building AIs that can communicate as naturally as humans. I mean, I think that's your mission statement, right?
Yeah, that's the goal. Yeah, but in practice, actually, you're building UltraVox, which is an open source, state of art, speech to speech model, right? Think like everyone, I guess, knows about OpenAI's voice mode, and you have built a very impressive model that is open source, right? And actually, we at CRISP have tried it.
We are so impressed by that. It's like super fast. and very high quality, so we just loved it. And the second thing, like you say on the website, you're building the world's best tech for handling real-time communication with LLMs over WebRTC. I would definitely like to dig into that as well.
You are experimenting with AI-human interaction at something called Town. I don't know what it is, so... Yeah, happy to talk about it, yeah. And the last thing is you're tracking the latency of models and providers over at the fastest AI, the fastest.ai, which I find to be an amazing resource. I check regularly for the fastest running LAMs.
I guess that's the core of what you guys have been doing. How many years have you been around?
We started the company in mid-2022. So we like to say we were like before the chat GPT craze sort of emerged. We made sort of an early bet on LLMs. But the voice thing was sort of like a pivot for us. Like we started in a different space.
We actually sort of started off as like a multi-agent framework. uh orchestration platform so uh we built like the entire way for agents to talk to each other in in english back and forth or for http but this was all back in the
days where the best model was gpt3 right so there was no tool there was no tool calling yet there was no rag yet like we sort of had just had to build all this up from scratch and so um
True visionaries, huh? Nobody was talking about that back then.
Got lucky is how I put it. I think we stumbled into some things and we sort of had our, what I call our holy crap moments on LLMs in early 2022 with the GPT-3 playground. And again, there were no chat models yet. There were only completion models.
But it was just so amazing that you could few shot these things and it was like, So here we are a couple of years later.
Yeah, yeah. Zach, tell me more about your team. How is it constructed in terms of your experience, right? It seems like you guys are big into WebRTC and you have that experience and then you take LLMs and then you build these speech-to-speech models and you have some secret, not secret, but very unique source, I guess,
to make it fast, smart, and so on. What does it need to build these models?
Well, yeah, I think there's two parts to... I should correct one thing, by the way, for the record, is that we are... The model itself is aspirationally speech-to-speech. Right now, we are speech-in-text-out. And then, like, our platform that we sort of, like, call UltraVox Real-Time has a speech component, but it's not digged into the model yet.
So that's, like, something that we are... working on and trying to produce for next year, which is a true fully speech in speech out. But, you know, as a small team, it was important that we pick like one problem to focus on first. And we chose to focus on the problem of speech understanding.
How can we get the model to understand speech really well, understand dialogue very well, understand things like turn taking intonation? These are the things that are really hard. And then we'll sort of like add the the the the speech generation a bit later.
Right now, probably in the early part of next year, that'll be part of the open source model.
Do you mean that it's like speech to text? So the LLM is text, but then you do TTS? Because it's so fast. I mean, it feels like very, very natural. It feels like speech to speech.
It does. I think the trick with all these things is you kind of get a latency budget, right? Is how I think about it. And you get to choose, like, if you save over here, you get to spend more for here. And so I think that the reality is that we judge the quality of these voice agents
or speech systems by the quality of the speech on the other end, because that's like the easiest thing for us as humans to reason about. Like, do you sound plausible? It's like the legibility test, right? Like what makes the system much more legible? And so for us,
it was always important that we don't skimp on the quality of voice on the other side. Even though there are faster TTS models out there than what we use by default, the quality matters a lot. But we don't have an ASR step. And we've also optimized the entire stack for low latency. So by saving latency over here,
we're able to spend it more on the quality of the speech on the other side. And this is why I think if you do apples to apples comparisons on speech quality, we tend to be faster than others for that reason.
And by embedding the TTS into the model, it will make it faster. Is that the idea?
Yeah, I think there's two things that you want to buy. I think like, yes, it will make it faster. I think latency is always like a thing that's top of mind. But I don't think like latency right now is the biggest barrier to feel like natural feeling conversations. Yeah, so I was saying is like,
I think that like, I don't think latency is like the number one barrier right now. Like, we can keep driving latency down and we will. But even latency itself is not like, there's no like, like singular right answer for what appropriate response speed is. Like if you think about in everyday human interactions, like there was,
if you and I were friends for 15 years and we're at a bar, like the, the, the latency like between our turns would be very, very low. But like, if we had just met and this was like a very formal environment, the latency would be much higher because we'd be erring on the side of respect.
And so the truth is that like latency is always a little bit of a fungible thing. But the thing we really care about is the naturalness and the feeling of naturalness of the dialogue. And like ultimately want speech to speech, because I think you want like a singular model where you're leveraging the full
power of the transformer and a large model to reason about what's happening in the dialogue. How should I respond? Like what's the what's the tone I'm getting and how does that affect the tone that I should generate on the other side? And so ultimately, you want as much as you can, I think,
to move these all into a singular model, because that's the only way that we think you're going to be able to actually get the level of naturalness that will sort of make you think as though, oh, this dialogue feels correct.
Yeah. And, um, so correct in terms of humanness, right? Like, so the, like a Turing test for Turing test for like human interaction is this like a person or.
Yeah. Exactly. Exactly. And not that we're trying to trick people, of course, but just that, like, um, like the expectation is that you should be able to, what I would say is you don't want to have to change the way you as a human speak, uh, to make the computer understand you,
which is what still has to happen today. Um, so.
And then can you decompose this into different components? What is it? How do you guys think about the humanness? Obviously, we have our own system. Humans have their own systems to filter noise or... you know, understand emotion. Is emotion part of this? Should we have like built-in emotion recognition, like audio based so that, you know,
the model is robust? How do you think about that?
Yeah, I mean, I think ultimately you have to. I think that the interesting question is like, are these discrete components? Are they all part of the same model? I think that's sort of like an interesting sort of empirical question that we sort of navigate as we make progress. But like, as you know, like,
Humans have decent built-in noise cancellation, it seems, but the models don't much. So, of course, we use crisp noise cancellation models, which are a great help to the model. And so I think that if tools exist, we should leverage those tools to help the models increase understanding. But at the same time,
the models themselves clearly need to become more robust in terms of their ability to handle adverse conditions, multiple speakers, background noise, and stuff like that. And so I think it's always going to be like a combination effort. And as much as we can, we're trying to sort of like, how do humans work?
Like, well, humans don't have an ASR step, right? As I'm talking, you're not like transcribing into text.
Well, sometimes I do because like English is not my first language. It is true. It is true.
Like when you're speaking a foreign language, sometimes like you go through a translation process. I have subtitles, yeah. But for the most part, like, And we then can use context to help us, even when there's gaps in understanding, like it's a loud environment or chaotic,
we as humans use context to help us drive the words that we might have missed. So our chief belief when we started UltraVox was we had to stop the transcript stage. We had to get to the point where the model was being fed the audio directly.
That way it can reason about the audio with the full power of the model. And I think that's sort of where we are today. It's like there's no ASR stage. The model consumes speech embeddings directly. And now the model can reason across those speech embeddings and fill in the gaps
better than it can in just an ASR stage. And of course, we get latency wins. So it's a combination of like, yeah, you want to be faster, but you also want the system to be smarter. And like the way we humans work is like the more context that we can take in,
the better we are able to reason about like how to respond, if I should respond, when I should respond. And that's kind of like what's driving our current strategy and thinking.
Very cool. Yeah. And when you think about the use cases for this, right? What are the top three use cases coming to mind like that you see from customers and others?
Yeah, I think there's the present world use cases, which is where almost all the attention is. And then there's also the world that we're also excited about in the future. And the future world, I think, needs more progress on the core modeling side. So we need smarter LLMs, for example.
And then we also need better voice AIs as well, better speech language models. And so the combination of these two will hopefully unlock new use cases as we evolve. I think humanoid robots, for example, more AI employees, group collaborations inside of Meets, all that good stuff. I think like right now,
I think the trend that we see is the same trend I think a lot of folks see, which is like our number one sort of incoming request is typically is like customer support, like outbound or inbound sort of phone call handling. We also see a number of, I would call them like sort of AI native companies.
They're trying to think about voice as like a primitive that they should have from the very beginning. um and uh one that i'm sort of particularly excited by uh just because it's like really fun to build is we partnered a little bit with like this uh toy company and
had this like sort of really fun sort of thing coming out next year they're doing almost all the toy work we just kind of like offer the the service that we have but i think it's a pretty magical experience that they've been sort of able to build um
for uh for for kids and stuff like that um but uh so yeah the bulk of the business is definitely in those first two categories for sure
Yeah, if you think about how kids are going to talk to toys, it really needs to be smart and be tuned to that. That's a really interesting use case. I know a company called Moxie. There is a Moxie robot that does it, but I'm not sure what AI they're using. Yeah, I'm not sure either.
And there's going to be called Hey Curio 2 that builds a really fun stuffed animal called Grok, I think that is about. So I think we're starting to see some really fun ideas in this space that aren't just like the very strict classic sort of mold here.
Zach, like you mentioned, so one of the things you're building is the best tech stack for real-time communication, LLM, and WebRTC, right? Can you elaborate what that means? What's that ideal tech stack of the future?
Yeah, well, the ideal tech stack is probably the one that works the best. So we have two things that we spend a lot of our days on, right? The model itself, that's the UltraVox model. But then we also productionize a SaaS offering, which we call UltraVox real time. which is where we sort of are running the model,
expose it as APIs, has built in things for like tools and all the stuff you sort of need to build productionized voice AI systems, right? Most people like that are paying that if people pay us, like we give the model away for free, of course, it's on Hugging Face, anyone can go use it.
We also contribute to VLLM, which is like probably the largest open source inference framework. We added in like the support for like audio input as the modality in VLLM. And we'll continue to push that forward. So all that we sort of give into the open source community for free.
And then ultra box real time is sort of like our opinionated stack on how all these pieces compose in a low latency way to sort of solve and like meet like real world customer problems. and so like what's the ideal stack i think it depends i mean so uh we clearly love
web rtc like a number of our like people on our team are from google and like the stadia teams and like the real-time teams where like how do you like eke out every last millisecond of latency from a system uh and like we've spent lots of time like
deep in the weeds about like um how do you be smart across every single stage of the problem um and so we spend a lot of time there But it's also about how do you efficiently route to the GPU? Here's a simple example. When you go to do inference, inference is stateless, right?
So when you actually go to ask the model to produce a response. And so for most systems, when you submit your request in, it gets routed to whatever GPU is available. And because all the context is passed in, it can be used to generate a response. But for us, like audio is the source of truth, right?
So like, we don't, we don't use the transcript ever. It's like the transcript is more just like a user facing accessibility feature. So audio embeddings are the, are what the model reasons about. But as those audio embeddings grow, the size gets larger. So if you were to do a completely stateless inference, your latency would be pretty bad.
So we instead have to do this best effort thing, that's very good best effort, where we try to lock a call to a particular GPU so we can make heavy use of the cache, for example, to drive down latency.
so like but yeah we spend a lot of time in our days in like web rtc land uh and uh you know gpu efficiencies like we try to remove any middlemen from that thing because like a lot of like providers also add these like proxies and every proxy is
just like 20 or 30 milliseconds here and and no one individually is terrible but when you start to like sum them up like it really eats at you and so a lot of like driving latency out is just being very meticulous about saying are you necessary is this necessary can we get rid of this
um and that's what we sort of spend our our time on and that's kind of what makes the demo possible um and we have more work to do here i feel i still think we can drive out another couple hundred milliseconds here with work and i guess like
supporting different languages different frameworks different platforms is going to be part of the roadmap right so that to make it like really easy for developers to use the api yeah yeah exactly exactly yeah
Yeah, and this is where we haven't done a phenomenal job, if I'm fully honest. I think we have a base set of APIs that are pretty low-level primitive. And so I think they're the right primitives, but they can be a little bit difficult to compose if you're not like... too difficult sometimes.
And so we're sort of like reworking things a little bit right now to make them a little bit more accessible. We've got SDKs for the primary languages, but again, like I wouldn't give them, I wouldn't give us an A plus for like a devX and usability.
And so these are sort of things that we're like very actively trying to lower the barrier to entry on.
Yeah. Look, let's switch the gears a bit. Like OpenAI yesterday announced about some improvements in their voice mode, right? A couple of things that caught my eye. Like first, like they introduced the mini model, right? Which is going to be... like way, way cheaper. I guess like it's just like a smaller LLM behind it.
So it's maybe it's going to be less smart. I don't know. We haven't tested it yet.
We also haven't, I was going to ask you if you had a chance to test it yet. And I think this is sort of what's really interesting is like, what's the parameter size, but I don't know yet.
Yeah. Yeah. Yeah. No, no idea yet. And the second thing is like this native WebRTC support was very interesting to see. So basically you can, they provide from what I understand like web RTC connection from the API so that you can like You don't need other providers in the middle, I guess. I think that's what it removes.
And you can just talk to OpenAI through WebRTC. What are your thoughts on this? I mean, obviously, the biggest competitor, right? How do you think about them? And Google has announced something.
I think Jim and I also did live... what's it, what's it called? Anyway, but they're, they're equivalent as well.
Yeah. Yeah. Yeah. I think like, I guess everyone is going to get in, like anthropic is probably going to get into there as well. So how do you think about the competition there? It must be hard when all these big companies are there, but I think it's the default intuition, but startups, if you just follow default intuition,
that's not how startups work. There is always a niche, and then if you do something way better, you win, right?
Yeah, yeah. I mean, my thoughts on this are always evolving because the space is evolving so rapidly. I think I'll say at a high level, the more people talking about voice AI is good for us, right? I think that we remain pretty convicted that voice is a really great modality. It's the way humans prefer to interact.
And so therefore, it's the way we've always... We don't have a better mechanism as humans for rapidly exchanging ideas than voice. It's the best. So like the more that we can align that to like the computer systems that we use, I think the better for everyone.
Um, I think the, uh, for open AI and web RTC support, I think it was completely expected. Uh, you know, when they first launched it, it was only, it was only web sockets. Um, and web sockets of course is great for server to server, but it's really bad, uh, when you're going down to client side devices.
And so to us, our, our bet was, that was only because like web sockets are TCP, right? Uh, whereas like you know webrtc is is a udp and like um i think that uh so to us it was very expected and makes sense uh it also makes sense that if you are open ai uh
you want to own as much of like the stack yourself as opposed to depending on third-party providers uh i think for the average person it doesn't make that much of a difference uh like whether it's like their webrtc stack or like someone else's webrtc stack i don't think that really matters like
it's just a glorified pipe between a client and some other some other peer um and i think it's more about for them an ownership mentality um and uh i think the pricing thing is interesting for sure uh like you know and that's where i think where um
i'm with you like what the key question is how how smart is that model like how like the mini model can it do like real world scenarios how's tool calling support that i need to go experiment with maybe over the break uh and then um
And for Gemini, I also think it was a great default experience, I think, out of the box. I think our view is that, again, we play in the domain of open source. And we chose open source, I think, A, from a philosophical perspective.
We think that we very heavily align with Lama and Mistral and how they think about the world and what openness gives us. But also, I think it's just from a practical business standpoint, I think that we're sort of really interested in the companies who are also interested in open source overall and the ability, therefore,
to run these stacks completely on-prem. So we also license our stack to run. So if you're a larger regulated company, the idea of trusting your entire strategy to a black box in the proprietary ecosystem is a little bit alarming. And sort of our bet was always gonna be that open source will continue to converge
with the capabilities of proprietary and faced with the optionality of like, do I put all of my confidence into the black box or do I go with the option set? I think larger enterprises I think are more and more um looking at things like llama and mistral because they like they present that
optionality that isn't necessarily present in the proprietary solutions and so like again net net i think it's good for us it's great to see more competition and sort of see um i'll sort of say what i've said before it's like none of us are still great yet
um i think uh oh yeah a lot of no one really has no one really has speech on like real speech understanding everyone is still dependent on silence and vad is like your indicator so like we're all still like kind of like hovering around the same
spots and i think our mission is like um we're only doing one thing we only focus on building the fastest most reliable best speech understanding system out there and so all of our time and energy goes into this one problem and so i think the
question is like if we just do this one thing can we do it really well for businesses i'm like Time will tell. We should do, like, a follow-up in six months and see, like, where we're at. But, like, that's – at least that's a strategy that we're taking.
No, I think that makes sense. Like, the open source angle and the enterprise angle is, I think, a very valid point. So – and, like, just to clarify for myself, do you guys – Like when you build like a speech, speech model, like speech, speech to speech or speech to, I don't know, speech to LLM, I guess.
Speech attacks. Yeah. Speech attacks. Yeah. Yeah. Not speech attacks, but speech to LLM, right? LLM. Oh, I see. I see what you're saying. I see what you're saying. Yeah. Got it. But do you have to like, if you want to change the, replace the, the underlying model, you need to do like full training again.
Is that how it works?
Yes, if the model is completely different, yeah, we will retrain. But there's a couple of nuanced points there.
Can you do, like, a checkpoint and then, like, fine-tune? Or it's just impossible? Yeah,
if it's in, like, the same embedding space, but, like, you cannot, for example, take an UltraVox adapter trained on Llama and expect it to apply to the world of Mistral. Like, those are two different. But, for example, like, when 3.3 came out with Llama, like, that was just a fine-tune of our projector.
uh and and that was that was very short and easy and so we upgraded our model behind the scenes from ultra box to 3.3 like overnight basically oh and we can also like reapply the same adapter to any fine tune as well like particularly laura's
all work out of the box uh without any need to retrain but yeah like if like a brand new but yeah you cannot use a projector like mistral to make it work with like jimma from google like that won't work because like they're in embedding spaces of course completely completely separate
Yeah. No, I love it. Look, let's talk about two years in. My last question always, how do you imagine the voice AI space in two years? I mean, it's a big, difficult, difficult one. But it's a fun one. Yeah, I mean, I used to say five years, but I'm down to two now because it's just...
Exactly. I feel like I got asked this question from a candidate. He's like, so what do you see the world like in five years? And I was like, I don't even know. Like if I think about when we started the company in 2022, like the best model was GPT-3.
And like, and now here we are in late 2024 and like GPT-3 is like, haha, what a dumb model. And the pace is insane. And so it's always a little bit hard. But I think from our vantage point, I think what we're really hoping to get to over the next couple of years are AIs
that are real collaborators. And I think that if you think about if you work in a company right it's in the larger the company the more time you spend in meetings because like uh the hard part of getting stuff done uh oftentimes it's not like the work
itself it's like the coordination around the work oh yeah um and uh i think what i like what the future i'm imagining is where like a lot of the like those collaborations are like always joint collaborations between humans and ais uh and so we've got ais like in the video call for example
And like right now, like all we get are like glorified note takers, right? Because we can't, they're not capable of participating in the dialogue yet. They don't understand multiple speakers. They don't understand like, like the rules of multi-person dialogue and when to interject. But like,
so like this bridge from like where we are now into the real world is like what I'm the most excited by and I think is totally possible. you know, you've got like, you've got more investment in humanoid robots over the last like nine months than like, I feel like the decade previously. So everyone's excited by this,
but like, but if you think about what it's going to take to make those robots be able to actually like dialogue in the real world, like a retail store where there's all these different speakers and like, like all the systems right now would completely fall flat. So I think like over the next couple of years,
I think we go from these things as like largely behind the scenes actors who you don't really trust with anything super important and get easily confused into like primary collaborators that we like look to more and more as like to help us refine ideas, lead meetings, like empathize a little bit.
I think these are sort of what's possible at the current trend lines and like think what, and like that's what I'm like most excited by. And so I sort of view it as These days, we're sort of plucking the low-hanging fruit of voice AI. But the real future, I think, is really around this deep collaboration concept.
And that's really where voice is best served. Because, like, again, whenever we have a complex problem, like if you and I were debating something on, like, crisp models, for example, we would almost guaranteed want to get in a meeting, right? Because going back and forth on Slack and text, this doesn't allow you to, like,
have the richness and speed of dialogue. Exactly. So, like, that's what I'm excited by.
we lose context and it's just like way more natural. And I think the moment you start to imagine this like collaborative meeting where there are like three agents and two people talking to each other, there are so many problems to solve there from tech perspective. And so there's a lot of value to be created and so on.
Yeah, I love that. I think that makes a lot of sense.
Yeah. And I feel like a lot of people sort of, I think like we fall into the trap of thinking like, oh, like voice AI is salt. Like we we've got, and it's like, and if you think about like how many, you know, I live in this space every day.
So I think it's a little bit different for us, but. Like it's like I have a list of like a hundred problems that have to be like addressed before we can even come even close to like making those things possible, right? Right now, our models still get confused.
Like if my daughter comes up and like ask me a question and the AI hears it, the AI like responds back to her. It's like, no, no, no, clearly that's my daughter and not me. Like, why don't you know that? And so we have so many obvious things to go off and solve on the speech
understanding side first, I think. But rich problem space.
Very cool, Zach. I think this was great. I really would like to follow up in six months, nine months and see where you guys, I'm like very fascinated in this technology. And yeah, thanks so much for your insights and time.
Yeah, no, thank you. And thanks to Chris for like the great models that we're already working with. And so thanks for what you guys do as well. Sounds great. Thanks, Zach. Thanks. Thanks.
Ready for more?
Type your email...
Subscribe
© 2026 Krisp Technologies · Privacy ∙ Terms ∙ Collection notice
Start your Substack
Get the app
Substack is the home for great culture
Hyper Icon
