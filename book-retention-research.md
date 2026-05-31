# Reading to Retain & Convey: Research Report

*A research brief on reading non-fiction to durably retain knowledge, explain ideas
clearly, connect them across books, and turn them into published writing — plus the
current tool landscape and a buildable custom system.*

**Prepared:** 2026-05-31

---

## 0. TL;DR

The bottleneck in "reading a lot but not retaining it" is almost never reading speed
or memory capacity — it's that **reading is passive recognition, and retention requires
active production.** The research is unusually clear and consistent on what works:

1. **Retrieve, don't reread.** After each section, close the book and recall/summarize
   from memory. This single habit (the "testing effect") is the highest-leverage change
   you can make.
2. **Space it out.** Re-engage with material over days and weeks, not in one sitting.
3. **Explain it as if teaching** (Feynman technique) — generating the explanation, in
   your own words, is where understanding and conveyability are built.
4. **Write atomic, linked notes** in your own words (Zettelkasten / evergreen notes).
   This is what lets ideas *connect across books* and become *the raw material for
   publishing*.
5. **Highlighting and rereading feel productive but are weak** — they create an
   "illusion of competence." Use them only as the *raw capture step* that feeds steps 1–4.

For tools: the realistic choice is **(a) an integrated app — RemNote** (notes +
auto-flashcards + AI in one place), or **(b) a stack — Readwise/Reader → Obsidian →
Anki**, optionally with **NotebookLM** for AI synthesis. A **custom system** on your
github.io site is very feasible using plain-markdown notes in git + an FSRS spaced-
repetition library + an LLM API for auto-quizzing — sketched in §6.

---

## 1. The learning science — what actually works

> Confidence key: ★★★ = strong, replicated, meta-analytic; ★★ = supported but
> moderated by conditions; ★ = weak / contested / popular-but-unproven.

### 1.1 Retrieval practice (the "testing effect") — ★★★
Pulling information *out* of memory produces far better long-term retention than putting
it back *in* by rereading.

- In the landmark Roediger & Karpicke (2006) study, people who read a prose passage and
  then **recalled** it retained substantially more on delayed tests (days/weeks later)
  than people who **reread** it — even though the rereaders did slightly *better* on an
  immediate 5-minute test. This is a clean "learning vs. performance" dissociation: the
  thing that feels better in the moment is worse for durable learning.
- Meta-analysis (Rowland 2014) puts the testing-vs-restudy benefit at a **medium-to-large
  effect (g ≈ 0.50)**, and **recall/production tests beat recognition tests** — i.e.,
  free recall ("what did that chapter argue?") beats multiple-choice.
- Retrieval practice even **beats elaborate concept-mapping** for learning from science
  texts, *including on inference questions* (Karpicke & Blunt 2011, *Science*) — so it
  builds comprehension, not just rote facts.
- *Caveat:* most foundational evidence is on factual/surface outcomes; transfer to
  complex comprehension is real but smaller and benefits from **feedback** (check your
  recall against the source).

**Apply to reading:** after each section/chapter, close the book and write — from memory —
what it said and why it matters. Then check.

### 1.2 Spaced (distributed) practice — ★★★
- Spacing reliably beats cramming. Cepeda et al. (2006) reviewed 184 articles / 317
  experiments; distributed practice won across study types and ages.
- **Optimal gap scales with how long you want to remember:** roughly **20–40% of the
  retention interval** for week-scale goals, dropping toward **5–10%** for year-scale
  goals (Cepeda et al. 2008). The function is broad and forgiving — you don't need to be
  precise, just don't do it all at once.
