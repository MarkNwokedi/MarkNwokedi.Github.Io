#!/usr/bin/env python3
"""Generate an Anki-importable deck (tab-separated) for *No-Drama Discipline*
(Siegel & Bryson). Cards mix terminology (term -> meaning) and "explain why/how"
prompts that force articulation, not just recognition.

Import into Anki: File -> Import -> select this .txt; it is tab-separated with
Front / Back / Tags columns and auto-creates the "No-Drama Discipline" deck.
"""

import csv

CARDS = [
    # ---- core framing ----
    ("In *No-Drama Discipline*, what does the word \"discipline\" actually mean, and where does it come from?",
     "It means \"to teach.\" It shares a root with \"disciple\" — a student/pupil (Latin *disciplina* = instruction). Discipline is about teaching, not punishing.",
     "concept"),
    ("What are the two goals of discipline (short-term and long-term)?",
     "Short-term: gain cooperation — stop the behavior / get the right thing done now. Long-term: build skills and the brain — self-control, empathy, relationships, and good decision-making for life.",
     "concept"),
    ("What is the central No-Drama Discipline strategy, in three words?",
     "Connect and Redirect. First connect emotionally to calm the child, then redirect (teach / problem-solve). Connection before correction.",
     "concept"),
    ("Why must you connect *before* you redirect or correct?",
     "An upset, dysregulated child literally can't learn. Connecting soothes the nervous system and moves the child from a reactive to a receptive state — only then can teaching land. It also strengthens the relationship.",
     "concept"),
    # ---- brain model ----
    ("Describe the \"downstairs brain.\"",
     "The lower, primitive parts (brainstem + limbic/amygdala). Runs basic functions, big emotions, and instincts like fight-flight-freeze. Developed early — it takes over when a child is overwhelmed.",
     "terminology"),
    ("Describe the \"upstairs brain.\"",
     "The cerebral cortex, especially the prefrontal cortex. Handles planning, decision-making, self-control, empathy, and morality. Still under construction into the mid-20s, so it's unreliable in kids.",
     "terminology"),
    ("During a meltdown, why can't you reason with a child?",
     "The downstairs brain has taken over and the upstairs brain is \"offline,\" so logic and self-control aren't available. You have to calm (connect) first; reasoning/teaching only works once the upstairs brain is back online.",
     "concept"),
    ("Reactive vs. receptive state — what's the difference, and why does it matter?",
     "Reactive = downstairs brain in charge (fight/flight), can't learn. Receptive = calm and open to connection and learning. Discipline only teaches when the child is receptive, which connection helps create.",
     "terminology"),
    # ---- tantrums ----
    ("\"Upstairs tantrum\" vs. \"downstairs tantrum\" — what's the difference and how do you respond to each?",
     "Upstairs: child is in control and choosing the behavior (often to get something) — respond with calm, firm boundaries; don't give in. Downstairs: child is genuinely overwhelmed, upstairs brain offline — respond with comfort and connection; you can't reason them out of it.",
     "terminology"),
    # ---- the three questions ----
    ("What are the three questions to ask yourself before responding to misbehavior?",
     "1) WHY did my child act this way? 2) WHAT lesson do I want to teach right now? 3) HOW can I best teach it? Pausing for these turns a reaction into intentional teaching.",
     "concept"),
    ("What does \"behavior is communication\" / \"chase the why\" mean?",
     "Misbehavior is a signal of an underlying need, feeling, or missing skill. Instead of reacting to the surface behavior, look for ('chase') what's driving it.",
     "concept"),
    ("In discipline, what's the \"can't vs. won't\" distinction?",
     "Often a child isn't refusing (won't) but genuinely lacks the developmental skill (can't) to handle the moment. Discipline should build the missing skill, not just punish the behavior.",
     "concept"),
    # ---- key terms / metaphors ----
    ("What is \"shark music\"?",
     "A metaphor for the background anxiety/dread we carry from our own past that colors how we react to our child. \"Turning down the shark music\" = noticing that baggage so it doesn't drive an overblown reaction.",
     "terminology"),
    ("What is \"mindsight\"?",
     "Dan Siegel's term for the ability to see and understand your own mind and others' minds — combining insight (into yourself) and empathy (into others). A key capacity discipline aims to build.",
     "terminology"),
    ("What does \"name it to tame it\" mean?",
     "Helping a child put big feelings into words (labeling the emotion) calms the reactive amygdala and engages the upstairs brain, leaving them calmer and more receptive.",
     "terminology"),
    ("What does it mean for a child to \"feel felt,\" and why does it matter?",
     "It's the sense that you truly understand and are attuned to their inner experience. Feeling felt makes a child feel safe and connected, which calms them toward receptivity.",
     "terminology"),
    ("How does discipline \"build the brain\"?",
     "Repeated experiences wire the brain. Each time you discipline by connecting and teaching (vs. just punishing), you exercise and strengthen upstairs-brain circuits for self-control, empathy, and decision-making.",
     "concept"),
    # ---- 1-2-3 of redirection ----
    ("In the 1-2-3 of redirection, what is the \"1\" — the one definition?",
     "One definition of discipline: discipline means to TEACH.",
     "concept"),
    ("In the 1-2-3 of redirection, what are the \"2\" principles? (verify against the book)",
     "1) Wait until your child is ready (receptive) before teaching. 2) Be consistent but not rigid — keep dependable boundaries while staying responsive to the child and situation.",
     "concept"),
    ("In the 1-2-3 of redirection, what are the \"3\" desired outcomes? (verify against the book)",
     "Insight (the child understands themselves), Empathy (understands how their actions affect others), and Repair (makes things right / makes amends).",
     "concept"),
    # ---- REDIRECT strategies ----
    ("What does the R-E-D-I-R-E-C-T acronym (redirect strategies) stand for?",
     "Reduce words; Embrace emotions; Describe (don't preach); Involve your child in the discipline; Reframe a no into a conditional yes; Emphasize the positive; Creatively approach the situation; Teach mindsight tools.",
     "terminology"),
    ("REDIRECT strategy — what does \"Reduce words\" mean?",
     "Don't lecture or pile on words, especially with an emotional child. Fewer words land better; over-talking escalates and gets tuned out.",
     "concept"),
    ("REDIRECT strategy — what does \"Embrace emotions\" mean?",
     "Accept and validate the child's feelings even while you limit the behavior. You can say no to an action while honoring the emotion behind it.",
     "concept"),
    ("REDIRECT strategy — what does \"Describe, don't preach\" mean?",
     "Instead of moralizing, simply describe what you see (\"I see wet towels on the floor\"). Describing invites the child to notice and problem-solve without triggering defensiveness.",
     "concept"),
    ("REDIRECT strategy — what does \"Reframe a no into a yes\" mean?",
     "Turn a flat refusal into a conditional yes (\"Yes — after dinner\"). It keeps the boundary while lowering reactivity and giving the child something to anticipate.",
     "concept"),
    # ---- connecting in the moment ----
    ("How do you connect with an upset child in the moment? (the connection moves)",
     "Communicate comfort (get below eye level, soothing touch/tone), validate the feelings, stop talking and listen, then reflect back what you heard — so the child feels felt and calms toward receptivity.",
     "concept"),
    # ---- big picture ----
    ("Why can fear-based punishment and harsh time-outs backfire?",
     "They can spike reactivity, damage the parent-child connection, model the wrong behavior, and teach compliance through fear rather than building real internal skills (self-control, empathy).",
     "concept"),
    ("What's the ultimate aim of discipline — external compliance or internal discipline?",
     "Internal discipline (self-discipline). The goal is lasting inner skills and judgment, not just short-term obedience driven by fear of punishment.",
     "concept"),
    ("What is the \"no-drama\" part — how should the parent show up?",
     "Respond rather than react: stay calm, lower the emotional intensity instead of escalating, and avoid power struggles. Your regulated state helps regulate the child.",
     "concept"),
]


def main(path="no-drama-discipline.txt"):
    header = [
        "#separator:tab",
        "#html:false",
        "#notetype:Basic",
        "#deck:No-Drama Discipline",
        "#columns:Front\tBack\tTags",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(header) + "\n")
        for front, back, kind in CARDS:
            assert "\t" not in front and "\t" not in back, "fields must not contain tabs"
            assert "\n" not in front and "\n" not in back, "fields must be single-line"
            f.write(f"{front}\t{back}\tNoDramaDiscipline {kind}\n")
    print(f"wrote {path} ({len(CARDS)} cards)")


if __name__ == "__main__":
    main()
