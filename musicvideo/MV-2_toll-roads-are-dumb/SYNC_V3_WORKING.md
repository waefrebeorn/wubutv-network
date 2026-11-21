# SYNC V3 — working notes (started 2026-11-02, after user denied v2)

User verdict, verbatim in substance: videos must sync to the lyrics.
No effort was made to sync anything up. The generated takes DID have
contextually correct phrases uttered, even if badly timed, but v2 did
not edit them to sync up. Submission denied. Keep working.

Accepted. This file is the sync work, not a defence of v2.

## What v2 actually did (verified from assemble_v2.sh + CUTLIST_V2.md)

- Every take played from frame 0, for 10.000s (S17: 8.01s), in order,
  concatenated. Take audio discarded with `-an`.
- Cuts sat on the 10s grid (cuts 1-16), then spent the 1.99s total
  trim budget at S17 so later cuts tracked line boundaries within
  0.01-2.51s. Section errors disclosed in CUTLIST_V2.md.
- At NO point did v2 measure where, inside a take, the singer actually
  sings. No onset, no phrase break, no slip, no trim-from-inside.
  That is the fault the user named, and it is correct.

## Measured take-internal timing (2026-11-02)

Method: each active v2 take's native audio (24kHz mono AAC, present
in the take file, discarded by v2) decoded to mono 16kHz, RMS in
0.5s windows. Loud = vocal/music present, drop = post-vocal beat /
quiet. Cross-checked against TAKE_HISTORY QC samples (2s/5s/8s)
and vehicle ORDER (sing-first vs beat-first). Onsets below are
estimates, +/- ~1s, not phoneme onsets. Full 0.5s profiles are in
the working log; dips are phrase-break candidates.

| Take | RMS shape (0.5s) | Vocal onset est. | Vocal end / shape |
| --- | --- | --- | --- |
| S01 t2 | loud 1.5-3s, dip 3.5, loud 4-6, dip 6.5, loud 7-8.5 | ~1.5s | 3 phrases, breaks ~3.5, ~6.5 |
| S02 t3 | loud throughout, fade 9s+ | 0s | continuous |
| S03 t2 | loud throughout | 0s | continuous |
| S04 t3 | loud throughout | 0s | continuous |
| S05 t3 | flat, no clear drop; QC: 2s weave, 5s+8s singing | ~4s (weave first) | sing after weave |
| S06 t2 | loud throughout | 0s | continuous |
| S07 t2 | dip 0.5, loud 2s+ | ~1s | continuous after |
| S08 t1 | dip 0.5, loud 1s+ | ~1s | fade 7s+ |
| S09 t2 | loud 0-4.5, drop to -25 from 5s | 0s | vocal ends ~4.5s, brow-wipe after |
| S10 t1 | loud, dip 1.5 (phrase break) | 0s | continuous |
| S11 t2 | loud 0-2, dip 2.5, loud 3-4, dip 4.5, loud 5-6.5, drop 7s+ | 0s | vocal ~0-6.5s, turn after |
| S12 t3 | quiet 0-1, loud 1s+, dips 3, 5, 7 | ~1s | phrases at ~3, ~5, ~7 |
| S13 t2 | loud throughout, fade end | 0s | continuous |
| S14 t1 | loud throughout | 0s | continuous |
| S15 t2 | loud, fade 7.5s+ | 0s | vocal to ~7s, rest after |
| S16 t1 | quiet 0-3, loud 3s+ | ~3s | dime first, then vocal |
| S17 t2 | loud 0-4, dip 4-6, loud 6.5-9 | 0s | phrases, break ~4-6 |
| S18 t1 | quiet 0.5, loud 3s+ | ~2.5s | watch first, then vocal |
| S19 t1 | loud throughout | 0s | continuous |
| S20 t2 | very quiet 0-5.5 (-36), loud 5.5-8.5, drop 8.5+ | ~5.5s | march first, vocal ~5.5-8.5s only |
| S21 t1 | loud 0-4, drop to -30 from 5s | 0s | vocal ~0-4s, echo gesture after |
| S22 t1 | loud early, gradual fade | 0s | continuous, fading |
| S23 t1 | quiet 0-2.5, loud 2.5s+ | ~2.5s | late onset |
| S24 t1 | loud, dip 6.5 | 0s | continuous |
| S25 t2 | loud 0-3.5, steady drop to -45 | 0s | vocal ~0-3.5s, place/step-back after |
| S26 t2 | loud 0-3.5, drop to -37 at 4s | 0s | vocal ~0-3.5s, silhouette after |
| S27 t2 | loud 0-3.5, drop at 4-5, quiet after | 0s | vocal ~0-3.5s, tear after |

