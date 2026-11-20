import json, os, subprocess, hashlib
P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(P, "work/segments"); os.makedirs(SEG, exist_ok=True)
FPS = 24
F = lambda fr: fr / 24.0
# (scene, take, [(kind, take_start, k, out_frame_start, out_frame_end)])
# W = warped sung span (k from word-span alignment); N = natural cover.
# SEGMENT LAW: setpts warp FIRST, then fps=24 resample. Every segment asserted
# for frames AND duration. Chant (S05-S08+S13/S14 donors) = natural-speed
# sub-cuts on chant onsets. S04 phrase B is a BAD-WORD montage (song holds
# "poop" 3.3s; take sings it in 0.46s -> cannot land in caps).
PLAN = [
 (1,  "mv26_s01_t1.mp4", [("N",0.00,1.4931,F(0),F(86)),("N",8.24,1.4441,F(86),F(147)),("W",2.40,1.1630,F(147),F(310))]),
 (2,  "mv26_s02_t2.mp4", [("N",0.00,1.3021,F(310),F(375)),("N",8.56,1.0,F(375),F(404)),("W",2.08,1.2217,F(404),F(594))]),
 (3,  "mv26_s03_t1.mp4", [("N",0.00,1.0251,F(594),F(687)),("W",3.78,0.7375,F(687),F(727)),("N",6.04,1.0,F(727),F(768))]),
 (4,  "mv26_s04_t1.mp4", [("W",4.00,1.3047,F(768),F(830)),("W",6.28,1.7926,F(830),F(867)),("N",2.16,1.0,F(867),F(890)),("N",8.00,1.0,F(890),F(923)),("N",0.00,1.0,F(923),F(972))]),
 (5,  "mv26_s05_t2.mp4", [("N",0.00,1.0,F(972),F(1042))]),
 (13, "mv26_s13_t1.mp4", [("N",0.00,1.0,F(1042),F(1112))]),
 (14, "mv26_s14_t1.mp4", [("N",0.00,1.0,F(1112),F(1182))]),
 (6,  "mv26_s06_t1.mp4", [("N",0.00,1.0,F(1182),F(1252))]),
 (7,  "mv26_s07_t1.mp4", [("N",0.00,1.0,F(1252),F(1322))]),
 (8,  "mv26_s08_t1.mp4", [("N",0.00,1.0,F(1322),F(1392))]),
 (5,  "mv26_s05_t2.mp4", [("N",3.30,1.0,F(1392),F(1447))]),
 (13, "mv26_s13_t1.mp4", [("N",2.92,1.0,F(1447),F(1517))]),
 (14, "mv26_s14_t1.mp4", [("N",3.90,1.0,F(1517),F(1587))]),
 (6,  "mv26_s06_t1.mp4", [("N",3.20,1.0,F(1587),F(1657))]),
 (7,  "mv26_s07_t1.mp4", [("N",6.34,1.0,F(1657),F(1727))]),
 (6,  "mv26_s06_t1.mp4", [("N",6.80,1.0,F(1727),F(1797))]),
 (14, "mv26_s14_t1.mp4", [("N",7.00,1.0,F(1797),F(1852))]),
 (5,  "mv26_s05_t2.mp4", [("N",6.60,1.0,F(1852),F(1922))]),
 (8,  "mv26_s08_t1.mp4", [("N",7.30,1.0,F(1922),F(1978))]),
 (9,  "mv26_s09_t2.mp4", [("N",0.00,1.5056,F(1978),F(2064))]),
 (9,  "mv26_s09_t3.mp4", [("W",1.32,0.8865,F(2064),F(2124)),("N",4.14,1.0,F(2124),F(2141))]),
 (9,  "mv26_s09_t2.mp4", [("N",5.18,1.0,F(2141),F(2248))]),
 (9,  "mv26_s09_t3.mp4", [("W",4.84,0.9414,F(2248),F(2309))]),
 (10, "mv26_s10_t1.mp4", [("N",0.00,1.1792,F(2309),F(2592))]),
 (11, "mv26_s11_t1.mp4", [("N",0.00,1.6281,F(2592),F(2828)),("W",6.04,0.5357,F(2828),F(2846)),("N",7.44,1.0,F(2846),F(2871))]),
]
def frames(o0, o1): return round(o1*FPS) - round(o0*FPS)
def md5f(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
    return h.hexdigest()
def seg(take, start, k, n_frames, out):
    vf = f"setpts={k}*(PTS-STARTPTS),fps=24,scale=1280:720:flags=lanczos,format=yuv420p,tpad=stop_mode=clone:stop_duration=3"
    cmd = ["ffmpeg","-y","-loglevel","error","-ss",str(start),"-i",take,"-vf",vf,
           "-frames:v",str(n_frames),"-an","-c:v","libx264","-preset","veryfast","-crf","14",out]
    subprocess.run(cmd, check=True)
    got = int(subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-count_frames",
        "-show_entries","stream=nb_read_frames","-of","csv=p=0",out], capture_output=True, text=True).stdout.strip())
    dur = float(subprocess.run(["ffprobe","-v","error","-select_streams","v:0",
        "-show_entries","stream=duration","-of","csv=p=0",out], capture_output=True, text=True).stdout.strip())
    return got, dur
log = open(os.path.join(P,"work/swing/build.log"),"w")
notes = open(os.path.join(P,"work/assembly_notes.md"),"a")
manifest_path = os.path.join(SEG,"segments.json")
segs_meta, concat, total = [], [], 0
for n, takef, parts in PLAN:
    take = os.path.join(P, "takes", takef)
    for i, (kind, ts, k, o0, o1) in enumerate(parts):
        nfr = frames(o0, o1)
        out = os.path.join(SEG, f"seg_{len(segs_meta):02d}_s{n:02d}_{i}.mp4")
        got, dur = seg(take, ts, k, nfr, out)
        msg = f"S{n}.{i} {kind} k={k} want {nfr}f got {got} dur {dur:.3f} (want {nfr/24:.3f})"
        print(msg, flush=True); log.write(msg+"\n"); log.flush()
        assert got == nfr, f"frame mismatch S{n}.{i}: want {nfr} got {got}"
        assert abs(dur - nfr/24) < 0.08, f"duration mismatch S{n}.{i}: {dur} vs {nfr/24}"
        total += got
        concat.append(out)
        segs_meta.append({"scene":n,"part":i,"kind":kind,"take":takef,"take_start":ts,"k":k,"out":[o0,o1],"frames":got,"md5":md5f(out)})
        json.dump(segs_meta, open(manifest_path,"w"), indent=1)
        notes.write(f"segment S{n}.{i} built: {nfr}f md5 {segs_meta[-1]['md5']}\n"); notes.flush()
print("TOTAL planned frames:", total, "target 2871", flush=True)
log.write(f"TOTAL planned frames: {total} target 2871\n"); log.close()
assert total == 2871, f"TOTAL {total} != 2871"
with open(os.path.join(SEG,"concat.txt"),"w") as f:
    for c in concat: f.write(f"file '{c}'\n")
joined = os.path.join(P,"work/swing/joined.mp4")
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",
                os.path.join(SEG,"concat.txt"),"-c","copy",joined], check=True)
notes.write(f"joined.mp4 built: total {total}f\n"); notes.close()
print("SEGMENTS DONE ->", joined, flush=True)
