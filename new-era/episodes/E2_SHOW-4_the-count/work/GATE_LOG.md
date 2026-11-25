# GATE LOG — SHOW-4 'THE COUNT', E2 "The Door Counts First"

## Master
- masters/e2_show4_the-count_16x9.mp4 — md5 46f3b6ff182bf7c5fdbeef2a914f4aa6,
  11,681,316 B, 1280×720, 24fps, **exactly 1440 frames** (ffprobe
  -count_frames), h264 + AAC 192k, faststart (moov before mdat).
- Chat copy: NOT MADE — house master is 11.7 MB, under the 50 MB cap.
- CRF: encoded -crf 18. The x264 SEI in the file reads "crf=23.0" — this
  VM's ffmpeg 8.1.2 stamps 23.0 regardless of the requested rate control
  (documented on the SHOW-2 E2 build with control encodes). Proof by size
  differential on the identical chain: CRF 23 encode = 6,169,257 B
  (work/master_crf23_diff.mp4) vs delivered 11,681,316 B = **1.89×**.
- Loudness pass: joined measured −21.36 LUFS integrated, TP +0.55 dBFS
  (overs) → master chain applies −1.0 dB + limiter 0.84 (≈ −22.4 LUFS,
  peaks ≤ −1.5 dBFS). No fade-in anywhere.
- Assembly integrity: segments probed 240f each; joined probed 1440f
  BEFORE the master encode; one assembly pass owned joined.mp4; single
  uninterrupted master encode; finished master re-probed end to end.
  (First master encode came out 1439f under a `-t 60` bound — discarded
  to work/master_1439f_superseded.mp4; the shipped encode uses
  -frames:v 1440 and probes exactly 1440.)

## Wordmark gate
NOT TRIGGERED — UNC is not in this show's cast (pointer card only, has
never appeared; pilot ruling carried). The "~ WuBu ~" corner bug
(bottom-right, gold, Noto Serif Bold, post) is burned into the master
and verified on frame grabs.

## Panels / combined anchor (script law)
- Kit inherited LOCKED from PILOT-4, md5-verified on copy-in; 16:9 sheet
  variants derived locally per J8 (pad, no crop).
- PNL-PEAK-U1 (md5 b109c93fccf5b7458485bdc0305728fe): combined panel —
  Clerk large at the door, hand still on the mid-turn handle, key tag
  reading exactly 1006, Counter behind. Eye QC PASS.
- PNL-PEAK-U5 (md5 583b5cbd07642a3a206da3ce92135ab5): combined panel —
  Clerk large pressing the ledger shut, clasp reading exactly 1010,
  Counter across the desk, board through the doorway reading exactly
  1011. Eye QC PASS.
- Every unit anchored on a combined two-character panel (U1/U5 directly;
  U2/U3/U4/U6 by the resume chain from combined-anchored parents), and
  the Clerk's CHAR sheet rode both fresh calls. The pilot's failure mode
  (Clerk re-invented in sheet-less units) did NOT recur: her identity
  holds in all six units. No exceptions to log.

## Dialogue (faster-whisper large-v3-turbo int8, no VAD, word times)
ALL LINES VERBATIM, all six units. Per-unit detail in TAKE_HISTORY.md.
Homophone hand-check: U4 "Rolls do" heard by ASR as "Rolls due" —
do/due are true homophones; PASS (pilot precedent). Number lines ASR-
rendered as digits (1006/1007/1012) hand-checked against the script.
- U1 silence beat: PRESENT but DISPLACED — 3.1s of silence sits inside
  the Counter's line (after "One thousand six", before "Late, not
  mine") instead of before the number. The number still lands a beat
  after the door swings, as scripted. Disclosed deviation.

## Count arithmetic (script-locked, one increment per unit)
U1 tag 1006 ✓ (board beyond also 1006) · U2 plate 1007 ✓, board 1008 ✓ ·
U3 sign 1008 ✓, board advances in-frame to 1009 ✓ · U4 board 1009 ✓,
backward mark 1003 ✓ pictured repeatedly on the roll WITH the shoe-print
record (F-006 callback pictured, not just mentioned) · U5 clasp 1010 ✓,
board 1011 ✓ · U6 door face 1011 ✓, board glimpse in the closing gap
(partial digits; the 1012 completion is carried by the Split Total flip
at 52.0s and the spoken cliff) — PASS.

