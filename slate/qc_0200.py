import subprocess, json, os, sys
import numpy as np

TAKES = {
    "B-1035": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1035_v1_take.mp4",
    "B-1036": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1036_v1_take.mp4",
    "B-1037": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1037_v1_take.mp4",
}
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/qc0200"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r

for b, src in TAKES.items():
    print("="*20, b, "="*20)
    # decode errors
    r = run(["ffmpeg","-v","error","-i",src,"-f","null","-"])
    print("decode stderr:", r.stderr.strip() or "CLEAN")
    # loudness
    r = run(["ffmpeg","-v","info","-i",src,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
    txt = r.stderr
    try:
        j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
        print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP  LRA:", j["input_lra"])
    except Exception as e:
        print("loudnorm parse fail:", str(e)[:200]); print(txt[-600:])
    # 0.5s-bin profiler with bin start times (windows [i*0.5,(i+1)*0.5) exactly)
    print("0.5s bins (start_s : max_dBFS):")
    for i in range(20):
        s0, s1 = i*0.5, (i+1)*0.5
        r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",src,
                 "-af","volumedetect","-f","null","-"])
        mx = None
        for line in r.stderr.splitlines():
            if "max_volume" in line:
                v = line.split("max_volume:")[1].split("dB")[0].strip()
                mx = v
        print(f"  {s0:4.1f}s : {mx}")
    # six-tile contact sheet (vstack=inputs=3 fix)
    tiles = []
    for t, lab in [(0.5,"t05"),(2.0,"t20"),(4.0,"t40"),(6.0,"t60"),(8.0,"t80"),(9.5,"t95")]:
        p = os.path.join(OUT, f"{b}_{lab}.png")
        r = run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",p])
        tiles.append(p)
    sheet = os.path.join(OUT, f"{b}_contact.png")
    r = run(["ffmpeg","-v","error","-y",
             "-i",tiles[0],"-i",tiles[1],"-i",tiles[2],"-i",tiles[3],"-i",tiles[4],"-i",tiles[5],
             "-filter_complex","[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",
             sheet])
    print("contact sheet:", sheet, "stderr:", r.stderr.strip()[:200] or "ok")
    # full frames at 0.5/9.5 for camera diff + wordmark gold scan
    f05 = os.path.join(OUT, f"{b}_f05.png"); f95 = os.path.join(OUT, f"{b}_f95.png")
    run(["ffmpeg","-v","error","-y","-ss","0.5","-i",src,"-frames:v","1",f05])
    run(["ffmpeg","-v","error","-y","-ss","9.5","-i",src,"-frames:v","1",f95])
    # camera: top-band (0..120px) mean abs diff
    import PIL.Image as I
    a = np.asarray(I.open(f05)).astype(float); c = np.asarray(I.open(f95)).astype(float)
    band = np.abs(a[:120]-c[:120]).mean()
    full = np.abs(a-c).mean()
    print(f"camera diff top-band: {band:.2f}  full-frame: {full:.2f}")
    # gold-pixel scan (wordmark) full frame
    for lab, fp in [("0.5s",f05),("9.5s",f95)]:
        img = np.asarray(I.open(fp)).astype(int)
        gold = (img[:,:,0]>150)&(img[:,:,1]>120)&(img[:,:,2]<110)
        n = gold.sum()
        ys, xs = np.where(gold)
        if n > 50:
            print(f"  gold pixels {lab}: n={n} bbox x[{xs.min()},{xs.max()}] y[{ys.min()},{ys.max()}]")
            # crop-zoom 2x around bbox
            x0,x1 = max(0,xs.min()-20), min(1280,xs.max()+20)
            y0,y1 = max(0,ys.min()-20), min(720,ys.max()+20)
            cr = I.open(fp).crop((x0,y0,x1,y1)); cr = cr.resize((cr.width*2,cr.height*2))
            crp = os.path.join(OUT, f"{b}_wordmark_{lab.replace('.','')}.png")
            cr.save(crp)
            print(f"    crop-zoom: {crp}")
        else:
            print(f"  gold pixels {lab}: n={n} (no wordmark region / n/a)")
    print()
