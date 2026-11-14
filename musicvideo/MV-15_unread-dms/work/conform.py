import subprocess, os, json
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print("FAIL", r.stderr[-800:]); raise SystemExit(1)
    return r
spans = {"S01":(0.00,5.68),"S02":(5.68,12.08),"S03":(12.08,18.48),"S04":(18.48,25.04),"S05":(25.04,31.90),"S06":(31.90,38.54),"S07":(38.54,44.80),"S08":(44.80,50.44),"S09":(50.44,56.36),"S10":(56.36,63.12),"S11":(63.12,69.54),"S12":(69.54,76.34),"S13":(76.34,83.14),"S14":(83.14,89.46),"S15":(89.46,96.76),"S16":(96.76,102.66),"S17":(102.66,110.66),"S18":(110.66,123.02),"S19":(123.02,131.80),"S20":(131.80,134.70),"S21":(134.70,143.34),"S22":(143.34,153.10),"S23":(153.10,162.50),"S24":(162.50,173.61)}
os.makedirs(f"{P}/work/conformed", exist_ok=True)
for s,(a,b) in spans.items():
    want = round((b-a)*24)
    src = f"{P}/work/segments/{s}.mp4"; out = f"{P}/work/conformed/{s}.mp4"
    if s == "S18":  # minterpolate 16fps-effective source
        fc = f"[0:v]minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir,scale=1280:720,format=yuv420p,tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},setpts=N/(24*TB)[v]"
        run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",out])
    elif s == "S05":  # drifting-orb graphic layer over freeze span (honest motion)
        fc = (f"[0:v]scale=1280:720,format=yuv420p,tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},setpts=N/(24*TB)[base];"
              f"[1:v]format=rgba,scale=300:300[orb];"
              f"[base][orb]overlay=x='200+700*t/6.86':y='300+120*sin(t*1.3)':eval=frame,format=yuv420p,trim=end_frame={want},setpts=N/(24*TB)[v]")
        run(["ffmpeg","-v","error","-y","-i",src,"-loop","1","-t","6.86","-i",f"{P}/work/overlays/orb.png","-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",out])
    else:
        fc = f"[0:v]scale=1280:720,format=yuv420p,tpad=stop_mode=clone:stop_duration=3,trim=end_frame={want},setpts=N/(24*TB)[v]"
        run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",fc,"-map","[v]","-c:v","libx264","-crf","8","-preset","medium","-r","24",out])
    nf = int(run(["ffprobe","-v","error","-count_frames","-show_entries","stream=nb_read_frames","-of","csv=p=0",out]).stdout.strip())
    print(s, "frames", nf, "want", want, "OK" if nf==want else "** MISMATCH **", flush=True)
print("conform done")
