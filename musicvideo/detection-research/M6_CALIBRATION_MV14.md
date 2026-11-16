# M6 calibration on MV-14 takes — 2026-11-11 (downtime-improvement sprint #2)

Follow-up to `SPRINT_2026-11-11.md`: sprint #1 found TSM M6 (native-rate
duplicate ratio, τd=0.0005) discriminates the rejected MV-8 v2 master
(0.197) from the accepted v3 (0.049), 4.0x — while freezedetect saw zero
freezes in both. This sprint calibrates M6 at TAKE level on the 51
ledgered MV-14 takes (46 KEEP + 5 REJECT) so the gate can run at fire
time, before a take enters a cut, instead of on masters after the fact.

## Method

- Script: `m6_calibrate.py` (same method as `tsm.py`: one FFmpeg decode
  per take at 160x90 gray, native 24fps; d24 = mean abs-diff of
  consecutive frame pairs; M6 = share of pairs with d24 < 0.0005).
  Raw numbers: `m6_mv14.json`.
- Every take file's md5 was verified against `work/TAKE_LEDGER.md`
  before measuring (51/51 matched; trust md5, not filenames).
- Two scopes per take:
  - **Full take** — the whole 5s/10s file as fired.
  - **Usable window** — the ledger's take-relative usable window only
    (e.g. S30 2.44–5.96s, S40 3.78–4.56s, S45 2.04–3.90s). This is
    the material that enters the cut; the rest is trimmed at assembly.
    REJECT takes have no usable window (no slot was ever cut from them).
- M1 here is the median native-rate frame diff — NOT the ledger's
  4fps motion mean (frames 0.71s apart), so the two numbers are on
  different scales and must not be compared directly.

## The calibrated gate bar

**Per-take gate (usable-window scope only): flag for EYE REVIEW when
window M6 > 0.10 AND window longest-dup-run ≥ 0.30s. Never auto-reject
on M6 — it is a review flag, same as the whole-master bar.**

Evidence on this 51-take sample:

- KEEP window M6: median 0.0000, mean 0.0090, max 0.2292. 38/46 KEEPs
  are exactly 0.0000 — most takes have literally zero near-duplicate
  pairs inside the slot. Only 2 KEEPs exceed 0.05 (S14 0.2292, S24
  0.0786); only 1 exceeds 0.10 (S14).
- KEEP window longest-dup-run: max 0.29s (S24); every other KEEP is
  ≤0.04s (a single frame).
- **Zero of 46 KEEPs meet BOTH conditions.** S14 meets the M6 half
  only (0.2292, run 0.04s); S24 is the closest take on both axes
  (0.0786, 0.29s) — just under the bar on both. The AND-combination
  is what makes this a gate instead of a flag-machine.
- A genuinely halted take — e.g. a take that reaches its end frame
  early and holds it for 1s inside a 2s window (the failure the
  2026-10-30 practitioner post described) — would score roughly
  M6 ≈ 0.5 with a 1.0s run, far above the bar on both axes. The bar
  is calibrated on the KEEP side; its sensitivity to a real halt is
  inferred from the master-level v2/v3 split, not proven at take
  level (no halted take exists in this sample — see the caveat below).

## False-flag risk — stated plainly

1. **M6 alone false-flags.** At M6 > 0.10 alone, S14 (a KEEP) flags:
   it is a sanctioned calm wordless pocket (empty night desk, frame
   pulsing twice, tape reel turning) whose duplicates are scattered
   single frames — longest run 0.04s, no hold anywhere. That is the
   take-level echo of sprint #1's v3 O-A segment (M6 0.223, longest
   run 0.04s): slow drift reads as duplicates without any freeze.
   The longest-run half of the gate exists precisely to let S14
   through.
2. **The margin on the run axis is thin.** S24's 0.29s run sits 0.01s
   under the 0.30s bar. S24 is a sanctioned calm pocket too (the
   vault "breathes" — lights dim, then come back down the aisle in
   a wave). Another calm pocket could plausibly cross 0.30s on a
   future take and meet the M6 half as well. The gate must stay a
   review flag: a flagged take gets an eye read, not a rejection.
3. **n=46, one project, one generator batch.** The bar is calibrated
   on MV-14 takes only. Re-check it against the next volley's takes
   (S47–S52 when the budget resets) before treating it as settled.
