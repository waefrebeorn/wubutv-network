# Sync research — cross-check lyric timing for WuBu music videos

Date: 2026-11-05. Test bed: MV-3 "I Am Your Dad (HE IS NOT YOUR DAD, RUN)".
Ordered by the user 2026-11-05 ~01:20 EST: research and develop better
syncing techniques — video dictation synced to song dictation, lyrics as
the context hint, a cross-check system. Kevin Bacon associative research
+ online research. Adapt mechanics only, never copy licensed material,
lines, or code verbatim (SLERM-style rebuilds).

Companion files in this dir (`recut_work/sync_proto/`):
`CROSSCHECK_SYNC_METHOD.md` (the method spec), `crosscheck_sync.py`
(the prototype), `take_crosscheck.json`, `placement_crosscheck.json`,
`master_dictation_report.json`, `master_motion_spotcheck.json`,
`VALIDATION_RECUT_16x9.md` (validation of the delivered re-cut master).

## 0. The problem, stated exactly

First law (user, 2026-11-05 ~01:30 EST): "the song is the tempo
gospel — everything syncs to the song." The song's tempo and word times
are the fixed, unmoving grid; the video warps to the song, never the
reverse — no song-side shifting, no song-side warping, no averaging the
two dictations toward a middle tempo. If a take cannot be warped to the
song within caps, it is cover/structural, never a reason to bend the
song. This is Law One of `CROSSCHECK_SYNC_METHOD.md` and it governs
every measurement in this report: the song dictation is the reference
that does not move, and every offset is measured against it.

The generator is prompt-only: no audio input, no word timings, no
lip-sync parameter. Sync is therefore an ASSEMBLY-side conversion problem,
not a generation problem. The WORD-SYNC standard (Slopcannon skill) already
says: measure both sides, convert then place, warp never freeze, gate on
the master. What was missing was the *cross-check*: the re-cut measured
each take once (one Whisper pass, unprompted) and trusted that single
dictation. A single dictation has no way to say "I am unsure here" — its
errors (mishears, pile-ups, dropped quiet bursts, long first-word stamps)
become assembly facts. The user's idea fixes that structurally: two
independent dictations (video side, song side) plus the known lyrics as a
third, independent constraint. Where all three agree, sync is confirmed.
Where they disagree, the disagreement IS the measurement — it names the
failure class (mishear, drift, phrasing gap, coverage gap) instead of
hiding it inside a warp factor.

MV-3's real numbers bound the problem: 729 song words over 354.8s;
mantra repeats ("I am your dad" ~100x) make token identity nearly
useless without position; takes drift by tempo up to ~1.8s (not a global
shift); S39 is a coverage gap (one mantra sung, ~6s of song repeats
uncovered); phrasing gaps in S01/S27/S34/S36 put mid-line words 1–2s off
even with endpoints exact. Any method that cannot see a phrasing gap or
a coverage gap is not a sync method for this material.

## 1. Kevin Bacon chains (association = warm-up input only)

Method as the production wheel runs it: solo-first, chains capped at 3
hops then a forced jump, hop 2 must cross category, one blind random
input per run that must appear in at least one finding, a ban list, no
endpoint recycling, separate novelty+usability pass before adoption.

Blind random input (drawn with `shuf` from /usr/share/dict/words,
2026-11-05): **"ledger"**. It lands in Chain 3 and in the method itself:
the cross-check's output is a per-word agreement LEDGER — two books
(video dictation, song dictation) that must reconcile, with every
disagreement carried as an open line, exactly like double-entry
bookkeeping. A word that appears in only one book is not a sync; it is
an unreconciled entry, and the method reports it as such.

