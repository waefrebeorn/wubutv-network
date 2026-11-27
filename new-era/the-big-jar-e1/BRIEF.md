# THE BIG JAR — E1 PRODUCTION BRIEF

Built from new-era/E3_PRODUCTION_BRIEF_TEMPLATE.md by the production
coordinator, 2026-11-27, from the LOCKED script
(the-big-jar-e1/SCRIPT_E1.md, parent-written, LOCKED v1 — dialogue
not altered by this brief). Bible: new-era/shows/THE_BIG_JAR.md.

## §0 — Episode header

```
SHOW: THE BIG JAR            EPISODE / PART: E1
TITLE (the question the episode answers): "Who Touches the Line First?"
CAPTION (the episode SENTENCE, §2): "Two neighbours race to fill the
  big jar before the fair. The loser carries the winner's jar home
  on his head."
REGISTER: fair-day street vernacular — plain spoken English, short
  verdict lines, counting out loud; temperature: warm, dry, public —
  everything is said in front of the street.
CONTINUITY_OWNER: the parent Muse (series RUNNING_BRIEF checked:
  new-era/shows/THE_BIG_JAR.md — cast, ledger rule, texture, E1
  rulings (a)–(d) all carried below).
GENERATOR: media.generate_video / media.generate_image (house tool,
  model unnamed) · mode: image-conditioned, native audio
MODEL_SYNTAX: veo-colon-noquotes (house default for this generator;
  speech block rendered NAME (trait, delivery): line, no quotation
  marks anywhere in the vehicle)
VOICE_ROUTE: NATIVE_TEXT_ONLY
  WAIVER: tiny-voca TTS is ON HOLD by standing user order (msg 730)
  and the production order for this episode specifies native
  generated audio only; recurring-character waiver recorded here per
  template §0. Voices are carried by per-character VOICE_SPEC_TEXT
  (fallback/drift-reducer) restated in every vehicle.
SHOW_OFF: MARO (the braggart — his U1 brag commits his whole roof;
  the street is his audience).
```

## §1 — Cast cards

```
CHARACTER: MARO            CARD_VERSION: E1-v1
CAST_CLASS: principal
LOOK (bound):
  LOOK_PACK: built this episode — refs/maro_sheet.png (multi-view
    sheet, QC reference) + refs/maro_front.png (frontal anchor,
    cropped from the sheet — the fed reference; S6 case (c): cast
    relative scale is baked at panel stage)
  CANONICAL_FACE_REF: refs/maro_front.png (sha256 logged in GATE_LOG
    at panel sign-off)
  REANCHOR_RULE: never chain a drifted frame; re-anchor to
    CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "MARO: a tall lean man of about forty with a
    long face and a long nose, dark hair swept back, wearing a work
    shirt thickly dusted chalk-white across the chest and shoulders,
    sleeves rolled to the elbow, dark trousers, heavy boots."
  IDENTITY_MODE: description-bound (LOOK_BLOCK_VERBATIM pasted in
    full in every vehicle)
  WARDROBE_STATES: MARO-DUST = chalk-dusted shirt, hat ON head
    (U1–U3) · MARO-NO-HAT = same shirt, hat gone — the hat is in the
    jar (U5–U6; U4 is the unit where it leaves his head)
VOICE_SPEC_TEXT: age ~40 · gender male · timbre dry baritone ·
  pace unhurried, public · accent plain street English ·
  trait: brags upward, at the sky and the street · breaks: goes
  quiet and flat when caught
PERSONA:
  TRAIT → OBSERVABLE_BEHAVIOUR: braggart → measures his own roof
    with his eyes like a bank account; commits big, in public
  TRAIT → OBSERVABLE_BEHAVIOUR: cheat → works at night, alone,
    grinning at the jar, never at a person
  EXAMPLE_LINE: "Then start painting, Widow. My whole roof is
    coming down."
  RIZZ CARD:
    CARRIER_WORDS: "my whole ___" (my whole roof)
    CATCHPHRASE: the public commitment brag — "My whole ___ is
      coming down / going in."
    BRAG: "My whole roof is coming down."
    AUDIBLE_TELL: when caught, the brag leaves his voice — flat,
      short, no lift at the end of the line
    length_trait: runs long when bragging; one-word flat when cornered
    SPECIMEN_LINES: "My whole roof is coming down." · "Paint is
      paint." · "A key sinks nowhere."
    REGISTER_DEVIATION: leans WITH the register — the loudest
      fair-day voice on the street
  NEVER_DOES: apologises · whispers a brag
  NEVER_SAYS: "sorry" · "I was wrong"
  SECRET: he has already decided the jar is his by any means (the
    night cheat is planted U2, shown not said)
  RENT: force the race / block PELL's win / price his whole house
MOTION_SIGNATURE: posture lead: chest out, chin up · gesture habit:
  points at his own property when he speaks · stillness behaviour:
  frozen grin when accused · tempo: strides, never hurries
STATE (episode):
  STATE_OPEN: MARO-DUST · hat on · roof whole · count 1—1
  STATE_CLOSE: MARO-NO-HAT · house empty, roof half gone · jar on
    his head · key returned to PELL by his own tipping hand
```

```
CHARACTER: PELL            CARD_VERSION: E1-v1
CAST_CLASS: principal
LOOK (bound):
  LOOK_PACK: refs/pell_sheet.png + refs/pell_front.png (frontal
    anchor, cropped; sha256 in GATE_LOG)
  CANONICAL_FACE_REF: refs/pell_front.png
  REANCHOR_RULE: never chain a drifted frame; re-anchor to
    CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "PELL: a short round man of about forty with
    a round face and short dark hair, wearing a buttoned brown coat
    over a plain shirt, a red string tied at his left wrist."
  IDENTITY_MODE: description-bound
  WARDROBE_STATES: PELL-COAT = coat buttoned, buttons present (U1)
    · PELL-OPEN = coat hanging open, buttons gone, shirt tied shut
    with red string (U2–U6)
VOICE_SPEC_TEXT: age ~40 · gender male · timbre lighter tenor ·
  pace quick, exact · accent plain street English · trait: counts
  things out loud, precisely · breaks: voice stops dead when he
  finds the proof — the object speaks first
PERSONA:
  TRAIT → OBSERVABLE_BEHAVIOUR: exact → holds objects high, states
    their count in plain words
  TRAIT → OBSERVABLE_BEHAVIOUR: stubborn → stakes the next thing
    instead of conceding, every time
  EXAMPLE_LINE: "Small things sink straight."
  RIZZ CARD:
    CARRIER_WORDS: counts as address — "One tile. Two lines."
    CATCHPHRASE: the count stated flat — "One ___. Two ___."
    BRAG: "My coat is full of buttons."
    AUDIBLE_TELL: when he has proof, he goes quieter and slower,
      one word at a time
    length_trait: short counted bursts; shortest line in the
      episode is his winner ("Small things sink straight.")
    SPECIMEN_LINES: "Your roof leaks." · "One tile. Two lines. It
      went in twice." · "Small things sink straight."
    REGISTER_DEVIATION: leans AGAINST the register — the quiet
      counter inside the loud street
  NEVER_DOES: shouts a brag · lets a count go unstated
  NEVER_SAYS: "maybe" · "I give up"
  SECRET: his door key is already tied with red string before U5 —
    he has been ready to stake the house all day
  RENT: force the count to be honest / block MARO's cheat / price
    his coat, then his house itself
MOTION_SIGNATURE: posture lead: chin up at taller men · gesture
  habit: holds the proof object high in one hand · stillness
  behaviour: stops dead mid-step when something is wrong ·
  tempo: bustles, short quick steps
STATE (episode):
  STATE_OPEN: PELL-COAT · buttons full · house furnished
  STATE_CLOSE: PELL-OPEN · house bare · key won back into his open
    hand · winner
```

