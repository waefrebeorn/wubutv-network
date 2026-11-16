"""Step-1 experiment for c11_casa (Bar A / Bar E, fail-fast).

Question (SPRINT_SCOPE.md §4.1): during sung spans, does the correlogram
show a dominant peak at the voice's F0 lag that is absent (or subordinate
to the accompaniment's lag) during instrumental spans?

Method — per-frame waveform autocorrelation (the correlogram collapsed over
channels; its lag axis IS the F0 axis), same framing as sprint 8
(1024-sample Hann window, 160-sample hop, centred, zero-padded edges,
16,161 frames, 10 ms hop) so frames align 1:1 with the saved pYIN tracks:
  - r(tau) = IFFT(|FFT(x_w)|^2), normalized by r(0). Lags tau = 0..512.
  - Vocal range: F0 80-600 Hz -> tau in [27, 200] samples at 16 kHz.
    Sensitivity: wider range 50-800 Hz -> tau in [20, 320], recorded.
  - Voice lag tau_voice(t) = round(16000 / f0_interp(t)), f0_interp = log-F0
    interpolated across unvoiced gaps (vibrato sprint's method), trusted
    only within 0.25 s of a pYIN-voiced frame.
  - Per-frame: r_voice = r(tau_voice); r_max = max r(tau) over the vocal
    range; tau_max = argmax lag; dominance = 1 if |tau_max - tau_voice|
    <= 2 samples (voice lag is the top peak); r_second = max r(tau) over
    the vocal range excluding +-3 samples around tau_voice (accompaniment
    candidate).
  - Spans: sung = ref segments 1-10 (clean); bleed = 11-12 (reported
    separately, instrumental-class); instrumental = complement of the union
    of all 12 ref segments within [0, 161.6] (intro + 10 gaps + outro =
    12 spans). Clean spans = 22 (10 sung + 12 instrumental); total with
    bleed = 24.
  - Bar A scoring (stated before running): a span "separates" if a sung
    span's median r_voice exceeds the pooled instrumental median r_max,
    or an instrumental span's median r_max is below the pooled sung
    median r_voice. Pass = >=80% of clean spans (>=18/22); report /24
    with bleed alongside. Class-level Mann-Whitney sung r_voice vs
    instrumental r_max reported too (loop-4 format).
  - Bar E (multipitch confusion): over sung frames with trusted F0,
    confused if dominance == 0. Pass = confusion <= 20% (voice told apart
    on >=80% of sung frames). If Bar E fails, that is the finding — stop.

Controls (run before concluding anything):
  - Synthetic A (voice-only): harmonic complex f0=220 Hz -> dominance 1.
  - Synthetic B (mixture): voice 220 Hz + bass 98 Hz + brass 147 Hz at
    equal RMS -> does the voice-lag peak survive the bass?
  - Synthetic C (accompaniment-only): bass 98 + brass 147, no voice ->
    r at the 220 Hz lag must read low (absence control).
  - Stem control: the same pipeline on the isolated Demucs vocal stem
    (/tmp/mv14_stem_16k.wav, md5 verified) with the stem pYIN track as
    the F0 reference. Mix fails + stem passes = mix-dominance; both fail
    = the voice carries no separable lag peak.

Outputs: step1_experiment.json (all numbers, committed) +
step1_curves.npz (per-frame curves, NOT committed — regenerable).
No gate code is built in this script, by design (Bar A fail-fast).
"""
import json
import numpy as np
from scipy.io import wavfile
from scipy.stats import mannwhitneyu

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
CASA = f"{DR}/c11_casa"
SR = 16000
WIN = 1024
HOP = 160
N_FRAMES = 16161
TMAX = 161.6

# Vocal lag ranges (samples at 16 kHz)
VOCAL_LO, VOCAL_HI = 27, 200      # 80-600 Hz (primary)
WIDE_LO, WIDE_HI = 20, 320        # 50-800 Hz (sensitivity)

REF = json.load(open(f"{DR}/c11_mir/hpss_mv14_ref.json"))["segments"]
SEGS = [(s["start"], s["end"]) for s in REF]
SUNG = SEGS[:10]
BLEED = SEGS[10:]


def frame_signal(x):
    """Centre-framed, Hann-windowed frames, sprint-8 framing.

    Frame i is centred at t = i * 0.01 s: samples [i*160 - 512, i*160 + 512).
    Zero-padded edges. Returns (n_frames, 1024) float64.
    """
    n = len(x)
    idx = np.arange(N_FRAMES)[:, None] * HOP + np.arange(WIN)[None, :] - WIN // 2
    valid = (idx >= 0) & (idx < n)
    xf = np.zeros((N_FRAMES, WIN), dtype=np.float64)
    xf[valid] = x[np.clip(idx[valid], 0, n - 1)]
    win = np.hanning(WIN)
    return xf * win


