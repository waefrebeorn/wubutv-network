# MV-3 Volley 11 QC — 1 KEEP, 0 REJECTED, 0 failed

Volley 11 (parent-ordered single-take volley): S38 t2 (CHARACTER
reroll) alone. Cap 6, 1 used — nothing else fired. The take landed
on the first attempt; no re-fire needed.

Method: faster-whisper base on take audio (RAW words, mishear classes
noted; numpy array input — the venv's av decode path is broken, see
qc10_analyze.py; per-take temp wav, transcribed sequentially — no
parallel-run cross-contamination possible on a single-take volley).
Full 1s–8s tile in qc11/ (the axis turns on the face; a contact
sheet alone is NOT a drift check). Motion from 160x90 gray frame
diffs. Near-dup threshold: mean abs diff <0.5. Frame gate: FAIL if
vocal near-dup (<0.5) run ≥24f during words OR vocal mean diff <0.5;
runs entirely in inter-repeat/inter-phrase gaps or post-line holds
with healthy word-window means PASS with disclosure (S22/S25
precedents). Ratio = song slot (line-table span) / take line (first
word onset to last word end). Usable 0.80–1.25; grey 0.60–0.80 /
1.25–1.60 (warp-rescue ≤1.5x to band edge at assembly only — no
warping in this volley); clear miss outside grey. Lyric-sequence
gate FIRST (ratio is not a lyric gate). A take sings its line
exactly once — no part of it a second time, and no part of it
missing (repeat defect = sequence fail; incomplete delivery =
sequence fail). Mishear classes on this track: game=dad,
dogs=hooks, see=say, word=words. One axis per reroll verdict.

## S38 t2 — KEEP (grey) — CHARACTER axis FIXED

- Lyric sequence: PASS. Full L39 exactly once, in order, 0.00–7.32:
  "Say it back to me, I am your dad, say it to yourself." No
  mishears, no part missing, no part repeated. Same delivery as t1
  (t1: 0.00–7.14) — the reroll changed only the character spec,
  per the one-axis rule.
- Ratio: slot 5.36s (L39 338.55–343.91) / line 7.32s = 0.73 → GREY.
  Warp 0.92x duration to the 0.80 edge at assembly (within the
  1.5x cap). Same band as t1 (0.75 grey) — pacing is not the axis
  here and was not re-opened.
- G1 character: PASS — the CHARACTER axis is fixed. A full
  8-sample tile (1s–8s) shows the big round ball head with solid
  black OVAL eyes, wide open, no white, no lids, in every frame —
  never dots, never egg-shaped. The S30 t3 strengthened oval spec
  now holds a third time (S30 t3, S36 t2, S38 t2): the dot-eyes /
  egg-head face variant that t1 imported on the standard vehicle
  is gone. Suit + cadmium tie, street-corner set. This closes the
  face-variant class: three cures, zero remaining members.
- G2 text: PASS. Plain corner walls, street furniture, fire
  hydrant, utility boxes — objects, no legible text anywhere.
- G4 performance window: PASS. Point on the call (1s–4s), hand to
  ear post-line (5s–8s) — matches the plan exactly, same staging
  as t1. Mouth open at speaking beats (2s/3s/4s); the 5s closed
  smile sits in the gap between "dad," (ends 4.86) and "say"
  (starts 5.38), a speaking rest, not a still.
- Frame gate: PASS with disclosure. Word-window vocal mean diff
  1.745; longest <0.5 run in vocal window 9f (1.71–2.08s, under
  the 24f gate). The 18f full-take run at 7.17–7.92s straddles the
  line end (7.32) into post-line rest — post-line-hold class,
  disclosed.
- Specs: 1280x720/24fps, 10.000s, md5 3edad7af7f76fd1bb7e8ffdca22c8de6.

## Volley-11 tally

KEEP: S38 t2 (grey 0.73, character FIXED). REJECTED: none. UNFIRED:
none — 1 attempt, 1 landed, 0 failed. No take was warped in this
volley.

Active keeps now 31 (30 + S38 t2). Structural set unchanged:
S04, S05, S21, S24, S25, S30, S35. Assembly decisions unchanged:
S37, S39. All 39 scenes are now resolved — no scene is left
unfired, unkept, or undecided except at the assembly layer (S37 /
S39 coverage, S25's 19.66s slot, structural covers for S04 / S05 /
S21 / S24 / S25 / S30 / S35). The build moves to assembly
(word-timed line-block+highlight captions, corner bug, 16:9 + 9:16
masters + chat copy, frame-exact counts, motion audit on the
delivered master).

Pattern: the strengthened oval spec is now 3/3 (S30 t3, S36 t2,
S38 t2). The face-variant class is closed — standard vehicles
imported it twice (S36 t1, S38 t1); the strengthened spec cured it
every time it was carried. Any future character reroll on this
track (none owed) should carry it by default.