- Forgetting after a single exposure is rapid (Ebbinghaus's "forgetting curve"), which
  is *why* spacing is needed. *(The often-quoted "67% forgotten in 24 hours" is
  illustrative, not precise — Ebbinghaus tested one person on nonsense syllables.)*
- **Retrieval + spacing are most powerful combined** — i.e., spaced retrieval. This is
  exactly what spaced-repetition software automates.

### 1.3 Elaboration & self-explanation — ★★
- **Self-explanation** ("how does this work? how does it relate to what I know?") while
  reading improves learning at about **g ≈ 0.55** across ~64 studies; strongest for
  conceptual material.
- **Elaborative interrogation** (asking/answering "*why* is this true?") helps — but is
  **moderated by prior knowledge**: it works better when you already have background, and
  low-knowledge learners can form *wrong* connections. So elaborate, but verify.

### 1.4 The Feynman technique / learning-by-teaching — ★★
- The benefit comes from **actually generating the explanation, not merely intending to
  teach.** Fiorella & Mayer (2013): students who *actually taught* (e.g., recorded a
  lesson) beat those who only *expected* to teach on delayed comprehension. "I'll explain
  this later" doesn't work; explaining now does.
- This is the direct bridge to your goal of **conveying ideas clearly** — the act of
  explaining simply *is* the practice of conveying, and it surfaces the gaps in your
  understanding.

### 1.5 Interleaving — ★★
- Mixing problem/concept types (vs. blocking one type) hurts practice-session performance
  but can **roughly double** delayed-test scores (Taylor & Rohrer 2010, in math).
- *Caveat:* strongest evidence is for **discriminating between confusable categories**;
  benefits depend on how similar the categories are (Firth et al. 2021). For reading,
  this means **reading several related books/sources side by side** (syntopical reading —
  §2.1) helps you tell competing ideas apart.

### 1.6 Dual coding — ★★
- Words + relevant visuals beat words alone — **but only** when text and image are
  coherent and don't overload (Mayer's multimedia principle). Sketching a diagram of an
  argument is a legitimate retention aid. *(The viral "89% improvement" stat is a single
  illustrative result, not a constant.)*

### 1.7 The "desirable difficulties" frame — ★★★
- Bjork & Bjork: conditions that **slow acquisition but improve long-term
  retention/transfer** — spacing, interleaving, retrieval, generation, varied practice.
  The unifying lesson: **performance during study is an unreliable indicator of
  learning.** If it feels a little hard and slow, it's often working.

### 1.8 What *doesn't* work (avoid the traps) — ★/debunked
- **Rereading and highlighting/underlining are low-utility** (Dunlosky et al. 2013, the
  major review that rated 10 techniques). They produce a **"fluency illusion"** —
  familiarity mistaken for mastery. Only **practice testing** and **distributed practice**
  earned a **high-utility** rating; summarization, highlighting, rereading, keyword
  mnemonics, and imagery-for-text were rated **low**.
- **"Learning styles" (visual/auditory/kinesthetic matching) is debunked** (Pashler et
  al. 2008). The studies using the proper design found no benefit. Don't waste effort
  tailoring to a "style."

> **The through-line:** capture is cheap and passive; learning is effortful and active.
> Every technique that works forces you to *produce* something — a recall, an
> explanation, a note, a connection.

---

## 2. Reading methodologies (how to structure the act of reading)

### 2.1 Adler & Van Doren — *How to Read a Book* — documented framework
Four cumulative **levels of reading**:
1. **Elementary** — decoding the words.
2. **Inspectional** — *systematic skimming* (title, preface, contents, index, key
   chapters) + a *superficial* first pass. Decide whether/how to read deeper. **Do this
   before committing** to a book.
3. **Analytical** — thorough reading of one book, organized around **four questions**:
   (1) What is the book about as a whole? (2) What is being said in detail, and how?
   (3) Is it true, in whole or part? (4) What of it — so what?
4. **Syntopical** — reading **many books on one subject** comparatively, to build an
   argument the books themselves don't state. *This is the level that produces original
   synthesis and is the engine of good writing.*
