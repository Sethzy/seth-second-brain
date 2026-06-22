---
type: raw_capture
source_type: x
url: https://x.com/HrubyOnRails/status/2022039848048361807
original_url: https://x.com/HrubyOnRails/status/2022039848048361807
author: "Rich\u00e1rd Hruby"
handle: HrubyOnRails
status_id: 2022039848048361807
captured_at: 2026-06-19T20:44:48+08:00
published_at: "Thu Feb 12 20:07:22 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 16
  reposts: 18
  likes: 228
---

# X post by @HrubyOnRails

## Source

- Original: [https://x.com/HrubyOnRails/status/2022039848048361807](https://x.com/HrubyOnRails/status/2022039848048361807)
- Canonical: [https://x.com/HrubyOnRails/status/2022039848048361807](https://x.com/HrubyOnRails/status/2022039848048361807)
- Author: Richárd Hruby (@HrubyOnRails)

## Verbatim Text

I replaced 100 login scripts with a browser agent loop

Most websites have a login flow. None of them look the same.

Some have email first, then password on a second screen. Some combine both. Most throw a CAPTCHA. Some ask you to pick a workspace. Some show a cookie banner to dismiss before you can do anything.

If you're building browser agents for authenticated use cases, this is your nightmare.

At [Anon](https://anon.com/), I've spent the last year building infrastructure that lets AI agents act on behalf of users across the web.

In the past, logging into hundreds of different services programmatically meant writing a dedicated login state machine for every single provider. Each one was a brittle mess. Hardcoded selectors and transitions. Everything breaks when a site ships a redesign on a Tuesday afternoon.

This is why I built the Login Machine ([GitHub](https://github.com/RichardHruby/login-machine), [hosted demo](https://login-machine.vercel.app/)).

One loop: screenshot the page, ask an LLM what it sees, programmatically act on the structured response. No hard coded scripts, works for any login!

Here's how I did it, and how you can replicate it 👇

---

# Why This Works (and why scripts don't)

Before I walk through the implementation, read this because it might change how you think about browser automation entirely.

Traditional login automation treats every provider as a known, static flow (a state machine if you will). You write a Playwright script like this:

```typescript
await page.fill('#email', credentials.email);
await page.fill('#password', credentials.password);
await page.click('button[type="submit"]');
```

This works until the site renames #email to #username, a cookie banner covers the submit button, or the flow adds an MFA step you didn't account for.

For one provider, you can maintain this. For ten, it's annoying. For a hundred, it's untenable.

At scale, it is the combinatorial explosion of cases that really kills this… (RIP ✝︎)

Different account types (member, admin, external admin, users with multiple roles etc.) behave differently across login flows. Multiply the providers by the account types by the flow variations and you get hundreds of possible paths through every login.

But wait… login pages are designed for humans. Every screen is self-contained. You can always deduce what to do without knowing the previous or next step.

An LLM with vision can do the same. Instead of hardcoding what each login page looks like, you send the model a screenshot and stripped-down HTML of the current page and ask:

> What kind of screen is this, and what are the interactive elements?

It returns structured data you can act on programmatically. That's the entire idea.

This also solves a problem of credential custody. When the LLM analyzes a page, its structured output describes exactly what fields are needed (an email, a password, a workspace picker). That output becomes an input request you can surface to the user through a dynamic UI, a password manager API, or a secrets vault. Credentials flow transiently into the browser session and are never stored or surfaced to the LLM.

The Login Machine tells you what to ask for. You decide how to collect it.

---

# How It Works

The Core Loop

No hardcoded transitions. No state machine that assumes "after email comes password." After every action, the system takes a fresh screenshot, sends it to the LLM…

The browser runs in the cloud on [BrowserBase](https://www.browserbase.com/). No Docker containers to manage, no browser binaries to update. BrowserBase handles fingerprinting, residential proxies, and keeps the session alive server-side. I just connect via CDP, do my work, and disconnect.

## HTML Extraction + Screenshot: Preparing the prompt

I don't send raw HTML to the LLM. I gut it and send along a screenshot.

A typical login page has thousands of lines of scripts, stylesheets, SVGs, tracking pixels, and hidden elements that add zero signal. Sending all of that burns tokens and drowns the actual form fields in noise.

The extraction function walks the DOM recursively and is ruthless about what it keeps:

```typescript
const extractBodyHTML = () => {
  function extractHTML(node: Element): string {
    // Skip anything the user can't see
    const styles = window.getComputedStyle(node);
    if (styles.display === "none" || styles.visibility === "hidden") return "";

    // Kill all non-content tags
    const exclude = ["SCRIPT", "STYLE", "svg", "IMG", "NOSCRIPT", "LINK"];
    if (exclude.includes(node.tagName)) return "";

    // Traverse Shadow DOM boundaries
    const root = node.shadowRoot || node;

    let html = `<${node.tagName.toLowerCase()}`;
    // Keep only useful attributes (id, class, type, name, placeholder, role)
    for (const attr of node.attributes) {
      if (["id", "class", "type", "name", "placeholder", "role", "aria-label"]
        .includes(attr.name)) {
        html += ` ${attr.name}="${attr.value}"`;
      }
    }
    html += ">";

    for (const child of root.children) {
      html += extractHTML(child);
    }

    html += `</${node.tagName.toLowerCase()}>`;
    return html;
  }
  return extractHTML(document.body);
};
```

Three things matter here:

1. Shadow DOM traversal - Many modern login forms (especially enterprise SSO widgets) live behind Shadow DOM boundaries. If you only walk node.children, you miss them entirely. Checking node.shadowRoot catches these.

2. Aggressive tag stripping - Scripts, styles, SVGs, images, no script blocks, link tags all gone. They contribute nothing to form identification and massively inflate token count.

3. Attribute filtering - Even on the tags we keep, we strip most attributes. The LLM doesn't need data-analytics-id or aria-describedby. It needs id, name, type, placeholder, the things that help it generate a working Playwright locator.

The iframe content gets extracted separately and appended with explicit tags:

```typescript
for (const frame of page.frames()) {
  if (frame !== page.mainFrame()) {
    const iframeHtml = await frame.evaluate(extractBodyHTML);
    bodyHtml += `<iframe-content>${iframeHtml}</iframe-content>`;
  }
}
```

This cut token usage by roughly 10x on complex pages like Amazon's login flow. And the LLM makes better decisions with less noise, fewer hallucinated locators, faster classification.

Along with all this, a screenshot helps the LLM with visual clues.

## Screen Classification: structured output screen types

I define six screen types, each with a strict Zod schema. [Vercel AI SDK](https://sdk.vercel.ai/)'s generateText with Output.object makes this straightforward. I pass a Zod schema and get typed, validated output back. The LLM classifies every page into one of them:

credential_login_form

The most common. A page with input fields and a submit button. The LLM returns Playwright locators for every element:

```json
{
  "type": "credential_login_form",
  "inputs": [
    {
      "type": "email",
      "name": "email",
      "label": "Email address",
      "playwrightLocator": "#email"
    },
    {
      "type": "password",
      "name": "password",
      "label": "Password",
      "playwrightLocator": "#password"
    }
  ],
  "submit": {
    "type": "button",
    "label": "Sign In",
    "playwrightLocator": "button:has-text('Sign In')"
  }
}
```

The LLM doesn't just identify that there's a form. It generates the exact locators needed to interact with each element.

choice_screen

An account picker, workspace selector, or MFA method screen. No input fields, just clickable options:

```json
{
  "type": "choice_screen",
  "name": "account_selector",
  "label": "Choose an account",
  "options": [
    {
      "optionText": "Personal Account",
      "optionPlaywrightLocator": "button:has-text('Personal Account')"
    },
    {
      "optionText": "Business Account",
      "optionPlaywrightLocator": "button:has-text('Business Account')"
    }
  ],
  "submit": {
    "type": "button",
    "name": "continue",
    "label": "Continue",
    "playwrightLocator": "button:has-text('Continue')"
  }
}

```

The submit field is optional. Most choice screens don't need it because the options themselves are clickable. It's only included when the page requires selecting an option and then clicking a separate "Continue" button to confirm.

magic_login_link

A "check your email" screen. No input fields, just an instruction to the user:

```json
{
  "type": "magic_login_link",
  "instructionText": "Check your email for a sign-in link"
}
```

The handler surfaces this to the user and waits for them to paste the magic link URL, then navigates the browser to it.

blocked_screen

A cookie banner, popup, or modal blocking the login flow. The LLM finds the dismiss button and the system clicks it automatically, then re-analyzes.

loading_screen

The page isn't ready yet. The system waits and retries.

logged_in_screen

Terminal state. We're in. 🚀

## Screen Type Handlers: Acting on the Classification

I create programmatic handlers for every structured output above, hence the LLM never sees user credentials.

The LLM's job ends at classification. It returns structured data of the screen type, locators, field labels. Then a completely separate handler takes over and uses those locators to interact with the page programmatically.

For a credential_login_form, the handler creates an input request in the database describing what fields are needed. A dynamic UI surfaces that request to the user, who types their credentials directly. Those credentials flow transiently into the browser session, get filled into the form, and are discarded:

```typescript
async function handleCredentialForm(
  page: Page,
  screen: CredentialLoginForm,
  userInput: Record<string, string>
) {
  // Fill each field using the LLM-generated locators
  for (const input of screen.inputs) {
    const value = userInput[input.name];
    await fillInPageOrFrame(page, input.playwrightLocator, value);
  }

  // Click submit if present
  if (screen.submit) {
    await clickInPageOrFrame(page, screen.submit.playwrightLocator);
  }
}
```

The LLM told us where the email field is (#email). It never sees what the user types into it. Credentials pass from the user's browser directly into the login form. They're never sent to the LLM, never logged, never stored.

For choice_screen, the handler presents the options to the user and clicks their selection. For blocked_screen, it clicks the dismiss button automatically.  No user input needed. For loading_screen, it waits and re-screenshots. Each handler is simple because the LLM already did the hard work of understanding the page.

## Putting It All Together: Multi step flows with dynamic UI

Here's a real four-step login showing the full system in action:

Email → Password → MFA → Account Selection → Logged In.

Four different screen types, handled by the same loop. The system didn't need to know this provider has four steps. It just kept looking at the page and responding to what it saw. At every step, the UI that collected user input was generated dynamically from the LLM's page analysis. Credentials flowed transiently through the browser session and were never stored.

This is the part that made me delete my state machines with zero regret. The LLM figures out the flow. The database mediates the handoff. The UI renders whatever the AI discovers. I didn't have to anticipate anything.

---

# Handling the Real World

Login pages in the wild are messy. A few things I had to solve that aren't obvious:

## Validation

Asking an LLM to generate Playwright locators sounds risky. What if it hallucinates a selector that doesn't exist?

I don't simply trust the LLM output. I validate every locator against the page before acting on it.

Here's the core of it:

```typescript
const { output: screen } = await generateText({
  model: anthropic("claude-sonnet-4-5-20250929"),
  output: Output.object({ schema: LoginStateSchema }),  // Zod schema
  system: LOGIN_SCREEN_SYSTEM_PROMPT,
  messages,
});

// Validate ALL locators exist on the live page
const locators = getScreenLocators(screen);
const results = await Promise.all(
  locators.map(async (loc) => ({
    locator: loc,
    exists: await validateLocator(session, loc),
  })),
);

const missing = results.filter((r) => !r.exists);
if (missing.length > 0) {
  // Validation failed — feed errors back for retry
  throw new Error(`Locators not found: ${missing.map((m) => m.locator).join(", ")}`);
}
```

Three layers of validation:

1. Zod schema parsing - The LLM output must conform to the exact shape I expect. If it returns garbage structure, it's rejected before I even check the DOM.

2. Element existence -  Every Playwright locator is checked against the live DOM, including all iframes. If the LLM says #login-button exists but it doesn't, validation fails.

3. Retry with context - If validation fails, the error is fed back to the LLM for self-correction.

## Self-Correction via Error History

When a locator fails validation, the system doesn't just retry blindly. It tells the LLM what went wrong:

```typescript
const MAX_ANALYSIS_RETRIES = 3;
const errorHistory: Array<{ error: string }> = [];

for (let attempt = 0; attempt < MAX_ANALYSIS_RETRIES; attempt++) {
  // Build context from previous failures
  const errorContext = errorHistory.length > 0
    ? `\n\n<error-history>\n${errorHistory.map((e, i) =>
        `Attempt ${i + 1}: ${e.error}`
      ).join("\n")}\n</error-history>`
    : "";

  const { output: screen } = await generateText({
    model: anthropic("claude-sonnet-4-5-20250929"),
    output: Output.object({ schema: LoginStateSchema }),
    system: LOGIN_SCREEN_SYSTEM_PROMPT,
    messages: [{
      role: "user",
      content: [
        { type: "text", text: `Current URL: ${url}\n\nHTML:\n${html}${errorContext}` },
        { type: "image", image: `data:image/jpeg;base64,${screenshot}` },
      ],
    }],
  });

  // Validate locators against the live DOM
  const locators = getScreenLocators(screen);
  const missing = /* ... check each locator ... */;

  if (missing.length === 0) return screen; // All locators valid

  errorHistory.push({
    error: `Locators not found: ${missing.map((m) => m.locator).join(", ")}`,
  });
}
```

The LLM sees its previous attempts and the specific validation errors. It learns from its mistakes within a single login attempt. Attempt 1 might generate #login-button which doesn't exist, so attempt 2 tries button[type="submit"] instead.

This is the same "feedback loop for self-correction" pattern that Netflix uses in their [text-to-query work](https://netflixtechblog.com/the-ai-evolution-of-graph-search-at-netflix-d416ec5b1151), validating LLM output against a known schema and feeding errors back for re-generation. They apply it to DSL generation. I apply it to browser automation. Same idea.

## CAPTCHAs

I'm excluding CAPTCHA handling from this demo... It's a rabbit hole that deserves its own post. But here's what I learned the hard way:

The best CAPTCHA solution is not seeing one in the first place. Residential proxies and proper browser fingerprinting eliminate most challenges before they appear. After that, it's a stack of fallbacks: browser-level CDP commands, vendor-specific solutions like [Browserbase's advanced stealth mode](https://docs.browserbase.com/guides/stealth-customization), and dedicated solvers like [2Captcha](https://2captcha.com/) for the rest.

The Login Machine itself doesn't understand CAPTCHAs. It just needs the page to be clear before the LLM can analyze it. In the production implementation CAPTCHAs are checked before and after every form submission, if one shows up, it gets handled at the infrastructure layer, and then the Login Machine continues as if nothing happened.

---

# Why This Works

Three design decisions make this system reliable:

1. Observe, don't assume. Every action is followed by a fresh page analysis. The system never guesses what screen comes next.

2. Validate before acting. LLM outputs are checked against the live DOM. Hallucinated selectors are caught and corrected before they cause errors.

3. Fail forward with context. When something goes wrong, the error becomes part of the next attempt's context. The LLM doesn't repeat the same mistake.

The result: a single system that handles Target, Amazon, Home Depot, QuickBooks, and any other login page without a single line of provider-specific code.

---

# The Stack

LLM - Claude Sonnet 4.5 via [Vercel AI SDK](https://ai-sdk.dev/)

Structured Output - Zod schemas + Vercel AI SDK generateText

Browser Automation - Playwright via CDP on [BrowserBase](https://www.browserbase.com/)

Frontend - Next.js 16, React 19, Tailwind 4

Validation - Zod schema parsing + live DOM locator checks

---

# What's Next

I'm open-sourcing the Login Machine. You can try the [hosted demo](https://login-machine.vercel.app/) or check out the code on [GitHub](https://github.com/RichardHruby/login-machine).

If you're building AI agents that need to interact with authenticated web services, you may find this a useful starting point.

Built at [Anon](https://anon.com/) by [Richard](https://github.com/RichardHruby) and [Jesse](https://github.com/jesse-olympus).

## X Article Metadata

- Title: I replaced 100 login scripts with a browser agent loop
- Preview: Most websites have a login flow. None of them look the same.
Some have email first, then password on a second screen. Some combine both. Most throw a CAPTCHA. Some ask you to pick a workspace. Some

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
