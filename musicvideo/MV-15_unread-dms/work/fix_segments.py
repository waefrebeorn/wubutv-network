import subprocess, os, json, hashlib
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print("FAIL", " ".join(cmd)[:200], r.stderr[-800:]); raise SystemExit(1)
    return r
def frames(p):
    return int(run(["ffprobe","-v","error","-count_frames","-show_entries","stream=nb_read_frames","-of","csv=p=0",p]).stdout.strip())
def render_warp(scene, take, a, b, span, extra=""):
    k = span/(b-a)
    fc = f"[0:v]trim=start={a}:end={b},setpts=(PTS-STARTPTS)*{k:.5f},fps=24{extra},scale=1280:720,format=yuv420p,trim=end_frame={round(span*24)},setpts=N/(24*TB)[vout]"
    out = f"{P}/work/segments/{scene}.mp4"
    run(["ffmpeg","-v","error","-y","-i",f"{P}/takes/{take}.mp4","-filter_complex",fc,"-map","[vout]","-c:v","libx264","-crf","8","-preset","medium","-r","24",out])
    nf = frames(out); want = round(span*24)
    print(scene, f"k={k:.3f} speed={1/k:.3f}x", "frames", nf, "want", want, "OK" if nf==want else "** MISMATCH **", flush=True)
# motion re-renders: same windows as build_segments.py, warped to plan span
render_warp("S02","mv15_s02_t1",0.25,5.93,6.40)
render_warp("S03","mv15_s03_t1",0.45,7.25,6.40)
render_warp("S06","mv15_s06_t1",0.30,7.36,6.64)
render_warp("S09","mv15_s09_t1",0.30,5.98,5.92)
render_warp("S10","mv15_s10_t1",0.50,6.92,6.76)
render_warp("S13","mv15_s13_t1",0.95,7.37,6.80)
render_warp("S14","mv15_s14_t1",0.20,7.00,6.32)
render_warp("S15","mv15_s15_t2",0.30,8.66,7.30)
render_warp("S17","mv15_s17_t1",0.95,7.63,8.00)
render_warp("S19","mv15_s19_t1",0.00,9.98,8.78)
render_warp("S22","mv15_s22_t1",0.45,6.87,9.76)
render_warp("S24","mv15_s24_t1",0.30,9.41,11.11)
# S20 with minterpolate (16fps-effective source)
render_warp("S20","mv15_s20_t1",0.30,4.24,2.90, extra=",minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir")
print("motion fixes done")
