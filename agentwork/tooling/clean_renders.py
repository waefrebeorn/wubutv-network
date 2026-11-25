#!/usr/bin/env python3
"""Clean regenerable render frames; keep every master, every spec, every line of code.

Rule: delete page-frame directories and intermediate pass dirs. Keep *.mp4, *.py, *.json,
*.md, sheets, ledgers. Nothing that cannot be rebuilt from a spec in this directory survives.
"""
import os
import shutil
import sys

DRY = "--dry" in sys.argv
SKIP = [s for s in os.environ.get("SKIP", "").split(":") if s]

KEEP_EXT = {".mp4", ".py", ".json", ".md", ".txt", ".csv", ".wav", ".c", ".sh", ".html", ".jsonl"}

# directories whose PNG/JPG frames are pure intermediates
FRAME_DIRS = [
    "/opt/data/work/wubu3d/out/plate_lamp/frames",
    "/opt/data/work/wubu3d/out/plate_lamp/frames_rast",
    "/opt/data/work/wubu3d/out/plate_lamp/frames_rast_c",
    "/opt/data/work/wubu3d/out/plate_lamp/graded",
    "/opt/data/work/wubu3d/out/plate_plain/frames",
    "/opt/data/work/wubu3d/out/plate_plain/frames_rast",
    "/opt/data/work/wubu3d/out/plate_plain/frames_rast_c",
    "/opt/data/work/wubu3d/out/plate_plain/graded",
    "/opt/data/work/wubu3d/out/demo_cinematic/frames",
    "/opt/data/work/wubu3d/out/demo_cinematic/frames_rast",
    "/opt/data/work/wubu3d/out/demo_cinematic/frames_rast_c",
    "/opt/data/work/wubu3d/out/demo_cinematic/graded",
    "/opt/data/work/wubu3d/out/demo_cinematic/denoised",
    "/opt/data/work/wubu3d/out/demo_moves/frames",
    "/opt/data/work/wubu3d/out/demo_moves/frames_rast",
    "/opt/data/work/wubu3d/out/demo_moves/graded",
    "/opt/data/work/wubu3d/out/demo_cartoon/frames",
    "/opt/data/work/wubu3d/out/demo_cartoon/graded",
    "/opt/data/work/wubu3d/out/demo_preview/frames",
    "/opt/data/work/wubu3d/out/demo_preview/graded",
    "/opt/data/work/wubu3d/out/film_handoff/frames",
    "/opt/data/work/wubu3d/out/cull_cmp",
    "/opt/data/work/ident/c_intro",
    "/opt/data/work/ident/c_lockup",
    "/opt/data/work/ident/c_end",
    "/opt/data/work/mystery/c_intro",
    "/opt/data/work/mystery/c_final",
    "/opt/data/work/mystery/k_intro",
    "/opt/data/work/mystery/k_end",
    "/opt/data/work/wubu-agi/promo_frames",
    "/opt/data/work/promo/card0", "/opt/data/work/promo/card1", "/opt/data/work/promo/card2",
    "/opt/data/work/promo/card3", "/opt/data/work/promo/card4", "/opt/data/work/promo/card5",
    "/opt/data/work/promo/card6",
]


def dir_size(p):
    total = 0
    for root, _, files in os.walk(p):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total


def main():
    freed = 0
    for d in FRAME_DIRS:
        if not os.path.isdir(d):
            continue
        if any(s in d for s in SKIP):
            print(f'skip (in use)        {d}')
            continue
        # keep any masters that somehow live inside a frame dir
        kept = []
        for f in os.listdir(d):
            p = os.path.join(d, f)
            if os.path.isfile(p) and os.path.splitext(f)[1].lower() in KEEP_EXT:
                kept.append((p, os.path.join(os.path.dirname(d), f)))
        size = dir_size(d)
        print(f'{"would free" if DRY else "free"} {size/1e6:8.1f} MB  {d}')
        if DRY:
            freed += size
            continue
        for src, dst in kept:
            shutil.move(src, dst)
        shutil.rmtree(d)
        freed += size
    print(f"\n{'would free' if DRY else 'freed'} {freed/1e9:.2f} GB")


if __name__ == "__main__":
    main()
