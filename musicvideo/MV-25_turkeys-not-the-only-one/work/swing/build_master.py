import json, os, subprocess, sys
P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(P, "work/segments"); os.makedirs(SEG, exist_ok=True)
FPS = 24
# scene plan: (scene, take, [(kind, take_start, k, out_start, out_end)])
# kind W = warped main (setpts k), N = natural span. Times in seconds.
PLAN = [
 (1,"t1",[("N",6.14,1.0,0.00,2.78),("W",0.00,0.911,2.78,8.10)]),
 (2,"t1",[("N",0.50,1.0,8.10,15.96)]),
 (3,"t1",[("W",0.00,0.794,15.96,21.90)]),
 (4,"t1",[("W",0.00,0.767,21.90,27.90)]),
 (5,"t1",[("N",0.66,1.0,27.90,31.58)]),
 (6,"t1",[("W",0.00,0.926,31.58,39.56)]),
 (7,"t1",[("W",0.00,0.913,39.56,48.12)]),
 (8,"t1",[("N",0.80,1.0,48.12,55.98)]),
 (9,"t1",[("W",0.00,0.925,55.98,63.86)]),
 (10,"t2",[("N",0.48,1.0,63.86,72.90)]),
 (11,"t1",[("W",1.04,0.817,72.90,79.24)]),
 (12,"t1",[("W",0.00,1.011,79.24,88.74)]),
 (13,"t1",[("W",0.00,0.967,88.74,96.92)]),
 (14,"t1",[("W",0.00,0.924,96.92,105.66)]),
 (15,"t1",[("N",1.00,1.0,105.66,113.02)]),
 (16,"t2",[("W",0.00,0.895,113.02,121.40)]),
 (17,"t1",[("N",0.60,1.0,121.40,130.14)]),
 (18,"t2",[("N",0.00,1.0,130.14,131.54),("N",5.00,1.0,131.54,133.60),("N",3.00,1.0,133.60,135.62),("N",8.00,1.0,135.62,137.54)]),
 (19,"t1",[("W",0.00,0.849,137.54,143.38)]),
 (20,"t2",[("W",0.00,1.045,143.38,151.28)]),
 (21,"t2",[("N",0.90,1.0,151.28,159.02)]),
 (22,"t2",[("W",0.00,1.286,159.58,168.56)]),
 (23,"t1",[("W",0.00,1.044,168.56,179.00)]),
 (24,"t1",[("N",4.54,1.0,179.00,181.62),("W",0.00,1.009,181.62,187.68)]),
 (25,"t1",[("W",0.00,0.850,187.68,196.00)]),
]
# fix S14 window: plan table window is 97.62-105.66
PLAN[13] = (14,"t1",[("W",0.00,0.924,97.62,105.66)])
def frames(t0, t1): return round(t1*FPS) - round(t0*FPS)
jobs = []
for sc, tk, parts in PLAN:
    for i,(kind, ts, k, o0, o1) in enumerate(parts):
        n = frames(o0, o1)
        take = os.path.join(P, f"takes/mv25_s{sc:02d}_{tk}.mp4")
        out = os.path.join(SEG, f"seg_{sc:02d}_{i}.mp4")
        if kind == "W":
            vf = f"setpts={k}*(PTS-STARTPTS),fps=24,scale=1280:720:flags=lanczos,format=yuv420p,tpad=stop_mode=clone:stop_duration=3"
        else:
            vf = "setpts=(PTS-STARTPTS),fps=24,scale=1280:720:flags=lanczos,format=yuv420p,tpad=stop_mode=clone:stop_duration=3"
        cmd = ["ffmpeg","-y","-loglevel","error","-ss",f"{ts:.2f}","-i",take,"-vf",vf,
               "-frames:v",str(n),"-an","-c:v","libx264","-preset","medium","-crf","14",out]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print("FAIL", sc, i, r.stderr[-400:]); sys.exit(1)
        got = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-count_frames",
            "-show_entries","stream=nb_read_frames","-of","csv=p=0",out], capture_output=True, text=True).stdout.strip()
        jobs.append((sc, i, out, n, int(got)))
        print(f"S{sc:02d}.{i} {kind} k={k} want {n}f got {got}", flush=True)
tot = sum(j[3] for j in jobs); print("TOTAL planned frames:", tot, "target 4704")
with open(os.path.join(SEG, "concat.txt"), "w") as f:
    for _,_,out,_,_ in jobs: f.write(f"file '{out}'\n")
json.dump([{"scene":a,"part":b,"file":c,"frames":d,"got":e} for a,b,c,d,e in jobs],
          open(os.path.join(P,"work/swing/segments.json"),"w"), indent=1)
print("SEGMENTS DONE")
