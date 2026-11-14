#!/usr/bin/env python3
"""MV-7 REBUILD-2 re-cut — measurement stage.
Builds the full line table (T lines from plan_data + chant lines + outro),
resolves take word slices, measures per-line VISIBLE-mouth lag from the
mouth-patch dark-red openness curve (build_rescue5 metric), checks song
RMS onsets in chant windows, emits anchors.json + head-strip grids.
NO rendering here."""
import json, subprocess, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan_data import T, ASSIGN, resolve, song_words, take_words, lyric_tokens, norm, BASE, FPS

W, H = 1248, 704
OUT = f"{BASE}/work/rebuild2_recut"
os.makedirs(f"{OUT}/strips", exist_ok=True)

# ---------- line table ----------
# chant lines: ref, lyric, a, b, kind, take_key, slice_spec
CHANT = [
 ("I1a","I'm The Nobody Man",0.00,2.485,"KEEP","U01t2",("words",0,4)),
 ("I1b","I'm The Nobody Man",2.485,4.97,"KEEP","U01t2",("words",4,6)),
 ("I1c","I'm The Nobody Man",4.97,7.445,"RESCUE","U02",("words",0,4)),
 ("I1d","I'm The Nobody Man",7.445,9.92,"RESCUE","U02",("words",4,8)),
 ("I2a","I'm The Nobody Man",9.92,12.16,"KEEP","U03",("words",0,4)),
 ("I2b","I'm The Nobody Man",12.16,14.40,"KEEP","U03",("words",4,8)),
 ("I2c","I'm The Nobody Man",14.40,19.58,"KEEP","U04",("words",0,4)),
 ("C1.Ta","Nobody Man",67.80,69.85,"COND","R16A",("all",)),
 ("C1.Tb","Nobody Man",69.85,71.90,"STRUCT","R16B",("all",)),
 ("C1.Tc","Nobody Man",71.90,73.87,"KEEP","R17A",("all",)),
 ("C1.Td","Nobody Man",73.87,75.84,"KEEP","R17B",("all",)),
 ("FC.Ta","I'm The Nobody Man",173.30,176.26,"KEEP","U39t2",("words",0,4)),
 ("FC.Tb","Nobody Man",176.26,178.30,"KEEP","U39t2",("words",4,6)),
 ("FC.Tc","Nobody Man",178.30,181.44,"KEEP","U40",("words",0,2)),
 ("FC.Td","Nobody Man",181.44,183.24,"KEEP","U40",("words",2,3)),
]
LINES = []
for ref, lyric, a, b, unit in T:
    kind, key = ASSIGN[ref]
    if ref == "C1.8":
        lyric = "Nobody Man, Nobody Man"
    LINES.append({"ref": ref, "lyric": lyric, "a": a, "b": b, "kind": kind,
                  "key": key, "unit": unit, "chant": False})
for ref, lyric, a, b, kind, key, spec in CHANT:
    LINES.append({"ref": ref, "lyric": lyric, "a": a, "b": b, "kind": kind,
                  "key": key, "unit": key, "chant": True, "spec": spec})
LINES.sort(key=lambda L: L["a"])

# ---------- take word slices ----------
def slice_for(L, chain_state):
    path, wjson = resolve(L["key"])
    tw = take_words(wjson)
    if L["key"].startswith("R"):
        return tw, path
    if L.get("spec"):
        s = L["spec"]
        if s[0] == "all":
            return tw, path
        return tw[s[1]:s[2]], path
    # U-take shared across lines: sequential match via plan_data.match_slice
    from plan_data import match_slice
    toks = lyric_tokens(L["lyric"])
    # expand hyphenated tokens to match ASR splitting
    exp = []
    for t in toks:
        exp.extend(t.split("-"))
    st = chain_state.get(L["key"], 0)
    m = match_slice(tw, exp, st)
    if m is None:
        return None, path
    chain_state[L["key"]] = m[1] + 1
    return tw[m[0]:m[1] + 1], path

# ---------- decode + openness ----------
def decode(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                       capture_output=True)
    arr = np.frombuffer(p.stdout, dtype=np.uint8)
    n = len(arr) // (W * H * 3)
    return arr[:n * W * H * 3].reshape(n, H, W, 3)

def openness_curve(frames):
    x0, x1 = int(0.455 * W), int(0.555 * W)
    y0, y1 = int(0.52 * H), int(0.63 * H)
    patch = frames[:, y0:y1, x0:x1].astype(np.int16)
    return ((patch[:, :, :, 0] < 110) & (patch[:, :, :, 0] - patch[:, :, :, 2] > 8)).mean(axis=(1, 2))

def mouth_event(curve, t_on, t_word_end):
    """First frame >= t_on-0.05 where score crosses thr (sustained 2 of 3)."""
    lo = max(0, int(round((t_on - 0.05) * FPS)))
    hi = min(len(curve) - 1, int(round(max(t_word_end, t_on + 0.35) * FPS)))
    win = curve[lo:hi + 1]
    if len(win) == 0:
        return None, 0.0
    thr = max(0.015, 0.35 * float(win.max()))
    for i in range(len(win)):
        if win[i] > thr and (i + 2 >= len(win) or (win[i + 1] > thr * 0.7 or win[min(i + 2, len(win) - 1)] > thr * 0.7)):
            return (lo + i) / FPS, float(win[i])
    return None, float(win.max())

