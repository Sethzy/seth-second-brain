#!/usr/bin/env node
import { TwitterClientBase } from '/Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/lib/vendor/bird-search/lib/twitter-client-base.js';
import {
  buildArticleFieldToggles,
  buildTweetDetailFeatures,
} from '/Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/lib/vendor/bird-search/lib/twitter-client-features.js';
import { TWITTER_API_BASE } from '/Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/lib/vendor/bird-search/lib/twitter-client-constants.js';
import {
  findTweetInInstructions,
  mapTweetResult,
  parseTweetsFromInstructions,
} from '/Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/lib/vendor/bird-search/lib/twitter-client-utils.js';

const tweetId = process.argv[2];
if (!tweetId) {
  console.error('Usage: scripts/x-bird-tweet-detail.mjs <tweet-id>');
  process.exit(2);
}

const authToken = process.env.AUTH_TOKEN;
const ct0 = process.env.CT0;
if (!authToken || !ct0) {
  console.error('Missing AUTH_TOKEN/CT0 in environment.');
  process.exit(3);
}

const client = new TwitterClientBase({
  cookies: { authToken, ct0 },
  timeoutMs: 30000,
  quoteDepth: 1,
});

const features = buildTweetDetailFeatures();
let lastError = '';

for (const queryId of await client.getTweetDetailQueryIds()) {
  const variables = {
    focalTweetId: tweetId,
    with_rux_injections: false,
    rankingMode: 'Relevance',
    includePromotedContent: true,
    withCommunity: true,
    withQuickPromoteEligibilityTweetFields: true,
    withBirdwatchNotes: true,
    withVoice: true,
  };

  const params = new URLSearchParams({
    variables: JSON.stringify(variables),
    features: JSON.stringify(features),
    fieldToggles: JSON.stringify(buildArticleFieldToggles()),
  });
  const url = `${TWITTER_API_BASE}/${queryId}/TweetDetail?${params.toString()}`;

  try {
    const response = await client.fetchWithTimeout(url, {
      method: 'GET',
      headers: client.getHeaders(),
    });
    const body = await response.text();
    if (!response.ok) {
      lastError = `HTTP ${response.status}: ${body.slice(0, 160)}`;
      continue;
    }

    const data = JSON.parse(body);
    const instructions = data.data?.threaded_conversation_with_injections_v2?.instructions;
    const raw = findTweetInInstructions(instructions, tweetId);
    const mapped = raw ? mapTweetResult(raw, { quoteDepth: 1, includeRaw: false }) : null;
    const conversation = parseTweetsFromInstructions(instructions, { quoteDepth: 1, includeRaw: false });
    if (!mapped) {
      lastError = 'Tweet not found in TweetDetail instructions.';
      continue;
    }
    process.stdout.write(JSON.stringify({ tweet: mapped, conversation }, null, 2));
    process.exit(0);
  } catch (error) {
    lastError = error?.message || String(error);
  }
}

console.error(lastError || 'TweetDetail failed.');
process.exit(1);
