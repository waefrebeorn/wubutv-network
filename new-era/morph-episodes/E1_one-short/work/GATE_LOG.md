# GATE LOG — ONE SHORT, E1 "Thirty-One Umbrellas"

Master: masters/E1_one-short_MASTER.mp4
md5 3b57d253a547ca40e82cf9bb6fb4df06 · 19,409,317 bytes
1280×720, 24fps, h264, EXACTLY 1440 frames (count_frames probe), AAC 48kHz
(mono — the generated takes are mono), faststart (moov @ byte 36, before
mdat), video exactly 60.000s (container 60.041s = AAC padding).
Under the 50MB chat cap as shipped — no chat copy needed.

## Format / encode gates
- Segments: 6 × 240f conformed (scale/crop to 1280×720, 24fps); joined
  probed BEFORE the master encode = 1440f = segment sum ✓ (one assembly
  pass owned work/joined.mp4; single uninterrupted master encode;
  master re-probed end to end ✓).
- CRF 18 proof by size differential (SEI string is not a valid gate on
  this ffmpeg — AGENTS.md): same chain at CRF 23 = 11,262,064 B;
  master = 19,409,317 B → 1.72× ✓.
- Loudness: joined measured −22.65 LUFS / TP −0.54. The first master
  encode's chain (volume −1.0dB + alimiter 0.84) did NOT hold the ceiling
  (measured TP −0.4 dBFS — the limiter passed the peaks; that encode was
  discarded pre-delivery). Shipped master: audio re-encoded at −1.2dB
  (video stream copied bit-exact) → integrated −23.37 LUFS, true peak
  −1.66 dBFS ✓. No fade-in ✓.

## Dialogue gate (ASR, faster-whisper large-v3-turbo int8, NO VAD)
Full-master ASR in work/qc/master_asr.txt. All 14 scripted lines present,
in order, by the scripted speakers, word-exact with three disclosed
deviations:
1. U1 count overshoot: "Nine, ten, eleven—" is followed by a completed
   "12" (the count continuing in character).
2. U4 trailing echo: "…Not me." gains a repeated final "Me."
3. U6 catchphrase doubled: "The book doesn't blink." is spoken twice
   (script: once).
