#!/usr/bin/env python3
"""E2 SHOW-5 assembly — recovery coordinator.
Usage: assemble.py U01c U02 U03 U04 U05 U06c   (take basenames, in unit order)
Steps: conform 6 segments (240f each, 1280x720, graphics+bug burned) ->
concat to work/joined.mp4 -> probe (must be 1440f) -> loudness measure ->
ONE master encode (CRF 18) with pure-gain loudness pass -> masters/.
Graphics per REFERENCE_STACK.md plan:
  U1: Seat Map pos2, 1.5-4.0s, bottom-left (HOOK; section 3.5: nothing before ~1.5s)
  U3: Two Tickets intact 1.5-2.2s -> torn 2.2-4.5s, bottom-left
  U6: Seat Map pos2, 8.8-10.0s (final graphic at the last cliff)
  All: ~ WuBu ~ bug bottom-right, full duration.
"""
import json, os, subprocess, sys

EP = os.path.expanduser("~/workspace/wubutv-network/new-era/episodes/E2_SHOW-5_the-last-seat")
GFX = f"{EP}/work/gfx"
SEG = f"{EP}/work/segments"
os.makedirs(SEG, exist_ok=True)

def run(cmd, **kw):
    print("+", " ".join(cmd[:3]), "...", flush=True)
    subprocess.run(cmd, check=True, **kw)

def frames(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-count_frames", "-show_entries", "stream=nb_read_frames",
                          "-of", "csv=p=0", path], capture_output=True, text=True)
    return int(out.stdout.strip())

def segment(idx, take):
    out = f"{SEG}/seg{idx}.mp4"
    src = f"{EP}/takes/{take}.mp4"
    base = ("[0:v]scale=1280:720:flags=lanczos,setsar=1,"
            "trim=end_frame=240,setpts=N/(24*TB)[base];")
    fc = base
    inputs = ["-i", src]
    last = "base"
    n = 1  # next input index
    def overlay(png, chain, xy, enable):
        nonlocal fc, last, n
        inputs.extend(["-loop", "1", "-i", png])
        fc += f"[{n}:v]{chain}[g{n}];[{last}][g{n}]overlay={xy}:enable='{enable}'[v{n}];"
        last = f"v{n}"
        n += 1
    if idx == 1:
        overlay(f"{GFX}/seatmap_pos2.png",
                "fade=t=in:st=1.5:d=0.3:alpha=1,fade=t=out:st=3.7:d=0.3:alpha=1,format=rgba",
                "24:H-h-24", "between(t,1.5,4.0)")
    if idx == 3:
        overlay(f"{GFX}/tickets_intact.png",
                "fade=t=in:st=1.5:d=0.3:alpha=1,format=rgba",
                "24:H-h-24", "between(t,1.5,2.2)")
        overlay(f"{GFX}/tickets_torn.png",
                "fade=t=out:st=4.2:d=0.3:alpha=1,format=rgba",
                "24:H-h-24", "between(t,2.2,4.5)")
    if idx == 6:
        overlay(f"{GFX}/seatmap_pos2.png",
                "fade=t=in:st=8.8:d=0.25:alpha=1,format=rgba",
                "24:H-h-24", "between(t,8.8,10.0)")
    overlay(f"{GFX}/bug_wubu.png", "format=rgba", "W-w-16:H-h-16", "gte(t,0)")
    fc += f"[{last}]null[vout]"
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc,
         "-map", "[vout]", "-map", "0:a:0",
         "-af", "apad=whole_dur=10", "-t", "10",
         "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p",
         "-r", "24", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", out])
    f = frames(out)
    print(f"seg{idx} ({take}): {f} frames", flush=True)
    assert f == 240, f"seg{idx} has {f} frames, expected 240"
    return out

def main():
    takes = sys.argv[1:]
    assert len(takes) == 6, "need exactly 6 take names"
    segs = [segment(i + 1, t) for i, t in enumerate(takes)]
    listfile = f"{EP}/work/concat_list.txt"
    with open(listfile, "w") as fh:
        for s in segs:
            fh.write(f"file '{s}'\n")
    joined = f"{EP}/work/joined.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
         "-c", "copy", joined])
    f = frames(joined)
    print(f"joined: {f} frames", flush=True)
    assert f == 1440, f"joined has {f} frames, expected 1440"
    # loudness measure (ebur128) on joined audio
    out = subprocess.run(["ffmpeg", "-i", joined, "-map", "0:a:0", "-af",
                          "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    meas = json.loads(out[out.rindex("{"):out.rindex("}") + 1])
    i_in, tp_in = float(meas["input_i"]), float(meas["input_tp"])
    gain = min(-16.0 - i_in, -1.5 - tp_in)
    print(f"loudness: input_i={i_in} LUFS input_tp={tp_in} dBTP -> gain {gain:+.2f} dB "
          f"(target -16 LUFS, ceiling -1.5 dBTP)", flush=True)
    master = f"{EP}/masters/E2_SHOW-5_the-last-seat_house.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", joined,
         "-map", "0:v:0", "-map", "0:a:0",
         "-af", f"volume={gain:.2f}dB",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
         "-r", "24", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-movflags", "+faststart", master])
    f = frames(master)
    size = os.path.getsize(master)
    print(f"MASTER: {master} frames={f} size={size}", flush=True)
    assert f == 1440
    print("ASSEMBLY DONE")

if __name__ == "__main__":
    main()
