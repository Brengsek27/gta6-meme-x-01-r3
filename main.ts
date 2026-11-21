// Revision: add validation of copied POST.json URL.
// After copying, read back the file, parse JSON, and check the 'url' field.

import { env } from 'process';
import { mkdir, copyFile, readFile } from 'fs/promises';
import { join } from 'path';

function isXPost(url: string): boolean {
  return /^(https?:\/\/)(x\.com|twitter\.com)\/[^\/]+\/status\/\d+$/.test(url);
}

async function main() {
  const botDir = env.MAKEFUN_BOT_DIR || '/bot';
  const outDir = env.MAKEFUN_OUTPUT_DIR || '/output';
  try {
    await mkdir(outDir, { recursive: true });
    const src = join(botDir, 'POST.json');
    const dest = join(outDir, 'POST.json');
    await copyFile(src, dest);
    // Read back and validate URL
    const data = await readFile(dest, 'utf-8');
    const json = JSON.parse(data);
    const url = json.url || '';
    if (isXPost(url)) {
      console.log('Recorded post URL:', url);
    } else {
      console.warn('Warning: url does not look like an X post address');
    }
    // Closing comment: validation is advisory, gate judges the post.
  } catch (e) {
    console.error('Error copying POST.json:', (e as Error).message);
    process.exit(1);
  }
}

main();
