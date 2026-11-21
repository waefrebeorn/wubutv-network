import subprocess, glob, sys

def take(u):
    return glob.glob(f"takes/media-generation-{u}-take1-*.mp4")[0]

def frame_gray(path, t, w=320, h=180):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", path,
                        "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray",
                        "-vf", f"scale={w}:{h}", "-"],
                       capture_output=True)
    return r.stdout

def mean(d):
    return sum(d) / len(d) if d else float("nan")

# U6 late frames for cliff inspection
f6 = take("u6")
for t in (8.5, 9.0, 9.25):
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", f6,
                    "-frames:v", "1", f"work/qc/u6_f{t}.png", "-y"], check=True)
print("u6 late frames extracted")

# U5 black start pinpoint
f5 = take("u5")
for t in (9.0, 9.05, 9.1, 9.15, 9.2):
    print(f"u5 t={t} mean={mean(frame_gray(f5, t)):.1f}")

# Motion at every unit start + end (MAE between frame@0.0 and frame@0.5; frame@9.0 and frame@9.5)
for u in ("u1", "u2", "u3", "u4", "u5", "u6"):
    f = take(u)
    a, b = frame_gray(f, 0.0), frame_gray(f, 0.5)
    mae_start = sum(abs(x - y) for x, y in zip(a, b)) / len(a)
    c, d = frame_gray(f, 9.0), frame_gray(f, 9.5)
    mae_end = sum(abs(x - y) for x, y in zip(c, d)) / len(c) if mean(c) > 1 else float("nan")
    print(f"{u} start-MAE={mae_start:.2f} end-MAE(9.0 vs 9.5)={mae_end}")
