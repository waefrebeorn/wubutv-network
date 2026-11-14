# MV-6 AUDIO BIBLE — "Sell the Lemons" (measured 2026-11-06)

## Witnesses
- **Tempo: 152.0 BPM — all three witnesses agree exactly** (median inter-beat interval, beat_track global, onset autocorrelation). Beat interval 0.3947s (IQR zero — machine-metronomic clicker track). 579 beats, first beat 0.163s. `work/beat_grid.json`. Downbeat phase index 1 (first downbeat 0.604s) but confidence margin thin (0.045) — treat downbeat phase as provisional; beat times themselves are solid.
- **Words:** `SONG_WORDS.json` — faster-whisper **base**, word timestamps, 376 words (363 usable; 13 degenerate tail stamps at 228.78s discarded). Pass 1 = raw 16k decode. NOTE: small model was fired first but this VM throttles background CPU to ~0.2 core and it could not finish in reasonable wall time; base completed and was cross-checked against the sheet.
- **Coverage gap — RESOLVED 2026-11-06 (volley-coordinator refinement, `work/head30_small_words.json` + `work/refine_head30.py`):** pass 1 (base) heard NOTHING before 30.0s, and the stage-1 [inferred] times (clicks to 14.5s, intro lines at 14.5–20.7) were **WRONG**. A faster-whisper **small** pass over the loudnormed 0–30s head heard the full lyric sequence (pass A unprompted: 39 words / 16 lyric hits; pass B prompted: 46 / 19), and a **tiny** unprompted pass independently reproduced the same segmentation (tiny mishears "Making head" = "Bacon head"). Adjudicated result: **singing starts at 2.72s** — intro hook line 2.72–5.32, "Sell the lemons" phrases at 6.88–8.34 / 9.92–11.60 / 15.70–18.00, Verse 1 runs **19.86–44.2** (L4 "Click" @28.94 dovetails with base's 30.00 tail catch). Remaining uncertainty: a possible 4th smeared hook echo 18.0–20.2 (small B only) and the wordless 11.6–15.7 gap. Method note: base was simply deaf at this level; small is the head witness of record. Environment note: system python3 has faster-whisper but no soundfile, and its PyAV cannot decode paths — load wav via stdlib `wave` → numpy array (pattern in work/refine_head30.py / work/qc_batch.py).
- Energy map: `work/energy_sections.json` (RMS per 0.5s) corroborates section boundaries (quiet verses, loud choruses, gaps at ~96.5–98.5, ~121–126 partially, 169–175 swell, fade from ~227.5).

## Performed section map (performed song BEATS the sheet)
| Section | Time | Note |
|---|---|---|
| Intro | 0.0–19.9 | Clicks only 0–2.7; hook line 2.72–5.32; "Sell the lemons" ×3 heard (6.88 / 9.92 / 15.70) — RE-MEASURED by small+tiny (see coverage note); stage-1 inferred times were wrong |
| Verse 1 | 19.9–44.2 | L1 @19.86, L4 "Click" @28.94 (small) dovetailing base's 30.00; L8 ends 44.2 |
| Chorus 1 | 44.2–73.3 | Sheet 8 lines land 45.0–67.5; performed tail adds echo repeats ("sell the lemons / never gonna stop" ×2) 67.5–73.3 — the chorus does NOT end where the sheet ends |
| Verse 2 | 73.3–98.6 | Joe line measured 82.6–86.0 |
| Chorus 2 | 98.6–121.0 | Same shape as C1, ends cleaner (~121.0) |
| Bridge | 121.0–145.2 | Chant ×2 (121.0–126.8); "Automate the line" 126.8–129.9; "dancing" line 129.9–133.0; "Sell the lemons…" ×4 sustained 133.0–145.2 |
| Verse 3 | 145.9–170.5 | 0.7s breath before it (145.2–145.9) |
| Final Chorus | 170.5–212.2 | Swell/pickup 170.5–173.4 (no words heard); mantra layers thin out after ~196.6 — long sustained "sell the lemons / never gonna stop" phrases to 212.2 |
| Outro | 212.2–228.8 | Clicks return ~212–218.5 (one ASR fragment "click upgrade sale" 212.1); "Bacon head…" + "Sell the lemons." ×3 at 218.5–223.1 / 224.7–226.6 / 226.6–228.8; fade from ~227.5 |

## Mishear traps (normalize before any matching)
- "Bacon hits / bacon hits" = **"Bacon head"** (every chorus; ASR never once hears "head" in the hook)
- "sale" = **"sell"** in chant/chorus tails ("click upgrade sale")
- "Lemon deep oak" = "Lemon Depot"; "Check back on" = "Jetpack on"; "g-gree" = "jig"; "birth" = "Rebirth"; "touchmull" = "touch"; "To play a stack" = "Multipliers stack"; "Boy, portal" = "Void portal"; "sees" = "saves"; "World to come" = "World 2 comes"; "dejected" = "deep"; "dreams" = "trees"
- Clicks in intro/outro decode as stray words — ignore non-sheet words under the click bed.
- Degenerate stamps: all words stamped exactly 228.78 with end==start are artifacts — discard.

## Vocal ownership
Single vocalist throughout (one Suno voice) = **Bacon Head (S1) sings everything**. Joe has no vocal presence anywhere. No speaker ambiguity in this track.
