#!/usr/bin/env python3
"""MV-3 CORRECTED 16:9 build (2026-11-06, MV-5 v4 method correction).

Base = the RETIMED build's scene table (retime_build.retimed_scenes()).
Corrections come from work/AUDIT_CORRECTED_PLAN.md (mouth-event audit of
the retimed master: 99 onsets read; probe strips for every closed onset):

- SHIFT (13 scenes): raise piece-0 head trim by N take-frames so the
  take's visible mouth-open lands on the song onset (measured mouth lag):
  S07 +5f, S08 +4f, S09 +9f, S10 +9f, S12 +4f, S14 +12f, S18 +4f,
  S19 +4f, S27 +12f, S28 +8f, S29 +16f, S34 +4f, S38 +4f.
- REWARP-SPLIT (S02): two phrases, one warp each, split at the take's
  mantra attack (take 4.0s = song 14.22s):
  A: take[13f:96f] w=117/83=1.4096 (playback 0.71x, spans 9.32-14.22)
  B: take[96f:FULL] w=99/120=0.825 (spans 14.22-18.34)
- S13: no assembly fix exists (probe: no mouth opening in the head
  window of the only take) — STRUCTURAL disclosure, unchanged.
- Captions: captions_16x9_corrected.ass (one proven fix: L02 "game").

Everything else — segment boundaries, leader, tail-loop cover, bug,
untouched track.mp3, exact 8516 frames — is identical to the retimed
build. Outputs are NEW paths; the retimed base is never overwritten.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = HERE
sys.path.insert(0, PROJ)
sys.path.insert(0, os.path.join(PROJ, "recut_work", "sync_proto"))
import assemble_mv3_recut as base
import retime_build

FPS = 24
SHIFTS = {  # scene -> extra head-trim frames on piece 0
    "S07": 5, "S08": 4, "S09": 9, "S10": 9, "S12": 4, "S14": 12,
    "S18": 4, "S19": 4, "S27": 12, "S28": 8, "S29": 16, "S34": 4,
    "S38": 4,
}


def corrected_scenes():
    out = []
    for sc, st, pieces in retime_build.retimed_scenes():
        pieces = [tuple(p) for p in pieces]
        if sc == "S02":
            fn = pieces[0][0]
            pieces = [
                (fn, 117.0 / 83.0, 13.0 / FPS, 4.0),
                (fn, 99.0 / 120.0, 4.0, "FULL"),
            ]
        elif sc in SHIFTS:
            fn, w, s, e = pieces[0]
            pieces[0] = (fn, w, s + SHIFTS[sc] / FPS, e)
        out.append((sc, st, pieces))
    return out


def main():
    base.SCENES = corrected_scenes()
    for sc, st, pieces in base.SCENES:
        if sc == "S02" or sc in SHIFTS:
            print(sc, pieces, flush=True)
    plan, take_frames = base.build_plan()
    for p in plan:
        print(f"{p['scene']} seg={p['seg_frames']}f warped={p['warped_total']}f "
              f"deficit={p['deficit']}f", flush=True)
    print("shortfalls (tail-loop cover):",
          [(p["scene"], p["deficit"]) for p in plan if p["deficit"] > 0],
          flush=True)
    assert sum(p["seg_frames"] for p in plan) + round(2.82 * FPS) == base.SONG_FRAMES
    inputs, fc, _ = base.build_filter(plan, take_frames, None)
    inter = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_corrected.mp4")
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for ip in inputs:
        cmd += ["-i", ip]
    cmd += ["-filter_complex", fc, "-map", "[vout]", "-c:v", "libx264",
            "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p",
            "-r", "24", "-an", inter]
    print("building corrected 16:9 intermediate ...", flush=True)
    subprocess.run(cmd, check=True)
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                         "-select_streams", "v:0",
                         "-show_entries", "stream=nb_read_frames",
                         "-of", "csv=p=0", inter],
                        capture_output=True, text=True, check=True).stdout.strip()
    print(f"  {inter}: {nf} frames (target {base.SONG_FRAMES})", flush=True)
    assert int(nf) == base.SONG_FRAMES, (inter, nf)
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=36:"
           f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
           f"x=w-tw-30:y=30")
    out = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_corrected.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", inter, "-i",
                    os.path.join(PROJ, "track.mp3"), "-filter_complex",
                    f"[0:v]subtitles={os.path.join(PROJ, 'captions_16x9_corrected.ass')},{bug}[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac",
                    "-ar", "48000", "-ac", "2", "-b:a", "192k",
                    "-movflags", "+faststart", out], check=True)
    print(f"corrected 16:9 final: {out}", flush=True)


if __name__ == "__main__":
    main()
