# Volley 11 fire record — S28 refire (take-audit verdict), 2026-11-05 ~15:53–16:21 EST

## Fired (3 videos — 1 refire + 2 authorized rerolls; volley cap 6)
| Take | Vehicle | md5 | Dur | Result file |
|---|---|---|---|---|
| mv5_s28_t2 | mv5_s28_t2_vehicle.txt (GIRL vehicle, singer flip CAT→GIRL) | 5fe5dacfb7226f96f8520d6e0d6d9b23 | 10.000s | takes/media-generation-mv5-s28-t2-0-51ba17f6-49e5-43fe-975c-cbea87100feb.mp4 |
| mv5_s28_t3 | mv5_s28_t3_vehicle.txt (PACING reroll, one variable: brisk 0.0–1.6s window, no held note) | e4a512fa4cad21b07a6700546d225c9b | 5.000s | takes/media-generation-mv5-s28-t3-0-e027ab34-71b1-495e-8f5a-a041cc8ef3b3.mp4 |
| mv5_s28_t4 | mv5_s28_t4_vehicle.txt (FRESH STAGING, 2nd reroll: girl RIDING the bike, glancing to camera, short 3s take, one-breath delivery, no held note on "comes") | f1396175fbf0f89fd9b65743b4e29b26 | 3.000s | takes/media-generation-mv5-s28-t4-0-1284fec1-0b90-47eb-9dc5-59838d782158.mp4 |

## QC summary
- t2: REJECT (PACING). Line sung once (unprompted 0.0–3.38s), ratio 0.47 vs L110b 1.6s. Frame rule PASSES. Singer fixed.
- t3: REJECT (PACING). Line sung once (unprompted 0.0–2.72s), ratio 0.59 vs L110b 1.6s. Pacing variable moved it −20% but still a clear miss on the boundary; no legal per-word placement (onset intervals need 0.26–0.66x warps). Frame rule PASSES. Best S28 picture yet (straw hat, eyes open).
- t4: REJECT (PACING). Line sung once (unprompted 0.0–2.18s), ratio 0.73 GREY, re-measured per the grey rule — unprompted decode confirms 2.18s, app song times confirm the 1.6s line with "Till the morning" bunched and "comes" held; per-word shape still fails (onset intervals 0.36/0.34/0.72 vs song 0.1/0.1/0.9 need 0.28/0.29/1.25x warps; band-edge warp leaves "morning" ~0.44s late). Frame rule PASSES (vocal mean 25.649, run 0). Best S28 picture yet (girl riding, turns to camera, mouth wide open on the line, closes to a smile after). 3s request honored exactly. Pace floor for this line measured at ~2.18s across three axes (3.38→2.72→2.18s). 2nd denied reroll — NO t5. **S28 goes STRUCTURAL** (t3 tail cover + captions on song times, "not a mouth-sung slot"). Generation for MV-5 is CLOSED: 21 KEEP + 1 PARTIAL + 7 STRUCTURAL across 29 slots.
- Prompted-repeat adjudication (both takes): the prompted decode's second "Till the morning comes" is a hallucination in both cases (unprompted hears it once; RMS tail falls to baseline). Same class as S19a t2's zero-duration-word loop.
- Pace floor established: model gives this 4-word line in 2.7–3.4s (t2/t3); t4's fresh riding staging + short 3s take moved it to 2.18s, but the per-word shape still fails — pace floor for this line is ~2.18s. S28 goes STRUCTURAL (t3's closed-mouth tail 3.0–5.0s is a usable reaction/listening shot; captions on song times). No t5.

## Evidence
- work/qc_v11.py + work/qc_v11/qc_v11_results.json + work/qc_v11_confirm.py (t2)
- work/qc_v11_t3.py + work/qc_v11_t3/qc_v11_t3_results.json + work/qc_v11_t3_confirm.py (t3)
- work/qc_v11_t4.py + work/qc_v11_t4/qc_v11_t4_results.json + work/qc_v11_t4_confirm.py (t4)
- work/gemini_takes_verdicts.md (audit verdict that opened this volley)