- The method treats reading as a **conversation with the author** and prescribes active
  marginalia. *Critiques are stylistic (rule-heavy, dated tone) rather than empirical;
  it's an influential framework, not a tested protocol.*

### 2.2 SQ3R — Survey, Question, Read, Recite, Review — ★★
- Created by psychologist Francis P. Robinson (*Effective Study*, 1946).
- **Why it works maps onto §1:** "Recite" and "Review" *are* retrieval practice and
  spacing. That's the empirically supported core.
- Evidence is **positive but uneven** (many small ESL/classroom studies; effects range
  from large, d ≈ 0.88, to non-significant). Treat the *Recite/Review* steps as the
  load-bearing ones.

### 2.3 Progressive summarization (Tiago Forte) — ★ (findability, not memory)
- Layered: L1 captured note → L2 **bold** the best → L3 ==highlight== the best of the
  bold → L4 short summary in your words → L5 remix.
- **Forte himself frames it as making notes *discoverable* later, not as a learning/
  memory technique.** There are no efficacy trials, and the bolding/highlighting steps
  are passive recognition. Useful for *organizing* a capture archive; don't mistake it
  for retention work.

### 2.4 Summary-writing & annotation — mixed
- **Writing summaries does aid memory** (items included in a summary are better
  remembered) — *if* you actually extract and rephrase main ideas. But Dunlosky rates
  summarization **low-utility overall** because most people write poor summaries that
  copy the original wording. The fix: summarize **from memory, in your own words** (which
  converts it into retrieval practice).
- Annotation/marginalia plausibly helps via elaborative encoding and retrieval cues, but
  the strong quantified blog claims ("a full letter grade," specific named studies) are
  largely **unverified secondary sources** — treat the magnitude skeptically.

---

## 3. Note-taking & PKM (how reading becomes connected, conveyable knowledge)

This is the layer that serves your goals of **connecting ideas across books** and
**publishing**.

### 3.1 Zettelkasten / Luhmann
- Niklas Luhmann's "slip-box" held **~90,000 index cards** (consistent across sources),
  linked by a branching alphanumeric ID scheme rather than folders.
- It's a **note-*linking*** methodology, not a note-*storage* one — value comes from the
  link network surfacing connections that become drafts.
- *Contested:* Luhmann's exact output (~50–70 books / ~400–550 articles **varies by
  source**), and critics note you **can't prove** the Zettelkasten *caused* his
  productivity or that it generalizes. Use it because the *mechanism* (atomic, linked,
  self-authored notes) aligns with the learning science — not because of the legend.

