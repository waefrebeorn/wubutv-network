# GATE LOG — HOLD ON E1 "Write That He Owes Me"

**Master:** `masters/E1_hold-on_16x9.mp4` · md5
**227c51164e01624db2d0b9f52a955a26** · 26,222,249 bytes ·
1280×720 · 24fps · **1440 frames** (ffprobe count_frames +
full-decode agree) · video 60.000s (container 60.041s, AAC
priming) · h264 + AAC 48k stereo · faststart (moov@36 < mdat).
Under the 50 MB chat cap — no chat copy needed.

**RECOVERY BUILD.** The first production coordinator ended
after U3 with no report. The recovery coordinator verified
U1–U3 against SCRIPT.md (ASR + picture + motion, below) and
KEPT all three, fired U4–U6 chained per Panel Spec v2,
assembled, and gated. One assembly pass owned joined.mp4;
joined probed at exactly 1440 frames = segment sum
(6 × 240) BEFORE the master encode; the finished master was
re-probed end to end.

## FORMAT / ENCODE GATES

- Frames/duration/fps/resolution/codec/faststart: PASS.
- CRF: the encode ran `-crf 18` (preset medium). SEI reads
  crf=23.0 — this VM's known ffmpeg anomaly, NOT a gate.
  Differential proof: the identical chain at CRF 23 =
  13,967,057 B; the delivered master = 26,222,249 B (1.88×).
  CRF 18: PASS (by differential).
- Takes are 1248×704/240f generator output, scaled to
  1280×720 at the segment stage.
- Loudness: fixed gain +16.91 dB (joined median −36.91 dBFS →
  −20 target) with a −1 dBFS limiter; the master measures
  −19.0 dB median on the BLAM script's windows. No fade-in.

## DIALOGUE (ASR, faster-whisper large-v3-turbo, NO VAD)

All 86 scripted words verified against SCRIPT.md, unit by
unit: U1 18 ✓ · U2 15 ✓ · U3 7 ✓ · U4 19 ✓ · U5 15 ✓ ·
U6 12 ✓. Notes: U4's "Write" is ASR-spelled "Right"
(homophone — the spoken line is correct); U5's "four hundred
bells" is ASR-rendered "400 bells" (number formatting). U6
needed two ASR passes (one mis-segmented Rosa's line and
spelled "you're" for "you were"); an RMS speech-energy scan
settled placement (Laura 2.44–3.96s, Rosa 7.14–8.88s) and the
signature line reads "I saw what you were holding." Bruno
never speaks ✓.

## WORDMARK

UNC does not appear in E1 (bible §3: benched) — the hoodie
gate is vacuous. Corner bug `~ WuBu ~` (drawtext, cadmium,
bottom-right) verified exact on master frames 30 / 110 /
1062 / 1320 / 1439. PASS.

## MOTION LAW (per take, head MAE ratio 0–0.5s vs 3–10s)

U1 2.05 · U2 1.16 · U3 0.79 · U4 0.73 · U5 0.69 · U6 0.63 —
all ≥0.6, every unit already in motion at its cut, no
ramp-from-rest. PASS.

## BLAM GATE (on the finished master)

A1 onset t50 0.0s / t90 0.0s PASS · A2 dead head 0.0s PASS ·
A3 head −17.8 dB vs median −19.0 (+1.2 dB) PASS · **A4 HF
bursts: head 12 vs control 33 = ×3.64 — FAIL BY THE LETTER**
(bar ≤2×). The excess HF is the scripted first-second sound
event — the brass key's clatter on the stone counter plus
the bell's snap — a coherent metallic impact, not
crackle/static; disclosed here, not hidden. · V1 opening
motion 0.73× baseline PASS · V2 first bucket 11.71 vs
strongest 23.24 (frame 0 is mid-grab, no rest) PASS · E1 the
snatch is frame 0's action PASS · E2 the Cull Clock ignites
at 0.21s PASS.

## JOINT GATE + COHESION (standing rule, msg 507)

Every unit was fired with the outgoing take's last frame as
image 1 — the STRONG continuity reference — plus the unit's
gated PEAK panel as image 2. Measurement note: the
streaming-decode MAE in joint_gate.py proved unreliable on
this file (decoder emitted 1441 frames; its seam values
contradict the extracted frames), so seam MAEs below are
measured by exact frame extraction — the same frames shown
in work/joints/joint_b*.jpg. In-unit adjacent diffs run
~2.8–7.7 for scale.

