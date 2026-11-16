# c11_tsm — C11 per-gap-targeted time-stretch core (M7 + OLA256 fallback)

Sprint: 2026-11-12. Spec: `~/workspace/research_notes/tsm-driedger-2014/SPRINT_SCOPE.md`.
Validation: `~/workspace/research_notes/tsm-driedger-2014/report.md`
(parent-verified in full ~04:44 EST). Build report: `../SPRINT_2026-11-12_C11_TSM.md`.

## What it is

M7 — the user's method (Telegram msg 292): cut at every hit, keep each hit
window (±25 ms) sample-identical, stretch each inter-hit gap to land its hit
exactly on the song-grid onset. Gap DSP is Driedger/Müller/Ewert 2014:
binary-mask HPSS (STFT N=1024, ℓ=5) → phase vocoder (N=4096) on harmonic +
OLA (N=256) on percussive, with a 50 ms hit-tail lookback so the PV picks up
in phase with the preceding hit. Uniform fallback: OLA256.

**Squeeze guard (hard rule):** a gap with alpha < 0.5 is NOT stretched — the
span is flagged BAD-WORD (assembly cuts to montage for exactly that span) and
the slot is filled with a truncated copy of the gap input. Gaps in [0.5, 0.7)
are stretched but flagged WARN (unmeasured band until the moderate-squeeze
take sets the guard precisely). The head gap is never flagged (no word body
before the first hit); the tail gap holds the last word's body and IS guarded.

**Not built:** M1 PV as the core (worst identity on sung material, 17/23);
M4 global-gap slicing (superseded by M7).

## Build

```
make          # c11_tsm (libc+libm only, -Wall -Wextra, zero warnings)
make asan     # c11_tsm_asan (ASan+UBSan; run a take through it, expect rc 0)
```

## Usage

```
c11_tsm m7  --in IN.wav --out OUT.wav --hits H0,H1,... --song S0,S1,...
            --alpha A [--words W0,W1,...] [--guard 0.5] [--opguard 0.7]
            [--no-guard] [--json report.json] [--take NAME]
c11_tsm ola --in IN.wav --out OUT.wav --alpha A
c11_tsm hp  --in IN.wav --out OUT.wav --alpha A
c11_tsm pv  --in IN.wav --out OUT.wav --alpha A
```

`--hits` are clip-local hit times (s); `--song` are song-grid onsets (s,
absolute — the first is the reference). `--alpha` is the overall out/in
length factor. Input/output are 16-bit PCM mono WAV. The `m7` JSON report
carries per-gap alphas, flags (none/warn/hard), in/out spans, the affected
word, and the hit-identity check (max|diff|, centre errors).

## Parity notes (why the C output matches the Python prototype bit-for-bit)

Every librosa 1.0.0 call in `tsm_proto.py` / `tsm_m4b.py` is replicated
exactly — see the header comment in `c11_tsm.c`. The traps, in order of
how much they cost:

- `librosa.stft` default `pad_mode` is `"constant"` (zero pad), not reflect.
- `phase_vocoder` in 1.0.0 takes RAW adjacent-frame phase differences
  (no expected-advance correction, no wrapping) and linearly interpolates
  magnitudes with extrapolation past the last frame.
- `scipy median_filter` in the prototype's HPSS uses `mode="nearest"`
  (edge repeat), not reflect.
- `np.hanning` (OLA leg) is the SYMMETRIC window; librosa's Hann is periodic.
- Python `round()` is round-half-to-even; C `round()` is half-away.
  `py_round()` replicates it for every sample-count computation.

Result: guard-off correlation vs the prototype's M7 outputs is 1.000000
(6 dp) on all four validation takes; per-gap alphas identical.

## Files

- `c11_tsm.c` — the whole core, one file.
- `Makefile`
- `validate_c11_tsm.py` — bars 1/6/7 + S49MOD construction (fw-venv).
  Writes `c11_tsm_validation.json`.
- `c11_grade.py` — ASR grades for bars 2/3/4/5 (faster-whisper
  large-v3-turbo, same config as the validation; checkpointed per clip).
- `c11_tsm_validation.json` — all bar results.
- `out/` — validation artifacts (take windows, C11 outputs, JSON reports).
  Never committed.
- `c11_grade.log` — ASR grade run log.