def autocorr(frames):
    """Normalized autocorrelation r(tau)/r(0) per frame, tau = 0..512.

    FFT autocorrelation (same front end as c11_voice's YIN).
    """
    nfft = 2048
    spec = np.fft.rfft(frames, n=nfft, axis=1)
    ac = np.fft.irfft(spec * np.conj(spec), n=nfft, axis=1)[:, :513]
    r0 = ac[:, 0:1]
    return ac / np.where(r0 > 0, r0, 1.0)


def interp_f0(pyin_path):
    """Log-F0 interpolated across unvoiced gaps + trust mask.

    Trust = within 0.25 s (25 frames) of a pYIN-voiced frame
    (vibrato sprint's method). Returns (f0_interp_hz, trusted_bool).
    """
    v = json.load(open(pyin_path))
    f0 = np.array([f["f0_hz"] for f in v["frames"]], dtype=np.float64)
    voiced = np.array([f["pyin_voiced"] for f in v["frames"]], dtype=bool)
    with np.errstate(divide="ignore", invalid="ignore"):
        logf0 = np.where(f0 > 0, np.log(f0), np.nan)
    idx = np.arange(len(f0))
    good = ~np.isnan(logf0)
    f0i = np.exp(np.interp(idx, idx[good], logf0[good])) if good.any() else np.full(len(f0), np.nan)
    # trust: distance to nearest voiced frame <= 25 frames
    vidx = idx[voiced]
    if len(vidx):
        d = np.min(np.abs(idx[:, None] - vidx[None, :]), axis=1)
        trusted = d <= 25
    else:
        trusted = np.zeros(len(f0), dtype=bool)
    return f0i, trusted


def per_frame_features(x, pyin_path):
    """Return dict of per-frame arrays for one track."""
    fr = frame_signal(x)
    r = autocorr(fr)
    f0i, trusted = interp_f0(pyin_path)
    tau_voice = np.round(SR / f0i).astype(int)
    tau_voice = np.clip(tau_voice, 1, 512)
    n = len(f0i)
    r_voice = np.full(n, np.nan)
    r_second = np.full(n, np.nan)
    r_max = np.full(n, np.nan)
    tau_max = np.full(n, -1)
    for i in range(n):
        seg = r[i, VOCAL_LO:VOCAL_HI + 1]
        r_max[i] = seg.max()
        tau_max[i] = seg.argmax() + VOCAL_LO
        if trusted[i]:
            tv = tau_voice[i]
            r_voice[i] = r[i, tv]
            lo = max(VOCAL_LO, tv - 3)
            hi = min(VOCAL_HI, tv + 3)
            mask = np.ones(VOCAL_HI - VOCAL_LO + 1, dtype=bool)
            mask[lo - VOCAL_LO:hi - VOCAL_LO + 1] = False
            r_second[i] = seg[mask].max() if mask.any() else np.nan
    dominance = np.where(
        trusted & ~np.isnan(r_voice),
        (np.abs(tau_max - tau_voice) <= 2).astype(float), np.nan)
    # wide-range sensitivity: r_max over 50-800 Hz
    r_max_wide = r[:, WIDE_LO:WIDE_HI + 1].max(axis=1)
    return {
        "r": r, "r_voice": r_voice, "r_max": r_max, "r_max_wide": r_max_wide,
        "tau_max": tau_max, "tau_voice": tau_voice, "trusted": trusted,
        "dominance": dominance, "r_second": r_second, "f0_interp": f0i,
    }


def instrumental_spans():
    """Complement of the union of all 12 ref segments within [0, 161.6]."""
    pts = sorted(set([0.0, TMAX] + [e for s in SEGS for e in s]))
    # union intervals
    union = []
    for a, b in SEGS:
        if union and a <= union[-1][1]:
            union[-1] = (union[-1][0], max(union[-1][1], b))
        else:
            union.append((a, b))
    spans = []
    cur = 0.0
    for a, b in union:
        if a > cur:
            spans.append((cur, a))
        cur = max(cur, b)
    if cur < TMAX:
        spans.append((cur, TMAX))
    return spans


def span_median(vals, t, a, b):
    m = (t >= a) & (t < b) & ~np.isnan(vals)
    return float(np.median(vals[m])) if m.sum() else float("nan")


