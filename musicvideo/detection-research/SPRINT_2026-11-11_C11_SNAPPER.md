# Sprint 5 — C11 word-time snapper (forced-aligner substitute) — 2026-11-11

Sprint 5 under the standing SLERM-C11 method (user msg 214), the
msg-227 survey (rank #2: the classical substitute for Qwen3-
ForcedAligner / WhisperX alignment), the msg-202 downtime-
improvement directive, and the msg-237 coding spree. The tool answers
the same question a forced aligner answers — "when exactly was this
word sung?" — from acoustic evidence the pipeline already computes
(spectral flux), with no neural model anywhere.

**Recovery note (read first).** The first sprint-5 coordinator
(fd0351c5, spawned ~21:40 EST) died at 22:08:44 EST on a runtime
transport error (`[transport] sqlx error: pool timed out while
waiting for an open connection`) — the same second that killed the
MV-14 volley-10 probe coordinator and the sprint-7 coordinator.
Its brief said "no files on disk", but the disk said otherwise: by
22:04 EST it had vendored slermes libjson (21:47), written the full
snap mode into `c11_mir.c` (~370 lines), updated the Makefile,
rebuilt both binaries, and run two full lambda sweeps (21:59 and
22:04, in `/tmp/snap*.json` / `/tmp/snap2_*.json`). What it never
wrote was the report. This sprint is a RECOVERY: it verified the
inherited code from scratch (clean rebuild, byte-diff of the LEGO,
regression, determinism, fresh validation runs), ran the validation
the first build never finished, and wrote this report. Nothing of
the first build's code was taken on trust; everything below was
re-measured here.

## What was built

`snap` mode in `detection-research/c11_mir/c11_mir.c` — an extension
of the c11_mir tool (a mode, not a fork), sharing the sprint-3/4
STFT front end (periodic Hann 1024/256, centred frames, 16 kHz mono)
and the sprint-3 Ellis-DP shape (per-state cost + predecessor +
backtrack), but NOT a copy of the beat tracker: states are candidate
frames per word, transitions are non-decreasing in frame (words
never cross), and the cost is

    lambda * |t_candidate - t_asr| + onset_cost(flux[candidate])

with a TIERED onset cost: 0 for a strong peak (flux >= 0.20),
0.5 for a weak peak (flux >= 0.05), 1.0 for not a peak at all (the
"stay" candidate — the ASR frame itself, always available, so a word
with no peak nearby simply does not move).

Two flux flavours: `mix` (full-band flux, as dumped by beats mode)
and `vocal` (flux restricted to 300–3400 Hz — suppresses kick/hat
bleed so the DP sees voice onsets first). A "gap" is measured on the
vocal-band ENERGY envelope (300–3400 Hz, `band_energy`), not on
flux: flux measures change, not presence — a sustained vowel has
high energy and near-zero flux, and the mix flux stays high on
drums between phrases. A gap is a 5-frame mean band energy below
0.05. (That threshold turned out to be miscalibrated — see
§"The gap test is invalid as shipped" below. The tool is sound;
the diagnostic threshold is not.)

Usage:

    ./c11_mir snap mv14_16k.wav SONG_WORDS.json snap_vocal_mv14.json \
        --flux vocal --window 0.4 --lambda 2.0

`SONG_WORDS.json` is `{"words": [{"word","start","end","prob"}]}`
(faster-whisper large-v3-turbo, no VAD). Output JSON carries
per-word `snapped_start`, `correction_s`, `on_peak`,
`flux_at_snapped`, `flux_at_asr`, `gap_asr`, `gap_snapped`, plus
summary counts (`n_moved`, `median_abs_correction_s`,
`n_gap_asr`/`n_gap_snapped`, `n_on_peak`). Runtime ~0.5 s on the
161.6 s MV-14 track (1.5 shared CPUs).

## LEGO vs fresh (msg-233 rule — surveyed all 9 repos)

