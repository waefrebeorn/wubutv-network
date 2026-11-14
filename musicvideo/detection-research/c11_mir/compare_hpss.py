#!/usr/bin/env python3
"""Sprint 6 validation for c11_hpss.
(a) HPSS masks vs librosa.decompose.hpss on the same 16k wav
    (same STFT: n_fft=1024, hop=256, Hann periodic, centre=True;
    librosa hpss kernel_size=31, margin=1.0). Bar: corr >= 0.999.
(b) Segment boundaries vs Demucs-RMS-VAD reference on MV-14
    (reference JSON from make_ref_segments.py). Bar: >= 80% of
    reference boundaries matched within +/-0.5 s, both directions.
Usage: compare_hpss.py [--masks-only] [--bounds-only]
"""
import json
import sys

import numpy as np

WAV = "../../MV-14_clip-it/work/track_16k.wav"
HARM_BIN = "hpss_mv14_harm.bin"
C_JSON = "hpss_mv14.json"
REF_JSON = "hpss_mv14_ref.json"


def corr(a, b):
    a = np.asarray(a, dtype=np.float64).ravel()
    b = np.asarray(b, dtype=np.float64).ravel()
    return float(np.corrcoef(a, b)[0, 1])


def masks_check():
    import librosa
    y, sr = librosa.load(WAV, sr=16000, mono=True)
    S = np.abs(librosa.stft(y, n_fft=1024, hop_length=256, window="hann",
                            center=True))
    H, P = librosa.decompose.hpss(S, kernel_size=31, margin=1.0)
    H = np.ascontiguousarray(H.T)  # librosa is [bin][frame]; C is [frame][bin]
    S = np.ascontiguousarray(S.T)
    c_harm = np.fromfile(HARM_BIN, dtype=np.float64)
    nframes = S.shape[0]  # S already transposed to [frame][bin] above
    c_harm = c_harm.reshape(nframes, 513)
    print(f"librosa S: {S.shape}, C harm: {c_harm.shape}")
    c = corr(c_harm, H)
    md = float(np.max(np.abs(c_harm - H)))
    rel = md / (float(np.max(np.abs(H))) or 1.0)
    print(f"harmonic mag vs librosa: corr={c:.6f} max|diff|={md:.6g} "
          f"rel_max|diff|={rel:.3g}")
    # isolated check: C masks are soft-mask; librosa H is already masked.
    # Also compare harmonic energy share.
    print(f"librosa harmonic share: "
          f"{float(np.sum(H**2) / np.sum(S**2)):.4f}")
    return {"hpss_corr": c, "hpss_max_abs_diff": md,
            "hpss_rel_max_diff": rel}


def boundary_match(ref_bounds, c_bounds, tol=0.5):
    """For each ref boundary, nearest C boundary of the same type;
    returns (n_matched, n_total, median |offset|)."""
    matched = 0
    offs = []
    for rb in ref_bounds:
        if not c_bounds:
            break
        d = min((abs(rb - cb), cb) for cb in c_bounds)[0]
        if d <= tol:
            matched += 1
            offs.append(min(abs(rb - cb) for cb in c_bounds))
    med = float(np.median(offs)) if offs else float("nan")
    return matched, len(ref_bounds), med


def bounds_check():
    ref = json.load(open(REF_JSON))
    c = json.load(open(C_JSON))
    out = {}
    for key in ("segments_vocal", "segments_full"):
        c_segs = c[key]
        r_starts = [s["start"] for s in ref["segments"]]
        r_ends = [s["end"] for s in ref["segments"]]
        c_starts = [s["start"] for s in c_segs]
        c_ends = [s["end"] for s in c_segs]
        ms, ts, med = boundary_match(r_starts, c_starts)
        me, te, mede = boundary_match(r_ends, c_ends)
        # reverse direction: C boundaries matched by a reference boundary
        cms, _, _ = boundary_match(c_starts, r_starts)
        cme, _, _ = boundary_match(c_ends, r_ends)
        print(f"{key}: ref {len(ref['segments'])} segs, C {len(c_segs)} segs")
        print(f"  starts ref->C: {ms}/{ts} ({100*ms/max(ts,1):.1f}%) "
              f"median|off|={med:.3f}s")
        print(f"  ends   ref->C: {me}/{te} ({100*me/max(te,1):.1f}%) "
              f"median|off|={mede:.3f}s")
        print(f"  starts C->ref: {cms}/{len(c_starts)} "
              f"({100*cms/max(len(c_starts),1):.1f}%)")
        print(f"  ends   C->ref: {cme}/{len(c_ends)} "
              f"({100*cme/max(len(c_ends),1):.1f}%)")
        tot_ref = ms + me
        tot_n = ts + te
        print(f"  OVERALL ref->C: {tot_ref}/{tot_n} "
              f"({100*tot_ref/max(tot_n,1):.1f}%)  bar: >=80%")
        tot_c = cms + cme
        tot_cn = len(c_starts) + len(c_ends)
        print(f"  OVERALL C->ref: {tot_c}/{tot_cn} "
              f"({100*tot_c/max(tot_cn,1):.1f}%)  bar: >=80%")
        out[key] = {
            "ref_segments": len(ref["segments"]),
            "c_segments": len(c_segs),
            "starts_matched": ms, "starts_total": ts,
            "starts_median_offset_s": med,
            "ends_matched": me, "ends_total": te,
            "ends_median_offset_s": mede,
            "overall_pct": 100 * tot_ref / max(tot_n, 1),
            "c_to_ref_overall_pct": 100 * tot_c / max(tot_cn, 1),
            "c_to_ref_starts_matched": cms,
            "c_to_ref_ends_matched": cme,
        }
    return out


if __name__ == "__main__":
    masks_only = "--masks-only" in sys.argv
    bounds_only = "--bounds-only" in sys.argv
    res = {}
    if not bounds_only:
        res["masks"] = masks_check()
    if not masks_only:
        res["bounds"] = bounds_check()
    json.dump(res, open("hpss_mv14_validation.json", "w"), indent=1)
    print("wrote hpss_mv14_validation.json")
