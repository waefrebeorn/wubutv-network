#!/usr/bin/env python3
"""Bar 2 (the loop-6 Bar C fixture, new signal class): do the SuperFlux-
family ODFs separate the 5 known MV-14 snap errors from the 15 controls?

Fixture (identical to MDX_STEMACT Bar C): errors = 1-based idx
34, 56, 60, 112, 162 into snap_mix_mv14.json; controls = loop-4 rule
(|correction| <= 0.05 s, prob >= 0.9, on_peak, first 15): idx 11, 17,
19, 26, 40, 58, 63, 64, 68, 73, 83, 85, 88, 91, 92.

Statistics per word, per ODF (ODF max-normalised to 1 first; the test
is rank-based so normalisation changes nothing):
  at_snapped      ODF value at the frame centred nearest snapped_start
  max_snapped_span  max ODF over frame centres in
                  [snapped_start, snapped_start + (asr_end - asr_start)]
  max_asr_span      max ODF over frame centres in [asr_start, asr_end]

PASS (pre-stated): Mann-Whitney one-sided (errors < controls) p < 0.05
AND errors median < controls median on >= 1 statistic on >= 1 of the
three judged ODFs (superflux, complex, harmonic-gated [hpss / f0gated]).
Plain mix flux is computed as context only — it is the signal class
that already failed in loops 5/6 and is NOT one of the judged ODFs.
"""
import json
import numpy as np
from scipy.stats import mannwhitneyu

ERRORS = [34, 56, 60, 112, 162]
CONTROLS = [11, 17, 19, 26, 40, 58, 63, 64, 68, 73, 83, 85, 88, 91, 92]

ODFS = {
    "superflux": ("out/odf_superflux_raw.txt", 0.032, True),
    "complex": ("out/odf_complex_raw.txt", 0.032, True),
    "hpss_harm_gated": ("out/odf_hpss_raw.txt", 0.016, True),
    "f0_gated": ("out/odf_f0gated_raw.txt", 0.016, True),
    "flux_mix_context": ("out/odf_flux_raw.txt", 0.016, False),
}

snap = json.load(open("../c11_mir/snap_mix_mv14.json"))
words = snap["words"]


def frame_at(odf, hop, t):
    i = int(round(t / hop))
    return float(odf[min(max(i, 0), len(odf) - 1)])


def span_max(odf, hop, t0, t1):
    i0 = int(np.ceil(t0 / hop - 1e-9))
    i1 = int(np.floor(t1 / hop + 1e-9))
    if i1 < i0:
        return frame_at(odf, hop, 0.5 * (t0 + t1))
    i0 = max(i0, 0)
    i1 = min(i1, len(odf) - 1)
    return float(odf[i0:i1 + 1].max())


def stats_for(odf, hop, w):
    dur = w["asr_end"] - w["asr_start"]
    return {
        "at_snapped": frame_at(odf, hop, w["snapped_start"]),
        "max_snapped_span": span_max(odf, hop, w["snapped_start"], w["snapped_start"] + dur),
        "max_asr_span": span_max(odf, hop, w["asr_start"], w["asr_end"]),
    }


def med_iqr(v):
    v = np.asarray(v)
    return float(np.median(v)), float(np.percentile(v, 25)), float(np.percentile(v, 75))


res = {"fixture": {"errors_idx_1based": ERRORS, "controls_idx_1based": CONTROLS,
                   "source": "../c11_mir/snap_mix_mv14.json"},
       "odfs": {}}
any_pass = False
for name, (path, hop, judged) in ODFS.items():
    odf = np.loadtxt(path)
    odf = odf / odf.max()
    per = {}
    for stat in ("at_snapped", "max_snapped_span", "max_asr_span"):
        ev = [stats_for(odf, hop, words[i - 1])[stat] for i in ERRORS]
        cv = [stats_for(odf, hop, words[i - 1])[stat] for i in CONTROLS]
        U, p = mannwhitneyu(ev, cv, alternative="less")
        em, eq1, eq3 = med_iqr(ev)
        cm, cq1, cq3 = med_iqr(cv)
        ok = bool(p < 0.05 and em < cm)
        per[stat] = {"errors_median": em, "errors_iqr": [eq1, eq3],
                     "controls_median": cm, "controls_iqr": [cq1, cq3],
                     "mw_U": float(U), "mw_p_one_sided_errors_less": float(p),
                     "stat_pass": ok,
                     "errors_values": [float(x) for x in ev],
                     "controls_values": [float(x) for x in cv]}
        if judged and ok:
            any_pass = True
    res["odfs"][name] = {"hop_s": hop, "judged": judged, "stats": per,
                         "odf_pass": bool(judged and any(s["stat_pass"] for s in per.values()))}

res["bar"] = ("MW one-sided p<0.05 AND errors median < controls median on >=1 statistic "
              "on >=1 judged ODF (superflux / complex / harmonic-gated)")
res["pass"] = any_pass
with open("out/bar_c_superflux.json", "w") as f:
    json.dump(res, f, indent=1)

for name, o in res["odfs"].items():
    for stat, s in o["stats"].items():
        print("%-18s %-16s err_med %.4f  ctl_med %.4f  U=%g  p=%.4f  %s" % (
            name, stat, s["errors_median"], s["controls_median"], s["mw_U"],
            s["mw_p_one_sided_errors_less"],
            "STAT-PASS" if s["stat_pass"] else ""))
print("BAR 2:", "PASS" if any_pass else "FAIL")
