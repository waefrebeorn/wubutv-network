# MV-7 REBUILD-2 — line-ratio audit (2026-11-07 ~08:20 EST)

Prepared after the user's 08:17 EST rejection of the otaku cut
("timing of the lyrics to the actual music is off — you just have videos
of someone saying nobody man over and over"). Do NOT re-deliver the otaku cut.

## Why the timing reads off — three causes, all verified on disk

1. **The otaku assembly warped each unit UNIFORMLY, not per word.**
   `work/otaku_assemble.py` applies one `setpts` multiplier per unit
   (take sung span -> whole unit window). No swing keyframes: `grep -i
   swing|keyframe work/otaku_assemble.py` returns nothing, although the
   standing method (SOUL.md / Slopcannon WORD-SYNC) is per-word warping
   between keyframes. A unit whose take rushes line 1 and drawls line 2
   keeps that imbalance — the second line's mouth lands up to **+1.56s**
   off the song (U25 C2.4) even when the unit's overall ratio looks fine.
2. **Anchors were take-AUDIO word times, and visible mouths lag them.**
   The rebuild notes say so plainly; the mouth gate found 30/61 onsets
   open at the exact frame, 13 closed past +0.33s, concentrated in the
   held-note chant takes. The hobo correction measured the same lag
   per scene (`work/correction/lag_final.csv`, 58 rows) — the MV-3 method
   exists and is reusable for the re-cut.
3. **Most takes were generated at the wrong tempo.** Warp speeds applied
   in the build run 0.785–1.742x. A take sped up 1.7x is a performer
   gabbling; no warp makes a 5s drawl land as a 2.5s line with natural
   mouths. This is what the user hears as "someone saying nobody man
   over and over."

## Method

- Song line spans: `LYRIC_TIMELINE.md` line table (confirmed starts).
  Chant/tag splits (I1a–d, I2a–c, C1.Ta–Td, FC.Ta–Td) are [inferred]
  even splits — the song transcription (`SONG_WORDS.json`, Whisper
  small) MERGES repeated chant words (e.g. one "nobody" stamp spanning
  two repetitions), so per-repetition song onsets inside the hook are
  unmeasured. Those line ratios are flagged [inferred].
- Take line spans: shipped take per `otaku_assemble.py` (t2 for
  U01/U19/U24/U34/U35/U39, t1 otherwise), from
  `work/otaku_take_words/*.json` segments, else word-count split.
- Gate (per MEMORY.md rebuild-2 order, MV-2 v6): line ratio
  (song span / take span) must sit 0.80–1.25. Onset drift = take line
  audio onset mapped through the build's uniform warp, minus song line
  onset. Drift >0.30s with a passing ratio = re-cut candidate.
- Full numbers: `work/rebuild2_line_audit.json` (per line) and
  `work/rebuild2_ratio_audit.json` (per unit).

## Dispositions (40 units)

### REFIRE — 25 units / 38 lines (single-line takes, pacing = named axis)
U01 (I1a+I1b — t2 STILL missing "I'm the" of line 2; take sings
"I'm the nobody man, nobody man"), U02 (I1c 1.38, I1d 1.56, onset
+0.44s), U05 V1.2 (0.60), U06 (V1.3 0.59, V1.4 0.57; sped 1.74x),
U08 (PC1.1 0.73, PC1.2 0.55), U11 C1.2 (1.40), U12 (C1.3 0.76,
C1.4 1.90, onset +1.14s), U13 (C1.5 0.71, C1.6 0.63), U14 C1.7
(0.66), U15 C1.8 (0.61 — "Nobody" held 2.34s in the take),
U16 (C1.Ta 0.75, C1.Tb 0.69), U17 (C1.Tc 0.78, C1.Td 0.72),
U18 V2.2 (0.59), U21 (PC2.1 0.79, PC2.2 0.47), U22 PC2.3 (0.68),
U24 C2.2 (1.62), U25 (C2.3 0.64, C2.4 2.72, onset +1.56s),
U27 (C2.7 0.64, C2.8 1.69, onset +1.47s), U32 FC.1 (0.62),
U33 (FC.3 0.60, FC.4 4.46 — take truncates the final word to "ma-"),
U34 FC.5 (0.49 — take drawls the line over 5.12s vs 2.52s song),
U35 FC.7 (0.71), U37 FC.9 (1.29), U39 FC.Tb (2.59 [inferred split]),
U40 (take sings "Nobody man man" — 2nd "Nobody" missing entirely).

### RE-CUT from existing take — 1 unit
U07 V1.6 only (ratio 1.15 passes, onset +0.36s): per-line re-warp
onto VISIBLE mouth events. Note U32 FC.2 (+0.51s) and U34 FC.6
(+0.58s) show the same pattern but their units are refires anyway,
so the fix rides with the new takes.

### KEEP — 10 units (pacing OK; re-cut must still re-anchor them on
visible mouth events, NOT take-audio — the mouth lag applies here too)
U03, U04, U09, U10, U19, U23, U26, U31, U36, U38.
Caveat: U38 FC.10 lyric stays [uncertain] (ASR "can't turn the small
things cray" vs sheet "Yeah, I turn the small things grand").

### No action
U20 — cover shot (guitar/room, no face); V2.6 ratio 0.69 affects only
cover motion, not lipsync. Keep as cover.
U28–U30 — bridge montage by design (no mouth sync).

## What rebuild-2 still needs (not done here)

1. **Measured chant/tag onsets.** The hook (7 reps, 0–19s) and both tag
   chants have no measured per-repetition song onsets — Whisper merges
   them and the timeline marks them inferred. Re-fire cannot be gated
   on the hook until these exist: ear-measure the 7 intro onsets
   (or forced-align the song against the performed lyric order), same
   for C1 tag (67.80–75.84) and FC tag (173.30–183.24).
2. **Re-fire vehicles**: one line per take, with the song line's span
   (from the table above) as the pacing target — the take must sing
   the line in 0.80–1.25x the song span, verified from the take
   transcription BEFORE assembly (generation miss, not warp fix).
3. **Re-cut anchors = visible mouth events** (MV-3 method,
   `work/correction/` tooling), per line, on the new master; gate on
   the master at every line onset before delivery.
4. Delivered otaku master verified on disk: 187.208s, 1280x720, 24fps,
   md5 c89c4757928a31b95ada25928d498020 — matches the rebuild notes.
   Do NOT re-deliver it.