### 3.2 Ahrens — *How to Take Smart Notes*
- Popularized three note types (his framing, **not** Luhmann's original terms):
  - **Fleeting notes** — quick captures, discarded after processing.
  - **Literature notes** — *your own words* on what you read, tied to the source.
  - **Permanent notes** — self-contained **atomic** ideas in your own voice, kept forever.
- Core principle: *"Writing is not what happens after thinking. Writing is the medium of
  thinking."* Write **one idea per note**, in **full sentences, as if for a reader**.
  > Note that "your own words" + "as if for a reader" = the **generation/Feynman effect
  > (§1.4) baked into your note system.** This is why a good note system is also a
  > retention and a conveyance system.

### 3.3 Forte — *Building a Second Brain* (CODE + PARA)
- **CODE** workflow: **C**apture (save what resonates) → **O**rganize → **D**istill
  (extract the essence) → **E**xpress (turn it into output). The **Express** step is your
  publishing goal.
- **PARA** organization: **P**rojects (active, with a "done") / **A**reas (ongoing
  responsibilities) / **R**esources (future-interest topics) / **A**rchives (inactive).
  Key idea: **organize by *actionability*, not by topic.**
- Premise: *"Your brain is for having ideas, not storing them."*

### 3.4 Matuschak — evergreen notes
- Notes should be **(1) atomic, (2) concept-oriented, (3) densely linked.** Factor by
  **concept** (not by book/author/project), and prefer **links over folders/tags**.
- **"Write notes for yourself by default."** Framing: evergreen-note-writing is "the
  fundamental unit of knowledge work," and the goal is **better thinking, not better
  note-taking.**

### 3.5 The PKM failure modes to avoid — ★ (well-attested criticisms)
- **Collector's fallacy:** saving/highlighting something is *not* knowing it. An untouched
  archive grows your library, not your knowledge. (Directly echoes the §1.8 fluency
  illusion.)
- **Over-tooling / perfectionism:** the community over-invests in building the perfect
  system instead of producing output. The point is to **write and express**, not to
  garden tools. Pick a system and start.

> **Synthesis:** Zettelkasten/evergreen *principles* (atomic, your-own-words, linked,
> output-oriented) are the same forces the learning science endorses — generation,
> elaboration, retrieval. The specific app barely matters; the *behaviors* do.

---

## 4. Mapping techniques → your four goals

| Your goal | The highest-leverage practices |
|---|---|
| **Recall facts long-term** | Spaced **retrieval practice** (§1.1–1.2) → spaced-repetition flashcards (Anki/RemNote/FSRS). Generate cards *from your own notes*. |
| **Explain ideas clearly** | **Feynman / learning-by-teaching** (§1.4): write each permanent note in plain language "as if for a reader" (§3.2); periodically explain a concept aloud/in writing without looking. |
| **Connect across books** | **Syntopical reading** (§2.1) + **atomic, densely-linked notes** (§3.1, §3.4). Links are where cross-book synthesis lives. |
| **Publish writing** | **CODE → Express** (§3.3) + "writing is thinking" (§3.2). A note network of self-authored atomic claims is literally a draft-in-waiting. |

---

## 5. Current tools (2025–2026)

> Pricing is **approximate** and was changing through 2025–26 (NotebookLM, Mem, and
> Logseq all restructured) — verify on vendor pages before committing money.

### Integrated (capture + notes + flashcards/AI in one place)
- **RemNote** — *closest single-app fit for you.* Outliner notes that **auto-generate
  spaced-repetition flashcards** (`::` Q&A, cloze), supports **SM-2 and FSRS**, PDF
  annotation (Pro), and **AI flashcard generation** from text/PDFs. Free tier ~10 docs;
  **Pro ~$8–10/mo**. Combines capture + notes + SRS + AI — the rare all-in-one.
- **Logseq** — free, open-source, **local-first plain-markdown**, built-in flashcards
  (`#card`, FSRS in the newer DB version). AI only via external plugins. *Caveat:* the
  2025–26 "DB version" uses a proprietary SQLite schema **not interoperable** with the
  markdown graph and **no auto-migration** — watch before investing heavily.

### Capture / read-it-later
- **Readwise + Reader** — **auto-syncs Kindle, Apple Books, Instapaper, etc.**, daily
  resurfacing email, and **auto-exports to Obsidian/Notion/Roam/Logseq**. Reader handles
  articles/PDF/EPUB/RSS/newsletters with **"Ghostreader" AI** summaries/Q&A. **~$8–13/mo**
  (cheaper "Lite" excludes Reader); 50% student discount. *No native SRS* — it feeds one.

### Spaced repetition (dedicated)
- **Anki** — **free** + open source (iOS app is a one-time $24.99). **FSRS is the default
  scheduler** since v23.10 (≈20–30% fewer reviews than SM-2 at equal retention). The gold
  standard for durable recall; requires manual (or scripted/AI-generated) card creation,
  no capture/linking.
- **Mochi** — markdown SRS flashcards, bidirectional links, **Anki `.apkg` import**, AI
  card generation from URLs/PDFs/EPUBs. Free single-device; **Pro $5/mo** for sync + AI.

### Networked notes / PKM
- **Obsidian** — **free** (even commercial, since Feb 2025), local markdown, huge plugin
  ecosystem: **Spaced Repetition** plugin (FSRS) for cards-in-notes, **Smart Connections**
  (semantic "related notes" + vault chat, local embeddings, no API key needed) and
  **Copilot** (chat-with-notes, bring-your-own Claude/OpenAI/Gemini/local model). Sync
  ~$4/mo, Publish ~$8/mo optional. *Most flexible; you assemble the pieces.*
- **Roam Research** — networked notes, block references, daily notes; community SRS via
  SmartBlocks. **$15/mo** (Believer $500/5yr). No first-party AI to speak of.
- **Notion (+ Notion AI)** — flexible docs/DBs; **Notion AI add-on ~$8–10/member/mo** for
  writing/summarize/workspace Q&A. **No native SRS.**
- **Mem.ai** — "AI thought partner," auto-linking/tagging, NL search over your notes.
  Free = 25 notes/25 chats/mo; **Pro ~$12/mo.** No SRS.

### AI synthesis over your library
- **Google NotebookLM** — upload PDFs/Docs/links/YouTube/text; **grounded, cited Q&A**
  over *your* sources, plus **Audio Overviews** (podcast-style discussion of your
  material), Video Overviews, and Mind Maps. **Genuinely useful free tier** (100
  notebooks, 50 sources each, 50 queries/day). **No capture, no flashcards, no SRS** —
  it's a synthesis/understanding tool, excellent for *§2.1 syntopical* work and for
  pressure-testing your understanding by interrogating your sources.

### Quick picks
- **Want one app, minimal assembly:** **RemNote** (notes + auto-SRS + AI).
- **Want best-in-class pieces, mostly free, you own your data:** **Readwise/Reader →
  Obsidian (Spaced Repetition + Copilot plugins) → Anki**, with **NotebookLM** for AI
  synthesis. This is the power-user stack.
- **Free/minimalist:** Kindle highlights → Obsidian (markdown) + Spaced Repetition
  plugin + NotebookLM (free).

---

## 6. A custom system you could build (incl. on github.io)

Your goals + a developer's comfort with code make a **plain-markdown-in-git +
static-site + LLM** system very realistic. It directly counters the "over-tooling" trap
because you build only the loop that matters: **capture → atomic note → spaced retrieval
→ AI-assisted synthesis → publish.**

### 6.1 Architecture (recommended)
```
   Kindle / Reader / web
          │  (capture)
          ▼
   Readwise API  ──►  highlights.json
   or My Clippings.txt
          │  (you distill → atomic notes, in your own words)
          ▼
   /notes/*.md  ───────────────►  Git repo (source of truth, plain markdown,
   atomic + [[wikilinks]]            backlinks via [[ ]])
          │                                  │
          │ (LLM API: generate Q&A)          │ (static site generator)
          ▼                                  ▼
   /cards/*.json  ──► spaced-repetition   Published "digital garden"
   (FSRS state)        review web app      (github.io) with backlinks,
                       (ts-fsrs, browser)  graph view, search
```

### 6.2 The building blocks (all real, mostly MIT-licensed)

**Spaced-repetition algorithm**
- **FSRS** (Free Spaced Repetition Scheduler, by Jarrett Ye) — the modern standard, based
  on a Difficulty/Stability/Retrievability memory model; you set a **target retention**
  (e.g. 0.90). It's now Anki's default and needs ~20–30% fewer reviews than the classic
  **SM-2** (SuperMemo, 1987).
- Libraries: **`ts-fsrs`** (TypeScript, MIT, runs in the browser — ideal for a static
  site), **`py-fsrs`** (Python), **`fsrs-browser`** (Rust→WASM), **`go-fsrs`** (backend).
  See **`awesome-fsrs`** for the curated list. A simple **SM-2** reference impl exists too
  if you want minimal.

**Highlight capture**
- **Readwise v2 API** — `GET /api/v2/export/` with a token; supports `updatedAfter` for
  incremental sync.
- **Kindle `My Clippings.txt`** — every Kindle highlight lands in this plain-text file on
  the device (USB); parse it directly (e.g. `kindle2readwise`) — *zero subscription path.*
- **Hypothes.is** — open-source web annotation with a REST API (`hypothes.is/api/`) if you
  read in the browser.

**Notes + static site (the github.io part)**
- **Quartz** (TypeScript, MIT) — purpose-built **digital-garden SSG**: backlinks, graph
  view, wikilinks, transclusion, full-text search, Obsidian-compatible. *Best fit if you
  want the published-garden look.*
- **Jekyll digital-garden template** — `[[ ]]` links + backlinks on Jekyll (what
  github.io natively builds); note it needs custom plugins, so build via **GitHub
  Actions** rather than vanilla Pages. *(That specific template was archived Dec 2025 —
  Quartz is the more actively maintained choice.)*
- Either way: **notes are plain `.md` in the git repo** — durable, portable, diffable, and
  the same files feed both the website and the flashcard generator.

**LLM-assisted flashcards / synthesis**
- Use the **Anthropic Claude API** (or any OpenAI-compatible endpoint) to: turn a note
  into atomic Q&A cards, draft summaries, and surface cross-note connections. Existing
  references: **`notes-2-anki`** (Claude → atomic cards), **`anki-llm`** (bulk gen via any
  OpenAI-compatible endpoint incl. local Ollama), **`md2anki`** (markdown → `.apkg`).

**Existing "plain-text SRS" patterns to copy**
- **`hashcards`** (Rust, Apache-2.0) — flashcards as **plain text in a git repo**, FSRS
  scheduling, local web review UI. Proves the **git-as-database** model.
- **TiddlyWiki + `fsrs4tw`/`twsr`** — full spaced repetition inside a **single
  self-contained HTML file**, no server. Proves the **fully client-side** model.

### 6.3 The one real constraint, and three ways around it
A static site (GitHub Pages) **has no server**, so your **review state** (which cards are
due, their FSRS stability/difficulty) needs somewhere to live:
1. **`localStorage` in the browser** — simplest; `ts-fsrs` computes the schedule
   client-side. Downside: state is per-device.
2. **Git as the database** — review writes a JSON back to the repo (via a GitHub Action,
   or a tiny commit from a local script). Cross-device, versioned, free. (The `hashcards`
   model.)
3. **A small serverless function** (Cloudflare Workers / Netlify / Vercel) + a free KV
   store — if you want real cross-device sync without manual commits.

For a v1, **option 1 (localStorage)** gets you a working spaced-repetition review page on
your github.io with zero backend.

### 6.4 Suggested MVP, then iterate
- **v0 (this weekend, no code):** Kindle → Obsidian (markdown notes, in your own words,
  one idea per note, `[[linked]]`) + the Spaced Repetition plugin. Prove the *habit*
  before building tooling.
- **v1:** Publish those same markdown notes as a **Quartz digital garden** on github.io
  (backlinks + graph + search) — your public "second brain."
- **v2:** Add a **browser review page** using `ts-fsrs` + `localStorage` that reads
  `cards/*.json`.
- **v3:** Add an **LLM script** (Claude API) that reads new notes and proposes Q&A cards
  for you to approve — auto-quizzing and connection-surfacing.

> **Build-vs-buy honest take:** if the *goal* is retention, buy/assemble (RemNote, or the
> Readwise→Obsidian→Anki stack) and start the habit **today** — that captures ~90% of the
> value. Build the custom github.io system if the *building itself* is motivating and you
> want a public digital garden as an output (which itself serves your "publish" goal via
> the generation effect).

---

## 7. A concrete weekly workflow (ties it all together)

1. **Before a book:** inspectional read (§2.1) — skim structure, decide if/why to read it,
   write the 1–2 questions you want it to answer.
2. **While reading:** highlight *sparingly* (capture only), and in the margin write **why**
   a passage matters / how it connects (elaborative interrogation, §1.3).
3. **After each chapter (the key step):** close the book and **free-recall** it in writing
   — what did it argue, what's the takeaway? Then check against your highlights (§1.1).
4. **Within a day or two:** convert recall + highlights into **2–5 atomic permanent
   notes**, in your own words, "as if for a reader," each **linked** to related notes
   (§3.2, §3.4). Optionally have an LLM draft flashcards from them for you to approve.
5. **Ongoing:** do your **spaced-repetition reviews** (FSRS) — a few minutes daily (§1.2).
6. **Monthly / when an idea clusters:** write something **public** — a short essay/post on
   your github.io — from the note network (CODE→Express, §3.3). Teaching it *is* the
   deepest retention step (§1.4) **and** your stated goal.

---

## Sources

**Learning science**
- Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), *Improving Students' Learning With
  Effective Learning Techniques*, Psychological Science in the Public Interest —
  https://journals.sagepub.com/doi/abs/10.1177/1529100612453266
