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
# --- Notes-area line-spacing presets (base units; x2.5 -> Manta px; ~mm @300dpi) ---
GAP_TIGHT, GAP_MED, GAP_WIDE = 42, 52, 66   # ~9mm / ~11mm / ~14mm


def design_cornell(c, note_gap=GAP_MED, page_num=None, total=None, link_back_to=None):
    # --- header band ---
    c.setFillColor(BAND)
    c.rect(0, H - 92, W, 92, stroke=0, fill=1)
    label(c, M, H - 42, "Book Capture", size=15, col=INK)
    label(c, M, H - 64, "Cornell method  ·  one page per chapter", size=8, col=MID, tracking=False)
    # meta fields top-right
    fx = W - M - 250
    label(c, fx, H - 36, "BOOK", 7.5, MID); line(c, fx + 34, H - 38, W - M, H - 38, LIGHT)
    label(c, fx, H - 58, "CH.", 7.5, MID);  line(c, fx + 34, H - 60, fx + 120, H - 60, LIGHT)
    label(c, fx + 140, H - 58, "DATE", 7.5, MID); line(c, fx + 180, H - 60, W - M, H - 60, LIGHT)
    # page number (multi-page notebooks only)
    if page_num is not None:
        c.setFillColor(MID); c.setFont("Helvetica", 7)
        c.drawCentredString(W / 2, H - 86, "page %02d%s" % (page_num, ("  /  %d" % total) if total else ""))

    y = H - 92
    # --- guiding question strip ---
    gh = 56
    rrect(c, M, y - gh, W - 2 * M, gh, r=8, stroke=LIGHT)
    label(c, M + 12, y - 18, "Guiding question(s)", 8, MID)
    line(c, M + 12, y - 34, W - M - 12, y - 34, FAINT, 0.7)
    line(c, M + 12, y - 44, W - M - 12, y - 44, FAINT, 0.7)
    y -= gh + 16

    # --- main: cue column + notes (rules aligned across both, true Cornell) ---
    main_top = y
    main_bot = M + 215
    cue_w = 150
    line(c, M + cue_w, main_top, M + cue_w, main_bot, MID, 1.0)
    line(c, M, main_top, W - M, main_top, MID, 1.0)
    line(c, M, main_bot, W - M, main_bot, MID, 1.0)
    label(c, M + 6, main_top - 16, "Cues / keywords", 7.5, MID)
    label(c, M + cue_w + 10, main_top - 16, "Notes  (while reading)", 7.5, MID)
    ny = main_top - 34
    while ny > main_bot + 8:
        line(c, M + 6, ny, M + cue_w - 8, ny, FAINT, 0.6)          # cue rule
        line(c, M + cue_w + 8, ny, W - M - 8, ny, FAINT, 0.6)      # notes rule (aligned)
        ny -= note_gap

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
    label(c, M, by, "Atomic note seeds  (one idea each, my words)", 7.5, MID)
    for i in range(3):
        checkbox(c, M, by - 22 - i * 26, 10)
        line(c, M + 18, by - 22 - i * 26, M + col_w, by - 22 - i * 26, FAINT, 0.7)
    rx = M + col_w + 16
    label(c, rx, by, "Connects to  /  quotes (pg)", 7.5, MID)
    for i in range(3):
        line(c, rx, by - 22 - i * 26, rx + col_w, by - 22 - i * 26, FAINT, 0.7)

    # optional "back to index" button (multi-page linked notebook)
    if link_back_to is not None:
        bw, bh = 104, 22
        bx, byk = W - M - bw, M + 6
        rrect(c, bx, byk, bw, bh, r=6, stroke=MID, sw=1.0)
        c.setFillColor(DARK); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(bx + bw / 2, byk + 7, "«  INDEX")
        c.linkRect("", link_back_to, (bx, byk, bx + bw, byk + bh), Border='[0 0 0]', relative=0)


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


def build_index_pdf(path, n_pages=60, note_gap=GAP_MED, title="Book Notes - Cornell"):
    """Multi-page notebook: an Index page hyperlinked to N Cornell capture pages."""
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle(title)

    # ---------- INDEX / HOME page ----------
    c.bookmarkPage("index")
    c.setFillColor(DARK); c.rect(0, H - 84, W, 84, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 16)
    c.drawString(M, H - 48, "INDEX")
    c.setFillColor(Color(0.85, 0.85, 0.85)); c.setFont("Helvetica", 8)
    c.drawString(M, H - 66, "tap an entry to jump to its capture page  ·  write book + chapter on the line")
    c.setFillColor(white); c.setFont("Helvetica", 8)
    c.drawRightString(W - M, H - 48, "BOOK ____________________")

    cols = 3
    rows = n_pages // cols
    gy_top = H - 108
    col_w = (W - 2 * M) / cols
    row_h = (gy_top - (M + 32)) / rows
    for i in range(n_pages):
        num = i + 1
        col = i // rows
        row = i % rows
        ex = M + col * col_w
        ey = gy_top - row * row_h
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 9)
        c.drawString(ex + 4, ey - 11, "%02d" % num)
        line(c, ex + 26, ey - 13, ex + col_w - 12, ey - 13, FAINT, 0.7)
        # tappable area over the whole entry row
        c.linkRect("", "page%02d" % num, (ex, ey - row_h + 4, ex + col_w - 8, ey + 3),
                   Border='[0 0 0]', relative=0)
    line(c, M, M + 24, W - M, M + 24, LIGHT, 0.8)
    label(c, M, M + 8, "Cornell capture  ·  %d pages  ·  keep keywords in the cue column for search" % n_pages,
          7.5, MID, tracking=False)
    c.showPage()

    # ---------- capture pages ----------
    for i in range(n_pages):
        num = i + 1
        c.bookmarkPage("page%02d" % num)
        design_cornell(c, note_gap=note_gap, page_num=num, total=n_pages, link_back_to="index")
        c.showPage()

    c.save()
    print("wrote", path, "(%d pages)" % (n_pages + 1))


if __name__ == "__main__":
    # --- original three comparison designs (unchanged) ---
    build("supernote-template-1-cornell.pdf",   design_cornell,   "Supernote Template 1 - Cornell")
    build("supernote-template-2-slipbox.pdf",   design_slipbox,   "Supernote Template 2 - Slip-box")
    build("supernote-template-3-dashboard.pdf", design_dashboard, "Supernote Template 3 - Dashboard")

    # --- finalized Cornell: medium spacing, repeating template (chosen) ---
    build("supernote-cornell-medium.pdf", lambda c: design_cornell(c, note_gap=GAP_MED), "Cornell - medium")
