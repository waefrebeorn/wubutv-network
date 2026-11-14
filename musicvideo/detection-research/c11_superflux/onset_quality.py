#!/usr/bin/env python3
"""Bar 3 onset quality: peak-picked onsets vs the MV-14 word grid.

Reference onsets: SONG_WORDS.json word starts (212 words) — the grid
loops 4-6 judged everything against (ASR word starts; no separate
hand-marked onset file exists in the tree).

Peak picking (pre-stated): local maxima (odf[t] > odf[t-1] and
odf[t] >= odf[t+1]) of the max-normalised ODF with value >= 0.20 —
the snapper's existing strong-peak tier (c11_mir snap: flux >= 0.20 =
strong peak). Thresholds 0.10/0.15/0.25/0.30 reported as sensitivity.

Matching: greedy by ascending |dt|, each reference and each peak used
at most once (mir_eval style). F reported at tolerances
25/50/100/150/200 ms (tolerance sensitivity is part of the bar: chant
vowels have slow attacks, +-50 ms may be too tight).

Instrumental spans: complement of the 12 Demucs ref sung segments
(c11_mir/hpss_mv14_ref.json) within [0, 161.6]. An instrumental FP is
an unmatched peak (at the judged tolerance) inside an instrumental
span.

BAR (pre-stated): SuperFlux F >= 0.80 at +-50 ms AND SuperFlux
instrumental FPs strictly fewer than plain mix flux's.
"""
import json
import numpy as np

ODFS = {
    "superflux": ("out/odf_superflux_raw.txt", 0.032),
    "complex": ("out/odf_complex_raw.txt", 0.032),
    "hpss_harm_gated": ("out/odf_hpss_raw.txt", 0.016),
    "f0_gated": ("out/odf_f0gated_raw.txt", 0.016),
    "flux_mix": ("out/odf_flux_raw.txt", 0.016),
}
THRESHOLDS = [0.10, 0.15, 0.20, 0.25, 0.30]
JUDGED_THRESHOLD = 0.20
TOLS = [0.025, 0.050, 0.100, 0.150, 0.200]
JUDGED_TOL = 0.050
DUR = 161.6

words = json.load(open("../../MV-14_clip-it/analysis/SONG_WORDS.json"))["words"]
ref_onsets = np.array([w["start"] for w in words])
ref_segs = json.load(open("../c11_mir/hpss_mv14_ref.json"))["segments"]


def in_instrumental(t):
    return not any(s["start"] <= t <= s["end"] for s in ref_segs)


def peaks(odf, hop, thr):
    o = odf / odf.max()
    idx = [t for t in range(1, len(o) - 1)
           if o[t] >= thr and o[t] > o[t - 1] and o[t] >= o[t + 1]]
    return np.array([t * hop for t in idx])


def match(pk, ref, tol):
    """Greedy ascending-|dt| matching. Returns (tp, matched_peak_mask)."""
    pairs = []
    for i, p in enumerate(pk):
        j = int(np.argmin(np.abs(ref - p)))
        if abs(ref[j] - p) <= tol:
            pairs.append((abs(ref[j] - p), i, j))
    pairs.sort()
    used_p, used_r, tp = set(), set(), 0
    pmask = np.zeros(len(pk), dtype=bool)
    for _, i, j in pairs:
        if i not in used_p and j not in used_r:
            used_p.add(i)
            used_r.add(j)
            pmask[i] = True
            tp += 1
    return tp, pmask


res = {"reference_onsets": int(len(ref_onsets)),
       "reference_source": "MV-14_clip-it/analysis/SONG_WORDS.json word starts",
       "peak_rule": "local max (strict left), normalised ODF >= threshold; judged threshold 0.20",
       "odfs": {}}
for name, (path, hop) in ODFS.items():
    odf = np.loadtxt(path)
    entry = {"hop_s": hop, "thresholds": {}}
    for thr in THRESHOLDS:
        pk = peaks(odf, hop, thr)
        row = {"n_peaks": int(len(pk)), "by_tolerance": {}}
        for tol in TOLS:
            tp, pmask = match(pk, ref_onsets, tol)
            fp = int(len(pk) - tp)
            fn = int(len(ref_onsets) - tp)
            prec = tp / len(pk) if len(pk) else 0.0
            rec = tp / len(ref_onsets)
            f = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
            fp_instr = int(sum(1 for t, m in zip(pk, pmask)
                               if not m and in_instrumental(t)))
            row["by_tolerance"]["%dms" % int(tol * 1000)] = {
                "tp": tp, "fp": fp, "fn": fn,
                "precision": round(prec, 4), "recall": round(rec, 4),
                "f_measure": round(f, 4), "fp_instrumental": fp_instr}
        entry["thresholds"]["%.2f" % thr] = row
    res["odfs"][name] = entry

sf = res["odfs"]["superflux"]["thresholds"]["0.20"]["by_tolerance"]["50ms"]
fl = res["odfs"]["flux_mix"]["thresholds"]["0.20"]["by_tolerance"]["50ms"]
res["bar"] = "SuperFlux F >= 0.80 at +-50 ms (thr 0.20) AND superflux fp_instrumental < flux fp_instrumental"
res["judged"] = {"superflux_f_50ms": sf["f_measure"], "superflux_fp_instrumental": sf["fp_instrumental"],
                "flux_fp_instrumental": fl["fp_instrumental"]}
res["pass"] = bool(sf["f_measure"] >= 0.80 and sf["fp_instrumental"] < fl["fp_instrumental"])
with open("out/onset_quality.json", "w") as f:
    json.dump(res, f, indent=1)

for name, e in res["odfs"].items():
    r = e["thresholds"]["0.20"]
    print("%-16s peaks %4d | " % (name, r["n_peaks"]) +
          "  ".join("F@%dms %.3f" % (int(t * 1000), r["by_tolerance"]["%dms" % int(t * 1000)]["f_measure"]) for t in TOLS) +
          " | FP_instr@50ms %d" % r["by_tolerance"]["50ms"]["fp_instrumental"])
print("BAR 3:", "PASS" if res["pass"] else "FAIL",
      "(SuperFlux F@50ms %.3f, FP_instr SF %d vs flux %d)" % (
          sf["f_measure"], sf["fp_instrumental"], fl["fp_instrumental"]))
