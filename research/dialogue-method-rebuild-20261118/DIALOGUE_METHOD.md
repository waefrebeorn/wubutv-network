# DIALOGUE METHOD — THE REBUILD (2026-11-18)

**Authority:** user ruling, 2026-11-18 ~19:28 EST — "the way that all
of the dialog is being made is wrong and none of the dialog makes
any sense and the whole point of transitioning the shows is to show
you that things needed to improve and how to change the dialog."
Diagnosis: `DIAGNOSIS.md` (this directory). Standard:
`THE_STANDARD.md` (this directory). This document is the method.
Where it conflicts with E2 law / the E2 Speech and Story Addendum /
TASTE §7–§8 dialogue items, the conflicts are named in the TASTE
addendum filed with it
(`new-era/research/TASTE_GUIDE_DIALOGUE_ADDENDUM_2026-11-18.md`) —
this method governs dialogue construction from adoption forward.

**The one-sentence version:** dialogue is written as people trying
to get something from each other, in lines that lean on the line
before them — and no gate may ever again be passed by a line whose
only job is to be found by the gate.

---

## 1. The pass order (replaces Pass 3 dialogue construction)

**Pass 3.0 — VOICE RULES BEFORE LINES.** Before any dialogue is
drafted, each speaking character gets a one-line SPEECH RULE on
their cast card, written from the Personality layer: how they ask,
how they lie, how they refuse, what they never do with words.
Form: the Poptoy specimens ("speaks in questions when hurt";
"over-explains when lying — volunteers dates nobody asked for").
A character without a speech rule does not speak in the episode.
*(Template: `SPEECH_RULE` field on the §1 cast card.)*

**Pass 3.1 — BANTER FIRST (F-27's mine-the-banter, made a step, not
a slogan).** The scene's exchange is drafted loose, as talk:
fragments, interruptions, wrong answers, overlaps, and reactions
are not merely allowed, they are the draft's job. The banter draft
is kept in the episode's work dir. Lines are then *harvested* into
the locked script; a locked line that exists in no banter draft
and was written directly to the board is presumed a ledger line
until defended. *(Template: `BANTER_DRAFT` field, §2 sign-off.)*

**Pass 3.2 — THE MOVE LEDGER.** Every harvested line is labelled
with (a) its MOVE — accuse / deny / dodge / plead / offer / refuse /
demand / expose / decide / react — and (b) its TARGET — the person
in the scene it is aimed at. A line whose target is "the room",
"the record", or the audience is cut, unless it is the episode's
one licensed grievance/confession beat (F-21-adjacent; logged).
Two consecutive lines by the same speaker carrying the same move
and no new fact are a repeated beat: cut or escalate (McKee).
*(Template: `line_move` + `line_target` per SPEECH BLOCK entry.)*

**Pass 3.3 — WANT CARRIAGE (replaces want announcement).** A want
enters dialogue only as a move: an offer, a demand, a refusal, a
complaint, a bargain — something the other character can answer,
refuse, or use. The grammatical form "I want X" / "that's all I
want" is **banned** from dialogue, with one named exception: a plea
where the nakedness is itself the move (a character begging,
stripped of tactics) — logged as an exception in the brief, at most
one per episode. Legibility of wants is achieved the genre's way:
one want per lead that does not change; the obstacle changing
shape in front of it; and the verdict restatement (§1.4) entering
it into the record *after* it has bitten. The gate question is no
longer "is the want stated by U2?" but "can a stranger recover the
want from the character's first two moves?" — tested by the
Stranger Test (§3), Q1.

**Pass 3.4 — FACT SPEND.** Each core fact of the episode is spent
exactly twice in dialogue: once as a move inside the action
(accusation, offer, entrance), and once as a **verdict
restatement** — a different voice, different words, after the fact
has landed ("Valentina is your sister" shape). Wording is never
repeated verbatim between the two spends, with one licensed
exception: a single key word may repeat, escalated ("His
FAVOURITE."). Recap at an episode head is a complaint or an
accusation, never narration. Bookend restatement of a U1 line at
U6 is not a spend — it is banned (§2).

**Pass 3.5 — THE PLAINNESS PASS (replaces the stumble repair).**
The locked dialogue is read aloud cold, in order, by a voice that
did not write it. The reader marks **meaning failures only**: a
line where the listener cannot say what was meant or who it was
meant for. Parse texture is not a failure: contractions are the
default surface and may never be "repaired" into expanded forms;
fragments are licensed wherever they complete, answer, or react;
a line's grammar may lean on the previous line (that dependence is
the twine, and it is the point). A meaning failure returns the
*exchange* to Pass 3.1 (banter), not the line to polish.
Hear-before-it-moves (F-26) survives with this definition of
"stumble" substituted; its old repair gradient is revoked.

## 2. Banned constructions (failure classes — gate logs cite these names)

