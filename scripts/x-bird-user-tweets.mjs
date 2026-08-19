#!/usr/bin/env node
import { importBirdModule } from './last30days-runtime.mjs';

const { TwitterClientBase } = await importBirdModule('twitter-client-base.js');
const { withSearch } = await importBirdModule('twitter-client-search.js');
const {
  buildArticleFieldToggles,
  buildUserTweetsFeatures,
} = await importBirdModule('twitter-client-features.js');
const { TWITTER_API_BASE } = await importBirdModule('twitter-client-constants.js');
const {
  extractCursorFromInstructions,
  parseTweetsFromInstructions,
} = await importBirdModule('twitter-client-utils.js');

const SearchClient = withSearch(TwitterClientBase);
const USER_TWEETS_FALLBACK_QUERY_IDS = ['Wms1GvIiHXAPBaCr9KblaA'];

function usage() {
  console.error('Usage: scripts/x-bird-user-tweets.mjs <handle> [--count N]');
}

function parseArgs(argv) {
  let handle;
  let count = 100;
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--count' && argv[i + 1]) {
      count = Number.parseInt(argv[i + 1], 10);
      i += 1;
    } else if (!arg.startsWith('-') && !handle) {
      handle = arg.replace(/^@/, '');
    }
  }
  if (!handle || !Number.isFinite(count) || count <= 0) {
    usage();
    process.exit(2);
  }
  return { handle, count };
}

function findInstructions(value, depth = 0) {
  if (!value || depth > 8) {
    return undefined;
  }
  if (Array.isArray(value)) {
    return undefined;
  }
  if (Array.isArray(value.instructions)) {
    return value.instructions;
  }
  if (typeof value !== 'object') {
    return undefined;
  }
  for (const nested of Object.values(value)) {
    const found = findInstructions(nested, depth + 1);
    if (found) {
      return found;
    }
  }
  return undefined;
}

async function resolveUserId(client, handle) {
  const result = await client.search(`from:${handle}`, 1);
  if (!result.success) {
    throw new Error(`Could not resolve @${handle} via X search: ${result.error}`);
  }
  const tweet = result.tweets?.find((item) => item.author?.username?.toLowerCase() === handle.toLowerCase());
  if (tweet?.authorId) {
    return tweet.authorId;
  }
  throw new Error(`Could not resolve @${handle} to a user id from recent public posts.`);
}

async function getUserTweetsQueryIds(client) {
  const primary = await client.getQueryId('UserTweets');
  return Array.from(new Set([primary, ...USER_TWEETS_FALLBACK_QUERY_IDS].filter(Boolean)));
}

async function fetchUserTweetsPage(client, userId, pageCount, cursor) {
  const features = buildUserTweetsFeatures();
  let lastError = '';
  let had404 = false;

  for (const queryId of await getUserTweetsQueryIds(client)) {
    const variables = {
      userId,
      count: pageCount,
      includePromotedContent: true,
      withQuickPromoteEligibilityTweetFields: true,
      withVoice: true,
      withV2Timeline: true,
      ...(cursor ? { cursor } : {}),
    };
    const params = new URLSearchParams({
      variables: JSON.stringify(variables),
      features: JSON.stringify(features),
      fieldToggles: JSON.stringify(buildArticleFieldToggles()),
    });
    const url = `${TWITTER_API_BASE}/${queryId}/UserTweets?${params.toString()}`;

    try {
      const response = await client.fetchWithTimeout(url, {
        method: 'GET',
        headers: client.getHeaders(),
      });
      const body = await response.text();
      if (response.status === 404) {
        had404 = true;
        lastError = `HTTP ${response.status}`;
        continue;
      }
      if (!response.ok) {
        lastError = `HTTP ${response.status}: ${body.slice(0, 200)}`;
        continue;
      }

      const data = JSON.parse(body);
      if (data.errors?.length) {
        lastError = data.errors.map((error) => error.message).join(', ');
        continue;
      }
      const instructions = findInstructions(data.data?.user?.result);
      const tweets = parseTweetsFromInstructions(instructions, { quoteDepth: 1, includeRaw: false });
      return {
        success: true,
        tweets,
        cursor: extractCursorFromInstructions(instructions),
        had404,
      };
    } catch (error) {
      lastError = error?.message || String(error);
    }
  }

  return { success: false, error: lastError || 'UserTweets failed', had404 };
}

