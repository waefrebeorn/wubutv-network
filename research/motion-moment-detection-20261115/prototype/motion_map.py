#!/usr/bin/env python3
"""motion_map.py — PROTOTYPE motion-moment map (research only, not production).

Builds a per-frame motion-moment map for one video file:
  * step curve d[i] = mean |F[i+1] - F[i]| at 320x180 gray, native fps
    (the exact signal/convention of the episode measure.py harness and
    the Joint Gate's MAE numbers, so map values compare 1:1 with
    GATE_LOG figures);
  * events extracted by hysteresis on the curve's OWN distribution
    (theta_lo = median, theta_hi = p75 of the smoothed curve) — no
    absolute constants, per the SHOW-3 J16 calibration failure;
  * per event: onset step, peak step/value, end step, class
    (BLIP < 6 steps, GESTURE 6-48, SUSTAINED > 48 at 24 fps);
  * head state (first 24 steps) and tail state (last 48 steps);
  * with --cuts f1,f2,... on a joined file: per-cut phase read on
    both sides + the J12 recommendation (local motion peak within
    +/-12 steps of the cut on the upstream side).

Usage:
  motion_map.py VIDEO [--cuts 240,480,...] [--out map.json]
"""
import argparse
import json
import subprocess
import sys

import numpy as np

W, H = 320, 180


def decode_gray(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf",
           f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (W * H)
    return np.frombuffer(raw[: n * W * H], dtype=np.uint8).reshape(n, W * H).astype(np.float32)


def smooth(x, k=3):
    if len(x) < k:
        return x.copy()
    ker = np.ones(k) / k
    return np.convolve(x, ker, mode="same")


def extract_events(s, th_lo, th_hi):
    """Hysteresis spans: runs of s >= th_lo containing a sample >= th_hi.
    Merge spans separated by <= 6 steps; drop spans < 4 steps."""
    above_lo = s >= th_lo
    spans = []
    i = 0
    n = len(s)
    while i < n:
        if above_lo[i]:
            j = i
            while j + 1 < n and above_lo[j + 1]:
                j += 1
            if np.max(s[i:j + 1]) >= th_hi:
                spans.append([i, j])
            i = j + 1
        else:
            i += 1
    merged = []
    for sp in spans:
        if merged and sp[0] - merged[-1][1] - 1 <= 6:
            merged[-1][1] = sp[1]
        else:
            merged.append(list(sp))
    events = []
    for a, b in merged:
        if b - a + 1 < 4:
            continue
        pk = a + int(np.argmax(s[a:b + 1]))
        dur = b - a + 1
        cls = "BLIP" if dur < 6 else ("GESTURE" if dur <= 48 else "SUSTAINED")
        events.append({"onset_step": int(a), "peak_step": int(pk),
                       "peak_val": round(float(s[pk]), 2),
                       "end_step": int(b), "dur_steps": int(dur),
                       "class": cls})
    return events


def phase_at(s, events, i, th_lo):
    """Phase of step i: SETTLED / RISING / PEAK / FALLING."""
    if i < 0 or i >= len(s):
        return "OUT"
    for ev in events:
        if ev["onset_step"] <= i <= ev["end_step"]:
            if abs(i - ev["peak_step"]) <= 2:
                return "PEAK"
            return "RISING" if i < ev["peak_step"] else "FALLING"
    return "SETTLED" if s[i] < th_lo else "DRIFT"


def build_map(path):
    fr = decode_gray(path)
    n = len(fr)
    d = np.mean(np.abs(np.diff(fr, axis=0)), axis=1)  # step i: frame i -> i+1
    s = smooth(d)
    qs = {q: round(float(np.percentile(s, q)), 2) for q in (25, 50, 75, 90, 95, 99)}
    th_lo = float(np.percentile(s, 50))
    th_hi = float(np.percentile(s, 75))
    events = extract_events(s, th_lo, th_hi)

    head_steps = s[:24]
    head_events = [e for e in events if e["onset_step"] < 24]
    if len(s) >= 1 and s[0] >= th_lo and any(
            e["onset_step"] == 0 for e in events):
        head_class = "IN-MOTION"
    elif head_events and head_events[0]["onset_step"] <= 12:
        head_class = "RAMP"
    elif head_events:
        head_class = "LATE-ONSET"
    else:
        head_class = "SETTLED-HEAD"
    head = {"class": head_class,
            "mean_0_12": round(float(np.mean(s[:12])), 2),
            "mean_0_24": round(float(np.mean(head_steps)), 2),
            "first_onset_step": head_events[0]["onset_step"] if head_events else None}

    tail_from = max(0, len(s) - 48)
    tail_events = [e for e in events if e["end_step"] >= tail_from]
    # settle point: last step after which s stays < th_lo to the end
    settle = None
    for i in range(len(s) - 1, -1, -1):
        if s[i] >= th_lo:
            settle = i + 1
            break
    tail = {"final12_mean": round(float(np.mean(s[-12:])), 2),
            "last_event": tail_events[-1] if tail_events else None,
            "settled_from_step": settle,
            "phase_at_final_step": phase_at(s, events, len(s) - 1, th_lo)}

    return {"file": path.split("/")[-1], "frames": int(n), "steps": int(len(s)),
            "curve_stats": qs, "th_lo_median": round(th_lo, 2),
            "th_hi_p75": round(th_hi, 2), "events": events,
            "head": head, "tail": tail}, s, events, th_lo


def joint_eval(s, events, th_lo, cut):
    """cut = first frame index of downstream unit in the joined file.
    The seam transition is step cut-1."""
    seam = cut - 1
    up_phase = phase_at(s, events, seam - 1, th_lo)
    down_phase = phase_at(s, events, cut, th_lo)
    # J12: local motion peak within +/-12 steps of the seam, upstream side
    lo = max(0, seam - 12)
    pk = lo + int(np.argmax(s[lo:seam + 1])) if seam >= lo else seam
    # downstream: first event onset at/after the cut
    down_onsets = [e["onset_step"] for e in events if e["onset_step"] >= cut]
    return {"cut_frame": int(cut), "seam_step_mae": round(float(s[seam]), 2),
            "upstream_phase_before_seam": up_phase,
            "upstream_final12_mean": round(float(np.mean(s[cut - 12:cut])), 2),
            "downstream_phase_at_head": down_phase,
            "downstream_head12_mean": round(float(np.mean(s[cut:cut + 12])), 2),
            "downstream_first_onset_after_cut": down_onsets[0] - cut if down_onsets else None,
            "j12_local_peak_step": int(pk),
            "j12_peak_offset_from_seam": int(pk - seam),
            "j12_peak_val": round(float(s[pk]), 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--cuts", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    m, s, events, th_lo = build_map(args.video)
    if args.cuts:
        cuts = [int(x) for x in args.cuts.split(",")]
        m["joints"] = [joint_eval(s, events, th_lo, c) for c in cuts]
        # episode BASE per Joint Gate sec.6: p95 of in-unit steps,
        # excluding 12 steps at each unit edge (all steps, not sampled)
        bounds = [0] + cuts + [len(s) + 1]
        inunit = []
        for a, b in zip(bounds[:-1], bounds[1:]):
            inunit.extend(s[a + 12:b - 12].tolist())
        m["episode_BASE_p95_inunit"] = round(float(np.percentile(inunit, 95)), 2)
    print(json.dumps(m, indent=1))
    if args.out:
        with open(args.out, "w") as f:
            json.dump(m, f, indent=1)


if __name__ == "__main__":
    main()