Ban list (previous findings + last runs' categories): Whisper-only word
timestamps as a sole source (the re-cut's single-pass method — this run
must improve on it, not repeat it); whole-clip setpts warp as the only
placement move (already the re-cut's fix); peak-tween (banned forever);
audio-driven repaint tools as the answer (out of scope — needs user
go-ahead on modality/spend); any technique requiring a GPU, a cloud
service, or a new paid account (zero-spend constraint).

Chain 1 — forced alignment → karaoke captions → broadcast lip-sync law.
Start: Montreal Forced Aligner (speech tech). Hop 1: karaoke caption
timing, where a word must light up within a frame of its sung onset or
the room notices. Hop 2 (crosses category, speech tech → broadcast
standards): ITU-R BT.1359-1 / EBU R37 lip-sync tolerances. Forced jump:
broadcast law gives the numbers the karaoke intuition only felt — see §3.

Chain 2 — cover-song DTW → DNA sequence alignment → subtitle timing.
Start: chroma/MFCC dynamic time warping for cover-song identification
(MIR). Hop 1: sequence alignment in bioinformatics — same DP, different
alphabet (bases instead of chroma vectors); the lesson is that alignment
scoring must be explicit about gaps and substitutions, not just distance.
Hop 2 (crosses category, MIR → subtitling practice): subtitle timing,
where the unit is the word and the failure is a word shown early/late.
Forced jump: the alignment object for MV work is the WORD SEQUENCE with
times attached, and the score must separate "wrong word" (substitution)
from "missing word" (gap) from "right word, wrong time" (offset) — three
different failure classes needing three different assembly responses.

Chain 3 — LyricWhiz LLM ensembling → double-entry ledger → court
stenography. Start: LyricWhiz (Whisper as ear, LLM as brain, ensembling
multiple transcriptions against the lyric context). Hop 1: the blind
input "ledger" — double-entry bookkeeping, where two independently kept
books must reconcile and every discrepancy is itself the audit finding.
Hop 2 (crosses category, ML ensembling → legal record-keeping): court
stenography verification, where a transcript is certified by a second
independent read and disagreements are flagged, never silently resolved.
Forced jump: the cross-check is an AUDIT, not a transcription — its
output is a reconciliation report (agreed / disagreed / missing /
extra), and the assembly decision follows the reconciliation, not the
raw transcript.

Chain 4 — Whisper initial_prompt → context priming in LLMs → karaoke
prompt sheets. Start: Whisper's initial_prompt parameter (a text hint
biasing the decoder). Hop 1: context priming generally — a model given
the answer's vocabulary decodes toward it, which is a bias to measure,
not a force to trust. Hop 2 (crosses category, ASR → live performance):
the karaoke prompt sheet — the singer sees the next line before singing
it, and the prompter's job is to keep the singer on the line, not to
sing it for them. Forced jump: the lyrics hint must be treated as a
PRIOR with a measurable effect (prompted vs unprompted agreement), and
the prototype measures exactly that — if the prompt changed nothing,
the hint is decoration; if it changed the words, the change itself is
data about decoder uncertainty.

## 2. What the literature and docs actually say

### 2.1 Forced alignment: MFA vs WhisperX vs raw Whisper word timestamps
- The Montreal Forced Aligner (Kaldi GMM-HMM) takes a KNOWN transcript
  and returns word/phone times. On hand-aligned TIMIT/Buckeye, Rousso et
  al. (2024) report MFA placing 72.8% of word boundaries within 25 ms
  (MAE 21.9 ms), vs WhisperX 52.7% (MAE 34.3 ms) and MMS 43.5% — MFA
  leads at every tolerance on both corpora, scoring only words correctly
  recognized, so transcription errors do not explain the gap.
  (arxiv.org/html/2406.19363v1; speechdata.ai/blog/forced-alignment-speech-data)
- WhisperX (Bain et al. 2023) adds VAD + wav2vec2 CTC phoneme forced
  alignment on top of Whisper: 93.2% vs 85.4% precision on telephone
  speech at a 200 ms tolerance. Its word times are tens-of-ms accurate
  on supported languages, at the cost of a second model and pipeline
  glue. (forasoft.com WhisperX guide; emergentmind.com/topics/whisperx)
- Raw Whisper / faster-whisper `word_timestamps=True` derives word times
  from attention weights, not from aligning to the sound. Rules of thumb
  put it usually under 200 ms on clean speech, worse after silence —
  and Whisper's own timestamps "can be inaccurate by several seconds"
  (WhisperX README, quoted in the same guides). MV-3's own data proves
  the failure modes on singing: zero-duration pile-ups (dozens of mantra
  repeats stamped at 282.18), long first-word stamps (S10 take "i"
  0–1.22s vs song 0–0.14s), dropped quiet bursts (8 takes needed slice
  re-transcription).
- A 2024 singing-specific test of open-source MFA found only 10.08% of
  samples above 80% recognition accuracy on singing audio — the
  off-the-shelf speech model is poor on sung voice until retrained on
  singing data (drpress.org JCEIM 2024). MFA is therefore NOT a
  drop-in for MV-3: it needs a singing-trained acoustic model we do not
  have, and installing/training one is out of scope for a zero-spend
  prototype. Its lesson survives instead as a design principle: a known
  transcript + an acoustic aligner beats a free transcription + attention
  timestamps, and the transcript we have (the performed lyrics) should
  constrain the alignment rather than merely prompt the decoder.
- Newest work (Scicom "Where Words Begin and End", Oct 2026, arxiv
  2610.17782) fine-tunes Whisper with LoRA to predict word starts/ends
  as timestamp tokens, reaching 11.6 ms boundary error on TIMIT vs
  18.2 ms for the best published system — but that is a trained model
  we do not have, not a tool we can run. Noted for the record, not adopted.

### 2.2 Lyrics-constrained transcription (the lyrics as context hint)
- LyricWhiz (arXiv 2306.17103): Whisper transcribes multiple times with
  language-specific prompts, then an LLM ensembles and corrects against
  lyric context — state-of-the-art zero-shot lyrics transcription, big
  WER reductions on English ALT benchmarks. Mechanism that transfers:
  prompt the decoder with the lyric context, then reconcile multiple
  decodes instead of trusting one. Mechanism that does NOT transfer
  as-is: the LLM ensembling step (needs an LLM call per take; the
  prototype replaces it with deterministic token alignment + the
  mishear map, which is free and auditable).
- Whisper's `initial_prompt` is a decoder bias, not a constraint: it
  raises the probability of prompted words but cannot force them, and
  it can also bias the decoder TOWARD the prompt when the audio says
  something else (a false-agreement risk the prototype must measure by
  running prompted vs unprompted on the same take and reporting the
  delta — Chain 4's point).
- The honest ceiling: no prompt makes Whisper a forced aligner. The
  prompt narrows the vocabulary; the times still come from attention.
  So the lyrics hint improves WORD IDENTITY (fewer mishears) more than
  it improves WORD TIME. The prototype's numbers confirm which of the
  two moved (see §5).

### 2.3 DTW audio alignment (MFCC/chroma)
- Cover-song identification aligns two performances of the same piece
  with DTW over chroma or MFCC sequences (Ellis & Poliner; Bertin-Mahieux
  & Ellis 2012; Serrà et al. 2008). Chroma captures harmony (key- and
  tempo-tolerant); MFCC captures timbre. A Nokia patent (US9892758B2)
  describes exactly the lag-search variant: correlate MFCC/chroma frames
  across lags, take the best lag as the alignment.
- Verdict for MV-3: DTW over audio features is the WRONG primary tool
  here, for a specific reason — the two sides are not two performances
  of the same audio. The take's audio is a different voice, different
  timbre, different room, singing a different slice of the song at a
  different tempo, over a different backing. MFCC-DTW would align
  timbre/energy, not words, and chroma-DTW would align harmony, which
  the take's generated backing does not share with the song. DTW's
  surviving role is narrow and real: COARSE alignment — a lag search on
  the vocal-envelope / onset cross-correlation between take audio and
  song audio inside a scene window, as a sanity check on the
  token-alignment's first-word offset (if envelope lag and word lag
  disagree by >0.5s, one of them is wrong and the scene gets flagged,
  not averaged). Envelope/onset correlation is cheap (numpy only) and
  is specified in the method doc as stage 2b; it was not needed for the
  prototype's headline numbers because token alignment already
  constrains the window, but it is the correct independent check when
  token alignment fails (garbled song window, e.g. S11/S13/S14).
- DTW over WORD TIMES (not audio) is a different, adopted idea: once
  both sides are word sequences with times, a monotonic alignment with
  a slope constraint is exactly DTW on the time axis — and that is what
  the prototype's placement + offset series already computes (first-word
  offset, last-word offset, drift). The warping path IS the drift curve.