```
CHARACTER: Widow BRAN            CARD_VERSION: E1-v1
CAST_CLASS: principal
LOOK (bound):
  LOOK_PACK: refs/bran_sheet.png + refs/bran_front.png (frontal
    anchor, cropped; sha256 in GATE_LOG)
  CANONICAL_FACE_REF: refs/bran_front.png
  REANCHOR_RULE: never chain a drifted frame; re-anchor to
    CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "Widow BRAN: an older woman of about
    sixty-five with grey hair in a tight bun and a lined, unsmiling
    face, wearing a dark widow's dress with a white apron, a paint
    pot in one hand and a wide paint brush in the other, always."
  IDENTITY_MODE: description-bound
  WARDROBE_STATES: BRAN-PAINT = the one state, all units — pot and
    brush in hand in every frame she appears
VOICE_SPEC_TEXT: age ~65 · gender female · timbre low, dry ·
  pace slow verdict pace · accent plain street English · trait:
  states law and sentences as facts, never argues · breaks: never
  breaks — the refusal is as flat as the law
PERSONA:
  TRAIT → OBSERVABLE_BEHAVIOUR: fair → paints the ruling on the
    glass where everyone can see it; counts on her fingers in
    public
  TRAIT → OBSERVABLE_BEHAVIOUR: final → wipes a cheat's count off
    with her sleeve, without a speech
  EXAMPLE_LINE: "Then tonight, you eat air."
  RIZZ CARD:
    CARRIER_WORDS: verdict nouns stated bare — "His dinner. His
      chair. His hat."
    CATCHPHRASE: the sentence as a list — "A cheat pays in things."
    BRAG: none — BRAN never brags; her brag-equivalent is the
      painted line itself
    AUDIBLE_TELL: none — flat at law, flat at refusal; the
      sameness IS the tell
    length_trait: two-beat verdicts; the second beat is shorter
    SPECIMEN_LINES: "First marked thing to touch the line wins." ·
      "Loser carries the jar home. On his head." · "Then tonight,
      you eat air."
    REGISTER_DEVIATION: under the register — drier and slower than
      the street around her
  NEVER_DOES: raises her voice · explains a ruling twice
  NEVER_SAYS: "I think" · "perhaps"
  SECRET: she counted MARO's roof gaps before anyone asked — she
    already knows (her U3 count is a performance of fairness, not
    a discovery)
  RENT: force the law to be public / block any private settlement /
    price: things, not words
MOTION_SIGNATURE: posture lead: upright on her stool, brush raised
  · gesture habit: paints while she speaks · stillness behaviour:
  waits, brush still, until the street is quiet · tempo: unhurried
STATE (episode):
  STATE_OPEN: BRAN-PAINT · painting "1 — 1"
  STATE_CLOSE: BRAN-PAINT · painting one last small thing on the
    glass — a door
```

```
NON-PRINCIPALS (not referenced; one permanent COSTUME_TOKEN each,
named verbatim in every vehicle they appear in):
  TILO — COSTUME_TOKEN: "the tool-man with a ladder over his
    shoulder and a belt of tools" (lends tools; changes sides U2)
  SARA — COSTUME_TOKEN: "the gossip in the bright headscarf"
    (gossips the count; helps the sentence land U4)
  UMBER — COSTUME_TOKEN: "the betting man in the flat cap with a
    coin in his fingers" (coin on MARO's side U1; moves it to
    PELL's side U3)
  THE FRUIT FAMILY (texture only, background, never named in
    dialogue) — COSTUME_TOKEN: "a small fruit family carrying a
    tiny table" (moves into MARO's emptied house, U4 background)
```

## §2 — Pre-production checklist (recorded from the locked script)

