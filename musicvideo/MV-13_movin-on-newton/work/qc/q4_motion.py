import subprocess, numpy as np, json
def analyze(path, w=160, h=90):
    cmd = ["ffmpeg","-v","error","-i",path,"-vf",f"scale={w}:{h},format=gray","-f","rawvideo","-pix_fmt","gray","-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw)//(w*h)
    fr = np.frombuffer(raw, dtype=np.uint8).reshape(n, h, w).astype(np.float32)/255.0
    d = np.abs(np.diff(fr, axis=0)).mean(axis=(1,2))  # per-pair mean abs diff, 0..1
    dup = d < 0.0005
    # longest dup run in frames -> seconds at 24fps
    best = cur = 0
    for x in dup:
        cur = cur+1 if x else 0
        best = max(best, cur)
    return {"frames": n, "mean_diff": round(float(d.mean()),4), "min_diff": round(float(d.min()),4),
            "m6": round(float(dup.mean()),4), "longest_dup_run_s": round(best/24.0,2),
            "near_still_ge12f": int((np.convolve(dup.astype(int), np.ones(12,dtype=int), mode='valid')>=12).sum())}
for name, path in [("q4_s04_t2","takes/media-generation-mv13-q4-s04-t2-0-c132962b-6fbc-46d0-9767-4ae0f4eebd37.mp4"),
                   ("q4_s25_t2","takes/media-generation-mv13-q4-s25-t2-0-5296b052-70dc-44ca-96b2-ac74e09dfe64.mp4")]:
    r = analyze(path)
    json.dump(r, open(f"work/qc/{name}/motion.json","w"), indent=1)
    print(name, json.dumps(r))
