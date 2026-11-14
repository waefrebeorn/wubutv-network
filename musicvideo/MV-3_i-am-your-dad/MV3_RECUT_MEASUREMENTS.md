# MV-3 re-cut — stage 1 measurements (all takes, word-level)

Date: 2026-11-04 (re-cut build). Method: each take's audio extracted to a
PER-TAKE wav (ffmpeg, mono 16k), transcribed sequentially with faster-whisper
base (~/workspace/fw-venv), word_timestamps=True, language=en. No shared temp
wav. Full-clip Whisper drops later quiet bursts on held takes (known class);
those takes got a slice re-transcription (offset added back) — see notes.
Song authority: SONG_WORDS.json + LYRIC_TIMELINE.md line spans (performed
words, not the lyric sheet). "game"/"dogs"/"see" = known song-side mishears.

## Diagnostic cross-check (7 takes already measured in MV3_TIMING_DIAGNOSTIC.md)

All 7 reproduced EXACTLY (first→last word spans): S01 0.00–4.54, S02
0.00–6.94, S07 0.00–8.96, S10 0.00–7.70, S19 0.00–8.12, S29 0.00–8.34, S39
0.00–3.14. No re-measurement of those 7 was needed beyond confirmation.

## Warp rule used (documented choice)

ratio = song line span / take line span (first word start → last word end).
Placement: take trimmed at its first word, placed at the segment start, so
the take first word lands on the song first word. End residual = take span
× w − song span (negative = mouth ends early, positive = late).

- usable [0.80, 1.25] → w = ratio (full alignment; endpoints land exactly).
- grey-fast (1.25, 1.60] → w = 1.25 (warp factor capped at the band edge).
- grey-slow [0.60, 0.80) → w = 0.80 (warp factor capped at the band edge).
- outside [0.60, 1.60] → COVER (no mouth claim).

Alternative considered and NOT used: the old assembly's grey formula
w = ratio/edge (which pins the RESIDUAL ratio at the band edge, e.g. S01
w = 1.088, mouth 1.24s early). The band-edge factor cap lands words closer
(S01: 0.50s early instead of 1.24s) while keeping every warp factor inside
the usable band. Parent may overrule; the cutlist records every w.

## Per-scene table