### 2.4 Phoneme-level alignment
- The alignment literature converges on phonemes as the unit that
  actually times singing (LyricAlly 2004; Fujihara et al. lyrics-to-audio
  alignment: phoneme network + Viterbi over a dominant-vocal signal,
  with vocal/non-vocal section estimation because non-vocal sections
  destroy alignment accuracy). Word times are aggregates of phoneme
  times; when Whisper stamps a whole word at one instant, the phoneme
  inside it that carries the onset (usually the first consonant/vowel)
  is what the ear actually syncs to.
- Verdict: phoneme alignment is the correct NEXT step, not this step.
  It needs either MFA-with-singing-model (unavailable, §2.1) or a CTC
  phoneme model (WhisperX's wav2vec2 aligner — installable but a second
  model download + pipeline glue, and its singing accuracy is
  unmeasured on this material). The prototype's word-level cross-check
  is the floor phoneme work stands on: if word agreement is low or
  offsets are wild, phoneme refinement refines noise. The method doc
  specifies phoneme alignment as stage 4 (gated: adopt only after the
  word-level cross-check passes its own gate on 3+ scenes).

### 2.5 How sync is MEASURED (perceptual tolerances)
- ITU-R BT.1359-1 (expert viewers, controlled tests): detectability
  +45 ms (audio leads video) to −125 ms (audio lags); acceptability
  +90 ms to −185 ms. Viewers notice early sound sooner than late sound.
