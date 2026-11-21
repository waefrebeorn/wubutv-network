# THE NIGHT LIST — E1 "The Sol Night" — GATE LOG

## STATUS: PRE-PRODUCTION COMPLETE — FIRING BLOCKED ON A MISSING VIDEO ALLOWANCE (2026-11-16)

**Zero videos have been generated.** The media tool contract for delegated
tasks states: when a task comes from another agent, check that the task states
how many videos the agent may make; if it does not, make none and say so.
The production brief for this episode states no video number. Everything else
is built and firing-ready (panels, plates, vehicles, assembly). Remedy: a
follow-up instruction stating an explicit allowance (the tool caps at 6
successful videos per message regardless; the episode's first pass is exactly
6 — one per unit — with any refires needing a further message).

## Pre-production record

- Workspace: panels/ takes/ masters/ work/ (+ qc/frames/stills) created;
  work/measure.py + work/asr.py inherited from E2_SHOW-3 (BLAM/joint/tail
  harness, house G7 ASR).
- Inherited panels copied from E2_SHOW-3 and md5-verified identical:
  CHAR-KEEPER 4cf35e28…, CHAR-UNC 4e552aed…, CHAR-LAURA 4c2159f6…,
  CHAR-DISPATCHER e6e6a05f…, WORLD-roster-room 136b5540….
- New panels generated + eye-read (verdicts in REFERENCE_STACK.md):
  CHAR-SOL (PASS), WORLD-night-desk (PASS — desk/board/beds/doorway all
  staged per the slate ruling), PROP-board-blank (PASS — 11 ruled rows),
  PROP-log-blank (PASS), ANCH-U1 (PASS), PEAK-U2 (PASS), PEAK-U3 (PASS —
  the PIL noon entry survived conditioning onto the page), PEAK-U4 (PASS),
  PEAK-U5 (PASS).
