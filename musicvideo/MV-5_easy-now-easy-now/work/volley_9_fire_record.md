# MV-5 Volley 9 — fire record (2026-11-05 ~08:19 EST)

Fired 6/6 (cap, FINAL volley). All status ok. Vehicles written before firing: S24 t2
(mv5_s24_t2_vehicle.txt — FIRST reroll, one variable: S23 WINDOW SPACING — R1 0–1.0,
listen 1.0–2.3, R2 2.3–3.4, listen 3.4–4.5, R3 4.5–5.8, listen 5.8–7.0; clipped
"now" language kept), S25 t1 (mv5_s25_vehicle.txt — NEW scene), S26 t1
(mv5_s26_vehicle.txt — NEW scene), S27 t1 (mv5_s27_vehicle.txt — NEW scene, visual
peak held note), S28 t1 (mv5_s28_vehicle.txt — NEW scene, CAT final line), S13 t7
(mv5_s13_t7_vehicle.txt — THIRD staging's 2nd attempt, on the t5 base 33/34 proven;
one variable: "Like" named as a required word with its own beat, S11-"time" fix
pattern; NO staging change — t5 vehicle otherwise verbatim, t6 step-forward split
window reverted; if t7 fails, S13 goes structural, no t8).
Take numbering resolved from TAKE_HISTORY.md (max existing + 1): S24 to t2, S25–S28
to t1, S13 to t7.

| Scene | Requested | Returned | File | md5 | Generation record |
|---|---|---|---|---|---|
| S24 t2 (first reroll) | 7s | 7.000s | takes/mv5_s24_t2.mp4 | f138d39f8dbcb6afccea817ef1f6084e | takes/media-generation-mv5-s24-t2-0-65d210e1-83d9-45c5-93e9-27d218b4570c.mp4 |
| S25 t1 | 6s | 6.000s | takes/mv5_s25_t1.mp4 | 008a1934e8a2340b1441e4ddfdec9550 | takes/media-generation-mv5-s25-t1-0-d58b9fd2-8cd0-4292-a0e9-a838b0027189.mp4 |
| S26 t1 | 8s | 8.000s | takes/mv5_s26_t1.mp4 | 597218f1dc8282ebefc2fc2253edb4d0 | takes/media-generation-mv5-s26-t1-0-4246a09f-bdde-41c0-8edc-6c8247a3fd7a.mp4 |
| S27 t1 | 6s | 6.000s | takes/mv5_s27_t1.mp4 | fdc6c6c02e1bf36178294117a4dc2b5b | takes/media-generation-mv5-s27-t1-0-0b3adff6-c0ba-4afc-8783-445d85f18861.mp4 |
| S28 t1 | 5s | 5.000s | takes/mv5_s28_t1.mp4 | c4030af7f9ab17548d137cd7cbcac652 | takes/media-generation-mv5-s28-t1-0-c29e7c85-48d4-4ea1-8e12-69ab30ca097a.mp4 |
| S13 t7 (third staging t2) | 10s | 10.000s | takes/mv5_s13_t7.mp4 | 384e1f6ca8d4700f00a189c20faaa6b9 | takes/media-generation-mv5-s13-t7-0-b5a60761-3a34-4722-8d20-8a853524c735.mp4 |

All 1280x720, 24fps. Every take returned at exactly its requested duration.

QC: work/qc_v9.py + work/qc_v9/qc_v9_results.json + work/qc_v9.log; confirmations
work/qc_v9_confirm.py + work/qc_v9_confirm.log (unprompted re-decodes + per-0.5s RMS).
See VOLLEY_PROGRESS.md + TAKE_HISTORY.md.
