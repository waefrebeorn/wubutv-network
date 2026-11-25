"""Day-1 falsifier for c11_vibrato (loop 3 top-1, SPRINT_SCOPE.md step 1).

Question: does the MV-14 MIX F0 track carry 5-7 Hz vibrato modulation
in sung spans that is absent in instrumental spans?

Method (Python, validation-only; the C tool comes after the falsifier passes):
- Load sprint-8's mix F0 track (voice_mv14.json, 10 ms hop, 16161 frames).
- Two contours: pYIN f0_hz (0=unvoiced; interpolate log-F0 across gaps,
  trust only frames within 0.25 s of a voiced frame) and raw YIN f0_yin
  (continuous but noisy; 5-frame median to kill octave spikes).
- Detrend: subtract 0.51 s moving average (removes vibrato, keeps drift).
- Bandpass 4-8 Hz (Butterworth order 4, filtfilt) on detrended cents.
- Modulation depth per frame = RMS of bandpassed cents over a 0.5 s
  sliding window, smoothed ~100 ms.
- Compare depth on sung spans (ref segments 1-10) vs instrumental spans
  (outside all ref segments), plus the outro (128.20-161.60) and ref 11-12
  separately. Also a spectral check: mean PSD of detrended cents in each class.

No C code, no gate, no thresholding here — measurement only.
"""
import json
import numpy as np
from scipy.signal import butter, filtfilt

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
VOICE = f"{DR}/c11_voice/voice_mv14.json"
REF = f"{DR}/c11_mir/hpss_mv14_ref.json"
OUT = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_vibrato/day1_falsifier.json"

v = json.load(open(VOICE))
frames = v["frames"]
t = np.array([f["t"] for f in frames])
f0_pyin = np.array([f["f0_hz"] for f in frames], dtype=float)
f0_yin = np.array([f["f0_yin"] for f in frames], dtype=float)
pyin_voiced = np.array([f["pyin_voiced"] for f in frames], dtype=bool)
hop = 0.010
fs = 1.0 / hop  # 100 Hz contour sample rate
n = len(t)

ref = json.load(open(REF))["segments"]
ref_segs = [(s["start"], s["end"]) for s in ref]
sung_clean = ref_segs[:10]          # ref 1-10: real sung spans
bleed = ref_segs[10:]               # ref 11-12: wordless-outro Demucs bleed

def in_spans(tt, spans):
    m = np.zeros(len(tt), dtype=bool)
    for a, b in spans:
        m |= (tt >= a) & (tt <= b)
    return m

is_sung = in_spans(t, sung_clean)
is_bleed = in_spans(t, bleed)
is_instr = ~(is_sung | is_bleed)    # outside ALL ref segments
is_outro = (t >= 128.20)            # confirmed wordless ride-out

def moving_average(x, w):
    # centred moving average, edge-padded (w odd)
    pad = w // 2
    xp = np.pad(x, pad, mode="edge")
    return np.convolve(xp, np.ones(w) / w, mode="valid")

def depth_curve(f0, voiced_mask=None, trust_radius_s=0.25):
    """Return (depth_cents_per_frame, trusted_mask)."""
    logf = np.log2(np.maximum(f0, 1.0))
    if voiced_mask is not None:
        # interpolate log-F0 across unvoiced gaps
        idx = np.arange(n)
        good = voiced_mask & (f0 > 0)
        logf_i = np.interp(idx, idx[good], logf[good])
        # trusted = within trust_radius of a voiced frame
        dist = np.abs(idx[:, None] - idx[good][None, :]).min(axis=1)
        trusted = dist * hop <= trust_radius_s
    else:
        logf_i = logf
        trusted = np.ones(n, dtype=bool)
    cents = 1200.0 * (logf_i - moving_average(logf_i, 51))  # detrend 0.51 s
    # 5-frame median to kill octave spikes (raw YIN only matters, harmless for pYIN)
    from scipy.ndimage import median_filter
    cents = median_filter(cents, size=5, mode="nearest")
    cents = cents - moving_average(cents, 51)  # re-detrend after median
    b, a = butter(4, [4.0, 8.0], btype="band", fs=fs)
    bp = filtfilt(b, a, cents)
    # sliding RMS over 0.5 s window, then ~100 ms smooth
    w = 51
    rms = np.sqrt(moving_average(bp ** 2, w))
    depth = moving_average(rms, 11)
    return depth, trusted, bp, cents