```
STORYLINE DECLARATIONS:
  PETTY_WANT: MARO wants to beat PELL in public and be carried
    home the winner of the street — and when the honest race turns
    against him he wants the win anyway, at night, with a string.
    COLLISION TEST: two neighbours empty their own houses into a
    giant jar to win a race, and the cheat is one roof tile used
    twice — PASS (a stranger can picture it)
  STATUS_CHANGE: MARO Winning → Caught and sentenced in public;
    PELL Losing → Winning on the smallest thing he owns
  FACE_AT_RISK: MARO's — the whole street watches his count wiped
    off the glass
  AUDIENCE_SECRET: MARO fishes his first tile out at night and
    drops it in again (two chalk lines on one tile) · holder:
    audience · planted_in_unit: U2 (shown night beat, no line)
  AUDIENCE_KNOWLEDGE: a cold viewer walking in knows two men are
    racing to fill a jar (frame 1, mid-motion) · has never seen
    the street, the jar, or the law · expects the tall braggart
    to win; fears the small man's coat runs out — both are wrong
  QUOTABLE: "Small things sink straight."
  STANDALONE_BEAT: frame: PELL holding the double-marked tile high
    · line "One tile. Two lines. It went in twice."
  HANGER_PAID: NA — E1 opens the series; the episode's own hanger
    (the key in the jar, U5) is paid inside the episode (U6, the
    tip). No prior hanger exists.
LEGIBILITY (synthesis §3 as fields):
  SENTENCE: "Two neighbours race to fill the big jar before the
    fair. The loser carries the winner's jar home on his head."
  FRAME_1_TABLEAU: the giant glass jar centre-frame between the
    two houses, FAIR DAY line painted near its top, MARO dropping
    a chalk-white tile in from screen-left and PELL a red-stringed
    button from screen-right, both mid-motion inside the first
    second; BRAN on her stool painting the count; the stand's
    banner reads FIRST TO THE LINE
  PROOF_PICTURE: PELL holding the double-marked tile high against
    the glass (U3) — one tile, two chalk lines, produced in his
    hand, never deduced
  LOSS_PICTURE: BRAN wiping MARO's painted count off the glass
    with her sleeve (U3) + MARO's face at poster size, the grin
    gone — the loss is a body event and a wiped scoreboard in the
    same unit
  RE-SPEND COUNT: 6 / 6 (the fill race is physically on screen and
    advancing in every unit)
  PANTOMIME RETELL: PASS — jar + line + two men feeding it / the
    race under a stated law / one man cheats at night, unseen by
    the town / the twice-used tile is produced and the count
    wiped / the cheat pays in things and the honest fill rises /
    the smallest marked thing touches the line / the loser
    carries the jar and frees the winner's key by tipping it
  JOINTS: U1→U2 therefore (the law is stated, so the race runs
    under it) · U2→U3 but (the night cheat is found by its
    object) · U3→U4 therefore (the proof forces the sentence) ·
    U4→U5 therefore (the honest fill is high enough for a key to
    reach the line) · U5→U6 but (the winning key locks the
    winner out of his own house)
  VERDICT_LEDGER read for this show before production: Y (new-era/
    VERDICT_LEDGER.md — performed-ear class standing: per-take ASR
    never clears; the master is ear-read cold before delivery)
PASS 3.5 — HEAR-BEFORE-IT-MOVES: the locked script was read cold
  by the parent at lock (script-stage record in SCRIPT_E1.md lock
  notes: joint audit + quote-back candidates + spoken-load note).
  Coordinator records the lock as-is; no dialogue altered.
PASS 3.6 — DIALOGUE BUILD RECORD: parent-authored script (msg 748);
  BANTER_DRAFT and harvest are the parent's handwriting process,
  recorded in the script's lock notes; WANT_CARRIAGE: MARO → brag/
  commitment (U1), denial (U3), protest (U4) · PELL → counter-brag
  (U1), refusal (U2), accusation + demand (U3), stake + answer
  (U5) · BRAN → law (U1), sentence + refusal (U4). No "I want X"
  announcements anywhere in the script.
FLOOR_CHECK (STRANGER) — SCRIPT STAGE: recorded at script lock by
  the parent (advisory; the script locked 2026-11-27 on the user's
  story approval). Production does not re-open it.
TASTE_TEST — SCRIPT STAGE: quote-back candidates recorded in the
  script lock notes ("Small things sink straight." / "Then
  tonight, you eat air." / "What will you put in it first?");
  SHOW_OFF = MARO (the brag). Recorded; master-stage taste test
  runs on the finished master (GATE_LOG §5.4).
PASS 4 — SPOKEN-LOAD AUDIT: per-unit §4.1 blocks below, signed
  before the first video call. U1 is over the template caps
  (35 words, 3 speakers) — the script is LOCKED and the excess is
  recorded as a known production risk with a mitigation (sequential
  turns, one speaker framed per line, load-bearing law lines
  cap-exempt); it is NOT rewritten.
```

## §3 — Panel, sequence and animatic gates (before the first video call)

Panels: one PEAK panel per unit, built from the adhered character
stills (storyboard grid generated from the three character sheets,
split into panels; composition written into the still prompt per
the template's §3 rule). Panel files + md5 + read-back verdicts are
logged in GATE_LOG §3 as they land.

```
SEQUENCE GATE: contact sheet panels/contact_sheet.png (CHAR
  sheets + six PEAKs) · blind first look + odd-one-out + reads-
  silent + story-in-one-sentence recorded in GATE_LOG §3 before
  any video call. SIGNED in GATE_LOG.
ANIMATIC GATE: panels at script durations (10s each) read in
  order against the script by the coordinator; spoken-load fit
  judged per §4.1 (U1 flagged, mitigation recorded). Recorded in
  GATE_LOG §3. SIGNED in GATE_LOG.
```

```
STORYBOARD / CONTINUITY BLOCK:
  continuity_rules_block: "THE STREET: one sunlit street of painted
    wood houses; MARO's taller house screen-LEFT, PELL's smaller
    house screen-RIGHT; between them the giant clear glass jar on
    its wooden stand, taller than a man, the FAIR DAY line painted
    in white near the top of the glass and a banner on the stand
    reading FIRST TO THE LINE. MARO always enters from screen-left,
    PELL from screen-right. BRAN sits on her stool at the jar,
    paint pot and brush in hand. MARO's things are marked
    chalk-white; PELL's things are tied with red string. The count
    is painted on the glass by BRAN and by nobody else. Warm
    fair-day daylight, soft highlight roll-off."
    (written once, carried verbatim; per-frame text never restates
    or paraphrases it — unit vehicles cite it as the GLOBAL
    SETTINGS world line)
  grid_then_split: Y (six PEAK panels generated as one storyboard
    grid conditioned on the three character sheets, then split)
  carry_forward: the U1 PEAK panel hands the street, the jar and
    the axis to every later panel and to the U1 vehicle, WITH the
    restated line: "same street, same jar between the same two
    houses, same warm fair-day light; only the fill level, the
    count on the glass and the houses' emptiness change."
  high_stakes_lock: PEAK-U3 (the double-marked tile held high
    against the glass — the episode's proof picture) and PEAK-U5
    (the key touching the line) are locked as stills before any
    video spend on their units
  coverage_plan (cine-styles — master-frame-first): every dialogue
    unit is fired as ONE master frame containing the exchange —
    the speakers framed together at the jar (two-shot / three-shot
    at medium distance), never as independent single-speaker
    shots cut together; screen sides, eyelines and light
    direction lock to the master frame of U1 and are restated in
    every vehicle. Reaction beats are inside the same generation
    (the listener's face, written as a muscle recipe), not
    separate reverses.
  axis_line (cine-styles — the 180° line in words): camera stays
    on the STREET side of the jar, always south of the
    MARO–PELL axis; MARO looks screen-RIGHT, PELL looks
    screen-LEFT, BRAN faces the street (toward camera) when she
    states law and sentences; cuts change angle by ≥30° and land
    on action.
  SIGNED: coordinator, at panel sign-off (GATE_LOG §3)
```

## §4.0 — GLOBAL SETTINGS header (carried at the head of every vehicle)

```
GLOBAL SETTINGS:
  duration exactly 10 seconds · aspect: exactly 1280x720 landscape
    16:9 widescreen
  music: NONE — ambient bed instead: street air, distant fair
    murmur, glass and pottery sounds (named per unit in
    audio_layers)
  audio_layers: (1) DIALOGUE (§4.4 speech block, last and
    isolated); (2) SFX: per unit, discrete sounds tied to visible
    actions only; (3) AMBIENT BED: street air, sparrows, a distant
    fair bell (U5: the fair bell rung hard); (4) MUSIC: none.
    "- No music, No logo, no text on screen." — EXCEPT the
    declared in-world text carried per §4.4 IN-WORLD TEXT
    TECHNIQUE (the painted count + FAIR DAY line + stand banner),
    which is this world's working surface and is specified
    exactly, block by block, per unit.
  house exclusions (constant): no subtitles · no captions · no
    morphing · no duplicate characters · no camera shake · no
    text other than the declared painted blocks
  arc / world: THE BIG JAR — one street, one jar · palette: chalk
    white #F2EEE3 · glass green-blue #7FA8A0 · string red #B33A2B
    (accent, ≤10% of frame)
  grade_block (cine-styles — the world's ONE locked grade
    sentence, carried VERBATIM at the head of every vehicle):
    "Warm fair-day daylight with soft highlight roll-off and
    lifted warm shadows; chalk white and glass green-blue
    dominate, string red is the single accent; shot on 35mm
    film, fine grain, gentle halation on the glass."
```

## §4 — Per-unit vehicle skeletons

Assembly order per vehicle (fixed): GLOBAL SETTINGS header (§4.0,
grade block verbatim at its head) → duration+aspect → PREV END
STATE quote → REFERENCE PRIORITY (role sentences per image) →
LOOK/VOICE blocks verbatim → persona instance + acting fields →
action sentences (physics phases; end state restated in prose at
the close) → SPEECH BLOCK last and isolated → {END} footer:
"One continuous shot, no cuts. No text, letters or logos. No
on-screen text, no subtitles, no captions, no morphing, no
duplicate props, no camera shake." — with the declared painted
blocks named as the only text exception in the vehicle's text
blocks list.

CAMERA / LIGHT COMMON: one motivated move per unit, named with
amplitude + speed (BP-4); lighting written source+direction+
quality+colour in every vehicle: "Key: warm late-morning sun from
frame-left at 45 degrees, soft and bright, 3:1 contrast, both
eyes readable; the jar's glass throws a green-blue rim on
whatever stands beside it." (U2 night beat and U6 evening carry
their own lighting sentences, below.)

