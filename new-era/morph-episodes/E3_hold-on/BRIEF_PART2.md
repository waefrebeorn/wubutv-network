# PRODUCTION BRIEF — HOLD ON E3 · PART 2 (filled E3 template v4 structure)

Built on the structure of `BRIEF.md` (Part 1, filled template
v4); Part 2 inherits its gate stack, TEXT RULE, master spec
and QC method in full. Script of record: `SCRIPT_PART2.md`
— **v1, LOCKED by the parent 2026-11-23** after the
independent cold read (work/COLD_READ_PART2.md: PASS).
Dialogue is locked: production may not change, add or drop
a single word. Series continuity of record:
`RUNNING_BRIEF.md` (same directory). Vocabulary law: a
voice or face is BOUND when its asset is attached to the
generation, CARRIED when only text describes it.

## §0 — Episode header

```
SHOW: HOLD ON (morph SHOW-2, retooled docket serial)
EPISODE / PART: E3 · Part 2 (story-episode 4 in continuity;
  pays Part 1's planted docket card — TOMORROW: THE NAME HE
  WON'T WRITE — the ladder's fourth rung, the Watcher accused)
TITLE (funnel grammar): Write That I Paid — HOLD ON, Part 2
CONTINUITY_OWNER: HOLD ON Continuity Editor (RUNNING_BRIEF.md)
GENERATOR: model media.generate_video (house video tool) ·
  mode image-conditioned, fixed 10s container, 16:9
MODEL_SYNTAX: veo-colon-noquotes
VOICE_ROUTE: NATIVE_TEXT_ONLY
  WAIVER: Laura (series regular) and Marta (guest) speak on
  the native route, as in Part 1. Mitigation, all mandatory:
  VOICE_SPEC_TEXT pasted verbatim BEFORE the dialogue in
  every speaking unit; voice check per speaker at
  production; ear test as the ship blocker. Voices are
  CARRIED by text, never bound. NO delivery meta-words
  (pause / beat / delivery) may appear in any VOICE_SPEC_TEXT
  (Part 1 DECISION_LOG P-10 law).
CAST_LOG (reproducibility record, completed at delivery):
  TO BE COMPLETED AT DELIVERY in COMPLETION.json.
```

UNC does not appear in this episode; the `~ WuBu ~` hoodie
wordmark gate is vacuous (the corner bug still reads exactly
"~ WuBu ~" in gold serif — assembly verifies head and tail).

