#!/usr/bin/env python3
"""Typeset the Book Note System starter guide as a clean, print-ready PDF.

Letter size, serif headings (Liberation Serif) + Helvetica body, real tables,
and a boxed monospace cheat sheet. Pure reportlab Platypus.
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                ListFlowable, ListItem, Preformatted, HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---- fonts ----
SERIF_B = "Helvetica-Bold"
try:
    pdfmetrics.registerFont(TTFont("GSerif", "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("GSerif-Bold", "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"))
    SERIF, SERIF_B = "GSerif", "GSerif-Bold"
except Exception:
    SERIF = "Helvetica"

# ---- palette ----
INK    = Color(0.08, 0.08, 0.08)
DARK   = Color(0.20, 0.20, 0.20)
GRAY   = Color(0.42, 0.42, 0.42)
STRUCT = Color(0.40, 0.40, 0.40)
GRID   = Color(0.78, 0.78, 0.78)
BAND   = Color(0.93, 0.93, 0.93)
BOX    = Color(0.96, 0.96, 0.96)

# ---- styles ----
title = ParagraphStyle("title", fontName=SERIF_B, fontSize=24, leading=27, textColor=INK, spaceAfter=4)
intro = ParagraphStyle("intro", fontName="Helvetica-Oblique", fontSize=9.5, leading=13.5, textColor=GRAY, spaceAfter=2)
h2    = ParagraphStyle("h2", fontName=SERIF_B, fontSize=14.5, leading=17, textColor=INK,
                       spaceBefore=15, spaceAfter=5)
sub   = ParagraphStyle("sub", fontName="Helvetica-Bold", fontSize=9.5, leading=13, textColor=DARK,
                       spaceBefore=7, spaceAfter=2)
body  = ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, leading=14, textColor=DARK, spaceAfter=5)
lead  = ParagraphStyle("lead", parent=body, spaceAfter=3)
cell  = ParagraphStyle("cell", fontName="Helvetica", fontSize=8.7, leading=11.5, textColor=DARK)
cellb = ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=8.7, leading=11.5, textColor=INK)
mono  = ParagraphStyle("mono", fontName="Courier", fontSize=8.2, leading=11.6, textColor=INK)


def C(t, bold=False):
    return Paragraph(t, cellb if bold else cell)


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, body), leftIndent=12) for t in items],
        bulletType="bullet", start="•", leftIndent=16, bulletFontSize=7,
        bulletColor=GRAY, spaceBefore=1, spaceAfter=1,
    )


def numbered(items):
    return ListFlowable(
        [ListItem(Paragraph(t, body), leftIndent=14) for t in items],
        bulletType="1", leftIndent=18, bulletFontName="Helvetica-Bold",
        bulletFontSize=9, spaceBefore=1, spaceAfter=1,
    )


def make_table(data, colWidths, header=True):
    t = Table(data, colWidths=colWidths, hAlign="LEFT")
    s = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, GRID),
    ]
    if header:
        s += [("BACKGROUND", (0, 0), (-1, 0), BAND),
              ("LINEBELOW", (0, 0), (-1, 0), 0.9, STRUCT)]
    t.setStyle(TableStyle(s))
    return t


def cheatsheet(text):
    """Monospace cheat sheet inside a shaded, padded box."""
    p = Preformatted(text, mono)
    box = Table([[p]], colWidths=[6.4 * inch])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX),
        ("BOX", (0, 0), (-1, -1), 0.6, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return box


def rule():
    return HRFlowable(width="100%", thickness=1.4, color=INK, spaceBefore=6, spaceAfter=2)


def build(path):
    doc = SimpleDocTemplate(path, pagesize=LETTER,
                            leftMargin=0.85 * inch, rightMargin=0.85 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                            title="Book Note System — Starter Guide")
    E = []
    E.append(Paragraph("Book Note System", title))
    E.append(Paragraph("A starter guide &mdash; read non-fiction, retain it, and be able to explain "
                       "and write about it. &nbsp;Physical books &rarr; Supernote Manta (Book Capture "
                       "template) &rarr; spaced-repetition retention loop.", intro))
    E.append(Paragraph("Keep this nearby for your first few books. After that it&rsquo;s muscle memory.", intro))
    E.append(rule())

    E.append(Paragraph("The one idea behind all of it", h2))
    E.append(Paragraph("<b>Reading is passive recognition; retention requires active production.</b> "
                       "Every step below makes you <i>produce</i> something &mdash; a recall, an explanation, "
                       "a note &mdash; instead of re-reading. If a step feels a little effortful, that&rsquo;s the "
                       "point. Highlighting and re-reading feel productive but are weak: they create an "
                       "<i>illusion</i> of knowing. The work is in the recall and the notes.", body))

    E.append(Paragraph("Your setup at a glance", h2))
    E.append(make_table([
        [C("Layer", True), C("Tool", True), C("Job", True)],
        [C("Capture + thinking"), C("Supernote Manta + Book Capture template"), C("Read, mark, recall, distill &mdash; by hand")],
        [C("Permanent notes"), C("Slip-box notebook (or Obsidian)"), C("One idea per note, linked, kept forever")],
        [C("Retention + reminders"), C("Anki / RemNote (spaced repetition)"), C("Tells you what to review, and when")],
        [C("Synthesis (optional)"), C("NotebookLM"), C("Quiz yourself / compare across books")],
    ], colWidths=[1.5 * inch, 2.2 * inch, 3.1 * inch]))
    E.append(Spacer(1, 5))
    E.append(Paragraph("Handwriting is an advantage &mdash; slower and more effortful than typing, which means "
                       "better encoding. Use it.", body))

    E.append(Paragraph("The workflow (four phases)", h2))
    E.append(Paragraph("1 &middot; Before a book &mdash; <font color='#777777'>5 min, once per book</font>", sub))
    E.append(bullets([
        "<b>Inspect it first.</b> Skim the cover, table of contents, intro, and index to get the shape of the argument.",
        "<b>Decide why you&rsquo;re reading it.</b> Write 1&ndash;2 questions you want answered &mdash; these go in the <b>Guiding question(s)</b> box and aim your attention.",
    ]))
    E.append(Paragraph("2 &middot; While reading &mdash; <font color='#777777'>one Book Capture page per chapter</font>", sub))
    E.append(bullets([
        "<b>Pencil in hand.</b> Underline sparingly &mdash; only what matters. Capturing everything = capturing nothing.",
        "In the <b>Notes</b> column, jot <b>why</b> a passage matters or how it connects &mdash; not just what it says.",
        "Put 2&ndash;4 <b>keywords</b> per page in the <b>Cues</b> column &mdash; these become search tags (the Manta searches handwriting).",
        "Don&rsquo;t transcribe yet. Notes here are <i>meant</i> to be messy and follow the chapter.",
    ]))
    E.append(Paragraph("3 &middot; After each chapter &mdash; <font color='#777777'>the most important step, ~10 min</font>", sub))
    E.append(numbered([
        "<b>Close the book.</b> In <b>Free recall</b>, write from memory what the chapter argued and the takeaway. This does most of the work. It feels harder than re-reading &mdash; good.",
        "<b>Check</b> your recall against your marks; fill gaps.",
        "<b>Distill 2&ndash;4 Atomic note seeds</b> &mdash; the ideas worth keeping, each as one short claim in your own words.",
        "Log any <b>Gaps</b>: what you didn&rsquo;t understand, and &mdash; once resolved &mdash; how you closed it.",
    ]))
    E.append(Paragraph("4 &middot; Weekly &mdash; <font color='#777777'>~20&ndash;30 min</font>", sub))
    E.append(bullets([
        "<b>Convert</b> the week&rsquo;s pages to text (handwriting recognition &rarr; export) and turn atomic seeds into <b>permanent notes</b> (one idea each, fully written, linked).",
        "<b>Make/approve flashcards</b> from those notes, then do your <b>spaced-repetition reviews</b> (a few minutes most days).",
        "Monthly, or when an idea-cluster forms, <b>write something</b> from your notes. Teaching it is the deepest retention step &mdash; and your end goal.",
    ]))

    E.append(Paragraph("How to fill each zone of the Book Capture page", h2))
    E.append(make_table([
        [C("Zone", True), C("What goes here", True), C("When", True)],
        [C("Book / Ch. / Date"), C("Identity, so the page is findable"), C("Start of chapter")],
        [C("Guiding question(s)"), C("1&ndash;2 questions you want answered"), C("Before reading")],
        [C("Cues / Keywords"), C("2&ndash;4 search tags per page"), C("While reading")],
        [C("Notes (while reading)"), C("Raw, multi-idea, follows the chapter &mdash; <i>not</i> atomic"), C("While reading")],
        [C("Free recall"), C("From memory, book closed: argument + takeaway"), C("After the chapter")],
        [C("Atomic note seeds"), C("2&ndash;4 single ideas, your words"), C("After the chapter")],
        [C("Gaps"), C("<i>what it was</i> / <i>how it was closed</i>"), C("As they arise / once resolved")],
    ], colWidths=[1.55 * inch, 3.45 * inch, 1.8 * inch]))
    E.append(Spacer(1, 4))
    E.append(Paragraph("The <b>Notes</b> zone is supposed to be messy and cover many ideas. The <b>Atomic "
                       "seeds</b> zone is where you decompose those into separate, single ideas. Don&rsquo;t "
                       "confuse the two.", body))

    E.append(Paragraph("Atomic notes &mdash; the core skill", h2))
    E.append(Paragraph("A chapter contains <b>many</b> ideas. An atomic note holds <b>exactly one</b>. So one "
                       "chapter becomes <b>several</b> atomic notes &mdash; you&rsquo;re <i>decomposing</i> the "
                       "chapter, not summarizing it.", body))
    E.append(Paragraph("A note is atomic when:", lead))
    E.append(bullets([
        "You can <b>title it with the idea itself</b> &mdash; &ldquo;Retrieval beats rereading&rdquo; &mdash; not a topic (&ldquo;Memory&rdquo;) or a location (&ldquo;Chapter 3&rdquo;).",
        "It&rsquo;s in <b>your own words</b>, a full sentence, standing on its own.",
        "You could <b>link it to a note from a different book</b> and it would still make sense.",
    ]))
    E.append(Paragraph("<b>Gut check:</b> if describing the note needs the word <i>&ldquo;and,&rdquo;</i> it&rsquo;s "
                       "probably <b>two</b> notes. Be selective &mdash; three sharp atomic notes beat a full-page "
                       "summary.", body))
    E.append(Paragraph("<i>Example &mdash; one chapter on &ldquo;anchoring&rdquo; might yield:</i> "
                       "&ldquo;Anchoring: an arbitrary number drags your estimate toward it.&rdquo; &middot; "
                       "&ldquo;Anchoring works even when the anchor is obviously random.&rdquo; &middot; "
                       "&ldquo;In negotiation, the first offer sets the anchor for the range.&rdquo;", body))

    E.append(Paragraph("The retention loop (makes it stick + reminds you)", h2))
    E.append(Paragraph("Notes alone don&rsquo;t create memory &mdash; <b>spaced retrieval</b> does. Wire your "
                       "seeds into a spaced-repetition app so it schedules reviews and reminds you:", body))
    E.append(numbered([
        "Turn key permanent notes into <b>flashcards</b>. Phrase the front as a real question (&ldquo;Why does retrieval beat rereading?&rdquo;), not a keyword.",
        "Use <b>Anki</b> or <b>RemNote</b> (FSRS). It shows each card right before you&rsquo;d forget it.",
        "<b>Review a few minutes most days.</b> Turn on the app&rsquo;s daily notification &mdash; that&rsquo;s your reminder.",
        "Spacing scales with your goal: to remember for a year, reviews stretch to months apart. The app handles it; you just show up.",
    ]))

    E.append(Paragraph("Pitfalls to avoid", h2))
    E.append(bullets([
        "<b>Collector&rsquo;s fallacy.</b> Saving/highlighting &ne; knowing. The note in your own words is the asset.",
        "<b>Passive re-reading &amp; highlighting.</b> Feels productive, builds little. Replace with free recall.",
        "<b>Over-tooling.</b> Don&rsquo;t perfect the system instead of using it. Two notebooks and a keyword habit is enough.",
        "<b>Summarizing instead of decomposing.</b> A summary is one blob; you want several atomic, linkable ideas.",
        "<b>Skipping the recall step</b> because it&rsquo;s harder than re-reading. That difficulty <i>is</i> the learning.",
    ]))

    E.append(Paragraph("One-page cheat sheet", h2))
    E.append(cheatsheet(
        "BEFORE   inspect the book; write 1-2 guiding questions.\n"
        "DURING   light marks; note WHY it matters; keywords in the cue column.\n"
        "AFTER    1. close book, FREE RECALL from memory\n"
        "         2. check against marks\n"
        "         3. distill 2-4 ATOMIC SEEDS (one idea each, your words)\n"
        "         4. log GAPS (what it was / how closed)\n"
        "WEEKLY   export -> permanent notes -> flashcards -> spaced reviews\n"
        "         -> (monthly) write something.\n"
        "\n"
        "ATOMIC NOTE = one idea, titled by the idea, your words, linkable.\n"
        "              If it needs \"and\", it's two notes.\n"
        "\n"
        "RULE OF THUMB: produce, don't re-read. If it's a little hard, it's working."
    ))
    doc.build(E)
    print("wrote", path)


if __name__ == "__main__":
    build("book-note-system-guide.pdf")
