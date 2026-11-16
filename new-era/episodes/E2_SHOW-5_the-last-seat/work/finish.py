#!/usr/bin/env python3
"""Finish: seg2 + concat + probe + loudness + ONE master encode.
Segments 1,3,4,5,6 already conformed by assemble.segment(). This script owns
work/joined.mp4 alone (single assembly pass) and never rebuilds segments."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat/work"))
from assemble import segment, frames, EP

segment(2, "U02")
segs = [f"{EP}/work/segments/seg{i}.mp4" for i in range(1, 7)]
listfile = f"{EP}/work/concat_list.txt"
with open(listfile, "w") as fh:
    for s in segs:
        fh.write(f"file '{s}'\n")
joined = f"{EP}/work/joined.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                "-i", listfile, "-c", "copy", joined], check=True)
f = frames(joined)
print(f"joined: {f} frames", flush=True)
assert f == 1440, f"joined has {f} frames, expected 1440"
out = subprocess.run(["ffmpeg", "-i", joined, "-map", "0:a:0", "-af",
                      "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
                      "-f", "null", "-"], capture_output=True, text=True).stderr
meas = json.loads(out[out.rindex("{"):out.rindex("}") + 1])
i_in, tp_in = float(meas["input_i"]), float(meas["input_tp"])
gain = min(-16.0 - i_in, -1.5 - tp_in)
print(f"loudness: input_i={i_in} LUFS input_tp={tp_in} dBTP -> gain {gain:+.2f} dB", flush=True)
master = f"{EP}/masters/E2_SHOW-5_the-last-seat_house.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined,
                "-map", "0:v:0", "-map", "0:a:0",
                "-af", f"volume={gain:.2f}dB",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                "-pix_fmt", "yuv420p", "-r", "24",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-movflags", "+faststart", master], check=True)
f = frames(master)
print(f"MASTER: {master} frames={f} size={os.path.getsize(master)}", flush=True)
assert f == 1440
print("FINISH DONE")
