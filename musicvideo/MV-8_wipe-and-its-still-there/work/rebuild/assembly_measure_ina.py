#!/usr/bin/env python3
"""Mean abs frame diff per 0.5s for IN-A take, 5.5-10s (lead-cover check)."""
import subprocess, numpy as np
P="/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there/takes/IN-A_v2.mp4"
W,H=1248,704
p=subprocess.run(["ffmpeg","-v","error","-ss","5.5","-i",P,"-t","4.5","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True)
a=np.frombuffer(p.stdout,dtype=np.uint8)
n=len(a)//(W*H)
a=a[:n*W*H].reshape(n,H,W).astype(np.int16)
print("frames decoded:",n)
for i in range(0,n-24,12):
    d=np.abs(a[i+12]-a[i]).mean()
    print(f"take {5.5+i/24:.2f}-{(5.5+(i+12)/24):.2f}s mean_abs_diff={d:.1f}")
# also fine: consecutive-frame diff 6.5-8.0
for i in range(int((6.5-5.5)*24),int((8.0-5.5)*24)):
    d=np.abs(a[i+1]-a[i]).mean()
    if i%6==0: print(f"take {5.5+i/24:.3f}s consec_diff={d:.1f}")