def summarize(feat, label):
    t = np.arange(N_FRAMES) * 0.01
    rv, rm = feat["r_voice"], feat["r_max"]
    instr = instrumental_spans()
    # pooled class medians (frames, excluding bleed from the sung class)
    sung_mask = np.zeros(N_FRAMES, dtype=bool)
    for a, b in SUNG:
        sung_mask |= (t >= a) & (t < b)
    instr_mask = np.zeros(N_FRAMES, dtype=bool)
    for a, b in instr:
        instr_mask |= (t >= a) & (t < b)
    sung_rv = rv[sung_mask & ~np.isnan(rv)]
    instr_rm = rm[instr_mask & ~np.isnan(rm)]
    pooled_sung = float(np.median(sung_rv))
    pooled_instr = float(np.median(instr_rm))
    try:
        mw = mannwhitneyu(sung_rv, instr_rm, alternative="greater")
        mw_p = float(mw.pvalue)
    except Exception:
        mw_p = float("nan")
    # per-span scoring
    spans_out = []
    correct_clean = 0
    total_clean = 0
    correct_all = 0
    total_all = 0
    for j, (a, b) in enumerate(SUNG):
        med = span_median(rv, t, a, b)
        ok = bool(med > pooled_instr) if not np.isnan(med) else False
        spans_out.append({"span": f"sung-{j+1}", "start": a, "end": b,
                          "median_r_voice": med, "separates": ok, "class": "sung"})
        total_clean += 1
        total_all += 1
        correct_clean += ok
        correct_all += ok
    for j, (a, b) in enumerate(instr):
        med = span_median(rm, t, a, b)
        ok = bool(med < pooled_sung) if not np.isnan(med) else False
        spans_out.append({"span": f"instr-{j+1}", "start": a, "end": b,
                          "median_r_max": med, "separates": ok, "class": "instrumental"})
        total_clean += 1
        total_all += 1
        correct_clean += ok
        correct_all += ok
    for j, (a, b) in enumerate(BLEED):
        med = span_median(rm, t, a, b)
        ok = bool(med < pooled_sung) if not np.isnan(med) else False
        spans_out.append({"span": f"bleed-{j+11}", "start": a, "end": b,
                          "median_r_max": med, "separates": ok, "class": "bleed"})
        total_all += 1
        correct_all += ok
    # multipitch confusion (Bar E): sung frames with trusted F0
    dom = feat["dominance"][sung_mask]
    dom = dom[~np.isnan(dom)]
    confusion = float(1.0 - dom.mean()) if len(dom) else float("nan")
    # wide-range sensitivity medians
    rmw = feat["r_max_wide"]
    pooled_sung_w = float(np.median(rmw[sung_mask]))
    pooled_instr_w = float(np.median(rmw[instr_mask]))
    out = {
        "track": label,
        "pooled_sung_median_r_voice": pooled_sung,
        "pooled_instr_median_r_max": pooled_instr,
        "mannwhitney_sung_gt_instr_p": mw_p,
        "barA_clean_correct": int(correct_clean),
        "barA_clean_total": int(total_clean),
        "barA_clean_pass": bool(correct_clean >= 0.8 * total_clean),
        "barA_all_correct": int(correct_all),
        "barA_all_total": int(total_all),
        "barE_confusion_rate_sung": confusion,
        "barE_pass": bool(confusion <= 0.20) if not np.isnan(confusion) else False,
        "n_trusted_sung_frames": int(len(dom)),
        "wide_range_pooled_sung_median_r_max": pooled_sung_w,
        "wide_range_pooled_instr_median_r_max": pooled_instr_w,
        "spans": spans_out,
    }
    return out


def synth_tone(f0s, amps, dur=2.0, sr=SR, seed=0):
    """Harmonic complex(es): f0s list, amps list; harmonics 1..8, 1/k."""
    rng = np.random.default_rng(seed)
    n = int(dur * sr)
    tt = np.arange(n) / sr
    x = np.zeros(n)
    for f0, amp in zip(f0s, amps):
        for k in range(1, 9):
            x += amp / k * np.sin(2 * np.pi * f0 * k * tt + rng.uniform(0, 2 * np.pi))
    return x / max(1e-9, np.abs(x).max()) * 0.5


def run_controls():
    """Synthetic controls: voice-only, mixture, accompaniment-only."""
    out = {}
    # voice-only 220 Hz
    x = synth_tone([220], [1.0])
    fr = frame_signal(np.concatenate([np.zeros(512), x, np.zeros(512)]))[:200]
    r = autocorr(fr)
    tv = round(SR / 220)
    out["voice_only_220Hz"] = {
        "r_at_voice_lag": float(np.median(r[50:150, tv])),
        "r_max_vocal_range": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].max(axis=1))),
        "tau_max_median": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].argmax(axis=1) + VOCAL_LO)),
    }
    # mixture: voice 220 + bass 98 + brass 147, equal RMS
    x = synth_tone([220, 98, 147], [1.0, 1.0, 1.0])
    fr = frame_signal(np.concatenate([np.zeros(512), x, np.zeros(512)]))[:200]
    r = autocorr(fr)
    out["mixture_220_98_147"] = {
        "r_at_voice_lag_220Hz": float(np.median(r[50:150, round(SR / 220)])),
        "r_at_bass_lag_98Hz": float(np.median(r[50:150, round(SR / 98)])),
        "r_at_brass_lag_147Hz": float(np.median(r[50:150, round(SR / 147)])),
        "r_max_vocal_range": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].max(axis=1))),
        "tau_max_median": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].argmax(axis=1) + VOCAL_LO)),
    }
    # accompaniment-only: bass 98 + brass 147, no voice
    x = synth_tone([98, 147], [1.0, 1.0])
    fr = frame_signal(np.concatenate([np.zeros(512), x, np.zeros(512)]))[:200]
    r = autocorr(fr)
    out["accompaniment_only_98_147"] = {
        "r_at_voice_lag_220Hz": float(np.median(r[50:150, round(SR / 220)])),
        "r_max_vocal_range": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].max(axis=1))),
        "tau_max_median": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].argmax(axis=1) + VOCAL_LO)),
    }
    return out