---

### U1 — THE LAW (day)

```
SPOKEN-LOAD AUDIT — U1
  camp: A (native multi) — EXCEPTION, director note: the locked
    script stages four short sequential turns at one frame; Camp B
    splitting would break the unit's single master frame. The
    load-bearing lines (BRAN's law ×2) are cap-exempt and must
    land intelligibly; the two brags are the accepted risk.
  speakers: 3 [BRAN, MARO, PELL]
  words_total: 35 · BRAN 16 · MARO 10 · PELL 9 · chars_total: ~185
  CAP CHECK: OVER the 2-speaker hard cap (18) — recorded, not
    rewritten (locked script; see §2 PASS 4 note). Mitigation:
    turns are sequential, never overlapping; one speaker framed
    in focus per line; each line ≤10 words.
  hard_words: none (all plain words; "Widow" is an address, not a
    name in prose — name hygiene kept: names appear only in the
    speech block wrappers and reference labels)
  language_accent: plain street English, all three speakers
  measured_sec: ~13–14s at performed pace if read end-to-end —
    the unit carries the lines across 10s of busy frame (painting,
    dropping, ladder going up); the audit records the overflow
    risk plainly: if a take drops a brag, the refire re-stages
    emphasis to the law lines first.
  silence_budget: lead 0.4 + internal pauses ~1.2 + turn gaps
    3 × 0.5 + tail 0.6 ≈ 3.7s · speech_window ≈ 6.3s ·
    implied_rate ≈ 5.5 wps on paper — OVER the 2.5 FAIL line as a
    continuous read; the staged reality is four separated bursts
    with action between (the script's own staging). Verdict:
    FIRE WITH RISK RECORDED (parent-locked script; fail-once
    rules govern the takes).
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed line present? Y (written per line in
    the vehicle: while one speaks, the others keep mouths closed
    and listen) · moving-hold line present? Y (both men keep
    dropping things in between turns)
  audio_layers: dialogue + street air, tile clink, brush on glass
    = 3 layers max; no music
  framing_check: speakers at medium distance, facing each other
    across the jar, mouths unobstructed? Y
  verdict: FIRE (risk recorded) · SIGNED: coordinator
PREV END STATE (opening-state block): "Before U1: the jar stands
  empty between the two whole houses; MARO's roof is whole, PELL's
  coat is buttoned; BRAN's brush is wet; the street is gathering."
REFERENCE PRIORITY:
  IDENTITY: PEAK-U1 panel (image 1 — identity + world + composition
    baked: cast relative scale is the S6 case for panel-primary)
  GEOMETRY: PEAK-U1 panel · WARDROBE: LOOK_BLOCK_VERBATIM per
    speaker + wardrobe states MARO-DUST / PELL-COAT / BRAN-PAINT
  role sentences: "Image 1: the opening frame of this exact shot —
    it defines the street, the jar, all three people's faces,
    clothes and positions; do not transfer any text from it except
    the painted count and the banner named below."
REFS_BOUND: PEAK-U1 panel (1 image)
STATE_ASSERT: at unit start, MARO is in MARO-DUST at screen-left
  already dropping a tile, PELL in PELL-COAT at screen-right
  already dropping a button, BRAN on her stool painting.
LISTENER_STATE: while BRAN states the law, both men listen with
  mouths closed, hands busy with the next thing; while MARO brags,
  PELL listens, mouth closed, eyes narrowing; while PELL answers,
  MARO listens, mouth closed, chin up.
PROOF_OBJECT: the jar itself + the FAIR DAY line (the law is
  painted on the world, not just said)
BIT: THE COUNT (the painted scoreboard starts: 1 — 1)
PERSONA_TRANSLATION: MARO chest out, pointing at his own roof ·
  PELL chin up, counting on his fingers · BRAN upright, brush
  raised, waiting for quiet before she speaks
OBJECTIVE: BRAN: bind both men to the law in public · MARO: commit
  biggest · PELL: answer the commitment
OBSTACLE: the other man's commitment
TACTICS: state → commit → counter-commit
WITHHELD: MARO will not say he will cheat; PELL will not say the
  key is already tied; BRAN will not say she has counted the roofs
EYE TASK: MARO's eyes go up to his own roof on the reaction beat
  and stay there a full beat (measuring it like a bank account)
END STATE:
  identity: MARO screen-left reaching up toward his roof; PELL
    screen-right holding another button; BRAN centre at the jar,
    brush down
  wardrobe: MARO-DUST · PELL-COAT · BRAN-PAINT (unchanged)
  prop: count "1 — 1" painted on the glass; ladder going up at
    MARO's house; UMBER's coin on MARO's side of the stand
  light: warm sun frame-left, soft, bright
ACTION / SCENE SENTENCES (close restates the end state in prose):
  both men already dropping things in as the shot opens (mid-
  motion, no settle); BRAN paints and states the law; the brags
  trade; TILO sets the ladder; SARA calls the count; the shot
  ends with the count 1 — 1 on the glass, the ladder up, both men
  reaching for the next thing.
  HOOK_TYPE (U1): RESULT-FIRST + Visible Gap — frame 1 is the
    race already running under a painted line nobody has reached
TEXT BLOCKS (in-world text technique — the only text in frame):
  text_block 1 = "1 — 1" · traits: hand-painted, uneven, white
    paint · surface: the jar's glass, beside the line
  text_block 2 = "FIRST TO THE LINE" · traits: hand-painted
    banner letters · surface: the stand's banner (established in
    the PEAK panel; the vehicle does not re-specify its wording
    beyond naming it as already painted)
SPEECH BLOCK (veo-colon-noquotes):
  BRAN (older woman, dry verdict pace, painting as she speaks):
    First marked thing to touch the line wins.
  BRAN (older woman, dry verdict pace): Loser carries the jar
    home. On his head.
  MARO (tall man, bragging upward to the street): Then start
    painting, Widow. My whole roof is coming down.
  PELL (short man, quick and exact): Your roof leaks. My coat is
    full of buttons.
  REACTION: carrier MARO's face · duration ~1.5s · follows PELL's
    line — his eyes go up to his own roof, measuring it; nobody
    speaks.
LINE LEDGER (moves): BRAN L1 state-law (REVEAL-BY-AUTHORITY /
  CARRIER: the law) · BRAN L2 state-price (REVEAL-BY-AUTHORITY) ·
  MARO brag-commit (BRAG) · PELL counter-brag (INSULT + BRAG)
KEEP_LIST: all four lines are the locked script's; cut_record:
  none (no compression at production stage — the script is the
  harvest)
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

### U2 — THE FEED, AND THE NIGHT (day → night)

```
SPOKEN-LOAD AUDIT — U2
  camp: A (native multi, 2 speakers, sequential) — director note:
    one exchange of two 8-word lines across the day frame; the
    night beat is silent by script.
  speakers: 2 [MARO, PELL] · words_total: 16 · MARO 8 · PELL 8
  CAP CHECK: inside the 2-speaker target band (14–16 total) ✓
  measured_sec: ~6.5s performed · silence_budget: lead 0.4 +
    internal 0.5 + turn gap 0.5 + tail 0.6 = 2.0s · speech_window
    ~5s (day half) · implied_rate ~2.4 wps in the day half ✓
    (the night beat is scripted silence — positive description:
    nobody speaks; only the lamp, the string, the tile)
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed Y · moving-hold Y (TILO carries the
    kettle across during the exchange)
  audio_layers: dialogue + street air (day) / lamp-quiet street,
    a string drawn through glass (night) = ≤3
  framing_check: Y
  verdict: PASS · SIGNED: coordinator
