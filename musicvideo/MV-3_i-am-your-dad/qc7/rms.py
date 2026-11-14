import sys, subprocess
import numpy as np
# Usage: rms.py <mp4> — RMS per 0.25s window
path = sys.argv[1]
raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar","16000","-f","f32le","-"],
                     capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.float32)
sr = 16000; w = sr//4
for i in range(0, len(a)//w):
    seg = a[i*w:(i+1)*w]
    print(f"{i*0.25:5.2f}-{(i+1)*0.25:5.2f} {np.sqrt((seg**2).mean()):.4f}")