| Class | Definition | E3 specimen it names |
|---|---|---|
| LEDGER LINE | A line whose addressee is the record/gate, not a person in the scene | "Ansel says the Courier held his tin. His coins are gone." |
| WANT ANNOUNCEMENT | A want declared in "I want X" form instead of used as a move (plea exception excepted) | "I want the book closed even by noon." |
| LAW RECITATION | A world-rule lectured before the event that teaches it; includes describing, in dialogue, a picture the viewer is already seeing | "At the bell, what's held stays held. What's loose changes. The Courier's hands are open." |
| BOOKEND RESTATEMENT | A closing line that restates an opening line with the outcome swapped in, existing to close a pair | "I wrote one true line today…" (for U1's "I write one true line today, or none.") |
| APHORISM PAIR | Two self-contained proverbs in sequence, answering no question | "We count what's brought." / "Receipts say what was paid, not what came." |
| ORPHAN LINE | A line that rules on nothing before it — answers, accepts, refuses, or contradicts no prior line | any line that survives the shuffle test |
| SYMMETRIC FILING | An exchange of matching-form statements (want for want, claim for claim) with no contact between them | ONE SHORT U1's demand/want-statement pair |
| FORMAL REPAIR | A gate repair that expands a contraction, names a subject the scene already supplies, or otherwise trades spokenness for parseability | "Thirty's the count" → "Thirty is the count" |

The **shuffle test** remains the standing diagnostic (addendum §3):
if a unit's lines can be reordered without loss, the unit contains
orphans and fails — but it is now a *diagnostic inside the Stranger
Test record*, not a construction target; lines are not written
*to* the shuffle test any more than to any other gate. They are
written to the banter, and the tests merely listen.

## 3. THE NEW GATE — THE STRANGER TEST

A dialogue-specific cold test. It exists because every current gate
asks comprehension questions (Gate E), parse questions
(hear-before-it-moves), or delivery questions (ear test, Gate (f)) —
and none asks the only question the user asks: *would a person say
that line, to that person, there?*

**Placement.** Twice: (a) at script stage, after Pass 3.5, **before
script lock** — a script may not lock without a PASS record;
(b) at master stage, on the finished master's own transcript,
beside Gate (f) — Gate (f) keeps comprehension; the Stranger Test
owns plausibility. A master-stage FAIL returns the episode to the
room as a story-gate failure (repaired, never disclosure-shipped).

**Inputs.** The dialogue ONLY — colon form, in order, with speaker
names. **No** picture summaries, premise, annotations, bible, or
gate paperwork. Annotations are stripped before the test: the E3
scripts' annotations would have told the reader what each line was
*for*, and that priming is part of the old blindness. The reader
did not write the dialogue and has not read the episode's brief.

**Procedure.** The reader reads the dialogue aloud once, in order,
flat. Then answers, in writing:

- **Q1 (per designed speaker):** "What does this person want?
  Answer from what they *do* with words. If the only evidence is a
  line where they announce it, write ANNOUNCED." (Quote the line
  relied on.)
- **Q2 (per exchange):** "What did the second line do to the
  first?" — one of: ANSWERED / REFUSED / DODGED / TOPPED /
  MISHEARD / **FILED ITS OWN STATEMENT**.
- **Q3 (per line — the would-a-person test):** mark any line
  **STAGE** if no person in that situation would say that sentence
  to that person. Each STAGE mark carries a reason of ≤6 words
  ("she's telling him his own news"; "nobody recites the rulebook").
- **Q4 (the gossip retell):** "Retell this scene the way you'd tell
  a friend, in two sentences." The retell is checked against the
  locked story: any fact the retell *needs* that is not in the
  dialogue must be listed (undramatized exposition); any fact the
  retell gets *wrong* is a legibility failure in the dialogue, not
  in the reader.

**FAIL conditions (any one fails the gate):**
1. ≥2 STAGE lines in the episode.
2. Any exchange scored FILED ITS OWN STATEMENT on both lines.
3. Q1 answered ANNOUNCED for any designed speaker (outside a
   logged plea exception).
4. The Q4 retell contradicts the locked story on any fact, or
   needs ≥2 facts that exist nowhere in the dialogue.

**On FAIL:** the record names the failure class(es) from §2, and
the repair is at Pass 3.1 (re-banter the exchange) — never
line-polish toward the test. The reader's Q3 reasons are quoted in
the GATE_LOG verbatim.

**Template fields (added by the v3 template patch):**
`STRANGER_TEST` sign-off block in §2 (reader, date, Q1–Q4 summary,
`stage_lines` count + line IDs, `stranger_verdict: PASS / FAIL`);
per-line `line_move` / `line_target` in §4.4; `SPEECH_RULE` in §1;
`BANTER_DRAFT` in §2; master-stage `STRANGER TEST (MASTER)` block
in §5.4 beside Gate (f). All are in the §6 grep contract — a brief
without them is not fireable, per the standing law that a rule
without a field does not exist.

## 4. What does NOT change

F-25 spoken-load caps and the Container Law (they are arithmetic,
not style); F-13 ear test and F-9 (delivery and story gates — they
keep their jobs; they were never the dialogue gate); Gate E's
transcript+pictures discipline for *story* sense; F-14 two-speaker
design (Camp B generation stands — but exchanges are now *written*
as exchanges in the banter draft, with interruption and overlap
marked as delivery notes for the edit, instead of being written as
alternating monologues); the colon form and prompt hygiene (F-16).

*End of method.*
