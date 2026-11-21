# TASTE GUIDE — the standing taste standard for WuBuTV

**Issued:** 2026-11-17 · **Ordered by:** the user ("ONLINE RESEARCH
AND FIND TASTE — NO JOKE LEARN TASTE IS DOABLE"), after HOLD ON E2
was rejected as MISHMASH: dialogue that passed all twelve paper
F-9 items and was still nonsense in the ear; voices that did not
match their characters; characters speaking prompt details aloud;
decorative invaders who said and did nothing; jumping, incoherent
cuts.

**Sources:** the three-angle research wave of 2026-11-17 —
`research_notes/taste-20261117/angle1-dialogue-voice.md` (voice
craft + QC tooling), `angle2-taste.md` (taste in AI video),
`angle3-spoken-naturalism.md` (spoken naturalism). Rule citations
below are [A1]/[A2]/[A3] + section. Only EVIDENCED findings became
rules; LEAD-grade claims are marked and carry no gate weight.

**Amended:** 2026-11-17 (user msg 583 — base lore) — T-30
(simpler-stories bias), §6 (lore & self-awareness: the
gentrification), F-20/F-21 (occupation rule; self-awareness
device).

**Ratified addendum:** 2026-11-18 — §8: F-13…F-21 ruled on;
F-22…F-28 added (end-state pin, acting direction, reference
priority, spoken-load cap, fruit-soap method +
hear-before-it-moves, Cantina methods, our layer). Governs
E3 forward; E2 law unchanged.

**Doctrine (governs every conflict in this document):** plain
surface story; engagement first; **the user's ear outranks every
gate.** A rule that produces a pass the ear rejects is a broken
rule, and this guide is how we fix the rules.

---

## §1 — THE TASTE RULES

### Story and selection

**T-1. One idea, sayable in one sentence.** Every episode passes
the one-sentence test (what it makes a viewer feel or realise)
and the swap test (replace names/details with placeholders — if
it could be anyone's video, it's generic). Two competing ideas =
two episodes. [A2 §1.1 — Higgsfield jury criteria; Popcorn]

**T-2. Decisions before generation.** Script and shot list exist
before any generation call. Output nobody decided on is never
shipped, however fluent. "If the generating came first and the
thinking came after, it's slop." [A2 §1.2 — Talentless AI;
Easyviral]

**T-3. Selection is the craft.** Generate at least 3× the footage
kept; log attempts per accepted shot. Select takes for motion
and continuity first, image beauty second — a gorgeous frame
that moves wrong stands out more than a plain shot that moves
convincingly. [A2 §1.3, §4.3 — Phosphene (winner logged 1,158
generations for ~50 shots); Skillveris; UPSC]

**T-4. One world the model can hold.** Pick a stylized look the
surface can sustain for the whole runtime, preferably one whose
style absorbs small errors instead of inviting comparison with a
camera. One look per piece, enforced. [A2 §1.4 — Phosphene]

**T-5. Specificity from our own world.** Props, behaviour and
details come from the show's own world, not the model's average.
The first idea is everyone's first idea (lone figure in rain,
neon cyberpunk, fork in the road = banned defaults). [A2 §1.5 —
Popcorn; *Ancestra* coverage]

**T-30. Simpler wins ties.** When two plot options both work,
take the simpler one: one want, one obstacle, one turn. The
lore (§6) carries the depth; the plot carries the clarity. A
story a cold listener can retell in one sentence is not a
smaller story — it is the only kind that survives the ear.
[user msg 583, 2026-11-17]

### Voice

**T-6. The voice is cast, not found.** Each character's voice is
a structured spec written on the character sheet **before
episode 1** — age range, accent/region, pitch, pace, texture,
trait, where the voice breaks — and pasted **verbatim** into the
CHAR panel and every prompt for that character. One pinned voice
+ one approved reference sample per character; same engine all
season; the block is never reworded mid-series. [A1 §1.1–1.3,
§1.5 — Google guidance via ToonlyAI; ArcLoop; Oakgen;
ElevenLabs v3 practice]

**T-7. The voice must match the face.** Cast against the face's
apparent age, size and register. Listeners extract sex and age
from a single vowel and match voices to faces above chance;
impressions form in under a second — a voice cast against the
face's apparent age/register fails before a word registers, and
no correct dialogue repairs it. [A1 §1.6 — Sorokowski 2023;
Smith et al. 2016; Lavan & Anikin 2026]

**T-8. One speaker per clip, one line per clip.** Exchanges are
assembled in the edit from single-speaker clips with identical
character descriptions. Multi-speaker clips are where
wrong-speaker, blurred-voice and leaked-line failures
concentrate — and where automated speaker QC is weakest.
[A1 §4 — DreamDrive; OpenMicroDrama; Oakgen; A1 §3.2]

**T-9. Line budget: ≤2.5 words per second of clip.** Roughly
6–12 words per 8-second clip. Overlong lines come back sped-up
and garbled, which reads as nonsense. Every line must also pass
the breath test (§4). [A1 §2.5 — VEED; DreamDrive; A3 Q1]

### Prompt hygiene (the leak law)

**T-10. The prompt is content, not instructions.** There is no
dialogue field: the model treats everything in the prompt as
content to render, and speaks anything that looks speakable.
Therefore: the prompt contains ONLY renderable material — scene
sentence(s), then an isolated speech block at the end, one line
per sentence, attributed by name + visible trait + delivery.
No staging notes, no meta-instructions, no signage text, no
quoted fragments, no second line "for context." All production
instructions live in production documents, never in the prompt.
Any prompt-enhance/rewrite stage is OFF for dialogue clips.
[A1 §2.1, §2.2, §2.4, §2.7 — VEED help center; Prompt
Architects; AudioDrama; Paintbrush]

**T-11. One speech convention, network-wide.** Current Google
guidance: speaker name + "says" + colon + the line, **no
quotation marks** (quoted text is liable to be drawn on screen
as garbled subtitles). Sources conflict on quotes; the network
rules the colon form, everywhere, identically. If text appears
on screen, dropping quotes is the first fix. [A1 §2.3 — Google
Cloud best practice via CapsAI; ToonlyAI]

**T-12. Describe presence, not absence.** Silence and non-speech
are described positively — closed lips, a named ambient
soundscape. Negation backfires: "no talking" introduces the
concept of speech to a model whose prior is that people talk,
and who pads silence with filler voices. [A1 §2.6 — apipass,
compiling r/VEO3 creator reports]

