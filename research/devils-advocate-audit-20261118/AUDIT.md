# DEVIL'S-ADVOCATE SYSTEM AUDIT — reference design, first/last frames, prompt design

**Ordered:** user msg 642 (2026-11-18) — heavy use of generated
reference-image design, first-frame/last-frame image design, and
prompt design; a triple devil's-advocate pass over the whole
system for the things *obviously* slipping us up; the banked
research shows what the successful others do — find where we are
not doing it, and fix the QC issues there.

**Method:** the E2 production record read as evidence, not as
reputation — all five episodes' VEHICLES.md (+ repair vehicles),
REFERENCE_STACK.md, work/GATE_LOG.md, DECISION_LOG.md, and the
four ear-test verdicts, against TASTE_GUIDE §§1–8, THE_SAUCE,
the Cantina study §5, the Clippie study, and the measured
video-api-mastery skill. Every factual claim below names its
file. Grep-verified negatives are stated as grep-verified.

**The fairness note, once, plainly:** F-22…F-27 were ratified
2026-11-18, *after* E2 wrapped; E2 ran under E2 law and broke
none of it by existing before it. That is not the charge. The
charge is narrower and worse: the *knowledge* was already in the
building while E2 was produced — the video-api lab is dated
2026-11-06, the anchor playbook 2026-09-26, the niceaunties
still-first study 2026-11-15, the Higgsfield studies and the
TASTE rules (T-6 voice spec, T-10/T-11 prompt hygiene and the
colon form, T-12 presence-not-absence, T-26 lock-don't-redescribe)
2026-11-17 — and the production *templates* carried almost none
of it. E2's rooms re-derived, per episode, in prose, what should
have been fields in a form. The user said it exactly (msg 642):
we can see what they are doing; we are not doing it. This audit
is about the template gap, not a knowledge gap.

**What E2 did right (the audit keeps these):** look blocks and
trait lines restated verbatim on every call (T-26 honoured in
all five episodes); inherited panels md5-locked and read back
before use — the ref-poisoning rule genuinely practised on
panels (all five REFERENCE_STACKs); panels eye-QC'd before
firing, with nits logged honestly (ONE SHORT's stack is the
model); joint eye-verdicts logged plainly, including INCOHESIVE
verdicts against the room's own work (E1 ONE SHORT J1/J4);
deterministic PIL plates for device text (NIGHT LIST board
states, ONE SHORT board); HOLD ON's held-object law; LAST
SEAT's written last-frame targets. The picture-side discipline
is real. Almost everything below is about the legs that were
never built: voice, persona, adjudication, and the speech block.

---

## 1. REFERENCE-DESIGN AUDIT — how the anchors are actually made

### 1.1 What exists today

Each E2 episode has a REFERENCE_STACK.md: a panel table (CHAR
hero/face sheets per character, WORLD panels, one PEAK panel per
unit, harvested JOINT frames), md5s, lock status, and eye-QC
notes. Panels are generated fresh per episode or inherited
md5-identical from E1 and re-verified at copy-in. This is a real
asset discipline — and it is **look-only**. The stack is a
wardrobe-and-faces ledger. It contains:

- **No voice data at all.** `grep -i voice` over all five E2
  REFERENCE_STACKs returns **0 hits in every file**. No voice
  spec (T-6/F-15), no enrollment sample, no engine pin — for any
  character, in any episode.
- **No persona data.** No Identity / Personality / Backstory
  fields, no want, no rent line. The "card" is a look block plus
  a panel list.
- **No drift taxonomy.** Drift is recorded in free prose in the
  gate logs; Clippie's four classes (identity / wardrobe / prop
  / motion), each with a named first fix, are never applied as a
  checklist anywhere in the E2 record (the phrase "identity
  drift" occurs a handful of times as prose — HOLD ON GATE_LOG
  flaw #7, ON AIR U4, NIGHT LIST U5 — never as one class of a
  four-class pass with its fix attempted).

### 1.2 Ad-hoc anchors vs a designed cast-sheet system

The CHAR sheets themselves are well made. The ad-hoc part is
*when and why new ones appear*:

- New characters are designed **inside the episode that needs
  them**, at production speed: HOLD ON E2 generated its June/Eli
  couple panels, its Courier face, and its Fruit Couple panel
  within the E2 panel batch (panels/ media-generation records);
  NIGHT LIST E2 generated the Blob Prince hero the same way;
  ONE SHORT E2 generated Hale and Champion sheets "text only"
  mid-production. There is no bible-stage cast-sheet build where
  the season's cast is designed, gated, and locked *before* a
  room opens — the sheet is a production artefact, not a casting
  decision. Cantina's rule is the inverse: the character is the
  asset, built once, versioned like code; episodes are
  performances of it (Cantina §5.1; F-27).
- PEAK panels are **composite generations** — ONE SHORT's stack
  records PEAKs generated from "WORLD + 3 sheets" and "WORLD +
  4 sheets" in a single image call. A composite panel is itself
  a generation with its own drift, and the record shows it:
  PEAK-U3's dressing put chalk X marks on the stacked chairs *a
  unit before the story does*; PEAK-U6 put a stray chalk X on
  the Counter's scalp. Both were caught by eye-QC and routed
  around in vehicle text ("NEVER restated in the U6 vehicle") —
  good practice, but it means the "contract still" (Cantina
  §5.3: wardrobe, setting, camera, lighting, finish decided in
  the still) sometimes contracts for things the story hasn't
  done yet, and the fix is a note, not a regeneration.
