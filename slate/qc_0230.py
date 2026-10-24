import subprocess, json, os, sys
import numpy as np

TAKES = {
    "B-1041": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1041v1_raw.mp4",
    "B-1042": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1042v1_raw.mp4",
    "B-1043": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/b1043v1_raw.mp4",
}
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/qc0230"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

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
        print("loudnorm parse fail:", str(e)[:200])
    # 0.5s-bin profiler, windows [i*0.5,(i+1)*0.5) exactly, bin start times printed
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
    # frames: 6 tiles + 0.5/8.0/9.5 full frames
    tiles = []
    for t, lab in [(0.5,"t05"),(2.0,"t20"),(4.0,"t40"),(6.0,"t60"),(8.0,"t80"),(9.5,"t95")]:
        p = os.path.join(OUT, f"{b}_{lab}.png")
        run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",p])
        tiles.append(p)
    sheet = os.path.join(OUT, f"{b}_contact.png")
    r = run(["ffmpeg","-v","error","-y",
             "-i",tiles[0],"-i",tiles[1],"-i",tiles[2],"-i",tiles[3],"-i",tiles[4],"-i",tiles[5],
             "-filter_complex","[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",
             sheet])
    print("contact sheet:", sheet, "stderr:", r.stderr.strip()[:200] or "ok")
    import PIL.Image as I
    f05 = tiles[0]; f95 = tiles[5]; f80 = tiles[4]
    a = np.asarray(I.open(f05)).astype(float); c = np.asarray(I.open(f95)).astype(float)
    band = np.abs(a[:120]-c[:120]).mean()
    full = np.abs(a-c).mean()
    print(f"camera diff top-band(0.5v9.5): {band:.2f}  full-frame: {full:.2f}")
    # wordmark: gold-pixel scan in the TIGHT torso band (y 200-520, x 420-860)
    for lab, fp in [("0.5s",f05),("8s",f80),("9.5s",f95)]:
        img = np.asarray(I.open(fp)).astype(int)
        sub = img[200:520, 420:860]
        gold = (sub[:,:,0]>150)&(sub[:,:,1]>120)&(sub[:,:,2]<110)
        n = int(gold.sum())
        if n > 50:
            ys, xs = np.where(gold)
            gx0, gy0 = 420+xs.min(), 200+ys.min()
            gx1, gy1 = 420+xs.max(), 200+ys.max()
            print(f"  gold torso-band {lab}: n={n} bbox x[{gx0},{gx1}] y[{gy0},{gy1}]")
            x0,x1 = max(0,gx0-24), min(1280,gx1+24)
            y0,y1 = max(0,gy0-24), min(720,gy1+24)
            cr = I.open(fp).crop((x0,y0,x1,y1)); cr = cr.resize((cr.width*2,cr.height*2))
            crp = os.path.join(OUT, f"{b}_wordmark_{lab.replace('.','')}.png")
            cr.save(crp)
            print(f"    crop-zoom: {crp}")
        else:
            print(f"  gold torso-band {lab}: n={n} (no region / wordmark n/a)")
    # bug region crop (bottom-right) from the 9.5s frame for eyeball check
    bugp = os.path.join(OUT, f"{b}_bug_br.png")
    I.open(f95).crop((950,590,1280,720)).resize((660,260)).save(bugp)
    print("  bug crop:", bugp)
    print()
