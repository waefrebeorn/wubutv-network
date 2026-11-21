# MV-7 OTAKU REBUILD — user order 2026-11-07 ~05:47 EST

## Verdict on the previous build
COMPLETELY REJECTED by the user (playback verdict, outranks all prior gates):
"creepy and no timing — make it a weeb otaku now — this is a hobo, creepy and no market."
The hobo original (20:03 EST 2026-11-06) and its timing correction (22:40 EST)
are DEAD. Never re-deliver them. Old takes are NOT reusable for this rebuild
(wrong character). Song, lyrics, LYRIC_TIMELINE.md, SONG_WORDS.json and the
103.36 BPM beat grid are unchanged and remain the timing authority.

## New character — THE NOBODY MAN as WEEB OTAKU (lock this, every prompt)
Young adult man in his mid-20s, bright and friendly, a proud anime-fan
creator who has posted from his room for years. Identity anchors (restate
in EVERY vehicle, condition on the new era stills):
- Tousled dark hair with ONE cadmium-yellow streak at the front
- Round glasses, bright alert eyes, clean-shaven, clear skin
- Warm determined smile — eager, a little shy, never tired/busted/creepy
- Oversized cozy COBALT hoodie with an abstract white star pattern
  (NO text, NO logo, NO wordmark — he is not UNC)
- Cat-ear headphones resting AROUND HIS NECK (never over the mouth/face)
- Abstract graphic tee under the hoodie (shapes only, no text)

## Room — cozy otaku creator room (marketable, bright, lived-in cute)
- Shelves of ORIGINAL generic anime-style figures (invented designs only —
  NO licensed anime/game characters, no recognizable franchise designs)
- Manga volumes with plain coloured spines — NO readable text anywhere
- Wall posters as abstract colourful art shapes — no licensed faces, no text
- Gaming desk, multiple monitors with ABSTRACT glow (no readable text/UI)
- Plushies, LED strip warmth, tidy-chaotic fan room — never dingy/dark/hobo

## Eras (generate 3 new anchor stills at 16:9 FIRST, read them back, QC them)
- Era A (S01–S10): small start — one modest figure shelf, one monitor,
  the SMALL SPARK LAMP: one tiny glowing star-shaped desk lamp (the motif,
  replaces the candle — otaku version of the small flame)
- Era B (S11–S19): room filling — more figures, second monitor, lamp glows on
- Era C (S20–S24): the kingdom — wall of glowing screens + full figure
  shelves, spark-lamp still burning on the desk, ONE brighter steady light
  among the screens (the one viewer). Final frame rhymes with the first.

## HARD BAN LIST (negative in every prompt)
no stubble, no beard, no thinning hair, no heavy-lidded eyes, no tired grin,
no busted grin, no older man, no dark dingy room, no candle, no gothic mood,
no creepy expression, no hood shadowing the face, no readable text, no logos,
no licensed characters, no franchise posters, no wordmark.

## Timing — the previous build's gate passed and the user still heard NO
## timing. This rebuild must fix perception, not just measurement:
1. SHORTER SINGING UNITS: re-split the 24-scene plan at LINE level from
   LYRIC_TIMELINE.md — each generated take covers 1–2 lines max (aim for a
   ≤~5 s sung window per take). No 8–10 s multi-line takes that drift.
   Every hook/chant occurrence gets its OWN fresh take. No reuse.
2. Performance-window staging per Slopcannon (facing camera, static MCU,
   gesture/camera only outside the sung window, lyric stated exactly twice,
   articulation clause, mouth closes after last word).
3. Measure BOTH sides (take audio word stamps + visible mouth events),
   phrase-smooth warp only, caps: speedups fine (disclose), never slow
   past 2x. Bad words → beat-cut montage for exactly that span.
4. KINETIC TIMING LAYER (visual-forms Family A4 HIGHLIGHT, in POST only):
   burn a kinetic lyric layer built from SONG_WORDS.json with
   visual-forms/tools/kinetic_ass.py — full line on screen, active word
   pops CADMIUM exactly on its song onset (2 frames early per playbook).
   This layer is the timing the viewer can SEE land. Audit onset frames
   on the rendered master.
5. MASTER GATE (all must pass on the rendered master, not the cutlist):
   mouth state open/transitional at every line + hook onset; motion gate
   (no frozen run ≥24f during words); kinetic onset audit (word pop within
   2 frames of onset); ffprobe AAC + x264 SEI crf=18.0; exact frame count.
   If a gate cannot pass honestly, disclose it — never claim a pass the
   user's playback will contradict.

## Deliverables
- masters/mv7_im_the_nobody_man_16x9_otaku.mp4 (CRF 18 house master)
- masters/mv7_im_the_nobody_man_16x9_otaku_50mb.mp4 (chat copy ≤50 MB,
  audio copied untouched) — deliver THIS in chat when done
- Write MV7_OTAKU_REBUILD_NOTES.md (takes, QC rows, warp extremes, disclosures)
- Rename MV7_DELIVERED.flag / MV7_TIMING_CORRECTED.flag to *.rejected-hobo
  and write MV7_OTAKU_DELIVERED.flag only when the new master truly ships.
- Commit project files (stage explicit paths, never git add -A).
- Announce via ~/workspace/freeq/announce.sh like every delivery.

Volley cap: ≤6 videos per agent run, chained — proceed autonomously on
standing authorization, never wait on the user.
