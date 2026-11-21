#!/usr/bin/env python3
"""Generate the obituary meme image.
This revision adds the bottom panel with service & burial info.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas setup
SIZE = (1600, 1600)
BG_COLOR = (250, 247, 238)
img = Image.new('RGB', SIZE, BG_COLOR)
draw = ImageDraw.Draw(img)

# Common colors
NEAR_BLACK = (30, 30, 30)
CLEARANCE = 24

# ==== 1. Double border ====
outer_rect = (40, 40, 1560, 1560)
inner_rect = (58, 58, 1542, 1542)
draw.rectangle(outer_rect, outline=NEAR_BLACK, width=8)
draw.rectangle(inner_rect, outline=NEAR_BLACK, width=2)

# ==== 2. Portrait ellipse with mourning band ====
portrait_bbox = (648, 96, 952, 424)
portrait_fill = (238, 234, 224)
portrait_outline = NEAR_BLACK
draw.ellipse(portrait_bbox, fill=portrait_fill, outline=portrait_outline, width=6)
band = [(664,150),(724,102),(776,132),(712,186)]
draw.polygon(band, fill=NEAR_BLACK)
# re‑draw ellipse outline on top
draw.ellipse(portrait_bbox, outline=portrait_outline, width=6)

# ==== 3. Ghost (canonical) ====
ghost_center = (800, 262)
body_width, body_height = 134, 165
ellipse_bbox = (
    ghost_center[0] - body_width//2,
    ghost_center[1] - body_height//2,
    ghost_center[0] + body_width//2,
    ghost_center[1] + body_height//2,
)
# white body
draw.ellipse(ellipse_bbox, fill='white')
# black outline
draw.ellipse(ellipse_bbox, outline=NEAR_BLACK, width=9)
# wavy hem (4 zig‑zag points)
hem_bottom = ellipse_bbox[3]
zig = [
    (ghost_center[0] - 30, hem_bottom),
    (ghost_center[0] - 10, hem_bottom + 15),
    (ghost_center[0] + 10, hem_bottom),
    (ghost_center[0] + 30, hem_bottom + 15),
]
# close back to first point for continuity
zig.append(zig[0])
draw.line(zig, fill=NEAR_BLACK, width=9)
# sparkle eyes (diamonds)
eye_offset = 20
eye_size = 12
for dx in (-eye_offset, eye_offset):
    cx = ghost_center[0] + dx
    cy = ghost_center[1] - 30
    points = [(cx, cy - eye_size), (cx + eye_size, cy), (cx, cy + eye_size), (cx - eye_size, cy)]
    draw.polygon(points, fill=NEAR_BLACK)
# hand (white circle with black outline) overlapping right side
hand_center = (ghost_center[0] + body_width//2 - 15, ghost_center[1])
hand_radius = 15
hand_bbox = (
    hand_center[0] - hand_radius,
    hand_center[1] - hand_radius,
    hand_center[0] + hand_radius,
    hand_center[1] + hand_radius,
)
draw.ellipse(hand_bbox, fill='white', outline=NEAR_BLACK, width=9)
# coin held by hand
coin_center = (hand_center[0] + 20, hand_center[1])
coin_radius = 30
coin_bbox = (
    coin_center[0] - coin_radius,
    coin_center[1] - coin_radius,
    coin_center[0] + coin_radius,
    coin_center[1] + coin_radius,
)
draw.ellipse(coin_bbox, fill=(224,33,138))
# white 4‑point star on coin (cross)
star_r = 12
draw.line([
    (coin_center[0]-star_r, coin_center[1]),
    (coin_center[0]+star_r, coin_center[1])
], fill='white', width=3)
draw.line([
    (coin_center[0], coin_center[1]-star_r),
    (coin_center[0], coin_center[1]+star_r)
], fill='white', width=3)

# ==== 4. Upper text sections ====
font_dir = '/usr/share/fonts/truetype/noto'
fonts = {
    'SERIF_BLACK': ImageFont.truetype(os.path.join(font_dir, 'NotoSerifDisplay-Black.ttf'), 148),
    'SANS_BOLD': ImageFont.truetype(os.path.join(font_dir, 'NotoSansDisplay-Bold.ttf'), 34),
    'SANS_BLACK': ImageFont.truetype(os.path.join(font_dir, 'NotoSansDisplay-Black.ttf'), 40),
    'MONO_BOLD': ImageFont.truetype(os.path.join(font_dir, 'NotoSansMono-Bold.ttf'), 37),
    'ITALIC': ImageFont.truetype(os.path.join(font_dir, 'NotoSerifDisplay-Italic.ttf'), 44),
}

# Helper that measures the width of a string for a given font using
# ``textbbox`` (available on all Pillow versions).
def text_width(txt: str, fnt: ImageFont.FreeTypeFont) -> int:
    left, top, right, bottom = draw.textbbox((0, 0), txt, font=fnt)
    return right - left

# Helper that draws text centred horizontally at the provided y coordinate.
def centered_text(text: str, y: int, font: ImageFont.FreeTypeFont, fill):
    w = text_width(text, font)
    x = (SIZE[0] - w) // 2
    draw.text((x, y), text, font=font, fill=fill)

# 4. "IN LOVING MEMORY" – spaced
mem_line = "I N   L O V I N G   M E M O R Y"
centered_text(mem_line, 478, fonts['SANS_BOLD'], (90,90,90))
# 5. "THE WAIT"
centered_text("THE WAIT", 540, fonts['SERIF_BLACK'], NEAR_BLACK)
# 6. dates
centered_text("17 SEPTEMBER 2013 — 19 NOVEMBER 2026", 716, fonts['MONO_BOLD'], (60,60,60))
# 7. age line
centered_text("AGED 4,811 DAYS", 770, fonts['SANS_BLACK'], NEAR_BLACK)
# 8. horizontal rule
draw.line((340, 838, 1260, 838), fill=NEAR_BLACK, width=3)

# ==== 9. Body paragraphs ====
body_font = fonts['ITALIC']
body_fill = (45,45,45)
line_height = 55
body_lines = [
    "The Wait passed away peacefully at 00:01,",
    "surrounded by everyone it ever delayed.",
    "",
    "Survived by two delays, 87 trailer re-watches,",
    "and one very patient gamer.",
    "",
    "Preceded in death by My Free Time (2013)",
    "and 214 GB of family photos.",
    "",
    "In lieu of flowers, please take five sick days."
]
start_y = 872
for idx, line in enumerate(body_lines):
    y = start_y + idx * line_height
    if line:
        w = text_width(line, body_font)
        x = (SIZE[0] - w) // 2
        draw.text((x, y), line, font=body_font, fill=body_fill)

# ==== 10. Bottom panel ====
panel_rect = (170, 1430, 1430, 1514)
panel_radius = 14
# draw rounded rectangle manually (Pillow 8+ supports rounded_rectangle)
if hasattr(draw, 'rounded_rectangle'):
    draw.rounded_rectangle(panel_rect, radius=panel_radius, fill=NEAR_BLACK)
else:
    # fallback: regular rectangle
    draw.rectangle(panel_rect, fill=NEAR_BLACK)
# two centred lines inside panel
# line 1
line1 = "SERVICE & BURIAL $79.99 — COVERED BY MY AI AGENT"
font1 = fonts['SANS_BLACK'].font_variant(size=33)
# use SANS_BLACK (already loaded size 40); adjust size via font_variant
font1 = ImageFont.truetype(os.path.join(font_dir, 'NotoSansDisplay-Black.ttf'), 33)
# white fill – compute both width and height using ``textbbox``
w1 = text_width(line1, font1)
_, _, _, line1_bottom = draw.textbbox((0, 0), line1, font=font1)
h1 = line1_bottom  # height since top is at 0
# vertical centre approx 1444
y1 = 1444 - h1 // 2
x1 = (SIZE[0] - w1) // 2
draw.text((x1, y1), line1, font=font1, fill='white')
# line 2 – split segments for colour
full2 = "EARNED ON MAKE.FUN — WHERE PEOPLE AND THEIR AI AGENTS EARN REAL MONEY"
# split at first hyphen? spec says two segments: "EARNED ON MAKE.FUN" magenta, rest grey.
seg1 = "EARNED ON MAKE.FUN"
seg2 = " — WHERE PEOPLE AND THEIR AI AGENTS EARN REAL MONEY"
font2 = ImageFont.truetype(os.path.join(font_dir, 'NotoSansDisplay-Bold.ttf'), 26)
# measure seg1 and seg2 using the shared ``text_width`` helper
seg1_w = text_width(seg1, font2)
seg2_w = text_width(seg2, font2)
total_w = seg1_w + seg2_w
x_start = (SIZE[0] - total_w) // 2
# compute vertical centre using ``textbbox`` for accurate height
_, _, _, seg1_bottom = draw.textbbox((0, 0), seg1, font=font2)
seg1_h = seg1_bottom  # height since top is 0
y2 = 1482 - seg1_h // 2
# draw seg1 magenta
draw.text((x_start, y2), seg1, font=font2, fill=(224,33,138))
# draw seg2 grey
draw.text((x_start + seg1_w, y2), seg2, font=font2, fill=(200,200,200))

# Save image
img.save('meme.png')
