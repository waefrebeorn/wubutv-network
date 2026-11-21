# FINISHER2 STATUS — HOLD ON E2 replacement production finisher (2026-11-17)

Session start ~06:47 EST. Predecessors: continuation coordinator
(gated script, fired U1_t2) + finisher 1 (QC'd U1_t2, fired
U2_t2 + U3_t2, ran ASR on both, extracted QC sheets, died
~11:15Z mid-QC — no written verdicts anywhere; GATE_LOG has
zero t2 entries).

## STATE FINDINGS (verified from disk this session)

- SCRIPT.md = gated repair script (Gate E REPAIR3 ALL TWELVE
  PASS, work/GATE_E_REPAIR3_VERDICT.md). REPAIR_CALLS.md =
  the t2 volley spec (verbatim calls, SR1 rotation).
- takes/: U1_t1..U6_t1 (old build) + U1_t2, U2_t2, U3_t2.
  U4_t2/U5_t2/U6_t2 never fired. masters/: only the F-9-failed
  E2_hold-on_16x9.mp4 (a33c7681…) — NEVER deliver. No flag.

## QC — t2 takes landed before this session

- **U1_t2 — PASS.** ASR (work/asr_u1_t2.json) verbatim, all 3
  lines. Sheet (work/qc_u1_t2/sheet.jpg) eye-checked: couple's
  hands slap onto the Courier's palm, June's fingers on the
  ring; board BLANK throughout; brass key on hook; Rosa (red
  dress) + Bruno (bald) entering the door; Fruit Couple
  pointing at the board. No UNC chest in frame → no wordmark
  surface. (Predecessor's PASS confirmed independently.)
- **U2_t2 — PASS.** ASR (work/asr/U2_t2.json) verbatim, all 4
  lines (trailing "my..." = 10.0s edge artifact only). Sheet
  (work/qc/U2_t2/sheet.jpg) eye-checked: June loaded (bouquet
  in elbow, handbag on wrist), Courier's open palm + counting
  hands, Laura in GREEN WORK SHIRT chalking the couples list
  at the wall's edge (her scripted job), Fruit Couple clamped
  on their shared bouquet grinning. Notes: (a) Laura's list
  board carries chalk names — that IS the scripted staging
  (she chalks the day's list); the verdict board itself
  carries no finished writing. (b) Peach renders doll-like in
  U2 frames vs fruit-headed in U1/U3 — generator variance,
  staging beats all present. No UNC chest in frame.
- **U3_t2 — PASS.** ASR (work/asr/U3_t2.json) verbatim, both
  lines. Sheet (work/qc/U3_t2/sheet.jpg) eye-checked: dropped
  bouquet on the ground, queue holding proofs (ladder, fish
  tank, frog with ring box), Fruit Couple clamped on shared
  bouquet, closing close-ups on June's bare fingers / the
  thumb-lock demo. No UNC chest in frame.

## SR1 chain state
work/frames/U1_t2_last.png, U2_t2_last.png, U3_t2_last.png all
extracted by predecessor → U4_t2 can fire with img1 =
U3_t2_last.png per REPAIR_CALLS.md.

## Assembly plan (from work/build_master.sh, t1 build)
Segments: scale/crop 1152x768→1280x720, 240f each; chalk
inserts cut into U1 (ins_u1), U5 (ins_u5), U6 (ins_u6) —
windows MUST be re-measured against t2 ASR at assembly;
joined.mp4 verified = 1440f before encode; bell overlay
(work/gfx/bell/, 1440 frames) + drawtext bug "~ WuBu ~"
0xFFCF3F bottom-right; loudness fixed gain to −20 dBFS
median + limiter; CRF 18 + CRF-23 differential proof.
FRESH master name: masters/E2_hold-on_REPAIR.mp4.

## Calls spent this session: 1 / 8 (U4_t2 first pass)

## U4_t2 — FIRED + QC PASS (this session)
Landed 1152x768/24fps/240f/10.000s exact. ASR verbatim-grade:
all 3 lines land ("write us married" heard as "right as
married"; Courier line lands without its "Rooms empty?" echo
prefix — content complete). Sheet eye-check: June practising
the thumb-lock at the wall, jaw set; two bags OUTSIDE the door;
Eli picks up both and carries them back inside; ROOMS sign
legible; Watcher (flat cap, canvas apron — plain, no text, no
wordmark surface) in close-up. Notes: fruit couple not in the
sampled frames; the to-camera beat reads on the Watcher's
close-up. work/frames/U4_t2_last.png extracted → SR1 chain
ready for U5.

## U5_t2 first pass — QC FAIL (rejected, kept as takes/U5_t2_rej1.mp4)
ASR verbatim (both lines). BUT the picture fails the
non-negotiable beat: dense sampling (14 frames, 1.0–9.0s,
work/qc/U5_t2_rej1/dense/) shows "the peach and the lime"
rendered as two HUMAN women in peach-pink and lime-green
dresses — not the fruit characters of U1/U2/U3. The bouquet
stays in the lime-dress woman's hand while both point; no
shared-stem hold, no visible slip, no dropped bouquet in
frame. The Fruit Couple's loss does not read — the exact
F-9 merits failure of the old master. Held-hands stack +
Courier's withdrawal (frames 0–0.5s) and the chalk beat
(Watcher + Laura, board unreadable scribbles) were fine.
Disposition: refire ONCE with the fruit characters spelled
out in U1's language and the slip made the visual centre.

## U5 refire — QC PASS (call 3 of 8)
ASR verbatim-grade (both lines; "writes" heard as "rights").
Slip verified on a 0.2s-step strip (work/qc/U5_t2/slip/):
4.6s Lime grips the shared bouquet with BOTH green hands
mid-lunge, Peach reaching in; 4.8s the bouquet lies ON THE
GROUND and both their hands are empty and open; 5.0s+ both
point at each other, bouquet stays down. Lime = proper green
lime-fruit character in tuxedo; Peach in the t2 set's
princess-bride rendering (consistent with U1_t2). Sheet:
hand-stack close-up with locking fingers + withdrawal,
Watcher at the board, Laura handing him the fresh chalk,
board unreadable scribbles. work/frames/U5_t2_last.png
extracted from the refire → SR1 chain ready for U6.

## U6_t2 — QC PASS (call 4 of 8)
ASR verbatim BOTH lines, incl. the L15 quote-lock ("'I believe
it'? Nobody holds your life for you — my couple held.") and
the appointment hanger ("Nobody? Tomorrow's docket reads
thefts."). Sheet: Watcher puts the key in June's hand; Eli
carrying bags INTO the room behind; Fruit Couple small at
mid-ground over their DROPPED bouquet, arguing; Courier's
empty open palm (the empty-hands beat); no cook anywhere.
Notes: board carries faint list-writing (the U2 couples-list
board, small in frame — no finished verdict word); speech
runs to 9.48s so the scripted silent tail is compressed.

## ASSEMBLY DECISIONS (t2 build)
- Insert windows re-measured against t2 ASR (t1 windows do
  NOT carry over — t1/t2 timings differ):
  - U1: PLAIN. No speech gap ≥0.8s exists in U1_t2 (gaps are
    3 and 6 frames); a 20f cutaway would cover the Watcher's
    rule line. ins_u1 not used. (F-9 reads story, not the
    device; the story-critical chalk beats are U5/U6.)
  - U5: ins_u5 (48f) at frames 182–230 — after the verdict
    line "I believe it. Wall writes married." ends (7.56s),
    over the take's chalking tail. Same window the t1 build
    used, re-derived from t2 ASR.
  - U6: ins_u6 trimmed to 23f (f000–f022 → ins_u6_t2/) at
    frames 158–181 — the measured gap between the moral's
    end (6.58s) and the hanger's start (7.56s).
- Build script: work/build_master_t2.sh (adapted from the
  t1 build; fresh master masters/E2_hold-on_REPAIR.mp4;
  CRF-23 proof work/master_crf23_repair.mp4).

## ASSEMBLY DONE — masters/E2_hold-on_REPAIR.mp4
BUILD_OK: segments 240f ×6, joined verified 1440f BEFORE
encode. Master: 29,914,050 B, md5
a6f6102c5c5b93a3239b0e89ef315996. Re-probe: 1280x720,
24fps, exactly 1440 frames read, AAC 48k stereo, faststart.
CRF-23 differential: 16,825,396 B → 1.78x (genuine CRF 18;
SEI string is not a valid gate on this ffmpeg build).
Under 50 MB → no delivery encode needed.

## MASTER GATES
- BLAM (work/blam_master.py): A1 t50 0.0s / t90 0.3s PASS ·
  A2 dead head 0.0s PASS · A3 head −3.4 dB vs median PASS ·
  A4 HF bursts head 2, ×0.91 vs control PASS · V1 head
  motion 0.72× baseline PASS · V2 first bucket 23.1, motion
  from frame 0, no ramp PASS · E1 hands-slam + slip is the
  frame-0 action PASS · E2 bell GFX ring draws on frames
  5–19 PASS. **BLAM: ALL PASS.**
- Dialogue ASR on the master (work/asr/MASTER_REPAIR.json):
  all 16 lines, in order, verbatim-grade. PASS.
- Wordmark full-span sweep (work/qc/master_repair/sweep.jpg,
  every 4s): the post bug "~ WuBu ~" gold bottom-right exact
  in every frame; NO chest-borne wordmark anywhere (the
  Watcher's apron is plain in all appearances); the only text
  surfaces are the intended ones (ROOMS signs, Laura's list,
  unreadable chalk). PASS.
- Joints: joint_gate.py on joined.mp4 — BASE 19.87; seams
  J1 0.12x, J2 0.12x, J3 0.97x, J4 0.04x, J5 0.09x; all five
  strips EYE-PASS (detail in GATE_LOG). JOINTS: ALL PASS.
- GATE_LOG.md appended with the full repair-build gate
  record.
- F-9 VERDICT: **PASS — ALL TWELVE ITEMS** (fresh-context
  cold reader; work/GATE_E_F9_REPAIR_VERDICT.md, 6,704 B,
  verified on disk). Deletion count 1/16; the appointment
  hanger exempt under clarification (i); the Courier's
  settlement reads in her own U5 concession line.
- **DELIVERED 2026-11-17:** E2_DELIVERED.flag raised;
  LEDGER.md delivery addendum appended (delivered-canon
  deltas recorded); repo commit c443ce61. Master
  29,914,050 B < 50 MB → no delivery encode needed.
  JOB COMPLETE.

## Calls spent: 4 / 8. Next: joint eye-pass, GATE_LOG, F-9.
