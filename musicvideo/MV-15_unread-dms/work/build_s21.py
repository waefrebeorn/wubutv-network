import subprocess, os
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print("FAIL", r.stderr[-800:]); raise SystemExit(1)
    return r
# S21 = L28 from t1 (phrases: 0-3.00 -> 3.02s ; 3.00-4.88 -> 2.14s) + L29 fragment from t2 (0-3.48 -> 3.48s, factor 1.000)
fc = ("[0:v]trim=start=0:end=3.00,setpts=(PTS-STARTPTS)*1.00667,fps=24,scale=1280:720,format=yuv420p[v0];"
      "[0:v]trim=start=3.00:end=4.88,setpts=(PTS-STARTPTS)*1.13830,fps=24,scale=1280:720,format=yuv420p[v1];"
      "[1:v]trim=start=0:end=3.48,setpts=(PTS-STARTPTS)*1.00000,fps=24,scale=1280:720,format=yuv420p[v2];"
      "[v0][v1][v2]concat=n=3:v=1:a=0,trim=end_frame=207,setpts=N/(24*TB)[vout]")
run(["ffmpeg","-v","error","-y","-i",f"{P}/takes/mv15_s21_t1.mp4","-i",f"{P}/takes/mv15_s21_t2.mp4","-filter_complex",fc,"-map","[vout]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/segments/S21.mp4"])
nf = run(["ffprobe","-v","error","-count_frames","-show_entries","stream=nb_read_frames","-of","csv=p=0",f"{P}/work/segments/S21.mp4"]).stdout.strip()
print("S21 frames", nf, "want 207")