- Aspect discipline is worked around, not designed: ONE SHORT's
  inherited sheets are 3:2 originals with locally padded 16:9
  derivatives ("E1 local pad of the locked sheet"). The measured
  skill is explicit that a ref at the wrong aspect degrades the
  first-frame lock and that unstated aspect follows the images
  (video-api-mastery, V-01/V-03). Padding preserves the md5
  lineage; it does not make the sheet a 16:9 design.

### 1.3 Against the three reference systems in our own research

- **Cantina — still-first, anchor-as-contract.** The anchor
  still decides wardrobe/setting/camera/lighting/finish; the
  video prompt's remaining job is action + dialogue; *gate the
  still, not the render*. We gate the still (eye-QC before
  firing — real) but the still does not carry the contract:
  because no REFERENCE PRIORITY block exists (§3), the video
  prompt re-argues the scene in prose and the model re-decides
  what the still settled. The contract is signed and then
  renegotiated on every call.
- **niceaunties — still → gate → animate, at volume.** 25–30
  prompts per video spent at the still layer; accidents
  harvested while they're still pictures; one cast stays one
  cast across hundreds of pieces because every piece starts
  from pictures, not descriptions (lilypads/niceaunties-20261115
  Q1). Our ratio is inverted: one panel per unit, generated
  once, locked — and the iteration spend happens at *video*
  prices (NIGHT LIST: three full versions; ON AIR U2: eleven
  generation attempts in repair). We spend our 25–30 rolls on
  the expensive layer.
- **Clippie — cast sheet as data.** Per character: stable name,
  a "looks like" note with **permanent traits only** (temporary
  state in the scene note), one locked voice, one secret; an
  explicit off-screen flag; scenes bound to cast entries by
  @mention; and the four-class drift taxonomy as the QC
  checklist, with continuity review approving stills **as a
  sequence** before motion (Clippie §§2, 6.4). We have the
  permanent/temporary split in practice (look blocks vs scene
  prose) and the off-screen flag nowhere; we have no voice in
  the sheet at all; and no E2 record shows a *sequence* review —
  panels are QC'd one at a time, never as a set of six PEAKs +
  sheets read together for relative size, prop ownership, and
  cast consistency before the first video call.

**Section verdict:** the reference system is a competent
*panel* system wearing the name of a *cast* system. Two of the
three legs Cantina names — voice and persona — have no artefact
at all, and the look leg is designed per-episode instead of
per-season.

---

## 2. FIRST-FRAME / LAST-FRAME AUDIT — is SR1 designed image work, or an afterthought?

SR1 (msg 507, after LAST SEAT E1 read as "a 24 trailer"): the
outgoing unit's last frame conditions the next unit's generation
as a strong reference. The E2 record shows **three different
executions** of the same rule, with three different outcomes —
which is itself the finding: SR1 was a principle each room
implemented for itself, not a mechanism in the template.

### 2.1 The three executions

- **Image chain (HOLD ON, ON AIR, NIGHT LIST, LAST SEAT):** the
  outgoing take's actual last frame (NIGHT LIST: harvested at
  frame 228 of the conformed take) rides as image 1; the unit's
  PEAK panel as image 2. HOLD ON's GATE_LOG joint section is
  the honest record: all five joints EYE-COHESIVE — and seam
  MAEs of 58.34 / 3.69 / 48.05 / 40.43 / 64.21, i.e. the image
  chain held *state*, not pixels, exactly as the measured skill
  predicts (a strong conditioner, never a frame source).