- Roediger & Karpicke (2006), *Test-Enhanced Learning / The Power of Testing Memory* —
  https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x
- Rowland (2014), *The Effect of Testing Versus Restudy on Retention* (meta-analysis),
  Psychological Bulletin — https://www.semanticscholar.org/paper/5d4dd1c73554ff1c5c493c2795aadd5aa8bfda17
- Karpicke & Blunt (2011), *Retrieval Practice Produces More Learning than Elaborative
  Studying with Concept Mapping*, Science — https://www.science.org/doi/10.1126/science.1199327
- Cepeda et al. (2008), *Spacing Effects in Learning: A Temporal Ridgeline of Optimal
  Retention*, Psychological Science — https://eric.ed.gov/?id=ED505660
- Cepeda et al. (2006) meta-analysis (discussion) —
  https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full
- Taylor & Rohrer (2010), *The Effects of Interleaved Practice* —
  https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1598 ; Rohrer et al. (2015) —
  https://files.eric.ed.gov/fulltext/ED557355.pdf
- Firth et al. (2021), interleaving review, Review of Education —
  https://bera-journals.onlinelibrary.wiley.com/doi/10.1002/rev3.3266
- Fiorella & Mayer (2013), *The Relative Benefits of Learning by Teaching and Teaching
  Expectancy* — https://www.sciencedirect.com/science/article/abs/pii/S0361476X13000209
