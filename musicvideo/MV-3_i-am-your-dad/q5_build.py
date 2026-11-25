#!/usr/bin/env python3
"""MV-3 Q5 build (2026-11-12, improvement program Q5 — recovery coordinator).

Base = the CORRECTED build's scene table (corrected_build.corrected_scenes()).
Only two pieces change — the Q5 replacement takes, both KEEP per work/q5/Q5_VERDICTS.md:

- S13: mv3_s13_t2.mp4, w=1.0, take[0.25s:9.25s] (6f head trim so the mouth,
  T at take 0.00 / O by 0.25s, lands OPEN on song 90.66 — the catalogue's
  only closed onset). Single smooth warp; every song onset in the slot
  lands on an open/transitional mouth (verified frame by frame in the
  verdict file). Slot seg 216f, warped 216f, deficit 0.
- S39: mv3_s39_t2.mp4, w=247/156=1.5833, take[0.0s:6.5s]. One smooth warp
  of the take's single sung phrase (0-5.92s) across the full mantra span;
  burst onsets read O/T under this warp. Used span ends at take 6.5s —
  NEVER the 7.25-8.0s eye-closed beat or the 8.58-9.67s still tail.
  Slot seg 247f, warped 247f, deficit 0. Slowest playback in the Q5
  master: 0.63x (inside the 0.5x floor), disclosed.

Everything else — all other scenes, leader, captions
(captions_16x9_corrected.ass, incl. the L02 "game" fix), bug, untouched
track.mp3, exact 8516 frames — is identical to the corrected build.
Outputs are NEW paths; the corrected master is never overwritten.
No commit. No delivered flag (parent writes it).

Stages: plan | inter | final  (run separately so a daemon restart
leaves recoverable progress on disk after each stage).
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = HERE
sys.path.insert(0, PROJ)
sys.path.insert(0, os.path.join(PROJ, "recut_work", "sync_proto"))
import assemble_mv3_recut as base
import corrected_build

FPS = 24


def q5_scenes():
    out = []
    for sc, st, pieces in corrected_build.corrected_scenes():
        pieces = [tuple(p) for p in pieces]
        if sc == "S13":
            pieces = [("mv3_s13_t2.mp4", 1.0, 0.25, 9.25)]
        elif sc == "S39":
            pieces = [("mv3_s39_t2.mp4", 247.0 / 156.0, 0.0, 6.5)]
        out.append((sc, st, pieces))
    return out


def plan_stage():
    base.SCENES = q5_scenes()
    plan, take_frames = base.build_plan()
    for p in plan:
        if p["scene"] in ("S13", "S39"):
            print(f"{p['scene']} seg={p['seg_frames']}f warped={p['warped_total']}f "
                  f"deficit={p['deficit']}f :: {p['pieces']}", flush=True)
    print("shortfalls (tail-loop cover):",
          [(p["scene"], p["deficit"]) for p in plan if p["deficit"] > 0],
          flush=True)
    assert sum(p["seg_frames"] for p in plan) + round(2.82 * FPS) == base.SONG_FRAMES
    s13 = [p for p in plan if p["scene"] == "S13"][0]
    s39 = [p for p in plan if p["scene"] == "S39"][0]
    assert s13["seg_frames"] == 216 and s13["warped_total"] == 216 and s13["deficit"] == 0, s13
    assert s39["seg_frames"] == 247 and s39["warped_total"] == 247 and s39["deficit"] == 0, s39
    print("plan OK: S13 216/216/0, S39 247/247/0, total 8516f", flush=True)


def inter_stage():
    base.SCENES = q5_scenes()
    plan, take_frames = base.build_plan()
    inputs, fc, _ = base.build_filter(plan, take_frames, None)
    inter = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_q5.mp4")
    cmd = ["ffmpeg", "-y", "-v", "error"]
    for ip in inputs:
        cmd += ["-i", ip]
    cmd += ["-filter_complex", fc, "-map", "[vout]", "-c:v", "libx264",
            "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p",
            "-r", "24", "-an", inter]
    print("building Q5 16:9 intermediate ...", flush=True)
    subprocess.run(cmd, check=True)
    nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                         "-select_streams", "v:0",
                         "-show_entries", "stream=nb_read_frames",
                         "-of", "csv=p=0", inter],
                        capture_output=True, text=True, check=True).stdout.strip()
    print(f"  {inter}: {nf} frames (target {base.SONG_FRAMES})", flush=True)
    assert int(nf) == base.SONG_FRAMES, (inter, nf)


def final_stage():
    FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=36:"
           f"fontcolor=0xFFC61E:box=1:boxcolor=black@0.5:boxborderw=12:"
           f"x=w-tw-30:y=30")
    inter = os.path.join(PROJ, "masters", "mv3_intermediate_16x9_q5.mp4")
    out = os.path.join(PROJ, "masters", "mv3_i_am_your_dad_16x9_q5.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", inter, "-i",
                    os.path.join(PROJ, "track.mp3"), "-filter_complex",
                    f"[0:v]subtitles={os.path.join(PROJ, 'captions_16x9_corrected.ass')},{bug}[v]",
                    "-map", "[v]", "-map", "1:a",
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac",
                    "-ar", "48000", "-ac", "2", "-b:a", "192k",
                    "-movflags", "+faststart", out], check=True)
    print(f"Q5 16:9 final: {out}", flush=True)


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "plan"
    {"plan": plan_stage, "inter": inter_stage, "final": final_stage}[stage]()