The first coordinator cloned 8 of the 9 user repos to `/tmp/lego`
(plfm_radar's clone failed on a full `/tmp`; this sprint checked it
via the GitHub API instead — it is a 10.5 GHz phased-array RADAR
system, 85 MB, whose only FFT content is an FPGA Verilog FFT core
and a Python ramp script: nothing audio-reusable). Greps for
`viterbi|dynamic programming|forward-backward|onset` across all
nine found NO dynamic-programming / Viterbi module anywhere.

| Component | Source | Verdict |
|---|---|---|
| JSON parsing (`json.c`/`json.h`, ~1000 lines) | slermes `lib/libjson` | LEGO — vendored verbatim. Verified here by byte-diff against upstream `main`: `json.h` identical; `json.c` differs ONLY by the LEGO note + `_POSIX_C_SOURCE` + `<strings.h>` (strcasecmp declaration, zero warnings). No logic changed. |
| STFT / flux front end | c11_mir core (sprints 3–4, our own prior work) | REUSED — already validated (flux corr 1.0000 vs scipy). BearRL's `wubu_stft` was considered and NOT used: swapping front ends would void the sprint-3/4 validation for zero gain. |
| DP lattice, tiered cost, candidate peaks, band flux/energy, gap test, word I/O (~370 lines added to `c11_mir.c`) | Fresh | No existing module does this in any surveyed repo. Written from scratch in C11. |
| plfm_radar | RF radar hardware | Nothing applicable (see above). |
| distiller-c11, money-room, Mini-GLM5.2, grahaos_audit, coope_audit, quantum_rng_audit | — | No DP / Viterbi / onset / STFT module found. |

## Design decisions (and the one the first build got wrong)

- **Tiered cost, not graded.** The first build used a graded
  `-log(flux)` onset term. It over-snaps: it chases the strongest
  peak in the window even from a decent onset — 209/212 words
  moved, median correction 0.160–0.175 s (sweep `snap_*_l0.5/l1`,
  21:59). The rebuild replaced it with the tiered cost above,
  which implements the brief literally: snap to the NEAREST strong
  onset; a word already on a peak stays. Second sweep (`snap2_*`,
  22:04): 162–167/212 moved at lambda 2.0, median 0.052–0.056 s.
- **Two flux flavours, one default.** `vocal` (300–3400 Hz) is the
  default recommendation: it agrees with `mix` within 16 ms on
  130/212 words, but on the 82 where they differ it is the one
  picking voice onsets instead of drum onsets. The tool keeps both
  so the choice stays measurable.
- **The stay candidate is always available.** A word with no peak
  within the window keeps its ASR time exactly. The DP can never
  invent an onset.
- **Monotonicity is a constraint, not a hope.** Transitions are
  non-decreasing in frame; the all-stay chain is always feasible
  (ASR starts are non-decreasing), so the DP always terminates.
- **No stem at runtime.** The survey scoped the snapper against
  "the vocal-stem onset envelope" — a Demucs stem. The built tool
  does NOT run Demucs: it uses band-restricted mix flux instead,
  so a snap costs 0.5 s instead of ~14 minutes. The stem is used
  here only as validation ground truth (see §"Stem validation"),
  not as a runtime dependency. That substitution is the tool's
  central bet, and the stem comparison is what tests it.

## Validation

### Build + regression (re-measured in this recovery)

- `make clean && make`: `gcc -std=c11 -O2 -Wall -Wextra`, ZERO
  warnings, exit 0. Both binaries rebuilt (60,800 B each).
- Beats mode regression: DP beats on MV-14 are BIT-IDENTICAL to
  sprint 3's `c11_beat_mv14.json` (`beats_s` equal, tempo 90.5 BPM,
  phase 0.460 s, n 247). The snap additions did not touch the
  beat/feature paths.
- Features mode: runs clean, MFCC 13×10101, chroma 12, 247 beats —
  shapes as in sprint 4.
- Determinism: two identical `snap --flux vocal` runs produce
  byte-identical word arrays.
- Runtime: snap ~0.5 s, beats ~0.6 s, features ~2.1 s on MV-14.

### Snap results on MV-14 (212 words, faster-whisper, no VAD)

Defaults: `--flux vocal --window 0.4 --lambda 2.0` (canonical
outputs `c11_mir/snap_vocal_mv14.json`, `snap_mix_mv14.json`).

