# MV-16 — VOLLEY PROGRESS

## Pilot (3 clips, template proof)
- t1 (S01/S05/S22): ALL REJECT G1 — photoreal, wrong faces (no anime
  lock in vehicle text). Word delivery verified by ASR (G7 1.00/0.90/1.00).
- Fix: anime lock line + anime character intros in ALL vehicles
  (MV-15 v2 template).
- t2 (S01/S05/S22): ANIME HOLDS on all three (frames read full-res).
  - S05 t2 KEEP — G7 pass (wrote/rode homophone override), ratio ~1.09.
    [SUPERSEDED at conform: t2 sings the friends' lines over S05's
    belted-car span — generator drift. S05 ships t3 (d2784618).]
  - S22 t2 KEEP — G7 1.00, ratio ~1.05, medium swap reads perfectly.
  - S01 t2 REJECT (sync) — words exact (G7 1.00) but delivery
    front-loaded: lines 1–2 by 3.7s, then 3.4s of closed-mouth
    blissful posing (frames 5.0/7.0 confirm mouth closed), "stopped
    me" lands 7.08–8.28 vs song 3.82–5.24 — outside warp caps for the
    hook slot. Re-fire as t3 with no-pause pacing language.

## Volley 1 (fired 2026-11-13): S01 t3, S02, S03, S04, S06, S07
## Volley 2: S08–S13 · Volley 3: S14–S19 · Volley 4: S20, S21, S23–S26 · Volley 5: S27, S28
All landed, no 429s. 47 clips on disk at this checkpoint (incl. pilot
+ rejects); a 48th (S05 t3) was fired at conform — 48 takes total.

## GRID AUDIT (2026-11-13) — the big catch
Scene-plan line mapping had been written from the lyric SHEET; the
PERFORMED grid (grid_lines.json) differs in chorus rotation and in
V1/V2/PC/OUT line texts. Take-ASR (disk-verified) confirmed which
takes sang sheet text. Verdicts:
- KEEP (text true): S01 t3 (t4 fired as pacing alternate), S02 t1,
  S09 t1, S10 t1, S13 t1, S22 t2.
  (S05 t2 was listed here in error — at conform it proved to sing the
  friends' lines over the belted-car span; S05 ships the t3 re-fire,
  d2784618. See TAKE_HISTORY.md.)
- REORDER-SALVAGE (right words, rotated order; chunk-reorder in
  assembly): S03 t1, S11 t1 (+ S20/S26 pending disk-ASR verify).
- REJECT (sheet text) → re-fired with grid text: S04, S06, S07, S08,
  S12, S14 (RF1) · S15, S16, S17, S19, S21, S23 (RF2) · S27, S28 (RF3).
  All RF takes landed; ASR verification in progress.
- S18/S24/S25 verdicts pending DISK take-ASR (an ASR delivery whose
  numbers were not backed by files on disk was discarded — disk is
  truth; the batch chain is re-verified file by file).