PREV END STATE (quoted from U1): "count 1 — 1 on the glass;
  ladder up at MARO's house; both men already reaching for the
  next thing."
REFERENCE PRIORITY:
  IDENTITY: U1 shipped take's last frame (image 1 — the chain:
    world, wardrobe, positions, light) · GEOMETRY: PEAK-U2 panel
    (image 2)
  role sentences: "Image 1: the previous shot's last frame — it
    defines the street, the jar and everyone's current state; the
    new shot continues from it. Image 2: this unit's composition —
    it defines where the fill and the count stand now; do not
    transfer faces from it over image 1."
REFS_BOUND: U1 last frame + PEAK-U2 panel (2 images)
  CURRENT STATE PER REFERENCE LINE: image 1 — MARO-DUST, roof
    whole, count 1—1 · image 2 — MARO-DUST with his roof half
    gone; PELL-OPEN, coat open, buttons gone, shirt tied with red
    string; count 9 — 7
STATE_ASSERT: at unit start the race has run: MARO's roof is half
  gone, tiles stacked by the jar; PELL's coat hangs open.
LISTENER_STATE: while MARO taunts, PELL listens mouth closed,
  looking at his own house (kettle, chair, door); while PELL
  refuses, MARO listens mouth closed, grin held.
PROOF_OBJECT: the stacked tiles and the open coat (the ledger read
  on bodies and houses)
BIT: THE LADDER (the count climbs: 9 — 7) + the planted cheat
PERSONA_TRANSLATION: MARO taunting, chin up · PELL flat, eyes on
  his own remaining things
OBJECTIVE: MARO: declare PELL spent · PELL: refuse the declaration
OBSTACLE: the other man's remaining house
TACTICS: taunt → refuse-by-inventory
WITHHELD: MARO will not say what he will do tonight; PELL will
  not say the key is tied and waiting