| | moved | median \|corr\| | mean \|corr\| | max \|corr\| | on peak | gaps |
|---|---|---|---|---|---|---|
| vocal λ=2.0 | 166/212 (78%) | 0.052 s | 0.063 s | 0.252 s | 181 | 115 -> 64 |
| mix λ=2.0 | 162/212 (76%) | 0.056 s | 0.062 s | 0.252 s | 183 | 115 -> 74 |

Correction distribution (vocal): p25 0.012 s, p75 0.092 s, p90
0.14 s, p99 0.228 s; 47 words move >0.1 s, 6 move >0.2 s, none
hits the ±0.4 s window cap. Direction is balanced (81 earlier,
80 later) — no systematic ASR lead/lag. Mix vs vocal snapped
times agree within 16 ms on 130/212 words (median |diff| 0.0 s,
max 0.336 s).

### Lambda sensitivity (second sweep, fixed build)

| lambda | vocal moved | vocal median | vocal gaps | mix moved | mix median | mix gaps |
|---|---|---|---|---|---|---|
| 1.0 | 167 | 0.056 s | 115 -> 61 | 165 | 0.058 s | 115 -> 71 |
| 2.0 | 166 | 0.052 s | 115 -> 64 | 162 | 0.056 s | 115 -> 74 |
| 4.0 | 144 | 0.036 s | 115 -> 74 | 136 | 0.034 s | 115 -> 85 |
| 8.0 | 97 | 0.008 s | 115 -> 101 | 78 | 0.004 s | 115 -> 103 |

λ=1 and λ=2 are nearly identical (the tiered cost saturates:
at λ=2 every strong peak inside ±0.4 s is worth reaching, since
λ·d < 1.0 out to 0.5 s). λ=4 halves the median correction;
λ=8 nearly freezes the DP (median 0.004–0.008 s). λ=2 sits on
the knee and is the default. (First build's graded cost, for
contrast: 209/212 moved at λ=0.5, median 0.160–0.175 s — the
over-snap the tiering was built to kill.)

### Window sensitivity

Window 0.25 / 0.40 / 0.60 s give IDENTICAL results at λ=2.0
(vocal: 166 moved, median 0.052 s, gaps 115 -> 64 in all three).
The nearest strong onset is almost always within 0.25 s on this
dense funk track, so the window never binds. The snapper is
window-insensitive here — a robustness result, not a tuning one.

### The gap test is invalid as shipped (honest finding)

The gap numbers above (115 -> 64) look like a pad-rule win. They
are mostly a threshold artifact, and this sprint caught it:

- The 0.05 threshold sits almost exactly at the MEDIAN band
  energy of ASR word starts (median 0.0448, p25 0.0207, p75
  0.0755). It labels ~half the words as "in a gap" by
  construction.
- Band energy (300–3400 Hz, mix) does not separate voice from
  no-voice on this track at all: the wordless outro measures
  0.0946 — LOUDER than the sung V1 (0.0264) — and inter-phrase
  gaps measure 0.027–0.178 against sung spans of 0.026–0.087.
  The band is dominated by instruments (guitar/keys/snare), not
  voice.
- At a calibrated threshold the story changes: below 0.01 (near
  silence in the band), 13% of ASR starts are gaps and the
  snapper moves all but ~1% of them out (28 -> 2 words). At 0.02
  it is 51 -> 7. The snapper DOES move anchors onto higher-energy
  frames (median anchor energy 0.045 -> 0.068, +52%), but the 0.05
  "gap" label is not measuring voice absence. Do NOT quote "115
  -> 64" as a pad-rule result. The gap test needs a voice-specific
  signal — the Demucs stem energy is the obvious one, and the stem
  validation below measures exactly that. A follow-up should
  either re-threshold the gap test on stem energy or replace it
  with a voicing detector; the tool's `gap_asr`/`gap_snapped`
  fields will then mean what they say.

### Stem validation