| Scene | Take | Prompted line(s) | Take words (span) | Song span | Ratio | Warp | Verdict |
|---|---|---|---|---|---|---|---|
| S01 | s01_t2 | L01 "Listen, all of you" | 4 words, 0.00–4.54 | 2.82–9.00 (6.18s) | 1.361 | 1.25 | grey-rescue; end −0.50s. PHRASING GAP: take pauses 0.94s after "listen", song holds "of" 2.46s — mid-line "all" starts +1.42s late under any whole-clip warp. |
| S02 | s02_t2 | L02 "You already know, I am your dad" | 7 words, 0.00–6.94 | 9.32–18.34 (9.02s) | 1.300 | 1.25 | grey-rescue; end −0.34s. Per-word max 1.32s (take rushes the tail vs song's held line). |
| S03 | s03_t1 | (instrumental, no vocal) | 1 ambient word 7.18–8.58 | — | — | 1.382 slow-mo | cutaway; no words, window filled as before. |
| S04 | s04_t1 | L03 (structural video cover) | 11 words, 0.00–7.58 | 32.16–35.72 | — | 1.0 partial 0–4.40s | structural cover; master audio carries the line. |
| S05 | s05_t1 | L04 (structural video cover) | 10 words, 0.00–6.92 | 36.56–39.74 | — | 1.0 partial 0–3.50s | structural cover. |
| S06 | s06_t1 | L05+L06 | 23 words, 0.00–8.10 | 40.06–47.60 (7.54s) | 0.931 | 0.9309 | usable; per-word max 0.27s — cleanest sync in the cut. |
| S07 | s07_t1 | L07+L08 | 20 words, 0.00–8.96 | 48.12–54.38 (6.26s) | 0.699 | 0.80 | grey-rescue; end +0.91s late — final word "tonight" lands late and is cut 0.15s by the scene boundary; master audio carries it. |
| S08 | s08_t1 | L09 | 21 words, 0.00–7.20 | 55.14–62.20 (7.06s) | 0.981 | 0.9806 | usable; per-word max 0.31s. |
| S09 | s09_t1 | L10 "dad x2 say-it" | 12 words, 0.00–7.58 | 62.64–67.90 (5.26s) | 0.694 | 0.80 | grey-rescue; end +0.80s late; per-word max 1.17s (burst gaps differ from song's). |
| S10 | s10_t1 | L11 | 14 words, 0.00–7.70 | 68.36–75.48 (7.12s) | 0.925 | 0.9247 | usable; per-word max 0.99s driven by Whisper's long first-word stamp (take "i" 0–1.22 vs song 0–0.14); words 4+ within 0.32s. |
| S11 | s11_t2 | L12 | 16 words, 0.00–8.48 | 76.28–82.90 (6.62s) | 0.781 | 0.80 | grey-rescue; end +0.16s. Song word count garbled (11 vs take 16) — span-level only. |
| S12 | s12_t2 | L13 "dad x2" | 8 words, 0.00–6.80 (2 bursts) | 82.92–87.50 (4.58s) | 0.674 | 0.80 | grey-rescue; end +0.86s late (lands in the breath gap before S13, before the cut). |
| S13 | s13_t1 | L14+L15 | 18 words, 0.00–7.82 | 90.66–99.76 (9.10s) | 1.164 | 1.1637 | usable; song count 16 vs take 18 (garble) — span-level only. Line ends 0.08s past the segment cut (breath joint). |
| S14 | s14_t1 | L16 | 13 words, 0.00–7.52 | 99.68–108.92 (9.24s) | 1.229 | 1.2287 | usable; song count 27 vs take 13 (middle garble "sit in the beast") — span-level only. |
| S15 | s15_t1 | L17 | 22 words, 0.72–7.82 | 108.92–115.90 (6.98s) | 0.983 | 0.9831 | usable; trim 0.72s lead-in; per-word max 0.35s. |
| S16 | s16_t1 | L18 | 18 words, 0.00–8.40 | 116.14–123.40 (7.26s) | 0.864 | 0.8643 | usable; per-word max 0.66s. |
| S17 | s17_t1 | L19 | 12 words, 0.88–6.10 | 123.74–128.90 (5.16s) | 0.989 | 0.9885 | usable; trim 0.88s lead-in; per-word max 0.48s. |
| S18 | s18_t2 | L20 | 14 words, 0.00–7.70 | 129.46–135.80 (6.34s) | 0.823 | 0.8234 | usable; song count 13 vs take 14 — span-level only. |
| S19 | s19_t1 | L21 | 16 words, 0.00–8.12 | 136.52–143.80 (7.28s) | 0.897 | 0.8966 | usable; song count 20 vs take 16 (mantra pile-up) — span-level only. |
| S20 | s20_t1 | L22 | 11 words, 0.00–6.96 | 143.76–149.10 (5.34s) | 0.767 | 0.80 | grey-rescue; end +0.23s; per-word max 1.00s (phrasing). |
| S21 | s21_t2 | L23 (structural) | 8 words, 0.00–8.00 (x2) | 150.30–159.50 | — | 1.0 | structural cover; 10f tail-loop. |
| S22 | s22_t1 | L24 "dad x2" | 8 words, 0.00–6.40 (burst 2 slice-recovered) | 160.70–166.50 (5.80s) | 0.906 | 0.9063 | usable; song count 6 vs take 8 (song merges the two "dad"s) — span-level only. |
| S23 | s23_t2 | L25 | 18 words, 0.00–8.78 | 168.76–182.12 (13.36s) | 1.522 | 1.25 | grey-rescue; end −2.39s (43f tail-loop cover). Song count 17 vs take 18 — span-level only. |
| S24 | s24_t2 | L26 (structural) | 12 words, 0.00–7.56 (bursts 2–3 slice-recovered) | 183.06–191.94 | — | 1.0 | structural cover; 53f tail-loop. |
| S25 | s25_t1+s25_t2 | L27 (structural) | t1 0.00–6.52, t2 0.00–6.96 (burst 2 slice-recovered) | 195.24–214.90 | — | 1.0 | structural cover; 28f tail-loop. |
| S26 | s26_t1 | L28 | 12 words, 0.00–6.54 | 215.40–220.64 (5.24s) | 0.801 | 0.8012 | usable (knife-edge 0.801); song count 11 vs take 12 — span-level only. |
| S27 | s27_t1 | L29 | 24 words, 0.00–8.16 | 220.64–230.00 (9.36s) | 1.147 | 1.1471 | usable by span, PHRASING GAP: take lingers on the first phrase then rushes the tail — mid-line hump +1.14–1.40s on words 5–13; endpoints land. No warp within caps fixes the hump (intervals needed 0.48–2.78x). |
| S28 | s28_t3 | L30+L31 | 34 words, 0.00–9.30 | 230.52–245.10 (14.58s) | 1.568 | 1.25 | grey-rescue; end −2.95s (50f tail-loop cover). Song count 36 vs take 34 — span-level only. |
| S29 | s29_t1 | L32 | 12 words, 0.00–8.34 | 245.10–250.70 (5.60s) | 0.671 | 0.80 | grey-rescue; end +1.07s late; per-word max 1.33s; final words land past the scene cut (segment 5.94s < warped span 6.67s) — master audio carries them. |
| S30 | s30_t3 | L33 (structural) | 11 words, 0.00–7.28 | 251.04–258.32 | — | 1.0 | structural cover (character FIXED, middle phrase missing — video only). |
| S31 | s31_t1 | L34 slice a (mantra) | 12 words, 0.00–6.32 (x3 bursts) | segment 258.32–268.50 (10.18s) | 1.611 | 1.25 | MANTRA-SLICE COVER: ratio 0.011 over the grey ceiling (history span 6.58 would give 1.547, inside grey) — warp factor itself is in-band; bursts paced to segment, individual song repeats NOT matched (song ~0.74s/repeat vs take ~2.2s/burst). |
| S32 | s32_t1 | L34 slice b (mantra) | 12 words, 0.00–7.82 (bursts 2–3 slice-recovered) | segment 268.50–278.50 (10.00s) | 1.279 | 1.25 | MANTRA-SLICE COVER: same disclosure as S31 (span ratio grey, repeats not matched). |
| S33 | s33_t1 | L34 slice c (mantra) | 12 words, 0.00–7.36 (bursts 2–3 slice-recovered) | segment 278.50–287.80 (9.30s) | 1.264 | 1.25 | MANTRA-SLICE COVER: same disclosure as S31. |
| S34 | s34_t1 | L35 "dad, dad, just a low voice" | 12 words, 0.00–7.16 | 287.80–296.00 (8.20s) | 1.145 | 1.1453 | usable by span, PHRASING GAP: song pauses 2.42s before the second "i" and sings "just" at 5.06s; take stretches "i" and sings "just" at 5.32s — tail words land +1.03–1.70s late. Intervals needed 0.27–4.56x: no warp within caps fixes this. |
| S35 | s35_t1+s35_t2 | L36 (structural) | t1 0.00–6.24, t2 0.00–6.28 (burst 2 slice-recovered) | 296.70–308.56 | — | 1.0 | structural cover (t1 full + t2 partial 0–4.18s, as before). |
| S36 | s36_t2 | L37 | 14 words, 0.00–8.30 | 309.88–321.44 (11.56s) | 1.393 | 1.25 | grey-rescue; end −1.19s (23f tail-loop). PHRASING GAP: song phrases sparsely (pauses 2.22s, 1.42s between phrases); take sings continuously — mid-line words land up to 2.09s early. |
| S37 | s37_t1 | L38 mantra (decision) | 8 words, 0.00–5.82 (x2 bursts) | first two repeats 323.32–327.54 (4.22s) | 0.725 | 0.80 | grey-rescue on the opening: bursts mouth-synced to the first two repeats, end +0.44s late. Remainder = own-hold loop montage cover (hold 5.82–9.0s verified moving: mean diff 2.39, no zero frames). No sung-burst replay — replaying sung bursts over later repeats would reuse vocal footage at a different song position. |
| S38 | s38_t2 | L39 | 13 words, 0.00–7.32 | 338.55–343.91 (5.36s) | 0.732 | 0.80 | grey-rescue; end +0.50s; per-word max 0.50s — best grey result. |
| S39 | s39_t1 | L40 mantra (decision) | 4 words, 0.00–3.14 (ONE mantra) | first repeat 344.55–346.35 (1.80s) | 0.573 | — | COVER: 0.573 is below the 0.60 grey floor — the single mantra cannot land on any song repeat within caps. Whole slot = montage cover (take video + tail at 1.0, 31f tail-loop; tail verified moving: mean diff 1.44, no zero frames). Captions stay song-timed. |

## Verdict counts

- Mouth scenes: 26 total = 14 span-usable + 12 grey-rescued.
  - Span-usable (endpoints land exactly): S06, S08, S10, S13, S14, S15, S16,
    S17, S18, S19, S22, S26, S27*, S34* (*carries a phrasing-gap disclosure).
  - Grey-rescued (band-edge warp, disclosed end residual): S01, S02, S07,
    S09, S11, S12, S20, S23, S28, S29, S36, S38.
- Cover slots (no mouth claim): S03 cutaway (1), structural S04, S05, S21,
  S24, S25, S30, S35 (7), mantra-slice S31–S33 (3), decision S39 whole slot
  (1). S37 is split: opening bursts grey mouth-synced, remainder hold-loop
  montage cover.
- Total: 26 + 1 + 7 + 3 + 1 + 1 (S37) = 39 scenes.

## Headline finding (for the parent's report)

Whole-line tempo drift — the diagnosed cause — is fixed by this warp plan:
every usable take's endpoints land exactly, every grey take's endpoints land
within a disclosed residual (worst −2.95s S28, +1.07s S29, both covered by
moving tail-loops / breath gaps). BUT the measurement also exposes a second,
unfixable-by-warp class: PHRASING GAPS. In S01, S27, S34, S36 (and milder in
S02, S09, S20, S29) the take places its pauses where the song does not, so
mid-line words drift 1–2s even with endpoints exact. No whole-clip or
per-word warp within the 0.80–1.25 caps can fix a pause placed in the wrong
spot (required interval factors 0.27–4.56x). Those scenes ship with disclosed
mid-line offsets, not with a sync claim. Closing them needs either new takes
sung to the song's phrasing or audio-driven repaint (user go-ahead on
modality/spend — not started).

## Files

- Per-take word JSONs: recut_work/measure/*.json (+ *_slice.json for the 8
  burst-drop takes). Untracked scratch, not committed.
- Scripts: recut_work_measure.py, recut_work_slices.py, recut_work_analyze.py
  (committed with the cutlist/report).
