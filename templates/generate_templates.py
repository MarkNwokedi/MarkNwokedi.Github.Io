#!/usr/bin/env python3
"""Generate 3 comparable Supernote note-template PDF designs.

Page is a 3:4 portrait ratio (matches Supernote A6X2/Nomad and A5X2/Manta screens),
sized here at 768x1024 pt for crisp on-device rendering. Pure vector so it scales.
Designs share the same learning-science DNA (guiding Q -> notes -> free recall ->
atomic seeds -> connections -> quotes) but differ in structure/density/aesthetic.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, black, white

# ---- page geometry (3:4 portrait) ----
W, H = 768.0, 1024.0
M = 40.0  # outer margin

# grayscale palette (e-ink: only grays render; keep it high-contrast)
INK   = Color(0, 0, 0)
DARK  = Color(0.20, 0.20, 0.20)
MID   = Color(0.45, 0.45, 0.45)
LIGHT = Color(0.72, 0.72, 0.72)
FAINT = Color(0.86, 0.86, 0.86)
BAND  = Color(0.93, 0.93, 0.93)


def line(c, x1, y1, x2, y2, col=LIGHT, w=0.8, dash=None):
    c.setStrokeColor(col)
    c.setLineWidth(w)
    if dash:
        c.setDash(dash, 0)
    else:
        c.setDash([], 0)
    c.line(x1, y1, x2, y2)
    c.setDash([], 0)


def rrect(c, x, y, w, h, r=10, stroke=MID, fill=None, sw=1.0):
    c.setLineWidth(sw)
    c.setStrokeColor(stroke)
    if fill is not None:
        c.setFillColor(fill)
        c.roundRect(x, y, w, h, r, stroke=1, fill=1)
    else:
        c.roundRect(x, y, w, h, r, stroke=1, fill=0)


def label(c, x, y, text, size=9, col=MID, font="Helvetica-Bold", tracking=True):
    t = text.upper() if tracking else text
    c.setFillColor(col)
    c.setFont(font, size)
    if tracking and font == "Helvetica-Bold":
        # crude letter-spacing for tag-like labels
        cx = x
        for ch in t:
            c.drawString(cx, y, ch)
            cx += c.stringWidth(ch, font, size) + 1.1
    else:
        c.drawString(x, y, t)


def text(c, x, y, s, size=10, col=DARK, font="Helvetica"):
    c.setFillColor(col)
    c.setFont(font, size)
    c.drawString(x, y, s)


def ruled(c, x, y_top, w, n, gap, col=FAINT):
    """n horizontal writing rules going downward from y_top."""
    for i in range(n):
        yy = y_top - i * gap
        line(c, x, yy, x + w, yy, col=col, w=0.7)


def dotgrid(c, x, y, w, h, step=22, col=LIGHT):
    c.setFillColor(col)
    yy = y
    while yy <= y + h + 0.1:
        xx = x
        while xx <= x + w + 0.1:
            c.circle(xx, yy, 0.7, stroke=0, fill=1)
            xx += step
        yy += step


def checkbox(c, x, y, s=11, col=MID):
    c.setStrokeColor(col)
    c.setLineWidth(1.0)
    c.rect(x, y, s, s, stroke=1, fill=0)


# ============================================================
# DESIGN 1 — "Cornell" : familiar, two-column, structured recall
# ============================================================
def design_cornell(c):
    # --- header band ---
    c.setFillColor(BAND)
    c.rect(0, H - 92, W, 92, stroke=0, fill=1)
    label(c, M, H - 42, "Book Capture", size=15, col=INK)
    label(c, M, H - 64, "Cornell method  ·  one page per chapter", size=8, col=MID, tracking=False)
    # meta fields top-right
    c.setFont("Helvetica", 9); c.setFillColor(DARK)
    fx = W - M - 250
    for i, (lab, w) in enumerate([("BOOK", 250), ("CH.", 120), ("DATE", 120)]):
        pass
    # row of meta
    label(c, fx, H - 36, "BOOK", 7.5, MID); line(c, fx + 34, H - 38, W - M, H - 38, LIGHT)
    label(c, fx, H - 58, "CH.", 7.5, MID);  line(c, fx + 34, H - 60, fx + 120, H - 60, LIGHT)
    label(c, fx + 140, H - 58, "DATE", 7.5, MID); line(c, fx + 180, H - 60, W - M, H - 60, LIGHT)

    y = H - 92
    # --- guiding question strip ---
    gh = 56
    rrect(c, M, y - gh, W - 2 * M, gh, r=8, stroke=LIGHT)
    label(c, M + 12, y - 18, "Guiding question(s)", 8, MID)
    ruled(c, M + 12, y - 34, W - 2 * M - 24, 1, 0, FAINT)
    line(c, M + 12, y - 44, W - M - 12, y - 44, FAINT, 0.7)
    y -= gh + 16

    # --- main: cue column + notes ---
    main_top = y
    main_bot = M + 250
    cue_w = 150
    # divider
    line(c, M + cue_w, main_top, M + cue_w, main_bot, MID, 1.0)
    line(c, M, main_top, W - M, main_top, MID, 1.0)
    line(c, M, main_bot, W - M, main_bot, MID, 1.0)
    label(c, M + 6, main_top - 16, "Cues / keywords", 7.5, MID)
    label(c, M + cue_w + 10, main_top - 16, "Notes  (while reading)", 7.5, MID)
    # faint rules in notes area
    ny = main_top - 34
    while ny > main_bot + 8:
        line(c, M + cue_w + 8, ny, W - M - 8, ny, FAINT, 0.6)
        ny -= 26
    # cue area: just a couple of tag underlines
    for i in range(4):
        line(c, M + 6, main_top - 40 - i * 30, M + cue_w - 8, main_top - 40 - i * 30, FAINT, 0.6)

    # --- free recall band (emphasised) ---
    fr_h = 96
    fr_top = main_bot - 14
    c.setFillColor(BAND)
    c.roundRect(M, fr_top - fr_h, W - 2 * M, fr_h, 8, stroke=0, fill=1)
    rrect(c, M, fr_top - fr_h, W - 2 * M, fr_h, r=8, stroke=MID, sw=1.2)
    label(c, M + 12, fr_top - 18, "Free recall  —  book closed:  what did it argue? takeaway?", 8, INK)
    for i in range(3):
        line(c, M + 12, fr_top - 36 - i * 22, W - M - 12, fr_top - 36 - i * 22, LIGHT, 0.7)

    # --- atomic seeds + connections/quotes (two columns) ---
    by = fr_top - fr_h - 16
    col_w = (W - 2 * M - 16) / 2
    # left: atomic seeds
    label(c, M, by, "Atomic note seeds  (one idea each, my words)", 7.5, MID)
    for i in range(3):
        checkbox(c, M, by - 22 - i * 26, 10)
        line(c, M + 18, by - 22 - i * 26, M + col_w, by - 22 - i * 26, FAINT, 0.7)
    # right: connects + quotes
    rx = M + col_w + 16
    label(c, rx, by, "Connects to  /  quotes (pg)", 7.5, MID)
    for i in range(3):
        line(c, rx, by - 22 - i * 26, rx + col_w, by - 22 - i * 26, FAINT, 0.7)

    # footer review tracker
    line(c, M, M + 30, W - M, M + 30, LIGHT, 0.8)
    label(c, M, M + 14, "Reviewed:", 7.5, MID)
    for i, d in enumerate(["1d", "1w", "1m", "3m"]):
        checkbox(c, M + 70 + i * 70, M + 6, 11)
        text(c, M + 86 + i * 70, M + 8, d, 8, MID)


# ============================================================
# DESIGN 2 — "Slip-box" : minimalist, spacious, Zettelkasten
# ============================================================
def design_slipbox(c):
    # thin top rule + ID
    line(c, M, H - M, W - M, H - M, INK, 1.4)
    label(c, M, H - M + 8, "Permanent note", 9, MID)
    # ID + date right aligned
    c.setFont("Helvetica-Bold", 11); c.setFillColor(INK)
    c.drawRightString(W - M, H - M + 6, "ID  __________")

    # title line
    y = H - M - 30
    label(c, M, y, "Title / claim (one idea, full sentence)", 7.5, MID)
    line(c, M, y - 22, W - M, y - 22, MID, 1.0)
    y -= 46

    # large open writing area with very faint rules
    body_bot = M + 150
    ny = y - 6
    while ny > body_bot:
        line(c, M, ny, W - M, ny, FAINT, 0.6)
        ny -= 30

    # bottom meta zone: source + links + tags
    line(c, M, body_bot, W - M, body_bot, LIGHT, 0.9)
    zy = body_bot - 22
    label(c, M, zy, "Source", 7.5, MID)
    line(c, M + 46, zy - 2, W - M, zy - 2, FAINT, 0.7)
    zy -= 30
    label(c, M, zy, "Links  →", 7.5, MID)
    line(c, M + 52, zy - 2, W - M, zy - 2, FAINT, 0.7)
    zy -= 18
    line(c, M + 52, zy, W - M, zy, FAINT, 0.7)
    zy -= 30
    label(c, M, zy, "Tags  #", 7.5, MID)
    line(c, M + 50, zy - 2, W - M, zy - 2, FAINT, 0.7)

    # tiny footer affordance: next-review dots
    label(c, M, M + 8, "review:  1d   1w   1m   3m   6m", 7.5, LIGHT, tracking=False)


# ============================================================
# DESIGN 3 — "Dashboard" : dense, guided, dot-grid, built-in tracker
# ============================================================
def design_dashboard(c):
    # header bar (dark)
    c.setFillColor(DARK)
    c.rect(0, H - 70, W, 70, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(M, H - 44, "CHAPTER DASHBOARD")
    c.setFont("Helvetica", 8); c.setFillColor(Color(0.85, 0.85, 0.85))
    c.drawRightString(W - M, H - 30, "BOOK ____________________")
    c.drawRightString(W - M, H - 44, "CH ____   DATE ________   PG ____")

    y = H - 70

    def section(c, x, y, w, h, title):
        rrect(c, x, y - h, w, h, r=7, stroke=LIGHT, sw=1.0)
        c.setFillColor(BAND); c.roundRect(x, y - 20, w, 20, 7, stroke=0, fill=1)
        # square off bottom of the title tab
        c.setFillColor(BAND); c.rect(x, y - 20, w, 12, stroke=0, fill=1)
        label(c, x + 8, y - 14, title, 7, INK)
        return y - h

    gap = 12
    full = W - 2 * M
    half = (full - gap) / 2

    # 1. guiding questions (full)
    h1 = 56
    section(c, M, y - gap, full, h1, "① Guiding questions")
    for i in range(2):
        line(c, M + 10, y - gap - 32 - i * 18, W - M - 10, y - gap - 32 - i * 18, FAINT, 0.6)
    y = y - gap - h1

    # 2. notes (full, dot grid)  — the big one
    h2 = 300
    top2 = section(c, M, y - gap, full, h2, "② Notes  (while reading)")
    dotgrid(c, M + 12, top2 + 12, full - 24, h2 - 40, step=22, col=FAINT)
    y = top2

    # 3 & 4 side by side: free recall  |  atomic seeds
    h3 = 150
    top3 = section(c, M, y - gap, half, h3, "③ Free recall (closed book)")
    for i in range(4):
        line(c, M + 10, top3 + h3 - 34 - i * 26, M + half - 10, top3 + h3 - 34 - i * 26, FAINT, 0.6)
    section(c, M + half + gap, y - gap, half, h3, "④ Atomic seeds")
    for i in range(4):
        checkbox(c, M + half + gap + 10, top3 + h3 - 36 - i * 26, 9)
        line(c, M + half + gap + 26, top3 + h3 - 34 - i * 26, M + full - 10, top3 + h3 - 34 - i * 26, FAINT, 0.6)
    y = top3

    # 5 & 6: connections | quotes
    h5 = 96
    top5 = section(c, M, y - gap, half, h5, "⑤ Connects to")
    for i in range(3):
        line(c, M + 10, top5 + h5 - 32 - i * 22, M + half - 10, top5 + h5 - 32 - i * 22, FAINT, 0.6)
    section(c, M + half + gap, y - gap, half, h5, "⑥ Quotes (pg)")
    for i in range(3):
        line(c, M + half + gap + 10, top5 + h5 - 32 - i * 22, M + full - 10, top5 + h5 - 32 - i * 22, FAINT, 0.6)
    y = top5

    # 7. spaced-review tracker (full, boxed dates)
    h7 = 50
    top7 = section(c, M, y - gap, full, h7, "⑦ Spaced review")
    bx = M + 14
    for d in ["1 day", "1 wk", "2 wk", "1 mo", "3 mo", "6 mo"]:
        checkbox(c, bx, top7 + 10, 12)
        text(c, bx + 17, top7 + 12, d, 8, MID)
        bx += (full - 28) / 6


# ============================================================
def build(path, drawfn, title):
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle(title)
    drawfn(c)
    c.showPage()
    c.save()
    print("wrote", path)


if __name__ == "__main__":
    build("supernote-template-1-cornell.pdf",   design_cornell,   "Supernote Template 1 - Cornell")
    build("supernote-template-2-slipbox.pdf",   design_slipbox,   "Supernote Template 2 - Slip-box")
    build("supernote-template-3-dashboard.pdf", design_dashboard, "Supernote Template 3 - Dashboard")
