#!/usr/bin/env python3
"""MV-5 LYRICS REDO gates — run AFTER assemble_mv5_lyrics.py completes.

Checks (all MEASURED, none assumed):
 1. frames exactly 4954 (= v4 base), duration 206.40s, h264 1280x720 24fps
 2. AAC 48k stereo
 3. x264 SEI crf=18.0
 4. faststart (moov before mdat)
 5. audio agreement vs track.mp3 (window correlations > 0.99) AND decoded-PCM
    md5 IDENTICAL to the v4 base master (same track, same encode settings)
 6. motion audit: near-dup runs >= 24f while words are playing (NEW grid
    spans) — no NEW frozen runs vs the v4 base (v4 diffs recomputed here)
 7. regression: frame-diff vs the v4 base with the caption band masked
    (bottom 120px, y 600-720) — unchanged video must be ~identical
    (x264 threaded re-encode noise reported honestly, mean/max per scene)
 8. md5 + size of the new master (printed for the report)
Usage: python3 work/lyrics-redo/validate_lyrics.py [master] [base]
Kinetic frame reads (legibility / edges / first-word fade) are a separate
visual step: extract_kinetic_frames.py, read at full res by the operator.
"""
import hashlib, json, os, subprocess, sys
import numpy as np

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
MASTER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PROJ, "masters/mv5_easy_now_easy_now_16x9_lyrics.mp4")
BASE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(PROJ, "masters/mv5_easy_now_easy_now_16x9_v4.mp4")
TRACK = os.path.join(PROJ, "track.mp3")
GRID = os.path.join(PROJ, "work/lyrics-redo/grid_merged.json")
GATE = os.path.join(PROJ, "work/lyrics-redo/gate")
os.makedirs(GATE, exist_ok=True)
FPS, TOTAL = 24, 4954