# ---------- song RMS onsets (chant sanity) ----------
def song_rms_onsets():
    import wave, struct
    wf = wave.open(f"{BASE}/work/track_16k.wav")
    n = wf.getnframes(); sr = wf.getframerate()
    raw = np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    hop = int(sr * 0.01)
    m = len(raw) // hop
    rms = np.sqrt((raw[:m * hop].reshape(m, hop) ** 2).mean(axis=1))
    out = {}
    for label, a, b in [("intro", 0.0, 19.58), ("tags", 67.8, 75.84), ("fctag", 173.3, 183.24)]:
        ia, ib = int(a * 100), int(b * 100)
        seg = rms[ia:ib]
        flux = np.maximum(0, np.diff(seg))
        peaks = []
        last = -200
        for i in range(1, len(flux)):
            if flux[i] > 0.045 and i - last > 110 and flux[i] == flux[max(0, i - 5):i + 6].max():
                peaks.append(round(a + i * 0.01, 2)); last = i
        out[label] = peaks
    return out

def main():
    chain = {}
    results = []
    strips = []  # (label, img)
    # resolve all slices first (cheap), then group by take so each take is
    # decoded exactly once and released
    jobs = []
    for L in LINES:
        sl, path = slice_for(L, chain)
        rec = {"ref": L["ref"], "lyric": L["lyric"], "a": L["a"], "b": L["b"],
               "kind": L["kind"], "key": L["key"], "chant": L["chant"], "take": path}
        results.append(rec)
        if L["kind"] in ("STRUCT", "MONTAGE"):
            rec["slice"] = None
            continue
        if sl is None:
            rec["error"] = "SLICE NOT FOUND"
            continue
        rec["slice"] = [{"w": w["word"], "s": w["start"], "e": w["end"]} for w in sl]
        jobs.append((L, sl, path, rec))
    from collections import defaultdict
    by_take = defaultdict(list)
    for job in jobs:
        by_take[job[2]].append(job)
    for path, tlines in by_take.items():
        frames = decode(path)
        curve = openness_curve(frames)
        for L, sl, _p, rec in tlines:
            pass
        for L, sl, _p, rec in tlines:
            _measure_line(L, sl, frames, curve, rec, strips)
        del frames, curve
    _finish(results, strips)

def _measure_line(L, sl, frames, curve, rec, strips):
    w1 = sl[0]
    ev, sc = mouth_event(curve, w1["start"], w1["end"])
    rec["head_audio_onset"] = w1["start"]
    rec["head_event"] = ev
    rec["head_lag"] = None if ev is None else round(ev - w1["start"], 3)
    rec["head_score_at_audio_onset"] = float(curve[min(len(curve) - 1, int(round(w1["start"] * FPS)))])
    rec["curve_max"] = float(curve.max())
    if L["kind"] == "COND" or L["ref"] in ("C1.Ta",):
        evs = []
        for w in sl:
            e2, _ = mouth_event(curve, w["start"], w["end"])
            evs.append(None if e2 is None else round(e2 - w["start"], 3))
        rec["word_lags"] = evs
    # head strip: frames at audio onset, event-1, event, event+1, event+3
    cx0, cy0, cw, ch = int(0.30 * W), int(0.26 * H), int(0.32 * W), int(0.34 * H)
    picks = []
    fa = int(round(w1["start"] * FPS))
    fe = int(round(ev * FPS)) if ev is not None else fa
    for f in (fa, fe - 1, fe, fe + 1, fe + 3):
        f = min(len(frames) - 1, max(0, f))
        picks.append(frames[f][cy0:cy0 + ch, cx0:cx0 + cw])
    strips.append((L["ref"], np.concatenate(picks, axis=1)))

def _finish(results, strips):
    json.dump({"lines": results, "song_rms_onsets": song_rms_onsets()},
              open(f"{OUT}/anchors.json", "w"), indent=1)
    # strip grids: 8 lines per grid, each strip scaled down
    per = 8
    for gi in range(0, len(strips), per):
        batch = strips[gi:gi + per]
        rows = []
        for label, s in batch:
            small = s[::2, ::2]
            lab = np.zeros((18, small.shape[1], 3), dtype=np.uint8)
            rows.append(np.concatenate([lab, small], axis=0))
        h = max(r.shape[0] for r in rows)
        rows = [np.pad(r, ((0, h - r.shape[0]), (0, 0), (0, 0))) for r in rows]
        grid = np.concatenate(rows, axis=0)
        gp = f"{OUT}/strips/headstrips_{gi // per:02d}.raw"
        grid.tofile(gp)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                        "-s", f"{grid.shape[1]}x{grid.shape[0]}", "-r", "1", "-i", gp,
                        "-frames:v", "1", f"{OUT}/strips/headstrips_{gi // per:02d}.jpg"], check=True)
        os.remove(gp)
        print("grid", gi // per, [b[0] for b in batch])
    for r in results:
        print(r["ref"], r["kind"], r["key"], "lag=", r.get("head_lag"),
              "ev=", r.get("head_event"), "err=", r.get("error", ""))

if __name__ == "__main__":
    main()
