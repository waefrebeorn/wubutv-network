# MV-5 Volley 3 — fire record (2026-11-05 ~06:47 EST)

Fired 6/6 (cap). All status ok. S11 t2 fired VERBATIM from mv5_s11_t2_vehicle.txt (pre-written);
S12/S13/S14/S15/S16 vehicles written to mv5_sXX_vehicle.txt before firing, from the plan's
scene table + bible + pose cards, fixed prompt order per the Slopcannon skill.

| Scene | Requested | Returned | File | md5 | Generation record |
|---|---|---|---|---|---|
| S11 t2 | 8s | 8.000s | takes/mv5_s11_t2.mp4 | 6426b5788318bf3ac9db982741e373ae | takes/media-generation-mv5-s11-t2-1793879329.json |
| S12 t1 | 9s | 9.000s | takes/mv5_s12_t1.mp4 | 4202db31b66386a7979143f587f91119 | takes/media-generation-mv5-s12-t1-1793879336.json |
| S13 t1 | 10s | 10.000s | takes/mv5_s13_t1.mp4 | deeac574cd58014601a9b21116b2d8bf | takes/media-generation-mv5-s13-t1-1793879333.json |
| S14 t1 | 5s | 5.000s | takes/mv5_s14_t1.mp4 | 8742e6e8991763e5ac29e502db54b2f2 | takes/media-generation-mv5-s14-t1-1793879321.json |
| S15 t1 | 5s | 5.000s | takes/mv5_s15_t1.mp4 | 72332ff6ccc1839d6c4d5db629a0562a | takes/media-generation-mv5-s15-t1-1793879321.json |
| S16 t1 | 10s | 10.000s | takes/mv5_s16_t1.mp4 | c47a0ed1c0bbdcbb5f3607e93062df70 | takes/media-generation-mv5-s16-t1-1793879330.json |

All 1280x720, 24fps. Every take returned at exactly its requested duration.

QC: work/qc_v3.py + work/qc_v3/qc_v3_results.json + work/qc_v3.log; confirmations
work/qc_v3_confirm.py + work/qc_v3_confirm.log (unprompted re-decodes + per-0.5s RMS).
Verdicts: 2 KEEP (S12, S15) / 4 REJECT (S11 t2, S13, S14, S16 — all DELIVERY).
See VOLLEY_PROGRESS.md + TAKE_HISTORY.md.