The pattern is exactly the complaint: v2 played S20's march for
5.5s over lyric, S25/S26/S27's post-vocal beats for 6+ seconds
over continuing lyric, S09/S11/S21's quiet beats over lyric, and
S01/S12's internal phrase breaks at arbitrary song times.

## Why a simple 10s-grid slip does not fix it (checked, not assumed)

- 27 takes x 10s = 270s for a 268.01s song: total trim budget
  1.99s. Slipping heads off takes loses footage: sum of beat-first
  slips is ~18s, so a head-slip cut ends ~22s short (computed).
- Moving cut points to lyric boundaries does not fix it either:
  line boundaries are irregular (lines 2-15s). Snapping 27 cuts
  to nearest boundaries gives scenes of 0-20s, several over 10s
  (take runs out) and several under 3s (choppy). Computed in
  /tmp/v3_plan*.py, not shipped as a cut.
- Conclusion: the fix is NOT a new grid. It is a phrase cut:
  cut each take at its measured internal phrase breaks, place
  each phrase chunk at its lyric line start, trim a chunk's tail
  to the line end if it runs long, hold the last frame briefly
  (target <1.5s per phrase) if it ends early. Pre-vocal beats
  play BEFORE their line starts (during the previous line's tail),
  post-vocal beats play AFTER their line ends (during the next
  line's head) only where the beat is short; where a beat is
  long (S20 march 5.5s, S25/S26/S27 post-vocal 6s+), the beat
  must be shortened in the cut, not played in full over lyric.

## V3 method (in progress, song audio untouched)

1. For each active take, list its phrase chunks from the RMS
   dips + QC samples above (chunk = between dips).
2. Map each chunk, in order, to the lyric lines in that scene's
   vehicle true-time window (e.g. S20: mantra line, S25: outro
   echo lines 45-47, S05: verse tail into chorus line).
   Lyrics are never copied into a generation vehicle; this
   mapping is edit-only, using LYRIC_TIMELINE.md line starts.
3. Build the cut chunk-by-chunk: chunk start = lyric line start
   (minus a short pre-vocal lead where the vehicle orders beat
   first), chunk end = next line start or chunk's own phrase
   break, whichever is earlier; hold <1.5s if the chunk ends
   early, trim if it runs long.
4. Verify the assembled v3 by sampling a frame at EVERY lyric
   line start in the master and checking: singer face-to-camera
   and mouth in a vocal passage, not in a pre/post beat.
   Any line start that fails gets its chunk re-slipped or
   re-cut before delivery. No v3 ships on grid alignment alone.
5. Master encoding for the v3 delivery will use the fixed-audio
   form already proven for MV-2 (AAC 48kHz stereo, +faststart,
   moov at front), not the MP3/moov-at-end form of v2.

## Open hard cases (disclosed, not hidden)

- S20: vocal only ~5.5-8.5s in a 10s take. A phrase cut can
  place that vocal on its mantra line, but the march beat
  cannot play in full without overlapping lyric. V3 will cut
  the march short. If the user wants the full march, that scene
  needs a re-fire with sing-first staging (cap: 6 videos per
  user message; not fired in this working pass without a
  separate go-ahead on spend/timing).
- S25/S26/S27 outro: three takes, each vocal ~3.5s, covering
  outro lines 45-48 (238.5-268.01, 29.5s). Phrase-cut alone
  leaves ~19s of outro lyric with no vocal footage in these
  takes. V3 will hold/beat-fill those gaps and disclose them;
  a fully vocal outro needs additional takes or a re-fire
  with longer vocal passages.
- Onset estimates above are +/-1s (RMS + QC, no ASR on this
  VM). V3 verification is visual (frame at each line start),
  not RMS, so a wrong RMS onset cannot pass silently.

Status: measurement done, phrase-cut plan written. Assembly
and line-start verification are the next steps; no v3 master
is claimed yet.

## Update 2026-11-02 ~03:24 EST — user order: time-stretch + word/syllable matching to phoneme detection

This order SUPERSEDES the assemble.md rule that peak warp / time-stretch
is dead and that generated audio is never a timing source. That rule
was written after v1's peak-tween failed; the user's new order is to
use time stretching, properly, with word and syllable matching — not
to repeat v1's peak pairing.

Why v1's peak-tween failed (verified from LIPSYNC_REPORT.json, not
assumed): it paired RMS peaks in order, regardless of words, and the
clamp-then-rescale loop collapsed most scenes to a near-uniform speed
(e.g. S01 all segments 0.777 except the tail). It never matched a
word in the take to the same word in the song. Word matching is the
fix, not a new peak list.

What was built for this order, 2026-11-02:
- Tool: faster-whisper (base model, CPU, int8) in ~/workspace/fw-venv.
  No whisper/torch was on this VM; av 19 breaks faster-whisper's file
  loader, so audio is decoded with ffmpeg to 16kHz mono WAV and fed
  as a numpy array (av bypassed). /tmp is only 512MB — tool venv and
  WAVs live under ~/workspace, not /tmp.
- Song word timings: SONG_WORDS_BASE.json, 404 words for the full
  track, base model. Example: Yeah 4.46-5.04, Listen 7.38-7.96,
  here 7.96-8.30, baby 8.42-8.68, Those 10.58-11.16, shiny 11.16-11.64.
  This is MORE precise than LYRIC_TIMELINE.md's bold-line starts
  (which put line 1 at 0s; whisper puts the first vocal at ~4.5s).
  Whisper mishears some words ("dumb" -> "done", "toll" -> "Toe/Tall",
  "plazas" -> "plasers") — matching must be by order + lyrics.txt
  ground truth, not by raw whisper text alone.
- Take word timings (pilot, base model): S01 t2, S20 t2, S25 t2, S05 t3
  saved as TAKE_WORDS_<scene>_BASE.json. S20: Toll 4.76-6.04, roads
  6.04-6.40, are 6.40-7.04, done 7.04-7.46. S25: toll 0.14-0.56, roads
  0.56-1.50, are 1.50-1.74, done 1.74-2.18. S05: Tall 3.32-4.72, roads
  4.72-5.70, are 5.70-6.34, done 6.34-7.36.
- Honest limit: whisper gives WORD times, not classified phonemes.
  Syllable timing inside a word = vowel-nucleus (RMS/band-energy)
  peaks inside that word's interval, or word onset for 1-syllable
  words. True phoneme classification (/p/ closure vs /b/, etc.)
  would need a wav2vec2 phoneme model + GPU/cloud spend, which is
  NOT built and needs a separate go-ahead. Do not claim phoneme-
  accurate lip-sync from whisper word times alone.

The stretch problem, with numbers (this is why literal unclamped
stretch cannot be the whole method):
- S20 Toll: take 1.28s vs song 0.70s (190-window first Toll) = 1.83x
  video speed to fit the word exactly. Roads 0.36 vs 0.20 = 1.80x.
- S25 roads: take 0.94s vs song 0.26s = 3.6x speed. Are 0.24 vs 0.44
  = 0.55x in the same phrase. Speeds swing 0.55x-3.6x inside one
  4-word phrase if every word is forced to its exact song duration.
- S01 Listen: take 1.88s vs song 0.58s = 3.24x.
Generated takes do not sing at song tempo; forcing every word to
its exact song duration makes motion visibly sped up / slowed down
inside a single phrase. That is a different failure, not a fix.

V3 method, revised per this order (song audio untouched throughout):
1. Transcribe all 27 v2 takes with the base model (word timestamps).
2. Match take words to song words by order + lyrics.txt (correcting
   whisper mishearings), giving anchor pairs (take onset -> song onset)
   per word, and syllable anchors inside multi-syllable words from
   energy peaks in that word's interval.
3. Time-stretch the VIDEO (setpts per segment, take audio discarded)
   between anchors where the ratio is sane (target 0.7-1.4x).
4. Where the ratio is extreme (e.g. >1.4x or <0.7x), do NOT stretch
   the whole word: trim the middle of the held vowel (keep onset +
   closure, motion stays at natural speed) and hold/trim the gap.
   This is stretch + vowel-trim, not stretch-only, and the choice
   per word is logged in the v3 cutlist so the user can see where
   stretch was used and where trim was used.
5. Verification unchanged: frame at EVERY lyric line start, singer
   face-to-camera in a vocal passage, not a beat. Plus a stretch
   report: every word's take duration, song duration, and speed/trim
   applied. No v3 ships on alignment numbers alone.

Open decision put to the user 2026-11-02: stretch+trim hybrid
(recommended, natural motion) vs literal unclamped stretch (exact
word durations, visible 0.55x-3.6x speed swings). Full take
transcription proceeds regardless; the choice only changes the
render rule for extreme-ratio words.

## Decision 2026-11-02 ~03:39 EST — user: swing the speeds, make the words match, time sweeping

User chose literal unclamped stretch, and named the look: time
sweeping. The swing IS the aesthetic, not a defect to trim away.
Hybrid trim is CANCELLED for v3. Render rule now: unclamped
setpts per word interval, song untouched, take audio discarded.

Work done for this decision, same night:
- All 27 v2 takes transcribed (base whisper): TAKE_WORDS_ALL_BASE.json.
  Word counts per take: S01 10, S02 18, S03 21, S04 19, S05 4,
  S06 18, S07 9, S08 4, S09 7, S10 7, S11 11, S12 14, S13 3,
  S14 7, S15 4, S16 9, S17 12, S18 13, S19 7, S20 4, S21 5,
  S22 4, S23 4, S24 12, S25 5, S26 4, S27 4. Total 219 take words
  vs 404 song words — takes sing selected lines/hooks, not every
  song word, so word matching is anchor-based, not full coverage.
- Matching v3 (WORD_MATCH_V3.json): vehicle window expanded +-12s
  + monotonic song order across takes (no reuse, no jumping to a
  later chorus for a common word like "the"/"go"). This fixed the
  first greedy matcher, which jumped S02's "pay" to song 65s and
  left S04-S27 unmatched. Remaining weak spots, disclosed:
  S04 only 3 anchors (S03's tail mis-match consumed its start),
  S21 2 anchors, S27 0 anchors (song's final toll at 257.82-260.80
  is already S26's anchor; S27 is the visual outro tail after
  260s, not a second vocal occurrence), S08/S16 partial.
  Those scenes fall back to their vehicle window at uniform speed
  in the swing script, not to a forced wrong word.
- Noise rule only (not a clamp): an onset interval whose speed is
  >4x or <0.25x is merged with its neighbour (whisper short-word
  timing noise, e.g. S10 "Speed->up" 7x, S12 "Poor->folks" 11.8x
  from a 0.12s song interval — a glitch, not swing). All other
  speeds swing unclamped, e.g. S01 3.13 / 0.47 / 5.18, S05
  1.40 / 4.08 / 2.00, S20 1.83 / 1.80 / 1.52, S25 0.57 / 3.62 / 0.55.
- Assembly script: assemble_v3_swing.py (parses ok, full render
  launched in background 2026-11-02). Scene windows are derived
  from anchors (first anchor song - first anchor take, last anchor
  song end + tail), enforced monotonic, gaps filled with a hold
  of the previous clip's last frame, intro gap before S01 held
  on S01's first frame. Master encoding: fixed-audio form
  (AAC 48kHz stereo, +faststart), captions_v2.srt, ~ WuBu ~ bug.
  No v3 master claimed until the render finishes and line-start
  verification passes.

## 2026-11-02 ~04:05-04:20 EST — swing render: crash, fix, verify, deliver
- First swing run crashed on S27 (empty anchor list -> negative window ->
  `No such filter: ''`, concat=n=0, no master, no report). Second flaw in
  the same run: old window model let tails swallow next scenes (S16 squeezed
  to a 0.56 s flash).
- Fix (assemble_v3_swing.py rewritten): words land exactly on song times;
  scene start = max(raw start, previous last word end); scene end = next
  scene's start; S27 outro from S26 last word end 260.80, swept to 268.01.
- Second run rendered clean: master `masters/mv2_toll_roads_are_dumb_v3_16x9.mp4`,
  md5 a847810701b4e0d309f30b4b4752cdd4, 74,168,025 bytes, 268.041 s,
  h264 1280x720 24 fps + AAC 48 kHz stereo + 48 subtitle cues, moov byte 36.
- Verification: frame at every lyric line boundary (48 samples, first
  detected sung word at/after each boundary, from the master). PASS with
  disclosed nits — see CUTLIST_V3_SWING.md. Headline nit: chorus-1 opening
  word lands on S05's back-turned ticket raise; mapping verified exact, so
  it is take staging, not a slip. No text in any frame, bug in all frames,
  zero >=2 s audio silences.
- v3 is 16:9 only; no 9:16 cut built.

## 2026-11-02 ~05:30 EST — best cut (V4 rebuild): verified, delivered

- Triple devil's advocate audit (DEVILS_ADVOCATE_V4.md): S04 proven
  wrong-segment and S21 proven window-collapse on the leader-fixed
  master; S02/S03/S16 proven garble-softness, not misplacement; whisper
  zero-duration burst (song words 205.20 x7) proven as the S21 collapse
  mechanism; matcher fixed to LCS + zero-duration exclusion.
- Volley V4 (5/6 used, 6th deliberately unspent): S01 t4, S05 t4, S04 t4,
  S21 t2 all KEEP (QC + whisper + LCS in TAKE_HISTORY.md); S01 t3
  REJECTED (no "Yeah").
- Rebuild: `assemble_v3_swing.py` with ACTIVE S01=t4, S05=t4, S04=t4,
  S21=t2; WORD_MATCH_V3.json + CUTLIST_V3_SWING.json updated (backups
  `*.bak-v3`); render exit 0, all 27 scenes + S27 outro.
- Best-cut master: `masters/mv2_toll_roads_are_dumb_v3_16x9.mp4`,
  md5 e5dcfe3a598b989b6d021e3e702a50b4, 75,396,196 bytes, 268.01 s,
  h264 1280x720 24 fps, AAC 48 kHz stereo, mov_text, +faststart,
  6,426 video frames (267.75 s video vs 268.01 s audio — per-segment
  frame rounding, disclosed tail nit; outro tear + final smile verified
  present at 266.0 / 267.5).
- Word-matched verification (`masters_work_v3/audit_v5/`): first-anchor
  frames all 26 scenes, fastest-sweep strip, verify sheet — PASS with
  the disclosed nits listed in CUTLIST_V3_SWING.md (nits: S02/S03/S08/
  S12 staging, garbled/burst heads unanchored at natural speed, S05
  'are' noise-merge interpolation +0.08 s, 6-frame tail shortfall,
  structural 27-scene / 48-line tail holds, longest S14).
- This supersedes the leader-fixed master (md5 f1bc6a94bd8a5c8ecde59b396b8a0135),
  which was verified but never delivered. The best cut is the delivered
  MV-2 v3. 16:9 only; no 9:16 cut built.
- Pipeline self-improvement loop (user order 2026-11-02 05:22 EST) is
  still running as separate work (deep research agent); its findings
  fold into the pipeline after this delivery and do not block it.
