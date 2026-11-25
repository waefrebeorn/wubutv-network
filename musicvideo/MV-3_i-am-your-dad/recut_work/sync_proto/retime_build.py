#!/usr/bin/env python3
"""MV-3 RETIMED 16:9 build (2026-11-05, user order: "retime it ... fast and best").

Single-format policy (user, 2026-11-05 ~01:31 EST, standing rule): ONLY
one 16:9 master from now on -- no 9:16, no chat copy. This script builds
16:9 ONLY. It never touches build 3's outputs (the delivered re-cut
masters/intermediates) and never touches the rejected cut.

What changed vs the re-cut (CUTLIST_RECUT.md): exactly three warp
factors, from the cross-check fit (fit_retime.py / retime_warps.json):
  S16  0.8643 -> 0.810  (median |off| 0.47 -> 0.28, max 0.66 -> 0.54)
  S18  0.8234 -> 0.965  (median |off| 0.77 -> 0.19, max 0.91 -> 0.37)
  S34  1.1453 -> 0.910  (median |off| 0.51 -> 0.26, end residual +1.70 -> +0.02)
Everything else -- segment boundaries, trims, tail-loop cover, captions,
bug, master audio, frame count (8516) -- is identical to the re-cut.
Law One: the song never moves; only these three take-side warps change.

Mechanics reused verbatim from assemble_mv3_recut.py (imported, SCENES
monkeypatched with the retimed warps): leader hold, setpts warp, concat,
tail-loop cover, per-scene trim, subtitles + bug + untouched track.mp3.

Outputs (new names, never overwrite):
  masters/mv3_intermediate_16x9_retimed.mp4
  masters/mv3_i_am_your_dad_16x9_retimed.mp4
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, PROJ)
import assemble_mv3_recut as base

WARPS = json.load(open(os.path.join(HERE, "retime_warps.json")))
RETIMED = "mv3_i_am_your_dad_16x9_retimed.mp4"


def retimed_scenes():
    out = []
    for sc, st, pieces in base.SCENES:
        # scenes the fit never scored (cutaway / structural cover) keep
        # their re-cut warp verbatim.
        w = WARPS.get(sc, {}).get("retimed_w", pieces[0][1])
        new_pieces = []
        for pi, (fn, ow, s, e) in enumerate(pieces):
            # only piece 0 (the sung piece) takes the new warp; S37's
            # hold-loop pieces stay 1.0 (cover, not mouth).
            new_pieces.append((fn, w if pi == 0 else ow, s, e))
        out.append((sc, st, new_pieces))
    return out


def main():
    base.SCENES = retimed_scenes()
    changed = [(sc, WARPS[sc]["recut_w"], WARPS[sc]["retimed_w"])
               for sc in WARPS if WARPS[sc]["adopted"]]
    print("retimed warps:", changed, flush=True)
    plan, take_frames = base.build_plan()
    for p in plan:
        print(f"{p['scene']} seg={p['seg_frames']}f warped={p['warped_total']}f "
              f"deficit={p['deficit']}f", flush=True)
    print("shortfalls (tail-loop cover):",
          [(p["scene"], p["deficit"]) for p in plan if p["deficit"] > 0], flush=True)
    inputs, fc, _ = base.build_filter(plan, take_frames, None)
    inter = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_retimed.mp4")
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for ip in inputs:
        cmd += ["-i", ip]
    cmd += ["-filter_complex", fc, "-map", "[vout]", "-c:v", "libx264",
            "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p",
            "-r", "24", "-an", inter]
    print(f"building retimed 16:9 intermediate ...", flush=True)
    subprocess.run(cmd, check=True)
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                         "-select_streams", "v:0",
                         "-show_entries", "stream=nb_read_frames",
                         "-of", "csv=p=0", inter],
                        capture_output=True, text=True, check=True).stdout.strip()
    print(f"  {inter}: {nf} frames (target {base.SONG_FRAMES})", flush=True)
    assert int(nf) == base.SONG_FRAMES, (inter, nf)
    # final: subtitles + bug + untouched master audio, as in the re-cut
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=36:"
           f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
           f"x=w-tw-30:y=30")
    out = os.path.join(PROJ, "masters", RETIMED)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", inter, "-i",
                    os.path.join(PROJ, "track.mp3"), "-filter_complex",
                    f"[0:v]subtitles={os.path.join(PROJ, 'captions_16x9.ass')},{bug}[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac",
                    "-ar", "48000", "-ac", "2", "-b:a", "192k",
                    "-movflags", "+faststart", out], check=True)
    print(f"retimed 16:9 final: {out}", flush=True)


if __name__ == "__main__":
    main()