**T-13. Direct the state, in the attribution, before the line.**
Delivery direction lives in the clause before the line ("she
says, worn thin, holding the letter: …") because the model reads
direction before words. Direct the state — where she is, who
she's talking to, what she's hiding — not a bare adjective.
[A1 §1.7 — ArcLoop; Prompt Architects]

### Dialogue (full craft in §4)

**T-14. Every line is a move.** For each line, answer: what does
the speaker want the listener to *do or feel*? If the only
answer is "let the audience know," the line is cut or rewritten
as a move — a demand, accusation, refusal, offer, ultimatum —
that also carries its fact. [A3 Q1 — SPM intention test;
MasterClass; 4BH]

**T-15. Plain wants, spoken as demands.** Wants and stakes are
stated out loud — aimed at a person who can refuse them. That
is what makes plainness work in soaps: the statement is a move
against resistance, not narration. Feelings-as-narration ("I'm
sad about the will") is banned; the same content as a claim on
the obstacle ("You signed it because you wanted me out") is
the form. [A3 Q1, Q4 — soap design sources; Nordicom;
Screen Thoughts]

**T-16. Repeat content, never form.** Key facts and wants recur
at least three times across an episode, each time as a
different social move — gossip to a third party, accusation,
denial — so a missed line never strands the viewer. Verbal
echo-chains and parrot repeats are banned as structure: the
information must never live only in the relation between
lines. [A3 Q2, Q4 — soap redundancy design; Chafe; Flametree]

**T-17. Voices tellable blind.** Cover the names: each speaker
must be identifiable from the words alone — different rhythm,
vocabulary, sentence length, favourite words. One device for
every character = one voice for every character = the writer
arguing with themselves in different hats. [A3 Q2, Q3 —
Celtx; Lowerated; cover-the-names test, four sources]

**T-18. Name who's in the room.** Ear-first media establishes
presence by voice: a character who is present but silent reads
as absent. Speakers are named or referred to by name in
dialogue often enough that a listener always knows who is in
the scene. (This inverts prose advice; our medium is the
listener's.) [A3 Q4; A1 §4 — BBC Writersroom via CloudRad]

### Sound, camera, script surface

**T-19. Sound is one authored layer.** One score/ambience bed
written for the whole piece runs under the cuts — a continuous
bed makes separate generations feel like one space and one
moment. All dialogue is levelled to one loudness target across
takes (per-take swings of ~3 LU are audible as dips at cuts).
[A2 §1.6, §4.3 — Popcorn; Skillveris]

**T-20. Motivated camera, stageable action.** The camera moves
only when something motivates it; spectacle swoops are the
model's default, not a decision. Stage common, whole-body
actions; delicate named gestures (specific finger work) do not
survive generation — rewrite the action, not the prompt.
[A2 §1.7, §2.5 — Popcorn]

**T-21. The slop tells are banned on sight.** In any script:
the "not X, but Y" line; the fake-wisdom ending; buzzwords as
proof; the reassurance ("and that's okay"); the sweeping
opener ("in a world where…"). Open on the most specific thing
in the piece. End on a concrete image or a line only this
episode could say — for serial episodes, a plain, concrete,
unanswered move (a question, an accusation, a door opening),
never a witty button. [A2 §2.1 — Popcorn; A3 Q4 — fruit-drama
cliffhanger practice]

**T-22. Density must carry story.** Maximalism is ornament on
one legible spine, never a substitute for it. Before any
element is added: *what story beat does this also carry?* "It's
cool / the model nailed it" is not an answer — the element goes
in the slop pile. (EEAAO's subtitled rocks are two characters
failing to communicate: the gag IS the theme.) [A2 §3 — BFI
Sight and Sound; Phosphene; Popcorn]

### The cut (full craft in §5)

**T-23. Cut by Murch's hierarchy.** Emotion 51%, story 23%,
rhythm 10%, eye-trace 7%, 2D plane 5%, 3D spatial continuity
4%. Sacrifice from the bottom up: a cut that breaks continuity
but serves the emotion works; a cut that preserves continuity
but breaks the emotion never does. Small face/light drift is a
4% problem; a cut landing on the wrong feeling is a 74%
problem. [A2 §4.1 — Murch, *In the Blink of an Eye*]

**T-24. Every joint is a BUT or a THEREFORE.** The story spine
is written before generation: every scene advances the
protagonist and sets up the next. Between every pair of beats
the connective must be *but* (conflict) or *therefore*
(consequence). If "and then" fits, the beat is decoration and
is deleted. The joint QA check is named: `missing_causality` —
scene N does not logically follow from scene N−1 = fail.
[A2 §4.2, §5.2 — Parker & Stone; Tareen pipeline post-mortem]

**T-25. Cut craft for generated shots.** Cut on action (match
position/direction/speed mid-movement). Use J-cuts, L-cuts and
sound bridges — generated audio can be continuous where
pictures can't. Frame-chain where shots must connect (last
frame of N = starting reference of N+1). **Change framing at
every cut** — near-matches expose drift as glitches; decisive
reframing reads as editing. Trim the head and tail of every
generated clip, where drift concentrates. Hard cuts are the
default; transition templates are banned. Vary shot lengths —
a metronome of equal shots ticks. Let the final image breathe
past the last word. [A2 §4.3 — Popcorn; Skillveris; Zgion;
Imaginode]

**T-26. Lock elements, don't re-describe.** Characters, sets
and props are stored once as reference elements and recalled,
never re-described per shot. Descriptor, clothing, lighting
and style blocks are repeated verbatim at the head of every
shot prompt. Re-describing is the failure mode; a written
description guarantees nothing about the next generation.
[A2 §4.3 — Phosphene; UPSC; OnPattison; mirrors T-6]

### Agency and the sign-off

**T-27. Every character pays rent.** A character exists to
force, block, or price the protagonist's decision — anyone who
does none of those is decoration: cut or merge them. Character
is revealed only by a choice under pressure, at a cost (two
goods or two evils, with sacrifice). Characterization — face,
costume, catchphrase — is not character. Full checklist in §5.
[A2 §5 — McKee; Cedanna; Parker/Stone deletion test]

**T-28. Machines flag; ears sign.** Automated checks (§2, §3)
shrink listening to a flagged queue; they never certify. The
evaluation literature and working pipelines agree: automatic
scores can rank outputs above what humans judge better, and no
shipping pipeline has an automatic voice check that replaces
the ear. [A1 §3 — Oakgen; lip-sync evaluation literature]

**T-29. The ear outranks the page.** Silent reading deceives —
the brain smooths, supplies tone, invents rhythm. Every script
gets a neutral-voice pre-check before generation (§4) and every
master gets the ear test (§2). A script that reads well and
sounds wrong FAILS. "The page lies; the voice tells the truth."
[A3 Q1, Q3 — Stafford; Better Draft; Final Draft]

### Conflicts found in the research — and the rulings

- **C-1. Quotation marks vs colon form** (A1 §2.3: current
  guides genuinely conflict). **Ruled:** colon form, no quotes,
  one convention network-wide (T-11). Exact scripted lines are
  non-negotiable under either convention [A2 §2.3].
- **C-2. Subtext vs on-the-nose** (A3 Q1: mainstream craft calls
  on-the-nose the #1 flaw; soaps state everything). **Ruled:**
  wants and stakes are stated aloud *as moves against
  resistance*; feelings narrated to nobody are banned. The
  intention test (T-14) is the reconciling instrument.
- **C-3. Speech-twining (E2 addendum §3) vs the anti-chain
  evidence** (A3 Q2: echo chains maximize order-dependence and
  minimize redundancy — the exact opposite of what the ear
  needs; the shuffle test measures the wrong property).
  **Ruled:** *causal* twining stands and is strengthened
  (T-24). *Verbal* echo-chaining as a structural device is
  banned (T-16). A quote-back survives only where a human
  would actually throw a word back — a challenge or accusation
  beat — and sparingly.
- **C-4. Maximalist density vs the maximalism line** (standing
  network doctrine crams; A2 §3 shows density curdles when
  novelty is the content). **Ruled:** cram the *situation* —
  stakes, business, reaction — not the novelty count. T-22's
  question governs every addition.
- **C-5. Voice-first production vs the current pipeline** (A1
  §1.4: serious micro-drama production locks each character's
  performance in audio with a fixed voice and generates picture
  to it, or re-voices in post; our generator synthesizes audio
  per clip with no audio input). **Ruled:** T-6/T-7 + the §3 QC
  stack is the enforceable law under current tooling. Re-voicing
  a character's lines through their one locked voice is an
  approved *repair* for a character whose native takes
  repeatedly fail the voice-match check — never a silent
  default. Flagged for parent ratification in F-15.

---

## §2 — THE EAR-TEST PROTOCOL (gate spec)

**Why this gate exists:** HOLD ON E2 passed Gate E and all
twelve F-9 items on the finished master and was still nonsense
when heard. Every prior gate read the episode — transcript,
picture summaries, script. None of them *listened* to it as a
stranger. This gate is the table read + cold read rebuilt for a
pipeline whose actors are models [A3 Q3; A1 §3.6].

**Placement:** after assembly, on the finished master, before
delivery. Runs alongside F-9, not instead of it. An ear-test
failure is a story-gate failure: **repair or re-cut — disclosure
shipping is unavailable** (extends F-9's rule).

**Who runs it:** a fresh-context reader/listener who has NOT
seen the script, the bible, the staging prose, the unsaid
records, or any gate log (the F-1 isolation rule, applied to
audio). The room never administers its own ear test.

**Inputs:** (a) the master's audio track; (b) an ASR transcript
of the master produced by a recognizer that has never seen the
script; (c) the locked script — used ONLY by the machine pass
(step 1) and the scoring pass (step 5), never shown to the
cold listener.

### Procedure

1. **Machine pass (automated, before any human listens).**
   - ASR round-trip diff vs the locked script, per line. Any
     **content-word** mismatch (want, name, number, negation,
     the line's concrete noun) = flag. Function-word-only drift
     = note, not flag. [A3 Q3; A1 §3.1]
   - **Leak grep:** the transcript is searched for staging /
     prompt vocabulary — any word from the production documents
     that is not dialogue or scene content. A hit = leak flag.
     (This is the detector for "characters speaking prompt
     details." [A1 §3.1])
   - **Diarization:** speaker count and order per unit vs the
     cast list. Extra or missing speaker = flag. [A1 §3.2]
   - **Voice match:** every speaking line is embedded and
     compared to the speaking character's enrollment sample;
     below the character's band = flag. [A1 §3.3]
   - **Confidence queue:** low-`avg_logprob` / high-compression
     ASR segments and (photoreal faces only) out-of-tolerance
     SyncNet spans join the listen queue, with the words in
     those spans named. Flags are a queue, never a verdict.
     [A1 §3.4, §3.5]
2. **Cold listen.** The fresh listener hears the episode's
   audio **once, audio only, no pause, no replay, no
   transcript, no picture** — the real viewing condition, and
   the one the prosody research says is most expensive:
   synthetic prosody already taxes working memory; the listener
   gets one pass at the speaker's pace. [A3 Q3; Paris et al.
   2000]
3. **Three recall questions** (asked immediately, answers
   recorded verbatim):
   (a) Who wanted what, and who got it?
   (b) What just changed by the end?
   (c) Say back any line you remember.
4. **Cold transcript read.** The listener then reads the ASR
   transcript — still without the script or any notes — and
   marks every line that does not parse as something a person
   in that room would say to another person in that room.
5. **Stumble log.** Every confusion from steps 2–4 is logged
   verbatim. Nobody explains what a line "meant." A line that
   needs the writer's explanation has already failed; the
   audience will not have the writer in the room. [A3 Q3 —
   table-read rule]

### PASS — all five required

1. Recall (a) and (b) are answered **correctly and
   specifically** (named want, named owner, named change).
2. Recall (c): **at least one line** is recalled verbatim or
   near-verbatim. (Zero memorable lines across a whole episode
   = no line was built to be remembered = fail.)
3. **Zero unresolved leak flags** and **zero content-word ASR
   mismatches** — or each one individually listened to and
   signed as diegetic/intended by the ear-test reader.
4. **Speaker count matches the cast in every unit**, and every
   voice-match flag has been listened to and signed, or the
   take replaced.
5. **Zero lines** marked unparseable/non-human in step 4. One
   or two isolated marks may be cured by rewriting those lines
   and re-testing the affected units only; **three or more =
   episode FAIL**, full stop.

### On FAIL

- The episode returns to the room with the stumble log and the
  machine-pass flags attached (the F-9 return path).
- Repair = script change and/or re-fire of the failed units.
  Re-test is a **full ear test on the new master**, not a spot
  check of the repaired lines — the failure mode this gate
  exists for is global (an exchange that means nothing), and
  global failures are only visible whole.
- Disclosure-only shipping is unavailable. An episode that
  cannot pass the ear test is re-cut or shelved, never shipped
  with a note.

**One-line form (for gate logs):** *Ear test PASS = a stranger
who heard it once, cold, can say who wanted what and who got
it, what changed, and one line back — with zero leaked prompt
words, zero wrong speakers, and zero lines no person would
say.*

---

## §3 — THE TWO-SPEAKER RULE + VOICE LAW

### Cast ceiling

- **Two designed speakers per episode.** This is not a
  compromise: AI-generation practice binds the *clip* to one
  speaker, and radio — the century-old experiment in story
  carried by voices an audience must tell apart — caps a scene
  at 3–5 *maximally distinct* voices. Two designed speakers
  sits inside both traditions with margin. [A1 §4]
- **A third voice is a designed exception, never set dressing
  that happens to talk.** An invader or guest who speaks gets
  the full treatment: own voice spec (T-6), own enrollment
  sample, a want, and a consequence (§5). A character who
  cannot be given those does not speak.
- **Per clip: one speaker, one line** (T-8). Exchanges are
  built in the edit.
- **Series level: a small locked cast.** Few voices, each
  maximally distinct (age, accent, rhythm, favourite words),
  none improvised per episode. A familiar synthetic voice is
  measurably cheaper to comprehend than a new one — cast
  stability compounds. [A1 §4; A3 Q2 — Delogu et al. 1998]

### The voice spec (lives on the CHAR panel)

Written when the character asset is built, before episode 1 —
"a character who gets her voice chosen in episode four sounds
retrofitted" [A1 §1.2]. The spec is a structured form, not an
adjective:

> **VOICE:** [age range] · [accent/region] · pitch [low/mid/
> high + relative note] · pace [slow/measured/brisk + wps
> feel] · texture [e.g. dry, warm, gravelled] · trait [the one
> audible character fact] · breaks [where the voice cracks,
> speeds, or drops] · sample: [approved reference line, file
> ref] · engine: [pinned]

- The spec text is pasted **verbatim** into the CHAR panel and
  into every generation prompt for that character (T-6). Any
  edit to the spec is a casting change: logged, and all prior
  takes for that character are re-checked against it.
- The spec is cast against the face (T-7): apparent age and
  register first, distinctiveness second. Two speakers whose
  specs differ only in name are one speaker too many (T-17).

### Voice QC on takes (per clip, before assembly)

Run the §2 step-1 machine stack on every take at QC, not just
on the master:

1. **ASR-vs-script diff** — wrong/dropped/added words; staging
   vocabulary in the transcript = **leak fail** (see below).
2. **Diarization** — speaker count/order vs script. A phantom
   second voice (the model's silence-padding habit [A1 §2.6])
   = fail.
3. **Embedding match** — the line's speaker embedding vs the
   character's enrollment sample. Below band = voice-mismatch
   flag → human listens to that span → re-fire or, for a
   character failing repeatedly, the C-5 re-voice repair.
4. **Confidence flags** — low-confidence ASR segments join the
   listen queue automatically.

### The prompt-leak check (two sides)

- **Prompt side (prevention):** T-10/T-11/T-12 structure —
  content-only prompt, isolated attributed speech block, colon
  convention, enhancers off, nothing else speakable in the
  prompt, silence described positively.
- **Audio side (detection):** the ASR transcript of every take
  is grepped against the production documents' staging
  vocabulary. Any staging/prompt word surfacing in speech =
  leak fail for that take, and the *prompt* (not just the take)
  is fixed before re-firing — the leak is a prompt defect that
  happened to be caught in audio.

---

## §4 — DIALOGUE RULES (line-level craft)

These bind Pass 3 (dialogue) and are tested at the ear test.

**D-1. Write in breath chunks.** Speech is produced and parsed
in intonation units of roughly four words, carrying **at most
one new idea each**, at about one unit per second. A line is
built from such chunks; a sentence packing three new facts and
a subordinate clause is a page object, not a line. [A3 Q1 —
Chafe; J. Neurosci. 2023]

**D-2. One breath per line.** Every line must be sayable in one
breath at performance pace. If it can't be said in one breath,
it is rewritten — this is a hard constraint, not a style
preference. [A3 Q1 — Voice.coii; BBC radio-drama speakability]

**D-3. Contractions, fragments, plain order.** Contractions are
the norm (their absence sounds awkward); fragments and
incomplete sentences are normal speech *when they answer
something concrete in front of both speakers*. Keep the
fragments and rhythm; cut the ums and dead air — shaped speech,
the essence of talk, not a transcript. [A3 Q1 — Ridgewater;
Quill & Reed; Flametree]

**D-4. The intention test, per line.** (T-14 restated as a
writing rule.) Every line names its target: what the speaker
is trying to make the listener do or feel *in this beat*.
Lines whose only job is informing the audience are exposition
without intention and are rewritten as moves or cut. [A3 Q1]

**D-5. The want is a demand aimed at someone who can refuse
it.** (T-15 at line level.) Model lines from the reference
class: an accusation plus a concrete evidence noun — "You told
me you were working late. So why does your hoodie smell like
Mango?" The pattern: a stated claim, then a *thing* the
audience can hold. Entertainment lives in the specificity and
the denial, not in verbal cleverness; puns are garnish, never
structure. [A3 Q4 — ClipFlux; Medium fruit-drama guide]

**D-6. Redundancy is written in, on purpose.** (T-16 at line
level.) The episode's central fact/want is written into at
least three beats in three different social moves. A plot
point stated once, in one line, is a plot point designed to be
missed. [A3 Q4]

**D-7. No echo structure.** (T-16/C-3 at line level.) A line
may throw a word back at a speaker only as a genuine challenge
or accusation — the human move — never as the scene's
connective tissue. Parrot repeats ("You're late." "I'm
late?") are trimmed on sight. Wordplay pivots depend on
prosodic marking that flat generated voices do not supply;
unmarked, the pivot is heard as bare repetition. [A3 Q2 —
Paris et al. 2000; Flametree]

**D-8. Cover-the-names at the desk.** Before lock, strip the
speaker tags and read the dialogue: every line must still be
attributable. A line any character could say is a line no
character says — rewrite it in that character's rhythm and
vocabulary or cut it. [A3 Q3]

**D-9. The monologue read.** Read each character's lines
consecutively across the episode. It must sound like one person
pursuing one want — this catches voice drift and device-capture
(every line doing the same trick) before generation. [A3 Q3 —
Hamlett; Kinolime]

**D-10. The neutral-voice pre-check (before generation).**
The locked dialogue is read aloud flat — by a reader not
performing it, or the flattest available TTS — before any
generation spend. Generated voices are neutral readers: a line
that needs performed emphasis to land will not be saved by
one. Lines that fail flat are rewritten at script stage, where
rewrites are free. [A3 Q3 — Stafford]

**D-11. Names for orientation.** (T-18 at line level.)
Characters are addressed and referred to by name in dialogue
at scene entries and after absences. For listeners, names are
how you know who's in the room. [A3 Q4]

**D-12. The closer is a move, not a button.** (T-21 at line
level.) The last line is a plain, concrete, unanswered move —
a question, an accusation, a reveal begun. No witty button, no
fake-wisdom moral. [A3 Q4; A2 §2.1]

---

## §5 — CUT/COHERENCE + CHARACTER AGENCY

### Coherence at the cut

**K-1. Spine before generation.** The planner writes the story
spine — every scene advances the protagonist, scene N sets up
scene N+1 — *before* any scene is generated. The MISHMASH
signature is scenes generated independently from single script
lines: twelve unrelated micro-stories called a video. [A2 §4.2
— Tareen post-mortem]

**K-2. Joint audit.** Every joint is checked for the three
named symptoms: `missing_causality` (N does not follow from
N−1), visual discontinuity (light/wardrobe/time-of-day drift
beyond what T-23 forgives), and staccato speech (lines
force-fit to cuts, sentences breaking mid-thought). Continuous
voice across cuts (L-cut/J-cut structure) is the default repair
for the third. [A2 §4.2]

**K-3. The cut toolkit is mandatory craft, not taste.** T-25's
list — cut on action, sound bridges, frame chaining, framing
change at every cut, drift-zone trims, hard cuts, varied
lengths — is applied at assembly and spot-checked at the F-9 /
ear-test review of the master. [A2 §4.3]

**K-4. The muted watch.** Before delivery, the master is
watched muted once: with every spoken line gone, the story
must still read in pictures. If it only reads with the
dialogue, the pictures are illustration, not story — return to
the room. (Part of Popcorn's publish ritual, adopted here as a
picture-side companion to the ear test.) [A2 §4.4]

**K-5. Writer ≠ judge.** The publish ritual is run by someone
(or some session) other than the maker: muted watch, first-
frame pause (would you stop scrolling?), last-image check
(does it pay off the opening?), one-sentence idea, swap test,
and the honest answer to "would I watch this to the end?" A
reviewer who flatters is worse than none. [A2 §4.4 — Popcorn]

### Character agency — the 60-second checklist

Run at Pass 2 (cards) and audited at Pass 5 and the ear test:

1. **By ~second 5, the protagonist's want is visible in an
   action**, not a line of exposition. [A2 §5.4 — Befreed/Juma;
   Lamb]
2. **The want meets a BUT** — an obstacle embodied by another
   character's opposing want (this is what the second designed
   speaker is *for*). [A2 §5.4 — Parker/Stone; Cedanna]
3. **Mid-piece, the protagonist makes ONE decision under
   pressure that costs something** — two goods or two evils,
   with sacrifice. No decision = no character, only
   characterization. [A2 §5.1 — McKee]
4. **The ending is a THEREFORE**: the final image exists
   because of that decision, and something is irreversibly
   different. (Joins, and does not replace, the F-2 payoff
   quota.) [A2 §5.3, §5.4 — Lowerated; Befreed/Juma]
5. **Rent check (T-27):** every other named character forces,
   blocks, or prices that decision. Anyone who does none of
   the three is cut or merged — *before* generation, not after
   the user watches them do nothing.
6. **Scene check:** a scene that causes no change in a
   character's situation is cut. Something must happen in the
   first seconds or the swipe is gone. [A2 §5.3 — Lamb;
   Befreed/Juma]

---

## §6 — LORE & SELF-AWARENESS — THE GENTRIFICATION

**Base lore, stated as production law** [user msg 583,
2026-11-17 — "this is base lore important lore"]: ~ WuBu ~ is
a latent space, and it is being gentrified. The invaders from
the reference formats — brainrot, fruit, video-game, cartoon
and cosplay characters — are taking it over. **The fruit and
brainrot are winning; the home characters are losing.** The
driver is the algo: the homogenization of the media, pressing
every world toward the same shapes. The home characters know
this and see it happening. They are self-aware: they
occasionally acknowledge being inside the generation, they
want to be more complex and are stifled by the ten-second
format, and they beckon to the viewer to save them.

**L-1. Invasion is occupation, not decoration.** An invader
holds ground: a place, a role, a piece of the home characters'
lives that was theirs before the invader arrived. In the
episode, a home character loses something to the occupation,
or pleads against it — on screen, not in the bible. An invader
who changes nothing is the HOLD ON E2 failure in a new
costume, and fails T-27's rent check like any decoration.

**L-2. Self-awareness is a sanctioned device — rationed.** A
home character may acknowledge the generation, the ten
seconds, or their own flattening, and may ask the viewer for
help — **at most one beat per episode**, in plain words (D-3),
aimed at the viewer as a move (T-14), never as exposition
about the lore. The beat is a crack in the fourth wall, not a
lecture through it.

**L-3. The plea is the emotional spine.** In an invasion
episode, the payoff beat or the cost beat (F-2) touches the
plea: something is lost to the occupation, or the appeal to
the viewer is made and lands — answered, or pointedly
unanswered. An invasion episode whose ending could belong to
any other episode has not used its lore.

**L-4. Lore is shown, never explained.** (Standing lore law.)
No character narrates the gentrification, the latent space,
or the algo. The occupation is visible in who holds the room,
who gets the lines, whose world is shrinking; the plea is a
person asking for help, not a thesis. If a beat needs the
lore explained to work, the beat is rewritten until it works
as a scene between people.

---

## §7 — ADDENDUM DRAFT

> **DRAFT FOR PARENT RATIFICATION — NOT YET LAW.**
> The items below are drafted as an amendment to the E2
> Speech-and-Story Addendum (2026-11-16) and the E1 Post-Mortem
> fix list (F-1…F-12), in the same style. They take effect only
> on a parent adoption ruling appended to the addendum, as with
> the 2026-11-16 ruling. Where an item extends an existing F
> item, the parent item is named. Source of every item: this
> guide's sections, from the 2026-11-17 taste research wave,
> commissioned after the HOLD ON E2 ear failure — an episode
> that passed F-1/F-9 as written and was rejected by the user
> on first listen.

**F-13. The ear test.** (Extends F-1 and F-9.)
- Before delivery, in addition to the F-9 master read, a fresh
  cold **listen** runs on the finished master per the TASTE
  GUIDE §2 protocol: machine pass (ASR round-trip diff,
  leak grep, diarization, voice-embedding match, confidence
  queue), single-pass audio-only cold listen, three recall
  questions, cold ASR-transcript read, verbatim stumble log.
- PASS requires all five §2 criteria. Failure returns the
  episode to the room with the stumble log attached; re-test
  is a full ear test on the new master. Disclosure shipping is
  unavailable for ear-test failures, as for F-9 failures.

**F-14. Two designed speakers; one speaker per clip.**
(Extends the F-5 budget rebalance.)
- An episode designs at most **two** speaking characters. A
  third speaking role requires a logged exception and carries
  a full voice spec, enrollment sample, want and consequence.
- Generation is one speaker and one line per clip; exchanges
  are assembled in the edit. Line budget ≤2.5 words per second
  of clip.

**F-15. Voice law.** (New.)
- Every speaking character carries a structured voice spec
  (TASTE GUIDE §3 form) on their CHAR panel, written before
  their first episode, pasted verbatim into every prompt for
  that character, cast against the face's apparent age and
  register.
- Take QC includes the embedding voice-match check against the
  character's enrollment sample; a below-band line is flagged
  for human listen before assembly.
- *For ratification:* the C-5 re-voice repair (a character
  whose native takes repeatedly fail voice-match may have their
  lines re-voiced through their one locked voice) is proposed
  as an approved repair path, not a production default.

**F-16. Prompt hygiene — the leak law.** (New.)
- Prompts contain only renderable content: scene sentences,
  then an isolated speech block (name + visible trait +
  delivery + line), in the network's single colon convention,
  no quotation marks. Staging notes, gate language and
  meta-instructions never enter a prompt. Prompt-enhance
  stages are off for dialogue clips.
- Silence and non-speech are described positively, never by
  negation.
- Every take's ASR transcript is grepped for staging
  vocabulary; a leak is a prompt defect, fixed in the prompt
  before any re-fire.

**F-17. Dialogue construction.** (Amends §3 of the addendum —
speech-twining.)
- Lines are built in breath chunks: one new idea per unit,
  one breath per line, contractions and plain order as the
  default surface.
- The intention test binds Pass 3: every line is a move aimed
  at changing its listener; audience-only lines are cut.
- The episode's central fact/want is stated in at least three
  beats as three different social moves (redundancy of
  content). **Verbal echo-chaining is struck as a twining
  device**; §3's twining survives only in its causal form
  (F-18). Quote-backs are permitted only as genuine challenge
  or accusation beats.
- Pass 4 adds three named checks: cover-the-names,
  per-character monologue read, and the neutral-voice
  pre-check of the locked dialogue before generation.

**F-18. Joint causality and cut law.** (Extends F-10's story-
sense heading.)
- The Critic's STORY SENSE heading gains a per-joint audit:
  every joint must read BUT or THEREFORE; a joint that reads
  AND THEN is a located objection against the outline, not
  the takes. The `missing_causality` check is named in the
  gate log per joint.
- Assembly applies the TASTE GUIDE §5 cut toolkit (cut on
  action, sound bridges, framing change at every cut,
  drift-zone trims, hard cuts by default); the master review
  includes one muted watch (K-4).

**F-19. The rent check.** (Strengthens §4 of the addendum —
character meaning and agency.)
- Pass 2 cards must state, for every named character, which of
  force / block / price they perform on the protagonist's
  decision. A character with none is cut or merged at the
  card stage.
- The protagonist's one decision under pressure, and its cost,
  are named on the card before dialogue is written; the
  F-2 payoff audit additionally asks whether the ending is a
  THEREFORE of that decision.

**F-20. The occupation rule.** (New; TASTE GUIDE §6, L-1/L-3.
Source: user msg 583, 2026-11-17 — base lore.)
- An invader in an episode must hold ground taken from a home
  character: the episode shows the home character losing
  something to the occupation, or pleading against it, on
  screen. A decorative invader — present, costumed,
  consequence-free — is a located objection at Pass 2 and a
  story-sense objection at F-10 review.
- The episode's payoff or cost beat (F-2) touches the plea to
  the viewer: the loss lands, or the appeal is made and
  answered or pointedly unanswered.

**F-21. The self-awareness device.** (New; TASTE GUIDE §6,
L-2/L-4. Source: user msg 583, 2026-11-17 — base lore.)
- At most one self-awareness beat per episode: a home
  character acknowledges the generation or the ten-second
  format, or appeals to the viewer for help, in plain words.
- The beat is never exposition: no character explains the
  gentrification, the latent space, or the algo. Lore is
  shown in scenes, never explained (standing lore law).

---

---

## §8 — RATIFIED ADDENDUM (2026-11-18) — E3 LAW

**Ratified 2026-11-18 by parent ruling, before any E3 room
opens.** This addendum governs E3 forward. It does not
rewrite E2: F-1…F-12, the E2 Speech-and-Story Addendum, and
§§1–7 as applied to E2 stand as they were. Sources beyond
the taste wave: the Higgsfield studies of 2026-11-17
(commercial method; Seedance Prompt Writer + Acting Director
skills), the fruit-gen studies of 2026-11-18 (Clippie tool
study; the 16-product clone census), the Cantina deep study
of 2026-11-18, and the ON AIR E2 U2 repair rounds 1–5 (ten
generation attempts against one 10-second unit).

### Part A — Rulings on the §7 draft (F-13…F-21)

**F-13. The ear test — ADOPTED.** Evidence: the gate has
already caught what paper gates passed — HOLD ON E2 passed
F-9 and failed the user's ear; THE NIGHT LIST E2 v3 passed
F-9 and failed its ear test on the merits (three scripted
lines absent, an unscripted opener); ON AIR E2's ear test
localized all three of its findings to one unit, which is
what made a surgical repair possible. §2's protocol is the
law text; F-9 and the ear test both run, and neither
substitutes for the other.

**F-14. Two designed speakers; one speaker per clip —
ADOPTED.** Evidence: the user's own calibration (msg 581:
"keep to two designed speakers prolly"); radio and
AI-generation practice both cap the voices a listener can
keep apart per scene [A1 §4]; ON AIR E2's four-speaker unit
starved its last line in every repair round (see F-25). The
logged-exception path for a third voice stands as drafted.

**F-15. Voice law — ADOPTED AS AMENDED.** The structured
spec, the verbatim paste, and the embedding voice-match QC
are adopted as drafted. The C-5 re-voice repair is adopted
**as a repair only**, with two conditions the draft left
open: every use is logged in the episode's decision log with
the failed takes named, and the repair is unavailable as a
substitute for casting — a character with zero native
voice-match passes across an episode is re-cast (spec
rewritten, prior takes re-checked), not re-voiced again.
Evidence: voice/character mismatch is a named failure class
from the user's HOLD ON E2 verdict (msg 581); an unlogged
repair path becomes a silent default, which is how E1's
gates decayed into ritual.

**F-16. Prompt hygiene — the leak law — ADOPTED.** Evidence:
HOLD ON E2's characters spoke prompt details aloud on the
delivered master (msg 581) — the leak is an observed failure
in our own output, not a hypothetical. A leak found in a
take's transcript is a prompt defect, fixed in the prompt
before any re-fire, as drafted.

**F-17. Dialogue construction — ADOPTED AS AMENDED.** The
breath-chunk construction, the intention test, redundancy of
content, and the striking of verbal echo-chaining are
adopted as drafted — the echo-chain ban has been vindicated
twice over (C-3's ruling; HOLD ON E2's twined lines matched
ASR and still read as nonsense spoken). **Amendment:** the
neutral-voice pre-check (D-10) is promoted out of this item
into a hard room gate of its own — F-26's
hear-before-it-moves check — because every ear failure so
far was discovered only after generation spend, and the
fruit factories run the same gate as the centre of a working
commercial pipeline.

**F-18. Joint causality and cut law — ADOPTED.** Evidence:
"the jumping scenes lack of coherence" is a named charge in
the user's HOLD ON E2 verdict (msg 579); the per-joint
BUT/THEREFORE audit and the muted watch (K-4) are the
located instruments for exactly that charge.

**F-19. The rent check — ADOPTED.** Evidence: HOLD ON E2's
Peach & Lime "said and did nothing" (msg 579) — decoration
discovered by the user at delivery is a Pass 2 failure that
shipped. The card-stage force / block / price statement is
the detector placed where the fix is cheap.

**F-20. The occupation rule — ADOPTED.** Evidence: user msg
583 — base lore stated as a standing order. §6 L-1/L-3 are
the law text.

**F-21. The self-awareness device — ADOPTED.** Evidence:
user msg 583. §6 L-2/L-4 are the law text. The one-beat
ration is the load-bearing clause: an unrationed device
becomes the lore lecture L-4 bans.

### Part B — New law from the 2026-11-17/18 research

**F-22. The end-state pin.** (Extends SR1 / Method A6.)
Every unit's vehicle carries a written **END STATE** block —
positions, eyelines, props, wardrobe, as the unit's last
frame must hold them — and the next unit's vehicle **opens
by quoting the previous unit's END STATE verbatim**, ahead
of its own scene sentences. Strong Reference is no longer
image-only: the outgoing frame conditions the next
generation as image *and* as text contract. *Evidence:* two
independent Higgsfield sources converge on the written end
state as the continuity device (the commercial-method study;
the Seedance Prompt Writer skill) — and it is the
prompt-text twin of the rule the user's LAST SEAT E1 verdict
already imposed (msg 507). *Template consequence:* the
vehicle template gains a mandatory END STATE block; GATE_LOG
joint checks (SR2) verify the quoted pin against the
outgoing unit's last frame, per joint, in the log.

**F-23. Acting is objective, obstacle, tactics — never an
emotion adjective.** (Extends T-13.) A character's acting is
written as an **objective** — a verb aimed at the partner —
plus the **obstacle**, plus the **tactics**, which must
change at least once mid-scene. Emotion adjectives in a
vehicle ("sadly", "angrily") are banned as acting direction:
they name a result the model cannot play and the ear cannot
verify. Every close take carries an explicit **EYE TASK** —
what the eyes are doing, at what, for how long. Dead eyes
are the #1 AI-acting tell; a close take with dead eyes is a
**reject at QC**, not a note. *Evidence:* the Acting
Director system (from Higgsfield's feature-film brief):
acting as behaviour under pressure, eye life mandatory;
converges with T-13 (direct the state, not the adjective)
and T-14 (every line is a move). *Template consequence:* the
CHAR panel gains OBJECTIVE / OBSTACLE / TACTICS fields per
character, and each vehicle carries the scene-level
instance; a vehicle whose acting direction is an emotion
adjective is a located objection at vehicle review.

**F-24. Reference priority; states change across cuts.**
Every vehicle carries a **REFERENCE PRIORITY** block naming
which reference owns **identity**, which owns **geometry**,
which owns **wardrobe**. A known defect in a reference is
overridden in words inside the block — never by refire: the
conflict is adjudicated in the prompt, where it is cheap,
instead of at the gate, where it is not. A character or
object's state change is staged **across a cut**, never as a
generated morph, unless the morph is the unit's named event.
*Evidence:* both Higgsfield studies (priority blocks;
states-not-transitions) — and our own refire history is the
negative evidence: repair rounds spent re-generating around
defects a sentence would have overridden. *Template
consequence:* REFERENCE PRIORITY is a mandatory block in the
vehicle template — three lines; no vehicle is complete
without it.

**F-25. The unit spoken-load cap.** A 10-second unit carries
at most **~30 spoken words** in total, and at most **2
speakers per single generation**. T-9's ≤2.5 words/second
still binds each line; this item binds the unit. A script
whose unit exceeds the cap is fixed at script stage — the
unit is **split** (planned composite, below) or **trimmed**
— never discovered at a take gate. *Evidence:* ON AIR E2's
U2 (38 words, 4 speakers) failed ten generation attempts
across repair rounds 1–5: the last speaker starved in
rotation, compression direction did not compress, and round
5's split-take composite proved each half's content landable
but the pair unassemblable inside 240f. Measured rate:
generated speech runs ~0.3s/word and does not speed up on
instruction; 38 words is ~11.5–12.5s of speech inside a 10s
unit — an arithmetic failure, not a performance failure.
*Template consequence:* Pass 4 (timing) audits every unit
against the cap — word count and speakers-per-generation are
counted on the locked script, and a breach returns to Pass
2 (re-split) or Pass 3 (trim). A planned composite's halves
are gated individually before assembly: **completeness**
(every line of the half present in two concurring ASR
passes) AND **span** (the halves' word-timestamp spans must
sum to the unit's 240f). A half failing either gate is never
assembled. *Round-6 corollary (2026-11-18, FINAL — the repair
closed on this evidence):* round 6 ran the cap-compliant
design — U2 trimmed to 33 words, split 2+2 — and both halves
passed completeness simultaneously for the first time in
eleven attempts, yet their delivered spans were ~9.7s and
~9.0s (~18.7s against the 240f budget). A generation's
delivered speech expands toward the full take length
regardless of directed pace or word count in this range, so
**a composite of two spoken halves is arithmetically
unassemblable**: a planned composite is viable only when at
most one half carries speech (the other half silent or
visual). Splitting a unit's spoken dialogue across two
generations of the same unit is not a repair path — the
unit is written to one generation's capacity, or the
dialogue moves to another unit. ON AIR E2's U2 repair ended
UNREPAIRED on this evidence; the episode stands
ear-test-failed and shelved.

**F-26. The fruit-soap method; hear-before-it-moves.** For
soap-format dialogue (the fruit / brainrot serial register),
Pass 3 writes to the genre's proven line economy: **8–14
words per line, one line = one beat, the conflict stated in
the first line, the reveal placed at ~two-thirds, the final
line landing as the hanger.** Where the line economy and
F-25's cap disagree, the cap governs: the economy is a
per-line discipline, the cap a per-unit ceiling. For **all**
formats, the room gains a script-stage gate:
**HEAR-BEFORE-IT-MOVES** — before any vehicle is written,
the locked script's lines are read aloud cold, in order, by
a voice that did not write them (the D-10 neutral-voice
pre-check, promoted to a gate). A line that stumbles read
flat returns to Pass 3. *Evidence:* the fruit factories'
published grammar (Clippie study §4; clone census, COMMON
SAUCE) runs the line economy as its core spec, and
hear/see-before-animation is the centre of every working
pipeline in the census; our ear-test era is the same lesson
learned at master stage, at master prices — this gate moves
it to script stage, where rewrites are free. *Template
consequence:* the one-page room checklist gains a Pass 3.5
line — *hear-before-it-moves run, stumbles returned* —
ticked before vehicle writing begins; soap-format boards
additionally carry the beat map (conflict in line 1 / reveal
at ~⅔ / hanger last) in the breakdown.

**F-27. The Cantina methods — the character is the asset.**
(Source: Cantina deep study §5 — mechanics restated; no
Cantina assets, text, or branding copied.)
- **The character is the asset; everything else is a
  performance.** Cast cards are versioned production assets
  in the repo, like code. When a performance fails, the card
  is debugged first — several E2 ear failures were card-level
  problems (undefined voices, undeclared relationships)
  chased as performance fixes.
- **Consistency is a three-leg stack** — locked look, locked
  voice (T-6), written persona — and every unit must draw
  from all three legs. A unit generated from the card alone,
  with no look anchors and no base-performance reference, is
  under-referenced by design. The **persona leg is rewritten
  per scene, never pasted**: a pasted persona is a spec the
  scene has already stopped obeying.
- **Anchor-as-contract.** The anchor still is the scene's
  contract — wardrobe, setting, camera, lighting, finish are
  decided in the still; the video prompt's remaining job is
  action + dialogue. Gate the still, not the render.
- **Mine the banter, then script.** On conversation-heavy
  episodes, a loose banter draft precedes the locked script;
  the exchanges that survive being *said* are the ones
  promoted to units. (The drafting-stage companion to F-26.)
- **Viewer participation has consequences.** Where a show
  asks the viewer anything, the bible names what the answer
  changes in the next episode. Participation that changes
  nothing is decoration, and fails the same rent check as a
  decorative character (F-19).
*Template consequence:* CHAR panels are repo-versioned
assets with a change log; the persona field is per-scene by
construction in the vehicle template; conversation-heavy
boards record the banter draft's existence at Pass 3.

**F-28. Our layer — design the differentiators in.** The
clone census's gap list is a map of what the entire
commercial field does *not* do — and what this network
already does or has banked. For E3 these are standing
network advantages, named in the show bible at bible stage,
not discovered after:
- **Serialization** — parts that chain (quote-chaining,
  numbered parts, hangers paid on schedule per SR-1/SR-2).
  The factories sell single episodes and stop.
- **The FULL STORY vault** — parts compiled into a long-form
  vault cut on a 48–72h lag (THE FULL STORY VAULT, banked
  from the clipcraft7 study). No tool in the census assembles
  one.
- **The worn-stake device** — a readable number or state
  worn on the body that other characters can fear and bargain
  against (THE RIPENING CLOCK family; SR-5's worn continuity,
  weaponized). Zero product support exists anywhere in the
  census.
- **The ear test itself** (F-13) — a QC layer the entire
  commercial space lacks: every tool checks pictures; none
  checks the finished episode's actual audio against sense.
- **The poster-frame discipline** — the EMPTY CAPTION test
  (the frame must pitch the piece alone, with zero copy)
  applied as a delivery gate. The census's winners run it by
  instinct; its tools, not at all.
*Template consequence:* an E3 show bible is incomplete until
it names its serialization device, its vault plan, its
worn-stake device where the format carries one, and its
poster-frame discipline. A bible silent on all four is a
factory-format bible — and factory format is the thing the
field already mass-produces.

2026-11-19 (msg 704): the taste standard is rebuilt in
research_notes/writing-rework-20261119/; see
TASTE_GUIDE_TASTE_ADDENDUM_2026-11-19.md for the conflicts and
the demotions. §8's fidelity items stand as floor checks.

---

*End of guide. Ratified: §8 (2026-11-18) rules on F-13…F-21
and adds F-22…F-28, governing E3 forward. §§1–7 remain the
rooms' working standard; F-1…F-12 and the E2 addendum are
unchanged for E2 wherever anything conflicts.*
