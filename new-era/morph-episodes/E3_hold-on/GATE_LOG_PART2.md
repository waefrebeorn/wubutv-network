# GATE LOG — HOLD ON E3 · PART 2 (production stage)

Built on the BRIEF.md §5 structure. Script of record:
SCRIPT_PART2.md LOCKED v1 (parent, 2026-11-23; cold read
of record work/COLD_READ_PART2.md — PASS). Production
coordinator session, 2026-11-23. Ruling stack: fail-once-
then-ship per unit; load-bearing lines (U4 L1, U6 L2)
exempt from the cap; the buried-hand law (the Watcher's
LEFT hand never leaves his coat pocket, U1–U6) is a
per-take REJECT class.

## §1 — Panel gate (pre-pro builds)

MARTA set (NEW character; generated 2026-11-23 against
PNL-CHAR-LAURA-hero-e2 as style reference; converted from
the generation webp to PNG under canonical names):
- PNL-CHAR-MARTA-face.png (2096×1184) sha256
  bdff5b0340ef019958eb566a96deb463be4a34d5c717d9cf46d3a283c090976e
  — EYE VERDICT: PASS. Weathered face, flour dust,
  bone-white headscarf, tan apron straps; backdrop and
  light match the Laura panels exactly; deadpan register
  matches the town. Reads a few years older than the
  card's "late 40s" — consistent across all four panels;
  accepted (mutual consistency is the binding property).
- PNL-CHAR-MARTA-hero.png (2096×1184) sha256
  ef5ac2d8a5841f7170d608dedb598d37f397e9d75da9405371335228e9b30161
  — PASS. Apron with the large front pocket, the notch
  knife in its sheath at the pocket, the cloth coin pouch
  tied at the waist, floury forearms. Same woman as the
  face panel.
- PNL-CHAR-MARTA-profile.png (2096×1184) sha256
  aac34dcb3def095f2170179abf197cebd205795a335b29cd4eb5c4bb2fdf15eb
  — PASS. Strict profile, scarf knot, knife at pocket.
- PNL-CHAR-MARTA-back.png (2096×1184) sha256
  a34f525b766c6f431321f6869ad5b25c7c86c0d402700734c0cdf1551ae2f80b
  — PASS. Crossed apron straps, tied bow, coin pouch,
  scarf knot. Same woman.
No refires spent on the Marta set (4/4 first-pass PASS).

PEAK panels (contract stills; generated 2026-11-23 in the
world of PNL-WORLD-market-wall; converted to PNG):
- PNL2-PEAK-U1-coinslap.png sha256 a595004e507edaf6… —
  PASS. Marta mid-slap at the counter, coin on the stone,
  queue behind, the Courier in cobalt holding the small
  box open-palmed, Laura in green, the Watcher in the
  cardigan. Wall and board blank.
- PNL2-PEAK-U2-notch.png sha256 a2c2afa2162e4734… —
  PASS. The notch being cut, Laura watching the coin; a
  man chalks the blank wall behind. The beat reads cold.
- PNL2-PEAK-U3-pocket.png sha256 ae11d3e6a386efdf… —
  PASS. Marta holding the coin out at her stall; the
  Watcher's left hand visibly in his pocket; the awning
  stripe reads cobalt against U1/U2's bone — the
  one-detail reset is legible on the sheet.
- PNL2-PEAK-U4-naming.png sha256 d5bb46e32aeb3f9e… —
  PASS with a note. Laura facing the Watcher, his left
  hand in pocket, chalk in his right; Marta behind. NOTE
  (IDENTITY, minor): the Watcher reads slightly younger
  in this still than his canonical face panel; the unit
  binds PNL-CHAR-WATCHER-face-16x9 as image 4 to govern.
- PNL2-PEAK-U5-bell.png sha256 7634fdf4d752df4b… —
  PASS. The bell hangs in frame; the Courier's hands open
  around the ring-box; Marta's coin up; the Watcher's
  right hand raised with the chalk, left hand in the
  pocket with coins showing at its mouth. The reveal
  reads cold.
- PNL2-PEAK-U6-freeze.png sha256 9230cf8b7a092cd3… —
  PASS. Laura's chalk stroke across the blank wall; the
  Watcher walking away down the street, back turned;
  Marta at the stall; the queue watching. Labelled
  DESTINATION (never image 1), per the Part 1 rule.

## §2 — Sequence + animatic gates

SEQUENCE GATE: contact sheet work/SEQ_SHEET_E3P2.png
(the six PEAKs). Blind first look (coordinator, before
re-reading the brief): a woman slams a coin down at a
wall counter before a queue → she cuts a notch in a coin
while the chalk-hand watches → she holds the coin out to
the keeper, whose hand stays in his pocket, under a
changed awning → the chalk-hand faces the keeper down →
at the bell every hand is open but his, and coins show
in his pocket → she chalks the wall herself and he walks
away. seq_reads_silent: Y. seq_odd_one_out: PNL2-PEAK-U4
(IDENTITY, minor — see §1 note). seq_anchor_panel:
PNL-WORLD-market-wall (world) · PNL-CHAR-MARTA-face
(new identity of record). Story in one sentence (from
the sheet alone): "A bread-seller's paid name was kept
off the wall by the keeper's pocket; his buried hand
convicts him at the bell, and her name goes up in the
chalk-hand's own writing." — matches the locked story.
SEQUENCE GATE: PASS.