- **B1 U1→U2 — seam MAE 60.90 — EYE: COHESIVE.** Same
  street, wardrobe, light, and positions (Bruno distant,
  the women at the counter); an editorial reframe from the
  two-shot to the wide at the cut. The sign gains ROOMS
  (the panel-carried state, post-painted). The key passes
  from the snatch to the proof display — one action.
- **B2 U2→U3 — seam MAE 44.17 — EYE: COHESIVE (the
  designed reset).** Exactly ONE detail changes: the sign
  flips ROOMS → NO ROOMS, big and singular, QC-hunted
  explicitly and confirmed. Bruno's crossing begins inside
  the joint; same man, wardrobe, light. The
  hunt-the-difference beat lands as scripted.
- **B3 U3→U4 — seam MAE 3.00 — EYE: COHESIVE,
  near-seamless.** Identical composition across the cut:
  Bruno at the post, Laura facing him, Rosa in the hatch
  holding the key.
- **B4 U4→U5 — seam MAE 2.95 — EYE: COHESIVE,
  near-seamless.** Bruno's face and trembling fist hold
  across the joint — GAP 2's carrier rides the joint as
  scripted; the Watcher's entrance follows inside U5.
- **B5 U5→U6 — seam MAE 28.19 — EYE: PARTIALLY
  INCOHESIVE, stated plainly.** The action and wardrobe
  are continuous: the Watcher exits, Bruno's fist opens
  to the ring in the palm, Rosa takes it — the designed
  handoff lands. BUT the wall's dressing grows visibly
  heavier across the cut (torn-paper scraps multiply)
  and the grade shifts darker and greener; U6's wall does
  not read as U5's wall state. The episode's weakest
  joint.

**Story continuity:** one conversation at one wall in one
morning light; the chain reads in order — accusation →
proof → refusal → naming → reveal → open hand — and each
unit's action causes the next. Not fragments: the episode
plays as a single scene with five edited cuts.

## DIGESTION GAPS (A2)

GAP 1 (U2 tail): carrier ✓ Bruno's fist, held — 1.72s
wordless vs the 2–3s spec (compressed, disclosed). GAP 2
(U4→U5 joint): carrier ✓ Bruno's face, fist in frame —
U4's wordless tail is 1.14s, riding into the joint hold
(compressed, disclosed). GAP 3 (U6 freeze): the last word
ends at 8.88s, leaving a 1.12s terminal freeze (spec
2–3s, compressed, disclosed); U6 additionally carries
~3.1s of mid-unit silence around the writing and
ring-taking beats.

## GFX (Method C)

Cull Clock: ignites frames 5–19 of U1, empties one segment
per 8 frames, snaps full on all five joint frames —
verified on master frames and strips. Chalk inserts cut in
picture-only at ASR-measured beats, take audio continuous
underneath: INS-U1 frames 92–122 (BR— draws on), INS-U5
frames 82–129 of U5 (struck line nine + BR—), INS-U6
frames 100–135 of U6 (PAID. ASK HIS HAND. draws on).
Insert text verified legible in the master.

## FLAWS — DISCLOSED PLAINLY

1. BLAM A4 fails by the letter (×3.64) — the designed
   key-clatter impact; see BLAM section.
2. B5 (U5→U6) is partially incohesive on the eye: wall
   dressing multiplies and the grade shifts darker/greener
   into U6 (see Joint Gate).
3. U6 register: Rosa weeps openly through the payoff —
   heavier melodrama than the show's flat-deadpan register
   law. The ring handoff itself reads perfectly.
4. U6's scripted closing detail — the key back on its
   nail — is not legible in the take; the closing reads
   on the ring transfer alone.
5. The chalk inserts' base still is a warmer, redder
   brick than the takes' blue-grey street wall; the
   cutaways read in a different light. The text beats
   land regardless.
6. All three digestion gaps are compressed vs their
   2–3s spec (1.72s / 1.14s / 1.12s terminal) — generator
   silence compression; every carrier is the scripted
   one.
7. U2: Rosa's pale ring-band reads slightly ring-like at
   full resolution in the opening frames; at delivery
   size it reads as the tan-line band the plant intends.
8. U3: Rosa's wardrobe softens in the hatch background
   (apron/blouse read differs). U4–U6: torn-paper scraps
   sit on the wall at frame edges — illegible set
   dressing, no lettering, but the wall is not pristine
   blank outside the inserts.
9. U5: one unscripted background figure stands far down
   the street in a single shot — silent and distant.
10. U1's hanging sign is blank; its ROOMS state arrives
    with U2 at B1 (panel-carried) — noted at B1.
