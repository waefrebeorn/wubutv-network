# E3 PRODUCTION BRIEF — ONE SHORT, Part 1 (filled template v2)

*Filled copy of `new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md` v2
(2026-11-18). Companion files in this episode dir: SCRIPT.md
(locked), GATE_LOG.md (room gates), DECISION_LOG.md. Production
opens `work/GATE_LOG.md` using template §5 sections verbatim.*

## §0 — Episode header

```
SHOW: ONE SHORT            EPISODE / PART: E3 Part 1 of the count-along serial
TITLE (funnel grammar): ONE SHORT — Part 1: Thirty-One Umbrellas — AND ONE BY THE DOOR
CONTINUITY_OWNER: WuBu (parent showrunner) — owns every joint sign-off J1–J5 and the §3 gates
GENERATOR: model house video generator (media.generate_video)  version current house build  mode native-audio 10s units, 16:9
MODEL_SYNTAX: veo-colon-noquotes
VOICE_ROUTE (per show, mandatory, one of):
  NATIVE_TEXT_ONLY
  WAIVER: the house generator synthesizes native audio and exposes no TTS,
  voice-pin, or lip-sync route; no other route exists in the current toolset.
  Mitigation carried instead: VOICE_SPEC_TEXT pasted verbatim before the
  dialogue in every unit prompt (drift-reducer, NOT a lock — the word
  "locked" is never used of these voices); VOICE_ENROL anchors cut from the
  E2 master for the Clerk and the Counter (§1) and the §5.2 three-instrument
  voice check + ear test run at production on every speaking unit.
CAST_LOG (reproducibility record, completed at delivery):
  model+version ____ · reference/element IDs bound ____ ·
  voice route + IDs NATIVE_TEXT_ONLY (waiver above) · settings ____ · seed (if exposed) ____
```

