#!/usr/bin/env python3
"""MV-7 OTAKU assembly: phrase-smooth warp per unit from take-word anchors.
Sung span of each take is uniformly warped (one factor per unit = phrase-smooth)
so take first/last sung words land on the song's sung span. Tail after the sung
span plays at natural speed (closed-mouth held). Every unit segment is forced to
exactly round(span*24) frames. Montage units: plain trim, no warp.
Writes work/otaku_assembly/segments + picture.mp4 (no audio) + assembly_map.json."""
import json, os, re, subprocess, sys

BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-7_the-nobody-man"
FPS = 24
SEG = f"{BASE}/work/otaku_assembly/segments"
os.makedirs(SEG, exist_ok=True)
units = json.load(open(f"{BASE}/work/otaku_units.json"))

NORM = {"spots": "sparks", "flipping": "flicking", "prayed": "made", "-made": "mad",
        "joints": "joins", "lonely": "low-lit", "same": "saved", "lessen": "lasts",
        "land": "lasts", "can't": "yeah", "cray": "grand"}
def norm(w):
    w = w.lower().strip(",.?!")
    return NORM.get(w, w)

def lyric_tokens(unit):
    toks = []
    for ln in unit["lines"]:
        toks += [norm(t) for t in re.split(r"[\s/]+", ln["lyric"]) if t.strip()]
    return toks

def find_span(take_words, toks):
    tw = [norm(w["word"]) for w in take_words]
    if not tw or not toks:
        return None
    # first occurrence of toks[0] (allow match on first 2 tokens), last occurrence of toks[-1] after it
    starts = [i for i, t in enumerate(tw) if t == toks[0]]
    if not starts:
        starts = [i for i, t in enumerate(tw) if t == toks[-1]]
        if not starts:
            return None
        i0 = starts[0]
    else:
        i0 = starts[0]
    ends = [i for i, t in enumerate(tw) if t == toks[-1] and i >= i0]
    if not ends:
        return None
    i1 = ends[0]
    # prefer an end that completes the sequence length roughly; if repeated hook, take the
    # occurrence whose span best matches expected token count
    i1 = min(ends, key=lambda e: (abs((e - i0 + 1) - len(toks)), e))
    return (take_words[i0]["start"], take_words[i1]["end"], i0, i1)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAIL:", " ".join(cmd)[:200]); print(r.stderr[-800:]); sys.exit(1)

def probe_dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())

amap = []
seg_files = []
for u in units:
    uid = u["unit"]
    REROLLED = {"U01", "U19", "U24", "U34", "U35", "U39"}
    tv = "t2" if uid in REROLLED and os.path.exists(f"{BASE}/takes/otaku/mv7o_{uid.lower()}_t2.mp4") else "t1"
    take = f"{BASE}/takes/otaku/mv7o_{uid.lower()}_{tv}.mp4"
    span = u["song_out"] - u["song_in"]
    frames = round(span * FPS)
    out = f"{SEG}/{uid}.mp4"
    seg_files.append(out)
    if not os.path.exists(take):
        amap.append({"unit": uid, "error": "TAKE MISSING"})
        print(uid, "TAKE MISSING"); continue
    tdur = probe_dur(take)
    VF = "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,format=yuv420p"
    if u["tag"] == "MONTAGE":
        run(["ffmpeg", "-y", "-v", "error", "-i", take, "-vf",
             f"{VF},trim=end_frame={frames},setpts=N/({FPS}*TB)",
             "-frames:v", str(frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", out])
        amap.append({"unit": uid, "tag": "MONTAGE", "frames": frames, "warp_speed": 1.0})
        print(uid, "montage frames", frames); continue
    twj = f"{BASE}/work/otaku_take_words/{uid}_{tv}.json" if tv == "t2" else f"{BASE}/work/otaku_take_words/{uid}.json"
    take_words = json.load(open(twj))["words"] if os.path.exists(twj) else []
    toks = lyric_tokens(u)
    found = find_span(take_words, toks)
    song_sung = u["sung_end"] - u["song_in"]
    if found:
        ts, te, i0, i1 = found
        anchor = "words"
    elif take_words:
        ts, te = take_words[0]["start"], take_words[-1]["end"]
        anchor = "all-words-fallback"
    else:
        ts, te = 0.3, max(0.6, tdur - 0.3)
        anchor = "rms-fallback"
    ts = max(0.0, ts - 0.04); te = min(tdur, te + 0.04)
    take_sung = max(0.3, te - ts)
    speed = take_sung / song_sung          # playback speed applied to sung span
    clamped = speed
    if speed < 0.5:
        clamped = 0.5
    m = 1.0 / clamped                       # setpts multiplier for sung span
    sung_frames = round(song_sung * FPS)
    tail_frames = frames - sung_frames
    parts = []
    sung_out = f"{SEG}/{uid}_sung.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{ts:.3f}", "-i", take, "-vf",
         f"{VF},setpts=(PTS-STARTPTS)*{m:.5f},trim=end_frame={sung_frames},tpad=stop_mode=clone:stop_duration=2,setpts=N/({FPS}*TB)",
         "-frames:v", str(sung_frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", sung_out])
    parts.append(sung_out)
    if tail_frames > 0:
        tail_src_start = te
        tail_out = f"{SEG}/{uid}_tail.mp4"
        avail = tdur - tail_src_start
        if avail >= tail_frames / FPS - 0.05:
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{tail_src_start:.3f}", "-i", take, "-vf",
                 f"{VF},trim=end_frame={tail_frames},tpad=stop_mode=clone:stop_duration=2,setpts=N/({FPS}*TB)",
                 "-frames:v", str(tail_frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", tail_out])
        else:
            # not enough tail: slow the remaining tail footage to fill (held pose, no words)
            mm = (tail_frames / FPS) / max(avail, 0.2)
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{tail_src_start:.3f}", "-i", take, "-vf",
                 f"{VF},setpts=(PTS-STARTPTS)*{mm:.5f},trim=end_frame={tail_frames},tpad=stop_mode=clone:stop_duration=2,setpts=N/({FPS}*TB)",
                 "-frames:v", str(tail_frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", tail_out])
        parts.append(tail_out)
    if len(parts) == 1:
        os.replace(parts[0], out)
    else:
        lst = f"{SEG}/{uid}.txt"
        open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
        run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", out])
    amap.append({"unit": uid, "tag": u["tag"], "frames": frames, "sung_frames": sung_frames,
                 "tail_frames": tail_frames, "take_span": [round(ts, 3), round(te, 3)],
                 "anchor": anchor, "warp_speed": round(speed, 3), "warp_speed_applied": round(clamped, 3)})
    print(uid, "speed", round(speed, 3), "anchor", anchor, "frames", frames)

json.dump(amap, open(f"{BASE}/work/otaku_assembly/assembly_map.json", "w"), indent=1)
lst = f"{BASE}/work/otaku_assembly/concat.txt"
open(lst, "w").write("".join(f"file '{p}'\n" for p in seg_files))
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
     "-c", "copy", f"{BASE}/work/otaku_assembly/picture.mp4"])
tot = sum(round((u["song_out"] - u["song_in"]) * FPS) for u in units)
print("expected frames:", tot)
r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                    "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0",
                    f"{BASE}/work/otaku_assembly/picture.mp4"], capture_output=True, text=True)
print("picture frames:", r.stdout.strip())
