#!/usr/bin/env node

import { existsSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));

function candidates() {
  const configured = process.env.LAST30DAYS_SCRIPTS_DIR;
  return [
    configured,
    path.join(ROOT, '.agents', 'skills', 'last30days', 'scripts'),
    path.join(os.homedir(), '.agents', 'skills', 'last30days', 'scripts'),
    path.join(os.homedir(), '.codex', 'skills', 'last30days', 'scripts'),
    path.join(os.homedir(), 'Documents', 'gtm-workspace', '.agents', 'skills', 'last30days', 'scripts'),
    path.join(os.homedir(), 'Documents', 'openai-interview-prep', 'skills', 'last30days', 'scripts'),
  ].filter(Boolean).map((candidate) => path.resolve(candidate));
}

export function resolveLast30DaysScriptsDir() {
  for (const candidate of candidates()) {
    if (
      existsSync(path.join(candidate, 'last30days.py'))
      && existsSync(path.join(candidate, 'lib', 'vendor', 'bird-search'))
    ) {
      return candidate;
    }
  }
  throw new Error(
    'Last30Days is optional but required for this command. Install '
    + 'mvanhorn/last30days-skill, or set LAST30DAYS_SCRIPTS_DIR to its scripts directory. '
    + `Searched: ${candidates().join(', ')}`,
  );
}

export async function importBirdModule(filename) {
  const modulePath = path.join(
    resolveLast30DaysScriptsDir(),
    'lib',
    'vendor',
    'bird-search',
    'lib',
    filename,
  );
  return import(pathToFileURL(modulePath).href);
}
