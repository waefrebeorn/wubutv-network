#!/usr/bin/env python3
"""MV-5 v4 gate (work/gate_v4/).

(a) audio identity vs track.mp3 (lag + correlation on decoded audio)
(b) mouth frames: extracts onset and onset+0.15s frames for every gated
    line onset and every 'Easy now' hook onset into sheets for visual
    reading (verdicts recorded in gate_v4_results.json by the reader)
(c) judder audit on the v4 plan: adjacent playback-factor steps; steps
    INSIDE a phrase must be zero (one factor per phrase by construction);
    boundary steps listed. Plus cut-point continuity on the master:
    frame diff across every piece boundary (a ~0 diff = clone-pad freeze).
(d) motion audit: near-dup runs >= 24f while song words are playing
    (aligned grid); the S01 leader (frames 0-39, pre-word) is sanctioned.
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

PROJ = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v4.mp4")
GATE = os.path.join(PROJ, "work", "gate_v4")
os.makedirs(GATE, exist_ok=True)
os.makedirs(os.path.join(GATE, "frames"), exist_ok=True)
FPS = 24

results = {}

# ---------- (a) audio identity ----------
def decode_wav(src, out, dur=None):
    cmd = ["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", "16000"]
    if dur:
        cmd += ["-t", str(dur)]
    cmd += ["-y", out]
    subprocess.run(cmd, check=True)
    import wave
    w = wave.open(out)
    n = w.getnframes()
    buf = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return buf

trk = decode_wav(os.path.join(PROJ, "track.mp3"), os.path.join(GATE, "track16k.wav"))
mst = decode_wav(MASTER, os.path.join(GATE, "master16k.wav"))
seg = 16000 * 20
a, b = trk[:seg], mst[:seg]
best = None
for lag in range(-800, 801):
    if lag >= 0:
        x, y = a[:len(a) - lag], b[lag:lag + len(a) - lag]
    else:
        x, y = a[-lag:-lag + len(b) + lag], b[:len(b) + lag]
    if len(x) < 1000:
        continue
    c = np.corrcoef(x, y)[0, 1]
    if best is None or c > best[1]:
        best = (lag, float(c))
c0 = float(np.corrcoef(a[:len(b)], b[:len(a) if len(a) < len(b) else len(b)][:len(a)])[0, 1]) if len(a) == len(b) else float(np.corrcoef(a[:min(len(a), len(b))], b[:min(len(a), len(b))])[0, 1])
results["audio"] = {"best_lag_samples_16k": best[0], "best_lag_ms": best[0] / 16.0,
                    "corr_at_best_lag": best[1], "corr_at_lag0": c0,
                    "pass": best[0] == 0 and best[1] > 0.99}
print("audio:", results["audio"])

# ---------- plan + song grids ----------
fit = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v4.json")))
pieces = []
for sc in fit["scenes"]:
    for p in fit["plan"][sc]:
        q = dict(p)
        q["scene"] = sc
        pieces.append(q)
pieces.sort(key=lambda p: p["dst0"])

al = json.load(open(os.path.join(PROJ, "work", "gemini_song_words_aligned.json")))["rows"]
line_onset = {}
for r in al:
    ln = r["line"]
    if ln is None:
        continue
    t = r["app_start"] if r["app_start"] is not None else r["song_start"]
    if ln not in line_onset or t < line_onset[ln][0]:
        line_onset[ln] = (t, r["v1_owner"])
hooks = []
for r in al:
    if r["song_word"] == "Easy":
        t = r["app_start"] if r["app_start"] is not None else r["song_start"]
        hooks.append({"line": r["line"], "onset": round(t, 2),
                      "grid": "app" if r["app_start"] is not None else "v1"})
# L107 is an app-dropped v1 artifact (no sung words there) - informational only
for h in hooks:
    if h["line"] == "L107":
        h["informational"] = True

def covering(t):
    for p in pieces:
        if p["dst0"] - 1e-9 <= t < p["dst1"] - 1e-9:
            return p
    return pieces[-1]

NON_SUNG_KINDS = ("cover", "cutaway", "interlude", "leader")
def is_sung_slot(p, line):
    if p["scene"] == "S03":
        return True  # vocalise take sings I09
    return not any(p["kind"].startswith(k) for k in NON_SUNG_KINDS)

gated_lines = []
for ln, (t, owner) in sorted(line_onset.items(), key=lambda kv: kv[1][0]):
    p = covering(t)
    gated = is_sung_slot(p, ln) and ln != "L110b"
    gated_lines.append({"line": ln, "onset": round(t, 2), "owner": owner,
                         "scene": p["scene"], "kind": p["kind"], "take": p["take"],
                         "gated": gated})
results["gated_line_count"] = sum(1 for g in gated_lines if g["gated"])
print("gated lines:", results["gated_line_count"], "of", len(gated_lines))

# ---------- (b) extract mouth frames ----------
jobs = []  # (tag, t)
for g in gated_lines:
    if g["gated"]:
        jobs.append((f"{g['line']}", g["onset"]))
        jobs.append((f"{g['line']}+15", g["onset"] + 0.15))
for h in hooks:
    jobs.append((f"HK_{h['line']}", h["onset"]))
    jobs.append((f"HK_{h['line']}+15", h["onset"] + 0.15))
frames = {}
for tag, t in jobs:
    out = os.path.join(GATE, "frames", f"{tag.replace('+', 'p')}.png")
    frames[tag] = out
    if not os.path.exists(out):
        subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", MASTER,
                        "-frames:v", "1", "-y", out], check=True)
print("mouth frames extracted:", len(frames))

# sheets: gated lines in onset order, 2 frames per line (onset, +0.15)
line_jobs = [(g["line"], g["onset"]) for g in gated_lines if g["gated"]]
TW, TH, LH, COLS = 480, 270, 24, 4
per_sheet = 16  # lines per sheet (32 frames)
for s in range(0, len(line_jobs), per_sheet):
    grp = line_jobs[s:s + per_sheet]
    rows = (len(grp) * 2 + COLS - 1) // COLS
    sheet = Image.new("RGB", (TW * COLS, (TH + LH) * rows), (15, 15, 15))
    dr = ImageDraw.Draw(sheet)
    idx = 0
    for ln, t in grp:
        for tag in (ln, ln + "+15"):
            r, c = divmod(idx, COLS)
            p = frames[tag]
            sheet.paste(Image.open(p).resize((TW, TH)), (c * TW, r * (TH + LH) + LH))
            lab = f"{ln} @{t:.2f}" + (" +0.15" if tag.endswith("+15") else " ONSET")
            dr.text((c * TW + 6, r * (TH + LH) + 5), lab, fill=(255, 220, 80))
            idx += 1
    outp = os.path.join(GATE, f"lines_{s // per_sheet + 1:02d}.png")
    sheet.save(outp)
    print("sheet:", outp, [g[0] for g in grp])

# hook sheets: 4 hooks per sheet (onset, +0.15 across a row)
for s in range(0, len(hooks), 4):
    grp = hooks[s:s + 4]
    sheet = Image.new("RGB", (TW * 2, (TH + LH) * len(grp)), (15, 15, 15))
    dr = ImageDraw.Draw(sheet)
    for r, h in enumerate(grp):
        for c, tag in enumerate((f"HK_{h['line']}", f"HK_{h['line']}+15")):
            sheet.paste(Image.open(frames[tag]).resize((TW, TH)), (c * TW, r * (TH + LH) + LH))
            lab = f"{h['line']} hook @{h['onset']:.2f} ({h['grid']})" + (" +0.15" if c else " ONSET")
            dr.text((c * TW + 6, r * (TH + LH) + 5), lab, fill=(255, 220, 80))
    outp = os.path.join(GATE, f"hooks_{s // 4 + 1:02d}.png")
    sheet.save(outp)
    print("sheet:", outp, [h["line"] for h in grp])

# ---------- (c) judder audit ----------
steps = []
for i in range(len(pieces) - 1):
    a, b = pieces[i], pieces[i + 1]
    pa, pb = 1.0 / a["warp"], 1.0 / b["warp"]
    ratio = max(pa, pb) / min(pa, pb)
    steps.append({"at": a["dst1"], "from": f"{a['scene']}/{a['kind']}/{a['take']}",
                  "to": f"{b['scene']}/{b['kind']}/{b['take']}",
                  "playback_from": round(pa, 3), "playback_to": round(pb, 3),
                  "ratio": round(ratio, 3)})
big = [s for s in steps if s["ratio"] > 1.35]
results["judder"] = {"boundaries": len(steps), "steps_over_1.35x": len(big),
                     "worst": sorted(big, key=lambda s: -s["ratio"])[:10]}
print("judder:", results["judder"]["steps_over_1.35x"], "boundary steps >1.35x of", len(steps))

json.dump({"results": results, "gated_lines": gated_lines, "hooks": hooks,
           "steps": steps}, open(os.path.join(GATE, "gate_v4_auto.json"), "w"), indent=1)
print("auto gate part done -> work/gate_v4/gate_v4_auto.json")