Not completed in this sprint — the stem was in flight, not on
disk, when the validation ran. The Demucs vocal stem for MV-14
was being computed by sprint 6 (audio-separator, htdemucs, single
stem Vocals, `~/workspace/tmp_hpss/mv14_demucs/`, started
~22:19 EST for the HPSS validation) when this sprint needed one;
this sprint started its own `demucs -n htdemucs` run, spotted the
duplicate (same input, same model), and killed it after 1:25 to
avoid double torch compute on the shared blade. At report time
the separator was still running (19+ min, sharing CPU with the
live volley and three sprints), so the stem-flux comparison is the
FIRST follow-up, with the exact commands:

    ffmpeg -y -i <stem.wav> -ac 1 -ar 16000 -sample_fmt s16 stem_16k.wav
    ./c11_mir snap stem_16k.wav SONG_WORDS.json snap_stem_mv14.json --flux mix
    # the stem IS the vocal channel, so mix flux = stem flux

then compare `snapped_start` against `snap_vocal_mv14.json`
(median |diff|, agreement within 16 ms) and recompute the gap
counts on stem energy at 0.01/0.02. The stem will also settle the
hand-check disagreements below (the five drum-chase cases and the
two ambiguous ones) — a stem flux peak at the snapper's position
vindicates it; silence there convicts it.

### Hand-check (24-word stratified sample)

Sample: 8 largest |correction| (112, 5, 79, 34, 190, 56, 57,
162), 8 gap_asr -> non-gap_snapped (1, 12, 13, 15, 25, 26, 27,
28), 8 random (seed 11: 59, 60, 129, 133, 144, 145, 157, 165).
For each word: vocal-flux + mix-flux local maxima (≥0.15) in
±0.4 s, the word's ASR span and its neighbours' boundaries, and
the phonetic prior (plosive burst / fricative / vowel swell).
Picks were reasoned from peaks + phonetics, word by word; the
traces and peak table are in `~/workspace/scratch_snapper/`
(`traces.txt`, and the peak table was generated alongside).

**Result: 15 agree / 7 disagree / 2 ambiguous.**

- Agree (15): 5 (only candidate peak, +0.24), 13 (+0.096, the
  /d/ burst), 15 (+0.048, inside the 0.12 s span), 26 (+0.08,
  the vowel), 27 (-0.144, the /p/ burst), 28 (+0.08), 57
  (+0.192, the /st/), 79 (+0.224), 129 (-0.08, the /s/ leading
  the vowel), 133 (-0.016, essentially ASR), 144 (-0.08),
  145 (+0.064, the /p/, flux 0.74), 157 (stayed — sustained
  phrase, no onset to find), 165 (-0.048), 190 (+0.224).
- Disagree (7): 12 (snap -0.028; the strongest peak, 0.55, sits
  at -0.08 — 3 frames, low confidence), 34 (snap -0.22 onto a
  drum transient; no in-span peak at all), 56 (snap -0.21 onto
  the 0.69 peak; the word is 0.14 s long), 59 (snap +0.088; the
  stronger peak is at -0.096 — an equidistant tie, low
  confidence), 60 (snap -0.128 onto the previous word's final
  /p/ release), 112 (snap -0.25; the word's span has NO vocal
  peak at all), 162 (snap -0.18 onto the 0.67 drum transient;
  no in-span peak).
