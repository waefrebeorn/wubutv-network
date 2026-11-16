# MV-7 "I'm The Nobody Man" — GATE (final master)

Master: `masters/mv7_im_the_nobody_man_16x9.mp4`
md5 46ba607394488f1c14fef7ab3a3f6b51 · 62,331,020 B · 4493f · 187.208s ·
1280×720 · 24fps · h264 · SEI crf=18.0 · AAC 48 kHz stereo · faststart (moov at 36).

## (a) Audio identity — PASS
Decoded master audio vs track.mp3 (16 kHz mono, full 187.200s):
best lag 0 samples (0.0000s) on the 30–60s slice; correlation at lag 0 = 0.998776;
mean |diff| 0.004916. The song is the sole master audio, untouched in timing.

## (b) Mouth state at onsets — PASS (58/58, hooks 25/25)
Read from the MASTER at every sung-picture phrase onset (onsets.json):
onset frame + 0.25s frame, contact sheets sheet_01–08.png.
Scores: O 28 · T 29 (transitional-open: closed at the exact onset frame,
open at +0.25s) · o 1 · C 0.
Hooks: O 11 · T 13 · o 1 · C 0 — 25/25 pass.
Lines: 58/58 pass. Zero closed onsets.
Weakest read: I-occ1 (o) — first frame of the video; mouth only slightly
parted at +0.25s. All other onsets O or T.
Covered (no mouth expected, not scored): C2.4, FC.4 (montage covers),
B.1–B.6 (bridge montage plates).
Frame-index correction: 20 of 58 onsets were first read ±1–2 frames off
(rounding drift in cumulative segment frames); the 14 affected onsets
were re-read at their TRUE first frames (corr_01–02.png). One score
changed: FC.5 T → O (its true first frame already shows the mouth
parted; the sheet frame had been the FC.4-cover tail).
Systematic ~0.25s mouth lag: most onsets read closed on the exact onset
frame and open at +0.25s. This is the takes' own mouth-audio lag
(phrases close between lines, then open on the word) — the mouth IS
opening on every word, inside 6 frames. Disclosed, not a failure.

## (c) Judder — PASS
Per-frame mean abs diff (160×90 gray, frame_diffs.npy):
vocal mean diff 2.953 (fail < 0.5). No near-dup run ≥24f during vocal
(longest: 20f at f2688–2707 inside the C2.4 montage cover; 19f at
f3163–3181 inside the S19 bridge plate; 17f at f239–255, intro chant
tail — all < 24f, two in non-vocal cover material).
Top diff spikes are cut points on segment boundaries, except a sustained
high-diff run f3075–f3095 (t 128.1–129.0s, diff ~34–40) inside the
S18 bridge plate: eyeballed frames f3052/f3085 — the plate take itself
cuts corkboard-of-receipts → glowing abstract dashboard. In-plate
montage motion, not an assembly step. No in-phrase setpts steps
(segments carry one smooth setpts factor each by construction).

## (d) Motion — PASS
Vocal mean diff 2.953; no frozen takes; Era A→B→C camera drift
(slow push-in) is the designed look, trimmed/cropped at assembly.

## Warp extremes (cutlist.json, all inside caps)
Slowest: S08-C1.7 0.5487x (1.82x slow) · S24-P2 0.5559x (1.80x slow) ·
S01a-occ3 0.6159x. Fastest: S05b-PC1.2 2.5333x (the known fastest squeeze) ·
S05a-PC1.1 1.9919x · S13-PC2.2 1.9151x. No segment past the 0.5x slow floor.