4. **Do NOT gate on full-take M6.** Full-take M6 > 0.10 would flag
   5/46 KEEPs (11%): S14 (0.336), S18 t2 (0.303), S41 (0.294), S45
   (0.163), S43 (0.151). In every case the signal is OUT-OF-SLOT
   material — the black fade-to-black tail after ~3.57s (a run of
   identical black frames; S41's 0.92s longest run IS the tail) and
   calm pre-line lead-ins (S45's head, S18 t2's slow aisle). The
   full-take scope measures what assembly trims. The gate needs the
   usable window, which the volley QC already records — so this is
   implementable in the existing QC flow, not a new measurement.

## What M6 does NOT do: it does not separate KEEP from REJECT here

- REJECT full M6: S16 t1 0.0000 (G2 subtitle), S18 t1 0.2101 (G1
  wardrobe), S19 t1 0.0924 (G2 subtitle), S25 t1 0.3698 (G1 hair),
  S25 t2 0.0504 (G2 subtitle). KEEP full M6 spans 0.0000–0.3361.
  The two populations overlap completely.
- This is EXPECTED, not a failure of M6: all five rejects are
  text/identity failures (burned-in subtitles, wrong shirt, full
  head of hair), not motion failures. M6 is a motion gate; it was
  never designed to catch a subtitle or a wrong shirt, and it would
  not have caught any of these five. The calibration's value is the
  KEEP distribution — proof the gate can run on normal takes without
  false-flagging them — not a claim that it separates these rejects.
- Side observation (not a gate): the two G1 rejects S18 t1 and S25 t1
  have extremely low full-take M1 (0.0009 / 0.0006 — 20–100x below
  typical takes), i.e. near-static at native rate. But S18 t2, a
  KEEP re-fire of the same scene, has the same character (full M1
  0.0008, window M1 0.0016), so native-rate M1 does not separate
  either. Do not build a gate on M1 from this sample.

## Per-take table (M6 τd=0.0005, native 24fps, 160x90 gray)

| Scene | Take | Verdict | Full M6 | Full longest run | Full M1 | Window M6 | Window longest run | Window M1 |
|---|---|---|---|---|---|---|---|---|
| S01 | t1 | KEEP | 0.0042 | 0.04s | 0.03935 | 0.0149 | 0.04s | 0.02333 |
| S02 | t1 | KEEP | 0.0000 | 0.00s | 0.03521 | 0.0000 | 0.00s | 0.02732 |
| S03 | t1 | KEEP | 0.0000 | 0.00s | 0.04048 | 0.0000 | 0.00s | 0.06266 |
| S04 | t1 | KEEP | 0.0420 | 0.08s | 0.03503 | 0.0000 | 0.00s | 0.04155 |
| S05 | t1 | KEEP | 0.0000 | 0.00s | 0.02058 | 0.0000 | 0.00s | 0.02153 |
| S06 | t1 | KEEP | 0.0084 | 0.04s | 0.02304 | 0.0139 | 0.04s | 0.03406 |
| S07 | t1 | KEEP | 0.0377 | 0.04s | 0.01008 | 0.0000 | 0.00s | 0.01385 |
| S08 | t1 | KEEP | 0.0084 | 0.04s | 0.02143 | 0.0000 | 0.00s | 0.03134 |
| S09 | t1 | KEEP | 0.0000 | 0.00s | 0.03290 | 0.0000 | 0.00s | 0.03861 |
| S10 | t1 | KEEP | 0.0588 | 0.25s | 0.04016 | 0.0000 | 0.00s | 0.05252 |
| S11 | t1 | KEEP | 0.0084 | 0.04s | 0.05106 | 0.0161 | 0.04s | 0.06189 |
| S12 | t1 | KEEP | 0.0000 | 0.00s | 0.02044 | 0.0000 | 0.00s | 0.01925 |
| S13 | t1 | KEEP | 0.0000 | 0.00s | 0.00997 | 0.0000 | 0.00s | 0.01102 |
| S14 | t1 | KEEP | 0.3361 | 0.04s | 0.00364 | 0.2292 | 0.04s | 0.00749 |
| S15 | t1 | KEEP | 0.0000 | 0.00s | 0.00481 | 0.0000 | 0.00s | 0.04688 |
| S16 | t1 | REJECT (G2 subtitle) | 0.0000 | 0.00s | 0.06220 | — | — | — |
| S17 | t1 | KEEP | 0.0000 | 0.00s | 0.06266 | 0.0000 | 0.00s | 0.06502 |
| S18 | t1 | REJECT (G1 wardrobe) | 0.2101 | 0.38s | 0.00091 | — | — | — |
| S16 | t2 | KEEP | 0.0000 | 0.00s | 0.04656 | 0.0000 | 0.00s | 0.08371 |
| S18 | t2 | KEEP | 0.3025 | 0.25s | 0.00077 | 0.0000 | 0.00s | 0.00162 |
| S19 | t1 | REJECT (G2 subtitle) | 0.0924 | 0.21s | 0.05962 | — | — | — |
| S20 | t1 | KEEP | 0.0000 | 0.00s | 0.02699 | 0.0000 | 0.00s | 0.02006 |
| S21 | t1 | KEEP | 0.0000 | 0.00s | 0.06118 | 0.0000 | 0.00s | 0.10079 |
| S22 | t1 | KEEP | 0.0000 | 0.00s | 0.02567 | 0.0000 | 0.00s | 0.03523 |
| S19 | t2 | KEEP | 0.0084 | 0.04s | 0.03715 | 0.0000 | 0.00s | 0.02377 |
| S23 | t1 | KEEP | 0.0000 | 0.00s | 0.05610 | 0.0000 | 0.00s | 0.06246 |
| S24 | t1 | KEEP | 0.0588 | 0.29s | 0.06657 | 0.0786 | 0.29s | 0.05607 |
| S25 | t1 | REJECT (G1 hair) | 0.3698 | 0.46s | 0.00060 | — | — | — |
| S26 | t1 | KEEP | 0.0084 | 0.04s | 0.01029 | 0.0175 | 0.04s | 0.01234 |
| S27 | t1 | KEEP | 0.0084 | 0.04s | 0.02737 | 0.0179 | 0.04s | 0.02073 |
| S25 | t2 | REJECT (G2 subtitle) | 0.0504 | 0.25s | 0.04606 | — | — | — |
| S28 | t1 | KEEP | 0.0000 | 0.00s | 0.02386 | 0.0000 | 0.00s | 0.01792 |
| S29 | t1 | KEEP | 0.0168 | 0.08s | 0.02328 | 0.0000 | 0.00s | 0.03267 |
| S30 | t1 | KEEP | 0.0000 | 0.00s | 0.01412 | 0.0000 | 0.00s | 0.01573 |
| S31 | t1 | KEEP | 0.0000 | 0.00s | 0.04689 | 0.0000 | 0.00s | 0.05236 |
| S32 | t1 | KEEP | 0.0000 | 0.00s | 0.02339 | 0.0000 | 0.00s | 0.03107 |
| S25 | t3 | KEEP | 0.0000 | 0.00s | 0.03422 | 0.0000 | 0.00s | 0.03342 |
| S33 | t1 | KEEP | 0.0672 | 0.04s | 0.00190 | 0.0278 | 0.04s | 0.00170 |
| S34 | t1 | KEEP | 0.0000 | 0.00s | 0.01589 | 0.0000 | 0.00s | 0.02033 |
| S35 | t1 | KEEP | 0.0000 | 0.00s | 0.05275 | 0.0000 | 0.00s | 0.06985 |
| S36 | t1 | KEEP | 0.0000 | 0.00s | 0.08954 | 0.0000 | 0.00s | 0.09635 |
| S37 | t1 | KEEP | 0.0084 | 0.04s | 0.01849 | 0.0000 | 0.00s | 0.01961 |
| S39 | t1 | KEEP | 0.0000 | 0.00s | 0.06883 | 0.0000 | 0.00s | 0.07286 |
| S40 | t1 | KEEP | 0.0000 | 0.00s | 0.03936 | 0.0000 | 0.00s | 0.06096 |
| S41 | t1 | KEEP | 0.2941 | 0.92s | 0.00312 | 0.0000 | 0.00s | 0.00890 |
| S42 | t1 | KEEP | 0.0084 | 0.04s | 0.00937 | 0.0000 | 0.00s | 0.02793 |
| S43 | t1 | KEEP | 0.1513 | 0.29s | 0.00153 | 0.0000 | 0.00s | 0.00194 |
| S38 | t2 | KEEP | 0.0252 | 0.08s | 0.01322 | 0.0000 | 0.00s | 0.01886 |
| S44 | t1 | KEEP | 0.0000 | 0.00s | 0.01139 | 0.0000 | 0.00s | 0.02711 |
| S45 | t1 | KEEP | 0.1632 | 0.04s | 0.00516 | 0.0000 | 0.00s | 0.02022 |
| S46 | t1 | KEEP | 0.0000 | 0.00s | 0.03588 | 0.0000 | 0.00s | 0.04147 |

## Beat tracking vs the measured grid (F-07 / F-13)

### BeatNet (F-07): BLOCKED — same 3.12 wall as madmom (F-13)

- BeatNet 1.1.1 installs cleanly on the lyrics venv (`pip install
  beatnet`, torch 2.15.0+cpu present), but it cannot run: it imports
  madmom at THREE points — `log_spect.py` (STFT/spectrogram feature
  extraction), `particle_filtering_cascade.py` (HMM bar state spaces
  for the PF decoder), and `BeatNet.py` (DBN decoder for offline
  mode). Both inference paths (PF and DBN) need madmom.
- madmom cannot build on Python 3.12 (sprint #1: `longintrepr.h`
  removed from the CPython public headers). There is no python3.11
  or 3.10 on this box (`/usr/bin/python*` = 3.12 only), so the
  ≤3.11 venv path needs a whole Python install — out of sprint scope,
  per the task's "do not burn the sprint on installs" limit.
- **F-07 and F-13 are the same wall, not two independent paths:**
  BeatNet's decoding IS madmom. The MV-14 beat comparison from
  BeatNet specifically is STILL OWED. Next path, in order: (a) a
  Python ≤3.11 venv with madmom + BeatNet (needs a Python install
  first); (b) nothing else on this box — do not shim madmom, the
  feature-extraction and HMM layers are the work itself.

### Fallback second opinion: librosa beat_track (NOT BeatNet)

Script `librosa_beat_mv14.py`, raw beats `librosa_beat_mv14.json`.
librosa was already in the lyrics venv (1.0.0); no install was needed.

- **Tempo AGREES: librosa 92.29 BPM vs measured 92.0 BPM** (median
  inter-beat interval 0.6502s vs measured 0.649s — 0.3% apart).
  Beat count agrees too: 238 beats over 3.81–159.15s, ~30–31 per
  20s window vs 30.8 expected. Drift over the track is negligible
  (−0.023s).
- **Per-beat PHASE agreement is LOOSE: median |offset| 0.145s**
  (22% of a beat period); only 20.6% of beats within 50ms and 39.9%
  within 100ms of the measured grid; max |offset| 0.324s (half a
  beat period — the wrap boundary). The offset is section-dependent,
  not a constant shift: median offset by 20s window runs +0.03s
  (20–40s), +0.08s (40–60s), +0.16s (60–80s), −0.23s (80–100s,
  the bridge), −0.03s (100–120s), +0.19s (120–140s), −0.22s
  (140–160s, the outro). A substantial minority of beats sit near
  the half-period — librosa slips phase in some sections, or the
  Suno track's own beat phase wanders section to section (or both;
  this run cannot tell them apart).
