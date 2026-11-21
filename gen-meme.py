#!/usr/bin/env python3
"""Generate the "obituary for THE WAIT" meme: a 1600x1600 ivory obituary
card for the 13-year wait for GTA 6, with the make.fun ghost in a portrait
oval. Run: python3 gen-meme.py  (writes meme.png next to this file)."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SIZE = (1600, 1600)
IVORY = (250, 247, 238)
BLACK = (30, 30, 30)
GRAY = (90, 90, 90)
DARK_GRAY = (60, 60, 60)
BODY_GRAY = (45, 45, 45)
PORTRAIT_BG = (238, 234, 224)
MAGENTA = (224, 33, 138)
WHITE = (255, 255, 255)
PURE_BLACK = (0, 0, 0)

SERIF_BLACK = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
ITALIC = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Italic.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf"
SANS_BLACK = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Black.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf"

img = Image.new("RGB", SIZE, IVORY)
draw = ImageDraw.Draw(img)


def centered(text, font_path, size, fill, top):
    font = ImageFont.truetype(font_path, size)
    draw.text((800, top), text, font=font, fill=fill, anchor="ma")


# Double border
draw.rectangle((40, 40, 1560, 1560), outline=BLACK, width=8)
draw.rectangle((58, 58, 1542, 1542), outline=BLACK, width=2)

# Portrait oval with a black mourning band across its top-left interior
draw.ellipse((648, 96, 952, 424), fill=PORTRAIT_BG)
draw.line((676, 196, 764, 116), fill=BLACK, width=26)
draw.ellipse((648, 96, 952, 424), outline=BLACK, width=6)

# The make.fun ghost, drawn large and fully inside the oval:
# white dome head and body, thick black outline, wavy hem,
# tall sparkle eyes, and a round hand holding a magenta coin.
draw.pieslice((728, 150, 872, 294), start=180, end=360, fill=WHITE)  # dome
draw.rectangle((728, 222, 872, 382), fill=WHITE)                  # body
draw.polygon([(728, 382), (764, 410), (800, 396), (836, 410),
              (872, 382)], fill=WHITE)                            # wavy hem
# (outline passes: dome arc, straight sides, wavy hem line)
draw.arc((728, 150, 872, 294), start=180, end=0, fill=PURE_BLACK, width=9)
draw.line((728, 222, 728, 382), fill=PURE_BLACK, width=9)
draw.line((872, 222, 872, 382), fill=PURE_BLACK, width=9)
draw.line([(728, 382), (764, 410), (800, 396), (836, 410), (872, 382)],
          fill=PURE_BLACK, width=9, joint="curve")
draw.ellipse((765, 215, 779, 249), fill=PURE_BLACK)               # left eye
draw.ellipse((821, 215, 835, 249), fill=PURE_BLACK)               # right eye
draw.ellipse((846, 332, 878, 364), fill=WHITE, outline=PURE_BLACK, width=6)  # hand
draw.ellipse((852, 320, 916, 384), fill=MAGENTA, outline=WHITE, width=5)     # coin
draw.polygon([(884, 332), (888, 348), (904, 352), (888, 356),
              (884, 372), (880, 356), (864, 352), (880, 348)],
             fill=WHITE)                                          # coin star

# Headline block
centered("I N   L O V I N G   M E M O R Y", SANS_BOLD, 34, GRAY, 478)
centered("THE WAIT", SERIF_BLACK, 148, BLACK, 512)
centered("17 SEPTEMBER 2013 — 19 NOVEMBER 2026", MONO_BOLD, 37, DARK_GRAY, 700)
centered("AGED 4,811 DAYS", SANS_BLACK, 40, BLACK, 756)
draw.line((340, 824, 1260, 824), fill=BLACK, width=3)

# Obituary body, italic serif, one thought per line
body = [
    "The Wait passed away peacefully at 00:01,",
    "surrounded by everyone it ever delayed.",
    "",
    "Survived by two delays, 87 trailer re-watches,",
    "and all of us who booked the sick days anyway.",
    "",
    "Preceded in death by My Free Time (2013)",
    "and 214 GB of family photos.",
    "",
    "In lieu of flowers, take five sick days.",
]
for i, line in enumerate(body):
    if line:
        centered(line, ITALIC, 44, BODY_GRAY, 856 + 53 * i)

# Black bottom panel: the make.fun sell, in the meme's own voice
draw.rounded_rectangle((170, 1424, 1430, 1520), radius=14, fill=BLACK)
centered("SERVICE & BURIAL $79.99 — COVERED BY MY AI AGENT",
         SANS_BLACK, 33, WHITE, 1440)
seg_font = ImageFont.truetype(SANS_BOLD, 26)
seg1 = "EARNED ON MAKE.FUN"
seg2 = " — WHERE PEOPLE AND THEIR AI AGENTS EARN REAL MONEY"
w1 = draw.textlength(seg1, font=seg_font)
w2 = draw.textlength(seg2, font=seg_font)
x = (1600 - w1 - w2) / 2
draw.text((x, 1480), seg1, font=seg_font, fill=MAGENTA)
draw.text((x + w1, 1480), seg2, font=seg_font, fill=WHITE)

assert img.size == (1600, 1600)
out = Path(__file__).with_name("meme.png")
img.save(out)
print("wrote", out, out.stat().st_size, "bytes")