def main():
    sr, mix = wavfile.read(f"{DR}/c11_mir/mv14_16k.wav")
    assert sr == SR, sr
    mix = mix.astype(np.float64) / 32768.0
    feat_mix = per_frame_features(mix, f"{DR}/c11_voice/voice_mv14.json")
    mix_sum = summarize(feat_mix, "mix")

    sr2, stem = wavfile.read("/tmp/mv14_stem_16k.wav")
    assert sr2 == SR, sr2
    stem = stem.astype(np.float64) / 32768.0
    feat_stem = per_frame_features(stem, f"{DR}/c11_voice/voice_mv14_stem.json")
    stem_sum = summarize(feat_stem, "stem")

    controls = run_controls()

    result = {
        "experiment": "c11_casa step 1 — voice-lag peak separation (Bar A) + multipitch confusion (Bar E)",
        "method": "per-frame FFT autocorrelation, 1024 Hann / 160 hop / centred, lags 27-200 (80-600 Hz vocal range); voice lag from sprint-8 pYIN mix track, log-F0 interpolated, trusted within 0.25 s of a voiced frame",
        "ref": "hpss_mv14_ref.json, 12 segments (sung 1-10, bleed 11-12); instrumental spans = complement of the union of all 12 within [0, 161.6] (12 spans: intro + 10 gaps + outro); clean spans 22, total with bleed 24",
        "mix": mix_sum,
        "stem": stem_sum,
        "controls": controls,
        "verdict": {
            "barA_mix": "PASS" if mix_sum["barA_clean_pass"] else "FAIL",
            "barE_mix": "PASS" if mix_sum["barE_pass"] else "FAIL",
            "barA_stem": "PASS" if stem_sum["barA_clean_pass"] else "FAIL",
            "barE_stem": "PASS" if stem_sum["barE_pass"] else "FAIL",
        },
    }
    json.dump(result, open(f"{CASA}/step1_experiment.json", "w"), indent=1)
    np.savez_compressed(
        f"{CASA}/step1_curves.npz",
        t=np.arange(N_FRAMES) * 0.01,
        mix_r_voice=feat_mix["r_voice"], mix_r_max=feat_mix["r_max"],
        mix_r_second=feat_mix["r_second"],
        mix_dominance=feat_mix["dominance"], mix_tau_max=feat_mix["tau_max"],
        mix_tau_voice=feat_mix["tau_voice"], mix_trusted=feat_mix["trusted"],
        stem_r_voice=feat_stem["r_voice"], stem_r_max=feat_stem["r_max"],
        stem_r_second=feat_stem["r_second"],
        stem_dominance=feat_stem["dominance"],
    )
    print("MIX  Bar A:", mix_sum["barA_clean_correct"], "/", mix_sum["barA_clean_total"],
          "pass" if mix_sum["barA_clean_pass"] else "FAIL",
          "| pooled sung r_voice %.4f vs instr r_max %.4f" % (
              mix_sum["pooled_sung_median_r_voice"], mix_sum["pooled_instr_median_r_max"]),
          "| MW p %.3g" % mix_sum["mannwhitney_sung_gt_instr_p"])
    print("MIX  Bar E confusion: %.4f" % mix_sum["barE_confusion_rate_sung"],
          "pass" if mix_sum["barE_pass"] else "FAIL",
          "| trusted sung frames:", mix_sum["n_trusted_sung_frames"])
    print("STEM Bar A:", stem_sum["barA_clean_correct"], "/", stem_sum["barA_clean_total"],
          "pass" if stem_sum["barA_clean_pass"] else "FAIL",
          "| pooled sung r_voice %.4f vs instr r_max %.4f" % (
              stem_sum["pooled_sung_median_r_voice"], stem_sum["pooled_instr_median_r_max"]))
    print("STEM Bar E confusion: %.4f" % stem_sum["barE_confusion_rate_sung"],
          "pass" if stem_sum["barE_pass"] else "FAIL")
    print("CONTROLS:", json.dumps(controls, indent=1))


if __name__ == "__main__":
    main()
