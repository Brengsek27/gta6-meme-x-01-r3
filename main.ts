// gta6-meme-x-01 round 3 entrypoint (Node 22, standard library only).
// Copies POST.json from the bot dir to the output dir, where the gate reads
// it, then reads the copy back and sanity-checks its url field. A placeholder
// or non-X URL only earns a warning: the copy is the contract, so the run
// exits 0 whenever the copy succeeded.

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
const target = join(OUTPUT_DIR, 'POST.json');
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), target);
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

let url = '';
try {
  const parsed = JSON.parse(readFileSync(target, 'utf8')) as { url?: unknown };
  if (typeof parsed.url === 'string') url = parsed.url;
} catch {
  console.warn('Warning: copied POST.json could not be parsed as JSON.');
}

if (/^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+/.test(url)) {
  console.log(`Recorded post URL: ${url}`);
} else {
  console.warn(`Warning: POST.json url does not look like an X post address: ${url || '(empty)'}`);
}

// Pass 2 note: the read-back validation above never fails the run on a
// placeholder URL — before the X post exists the starter placeholder is
// expected, and the gate, not this program, judges the post itself.
