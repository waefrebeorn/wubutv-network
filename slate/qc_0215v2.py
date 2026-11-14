import subprocess, json, os
import numpy as np

TAKES = {
    "B-1039v2": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1039-drawn-pail-v2-0-bed8b7c0-6907-4b3a-b17f-afc0d67bcc0d.mp4",
    "B-1040v2": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1040-split-log-v2-0-5b4988ff-51bd-4d61-85d7-5c3966004e65.mp4",
}
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/qc0215v2"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

for b, src in TAKES.items():
    print("="*20, b, "="*20)
    r = run(["ffmpeg","-v","error","-i",src,"-f","null","-"])
    print("decode stderr:", r.stderr.strip() or "CLEAN")
    r = run(["ffmpeg","-v","info","-i",src,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
    txt = r.stderr
    try:
        j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
        print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP  LRA:", j["input_lra"])
    except Exception as e:
        print("loudnorm parse fail:", str(e)[:200])
    print("0.5s bins (start_s : max_dBFS):")
    for i in range(20):
        s0, s1 = i*0.5, (i+1)*0.5
        r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",src,
                 "-af","volumedetect","-f","null","-"])
        mx = None
        for line in r.stderr.splitlines():
            if "max_volume" in line:
                mx = line.split("max_volume:")[1].split("dB")[0].strip()
        print(f"  {s0:4.1f}s : {mx}")
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
    a = np.asarray(I.open(tiles[0])).astype(float); c = np.asarray(I.open(tiles[5])).astype(float)
    band = np.abs(a[:120]-c[:120]).mean()
    full = np.abs(a-c).mean()
    print(f"camera diff top-band(0.5v9.5): {band:.2f}  full-frame: {full:.2f}")
    for lab, fp in [("0.5s",tiles[0]),("8s",tiles[4]),("9.5s",tiles[5])]:
        img = np.asarray(I.open(fp)).astype(int)
        sub = img[200:520, 420:860]
        gold = (sub[:,:,0]>150)&(sub[:,:,1]>120)&(sub[:,:,2]<110)
        n = int(gold.sum())
        if n > 50:
            ys, xs = np.where(gold)
            print(f"  gold torso-band {lab}: n={n} bbox x[{420+xs.min()},{420+xs.max()}] y[{200+ys.min()},{200+ys.max()}]")
        else:
            print(f"  gold torso-band {lab}: n={n} (no region / n/a)")
    bugp = os.path.join(OUT, f"{b}_bug_br.png")
    I.open(tiles[5]).crop((950,590,1280,720)).resize((660,260)).save(bugp)
    print("  bug crop:", bugp)
    print()
