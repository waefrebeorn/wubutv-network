import subprocess, os, shutil
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
BK = f"{P}/work/conformed_orig"
os.makedirs(BK, exist_ok=True)
# ZERO-STILL HONESTY FIX: scenes whose conformed output carried near-dup runs >=2 in the
# pregrain measurement get a real camera move (slow 256px pan over the span) at conform.
# id, want frames, span s, x expression
PAN = [
 ("S09", 142, 5.92,  "256*t/5.92"),
 ("S13", 163, 6.80,  "256-256*t/6.80"),
 ("S17", 192, 8.00,  "256*t/8.00"),
 ("S19", 211, 8.78,  "256-256*t/8.78"),
 ("S20", 70,  2.90,  "256*t/2.90"),
 ("S24", 267, 11.11, "256*t/11.11"),
]
def frames(path):
    r = subprocess.run(["ffprobe","-v","error","-count_frames","-select_streams","v:0","-show_entries","stream=nb_read_frames","-of","csv=p=0",path], capture_output=True, text=True)
    return int(r.stdout.strip())
def backup(sid):
    src = f"{P}/work/conformed/{sid}.mp4"; dst = f"{BK}/{sid}.mp4"
    if not os.path.exists(dst): shutil.copy2(src, dst)
for sid, want, span, x in PAN:
    backup(sid)
    fc = (f"[0:v]fps=24,scale=1536:864,crop=1280:720:x='{x}':y=72,format=yuv420p,"
          f"tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},setpts=N/(24*TB)[v]")
    cmd = ["ffmpeg","-v","error","-y","-i",f"{P}/work/segments/{sid}.mp4","-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/conformed/{sid}.mp4"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(sid, "FAIL", r.stderr[-300:]); continue
    got = frames(f"{P}/work/conformed/{sid}.mp4")
    print(sid, "pan-conform frames", got, "want", want, "OK" if got==want else "MISMATCH", flush=True)
# S05: parent's patched orb branch, with the pan inserted on the base BEFORE the overlay.
backup("S05")
fc = ("[0:v]fps=24,scale=1536:864,crop=1280:720:x='256*t/6.86':y=72,format=yuv420p[base];"
      "[1:v]scale=300:300,format=rgba,colorchannelmixer=aa=0.85[orb];"
      "[base][orb]overlay=x='200+700*(t-0.3)/6.26':y='300+40*sin(t*1.3)':enable='between(t,0.3,6.56)',"
      "tpad=stop_mode=clone:stop_duration=3,trim=end_frame=165,setpts=N/(24*TB)[v]")
cmd = ["ffmpeg","-v","error","-y","-i",f"{P}/work/segments/S05.mp4","-loop","1","-t","6.86","-i",f"{P}/work/overlays/orb.png","-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/conformed/S05.mp4"]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("S05 FAIL", r.stderr[-300:])
else:
    got = frames(f"{P}/work/conformed/S05.mp4")
    print("S05 pan+orb conform frames", got, "want 165", "OK" if got==165 else "MISMATCH", flush=True)
print("conform_fix done")
