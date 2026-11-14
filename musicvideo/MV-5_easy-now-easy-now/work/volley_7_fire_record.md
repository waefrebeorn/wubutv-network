# MV-5 Volley 7 — fire record (2026-11-05 ~07:47 EST)

Fired 6/6 (cap). All status ok. Vehicles written before firing: S13 fresh-staging t3
(mv5_s13_fresh_t3_vehicle.txt — SECOND reroll of the fresh vehicle, one variable:
WINDOW REBALANCE to the model's demonstrated pace — L51 2.0s, L50/L52 1.2s+ each),
S16 fresh-staging t3 (mv5_s16_fresh_t3_vehicle.txt — SECOND reroll of the fresh
vehicle, one variable: HOLD CAP — each "now" short/clipped, mouth closes at window
end; pause structure + turns kept from t2), S19 t3 (mv5_s19_t3_vehicle.txt — SECOND
reroll, one variable: RESTRUCTURE — head L74+L75 compressed to 0.0–2.0s, each tail
line its own 1.2s+ window, 2.7–3.3 listening beat dropped), S21 t2
(mv5_s21_t2_vehicle.txt — FIRST reroll, one variable: TAIL PACING + REQUIRED WORDS —
head brisk ~1.0s/line, L87/L88/L89 named, lean-back only after the last word),
S22 t2 (mv5_s22_t2_vehicle.txt — FIRST reroll, one variable: CLIPPED ATTACKS —
three short "No"s under 0.5s each, mouth closed between, all inside 0.0–1.7s),
S24 t1 (mv5_s24_vehicle.txt — NEW scene, modelled on the S23 t1 KEEP vehicle;
refrains short/clipped per the S16 hold lesson).
Take numbering resolved from TAKE_HISTORY.md (max existing + 1): S13/S16 fresh
vehicles go to t5, S19 to t3, S21/S22 to t2, S24 to t1.

| Scene | Requested | Returned | File | md5 | Generation record |
|---|---|---|---|---|---|
| S13 t5 (fresh-staging t3) | 10s | 10.000s | takes/mv5_s13_t5.mp4 | d30276b8d331ba90804854effa4f6c38 | takes/media-generation-mv5-s13-t5-1793882762.json |
| S16 t5 (fresh-staging t3) | 10s | 10.000s | takes/mv5_s16_t5.mp4 | b2aca41fc66f639d219e79e1065a9ce3 | takes/media-generation-mv5-s16-t5-1793882762.json |
| S19 t3 | 7s | 7.000s | takes/mv5_s19_t3.mp4 | 07a4fd6b58dbcae61f8dd5592a34171b | takes/media-generation-mv5-s19-t3-1793882762.json |
| S21 t2 | 10s | 10.000s | takes/mv5_s21_t2.mp4 | 5e669aa10e474237e96b3547fc70b49b | takes/media-generation-mv5-s21-t2-1793882762.json |
| S22 t2 | 5s | 5.000s | takes/mv5_s22_t2.mp4 | 4422acfcbf01ee5a1769c5c093436596 | takes/media-generation-mv5-s22-t2-1793882762.json |
| S24 t1 | 7s | 7.000s | takes/mv5_s24_t1.mp4 | eda851c484e4a4d84ad8d4b88b55e74c | takes/media-generation-mv5-s24-t1-1793882762.json |

All 1280x720, 24fps. Every take returned at exactly its requested duration.
Volley 6 was recovered from disk (its agent handoff never reached the parent);
volley 6 QC is complete on disk (1 KEEP S23 / 5 REJECT) — nothing re-fired.

QC: work/qc_v7.py + work/qc_v7/qc_v7_results.json + work/qc_v7.log; confirmations
work/qc_v7_confirm.py + work/qc_v7_confirm.log (unprompted re-decodes + per-0.5s RMS).
See VOLLEY_PROGRESS.md + TAKE_HISTORY.md.
