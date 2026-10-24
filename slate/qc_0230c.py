#!/usr/bin/env python3
"""QC v2 takes for the 2026-10-19 02:30 EDT bumper-factory run."""
import subprocess, json, os
import numpy as np

T = "/home/hatch/workspace/wubutv-network/takes/2026-10-19"
TAKES = {
    "B-1261v2": f"{T}/media-generation-b1261-the-customs-house-v2-0-b494c7fc-ca4c-4e7c-8e13-9b079d3fd631.mp4",
    "B-1262v2": f"{T}/media-generation-b1262-the-viaduct-v2-0-cfdc673e-2151-477b-b8b6-c649594b1802.mp4",
}
OUT = f"{T}/qc0230v2"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def frame(src, t, out):
    run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",out])

for b, src in TAKES.items():
    print("="*24, b, "="*24)
    r = run(["ffprobe","-v","error","-select_streams","v:0","-show_entries",
             "stream=width,height,nb_frames,duration","-of","json",src])
    try:
        st = json.loads(r.stdout)["streams"][0]
        print("meta:", st.get("width"), "x", st.get("height"), "frames:", st.get("nb_frames"), "dur:", st.get("duration"))
    except Exception as e:
        print("ffprobe fail:", str(e)[:200])
    r = run(["ffmpeg","-v","error","-i",src,"-f","null","-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    r = run(["ffmpeg","-v","info","-i",src,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
    txt = r.stderr
    try:
        j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
        print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP")
    except Exception as e:
        print("loudnorm fail:", str(e)[:200])
    # 0.5s bins
    print("0.5s bins:")
    for i in range(20):
        s0, s1 = i*0.5, (i+1)*0.5
        r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",src,"-af","volumedetect","-f","null","-"])
        mx = None
        for line in r.stderr.splitlines():
            if "max_volume" in line:
                mx = line.split("max_volume:")[1].split("dB")[0].strip()
        print(f"  {s0:4.1f}s : {mx}")
    # contact sheet
    tiles = []
    for t, lab in [(0.5,"t05"),(2.0,"t20"),(4.0,"t40"),(6.0,"t60"),(8.0,"t80"),(9.5,"t95")]:
        p = os.path.join(OUT, f"{b}_{lab}.png")
        frame(src, t, p); tiles.append(p)
    sheet = os.path.join(OUT, f"{b}_contact.png")
    r = run(["ffmpeg","-v","error","-y","-i",tiles[0],"-i",tiles[1],"-i",tiles[2],"-i",tiles[3],
             "-i",tiles[4],"-i",tiles[5],
             "-filter_complex","[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",
             sheet])
    print("contact:", sheet, r.stderr.strip()[:120] or "ok")
    # wordmark gold scan 0.5/9.5
    from PIL import Image as I
    for lab, tt in [("05",0.5),("95",9.5)]:
        fp = os.path.join(OUT, f"{b}_f{lab}.png"); frame(src, tt, fp)
        img = np.asarray(I.open(fp)).astype(int)
        gold = (img[:,:,0]>150)&(img[:,:,1]>120)&(img[:,:,2]<110)
        n = gold.sum(); ys, xs = np.where(gold)
        if n > 50:
            print(f"  gold {lab}: n={n} x[{xs.min()},{xs.max()}] y[{ys.min()},{ys.max()}]")
            x0,x1 = max(0,xs.min()-20), min(1280,xs.max()+20)
            y0,y1 = max(0,ys.min()-20), min(720,ys.max()+20)
            cr = I.open(fp).crop((x0,y0,x1,y1)); cr = cr.resize((cr.width*2,cr.height*2))
            crp = os.path.join(OUT, f"{b}_wordmark_{lab}.png"); cr.save(crp)
            print(f"    crop: {crp}")
        else:
            print(f"  gold {lab}: n={n} (none)")
    # mouth strips 7.0/7.25/7.5/8.0/8.75/9.0
    strips = []
    for t in [7.0,7.25,7.5,8.0,8.75,9.0]:
        p = os.path.join(OUT, f"{b}_mouth_{t:.2f}.png")
        frame(src, t, p); strips.append(p)
    strip = os.path.join(OUT, f"{b}_mouthstrip.png")
    r = run(["ffmpeg","-v","error","-y"]+sum([["-i",p] for p in strips],[])+
            ["-filter_complex","[0][1][2]hstack=inputs=3[r1];[3][4][5]hstack=inputs=3[r2];[r1][r2]vstack,scale=1440:480",strip])
    print("mouthstrip:", strip, r.stderr.strip()[:120] or "ok")
    # bug crop
    bug = os.path.join(OUT, f"{b}_bug.png")
    run(["ffmpeg","-v","error","-y","-ss","5.0","-i",src,"-frames:v","1","-vf","crop=500:220:780:500",bug])
    print("bug:", bug)
    print()
print("DONE")