- EBU R37: end-to-end +40/−60 ms; ATSC: audio lead ≤15 ms, lag ≤45 ms
  at the encoder. Film practice: ±22 ms (half a frame at 24 fps).
  (en.wikipedia.org/wiki/Audio-to-video_synchrony; versely.studio
  lip-sync tolerance guide)
- Plain-language reading: below ~45 ms lead / ~125 ms lag, expert
  viewers cannot reliably detect a sync error; below ~20 ms nobody can.
  A 1-frame (41.7 ms) error at 24 fps sits exactly on the detectability
  edge. MV-3's warp residuals (0.27–0.50s on the best usable scenes,
  1–2s mid-line on phrasing-gap scenes) are 6–50x the detectability
  threshold. This is why the user's playback verdict was categorical:
  the re-cut's best scenes are still an order of magnitude outside
  broadcast tolerance, and the honest claim for them is "words land in
  the right order at roughly the right time", never "in sync" in the
  broadcast sense. The method doc's gates are therefore set in two
  tiers: a PERCEPTUAL tier (±0.125s, inside detectability for lag and
  near it for lead) that almost nothing in MV-3 meets, and a WORKING
  tier (±0.25s / ±0.50s) that separates usable takes from cover slots.
  Reporting both tiers honestly is the point of the cross-check; hiding
  the perceptual tier would be repeating the v5 mistake (passing
  internal checks, failing on playback).

### 2.6 Lyrics-to-audio alignment literature (singing-specific)
- The field's standard pipeline (Fujihara/Goto; LyricAlly; later
  HMM/CTC variants): extract the dominant vocal, estimate vocal vs
  non-vocal sections, build a phoneme network from the lyrics, Viterbi
  align. Two findings transfer directly: (1) non-vocal sections must be
  excluded BEFORE alignment or they corrupt it — MV-3's analogue is
  excluding pile-up/zero-duration words and instrumental windows from
  offset stats (the prototype does this); (2) singing-adapted acoustic
  models beat speech models by a wide margin — MV-3's analogue is the
  mishear map (game/dad, dogs/hooks, see/say), which is a poor man's
  domain adaptation, documented as such and never hidden.
- Word-level lyrics-audio sync with separated vocals (ResearchGate,
  2017) adds: separate the vocal first, then align. MV-3 cannot
  separate the take's vocal from its generated backing with on-disk
  tools (no separator installed, and installing one is a new dependency,
  not a zero-spend move) — noted as a future stage, gated on the same
  evidence bar as phoneme alignment.

## 3. Novelty + usability pass (what survives for THIS problem)

