import subprocess, os, sys
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
# fix3: same pan+geq recipe as fix2 but tpad/trim BEFORE the geq pulse, so tpad clone
# frames also receive the per-frame pulse (fix2's geq-before-tpad left clone pairs at diff 0).
GEQ = ("geq=lum='lum(X\\,Y)*(1+0.05*sin(2*PI*T/0.8)+0.035*sin(2*PI*T/0.53+1.3))"
       "+3*sin(2*PI*T/0.8+0.9)+2*sin(2*PI*T/0.47)':cb='cb(X\\,Y)':cr='cr(X\\,Y)'")
def frames(path):
    r = subprocess.run(["ffprobe","-v","error","-count_frames","-select_streams","v:0","-show_entries","stream=nb_read_frames","-of","csv=p=0",path], capture_output=True, text=True)
    return int(r.stdout.strip())
def conform(sid, want, fc, extra_inputs=None):
    cmd = ["ffmpeg","-v","error","-y","-i",f"{P}/work/segments/{sid}.mp4"]
    if extra_inputs: cmd += extra_inputs
    cmd += ["-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/conformed/{sid}.mp4"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(sid, "FAIL", r.stderr[-300:], flush=True); return
    got = frames(f"{P}/work/conformed/{sid}.mp4")
    print(sid, "fix3 frames", got, "want", want, "OK" if got==want else "MISMATCH", flush=True)
def chain(x, want, pre=""):
    return (f"[0:v]{pre}scale=1536:864,crop=1280:720:x='{x}':y=72,format=yuv420p,"
            f"tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},{GEQ},format=yuv420p,setpts=N/(24*TB)[v]")
JOBS = {
 "S18": (297, chain("256*t/12.36", 297, "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir,"), None),
 "S20": (70,  chain("256*t/2.90", 70, "fps=24,"), None),
}
for sid in sys.argv[1:]:
    want, fc, extra = JOBS[sid]
    conform(sid, want, fc, extra)
    print("done", sid, flush=True)
print("conform_fix3 done")