- Post plates built deterministically (PIL; scripts in work/gfx/):
  board_stateA (SOL struck), board_stateB (SOL restored; ships as
  PNL-PEAK-U6), log_page (NOON "12:00 — SOL struck — U.", NIGHT blank),
  PEAK-U1 (strike 65% across SOL, dust burst), PEAK-U4 receipts (the two
  slips at UNC's hands marked BED 7 in post ink).
- VEHICLES.md: exact firing prompts for U1–U6 locked (E2 proven shape:
  single PEAK/chain anchors, trait lines verbatim, dialogue LAST as one
  quoted block, brisk pacing on the two FULL-TALK units).
- REFERENCE_STACK.md: all five boundaries classified JOINT; J4 = U5
  re-anchor; rotation + harvest protocol written.
- work/assemble.sh: house assembly written and ready (conform 240f ×6 →
  joined probed = 1440f → one uninterrupted encode → CRF-23 differential →
  chat copy if >50 MB → end-to-end probe).

## Pre-disclosed flaws / risks (known before firing)

1. The Keeper reads older than his late-30s sheet in the inherited CHAR
   panel — a build-recurring flaw from E2, accepted there; carried knowingly.
2. PEAK-U3's page carries real drawn text (mine, PIL) — intentional: it is
   the script's seen reveal, and the plate insert fallback exists if the
   take's page drifts.
3. The BED 7 receipts on PEAK-U4 are small in frame; their legibility in the
   take depends on the generator's push-in. The U1 bed-tag beat is carried
   by vehicle text only (no tag plate) — a wants-beat, not a gate.
4. WORLD-night-desk keeps the inherited TELEVISION STATION CLOSED sign as
   set dressing (canon: the office sits in the closed station).
5. PEAK-U5's board is a wide chalkboard variant vs the tall board elsewhere
   (generator variance); the U5 name reveal is a post composite/insert by
   design, decided at QC and disclosed either way.
6. U4 remains the tight unit (DECISION_LOG Pass 4): UNC's entrance must run
   UNDER Sol's first line or Gap 2's carrier compresses — QC checks the
   carrier (Sol's held face), not a word count.

## Gates — TO BE MEASURED AT FIRING

- BLAM (U1 + master): A1 t50 ≤0.5s / t90 ≤1.5s · A2 dead head ≤0.2s ·
  A3 head within 6 dB of median or accent ≤0.5s (a chalk-snap accent is
  pre-built into assemble.sh, disclosed) · A4 crackle ≤2× control ·
  V1 opening motion ≥0.6× baseline · V2 no ramp-from-rest ·
  E1 named impact ≤1.0s (the strike) · E2 first cut/graphic ≤3.0s.
- ASR verbatim per unit (G7); homophones cleared by amplified-slice
  hand-checks only.
- JOINT GATE per boundary: seam MAE ≤58 (320×180 gray); item 6 by visible
  motion + calibration log (the ≥8 head-MAE floor is miscalibrated).
- Wordmark: U4 full-span sweep wherever UNC's chest is visible;
  glyph-exact "~ WuBu ~" or one refire; second drift = no ship.
- Digestion-gap carriers: U2 the Keeper's stare at the wet strike ·
  U4 Sol's held face to UNC · U6 the freeze (question card in post).
- Format: 6×10s, 1280×720, 24fps, EXACTLY 1440 frames, CRF 18 (proof =
  size differential vs CRF-23, logged), AAC, faststart, corner bug,
  loudness pass. E1_DELIVERED.flag on completion.

---

## FIRING + ASSEMBLY RECORD (replacement coordinator, 2026-11-16)

Authorization: parent follow-up brief with EXPLICIT video allowance (6 units,
user msg 497 standing order). All six units fired first pass — zero 429s,
zero refires needed. Raw takes: 1248×704, 24fps, exactly 240f / 10.000s each.

### Per-unit QC
- **ASR verbatim (G7): PASS ×6.** U1 "You struck my name. I slept in the rain.
  Sit down, Sol. One quiet night." · U2 "I watched Peter pay you at midnight.
  UNC takes Peter's money. Not me. Then why is it still wet?" · U3 "Nobody
  struck him at night. It was noon. I'm never here at noon." · U4 "I knocked
  at noon. The desk was empty. You sold his bed at noon. Let him blame the
  pen." · U5 "One on. One off. That's the rule." · U6 "Eleven names. Ten
  beds. Then strike yours, Keeper. Or strike mine." (ASR prints "11" for
  "Eleven" — numeral normalization only; words match.)
- **Wordmark (U4, full-span sweep): PASS, no refire.** UNC's chest is visible
  only in the opening receipts setup (frames 0–48 sampled at 0/24/48 + crops);
  glyph-exact "~ WuBu ~" in yellow-gold, small, shadowed, at the frame's right
  edge in every chest-visible frame. No drift anywhere in the span.
- **Gap carriers: ALL PRESENT.** Gap 1 (U2 tail): the Keeper's held profile
  stare at a list bearing vermilion strikes. Gap 2 (U4 tail): Sol's held wet
  face turned toward UNC. Gap 3 (U6 tail): the freeze — hand + chalk hovering
  under KEEPER on the board, question card over it in the master (57–60s).
- **Post-beat map outcomes:** U1 frame 0 = the vermilion mark on SOL already
  on the board (S vermilion + stroke under the name); the strike-completion
  overlay was NOT needed. U3's log page READS in-take at frame 0 — "NOON /
  12:00 / SOL struck / — U.", NIGHT column blank — the PIL entry survived
  conditioning (plate insert not needed). U4's slips read BED 7 in-take at
  UNC's hands. U5's writing is IN-TAKE: the Keeper writes S-O-L stroke by
  stroke in close-up (post stroke composite / board_stateB insert NOT
  needed). U6's board pan reads LAURA/EMMETT/TESS/HAROLD → KEEPER in chalk.
- **Motion / tails:** U1 tail joint frame 213 (MAE 6.22 ≥ median 6.14) —
  Sol's look at the beds carries J1. U5 tail MAE 6.22 — still drifting
  closer at the cut: a true motion cliff into U6. U2 tail settles to the
  stare (carrier by design). U3 tail near-still (see flaws). U4 tail
  settles onto Sol's face (carrier by design). U6 tail = the freeze.

### JOINT GATE (seam MAE, 320×180 gray, bar ≤58)
J1 22.35 ✓ · J2 46.77 ✓ (stare → log page; highest, still under bar) ·
J3 24.12 ✓ · J4 (declared re-anchor) 22.71 ✓ · J5 15.70 ✓.
Item 6 (head motion): U2/U3/U4/U6 heads all open in motion or on a
picture event (log page at U3 frame 0); logged as calibration data.

### BLAM
- U1 take: A1 t50 0.0 / t90 0.0 ✓ · A2 0.0s ✓ · A3 +2.3 dB ✓ · A4 4 ≤ 2×4 ✓
  · V1 1.48 ✓ · V2 ✓ · E1 the vermilion strike on SOL at frame 0 ✓ ·
  E2 the strike/board is the frame-0 graphic event ✓.
- Master: A1 t50 0.0 / t90 0.1 ✓ · A2 0.0s ✓ · A3 +5.9 dB (snap accent at
  0.25s, pre-built in assemble.sh, disclosed) ✓ · A4 3 ≤ 2×7 ✓ ·
  V1 1.48 ✓ · V2 ✓.

### Assembly
One assembly pass. joined.mp4 probed = 1440f BEFORE the master encode;
single uninterrupted master encode; master re-probed end to end:
h264 1280×720 24fps, **exactly 1440 frames**, AAC, 60.000s, faststart
(moov ahead of mdat), "~ WuBu ~" corner bug throughout, question card
over the U6 freeze, loudness pass (loudnorm I=-16).
**CRF-18 proof (size differential): master 20,594,921 B vs CRF-23
10,594,187 B = 1.94×.** Master ≤50 MB → no chat copy required.
**Master: masters/E1_the-night-list.mp4 — md5 c8154d92aff983396029cf60f8b57f63.**

### Repairs made during production
- assemble.sh step 3 as inherited had a filter-graph syntax error
  (`asetpts...[loudnorm=...][base]` — two link labels on one output);
  the first assembly run died at the master encode AFTER joined.mp4
  probed 1440. Fixed in place (loudnorm chained with a comma) and the
  encode re-run from the verified joined.mp4. Disclosed here per the
  one-assembly-pass rule: the joined intermediate never changed hands.

### FLAWS — disclosed plainly
1. The Keeper reads older than his late-30s sheet (pre-disclosed #1,
   inherited CHAR panel; consistent across all six units).
2. U1's strike reads as a vermilion S + underline stroke on SOL rather
   than a full diagonal strike-through; legible at frame 0 and at phone
   size, but softer than the PEAK plate's 65% stroke.
3. U1's mid-room board renders as a two-column roster (generator
   dressing) behind Sol; the roster that reads canonically is U6's.
4. U3's tail is the Keeper held in the doorway, NOT the scripted
   noon-column-stays-in-frame; J3's paper→paper handoff therefore lands
   as face→desk. The reveal itself is unaffected (page reads at U3
   frame 0). U3 is also the stillest take (median MAE 1.75).
5. U3's NIGHT column header glyphs are slightly garbled/reversed in
   the page close-up; the column is blank as scripted and the NOON
   entry is crisp.
6. U5's board is the wide variant (pre-disclosed #5) and carries only
   the SOL row in close-up; the other ten names are established in
   U1/U6, not re-shown in U5.
7. PEAK-U3's drawn page (pre-disclosed #2) shipped as designed — the
   in-take page IS the PIL-conditioned plate image.
8. The U1 bed-tag beat (Production Notes beat 4) is not legible in the
   take — the bag lands by the empty bed, but no readable BED 7 tag;
   logged pre-production as a wants-beat, not a gate.