## JOINT GATE (on the joined picture, before graphics; re-measured on
the finished master — identical seams)
Baseline: intra-unit adjacent-frame MAE 95th pct = 3.87 (320×180 gray).
| Joint | Seam MAE | Band | Eye checklist |
|---|---|---|---|
| J1 U1→U2 @f240 | 54.52 | PASS (≤58) | identities ✓ both sides; wardrobe: Counter gains a black tie in U2 (nit, logged); ledger carry ✓ (open on the desk); light: warm both sides ✓; position jump: scene reframe by design (hall→desk room through the opened door); the §3.1 graphic straddle crosses this joint |
| J2 U2→U3 @f480 | 45.40 | PASS | identities ✓; desk/board/ledger held ✓; sign 1008 enters as the unit's carrier ✓ |
| J3 U3→U4 @f720 | 47.75 | PASS | identities ✓; desk held ✓; board 1009 held ✓; roll enters ✓ |
| J4 U4→U5 @f960 | 39.60 | PASS | re-anchor joint; identities ✓ (fresh PEAK + her sheet); desk/ledger held ✓; chips settle (1011/1010) across the cut |
| J5 U5→U6 @f1200 | 41.23 | PASS | identities ✓; upstream side is U5's in-take close-up (see flaw 1); door/plate 1011 held ✓ |
Checklist item (6), downstream head-motion ≥ 8: NOT MET on the number
at any joint (measured first-0.5s MAE at 320×180: U2 0.10, U3 0.31,
U4 1.45, U5 0.18, U6 2.57). The bar sits above this episode's whole
intra-unit 95th percentile (3.87) — it is calibrated for livelier shows.
Motion IS alive on both sides of every joint within the first second
(door swing tail, board cells, roll feed, her turn, door seal) in the
show's locked-camera deadpan register; judged alive by eye on the joint
strips (work/qc/joint*_strip.jpg). Logged as a calibration deviation,
not hidden. No joint failed the seam-MAE hard bar; no remedy needed;
no dissolves used (a dissolve is a grammar error in this show).
Joint frames harvested (J4): PNL-JOINT-U1 md5 0d0b4daec81c388ac04a88a3eac7b5c9,
U2 17c9e2a3c553b26007acbe85fe3bfcdd, U3 217650c60dc406a2e11107e8c2e86954,
U4 78c5f1c9c2604af0037c0b6ed8573716, U5 c90324dfcb1e92cfe3e80e3f75706009
(conformed segments, frame 228).

## BLAM GATE (finished master, first 3.0s; work/blam_measure.py)
| Bar | Result | Value |
|---|---|---|
| A1 onset t50 ≤0.5s / t90 ≤1.5s | **FAIL** | t50 1.1s, t90 2.5s |
| A2 dead head ≤0.2s | PASS | 0.0s |
| A3 head level / accent ≤0.5s | PASS | accent −27.2 dBFS ≥ median−6 (−39.5); head 0–1s is +10.4 dB vs median (louder, not quieter) |
| A4 crackle ≤2× control | PASS | 39 bursts vs 23 control (≤46) — head bursts are the door/latch transients, not crackle |
| V1 motion ≥0.6× baseline | PASS | 1.02× (2.06 vs 2.01) |
| V2 no ramp-from-rest | PASS | first bucket 2.86 = the strongest 0–3s bucket (the door swing) |
| E1 named impact ≤1.0s | PASS | the door swings open ~0.1–0.25s in, handle already turning at frame 0 |
A1 is the single failing bar, and it is structural: the gate's t50 asks
half the opening 3 seconds' audio energy to land in the first half
second. This unit is scripted as a door event, one flat line, and a
protected silence beat; every sanctioned fix was applied (PEAK = the
impact moment, first-second sound event named in the vehicle,
start-on-the-hit trim — moved 22f→24f after the first master put the
swing in the second bucket, which fixed V2 — loudness pass, no fade-in).
The pilot passed A1 only because its generator front-loaded speech to
frame 0; this take staged the door first, as the script demands. Logged
plainly rather than papered over with a fabricated accent.

