import subprocess, sys
import numpy as np
from PIL import Image, ImageDraw
# usage: diag_strip.py <video> <f_start> <f_end> <out.jpg> [label]
video, f0, f1, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
label = sys.argv[5] if len(sys.argv) > 5 else ""
W, H = 1280, 720
# native res of takes is 1248x704; detect via probe
import json
pr = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","json",video],capture_output=True,text=True)
st = json.loads(pr.stdout)["streams"][0]; W, H = st["width"], st["height"]
proc = subprocess.Popen(["ffmpeg","-v","error","-i",video,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
frames = {}
fi = -1
while fi < f1:
    buf = proc.stdout.read(W*H*3)
    if len(buf) < W*H*3: break
    fi += 1
    if fi >= f0: frames[fi] = np.frombuffer(buf,np.uint8).reshape(H,W,3).copy()
proc.kill()
cx0, cy0, cw, ch = int(0.30*W), int(0.26*H), int(0.32*W), int(0.34*H)
PW, PH = 250, 215
n = len(frames); cols = min(n, 8); rows = (n + cols - 1)//cols
grid = Image.new("RGB",(cols*PW, rows*PH),(24,24,24)); dr = ImageDraw.Draw(grid)
for i,(f,fr) in enumerate(sorted(frames.items())):
    crop = Image.fromarray(fr[cy0:cy0+ch, cx0:cx0+cw]).resize((PW, PH-20))
    x, y = (i%cols)*PW, (i//cols)*PH
    grid.paste(crop,(x,y+20)); dr.text((x+6,y+4), f"f{f} {label}", fill=(255,255,90))
grid.save(out, quality=88); print("wrote", out, "frames", f0, "-", f1)
