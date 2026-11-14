# MV-5 Volley 2 — fire record (2026-11-05 ~06:25 EST)

Fired 6/6 (cap). All status ok. S08 t2 fired VERBATIM from mv5_s08_t2_vehicle.txt (pre-written);
S06/S07/S09/S10/S11 vehicles written to mv5_sXX_vehicle.txt before firing, from the plan's
scene table + bible + pose cards, fixed prompt order per the Slopcannon skill.

| Scene | Requested | Returned | File | md5 | Generation record |
|---|---|---|---|---|---|
| S08 t2 | 10s | 10.000s | takes/mv5_s08_t2.mp4 | fc07dcacf30e91cdcd98a89b5148760e | takes/media-generation-mv5-s08-t2-1793878245.json |
| S06 t1 | 8s | 10.000s | takes/mv5_s06_t1.mp4 | bc19ed1009cd1324c1135def0f6194ec | takes/media-generation-mv5-s06-t1-1793878248.json |
| S07 t1 | 10s | 10.000s | takes/mv5_s07_t1.mp4 | 3bdd0f48a7999696b27a6c4e1e0da7f2 | takes/media-generation-mv5-s07-t1-1793878246.json |
| S09 t1 | 10s | 10.000s | takes/mv5_s09_t1.mp4 | 37c3ffb0da3982331bbb4ac2547bd991 | takes/media-generation-mv5-s09-t1-1793878249.json |
| S10 t1 | 9s | 10.000s | takes/mv5_s10_t1.mp4 | 89830a0407ad9c8cafff1879e0dbc548 | takes/media-generation-mv5-s10-t1-1793878250.json |
| S11 t1 | 8s | 8.000s | takes/mv5_s11_t1.mp4 | fadaa0993bae406e59a7e682bdd236e3 | takes/media-generation-mv5-s11-t1-1793878246.json |

All 1280x720, 24fps. S06/S10 returned 10s against 8s/9s requests (tool rounds up);
the excess is hold/pose and trims cleanly.

QC: work/qc_v2.py + work/qc_v2/qc_v2_results.json + work/qc_v2.log.
Verdicts: 5 KEEP (S06, S07, S08 t2, S09, S10) / 1 REJECT (S11 t1, DELIVERY —
"Calling mango sweet" never sung). See VOLLEY_PROGRESS.md + TAKE_HISTORY.md.
