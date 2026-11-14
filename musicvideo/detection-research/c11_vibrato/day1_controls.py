"""Controls for the day-1 falsifier — run BEFORE concluding anything.

1. SYNTHETIC validation of the depth pipeline itself:
   - 6 Hz vibrato, +/-50 cents sine -> expect depth ~35 cents (50/sqrt(2)).
   - 6 Hz vibrato, +/-5 cents sine -> expect depth ~3.5 cents.
   - Straight tone (0 cents) -> expect depth ~0.
   - 3 Hz wobble +/-50 cents -> expect depth ~35 cents too (band is 4-8 Hz,
     so a 3 Hz wobble should be ATTENUATED by the bandpass — check how much).
   If the pipeline cannot recover synthetic 6 Hz vibrato, the null result
   on the mix is meaningless.
2. STEM control: same measurement on the Demucs vocal stem F0 track
   (voice_mv14_stem.json). The stem isolates the voice.
   - If the stem shows clear 5-7 Hz vibrato in sung spans, vibrato EXISTS
     but the mix F0 track cannot see it (accompaniment dominates) — the
     mix sensor still fails, but the diagnosis differs.
   - If the stem is ALSO flat (~2-3 cents), the chant is genuinely
     straight-tone — the cleanest FAIL FAST.
3. Per-block spectral check: Welch PSD on continuous sung blocks only
   (no zero-masking), mix + stem.
"""
import json
import numpy as np
from scipy.signal import butter, filtfilt, welch
from scipy.ndimage import median_filter

DR = "/home/hatch/workspace/wubutv-network/musicvideo/detection-research"
OUT = f"{DR}/c11_vibrato/day1_controls.json"
fs = 100.0  # 10 ms hop

def moving_average(x, w):
    pad = w // 2
    xp = np.pad(x, pad, mode="edge")
    return np.convolve(xp, np.ones(w) / w, mode="valid")

def depth_of_cents(cents):
    """Detrend (0.51 s MA) + 4-8 Hz bandpass + 0.5 s RMS + 100 ms smooth."""
    c = cents - moving_average(cents, 51)
    c = median_filter(c, size=5, mode="nearest")
    c = c - moving_average(c, 51)
    b, a = butter(4, [4.0, 8.0], btype="band", fs=fs)
    bp = filtfilt(b, a, c)
    rms = np.sqrt(moving_average(bp ** 2, 51))
    return moving_average(rms, 11), bp, c

# --- 1. synthetic ---
rng = np.random.default_rng(0)
n = 16161
tt = np.arange(n) / fs
synth = {}
for label, cents in [
    ("vib6Hz_pm50", 50 * np.sin(2 * np.pi * 6.0 * tt)),
    ("vib6Hz_pm5", 5 * np.sin(2 * np.pi * 6.0 * tt)),
    ("straight", np.zeros(n)),
    ("wobble3Hz_pm50", 50 * np.sin(2 * np.pi * 3.0 * tt)),
    ("vib6Hz_pm50_plus_noise10", 50 * np.sin(2 * np.pi * 6.0 * tt) + rng.normal(0, 10, n)),
]:
    d, _, _ = depth_of_cents(cents)
    mid = d[1000:-1000]  # trim filter edges
    synth[label] = {"median_cents": round(float(np.median(mid)), 2),
                    "mean_cents": round(float(mid.mean()), 2)}
    print("synth", label, "-> median", synth[label]["median_cents"], "mean", synth[label]["mean_cents"])

# --- 2. stem control ---
v = json.load(open(f"{DR}/c11_voice/voice_mv14_stem.json"))
frames = v["frames"]
t = np.array([f["t"] for f in frames])
f0_pyin = np.array([f["f0_hz"] for f in frames], dtype=float)
f0_yin = np.array([f["f0_yin"] for f in frames], dtype=float)
pyin_voiced = np.array([f["pyin_voiced"] for f in frames], dtype=bool)
n = len(t)
ref = json.load(open(f"{DR}/c11_mir/hpss_mv14_ref.json"))["segments"]
ref_segs = [(s["start"], s["end"]) for s in ref]
sung_clean, bleed = ref_segs[:10], ref_segs[10:]

def in_spans(tt, spans):
    m = np.zeros(len(tt), dtype=bool)
    for a, b in spans:
        m |= (tt >= a) & (tt <= b)
    return m

is_sung = in_spans(t, sung_clean)
is_bleed = in_spans(t, bleed)
is_instr = ~(is_sung | is_bleed)
is_outro = t >= 128.20

