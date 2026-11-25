import subprocess, glob, os

os.makedirs("work/segments", exist_ok=True)

TAKES = {
    "U1": (glob.glob("takes/media-generation-u1-take1-*.mp4")[0], None),
    "U2": (glob.glob("takes/media-generation-u2-take1-*.mp4")[0], None),
    "U3": (glob.glob("takes/media-generation-u3-take1-*.mp4")[0], None),
    "U4": (glob.glob("takes/media-generation-u4-take1-*.mp4")[0], None),
    # (trim_end_frame, setpts_factor, atempo)
    "U5": (glob.glob("takes/media-generation-u5-take1-*.mp4")[0], (219, 240 / 219, 219 / 240)),
    "U6": (glob.glob("takes/media-generation-u6-take1-*.mp4")[0], (210, 240 / 210, 210 / 240)),
}

for unit, (src, fix) in TAKES.items():
    out = f"work/segments/seg_{unit}.mp4"
    if fix is None:
        vf = "scale=1280:720:flags=lanczos,fps=24,format=yuv420p"
        af = "aresample=48000"
    else:
        endf, factor, atempo = fix
        vf = f"trim=end_frame={endf},setpts={factor:.6f}*PTS,scale=1280:720:flags=lanczos,fps=24,format=yuv420p"
        af = f"atrim=end_sample=999999999,atempo={atempo:.6f},aresample=48000"
    cmd = ["ffmpeg", "-v", "error", "-i", src,
           "-vf", vf, "-af", af, "-frames:v", "240",
           "-c:v", "libx264", "-crf", "12", "-preset", "medium",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
           out, "-y"]
    subprocess.run(cmd, check=True)
    n = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-count_frames", "-show_entries", "stream=nb_read_frames",
                        "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    print(unit, "frames:", n)

with open("work/concat.txt", "w") as fh:
    for unit in ("U1", "U2", "U3", "U4", "U5", "U6"):
        fh.write(f"file 'segments/seg_{unit}.mp4'\n")

subprocess.run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
                "-i", "work/concat.txt", "-c", "copy", "work/joined.mp4", "-y"], check=True)
r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                    "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
                    "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1",
                    "work/joined.mp4"], capture_output=True, text=True)
print("JOINED:\n", r.stdout)