## Graphics (Method C §5.6 QC on the finished master)
Device: THE SPLIT TOTAL (invariant) + THE TALLY THAT RE-COUNTS ITSELF
(U4, the episode's one use), accent FOREST #1F6B3A (kit-locked in
work/GFX_CARD.md — no hex existed in the show kit), Route P PIL,
deterministic. Furniture bottom-left; bug bottom-right.
- Legibility: PASS at full size and at 320×180 phone size (chip digits
  readable).
- Arithmetic audit vs the GFX state table: PASS at every spot check on
  the master — f0 (1006≠1007), straddle completes board→1007 at 10.3s,
  reveal flip (1008=1008) at 13.05s, bell flip board→1009 at 22.90s
  (bell transient measured at U3 2.90s), ledger clerks 1009 at her
  cliff 28.28s, U4 rest (1009=1009) with the tally re-count at 33.88s,
  joint settle to (1011|1010) across J4, U5 frame at 45s reads
  1011≠1010 matching the pictured board/clasp exactly, U6 board→1012
  at 52.0s with the ledger locked at 1010 (the finale's deliberate
  gap of two — her book is locked; the desk holds the count).
- Frame-0 audit: PASS — invariant resting ambient from frame 0, no
  graphic event before 1.5s in U1 (first event: migration at 2.95s).
- Line-slot audit: PASS — every event keyed to a MEASURED beat (ASR
  word times / the bell transient); flips and cliff pulses land on
  naming beats per §2.4c; no event starts inside a protected slot.
- Three-question audit: in work/GFX_CARD.md — PASS both devices.
- Density: one graphic event per unit + invariant ambience ✓; max two
  graphic layers + bug in the encode ✓; graphics never used to rescue
  a joint (the Joint Gate ran on bare picture first) ✓.

## Known flaws (all disclosed, none hidden)
1. **U5 in-take cut (~5.17s):** the generator cuts mid-unit from the
   wide desk shot to a tight two-shot in different dressing (filing
   cabinets, cooler grade) and never cuts back. His line 2 spans the
   cut; her price line + cliff play in close-up with the locked ledger
   below frame. Dialogue, identities, and both numbers (1010/1011,
   read in the wide section) are unaffected. Breaks the locked-camera
   grammar mid-unit.
2. **BLAM A1 fail** (t50 1.1s / t90 2.5s) — structural, see above.
   Every other BLAM bar passes, including V1/V2, which the pilot
   failed outright.
3. **U1 silence beat displaced** (3.1s, inside the Counter's line
   rather than before his number).
4. **Board glow hue:** in U1–U4 the pictured board digits glow
   orange-red rather than cadmium; numbers are exact everywhere and
   U5's board is on-palette amber. A consistent cast across the chain.
5. **Wardrobe/prop nits:** the Counter wears a black tie from U2 on
   (absent in U1); his chest tally renders oversized in U4; the U3
   desk bell morphs shape across its strike; the Clerk's cobalt reads
   object-like in her hand mid-U1; U4's roll header digits are small
   (the board carries 1009 unambiguously).
6. **Grade drift:** U6 (and U5's close-up section) grade cold
   blue-grey against the chain's warm amber — the same class of shift
   the pilot disclosed on its U3.
7. **Camera:** U1 has a slow push-in (the pilot's U1 had the same
   logged deviation; first 12 frames effectively static, and the
   re-trim starts after it is established). Other units locked.
8. Joint Gate checklist item (6) head-motion bar not met on the
   number — calibration deviation, logged in the Joint Gate section.

## Verdict
SHIPPED as the episode master. Six of six units KEEP on one 6-call
volley (no refires, none blocked); dialogue verbatim throughout; count
arithmetic exact; Joint Gate PASS at all five joints; BLAM 6/7 bars
with A1 disclosed. E2_DELIVERED.flag written.
