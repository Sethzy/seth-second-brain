---
type: raw_capture
source_type: x
url: https://x.com/tomcrawshaw01/status/2018348937208627380
original_url: https://x.com/tomcrawshaw01/status/2018348937208627380
author: "Tom"
handle: tomcrawshaw01
status_id: 2018348937208627380
captured_at: 2026-06-19T20:44:11+08:00
published_at: "Mon Feb 02 15:41:00 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 20
  reposts: 75
  likes: 738
---

# X post by @tomcrawshaw01

## Source

- Original: [https://x.com/tomcrawshaw01/status/2018348937208627380](https://x.com/tomcrawshaw01/status/2018348937208627380)
- Canonical: [https://x.com/tomcrawshaw01/status/2018348937208627380](https://x.com/tomcrawshaw01/status/2018348937208627380)
- Author: Tom (@tomcrawshaw01)

## Verbatim Text

The Secure Way to Self-Host OpenClaw on a VPS (Step-by-Step)

The default OpenClaw install has zero security. Ports exposed. No authentication. 900+ instances already found wide open. This step-by-step guide locks yours down with a private network, firewall, and token auth, all for just $6/month.

---

OpenClaw is the hottest AI tool right now.

People are dropping $700 on Mac Minis just to run it 24/7.

But here's what nobody's telling you:

If you set it up wrong, you're wide open.

Security researchers have already found 900+ instances with zero protection, ports exposed, API keys ready to steal.

One guy burned $300 in two days. He was the only one using it.

Set it up right, though?

This thing is a beast. You give it a task, it handles it. No babysitting.

This guide shows you how to lock it down on a VPS for just $6/month, no Mac Mini required.

## Want to Watch Me Set This Up in Real-Time?

I've got a full video walkthrough on my YouTube channel where I run the installation on my VPS and layer on the security protocol.

👉 https://youtu.be/qIJXGLfoxyg

If you'd rather follow along step-by-step in text, keep reading.

## The 5 Layers That Make Your Bot Invisible to Attackers

Tailscale — Creates a private encrypted network. Your bot becomes invisible to the public internet.

UFW Firewall — Blocks the bot's port from public access.

Token Auth — Requires a password to access the dashboard.

Fail2ban — Blocks hackers trying to brute-force your SSH.

Auto Updates — Keeps your server patched automatically.

By the time you're done, your OpenClaw instance won't exist to anyone who isn't on your private network.

## Before You Start (5-Minute Checklist)

- A VPS with OpenClaw already installed (I use [Hostinger](http://hostinger.com/GROWTHLAB))

- Access to your VPS terminal

- A Tailscale account (free at tailscale.com)

- Tailscale app on your laptop

That's it. Let's go.

## Get a VPS Running for $6/Month

I use Hostinger for all my VPS hosting.

It's what I run my self-hosted n8n on, and it's what we're using today.

They have a one-click Docker setup that makes installing OpenClaw dead simple.

But unfortunately  the default install has zero hardened security.

That's exactly what this guide fixes.

👉 [Get a Hostinger VPS here from just $6/mont](http://hostinger.com/GROWTHLAB)h

I'm using the $6.99/month plan for this walkthrough. If you're running heavy workloads, grab a bigger machine.

## Step 1: Install Tailscale on Your VPS

Open your VPS terminal and run:

curl -fsSL https://tailscale.com/install.sh | sh

Wait for it to complete.

## Step 2: Authenticate Tailscale

Run:

sudo tailscale up

This outputs a URL.

Copy it, open it in your browser, and log in to your Tailscale account to authorize the machine.

Confirm it worked:

tailscale ip -4

You should see a 100.x.x.x IP address.

This is your VPS's private Tailnet address, the first layer of invisibility.

## Step 3: Find Your Bot's Port

Run:

docker ps

Look for the port mapping in the output. It looks like:

0.0.0.0:44452->44452/tcp

Write down your port number. Yours will likely be different.

## Step 4: Set Up Tailscale Serve

Replace YOUR_PORT with the port number from Step 3:

sudo tailscale serve --bg http://localhost:YOUR_PORT

Check it's configured:

tailscale serve status

This shows your ts.net URL, something like:

https://srv1234567.tail8328fe.ts.net

Write this down. You'll need it to access your dashboard.

## Step 5: Install Tailscale on Your Laptop

1. Download the Tailscale app from their website

2. Sign in with the same account you used for your VPS

3. Test the connection by opening your ts.net URL in your phone's browser

If you see the OpenClaw dashboard (even with an auth error), it's working.

Your bot is now only accessible through your private network.

## Step 6: Configure the Firewall

Replace YOUR_PORT with your port number:

sudo ufw allow OpenSSH
sudo ufw allow in on tailscale0
sudo ufw deny YOUR_PORT
sudo ufw enable

Type y when asked to confirm.

This blocks the public internet from ever reaching your bot's port.

## Step 7: Verify Your Bot Is Actually Hidden

This should work:Access your ts.net URL from your phone (with Tailscale connected)

This should NOT work:Access http://YOUR_VPS_PUBLIC_IP:YOUR_PORT from any browser

If the public IP doesn't load, your firewall is doing its job.

You're no longer one of those 900 exposed instances.

## Step 8: Get Your Gateway Token

Run:

docker inspect $(docker ps -q) | grep -i OPENCLAW_GATEWAY_TOKEN

You'll see output like:

"OPENCLAW_GATEWAY_TOKEN=abc123def456ghi789jkl",

Copy the token (everything after the = sign, without quotes or comma).

This is your dashboard password.

## Step 9: Access Your Secured Dashboard

Your full dashboard URL format is:

https://YOUR_TAILSCALE_URL?token=YOUR_TOKEN

Example:

https://srv1234567.tail8328fe.ts.net?token=abc123def456ghi789jkl

You'll need this tokenized URL every time you access your dashboard.

No token = no access. That's the point.

## Step 10: Block Brute-Force Attacks with Fail2ban

This protects your VPS from hackers trying to guess your SSH password:

sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

Verify it's running:

sudo systemctl status fail2ban

Should show active (running) in green.

Anyone who tries to brute-force their way in gets automatically blocked.

## Step 11: Enable Auto Security Updates

Keep your server patched without thinking about it:

sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades

Select "Yes" when prompted.

Your server now patches itself. One less thing to worry about.

## Step 12: Telegram Setup

If you want to control your bot via Telegram:

Create a Telegram Bot:

1. Open Telegram and message @BotFather

2. Send /newbot

3. Choose a display name and username (must end with bot)

4. Save the token BotFather gives you

Get Your Telegram User ID:

1. Message @userinfobot on Telegram

2. Save the user ID it returns

Configure Allowlist:Add your bot token and user ID to your OpenClaw config so only YOU can message the bot.

Now you can talk to your AI agent from your phone, and nobody else can.

## Commands You'll Actually Use Again

Check Tailscale IP: tailscale ip -4

Check serve status: tailscale serve status

Check firewall status: sudo ufw status

Check bot is running: docker ps

View bot logs: docker logs $(docker ps -q)

Get gateway token: docker inspect $(docker ps -q) | grep -i OPENCLAW_GATEWAY_TOKEN

Bookmark this. You'll come back to it.

## Your Bot Is Now Invisible to the Public Internet

Here's what you just installed:

✅ Private network access only (Tailscale)

✅ Public port blocked (UFW Firewall)

✅ Dashboard password protected (Token Auth)

✅ SSH brute-force protection (Fail2ban)

✅ Auto security updates enabled

You're no longer one of those 900 exposed installations that security researchers are finding.

Your API keys are safe.

Your Anthropic bill is safe.

You can actually sleep at night.

## Now You Can Actually Use This Thing

I'm not going deep on how to USE OpenClaw in this guide, that's a separate tutorial.

But now that you've got it locked down, you can start experimenting.

Give it tasks.

Let it run.

See what it can build for you.

This isn't a chatbot you babysit. It's an AI agent with its own brain.

And now it's yours, secured and ready to go.

## Stuck? Here's How to Fix It

If something breaks or you hit a wall, here's what to do:

1. Copy the error message

2. Paste it into Claude

3. Tell it what step you're on

It'll sort you out.

Or drop your question in the comments, I'll help where I can.

## Watch the Full Setup

Want to see me do this live? The full video walkthrough is on my YouTube:

👉 https://youtu.be/qIJXGLfoxyg

That's everything.

Now go build something.

## X Article Metadata

- Title: The Secure Way to Self-Host OpenClaw on a VPS (Step-by-Step)
- Preview: The default OpenClaw install has zero security. Ports exposed. No authentication. 900+ instances already found wide open. This step-by-step guide locks yours down with a private network, firewall, and

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
