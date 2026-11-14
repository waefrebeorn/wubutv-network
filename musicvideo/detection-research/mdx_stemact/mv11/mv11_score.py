#!/usr/bin/env python3
"""MV-11 generalisation leg scorer (MDX_STEMACT).

Bar A stem-to-stem: the c11 stem's RMS-VAD boundaries reproduce the Demucs
stem's RMS-VAD boundaries within +/-0.5 s (span-start metric, same as
c11_sep stage 4 / validate_stemact.py). No HPSS ref exists for MV-11, so
the Demucs stem's own segments ARE the reference.
Also reports: stem corr vs Demucs, per-stem segment counts, and the
Bar B-style envelope separation (sung = inside Demucs segments,
instrumental = outside all Demucs segments) on each stem.
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DR = HERE.parent.parent
sys.path.insert(0, str(DR / "c11_mir"))
sys.path.insert(0, str(DR / "c11_sep"))
sys.path.insert(0, str(HERE.parent))
from make_ref_segments import rms_vad  # noqa: E402
from validate_fulltrack import corr, load_mono, match_boundaries  # noqa: E402
from stem_activity_curve import envelope_25ms  # noqa: E402

C11 = HERE / "mv11_c11_vocals.wav"
DEM = Path("/home/hatch/workspace/wubutv-network/musicvideo/MV-11_water-hit-my-balls"
           "/analysis/tests/separation/track_44k_vocals_htdemucs.wav")


def segs_of(path):
    y = load_mono(str(path))
    tl = len(y) / 44100
    return [(float(d["start"]), float(d["end"]))
            for d in rms_vad(y, 44100, tl)], y, tl


def env_stats(y, ref_segs):
    t, env, _ = envelope_25ms(y)
    inside = np.zeros(len(env), dtype=bool)
    for s, e in ref_segs:
        inside |= (t >= s) & (t < e)
    out = {}
    for label, mask in (("sung", inside), ("instrumental", ~inside)):
        v = env[mask]
        out[label] = {"n_frames": int(mask.sum()),
                      "median": float(np.median(v)),
                      "q25": float(np.percentile(v, 25)),
                      "q75": float(np.percentile(v, 75))}
    out["iqr_non_overlap"] = bool(out["sung"]["q25"] > out["instrumental"]["q75"])
    out["ratio"] = out["sung"]["median"] / out["instrumental"]["median"]
    return out


def main():
    dem_segs, dem_y, tl = segs_of(DEM)
    c11_segs, c11_y, _ = segs_of(C11)
    d_starts, d_ends, n_extra, n_spans = match_boundaries(dem_segs, c11_segs)
    c = corr(c11_y, dem_y)
    doc = {
        "leg": "mv11_generalisation",
        "track": "MV-11 Water hit my balls (172.416 s)",
        "c11_vocals": str(C11),
        "demucs_reference": str(DEM),
        "stem_corr_vs_demucs_mono": c,
        "bar_a_stem_to_stem": {
            "method": "RMS-VAD (verbatim recipe) on each stem; Demucs "
                      "segments are the reference; span-start metric",
            "n_demucs_ref_segments": len(dem_segs),
            "n_ref_spans_overlap_merged": n_spans,
            "n_c11_pred_segments": len(c11_segs),
            "n_pred_extra_pieces": n_extra,
            "dStart_per_span_s": [round(float(d), 3) for d in d_starts],
            "max_abs_dStart_s": float(max(d_starts)) if d_starts else None,
            "dEnd_per_span_s": [round(float(d), 3) for d in d_ends],
            "max_abs_dEnd_s": float(max(d_ends)) if d_ends else None,
            "bar_s": 0.5,
            "pass": bool(d_starts and max(d_starts) <= 0.5),
            "demucs_segments": [[round(s, 2), round(e, 2)] for s, e in dem_segs],
            "c11_segments": [[round(s, 2), round(e, 2)] for s, e in c11_segs],
        },
        "bar_b_style": {
            "method": "25 ms RMS envelope; sung = inside Demucs segments, "
                      "instrumental = outside all Demucs segments",
            "c11": env_stats(c11_y, dem_segs),
            "demucs": env_stats(dem_y, dem_segs),
        },
    }
    Path(HERE / "mv11_score.json").write_text(json.dumps(doc, indent=2))
    print(json.dumps(doc, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
