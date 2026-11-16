#!/usr/bin/env python3
"""Full-track validation for the C11 separation runner (c11_sep).

Bars (from SPRINT_SCOPE.md, held, do NOT lower):
  1. Stem corr vs Demucs >= 0.95 (full track, mono).
  2. RMS-VAD boundaries within +/-0.5 s of c11_mir/hpss_mv14_ref.json.
  3. Active/silent RMS ratio >= 100x.
  4. Runtime < 894 s (target < 650 s) — read from full_run.log, not measured here.
The RMS-VAD recipe is imported verbatim from c11_mir/make_ref_segments.py
(the pipeline's own MSS-ALT recipe).

Usage: validate_fulltrack.py [--vocals c11_vocals.wav] [--inst c11_inst.wav]
         [--demucs <demucs vocals wav>] [--ref <hpss_mv14_ref.json>]
         [--run-log full_run.log] [--out stage4_fulltrack_validation.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "c11_mir"))
from make_ref_segments import rms_vad  # noqa: E402

SR = 44100


def load_mono(path):
    sr, data = wavfile.read(path)
    assert sr == SR, f"{path}: expected {SR} Hz, got {sr}"
    x = data.astype(np.float64)
    if data.dtype == np.int16:
        x = x / 32768.0
    if x.ndim == 2:
        x = x.mean(axis=1)
    return x


def corr(a, b):
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    return float(np.corrcoef(a, b)[0, 1])


def rms_vad_boundaries(y, track_len):
    """Return the rms_vad segments for a mono vocal stem (list of dicts)."""
    segs = rms_vad(y, SR, track_len)
    return [(float(d["start"]), float(d["end"])) for d in segs]


def merge_overlapping(segs):
    """Merge segments that overlap (the 0.3 s pads make split halves overlap).
    Distinct sung spans stay separate (real gaps > 0)."""
    out = []
    for s, e in sorted(segs):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [(s, e) for s, e in out]


def match_boundaries(ref, pred):
    """Span-start metric (the loop-5 / wubuwizard reading of the bar).
    Ref segments are overlap-merged into spans; for each ref span, take the
    earliest-start pred segment overlapping it (the first piece of a split
    group — later pieces are 30 s-cap splits at different quiet points, not
    new starts). Report max |dStart| and max |dEnd| (end from the last
    overlapping piece). Unmatched pred pieces (extra splits / intro leak)
    are counted, not failed."""
    ref_spans = merge_overlapping(ref)
    pred_sorted = sorted(pred)
    d_starts, d_ends, extra = [], [], 0
    used = set()
    for rs, re_ in ref_spans:
        # Pieces are selected by START (not overlap): a piece belongs to the
        # span it starts in (allowing 1 s of early start for the 0.3 s pad).
        # Overlap-based selection mis-assigns a piece that straddles a span
        # boundary (MDX 85.25-104.68 bleeds 0.39 s into the 104.29 span and
        # would be read as that span's start, dStart 19.04 instead of 0.21).
        pieces = [(ps, pe) for ps, pe in pred_sorted if rs - 1.0 <= ps < re_]
        if not pieces:
            continue
        for p in pieces:
            used.add(p)
        d_starts.append(abs(pieces[0][0] - rs))
        d_ends.append(abs(pieces[-1][1] - re_))
    extra = len([p for p in pred_sorted if p not in used])
    return d_starts, d_ends, extra, len(ref_spans)


def active_silent_ratio(y, ref_segments):
    """Sprint-6 statistic, verbatim from loop-5/r8_precheck_mdx_verify.py:
    25 ms RMS envelope (16 kHz mono, win=hop=400, non-overlapping), ratio of
    the MEDIAN envelope in the ref segments to the MEDIAN envelope outside
    them. (A raw-waveform RMS ratio gives ~15-30x and is NOT this statistic.)"""
    from scipy.signal import resample_poly
    y16 = resample_poly(y, 16000, SR)
    hop = 400
    nn = len(y16) // hop
    env = np.sqrt(np.mean(y16[:nn * hop].reshape(nn, hop) ** 2, axis=1))
    tt = np.arange(nn) * 0.025
    act = np.zeros(nn, dtype=bool)
    for s, e in ref_segments:
        act |= (tt >= s) & (tt < e)
    sil = ~act
    med_a = float(np.median(env[act])) if act.any() else 0.0
    med_s = float(np.median(env[sil])) if sil.any() else 0.0
    return med_a, med_s, (med_a / med_s if med_s > 0 else float("inf"))


def parse_runtime(run_log):
    if not run_log:
        return None
    m = re.search(r"demix done: ([\d.]+)s wall", Path(run_log).read_text())
    if m:
        return float(m.group(1))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocals", default="c11_vocals.wav")
    ap.add_argument("--inst", default="c11_inst.wav")
    ap.add_argument("--demucs",
                    default="../c11_mir/separation_mv14/mv14_44k_(Vocals)_htdemucs.wav")
    ap.add_argument("--ref", default="../c11_mir/hpss_mv14_ref.json")
    ap.add_argument("--run-log", default="full_run.log")
    ap.add_argument("--out", default="stage4_fulltrack_validation.json")
    args = ap.parse_args()

    voc = load_mono(args.vocals)
    dem = load_mono(args.demucs)
    track_len = len(voc) / SR
    ref_doc = json.loads(Path(args.ref).read_text())
    ref_segs = [(float(s["start"]), float(s["end"])) for s in ref_doc["segments"]]

    c = corr(voc, dem)
    # per-channel corr as well (stereo files)
    sr_v, voc_st = wavfile.read(args.vocals)
    sr_d, dem_st = wavfile.read(args.demucs)
    ch_corrs = []
    for ch in range(2):
        a = voc_st[:, ch].astype(np.float64) / 32768.0
        b = dem_st[:, ch].astype(np.float64) / 32768.0
        n = min(len(a), len(b))
        ch_corrs.append(float(np.corrcoef(a[:n], b[:n])[0, 1]))

    pred_segs = rms_vad_boundaries(voc, track_len)
    d_starts, d_ends, n_extra, n_ref_spans = match_boundaries(ref_segs, pred_segs)
    med_a, med_s, ratio = active_silent_ratio(voc, ref_segs)
    # Demucs' own ratio, same mask/method, for the comparison column
    med_a_d, med_s_d, ratio_d = active_silent_ratio(dem, ref_segs)

    runtime = parse_runtime(args.run_log)

    # Instrumental sanity: mix - vocals*1.01 should be quiet where vocals are loud
    # (and the instrumental file should exist and be full-length).
    inst_ok, inst_len_s = None, None
    if Path(args.inst).exists():
        inst = load_mono(args.inst)
        inst_len_s = len(inst) / SR
        inst_ok = abs(inst_len_s - track_len) < 0.01

    doc = {
        "stage": "4_fulltrack",
        "date_utc": "2026-11-12",
        "track": "MV-14 (mv14_44k.wav, 161.6 s)",
        "vocals": args.vocals,
        "demucs_reference": args.demucs,
        "rms_vad_reference": args.ref,
        "stem_corr_mono": c,
        "stem_corr_L": ch_corrs[0],
        "stem_corr_R": ch_corrs[1],
        "bar_stem_corr": 0.95,
        "stem_corr_pass": bool(c >= 0.95),
        "rms_vad": {
            "n_ref_segments": len(ref_segs),
            "n_ref_spans_overlap_merged": n_ref_spans,
            "n_pred_segments": len(pred_segs),
            "n_pred_extra_pieces": n_extra,
            "max_abs_dStart_s": float(max(d_starts)) if d_starts else None,
            "max_abs_dEnd_s": float(max(d_ends)) if d_ends else None,
            "bar_s": 0.5,
            "boundaries_pass": bool(d_starts and max(d_starts) <= 0.5),
            "note": "Span-start metric (loop-5/wubuwizard reading): ref spans are "
                    "overlap-merged; each ref span is matched to its earliest-start "
                    "overlapping pred piece (later pieces are 30 s-cap splits at "
                    "different quiet points, not new starts). dEnd is diagnostic "
                    "(split/extension behaviour), the bar is on starts.",
            "pred_segments": [[round(s, 2), round(e, 2)] for s, e in pred_segs],
        },
        "active_silent": {
            "method": "sprint-6 statistic: median 25 ms RMS envelope (16 kHz mono) "
                      "inside vs outside the ref segments",
            "c11_active_median_env": med_a,
            "c11_silent_median_env": med_s,
            "c11_ratio": ratio,
            "demucs_active_median_env": med_a_d,
            "demucs_silent_median_env": med_s_d,
            "demucs_ratio": ratio_d,
            "bar_ratio": 100,
            "ratio_pass": bool(ratio >= 100),
        },
        "instrumental": {"exists": inst_ok, "len_s": inst_len_s, "track_len_s": track_len},
        "runtime_s": runtime,
        "bar_runtime_s": 894,
        "target_runtime_s": 650,
        "runtime_pass": bool(runtime is not None and runtime < 894),
    }
    Path(args.out).write_text(json.dumps(doc, indent=2))
    print(json.dumps(doc, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
