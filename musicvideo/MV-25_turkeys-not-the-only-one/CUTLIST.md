# MV-25 "Turkey's Not the Only One" — CUTLIST

Master: `masters/mv25_turkeys_not_the_only_one_16x9.mp4` — 1280×720, 24fps,
4704 frames, 196.000s. Audio: track.mp3 re-encoded AAC 48kHz 192k (never
stream-copied). Lyric captions as a mov_text subtitle track (never burned in).
`~ WuBu ~` corner bug burned in post (drawtext, gold, bottom-right).

Assembly method: per-scene segments rendered frame-exact (cumulative
round(t×24) tiling), concat stream-copy → joined.mp4 (verified 4704f / 196.000s)
→ single CRF 18 master encode. Singing scenes: ONE smooth phrase warp per scene
(setpts factor k = song vocal span ÷ take vocal span), first word anchored to
the song's first word. Wordless scenes at natural speed. Segments at CRF 14
intermediate. Segment map: work/swing/segments.json; builder:
work/swing/build_master.py.

| Scene | Window (s) | Take | Assembly |
|---|---|---|---|
| S01 | 0.00–8.10 | t1 | Head cover: take 6.14–8.92 natural (post-line presentation span, mouths closed) 0.00–2.78; main take 0.00– k=0.911, first word lands 2.78 |
| S02 | 8.10–15.96 | t1 | take 0.50– natural |
| S03 | 15.96–21.90 | t1 | take 0.00– k=0.794 |
| S04 | 21.90–27.90 | t1 | take 0.00– k=0.767 |
| S05 | 27.90–31.58 | t1 (5s) | take 0.66– natural |
| S06 | 31.58–39.56 | t1 | take 0.00– k=0.926 |
| S07 | 39.56–48.12 | t1 | take 0.00– k=0.913 |
| S08 | 48.12–55.98 | t1 | take 0.80– natural — WORDLESS COVER (hook window) |
| S09 | 55.98–63.86 | t1 | take 0.00– k=0.925 |
| S10 | 63.86–72.90 | t2 | take 0.48– natural — WORDLESS COVER (hook window) |
| S11 | 72.90–79.24 | t1 | take 1.04– k=0.817 |
| S12 | 79.24–88.74 | t1 | take 0.00– k=1.011 |
| S13 | 88.74–97.62 | t1 | take 0.00– k=0.967 — extended 0.70s to fill the plan's instrumental gap before S14 |
| S14 | 97.62–105.66 | t1 | take 0.00– k=0.924 |
| S15 | 105.66–113.02 | t1 | take 1.00– natural — WORDLESS COVER (hook window) |
| S16 | 113.02–121.40 | t2 | take 0.00– k=0.895 |
| S17 | 121.40–130.14 | t1 | take 0.60– natural — WORDLESS COVER (hook window) |
| S18 | 130.14–137.54 | t2 | Montage sub-cuts on chant onsets: 130.14 take 0.00– (table wide) / 131.54 take 5.00– (adults serving) / 133.60 take 3.00– (turkey ECU) / 135.62 take 8.00– (stuffing ECU), all natural |
| S19 | 137.54–143.38 | t1 | take 0.00– k=0.849 |
| S20 | 143.38–151.28 | t2 | take 0.00– k=1.045 |
| S21 | 151.28–159.58 | t2 | take 0.90– natural — WORDLESS COVER (hook window); extended 0.56s to fill the plan gap before S22 |
| S22 | 159.58–168.56 | t2 | take 0.00– k=1.286 |
| S23 | 168.56–179.00 | t1 | take 0.00– k=1.044 (10.44s window over a 10s take) — WORDLESS COVER (hook window) |
| S24 | 179.00–187.68 | t1 | Head cover: take 4.54–7.16 natural (candlelit post-line span) 179.00–181.62; main take 0.00– k=1.009, first word lands 181.62. Window corrected from the pre-pro split (see GATE_LOG) |
| S25 | 187.68–196.00 | t1 | take 0.00– k=0.850, onset anchored at 187.68 |

Rejected takes (not in the master): S08/S10 singing vehicles refused by the
generator (never produced); t1 takes of S10, S16, S18, S20, S21, S22 replaced
by t2 on the cast axis (apparent minors) — see GATE_LOG.md / TAKE_HISTORY.md.