EYE TASK: PELL's eyes travel kettle → chair → door on his line
END STATE:
  identity: day: both men at the jar, count painted; night: MARO
    alone at the jar under one lamp, grinning at the glass
  wardrobe: MARO-DUST · PELL-OPEN · BRAN-PAINT (day frame)
  prop: painted count "9 — 7"; inside the jar, one tile carrying
    TWO white chalk lines
  light: day warm sun frame-left → night: one lamp, most of the
    street in darkness (lighting sentence for the night beat:
    "Key: a single street lamp above the jar, hard warm point of
    light, the rest of the street falls into darkness")
ACTION / SCENE SENTENCES: the day frame runs the feed and the
  exchange; TILO carries PELL's kettle toward the jar (the
  street's first side-switch); SARA gossips the count to a growing
  knot of neighbours; the light falls to night inside the same
  continuous shot — MARO creeps out with a string, fishes his
  FIRST tile back out of the jar and drops it in again, grinning
  at the jar; the shot ends on the tile against the glass with
  two white chalk lines, the painted count 9 — 7 beside it.
  (Day→night inside one generation is this unit's named event:
  THE NIGHT CHEAT, a time-passage, not a morph of any person.)
TEXT BLOCKS: text_block 1 = "9 — 7" · hand-painted, uneven, white
  paint · the jar's glass
SPEECH BLOCK:
  MARO (tall man, taunting, chin up): Nine tiles. Your buttons
    are finished, little man.
  PELL (short man, flat, looking at his own house): Buttons are
    finished. I still have a house.
  REACTION: carrier the tile in the jar (night) · duration ~2s ·
    follows the night beat — close on the tile: two chalk lines;
    nobody speaks.
LINE LEDGER: MARO taunt-declare (INSULT) · PELL refuse (DENY /
  CARRIER: the inventory)
KEEP_LIST: both lines · cut_record: none
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

### U3 — THE TILE (day)

```
SPOKEN-LOAD AUDIT — U3
  camp: A (native multi, 2 speakers, 3 turns) — director note:
    accusation / denial / demand is one exchange and the unit's
    whole engine; turns are short and sequential.
  speakers: 2 [PELL, MARO] · words_total: 26 · PELL 16 · MARO 10
  CAP CHECK: OVER the 2-speaker hard cap (18) — recorded, not
    rewritten (locked script). PELL's accusation (8 words) is
    cap-exempt (load-bearing); the demand (8) is its pair. The
    denial is the accepted risk line.
  measured_sec: ~10s performed end-to-end; the unit also carries
    the count-and-wipe action after the lines — lines ride the
    first ~7s, the wipe lands in the tail.
  silence_budget: lead 0.4 + turn gaps 2 × 0.5 + tail 0.8 ≈ 2.2s ·
    speech_window ≈ 7s · implied_rate ≈ 3.7 wps — over target;
    risk recorded (see U1 note; fail-once rules govern).
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed Y (the street listens; BRAN counts in
    silence after the demand) · moving-hold Y (the kettle sinks
    during the open)
  audio_layers: dialogue + street hush, glass knock, brush and
    sleeve on glass = ≤3
  framing_check: Y — PELL framed with the tile high; MARO's
    reaction at poster size in the tail
  verdict: FIRE (risk recorded) · SIGNED: coordinator
PREV END STATE (quoted from U2): "painted count 9 — 7; inside the
  jar, one tile with two marks."
REFERENCE PRIORITY:
  IDENTITY: U2 shipped take's last frame (image 1 — night frame;
    the unit OPENS by restating day: the vehicle names the return
    to warm day light as its first action sentence, constants
    named before the new action per cine #8) · GEOMETRY: PEAK-U3
    panel (image 2 — the proof picture, high_stakes_lock)
  role sentences: "Image 1: the previous shot's last frame — it
    defines the street, the jar and the tile with two marks
    inside it. Image 2: this unit's composition — PELL holding
    the double-marked tile high against the glass; it defines
    the pose and the framing, not new faces."
REFS_BOUND: U2 last frame + PEAK-U3 panel (2 images)
  CURRENT STATE: image 1 — night, MARO alone, tile double-marked
    in the jar · image 2 — day, PELL-OPEN, tile in his raised
    hand, BRAN at the jar with her counting fingers ready
STATE_ASSERT: at unit start it is day again; PELL is dropping his
  kettle in; the double-marked tile lies inside the jar.
LISTENER_STATE: while PELL accuses, MARO listens mouth closed,
  grin fixed; while MARO denies, PELL listens mouth closed,
  holding the tile higher; after the demand, everyone is silent
  while BRAN counts.
PROOF_OBJECT: THE TILE — one roof tile, two white chalk lines
BIT: THE TOO-SPECIFIC DENIAL answered by THE COUNT (the public
  test: roof gaps vs tiles, counted on fingers)
PERSONA_TRANSLATION: PELL stops dead mid-step, then holds the tile
  high, voice quiet and counted · MARO's grin goes fixed, then
  gone · BRAN counts on raised fingers for the street
OBJECTIVE: PELL: make the street see it · MARO: make the paint
  mean nothing
OBSTACLE: the object itself
TACTICS: accuse-with-proof → deny → demand the test
WITHHELD: BRAN will not say she already counted the roofs; PELL
  will not say what the sentence should be — he asks for the test,
  not the verdict
EYE TASK: MARO's eyes go from the tile to BRAN's counting fingers
  and stay there (the grin dies while he watches the count)
END STATE:
  identity: MARO at poster size, grin gone; the street seated on
    PELL's side; BRAN at the wiped glass
  wardrobe: MARO-DUST · PELL-OPEN · BRAN-PAINT
  prop: MARO's side of the painted count WIPED CLEAN off the
    glass; the double-marked tile standing on the stand in front
    of everyone; UMBER's coin now on PELL's side
  light: warm sun frame-left, soft, bright (day restored)
ACTION / SCENE SENTENCES: PELL drops his kettle in; sinking, it
  knocks the double-marked tile up against the glass; PELL stops
  dead, fishes the tile out with TILO's hook and holds it high;
  the exchange fires; BRAN counts the gaps in MARO's roof, then
  the tiles in the jar, holding up fingers for the street — the
  numbers do not match; she wipes MARO's painted count off the
  glass with her sleeve; the shot ends on MARO's face at poster
  size, the grin gone, the wiped glass beside him and the tile on
  display.
TEXT BLOCKS: none new — the painted count is WIPED in this unit
  (the wipe is the text event; no new lettering is specified)
SPEECH BLOCK:
  PELL (short man, quiet and counted, holding the tile high): One
    tile. Two lines. It went in twice.
  MARO (tall man, grin fixed): Paint is paint. That jar is full
    of my roof.
  PELL (short man, to the judge, demanding): Judge. Count his
    tiles. Then count his roof.
  REACTION: carrier MARO's face · duration ~2s · follows BRAN's
    wipe — poster-size face, grin gone; nobody speaks.
LINE LEDGER: PELL accuse (ACCUSE-WITH-PROOF / CATCHPHRASE shape:
  the count) · MARO deny (DENY / TOO-SPECIFIC DENIAL) · PELL
  demand (REVEAL-BY-AUTHORITY demanded)
KEEP_LIST: all three lines (accusation cap-exempt) · cut_record:
  none
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

### U4 — THE PAYMENT (day)

```
SPOKEN-LOAD AUDIT — U4
  camp: A (native multi, 2 speakers, 3 turns)
  speakers: 2 [BRAN, MARO] · words_total: 21 · BRAN 16 · MARO 5
  CAP CHECK: over the hard cap (18) by 3 — recorded, not
    rewritten. BRAN's sentence (11 words) is the unit's engine
    and rides as one verdict in two beats.
  measured_sec: ~8.5s performed · silence_budget: lead 0.4 +
    turn gaps 2 × 0.5 + tail 0.6 = 2.0s · speech_window ≈ 7s ·
    implied_rate ≈ 3.0 wps — over target, risk recorded.
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed Y (MARO silent through the drops;
    his face carries the beats) · moving-hold Y
  audio_layers: dialogue + street quiet, pot and chair and hat
    landing in glass = ≤3
  framing_check: Y
  verdict: FIRE (risk recorded) · SIGNED: coordinator
PREV END STATE (quoted from U3): "MARO's side of the glass wiped
  clean; the cheating tile on display; the street seated on
  PELL's side."
REFERENCE PRIORITY:
  IDENTITY: U3 shipped take's last frame (image 1) · GEOMETRY:
    PEAK-U4 panel (image 2)
  role sentences: "Image 1: the previous shot's last frame — it
    defines the street, the wiped glass and everyone's current
    state. Image 2: this unit's composition — BRAN painting three
    small pictures on the glass; it defines her pose and the
    pictures' placement, not new faces."
REFS_BOUND: U3 last frame + PEAK-U4 panel (2 images)
  CURRENT STATE: image 1 — count wiped, tile on display, street
    on PELL's side · image 2 — BRAN painting a dinner pot, a
    chair, a hat on the glass; MARO beside his house door
STATE_ASSERT: at unit start BRAN is painting the sentence on the
  glass; MARO stands by his house; his dinner, chair and hat are
  still his.
LISTENER_STATE: while BRAN sentences, MARO listens mouth closed;
  while MARO protests, BRAN listens mouth closed, brush still;
  during the drops, the whole street is silent and MARO's face
  carries each landing.
PROOF_OBJECT: the three painted pictures (the sentence as pictures
  — BRAN's rulings are pictures, not speeches) + the things
  themselves going in
BIT: THE SWORN STACK (the sentence paid item by item: dinner,
  chair, hat)
PERSONA_TRANSLATION: BRAN points with the brush — at MARO, at his
  house, at the jar · MARO carries each thing like it weighs more
  than the last
OBJECTIVE: BRAN: make the price public and payable · MARO: keep
  tonight's dinner
OBSTACLE: the law has already been stated in front of everyone
TACTICS: sentence → protest → refusal (the price stands)
WITHHELD: MARO will not say he is sorry; BRAN will not say the
  sentence could be smaller
EYE TASK: MARO's eyes stay on the pot as it sinks (the first
  payment), then drop with each thing after
END STATE:
  identity: MARO at his emptied house's open door, hat gone from
    his head; BRAN at the jar; the street quiet
  wardrobe: MARO-DUST shirt, NO HAT (the hat is in the jar) ·
    PELL-OPEN (watching) · BRAN-PAINT
  prop: the jar high and honest — the fill past PELL's things;
    inside MARO's empty house, a small fruit family's tiny table
    (texture, background, unexplained)
  light: warm sun frame-left, soft, bright
ACTION / SCENE SENTENCES: BRAN paints three small pictures on the
  glass — a dinner pot, a chair, a hat — and points at MARO, at
  his house, at the jar; the sentence and the protest and the
  refusal fire; MARO puts in his dinner (the pot, steam still
  rising), then his chair, then his hat, each sinking, the fill
  rising honestly past PELL's things; SARA carries the pot the
  last two steps for him; every drop lands on MARO's face; behind
  him his emptied house stands with its door open and a small
  fruit family carries a tiny table in; the shot ends on the high
  honest jar and MARO's empty doorway.
TEXT BLOCKS: text_block 1 = three small painted pictures (a dinner
  pot, a chair, a hat) · traits: hand-painted, simple, white
  paint · surface: the jar's glass (pictures, not words — no
  lettering specified)
