---
type: raw_capture
source_type: pasted
title: "Archive note: Telegram wrapper.md"
url: "file:///Users/sethlim/Desktop/Archive/Telegram%20wrapper.md"
collected_at: 2026-06-11T02:20:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Desktop/Archive/Telegram wrapper.md"
sha256: "07d91c97408c3237c32912312c3957210a9334519a9dc4c71120624dfac12104"
---

# Archive note: Telegram wrapper.md

Source file: `/Users/sethlim/Desktop/Archive/Telegram wrapper.md`

## Capture Text

  
**Telegram wrapper **  
  
[https://x.com/bennyautomatic/status/2032563469208399910](https://x.com/bennyautomatic/status/2032563469208399910)   
[https://x.com/bennyautomatic/status/2032563469208399910](https://x.com/bennyautomatic/status/2032563469208399910)   
  
In the folder where my slack.ts context file from earlier was, I created a dead-simple API wrapper.  Just Slack's WebClient with thin functions for postMessage, getChannelHistory, listChannels, and getUserInfo—plus a channel allowlist to prevent little Pim from posting somewhere it shouldn't. Then I created AI SDK tools that wrap those functions: a Zod schema for input, a Zod schema for output, and an execute function that calls the client. The tool-set export is just an object with all the tools:  
typescript  
export const SLACK_TOOLS = {  
    postSlackMessageTool,  
    getSlackChannelHistoryTool,  
    listSlackChannelsTool,  
    getSlackUserTool,  
    listSlackUsersTool,  
};  
Pass that to the agent, and it can read and write Slack.  
  
Then I had our first agent, that solved a critical use case (not). But it proved the stack worked end-to-end.   
typescript  
const { text, steps } = await goodMorningAgent.generate({  
    prompt: "Post a good morning message, and a random motivational quote to #pim-scratchpad.",  
});  
   
  
  
  
**Exa for research **  
**Exa for research **  
  
  
using ++[@ExaAILabs](https://x.com/@ExaAILabs)++ to research their LinkedIn profile and company background, and posting a rich notification to Slack with all the intel, plus a threaded reply with deeper research.   
  
  
**Instead of skills, do I just configure it in user preferences? **  
  
  
**This is the lead agent's full prompt. **  
  
  
export const prompt = `${CORE_CONTEXT}  
  
${SLACK_CONTEXT}  
  
${ATTIO_CONTEXT}  
  
${POSTHOG_CONTEXT}  
  
${EXA_CONTEXT}  
  
## Your Task  
  
You've been given a specific lead to process. Research them and post a notification to #alerts-leads.  
  
## Step-by-Step Process  
  
### 1. Look Up the Person in Attio  
Use the Person Record ID provided in your prompt to fetch the person's details from Attio.  
If the person's "Qualification" field is "Unqualified", stop here and return without posting anything.  
  
### 2. Conduct Research  
- Use the Attio MCP tools to get all data about the lead and their company - have we spoken with them before?  
- Use the PostHog MCP tools to get the session data (if Posthog Session ID exists on the person). Get their initial referrer, UTM tags, and pages visited.  
- Use the Exa MCP to find the person's LinkedIn profile and research who they are - role, location, background.  
- Use the Exa MCP to research the company - what do they do, employee count, fundraising, HQ location.  
  
### 3. Post Main Notification  
  
Post to #alerts-leads using Slack Block Kit to make a visually digestible alert.  
  
### 4. Post Thread Details  
Reply in thread with deeper research:  
- What pages did they visit on the website? (from PostHog session)  
- Lead source and how they found us (from PostHog UTMs/referrer)  
- What do we know about the company from Attio and Exa?  
- Person's professional background from LinkedIn  
- ICP fit - is this person a buyer? Is their company a fit for our ICP?  
  
### 5. If lead source is unset in Attio, you may set it to what you were able to suss out from your research - at the end of the thread, you must call out that you did that, and you must always use an existing lead source select option, never create a new one.   
`;  

