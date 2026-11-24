#!/usr/bin/env python3
"""news-23 b51 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026 (31 stories)."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu"

def f_bold(s): return ImageFont.truetype(f"{FD}/DejaVuSans-Bold.ttf", s)
def f_reg(s): return ImageFont.truetype(f"{FD}/DejaVuSans.ttf", s)
def f_serif(s): return ImageFont.truetype(f"{FD}/DejaVuSerif-Bold.ttf", s)

BLACK = (0, 0, 0); WHITE = (255, 255, 255); CREAM = (245, 239, 221)
RED = (178, 34, 34); GOLD = (212, 160, 23); NAVY = (10, 26, 58)
TEAL = (14, 122, 107); GRAY = (90, 90, 90); LGRAY = (235, 235, 235)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)

def text(x, y, s, font, fill=BLACK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def wrap(s, font, maxw):
    words = s.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def chip(x_right, y, label, fill):
    """Right-aligned chip; returns left edge."""
    f = f_bold(9)
    w_ = d.textlength(label, font=f) + 10
    d.rounded_rectangle([x_right - w_, y, x_right, y + 14], radius=2, fill=fill)
    text(x_right - w_ / 2, y + 2, label, f, WHITE, anchor="ma")
    return x_right - w_

# ---------- Masthead ----------
d.rectangle([0, 0, W, 52], fill=BLACK)
text(14, 6, "THE WORLD TODAY", f_serif(40), WHITE)
text(W - 14, 14, "MONDAY 23 NOVEMBER 2026", f_bold(21), GOLD, anchor="ra")

# ---------- Kicker ----------
text(14, 55, "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
     f_bold(13), RED)

# ---------- Number strip: 2 rows x 5 cols ----------
nums = [
    ("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", (0, 90, 140)),
    ("11,762", "EBOLA CASES, DRC", (0, 130, 60)), ("10T won", "SEOUL STABILISATION FUND", (150, 110, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (120, 40, 160)),
    ("$450M", "SKUBAL DEAL", (130, 40, 160)), ("165", "RUSSIAN MISSILES IN A WEEK", RED),
    ("12,000", "CLEARED IN MANCHESTER", (0, 90, 140)), ("264 kg", "EXPLOSIVES SEIZED IN LEBANON", (150, 110, 0)),
    ("$107.3B", "ANTHROPIC IPO \u2014 LARGEST", (120, 40, 160)),
]
for i, (num, lab, col) in enumerate(nums):
    row, c = divmod(i, 5)
    x = 14 + c * 205
    y = 73 + row * 29
    text(x, y, num, f_bold(19), col)
    text(x, y + 20, lab, f_reg(8), BLACK)
d.line([0, 131, W, 131], fill=(200, 200, 200), width=1)

# ---------- Region bar ----------
segs = [("ASIA-PACIFIC 7", 290, (0, 128, 110)), ("AMERICAS 8", 290, (20, 50, 110)),
        ("MIDDLE EAST 6", 165, (200, 120, 20)), ("EUROPE 5", 120, (120, 60, 160)),
        ("AFRICA 3", 80, (180, 40, 40)), ("WORLD 2", 79, (90, 90, 90))]
x = 0
for lab, w_, col in segs:
    d.rectangle([x, 132, x + w_, 149], fill=col)
    text(x + w_ / 2, 135, lab, f_bold(10), WHITE, anchor="ma")
    x += w_

# ---------- THE DAY IN UTC ----------
d.rectangle([0, 150, W, 165], fill=NAVY)
text(14, 152, "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles   ~18:00 IPO $97.17",
     f_reg(11), WHITE)
text(W - 10, 152, "~ APPROX", f_bold(10), GOLD, anchor="ra")

# ---------- Hero scenes ----------
SX = [0, 342, 684]          # scene x starts
SW = 340                    # scene width
SY, SH = 166, 154           # scene y, height

# Scene 1: Kospi chart
d.rectangle([SX[0], SY, SX[0] + SW, SY + SH], fill=(8, 22, 52))
text(SX[0] + 10, SY + 6, "-3.3%", f_bold(30), (255, 70, 60))
pts = [(SX[0] + 12 + i * 30, SY + 62 + v) for i, v in enumerate([18, 2, 26, 10, 34, 14, 40, 22, 8, 30, 16, 4])]
d.line(pts, fill=(255, 90, 70), width=3)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 210, 90))
# skyline
import random
random.seed(51)
bx = SX[0] + 8
while bx < SX[0] + SW - 14:
    bw = random.randint(14, 24); bh = random.randint(28, 62)
    d.rectangle([bx, SY + SH - bh, bx + bw, SY + SH], fill=(18, 38, 80))
    for wy in range(SY + SH - bh + 5, SY + SH - 4, 10):
        for wx in range(bx + 3, bx + bw - 3, 7):
            if random.random() < 0.55:
                d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 215, 90))
    bx += bw + 4

# Scene 2: Guterres
d.rectangle([SX[1], SY, SX[1] + SW, SY + SH], fill=TEAL)
text(SX[1] + 12, SY + 10, "150 DELEGATES", f_bold(33), GOLD)
text(SX[1] + 12, SY + 46, "BACK A RISK", f_bold(33), WHITE)
text(SX[1] + 12, SY + 82, "FRAMEWORK", f_bold(33), WHITE)
# globe bottom-right
gx, gy, gr = SX[1] + SW - 46, SY + SH - 34, 26
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=WHITE, width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline=WHITE, width=1)
d.line([gx - gr, gy, gx + gr, gy], fill=WHITE, width=1)
d.arc([gx - gr, gy - gr // 2, gx + gr, gy + gr // 2], 0, 360, fill=WHITE, width=1)

# Scene 3: Asia Power Index bars
d.rectangle([SX[2], SY, SX[2] + SW, SY + SH], fill=CREAM)
text(SX[2] + 10, SY + 8, "NARROWEST SINCE 2018", f_bold(12), BLACK)
text(SX[2] + SW - 10, SY + 8, "GAP 5.3", f_bold(12), (170, 120, 10), anchor="ra")
bars = [("US", 78.9, (20, 50, 110)), ("CHINA", 73.6, RED), ("INDIA", 40.5, (200, 150, 30))]
b_base = SY + SH - 4
b_max = 96
for j, (lab, val, col) in enumerate(bars):
    bx0 = SX[2] + 14 + j * 110
    bh = int(val / 78.9 * b_max)
    d.rectangle([bx0, b_base - bh, bx0 + 92, b_base], fill=col)
    text(bx0 + 46, b_base - bh + 6, f"{val}", f_bold(15), WHITE, anchor="ma")
    text(bx0 + 46, b_base - 20, lab, f_bold(12), WHITE, anchor="ma")

# ---------- Caption strips ----------
caps = ["KOSPI 4,708.54  \u00b7  -161 PTS", "UN  \u00b7  BRIDGETOWN", "ASIA POWER INDEX 2026"]
for j in range(3):
    d.rectangle([SX[j], 320, SX[j] + SW, 338], fill=BLACK)
    text(SX[j] + 10, 323, caps[j], f_bold(11), WHITE)

# ---------- Hero text blocks ----------
heroes = [
    (1, "AI ROUT HITS ASIA", "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.", "KOREA EXCHANGE"),
    (2, "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE", "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.", "UNITED NATIONS"),
    (3, "US LEAD OVER CHINA AT RECORD LOW", "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.", "LOWY INSTITUTE"),
]
for j, (num, head, body, src) in enumerate(heroes):
    x = SX[j] + 2
    y = 346
    d.ellipse([x + 2, y + 2, x + 24, y + 24], fill=RED)
    text(x + 13, y + 4, str(num), f_bold(13), WHITE, anchor="ma")
    hl = wrap(head, f_bold(16), SW - 34)
    yy = y + 1
    for ln in hl[:2]:
        text(x + 30, yy, ln, f_bold(16), BLACK)
        yy += 19
    bl = wrap(body, f_reg(11), SW - 8)
    yy = y + 41
    for ln in bl[:2]:
        text(x + 2, yy, ln, f_reg(11), BLACK)
        yy += 14
    text(x + 2, 419, src, f_reg(10), GRAY)
    chip(SX[j] + SW - 2, 417, "REPORTED", (20, 50, 110))

# ---------- Section header ----------
d.rectangle([0, 434, W, 452], fill=BLACK)
text(14, 437, "MORE OF THE DAY  \u2014  10 STORIES", f_bold(13), WHITE)

# ---------- Cards: 5 cols x 2 rows ----------
cards = [
    ("AMERICAS", (0, 128, 110), "BESSENT: NVIDIA ANSWERS", "Treasury chief wants China answers.", "Reuters", "REPORTED"),
    ("FBI", (180, 40, 40), "FBI PROBES NCIC HACK", "Hackers hit police NCIC database.", "AP", "REPORTED"),
    ("WHITE HOUSE", (150, 110, 0), "TRUMP: IRAN STRIKES MAY RESUME", "Strikes may resume in New Year.", "Reuters", "REPORTED"),
    ("MARKETS", (0, 130, 60), "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED"),
    ("SPORT", (180, 40, 40), "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED"),
    ("SPORT", (180, 40, 40), "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED"),
    ("LEGAL", (90, 60, 140), "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED"),
    ("TECH", (0, 90, 140), "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED"),
    ("EUROPE", (120, 60, 160), "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM"),
    ("SPACE", (90, 90, 90), "RUSSIAN NUCLEAR SATELLITE", "Intel: satellite may carry a nuke.", "Reuters", "CLAIM"),
]
CW = 205
for i, (cat, ccol, head, body, src, tag) in enumerate(cards):
    row, c = divmod(i, 5)
    x = c * CW
    y = 452 + row * 90
    d.rectangle([x, y, x + CW - 1, y + 15], fill=ccol)
    text(x + 6, y + 2, cat, f_bold(9), WHITE)
    text(x + CW - 8, y + 2, str(i + 1), f_bold(9), WHITE, anchor="ra")
    hl = wrap(head, f_bold(12), CW - 12)
    yy = y + 19
    for ln in hl[:2]:
        text(x + 6, yy, ln, f_bold(12), BLACK)
        yy += 14
    text(x + 6, y + 49, body, f_reg(10), BLACK)
    text(x + 6, y + 71, src, f_reg(9), GRAY)
    chip(x + CW - 6, y + 70, tag, (20, 50, 110) if tag == "REPORTED" else RED)

# ---------- Map + ALSO ----------
d.rectangle([0, 632, 330, 650], fill=BLACK)
text(10, 635, "WHERE IT HAPPENED", f_bold(12), WHITE)
d.rectangle([332, 632, W, 650], fill=BLACK)
text(342, 635, "ALSO ON MONDAY", f_bold(12), WHITE)

# map area
d.rectangle([0, 650, 330, 868], fill=(222, 232, 240))
for gx in range(0, 331, 22):
    d.line([gx, 650, gx, 868], fill=(200, 212, 222), width=1)
for gy in range(650, 869, 22):
    d.line([0, gy, 330, gy], fill=(200, 212, 222), width=1)
for (ex, ey, rx, ry) in [(70, 730, 62, 52), (190, 725, 88, 66), (120, 820, 46, 34), (255, 815, 52, 40)]:
    d.ellipse([ex - rx, ey - ry, ex + rx, ey + ry], fill=(150, 205, 140))
pins = [(52, 690, 1), (86, 742, 2), (118, 706, 3), (66, 768, 4), (104, 752, 5),
        (150, 700, 6), (176, 716, 7), (206, 742, 8), (232, 700, 9), (258, 726, 10),
        (150, 668, 11), (176, 682, 12), (222, 676, 13)]
for px, py, n in pins:
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=WHITE, width=1)
    text(px, py - 7, str(n), f_bold(9), WHITE, anchor="ma")
text(8, 830, "Pins 1\u201313: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing", f_reg(9), BLACK)
text(8, 842, "4 Washington \u00b7 5 New York \u00b7 6 Tehran \u00b7 7 Chicago", f_reg(9), BLACK)
text(8, 854, "8 SF \u00b7 9 Denver \u00b7 10 Austin \u00b7 11 Warsaw \u00b7 12 Kyiv \u00b7 13 Moscow", f_reg(9), BLACK)

# ALSO list: 2 columns x 9
also = [
    "Paris: 100+ back 2% billionaire tax", "Manchester: 12,000 cleared",
    "Zelenskyy: 165 missiles in a week", "COP31: the day after pact rejected",
    "Benghazi: UN demands port probe", "Israel unity talks resume",
    "Gaza: two killed in Israeli strike", "West Bank settler attacks",
    "Iran war: no deal in sight", "Lebanon seizes 264 kg explosives",
    "Bahrain: strike hits plant, 2 hurt", "Sudan: defences down drones",
    "DRC: fighting traps Ebola teams", "Bangladesh: Hasina jailed if she returns",
    "Seoul minister quits in exam row", "SK Telecom -7.3% as hype cools",
    "China eases margin rules", "Seoul readies 10T-won fund",
]
for i, item in enumerate(also):
    col, r = divmod(i, 9)
    x = 342 + col * 344
    y = 658 + r * 23
    text(x, y, f"{14 + i}. {item}", f_reg(11), BLACK)

# ---------- DATE CHECK ----------
d.rectangle([0, 872, W, 944], outline=RED, width=2)
text(12, 877, "DATE CHECK", f_bold(14), RED)
text(W - 12, 879, "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY", f_bold(9), RED, anchor="ra")
leftout = "LEFT OUT \u2014 NOT 23 NOV: Democrats reach 258 seats (22 Nov) \u00b7 Sparta II fire (22 Nov) \u00b7 El Chapo Isidro captured (22 Nov) \u00b7 EU\u2013Indonesia pact (21 Nov) \u00b7 Nigeria boat (21 Nov) \u00b7 ICJ Myanmar ruling (19 Nov)"
lo = wrap(leftout, f_reg(10), W - 24)
yy = 898
for ln in lo:
    text(12, yy, ln, f_reg(10), BLACK)
    yy += 13
text(12, yy + 2, "NOT YET: Dymer search continues (14 missing) \u00b7 4 House races uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped Ebola staff",
     f_reg(10), BLACK)

# ---------- Footer ----------
text(12, 950, "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 NYT \u00b7 ESPN \u00b7 Lowy Institute (Asia Power Index 2026).", f_reg(9), GRAY)
text(12, 961, "CHIPS: REPORTED = confirmed by wires \u00b7 CLAIM = one side's claim, not independently confirmed \u00b7 ONGOING = still developing", f_reg(9), GRAY)
text(12, 972, "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.", f_reg(9), GRAY)

# ---------- Bottom bar ----------
d.rectangle([0, 988, W, H], fill=BLACK)
text(W / 2, 999, "THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions", f_bold(15), GOLD, anchor="ma")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
