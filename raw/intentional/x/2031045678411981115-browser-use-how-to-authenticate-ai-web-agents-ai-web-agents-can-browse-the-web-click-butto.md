---
type: raw_capture
source_type: x
url: https://x.com/browser_use/status/2031045678411981115
original_url: https://x.com/browser_use/status/2031045678411981115
author: "Browser Use"
handle: browser_use
status_id: 2031045678411981115
captured_at: 2026-06-19T21:43:14+08:00
published_at: "Mon Mar 09 16:33:19 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 4
  reposts: 22
  likes: 231
---

# X post by @browser_use

## Source

- Original: [https://x.com/browser_use/status/2031045678411981115](https://x.com/browser_use/status/2031045678411981115)
- Canonical: [https://x.com/browser_use/status/2031045678411981115](https://x.com/browser_use/status/2031045678411981115)
- Author: Browser Use (@browser_use)

## Verbatim Text

How to Authenticate AI Web Agents

AI web agents can browse the web, click buttons, fill forms, and extract data. They can do almost anything a human can do online...except log in.

Authentication isn't a minor inconvenience; it prevents agents from completing tasks truly useful to you. Unauthenticated agents can't check your email, manage your calendar, or process a return.

Here's how to enable your agents to securely authenticate with your accounts, so they can access the services you use.

---

# Cookie Syncing

When you log into a website, your browser stores cookies that prove you're authenticated. On future visits, your browser automatically sends these cookies back, so the server recognizes you without another login.

Cookie syncing copies your browser's cookie store to the agent's browser. Since the browser now has the same cookies, each website treats the agent as "you."

Browser Use supports syncing your real Chrome profile to the cloud with a single terminal command. You can also export cookies as a file.

```python
# Sync your Chrome profile to Browser Use Cloud
# export BROWSER_USE_API_KEY=your_key && curl -fsSL https://browser-use.com/profile.sh | sh

# Or use your Chrome profile directly (OSS)
browser = Browser.from_system_chrome()

# Or export cookies for use anywhere (OSS)
await browser.export_storage_state('auth.json')
browser = Browser(storage_state='auth.json')
```

---

# Password Managers

Password managers like 1Password let agents retrieve credentials from a vault and fill login forms automatically. This includes stored TOTP codes — the 6-digit codes from authenticator apps that refresh every 30 seconds.

The agent never sees your actual passwords, and values are filled programmatically.

Connect your 1Password service account in [Cloud settings](https://cloud.browser-use.com/settings?tab=secrets), and the agent automatically retrieves and fills credentials. In the open-source library, use the [1Password SDK](https://github.com/1Password/onepassword-sdk-python) with a custom tool.

---

# Two-Factor Authentication (2FA)

Many sites require a second factor after your password. The most common type is TOTP. These codes are derived from a shared secret key and the current time, refreshing every 30 seconds.

If you have the secret key, you can generate these codes programmatically without having to use an authenticator app.

Browser Use generates TOTP codes automatically. Use placeholders ending in `bu_2fa_code`, and fresh codes are generated at input time:

```python
agent = Agent(
    task='Go to example.com/login, enter x_user, x_pass, and x_bu_2fa_code',
    sensitive_data={
        'x_user': 'myusername',
        'x_pass': 'mypassword',
        'x_bu_2fa_code': 'JBSWY3DPEHPK3PXP',  # TOTP secret key
    },
)
```

The agent never sees your actual credentials, only placeholder names. Values are injected directly into the page.

Where to find your TOTP secret: During 2FA setup, look for "manual entry" or "can't scan QR code." In 1Password, edit the item and reveal the one-time password secret.

---

# Email & SMS Verification

Some sites send verification codes via email or SMS instead of using TOTP. You can send these codes to an inbox managed by your agent so it can complete the verification.

[AgentMail](https://docs.agentmail.to/welcome) is a standalone API for creating agent-managed inboxes. You create an inbox, use that email when signing up or verifying, then poll for the incoming code.

Pair AgentMail with a custom tool to create inboxes for agent verification:

```python
inbox = await email_client.inboxes.create()

@tools.registry.action('Get verification code from email')
async def get_verification_code():
    emails = await email_client.inboxes.messages.list(inbox_id=inbox.inbox_id)
    if emails.messages:
        return ActionResult(extracted_content=emails.messages[0].text)
    return ActionResult(error='No emails yet')
```

---

# The Bigger Picture

Right now, we're in an odd moment. Agents have become remarkably capable, but the infrastructure they operate on was built for humans. There's no native authentication framework for autonomous agents that's been widely adopted, so the techniques in this guide are our best workarounds.

The methods above — cookie syncing, password managers, TOTP generation, and persistent hosted browsers — let agents access your accounts today.

And when agent-native authentication arrives, Browser Use will be pioneering it.

---

Full documentation: [Authentication Guide](https://docs.browser-use.com/customize/browser/authentication) | [Cloud Authentication](https://docs.cloud.browser-use.com/usage/authentication)

## X Article Metadata

- Title: How to Authenticate AI Web Agents
- Preview: AI web agents can browse the web, click buttons, fill forms, and extract data. They can do almost anything a human can do online...except log in.
Authentication isn't a minor inconvenience; it

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