- Ambiguous (2): 1 (no vocal-band energy anywhere in ±0.32 s;
  the snapper's -0.128 peak sits inside the previous word),
  25 (a cluster of pre-ASR peaks, most likely the previous
  word's syllables).

**The pattern is the finding.** All five clear disagreements
share one failure mode: the word has NO strong (≥0.20) vocal-flux
peak inside its own ASR span, so the DP reaches outside the span
— always EARLIER — onto a strong peak that belongs to the
previous word or a drum. The snapper's errors concentrate in the
large-correction tail: the 21 moved words with no in-span strong
peak have median |correction| 0.128 s (vs 0.052 s overall), and
88/212 snapped positions sit before the previous word's ASR end.

**Recommended rule (follow-up, NOT applied here): "stay if no
in-span strong peak"** — if no candidate ≥0.20 falls within
[ASR start, ASR end], keep the ASR time. On MV-14 it would hold
21 words (10%) at ASR, including all five clear hand-check
errors, and it preserves all 15 hand-check agrees (each has an
in-span strong peak). It is conservative by construction: it only
ever keeps the ASR time, never invents an anchor. It needs one
re-validation run after patching (the numbers in this report are
for the tool as built).

**Caveat, stated plainly:** this hand-check was NOT blind — the
peak table I judged from also printed the snapper's snapped
values, so confirmation bias is possible even though the picks
were reasoned from peaks and phonetics. The stem comparison
above is the blind check, and it is owed before the snapper's
output feeds assembly warps.

## Performance

- snap: ~0.5 s on the 161.6 s MV-14 track (STFT dominates).
- beats: ~0.6 s; features: ~2.1 s. Peak memory ~120 MB.
- No Python, no weights, no torch at runtime.

## Honest limits

1. **No stem at runtime** — the band-flux substitute is the bet;
   the stem comparison is the evidence for it (see §"Stem
   validation"). If the stem disagrees systematically, the vocal
   band needs narrowing or the tool needs a stem input mode.
2. **The gap test as shipped is miscalibrated** (see above) —
   its numbers must not be quoted as pad-rule results until it
   runs on a voice-specific signal.
3. **The DP cannot fix what Whisper got wrong.** A missed,
   hallucinated, or duplicated word has no anchor to snap; a word
   whose ASR order is wrong breaks the monotonicity assumption.
   22/212 words have prob < 0.5.
4. **Validation is MV-14 only.** Chant-dense funk is the
   snapper's best case (onsets everywhere). Sparse ballads and
   sustained vowels (long notes with no onset at the word start)
   are untested — the stay candidate covers them, but that is
   unproven.
5. **The hand-check sample is small (24/212) and was not
   blind** (see §"Hand-check") — the stem comparison is the blind
   check and is owed before snapped anchors feed assembly warps.
6. **Known failure mode, unpatched:** when a word has no strong
   peak in its own span, the DP reaches earlier onto a previous-
   word or drum peak (5/5 clear hand-check errors). The "stay if
   no in-span strong peak" rule fixes it on MV-14; it is a
   follow-up patch, not yet applied or re-validated.

## Next

- FIRST: stem-flux snap comparison + stem-energy gap counts
  (commands in §"Stem validation"), once sprint 6's stem lands.
  It settles the 7 hand-check disagreements and calibrates the
  gap test.
- Patch the "stay if no in-span strong peak" rule and re-run the
  full validation (hand-check the 21 affected words again).
- HPSS + RMS-VAD (sprint 6, running) supplies the segmentation
  the snapper's word times feed into; together they replace the
  forced-alignment step for the pipeline (WhisperX/Qwen3
  aligner unneeded for our tracks).
- Follow-up: re-threshold the gap test on stem energy (or a
  voicing detector) so `gap_asr` means "voice absent".
- Follow-up: run the snapper on MV-13 (97 BPM, 394 words) and
  MV-12 (131.5 BPM) as a second/third validation track.
- The snapper's output format (`snapped_start` per word) plugs
  directly into the assembly warp: replace the ASR anchor with
  the snapped anchor before keyframing.

## Files

- `c11_mir/c11_mir.c` (+385 lines snap mode, + `band_flux` /
  `band_energy` helpers) — the tool.
- `c11_mir/json.c`, `c11_mir/json.h` — LEGO'd slermes libjson.
- `c11_mir/Makefile` — builds both binaries with json.c.
- `c11_mir/snap_vocal_mv14.json`, `c11_mir/snap_mix_mv14.json` —
  canonical λ=2.0 outputs on MV-14 (212 words).
- `c11_mir/README.md` — snap usage documented.
- This report. DETECTION_FINDERS.md run entry appended.
- Scratch (not committed): `~/workspace/scratch_snapper/`
  (`handcheck.py`, `traces.txt`, `mv14_44k.wav`, sweep JSONs in
  `/tmp/snap*.json` — /tmp is ephemeral; the sweep table in this
  report is the durable record).

No commit, no Telegram (parent owns both).
