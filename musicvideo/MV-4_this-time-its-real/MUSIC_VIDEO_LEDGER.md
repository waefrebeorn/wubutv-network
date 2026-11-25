# MUSIC VIDEO LEDGER — MV-4 "This Time It's Real (Futurama is cancelled)" (NOVA)

Assembled 2026-11-05. Full song, 30 scenes, one original space-crooner (NOVA) with
BOLT (robot dancer) and ZIB (three-eyed alien dancer) supporting. Suno track is the sole
master audio; generated take audio was mined for timing, then dropped. Original
retro-future cartoon space world in the Futurama SPIRIT — farewell dance party, delivery
spaceship, robots and aliens dancing — no licensed characters, logos, or copied designs.
The song's own lyrics name Futurama and quote "Good news, everyone"; the user's sung
words stay verbatim; on-screen characters are original WuBuTV-native.

## Master (verified 2026-11-05, ffprobe + full decode + md5)

| Master | File | Size | md5 | Spec |
| --- | --- | --- | --- | --- |
| 16:9 | `masters/mv4_this_time_its_real_16x9.mp4` | 130,091,539 | `dca20f5c1bc4878a30897291be4911c7` | 1280x720, h264 + AAC 48kHz stereo, 238.805s, 5731 frames @24fps, faststart |

ONE 16:9 only (standing rule from 2026-11-05 01:31 EST: "only one 16:9 from now on").
Captions burned in (346 events, line-block + per-word cadmium highlight); corner bug
`~ WuBu ~` on all frames. Master audio is `track.mp3` re-encoded to AAC 192k.

## Source

- Track: `track.mp3`, md5 `d46af0ef2e5abfca97db16905d20fb7d`, 238.805s, extracted from the
  user-sent Suno video export (`track.mp4`, md5 `5b877cb3868501dc57494ca568775cb9`,
  10,103,934 B, 824x1464, 238.800s).
- Song words: `SONG_WORDS.json` (360 words, measured from the audio; performed song, not the sheet).
- Lyrics: `lyrics.txt` (verbatim owner text). Captions: `captions_16x9.ass`, keyed to SONG_WORDS times.
- MUSIC_TAG source id: `MV-4-THIS-TIME-ITS-REAL`. No `music/tags.json` row (music-video
  masters take no bed/sting row — recorded here instead).

## Cut

See `CUTLIST.md` for the full scene table and `masters/ASSEMBLY_REPORT.md` for validation.
Active takes: S01–S05 t1, S06 t3, S07–S22 t1, S24 t1, S26 t1, S27 t1, S28 t1, S29 t1,
S30a t1, S30b t1. S23 + S25 structural (montage cover, two failed attempts each — no volley 7).
S05 restaged (original vehicle denied `integrity_check_failed`, never re-fired); S06 t3 fixed
the G2 name-sign / "T" glyph rejects; S18 t2 fixed the "WuBuTV." watermark; S21 restaged
after a denied generation; S23 t2 rejected (watermark + missing repeat); S25 t2 blocked
(generation denied, never re-fired).

Placement: per-scene grid search (warp 0.80–1.25, trim near first word) maximizing words
inside +/-0.50s of the song's word times. Segment boundaries = next scene's song first-word
time. Tail-loops cover the inter-scene no-word gaps (S08, S09, S11, S19, S20, S28, S30a, S30b).
S11 trimmed at first-delivery end (7.22s).

## Sync (gated on the master itself)

- Master audio dictated: 379 words vs 360 song words, 329 aligned pairs, median |offset|
  **0.020s**, 0 token mismatches. Agreement 0.914 is a repeat-line pairing artifact (the song
  repeats "Futurama's finished" and the outro's soft lines; difflib mis-pairs identical lines
  across the track). Audio PASS.
- Motion audit on the master: 5731 frames, mean diff 4.249. Longest near-dup run 26f at
  30.92–32.00s — inside S04, in the no-word gap after "in style", the take's post-line held
  pose, not during vocal. Adjudicated PASS (frame rule fails only on >=24f DURING VOCAL).
  Next runs 19f/14f in S20's tail-loop (the 155.16–158.76 no-word gap). Motion PASS.
- Picture spot-check: 14 frames at song word times — mouths open/singing at the word times
  in the sampled scenes; S23/S25 montages and S28/S30 cutaways show the right picture;
  captions + bug present throughout. Picture PASS.
- Overall: **WORKING SYNC** (not SYNCED — the generated takes' internal tempo drift does not
  support the SYNCED tier: median <=0.125s and max <=0.25s per scene).

## Flags in the cut (disclosed, no reroll ordered)

- S12 weakest sync (tempo drift; 8/17 words inside +/-0.50s, median 0.528s).
- S26 weak (1/4 words inside +/-0.50s, median 0.876s; 4-word slow line, take evenly spaced
  vs song back-loaded).
- S29 repeat gap: the song repeats "Good news, everyone" twice but the take sings it once;
  the second repeat has no dedicated mouth (max paired-word offset 1.99s).
- S19 first-half words garbled in take audio ("the old ones" -> "the line like muscles");
  master audio carries the correct words.