*Cast note: UNC does not appear in this show (bible §3 kills the
satellite cast; UNC is network property, not this show's). The
hoodie wordmark law therefore does not arise in-frame; the
network corner bug "~ WuBu ~" is an assembly post element.*

---

## §1 — Cast cards

```
CHARACTER: THE CLERK            CARD_VERSION: OS-CLERK v2 (E3 revision of the E1/E2 card)
OFF_SCREEN: N

LOOK (bound, not described):
  LOOK_PACK: front_neutral E2_one-short/panels/PNL-CHAR-CLERK-sheet-16x9.png (sheet view 1)
             three_quarter E2_one-short/panels/PNL-CHAR-CLERK-sheet-16x9.png (sheet view 2)
             profile PRODUCTION STEP 1: generate supplement sheet E3_one-short/panels/PNL-CHAR-CLERK-supp-16x9.png
             full_body E2_one-short/panels/PNL-CHAR-CLERK-sheet-16x9.png (sheet view 3)
             close_up PRODUCTION STEP 1: supplement sheet (as above)
             back_or_silhouette PRODUCTION STEP 1: supplement sheet (as above)
             expression_set[3–5 named]: flat-verdict (on sheet) · page-reading (on sheet) ·
               price-naming (supplement) · book-reveal (supplement) · freeze-flat (supplement)
             (units may not fire until the supplement sheet is generated, eye-QC'd and
              locked at the Sequence Gate — the supplement is a still-layer reroll, uncapped)
  CANONICAL_FACE_REF: file E2_one-short/panels/PNL-CHAR-CLERK-sheet-16x9.png
             sha256 ec43c25a3311e6717ce84d189b4ed10237b9226e5de475d83bd25cc9278267c1
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "a woman in her fifties with a sharp black bob and round spectacles, bone-white blouse under an ink-black vest, cobalt-blue ink staining her fingertips"
  WARDROBE_STATES: STATE OS-CLERK-STD = ref still E2_one-short/panels/PNL-CHAR-CLERK-sheet-16x9.png
             (bone blouse, ink vest, spectacles, cobalt fingertips — the only state this part)

VOICE (route per §0):
  VOICE_SPEC_TEXT (fallback / drift-reducer only — NOT a lock):
    age ~55 · gender female · timbre dry, low, unhurried · pace measured, complete sentences ·
    accent neutral bureau · trait never raises her voice; prices and verdicts land flat ·
    breaks never
  VOICE_ENROL: file E3_one-short/work/voice_enrol/CLERK_enrol.wav · seconds ~2.7
    (production step 0: cut from E2 master masters/oneshort_E2_master.mp4,
     the Clerk's want line at 10.36–13.08s per the E2 ear-test transcript)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: believes customers miscount by one → she reads every
    claim as a number to be tested, never as a fact to be answered
  TRAIT → OBSERVABLE_BEHAVIOUR: the book is hers → she charges for opening it, in
    concessions, and the charge is collected in picture, never announced
  EXAMPLE_LINE (a line only this character would say): "Receipts say what was paid, not what came."
  NEVER_DOES: never looks at the shelf · never raises her voice
  NEVER_SAYS: never says where the one goes · never apologizes for the count
  SECRET: she has never once checked the shelf herself
  RENT: force — she can close the book on the true number and end any claim /
        block — she can refuse to open the book /
        price — a recount costs the customer one kept item, collected in picture
  BACKSTORY_ACTIVE_FACT (the one fact THIS episode uses): every page of her book
    ends one short; the book has never closed even in her tenure — until this count

PERFORMANCE:
  MOTION_SIGNATURE (3–5 observable entries, verbatim across units):
    stillness lead — she does not come to the work; the work comes to the counter ·
    fingertip tap on the book when a price is named ·
    hand flat on paper to pin a claim ·
    writes in the book without looking down ·
    tempo: slowest in the room

STATE (per episode):
  STATE_OPEN:  wardrobe_state_id OS-CLERK-STD · condition fresh page, book open ·
               props_held pen · knowledge believes the customer miscounted ·
               emotion flat · relationship_delta none yet
  STATE_CLOSE: wardrobe_state_id OS-CLERK-STD · condition book closed even on thirty,
               certificate stamped, deposit envelope inside the book as its marker ·
               props_held none · knowledge unchanged — she still believes the customer
               miscounted, and the audience knows she is wrong ·
               emotion flat · relationship_delta the Planner's claim is dead;
               the office owes her nothing
  (STATE_CLOSE of Part 1 = STATE_OPEN of Part 2, or a STATE_CHANGE_NOTE
   says when/why the change begins on screen: STATE_CHANGE_NOTE — none;
   Part 2 opens on this state.)
```

```
CHARACTER: THE COUNTER            CARD_VERSION: OS-COUNTER v2 (E3 revision of the E1/E2 card)
OFF_SCREEN: N

LOOK (bound, not described):
  LOOK_PACK: front_neutral E2_one-short/panels/PNL-CHAR-SNH-sheet-16x9.png (sheet view 1)
             three_quarter E2_one-short/panels/PNL-CHAR-SNH-sheet-16x9.png (sheet view 2)
             profile PRODUCTION STEP 1: generate supplement sheet E3_one-short/panels/PNL-CHAR-COUNTER-supp-16x9.png
             full_body E2_one-short/panels/PNL-CHAR-SNH-sheet-16x9.png (sheet view 3)
             close_up PRODUCTION STEP 1: supplement sheet (as above)
             back_or_silhouette PRODUCTION STEP 1: supplement sheet (as above)
             expression_set[3–5 named]: counting-flat (on sheet) · hand-stopped (supplement) ·
               shelf-count (supplement) · freeze-look (supplement) · denial-flat (on sheet)
             (units may not fire until the supplement sheet is generated, eye-QC'd and
              locked at the Sequence Gate)
  CANONICAL_FACE_REF: file E2_one-short/panels/PNL-CHAR-SNH-sheet-16x9.png
             sha256 12075de7815ff38250061f0008551f5bf950800189da8482600bc50ca0441f38
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "a gaunt man with close-cropped grey hair and deep-set eyes, an ink-dark work shirt, a brass tally counter on a chain at his chest with a small blank tally card beside it"
  WARDROBE_STATES: STATE OS-COUNTER-STD = ref still E2_one-short/panels/PNL-CHAR-SNH-sheet-16x9.png
             (ink work shirt, tally counter on chain, streak card — the only state this part)

VOICE (route per §0):
  VOICE_SPEC_TEXT (fallback / drift-reducer only — NOT a lock):
    age ~60 · gender male · timbre flat, dry, low · pace slow, numbers evenly spaced ·
    accent neutral · trait fragments and counting chains; verdicts in five words or fewer ·
    breaks never — he stops mid-count instead of erring
  VOICE_ENROL: file E3_one-short/work/voice_enrol/COUNTER_enrol.wav · seconds ~2.1
    (production step 0: cut from E2 master masters/oneshort_E2_master.mp4,
     the Counter's want line at 13.66–15.78s per the E2 ear-test transcript)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: professional shame (the back-step) → he recounts any
    pile his hand doubts, without being asked, and says nothing about why
  TRAIT → OBSERVABLE_BEHAVIOUR: notices patterns in his hands before his words →
    his hand stops over a light pile a full unit before he names anything
  EXAMPLE_LINE (a line only this character would say): "Six, twelve, eighteen — wobbly again."
  NEVER_DOES: never looks at the shelf (he counts it in U6 without looking at it —
    eyes travel it the way they travel a pile, and the distinction is the performance) ·
    never certifies a number he did not count
  NEVER_SAYS: never says where the one goes · never says a subtotal he has not reached
  SECRET: he once stepped a count backward — 1003 to 1002 — and hid it; the streak began there
  RENT: force — the count itself: his number is the only fact the office trades on /
        block — he can refuse a recount by stilling his hands /
        price — a recount costs the customer one kept item, and he collects it
  BACKSTORY_ACTIVE_FACT (the one fact THIS episode uses): his streak stands at 41
    board-mismatches; he wants one even count before the streak reaches him

PERFORMANCE:
  MOTION_SIGNATURE (3–5 observable entries, verbatim across units):
    counts in batches, aloud, evenly ·
    hand stops mid-air when a pile runs light ·
    tally counter clicked once per batch, never fiddled ·
    turns his whole body, not his head, to count something new ·
    tempo: metronome

STATE (per episode):
  STATE_OPEN:  wardrobe_state_id OS-COUNTER-STD · condition at the crates, tally in hand ·
               props_held brass tally counter · knowledge suspects a pile before the board does ·
               emotion flat · relationship_delta none yet · streak card reads 41 (post plate)
  STATE_CLOSE: wardrobe_state_id OS-COUNTER-STD · condition has counted the shelf — one
               item — and said nothing · props_held brass tally counter ·
               knowledge he knows what is on the shelf; the room does not ·
               emotion flat · relationship_delta one part closer to saying it to a
               customer's face (his serial arc) · streak card reads 42 (post plate)
  (STATE_CLOSE of Part 1 = STATE_OPEN of Part 2.)
```

```
CHARACTER: THE PLANNER (the Peach Planner — this part's customer; the invasion)
            CARD_VERSION: OS-PEACH v1 (NEW character, built for E3)
OFF_SCREEN: N

LOOK (bound, not described):
  LOOK_PACK: front_neutral E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 1) — TO GENERATE, production step 1
             three_quarter E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 2) — TO GENERATE
             profile E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 4) — TO GENERATE
             full_body E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 3) — TO GENERATE
             close_up E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 5) — TO GENERATE
             back_or_silhouette E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png (sheet view 6) — TO GENERATE
             expression_set[3–5 named]: demand-maximum · accusation-maximum ·
               stake-placed · verdict-struck · door-quiet
             (the sheet does not exist yet: this brief may not fire until it is
              generated, eye-QC'd, locked at the Sequence Gate, and the sha256
              below is entered — still-layer rerolls uncapped until it locks)
  CANONICAL_FACE_REF: file E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png
             sha256 1af522157bde7c18bdd33ff42a41831d326b90bec2cca929c86bd5e07e44eb91
             (entered at production step 1, 2026-11-18 — sheet generated, eye-QC'd,
              locked; see work/GATE_LOG.md §3 sign-offs)
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "a woman in her thirties in a peach-satin trouser suit with a giant plain foam peach fascinator, glossy dark hair in a high ponytail, wide maximum-expression eyes, clutching a blank cream folder flat against her chest"
  WARDROBE_STATES: STATE OS-PEACH-WED = ref still E3_one-short/panels/PNL-CHAR-PEACH-sheet-16x9.png
             (peach-satin suit, foam peach fascinator, blank folder — the only state this part)

VOICE (route per §0):
  VOICE_SPEC_TEXT (fallback / drift-reducer only — NOT a lock):
    age ~32 · gender female · timbre bright, carrying, theatrical · pace fast, sentences tumble ·
    accent fruit-soap melodrama register, everything at full expression ·
    trait states wants as deadlines · breaks never — she escalates, she does not crack
  VOICE_ENROL: file none — new character, no enrollment exists ·
    seconds 0   (the §5.2 voice check ceiling for her this part is PASS-EAR-ONLY;
    her enrollment is cut from Part 1's locked master and banked for Part 2)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: counts claims, not objects → she reads the receipt as
    the truth and the finished pile as an insult
  TRAIT → OBSERVABLE_BEHAVIOUR: deadline panic worn as command → every line she
    speaks carries the noon clock, including her quietest one
  EXAMPLE_LINE (a line only this character would say): "Thirty-one umbrellas. Count them before noon."
  NEVER_DOES: never counts the load herself · never lowers her voice or her chin (until U6)
  NEVER_SAYS: never admits her own umbrella was inside her number · never says thirty
  SECRET: her thirty-one includes the umbrella she carried in her own hand
  RENT: force — her deposit plus the noon deadline can force a recount on the spot /
        block — the count cannot close without her signature /
        price — the recount's price (deposit kept, one item kept) is charged to
        whoever demanded it and was wrong — her
  BACKSTORY_ACTIVE_FACT (the one fact THIS episode uses): the wedding is at noon and
    her fee is paid per certified umbrella — thirty-one is money, not vanity

PERFORMANCE:
  MOTION_SIGNATURE (3–5 observable entries, verbatim across units):
    enters mid-stride; never arrives standing still ·
    thrusts objects (receipt, envelope) forward at chest height when she stakes them ·
    points at the board, never at the pile ·
    catches falling objects against her hip without breaking a line ·
    tempo: double the office's

STATE (per episode):
  STATE_OPEN:  wardrobe_state_id OS-PEACH-WED · condition mid-stride entering, claim
               of 31 in her mouth · props_held blank folder; deposit envelope in hand;
               her own peach-handled umbrella standing by the door ·
               knowledge certain the office lost one · emotion maximum ·
               relationship_delta none yet
  STATE_CLOSE: wardrobe_state_id OS-PEACH-WED · condition signed at thirty, leaving
               into rain without her umbrella · props_held crate of thirty umbrellas ·
               knowledge she has asked the question and been given no answer ·
               emotion struck quiet · relationship_delta her claim is dead; her
               umbrella is the shelf's first item; her question is the serial's hanger
  (She does not recur within the season except by the bible's Inspector rule —
   this card is banked, not continued, unless a later part re-casts her chair.)
```

---

## §2 — Room gates before any vehicle is written (sign-off block)

```
PASS 3.5 — HEAR-BEFORE-IT-MOVES (F-26; blocking):
  reader (did not write the script): the room's critic pass — role-separated per the
    Writers Room Method (script written by the storyline/dialogue passes; the read
    was run cold, in order, no notes in hand). The independent second ear is the
    parent's Gate (f) cold run at production; this room does not claim otherwise.
  read_aloud_cold_in_order: Y     date: 2026-11-18
  stumbles logged: 1 — U5 line 2 draft "Thirty's the count" stumbled read flat
    (possessive blur) → returned to Pass 3, rewritten "Thirty is the count.
    The book closes even." — see GATE_LOG.md. No other stumbles.
  banter draft exists (conversation-heavy episodes, F-27): Y — mined at the
    Pass 3 pre-step; surviving exchanges recorded in DECISION_LOG.md
  SIGNED: writers room (showrunner pass), 2026-11-18
PASS 4 — SPOKEN-LOAD AUDIT: every unit's §4.1 block signed before
  the first video call. SIGNED: writers room (showrunner pass), 2026-11-18 —
  all six audits PASS (see §4.1 blocks; U5 passes at the 2.0 wps target line)
```

---

## §3 — Panel, Sequence and Animatic gates (production stage — filled protocol, signed at production)

*These gates run at production, before the first video call. The
fields below are filled with this episode's panel plan and the
reads the gate must produce; the sign-offs are production's.
A §3 gate with an unsigned SIGNED line blocks every video call.*

```
SEQUENCE GATE (Pass 1 §B.5 + Pass 2 animatic-era fields):
  contact sheet (all CHAR sheets + all six PEAKs): file E3_one-short/work/seq_sheet.png
    (built at production from: PNL-CHAR-CLERK-sheet-16x9 + CLERK-supp + PNL-CHAR-SNH-sheet-16x9
     + COUNTER-supp + PNL-CHAR-PEACH-sheet-16x9 + PNL-PEAK-U1..U6 + PNL-SHELF-E3;
     PEAK and supplement panels are production step 1, still-layer, rerolls uncapped)
  seq_sheet_blind_first_look_done: AT PRODUCTION — Y required before sign-off
  seq_odd_one_out: AT PRODUCTION — panel ID or none + class
                   IDENTITY / WARDROBE / PROP / MOTION / LIGHT
  seq_anchor_panel: PNL-CHAR-CLERK-sheet-16x9.png (the show's proven anchor;
                   the combined two-character anchor discipline is morph inheritance)
  seq_priority_fix_order_followed: AT PRODUCTION — Y required (identity → wardrobe → prop → environment)
  seq_reads_silent: AT PRODUCTION — Y required
  seq_story_in_one_sentence: the gate's target read, written by this room —
    "A planner claims thirty-one umbrellas; the office counts thirty, stamps
     thirty, and keeps her own umbrella."
    (if the reviewer's sheet-alone sentence is not this story, FAIL)
  reviewer (not the panel maker): CONTINUITY_OWNER
  SIGNED: AT PRODUCTION (blocking)

ANIMATIC GATE (Pass 2, Angle 3 — NEW; both gates must PASS before
any video generation call):
  animatic_file: E3_one-short/work/animatic.mp4  (PEAK panels at script durations
                   + scratch dialogue timing track)
  animatic_watched_at_speed_uninterrupted: AT PRODUCTION — Y required
  animatic_reviewer (not the panel maker): CONTINUITY_OWNER
  animatic_reads_audio_only: AT PRODUCTION — Y required
  animatic_first_confusion_at: AT PRODUCTION — panel/time or none
  animatic_spoken_load_check: pre-computed PASS from the six §4.1 audits
    (every unit's implied_rate ≤2.0); final confirmation AT PRODUCTION —
    any §4.1 overflow there = FAIL, fixed in the script or the durations,
    never at the take
  animatic_panels_reordered_or_cut: AT PRODUCTION — IDs or none
  SIGNED: AT PRODUCTION (blocking)
```

---

## §4 — Per-unit vehicle skeletons

### U1 — BLAM unit · Camp A exception

```
SPOKEN-LOAD AUDIT — U1
  camp: A (native multi) — EXCEPTION to the Camp B default
  director note (Camp A only): the BLAM unit. The claim and the office's answer
    are one ritual breath (bible §6: the want-line rides the slam at ~0.5s and
    the office register answers inside the same unit, or the opening's energy
    splits across a cut and A1 dies). Two turns, 14 words total, one turn
    change — inside every Camp A cap below. No other unit in this episode
    uses Camp A.
  speakers: 2  [PLANNER, CLERK]
  words_total: 14   words_by_speaker: PLANNER 6 · CLERK 8   chars_total: 85
  CAP CHECK: 2 speakers (Camp A exception) — target 14–16 TOTAL ✓ (14),
             HARD CAP 18 TOTAL ✓, ≤9 words/turn ✓ (6, 8), ≤2 turns ✓, 1 turn change ✓.
  hard_words: thirty-one (number — spoken as written, evenly)
  language_accent (per speaker, explicit — never implicit): PLANNER fruit-soap
             melodrama register, full expression · CLERK neutral bureau, flat
  measured_sec: 6.3  (timed performed-read estimate at 0.45 s/word — the
             authority figure for this audit; a silent read is not a measurement)
  silence_budget: lead 0.3s (speech rides the slam's tail — the impact IS the
             lead-in) + internal_pause 0.2s + turn_gap 0.5s + tail 0.5s = 1.5s total
  speech_window: 10 − 1.5 = 8.5s
  implied_rate: 14 / 8.5 = 1.65 wps  [PASS ≤2.0]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW: one generation,
             one spoken container — no composite is planned for any unit
             in this episode)
  time_slots (Camp A only): 0.0–4.5s: PLANNER (want-line over the crash tail,
             onset ~0.5s) / 4.5–10.0s: room settles, CLERK (want line at ~5.5s)
  non_speaker: mouth-closed line present? Y (the Counter counts silently,
             mouth closed, catching the sliding umbrella) · moving-hold line present? Y
  audio_layers: dialogue + crash/room tone = 2  [≤3; no music under dialogue]
  framing_check: speaker medium close-up / facing / mouth unobstructed? Y
             (Planner mid-stride medium, face clear of the crate; Clerk medium
              behind the counter, face clear of the book)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (U1: the opening-state block): "Office at open: counter-wide,
  cold morning light from the door side; the Clerk behind the counter right,
  book open, pen in hand; the Counter floor-side left among stacked crates;
  the shelf in the CCTV corner EMPTY; the office door closed; the split-flap
  board's two windows blank dark shutters."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-PEACH-sheet-16x9.png (Planner) · PNL-CHAR-CLERK-sheet-16x9.png (Clerk)
  GEOMETRY: E2_one-short/panels/PNL-WORLD-office.png · PEAK PNL-PEAK-U1 (production step 1)
  WARDROBE: the three CHAR sheets, by character
  known-defect overrides (POSITIVE statements only): the board's two windows
  stay blank dark shutters in every frame · the fascinator stays a plain foam
  peach shape — smooth, featureless, no face, no text · the crate's umbrellas
  are plain black and uniform
REFS_BOUND: WORLD + CLERK sheet + COUNTER sheet + PEACH sheet (when locked) + PEAK-U1
PRIMARY_BOUND_CHARACTER: PLANNER  (new character, highest drift risk; the Clerk
  is bound by her locked sheet as secondary ref; the Counter is prompt-carried
  this unit — he does not speak and his sheet is bound at U2)
VOICE_REF_CLIP attached (AUDIO_REFERENCE route): NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the PLANNER is in wardrobe state OS-PEACH-WED,
  holding her blank folder, condition mid-stride entering; the CLERK is in
  OS-CLERK-STD, holding a pen, condition at the open book; the COUNTER is in
  OS-COUNTER-STD, holding nothing, tally counter on its chain.
CHAIN: outgoing last frame (harvested after conform) = image 1 ·
  gated PEAK = image 2. Snapshot/resume chaining is NOT used.

PERSONA_INJECTION: PER_UNIT —
  PLANNER: counts claims, not objects; every line carries the noon clock.
  CLERK: reads every claim as a number to be tested; charges for the book in picture.
PERSONA_TRANSLATION:
  PLANNER — mid-stride command: chin up, folder hugged, voice thrown over the
  crash; gaze on the Clerk, flicking to the board as its shutters flip.
  CLERK — stillness lead: she does not look up for the crash; the book holds
  her eyes until her own line.
OBJECTIVE: PLANNER — to conscript the office's count to her number before noon ·
  CLERK — to settle the book even by noon
OBSTACLE: PLANNER — the office counts only what is brought, and her number
  includes what she carried · CLERK — a claim arriving louder than the load
TACTICS: PLANNER command (the deadline) → stake (the fee) ·
  CLERK absorb (let the crash finish) → terms (her want stated as the price of admission)
EYE TASK: PLANNER — eyes on the Clerk through her line, then a flick to the
  board as it flips; hold on the board ~1s (she watches her number, never the pile) ·
  CLERK — eyes on the book through the crash; lift to the Planner only on her
  own line; hold flat through the tail
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated here if this is the unit where it is paid or refused: the
  Clerk's want IS her rent stated — the book closes even, or it does not close

END STATE (the pin):
  end_state.identity: Planner centre behind the crate, facing the counter;
    Clerk behind the counter right, facing the Planner; Counter floor-side
    left, crouched, holding the caught umbrella, facing the pile
  end_state.wardrobe: Planner peach-satin suit + foam peach fascinator; Clerk
    bone blouse, ink vest, spectacles; Counter ink work shirt, tally counter on chain
  end_state.prop: crate of black hire umbrellas spilled across the counter, one
    umbrella in the Counter's hand; the Planner's peach-handled umbrella
    standing by the door; hire receipt flat on the counter; book open; board
    windows in the flipped position (numbers are post)
  end_state.light: cold morning light raking from the door side (frame left),
    cadmium practical glow over the counter
ACTION / SCENE SENTENCES: the door slams mid-frame, the bell rings, the crate
  crashes across the counter; the Planner strides in mid-sentence; the board's
  shutters flip once on the slam; the Counter catches a sliding umbrella
  without looking up; the camera pushes in with the load. Named event: THE SLAM.
DELIVERY_NOTE per line: PLANNER — thrown over the crash tail, no pause before
  it · CLERK — flat, unhurried, after the last umbrella settles
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  PLANNER (peach fascinator, mid-stride, commanding): Thirty-one umbrellas. Count them before noon.
  CLERK (behind the counter, flat, eyes on the book): I want the book closed even by noon.
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces (signs, tags, boards, documents) are described as
  blank/illegible texture: the split-flap board's two windows (blank dark
  shutters), the book's open pages (blank ruled texture), the hire receipt
  (blank paper), the Planner's folder (blank cream), the streak card (blank card).
  PIL plates are the DEFAULT carrier for in-world text (board numbers, book
  entries, the certificate, the streak number, the end card), composited at
  assembly — never a fallback.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

### U2 — the count begins · Camp B

```
SPOKEN-LOAD AUDIT — U2
  camp: B (1 speaker per clip) — the default
  speakers: 1  [COUNTER]
  words_total: 15   words_by_speaker: COUNTER 15   chars_total: 88
  CAP CHECK: 1 speaker — target 14–17 words ✓ (15), HARD CAP 20 ✓.
  hard_words: eighteen, nineteen, twenty (number chain — one number per
             umbrella placed, evenly spaced)
  language_accent: neutral, flat counting register
  measured_sec: 6.8
  silence_budget: lead 0.4s + internal_pause 0.5s + turn_gap 0s + tail 0.7s = 1.6s total
  speech_window: 10 − 1.6 = 8.4s
  implied_rate: 15 / 8.4 = 1.79 wps  [PASS ≤2.0]
  generation_sec: 10   span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (Clerk at her book, Planner watching
             the pile, folder hugged) · moving-hold line present? Y
  audio_layers: dialogue + tally clicks / room tone = 2
  framing_check: Y (Counter medium, facing along the counter, mouth unobstructed)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (quoted verbatim from U1's END STATE): "Planner centre behind
  the crate, facing the counter; Clerk behind the counter right, facing the
  Planner; Counter floor-side left, crouched, holding the caught umbrella,
  facing the pile — crate spilled across the counter, the Planner's umbrella
  by the door, receipt on the counter, book open, board flipped."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-SNH-sheet-16x9.png (Counter)
  GEOMETRY: PNL-WORLD-office.png · PEAK PNL-PEAK-U2
  WARDROBE: PNL-CHAR-SNH-sheet-16x9.png
  known-defect overrides (POSITIVE statements only): the counted row reads as
  an honest row of umbrellas lying parallel — the board carries the arithmetic,
  never the pile · the streak card stays a blank card at his chest
REFS_BOUND: WORLD + COUNTER sheet + CLERK sheet + PEAK-U2
PRIMARY_BOUND_CHARACTER: COUNTER
VOICE_REF_CLIP attached: NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the COUNTER is in wardrobe state OS-COUNTER-STD,
  holding the caught umbrella, condition starting batch one; streak card at 41 (post).
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2.

PERSONA_INJECTION: PER_UNIT — COUNTER: notices patterns in his hands before
  his words; recounts any pile his hand doubts without being asked.
PERSONA_TRANSLATION: the metronome — shoulders still, only the counting hand
  and the clicker move; gaze travels along the row, never to faces.
OBJECTIVE: to run the count so clean it cannot be argued with
OBSTACLE: the pile is smaller than the claim — his hand already suspects it
TACTICS: recite (the chain, evenly) → declare (his want, stated to the room
  while the count continues)
EYE TASK: eyes on the umbrellas, one per number; on the want line, eyes lift
  to the board's counted window for one beat, then back to the pile
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated: his force is exercised here — his number becomes the office's fact

END STATE (the pin):
  end_state.identity: Counter standing at the counter's end, facing along the
    completed row; Clerk behind the counter right at the book; Planner
    centre-right, watching the pile
  end_state.wardrobe: unchanged — Counter ink work shirt + tally chain; Clerk
    bone blouse, ink vest; Planner peach suit + fascinator
  end_state.prop: one row of twenty black umbrellas laid along the counter;
    the remaining pile beside the crate, visibly small; receipt flat on the
    counter; the Counter's hand stopped mid-air over the pile (GAP 1's held
    beat IS this unit's tail state)
  end_state.light: cold morning light from the door side, unchanged
ACTION / SCENE SENTENCES: batch one is laid along the counter and counted
  aloud, one tally click per batch; the board's shutters flip at the cliff;
  GAP 1 (tail, 2–3s): his hand stops mid-air over the remaining pile and
  holds — he has felt it run light, and says nothing. Named event: none.
DELIVERY_NOTE per line: chain line — even spacing, one number per umbrella
  placed · want line — same flat register, no emphasis on "even"
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  COUNTER (gaunt, tally counter on a chain, counting hand moving): Eighteen, nineteen, twenty — batch one stands now.
  COUNTER (same register, eyes lifting to the board): One count even — that's all I want today.
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces: the board's windows, the streak card, the receipt,
  the book's pages — all blank texture; numbers are post PIL plates.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

### U3 — QUIET unit · Camp B

```
SPOKEN-LOAD AUDIT — U3
  camp: B (1 speaker per clip) — the default
  speakers: 1  [CLERK]
  words_total: 12   words_by_speaker: CLERK 12   chars_total: 70
  CAP CHECK: 1 speaker — target 14–17; this is the episode's QUIET unit
             (slate fix F4.1 stands: the pile, not the talk, carries the turn) —
             12 words is a design value, not an underrun; HARD CAP 20 ✓.
  hard_words: none
  language_accent: neutral bureau, flat
  measured_sec: 5.4
  silence_budget: lead 0.4s + internal_pause 0.5s + turn_gap 0s + tail 0.7s = 1.6s total
  speech_window: 10 − 1.6 = 8.4s
  implied_rate: 12 / 8.4 = 1.43 wps  [PASS ≤2.0]
  generation_sec: 10   span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (the Counter counts batch two in
             silence, mouth closed) · moving-hold line present? Y (the Planner
             reads the board as it settles)
  audio_layers: dialogue + room tone = 2
  framing_check: Y (Clerk medium behind the counter, receipt at chest height,
             mouth unobstructed)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (quoted verbatim from U2's END STATE): "Counter standing at
  the counter's end, facing along the completed row of twenty; Clerk behind
  the counter right at the book; Planner centre-right watching the pile; the
  remaining pile beside the crate, visibly small; the Counter's hand stopped
  mid-air over the pile."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-CLERK-sheet-16x9.png (Clerk)
  GEOMETRY: PNL-WORLD-office.png · PEAK PNL-PEAK-U3
  WARDROBE: PNL-CHAR-CLERK-sheet-16x9.png
  known-defect overrides (POSITIVE statements only): the receipt in her hand
  stays blank paper — its surface reads as smooth blank texture at every distance
REFS_BOUND: WORLD + CLERK sheet + COUNTER sheet + PEAK-U3
PRIMARY_BOUND_CHARACTER: CLERK
VOICE_REF_CLIP attached: NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the CLERK is in wardrobe state OS-CLERK-STD,
  holding the hire receipt (picked up this unit), condition reading a claim.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2.

PERSONA_INJECTION: PER_UNIT — CLERK: reads every claim as a number to be
  tested; the book is hers and she charges for it in picture.
PERSONA_TRANSLATION: the verdict voice at rest — she reads paper the way other
  people read faces; cobalt fingertips at the receipt's edge; stillness lead.
OBJECTIVE: to separate the claim from the count before the accusation forms
OBSTACLE: the receipt is real paper with a real price — the customer will wave it
TACTICS: cite the office rule (the carrier line) → reclassify (a receipt is a
  payment record, not a count)
EYE TASK: eyes on the receipt through both lines; at the cliff, eyes lift to
  the board as the counted window settles — her gaze arrives with the number
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated: her block is exercised here — the receipt is refused as evidence

END STATE (the pin):
  end_state.identity: Clerk behind the counter right, holding the receipt at
    chest height, facing the Planner; Counter floor-side left, standing back
    from the finished pile; Planner centre, reading the board
  end_state.wardrobe: unchanged all three
  end_state.prop: the full counted row of thirty black umbrellas along the
    counter; the crate empty beside it; the receipt in the Clerk's hand; the
    board in its settled position (numbers are post)
  end_state.light: cold morning light from the door side, unchanged
ACTION / SCENE SENTENCES: batch two is counted in frame in silence behind her
  lines; the board's shutters flip at the cliff to the settled position; she
  sets the receipt down flat at the cliff. Named event: none.
DELIVERY_NOTE per line: carrier line — flat audio-logo delivery, no warmth ·
  second line — a ruling, with a slight pause after "paid"
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  CLERK (behind the counter, flat, receipt rising): We count what's brought.
  CLERK (eyes on the receipt, ruling): Receipts say what was paid, not what came.
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces: the receipt, the book's pages, the board's windows
  — blank texture; all lettering is post.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

### U4 — accusation + the stake · Camp B

```
SPOKEN-LOAD AUDIT — U4
  camp: B (1 speaker per clip) — the default
  speakers: 1  [PLANNER]
  words_total: 16   words_by_speaker: PLANNER 16   chars_total: 92
  CAP CHECK: 1 speaker — target 14–17 words ✓ (16), HARD CAP 20 ✓.
  hard_words: thirty-one (number — spoken as written)
  language_accent: fruit-soap melodrama register, full expression
  measured_sec: 7.2
  silence_budget: lead 0.4s + internal_pause 0.5s + turn_gap 0s + tail 0.7s
             (the tail carries GAP 2's CCTV hold, which extends past the unit
              boundary as the joint's held beat) = 1.6s total
  speech_window: 10 − 1.6 = 8.4s
  implied_rate: 16 / 8.4 = 1.90 wps  [PASS ≤2.0]
  generation_sec: 10   span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (the Clerk's hand comes to rest
             near — not on — the envelope; the Counter turns back to the pile
             at the tail) · moving-hold line present? Y
  audio_layers: dialogue + room tone (envelope slap is a room event) = 2
  framing_check: Y (Planner medium across the counter, face clear of the folder)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (quoted verbatim from U3's END STATE): "Clerk behind the
  counter right, holding the receipt at chest height, facing the Planner;
  Counter floor-side left, standing back from the finished pile; Planner
  centre, reading the board; the counted row of thirty along the counter;
  the crate empty beside it."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-PEACH-sheet-16x9.png (Planner — PRODUCTION BLOCKER: this
  unit may not fire until the sheet is locked and its sha256 entered in §1)
  GEOMETRY: PNL-WORLD-office.png · PEAK PNL-PEAK-U4
  WARDROBE: PNL-CHAR-PEACH-sheet-16x9.png
  known-defect overrides (POSITIVE statements only): the deposit envelope is
  blank cream, sealed, its face smooth and unmarked at every distance
REFS_BOUND: WORLD + PEACH sheet + CLERK sheet + PEAK-U4
PRIMARY_BOUND_CHARACTER: PLANNER
VOICE_REF_CLIP attached: NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the PLANNER is in wardrobe state OS-PEACH-WED,
  holding her deposit envelope (produced this unit), condition accusing; her
  own umbrella still standing by the door.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2.

PERSONA_INJECTION: PER_UNIT — PLANNER: counts claims, not objects; deadline
  panic worn as command; her money is the argument.
PERSONA_TRANSLATION: full-expression attack — chin up, folder hugged, the
  accusation thrown at the Clerk while her body angles at the board; tempo
  double the room's.
OBJECTIVE: to force a recount that saves her fee
OBSTACLE: the board already reads thirty, and the book is older than her claim
TACTICS: accuse (the crash lost one) → stake (the deposit, bought in advance)
EYE TASK: eyes on the Clerk for the accusation; down to the envelope as it
  lands; then hard at the board for the tail beat — she is daring it to change
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated: her force is exercised here — the deposit buys the recount;
  its price is named in §1 and collected in U5

END STATE (the pin):
  end_state.identity: Planner centre, facing the Clerk across the counter,
    the envelope between them under nobody's hand; Clerk behind the counter
    right, hand resting near the envelope; Counter at frame left, turning
    back toward the pile
  end_state.wardrobe: unchanged all three
  end_state.prop: deposit envelope flat on the counter; the counted row of
    thirty undisturbed (one umbrella caught at her hip is returned to the
    row inside the unit); her umbrella still by the door; the shelf still empty
  end_state.light: cold morning light from the door side, unchanged
ACTION / SCENE SENTENCES: the accusation is delivered across the counter; the
  envelope slaps down flat on the stake line; one umbrella rolls off the row
  and she catches it against her hip without breaking the line and sets it
  back; GAP 2 (tail, 2–3s): the angle cuts to the CCTV corner — the shelf
  EMPTY and her own umbrella standing by the door in one frame, nobody
  looking at either. Named event: THE STAKE (the envelope slap).
DELIVERY_NOTE per line: accusation — thrown, no pause before it · stake line
  — slower, each word placed; the envelope lands on its first word
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  PLANNER (peach fascinator, chin up, across the counter): You lost one in the crash. I packed thirty-one.
  PLANNER (envelope slapping down, slower): Recount them. My deposit rides on it.
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces: the envelope, the board's windows, the book's
  pages — blank texture; all lettering is post.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

### U5 — the reveal + the verdict · Camp B

```
SPOKEN-LOAD AUDIT — U5
  camp: B (1 speaker per clip) — the default
  speakers: 1  [CLERK]
  words_total: 17   words_by_speaker: CLERK 17   chars_total: 96
  CAP CHECK: 1 speaker — target 14–17 words ✓ (17, at the target ceiling),
             HARD CAP 20 ✓. No trim is available: the reveal line and the
             verdict line are the unit's two beats, and both are load-bearing.
  hard_words: none
  language_accent: neutral bureau, flat, half a register deeper than U3
  measured_sec: 7.7
  silence_budget: lead 0.4s + internal_pause 0.5s + turn_gap 0s + tail 0.6s = 1.5s total
  speech_window: 10 − 1.5 = 8.5s
  implied_rate: 17 / 8.5 = 2.00 wps  [PASS — at the ≤2.0 target line; the two
             lines are short sentences with a full stop between them, and the
             Animatic Gate re-checks this unit first]
  generation_sec: 10   span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (the Planner watches the book; the
             Counter recounts in silence, collecting the price in picture) ·
             moving-hold line present? Y
  audio_layers: dialogue + room tone (recount handling) = 2
  framing_check: Y (Clerk medium at the open book, face clear of the pages;
             the book angle is the show's declared close angle)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (quoted verbatim from U4's END STATE): "Planner centre, facing
  the Clerk across the counter, the envelope between them under nobody's
  hand; Clerk behind the counter right, hand resting near the envelope;
  Counter at frame left, turning back toward the pile; the counted row of
  thirty undisturbed; her umbrella still by the door; the shelf still empty."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-CLERK-sheet-16x9.png (Clerk)
  GEOMETRY: PNL-WORLD-office.png · PEAK PNL-PEAK-U5 · the CCTV insert angle
  follows E2_one-short/panels/PNL-SHELF.png's framing (shelf angle reference)
  WARDROBE: PNL-CHAR-CLERK-sheet-16x9.png
  known-defect overrides (POSITIVE statements only): the book's pages read as
  blank ruled texture at every distance · the certificate on the counter is a
  blank cream card until the post stamp · the deposit envelope's face stays
  smooth and unmarked as it slides into the book
REFS_BOUND: WORLD + CLERK sheet + COUNTER sheet + PEAK-U5
PRIMARY_BOUND_CHARACTER: CLERK
VOICE_REF_CLIP attached: NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the CLERK is in wardrobe state OS-CLERK-STD,
  holding the book (opened this unit), condition revealing; the Counter is
  mid-recount; the Planner's umbrella still by the door at unit start.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2.

PERSONA_INJECTION: PER_UNIT — CLERK: the book is hers; its history outranks
  any single claim; she charges for it in picture and the charge is collected
  inside this unit.
PERSONA_TRANSLATION: the authority at the reveal — she stands for the book's
  lines (her one rise in the episode); cobalt fingertip travelling the page;
  voice half a register deeper, not louder.
OBJECTIVE: to end the claim with the book's authority
OBSTACLE: the customer's money is on the counter and her noon is real
TACTICS: widen (every count in the book) → settle (this count, this verdict,
  the stamp)
EYE TASK: eyes down the book's page for the reveal line; lift to the Planner's
  face for the verdict line; hold on her through the stamp
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated: her price is collected here — deposit into the book, and the
  Counter shelves the Planner's umbrella in the same unit

END STATE (the pin):
  end_state.identity: Clerk behind the counter right, book open before her,
    the stamp just lifted from the certificate; Planner centre, facing the
    certificate, the pen beside her hand; Counter floor-side left, back
    half-turned from the door, empty-handed
  end_state.wardrobe: unchanged all three
  end_state.prop: certificate (post-stamped) on the counter; deposit envelope
    inside the open book as its marker; the Planner's umbrella now standing
    ON THE SHELF in the CCTV corner; the counted row of thirty intact; the
    board in its settled position (numbers are post)
  end_state.light: cold morning light from the door side; the cadmium
    practical over the counter warms the book angle
ACTION / SCENE SENTENCES: the recount runs behind the dialogue and confirms
  the row; mid-unit the Counter passes the door with the last batch, lifts the
  Planner's umbrella from the door stand and sets it on the shelf as he
  passes, eyes on the pile; the Clerk opens the book, delivers the reveal,
  stamps the certificate, slides the envelope into the book. The umbrella's
  state change (door → shelf) is staged in plain view as an action across
  the unit, never as a morph (F-24). Named event: THE PRICE COLLECTED.
DELIVERY_NOTE per line: reveal line — unhurried, fingertip on the page ·
  verdict line — after a full beat, flat as a stamp; a ~1s reaction hold on
  the Planner follows inside the unit's tail
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  CLERK (book open, fingertip on the page, deeper register): Every count in this book came up one short.
  CLERK (eyes lifting to the Planner, flat): Thirty is the count. The book closes even.
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces: the book's pages (blank ruled texture), the
  certificate (blank until the post stamp), the board's windows, the
  envelope — all lettering is post PIL plates.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

### U6 — payoff completed + the hanger · Camp B

```
SPOKEN-LOAD AUDIT — U6
  camp: B (1 speaker per clip) — the default
  speakers: 1  [PLANNER]
  words_total: 6   words_by_speaker: PLANNER 6   chars_total: 30
  CAP CHECK: 1 speaker — the SILENCE-BEAT unit (bible §8): one line, then the
             freeze carries the unit; HARD CAP 20 ✓.
  hard_words: none
  language_accent: fruit-soap register, struck quiet — the first time she is
             quieter than the room
  measured_sec: 2.7
  silence_budget: lead 0.5s + internal_pause 0s + turn_gap 0s + tail 2.0s
             (GAP 3's freeze is inside this tail) = 2.5s total
  speech_window: 10 − 2.5 = 7.5s
  implied_rate: 6 / 7.5 = 0.80 wps  [PASS ≤2.0]
  generation_sec: 10   span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (the Clerk at the book; the Counter
             counting the shelf silently, lips still) · moving-hold line present? Y
  audio_layers: dialogue + rain at the open door = 2
  framing_check: Y (Planner at the door in profile-to-lens, mouth unobstructed
             for her line; the freeze is the CCTV wide)
  verdict: PASS
  SIGNED (Pass 4): writers room, 2026-11-18

PREV END STATE (quoted verbatim from U5's END STATE): "Clerk behind the
  counter right, book open before her, the stamp just lifted from the
  certificate; Planner centre, facing the certificate, the pen beside her
  hand; Counter floor-side left, back half-turned from the door,
  empty-handed; the Planner's umbrella now standing ON THE SHELF; the
  counted row of thirty intact."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-PEACH-sheet-16x9.png (Planner — PRODUCTION BLOCKER as
  §1) · PNL-CHAR-SNH-sheet-16x9.png (Counter — the freeze is a two-face frame)
  GEOMETRY: the CCTV shelf angle (E2_one-short/panels/PNL-SHELF.png framing)
  · PNL-WORLD-office.png · PEAK PNL-PEAK-U6
  WARDROBE: the respective CHAR sheets
  known-defect overrides (POSITIVE statements only): the frame's bottom
  strip stays clear of faces and props — the end card's space; the shelf
  holds exactly one umbrella, peach-handled, distinct from the black hire row
REFS_BOUND: WORLD + PEACH sheet + COUNTER sheet + CLERK sheet + PEAK-U6
PRIMARY_BOUND_CHARACTER: PLANNER
VOICE_REF_CLIP attached: NA — NATIVE_TEXT_ONLY (waiver, §0)
STATE_ASSERT: at unit start, the PLANNER is in wardrobe state OS-PEACH-WED,
  holding the pen (put into her hand at the unit head), condition signing;
  her umbrella is on the shelf; the crate of thirty is at her feet.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2. (U6 is the
  part's last unit; its last frame is the part's poster-eligible freeze and
  Part 2's U1 opening-state source.)

PERSONA_INJECTION: PER_UNIT —
  PLANNER: the deadline is spent; what is left is the question.
  COUNTER (silent this unit): his arc's act — he counts the shelf the way he
  counts a pile, and his eyes finish what his mouth never starts.
PERSONA_TRANSLATION:
  PLANNER — the register cracks downward: she signs without flourish, crosses
  to the door at office tempo for the first time, and her hand — not her
  voice — makes the last beat, rising to the empty door stand.
  COUNTER — whole-body turn to the shelf; one tally click; stillness.
OBJECTIVE: PLANNER — to recover the one she is missing before she leaves ·
  COUNTER (silent) — to count the shelf, once, and be seen counting it
OBSTACLE: PLANNER — the certificate is signed, the book is closed, and the
  answer stands behind her on a shelf she has never looked at
TACTICS: PLANNER sign (complete the payoff) → reach (for her umbrella, by
  habit) → ask (the question, to a room that will not answer)
EYE TASK: PLANNER — eyes on the certificate as she signs; on the empty door
  stand as her hand rises; then out the door at the rain — she never sees
  the shelf · COUNTER — eyes travel the shelf, stop on her umbrella, then
  lift to the lens and hold for the freeze's last beat: this episode's ONE
  rationed self-awareness beat (F-21), spent here, unspoken
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
RENT restated: the payoff completes here — her signature is her block
  surrendered; the price she paid (deposit + umbrella) is not refunded

END STATE (the pin):
  end_state.identity: Planner at the open door, foreground edge, hand raised
    toward the empty stand, facing out; Counter centre-left, turned to the
    shelf, eyes on the lens; Clerk behind the counter right at the frame's
    edge, book open
  end_state.wardrobe: unchanged all three
  end_state.prop: signed certificate on the counter; crate of thirty at the
    door beside her; her umbrella ON THE SHELF; deposit envelope inside the
    book; board in its settled position; streak card at 42 (post)
  end_state.light: cold morning light; rain-grey light through the open door
    behind her
ACTION / SCENE SENTENCES: she signs the certificate; takes the crate handle;
  crosses to the door; her hand rises to the empty stand; the Counter turns
  his whole body and counts the shelf with his eyes and one tally click,
  stopping on her umbrella; GAP 3 (tail, final 2–3s): the freeze holds on
  the CCTV corner — shelf with one umbrella, her raised hand, his look.
  Named event: none — the freeze is the event's opposite, by design.
DELIVERY_NOTE per line: the question — small, level, no melodrama; a real
  question asked of a room that will not answer
SPEECH BLOCK (veo-colon-noquotes; last, isolated):
  PLANNER (at the door, quiet, hand rising): Then where does the one go?
TEXT RULE: this vehicle contains no words of any in-world text.
  Declared-blank surfaces: the board, the book, the certificate, the streak
  card — blank as declared. The end card (her question + the count-along
  call: post your count of the load) is a post PIL plate in the frame's
  cleared bottom strip — never generator-rendered.
DURATION + ASPECT line: 10 seconds, 16:9, 1280×720, 24fps
```

---

*End of brief. Production opens `work/GATE_LOG.md` on template §5
(per-take QC with the four drift classes, the three-instrument voice
check, per-joint logs, master gates incl. the mechanical diff, the
ear-test sign-off, Gate (f) THE COLD RUN, and the calibration ledger)
and fills CAST_LOG in §0 at delivery.*
