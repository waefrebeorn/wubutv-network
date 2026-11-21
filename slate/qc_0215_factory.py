import subprocess, json, os, re
import numpy as np
from PIL import Image

TAKES = {
    "b1231": "/home/hatch/workspace/wubutv-network/takes/2026-10-18/media-generation-b1231-the-threaded-reel-v1-0-405bf42d-6316-491d-96c6-8f617cfb471e.mp4",
    "b1233": "/home/hatch/workspace/wubutv-network/takes/2026-10-18/media-generation-b1233-the-flash-code-v1-0-4e45fa62-b099-405d-8e66-664de7af6501.mp4",
    "b1234": "/home/hatch/workspace/wubutv-network/takes/2026-10-18/media-generation-b1234-the-seed-drill-v1-0-4a8e121a-0d53-4440-998d-032dccb9031d.mp4",
}
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-18/qc_0215"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def pcm(src):
    r = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le","-"],
                       capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32)

def specflat(x, sr=16000):
    w = x * np.hanning(len(x))
    S = np.abs(np.fft.rfft(w))**2 + 1e-12
    S = S[1:]  # drop DC
    gm = np.exp(np.mean(np.log(S)))
    am = np.mean(S)
    return float(gm/am)

for b, src in TAKES.items():
    print("="*20, b, "="*20)
    r = run(["ffmpeg","-v","error","-i",src,"-f","null","-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    r = run(["ffmpeg","-v","info","-i",src,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
    txt = r.stderr
    try:
        j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
        print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP  LRA:", j["input_lra"])
    except Exception as e:
        print("loudnorm parse fail", str(e)[:150])
    # fine voice window: 0.25s bins 7.0-9.75s, max dBFS + spectral flatness
    a = pcm(src)
    sr = 16000
    print("bin(s) : peak_dBFS flatness")
    for i in range(28, 40):
        s0 = i*0.25; s1 = (i+1)*0.25
        seg = a[int(s0*sr):int(s1*sr)]
        peak = 20*np.log10(max(np.abs(seg).max(), 1e-9))
        fl = specflat(seg)
        flag = ""
        if peak > -30 and fl < 0.35: flag = "  <-- VOICE-GRADE"
        print(f"  {s0:4.2f}-{s1:4.2f} : {peak:7.2f} {fl:.3f}{flag}")
    # 6-tile contact sheet
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
    print("contact:", sheet)
    # voice-window mouth frames
    for t in [7.0,7.25,7.5,7.75,8.0,8.25,8.5,8.75,9.0,9.5]:
        p = os.path.join(OUT, f"{b}_m{str(t).replace('.','')}.png")
        run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",p])
    # camera diff 0.5 vs 9.5
    f05 = os.path.join(OUT, f"{b}_f05.png"); f95 = os.path.join(OUT, f"{b}_f95.png")
    run(["ffmpeg","-v","error","-y","-ss","0.5","-i",src,"-frames:v","1",f05])
    run(["ffmpeg","-v","error","-y","-ss","9.5","-i",src,"-frames:v","1",f95])
    A = np.asarray(Image.open(f05)).astype(float); C = np.asarray(Image.open(f95)).astype(float)
    print(f"camera diff full-frame mean: {np.abs(A-C).mean():.2f}")
    # wordmark gold scan + crop-zoom
    for lab, fp in [("0.5s",f05),("9.5s",f95)]:
        img = np.asarray(Image.open(fp)).astype(int)
        gold = (img[:,:,0]>150)&(img[:,:,1]>120)&(img[:,:,2]<110)
        n = int(gold.sum())
        if n > 50:
            ys, xs = np.where(gold)
            print(f"  gold {lab}: n={n} bbox x[{xs.min()},{xs.max()}] y[{ys.min()},{ys.max()}]")
            x0,x1 = max(0,xs.min()-30), min(1280,xs.max()+30)
            y0,y1 = max(0,ys.min()-30), min(720,ys.max()+30)
            cr = Image.open(fp).crop((x0,y0,x1,y1)); cr = cr.resize((cr.width*3,cr.height*3))
            crp = os.path.join(OUT, f"{b}_wordmark_{lab.replace('.','')}.png")
            cr.save(crp); print(f"    crop-zoom: {crp}")
        else:
            print(f"  gold {lab}: n={n}")
    print()