- Bjork & Bjork (2011), *Making Things Hard on Yourself, But in a Good Way* (UCLA) —
  https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf
- Pashler, McDaniel, Rohrer & Bjork (2008), *Learning Styles: Concepts and Evidence* —
  https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01038.x
- Elaborative interrogation overview — https://www.cognitivepsychology.com/Elaborative_Interrogation
- Self-explanation — https://learning.northeastern.edu/the-power-of-self-explanation/
- Fluency illusion — https://www.psychologyinaction.org/2018-10-22-the-dangers-of-fluency/

**Reading methodologies**
- Adler & Van Doren, *How to Read a Book* — https://en.wikipedia.org/wiki/How_to_Read_a_Book ;
  Farnam Street summary — https://fs.blog/how-to-read-a-book/ ; levels — https://fs.blog/levels-of-reading/
- SQ3R — https://en.wikipedia.org/wiki/SQ3R ; efficacy studies —
  https://www.researchgate.net/publication/380172463 ;
  https://www.researchgate.net/publication/355493889
- Progressive Summarization (Forte) —
  https://fortelabs.com/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/ ;
  critique — https://jamesstuber.com/progressive-summarization-a-waste/
- Summary writing & memory (Educational Psychology Review, 2016) —
  https://link.springer.com/article/10.1007/s10648-014-9290-2