| Technique | Novel? | Usable here? | Verdict |
|---|---|---|---|
| Lyrics as Whisper initial_prompt, prompted-vs-unprompted delta measured | Yes — re-cut used one unprompted pass only | Yes — free, same venv, same model | ADOPTED (prototype stage 1) |
| Two independent dictations + token alignment + mishear map | Yes — the user's cross-check idea itself | Yes — pure Python, deterministic | ADOPTED (prototype core) |
| Per-word offset + drift + tolerance buckets (not slot ratio) | Yes — replaces span ratio as the sync score | Yes — computed from existing measure JSONs | ADOPTED (prototype stage 3) |
| Agreement ledger: agreed/missing/extra per word, per scene | Yes — Chain 3's ledger, the blind input's contribution | Yes — the report format itself | ADOPTED |
| Envelope/onset cross-correlation as coarse check | Known technique, new role here | Yes — numpy only, no new deps | ADOPTED as stage 2b (spec only; prototype flags where token alignment needs it) |
| MFA forced alignment | Known, not novel here | No — speech model poor on singing (10% >80% acc.); no singing model on disk | REJECTED for now; principle kept (known transcript should constrain alignment) |
| WhisperX wav2vec2 phoneme alignment | Known | Partial — needs a second model download + glue; singing accuracy unmeasured | DEFERRED to stage 4, gated |
| MFCC/chroma DTW between take and song audio | Known | No as primary — aligns timbre/harmony, not words, across different voices/backings | REJECTED as primary; DTW-on-word-times adopted instead |
| Phoneme-level alignment | Known | Not yet — needs a model we do not have | DEFERRED to stage 4, gated |
| Vocal separation before alignment | Known | No — no separator on disk; new dependency | DEFERRED, gated |
| Audio-driven repaint (MuseTalk/LatentSync etc.) | Known | Out of scope — needs user go-ahead on modality/spend | EXCLUDED by task scope |
| LLM ensembling of decodes (LyricWhiz-style) | Known | No — needs an LLM call per take; replaced by deterministic alignment + mishear map | REJECTED; mechanism adapted, step not copied |

## 4. What the prototype is (and is not)

Built: `crosscheck_sync.py` — song dictation + take dictation (prompted
and unprompted) + lyrics-constrained token alignment + per-word
offset/drift report + all-scene placement cross-check from the existing
measure JSONs + master-audio dictation stability check + picture-motion
spot check on the delivered master. Runs on the existing fw-venv +
ffmpeg, zero spend, read-only on masters.

Not built (deliberately): no new model, no forced aligner install, no
vocal separator, no repaint, no video generation, no re-encoding of any
master. The prototype measures sync; it does not manufacture it.

Note (2026-11-05 ~01:33 EST): MV-4 "This Time It's Real (Futurama is
cancelled)" (238.8s) is in flight, and this method is its assembly
standard too — see the track-agnostic note at the top of
`CROSSCHECK_SYNC_METHOD.md`. The MV-3 retimed 16:9 remains the first
deliverable; MV-4 assembly consumes the method next, with a per-project
adapter (scene table + mishear map as inputs) as the defined next step
for the prototype.

## 5. Prototype results (measured 2026-11-05)

Full numbers: `VALIDATION_RECUT_16x9.md`, `take_crosscheck.json`,
`placement_crosscheck.json`, `master_motion_spotcheck.json`.

- **Take cross-check (3 takes, prompted vs unprompted):** the lyrics
  hint changed almost nothing — same word counts, same agreement,
  offsets shifted ≤0.07s. S06 (cleanest): agreement 0.957, median
  |off| 0.08s, max 0.27s. S01: median 1.15s (phrasing gap reproduced
  exactly: "all" +1.42s). S27: median 0.96s (mid-line hump to +1.40s
  reproduced). The hint's value on this material is confirmation, not
  correction — and the independent re-measurement landing on the same
  numbers as the re-cut's single pass is itself the cross-check working.
- **Placement cross-check (all 31 mouth scenes):** 7 WORKING SYNC, 17
  GREY/disclosed, 6 COVER, 1 DOUBT (S14, garbled song window). No scene
  meets the perceptual tier (±0.125s median / ±0.25s max); best is S06
  (0.08s / 0.27s). Sharpest correction vs span analysis: S13 was
  "span-usable" in the re-cut but scores median 1.77s per-word with 0/13
  words within 0.25s — span-usable ≠ word-synced.
- **Picture motion:** 31/31 mouth scenes moving at their first
  song-word time (S01 borderline 0.85 = the disclosed leader hold).
- **Warp fit → retime:** 3 of 31 scenes improve under a least-squares
  warp within caps (S16, S18, S34); S27/S28 fits rejected by the
  end/max guards — the fit is not allowed to trade the ending for the
  middle. The retimed 16:9 master is built from exactly those three
  warp changes; everything else is the re-cut.
- **Master-audio dictation stability (identical audio, two passes):**
  agreement 0.675 (585 vs 729 words — the prompted pass drops ~144
  mantra repeats), median |offset| 0.02s, 387/459 usable pairs within
  ±0.25s, one unresolved 21.1s wrong-repeat outlier out of 459 pairs.
  Timing is stable; identity is not. This sets the method's agreement
  ceiling (~0.68) on mantra-dense material. A wrong-repeat filter was
  added and corrected during this check (a dumber first version hid
  real tail error in S23/S28 and was reverted — see validation §2).
