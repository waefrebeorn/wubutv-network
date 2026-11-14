# Cross-check sync method — video dictation vs song dictation, lyrics as context hint

Version 1, 2026-11-05. Companion: `SYNC_RESEARCH.md` (why each step
exists), `crosscheck_sync.py` (the prototype), `VALIDATION_RECUT_16x9.md`
(the re-cut scored by this method). Builds on the WORD-SYNC standard in
the Slopcannon skill (measure both sides, convert then place, warp never
freeze, gate on the master); it does not replace it — it replaces the
single unprompted Whisper pass the re-cut trusted with a reconciled
two-dictation measurement.

**Track-agnostic:** this spec applies to any song and any takes. MV-3
is the test bed it was built and validated on; it is also the assembly
standard for MV-4 "This Time It's Real (Futurama is cancelled)"
(238.8s, project `musicvideo/MV-4_this-time-its-real/`, in flight as of
2026-11-05 ~01:33 EST) and for future MV builds. Per-track inputs are
exactly four things, supplied fresh per project: the song dictation
(measured from that track's master audio), the performed lyrics text
(the hint), that track's mishear map (calibrated from its own
dictations — MV-3's game/dad, dogs/hooks classes do NOT carry over),
and that build's cutlist/placement table. Nothing else in the procedure
is track-specific: the alignment, scoring, gates, and verdicts are the
same. The prototype (`crosscheck_sync.py`) is MV-3-wired today (it
imports MV-3's scene table); a per-project adapter — scene table +
mishear map as inputs — is the defined next step before MV-4 assembly
consumes it, not a rebuild of the method.

## Law One — the song is the tempo gospel (user, 2026-11-05 ~01:30 EST)

"The song is the tempo gospel — everything syncs to the song." The
song's tempo and word times are the fixed, unmoving grid. The video
warps to the song, never the reverse. This governs every step below:

- No song-side shifting: a take's words are moved onto the song's word
  times; the song's word times are never moved onto a take.
- No song-side warping: the song is never time-stretched, squeezed, or
  re-timed to fit a take. The master audio is muxed untouched, always.
- No averaging the two dictations toward a middle tempo: when the video
  dictation and the song dictation disagree on tempo, the song wins
  outright. A compromise tempo is a second wrong tempo, not a sync.
- If a take cannot be warped to the song within the caps (0.80–1.25
  usable, grey to band edge only), it is cover / structural — never a
  reason to bend the song. A slot that cannot meet the gospel is a
  cover slot, and the ledger says so plainly.

Any method step, tool, or future stage that would move the song to fit
the picture violates Law One and is out — including any future
forced-alignment or DTW variant that re-times the reference. The
reference does not move.

## 0. Principle

Three independent sources, none trusted alone:

1. **Song dictation** — the song's performed words with times
   (`SONG_WORDS.json`, measured from the master audio). This is the
   timing authority.
2. **Video dictation** — the take's (or the master's picture-side
   placement's) performed words with times, transcribed from the take's
   own audio.
3. **Lyrics hint** — the known performed lyric text, fed to the decoder
   as `initial_prompt`. It biases decoding toward the known vocabulary;
   it cannot force words. Prompted and unprompted decodes are BOTH run
   and their delta is reported, so the hint's effect is measured, not
   assumed.

Where all three agree, sync is confirmed. Where they disagree, the
disagreement names the failure class. The output is an agreement LEDGER
per scene: agreed words (with per-word offset), missing song words
(coverage signal), extra take words (repeat/extra signal), and a
reconciliation verdict. A word in only one book is an unreconciled
entry, never a sync.

## 1. Inputs

| Input | Source | Rule |
|---|---|---|
| Song audio | `track.mp3` (md5 recorded, never re-encoded) | Sole timing authority |
| Song dictation | `SONG_WORDS.json` + `LYRIC_TIMELINE.md` (performed words, not the sheet) | Re-measured if the track is re-delivered; the old grid is void |
| Performed lyrics text | `LYRIC_TIMELINE.md` line table (performed text) | The hint. The abridged sheet (`lyrics.txt`) is NEVER the hint where it differs from the performance |
| Take audio | `takes/mv3_s<kk>_t<t>.mp4` | Extract wav with ffmpeg (mono 16k); per-take temp wav, deleted after; never share a temp wav between runs; transcribe sequentially |
| Placement | `assemble_mv3_recut.py` SCENES table (scene start, per-piece warp `w`, trim start `s`) — or the current cutlist's equivalent | Import the table, never retype it; placement math is `master = scene_start + (take_t − s) × w`, accumulating across pieces |
| Mishear map | MV-3 classes: game→dad, dogs→hooks, see→say, face→phrase, done→dumb (plus MV-2's told/tall/toe→toll, paid→pay, tell→sell where the track uses them) | Apply to BOTH sides equally, before matching; record the map version in the report. A mishear is a decoding artifact, not a lyric difference |

## 2. Procedure (step by step)

### Stage 1 — Dictate both sides, twice where it matters
1a. Song side: transcribe the full song audio with the full performed
lyrics as `initial_prompt`. Keep the unprompted song dictation too
(`SONG_WORDS.json` already is one). Compare prompted vs unprompted:
agreement rate + which words changed. If the prompt changed nothing,
the hint is decoration on this track — say so.
1b. Take side: for each take in the cut, transcribe twice — once
unprompted, once with that scene's performed line as `initial_prompt`.
Report both. The delta (words gained/lost, times shifted) is the
decoder-uncertainty measurement for that take.
1c. Split-half recheck (MV-2 rule, kept): a zero-word full-clip decode
is NOT a no-line verdict — re-transcribe the 0–5s half before calling
a take lineless. Quiet-burst takes get a slice re-transcription with
the offset added back (re-cut precedent: 8 takes).

### Stage 2 — Normalize, then align tokens (not slots)
2a. Normalize both word lists: lowercase, strip punctuation, apply the
mishear map. Keep the raw words alongside for audit.
2b. (Coarse check) Vocal-envelope / onset cross-correlation between take
audio and song audio inside the scene window, as a sanity check on the
token alignment's first-word offset. If envelope lag and word lag
disagree by >0.5s, flag the scene DOUBT — do not average the two
numbers. This is the independent check for garbled windows (S11/S13/
S14 class) where token identity is unreliable.
2c. Align the take's normalized token sequence against the song window's
normalized token sequence (song words with start in [scene_start,
scene_end)) with a monotonic sequence alignment (difflib SequenceMatcher
in the prototype; DTW on the token index axis is the equivalent formal
statement). Record opcodes: equal / replace / delete (song word missing
in take) / insert (take word with no song counterpart). Position is
part of the match: in mantra blocks, identical tokens recur, so a match
is only credited to the occurrence whose time is nearest the song
occurrence — a token matched to the wrong repeat is a mismatch, not a
match. Implemented as the wrong-repeat test: a matched pair more than
2.0s apart is dropped ONLY when an unmatched occurrence of the same
token exists within 0.5s of the take word's placed time; otherwise the
pair is kept as real timing error (a take tail genuinely ending 2–3s
early must stay visible — a blanket >2s drop hides it, as a first
version of this filter did on S23/S28 before it was caught and fixed).
2d. Exclude from offset statistics (but count and report): song words
with zero duration (Whisper pile-up stamps, e.g. the 282.18 block),
take words falling outside every cutlist piece span (tail-loop region),
and words in instrumental windows. Exclusion is never silent.

### Stage 3 — Place, then score per word
3a. Map each matched take word into master time with the placement
formula (§1). No global shift is ever applied: the offset series IS the
measurement. Only the take side moves — Law One: the song's word times
are never shifted, warped, or averaged toward the take.
3b. Per matched word with usable time on both sides: offset = take word
start (placed) − song word start. Report per scene:
- agreement = matched / song words in window
- median |offset|, max |offset|, mean offset (sign shows early/late bias)
- drift = last-word offset − first-word offset (tempo drift, the MV-3
  diagnosed cause — a drift near zero with large median offset is a
  shift; a drift near the max offset is tempo)
- tolerance buckets: % matched within ±0.125s (perceptual tier), ±0.25s,
  ±0.50s, ±1.00s (working tiers)
- missing song words (coverage signal) and extra take words
  (repeat/extra signal), listed by word and time
3c. Phrasing-gap detection (the re-cut's second failure class): if
mid-line offsets exceed both endpoints' offsets by >0.5s (a "hump"),
flag PHRASING GAP with the hump's words and magnitude. No whole-clip or
per-word warp within 0.80–1.25 can fix a pause in the wrong place —
the flag is the verdict, not a prompt for more warping.

### Stage 4 — Gate on the master (the WORD-SYNC gate, now cross-checked)
4a. Run stages 1–3 for every mouth scene from the take dictations +
cutlist placement (the prototype's `placement` mode), AND transcribe
the delivered master's audio with the full-lyrics prompt and align it
to the song dictation (the prototype's `master` mode). The master-audio
check bounds dictation instability (same audio both sides); the
placement check scores the picture. Both numbers are reported; neither
substitutes for the other.
4b. Picture-motion spot check: at each scene's first song-word time,
confirm the master frame differs from the frame 0.5s earlier
(mean abs diff > 0.5 at 160×90). Moving picture is necessary, not
sufficient, for mouth sync — it rules out frozen coverage and nothing
more. A STILL at a word time fails the scene regardless of its offset
score.
4c. Verdicts per scene (in order):
- **SYNCED** — agreement ≥0.9 AND median |offset| ≤0.125s AND max
  |offset| ≤0.25s AND no phrasing hump >0.5s AND picture moving.
  (Perceptual tier. Expect this to be rare on prompt-only takes; that
  is the honest result, not a failure of the method.)
- **WORKING SYNC** — agreement ≥0.9 AND median |offset| ≤0.25s AND max
  |offset| ≤0.50s AND no hump >0.5s AND picture moving. Ships as
  measured placement with the numbers disclosed.
- **GREY / DISCLOSED** — endpoints land within the warp caps but
  median or max offset exceeds the working tier, or a phrasing hump
  exists. Ships only with the residual disclosed (end residual + worst
  mid-line offset + hump words). This is where most MV-3 grey scenes
  land.
- **COVER** — agreement <0.7, or a coverage gap (song words with no
  take counterpart spanning >1s), or ratio outside [0.60, 1.60], or
  picture still at word time. No mouth claim; montage/cutaway/reaction
  cover with captions keyed to song times and the row flagged
  "not a mouth-sung slot".
- **DOUBT** — token alignment and envelope check disagree by >0.5s, or
  prompted/unprompted dictations disagree on >20% of the scene's words.
  Do not ship on a DOUBT verdict — re-measure (slice re-transcription,
  ear check on first/last words) before any verdict.
4d. Whole-master verdict: the master holds word-sync only if every
mouth scene is SYNCED or WORKING SYNC, or every other scene is a
disclosed GREY / flagged COVER. One undisclosed grey scene fails the
master. The verdict is published with the per-scene ledger, never as a
single number.

## 3. Failure modes (what each one looks like in the ledger)

| Failure | Ledger signature | Assembly response |
|---|---|---|
| Tempo drift (diagnosed MV-3 cause) | Offsets grow monotonically across the line; drift ≈ max offset; endpoints fixable by warp | Whole-clip warp within caps; re-score after warp |
| Phrasing gap | Mid-line hump: offsets spike mid-line, endpoints near zero | No warp fixes it; disclose, or re-fire the take sung to the song's phrasing, or cover |
| Coverage gap (S39 class) | Song words missing in a contiguous run >1s; take ends early | Montage cover; no sync claim; captions stay song-timed |
| Mantra pile-up | Dozens of song words at one timestamp; agreement inflated, offsets meaningless | Exclude zero-duration words; score the block by span + burst count, never per-word |
| Mishear class | Systematic substitution (game/dad) on one or both sides | Mishear map; if a NEW systematic substitution appears, extend the map and re-run — never hand-edit a single word |
| Dropped quiet burst | Take words missing in the tail; slice re-transcription recovers them | Slice re-transcribe before verdict; a full-clip-only decode never closes a take |
| Long first-word stamp | First offset large, words 2+ clean (S10 class) | Re-measure the first word from visual + acoustic evidence (mouth state + RMS jump) before trusting the stamp |
| Prompt false-agreement | Prompted decode gains words the unprompted decode lacks AND the audio does not support (ear check) | DOUBT verdict; the prompt is a prior, not evidence — unprompted agreement is the floor |
| Frozen picture at word time | Motion spot check fails | FAIL regardless of offset score; re-cut the cover |
| Wrong-repeat match (mantra) | High agreement but offsets scatter ±seconds with no drift structure | Position-constrained matching (§2c); if it cannot be resolved, score by span only and flag |

## 4. What this method deliberately does NOT do

- It does not generate or repaint anything. It measures.
- It does not move the song. Law One: no song-side shifting, warping,
  or tempo averaging, in this method or any future stage of it.
- It does not use MFA, WhisperX, a phoneme model, a vocal separator,
  or an LLM ensemble. Those are stage-4 future work (see §5), each
  gated on evidence, none assumed.
- It does not claim phoneme accuracy, broadcast tolerance, or
  lip-sync. Its claim is exactly: "these words, at these times, agree
  or disagree by this much, by two independent decodes reconciled
  against the known lyrics."
- It does not average away disagreement. A disagreement is a line in
  the ledger, not noise to smooth.

## 5. Future stages (gated, not started)

- **Stage 4a — WhisperX / wav2vec2 phoneme alignment**: adopt only if
  the word-level cross-check passes its own gate on 3+ scenes AND a
  phoneme pass changes a scene verdict on measured data. Requires a
  second model download; singing accuracy must be measured on MV-3
  takes first, not assumed from speech benchmarks.
- **Stage 4b — Vocal separation before alignment**: adopt only if a
  separator demonstrably raises take agreement on the noisiest takes
  without changing the song side. New dependency; zero-spend constraint
  applies until the user approves otherwise.
- **Stage 4c — MFA with a singing-trained model**: adopt only if a
  singing acoustic model is available on disk; the off-the-shelf speech
  model is measured poor on singing and is not used.
- **Stage 4d — Envelope/onset DTW as a scored stage**: promote §2b from
  sanity check to scored stage once it has agreed with token alignment
  on 10+ scenes.
- **Never**: audio-driven repaint as the sync answer without the user's
  go-ahead on modality/spend. That is a different project, not a next
  stage of this method.
