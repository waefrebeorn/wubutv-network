import subprocess, numpy as np, os
P="/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back"
def dec(path, out):
    subprocess.run(["ffmpeg","-y","-v","error","-i",path,"-map","0:a:0","-ar","48000","-ac","1","-f","f32le",out],check=True)
    return np.fromfile(out,dtype=np.float32)
a=dec(f"{P}/masters/mv34_jensens-back_16x9.mp4","/tmp/m34_master.f32")
b=dec(f"{P}/track.mp3","/tmp/m34_track.f32")
n=min(len(a),len(b)); a,b=a[:n],b[:n]
# best integer offset in +-4800 samples by correlation on a loud window
w=slice(48000*40,48000*50)
best=(0,-2)
for off in range(-2400,2401,24):
    aa=a[w.start+off:w.stop+off] if off>=0 else a[w.start:w.stop]
    bb=b[w.start:w.start+len(aa)] if off>=0 else b[w.start-off:w.start-off+len(aa)]
    m=min(len(aa),len(bb)); aa,bb=aa[:m],bb[:m]
    c=np.corrcoef(aa,bb)[0,1]
    if c>best[1]: best=(off,c)
off=best[0]
if off>=0: aa,bb=a[off:],b[:len(a)-off]
else: aa,bb=a[:len(a)+off],b[-off:]
d=aa-bb
print(f"samples compared={len(d)} best_offset_samples={off} ({off/48:.2f} ms) window_corr={best[1]:.6f}")
print(f"full corr={np.corrcoef(aa,bb)[0,1]:.6f} rms_diff={np.sqrt((d**2).mean()):.5f} max_abs_diff={np.abs(d).max():.4f} rms_track={np.sqrt((bb**2).mean()):.5f}")
