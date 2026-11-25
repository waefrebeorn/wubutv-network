import json, os, subprocess, hashlib
P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(P, "work/segments")
def md5f(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()
def seg(take, start, k, n_frames, out):
    vf = f"setpts={k}*(PTS-STARTPTS),fps=24,scale=1280:720:flags=lanczos,format=yuv420p,tpad=stop_mode=clone:stop_duration=3"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-ss",str(start),"-i",take,"-vf",vf,
           "-frames:v",str(n_frames),"-an","-c:v","libx264","-preset","veryfast","-crf","14",out], check=True)
    got = int(subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-count_frames",
        "-show_entries","stream=nb_read_frames","-of","csv=p=0",out], capture_output=True, text=True).stdout.strip())
    dur = float(subprocess.run(["ffprobe","-v","error","-select_streams","v:0",
        "-show_entries","stream=duration","-of","csv=p=0",out], capture_output=True, text=True).stdout.strip())
    assert got == n_frames, f"{out}: want {n_frames} got {got}"
    assert abs(dur - n_frames/24) < 0.08, f"{out}: dur {dur}"
    return got
meta = json.load(open(os.path.join(SEG, "segments.json")))
# seg_00: S01 head slowed sprint, extended (0 -> frame 109)
out0 = os.path.join(SEG, "seg_00_s01_0.mp4")
seg(os.path.join(P, "takes", "mv26_s01_t1.mp4"), 0.00, 1.9000, 109, out0)
meta[0].update({"kind":"N","take":"mv26_s01_t1.mp4","take_start":0.00,"k":1.9000,"out":[0.0,109/24],"frames":109,"md5":md5f(out0),
                "note":"FIX: head extended; slow-mo sprint 1.9x"})
# seg_01: S01 pre-word insert = S13 platform close-up tail (frame 109 -> 147)
out1 = os.path.join(SEG, "seg_01_s01_1.mp4")
seg(os.path.join(P, "takes", "mv26_s13_t1.mp4"), 8.30, 0.9314, 38, out1)
meta[1].update({"kind":"N","take":"mv26_s13_t1.mp4","take_start":8.30,"k":0.9314,"out":[109/24,147/24],"frames":38,"md5":md5f(out1),
                "note":"FIX: replaces static s01 tail; unused s13 tail close-up, eyes-darting insert"})
json.dump(meta, open(os.path.join(SEG, "segments.json"), "w"), indent=1)
total = sum(m["frames"] for m in meta)
assert total == 2871, total
concat = [os.path.join(SEG, f) for f in sorted(os.listdir(SEG)) if f.startswith("seg_") and f.endswith(".mp4")]
# order by numeric prefix
concat.sort(key=lambda p: int(os.path.basename(p).split("_")[1]))
with open(os.path.join(SEG, "concat.txt"), "w") as f:
    for c in concat: f.write(f"file '{c}'\n")
joined = os.path.join(P, "work/swing/joined.mp4")
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",
                os.path.join(SEG, "concat.txt"), "-c", "copy", joined], check=True)
print("FIX DONE, total frames:", total, "segments:", len(concat))