- **Resume chain (ONE SHORT, both episodes):** chained units
  fired as `resume_from_snapshot_id` calls — which have **no
  image slot at all**. Continuity rides on an unmeasured tool
  behaviour (see Finding 7). The "strong reference" for U2/U3/
  U4/U6 is a prose restatement ("Continue in the same office,
  same light, same positions: …").
- **Written targets (LAST SEAT only):** each unit's vehicle
  carries a "Last-frame target (J{n})" block — positions, props,
  lamp state, held objects — and the next unit opens by
  restating that state ("Open on the identical table/box/coin-
  row/cat/tally state (J2)"). This is F-22's end-state pin in
  embryo, invented locally by one room. Its joints: J1 PASS,
  J2–J4 CONDITIONAL (nits: cat out of frame, population shift),
  J5 PASS; its ear test passed. The only episode that designed
  its last frames *in writing* is the episode whose joints
  needed the least repair prose.

### 2.2 Where joints actually failed, and why

- **E1 ONE SHORT J1 and J4 — EYE: WORLD INCOHESIVE** (E1
  GATE_LOG, joint eye-cohesion section): J1 "the room
  re-dresses from the shopfront counter to a back-office desk
  (green banker's lamps, noticeboard, a background staffer)";
  J4 swaps the room back and "restores the true Clerk… after
  the U3/U4 drift." Seam MAEs were 1.13 and 1.87 — near-zero,
  "would claim perfect cohesion; the eye check says otherwise."
  Cause, stated in the same log: the build "was fired with the
  pre-507 method (resume chains; chained units have no image
  slot, so no joint was strong-reference conditioned on a
  harvested last frame)." The joint failed because there was no
  image at the joint — only a snapshot handle and a paragraph.
- **E2 ONE SHORT repeated the identical architecture** (its
  REFERENCE_STACK "Generation routes": U2/U3/U4 resume from
  U1/U2/U3; U6 resume from U5) — and this time all five joints
  passed the eye gate. Same mechanism, opposite outcome, no
  variable controlled: that is the definition of a lottery, and
  it means E2's pass is not evidence the method works.
- **ON AIR J4 (U4→U5) — CONDITIONAL, the episode's one
  non-continuous joint:** "UNC's face is the younger variant on
  the U5 side (U5 take1 was anchored on take1's drifted U4
  tail)." The chain faithfully propagated a drifted tail. SR1
  as practised has no drift check on the anchor itself: whatever
  the outgoing take ended on — right or wrong — becomes the
  next unit's constitution.
- **HOLD ON B1 (U1→U2) — the weakest joint (MAE 58.34, grade
  step):** U1's tail had itself drifted from the script — "tail
  drifts from the scripted palm close-up to a couple+fruits
  two-shot; rings read on fingers in the last frame instead of
  on the Courier's palm" — breaking the episode's own
  held-object law at the first joint. U2 "re-establishes the
  ring on the Courier's palm… restored inside U2, not across
  the frame line." The end state existed as scene prose, not as
  a pinned target the take was graded against before it was
  allowed to anchor U2.
- **NIGHT LIST J4/J5 (v1) — world break:** U5's drift (Keeper/
  UNC face merge, clothed goblin invader, two-tier bunks in a
  green dormitory) is recorded in REFIRE_VEHICLES.md as "a world
  break at J4/J5 as well" — discovered at F-9 stage, repaired
  by refire. The joint gate ran; it ran *after* the money.

### 2.3 The afterthought pattern

Three tells that last-frame work is reactive, not designed:
(1) only one of five episodes writes its last-frame targets
down; (2) the harvest point is a convention (frame 228) rather
than a chosen frame — the chain anchors on wherever the take
happened to be at 9.5s, drift included; (3) no vehicle anywhere
states what the *first* frame must be beyond the PEAK panel and
a framing sentence — the first frame is the panel's job, the
last frame is nobody's job, and the joint is where the two
unowned ends meet. The successful others invert this: the
anchor still is designed as the scene's contract (Cantina), and
the written end state is the next unit's opening contract
(Higgsfield, twice, independently — F-22's evidence).

---

## 3. PROMPT-DESIGN AUDIT — the vehicles as actually fired

### 3.1 The named blocks are absent — everywhere

Grep over all five episodes' VEHICLES.md, HOLD ON's
VEHICLES_REPAIR.md, and NIGHT LIST's V3_VEHICLES.md for the E3
template's named fields — `END STATE`, `REFERENCE PRIORITY`,
`OBJECTIVE`, `EYE TASK` — returns **zero files**. Not one
vehicle in the entire E2 production, first pass or repair,
carries an end-state block, a reference-priority block, an
objective/obstacle/tactics field, or an eye-task field. What
exists instead is good prose: end states as sentences inside
action text ("The shot ends pushing in slowly to a held close
frame of the OUT tray…" — ON AIR U2), eye beats as incidental
staging ("her eyes flick once to the glowing red microphone
light" — ON AIR U1; "The Courier turns and looks straight into
the camera for her line" — HOLD ON U4). Prose can be skipped by
a model and cannot be checked by a gate; a field can be both.
The worst offenders are not bad prompts — they are *unstructured*
ones, where the load-bearing instructions are indistinguishable
from colour.

### 3.2 The speech block breaks the network's own convention in all five episodes

T-11 ruled, network-wide: speaker name + "says" + colon + the
line, **no quotation marks** (quoted text is liable to be drawn
on screen and blurs attribution). T-10: the prompt contains only
renderable material, speech isolated at the end, attributed by
name + visible trait + delivery. The E2 record:

- **HOLD ON:** `JUNE says: "Write us married, or noon loses our
  room."` — quotes throughout, merged block at the end.
- **ONE SHORT:** dialogue in single quotes inside action prose,
  distributed through the unit ('Certify twenty-four chairs —
  hall pays by the chair.'), not isolated as a block.
- **NIGHT LIST:** TEXT 3 is a run of escaped quoted lines with
  **no speaker names at all** — `\"You put him back on, Keeper.
  Eleven names—\" \"I want quiet: name off ends arguing.\"` —
  attribution exists only as prose in TEXT 2 ("The woman speaks
  first, fast and angry; the tall man answers flatly…"). The
  model is told an *order*, not who owns which line.
- **ON AIR:** one merged single-quoted block, attribution by
  prose ("The seated man speaks first, then the man in the
  yellow blazer, then the showman shouts through the glass, then
  the older man's voice on the speaker: '…' '…' '…' '…'").
- **LAST SEAT:** `DANCER: "I want this stage open; shall I dance
  again?"` — name + colon, but still quoted.
- **NIGHT LIST v3 (the repair):** improved to `LAURA: "You put
  him back on. Eleven names—"` — names added; quotes kept.

The measured audio behaviour makes this expensive: the
generator synthesises quoted speech verbatim when it works —
and when the block is crowded or attribution is prose-only, the
failure modes are dropped lines, garbled lines, and *invented*
lines (video-api-mastery: with no clear audio instruction the
outcome is a lottery — invented spoken line vs near-silence,
V-02/V-03). The ear-test record is that lottery's results page:
NIGHT LIST v3 opened with an **unscripted** line — "Desk takes
the last bed, eleven names for ten beds. Eleven names. Say it
with me." — that contradicts the premise and contains a
recitation instruction; ON AIR's master dropped the invader's
"Number Four." and the Colonel's condition line outright
(§4, Finding 2).

### 3.3 Load was never counted where it binds

The rooms counted episode totals (the SLATE compliance grid:
80–95 words per episode, all ✓). The binding constraint is
per-unit, and no E2 vehicle prints its unit's word/speaker
count as a checked field — the counts that do appear (HOLD ON's
"(25w)", LAST SEAT's "(21w, 3 lines)") are descriptive, and
HOLD ON U1 still shipped 25 words / 3 speakers and U2 24 words
/ 4 speech turns including a unison invader line. ON AIR U2 —
38 words, 4 speakers — was fired as designed, failed the ear
test on exactly the lines that starved, and consumed six repair
rounds (Findings 3). T-9's ≤2.5 words/second existed on paper;
nobody's checklist divided the unit by it.

### 3.4 Declared law breached inside the vehicle text

NIGHT LIST's bible-level production declaration: the board and
book are generated BLANK; all handwriting is post. Its own U5
vehicle asks the generator for "a small tag **reading HELD** on
its rail"; U6's vehicle has the Keeper write his name on the
board in-take; U1's board carries the roster. The PIL plates
existed — as *backup* ("inserts ONLY if a take's own rendering
falls short — decided at QC"). The plan, in other words, was to
let the generator attempt the text first and composite over it
if it failed: the declared law run in reverse. HOLD ON shows
the same pattern from the other side: signage declared blank/
post, takes delivered with generator-invented "ROOMS" signage
and an unscripted "FRUIT COUPLE" sign, logged as flaws and kept.

### 3.5 What the vehicles do well

Duration + aspect stated in text on every call (all five
episodes — the skill's one non-negotiable, honoured). Anti-text
lines present. Look blocks verbatim. Dialogue-last as a house
habit in four of five. HOLD ON's stack-level held-object law
and NIGHT LIST's joint table are genuinely designed continuity
documents. The audit's complaint is not craft; it is that the
craft lives in prose habits that vary by room, instead of in
fields that survive a room change.

---

## 4. DEVIL'S-ADVOCATE FINDINGS — the slipping points, ranked by damage

Each finding: the evidence, what the successful others do
instead, and a fix written to paste into the production brief
template. "Damage" is measured in shipped failures, repair
spend, and failure classes our own gates cannot see.

---

**F1. The voice leg of the character stack does not exist — so
our worst failure class has no instrument.**
*Evidence:* all five REFERENCE_STACKs contain zero voice data
(grep-verified); no character in E2 has a structured voice spec,
an enrollment sample, or a pinned engine; the §3 voice-QC stack
(ASR diff, diarization, embedding voice-match) has zero mentions
in any E2 GATE_LOG; every ear-test verdict carries the scope
note that voice/character match "cannot be judged from an ASR
transcript and was not assessed." The user's msg-581 verdict on
HOLD ON E2 — "many voices did not match character" — names a
failure our pipeline is structurally unable to detect, let alone
prevent.
*What they do:* Cantina and Clippie both treat voice as
identity — one locked voice per character, spec'd as a
structured text recipe before episode 1, kept across every line
and episode; a familiar silhouette with a different voice "can
feel like a new character" (Clippie §3; Cantina §5.2; our own
T-6/F-15 say the same and were not implemented).
*Fix (paste into the brief template):*
> **VOICE (mandatory, per speaking character, before episode 1):**
> the CHAR card carries the §3 VOICE block — age range · accent/
> region · pitch · pace · texture · trait · breaks · enrollment
> sample (file path) · engine (pinned). The block is pasted
> VERBATIM into every vehicle in which the character speaks. A
> vehicle for a speaking character with no VOICE block on the
> card DOES NOT FIRE. Per-take QC logs one line per speaker —
> `VOICE CHECK: <char> — match / flag (listened) / re-fire` —
> human listen until embedding tooling lands; "not assessed" is
> not a permitted QC outcome.

**F2. Speech is fed as one merged quoted block with prose-only
attribution — the format most likely to drop, garble, or invent
lines.**
*Evidence:* §3.2 — all five episodes quote their dialogue; NIGHT
LIST's speech block carries no speaker names at all; its v3
master opened with an unscripted line contradicting the premise
("Desk takes the last bed… Say it with me."), dropped three
scripted lines (the opener, the Keeper's ruling, the invader's
only line) and garbled two more, including the payoff's verdict
words ("Drive-drive bed wanted, nothing carried") —
EAR_TEST_V3_VERDICT.md. ON AIR's master dropped the invader's
"Number Four." and the Colonel's condition line, the two
half-lines its payoff causally depends on — EAR_TEST_VERDICT.md
Findings 1–2. The video-api skill measures why: quoted speech is
synthesised verbatim when the block is clean; crowded or
unattributed blocks fall into the invented-speech lottery.
*What they do:* the factories' atomic unit is one speaker, one
line, one scene; dialogue is written in the model's native
speech format — speaker + voice + colon, **no quotation marks**,
because quotes leak on-screen text and merged blocks blur
ownership (CENSUS §6 #2/#6; Clippie §1; our T-10/T-11 ruled the
same and were not carried into the vehicle format).
*Fix:*
> **SPEECH BLOCK (the only permitted form):** the vehicle ends
> with the speech block, isolated, one line per entry, in the
> form `NAME (visible trait, delivery): the line` — colon form,
> NO quotation marks anywhere in the prompt. Attribution lives
> in the block, never only in prose. One speaker per entry;
> unison lines are forbidden (two speakers = two entries or a
> script change). Nothing speakable appears anywhere else in
> the prompt.

**F3. Units are written past one generation's capacity, and the
bill is paid in repair rounds at master prices.**
*Evidence:* ON AIR U2 (38 words, 4 speakers, one 10s unit) —
ear-test FAIL localised to U2; repair rounds 1–6, eleven
generation attempts, closed UNREPAIRED on the span law
(GATE_LOG repair sections; TASTE F-25 + round-6 corollary).
NIGHT LIST: 43 refire mentions in its GATE_LOG, three complete
versions, ear-test FAIL on v3. HOLD ON: F-9 repair rounds
through round 3, then user rejection (msg 579). The rooms
audited episode word totals (80–95 ✓) while the binding
constraint — per-unit load — was never a printed, checked field
on any vehicle (§3.3).
*What they do:* Clippie's architecture simply refuses the unit
size — one line = one scene = one clip of 4–7s, 8–14 words
(Clippie §§1–2); the census's whole field runs the same economy
(CENSUS §6 #2). Nobody in the field discovers load at the
master; the format makes overload unrepresentable.
*Fix:*
> **UNIT LOAD (printed at the head of every vehicle, counted
> before firing):** `LOAD: <n> words / <n> speakers (cap ~30 /
> ≤2 per generation)`. A unit over cap returns to the script
> pass — split (at most one spoken half, per the round-6
> corollary) or trimmed — and is never fired "to see." Pass 4
> signs the load line for all six units before the first call.

**F4. Drift is chained, not corrected: a drifted tail becomes
the next unit's constitution.**
*Evidence:* ON AIR U5 "anchored on take1's drifted U4 tail" →
UNC's younger face variant across J4, the episode's one
CONDITIONAL joint. HOLD ON: the Peach drifts toward a "crowned
pink-princess design" in U1's tail; U2's log accepts the
resulting mascot-suit redesign as "consistent with U1's tail" —
the drift ratified as the new design — and by U4 she has
"drifted further toward a pink princess doll," with gibberish
lettering on her sash (GATE_LOG U1/U2/U4 QC). NIGHT LIST v1 U5:
identity-grade drift (Keeper/UNC face merge, clothed goblin
invader, bunk-bed world) found at F-9 and repaired by refire
with scattered negations in trait lines ("NOT cropped, NOT
silver," "no clothes, no ears") — T-12's named trap: negation
introduces the concept it bans.
*What they do:* Clippie's taxonomy gives each drift class a
first fix *at the reference* (identity → check cast/name/
reference; wardrobe → shorten the note to defining colours and
shapes); Cantina gates the still, not the render; F-24 (from
Higgsfield) adjudicates known defects in words inside the
prompt's priority block — positively stated — instead of
re-generating around them.
*Fix:*
> **TAIL-DRIFT RULE:** a take whose last frame fails the drift
> checklist (§5F) may NOT serve as the next unit's chain anchor.
> The next unit re-anchors from the gated CHAR/PEAK stack, the
> break is logged in GATE_LOG as a designed re-anchor (ONE
> SHORT's U5 precedent), and the drifted tail is never quoted
> as a state source. Known reference defects are overridden in
> the REFERENCE PRIORITY block as positive statements ("the
> Keeper's hair is dark, wavy, greying at the temples") — bare
> negations ("NOT silver") are not a permitted override form.

**F5. No vehicle adjudicates its references — when the images
disagree, the model decides, and the end anchor is the weakest
element it has.**
*Evidence:* zero REFERENCE PRIORITY blocks in the entire E2
record (grep-verified, §3.1). The two-image stacks routinely
pair images that disagree by design (the outgoing frame = where
we are; the PEAK = where the unit must arrive). The measured
skill says what happens undecided: the model leans on the
stronger/first ref and even overrides the second ref's drift
toward it (V-03); the destination image is "the least exact in
the chain" (end-anchor MAE 51.85 vs start 43.17). NIGHT LIST v2
paid for it directly: PEAK-U6 — a panel depicting the unit's
*end* state, Elias already on the bed — used as an anchor
"conditioned the doubling in both v2 U6 rolls" (DECISION_LOG
R3-7), diagnosed only after two wasted generations.
*What they do:* Higgsfield's priority block, from two
independent sources: name which reference owns identity, which
owns geometry, which owns wardrobe; adjudicate conflicts in the
prompt, where it is cheap, instead of at the gate, where it is
not (F-24).
*Fix:*
> **REFERENCE PRIORITY (three lines, every vehicle):**
> `IDENTITY: <panel> · GEOMETRY: <panel> · WARDROBE: <panel>`
> followed by any known-defect overrides (positive statements).
> A panel depicting the unit's END state is labelled
> DESTINATION in the stack and may never be image 1.

**F6. The end state is prose, not a pin — tails land where they
land, and the miss is found at QC, not prevented.**
*Evidence:* only LAST SEAT wrote last-frame targets (§2.1) —
and it is the episode with the cleanest joint record and a
passed ear test. Elsewhere: HOLD ON U1's tail missed its
scripted palm close-up and put the ring on fingers instead of
the Courier's palm, breaking the episode's own held-object law
at the first joint; the state was "restored inside U2, not
across the frame line" (GATE_LOG B1). ON AIR's end states are
sentences inside action prose, quoted by nobody.
*What they do:* the written END STATE is the continuity device
in two independent Higgsfield sources — positions, eyelines,
props, wardrobe as the last frame must hold them, quoted
verbatim at the head of the next unit's prompt (F-22). It is
the prompt-text twin of SR1, and SR1 without it is an image
asked to carry a contract it cannot read.
*Fix:*
> **END STATE (mandatory block, every vehicle):** positions ·
> eyelines · props (with held-object state) · wardrobe, as the
> unit's last frame must hold them. The next unit's vehicle
> OPENS by quoting the previous END STATE verbatim, ahead of
> its own scene sentences. GATE_LOG's joint check verifies the
> quote against the outgoing take's actual last frame and names
> the frame file; a mismatch is a joint defect, not a nit.

**F7. A production chain load-bears on an unmeasured tool
behaviour our own skill fences off.**
*Evidence:* video-api-mastery lists `resume_from_snapshot_id`
chaining as UNTESTED #1 — "whether context, character, or scene
actually carries is UNKNOWN… do not build workflow on these" —
and specifies the exact one-call test, which has never been
run. ONE SHORT built its chains on resume calls in both
episodes (REFERENCE_STACK "Generation routes"); E1's result was
J1/J4 WORLD INCOHESIVE with mid-chain Clerk drift at near-zero
seam MAE; E2's identical architecture passed all five eye
joints. An unmeasured behaviour produced both outcomes.
*What they do:* the field's continuity is artefact-based —
locked references re-presented every scene (Clippie cast
library; Cantina base performances as reference substrate) —
never a session handle whose carry is assumed.
*Fix:*
> **CHAINING RULE:** until the video-api lab's specified resume
> test is run and its result recorded in the lab log, no E3
> chain uses snapshot resume as a continuity mechanism. Chains
> carry images: outgoing last frame (image 1) + gated PEAK
> (image 2), per the HOLD ON / LAST SEAT execution. The lab
> test is a standing one-call experiment, fired under the next
> available budget, and the skill's UNTESTED entry is updated
> with the measurement either way.

**F8. Panels are gated one at a time, never as a sequence — and
the iteration spend sits on the expensive layer.**
*Evidence:* no E2 stack or gate log records a sequence review
of an episode's panels as a set; QC is per-panel (thorough in
ONE SHORT, thinner elsewhere). Composite PEAKs imported story
errors into the contract still (X marks a unit early; a scalp
X) that were noted and routed around rather than regenerated
(§1.2). Meanwhile the roll count lands on video: NIGHT LIST
three versions, ON AIR U2 eleven attempts, HOLD ON two repair
builds.
*What they do:* Clippie's continuity review approves stills
**as a sequence** — silhouette, clothing, props, relative size,
who holds what — before any motion spend; niceaunties spends
25–30 prompts per piece at the still layer, where a reroll
costs seconds, and harvests accidents there (Clippie §2;
niceaunties Q1).
*Fix:*
> **SEQUENCE GATE (before the first video call):** all CHAR
> sheets + all six PEAK panels on one contact sheet, read as a
> set — cast consistency, relative size, prop ownership,
> world/palette continuity, story-state correctness per unit —
> and signed in GATE_LOG. A panel whose error touches a later
> unit's story state is REGENERATED, not noted. Still-layer
> rerolls are uncapped; video refires are the capped currency.

**F9. The persona leg is missing: characters are looks with
lines, so "said and did nothing" is designed in at the card.**
*Evidence:* zero OBJECTIVE/OBSTACLE/TACTICS fields and zero
persona blocks in the E2 record (§3.1); acting direction exists
only as incidental prose. The user-named HOLD ON failure —
Peach & Lime "said and did nothing" (msg 579) — is a card-stage
rent failure (F-19): the invaders were given a unison line and
a bouquet, no want with a consequence; two repair builds then
chased a card problem as a performance problem, the exact
misdiagnosis Cantina §5.1 warns against ("several of our E2 ear
failures were card-level problems chased as performance
fixes"). NIGHT LIST's Blob Prince repeats the shape: scripted
one line, which then never even reached the master audio.
*What they do:* Cantina's persona leg — Identity / Personality
/ Backstory on a versioned card, the persona **rewritten per
scene, never pasted**; acting written as objective (a verb aimed
at the partner) + obstacle + tactics that change mid-scene,
with an explicit eye task on close takes (Acting Director via
Higgsfield; F-23/F-27).
*Fix:*
> **CARD + VEHICLE FIELDS:** the CHAR card carries PERSONA
> (Identity / Personality / Backstory) and a RENT line (force /
> block / price — a character with none does not speak). Every
> vehicle carries, per speaking character, the per-scene
> PERSONA INSTANCE (the card's persona rewritten for this
> scene) and `OBJECTIVE: <verb at partner> · OBSTACLE: <what
> resists> · TACTICS: <move 1 → move 2>`; every close take
> carries `EYE TASK: <what the eyes do, at what, how long>`.
> Emotion adjectives as acting direction are a located
> objection at vehicle review.

**F10. Blank-surface law is declared in the bible and breached
in the vehicle — generator text is attempted first, plates are
the fallback.**
*Evidence:* §3.4 — NIGHT LIST's U5 vehicle requests a tag
"reading HELD"; U6 stages in-take name-writing; its stack
records the PIL plates as inserts "ONLY if a take's own
rendering falls short." HOLD ON's takes arrived with invented
"ROOMS" and "FRUIT COUPLE" signage, logged as flaws, kept.
*What they do:* the field treats text as a post layer by
construction — Clippie's captions are generated from the synced
speech in the editor, checked against the words actually
spoken; the census's winners keep in-image text to the still
layer, where it is composed, not rolled (CENSUS §6 #7).
*Fix:*
> **TEXT RULE:** a vehicle may not contain the words of any
> in-world text (signs, tags, board writing, documents). Such
> surfaces are described as blank/illegible texture, and the
> PIL plate is the DEFAULT carrier, composited at assembly —
> never a fallback for a failed generation. A take with legible
> invented text on a declared-blank surface is a reject class,
> not a nit.

**F11. The drift taxonomy sits in our research, unadopted —
so every room re-diagnoses the same four failures from
scratch.**
*Evidence:* invader identity drift (HOLD ON Peach → princess;
NIGHT LIST blob → goblin), face-variant drift (ON AIR UNC;
NIGHT LIST Keeper), world drift (NIGHT LIST bunks; E1 ONE SHORT
room swap), prop/state drift (HOLD ON ring; ONE SHORT panel
X's) — the same four classes across five episodes, logged in
five different prose styles, with no class → first-fix mapping
ever applied (§1.1).
*What they do:* Clippie publishes the taxonomy *as* the QC
checklist: identity drift → check cast/name/reference; wardrobe
drift → shorten the appearance note to defining colours and
shapes; prop drift → state the owner and position; motion
drift → simplify the action, check start and end frames —
"motion does not repair an inconsistent starting image"
(Clippie §2).
*Fix:*
> **DRIFT CHECKLIST (printed in the GATE_LOG template):** every
> take's QC classifies drift as IDENTITY / WARDROBE / PROP /
> MOTION (or NONE), and a drift note is incomplete without its
> class and the class's first fix attempted. Cross-episode, the
> class counts are the production system's drift ledger.

**F12. Hear-before-it-moves ran at half strength: the pictures
were heard before they moved; the lines were not.**
*Evidence:* the still side of the gate genuinely ran (panels
eye-QC'd pre-firing, all stacks). The voice side has no E2
record at all: no neutral-voice read of a locked script, no
banter draft on the conversation-heavy episodes, no
hear-before-it-moves tick anywhere — and the failure it exists
to catch is the one the user caught at delivery: HOLD ON's
twined lines ("'Believed'? I want couples written — believed
isn't") that matched ASR and still read as nonsense spoken
(F-9 repair verdict quotes them passing every paper question).
*What they do:* the gate is the centre of every working
pipeline in the census — picture + **performed voice line**
reviewed together before animation spend (Clippie §2 step 4;
CENSUS §6 #4); Cantina mines the banter first and scripts what
survives being *said* (§5.4). Our F-26 promotes the same check
to a script-stage gate.
*Fix:*
> **PASS 3.5 (blocking):** before any vehicle is written, the
> locked script is read aloud cold, in order, by a voice that
> did not write it; the reader is named in DECISION_LOG and
> every stumble is logged and returned to Pass 3. Conversation-
> heavy episodes additionally record the banter draft's
> existence at Pass 3 (F-27). No vehicle writing begins on an
> unsigned Pass 3.5.

---

## 5. THE REVISED REFERENCE + PROMPT DESIGN PROTOCOL — standing procedure for E3

*One section, written to be adopted as law. It assumes E3 law
(TASTE §8) and adds the template machinery E2 lacked. Where it
repeats an F-item, it gives the item its field, its checkbox,
and its owner.*

### A. The cast sheet is data (built at bible stage, before the room opens)

Per character, a repo-versioned CHAR card — the character is
the asset; episodes are performances of it:

1. **LOOK block** — permanent traits only (defining colours and
   shapes); temporary state never lives here.
2. **VOICE block** — the §3 structured spec (age · accent ·
   pitch · pace · texture · trait · breaks) + enrollment sample
   file path + pinned engine. Written before the character's
   first episode; any edit is a casting change (logged; prior
   takes re-checked).
3. **PERSONA block** — Identity / Personality / Backstory +
   one secret + a RENT line (force / block / price on the
   protagonist's decision; a character with none does not
   speak).
4. **OFF-SCREEN flag** for characters discussed but never shown.
5. **STATE LEDGER** (per episode, not per card): who holds
   what, who knows what, what was promised — temporary state
   lives here and in scene notes, never in the LOOK block.

### B. Panel design (the still is the contract)

1. CHAR sheets (hero + face) are generated **at master aspect**
   — never padded or cropped from another aspect.
2. One PEAK panel per unit, designed as the unit's contract
   still: wardrobe, setting, camera, lighting, finish are
   decided *in the still*; the video prompt's remaining job is
   action + dialogue.
3. Every panel is **read back before use** (the ref-poisoning
   rule) and logged in the stack with md5 + status.
4. A panel depicting a unit's END state is labelled
   **DESTINATION** and may never be image 1.
5. **SEQUENCE GATE:** all sheets + all six PEAKs on one contact
   sheet, read as a set (cast consistency, relative size, prop
   ownership, world continuity, per-unit story-state
   correctness), signed in GATE_LOG **before the first video
   call**. Story-state errors in a panel are regenerated, not
   noted. Still-layer rerolls are uncapped.

### C. First-frame / last-frame design (the chain is a contract at both ends)

1. Every vehicle carries an **END STATE block**: positions ·
   eyelines · props (held-object state named) · wardrobe, as
   the unit's last frame must hold them.
2. The next vehicle **opens by quoting the previous END STATE
   verbatim**, ahead of its own scene sentences.
3. The chain anchor is the outgoing take's **actual last
   frame**, harvested after conform, carried as image 1; the
   gated PEAK is image 2.
4. **Tail-drift rule:** a take whose last frame fails the drift
   checklist (F) does not anchor the next unit; re-anchor from
   the gated stack and log the designed break.
5. Snapshot/resume chaining is **not** a continuity mechanism
   until the video-api lab's specified test is run and recorded.

### D. Reference priority (adjudicate in the prompt, not at the gate)

Every vehicle carries three lines —
`IDENTITY: <panel> · GEOMETRY: <panel> · WARDROBE: <panel>` —
plus known-defect overrides stated **positively** (presence,
not absence). A conflict with no owner named in the block is a
vehicle-review objection.

### E. Prompt assembly (per vehicle, in this order, nothing else)

1. Duration + aspect line.
2. The quoted END STATE of the previous unit (U1: the
   opening-state block).
3. REFERENCE PRIORITY block.
4. LOOK blocks verbatim from the cards; VOICE spec verbatim for
   each speaker.
5. Per-scene PERSONA INSTANCE (the card's persona rewritten for
   this scene — never pasted) + OBJECTIVE / OBSTACLE / TACTICS
   per speaking character + EYE TASK on every close take.
6. Action/scene sentences — renderable content only: no staging
   vocabulary, no gate language, no in-world text words;
   silence and non-speech described positively.
7. **SPEECH BLOCK, last, isolated:** one speaker per entry,
   `NAME (visible trait, delivery): line` — colon form, **no
   quotation marks anywhere in the prompt**; no unison entries;
   nothing speakable anywhere else in the prompt.
8. **UNIT LOAD line** at the vehicle's head: words / speakers
   counted against the ~30-word / ≤2-speaker cap before firing.

### F. Gates around the spend

- **Pre-flight (blocking, before the first video call):**
  Pass 3.5 hear-before-it-moves signed (reader named, stumbles
  logged); SEQUENCE GATE signed; per-unit load audit signed.
- **Per take:** ASR-vs-script diff; diarization; VOICE CHECK
  line per speaker (match / flag-listened / re-fire — "not
  assessed" is not an outcome); **DRIFT CHECKLIST** — IDENTITY /
  WARDROBE / PROP / MOTION, each note carrying its class and
  the class's first fix; tail-frame drift check before the take
  may anchor the next unit.
- **Per joint:** the END STATE quote verified against the
  outgoing take's actual last frame (frame file named in
  GATE_LOG); eye verdict logged; seam MAE recorded as
  calibration only.
- **Unchanged:** the ear test on the finished master (F-13) —
  this protocol exists so the ear test stops being the first
  place the truth is heard.

---

*End of AUDIT.md. Sources: the E2 production record as cited
throughout; TASTE_GUIDE_2026-11-17.md §§1–8;
research_notes/slerm-their-shows-20261118/ (THE_SAUCE,
RETOOL_PLAN, SLERM_VIDEO_METHOD); Cantina product_report §5;
Clippie report §§1–6; niceaunties lilypad study Q1;
custom-skills/video-api-mastery/SKILL.md.*
