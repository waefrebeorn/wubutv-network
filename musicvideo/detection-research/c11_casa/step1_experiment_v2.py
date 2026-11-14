"""Step-1 experiment v2 for c11_casa (Bar A / Bar E, fail-fast).

SUPERSEDES v1 (step1_experiment_v1_seedmix.json): v1 seeded the voice lag
from the mix pYIN Viterbi path (voice_mv14.json f0_hz). SEED AUDIT showed
that path is pinned at the 50 Hz fmin floor on 2525/3101 voiced frames
(81%) — it tracks the mix's dominant periodicity (the bass), not the
voice. The stem pYIN path is pinned at the 800 Hz fmax ceiling on
1148/1825 voiced frames (63%) — octave runaway. NEITHER saved pYIN track
is a voice-F0 track (both faithfully reproduce librosa.pyin's systematic
bias on this material: the C code reimplements librosa's pYIN, so the
"validation" correlates two implementations of the same algorithm, not
the algorithm against truth). v1 therefore measured a 50 Hz bass lag, not
a voice lag — its Bar A 0/22 / confusion 95.5% are WITHDRAWN as a voice
test (the numbers are correct measurements of the bass lag; the
interpretation was wrong).

v2 seeds the voice lag EMPIRICALLY from the isolated Demucs vocal stem:
tau_voice(t) = the stem autocorrelation's top peak in the vocal lag
range [27, 200] (80-600 Hz), median-filtered over 11 frames (110 ms),
trusted only where the stem frame has RMS > 1% of max AND stem r_max >
0.2. The stem IS the voice isolated; its dominant in-range periodicity
is the voice (plus small Demucs bleed). The mix is then tested for a
peak at THAT lag during sung spans. The stem is the reference, not a
second Bar A test (r_voice on the stem = r_max by construction on
trusted frames) — the stem leg of v2 is a STABILITY check: is the
voice's lag stable/continuous enough to be a reference at all?

Method — per-frame FFT autocorrelation (same framing as sprint 8:
1024-sample Hann, 160-sample hop, centred, zero-padded, 16,161 frames):
  - r(tau) normalized by r(0), tau = 0..512. Vocal range tau [27, 200].
  - Per-frame mix features: r_voice = mix r(tau_voice); r_max = max mix
    r(tau) over the vocal range; dominance = 1 if the mix top peak is at
    tau_voice (+-2), 2*tau_voice (+-4), or tau_voice/2 (+-2) — the
    voice-consistent lag set (octave-aware from the start; v1's strict
    rule penalized the voice's own octave, which the follow-up showed
    accounts for only 0.1% of frames — the confusion was real, but the
    rule is now correct by construction).
  - Spans: sung = ref 1-10; bleed = 11-12 (instrumental-class, reported
    separately); instrumental = complement of the union of all 12 ref
    segments (12 spans: intro + 10 gaps + outro). Clean spans 22, total 24.
  - Bar A (same scoring as v1): sung span separates if median r_voice >
    pooled instrumental median r_max; instrumental span separates if
    median r_max < pooled sung median r_voice. Pass >= 18/22 clean (80%).
  - Bar E (multipitch confusion): over sung frames with a trusted stem
    reference, confused if the mix top peak is outside the
    voice-consistent lag set. Pass = confusion <= 20%.

Controls: same synthetics as v1 (voice-only 220 Hz dominance 1;
mixture 220+98+147; accompaniment-only absence) — they validate the
pipeline, and they reproduce identically.

Outputs: step1_experiment.json (v2 numbers) + step1_curves.npz.
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

VOCAL_LO, VOCAL_HI = 27, 200      # 80-600 Hz
WIDE_LO, WIDE_HI = 20, 320        # 50-800 Hz (sensitivity)

REF = json.load(open(f"{DR}/c11_mir/hpss_mv14_ref.json"))["segments"]
SEGS = [(s["start"], s["end"]) for s in REF]
SUNG = SEGS[:10]
BLEED = SEGS[10:]


def frame_signal(x):
    n = len(x)
    idx = np.arange(N_FRAMES)[:, None] * HOP + np.arange(WIN)[None, :] - WIN // 2
    valid = (idx >= 0) & (idx < n)
    xf = np.zeros((N_FRAMES, WIN), dtype=np.float64)
    xf[valid] = x[np.clip(idx[valid], 0, n - 1)]
    return xf * np.hanning(WIN)


def autocorr(frames):
    nfft = 2048
    spec = np.fft.rfft(frames, n=nfft, axis=1)
    ac = np.fft.irfft(spec * np.conj(spec), n=nfft, axis=1)[:, :513]
    r0 = ac[:, 0:1]
    return ac / np.where(r0 > 0, r0, 1.0)


def frame_rms(frames):
    return np.sqrt(np.mean(frames ** 2, axis=1))


def median_filter(a, w=11):
    pad = w // 2
    ap = np.pad(a, pad, mode="edge")
    return np.array([np.median(ap[i:i + w]) for i in range(len(a))])


def voice_lag_reference(stem_r, stem_rms):
    """tau_voice(t) from the stem's own top in-range peak.

    Smoothed (11-frame median), trusted where the stem is loud enough
    (RMS > 1% of max) and has a real periodic peak (r_max > 0.2).
    Returns (tau_ref, trusted, tau_raw, r_max_stem).
    """
    seg = stem_r[:, VOCAL_LO:VOCAL_HI + 1]
    r_max = seg.max(axis=1)
    tau_raw = seg.argmax(axis=1) + VOCAL_LO
    tau_ref = median_filter(tau_raw.astype(float), 11).astype(int)
    tau_ref = np.clip(tau_ref, VOCAL_LO, VOCAL_HI)
    trusted = (stem_rms > 0.01 * stem_rms.max()) & (r_max > 0.2)
    return tau_ref, trusted, tau_raw, r_max


def mix_features(mix_r, tau_ref, trusted):
    n = mix_r.shape[0]
    r_voice = np.full(n, np.nan)
    r_second = np.full(n, np.nan)
    r_max = mix_r[:, VOCAL_LO:VOCAL_HI + 1].max(axis=1)
    tau_max = mix_r[:, VOCAL_LO:VOCAL_HI + 1].argmax(axis=1) + VOCAL_LO
    r_max_wide = mix_r[:, WIDE_LO:WIDE_HI + 1].max(axis=1)
    for i in range(n):
        if not trusted[i]:
            continue
        tv = tau_ref[i]
        r_voice[i] = mix_r[i, tv]
        seg = mix_r[i, VOCAL_LO:VOCAL_HI + 1]
        lo = max(VOCAL_LO, tv - 3)
        hi = min(VOCAL_HI, tv + 3)
        mask = np.ones(VOCAL_HI - VOCAL_LO + 1, dtype=bool)
        mask[lo - VOCAL_LO:hi - VOCAL_LO + 1] = False
        r_second[i] = seg[mask].max() if mask.any() else np.nan
    # voice-consistent lag set: tau, 2*tau, tau/2
    in_set = (
        (np.abs(tau_max - tau_ref) <= 2)
        | (np.abs(tau_max - 2 * tau_ref) <= 4)
        | (np.abs(tau_max - tau_ref / 2.0) <= 2)
    )
    dominance = np.where(trusted & ~np.isnan(r_voice), in_set.astype(float), np.nan)
    return {
        "r_voice": r_voice, "r_max": r_max, "r_max_wide": r_max_wide,
        "tau_max": tau_max, "tau_ref": tau_ref, "trusted": trusted,
        "dominance": dominance, "r_second": r_second,
    }


def instrumental_spans():
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
    sung_mask = np.zeros(N_FRAMES, dtype=bool)
    for a, b in SUNG:
        sung_mask |= (t >= a) & (t < b)
    instr_mask = np.zeros(N_FRAMES, dtype=bool)
    for a, b in instr:
        instr_mask |= (t >= a) & (t < b)
    sung_rv = rv[sung_mask & ~np.isnan(rv)]
    instr_rm = rm[instr_mask & ~np.isnan(rm)]
    pooled_sung = float(np.median(sung_rv)) if len(sung_rv) else float("nan")
    pooled_instr = float(np.median(instr_rm)) if len(instr_rm) else float("nan")
    try:
        mw_p = float(mannwhitneyu(sung_rv, instr_rm, alternative="greater").pvalue)
    except Exception:
        mw_p = float("nan")
    spans_out = []
    correct_clean = total_clean = correct_all = total_all = 0
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
    dom = feat["dominance"][sung_mask]
    dom = dom[~np.isnan(dom)]
    confusion = float(1.0 - dom.mean()) if len(dom) else float("nan")
    rmw = feat["r_max_wide"]
    return {
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
        "wide_range_pooled_sung_median_r_max": float(np.median(rmw[sung_mask])),
        "wide_range_pooled_instr_median_r_max": float(np.median(rmw[instr_mask])),
        "spans": spans_out,
    }


def synth_tone(f0s, amps, dur=2.0, sr=SR, seed=0):
    rng = np.random.default_rng(seed)
    n = int(dur * sr)
    tt = np.arange(n) / sr
    x = np.zeros(n)
    for f0, amp in zip(f0s, amps):
        for k in range(1, 9):
            x += amp / k * np.sin(2 * np.pi * f0 * k * tt + rng.uniform(0, 2 * np.pi))
    return x / max(1e-9, np.abs(x).max()) * 0.5


def run_controls():
    out = {}
    for name, f0s, amps in [
        ("voice_only_220Hz", [220], [1.0]),
        ("mixture_220_98_147", [220, 98, 147], [1.0, 1.0, 1.0]),
        ("accompaniment_only_98_147", [98, 147], [1.0, 1.0]),
    ]:
        x = synth_tone(f0s, amps)
        fr = frame_signal(np.concatenate([np.zeros(512), x, np.zeros(512)]))[:200]
        r = autocorr(fr)
        tv = round(SR / 220)
        out[name] = {
            "r_at_voice_lag_220Hz": float(np.median(r[50:150, tv])),
            "r_max_vocal_range": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].max(axis=1))),
            "tau_max_median": float(np.median(r[50:150, VOCAL_LO:VOCAL_HI + 1].argmax(axis=1) + VOCAL_LO)),
        }
    return out


def seed_audit():
    """pYIN pinning counts (the finding that invalidated v1's seed)."""
    out = {}
    for name, path in [("mix", f"{DR}/c11_voice/voice_mv14.json"),
                       ("stem", f"{DR}/c11_voice/voice_mv14_stem.json")]:
        v = json.load(open(path))
        f0 = np.array([f["f0_hz"] for f in v["frames"]])
        pv = np.array([f["pyin_voiced"] for f in v["frames"]])
        out[name] = {
            "voiced_frames": int(pv.sum()),
            "at_fmin_50Hz": int(((f0[pv] == 50.0)).sum()),
            "at_fmax_800Hz": int(((f0[pv] == 800.0)).sum()),
            "median_f0_voiced": float(np.median(f0[pv])) if pv.sum() else float("nan"),
            "frac_voiced_in_125_350Hz": float(((f0[pv] >= 125) & (f0[pv] <= 350)).mean()) if pv.sum() else float("nan"),
        }
    return out


def main():
    sr, mix = wavfile.read(f"{DR}/c11_mir/mv14_16k.wav")
    assert sr == SR
    mix = mix.astype(np.float64) / 32768.0
    sr2, stem = wavfile.read("/tmp/mv14_stem_16k.wav")
    assert sr2 == SR
    stem = stem.astype(np.float64) / 32768.0

    mix_fr = frame_signal(mix)
    stem_fr = frame_signal(stem)
    mix_r = autocorr(mix_fr)
    stem_r = autocorr(stem_fr)
    stem_rms = frame_rms(stem_fr)

    tau_ref, trusted, tau_raw, r_max_stem = voice_lag_reference(stem_r, stem_rms)
    feat = mix_features(mix_r, tau_ref, trusted)
    mix_sum = summarize(feat, "mix")

    # stem stability: is the voice's lag stable enough to be a reference?
    t = np.arange(N_FRAMES) * 0.01
    sung_mask = np.zeros(N_FRAMES, dtype=bool)
    for a, b in SUNG:
        sung_mask |= (t >= a) & (t < b)
    tr_sung = trusted & sung_mask
    raw = tau_raw[tr_sung]
    refd = tau_ref[tr_sung]
    # fraction of trusted sung frames where the raw top peak is within +-2 of the smoothed ref
    stable_frac = float((np.abs(raw - refd) <= 2).mean()) if len(raw) else float("nan")
    f0_ref = SR / refd.astype(float)
    stability = {
        "n_trusted_sung_frames": int(tr_sung.sum()),
        "frac_raw_top_peak_within_2_of_smoothed_ref": stable_frac,
        "ref_lag_median_samples": float(np.median(refd)) if len(refd) else float("nan"),
        "ref_f0_median_Hz": float(np.median(f0_ref)) if len(f0_ref) else float("nan"),
        "ref_f0_IQR_Hz": [float(np.percentile(f0_ref, 25)), float(np.percentile(f0_ref, 75))] if len(f0_ref) else [float("nan"), float("nan")],
        "ref_lag_per_segment_median": [],
    }
    for j, (a, b) in enumerate(SUNG):
        m = (t >= a) & (t < b) & trusted
        if m.sum():
            stability["ref_lag_per_segment_median"].append(
                {"seg": j + 1, "median_tau": float(np.median(tau_ref[m])),
                 "median_f0_Hz": float(SR / np.median(tau_ref[m])), "n": int(m.sum())})
    # octave check on the stem: fraction of trusted sung frames where the top peak is at 2x the smoothed ref
    oct_frac = float((np.abs(raw - 2 * refd) <= 4).mean()) if len(raw) else float("nan")
    stability["frac_raw_top_peak_at_octave_of_ref"] = oct_frac

    controls = run_controls()
    audit = seed_audit()

    result = {
        "experiment": "c11_casa step 1 v2 — voice-lag peak separation (Bar A) + multipitch confusion (Bar E). Voice lag seeded EMPIRICALLY from the isolated Demucs stem autocorrelation (v1 seeded from the mix pYIN Viterbi path and is WITHDRAWN — see seed_audit).",
        "method": "per-frame FFT autocorrelation, 1024 Hann / 160 hop / centred, lags 27-200 (80-600 Hz vocal range); tau_voice = stem top in-range peak, 11-frame median smoothed, trusted where stem RMS > 1% max and stem r_max > 0.2; octave-aware dominance (tau, 2*tau, tau/2)",
        "ref": "hpss_mv14_ref.json, 12 segments (sung 1-10, bleed 11-12); instrumental spans = complement of the union of all 12 within [0, 161.6] (12 spans); clean spans 22, total with bleed 24",
        "seed_audit": audit,
        "stem_stability": stability,
        "mix": mix_sum,
        "controls": controls,
        "verdict": {
            "barA_mix": "PASS" if mix_sum["barA_clean_pass"] else "FAIL",
            "barE_mix": "PASS" if mix_sum["barE_pass"] else "FAIL",
        },
    }
    json.dump(result, open(f"{CASA}/step1_experiment.json", "w"), indent=1)
    np.savez_compressed(
        f"{CASA}/step1_curves.npz",
        t=t,
        mix_r_voice=feat["r_voice"], mix_r_max=feat["r_max"],
        mix_r_second=feat["r_second"],
        mix_dominance=feat["dominance"], mix_tau_max=feat["tau_max"],
        tau_ref=tau_ref, trusted=trusted,
        stem_r_max=r_max_stem, stem_tau_raw=tau_raw,
    )
    print("V2 MIX Bar A:", mix_sum["barA_clean_correct"], "/", mix_sum["barA_clean_total"],
          "pass" if mix_sum["barA_clean_pass"] else "FAIL",
          "| pooled sung r_voice %.4f vs instr r_max %.4f" % (
              mix_sum["pooled_sung_median_r_voice"], mix_sum["pooled_instr_median_r_max"]),
          "| MW p %.3g" % mix_sum["mannwhitney_sung_gt_instr_p"])
    print("V2 MIX Bar E confusion (octave-aware): %.4f" % mix_sum["barE_confusion_rate_sung"],
          "pass" if mix_sum["barE_pass"] else "FAIL",
          "| trusted sung frames:", mix_sum["n_trusted_sung_frames"])
    print("STEM stability: trusted sung frames", stability["n_trusted_sung_frames"],
          "| raw top peak within +-2 of smoothed ref: %.3f" % stable_frac,
          "| at octave: %.3f" % oct_frac,
          "| ref F0 median %.1f Hz IQR [%.1f, %.1f]" % (
              stability["ref_f0_median_Hz"], stability["ref_f0_IQR_Hz"][0], stability["ref_f0_IQR_Hz"][1]))
    print("SEED AUDIT:", json.dumps(audit, indent=1))
    print("CONTROLS:", json.dumps(controls, indent=1))


if __name__ == "__main__":
    main()
