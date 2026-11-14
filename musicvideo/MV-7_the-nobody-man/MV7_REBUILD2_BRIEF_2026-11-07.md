# MV-7 REBUILD-2 — user order 2026-11-07 ~08:17 EST

User verdict on the otaku rebuild (delivered ~06:53 EST): REJECTED.
"the timing of the lyrics to the actual music is off — you just have
videos of someone saying nobody man over and over and over".
Order: re-cut AND re-fire AND re-analyze, using the timing and the
words based off of the song. The otaku cut is dead — do NOT re-deliver
it. MV7_OTAKU_DELIVERED.flag has been renamed *.rejected-timing.

## Parent re-analysis (2026-11-07, from SONG_WORDS.json + work/otaku_take_words/)

Line ratio = song sung span / take sung span (first word onset to last
word end, both measured). MV-2 v6 generation band: 0.80–1.25. A take
outside the band is a GENERATION MISS — assembly warping cannot fix it;
it must be re-fired with PACING as the named axis, or SPLIT.

CLEAR MISSES (take sings far too slow; the otaku cut squeezed them
1.25–1.74x, which is why the mouths read as generic chant):
- U06 0.577 · U08 0.587 · U17 0.590 · U15 0.607 · U16 0.608 ·
  U34(t2) 0.609 · U21 0.617 · U14 0.665 · U32 0.667 · U20 0.677
  (also: no face in take — cover only) · U13 0.679 · U22 0.679 ·
  U18 0.697 · U35(t2) 0.708 · U05 0.730
GREY / STRETCHED: U02 1.263 · U37 1.290 · U36 1.232 (edge)
IN BAND (keep candidates, still need mouth-event anchoring):
U01t2 .866 · U38 .874 · U33 .928 (truncates final word — bad-word
rule) · U03 .957 · U07 .958 · U12 .961 · U10 .982 · U09 .986 ·
U25 .991 · U23 .994 · U04 1.005 · U11 1.017 · U19t2 1.031 ·
U24t2 1.088 · U26 1.111 · U31 1.145 · U40 1.154 (words garbled:
"nobody man man") · U39t2 1.163 · U27 .828
BRIDGE: U28–U30 are montage by design; their take audio is NOT the
bridge lines (ASR hears outro phrases) — montage stays legitimate
ONLY if cut on beats with the kinetic layer carrying the words, and
U31 (1.145, in band) returns to his face for B.6.

Second failure the re-cut must fix: the otaku gate itself counted
30/61 mouths open at exact onset (48/61 by +0.33s). Anchors were
take-AUDIO word times; visible mouths lag them. Rebuild-2 anchors on
VISIBLE MOUTH EVENTS only (MV-3 method): measure each kept/refired
take's mouth-open onsets from its frames, shift/warp phrases so the
mouth event lands on the song word onset.

## Rebuild-2 rules (non-negotiable)

1. Song is the grid: SONG_WORDS.json (330 words, measured) + beat
   grid (103.36 BPM, work/beat_grid.json). Every unit's placement is
   computed from THOSE word times, per line, per word.
2. Re-fire every CLEAR MISS unit as SINGLE-LINE takes (split 2-line
   units into one take per line — shorter vehicles pace faster).
   Vehicle discipline per Slopcannon: exact lyric in quotes at least
   twice, performance window in whole/half seconds, brisk/fast
   delivery wording ("sings briskly, quick tempo, no lingering —
   the whole line in about X seconds"), articulation clause,
   mouth closes after last word. Otaku identity lock + era stills
   unchanged (refs/otaku_eraA/B/C.webp). Volley cap 6, autonomous.
   A re-fired take only enters the cut if its measured line ratio
   lands 0.80–1.25 (grey 0.60–0.80 / 1.25–1.60 needs forced-alignment
   re-measure + mouth check before use). Two failed pacing pulls on
   a line = split it smaller or mark STRUCTURAL and cover it with
   beat-cut montage + kinetic words (bad-word rule), disclosed.
3. KEEP-pool takes (in band) are re-anchored on mouth events, phrase-
   smooth warps only, no slow past 0.5x, speedups disclosed.
4. Kinetic HIGHLIGHT layer rebuilt from SONG_WORDS.json (it was the
   one layer actually on song time — keep that standard).
5. GATE ON THE MASTER, stricter than last time: mouth state read at
   EVERY sung line onset (open/transitional at onset or +1 frame —
   not +0.33s), frame count exact (4493), SEI crf=18.0, AAC probe,
   motion check during words. Any line onset closed on the master =
   fix that unit (shift to its mouth event / swap take / montage
   cover for that line) before delivery. Do not ship a disclosed
   30/61 again.
6. Deliverables: masters/mv7_im_the_nobody_man_16x9_rebuild2.mp4
   (house CRF 18) + _50mb chat copy (AAC copied untouched), notes in
   MV7_REBUILD2_NOTES.md, MV7_REBUILD2_DELIVERED.flag, commit +
   announce via ~/workspace/freeq/announce.sh.
7. Incremental on-disk progress: MV7_REBUILD2_PROGRESS.md updated
   after every volley and every stage — if you die, the next agent
   resumes from disk. Keep the final report SHORT.
