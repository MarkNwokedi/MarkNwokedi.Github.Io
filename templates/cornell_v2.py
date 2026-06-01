#!/usr/bin/env python3
"""Cornell-style "Book Capture" planner for the Supernote Manta (e-ink).

Base canvas 768x1024 pt (3:4). Final export renders to 1920x2560 px (scale 2.5x),
the Manta's native panel. Pure vector, grayscale only, high contrast.

Design system
-------------
- Grid: equal outer margins; a single baseline pitch (P) drives EVERY writing rule
  so the whole sheet shares one vertical rhythm.
- Type: Times (serif) display title for craft; an all-caps tracked Helvetica-Bold
  SECTION-LABEL system; an oblique helper-text style. One consistent hierarchy.
- Structural motif: a left ACCENT TICK + a thin DOUBLE-RULE under every section
  label. All corners square. No rounded boxes, no decorative fills.
- Importance: Notes is the hero (largest), then Free recall, then the seed rows.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz  # pymupdf for rendering

# ---- register serif for the display title ----
SERIF = "Helvetica"  # fallback
try:
    pdfmetrics.registerFont(TTFont("BookSerif", "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("BookSerif-Bold", "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"))
    SERIF = "BookSerif"
    SERIF_B = "BookSerif-Bold"
except Exception:
    SERIF_B = "Helvetica-Bold"

# ---- page geometry ----
W, H = 768.0, 1024.0
M = 56.0                 # equal outer margin
P = 52.0                 # ONE writing-line pitch everywhere (~11mm on device)

# ---- grayscale palette (e-ink; high contrast) ----
INK    = Color(0, 0, 0)          # primary marks / title
NEAR   = Color(0.12, 0.12, 0.12) # strong text
LABEL  = Color(0.32, 0.32, 0.32) # section labels
HELP   = Color(0.46, 0.46, 0.46) # helper text
STRUCT = Color(0.40, 0.40, 0.40) # structural hairlines (column / frame)
RULE   = Color(0.66, 0.66, 0.66) # secondary structure
WRITE  = Color(0.72, 0.72, 0.72) # writing rules (~28% -> visible, not loud)

SANS = "Helvetica"
SANS_B = "Helvetica-Bold"


# ---------- primitives ----------
def hline(c, x1, x2, y, col=WRITE, w=0.8):
    c.setStrokeColor(col); c.setLineWidth(w); c.setDash([], 0)
    c.line(x1, y, x2, y)


def vline(c, x, y1, y2, col=STRUCT, w=1.0):
    c.setStrokeColor(col); c.setLineWidth(w); c.setDash([], 0)
    c.line(x, y1, x, y2)


def tracked(c, x, y, s, font, size, col, tracking=1.4):
    """Draw letter-spaced (tracked) text, return end x."""
    c.setFillColor(col); c.setFont(font, size)
    cx = x
    for ch in s:
        c.drawString(cx, y, ch)
        cx += c.stringWidth(ch, font, size) + tracking
    return cx - tracking


def tracked_width(c, s, font, size, tracking):
    w = 0.0
    for ch in s:
        w += c.stringWidth(ch, font, size) + tracking
    return w - tracking


def section_label(c, x, y, x_end, text, tick=True, helper_text=None):
    """All-caps tracked label + the double-rule motif under it, with a left tick.

    Optional helper_text is right-aligned to the rule end (oblique, mid-gray),
    sitting on the same baseline as the label so it never collides.
    """
    label_size = 8.5
    lx = x + (12 if tick else 0)
    tracked(c, lx, y, text.upper(), SANS_B, label_size, LABEL, 1.6)
    if helper_text:
        c.setFont("Helvetica-Oblique", 7.5)
        hw = c.stringWidth(helper_text, "Helvetica-Oblique", 7.5)
        c.setFillColor(HELP)
        c.drawString(x_end - hw, y, helper_text)
    rule_y = y - 8
    # double rule under the whole zone width
    hline(c, x, x_end, rule_y, col=STRUCT, w=1.1)
    hline(c, x, x_end, rule_y - 2.6, col=RULE, w=0.5)
    # left accent tick (the one motif)
    if tick:
        c.setStrokeColor(INK); c.setLineWidth(2.4)
        c.line(x, y + 8.5, x, y - 2.0)
    return rule_y


def helper(c, x, y, s, col=HELP, size=7.5):
    c.setFillColor(col); c.setFont("Helvetica-Oblique", size)
    c.drawString(x, y, s)


def checkbox(c, x, y, s=11, col=LABEL):
    c.setStrokeColor(col); c.setLineWidth(1.1); c.setDash([], 0)
    c.rect(x, y, s, s, stroke=1, fill=0)


def write_rules(c, x1, x2, y_first, n, col=WRITE, w=0.8):
    for i in range(n):
        hline(c, x1, x2, y_first - i * P, col=col, w=w)


# ---------- layout constants ----------
LABEL_GAP = 30.0   # label baseline -> first writing rule
ZONE_GAP  = 34.0   # bottom rule of a zone -> next label baseline
N_NOTES   = 7      # hero line count (dominant zone)


# ---------- the page ----------
def design(c):
    L = M
    R = W - M
    inner = R - L

    # ============ 1. IDENTITY / TITLE BLOCK ============
    title_base = H - M - 22
    c.setFillColor(INK); c.setFont(SERIF_B, 30)
    c.drawString(L, title_base, "Book Capture")
    helper(c, L, title_base - 17, "Cornell capture  ·  one page per chapter", HELP, 8.5)

    # meta fields: right-aligned stacked block (BOOK on top, CH. + DATE below).
    # Bottom row baseline aligns with the serif title baseline for a tight lockup.
    mx = L + inner * 0.50
    m_top = title_base + 18
    m_bot = title_base
    tracked(c, mx, m_top, "BOOK", SANS_B, 7.5, LABEL, 1.4)
    hline(c, mx + 38, R, m_top - 2, col=RULE, w=0.9)
    tracked(c, mx, m_bot, "CH.", SANS_B, 7.5, LABEL, 1.4)
    chx = mx + 32
    hline(c, chx, mx + inner * 0.22, m_bot - 2, col=RULE, w=0.9)
    dlx = mx + inner * 0.27
    tracked(c, dlx, m_bot, "DATE", SANS_B, 7.5, LABEL, 1.4)
    hline(c, dlx + 40, R, m_bot - 2, col=RULE, w=0.9)

    # strong rule closing the identity block (top of structural grid)
    id_rule = title_base - 30
    hline(c, L, R, id_rule, col=INK, w=1.5)

    # ============ 2. GUIDING QUESTION ============
    gq_label_y = id_rule - 28
    section_label(c, L, gq_label_y, R, "Guiding question(s)")
    gq_top = gq_label_y - LABEL_GAP
    hline(c, L, R, gq_top, col=WRITE)
    hline(c, L, R, gq_top - P, col=WRITE)
    gq_bottom = gq_top - P

    # ============ 3. CORNELL CORE (hero) ============
    core_label_y = gq_bottom - ZONE_GAP
    cue_w = 158
    cue_x = L
    notes_x = L + cue_w + 20
    section_label(c, cue_x, core_label_y, L + cue_w, "Cues")
    section_label(c, notes_x, core_label_y, R, "Notes", tick=False,
                  helper_text="while reading")

    core_top = core_label_y - LABEL_GAP
    core_bottom = core_top - (N_NOTES - 1) * P
    for i in range(N_NOTES):
        y = core_top - i * P
        hline(c, cue_x, L + cue_w - 8, y, col=WRITE)        # cue rule
        hline(c, notes_x, R, y, col=WRITE)                  # notes rule (aligned)
    vline(c, L + cue_w, core_top + 14, core_bottom - 12, col=STRUCT, w=1.1)

    # ============ 4. FREE RECALL ============
    fr_label_y = core_bottom - ZONE_GAP
    section_label(c, L, fr_label_y, R, "Free recall", tick=True,
                  helper_text="book closed — what did it argue?  takeaway?")
    fr_top = fr_label_y - LABEL_GAP
    for i in range(3):
        hline(c, L, R, fr_top - i * P, col=WRITE)
    fr_bottom = fr_top - 2 * P

    # ============ 5. SEEDS + CONNECTIONS ============
    half = (inner - 28) / 2
    sx1 = L
    sx2 = L + half + 28
    seed_label_y = fr_bottom - ZONE_GAP
    section_label(c, sx1, seed_label_y, sx1 + half, "Atomic note seeds",
                  helper_text="one idea each")
    section_label(c, sx2, seed_label_y, sx2 + half, "Connects to / quotes", tick=False,
                  helper_text="page")
    seed_top = seed_label_y - LABEL_GAP
    for i in range(3):
        y = seed_top - i * P
        checkbox(c, sx1, y - 4, 11)
        hline(c, sx1 + 20, sx1 + half, y, col=WRITE)
        hline(c, sx2, sx2 + half, y, col=WRITE)


def build_pdf(path):
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("Book Capture — Cornell")
    design(c)
    c.showPage()
    c.save()
    print("wrote", path)


def render_png(pdf_path, png_path, target_w=None):
    doc = fitz.open(pdf_path)
    page = doc[0]
    if target_w:
        zoom = target_w / W
    else:
        zoom = 1.4
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
    pix.save(png_path)
    print("rendered", png_path, pix.width, "x", pix.height)
    doc.close()


if __name__ == "__main__":
    build_pdf("supernote-cornell-medium.pdf")
    # working preview (~1.4x)
    render_png("supernote-cornell-medium.pdf", "preview-v2.png", target_w=1075)
    # final device export: exactly 1920x2560 (2.5x of 768x1024)
    render_png("supernote-cornell-medium.pdf", "supernote-cornell-medium-manta.png", target_w=1920)
