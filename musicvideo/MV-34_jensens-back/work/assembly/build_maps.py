#!/usr/bin/env python3
"""MV-34 assembly — capped-QP map builder (MV-30 fix2 lineage,
build_maps2.py ported). Per WARP segment: anchors from the standing
renderer's build_map over the FA word pairs; chunk map through the
anchors; if any chunk ratio leaves [0.50, 2.00], the capped-warp QP
runs on a 96/s grid (derivative fidelity to the chunk map + anchor
penalties, box [0.50, 2.00], exact span integral). PLAIN/COVER
segments get constant-ratio maps. Cut-point moves are DISABLED — all
spans were hand-derived from the takes' own audio at prep (re-chunks
ledgered in ASSEMBLY_LOG); head/tail chunk ratios are logged.

Outputs maps/segNNN_capped.json per segment, map_summary.json, and
histogram.json — the PRE-ENCODE STRUCTURAL GATE: any local ratio
outside [0.50, 2.00] across every map fails the build here.
"""
import importlib.util, json, math, os
import numpy as np

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = os.path.join(P, "work", "assembly")
MAPS = os.path.join(A, "maps")
FPS = 24.0
CAP_LO, CAP_HI = 0.50, 2.00
GRID = 96.0
HERO_SCENES = {"S01", "S08", "S09", "S10"}

spec = importlib.util.spec_from_file_location(
    "render_warp", os.path.expanduser(
        "~/workspace/research_notes/lipsync-fix-20261122/prototype_warp/render_warp.py"))
rw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rw)


def project_box_sum(v, dt, total):
    target = total / dt
    lo, hi = -100.0, 100.0
    for _ in range(60):
        mu = 0.5 * (lo + hi)
        if float(np.clip(v - mu, CAP_LO, CAP_HI).sum()) > target:
            lo = mu
        else:
            hi = mu
    return np.clip(v - 0.5 * (lo + hi), CAP_LO, CAP_HI)


def solve_capped(d, dt, total, G, targets, w, iters=2500):
    N = len(d)
    L = 2.0 + (2.0 * float(np.sum(w * np.sum(G * G, axis=1)))
               if G is not None and len(targets) else 0.0)
    c = project_box_sum(d.copy(), dt, total)
    y = c.copy()
    tf = 1.0
    for _ in range(iters):
        g = 2.0 * (y - d)
        if G is not None and len(targets):
            g = g + 2.0 * (G.T @ (w * (G @ y - targets)))
        c_new = project_box_sum(y - g / L, dt, total)
        t_new = 0.5 * (1.0 + math.sqrt(1.0 + 4.0 * tf * tf))
        y = c_new + ((tf - 1.0) / t_new) * (c_new - c)
        delta = float(np.max(np.abs(c_new - c)))
        c, tf = c_new, t_new
        if delta < 1e-10:
            break
    return project_box_sum(c, dt, total)


def chunk_ratios(pts):
    return [(pts[i + 1][1] - pts[i][1]) / (pts[i + 1][0] - pts[i][0])
            for i in range(len(pts) - 1)]


plan = json.load(open(os.path.join(A, "segment_plan.json")))
os.makedirs(MAPS, exist_ok=True)
summary = {"segments": []}
hist_samples = []

