---
type: raw_capture
source_type: x
title: "Sunder sync: 56-twitter-tokifyi-free-custom-email-cloudflare-gmail-FULL.md"
url: "https://x.com/tokifyi"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/56-twitter-tokifyi-free-custom-email-cloudflare-gmail-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/56-twitter-tokifyi-free-custom-email-cloudflare-gmail-FULL.md"
sha256: "1132aeedfbf08c056755bb7425880a4e9320709d97917b282387e2c1896a4262"
duplicate_of: ""
---

# Sunder sync: 56-twitter-tokifyi-free-custom-email-cloudflare-gmail-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/56-twitter-tokifyi-free-custom-email-cloudflare-gmail-FULL.md`

Primary URL: https://x.com/tokifyi

Duplicate of existing source-map entry: `none`

## Capture Text

# Free Custom Email Address Using Cloudflare + Gmail

**Source:** https://x.com/tokifyi (Article)
**Author:** @tokifyi
**Date:** February 23, 2026
**Views:** 1.7M

## Summary

Get a custom email address for FREE using Cloudflare Email Routing + Gmail. Most people pay $6-12/month for Google Workspace or Microsoft 365 just to get a custom email. This setup costs nothing except the domain itself.

## What You Need

- A domain name ($10-15/year from Namecheap, GoDaddy, etc. - students: free via GitHub Student Pack)
- A Gmail account (free)
- Cloudflare account (free)

## Step 1: Get a Domain

- Buy one from Namecheap, Porkbun, or any registrar
- Cheapest options: .xyz, .site, .online (~$2-5/year)
- Premium options: .com, .io, .ai (~$10-15/year)
- Students: Get free domains from GitHub Student Pack: https://education.github.com/pack
- Pick something short and memorable for your brand

## Step 2: Add Your Domain to Cloudflare

- Sign up at cloudflare.com (free plan works perfectly)
- Click "Add a site" and enter your domain
- Cloudflare will scan your DNS records
- Copy the two nameservers Cloudflare gives you
- Go back to your domain registrar and update the nameservers
- Wait about 5-10 minutes for DNS to propagate globally

## Step 3: Enable Email Routing

- In Cloudflare dashboard, go to Email → Email Routing
- Click "Get Started" to enable the feature
- Enter your Gmail address as the destination email
- Check your Gmail for a confirmation link from Cloudflare
- Click it to verify you own that inbox
- You're now ready to create custom addresses

## Step 4: Create Custom Email Addresses

- Click "Create address" in the Email Routing section
- Type the address you want: hello@, contact@, support@, sales@, hi@
- Choose where it forwards to (your Gmail)
- Click Save
- Repeat for unlimited addresses - they're all free
- Each one can go to the same Gmail or different inboxes

## Step 5: Send FROM Your Custom Email (Optional)

1. Open Gmail and go to Settings → See all settings
2. Click the "Accounts and Import" tab
3. Under "Send mail as", click "Add another email address"
4. Enter your name and your custom email (e.g. hello@yourdomain.com)
5. On the next page, Gmail will ask for SMTP server details
6. **Important:** Gmail will pre-populate the SMTP server with Cloudflare's MX record
7. Replace the pre-populated server with: `smtp.gmail.com`
8. Port: `587`
9. Username: your full Gmail address (e.g. you@gmail.com)
10. Password: a Google App Password (NOT your regular Gmail password)
11. To get an App Password: go to Google Account → Security → 2-Step Verification (enable it if you haven't) → App passwords → generate one for "Mail"
12. Click "Add Account"
13. Gmail will send a verification email to your custom address
14. Cloudflare forwards it right back to your Gmail inbox
15. Enter the confirmation code or click the verification link
16. Done. You can now send emails from your custom address directly in Gmail

## Step 6: Verify Your DNS Records

Cloudflare automatically sets up SPF, DKIM, and DMARC records when you enable email routing. You don't need to configure anything manually.

To double-check:
- Go to Cloudflare → DNS → Records
- You should see MX records pointing to Cloudflare
- You should see TXT records for SPF and DKIM already in place
- If anything looks off, try disabling and re-enabling email routing

**Note on DKIM:** Unlike Google Workspace, regular Gmail doesn't sign outgoing emails with your custom domain's DKIM key. This means some recipients might flag your emails. For personal and freelance use, the SPF record Cloudflare sets up is usually enough. If deliverability becomes an issue, that's when you'd consider upgrading to Google Workspace.

## The Result

- You receive emails at hello@yourdomain.com in your normal Gmail inbox
- You can reply from that address
- You look professional
- You pay $0/month for email (just the annual domain cost)
- No storage limits because it's using your free Gmail storage

## Important Limitations

- Cloudflare only forwards emails - it doesn't store them or provide a mailbox
- When sending via Gmail's "Send mail as", emails may go to spam initially (needs SPF/DKIM setup)
- Gmail limits: 500 emails sent per day from custom addresses
- Not ideal for high-volume business email or teams (stick with Google Workspace for that)

## Use Cases

**Perfect for:** freelancers, side projects, personal brands, small businesses, portfolio sites

**Not ideal for:** large teams, high-volume sales email, enterprises

## Cost Comparison

- This method: ~$10/year (domain only)
- Google Workspace: $72+/year ($6/mo)
- Microsoft 365: $144+/year ($12/mo)

