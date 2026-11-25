# MV-4 ASSEMBLY REPORT — "This Time It's Real (Futurama is cancelled)"

Assembled 2026-11-05. ONE 16:9 master only (standing rule: one 16:9, no 9:16, no chat copy).

## Master (verified from the file itself)

| | |
|---|---|
| File | `masters/mv4_this_time_its_real_16x9.mp4` |
| md5 | `dca20f5c1bc4878a30897291be4911c7` |
| Size | 130,091,539 B |
| Video | h264, 1280x720, 24fps, **5731 frames** (exact), 238.805s |
| Audio | AAC 48kHz stereo, 192k — `track.mp3` (md5 `d46af0ef2e5abfca97db16905d20fb7d`) re-encoded; generated clip audio dropped |
| Container | faststart |
| Full decode | OK, zero errors |
| Captions | burned in (`captions_16x9.ass`: 346 events, line-block + per-word cadmium highlight) |
| Corner bug | `~ WuBu ~` (DejaVuSans-Bold, cadmium #FFC61E, bottom-right, all frames) |

Build: `assemble_mv4.py` (49 pieces: 26 singing scenes + 2 montages + 3 cutaways + 8 tail-loops),
libx264 medium CRF 18. First attempt died mid-encode (session reaped at ~82MB, no moov atom);
rebuilt detached via setsid/nohup — the encode survived 21+ minutes under a post-reboot load
average of 12–17 (the VM rebooted ~09:22 EST that morning). Lesson for the next build: launch
long encodes detached from the start; an exec-session child does not survive.

## Cut

See `CUTLIST.md` for the full per-scene table. Coverage: 28/30 scenes from KEEP takes
(29 takes; S30 = 2 takes), S23 + S25 structural montages. No volley 7.

- Placement: per-scene grid search over warp [0.80, 1.25] x trim near the first word,
  maximizing words inside +/-0.50s of the song's word times, then median |offset|.
  Where the grid did not beat the endpoint-anchored SPAN placement on band count, SPAN kept.
  All warps inside the 0.80–1.25 caps. Song is tempo gospel — the picture warps, never the song.
- Segment boundaries = next scene's song first-word time (cumulative rounding, sum 5731f);
  inter-scene no-word gaps are covered by the previous take's tail.
- S11 trimmed at first-delivery end (7.22s); the repeat tail is not used in its segment
  (its 8-frame tail-loop replays post-second-delivery held pose, frames 229–240).
- S28/S30a/S30b are 0-word cutaways (w=1.0). S23/S25 are montages from post-word tails
  (every slice starts after the donor's segment use AND after the donor's last word +1 frame).
- S03/S08 first-word onsets corrected by visual + RMS cross-check (mouth closed at 0.0s,
  open by 0.5s; RMS rise): S03 0.45s, S08 0.30s. Whisper back-filled both to 0.00 and the
  prompted decode overshot both to 1.06.
- QC ratio correction applied: QC "duration ratios" were window-based, but windows contain
  pre-word instrumental gaps; assembly warps use measured song WORD spans (S09 1.08 -> 0.868
  is the largest correction; S03's span warp was likewise biased by its false 0.00 first-word stamp).

## Validation — GATE ON THE MASTER (not the cutlist)

### (a) Audio (master's own audio dictated, aligned to SONG_WORDS)

- Dictated 379 words vs 360 in SONG_WORDS; 329 aligned pairs; **median |offset| 0.020s**;
  **0 token mismatches** among paired words.
- Agreement 0.914 (not 1.00) is a repeat-line artifact, not a timing error: the song repeats
  "Futurama's finished" and the outro's soft lines many times, so difflib mis-pairs identical
  lines across the track (worst pair: outro "real" dictated 236.22s paired to the held-line
  "real" at 222.81s, 13.41s — the same word sung twice, softly, at the end), and Whisper
  splits the outro's held line into extra tokens (220–240s: 13 dictated vs 5 in SONG_WORDS).
  Per-20s bucket counts match within +/-1 everywhere except the outro.
- Verdict: **AUDIO PASS** — right song, complete (238.8s of audio), correctly timed, no drift.
  (The script's first-run gate printed FAIL on a raw-agreement threshold; the threshold was
  wrong for a repeat-heavy song and is corrected in `validate_master.py` to median + token identity.)

### (b) Motion (full master decoded at 160x90, native 24fps)

- 5731 frames decoded. Overall mean diff **4.249** (threshold 0.5 — the picture is moving).
- Longest near-dup (<0.5) run: **26f at 30.92–32.00s** — inside S04, in the **no-word gap**
  30.54–32.36 (after "in style", before the chorus). It is the take's post-line held pose,
  not a freeze during words. Frame rule is "FAIL if vocal near-dup run >=24f DURING VOCAL" —
  this run is not during vocal. **Adjudicated: PASS.**
- Next runs: 19f at 155.79–156.58s and 14f at 158.17–158.75s (both in S20's tail-loop,
  the 155.16–158.76 no-word gap — held pose, not during vocal); 15f at 76.42–77.04s
  (S10, mid-"They sealed it up", under the 24f gate); all others <=13f.
- Per-scene mean diffs: lowest S20 1.060, S03 1.100, S01 1.379; highest S28 14.324,
  S22 10.936. No scene averages under 0.5. **MOTION PASS.**

### (c) Picture sync (14 frames sampled at song word times, read visually)

- Singing scenes sampled (S01, S03, S05, S08, S10, S12, S16, S19, S21, S29): mouths are
  open/singing at the word times (S01 "over", S03 "conclusion", S08 "dark", S12 "mean",
  S16 "dark" clearly open; S05/S10/S19/S21/S29 mid-word consonant shapes — "memory" caught
  on the "m", lips together, correct). Captions render on every frame with the per-word
  cadmium highlight; the `~ WuBu ~` bug is present bottom-right on every frame.
- S23 montage at 177.0s shows the dance floor (NOVA + BOLT + ZIB), S25 at 191.0s shows the
  ship-window wide shot, S28 at 208.0s shows the delivery ship lifting off, S30b at 235.0s
  shows NOVA waving as the ship rises. All correct picture for their slots.
- **PICTURE PASS.**

### Overall gate: PASS — WORKING SYNC

Per-scene placement (from `work/assembly_fit.json`, measured on the takes, carried into the master):
26 singing scenes; words inside +/-0.50s: S04/S05/S09/S11/S13/S14/S16/S17/S19/S20 100%,
most others 70–90%. Median |offset| per scene 0.05–0.35s except the disclosed weak scenes below.
This is a WORKING SYNC master, not a SYNCED one (SYNCED needs median <=0.125s and max <=0.25s
per scene; the generated takes' internal tempo drift does not support that tier).

## Disclosures (honest, carried from QC + assembly)

- **S12 weakest sync** (tempo drift: take fast-then-slow; 8/17 words inside +/-0.50s, median
  0.528s). No single warp fixes a drifting take; the grid placement (warp 1.100) is the best
  single-warp compromise (SPAN was 4/17).
- **S26 weak** (1/4 words inside +/-0.50s, median 0.876s): a 4-word slow line whose take is
  evenly spaced while the song back-loads the words. Kept at SPAN warp 1.20 (grid wanted the
  1.25 cap for a 0.076s median gain on 4 words — not worth it).
- **S29 repeat gap**: the song repeats "Good news, everyone" twice (211.75–213.89 and
  214.17–216.73) but the take sings it once (7 words vs 10). The single delivery stretches
  across both repeats; the second repeat has no dedicated mouth (max paired-word offset
  1.99s on the "For" that follows). The take is QC-passed against its vehicle, which listed
  the line once. Captions show the repeat twice, correctly.
- **S19 garble**: first-half words garbled in the take audio ("the old ones" renders as
  "the line like muscles"); the master audio carries the correct words. Placement is tight
  (13/13 words inside +/-0.50s, median 0.119s).
- **Last-word ends**: several scenes sit at the -0.75s last-word-end bound (S03, S07, S08,
  S12, S15, S17) — the take's final word is short, so the mouth closes up to 0.75s before
  the song's held final note ends. The middle words are tight; the band objective chose
  this trade-off.
- **Hue drift (disclosed, no reroll ordered)**: S10 blue-violet skin, S16 blue-grey skin +
  red lips, S17 blue-violet, S25 lavender-grey (strongest). Warm/detailed face render vs
  S01's flatter pale style is now the house style. Added accessories throughout (gold
  epaulettes, chains, chest panels, bow ties). BOLT round head + antenna ball in S14/S21/S22
  (bible says rectangular, no antenna ball). S30b ship-design drift (teal/red rocket vs the
  yellow/blue delivery ship in S28/S30a).
- **S23/S25 are montages, not mouth-sung slots** — flagged as such in the captions' context;
  the picture does not pretend to sing those lines.
- **S01/S02** are the loosest early scenes (8/15 and 9/16 words inside +/-0.50s, medians
  0.214s / 0.345s) — the takes have a mid-line tempo break a single warp cannot fix.

## Files

- Master: `masters/mv4_this_time_its_real_16x9.mp4` (md5 above; git-ignored media — ships via HF CDN, not the text repo)
- Cutlist: `CUTLIST.md` (per-scene placement + montage slices + tail-loops)
- Captions: `captions_16x9.ass` (346 events; `make_captions_mv4.py`)
- Assembly: `assemble_mv4.py` (plan + filter graph + encode)
- Measurement: `build_cutlist.py` (grid search), `work/assembly_fit.json`,
  `work/assembly_take_words/` (unprompted + prompted Whisper per take),
  `work/transcribe_assembly_takes.py`
- Validation: `validate_master.py`, `work/master_dictation.json`,
  `work/master_motion.json`, `work/master_check/` (14 word-time frames + 2 contact sheets),
  `work/firstword/` (S03/S08 first-word onset evidence)
- Ledger: `MUSIC_VIDEO_LEDGER.md`

## Not done by this assembly

- No `MV4_DELIVERED.flag` written (parent verifies from disk and delivers).
- No S19 t2 / S16 t2 / S10 t2 rerolls (parent-order-only, not ordered).
- No volley 7. S23 + S25 stay structural.
