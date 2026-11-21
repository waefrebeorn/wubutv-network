"""Stage A: f0-anchor the Gemini 3.5 Transcribe speaker labels for MV-5.

Evidence base: librosa pyin track (work/pyin_f0.npy + work/pyin_vp.npy,
fmin 65, fmax 500, hop 512 @16k) and aubio YIN track (work/f0_track.npy +
work/f0_conf.npy), both computed on work/tmp_audio.f32. Verified this run:
tmp_audio.f32 and work/gemini/song_16k.wav carry the SAME signal at lag 0
(corr 0.9999999978, identical length 3,302,400 samples) — only a sqrt(2)
gain difference (mono-sum vs mono-mean). f0 estimation is gain-invariant,
so both tracks apply to the Gemini wav as-is.

Outputs:
  work/gemini_f0_segments.json — per-Gemini-segment pyin+aubio stats
  work/gemini_line_f0.json     — per-SONG_WORDS-line pyin stats (Stage B evidence)
  stdout summary for work/gemini_speakers.md
"""
import json, os
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
SR = 16000
HOP = 512

CAT_LO, CAT_HI = 97, 160   # v1: CAT low voice
GIRL_LO, GIRL_HI = 200, 330  # v1: GIRL high voice

pyin = np.load(os.path.join(WORK, "pyin_f0.npy"))
vp = np.load(os.path.join(WORK, "pyin_vp.npy"))
pyin_times = np.arange(len(pyin)) * HOP / SR
aub = np.load(os.path.join(WORK, "f0_track.npy"))
aconf = np.load(os.path.join(WORK, "f0_conf.npy"))
aub_times = np.arange(len(aub)) * HOP / SR


def band_frac(vals):
    """Fraction of voiced values in each band."""
    n = len(vals)
    if n == 0:
        return {"bass_lt80": None, "cat_97_160": None, "mid_160_200": None,
                "girl_200_330": None, "high_gt330": None}
    return {
        "bass_lt80": round(float(np.mean(vals < 80)), 3),
        "cat_97_160": round(float(np.mean((vals >= 97) & (vals <= 160))), 3),
        "mid_160_200": round(float(np.mean((vals > 160) & (vals < 200))), 3),
        "girl_200_330": round(float(np.mean((vals >= 200) & (vals <= 330))), 3),
        "high_gt330": round(float(np.mean(vals > 330)), 3),
    }


def modes(vals):
    """Top-2 10 Hz histogram modes over 65-500 Hz."""
    if len(vals) == 0:
        return []
    hist, edges = np.histogram(vals, bins=np.arange(65, 505, 10))
    order = np.argsort(hist)[::-1][:2]
    return [{"center_hz": int(edges[b] + 5), "frames": int(hist[b])}
            for b in order if hist[b] > 0]


def stats_for(start, end):
    # Zero-length Gemini segments (e.g. 122-122): widen to 1s so the window
    # actually contains the sung line; flagged by caller via duration.
    if end <= start:
        end = start + 1.0
    # Voiced = librosa pyin's own decision (non-NaN). The saved vp array is
    # degenerate here (mean 0.019, only 24/6451 frames > 0.5) and selecting
    # on it keeps a tiny biased subset — it once returned 263 Hz for a
    # 145-160 Hz CAT line because only the next line's onset passed.
    m = (pyin_times >= start) & (pyin_times < end) & ~np.isnan(pyin)
    vals = pyin[m]
    n_total = int(((pyin_times >= start) & (pyin_times < end)).sum())
    ma = (aub_times >= start) & (aub_times < end) & (aconf > 0.5) & (aub >= 60) & (aub <= 500)
    avals = aub[ma]
    out = {
        "pyin_voiced_frames": int(len(vals)),
        "pyin_total_frames": n_total,
        "pyin_coverage": round(len(vals) / n_total, 3) if n_total else None,
        "pyin_median": round(float(np.median(vals)), 1) if len(vals) else None,
        "pyin_p25": round(float(np.percentile(vals, 25)), 1) if len(vals) else None,
        "pyin_p75": round(float(np.percentile(vals, 75)), 1) if len(vals) else None,
        "pyin_bands": band_frac(vals),
        "pyin_modes": modes(vals),
        "aubio_voiced_frames": int(len(avals)),
        "aubio_median": round(float(np.median(avals)), 1) if len(avals) else None,
        "aubio_modes": modes(avals),
    }
    return out


