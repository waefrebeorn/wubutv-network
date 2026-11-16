#!/usr/bin/env python3
"""MV-5 v5 master gates (Q10 repair) — run AFTER assemble_mv5_v5.py completes.
Checks: frames == 4954, duration ~206.417s, h264 1280x720 24fps, AAC 48k
stereo, x264 SEI crf=18.0, faststart (moov before mdat), md5, master-audio
agreement vs track.mp3 (waveform correlation, 7 windows, >0.99), and the
motion audit (no frozen run >=24f inside any SUNG piece — phrase-* kinds;
covers/gaps are montage by design and excluded).
Usage: python3 work/q10/gate_mv5_v5.py [master_path]
Writes work/q10/gate_v5.json.
"""
import hashlib, json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MASTER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    PROJ, "masters", "mv5_easy_now_easy_now_16x9_v5.mp4")
TRACK = os.path.join(PROJ, "track.mp3")
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v5.json")))
FPS = 24
OUT_JSON = os.path.join(PROJ, "work", "q10", "gate_v5.json")

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

ok = True
results = {}
def check(name, cond, detail=""):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {detail}")
    results[name] = {"pass": bool(cond), "detail": str(detail)}
    ok = ok and bool(cond)

print("master:", MASTER)
print("size:", os.path.getsize(MASTER))
m = md5(MASTER)
print("md5:", m)
results["md5"] = m
results["size"] = os.path.getsize(MASTER)

v = ffprobe(MASTER, ["-count_frames", "-select_streams", "v:0",
    "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration",
    "-show_entries", "format=duration", "-of", "json"])
vs, fmt = v["streams"][0], v["format"]
check("video codec h264", vs["codec_name"] == "h264", vs["codec_name"])
check("resolution 1280x720", (vs["width"], vs["height"]) == (1280, 720),
      f'{vs["width"]}x{vs["height"]}')
check("fps 24", vs["r_frame_rate"] == "24/1", vs["r_frame_rate"])
check("frames exactly 4954", int(vs["nb_read_frames"]) == 4954, vs["nb_read_frames"])
check("duration 206.417s", abs(float(fmt["duration"]) - 206.4167) < 0.05, fmt["duration"])

a = ffprobe(MASTER, ["-select_streams", "a:0",
    "-show_entries", "stream=codec_name,sample_rate,channels", "-of", "json"])["streams"][0]
check("audio AAC", a["codec_name"] == "aac", a["codec_name"])
check("audio 48k stereo", (a["sample_rate"], a["channels"]) == ("48000", 2),
      f'{a["sample_rate"]} {a["channels"]}ch')

sei = subprocess.run(["strings", MASTER], capture_output=True, text=True).stdout
line = [l for l in sei.splitlines() if "x264 - core" in l]
check("x264 SEI crf=18.0", bool(line) and "crf=18.0" in line[0],
      line[0][:120] if line else "NO SEI LINE")

with open(MASTER, "rb") as f:
    head = f.read(2_000_000)
check("faststart moov before mdat", 0 < head.find(b"moov") < head.find(b"mdat"),
      f'moov@{head.find(b"moov")} mdat@{head.find(b"mdat")}')

print("audio agreement (master vs track.mp3, 16k mono, 7 windows):")
mw, tw = wav16k(MASTER), wav16k(TRACK)
print(f"  lengths: master {len(mw)/16000:.2f}s track {len(tw)/16000:.2f}s")
cors = []
for start_s in (5, 30, 60, 90, 120, 150, 180):
    s = int(start_s * 16000)
    mm, tt = mw[s:s + 16000], tw[s:s + 16000]
    if len(mm) < 16000 or len(tt) < 16000:
        continue
    mm, tt = mm - mm.mean(), tt - tt.mean()
    c = float(np.dot(mm, tt) / (np.linalg.norm(mm) * np.linalg.norm(tt) + 1e-12))
    cors.append(c)
    print(f"  @{start_s}s corr={c:.4f}")
check("audio agreement corr > 0.99 all windows", cors and min(cors) > 0.99,
      f"min={min(cors):.4f}" if cors else "no windows")

# --- motion audit: no frozen run >=24f inside any SUNG (phrase-*) piece ---
def decode(scale):
    w, h = scale
    proc = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", MASTER, "-vf", f"scale={w}:{h},format=gray",
         "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True)
    raw = np.frombuffer(proc.stdout, dtype=np.uint8)
    nfr = raw.size // (w * h)
    return raw[:nfr * w * h].reshape(nfr, h, w).astype(np.int16)

def longest_run(seg):
    run = best = 0
    for d in seg:
        run = run + 1 if d < 0.5 else 0
        best = max(best, run)
    return best

frames = decode((160, 90))
diffs = np.abs(frames[1:] - frames[:-1]).mean(axis=(1, 2))
print(f"motion 160x90: {frames.shape[0]} frames, overall mean {diffs.mean():.3f}, "
      f"longest near-dup run {longest_run(diffs)}f")
worst = []
for sc in FIT["scenes"]:
    for p in FIT["plan"][sc]:
        if not p["kind"].startswith("phrase-"):
            continue
        va = int(round(p["dst0"] * FPS)); vb = int(round(p["dst1"] * FPS))
        seg = diffs[va:max(va + 1, vb - 1)]
        r = longest_run(seg)
        if r >= 24:
            worst.append({"scene": sc, "kind": p["kind"], "take": p["take"],
                          "dst": [p["dst0"], p["dst1"]], "run": r})
        print(f"  {sc} {p['kind']:22} {p['take']:16} "
              f"{p['dst0']:7.2f}-{p['dst1']:7.2f} longest-neardup {r}f"
              + ("  <-- FAIL >=24f" if r >= 24 else ""))
check("motion: no frozen run >=24f in any sung piece", not worst,
      f"{len(worst)} failing pieces" if worst else "0 failing pieces")
results["motion_failing_pieces"] = worst

# 320x180 second opinion on the overall longest run
frames2 = decode((320, 180))
diffs2 = np.abs(frames2[1:] - frames2[:-1]).mean(axis=(1, 2))
print(f"motion 320x180: {frames2.shape[0]} frames, overall mean {diffs2.mean():.3f}, "
      f"longest near-dup run {longest_run(diffs2)}f")
results["motion_320x180_longest_run"] = int(longest_run(diffs2))

json.dump(results, open(OUT_JSON, "w"), indent=1)
print(f"\nwrote {OUT_JSON}")
print("ALL GATES PASS" if ok else "GATES FAILED")
sys.exit(0 if ok else 1)