**PKM systems**
- Zettelkasten — https://en.wikipedia.org/wiki/Zettelkasten ;
  https://zettelkasten.de/posts/concepts-sohnke-ahrens-explained/ ;
  Luhmann's original method — https://www.ernestchiang.com/en/posts/2025/niklas-luhmann-original-zettelkasten-method/
- Ahrens, *How to Take Smart Notes* — https://fortelabs.com/blog/how-to-take-smart-notes/ ;
  https://aliabdaal.com/book-notes/how-to-take-smart-notes/
- Matuschak evergreen notes — https://notes.andymatuschak.org/Evergreen_notes ;
  concept-oriented — https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented
- Building a Second Brain (CODE/PARA) — https://fortelabs.com/blog/basboverview/ ;
  https://www.buildingasecondbrain.com/
- Collector's fallacy — https://zettelkasten.de/posts/collectors-fallacy/ ;
  over-tooling critique — https://writing.bobdoto.computer/tensions-between-zettelkasten-and-the-productivity-scene/

**Tools (2025–2026)**
- Readwise — https://readwise.io/pricing ; docs — https://docs.readwise.io/ ;
  pricing review — https://www.readless.app/blog/readwise-reader-pricing-2026
- Anki — https://github.com/open-spaced-repetition/fsrs4anki ;
  cost — https://blog.educate-ai.com/en/anki-pricing-cost-ios-android-desktop