# ---- per-Gemini-segment ----
gem = json.load(open(os.path.join(WORK, "gemini_song.json")))
seg_out = []
for s in gem["segments"]:
    st = stats_for(s["start"], s["end"])
    seg_out.append({**s, **st})
json.dump(seg_out, open(os.path.join(WORK, "gemini_f0_segments.json"), "w"), indent=1)

# ---- per-SONG_WORDS-line ----
sw = json.load(open(os.path.join(BASE, "SONG_WORDS.json")))
line_out = []
for ln in sw["lines"]:
    st = stats_for(ln["start"], ln["end"])
    line_out.append({"id": ln["id"], "section": ln["section"], "text": ln["text"],
                     "start": ln["start"], "end": ln["end"],
                     "v1_owner": ln["owner"], "v1_confidence": ln.get("confidence"),
                     **st})
json.dump(line_out, open(os.path.join(WORK, "gemini_line_f0.json"), "w"), indent=1)

# ---- summary ----
def label_agg(label):
    rows = [r for r in seg_out if r["speaker"] == label]
    meds = [r["pyin_median"] for r in rows if r["pyin_median"] is not None]
    tot_v = sum(r["pyin_voiced_frames"] for r in rows)
    # pooled band fractions (frame-weighted)
    pooled = {}
    for k in ["bass_lt80", "cat_97_160", "mid_160_200", "girl_200_330", "high_gt330"]:
        num = sum(r["pyin_bands"][k] * r["pyin_voiced_frames"] for r in rows
                  if r["pyin_bands"][k] is not None)
        pooled[k] = round(num / tot_v, 3) if tot_v else None
    in_cat = sum(1 for m in meds if 97 <= m <= 160)
    in_girl = sum(1 for m in meds if 200 <= m <= 330)
    return {"segments": len(rows), "voiced_frames": tot_v,
            "median_of_medians": round(float(np.median(meds)), 1) if meds else None,
            "median_range": (round(min(meds), 1), round(max(meds), 1)) if meds else None,
            "segs_median_in_cat_band": in_cat, "segs_median_in_girl_band": in_girl,
            "pooled_bands": pooled}

print("== per-label aggregates (pyin) ==")
for lab in ["spk_0", "spk_1", "spk_2"]:
    print(lab, json.dumps(label_agg(lab)))

print("\n== spk_2 segments (the question) ==")
for r in seg_out:
    if r["speaker"] == "spk_2":
        print(f"{r['start']:>4}-{r['end']:<4} med={r['pyin_median']} p25={r['pyin_p25']} p75={r['pyin_p75']} "
              f"n={r['pyin_voiced_frames']} bands={r['pyin_bands']} modes={r['pyin_modes']} "
              f"aubio_med={r['aubio_median']} :: {r['text'][:40]}")

print("\n== spk_1 'Easy now' segments (same text, comparison set) ==")
for r in seg_out:
    if r["speaker"] == "spk_1" and r["text"].startswith("Easy now"):
        print(f"{r['start']:>4}-{r['end']:<4} med={r['pyin_median']} p25={r['pyin_p25']} p75={r['pyin_p75']} "
              f"n={r['pyin_voiced_frames']} girl_frac={r['pyin_bands']['girl_200_330']} modes={r['pyin_modes']}")

print("\n== spk_0 segments with median in/near GIRL band (possible cross-label) ==")
for r in seg_out:
    if r["speaker"] == "spk_0" and r["pyin_median"] is not None and r["pyin_median"] >= 180:
        print(f"{r['start']:>4}-{r['end']:<4} med={r['pyin_median']} bands={r['pyin_bands']} :: {r['text'][:60]}")
print("\n== spk_1 segments with median in/near CAT band ==")
for r in seg_out:
    if r["speaker"] == "spk_1" and r["pyin_median"] is not None and r["pyin_median"] <= 180:
        print(f"{r['start']:>4}-{r['end']:<4} med={r['pyin_median']} bands={r['pyin_bands']} :: {r['text'][:60]}")
print("\nsegments written:", len(seg_out), "lines written:", len(line_out))