for e in plan:
    idx = e["idx"]
    t0, t1 = [float(x) for x in e["take_span"]]
    s0, s1 = [float(x) for x in e["song_span"]]
    map_path = os.path.join(MAPS, f"seg{idx:03d}_capped.json")
    rec_path = os.path.join(MAPS, f"seg{idx:03d}_rec.json")
    if e["kind"] in ("PLAIN", "COVER"):
        ratio = (s1 - s0) / (t1 - t0)
        assert CAP_LO - 1e-9 <= ratio <= CAP_HI + 1e-9, \
            f"seg{idx:03d} plain ratio {ratio} out of cap"
        tg = np.array([t0, t1])
        yg = np.array([s0, s1])
        rec = {"seg": idx, "scene": e["scene"], "kind": e["kind"],
               "take": e["take"], "take_span": [t0, t1], "song_span": [s0, s1],
               "method": "constant-ratio", "ratio": round(ratio, 4),
               "word_drifts": []}
        hist_samples.extend([ratio] * max(2, int((s1 - s0) * FPS)))
    else:
        # anchors + QP penalties run on the ALIGN lists (drop_idx words
        # carried); drift is reported on the FULL paired lists. Onsets
        # are clamped into the (frame-quantized) spans — a word can sit
        # up to 1 frame outside its segment edge after quantization.
        def clamp(ws, lo, hi):
            return [{"word": w["word"],
                     "start": min(max(w["start"], lo), hi)} for w in ws]
        asw = clamp(e["align_song_words"], s0, s1)
        atw = clamp(e["align_take_words"], t0, t1)
        sw = clamp(e["song_words"], s0, s1)
        tw = clamp(e["take_words"], t0, t1)
        mean = (s1 - s0) / (t1 - t0)
        assert CAP_LO - 1e-9 <= mean <= CAP_HI + 1e-9, \
            f"seg{e['idx']:03d}: mean ratio {mean:.3f} infeasible"
        anchors = rw.build_map(asw, atw, (t0, t1), (s0, s1))
        inner = [(a["take_time"], a["song_time"]) for a in anchors
                 if t0 + 1e-9 < a["take_time"] < t1 - 1e-9]
        pts = [(t0, s0)] + inner + [(t1, s1)]
        ks = chunk_ratios(pts)
        all_in = all(CAP_LO - 1e-9 <= k <= CAP_HI + 1e-9 for k in ks)

        def chunk_eval(tq, pts=pts):
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            return float(np.interp(tq, xs, ys))

        rounds = []
        if all_in:
            tg = np.linspace(t0, t1, int(math.ceil((t1 - t0) * GRID)) + 1)
            yg = np.array([chunk_eval(x) for x in tg])
            method = "chunk (already in cap)"
        else:
            N = int(math.ceil((t1 - t0) * GRID))
            dt = (t1 - t0) / N
            mids = t0 + (np.arange(N) + 0.5) * dt
            xs = np.array([p[0] for p in pts])
            seg_i = np.clip(np.searchsorted(xs, mids) - 1, 0, len(ks) - 1)
            d = np.array([ks[i] for i in seg_i])
            anchor_times = {round(ta, 6) for ta, _ in inner}
            extra = []
            for sww, tww in zip(asw, atw):
                if t0 + 1e-9 < tww["start"] < t1 - 1e-9 and \
                        round(tww["start"], 6) not in anchor_times:
                    extra.append((tww["start"], sww["start"]))
            pen = inner + extra
            if pen:
                G = np.zeros((len(pen), N))
                for ai, (ta, sa_) in enumerate(pen):
                    rel = ta - t0
                    full = int(math.floor(rel / dt))
                    G[ai, :min(full, N)] = dt
                    if full < N:
                        G[ai, full] = rel - full * dt
                targets = np.array([sa_ - s0 for _, sa_ in pen])
            else:
                G, targets = None, np.zeros(0)
            n_anchor = len(inner)
            base_w = 1500.0 if e["scene"] in HERO_SCENES else 300.0
            c = None
            for rnd in range(4):
                if pen:
                    w = np.concatenate([
                        np.full(n_anchor, base_w * (4.0 ** rnd)),
                        np.full(len(extra), 25.0)])
                else:
                    w = np.zeros(0)
                c = solve_capped(d, dt, s1 - s0, G, targets, w)
                drifts = ([float(x) for x in (G @ c - targets) * 1000.0]
                          if pen else [])
                worst = max((abs(x) for x in drifts[:n_anchor]), default=0.0)
                rounds.append({"round": rnd,
                               "weight": float(base_w * (4.0 ** rnd)),
                               "worst_anchor_drift_ms": round(worst, 1)})
                if worst <= (120.0 if e["scene"] in HERO_SCENES else 250.0) \
                        or rnd == 3:
                    break
            tg = t0 + np.arange(N + 1) * dt
            yg = np.concatenate([[s0], s0 + np.cumsum(c * dt)])
            yg[-1] = s1
            method = "capped warp"
        fine_t = np.linspace(t0, t1, 20001)
        fine_d = np.diff(np.interp(fine_t, tg, yg)) / np.diff(fine_t)
        cmin, cmax = float(fine_d.min()), float(fine_d.max())
        assert cmin >= CAP_LO - 1e-6 and cmax <= CAP_HI + 1e-6, \
            f"seg{idx:03d}: final derivative out of box [{cmin},{cmax}]"
        hist_samples.extend(float(x) for x in
                            np.diff(yg) / np.diff(tg) if x > 0)
        drop_set = set(e.get("drop_idx", []))
        word_drifts = []
        for wi, (sww, tww) in enumerate(zip(sw, tw)):
            img = float(np.interp(tww["start"], tg, yg))
            word_drifts.append({
                "word": sww["word"].strip(),
                "song_onset": sww["start"], "take_onset": tww["start"],
                "carried": wi in drop_set,
                "drift_ms": round((img - sww["start"]) * 1000.0, 1)})
        worst_word = max(word_drifts, key=lambda r: abs(r["drift_ms"])) \
            if word_drifts else None
        rec = {"seg": idx, "scene": e["scene"], "kind": "WARP",
               "take": e["take"], "take_span": [t0, t1], "song_span": [s0, s1],
               "method": method,
               "chunk_ratios": [round(k, 3) for k in ks],
               "capped": {"ratio_min": round(cmin, 4),
                          "ratio_max": round(cmax, 4)},
               "qp_rounds": rounds, "penalty_extra_words": len(extra),
               "worst_word_drift": worst_word, "word_drifts": word_drifts}
        print(f"seg{idx:03d} {e['scene']:6s} method={method} chunks="
              f"{[round(k, 2) for k in ks]} -> [{cmin:.3f},{cmax:.3f}] "
              f"worst drift {worst_word['drift_ms'] if worst_word else 0} ms")
    summary["segments"].append(rec)
    json.dump(rec, open(rec_path, "w"), indent=1)
    json.dump({"seg": idx, "scene": e["scene"],
               "take_span": [float(t0), float(t1)], "song_span": [s0, s1],
               "anchors": (rw.build_map(e["align_song_words"],
                                        e["align_take_words"],
                                        (t0, t1), (s0, s1))
                           if e["kind"] == "WARP" else []),
               "method": rec["method"],
               "t_grid": [round(float(x), 6) for x in tg],
               "y_grid": [round(float(x), 6) for x in yg]},
              open(map_path, "w"))

json.dump(summary, open(os.path.join(A, "map_summary.json"), "w"), indent=1)

# ---- warp-slope histogram: the pre-encode structural gate ----
hs = np.array(hist_samples)
bins = [0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 1.10, 1.25, 1.50, 1.75, 2.00]
counts, _ = np.histogram(hs, bins=bins)
hist = {"samples": int(len(hs)), "ratio_min": round(float(hs.min()), 4),
        "ratio_max": round(float(hs.max()), 4),
        "bins": {f"{bins[i]:.2f}-{bins[i + 1]:.2f}": int(counts[i])
                 for i in range(len(counts))},
        "out_of_cap": int(int((hs < CAP_LO - 1e-6).sum()) +
                          int((hs > CAP_HI + 1e-6).sum())),
        "gate": "PASS" if float(hs.min()) >= CAP_LO - 1e-6
                and float(hs.max()) <= CAP_HI + 1e-6 else "BLOCK"}
json.dump(hist, open(os.path.join(A, "histogram.json"), "w"), indent=1)
print("HISTOGRAM:", json.dumps(hist))
assert hist["gate"] == "PASS", "WARP-SLOPE GATE BLOCKED"
print("MAPS_DONE")
