#!/usr/bin/env python3
"""MV-5 picture checks.

(1) Donor-slice mouth check (from the TAKES, before assembly): one frame
    from the middle of every donor slice in the fit plan, tiled into a
    contact sheet — read it to confirm the mouth is closed / the shot is a
    reaction or B-roll, never a sung mouth forming a different word.
(2) Master contact sheet (after the build): one frame per scene at the
    scene's first sung word time (from the fit plan), tiled — read it to
    confirm the right characters, locks holding, and mouths open on words.
"""
import json, os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5.json")))
FPS = 24
TMP = "/tmp/mv5_pics"
os.makedirs(TMP, exist_ok=True)

def grab(src, t, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", src,
                    "-frames:v", "1", "-vf", "scale=320:180", out], check=True)

def tile(frames, out, cols=8):
    from PIL import Image
    n = len(frames)
    rows = (n + cols - 1) // cols
    W, H = 320, 180
    sheet = Image.new("RGB", (cols * (W + 2) + 2, rows * (H + 2) + 2), "black")
    for k, f in enumerate(frames):
        im = Image.open(f).resize((W, H))
        x = 2 + (k % cols) * (W + 2)
        y = 2 + (k // cols) * (H + 2)
        sheet.paste(im, (x, y))
    sheet.save(out, quality=88)
    print(f"sheet {n} frames {cols}x{rows} -> {out}")

def donor_sheet():
    frames = []
    labels = []
    for sc in FIT["scenes"]:
        for p in FIT["plan"][sc]:
            if not p["kind"].startswith(("donor-", "cover-")):
                continue
            mid = (p["sf"] + p["ef"]) / 2 / FPS
            out = os.path.join(TMP, f"donor_{sc}_{p['take']}_{p['sf']}.jpg")
            grab(os.path.join(PROJ, "takes", p["take"] + ".mp4"), mid, out)
            frames.append(out)
            labels.append(f"{sc} {p['take']}[{p['sf']}:{p['ef']}]")
    tile(frames, os.path.join(PROJ, "work", "donor_contact_sheet.jpg"))
    print("\n".join(labels))

def master_sheet():
    master = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9.mp4")
    if not os.path.exists(master):
        print("master not built yet; skipping master sheet")
        return
    SUNG = {"span", "span-grey", "refrain-R1", "refrain-R2", "refrain-R3",
            "refrain-R4", "refrain-R2-grey", "refrain-R3-grey",
            "refrain-R4-env", "L39-grey", "L40-tail", "no-need-to",
            "refrain-R1-grey"}
    frames = []
    for sc in FIT["scenes"]:
        sung = [p for p in FIT["plan"][sc] if p["kind"] in SUNG]
        if sung:
            t = sung[0]["dst0"] + 0.15
        else:
            # cover scene: mid-scene
            t = (FIT["plan"][sc][0]["dst0"] + FIT["plan"][sc][-1]["dst1"]) / 2
        out = os.path.join(TMP, f"master_{sc}.jpg")
        grab(master, t, out)
        frames.append(out)
        print(f"{sc}: frame at {t:.2f}s ({'sung' if sung else 'cover'})")
    tile(frames, os.path.join(PROJ, "work", "master_contact_sheet.jpg"), cols=6)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "master":
        master_sheet()
    else:
        donor_sheet()