def stats(name, depth, mask):
    d = depth[mask]
    q = np.percentile(d, [25, 50, 75])
    return {"n_frames": int(mask.sum()),
            "median_cents": round(float(q[1]), 2),
            "q1_cents": round(float(q[0]), 2),
            "q3_cents": round(float(q[2]), 2),
            "mean_cents": round(float(d.mean()), 2)}

def psd_peak(cents, mask, label):
    # mean PSD of detrended cents over the masked frames, via Welch on 2 s blocks
    from scipy.signal import welch
    f, p = welch(cents, fs=fs, nperseg=200)
    # restrict to blocks fully inside the mask: approximate by zeroing outside
    x = np.where(mask, cents, 0.0)
    f, p = welch(x, fs=fs, nperseg=200)
    band = (f >= 3) & (f <= 10)
    pk = f[band][np.argmax(p[band])]
    return {"peak_hz": round(float(pk), 2),
            "power_4_8hz": round(float(p[(f >= 4) & (f <= 8)].sum()), 4),
            "power_2_4hz": round(float(p[(f >= 2) & (f < 4)].sum()), 4),
            "power_8_12hz": round(float(p[(f > 8) & (f <= 12)].sum()), 4)}

results = {"track": "MV-14 mix, sprint-8 voice_mv14.json (16161 frames, 10 ms hop)",
           "ref": "hpss_mv14_ref.json, 12 segments; sung=1-10, bleed=11-12",
           "n_frames": n,
           "pyin_voiced_frames": int(pyin_voiced.sum()),
           "pyin_voiced_frac": round(float(pyin_voiced.mean()), 4)}

for label, f0, vm in (("pyin", f0_pyin, pyin_voiced), ("raw_yin", f0_yin, None)):
    depth, trusted, bp, cents = depth_curve(f0, vm)
    cov_sung = float((trusted & is_sung).sum() / max(is_sung.sum(), 1))
    cov_instr = float((trusted & is_instr).sum() / max(is_instr.sum(), 1))
    entry = {
        "coverage_sung_trusted_frac": round(cov_sung, 3),
        "coverage_instr_trusted_frac": round(cov_instr, 3),
        "sung": stats(label, depth, is_sung & trusted),
        "instrumental": stats(label, depth, is_instr & trusted),
        "bleed_ref11_12": stats(label, depth, is_bleed & trusted),
        "outro": stats(label, depth, is_outro & trusted),
        "psd_sung": psd_peak(cents, is_sung, label),
        "psd_instrumental": psd_peak(cents, is_instr, label),
    }
    # per-ref-segment medians (sung spans 1-10 + bleed 11-12)
    entry["per_segment_median_cents"] = []
    for i, (a, b) in enumerate(ref_segs, 1):
        m = (t >= a) & (t <= b) & trusted
        entry["per_segment_median_cents"].append(
            {"seg": i, "start": a, "end": b,
             "median": round(float(np.median(depth[m])), 2) if m.sum() else None,
             "trusted_frac": round(float(m.sum() / max(((t >= a) & (t <= b)).sum(), 1)), 3)})
    results[label] = entry
    np.save(f"/home/hatch/workspace/wubutv-network/musicvideo/detection-research/c11_vibrato/day1_depth_{label}.npy", depth)

json.dump(results, open(OUT, "w"), indent=1)
for label in ("pyin", "raw_yin"):
    e = results[label]
    print(f"--- {label} (trusted coverage sung {e['coverage_sung_trusted_frac']}, instr {e['coverage_instr_trusted_frac']}) ---")
    print("  sung median/IQR:", e["sung"]["median_cents"], f"[{e['sung']['q1_cents']},{e['sung']['q3_cents']}]",
          " instrumental:", e["instrumental"]["median_cents"], f"[{e['instrumental']['q1_cents']},{e['instrumental']['q3_cents']}]")
    print("  bleed 11-12 median:", e["bleed_ref11_12"]["median_cents"], " outro median:", e["outro"]["median_cents"])
    print("  PSD peak sung:", e["psd_sung"]["peak_hz"], "Hz  instr:", e["psd_instrumental"]["peak_hz"], "Hz")
    print("  per-segment medians:", [s["median"] for s in e["per_segment_median_cents"]])
print("wrote", OUT)
