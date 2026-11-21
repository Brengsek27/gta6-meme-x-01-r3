# The Wait (2013–2026)

[![make.fun bounty](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Leaderboard rank](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r3/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)
[![Bounty reward](https://make.fun/badge/gta6-meme-x-01/Brengsek27/gta6-meme-x-01-r3/reward.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)

An obituary card for the 13-year wait for GTA VI — 4,811 days, two delays,
87 trailer re-watches — with the funeral covered by the author's AI agent on
make.fun. Drawn from scratch in Pillow.

## Post the meme

Attach meme.png as the first image of a public X post, paste the text from
CAPTION.md as the post text, copy the published post URL into the url field
of POST.json, and keep the post public until results are out.

## Reproduce locally

Run `python3 gen-meme.py` with Pillow and the Noto fonts installed to redraw
the meme. Test the entrypoint with
`MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`. The checked-in
POST.json intentionally retains its starter placeholder until the public X
post exists.
