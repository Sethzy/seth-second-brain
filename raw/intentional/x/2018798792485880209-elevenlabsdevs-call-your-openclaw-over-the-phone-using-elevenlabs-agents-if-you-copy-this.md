---
type: raw_capture
source_type: x
url: https://x.com/ElevenLabsDevs/status/2018798792485880209
original_url: https://x.com/ElevenLabsDevs/status/2018798792485880209
author: "ElevenLabs Developers"
handle: ElevenLabsDevs
status_id: 2018798792485880209
captured_at: 2026-06-19T20:16:00+08:00
published_at: "Tue Feb 03 21:28:34 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 65
  reposts: 178
  likes: 1883
---

# X post by @ElevenLabsDevs

## Source

- Original: [https://x.com/ElevenLabsDevs/status/2018798792485880209](https://x.com/ElevenLabsDevs/status/2018798792485880209)
- Canonical: [https://x.com/ElevenLabsDevs/status/2018798792485880209](https://x.com/ElevenLabsDevs/status/2018798792485880209)
- Author: ElevenLabs Developers (@ElevenLabsDevs)

## Verbatim Text

Call Your OpenClaw over the phone using ElevenLabs Agents

if you copy this article to your coding agent, it can perform many steps from it for you

What if you could simply call your OpenClaw bot and ask how your coding agent is doing? Or ask it to remember something while you're driving? Or perhaps get a digest of recent moltbook bangers?

While OpenClaw supports text-to-speech and speech-to-text out of the box, it takes effort to make it truly conversational.

ElevenLabs Agents platform orchestrates all things voice, leaving your OpenClaw to be the brains.

## The Architecture

ElevenLabs Agents handle turn taking, speech synthesis and recognition, phone integration, and other voice related things. 

OpenClaw handles tools, memory and skills. 

Systems interact using standard OpenAI /chat/completions protocol.

## Prerequisites

- ElevenLabs account

- OpenClaw installed and running

- ngrok installed

- A Twilio account (if you want phone numbers)

## Setting Up OpenClaw

In your openclaw.json, enable the chat completions endpoint:

```json
{
    "gateway": {
        "http": {
            "endpoints": {
                "chatCompletions": {
                    "enabled": true
                }
            }
        }
    }
}
```

This exposes /v1/chat/completions on your gateway port. That's the universal endpoint ElevenLabs will use to interact with your OpenClaw.

## Exposing Your Claw with ngrok

Start your tunnel:

```bash
ngrok http 18789
```

(Replace 18789 with whatever port your gateway runs on.)

ngrok gives you a public URL like \[https://your-unique-url.ngrok.io\](https://abc123.ngrok.io/). Keep this terminal open — you'll need that URL for the next step.

## Configuring ElevenLabs

In the ElevenLabs Agent:

1. Create a new ElevenLabs Agent

2. Under LLM settings, select Custom LLM

1. Set the URL to your ngrok endpoint: [https://](https://abc123.ngrok.io/v1/chat/completions)[your-unique-url](https://abc123.ngrok.io/)[.ngrok.io/v1/chat/completions\](https://abc123.ngrok.io/v1/chat/completions)

2. Add your OpenClaw gateway token as the authentication header

Alternatively, instead of manually following the steps above, your coding agent can make these requests:

```
Step 1: Create the secret
curl -X POST https://api.elevenlabs.io/v1/convai/secrets \
-H "xi-api-key: YOUR_ELEVENLABS_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"type": "new",
"name": "openclaw_gateway_token",
"value": "YOUR_OPENCLAW_GATEWAY_TOKEN"
}'
This returns a response with secret_id:
{"type":"stored","secret_id":"abc123...","name":"openclaw_gateway_token"}
Step 2: Create the agent
curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \
-H "xi-api-key: YOUR_ELEVENLABS_API_KEY" \
-H "Content-Type: application/json" \
-d '{
"conversation_config": {
"agent": {
"language": "en",
"prompt": {"llm": "custom-llm", "prompt": "You are a helpful assistant.", "custom_llm": {"url": "https://YOUR_NGROK_URL.ngrok-free.app/v1/chat/completions", "api_key": {"secret_id": "RETURNED_SECRET_ID"}}}}}}'
Replace:
- YOUR_ELEVENLABS_API_KEY - your ElevenLabs API key
- YOUR_OPENCLAW_GATEWAY_TOKEN - from ~/.openclaw/openclaw.json under gateway.auth.token
- YOUR_NGROK_URL - your ngrok subdomain
- RETURNED_SECRET_ID - the secret_id from step 1
```

ElevenLabs will now route all conversation turns through your Claw. It sends the full message history on each turn, so your assistant has complete context.

At this stage, you can already talk to your OpenClaw bot using your ElevenLabs agent!

## Attaching a Phone Number

This is where it gets interesting.

1. In Twilio, purchase a phone number

2. In the ElevenLabs agent settings, go to the Phone section

1. Enter your Twilio credentials (Account SID and Auth Token)

2. Connect your Twilio number to the agent

That's it. Your Claw now answers the phone! 🦞

## X Article Metadata

- Title: Call Your OpenClaw over the phone using ElevenLabs Agents
- Preview: if you copy this article to your coding agent, it can perform many steps from it for you
What if you could simply call your OpenClaw bot and ask how your coding agent is doing? Or ask it to remember

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
