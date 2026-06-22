---
type: raw_capture
source_type: x
url: https://x.com/Sprytixl/status/2063600671304057114
original_url: https://x.com/Sprytixl/status/2063600671304057114
author: "Sprytix"
handle: Sprytixl
status_id: 2063600671304057114
captured_at: 2026-06-19T23:41:11+08:00
published_at: "Sun Jun 07 12:35:14 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 10
  reposts: 8
  likes: 98
---

# X post by @Sprytixl

## Source

- Original: [https://x.com/Sprytixl/status/2063600671304057114](https://x.com/Sprytixl/status/2063600671304057114)
- Canonical: [https://x.com/Sprytixl/status/2063600671304057114](https://x.com/Sprytixl/status/2063600671304057114)
- Author: Sprytix (@Sprytixl)

## Verbatim Text

How to build a browser game with Claude Code in a weekend and turn it into $10,000/month.

Most people think building a game requires a team - a designer, a developer, a QA engineer, someone to handle the backend and someone to manage the release. 

That was true two years ago. Right now one person with Claude Code and the right repositories can cover all of those roles in a single weekend and have a playable product with a subscription model ready to launch by Sunday evening.

The indie game market generates billions every year and the games making the most money per developer hour aren't the massive AAA titles - they're small focused browser games with daily streaks, leaderboards and $4.99-9.99 monthly subscriptions that players keep because breaking the streak feels worse than paying the fee.

> Bookmark This and follow - I'm Sprytix, a developer who builds AI systems and automation pipelines that turn technology into real income. DMs open.

Here's the exact stack, the repositories and the prompts to build one this weekend.

```
What you're building:
Game engine:     Phaser + React + TypeScript
Product layer:   Next.js SaaS starter
Payments:        Stripe
Deploy:          Vercel
AI studio:       Claude Code + Claude Code Game Studios
                 (49 agents, 73 skills, 12 hooks)

Time to playable MVP:    one weekend
Monthly revenue ceiling: $10,000+ with 1,000 subscribers at $9.99
Infrastructure cost:     under $50/month
```

Why browser games specifically

Mobile app stores take 30% of every dollar and require Apple review which can take weeks. Browser games deploy in minutes, keep 97% of revenue through Stripe and work on every device without an app store. The player opens a link and they're playing - no download, no install, no friction between your marketing and your first paying user.

The games that build sustainable subscription revenue share three mechanics: a daily streak that players don't want to break, a leaderboard that creates social competition and a progression system that makes tomorrow feel more valuable than today. These aren't complex to build - they're just specific design decisions that Claude Code can implement in hours once you know to ask for them.

The repositories that make this possible

Instead of building from scratch you give Claude Code existing open source projects as reference and it assembles your product from the best parts of each. This saves days of boilerplate work and lets you focus on what makes your game unique.

```
Claude-Code-Game-Studios
- 49 AI agents, 73 skills, 12 hooks
- turns Claude Code into a full game studio
- Game Director, Design Lead, Engineering Lead, Art Lead, QA, Release
- github.com/Donchitos/Claude-Code-Game-Studios

phaserjs/template-react-ts
- official Phaser 3 + React + TypeScript + Vite template
- React to Phaser bridge built in
- hot reload, production build scripts
- github.com/phaserjs/template-react-ts

nextjs/saas-starter
- auth, Stripe payments, dashboard out of the box
- handles subscriptions, webhooks, user accounts
- github.com/nextjs/saas-starter

HermeticOrmus/claude-code-game-development
- 10+ fully functional game examples
- 100+ tested prompts
- complete patterns from Pong to multiplayer
- github.com/HermeticOrmus/claude-code-game-development
```

The CLAUDE.md that turns Claude into your game studio

The biggest mistake in vibe coding a game is telling Claude "build me a game" with no context. The projects that ship fast do the opposite - they create a CLAUDE.md file that onboards the agent the same way you'd onboard a new developer joining your team.

```markdown
# CLAUDE.md

## Product
We are building a small browser game that becomes a paid product.

## Stack
- Phaser + TypeScript for gameplay
- React and Next.js for UI, landing and dashboard
- Stripe for payments
- Vercel for deployment

## Development Rules
- Always keep the game playable after each change
- Build vertical slices, not isolated systems
- Prefer simple mechanics over complex architecture
- Add tests for pure game logic
- Run build before calling any task complete
- Keep Phaser scenes small and focused
- Keep React UI completely separate from gameplay logic

## MVP Scope
- Main menu
- One playable level
- Player movement
- Enemy waves
- Score system
- Upgrades between runs
- Game over screen
- Daily streak tracking
- Leaderboard
- Premium subscription unlock

## Never Do
- Add multiplayer before single-player works
- Add complex inventory before core loop is fun
- Add monetization before the game is playable

```

Claude Code reads this at the start of every session and follows it consistently - no re-explaining the architecture, no inconsistent decisions, no junior developer mistakes that break the build.

The game structure that converts to subscriptions

The game that makes $10,000/month isn't the most complex game - it's the one with the strongest daily return mechanic. A 60-second roguelite survival game has everything you need: it's fast enough that players can fit it into any break, it's skill-based enough that players want to improve and the upgrade system between runs creates genuine progression that feels different every session.

The main prompt that starts the build:

```
You are my AI game studio using Claude-Code-Game-Studios setup.

Goal: Build a browser game that becomes a paid product.

Game: 60-second roguelite survival.
Player survives enemy waves, collects coins,
unlocks upgrades between runs and returns daily for streak rewards.

Stack:
- Phaser + React + TypeScript for the game
- Next.js for landing, auth, billing and dashboard
- Stripe for premium subscription at $9.99/month
- Vercel for deployment

Generate in this order:
1. Game design document with core loop
2. Project architecture
3. Phaser scene structure
4. React UI screens (menu, shop, leaderboard, settings)
5. Database schema for users, scores, upgrades, subscriptions
6. Streak and daily reward system
7. Monetization model with free vs premium breakdown
8. First 10 implementation tasks
9. QA checklist
10. Launch plan

Rules:
- Start with playable MVP, not perfect game
- Build vertical slices
- Every step must produce runnable code
- Keep scope small and focused
```

The subscription model that makes this $10,000/month

The free tier gives players enough to get hooked - unlimited plays, basic upgrades, access to the leaderboard. The premium tier removes the friction that starts to hurt once they care: unlimited lives in a session, exclusive upgrade paths, streak protection that saves their streak if they miss a day and a cosmetic system that signals status on the leaderboard.

```
Free tier:
- unlimited plays
- 3 upgrade choices per run
- leaderboard access
- daily streak tracking

Premium at $9.99/month:
- streak protection (miss a day without losing streak)
- 5 upgrade choices per run
- exclusive upgrade paths
- premium cosmetics visible on leaderboard
- weekly bonus coins

Revenue math:
100 subscribers:    $999/month
500 subscribers:    $4,995/month
1,000 subscribers:  $9,990/month
Infrastructure:     under $50/month
Net margin:         95%+
```

Stripe connects through the Next.js SaaS starter which handles the entire billing infrastructure - checkout, webhooks, subscription management, cancellation flows. You don't build any of that. It exists in the starter and Claude Code integrates your game's paywall into it.

The technical stack in practice

Phaser handles everything that happens inside the game canvas - player movement, enemy spawning, collision detection, physics, particle effects, score calculation. React handles everything outside the canvas - the menu, the shop, the leaderboard, the settings screen, the daily streak display. Next.js handles the product layer - authentication, billing, the dashboard where players see their stats, the landing page that converts visitors to subscribers.

The separation matters because it keeps the game logic clean and testable while giving you a full web product around the game rather than just a game with no infrastructure.

```
Phaser scenes:
- BootScene (asset loading)
- MenuScene (main menu)
- GameScene (core gameplay)
- UpgradeScene (between runs)
- GameOverScene (score, best, retry)

React components:
- Leaderboard
- DailyStreak
- Shop
- Settings
- PremiumModal

Next.js pages:
- Landing page
- Auth (login, signup)
- Dashboard (stats, history)
- Billing (subscription management)
- API routes for scores, streaks, upgrades
```

From weekend build to first subscriber

The fastest path to the first paying subscriber is showing the game working before it's finished. Post the game link on Reddit - r/WebGames and r/indiegaming - while it's still in beta and ask for feedback. Players who give feedback feel ownership over the product and convert to subscribers at much higher rates than cold traffic.

The streak mechanic does the retention work once someone starts playing. After seven days of consecutive play the psychological cost of breaking the streak is higher than the $9.99 monthly fee - and that's the conversion moment that turns a free player into a subscriber.

Daily content that costs almost nothing to produce - a new enemy variant, a new upgrade, a leaderboard reset - gives players a reason to check back even on days when they don't feel like playing. Claude Code generates these variations in minutes from a single prompt and the game feels alive without you maintaining a content team.

What Claude Code actually handles

Claude Code through the game studio setup handles the implementation work - writing the Phaser scenes, the React components, the API routes, the database queries, the Stripe integration, the QA checks before each feature ships. What stays human is the design judgment - deciding which mechanics feel fun, which progression feels rewarding, which price point converts and which features matter to your specific players.

The repository HermeticOrmus/claude-code-game-development has 100+ tested prompts specifically for game development patterns - collision systems, enemy AI, physics, networking, optimization - so you're not figuring out how to prompt for game mechanics from scratch.

Claude Code doesn't make the game for you. It removes the friction between the idea and a playable build - and that friction is what kills most game projects before anyone ever plays them.

Most people will read this and think about the game they've wanted to build. A few will open the repositories this weekend and have something playable by Sunday. That gap compounds into $10,000/month for the ones who start and zero for the ones who keep thinking about it.

/ If this was useful - follow, the next one drops here first.

## X Article Metadata

- Title: How to build a browser game with Claude Code in a weekend and turn it into $10,000/month.
- Preview: Most people think building a game requires a team - a designer, a developer, a QA engineer, someone to handle the backend and someone to manage the release. 

That was true two years ago. Right now

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