- Last-word ends at the -0.75s bound in S03/S07/S08/S12/S15/S17 (take's final word short).
- Hue drift: S10 blue-violet skin, S16 blue-grey skin + red lips, S17 blue-violet,
  S25 lavender-grey (strongest). Warm/detailed face render vs S01's flatter pale style is
  now the house style. Added accessories throughout (gold epaulettes, chains, chest panels).
  BOLT round head + antenna ball in S14/S21/S22 (bible says rectangular, no antenna ball).
  S30b ship-design drift (teal/red rocket vs yellow/blue delivery ship in S28/S30a).
- S01/S02 loosest early scenes (8/15 and 9/16 words inside +/-0.50s) — mid-line tempo break
  a single warp cannot fix.

## Files

- Takes: `takes/` (KEEP takes as listed above; rejected takes kept on disk, never chained:
  S06 t1/t2, S18 t1, S23 t1/t2, S25 t1; S05 denied vehicle archived as `mv4_s05_denied_vehicle.txt`).
- Assembly: `assemble_mv4.py`, `build_cutlist.py`, `make_captions_mv4.py`, `validate_master.py`,
  `CUTLIST.md`, `masters/ASSEMBLY_REPORT.md`, `work/assembly_fit.json`,
  `work/assembly_take_words/` (unprompted + prompted Whisper per take).
- Method: cross-check sync spec at `../MV-3_i-am-your-dad/recut_work/sync_proto/CROSSCHECK_SYNC_METHOD.md`
  (per-project adapter: scene table + mishear map as inputs).

## Delivery

- `MV4_DELIVERED.flag` NOT written by assembly — the parent verifies the master from disk
  and delivers it as a chat attachment, then writes the flag and disables the MV kickstand
  ladder (`mv-kickstand-1m/5m/10m/15m/25m`).
- Optional rerolls S19 t2 / S16 t2 / S10 t2 are parent-order-only and were NOT ordered.

## Lyrics redo (2026-11-12)

User playback verdict ~12:41 EST (on the MV-3 Q5 presentation): "lyrics on screen
are wrong and no alignment to music" — redo lyrics + timings for MV-4 (and MV-5,
MV-6, MV-2). Reassembly only: same takes, warps, montage, bug; only the kinetic
caption layer replaced. Full record: `work/lyrics-redo/LYRICS_REDO_NOTES.md`.

- **What was wrong:** the old caption TEXT was (almost) right; the old caption
  TIMES were wrong. Old grid = faster-whisper BASE + hand-normalizations.
  New grid = faster-whisper large-v3-turbo, full clip, no VAD (55 segments,
  364 words). **81/360 words moved >0.10s; median |shift| 0.22s; 21 words
  moved ≥0.5s** — line starts L06 "That's" −1.14s, L19 "But" −0.86s,
  L51 "Futurama's" +1.50s, L26 "Futurama's" +0.66s. The outro was worst:
  old L57 was one 17.26s static block sitting through ~10s of silence and
  burned the sheet's stage direction "(repeat, soft)" on screen for 17s.
  Old grid also mislabeled L14/L29 "Good news" as "Cut/Could news", which
  broke karaoke on both lines (block-only in the delivered master).
- **New captions:** `work/lyrics-redo/mv4_kinetic_redo.ass` — 322 events
  (314 karaoke steps + 8 block events), 52 lines karaoke, 5 block
  (L24, L27, L44, L48, L55), L54 forced block, L57 split into two
  per-phrase blocks ("Good news, everyone." 230.56–234.24; "For real this
  time." 234.24–238.02; the 220.77–230.56 silence stays caption-free).
  Per-line fs scaling capped at 1100px estimated width (MV-13 fix);
  single-backslash overrides only, 0 double-backslash lines (MV-12 fix).
- **New master:** `masters/mv4_this_time_its_real_16x9_lyrics.mp4` —
  129,340,998 B, md5 `1456487dde2be81577fbb0b69c07acd4`, 5731f, 238.805s,
  1280×720, h264 CRF 18, AAC 48k stereo, faststart. Decoded-PCM audio md5
  matches the base master (`dc29cad83fa22b35a17cc3bf1de85d7a`). **Gates ALL
  PASS** (fixed alignment-aware regression gate; re-encode reproduced the
  file bit-identically, confirming the assembly+encode pipeline is
  deterministic; full-res burned kinetic frame reads 7/7 PASS).
- **Chat copy:** `masters/mv4_this_time_its_real_16x9_lyrics_chat.mp4`
  (854×480 crf 23, AAC copied, 46,259,256 B / ~44.1 MB, md5
  `5131d33a388385673fa78884b03337c0`, 5731f, 238.805s, faststart).
- **Q3 note:** the take sync was built on the old (wrong) grid — segment
  boundaries use OLD first-word times (S06 23.34 vs new 23.18; S13 95.40
  vs new 96.06; S26 188.24 vs new 187.90). Take-level word sync inherits
  the old grid's errors; that is Q3's territory, still BLOCKED on the
  snapper stay-rule patch (no sensor). No takes were re-warped in this job.
- Base master untouched (md5 `dca20f5c1bc4878a30897291be4911c7`). NO commit,
  NO delivered flag — the parent writes it.