**Fail-once-then-ship (standing, TV shows):** each unit gets
its first take + ONE refire; a second failure ships the best
take with flaws disclosed. EXEMPT from the cap — refire
until they land: U4 L1 "That hand's been in your pocket all
morning." and U6 L2 "The street votes on his name tonight."
(the script's designated load-bearing lines).

**The buried-hand law (this episode's QC spine):** the
Watcher's LEFT hand stays inside his coat pocket in EVERY
unit, U1–U6, including U5 (the coat swings, the pocket
gapes, the hand stays in) and U6 (he walks away with it
still buried). A take where that hand comes out before or
during U5's reveal is a REJECT.

---

## §1 — Cast cards

```
CHARACTER: LAURA            CARD_VERSION: E3.3 (carried from E3.2, unchanged)
OFF_SCREEN: N

LOOK (bound, not described):
  LOOK_PACK: front_neutral E2_hold-on/panels/PNL-CHAR-LAURA-hero-e2.png ·
             profile E3_hold-on/panels/PNL-CHAR-LAURA-profile.png ·
             close_up E2_hold-on/panels/PNL-CHAR-LAURA-face-e2.png ·
             back_or_silhouette E3_hold-on/panels/PNL-CHAR-LAURA-back.png
  CANONICAL_FACE_REF: file new-era/morph-episodes/E2_hold-on/panels/PNL-CHAR-LAURA-face-e2.png
             sha256 2905d67bd11cf770aa5f9bff0769877892b68dfdb3213db2b80a8dd9fc60f3cb
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "adult woman, early 30s; dark brown hair in a low ponytail; forest-green work shirt with two chest pockets; dark trousers; a stub of white chalk in her hand; NO headphones"
  WARDROBE_STATES: STATE LAURA-GREEN-WORK = E2_hold-on/panels/PNL-CHAR-LAURA-hero-e2.png

VOICE (route per §0: NATIVE_TEXT_ONLY + waiver):
  VOICE_SPEC_TEXT: age early 30s · gender female · timbre dry,
    low, unhurried · pace measured, one beat per clause ·
    accent flat depot-town neutral · trait states facts, never
    pleads · breaks never breaks — every sentence lands whole,
    at the same pace, finished
    (no delivery meta-words in this text — P-10 law)
  VOICE_ENROL: file NA (native route)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: notices before she speaks →
    her eyes go to hands and held things before they go to faces
  TRAIT → OBSERVABLE_BEHAVIOUR: writes only what she can stand
    behind → her chalk hovers, unwritten, when proof is missing
  NEVER_DOES: never writes a line she has not verified ·
    never raises her voice or hurries a ruling
  NEVER_SAYS: never says "maybe" · never says "trust me"
  SPEECH_RULE: rules by testing, not by telling — she sets a
    proof running and lets it speak; she refuses in plain
    words and never explains a refusal twice
  length_trait: clipped and even — short declaratives, one
    fact per line
  SECRET: none unspent this episode — she has written one
    true line (Part 1); this episode she writes her second
  RENT: force the wall believes her chalk / block she cannot
    accuse without proof she can point at / price if she writes
    one false line, the street stops bringing her the truth

PERFORMANCE:
  MOTION_SIGNATURE: chalk hand leads every gesture · gaze to
    hands before faces · stillness behaviour: chalk hovering
    motionless mid-air · tempo slow and even · she steps
    between people instead of raising her voice

STATE (this episode):
  STATE_OPEN: LAURA-GREEN-WORK · chalk stub in hand, fresh ·
    knowledge she works the docket under the keeper · emotion
    flat, working
  STATE_CLOSE: LAURA-GREEN-WORK · chalk worn, dust on fingers ·
    knowledge she has chalked MARTA PAID in her own hand and
    given the keeper's name to the street · relationship_delta
    the street watched her write against her own keeper
```

```
CHARACTER: MARTA            CARD_VERSION: E3.3 (NEW — guest archetype: the bread-seller; built at Part 2 pre-pro)
OFF_SCREEN: N

LOOK (bound, not described):
  LOOK_PACK: front_neutral E3_hold-on/panels/PNL-CHAR-MARTA-hero.png ·
             profile E3_hold-on/panels/PNL-CHAR-MARTA-profile.png ·
             close_up E3_hold-on/panels/PNL-CHAR-MARTA-face.png ·
             back_or_silhouette E3_hold-on/panels/PNL-CHAR-MARTA-back.png
             (built 2026-11-23, eye-gated against the Laura
              panels for world/wardrobe/register match — all
              four PASS, mutually consistent; record in
              GATE_LOG_PART2.md §1)
  CANONICAL_FACE_REF: file E3_hold-on/panels/PNL-CHAR-MARTA-face.png
             sha256 bdff5b0340ef019958eb566a96deb463be4a34d5c717d9cf46d3a283c090976e
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "adult woman, late 40s; weathered face; grey-streaked dark hair tied back under a plain bone-white headscarf; bone-white work blouse under a heavy tan canvas apron with one large front pocket; a small notch knife in a sheath at the apron pocket; a small cloth coin pouch tied at her waist; dark skirt; flour dust on her hands and forearms; flat deadpan face"
  WARDROBE_STATES: STATE MARTA-BAKER-APRON = E3_hold-on/panels/PNL-CHAR-MARTA-hero.png

VOICE (route per §0: NATIVE_TEXT_ONLY + waiver):
  VOICE_SPEC_TEXT: age late 40s · gender female · timbre
    plain, work-worn, a little hoarse · pace plain and
    direct, one fact at a time · accent flat depot-town
    neutral · trait says what she paid and what she is
    owed, nothing extra · breaks never breaks — challenged,
    she repeats the fact, flatter
    (no delivery meta-words in this text — P-10 law)
  VOICE_ENROL: file NA (native route)

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: marks what is hers → she cuts
    a notch in every coin she earns, so a coin can testify
  TRAIT → OBSERVABLE_BEHAVIOUR: pays in the open → coins cross
    the counter in full view, slapped down, never slipped
  EXAMPLE_LINE: "Write that I paid, Laura."
  NEVER_DOES: never begs · never touches the wall herself
  NEVER_SAYS: never says "please" · never says a number she
    cannot show
  SPEECH_RULE: demands first and proves second — every line
    is a fact she can point at: the coin, the pocket, the wall
  length_trait: short declaratives, counts and facts; longer
    only when she contrasts (light vs hiding) — her lines run
    shorter than Laura's longest, never tumbling
    (the two designed speakers' traits DIFFER: Laura
     clipped-and-even vs Marta plain-counting)
  SECRET: none — her facts are all on the counter; what she
    does not know is who else paid the keeper
  RENT: force her stall feeds the depot corner; her notch is
    trusted / block the wall's record is the only proof the
    landlord accepts / price if the wall keeps calling her
    owing, she loses her room
  BACKSTORY_ACTIVE_FACT: she paid the keeper a notched coin
    yesterday and watched him write for everyone but her

PERFORMANCE:
  MOTION_SIGNATURE: coins handled flat-palmed and shown ·
    the notch turned to the light · stillness behaviour:
    hands still on the counter after a fact · tempo plain,
    unhurried · she steps up to the counter, never around it

STATE (this episode):
  STATE_OPEN: MARTA-BAKER-APRON · condition floury from the
    morning bake · props_held one notched coin, slapped down ·
    knowledge she paid yesterday; the wall still calls her
    owing · emotion flat, certain · relationship_delta she is
    accusing the keeper at his own wall
  STATE_CLOSE: MARTA-BAKER-APRON · condition unchanged ·
    props_held today's notched coin, held up at the bell ·
    knowledge her name stands written PAID in Laura's hand ·
    emotion flat · relationship_delta the street saw the
    keeper's pocket; her name is up
```

```
CHARACTER: THE WATCHER      CARD_VERSION: E3.3 (carried from E3.2, unchanged look)
OFF_SCREEN: N
SILENT THIS EPISODE — no lines. The accused; his buried hand testifies.

LOOK (bound, not described):
  LOOK_PACK: front_neutral E2_hold-on/panels/PNL-CHAR-WATCHER-hero-16x9.png ·
             profile E3_hold-on/panels/PNL-CHAR-WATCHER-profile.png ·
             close_up E2_hold-on/panels/PNL-CHAR-WATCHER-face-16x9.png
  CANONICAL_FACE_REF: file new-era/morph-episodes/E2_hold-on/panels/PNL-CHAR-WATCHER-face-16x9.png
             sha256 81bcf9b70b07ab2fc4cc1e53016ab06bf64582bcc5801d9ff5573e46eefb29db
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "adult man, 68; short grey stubble beard; deep-set eyes; ink-black cardigan over a bone-white shirt; sleeves pushed up; white chalk dust on fingers and forearms; holds a stub of white chalk"
  WARDROBE_STATES: STATE WATCHER-INK-CARDIGAN = E2_hold-on/panels/PNL-CHAR-WATCHER-hero-16x9.png

VOICE: NA this episode (silent).

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: is paid and does not hide it →
    he pockets a coin in plain sight, without looking down
  TRAIT → OBSERVABLE_BEHAVIOUR: keeps one hand buried → his
    LEFT hand stays inside his coat pocket the whole episode —
    chalking, taking coins, facing the bell, walking away
  NEVER_DOES: never explains the reset · never touches a thing
    someone else is holding · never brings the left hand out
  SPEECH_RULE: does not speak in docket episodes — his
    rulings are deeds; this episode his deed is a refusal:
    the hand that does not come out
  SECRET: one name on the docket is his own problem — the
    name he won't write is Marta's, bought down by the
    landlord's two coins in his pocket beside her notched one
  RENT: force his strike is the only eraser the town trusts /
    block the wall says what it is paid to say, and he is the
    one being paid / price every struck line costs him a payer

PERFORMANCE:
  MOTION_SIGNATURE: chalks one-handed, right hand only ·
    pockets coins without looking at them · stillness
    behaviour: absolute · tempo slowest in frame · his coat
    swings only when the bell cracks (U5)

STATE (this episode):
  STATE_OPEN: WATCHER-INK-CARDIGAN · chalk dust on the right
    hand's fingers · props_held chalk stub in the right hand;
    the left hand in the coat pocket, holding three coins
    (unseen) · knowledge he took two coins to keep a name
    down · emotion flat
  STATE_CLOSE: WATCHER-INK-CARDIGAN · props_held the chalk,
    lowered; the left hand still in the pocket · knowledge
    the street has seen the pocket's mouth and his name goes
    to its vote tonight · emotion flat · relationship_delta
    the keeper walked away from his own wall
```

```
CHARACTER: THE COURIER      CARD_VERSION: E3.3 (carried from E3.2, unchanged look)
OFF_SCREEN: N
SILENT THIS EPISODE — no lines. In the queue; her open hands are the contrast.

LOOK (bound, not described):
  LOOK_PACK: front_neutral E2_hold-on/panels/PNL-CHAR-COURIER-hero-16x9.png ·
             profile E3_hold-on/panels/PNL-CHAR-COURIER-profile.png ·
             close_up E2_hold-on/panels/PNL-CHAR-COURIER-face.png
  CANONICAL_FACE_REF: file new-era/morph-episodes/E2_hold-on/panels/PNL-CHAR-COURIER-face.png
             sha256 d7df976eab8f9f4c5d4c8e4c08454fb04a7e34e81944453d0ec8db84610ecb42
  REANCHOR_RULE: never chain a drifted frame; re-anchor to CANONICAL_FACE_REF
  LOOK_BLOCK_VERBATIM: "adult woman, early 30s; black bob haircut with a straight fringe; long cobalt-blue work coat; a canvas satchel on a dark strap across her body; flat deadpan face"
  WARDROBE_STATES: STATE COURIER-COBALT-COAT = E2_hold-on/panels/PNL-CHAR-COURIER-hero-16x9.png

VOICE: NA this episode (silent).

PERSONA (behaviour, not adjectives):
  TRAIT → OBSERVABLE_BEHAVIOUR: lets her hands testify → she
    holds the ring-box in both hands, open-palmed, all episode
  SECRET: she saw whose hand was at Ansel's stall (Part 1) —
    UNSPENT; she says nothing this episode either
  RENT: force her record is the town's gold standard / block
    she will not defend herself in words / price none this
    episode — she is the picture's standing contrast

PERFORMANCE:
  MOTION_SIGNATURE: hands open, palms up, offered · stillness
    behaviour: statue-still · tempo deliberate · satchel
    never leaves her shoulder

STATE (this episode):
  STATE_OPEN: COURIER-COBALT-COAT · props_held a stranger's
    ring-box in both open hands · emotion flat
  STATE_CLOSE: unchanged — the box still held, still open
```

The Peach and the Lime do NOT appear in Part 2 (picture or
voice). The Peach appears only as her name on the wall —
a PIL plate (H-1, §4 plate spec).

---

## §2 — Room gates (script stage — of record, not re-run)

```
STORYLINE DECLARATIONS:
  AUDIENCE_SECRET: none planted this episode — the audience
    sees the pocket's contents only when the street does (U5);
    the episode's withheld fact (the landlord's two coins) is
    spoken once, at U4, as Laura's noticed fact
  HANGER_PAID: H-2 (Part 1's docket card TOMORROW: THE NAME
    HE WON'T WRITE) is this episode's case; H-1 (the Peach's
    name vote) is paid in U1's background as a PIL plate —
    showrunner ruling of record (DECISION_LOG 2026-11-23):
    the street voted YES, PEACH stands chalked. Open hanger
    booked forward: H-4 — the U6 freeze question SHOULD
    LAURA WRITE THE WATCHER'S NAME?, due Part 3 U1 background.

PASS 3.5 HEAR-BEFORE-IT-MOVES + PASS 3.7 STRANGER TEST +
  QUOTE-BACK (script stage): the independent cold read of
  record is work/COLD_READ_PART2.md — PASS: full story
  retold from the dialogue alone; 14/14 lines perform an
  action, zero remark-only; all five joints therefore/but;
  quote-back landed verbatim ("My coin's in the light.
  Yours is hiding."). Three flags ruled on by the parent in
  SCRIPT_PART2.md's lock block; none blocking. The script
  LOCKED on this gate, 2026-11-23.
PASS 4 SPOKEN-LOAD AUDIT: every unit's §4.1 block signed
  below before the first video call (80 words total, every
  unit inside its cap; FULL-TALK U1 18 + U4 19, never
  adjacent; QUIET U3 8; U6 SILENCE-BEAT 11).
```

---

## §3 — Panel, Sequence and Animatic gates (before the first video call)

Panel plan for this episode. INHERITED (sha256-verified in
BRIEF.md §1/§3): LAURA hero/face · WATCHER hero/face ·
COURIER hero/face · PNL-WALL2-closeup-16x9 ·
PNL-WORLD-market-wall. BUILT at Part 2 pre-pro (generated,
read back, eye-gated, logged with sha256 + status in
GATE_LOG_PART2.md §1 before use): the MARTA set
(face/hero/profile/back) · PEAK panels, one per unit, the
unit's contract still: PNL2-PEAK-U1-coinslap (the coin
slap at the counter, frame-0 contract) ·
PNL2-PEAK-U2-notch (the notch cut at the counter) ·
PNL2-PEAK-U3-pocket (the coin taken blind, the buried
hand) · PNL2-PEAK-U4-naming (Laura between, eyes on the
pocket) · PNL2-PEAK-U5-bell (hands open at the bell, the
pocket's mouth) · PNL2-PEAK-U6-freeze (the strike, the
keeper walking away — labelled DESTINATION, never image 1).

```
SEQUENCE GATE:
  contact sheet: file E3_hold-on/work/SEQ_SHEET_E3P2.png
    (the six PEAKs; built at pre-pro)
  seq_reads_silent: must be Y — the sheet alone must tell:
    coin slapped down, notch cut, coin pocketed blind, the
    naming stare at the pocket, hands open at the bell with
    the pocket gaping, the strike and the keeper leaving
  seq_story_in_one_sentence: "A bread-seller's paid name was
    kept off the wall by the keeper's pocket; his buried
    hand convicts him at the bell, and her name goes up in
    the chalk-hand's own writing."
  SIGNED: at production — record in GATE_LOG_PART2.md §2

ANIMATIC GATE:
  animatic_file: E3_hold-on/work/animatic_E3P2.mp4 (PEAK
    panels at script durations + the §4.1 measured_sec
    timing plan as a scratch track)
  animatic_spoken_load_check: must be PASS — every line
    fits its unit at the §4.1 measured rate
  SIGNED: at production — blocking; no video call before it;
    record in GATE_LOG_PART2.md §2
```

---

## §4 — Per-unit vehicle skeletons

Verbatim blocks carried in EVERY unit prompt (assembly
order: duration+aspect → PREV END STATE → REFERENCE
PRIORITY → LOOK/VOICE verbatim → persona instance + acting
→ action sentences → SPEECH BLOCK last and isolated):

WORLD (verbatim, carried from Part 1): "A cobbled depot
street in the morning: a tall brick wall, COMPLETELY BLANK
(no writing, no marks, no lettering of any kind); a wide
wooden door set in the wall with a plain BLANK hanging sign
board above it; an iron hook beside the door; a stone
counter along the wall's base; a market stall at frame
right with a cobalt-striped awning and cadmium-yellow
crates; down the street a queue of townspeople holding
their proofs. Morning light from frame LEFT. Palette
INK / COBALT / BONE with one CADMIUM accent."
  (Per-unit awning state rides in the known-defect
  overrides, as in Part 1: U1–U2 the awning stripe is BONE;
  the U3 reset turns it COBALT; U3–U6 cobalt.)

STYLE (carried from Part 1 with one recorded deviation —
the fruit clause is dropped because no fruit character
appears in Part 2 and the clause is a population risk):
"Photorealistic live-action, cinematic, slight codec
softness, never ad-clean. Exactly 10 seconds, 16:9
widescreen, 1280x720. No captions, no subtitles, no titles,
no text or lettering anywhere in the picture; the brick
wall and the sign board stay completely blank. Flat
deadpan performances; nobody shouts, nobody weeps.
Everyone is deadpan."

VOICE_SPEC_TEXT blocks (§1 cards) are pasted verbatim
BEFORE the speech block in every unit where that
character speaks.

STANDING VEHICLE LAWS (learned in Part 1, all carried):
- ONE CONTINUOUS SHOT per unit: camera locked, no cut, no
  zoom, no reframe, unless the unit block says otherwise.
- Every governing law is stated at THREE loci (header /
  cast block, action block, closing Final block) — the
  blank-board assertion, the one-of-each-character casting
  rule, the speaker-only mouth rule, and this episode's
  buried-hand law.
- The board/plaque is a proven TEXT ATTRACTOR: if any take
  letters it, the standing refire is the BOARD-FREE
  REFRAME (the board leaves the set at every locus).
- Non-speakers: mouths closed, faces flat, no reaction
  animation inside another's speech span; each non-speaker
  carries a named held task.
- Meta-word audit before firing: no speakable delivery
  meta-words (pause / beat / delivery) anywhere in the
  vehicle outside the speech block's stage tags.

### UNIT 1 — HOOK + SETUP · MARTA

```
SPOKEN-LOAD AUDIT — U1
  camp: B (1 speaker per clip)
  speakers: 1  [MARTA]
  words_total: 18   words_by_speaker: MARTA 18   chars_total: 97
  CAP CHECK: FULL-TALK — 18 words, inside the 17–19 class
    band, within HARD CAP 20
  hard_words: none
  language_accent: MARTA — flat depot-town neutral
  measured_sec: 6.7
  silence_budget: lead 0.2s + internal_pause 0.5s
             + turn_gap NA (1 speaker) + tail 0.8s = 1.5s total
  speech_window: 10 − 1.5 = 8.5s
  implied_rate: 18 / 8.5 = 2.12 wps  [PASS — under the ≤2.5
    fail threshold; the first line lands inside 3s on the
    coin slap's ring (BLAM)]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y (Laura, the
    Watcher, the Courier: mouths closed, no speech motion) ·
    moving-hold line present? Y (the Courier holds the
    ring-box open-palmed; the Watcher chalks one-handed)
  audio_layers: dialogue + street ambience (incl. bell tick) = 2
  framing_check: speaker medium-wide at the counter / facing /
    mouth unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (opening-state block — no previous unit):
  "Opening state: morning at the wall; the docket queue is
   already moving; Marta crosses to the counter with a coin
   in her hand; Laura stands at the wall with her chalk,
   lowered; the Watcher stands at the wall chalking with his
   right hand, his left hand in his coat pocket; the Courier
   waits in the queue holding a small ring-box in both open
   hands."
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-MARTA-face · GEOMETRY: PNL-WORLD-market-wall ·
  WARDROBE: PNL-CHAR-MARTA-hero
  known-defect overrides (POSITIVE statements only): the
  wall's brick field is bare, evenly lit brick; the stall
  awning's stripe is bone-white; the coin is one plain coin
  with a small notch cut in its edge
REFS_BOUND: PNL-WORLD-market-wall (image 1, world anchor) ·
  PNL2-PEAK-U1-coinslap (image 2, the unit's contract still) ·
  PNL-CHAR-MARTA-face (image 3, speaker identity — P-10 fix) ·
  LAURA hero · WATCHER hero · COURIER hero (carried slots)
PRIMARY_BOUND_CHARACTER: MARTA (all others prompt-carried)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, Marta is in wardrobe state
  MARTA-BAKER-APRON, one notched coin in her hand, condition
  floury from the morning bake.
PROOF_OBJECT: the notched coin — the demand is made OVER
  the coin: slapped flat on the counter at frame 0, it
  spins and settles notch-up while she speaks. The claim
  is never reported; it is slammed down.
CHAIN: outgoing last frame (harvested after conform) = image 1
  for U2 · gated PEAK = image 2

PERSONA_INJECTION: PER_UNIT — Marta pays in the open and
  demands in facts: the coin lands before the words do.
PERSONA_TRANSLATION: coin hand leading; gaze counter →
  Laura → the wall; tempo plain and unhurried; line-reading
  flat, a fact stated at a counter, not a plea
OBJECTIVE: to get her name written as paid, today
OBSTACLE: the keeper at the wall is not writing it — he
  chalks on, one-handed, and does not turn
TACTICS: slaps the proof down → names where yesterday's
  coin went → names what the wall still says
  (change: from demanding to indicting the record)
EYE TASK: on the coin at the slap, up to Laura for the
  demand, across to the wall for the owing line; no eye
  contact with camera at any point
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: Frame 0 is mid-motion: Marta's
  hand is already coming down as the picture opens; the
  coin SLAPS flat onto the stone counter and spins,
  clattering, inside the first second (BLAM — named
  impact: the coin's slap and ring, ≤1.0s in; no dead
  head; no ramp-from-rest; the queue is already walking).
  The notch cut in the coin catches the light as it
  settles. The queue moves behind her. The Watcher stands
  at the wall chalking with his right hand; his left hand
  is inside his coat pocket and stays there. In the queue
  the Courier holds a small ring-box in both open hands,
  palms up. Laura stands at the wall, chalk lowered,
  watching the coin. Nobody writes anything in this shot.
DELIVERY_NOTE per line: L1 flat and direct, the demand
  thrown at Laura as the coin settles; L2 level, the fact
  aimed past Laura at the keeper's back — "his pocket"
  lands the weight; L3 at the wall itself, the record
  indicted in plain words
LINE LEDGER:
  L1 · line_move: demand · line_target: Laura ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "Laura"
  L2 · line_move: accuse · line_target: the Watcher ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "yesterday"
  L3 · line_move: indict · line_target: the wall ·
    line_genre_move: ENTER-CONTRADICT · payload word last: "rent"
SPEECH BLOCK:
  MARTA (coin settling, flat): Write that I paid, Laura.
  MARTA (level, past Laura): My coin went in his pocket yesterday.
  MARTA (at the wall): Wall still says I owe the rent.
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field and the hanging sign board — described as blank,
  unmarked brick and bare wood texture. PIL plates
  (assembly): the Part 2 wall stack — MARTA — OWES THE
  RENT (fresh docket hand) with the blank space beside it;
  PEACH small and fresh above; weathered below: the struck
  SHE HELD MY TIN. MY COINS ARE GONE. and HANDS OPEN.
  COINS LOOSE. from Part 1. No other text this unit.
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Marta at the counter, hand flat on the
    stone beside the settled coin; Laura at the wall, chalk
    lowered, looking at the coin; the Watcher at the wall,
    chalking one-handed; the Courier in the queue, ring-box
    held open-palmed; the queue behind
  end_state.wardrobe: Marta in MARTA-BAKER-APRON; Laura in
    LAURA-GREEN-WORK; the Watcher in WATCHER-INK-CARDIGAN,
    left hand in his coat pocket
  end_state.prop: one notched coin at rest on the stone
    counter, notch up; the ring-box in the Courier's hands
  end_state.light: morning light from frame left, cool bone daylight
```

### UNIT 2 — PROOF · LAURA

```
SPOKEN-LOAD AUDIT — U2
  camp: B (1 speaker per clip)
  speakers: 1  [LAURA]
  words_total: 13   words_by_speaker: LAURA 13   chars_total: 71
  CAP CHECK: MIXED — 13 words, inside the 12–15 class band
  hard_words: none
  language_accent: LAURA — flat depot-town neutral
  measured_sec: 4.8
  silence_budget: lead 0.4s + internal_pause 0.45s
             + turn_gap NA + tail 0.6s = 1.45s total
  speech_window: 10 − 1.45 = 8.55s
  implied_rate: 13 / 8.55 = 1.52 wps  [PASS]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y (Marta works the
    knife with her mouth closed; the Watcher chalks, silent) ·
    moving-hold line present? Y (the notch being cut is the
    unit's moving hold; the Watcher's chalk keeps moving)
  audio_layers: dialogue + street ambience (incl. bell tick) = 2
  framing_check: speaker medium close-up / facing / mouth
    unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (quoted verbatim from U1's §4):
  "end_state.identity: Marta at the counter, hand flat on the
    stone beside the settled coin; Laura at the wall, chalk
    lowered, looking at the coin; the Watcher at the wall,
    chalking one-handed; the Courier in the queue, ring-box
    held open-palmed; the queue behind
  end_state.wardrobe: Marta in MARTA-BAKER-APRON; Laura in
    LAURA-GREEN-WORK; the Watcher in WATCHER-INK-CARDIGAN,
    left hand in his coat pocket
  end_state.prop: one notched coin at rest on the stone
    counter, notch up; the ring-box in the Courier's hands
  end_state.light: morning light from frame left, cool bone daylight"
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-LAURA-face-e2 · GEOMETRY: PNL-WORLD-market-wall ·
  WARDROBE: PNL-CHAR-LAURA-hero-e2
  known-defect overrides (POSITIVE statements only): the
  awning stripe is bone-white; the knife is a small plain
  knife; today's coin is plain until the notch is cut
REFS_BOUND: U1 outgoing last frame (image 1) ·
  PNL2-PEAK-U2-notch (image 2) · PNL-CHAR-LAURA-face-e2
  (image 3, speaker identity — P-10 fix) · PNL-CHAR-MARTA-hero
PRIMARY_BOUND_CHARACTER: LAURA (Marta is bound by her hero
  panel as the picture's second figure)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, Laura is in wardrobe state
  LAURA-GREEN-WORK, holding her chalk stub, lowered.
PROOF_OBJECT: the notch — cut fresh into today's coin on
  camera: the proof is manufactured in front of the street,
  and Laura states its rule while it happens.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2

PERSONA_INJECTION: PER_UNIT — Laura does not lift the
  chalk: she steps to Marta and reads the proof instead —
  her hand stops Marta's reach toward the wall, palm down.
PERSONA_TRANSLATION: gaze coin → Marta's hands → down the
  wall to the keeper; tempo slow and even; line-reading
  flat, a rule noticed aloud, not taught
OBJECTIVE: to make the coin testify before anyone chalks
OBSTACLE: Marta's demand is already loud; the keeper is
  already not listening
TACTICS: stops the chalk-ward reach → watches the notch
  cut → states what the notch means for the pocket
  (change: from refusing to proving)
EYE TASK: on Marta's hands and the knife for the cut, then
  down the wall to the Watcher's pocket on the second line
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: Laura steps to the counter and
  sets her palm down between Marta and the wall — no chalk
  on a say-so. Marta takes her little notch knife from her
  apron pocket and cuts a fresh notch into today's coin on
  the stone, the way she has cut every coin she ever
  earned; the notch flashes as she turns the coin. Down
  the wall the Watcher chalks the next man's line,
  one-handed, unhurried; his left hand does not leave his
  coat pocket. Laura watches the coin, then looks down the
  wall, and says what the notch means.
DELIVERY_NOTE per line: L1 even, noticed aloud, the rule
  stated as a fact of the street; L2 a half-tone lower,
  aimed down the wall — the accusation carried by the
  noticing, payload on "yours"
LINE LEDGER:
  L1 · line_move: notice · line_target: Marta ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "notch"
  L2 · line_move: accuse-by-proof · line_target: the Watcher ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "yours"
SPEECH BLOCK:
  LAURA (watching the coin, flat): Every coin you earn wears a notch.
  LAURA (down the wall, lower): One in his pocket wears yours.
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field (the Part 2 wall stack persists as PIL plates from
  U1, unchanged) and the hanging sign board — blank,
  unmarked. PIL plates: the U1 stack only; no new text.
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Marta at the counter holding today's
    notched coin up, notch to the light; Laura beside her,
    chalk still lowered, gaze down the wall; the Watcher at
    the wall chalking one-handed, left hand in his pocket
  end_state.wardrobe: states as opened
  end_state.prop: today's coin notched, in Marta's raised
    hand; the exhibit coin (U1's) still on the counter
  end_state.light: morning light from frame left, cool bone daylight
```

### UNIT 3 — TWIST · MARTA · QUIET

```
SPOKEN-LOAD AUDIT — U3
  camp: B (1 speaker per clip)
  speakers: 1  [MARTA]
  words_total: 8   words_by_speaker: MARTA 8   chars_total: 43
  CAP CHECK: QUIET — 8 words, inside the 5–8 class band;
    the unit's head is the scripted REACTION (GAP 1)
  hard_words: none
  language_accent: MARTA — flat depot-town neutral
  measured_sec: 3.0
  silence_budget: lead 2.0s (REACTION — DIGESTION GAP 1 at
             the unit's head, carrier OBJECT: the notched
             coin in Marta's open palm, bell ticking, no
             words — a scripted beat in the SPEECH BLOCK)
             + internal_pause 0.4s + tail 1.6s = 4.0s total
  speech_window: 10 − 4.0 = 6.0s
  implied_rate: 8 / 6.0 = 1.33 wps  [PASS]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y · moving-hold
    line present? Y (the Watcher takes the coin and pockets
    it without looking down — a moving hold broken by the
    accused, which is the unit's event)
  audio_layers: dialogue + street ambience (bell tick
    prominent in the gap) = 2
  framing_check: speaker medium close-up at the counter /
    facing / mouth unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (quoted verbatim from U2's §4):
  "end_state.identity: Marta at the counter holding today's
    notched coin up, notch to the light; Laura beside her,
    chalk still lowered, gaze down the wall; the Watcher at
    the wall chalking one-handed, left hand in his pocket
  end_state.wardrobe: states as opened
  end_state.prop: today's coin notched, in Marta's raised
    hand; the exhibit coin (U1's) still on the counter
  end_state.light: morning light from frame left, cool bone daylight"
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-MARTA-face · GEOMETRY: PNL-WORLD-market-wall ·
  WARDROBE: PNL-CHAR-MARTA-hero
  known-defect overrides (POSITIVE statements only): the
  awning stripe is cobalt now; every other element of the
  street matches the previous unit exactly
REFS_BOUND: U2 outgoing last frame (image 1) ·
  PNL2-PEAK-U3-pocket (image 2) · PNL-CHAR-MARTA-face
  (image 3, speaker identity — P-10 fix) · WATCHER hero
PRIMARY_BOUND_CHARACTER: MARTA (the Watcher is bound by his
  hero panel as the picture's second figure)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, Marta is in wardrobe state
  MARTA-BAKER-APRON, today's notched coin in her open palm.
PROOF_OBJECT: today's coin — held close at the gap, then
  paid across the counter into the keeper's blind pocket:
  the proof object is swallowed by the accused on camera.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2

PERSONA_INJECTION: PER_UNIT — Marta pays in the open a
  second time, knowing what the street now knows; her lines
  count the cost and name the refusal, nothing more.
PERSONA_TRANSLATION: palm open and still through the gap;
  gaze coin → the keeper's face → the wall; tempo plain;
  line-reading flat counts, no rise
OBJECTIVE: to be heard today — to make him write for her
  in front of everyone
OBSTACLE: he takes the coin the way he took yesterday's —
  blind — and writes for the next man instead
TACTICS: holds the proof through the bell's tick → pays
  it across → counts the cost → exposes the refusal
  (change: from paying to testifying)
EYE TASK: Marta's eyes stay on the coin through the gap,
  rise to the Watcher's face as he takes it, and follow
  his chalk to the next man's line on the second line
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: The unit opens held: today's
  notched coin in Marta's open palm in close view, the
  bell ticking, nobody speaking, two seconds (REACTION —
  DIGESTION GAP 1). The bell has rung in the reset; the
  street has changed in exactly one detail: the stall
  awning's stripe is cobalt where it was bone; everything
  else is as it was. The queue shuffles one step up. The
  Watcher chalks a line for the man ahead of Marta at
  once — writes for him without a blink. Marta steps up
  and holds out today's notched coin to be heard. The
  Watcher takes it and pockets it without looking down,
  turns back to the wall, and chalks the NEXT man's line.
  Not hers. His left hand never leaves his coat pocket;
  he has chalked one-handed all morning.
DELIVERY_NOTE per line: L1 flat, after he pockets the
  coin — the cost counted in four words; L2 level, to the
  street as much as to him — the refusal named in plain
  words, payload on "me"
LINE LEDGER:
  REACTION (GAP 1) · line_move: react · line_target: the
    street (the held object addresses no one) ·
    line_genre_move: NONE (a scripted silence — A-4
    exemption; carrier OBJECT) · follows_line U2 L2
  L1 · line_move: count the cost · line_target: the Watcher ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "now"
  L2 · line_move: expose · line_target: the street ·
    line_genre_move: ENTER-CONTRADICT · payload word last: "me"
SPEECH BLOCK:
  REACTION: carrier object (today's notched coin in Marta's open palm) · duration 2.0s · follows_line U2 L2
  MARTA (flat, after the pocketing): Paid him twice now.
  MARTA (level, to the street): He writes for everyone but me.
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field (the Part 2 wall stack persists as PIL plates) and
  the hanging sign board — blank, unmarked, re-asserted
  here with the action block. PIL plates: the U1 stack only.
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Marta at the counter, her hand empty
    now, palm still open; the Watcher turned back to the
    wall, chalking the next man's line one-handed; Laura
    watching from beside the counter; the queue shifted
    one step
  end_state.wardrobe: states as opened; the awning stripe cobalt
  end_state.prop: today's coin gone into the Watcher's
    right-side pocket (unseen); the exhibit coin still
    on the counter
  end_state.light: morning light from frame left, cool bone daylight
```

### UNIT 4 — CLASH · LAURA

```
SPOKEN-LOAD AUDIT — U4
  camp: B (1 speaker per clip)
  speakers: 1  [LAURA]
  words_total: 19   words_by_speaker: LAURA 19   chars_total: 103
  CAP CHECK: FULL-TALK — 19 words, at the 17–19 class
    ceiling, within HARD CAP 20. L1 is LOAD-BEARING
    (exempt from the fail-once cap — refire until it lands)
  hard_words: none
  language_accent: LAURA — flat depot-town neutral
  measured_sec: 7.0
  silence_budget: lead 0.3s + internal_pause 0.5s
             + turn_gap NA + tail 0.5s = 1.3s total
  speech_window: 10 − 1.3 = 8.7s
  implied_rate: 19 / 8.7 = 2.18 wps  [PASS — under the ≤2.5
    fail threshold; three short lines in separated spans]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y (the Watcher's
    mouth stays closed — he answers nothing; Marta silent) ·
    moving-hold line present? Y (his chalk stops mid-air —
    a hold arrested, the unit's picture event)
  audio_layers: dialogue + street ambience (incl. bell tick) = 2
  framing_check: speaker medium close-up / facing / mouth
    unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (quoted verbatim from U3's §4):
  "end_state.identity: Marta at the counter, her hand empty
    now, palm still open; the Watcher turned back to the
    wall, chalking the next man's line one-handed; Laura
    watching from beside the counter; the queue shifted
    one step
  end_state.wardrobe: states as opened; the awning stripe cobalt
  end_state.prop: today's coin gone into the Watcher's
    right-side pocket (unseen); the exhibit coin still
    on the counter
  end_state.light: morning light from frame left, cool bone daylight"
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-LAURA-face-e2 · GEOMETRY: PNL-WORLD-market-wall ·
  WARDROBE: PNL-CHAR-LAURA-hero-e2
  known-defect overrides (POSITIVE statements only): the
  Watcher's left hand is inside his coat pocket in every
  frame; his chalk is in his right hand
REFS_BOUND: U3 outgoing last frame (image 1) ·
  PNL2-PEAK-U4-naming (image 2) · PNL-CHAR-LAURA-face-e2
  (image 3, speaker identity — P-10 fix) · PNL-CHAR-WATCHER-face-16x9
PRIMARY_BOUND_CHARACTER: LAURA (the Watcher is bound by his
  face panel as the picture's second figure)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, Laura is in wardrobe state
  LAURA-GREEN-WORK, holding her chalk stub, condition focused.
PROOF_OBJECT: the pocket — the clash is fought over the
  hand nobody can see: Laura's lines name it, price it,
  and order it out. The object under accusation is an
  absence the whole street has been looking at all morning.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2

PERSONA_INJECTION: PER_UNIT — Laura steps between people
  instead of raising her voice; she names only what she
  can point at — and she points at a pocket.
PERSONA_TRANSLATION: body placed between Marta and the
  wall; gaze drops to his pocket and stays; tempo even,
  unhurried; line-reading flat — the noticed fact, the
  price, the order, in three separate spans
OBJECTIVE: to make the keeper answer for the buried hand
  in front of the street
OBSTACLE: he answers nothing; his silence is his authority
TACTICS: names the buried hand → prices it with the
  landlord's boy's two coins → orders it out
  (change: from noticing to ruling the test)
EYE TASK: Laura's eyes drop to the pocket on the first
  line and do not leave it; the Watcher's eyes stay on
  Laura — dead or wandering eyes on either = reject (F-23)
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: Laura steps in between Marta
  and the wall and faces the Watcher. The queue goes
  quiet. She names what she has been watching all morning,
  then the second fact, then the order. The Watcher says
  nothing. His chalk stops mid-air. His left hand does
  not leave his coat pocket. Marta stands behind Laura,
  watching the pocket too.
DELIVERY_NOTE per line: L1 flat and level, the noticed
  fact named like a count — the whole case in one line,
  payload on "morning"; L2 lower, the price stated as
  record, payload on "coins"; L3 short and final, an
  order given the way she gives instructions to the
  street — no rise, no repeat
LINE LEDGER:
  L1 · line_move: name · line_target: the Watcher ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "morning"
    LOAD-BEARING LINE — exempt from the fail-once cap
  L2 · line_move: price it · line_target: the Watcher ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "coins"
  L3 · line_move: order · line_target: the Watcher ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "out"
SPEECH BLOCK:
  LAURA (flat, eyes on the pocket): That hand's been in your pocket all morning.
  LAURA (lower, as record): Yesterday the landlord's boy paid it two coins.
  LAURA (short, final): Bring it out.
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field (the Part 2 wall stack persists as PIL plates) and
  the hanging sign board — blank, unmarked, re-asserted
  with the action block. PIL plates: the U1 stack only.
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Laura between Marta and the wall,
    facing the Watcher, eyes on his pocket; the Watcher
    facing her, chalk stopped mid-air in his right hand,
    left hand in his coat pocket; Marta behind Laura; the
    queue silent
  end_state.wardrobe: states as opened
  end_state.prop: the chalk arrested in the Watcher's right
    hand; the exhibit coin still on the counter
  end_state.light: morning light from frame left, cool bone daylight
```

### UNIT 5 — THE BELL BREAKS THE LIE · MARTA

```
SPOKEN-LOAD AUDIT — U5
  camp: B (1 speaker per clip)
  speakers: 1  [MARTA]
  words_total: 11   words_by_speaker: MARTA 11   chars_total: 60
  CAP CHECK: MIXED-low — 11 words by design (the unit is
    the bell and the pocket's mouth; the lines only ratify)
  hard_words: none
  language_accent: MARTA — flat depot-town neutral
  measured_sec: 4.1
  silence_budget: lead 2.0s (REACTION — DIGESTION GAP 2 at
             the unit's head, carrier FACE: the Watcher's
             face, the pocketed hand low in frame, no words)
             + internal_pause 0.45s + tail 0.5s = 2.95s total
  speech_window: 10 − 2.95 = 7.05s
  implied_rate: 11 / 7.05 = 1.56 wps  [PASS]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y · moving-hold
    line present? Y (every hand at the wall comes up or
    holds open at the bell — except one; the coat's swing
    is the unit's motion event)
  audio_layers: dialogue + street ambience + the bell's
    crack = 3 (the bell is this unit's named sound event;
    no music)
  framing_check: speaker medium-wide / facing / mouth
    unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (quoted verbatim from U4's §4):
  "end_state.identity: Laura between Marta and the wall,
    facing the Watcher, eyes on his pocket; the Watcher
    facing her, chalk stopped mid-air in his right hand,
    left hand in his coat pocket; Marta behind Laura; the
    queue silent
  end_state.wardrobe: states as opened
  end_state.prop: the chalk arrested in the Watcher's right
    hand; the exhibit coin still on the counter
  end_state.light: morning light from frame left, cool bone daylight"
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-MARTA-face · GEOMETRY: PNL-WORLD-market-wall ·
  WARDROBE: PNL-CHAR-MARTA-hero
  known-defect overrides (POSITIVE statements only): the
  coins in the pocket's mouth are three plain coins, one
  with a small notch in its edge; the Watcher's left hand
  stays inside the pocket — only the coat swings
REFS_BOUND: U4 outgoing last frame (image 1) ·
  PNL2-PEAK-U5-bell (image 2) · PNL-CHAR-MARTA-face
  (image 3, speaker identity — P-10 fix) · WATCHER hero
PRIMARY_BOUND_CHARACTER: MARTA (the Watcher is bound by his
  hero panel as the picture's second figure — his coat and
  pocket carry the reveal)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, the Watcher is in wardrobe
  state WATCHER-INK-CARDIGAN, left hand in his coat pocket,
  condition cornered and flat.
PROOF_OBJECT: the pocket's mouth — the proof testifies
  itself this unit: the bell swings the coat and the
  street sees three coins, one notched. No character has
  to argue it.
CHAIN: outgoing last frame = image 1 · gated PEAK = image 2

PERSONA_INJECTION: PER_UNIT — Marta holds her coin the
  way the bell counts: up, open, in the light; her lines
  rule the event and state the contrast, nothing more.
PERSONA_TRANSLATION: palm up and still; gaze from her own
  coin across to his pocket; tempo plain; line-reading
  flat — an event ruled, then a contrast stated
OBJECTIVE: to let the bell make the accusation she cannot
OBSTACLE: two seconds of held silence in which the street
  could look away
TACTICS: holds her coin in the light through the crack →
  rules the event → states the contrast
  (change: from paying to judging)
EYE TASK: the held face is the Watcher's — his eyes stay
  on the street for the full two seconds of GAP 2 before
  the bell; dead or wandering eyes on this hold = reject
  (F-23); Marta's eyes go from her coin to his pocket
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: The unit opens held on the
  Watcher's face, the pocketed hand low in frame, the
  bell ticking, nobody speaking, two seconds (REACTION —
  DIGESTION GAP 2). The noon bell cracks. Along the wall,
  hands do what the bell counts: the Courier's stay open
  around the ring-box; Marta takes the exhibit
  coin from the counter and holds it up in her open
  palm — held, it stays hers, in the light. The Watcher's right hand rises with the chalk.
  His left stays in his pocket. The bell's crack swings
  his coat on its hook of a shoulder — and the pocket
  gapes: three coins sit in its mouth, and one of them
  wears a fresh-cut notch, catching the light exactly as
  Marta's did on the counter. The street sees it. Marta
  speaks over the settled sight.
  Named event (if any): the pocket's mouth (the episode's turn)
DELIVERY_NOTE per line: L1 flat, after the crack — the
  event ruled in three words, payload on "Watcher"; L2
  the contrast, plain and final — her coin named first,
  his second, the payload left on "hiding"
LINE LEDGER:
  REACTION (GAP 2) · line_move: react · line_target: the
    room (the held face addresses no one) ·
    line_genre_move: NONE (scripted silence — A-4
    exemption; carrier FACE) · follows_line U4 L3
  L1 · line_move: rule the event · line_target: the Watcher ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "Watcher"
  L2 · line_move: contrast-accuse · line_target: the Watcher ·
    line_genre_move: ACCUSE-WITH-PROOF · payload word last: "hiding"
SPEECH BLOCK:
  REACTION: carrier face (the Watcher's face, the pocketed hand low in frame) · duration 2.0s · follows_line U4 L3
  MARTA (after the crack, flat): Bell rang, Watcher.
  MARTA (plain, final): My coin's in the light. Yours is hiding.
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field (the Part 2 wall stack persists as PIL plates) and
  the hanging sign board — blank, unmarked. PIL plates:
  the U1 stack only; no new text this unit.
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Marta at the counter, palm up, her
    notched coin in the light; the Watcher with his right
    hand raised, chalk in it, his coat swung open at the
    pocket, three coins showing in its mouth, his left
    hand still inside the pocket; the Courier's hands open
    around the ring-box; Laura watching the pocket; the
    queue staring
  end_state.wardrobe: states as opened; the Watcher's coat
    swung at the left side
  end_state.prop: three coins in the pocket's mouth, one
    with a fresh-cut notch; the exhibit coin in Marta's
    open palm, held to the light
  end_state.light: morning light from frame left, cool bone daylight
```

### UNIT 6 — CONSEQUENCE · LAURA · SILENCE-BEAT

```
SPOKEN-LOAD AUDIT — U6
  camp: B (1 speaker per clip)
  speakers: 1  [LAURA]
  words_total: 11   words_by_speaker: LAURA 11   chars_total: 59
  CAP CHECK: SILENCE-BEAT — 11 words, inside the class
    band (the unit is deeds: the strike, the true line,
    the offered chalk refused, the keeper leaving). L2 is
    LOAD-BEARING (exempt from the fail-once cap)
  hard_words: none
  language_accent: LAURA — flat depot-town neutral
  measured_sec: 4.1
  silence_budget: lead 0.3s + internal_pause 0.45s
             + turn_gap NA + tail 3.0s = 3.75s total
             (tail includes DIGESTION GAP 3: the final 2.5s
              freeze, picture-only, written in the SPEECH
              BLOCK as a REACTION entry)
  speech_window: 10 − 3.75 = 6.25s
  implied_rate: 11 / 6.25 = 1.76 wps  [PASS]
  generation_sec: 10   span_cost_sec: 10  (CONTAINER LAW)
  non_speaker: mouth-closed line present? Y · moving-hold
    line present? Y (Laura's chalk moves twice — the strike
    and the writing; the Watcher's walk away is the unit's
    second motion)
  audio_layers: dialogue + street ambience = 2
  framing_check: speaker medium-wide at the wall / facing /
    mouth unobstructed? Y
  verdict: PASS
  SIGNED (Pass 4): Part 2 production coordinator, 2026-11-23

PREV END STATE (quoted verbatim from U5's §4):
  "end_state.identity: Marta at the counter, palm up, her
    notched coin in the light; the Watcher with his right
    hand raised, chalk in it, his coat swung open at the
    pocket, three coins showing in its mouth, his left
    hand still inside the pocket; the Courier's hands open
    around the ring-box; Laura watching the pocket; the
    queue staring
  end_state.wardrobe: states as opened; the Watcher's coat
    swung at the left side
  end_state.prop: three coins in the pocket's mouth, one
    with a fresh-cut notch; the exhibit coin in Marta's
    open palm, held to the light
  end_state.light: morning light from frame left, cool bone daylight"
REFERENCE PRIORITY:
  IDENTITY: PNL-CHAR-LAURA-face-e2 · GEOMETRY: PNL-WALL2-closeup-16x9
  (the wall field for the strike and the true line) ·
  WARDROBE: PNL-CHAR-LAURA-hero-e2
  known-defect overrides (POSITIVE statements only): the
  wall's chalk field is bare brick at unit start except
  the standing wall stack (a post plate, not generated)
REFS_BOUND: U5 outgoing last frame (image 1) ·
  PNL2-PEAK-U6-freeze (image 2 — the PEAK is the strike
  and the keeper leaving; the panel is labelled DESTINATION
  and may never be image 1) · PNL-CHAR-LAURA-face-e2
  (image 3, speaker identity) · WATCHER hero · WALL2 closeup
PRIMARY_BOUND_CHARACTER: LAURA (the Watcher is
  prompt-carried this unit)
VOICE_REF_CLIP: NA (native route)
STATE_ASSERT: at unit start, Laura is in wardrobe state
  LAURA-GREEN-WORK, holding her chalk stub, condition resolved.
PROOF_OBJECT: the chalk — the settlement is written in
  her hand on camera: the strike through OWES and MARTA
  PAID beneath it. The writing IS the closing argument.
CHAIN: outgoing last frame = the episode's freeze (no U7)

PERSONA_INJECTION: PER_UNIT — Laura writes only what she
  can stand behind: the true line goes up in her own hand;
  his name does not, because the street has not spoken.
PERSONA_TRANSLATION: chalk moving with certainty for the
  first time today; gaze line → the offered chalk → the
  walking man; line-reading quiet, addressed to Marta and
  the street, not to camera
OBJECTIVE: to close the case on the wall and hand the
  keeper's name to the street, tonight
OBSTACLE: the chalk she holds out to him — he could take
  it and write his own name; he refuses by leaving
TACTICS: strikes the owing line → writes PAID in her own
  hand → offers him the chalk → gives his name to the
  street's vote (change: from writing to handing over)
EYE TASK: Laura's eyes stay on the wall through the
  writing, follow the offered chalk to his face, and stay
  on his back as he leaves; she does not look at camera
PERFORMANCE_SOURCE: TEXT_ONLY (stricter gate applies)
ACTION / SCENE SENTENCES: Laura chalks with her own hand:
  she strikes one stroke through the owing line's place
  on the blank wall and writes beneath it — the wall is
  generated BLANK; the letters are a post layer, her hand
  moves as if writing. She holds the chalk out toward the
  Watcher — his name is his to write or refuse. He looks
  at the chalk, turns, and walks away from his own wall
  down the street, his left hand still in his pocket.
  The queue watches the keeper leave the wall standing.
  Laura gives Marta the result, then gives his name to
  the street. The picture freezes on the wall and the
  walking man for the final two to three seconds
  (REACTION — DIGESTION GAP 3).
  Named event (if any): the strike (the record corrected
  by the chalk-hand's own hand, against her keeper)
DELIVERY_NOTE per line: L1 quiet, to Marta — the result
  handed over in four words, payload on "Marta"; L2
  slower, to the street — the decider named (the street)
  and the time named (tonight), no procedure word; the
  freeze does the asking
LINE LEDGER:
  L1 · line_move: hand over · line_target: Marta ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "Marta"
  L2 · line_move: refer · line_target: the street ·
    line_genre_move: REVEAL-BY-AUTHORITY · payload word last: "tonight"
    LOAD-BEARING LINE — exempt from the fail-once cap
  REACTION (GAP 3) · line_move: react · line_target: the
    street (the frozen room) · line_genre_move: NONE
    (scripted silence — A-4 exemption) · follows_line U6 L2
SPEECH BLOCK:
  LAURA (to Marta, quiet): Your name's up, Marta.
  LAURA (to the street, quiet): The street votes on his name tonight.
  REACTION: carrier room (the frozen street at the wall — the struck line, MARTA PAID fresh beneath it, the keeper walking away, hand buried) · duration 2.5s · follows_line U6 L2
TEXT RULE: this vehicle contains no words of any in-world
  text. Declared-blank surfaces: the brick wall's chalk
  field and the hanging sign board — blank, unmarked in
  the generation. PIL plates (assembly, on the take's wall
  field): stage 1 (until the strike) the U1 stack; stage 2
  (from the strike) MARTA — OWES THE RENT struck through
  with one chalk stroke + MARTA PAID. beneath it in
  Laura's docket hand; freeze stage (final 2.5s) stage 2 +
  the vote question across the lower wall field: SHOULD
  LAURA WRITE THE WATCHER'S NAME?
DURATION + ASPECT line: Exactly 10 seconds, 16:9 widescreen, 1280x720.
END STATE (the pin):
  end_state.identity: Laura at the wall, chalk lowered from
    the written line, facing the street; Marta at the
    counter; the Watcher walking away down the street,
    back half-turned, left hand in his pocket; the Courier
    still holding the ring-box; the queue watching him go
    — the picture frozen
  end_state.wardrobe: states as opened; Laura's fingers
    chalk-dusted
  end_state.prop: the chalk stub lowered in Laura's hand;
    the coins still in the Watcher's pocket, unseen again
    as his coat settles
  end_state.light: morning light from frame left, cool bone
    daylight, held in the freeze
```

---

## §5 — GATE_LOG sections (production stage)

The production gate record for Part 2 lives in
`GATE_LOG_PART2.md` (episode root), built on the BRIEF.md
§5 structure: §1 panel gate (Marta set + PEAKs, sha256 +
eye verdicts) · §2 sequence + animatic gates · §3 per-take
QC blocks (§5.1 format of BRIEF.md: drift rows, machine
flags as triage only, ASR-vs-script diff, attempt log,
tail-drift verdict) · §4 voice check per speaker (§5.2
format; permitted outcomes only) · §5 per-joint log J1–J5
(§5.3 format) · §6 master gates (§5.4 format: dual-
checkpoint transcription protocol with a NON-Whisper
second architecture, mechanical diff, ear test sign-off,
Gate (f) cold run, poster frame, master Stranger test,
calibration + reject-bank entries) · §7 delivery record.

Master spec (carried from Part 1, binding): six conformed
segments of exactly 240f at 1280×720; joined file verified
BEFORE the master encode at exactly 1440f / 60.000000s
(concat FILTER, never the demuxer — Part 1's drift lesson);
single uninterrupted encode, libx264 CRF 18, proven by
SIZE DIFFERENTIAL against a CRF 23 encode of the same
joined file (the SEI string is not evidence on this
build); PIL chalk plates per §4; ~ WuBu ~ corner bug (gold
serif, bottom-right, verified head and tail); loudnorm to
−18 LUFS / TP −2; AAC 48kHz 192k; faststart; mov_text
subtitle track + burned-in subtitles from the scripted
lines at the master's measured timings; chat copy ≤50 MB
under a fresh filename; poster frame. NO delivered flag —
the parent delivers.

### 5.5 Delivery — social caption step (A-12)

```
CAPTION_RULE: platform captions pick exactly one form —
  REACTION / TORN_FRAGMENT / CHEAP_QUESTION — and never
  describe, summarize, or hashtag-explain the episode.
  form: TORN_FRAGMENT
  caption: "in his pocket yesterday"
  (a torn mid-scene fragment of U1's accusation; it points
   at the episode's closing open question — the keeper's
   name, and the street's vote on it — without repeating
   or explaining it)
```

---

## §6 — Field-presence checklist (this brief, filled)

- Brief header: `VOICE_ROUTE` ✓ NATIVE_TEXT_ONLY + waiver ·
  `MODEL_SYNTAX` ✓ veo-colon-noquotes · `CONTINUITY_OWNER` ✓
- Per character: `CANONICAL_FACE_REF` ✓ ×4 (sha256 for
  Laura, Marta, the Watcher, the Courier) ·
  `LOOK_BLOCK_VERBATIM` ✓ ×4 · `VOICE_SPEC_TEXT` ✓ ×2
  speakers (silent cards NA by role) · `SPEECH_RULE` ✓ ×4 ·
  `length_trait` ✓ ×2 speakers (the two designed speakers'
  traits differ: Laura clipped-and-even, Marta
  plain-counting) · `NEVER_DOES` ✓ · `NEVER_SAYS` ✓ ·
  `RENT` ✓ ×4 · `MOTION_SIGNATURE` ✓ ×4 · `STATE_OPEN` ✓ ·
  `STATE_CLOSE` ✓
- Room: `AUDIENCE_SECRET` ✓ (§2) · `HANGER_PAID` ✓ (§2) ·
  Pass 3.5/3.7 of record ✓ (§2, COLD_READ_PART2) · Pass 4
  sign-off ✓ (§2 + every §4.1 block signed)
- Panels: `SEQUENCE GATE` ✓ specified, gate record at
  production (GATE_LOG_PART2.md §1–§2) · `ANIMATIC GATE` ✓
  specified, signs at production (blocking)
- Per unit: `SPOKEN-LOAD AUDIT` ✓ ×6 (incl. `measured_sec`,
  `implied_rate`, `span_cost_sec`) · `PREV END STATE` ✓ ×6 ·
  `REFERENCE PRIORITY` ✓ ×6 · `REFS_BOUND` ✓ ×6 ·
  `STATE_ASSERT` ✓ ×6 · `PROOF_OBJECT` ✓ ×6 ·
  `PERSONA_TRANSLATION` ✓ ×6 · `OBJECTIVE` ✓ · `OBSTACLE` ✓ ·
  `TACTICS` ✓ ×6 · `EYE TASK` ✓ ×6 · `END STATE` ✓ ×6
  (four sub-fields) · `SPEECH BLOCK` ✓ ×6 · `line_move` ✓ ·
  `line_target` ✓ · `line_genre_move` ✓ (LINE LEDGER in
  every unit) · `REACTION` ✓ (the three digestion gaps
  written as REACTION entries in U3 / U5 / U6 speech blocks)
- Per take (production stage): four drift rows with
  classes ✓ specified (GATE_LOG_PART2.md §3) ·
  `motion_at_cut_in` ✓ · attempt log ✓ · tail-drift verdict ✓
- Per speaker (production stage): `voice_check_outcome` ✓
  specified, permitted values only
- Per joint (production stage): `joint_eye_verdict` ✓ +
  `joint_mismatch_class` ✓ specified
- Master (production stage): transcription settings block ✓ ·
  mechanical diff fields ✓ · ear test sign-off ✓ ·
  `cold_verdict` ✓ · `poster_frame_verdict` ✓ ·
  `stranger_master_verdict` ✓ specified
- Delivery: `CAPTION_RULE` ✓ (§5.5, form declared)

— End of brief (Part 2, filled on the template v4
structure), 2026-11-23.
