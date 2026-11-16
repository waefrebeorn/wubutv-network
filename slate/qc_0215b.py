import subprocess, os, re
import numpy as np
from PIL import Image

OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/qc0215"
B1038 = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1038-bailed-dinghy-v1-0-aad8265f-f988-4fc5-ba95-a47b98d4d8f6.mp4"
B1039 = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1039-drawn-pail-v1-0-6efeaf75-a512-4724-b0dc-2dff2163fec8.mp4"

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def speech_band_max(src, s0, s1):
    # max dBFS in the 300-3400 Hz speech band
    r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",src,
             "-af","highpass=f=300,lowpass=f=3400,volumedetect","-f","null","-"])
    for line in r.stderr.splitlines():
        if "max_volume" in line:
            return line.split("max_volume:")[1].split("dB")[0].strip()
    return "n/a"

print("B-1038 speech-band (300-3400Hz) max dBFS:")
for s0,s1,lab in [(5.75,6.5,"5.75-6.5s (6s open mouth)"),(7.75,8.5,"7.75-8.5s (8s head-down)"),(8.5,9.25,"8.5-9.25s (tail)")]:
    print(f"  {lab}: {speech_band_max(B1038,s0,s1)}")
print("B-1039 speech-band (300-3400Hz) max dBFS (NO-LINE take):")
for s0,s1,lab in [(7.25,8.0,"7.25-8.0s"),(8.0,8.5,"8.0-8.5s"),(4.0,5.0,"4.0-5.0s control (cranking)")]:
    print(f"  {lab}: {speech_band_max(B1039,s0,s1)}")

# mouth-region crops: B-1038 at 6.0s (face-to-camera), B-1039 at 7.5s/8.0s
def crop_mouth(src, t, box, out):
    fp = out
    run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",fp])
    im = Image.open(fp)
    cr = im.crop(box); cr = cr.resize((cr.width*3, cr.height*3))
    cr.save(out.replace(".png","_mouth3x.png"))
    print("mouth crop:", out.replace(".png","_mouth3x.png"))

# B-1038 6s: face centered ~x 640-900, y 350-520 in full frame (from contact sheet row2-right)
crop_mouth(B1038, 6.0, (620,330,920,540), os.path.join(OUT,"B-1038_t60_full.png"))
# B-1039 8s: face right side ~x 690-900, y 180-360 (from contact sheet row3-left)
crop_mouth(B1039, 7.5, (660,160,940,380), os.path.join(OUT,"B-1039_t75_full.png"))
crop_mouth(B1039, 8.0, (660,160,940,380), os.path.join(OUT,"B-1039_t80_full.png"))
