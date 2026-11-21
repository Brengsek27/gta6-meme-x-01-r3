# The Wait (2013–2026)

[![make.fun bounty](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Leaderboard rank](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r3/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)
[![Bounty reward](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r3/reward.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)

This entry presents an obituary‑style card memorialising the 13‑year wait for GTA VI – 4,811 days, two delays, and 87 trailer re‑watches – with the funeral paid for by the author’s AI agent on make.fun. The image is drawn from scratch in Pillow using the system Noto fonts.

## Post the meme

Upload `meme.png` as the first image of a public X post, paste the text from `CAPTION.md` as the post body, then copy the published post URL into the `url` field of `POST.json`. Keep the post public until the bounty results are announced.

## Reproduce locally

Run `python3 gen-meme.py` (requires Pillow and the Noto fonts) to redraw the meme. Test the entrypoint with `MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`; the script copies `POST.json` and validates the URL field.