Hand-checks passed per E2 precedent: "hire" ASR-rendered "higher"
(homophone); number lines ASR-rendered as digits; U6's stressed "GO"
ASR-rendered as spelled letters "G-O" (emphasis artifact — the script's
words with the script's stress).

## The board (Method C arithmetic audit)
Post board only (PIL, deterministic); generator piles were never asked to
carry a count. State chain verified on frame grabs:
––|–– → CLAIMED 31 @0.30 (the slam) → COUNTED 20 @18.94 (on "twenty") →
COUNTED 30 @29.00 (U3 tail, batch complete in silence) → COUNTED blank
@30.00 (recount) → COUNTED 30 @39.00 → settle 30|31 with a pulse @50.42
(on "umbrella"). Values change ONLY on naming beats, never at frame 0 ✓.
30 counted vs 31 claimed = one short ✓. Board legible at phone size
(390px check) ✓. In-world board windows stay blank in every take ✓.
U6 cliff also ships as a post card ("Then where does the one GO?", serif
italic, bone on ink) fading in over the freeze from 57.98s; it reaches
full alpha ~0.1s after the spoken line ends — negligible overlap,
disclosed.

## BLAM GATE (on the finished master; U1 segment measured separately)
A1 FAIL — t50 1.0s (bar ≤0.5), t90 2.3s (bar ≤1.5). Structural: the
take's want-line lands at 1.58s; the slam stack carries A2/A3 but cannot
pull the first-3s energy centroid under the A1 bars. A head trim was
evaluated and rejected: modelling showed it could not flip either bar
without cutting into the crash and the entrance.
A2 PASS — dead head 0.0s. A3 PASS — accent −17.1 dBFS inside 0.5s, head
0–1s at −18.0 vs median −36.5. A4 PASS on the master (0 head bursts vs 0
control; note the raw U1 segment measured 31 vs 2 — the limiter pass
tamed the crash transients below the detector threshold; the segment
number is recorded here for honesty). V1 PASS — opening motion ratio
1.65 (bar ≥0.6). V2 PASS — no ramp-from-rest (first bucket 6.03-class,
in-motion at frame 0). E1 PASS — named impact (door slam + bell +
umbrella crash) at ≤0.5s. E2 PASS — first graphic (board flip) at 0.30s.

## JOINT GATE (measured on joined and re-measured on the master)
Baseline 95th pct ≈11.5, median ≈5.9. Seam MAEs: J1 1.13, J2 1.90,
J3 0.80, J4 1.87, J5 0.89 — all far under the ≤58 bar: PASS ×5.
Item-6 (distribution-relative rule, post-msg-470): head-12 means
8.86 / 15.15 / 8.60 / 14.97 / 14.05, all ≥ episode p25 (2.74) and ≥
baseline median: PASS ×5. Every cut lands in motion ✓.

## JOINT EYE-COHESION (msg-507 standing rule — eye verdicts, not MAE)
This build was fired with the pre-507 method (resume chains; chained
units have no image slot, so no joint was strong-reference conditioned
on a harvested last frame). The MAE numbers above are near-zero and
would claim perfect cohesion; the eye check says otherwise at two
joints. Logged plainly:
- J1 (U1→U2): CAST COHESIVE / WORLD INCOHESIVE. Faces, wardrobe and the
  count carry across the cut, but the room re-dresses from the shopfront
  counter to a back-office desk (green banker's lamps, noticeboard, a
  background staffer). The cut reads as a world swap behind held
  elements.
- J2 (U2→U3): COHESIVE. Same desk-office world; the Counter is large on
  both sides, mid-action; the cut is a coverage angle change on a
  continuous action.
- J3 (U3→U4): WORLD COHESIVE / BLOCKING JUMP. Same office state, but
  the Planner crosses to the Counter's side off-screen across the cut
  (her U4 move is scripted; it is not witnessed).
- J4 (U4→U5): WORLD INCOHESIVE / CAST REPAIRED. The designed re-anchor
  swaps the room back to the shopfront (bone counter, shelves, board)
  and restores the true Clerk (bob + spectacles) after the U3/U4 drift.
  Story logic (recount → the book) carries; the room does not.
- J5 (U5→U6): COHESIVE. A coverage cut from the book two-shot to the
  Counter at the shelves; world family, wardrobe and light continuous;
  the story beat (book → shelf count) carries the cut.
STORY COHESION (msg-507 note): the episode's story reads as ONE
continuous count — claim → count → accusation → recount → the book →
the shelf — carried by verbatim dialogue and the board's state chain;
it is not trailer fragments. The picture's world state is the weak axis
(J1, J4 swaps; the U3/U4 Clerk drift between them).

## Digestion gaps (A2 — verified like word counts, from master ASR)
- GAP 1 (after U2's turn; carrier: the Counter's stopped hand): ~1.0s of
  silence inside U2 after "twenty" (ends 19.02s ep), and the experienced
  pause to the next spoken line is 3.06s across the joint. PASS as
  experienced; the intra-unit portion is compressed (generator pattern,
  cf. every E2 build).
- GAP 2 (after U4's peak turn; carrier: the shelf, CCTV angle): NOT
  REALIZED. U4's dialogue runs to 39.44s ep (9.36s local), leaving no
  room inside the 240f segment for the 2–3s insert. PNL-SHELF was
  generated and gated (one umbrella, handle up, phone-legible) but is
  not cut in. The shelf pays off in U6 instead. FAIL — disclosed.
- GAP 3 (final 2–3s of U6; carrier: the Clerk's face): silence from
  58.12s to 60.00 = 1.88s under the question card. Marginally under the
  2–3s script; the freeze framing is the Planner+Clerk two-shot, not
  the scripted single on the Clerk. PARTIAL — disclosed.
- Reaction holds: after the receipt line 1.78s ✓; after the naming line
  1.92s ✓; after the price reveal 3.60s of book business ✓.

## Shelf vs LEDGER §5
Required state: ONE umbrella (black, from the hire load), standing,
handle up, on the shelf behind the Clerk. Verified in PNL-PEAK-U6 and in
the U6 take (the umbrella stands on the shelf behind the Counter as he
counts it, frame-left, legible) ✓. No other unit shows the shelf
stocked ✓.

## Identity / wordmark
- Clerk: holds in U1, U2, U5, U6 (her sheet rode both fresh calls);
  DRIFTS in U3/U4 background (bob + spectacles lost; no lines in those
  units) — disclosed above and in TAKE_HISTORY.
- Counter: holds all six units (tally counter on chain visible; it
  renders as a round disc in U1's tail — device-class nit).
- Planner: holds all six units (new sheet, generated for this episode).
- Cobalt: the Clerk's ink reads as full blue gloves mid-chain and as
  bright cyan in U5/U6 — saturation drift, disclosed.
- Wordmark gate: UNC is not in this show's cast — NOT TRIGGERED (E2
  ruling carried). The network corner bug ("~ WuBu ~", gold Noto Serif
  Bold, bottom-right, post) is verified on frame grabs ✓.
- No readable in-take text anywhere: receipts and book pages render as
  blank paper / illegible scribble-numerals ✓.

## Verdict
SHIP with disclosed flaws: BLAM A1 fail; GAP 2 unrealized; GAP 3
marginal + two-shot framing; Clerk background drift in U3/U4; world
swaps at J1/J4 (eye cohesion partial — story cohesion holds); three
one-word dialogue deviations (count overshoot, echoed "me", doubled
catchphrase). All other gates pass.