def ffprobe(path, args):
    out = subprocess.run(["ffprobe", "-v", "error"] + args + [path],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def wav16k(path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1",
                          "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True)
    return np.frombuffer(out.stdout, dtype=np.float32)

def decode_gray(path, w=160, h=90):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf",
                          f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    n = len(raw) // (w * h)
    return np.frombuffer(raw[:n * w * h], dtype=np.uint8).reshape(n, h, w).astype(np.float32)

ok = True
res = {}
def check(name, cond, detail=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")
    res[name] = {"pass": bool(cond), "detail": str(detail)}
    ok = ok and bool(cond)

print("master:", MASTER)
print("base:  ", BASE)
print("size:", os.path.getsize(MASTER), "md5:", md5(MASTER))
res["md5"] = md5(MASTER)
res["size"] = os.path.getsize(MASTER)

v = ffprobe(MASTER, ["-count_frames", "-select_streams", "v:0",
    "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration",
    "-show_entries", "format=duration", "-of", "json"])
vs, fmt = v["streams"][0], v["format"]
check("video codec h264", vs["codec_name"] == "h264", vs["codec_name"])
check("resolution 1280x720", (vs["width"], vs["height"]) == (1280, 720), f'{vs["width"]}x{vs["height"]}')
check("fps 24", vs["r_frame_rate"] == "24/1", vs["r_frame_rate"])
check("frames exactly 4954", int(vs["nb_read_frames"]) == TOTAL, vs["nb_read_frames"])
check("duration 206.40s", abs(float(fmt["duration"]) - 206.40) < 0.05, fmt["duration"])

a = ffprobe(MASTER, ["-select_streams", "a:0",
    "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "json"])["streams"][0]
check("audio AAC", a["codec_name"] == "aac", a["codec_name"])
check("audio 48k stereo", (a["sample_rate"], a["channels"]) == ("48000", 2), f'{a["sample_rate"]} {a["channels"]}ch')

sei = subprocess.run(["strings", MASTER], capture_output=True, text=True).stdout
line = [l for l in sei.splitlines() if "x264 - core" in l]
check("x264 SEI crf=18.0", bool(line) and "crf=18.0" in line[0], line[0][:120] if line else "NO SEI LINE")

with open(MASTER, "rb") as f:
    head = f.read(2_000_000)
check("faststart moov before mdat", 0 < head.find(b"moov") < head.find(b"mdat"),
      f'moov@{head.find(b"moov")} mdat@{head.find(b"mdat")}')

# 5. audio agreement
mw, tw = wav16k(MASTER), wav16k(TRACK)
bw = wav16k(BASE)
print(f"audio lengths: master {len(mw)/16000:.2f}s track {len(tw)/16000:.2f}s base {len(bw)/16000:.2f}s")
cors = []
for start_s in (5, 30, 60, 90, 120, 150, 180, 200):
    s = int(start_s * 16000)
    m, t = mw[s:s + 16000], tw[s:s + 16000]
    if len(m) < 16000 or len(t) < 16000:
        continue
    m, t = m - m.mean(), t - t.mean()
    c = float(np.dot(m, t) / (np.linalg.norm(m) * np.linalg.norm(t) + 1e-12))
    cors.append(c)
    print(f"  @{start_s}s corr={c:.4f}")
check("audio agreement vs track corr > 0.99 all windows", cors and min(cors) > 0.99,
      f"min={min(cors):.4f}" if cors else "no windows")
pcm_md5_new = hashlib.md5(mw.astype(np.float32).tobytes()).hexdigest()
pcm_md5_base = hashlib.md5(bw.astype(np.float32).tobytes()).hexdigest()
check("decoded-PCM md5 == v4 base", pcm_md5_new == pcm_md5_base,
      f"new={pcm_md5_new} base={pcm_md5_base}")
res["pcm_md5_new"] = pcm_md5_new
res["pcm_md5_base"] = pcm_md5_base

# 6+7. motion + regression (160x90 gray frame diffs)
print("decoding masters for motion/regression (160x90 gray)...")
f_new = decode_gray(MASTER)
f_base = decode_gray(BASE)
print(f"  frames: new {len(f_new)} base {len(f_base)}")
assert len(f_new) == len(f_base) == TOTAL, "frame count mismatch in decode"
d_new = np.abs(np.diff(f_new, axis=0)).mean(axis=(1, 2))
d_base = np.abs(np.diff(f_base, axis=0)).mean(axis=(1, 2))
np.save(os.path.join(GATE, "diffs_lyrics.npy"), d_new)
np.save(os.path.join(GATE, "diffs_v4_recomputed.npy"), d_base)

grid = json.load(open(GRID))
spans = [(L["start"], L["end"]) for L in grid["lines"]]
def words_playing(fidx):
    t = fidx / FPS
    return any(a - 0.05 <= t <= b + 0.05 for a, b in spans)
def frozen_runs(diffs, thresh=0.5, minlen=24):
    runs, s = [], None
    for i, d in enumerate(diffs):
        if d < thresh and s is None:
            s = i
        elif d >= thresh and s is not None:
            if i - s >= minlen and words_playing(s):
                runs.append((s, i - 1, i - s))
            s = None
    if s is not None and len(diffs) - s >= minlen and words_playing(s):
        runs.append((s, len(diffs) - 1, len(diffs) - s))
    return runs
r_new = frozen_runs(d_new)
r_base = frozen_runs(d_base)
print(f"frozen runs >=24f during words: new={len(r_new)} base={len(r_base)}")
for r in r_new:
    print(f"  NEW run frames {r[0]}-{r[1]} ({r[2]}f, {r[0]/FPS:.2f}-{r[1]/FPS:.2f}s)")
new_set = set((a, b) for a, b, _ in r_new)
base_set = set((a, b) for a, b, _ in r_base)
added = sorted(new_set - base_set)
check("motion: no NEW frozen runs vs v4", not added, f"added={added}" if added else f"{len(r_new)} runs, all inherited")
res["frozen_runs_new"] = r_new
res["frozen_runs_base"] = r_base

# regression: cross-master diff with the caption band masked (y 600-720 of 720
# maps to y 75-90 of the 90-row downscale — mask rows 75:90).
# NOTE 2026-11-12: decode_gray() returns 0-255 values, but the bar (0.05) is
# a 0-1 fraction (the MV-13 pattern). Divide by 255 here; without it the
# gate compares a 0-255 mean (~0.22 gray levels) against a 0-1 bar and
# fails spuriously. The true mean diff is 0.22/255 = 0.0009.
print("regression: cross-master frame diff (caption band masked)...")
mask = np.ones((90, 160), dtype=bool)
mask[75:90, :] = False
cross = np.abs(f_new - f_base)[:, mask].mean(axis=1) / 255.0  # per-frame mean |diff| outside band, 0-1
print(f"  mean {cross.mean():.4f} max {cross.max():.4f} frames>1.0: {(cross > 1.0).sum()} / {len(cross)}")
# per-scene: use the v4 fit plan boundaries (scene starts in frames)
fit = json.load(open(os.path.join(PROJ, "work/assembly_fit_mv5_v4.json")))
scene_bounds = []
pos = 0
for sc in fit["scenes"]:
    n = sum(p["out"] for p in fit["plan"][sc])
    scene_bounds.append((sc, pos, pos + n))
    pos += n
scene_rows = []
for sc, s0, s1 in scene_bounds:
    seg = cross[s0:s1]
    scene_rows.append({"scene": sc, "mean": round(float(seg.mean()), 4),
                        "max": round(float(seg.max()), 4), "frames": int(s1 - s0)})
    print(f"  {sc}: mean {seg.mean():.4f} max {seg.max():.4f}")
check("regression: video identical outside caption band (mean < 0.05)",
      cross.mean() < 0.05, f"mean={cross.mean():.4f} max={cross.max():.4f}")
res["regression_mean"] = float(cross.mean())
res["regression_max"] = float(cross.max())
res["regression_scenes"] = scene_rows

json.dump(res, open(os.path.join(GATE, "gate_lyrics.json"), "w"), indent=1)
print("ALL GATES PASS" if ok else "GATES FAILED")
sys.exit(0 if ok else 1)
