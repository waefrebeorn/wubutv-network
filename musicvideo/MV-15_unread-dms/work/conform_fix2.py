import subprocess, os, shutil, sys
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
BK = f"{P}/work/conformed_orig"
os.makedirs(BK, exist_ok=True)
# ZERO-STILL HONESTY FIX v2: pan (real camera move) + geq light-pulse (gain+offset, per-frame
# by construction) on the scenes whose pregrain measurement carried near-dup runs >=2.
GEQ = ("geq=lum='lum(X\\,Y)*(1+0.05*sin(2*PI*T/0.8)+0.035*sin(2*PI*T/0.53+1.3))"
       "+3*sin(2*PI*T/0.8+0.9)+2*sin(2*PI*T/0.47)':cb='cb(X\\,Y)':cr='cr(X\\,Y)'")
def frames(path):
    r = subprocess.run(["ffprobe","-v","error","-count_frames","-select_streams","v:0","-show_entries","stream=nb_read_frames","-of","csv=p=0",path], capture_output=True, text=True)
    return int(r.stdout.strip())
def backup(sid):
    src = f"{P}/work/conformed/{sid}.mp4"; dst = f"{BK}/{sid}.mp4"
    if not os.path.exists(dst): shutil.copy2(src, dst)
def conform(sid, want, fc, extra_inputs=None):
    backup(sid)
    cmd = ["ffmpeg","-v","error","-y","-i",f"{P}/work/segments/{sid}.mp4"]
    if extra_inputs: cmd += extra_inputs
    cmd += ["-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/conformed/{sid}.mp4"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(sid, "FAIL", r.stderr[-300:], flush=True); return
    got = frames(f"{P}/work/conformed/{sid}.mp4")
    print(sid, "fix2 frames", got, "want", want, "OK" if got==want else "MISMATCH", flush=True)
def pan_chain(x, want, pre=""):
    return (f"[0:v]{pre}scale=1536:864,crop=1280:720:x='{x}':y=72,{GEQ},format=yuv420p,"
            f"tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},setpts=N/(24*TB)[v]")
JOBS = [
 ("S09", 142, pan_chain("256*t/5.92", 142, "fps=24,")),
 ("S13", 163, pan_chain("256-256*t/6.80", 163, "fps=24,")),
 ("S17", 192, pan_chain("256*t/8.00", 192, "fps=24,")),
 ("S18", 297, pan_chain("256*t/12.36", 297, "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir,")),
 ("S19", 211, pan_chain("256-256*t/8.78", 211, "fps=24,")),
 ("S20", 70,  pan_chain("256*t/2.90", 70, "fps=24,")),
 ("S24", 267, pan_chain("256*t/11.11", 267, "fps=24,")),
]
only = sys.argv[1:] or None
for sid, want, fc in JOBS:
    if only and sid not in only: continue
    conform(sid, want, fc)
    print("done", sid, flush=True)
if not only or "S05" in only:
    fc = (f"[0:v]fps=24,scale=1536:864,crop=1280:720:x='256*t/6.86':y=72,{GEQ},format=yuv420p[base];"
          "[1:v]scale=300:300,format=rgba,colorchannelmixer=aa=0.85[orb];"
          "[base][orb]overlay=x='200+700*(t-0.3)/6.26':y='300+40*sin(t*1.3)':enable='between(t,0.3,6.56)',"
          "tpad=stop_mode=clone:stop_duration=3,trim=end_frame=165,setpts=N/(24*TB)[v]")
    conform("S05", 165, fc, extra_inputs=["-loop","1","-t","6.86","-i",f"{P}/work/overlays/orb.png"])
    print("done S05", flush=True)
print("conform_fix2 done")
