import subprocess, json, os, sys
import numpy as np
from PIL import Image

SRC = sys.argv[1]
B = sys.argv[2]
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-18/qc0330"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

print("="*20, B, SRC.split("/")[-1][:60], "="*20)
r = run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate,duration,nb_frames","-show_entries","format=duration","-of","default=noprint_wrappers=1",SRC])
print(r.stdout.strip().replace("\n"," "))
r = run(["ffmpeg","-v","error","-i",SRC,"-f","null","-"])
print("decode:", r.stderr.strip() or "CLEAN")
r = run(["ffmpeg","-v","info","-i",SRC,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
txt = r.stderr
try:
    j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
    print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP")
except Exception as e:
    print("loudnorm fail:", str(e)[:150])
print("0.5s bins:")
bins = []
for i in range(20):
    s0, s1 = i*0.5, (i+1)*0.5
    r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",SRC,"-af","volumedetect","-f","null","-"])
    mx = "?"
    for line in r.stderr.splitlines():
        if "max_volume" in line:
            mx = line.split("max_volume:")[1].split("dB")[0].strip()
    bins.append(mx)
    print(f"  {s0:4.1f}s : {mx}")
tiles = []
for t, lab in [(0.5,"t05"),(2.0,"t20"),(4.0,"t40"),(6.0,"t60"),(8.0,"t80"),(9.5,"t95")]:
    p = os.path.join(OUT, f"{B}_{lab}.png")
    run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",SRC,"-frames:v","1",p])
    tiles.append(p)
sheet = os.path.join(OUT, f"{B}_contact.png")
run(["ffmpeg","-v","error","-y","-i",tiles[0],"-i",tiles[1],"-i",tiles[2],"-i",tiles[3],"-i",tiles[4],"-i",tiles[5],
     "-filter_complex","[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",sheet])
print("contact:", sheet)
a = np.asarray(Image.open(tiles[0])).astype(float); c = np.asarray(Image.open(tiles[5])).astype(float)
print(f"camera diff full-frame(0.5v9.5): {np.abs(a-c).mean():.2f}")
for lab, fp in [("0.5s",tiles[0]),("8s",tiles[4]),("9.5s",tiles[5])]:
    img = np.asarray(Image.open(fp)).astype(int)
    sub = img[200:520, 420:860]
    gold = (sub[:,:,0]>150)&(sub[:,:,1]>120)&(sub[:,:,2]<110)
    n = int(gold.sum())
    print(f"  gold torso-band {lab}: n={n}")
bugp = os.path.join(OUT, f"{B}_bug_br.png")
Image.open(tiles[5]).crop((950,590,1280,720)).resize((660,260)).save(bugp)
print("bug crop:", bugp)