SPEECH BLOCK:
  BRAN (older woman, dry verdict pace, painting): A cheat pays
    in things. His dinner. His chair. His hat.
  MARO (tall man, protesting): My dinner is tonight's dinner.
  BRAN (older woman, flat, refusing): Then tonight, you eat air.
  REACTION: carrier MARO's face · duration ~1s per drop · follows
    each thing sinking — the face changes state at every landing;
    nobody speaks during the drops.
LINE LEDGER: BRAN sentence (REVEAL-BY-AUTHORITY / CATCHPHRASE:
  the list) · MARO protest (plead) · BRAN refuse (DENY answered
  by verdict)
KEEP_LIST: all three lines · cut_record: none
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

### U5 — THE KEY (day, fair light)

```
SPOKEN-LOAD AUDIT — U5
  camp: A (native multi, 2 speakers, 3 turns)
  speakers: 2 [PELL, MARO] · words_total: 18 · PELL 10 · MARO 8
  CAP CHECK: at the 2-speaker hard cap (18) ✓ — budgeted tight:
    no extra words anywhere in the vehicle
  measured_sec: ~7.5s performed · silence_budget: lead 0.4 +
    turn gaps 2 × 0.5 + tail 1.0 (the sink and the bell) = 2.4s ·
    speech_window ≈ 6.5s · implied_rate ≈ 2.8 wps — near target;
    the sink + bell carry the tail in silence
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed Y · moving-hold Y (BRAN's hand on the
    bell rope through the exchange)
  audio_layers: dialogue + street held breath, the key sinking
    through glass, THE FAIR BELL rung hard = ≤3
  framing_check: Y — the key and the line both readable; PELL's
    palm opens the unit
  verdict: PASS · SIGNED: coordinator
PREV END STATE (quoted from U4): "the jar high and honest; MARO's
  house empty, door open, a fruit family's table inside it."
REFERENCE PRIORITY:
  IDENTITY: U4 shipped take's last frame (image 1) · GEOMETRY:
    PEAK-U5 panel (image 2 — the key touching the line,
    high_stakes_lock)
  role sentences: "Image 1: the previous shot's last frame — it
    defines the street, the high jar and everyone's current
    state. Image 2: this unit's composition — the small
    red-stringed key sinking to the painted line inside the
    glass; it defines the key's path and the framing, not new
    faces."
REFS_BOUND: U4 last frame + PEAK-U5 panel (2 images)
  CURRENT STATE: image 1 — jar high, one hand of space below the
    line; MARO hatless · image 2 — PELL-OPEN, his bare house
    behind him, the key in his open palm with a fresh red string
STATE_ASSERT: at unit start the fill stands one hand below the
  FAIR DAY line; PELL's house is bare; the key is in his palm.
LISTENER_STATE: while PELL stakes, MARO listens mouth closed,
  eyes on the key; while MARO taunts, PELL listens mouth closed,
  looking at the line; while PELL answers, MARO listens, and his
  face changes first.
PROOF_OBJECT: THE KEY — small, red-stringed, sinking straight to
  the line (the win is a body event inside the glass, not the
  painted count)
BIT: THE KEY WORD LOUDER inverted — the smallest thing wins
  (the stake shrinks, the payoff grows)
PERSONA_TRANSLATION: PELL holds the key up for the street before
  he speaks · MARO leans in, dismissive · BRAN still, hand on the
  bell rope, waiting for the touch
OBJECTIVE: PELL: end the race with the last thing he owns ·
  MARO: shrink the stake before it lands
OBSTACLE: one hand of empty glass below the line
TACTICS: stake → taunt → answer-and-act (the line and the drop
  are one beat)
WITHHELD: PELL will not say the key is his door key until the
  line forces it in U6 — here it is only "my door" by the script's
  own wording ("My last thing is my door")
EYE TASK: MARO's eyes follow the key down through the fill and
  stay on the line after it touches (his face reads the loss
  before the bell)
END STATE:
  identity: PELL lit with disbelief into joy; MARO looking from
    the jar to his own empty house; BRAN ringing the bell; TILO
    holding the bell rope for PELL (final side-switch)
  wardrobe: MARO-NO-HAT · PELL-OPEN · BRAN-PAINT
  prop: the red-stringed key resting ON the FAIR DAY line inside
    the glass; BRAN's painted final count with a star beside the
    key
  light: fair light — warm sun frame-left, brighter, the glass
    halation stronger at the touch
ACTION / SCENE SENTENCES: PELL holds the key up for the street;
  the exchange fires; PELL drops the key; it sinks straight down
  through the fill and TOUCHES the FAIR DAY line — the first
  marked thing to touch it; BRAN rings the fair bell hard and
  paints the final count with a star beside the key; the shot
  ends on the key resting on the line inside the glass, the bell
  still swinging, PELL's face open with joy and MARO's face
  turned toward his empty house.
TEXT BLOCKS: text_block 1 = the final count with a star ·
  traits: hand-painted, white paint, a five-pointed star beside
  the number · surface: the jar's glass (the exact digits are
  BRAN's running count as established — the vehicle specifies
  "the final count, with a star beside it" and the star is the
  new mark; digits follow the fill story, QC reads them for
  plausibility, not a prescribed total)
SPEECH BLOCK:
  PELL (short man, plain, holding the key up): My last thing is
    my door.
  MARO (tall man, dismissive): A key sinks nowhere. It is too
    small.
  PELL (short man, quiet, answering as he drops it): Small
    things sink straight.
  REACTION: carrier PELL's face, then MARO's · duration ~2s ·
    follows the bell — disbelief into joy on one face, the loss
    read on the other; nobody speaks.
LINE LEDGER: PELL stake (offer/stake / CARRIER: the inventory) ·
  MARO taunt (INSULT) · PELL answer (CATCHPHRASE — the episode
  QUOTABLE)
KEEP_LIST: all three lines · cut_record: none
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

### U6 — THE CARRY, AND THE KOAN (evening)

```
SPOKEN-LOAD AUDIT — U6
  camp: A (native multi by cast, one speaker only) — the koan is
    the unit's only line and it is cap-exempt (load-bearing)
  speakers: 1 [MARO] · words_total: 7 · MARO 7
  CAP CHECK: well inside every cap ✓
  measured_sec: ~3s performed · silence_budget: the unit is
    mostly carried silence — the carry, the knocking, the held
    face, the tip; speech_window ≈ 3s · implied_rate n/a (one
    line, held)
  generation_sec: 10 · span_cost_sec: 10
  non_speaker: mouth-closed Y — PELL's answer is a held face, no
    line, by script · moving-hold Y (the street walks with him)
  audio_layers: NO dialogue until the koan + evening street, the
    jar's glass creaking under its weight, footsteps, a door
    knocked twice = ≤3
  framing_check: Y — the held face at poster size is the unit's
    centre; MARO framed under the jar, breathing hard
  verdict: PASS · SIGNED: coordinator