def stem_depth(f0, voiced_mask=None):
    logf = np.log2(np.maximum(f0, 1.0))
    if voiced_mask is not None:
        idx = np.arange(n)
        good = voiced_mask & (f0 > 0)
        logf_i = np.interp(idx, idx[good], logf[good])
        dist = np.abs(idx[:, None] - idx[good][None, :]).min(axis=1)
        trusted = dist * 0.010 <= 0.25
    else:
        logf_i, trusted = logf, np.ones(n, dtype=bool)
    cents = 1200.0 * logf_i
    d, bp, c = depth_of_cents(cents)
    return d, trusted, bp, c

def st(d, m):
    q = np.percentile(d[m], [25, 50, 75])
    return {"n": int(m.sum()), "median": round(float(q[1]), 2),
            "q1": round(float(q[0]), 2), "q3": round(float(q[2]), 2)}

def block_psd(cents, mask):
    """Welch PSD averaged over continuous masked blocks >= 2 s."""
    segs = []
    m = mask.copy()
    i = 0
    while i < len(m):
        if m[i]:
            j = i
            while j < len(m) and m[j]:
                j += 1
            if (j - i) >= 200:
                segs.append(cents[i:j])
            i = j
        else:
            i += 1
    if not segs:
        return None
    ps = []
    for s in segs:
        f, p = welch(s, fs=fs, nperseg=200)
        ps.append(p)
    p = np.mean(ps, axis=0)
    band = (f >= 3) & (f <= 10)
    pk = f[band][np.argmax(p[band])]
    return {"peak_hz": round(float(pk), 2),
            "p_4_8": round(float(p[(f >= 4) & (f <= 8)].sum()), 5),
            "p_2_4": round(float(p[(f >= 2) & (f < 4)].sum()), 5),
            "p_8_12": round(float(p[(f > 8) & (f <= 12)].sum()), 5),
            "n_blocks": len(segs)}

stem = {"pyin_voiced_frames": int(pyin_voiced.sum()),
        "pyin_voiced_frac": round(float(pyin_voiced.mean()), 4)}
for label, f0, vm in (("pyin", f0_pyin, pyin_voiced), ("raw_yin", f0_yin, None)):
    d, trusted, bp, c = stem_depth(f0, vm)
    e = {"coverage_sung": round(float((trusted & is_sung).sum() / is_sung.sum()), 3),
         "coverage_instr": round(float((trusted & is_instr).sum() / is_instr.sum()), 3),
         "sung": st(d, is_sung & trusted),
         "instrumental": st(d, is_instr & trusted),
         "bleed": st(d, is_bleed & trusted),
         "outro": st(d, is_outro & trusted),
         "psd_sung_blocks": block_psd(c, is_sung),
         "psd_instr_blocks": block_psd(c, is_instr),
         "per_segment_median": []}
    for i, (a, b) in enumerate(ref_segs, 1):
        m = (t >= a) & (t <= b) & trusted
        e["per_segment_median"].append({"seg": i, "median": round(float(np.median(d[m])), 2) if m.sum() else None})
    stem[label] = e
    print(f"--- stem {label} (coverage sung {e['coverage_sung']}, instr {e['coverage_instr']}) ---")
    print("  sung:", e["sung"], " instr:", e["instrumental"], " bleed:", e["bleed"], " outro:", e["outro"])
    print("  PSD peak sung:", e["psd_sung_blocks"], "\n  PSD peak instr:", e["psd_instr_blocks"])
    print("  per-seg medians:", [s["median"] for s in e["per_segment_median"]])

# also re-run block PSD on the MIX pYIN cents for a clean spectral comparison
vm = json.load(open(f"{DR}/c11_voice/voice_mv14.json"))
mf = vm["frames"]
mt = np.array([f["t"] for f in mf])
mf0 = np.array([f["f0_hz"] for f in mf], dtype=float)
mvoiced = np.array([f["pyin_voiced"] for f in mf], dtype=bool)
idx = np.arange(len(mt))
good = mvoiced & (mf0 > 0)
logf = np.log2(np.maximum(mf0, 1.0))
logf_i = np.interp(idx, idx[good], logf[good])
mcents = 1200.0 * logf_i
_, _, mc = depth_of_cents(mcents)
mix_psd = {"sung": block_psd(mc, in_spans(mt, sung_clean)),
           "instr": block_psd(mc, ~(in_spans(mt, sung_clean) | in_spans(mt, bleed)))}
print("mix pYIN block PSD:", mix_psd)

json.dump({"synthetic": synth, "stem": stem, "mix_block_psd": mix_psd}, open(OUT, "w"), indent=1)
print("wrote", OUT)
