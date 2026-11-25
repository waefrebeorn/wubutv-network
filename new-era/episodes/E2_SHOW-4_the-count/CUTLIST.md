# CUTLIST — SHOW-4 'THE COUNT', E2 "The Door Counts First"

Master: masters/e2_show4_the-count_16x9.mp4 (see GATE_LOG.md for hashes)

| Unit | Source take | Conform | Frames |
|---|---|---|---|
| U1 | takes/U1_t1.mp4 (1248×704) | head trim 24f (start-on-the-hit), setpts ×1.111111 + atempo 0.9, scale→1280×720 | 240 |
| U2 | takes/U2_t1.mp4 (1280×720) | scale/conform only | 240 |
| U3 | takes/U3_t1.mp4 (1280×720) | scale/conform only | 240 |
| U4 | takes/U4_t1.mp4 (1280×720) | scale/conform only | 240 |
| U5 | takes/U5_t1.mp4 (1248×704) | scale→1280×720 | 240 |
| U6 | takes/U6_t1.mp4 (1280×720) | scale/conform only | 240 |

Assembly (§5.5 order): segments conformed (CRF 12 intermediates,
work/segments/) → concat copy → work/joined.mp4 (probed: exactly 1440f
before the master encode) → JOINT GATE on the joined picture → single
master encode: joined + Split Total layer + Tally layer (work/
render_encode.py, deterministic PIL) + ~ WuBu ~ bug (drawtext, gold,
bottom-right) + loudness pass (measured −21.36 LUFS in / TP +0.55 →
−1.0 dB + limiter 0.84; no fade-in) → libx264 CRF 18, AAC 192k, faststart.
Exactly one assembly pass owned joined.mp4 at a time; the U1 re-trim
(22f→24f, for the BLAM V2 bucket) rebuilt seg_U1 and re-joined BEFORE
any master encode of the final chain.

Joints (all JOINT class, cut on unit boundaries; the U1→U2 joint carries
the §3.1 Split Total straddle — a forest '7' slides into the board chip
across the cut, completing the board's 1006→1007 in U2's hook):
J1 @f240 · J2 @f480 · J3 @f720 · J4 @f960 · J5 @f1200. No dissolves.
