# RESUME SPEC — HOLD ON E3 Part 1, v6 production, session 2

Written by session 9a09f35c (2026-11-18) at a clean stop.
Read with: SCRIPT.md (v6 LOCKED), BRIEF.md, DECISION_LOG.md
(R3-1..R3-4), GATE_LOG.md §§E.4/F/G, work/GATE_LOG.md §6.

## State

- U1 v6: ACCEPTED — takes_v6/U1_t1.mp4
  (md5 b20112cc85e822449a8899a4e1a0783e). Chain frame:
  work/chain/U1v6_last.png.
- U2 v6: t1 REJECTED (TEXT sash lettering + PROP second
  bouquet; speech was 17/17). Take is outtakes/material,
  never assembled. Full QC: work/GATE_LOG.md §6.2.
- U3–U6: not fired. No assembly, no master, no flag.

## Owed, in order

1. **U2 t2** — vehicle BANKED: work/vehicles_v6/U2_v6_t2.txt.
   Images, in order: work/chain/U1v6_last.png (1) ·
   panels/PNL-PEAK-U2-tinoverpalm.png (2) ·
   panels/PNL-CHAR-FRUIT-16x9.png (3). Fire it as ONE call.
   QC per §6 pattern (frames at 0/2.5/5/7.5/9.9 + zooms on
   the sash and the Lime's hands; dual-checkpoint ASR:
   /tmp/asr2.py pattern — faster-whisper large-v3 +
   distil-large-v3, VAD on, condition_on_previous_text=False,
   audio fed as an ffmpeg-decoded float array because this
   VM's PyAV rejects faster-whisper's file path). Watch
   specifically: sash lettering (any frame), a second
   bouquet, her one-handed hold during L3, tail = pin.
   On PASS: harvest work/chain/U2v6_last.png from the tail.
2. **U3 t1** — vehicle BANKED: work/vehicles_v6/U3_v6.txt.
   Images: U2v6 chain (1) · panels/PNL-PEAK-U3-hands.png (2) ·
   panels/PNL-CHAR-LAURA-face-e2.png (3). Standing hazards:
   speaker identity (face bound + casting rule — in the
   vehicle), board text (late assertion — in), tin/palms
   absence (in), tail performance (closing block — in).
   If a defect is confined to post-speech frames against
   the pinned hands-up tableau, the parent-ruled TAIL TRIM
   precedent applies (trim to last compliant frame, hold,
   disclose).
3. **U4 t1** — vehicle BANKED: work/vehicles_v6/U4_v6.txt.
   Images: U3 chain (1) · panels/PNL-PEAK-U4-naming.png (2) ·
   panels/PNL-CHAR-LAURA-face-e2.png (3) ·
   panels/PNL-WORLD-market-wall.png (4). The board runs the
   R3-4 three-layer countermeasure (geometry binding via
   image 4 + the size/position-named Final assertion). If
   the board letters again: STOP the unit, record a
   board-free reframe recommendation — no third board
   attempt.
4. **U5 t1** — vehicle BANKED: work/vehicles_v6/U5_v6.txt.
   Images: U4 chain (1) · panels/PNL-PEAK-U5-spill.png (2) ·
   panels/PNL-CHAR-FRUIT-16x9.png (3). Watch: exactly nine
   coins, three into the drain; the accused's hands never
   move; the Peach's held face at the head (dead/wandering
   eyes = reject); sash blank.
5. **U6 t1** — vehicle BANKED: work/vehicles_v6/U6_v6.txt.
   Images: U5 chain (1) · panels/PNL-PEAK-U6-hover.png (2 —
   DESTINATION, never image 1) ·
   panels/PNL-CHAR-LAURA-face-e2.png (3) ·
   panels/PNL-WALL2-closeup-16x9.png (4). Watch: no letters
   formed by any chalk; the freeze holds the pin.

## Then

- Conform each accepted take to 1280×720, 24fps, exactly
  240f, AAC 48k (takes land 1248×704 — scale/pad). Per-joint
  eye log (BRIEF §5.3) as each chain frame is harvested.
- PIL plates (assembly, on the takes' wall regions; judge
  at Gate (f)): U1 docket line (SHE HELD MY TIN. MY COINS
  ARE GONE.) persisting U1–U5; U4 adds the tally rows beside
  it; U6 plate set: the docket line struck through, the true
  line beneath (HANDS OPEN. COINS LOOSE.), the board card
  (TOMORROW: THE NAME HE WON'T WRITE.), and the freeze
  question on the final freeze (SHOULD LAURA WRITE THE
  PEACH'S NAME?).
- ONE assembly pass owns joined.mp4; ffprobe it against the
  1440f segment sum BEFORE the master encode; single
  uninterrupted encode; re-probe the master end to end.
- Master gates in order (BRIEF §5.4 + dispatch): format
  probe (CRF 18 by SIZE DIFFERENTIAL vs a CRF-23 control of
  the same chain — never the SEI string) · BLAM A1–A4/V1–V2/
  E1–E2 · F-9 protocol-correct (speaker-attributed master
  transcript interleaved with picture summaries; exactly one
  re-run if an input defect is found) · EAR-TEST (cold listen
  of the master's own audio) · Gate (f) cold run · STRANGER
  TEST (MASTER) under the §3 Q2 Camp B clarification
  (DIALOGUE_METHOD.md §3; picture-answered lines judged here)
  · POSTER_FRAME · ZHE CHECKS (muted pass: sound off AND
  subtitles off). A dialogue-plausibility failure at master
  stage STOPS the episode for the parent — never
  disclosure-shipped, never self-repaired by rewriting lines.
- Delivery on ALL PASS: master at masters/ per the brief's
  naming, chat copy ≤50 MB under a FRESH filename,
  E3_DELIVERED.flag at the episode root, COMPLETION.json
  before the final report. No commits (the parent commits).

## Spend ledger

Session 1 (9a09f35c): video 2 (U1 accept, U2 reject) ·
images 0. Lifetime v5 production spend is recorded in
DECISION_LOG / work/GATE_LOG §§0–5 and does not carry into
the v6 allowance except as history.
