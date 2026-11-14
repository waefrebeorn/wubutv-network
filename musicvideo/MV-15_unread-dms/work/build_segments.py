import subprocess, os, json
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print("FAIL", r.stderr[-600:]); raise SystemExit(1)
    return r
def render(scene, take, parts):
    """parts: (take_a, take_b, song_dur) — setpts factor = song_dur/(take_b-take_a)"""
    fc_parts, labels = [], []
    for i,(ta,tb,sd) in enumerate(parts):
        k = sd/(tb-ta)
        fc_parts.append(f"[0:v]trim=start={ta}:end={tb},setpts=(PTS-STARTPTS)*{k:.5f},fps=24,format=yuv420p[v{i}]")
        labels.append(f"[v{i}]")
    fc = ";".join(fc_parts) + ";" + "".join(labels) + f"concat=n={len(parts)}:v=1:a=0[vout]"
    run(["ffmpeg","-v","error","-y","-i",f"{P}/takes/{take}.mp4","-filter_complex",fc,"-map","[vout]","-c:v","libx264","-crf","8","-preset","medium","-r","24",f"{P}/work/segments/{scene}.mp4"])
    total = sum(sd for _,_,sd in parts)
    nf = int(run(["ffprobe","-v","error","-count_frames","-show_entries","stream=nb_read_frames","-of","csv=p=0",f"{P}/work/segments/{scene}.mp4"]).stdout.strip())
    want = round(total*24)
    print(scene, "factors", [round(sd/(tb-ta),3) for ta,tb,sd in parts], "frames", nf, "want", want, "OK" if abs(nf-want)<=1 else "** MISMATCH **")
# LIPS — (take_a, take_b, song_dur)
render("S01","mv15_s01_t3", [(0,3.38,3.02),(3.38,5.60,2.66)])
render("S04","mv15_s04_t2", [(0,3.14,3.48),(3.14,5.64,3.08)])
render("S08","mv15_s08_t1", [(0,2.72,2.98),(2.72,3.62,0.96),(3.62,4.66,1.70)])
render("S11","mv15_s11_t2", [(0,3.46,3.46),(3.46,6.50,2.96)])
render("S16","mv15_s16_t2", [(0,4.12,3.26),(4.12,6.54,2.64)])
render("S18","mv15_s18_t1", [(5.94,9.90,4.92),(0,3.14,3.16),(3.14,5.94,4.28)])
render("S23","mv15_s23_t1", [(0,3.74,4.28),(3.74,5.52,3.36),(5.52,7.28,1.76)])
# MOTION trims (song_dur = b-a)
for scene, take, a, b in [
 ("S02","mv15_s02_t1",0.25,5.93),("S03","mv15_s03_t1",0.45,7.25),("S05","mv15_s05_t1",0.75,7.55),
 ("S06","mv15_s06_t1",0.30,7.36),("S07","mv15_s07_t2",0.65,6.91),("S09","mv15_s09_t1",0.30,5.98),
 ("S10","mv15_s10_t1",0.50,6.92),("S12","mv15_s12_t1",0.30,7.10),("S13","mv15_s13_t1",0.95,7.37),
 ("S14","mv15_s14_t1",0.20,7.00),("S15","mv15_s15_t2",0.30,8.66),("S17","mv15_s17_t1",0.95,7.63),
 ("S19","mv15_s19_t1",0.00,9.98),("S20","mv15_s20_t1",0.30,4.24),("S22","mv15_s22_t1",0.45,6.87),
 ("S24","mv15_s24_t1",0.30,9.41)]:
    render(scene, take, [(a,b,b-a)])
print("done (S21 after t2 ASR)")