ANIMATIC GATE: work/animatic_E3P2.mp4 (the six PEAKs at
10.0s each, 60.000s). Watched at speed uninterrupted:
the chain reads in order with no confusion point; first
confusion at: none. animatic_spoken_load_check: PASS —
every unit's §4.1 audit verifies its lines fit the 10s
container at the measured rate (implied rates 1.33–2.18
wps, all under the 2.5 fail line; the three REACTION
gaps are carried inside the units' silence budgets).
animatic_panels_reordered_or_cut: none.
ANIMATIC GATE: PASS — video generation may begin.

## §3 — Per-take QC (filled per take at production)

### U1 — HOOK + SETUP · MARTA

**U1_t1** — takes_part2/U1_t1.mp4 · md5
38f36553a181a2e25ee63f28757da0cc · native 1248×704, 240f,
10.000s. Refs bound: PNL-WORLD-market-wall (1) ·
PNL2-PEAK-U1-coinslap (2) · PNL-CHAR-MARTA-face (3).
- IDENTITY: PASS — Marta matches her face panel exactly
  (weathered face, headscarf, tan apron, coin pouch,
  knife at the pouch); Laura in green with the ponytail;
  the Watcher balding-grey in the ink cardigan; the
  Courier in cobalt with the ring-box in open hands.
  One of each; no doubles.
- WARDROBE: PASS — states as opened; flour on Marta's
  hands; chalk dust on the Watcher's right hand.
- PROP: PASS — exactly one coin, slapped flat at frame 0,
  spinning, settled notch-up on the counter by mid-shot
  and still there at the tail; the ring-box held
  open-palmed throughout; Laura's chalk lowered, never
  touching the wall (nobody writes — correct).
- MOTION: PASS — frame 0 mid-motion (her arm already
  coming down; motion blur + dust puff on the counter at
  0.5s); queue already walking; motion_at_cut_in Y.
  The Watcher chalks one-handed at the wall throughout.
- TEXT SURFACES: PASS — board zoom read: bare weathered
  wood, no lettering; wall brick blank (faint non-letter
  chalk scuffs at the corner where he chalks — no
  letterforms; the PIL stack covers the field at
  assembly).
- BURIED-HAND LAW: PASS — verified head (0.5s), mid
  (5.0s zoom: left hand inside the coat pocket, cuff at
  the pocket mouth), tail (9.9s): the left hand never
  leaves the pocket in any sampled frame.
- MOUTH DISCIPLINE: PASS — only Marta's mouth moves;
  sampled frames show all other mouths closed.
- ASR (dual, work/qc_part2/U1_t1/asr.json): large-v3 and
  distil-large-v3 AGREE word-for-word, 3 segments:
  1.20–2.60 "Write that I paid, Laura." · 4.08–5.96
  "My coin went in his pocket yesterday." · 7.72–9.30
  "Wall still says I owe the rent." (distil boundaries
  1.20–2.72 / 4.44–6.32 / 8.02–9.42). 18/18 scripted
  words, in order, zero extra, zero missing.
- BLAM (U1): frame 0 mid-motion slap ✓ · named impact
  (coin slap + clatter) inside the first second ✓ ·
  first spoken word at 1.20s (inside 3s) ✓ · head RMS
  0.0964 vs ambient 0.1051 — no dead head ✓.
- TAIL: end state matches the §4 pin (Marta's hand flat
  beside the settled coin; Laura at the wall, chalk
  lowered; Watcher chalking one-handed; Courier
  open-palmed). Chain frame harvested:
  work/chain_part2/U1_last.png.
- VERDICT: **ACCEPTED — first take.** No refire spent.

### U2 — PROOF · LAURA

**U2_t1** — takes_part2/U2_t1.mp4 · md5
b85d53050dadfb137b49b212ff4f9ea9 · native 1248×704, 240f,
10.000s. Refs bound: U1_last (1) · PNL2-PEAK-U2-notch (2) ·
PNL-CHAR-LAURA-face-e2 (3) · PNL-CHAR-MARTA-hero (4).
- IDENTITY: PASS — Laura (ponytail, green shirt) beside
  Marta at the counter; Marta matches her panels; the
  Watcher at the wall behind; the Courier in cobalt with
  the ring-box. One of each.
- WARDROBE: PASS — states as chained from U1.
- PROP: PASS — the notch is cut on camera: Marta works
  the knife at the counter through the middle frames and
  holds the coin up in her fingers at the tail, turning
  it (tail zoom read). The exhibit coin rests on the
  counter (a second coin-like mark beside it reads as
  its shadow/scuff — the two story coins are accounted
  for; minor, noted). Laura's palm comes down flat on
  the stone between Marta and the wall — the scripted
  beat reads.
- MOTION: PASS — continuous counter work; the Watcher
  chalks one-handed down the wall; motion_at_cut_in Y
  (chained frame continues the street's motion).
- TEXT SURFACES: PASS — board bare wood in every sampled
  frame; wall blank (non-letter chalk scuffs only).
- BURIED-HAND LAW: PASS — 5.5s zoom: the Watcher's left
  hand inside his coat pocket, cuff at the pocket mouth;
  head and tail samples show no hand-out event.
- MOUTH DISCIPLINE: PASS — Marta's mouth closed while
  she works (tail zoom); only Laura speaks.
- ASR (dual, work/qc_part2/U2_t1/asr.json): large-v3
  (authority) 2 segments, verbatim: 3.12–5.08 "Every
  coin you earn wears a notch." · 7.14–8.64 "One in his
  pocket wears yours." — 13/13 words, in order, zero
  extra. distil-large-v3 merges the span and reads
  "where's yours" for "wears yours" — the known distil
  homophone noise class; Checkpoint A reads "wears" in
  both lines; adjudicated to A. Head RMS 0.0198 vs
  ambient 0.0205 (quiet street head — no gap scripted
  this unit; first word 3.12s over the cutting action).
- TAIL: matches the §4 pin in substance (coin in Marta's
  fingers, held up; Laura beside her, chalk lowered;
  Watcher one-handed at the wall). Chain frame:
  work/chain_part2/U2_last.png.
- VERDICT: **ACCEPTED — first take.** No refire spent.
  Joint note: the unit's framing sits closer (medium)
  than U1's wide — recorded at J1.

### U3 — TWIST · MARTA · QUIET

**U3_t1** — takes_part2/U3_t1.mp4 · md5
c3c74a267e37fefad6946ea2ca711e3d · native 1280×720, 240f,
10.000s. Refs bound: U2_last (1) · PNL2-PEAK-U3-pocket (2) ·
PNL-CHAR-MARTA-face (3). Fired by the successor coordinator
2026-11-24 ~04:38Z, after the 2026-11-23 502 outage lifted
(six fire attempts across ~90 minutes of outage — 502s are
not take failures and consumed no refire).
- IDENTITY: PASS — Marta matches her face panel (weathered
  face, headscarf, tan apron, notch knife at the apron
  pocket, coin pouch); Laura in green with chalk at the
  head frames; the Watcher balding-grey in the ink cardigan;
  the Courier in cobalt with the ring-box from mid-shot on.
  One of each; no doubles.
- WARDROBE: PASS — states as chained from U2; the awning
  stripe is COBALT from this unit (the one-detail reset
  reads on screen, blue-white stripes at the stall).
- PROP: PASS with a nit — the notched coin starts in
  Marta's open palm (0.5s), is taken by the Watcher at the
  counter (~3.0s) and her palm is empty from 5.0s on; the
  exhibit coin rests on the counter. NIT: several faint
  coin-like discs read on the counter stone beyond the one
  exhibit coin (stone marks vs coins not resolvable at this
  size) — disclosed, same class as Part 1's U5 coin-count
  nit. The take at 3.0s reads with a chalk-white object in
  the Watcher's fingers over her palm; the palm is empty
  after, so the pocketing reads.
- MOTION: PASS with a nit — continuous action throughout,
  motion_at_cut_in Y (chained from U2's tail staging).
  NIT: the camera slowly reframes across the unit (opens
  tighter on Marta at the counter, settles wider with the
  Courier in frame) instead of the briefed locked shot —
  a drift, not a cut; world and light stay continuous.
- TEXT SURFACES: PASS — board bare wood in every sampled
  frame; wall blank (faint non-letter chalk tally scuffs
  where he chalks — no letterforms; the PIL stack covers
  the field at assembly).
- BURIED-HAND LAW: PASS — sampled 0.5 / 3.0 / 5.0 / 7.0 /
  9.9s: the Watcher's left hand never leaves his coat
  pocket; mid and tail frames show the white cuff at the
  pocket mouth with the hand inside. He takes the coin
  with his RIGHT hand.
- MOUTH DISCIPLINE: PASS — only Marta's mouth moves
  (5.0s, 7.0s mid-line); all other mouths closed.
- ASR (dual, work/qc_part2/U3_t1/asr.json): large-v3 and
  distil-large-v3 AGREE word-for-word, one merged span
  2.80–7.67 "Paid him twice now. He writes for everyone
  but me." — 8/8 scripted words, in order, zero extra,
  zero missing. Head RMS 0.0211 vs ambient 0.0188 (quiet
  street head). GAP 1 performed ~2.8s of held silence
  before L1 vs 2.0s scripted — inside the unit's silence
  budget class; disclosed.
- TAIL: matches the §4 pin in substance (Marta at the
  counter, hands on the stone, palm open at rest; the
  Watcher back at the wall chalking one-handed at 7.0s,
  at frame right by the tail; queue shifted). Chain frame
  harvested: work/chain_part2/U3_last.png.
- VERDICT: **ACCEPTED — first take.** No refire spent.
  Laura drifts out of frame in the back half (she is
  scripted only as watching from beside the counter) —
  disclosed staging nit.

### U4 — CLASH · LAURA

**U4_t1** — takes_part2/U4_t1.mp4 · md5
7464ad43de55b9c573b4b70bad1a79af · native 1248×704, 240f,
10.000s. Refs bound: U3_last (1) · PNL2-PEAK-U4-naming (2) ·
PNL-CHAR-LAURA-face-e2 (3) · PNL-CHAR-WATCHER-face-16x9 (4).
- IDENTITY: PASS — Laura matches her face panel (ponytail,
  green work shirt); the Watcher matches his face panel
  (grey stubble, deep-set eyes, ink cardigan) — the §1
  PEAK note's young-reading is governed by the bound face
  panel as briefed; Marta matches her panels at frame
  right. One of each; no doubles.
- WARDROBE: PASS — states as chained; awning cobalt.
- PROP: PASS — his chalk stub in the right hand, raised
  and arrested from mid-shot on; the exhibit coin on the
  counter at the head frames; no other coins shown (the
  named coins stay inside the pocket, unseen — correct).
- MOTION: PASS — Laura steps in between Marta and the
  wall across the head frames and holds the confrontation;
  motion_at_cut_in Y (opens on U3's exact tail staging).
- TEXT SURFACES: PASS — board bare wood in every sampled
  frame; wall blank (non-letter chalk scuffs only).
- BURIED-HAND LAW: PASS — sampled 0.5 / 3.0 / 5.0 / 7.0 /
  9.9s: the left hand stays inside the coat pocket in
  every frame, white cuff visible at the pocket mouth in
  the 5.0 / 7.0 / 9.9s frames; it does not come out at
  the order. His chalk stops and stays stopped.
- MOUTH DISCIPLINE: PASS — only Laura's mouth moves
  (3.0s, 7.0s mid-line); the Watcher's mouth closed
  throughout — he answers nothing; Marta silent.
- EYE TASK: PASS with a nit — the Watcher's eyes stay on
  Laura, level, in every confrontation frame (no dead or
  wandering eyes, F-23 held). NIT: Laura's gaze reads at
  his face in the wide frames; at 3.0s it is downcast
  toward the pocket as scripted. The naming lands on the
  dialogue; disclosed.
- ASR (dual, work/qc_part2/U4_t1/asr.json): large-v3 and
  distil-large-v3 AGREE word-for-word, 3 segments:
  2.58–4.48 "That hand's been in your pocket all morning."
  · 5.54–7.90 "Yesterday the landlord's boy paid it two
  coins." · 8.96–9.62 "Bring it out." — 19/19 scripted
  words, in order, zero extra, zero missing. LOAD-BEARING
  L1 landed verbatim on the first take.
- TAIL: matches the §4 pin (Laura between Marta and the
  wall facing the Watcher, his chalk arrested mid-air,
  left hand in pocket; Marta behind; queue silent). Chain
  frame: work/chain_part2/U4_last.png.
- VERDICT: **ACCEPTED — first take.** No refire spent.

### U5 — REVEAL · MARTA · GAP 2 at the head

**U5_t1** — takes_part2/U5_t1.mp4 · md5
0e4315268046b32e42f252ed8952f8b7 · native 1248×704, 240f,
10.000s. Refs bound: U4_last (1) · PNL2-PEAK-U5-bell (2) ·
PNL-CHAR-MARTA-face (3). Landed 2026-11-24 ~05:35Z on the
third fire attempt (two upstream 502 flaps before it —
not take failures, no refire consumed).
- IDENTITY: PASS with a nit — Marta, Laura and the Courier
  match their panels; the bell hangs in frame; the queue
  holds. NIT: the Watcher reads auburn-haired and younger
  than his panel under this unit's bluer grade (the gaunt
  face structure, deep-set eyes and stubble pattern are
  his; the light temperature shifted cool across the
  joint — see J4). Disclosed.
- WARDROBE: PASS — states as chained; awning cobalt.
- PROP: PASS with nits — the Courier's hands stay open
  around the red ring-box in every sampled frame; three
  coins show at the Watcher's pocket mouth from mid-shot
  (two bright, one darker below — the notch is not
  resolvable at this scale, same class as Part 1's U5
  coin nit); Marta holds her coin up in the light.
  NITS: (a) two of the pocket coins are already visible
  at the coat front during the GAP-2 hold, before the
  crack — the reveal is pre-shown inside its own unit;
  (b) Marta's coin is pinched between finger and thumb
  rather than resting in an open palm.
- MOTION: PASS — the hold reads held (no speech before
  2.61s on ASR); hands along the wall do what the bell
  counts; the coat sits swung at the pocket.
- TEXT SURFACES: PASS — board bare wood in every sampled
  frame; wall blank.
- BURIED-HAND LAW: PASS — sampled 0.5 / 1.5 / 3.0 / 5.0 /
  7.0 / 9.9s: the left hand stays inside the coat pocket
  in every frame, including the bell moment; only the
  coat swings. The hand never comes out.
- MOUTH DISCIPLINE: PASS — Marta is the only speaker;
  the Watcher's and Laura's mouths closed in all sampled
  frames.
- ASR (dual, work/qc_part2/U5_t1/asr.json): large-v3 one
  merged span 2.61–8.85 "Bell rang, Watcher. My coin's in
  the light. Yours is hiding." — 11/11 scripted words, in
  order, zero extra, zero missing. distil agrees except
  "coins" for "coin's" (homophone-class noise; adjudicated
  to Checkpoint A per the U2 precedent). Head RMS 0.056
  vs ambient 0.083 — no speech in the GAP-2 hold. NIT:
  both lines delivered as one contiguous span rather than
  split around the crack's settle.
- TAIL: matches the §4 pin (Marta's coin up in the light,
  his right hand raised with chalk, coat open at the
  pocket, three coins showing, left hand in; Courier open
  around the box; Laura watching the pocket; queue
  staring). Chain frame: work/chain_part2/U5_last.png.
- VERDICT: **ACCEPTED — first take.** No refire spent.

### U6 — CLOSE · LAURA · SILENCE-BEAT

**U6_t1** — takes_part2/U6_t1.mp4 · md5
76af74c6ce0271df6a7a571e8031492e · native 1248×704, 240f,
10.000s. Refs bound: U5_last (1) · PNL2-PEAK-U6-freeze (2) ·
PNL-CHAR-LAURA-face-e2 (3) · PNL-WALL2-closeup-16x9 (4).
- IDENTITY: PASS with a nit — the head frame opens on
  U5's exact tail staging (Laura, the Courier with the
  ring-box, the Watcher grey and gaunt with chalk raised
  and coins at the pocket, Marta with her coin up). Laura's
  face wobbles in the late frames (reads younger at 8.5s).
- CAMERA: FAIL — the shot roams: wide at the head, a wall
  close-up for the writing (3.0s, 5.0s), over Laura's
  shoulder (7.0s), a down-street view for the walk-away
  (8.5s, 9.9s). The brief locks one wide shot; the U6 wall
  plates and the freeze composite are built for the wide
  field, so the roaming framing breaks the post plan.
- TEXT SURFACES: FAIL — Laura's chalk strokes form
  letter-like pseudo-writing across the wall field (clear
  cross-barred verticals and loops at 5.0 / 7.0 / 9.9s),
  against the explicit strokes-never-letters direction.
- BURIED-HAND LAW: NOT BREACHED on the evidence — the
  Watcher walks away with his back turned and his hands
  not visible (8.5s, 9.9s); no frame shows the left hand
  out. Compliance unverifiable at the tail (back view).
- FREEZE: FAIL — 8.5s and 9.9s frames differ (he walks
  on, her mouth closes): no native freeze in the last
  2.5s. (Fixable in post; not a standalone reject ground.)
- ASR (dual, work/qc_part2/U6_t1/asr.json): large-v3
  4.05–8.17 "Your name's up, Marta. The street vote votes
  on his name tonight."; distil agrees in two segments.
  L1 verbatim (4/4). LOAD-BEARING L2 FAILED on both
  checkpoints: "The street vote votes on his name
  tonight." — an extra "vote" replaces the scripted
  "votes" construction (scripted: "The street votes on
  his name tonight."). 10/11 words; the failed word is
  the line's verb.
- VERDICT: **REJECTED.** The load-bearing failure alone
  mandates a refire (exempt from the fail-once cap); the
  camera and text-surface failures are independent
  grounds. U6_t2 fired under the same vehicle; its first
  attempt hit the upstream 502 flap — retry cadence
  continues; 502s consume nothing.

**U6_t2** — takes_part2/U6_t2.mp4 · md5
b3e9fbdc8aaeb9da12b81b8d6f0c30a2 · native 1248×704, 240f,
10.000s. Same refs and vehicle as t1.
- PICTURE: same class as t1 — opens on U5's tail staging
  (0.5s: the confrontation group, coins at the pocket,
  Marta's coin up), then the camera goes to the wall
  (5.0s: Laura in profile offering the chalk, wall field
  at frame left carrying FAINT chalk scribbles — present
  but less letter-like than t1's) and ends on the
  down-street view (9.9s: the Watcher walking away,
  back turned, mid-street; Laura at the wall; the queue
  watching). Buried hand never shown out; back view at
  the tail leaves compliance unverifiable, as in t1.
  No native freeze.
- ASR (dual, work/qc_part2/U6_t2/asr.json): L1 verbatim
  on both checkpoints, 3.34–4.58 "Your name's up, Marta."
  L2: large-v3 5.96–8.10 "The street votes on his name
  tonight, tonight."; distil 5.92–8.32 agrees. The
  scripted line is present word-for-word in order, PLUS
  a trailing echoed "tonight" after it.
- VERDICT: **NOT ACCEPTED — load-bearing line not clean.**
  The exemption's bar is the line landed verbatim; an
  echoed extra word is a failed landing of the hanger
  line. U6_t3 fired under the exemption (502 on its
  first attempt; cadence continues). If t3 lands L2
  clean, the ship take is the better picture of t2/t3;
  the freeze is built in post at assembly either way.

**U6_t3** — takes_part2/U6_t3.mp4 · md5
6f2b92dfd88f1eef22e311afebd80680 · native 1248×704, 240f,
10.000s. Same refs and vehicle as t1/t2.
- ASR (dual, work/qc_part2/U6_t3/asr.json): BOTH
  checkpoints agree word-for-word, zero extra, zero
  missing: L1 3.63–4.91 "Your name's up, Marta." · L2
  6.01–8.07 "The street votes on his name tonight."
  **The load-bearing hanger line landed CLEAN.**
- PICTURE: FAIL on text surfaces — the head frame (0.5s)
  opens clean on U5's tail staging, but once Laura
  writes, the wall carries READABLE chalk lettering
  ("WATCHER" and further fragments legible at 5.0s and
  9.9s, wall at frame left in the wall-side and
  down-street framings). Generated in-picture text is a
  hard fail under the post-layer law; the plates cannot
  cover lettering in these roaming perspectives.
  Camera roams as in t1/t2; no native freeze; the
  Watcher walks away back-turned (buried hand not
  verifiably out).
- VERDICT: **NOT SHIPPABLE AS-IS despite the clean
  line.** U6_t4 fired under the exemption's purpose —
  a shippable take carrying the verbatim line (first
  attempt 502; cadence continues). Fallback of record:
  if t4 cannot land or also fails, ship t3 over t2 —
  the exemption prioritises the verbatim hanger line;
  the wall lettering would ship disclosed.

**U6_t4** — takes_part2/U6_t4.mp4 · md5
2bb2b7c1d809913009de0ba14c8a18e1 · native 1248×704, 240f,
10.000s. Same refs and vehicle as t1–t3.
- ASR (dual, work/qc_part2/U6_t4/asr.json): BOTH
  checkpoints agree word-for-word, one merged span
  1.01–5.84 (distil to 5.96): "Your name's up, Marta.
  The street votes on his name tonight." — 11/11 scripted
  words, in order, zero extra, zero missing. **The
  load-bearing hanger line landed CLEAN in a take whose
  picture is shippable.**
- TEXT SURFACES: PASS — the wall carries only faint
  chalk strokes and scribbles (5.0s, 8.5s, 9.9s); NO
  readable lettering anywhere (contrast t3). Board
  blank in the head frames.
- IDENTITY / STAGING: opens on U5's exact tail staging
  (0.5s — the confrontation group, bell in frame);
  the Watcher grey and gaunt, matching his panel;
  Laura at the wall in profile for the writing; he
  walks away down the street, back turned, the queue
  watching (8.5s, 9.9s); Marta at the counter.
- BURIED-HAND LAW: PASS — at 3.0s, front-readable: his
  left hand is inside the coat pocket, cuff at the
  pocket mouth, while he looks down at the counter;
  the walk-away is back-view (hand not visible, never
  shown out).
- CAMERA / FREEZE: the camera roams wall-side and
  down-street as in t1–t3 (the class is constant across
  all four U6 takes — the wall close-up reference pulls
  it); no native freeze (8.5s ≠ 9.9s). The freeze is
  built in post at assembly: picture held from 7.5s,
  which is after both lines end (~5.96s), so the hold
  touches no dialogue. Both disclosed.
- NITS: both lines delivered early as one contiguous
  span, leaving ~4s of silent walk-away (serves the
  SILENCE-BEAT design); Marta's expression softens
  toward a smile at 3.0s (she does not speak).
- VERDICT: **ACCEPTED — U6 SHIP TAKE.** The exemption
  chain closes: t1 (line garbled) → t2 (line echoed) →
  t3 (line clean, wall lettered) → t4 (line clean, wall
  clean). All six units now hold accepted takes.

## §4 — Voice check (per speaker, at production)

MARTA (first speaking unit U1): the performed voice reads
as the card specifies — a working woman in her late 40s,
plain and a little hoarse, flat depot register, facts
counted without rise. voice_check_outcome:
CONSISTENT_WITH_TEXT_SPEC. (Native route: no enrolled
reference exists; the ear verdict is against the §1
VOICE_SPEC_TEXT, per the §0 waiver.)

LAURA (first speaking unit U2): delivery profile matches
the card — two even, unhurried spans (3.12–5.08,
7.14–8.64), segment RMS 0.138/0.110 in line with the
episode's flat register, no rise or plead in the pacing;
the voice is the series' Laura register as carried from
Part 1. voice_check_outcome: CONSISTENT_WITH_TEXT_SPEC.

## §5 — Per-joint log J1–J5 (at production)

JOINT J1 (U1 outgoing → U2 incoming):
  joint_subjects_checked: Marta (counter, left) · Laura
    (wall/counter, right) · the Watcher (wall) · the
    Courier (queue) · the counter, board, awning, crates
  joint_eye_verdict: MATCH — same street geometry, same
    cast positions and wardrobe states, same morning
    light from frame left; U2 opens on U1's exact tail
    staging (Marta's hand at the counter, the coin down)
  joint_mismatch_class: FRAMING — U2's shot sits closer
    (medium) than U1's wide; world, wardrobe, positions
    and light all continuous. Accepted as a coverage
    step, not a world break; the remaining units are
    briefed to hold their chained framing.

JOINT J2 (U2 outgoing → U3 incoming):
  joint_subjects_checked: Marta (counter) · Laura (counter,
    head frames) · the Watcher (wall → counter → wall) ·
    the Courier (queue, from mid-shot) · the counter, board,
    awning, bread stall
  joint_eye_verdict: MATCH — U3 opens on U2's tail staging
    (Marta at the counter with the notched coin raised;
    the Watcher one-handed at the wall; same morning light
    from frame left). The one scripted world change lands:
    the awning stripe is cobalt from this unit.
  joint_mismatch_class: FRAMING — U3's camera slowly
    reframes from a counter-medium to a wider street view
    across the unit (drift, not a cut); world, wardrobe,
    positions and light continuous. Accepted as a coverage
    drift, disclosed at §3 U3.

JOINT J3 (U3 outgoing → U4 incoming):
  joint_subjects_checked: Marta (counter) · Laura (beside
    the counter → steps in) · the Watcher (wall) · the
    queue · the counter, board, awning
  joint_eye_verdict: MATCH — U4 opens on U3's exact tail
    staging (Marta at the counter, hands on the stone; the
    Watcher at the wall at frame right; Laura in green
    behind Marta) and the confrontation develops out of it
    without a world break; same light, same wardrobe states.
  joint_mismatch_class: NONE material — framing settles
    into the two-shot confrontation the unit is briefed for.

JOINT J4 (U4 outgoing → U5 incoming):
  joint_subjects_checked: Marta (counter) · Laura (green,
    at the wall) · the Watcher (confrontation) · the Courier
    (ring-box) · the queue · the bell, board, awning
  joint_eye_verdict: MATCH with a disclosed light drift —
    U5 opens on U4's tail staging (the confrontation holds,
    positions and wardrobe continuous, the bell now in
    frame) and the reveal develops out of it.
  joint_mismatch_class: LIGHT — U5's grade runs noticeably
    bluer/cooler than U4's bone daylight across the joint;
    the Watcher's hair reads auburn under it. World,
    wardrobe, positions continuous. Accepted as a light
    drift, disclosed at §3 U5 and §5.

JOINT J5 (U5 outgoing → U6 incoming, ship take U6_t4):
  joint_subjects_checked: Marta (counter, coin up) ·
    Laura (watching the pocket → at the wall) · the
    Watcher (confrontation → walks away) · the Courier
    (ring-box) · the queue · the bell, board, awning
  joint_eye_verdict: MATCH at the head — U6_t4 opens on
    U5's exact tail staging (same group framing, same
    positions, the bell in frame, coins at the pocket,
    Marta's coin raised). The unit then develops to the
    wall and the walk-away as scripted.
  joint_mismatch_class: FRAMING (disclosed) — U6's camera
    roams to the wall-side and down-street views instead
    of holding the wide master framing (constant across
    all four U6 takes); world, wardrobe, positions and
    light continuous at the joint itself. LIGHT: U6
    continues U5's cooler blue grade, so the J4 drift
    carries through the close rather than breaking at J5.

## §6 — Master gates (after assembly)

Master: masters/E3_hold-on_part2_16x9.mp4 · md5
8bce866379c109b22ceefe78757fad05 · 21,947,820 B.

ASSEMBLY (Part 1 method, one pass): six conformed
segments of exactly 240f / 10.000000s at 1280×720 (takes
scaled from native 1248×704; U3 native 1280×720), PIL
chalk plates composited per segment (placement-check
frames in work/placement_part2/; U2/U3/U4/U5 plates
re-origined at assembly to the accepted takes' actual
wall fields — make_plates_tuned.py; U6 plates tuned to
U6_t4 — make_plates_u6_tuned.py; U6's picture held from
7.5s as the post freeze, plates switching stage 1 →
stage 2 at 4.5s → freeze plate at 7.5s). Segments joined
by the concat FILTER (never the demuxer); joined file
verified BEFORE the master encode: 1440 video frames,
audio stream exactly 60.000000s, zero start offsets on
both streams (work/assembly_part2/joined_part2.mp4).
Single master encode: CRF 18, AAC 48kHz 192k, faststart,
~ WuBu ~ corner bug head and tail (verified on frames at
2s and 59.5s), mov_text (14 cues) + burned-in subtitles
from the scripted lines at the takes' measured ASR
timings (work/assembly_part2/subs_part2.ass/.srt).
Loudnorm: joined measured −20.09 LUFS / TP −0.33;
master audio lands −18.61 LUFS / TP −2.29 (two-pass
loudnorm, dynamic; first pass −18.79 / −1.97 was
superseded by the compensated second encode, whose
audio was stream-copied into the final master —
work/assembly_part2/master_v2_audio-donor.mp4).

CRF PROOF (size differential, per the SEI anomaly rule):
CRF-23 encode of the same joined file = 11,412,268 B
(work/assembly_part2/joined_part2_crf23.mp4); master
21,947,820 B → 1.92× (Part 1: 1.98×). CRF 18 confirmed.

PROBE (final master): h264 1280×720, 1440 frames read,
start_time 0.000000; AAC stream duration 60.000000s;
mov_text 14 cues. Container note: the format/video
stream duration fields read 60.041667s — the mp4 mdhd
counts one extra frame interval, inherited from the
segment timestamps; the decoded content is exactly
1440 frames with a 60.000000s audio stream. Disclosed.

TRANSCRIPTION (master, dual checkpoint;
work/qc_part2/master/asr.json): Checkpoint A large-v3
and Checkpoint B distil-large-v3 run on the finished
master. MECHANICAL DIFF vs SCRIPT_PART2.md (locked):
**14/14 lines present, in order, verbatim on Checkpoint
A; zero extra, zero missing.** Both load-bearing lines
verbatim on the master: U4 L1 at 32.50–34.48, U6 L2 at
54.08–55.86. Checkpoint B agrees except its standing
homophone-class noise at U2 L2 ("where's yours") and
U5 L2 ("coins") — adjudicated to A per the take-level
precedents. First word 1.20s; last word ends 55.86s;
the freeze tail (57.5–60s) is silent.

EAR TEST (cold, master transcript + frames vs the
locked script): PASS — the surface story reads exactly
as locked with no reference to the script: Marta's
accusation, the notch proof, the twice-paid twist, the
naming of the buried hand, the bell reveal (three coins,
one notched), MARTA PAID struck and chalked, the chalk
offered and refused, the walk-away, the street's vote
tonight. The three digestion gaps hold on the master
(U3's held coin ~2.8s of quiet at 20–22.8s; U5's held
face before the crack at 40–42.6s; the frozen close).

GATE (f) COLD RUN: cold_verdict PASS — a cold viewer
retells the whole case from the master alone (see the
ear-test retelling) and lands the closing question
unaided: should Laura write the Watcher's name?
poster_frame_verdict: PASS — masters/
E3_hold-on_part2_poster.png (44s, the bell reveal: his
chalk raised, coins at the pocket, her coin up) sells
the episode's turn in one frame.
stranger_master_verdict: PASS (floor check) — nothing
in the master requires Part 1 knowledge beyond what
the wall itself shows (the struck Part 1 lines read as
the wall's history, as designed).

BLAM (master level): U1's take-level BLAM record
stands (coin-slap head, first word 1.20s); first cut at
exactly 10.0s by construction.

## §7 — Delivery record

DELIVERABLES (no delivered flag written, no commit —
the parent verifies from disk and delivers):
- House master: masters/E3_hold-on_part2_16x9.mp4
  md5 8bce866379c109b22ceefe78757fad05 · 21,947,820 B ·
  1440f · 1280×720 24fps · CRF 18 (proof 1.92×) · AAC
  48kHz · faststart · bug · mov_text + burned subs.
- Chat copy: masters/E3_hold-on_part2_16x9_chat.mp4
  (byte-identical copy, 21,947,820 B ≤ 50 MB).
- Poster: masters/E3_hold-on_part2_poster.png (44s).

TAKE RECORD: U1_t1, U2_t1, U3_t1, U4_t1, U5_t1 all
accepted on first takes. U6 shipped on U6_t4 after the
load-bearing exemption chain (t1 line garbled → t2 line
echoed → t3 line clean but wall lettered → t4 line
clean, wall clean). Production ran through a long
upstream 502/503 outage window (2026-11-24 ~02:56Z–
~08:0xZ, flapping); outage attempts consumed no
refires at any point.

FLAWS DISCLOSED PLAINLY:
1. U6's camera roams (wall-side and down-street views)
   instead of holding the brief's locked wide shot —
   constant across all four U6 takes; the freeze and
   the stage-2 wall stack were therefore built in post
   against the take's actual framings (plates tuned).
2. U6 has no native freeze: the final 2.5s are a post
   hold of the 7.5s frame (after all dialogue ends).
3. U5: the pocket coins are already visible during the
   GAP-2 hold, before the bell crack — the reveal is
   pre-shown inside its own unit. The Watcher also
   reads auburn-haired/younger under U5's bluer grade
   (light drift across J4, carrying into U6).
4. U3: the camera slowly reframes instead of holding
   the locked shot; faint extra coin-like discs read
   on the counter; Laura drifts out of frame late;
   GAP 1 performed ~2.8s vs 2.0s scripted.
5. U4: Laura's pocket-gaze lands cleanly only in the
   3.0s frame; his chalk reads raised toward her
   rather than arrested mid-stroke at the wall.
6. Plate approximations: static chalk stacks over
   drifting framings — small grazes where a stack's
   edge crosses a head or board edge (U2 residue at
   the Watcher's hairline; the freeze stack at Laura's
   hair edge). The wall text itself is everywhere the
   post layer, as the law requires.
7. Container wart: the master's format/video duration
   fields read 60.041667s (one extra frame interval in
   the mdhd) while the decoded content is exactly
   1440 frames with a 60.000000s audio stream.
8. Loudness lands at −18.61 LUFS (target −18) with
   TP −2.29 (ceiling −2): inside a decibel on the
   integrated figure, compliant on true peak.
9. U1's take carries faint generated palette-word
   chalk on the wall at frame right (accepted at
   take level by the first coordinator; the PIL stack
   covers the wall's record field).

Social caption (BRIEF §5.5, for the parent's posting
step): form TORN_FRAGMENT — "in his pocket yesterday".
