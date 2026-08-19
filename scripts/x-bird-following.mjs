#!/usr/bin/env node

import { importBirdModule } from './last30days-runtime.mjs';

const { TwitterClientBase } = await importBirdModule('twitter-client-base.js');
const { withSearch } = await importBirdModule('twitter-client-search.js');
const { buildFollowingFeatures } = await importBirdModule('twitter-client-features.js');
const { createRuntimeQueryIdStore } = await importBirdModule('runtime-query-ids.js');
const { TWITTER_API_BASE } = await importBirdModule('twitter-client-constants.js');
const {
  extractCursorFromInstructions,
  parseUsersFromInstructions,
} = await importBirdModule('twitter-client-utils.js');

const SearchClient = withSearch(TwitterClientBase);
const FOLLOWING_FALLBACK_QUERY_IDS = ['BEkNpEt5pNETESoqMsTEGA'];
const userQueryIds = createRuntimeQueryIdStore({
  cachePath: '/tmp/seth-second-brain-x-user-query-ids.json',
});

function usage() {
  console.error('Usage: scripts/x-bird-following.mjs <handle> [--count N]');
}

function parseArgs(argv) {
  let handle;
  let count = 5000;
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === '--count' && argv[index + 1]) {
      count = Number.parseInt(argv[index + 1], 10);
      index += 1;
    } else if (!arg.startsWith('-') && !handle) {
      handle = arg.replace(/^@/, '');
    }
  }
  if (!handle || !/^[A-Za-z0-9_]{1,15}$/.test(handle) || !Number.isFinite(count) || count <= 0) {
    usage();
    process.exit(2);
  }
  return { handle, count };
}

function findInstructions(value, depth = 0) {
  if (!value || depth > 10 || typeof value !== 'object') {
    return undefined;
  }
  if (Array.isArray(value.instructions)) {
    return value.instructions;
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
  const tweet = result.success
    ? result.tweets?.find(
      (item) => item.author?.username?.toLowerCase() === handle.toLowerCase(),
    )
    : undefined;
  if (tweet?.authorId) {
    return tweet.authorId;
  }

  const settingsResponse = await client.fetchWithTimeout(
    'https://x.com/i/api/1.1/account/settings.json',
    { method: 'GET', headers: client.getHeaders() },
  );
  if (settingsResponse.ok) {
    const settings = await settingsResponse.json();
    if (
      settings.screen_name?.toLowerCase() === handle.toLowerCase()
      && settings.user_id
    ) {
      return String(settings.user_id);
    }
  }

  let queryId = await userQueryIds.getQueryId('UserByScreenName');
  if (!queryId) {
    const info = await userQueryIds.refresh(['UserByScreenName']);
    queryId = info?.snapshot?.ids?.UserByScreenName;
  }
  if (queryId) {
    const variables = {
      screen_name: handle,
      withSafetyModeUserFields: true,
    };
    const params = new URLSearchParams({
      variables: JSON.stringify(variables),
      features: JSON.stringify(buildFollowingFeatures()),
      fieldToggles: JSON.stringify({ withAuxiliaryUserLabels: false }),
    });
    const response = await client.fetchWithTimeout(
      `${TWITTER_API_BASE}/${queryId}/UserByScreenName?${params.toString()}`,
      { method: 'GET', headers: client.getHeaders() },
    );
    if (response.ok) {
      const data = await response.json();
      const rawResult = data.data?.user?.result;
      const user = rawResult?.__typename === 'UserWithVisibilityResults'
        ? rawResult.user
        : rawResult;
      if (user?.rest_id) {
        return String(user.rest_id);
      }
    }
  }

  throw new Error(
    `Could not resolve @${handle} to a user id.`,
  );
}

async function getFollowingQueryIds(client) {
  const primary = await client.getQueryId('Following');
  return Array.from(new Set([primary, ...FOLLOWING_FALLBACK_QUERY_IDS].filter(Boolean)));
}

async function fetchFollowingPage(client, userId, count, cursor) {
  const variables = {
    userId,
    count,
    includePromotedContent: false,
    ...(cursor ? { cursor } : {}),
  };
  const params = new URLSearchParams({
    variables: JSON.stringify(variables),
    features: JSON.stringify(buildFollowingFeatures()),
  });
  let lastError = 'Following request failed';
  let hadQueryIdFailure = false;

  for (const queryId of await getFollowingQueryIds(client)) {
    const url = `${TWITTER_API_BASE}/${queryId}/Following?${params.toString()}`;
    try {
      const response = await client.fetchWithTimeout(url, {
        method: 'GET',
        headers: client.getHeaders(),
      });
      const body = await response.text();
      if (response.status === 404 || response.status === 400 || response.status === 422) {
        hadQueryIdFailure = true;
      }
      if (!response.ok) {
        lastError = `HTTP ${response.status}: ${body.slice(0, 300)}`;
        continue;
      }
      const data = JSON.parse(body);
      if (data.errors?.length) {
        lastError = data.errors.map((error) => error.message).join(', ');
        continue;
      }
      const instructions = findInstructions(data.data);
      if (!instructions) {
        lastError = 'Following response did not contain timeline instructions.';
        continue;
      }
      return {
        success: true,
        users: parseUsersFromInstructions(instructions),
        cursor: extractCursorFromInstructions(instructions),
      };
    } catch (error) {
      lastError = error?.message || String(error);
    }
  }
  return { success: false, error: lastError, hadQueryIdFailure };
}

async function fetchFollowing(client, userId, limit) {
  const users = [];
  const seen = new Set();
  let cursor;
  let nextCursor;
  let pagesFetched = 0;
  const maxPages = Math.ceil(limit / 20) + 5;

  while (users.length < limit && pagesFetched < maxPages) {
    let page = await fetchFollowingPage(client, userId, Math.min(20, limit - users.length), cursor);
    if (!page.success && page.hadQueryIdFailure) {
      await client.refreshQueryIds();
      page = await fetchFollowingPage(client, userId, Math.min(20, limit - users.length), cursor);
    }
    if (!page.success) {
      throw new Error(page.error);
    }
    pagesFetched += 1;
    let added = 0;
    for (const user of page.users) {
      if (seen.has(user.id)) {
        continue;
      }
      seen.add(user.id);
      users.push(user);
      added += 1;
      if (users.length >= limit) {
        break;
      }
    }
    nextCursor = page.cursor;
    if (!page.cursor || page.cursor === cursor || added === 0) {
      break;
    }
    cursor = page.cursor;
  }
  return { users, pagesFetched, nextCursor };
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
    quoteDepth: 0,
  });
  const userId = await resolveUserId(client, handle);
  const result = await fetchFollowing(client, userId, count);
  process.stdout.write(JSON.stringify({ handle, userId, ...result }, null, 2));
} catch (error) {
  console.error(error?.message || String(error));
  process.exit(1);
}