- Librosa also misses the intro: first beat 3.808s vs the grid's
  0.240s — the sparse instrumental intro has no beat for it to lock
  onto, so the grid's phase in 0–4s is extrapolated, not confirmed.
- **Verdict: the measured grid's TEMPO is confirmed (92.0 BPM), but
  its single global PHASE should not be trusted beat-by-beat.**
  For swing-keyframe work the pipeline already anchors on per-word
  ASR timings from the takes themselves — that stays the right
  authority; do not re-time anything off the global grid phase
  alone. A BeatNet run (once the ≤3.11 wall is cleared) is still
  the owed cross-check: BeatNet's downbeat output would also say
  whether the bar lines fall where the plan thinks they do.

## What to do with this

1. **Add the M6 column to volley QC** (the sprint #1 recommendation,
   now calibrated): for each take, compute window-scope M6 +
   longest-dup-run over the ledgered usable window at QC time
   (~1s per take, same decode as the motion audit). Flag for eye
   review when M6 > 0.10 AND longest run ≥ 0.30s. Record the numbers
   in the ledger row; never auto-reject.
2. **Re-check the bar on volley 10's takes** (S47–S52) when the
   budget resets — especially any calm wordless pocket, which is
   where the false-flag risk lives (S14/S24 precedent).
3. **Clear the ≤3.11 wall once, for both F-07 and F-13**, as its own
   job (install Python ≤3.11, venv, madmom + BeatNet) — then run the
   owed BeatNet vs measured-grid comparison and the madmom
   comparison in one pass. Do not re-litigate the 3.12 build.
4. Still owed from sprint #1, untouched here: the TSM
   temporal-signature reuse cross-check (v3 vs its takes).