- RemNote — https://www.remnote.com/pricing ;
  AI cards — https://help.remnote.com/en/articles/10102901-generating-flashcards-with-ai
- Obsidian — https://obsidian.md/pricing ; Smart Connections —
  https://github.com/brianpetro/obsidian-smart-connections ; Copilot —
  https://github.com/logancyang/obsidian-copilot
- Logseq — https://neuracache.com/logseq-flashcards-spaced-repetition
- Roam — https://www.saasworthy.com/product/roam-research/pricing
- Notion AI — https://workflowautomation.net/reviews/notion-ai
- Mem — https://support.mem.ai/article/43-what-is-the-pricing-for-mem
- Mochi — https://mochi.cards/ ; https://mochi.cards/faq.html
- NotebookLM — https://support.google.com/notebooklm/answer/16213268 ;
  https://elephas.app/blog/notebooklm-free-vs-plus

**Buildable system**
- FSRS — https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm ;
  Anki scheduler — https://faqs.ankiweb.net/what-spaced-repetition-algorithm
- Libraries: ts-fsrs — https://github.com/open-spaced-repetition/ts-fsrs ;
  py-fsrs — https://github.com/open-spaced-repetition/py-fsrs ;
  awesome-fsrs — https://github.com/open-spaced-repetition/awesome-fsrs
- Capture: Readwise API — https://readwise.io/api_deets ;
  Kindle — https://github.com/biokraft/kindle2readwise ;
  Hypothesis API — https://h.readthedocs.io/en/latest/api/
- Static sites: Quartz — https://github.com/jackyzha0/quartz ;
  Jekyll digital garden — https://github.com/maximevaillancourt/digital-garden-jekyll-template
- LLM flashcards: anki-llm — https://github.com/raine/anki-llm ;
  notes-2-anki — https://github.com/drewnode/notes-2-anki ;
  md2anki — https://github.com/lucagrippa/md2anki
- Plain-text SRS: hashcards — https://borretti.me/article/hashcards-plain-text-spaced-repetition ;
  fsrs4tw — https://github.com/open-spaced-repetition/fsrs4tw

> **Sourcing caveat:** several primary domains (publishers, vendor pricing pages) returned
> HTTP 403 to automated fetching during research, so a few exact figures — Roediger &
> Karpicke's specific recall percentages, Luhmann's exact publication count, and the most
> volatile 2025–26 tool prices — rest on corroborated secondary sources and should be
> verified against the primary page before being quoted precisely. Directional findings
> and effect sizes are consistent across multiple independent sources.