async function fetchTimeline(client, userId, limit) {
  const tweets = [];
  const seen = new Set();
  let cursor;
  let nextCursor;
  let pagesFetched = 0;
  const maxPages = Math.max(12, Math.ceil(limit / 20) + 5);

  while (tweets.length < limit) {
    const pageCount = Math.min(20, limit - tweets.length);
    let page = await fetchUserTweetsPage(client, userId, pageCount, cursor);
    if (!page.success && page.had404) {
      await client.refreshQueryIds();
      page = await fetchUserTweetsPage(client, userId, pageCount, cursor);
    }
    if (!page.success) {
      throw new Error(page.error);
    }

    pagesFetched += 1;
    let added = 0;
    for (const tweet of page.tweets || []) {
      if (!tweet?.id || seen.has(tweet.id)) {
        continue;
      }
      seen.add(tweet.id);
      tweets.push(tweet);
      added += 1;
      if (tweets.length >= limit) {
        break;
      }
    }

    const pageCursor = page.cursor;
    if (!pageCursor || pageCursor === cursor || added === 0 || pagesFetched >= maxPages) {
      nextCursor = pageCursor;
      break;
    }
    cursor = pageCursor;
    nextCursor = pageCursor;
  }

  return { tweets, nextCursor };
}

async function fetchTimelineViaSearch(client, handle, limit) {
  const tweets = [];
  const seen = new Set();
  let maxId;
  let nextCursor;

  while (tweets.length < limit) {
    const remaining = limit - tweets.length;
    const query = `from:${handle}${maxId ? ` max_id:${maxId}` : ''}`;
    const result = await client.search(query, Math.min(40, remaining), { maxPages: 4 });
    if (!result.success) {
      throw new Error(result.error);
    }

    let oldestId;
    let added = 0;
    for (const tweet of result.tweets || []) {
      if (tweet.author?.username?.toLowerCase() !== handle.toLowerCase()) {
        continue;
      }
      if (!tweet.id || seen.has(tweet.id)) {
        continue;
      }
      seen.add(tweet.id);
      tweets.push(tweet);
      added += 1;
      if (!oldestId || BigInt(tweet.id) < BigInt(oldestId)) {
        oldestId = tweet.id;
      }
      if (tweets.length >= limit) {
        break;
      }
    }

    nextCursor = result.nextCursor;
    if (!oldestId || added === 0) {
      break;
    }
    maxId = (BigInt(oldestId) - 1n).toString();
  }

  return { tweets, nextCursor };
}

const { handle, count } = parseArgs(process.argv.slice(2));
const authToken = process.env.AUTH_TOKEN;
const ct0 = process.env.CT0;
if (!authToken || !ct0) {
  console.error('Missing AUTH_TOKEN/CT0 in environment.');
  process.exit(3);
}

try {
  const client = new SearchClient({
    cookies: { authToken, ct0 },
    timeoutMs: 30000,
    quoteDepth: 1,
  });
  const userId = await resolveUserId(client, handle);
  let timeline;
  let retrievalMethod = 'UserTweets';
  try {
    timeline = await fetchTimeline(client, userId, count);
  } catch (error) {
    const message = error?.message || String(error);
    if (!/HTTP 429|rate limit/i.test(message)) {
      throw error;
    }
    timeline = await fetchTimelineViaSearch(client, handle, count);
    retrievalMethod = 'SearchTimeline';
  }
  process.stdout.write(JSON.stringify({ handle, userId, retrievalMethod, ...timeline }, null, 2));
} catch (error) {
  console.error(error?.message || String(error));
  process.exit(1);
}
