#!/usr/bin/env python3
"""MDX_STEMACT validator — Slopcannon improvement loop 6, top-1 sprint.

Bars (held, from loop 5 §3 #2 / loop-06 SPRINT_SCOPE.md — do NOT lower):
  Bar A: RMS-VAD boundaries reproduce the Demucs stem-activity boundaries
         within +/-0.5 s on the 12 ref segments (span-start metric, as in
         c11_sep stage 4). Report max |dStart| per stem; dEnd diagnostic.
  Bar B: 25 ms RMS envelope separates sung from instrumental with
         non-overlapping IQRs, on ALL THREE stems (c11, ONNX MDX, Demucs).
         Sung = inside ref segments 1-10; instrumental = outside all 12
         ref segments (bleed segs 11-12 excluded from both classes).
         Sprint-6 median-ratio (active/silent >=100x, all 12 as active)
         reported alongside as a secondary, not the bar.
  Bar C: stem-envelope-at-snapped-position separates the 5 known snap
         errors (1-based idx 34, 56, 60, 112, 162 into snap_mix_mv14.json)
         from the 15 correct controls (loop-4 rule: |correction| <= 0.05 s,
         prob >= 0.9, on_peak, first 15): Mann-Whitney one-sided p < 0.05
         AND errors median < correct median. Judged on the c11 stem;
         ONNX stem reported alongside. Diagnostic (NOT a bar): distance
         from the snapped position to the nearest stem-envelope rising edge.

Calibration: run on the ONNX MDX stem FIRST and reproduce loop 5's numbers
(17 segments, max |dStart| 0.21 s, ratio 248.8x) within rounding before
running on the c11 stem. If calibration fails, stop and report.

Usage:
  python3 validate_stemact.py --stem <stem.wav> --name <mdx|c11|demucs>
      [--calibrate] [--out stem_<name>_validation.json]
  python3 validate_stemact.py --bar-c --stems c11:<wav> mdx:<wav>
      [--out bar_c.json]
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.stats import mannwhitneyu

HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(DR / "c11_mir"))
sys.path.insert(0, str(DR / "c11_sep"))
from make_ref_segments import rms_vad  # noqa: E402
from validate_fulltrack import (active_silent_ratio, corr, load_mono,  # noqa: E402
                                match_boundaries, merge_overlapping)
from stem_activity_curve import envelope_25ms, rising_edges  # noqa: E402

REF = DR / "c11_mir" / "hpss_mv14_ref.json"
SNAP_MIX = DR / "c11_mir" / "snap_mix_mv14.json"
DEMUX = DR / "c11_mir" / "separation_mv14" / "mv14_44k_(Vocals)_htdemucs.wav"

ERR_IDX_1BASED = [34, 56, 60, 112, 162]


def ref_segments():
    doc = json.loads(REF.read_text())
    return [(float(s["start"]), float(s["end"])) for s in doc["segments"]]


def env_stats(t, env, ref_segs):
    """Median + IQR of the 25 ms envelope per class."""
    sung = np.zeros(len(env), dtype=bool)
    for s, e in ref_segs[:10]:  # segments 1-10 are sung; 11-12 are bleed
        sung |= (t >= s) & (t < e)
    inside_all = np.zeros(len(env), dtype=bool)
    for s, e in ref_segs:
        inside_all |= (t >= s) & (t < e)
    instr = ~inside_all  # outside all 12 ref segments
    out = {}
    for label, mask in (("sung", sung), ("instrumental", instr)):
        v = env[mask]
        out[label] = {
            "n_frames": int(mask.sum()),
            "median": float(np.median(v)),
            "q25": float(np.percentile(v, 25)),
            "q75": float(np.percentile(v, 75)),
            "iqr": float(np.percentile(v, 75) - np.percentile(v, 25)),
        }
    out["iqr_non_overlap"] = bool(out["sung"]["q25"] > out["instrumental"]["q75"])
    return out


def validate_stem(path, name):
    y = load_mono(path)
    track_len = len(y) / 44100
    ref_segs = ref_segments()
    # Bar A: RMS-VAD (verbatim recipe) + span-start metric
    pred = [(float(d["start"]), float(d["end"]))
            for d in rms_vad(y, 44100, track_len)]
    d_starts, d_ends, n_extra, n_ref_spans = match_boundaries(ref_segs, pred)
    # Bar B: 25 ms envelope class stats + sprint-6 ratio (secondary)
    t, env, _ = envelope_25ms(y)
    stats = env_stats(t, env, ref_segs)
    med_a, med_s, ratio = active_silent_ratio(y, ref_segs)
    # Stem corr vs Demucs (diagnostic for c11/mdx; 1.0 for demucs itself)
    dem = load_mono(str(DEMUX))
    c = corr(y, dem)
    doc = {
        "stem": name,
        "vocals": str(path),
        "track": "MV-14 (161.6 s)",
        "stem_corr_vs_demucs_mono": c,
        "bar_a": {
            "n_ref_segments": len(ref_segs),
            "n_ref_spans_overlap_merged": n_ref_spans,
            "n_pred_segments": len(pred),
            "n_pred_extra_pieces": n_extra,
            "dStart_per_span_s": [round(float(d), 3) for d in d_starts],
            "max_abs_dStart_s": float(max(d_starts)) if d_starts else None,
            "dEnd_per_span_s": [round(float(d), 3) for d in d_ends],
            "max_abs_dEnd_s": float(max(d_ends)) if d_ends else None,
            "bar_s": 0.5,
            "pass": bool(d_starts and max(d_starts) <= 0.5),
            "pred_segments": [[round(s, 2), round(e, 2)] for s, e in pred],
        },
        "bar_b": {
            "method": "25 ms RMS envelope (16 kHz mono, win=hop=400); "
                      "sung = inside ref segments 1-10, instrumental = "
                      "outside all 12 ref segments (bleed 11-12 excluded "
                      "from both classes)",
            "sung": stats["sung"],
            "instrumental": stats["instrumental"],
            "iqr_non_overlap": stats["iqr_non_overlap"],
            "pass": stats["iqr_non_overlap"],
            "secondary_ratio": {
                "method": "sprint-6 statistic (median envelope inside all "
                          "12 ref segments vs outside), verbatim from "
                          "validate_fulltrack.active_silent_ratio",
                "active_median_env": med_a,
                "silent_median_env": med_s,
                "ratio": ratio,
                "bar_ratio": 100,
                "ratio_pass": bool(ratio >= 100),
            },
        },
    }
    return doc


def controls_and_errors():
    snap = json.loads(SNAP_MIX.read_text())
    words = snap["words"]
    errors = [(i, words[i - 1]) for i in ERR_IDX_1BASED]
    ctrls = [(i + 1, w) for i, w in enumerate(words)
             if abs(w["correction_s"]) <= 0.05 and w["prob"] >= 0.9
             and w["on_peak"]][:15]
    return words, errors, ctrls


def env_at(t, env, pos):
    idx = int(np.floor(pos / 0.025))
    idx = max(0, min(idx, len(env) - 1))
    return float(env[idx])


def bar_c(stem_paths):
    words, errors, ctrls = controls_and_errors()
    out = {"errors_idx_1based": ERR_IDX_1BASED,
           "controls_idx_1based": [i for i, _ in ctrls],
           "rule": "controls: |correction| <= 0.05 s, prob >= 0.9, on_peak, "
                   "first 15 (loop-4 rule); bar: Mann-Whitney one-sided "
                   "p < 0.05 AND errors median < correct median",
           "per_stem": {}}
    for name, path in stem_paths:
        y = load_mono(path)
        t, env, _ = envelope_25ms(y)
        thr = float(0.10 * np.percentile(env, 99))
        edges = rising_edges(t, env, thr)
        rows = {}
        for group, items in (("errors", errors), ("controls", ctrls)):
            vals, vals_norm, dists, dists_abs = [], [], [], []
            detail = []
            for i, w in items:
                pos = w["snapped_start"]
                v = env_at(t, env, pos)
                # local normalisation diagnostic: env / median env in +-1 s
                lo = max(0, int((pos - 1.0) / 0.025))
                hi = min(len(env), int((pos + 1.0) / 0.025) + 1)
                loc = float(np.median(env[lo:hi])) if hi > lo else 0.0
                vn = v / loc if loc > 0 else float("nan")
                if len(edges):
                    k = int(np.argmin(np.abs(edges - pos)))
                    d = float(edges[k] - pos)
                else:
                    d = float("nan")
                vals.append(v)
                vals_norm.append(vn)
                dists.append(d)
                dists_abs.append(abs(d))
                detail.append({"idx_1based": i, "word": w["word"],
                               "asr_start": w["asr_start"],
                               "snapped_start": pos,
                               "correction_s": w["correction_s"],
                               "env_at_snapped": v,
                               "env_at_snapped_over_local_median": vn,
                               "dist_to_nearest_rising_edge_s": d})
            rows[group] = {"values": vals, "detail": detail,
                           "median": float(np.median(vals)),
                           "q25": float(np.percentile(vals, 25)),
                           "q75": float(np.percentile(vals, 75)),
                           "median_norm": float(np.median(vals_norm)),
                           "median_dist_rising_edge_s": float(np.median(dists)),
                           "median_abs_dist_rising_edge_s": float(np.median(dists_abs))}
        u = mannwhitneyu(rows["errors"]["values"], rows["controls"]["values"],
                         alternative="less")
        p = float(u.pvalue)
        passed = bool(p < 0.05 and rows["errors"]["median"] < rows["controls"]["median"])
        out["per_stem"][name] = {
            "vocals": str(path),
            "env_threshold_0.1xp99_25ms": thr,
            "errors": rows["errors"],
            "controls": rows["controls"],
            "mann_whitney_U": float(u.statistic),
            "p_one_sided_errors_lt_controls": p,
            "errors_median_lt_controls_median": bool(
                rows["errors"]["median"] < rows["controls"]["median"]),
            "pass": passed,
        }
    out["judged_on"] = "c11"
    out["pass"] = out["per_stem"]["c11"]["pass"]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stem", default=None)
    ap.add_argument("--name", default=None)
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--bar-c", action="store_true")
    ap.add_argument("--stems", nargs="*", default=None,
                    help="name:path pairs for --bar-c")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.bar_c:
        pairs = []
        for s in args.stems:
            n, p = s.split(":", 1)
            pairs.append((n, p))
        doc = bar_c(pairs)
    else:
        doc = validate_stem(args.stem, args.name)
        if args.calibrate:
            # loop-5 numbers on the ORT MDX vocals: 17 segments,
            # max |dStart| 0.21 s, ratio 248.8x. NOTE: loop-5's ratio uses
            # the SUNG-ONLY active mask (ref segments 1-10) vs outside-all-12
            # silent mask (r8_precheck_mdx_verify.py lines 149-150: act_m =
            # span_mask(sung), sil_m = ~span_mask(segs)); the all-12-active
            # variant is 242.7x and is what validate_fulltrack computes.
            # The sung-only ratio is this validator's Bar B medians ratio.
            cal = {
                "expected_n_pred_segments": 17,
                "expected_max_abs_dStart_s": 0.21,
                "expected_ratio": 248.8,
                "ratio_masks": "active = ref segments 1-10 (sung), silent = "
                               "outside all 12 (loop-5 lines 149-150)",
                "got_n_pred_segments": doc["bar_a"]["n_pred_segments"],
                "got_max_abs_dStart_s": doc["bar_a"]["max_abs_dStart_s"],
                "got_ratio": doc["bar_b"]["sung"]["median"]
                             / doc["bar_b"]["instrumental"]["median"],
                "got_ratio_all12_active_variant":
                    doc["bar_b"]["secondary_ratio"]["ratio"],
            }
            cal["segments_match"] = cal["got_n_pred_segments"] == 17
            cal["dstart_match"] = (cal["got_max_abs_dStart_s"] is not None
                                   and abs(cal["got_max_abs_dStart_s"] - 0.21) <= 0.011)
            cal["ratio_match"] = abs(cal["got_ratio"] - 248.8) <= 1.0
            cal["calibration_pass"] = (cal["segments_match"] and cal["dstart_match"]
                                       and cal["ratio_match"])
            doc["calibration_vs_loop5"] = cal
            print("CALIBRATION:", json.dumps(cal, indent=2))
    Path(args.out).write_text(json.dumps(doc, indent=2))
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
