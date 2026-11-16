# MV-5 Volley 4 — fire record (2026-11-05 ~07:00 EST)

Fired 6/6 (cap). All status ok. S11 fresh staging written to mv5_s11_fresh_vehicle.txt
(NEW vehicle from scratch — P-WALK arrival into the vendor counter + a distinct
turn-to-camera mango beat for "time with our feet"; the retired t1/t2 vehicles were
NOT reused or edited). S13 t2 / S14 t2 / S16 t2 reroll vehicles written to
mv5_sXX_t2_vehicle.txt before firing, one named axis each (DELIVERY). S17/S18 vehicles
written to mv5_sXX_vehicle.txt before firing, from the plan's scene table + bible +
pose cards, fixed prompt order per the Slopcannon skill.

| Scene | Requested | Returned | File | md5 | Generation record |
|---|---|---|---|---|---|
| S11 t3 (FRESH STAGING) | 8s | 8.000s | takes/mv5_s11_t3.mp4 | 465e03d161c578b6f3bb6945eae00e2b | takes/media-generation-mv5-s11-t3-1793879891.json |
| S13 t2 | 10s | 10.000s | takes/mv5_s13_t2.mp4 | 951a9afb3aac9c779940934a9d51c1db | takes/media-generation-mv5-s13-t2-1793879899.json |
| S14 t2 | 5s | 5.000s | takes/mv5_s14_t2.mp4 | f52858ba42b724e321c1991a7a2d6d7c | takes/media-generation-mv5-s14-t2-1793879885.json |
| S16 t2 | 10s | 10.000s | takes/mv5_s16_t2.mp4 | fb876049fe1250a503eb6dbeb317e167 | takes/media-generation-mv5-s16-t2-1793879894.json |
| S17 t1 | 10s | 10.000s | takes/mv5_s17_t1.mp4 | c239ec5925bc66710e080e9b62bb1ff1 | takes/media-generation-mv5-s17-t1-1793879895.json |
| S18 t1 | 9s | 9.000s | takes/mv5_s18_t1.mp4 | 5747e5443e07633313dae30c5486a58f | takes/media-generation-mv5-s18-t1-1793879890.json |

All 1280x720, 24fps. Every take returned at exactly its requested duration.
Note: mv5_s11_t3.mp4 is named t3 ONLY by the file convention — it is the fresh
staging's first take, NOT a third reroll of the retired S11 vehicle.

QC: work/qc_v4.py + work/qc_v4/qc_v4_results.json + work/qc_v4.log; confirmations
work/qc_v4_confirm.py + work/qc_v4_confirm.log (unprompted re-decodes + per-0.5s RMS).
Verdicts: 2 KEEP (S17 grey rescue, S18 cutaway) / 4 REJECT (S11 t3, S13 t2, S14 t2,
S16 t2 — all DELIVERY). S13/S14/S16 retire to fresh staging after two denied rerolls;
S11's fresh staging has had ONE denied attempt.
See VOLLEY_PROGRESS.md + TAKE_HISTORY.md.
