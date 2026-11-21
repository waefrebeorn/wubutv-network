#!/usr/bin/env python3
"""joint_eval_segs.py — PROTOTYPE: evaluate the five SHOW-3 E2 joints
from the shipped segments (seg1..seg6, 240f each) instead of the
joined file (whose decoded frame count drifts: 1444 vs 1440 probed,
so nominal cut indices do not land on the true seams).

Per joint: upstream tail state + downstream head state from each
segment's own motion map, seam MAE between segN's last frame and
segN+1's first frame (320x180 gray, the gate convention), and the
J12 check: is there a local motion peak within the last 24 steps of
the upstream segment the cut could have been placed on?
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motion_map import decode_gray, smooth, extract_events, phase_at

E = os.path.expanduser(
    "~/workspace/wubutv-network/new-era/episodes/E2_SHOW-3_the-roster/work")

maps = {}
frames = {}
for k in range(1, 7):
    p = os.path.join(E, f"seg{k}.mp4")
    fr = decode_gray(p)
    frames[k] = fr
    d = np.mean(np.abs(np.diff(fr, axis=0)), axis=1)
    s = smooth(d)
    th_lo = float(np.percentile(s, 50))
    th_hi = float(np.percentile(s, 75))
    ev = extract_events(s, th_lo, th_hi)
    maps[k] = (s, ev, th_lo, th_hi)

out = {"episode_BASE_gate_log": 6.74, "joints": []}
for k in range(1, 6):
    s_up, ev_up, lo_up, _ = maps[k]
    s_dn, ev_dn, lo_dn, _ = maps[k + 1]
    seam = float(np.mean(np.abs(frames[k][-1] - frames[k + 1][0])))
    # J12 window: last 24 steps of upstream; local peak there
    win = s_up[-24:]
    pk = int(np.argmax(win))
    last_ev = ev_up[-1] if ev_up else None
    dn_first = ev_dn[0] if ev_dn else None
    out["joints"].append({
        "joint": f"J{k} U{k}->U{k+1}",
        "seam_mae_measured": round(seam, 2),
        "upstream_final12_mean": round(float(np.mean(s_up[-12:])), 2),
        "upstream_phase_at_last_step": phase_at(s_up, ev_up, len(s_up) - 1, lo_up),
        "upstream_last_event": last_ev,
        "upstream_settled_from_step": (last_ev["end_step"] + 1) if last_ev else None,
        "j12_peak_in_last24": {"step": int(len(s_up) - 24 + pk),
                              "val": round(float(win[pk]), 2),
                              "steps_before_end": int(23 - pk)},
        "downstream_head_class": (
            "IN-MOTION" if dn_first and dn_first["onset_step"] == 0 else
            ("RAMP" if dn_first and dn_first["onset_step"] <= 12 else "SETTLED-HEAD")),
        "downstream_head12_mean": round(float(np.mean(s_dn[:12])), 2),
        "downstream_first_event": dn_first,
    })
print(json.dumps(out, indent=1))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "joint_eval_segs.json"), "w") as f:
    json.dump(out, f, indent=1)