PREV END STATE (quoted from U5): "bell ringing; the red-stringed
  key resting on the line inside the glass; BRAN's painted star."
REFERENCE PRIORITY:
  IDENTITY: U5 shipped take's last frame (image 1) · GEOMETRY:
    PEAK-U6 panel (image 2)
  role sentences: "Image 1: the previous shot's last frame — it
    defines the street, the full jar, the star on the glass and
    everyone's current state. Image 2: this unit's composition —
    MARO carrying the full jar on his head down the street; it
    defines the carry and the framing, not new faces."
REFS_BOUND: U5 last frame + PEAK-U6 panel (2 images)
  CURRENT STATE: image 1 — day, bell ringing, key on the line ·
    image 2 — evening, MARO-NO-HAT with the full jar on his head,
    PELL-OPEN at his own locked door
STATE_ASSERT: at unit start the race is over and the price is
  due: MARO lifts the jar.
LISTENER_STATE: PELL listens to the koan with mouth closed and
  does not answer in words — the held face IS the answer; the
  street walks in silence on PELL's side.
PROOF_OBJECT: the jar on the loser's head (the price paid as a
  body event) + the key sliding down the glass into PELL's hand
BIT: THE KOAN BUTTON (the episode's ending per the bible: the
  loser's question, the winner's held face)
PERSONA_TRANSLATION: MARO knees bending under the jar, both hands
  steadying it, breathing hard — the brag gone out of his posture ·
  PELL knocks on his own door like a stranger
OBJECTIVE: MARO: pay the price and ask the one question left ·
  PELL: get into his own house
OBSTACLE: the key is inside the jar on MARO's head — only the
  loser can free it, by tipping the jar he lost with (ruling (a))
TACTICS: carry → knock → koan → tip (the payment completes the
  freeing)
WITHHELD: PELL will not beg; MARO will not explain the tip before
  he does it
EYE TASK: PELL's eyes go jar → key inside it → his locked door →
  back to the jar during the held face (the whole situation read
  in one look, no line)
END STATE:
  identity: PELL holding the key high; MARO standing under the
    (now tipped, steadied) jar; BRAN painting at the glass
  wardrobe: MARO-NO-HAT · PELL-OPEN · BRAN-PAINT
  prop: the red-stringed key in PELL's open hand, held high; on
    the glass, one last small painting — a door
  light: evening — warm low sun from frame-left, long shadows,
    the street lamps not yet lit (lighting sentence: "Key: low
    warm evening sun from frame-left, long soft shadows, 4:1
    contrast, both eyes readable")
ACTION / SCENE SENTENCES: MARO lifts the full jar onto his head —
  anticipation (the crouch), action (the lift, knees bending),
  recovery (both hands steadying it) — and carries it down the
  street to PELL's house, the whole street walking with him on
  PELL's side; he stops at PELL's door, jar on head, breathing
  hard; PELL knocks on his own door, nothing, knocks again — the
  house is locked and he is outside it; the koan fires; PELL's
  answer is a held face at poster size, no line; MARO tips the
  jar, slow and careful, and the red-stringed key slides down the
  glass into PELL's open hand; the final frame holds PELL with
  the key high, MARO under the jar, BRAN painting one last small
  thing on the glass — a door.
TEXT BLOCKS: text_block 1 = one small painted door (picture, not
  words) · traits: hand-painted, simple, white paint · surface:
  the jar's glass
SPEECH BLOCK:
  MARO (tall man, jar on his head, breathing hard, quiet — the
    brag gone): What will you put in it first?
  REACTION: carrier PELL's face · duration ~2.5s · follows the
    koan — held at poster size, no line; then the tip.
LINE LEDGER: MARO koan question (the KOAN — cap-exempt,
  load-bearing; target class DELIGHT licensed: the episode's
  SHOW_OFF asks it stripped of the brag)
KEEP_LIST: the koan · cut_record: none
DURATION + ASPECT line: exactly 10 seconds, exactly 1280x720
  landscape 16:9 widescreen
```

---

## Production notes (coordinator)

- Fire order is RISK-FIRST: U1 (identity + voice + light proof)
  fires before U2–U6; units chain in order, each conditioned on
  the previous shipped take's last frame + its PEAK panel.
- FAIL-ONCE-THEN-SHIP governs every unit: first take + ONE refire;
  past the cap the best take ships with the flaw disclosed in
  GATE_LOG. Cap-exempt load-bearing lines: BRAN's law (U1),
  PELL's accusation (U3), MARO's koan (U6) — a take where a
  load-bearing line is unintelligible is a failed take.
- The painted count is a working surface: QC reads it per unit
  (1—1 · 9—7 · wiped · final count + star). The count is a
  scoreboard, never the proof (bible ruling).
- Native generated audio only. No TTS. No licensed characters.
  The ~ WuBu ~ corner bug is composited at assembly.
- Assembly: one master, single uninterrupted pass, exactly
  1440 frames / 60.000s (see GATE_LOG §5.4 for the probe record).
