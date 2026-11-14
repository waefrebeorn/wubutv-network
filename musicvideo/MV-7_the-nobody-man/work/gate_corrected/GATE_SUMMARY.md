# MV-7 CORRECTED GATE — SUMMARY (2026-11-06 night EST)

Master under test: `masters/mv7_im_the_nobody_man_16x9_corrected.mp4`
md5 d74de9cda8dc084c21dd8147ca668901 · 61,946,109 B · 4493f · 1280×720 24fps

| Check | Result |
|---|---|
| Audio identity vs track.mp3 | PASS — lag 0 samples; corr at lag 0 = 0.998776 |
| Mouth offset median | 0.146s → **0.000s** (target ≤0.08s) |
| Mouth offset max | 1.000s → **0.083s** (2f) |
| Onsets >0.15s late | 29/58 → **0/58** |
| Closed onsets | **0** |
| Hooks | **25/25** |
| Worsened scenes | **0** |
| Judder | PASS — no near-dup runs ≥24f in vocal material |
| Motion | PASS — vocal mean diff 2.939 (fail <0.5) |
| Audio codec | AAC 48kHz stereo ✓ |
| x264 SEI | crf=18.0 ✓ |
| Frames | 4493 ✓ · faststart ✓ |

After-lag distribution (58 scored onsets): 0f ×36, +1f ×15, +2f ×7.
Per-onset before/after: `lag_after.csv`; strips: `strips/strip_<label>.png`;
frames: `frames/`. Before-table: `../../correction/lag_final.csv`.

50MB copy: `masters/mv7_im_the_nobody_man_16x9_corrected_50mb.mp4`
md5 04953a7cada34eef5c88d9c5b1ed4654 · 38,613,113 B · 4493f ·
audio streamhash fd13495398dcb1e810f12acd2de38efa = house master (copied).

**VERDICT: PASS**
