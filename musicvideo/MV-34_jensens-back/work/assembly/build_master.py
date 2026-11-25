#!/usr/bin/env python3
"""MV-34 assembly renderer: capped-map frame selection per segment
(render_capped.py, MV-30 fix2 lineage), segment encodes (CRF 14
veryfast intermediate), concat, joined probe assert. Exactly ONE
assembly pass owns work/joined.mp4. Resumable via
work/assembly/segments_ledger.json (atomic writes). Per-segment
output frames are deleted after encode to bound disk use; the
render logs (maps/segNNN_render.json) carry the realized word
onset errors for GATE_LOG.
"""
import json, os, shutil, subprocess, sys

P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = os.path.join(P, "work", "assembly")
MAPS = os.path.join(A, "maps")
SEGDIR = os.path.join(A, "segments")
FRAMES_ROOT = os.path.join(A, "take_frames")
OUTFRAMES = os.path.join(A, "seg_frames")
LEDGER = os.path.join(A, "segments_ledger.json")
FPS = 24
TOTAL_FRAMES = 1450

# per-take extraction filter (conform): S24 centre-crops 1152x768 -> 16:9
VF = {}
VF_DEFAULT = "fps=24,scale=1280:720"


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(cmd)[:300])
        print(r.stdout[-1500:])
        print(r.stderr[-2500:])
        sys.exit(1)
    return r.stdout


def probe_frames(path):
    out = run(["ffprobe", "-v", "error", "-count_frames", "-select_streams",
               "v:0", "-show_entries", "stream=nb_read_frames",
               "-of", "csv=p=0", path])
    return int(out.strip())


def save_ledger(led):
    tmp = LEDGER + ".tmp"
    with open(tmp, "w") as f:
        json.dump(led, f, indent=1)
    json.load(open(tmp))
    os.rename(tmp, LEDGER)


def main():
    plan = json.load(open(os.path.join(A, "segment_plan.json")))
    led = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
    os.makedirs(SEGDIR, exist_ok=True)
    os.makedirs(FRAMES_ROOT, exist_ok=True)
    os.makedirs(OUTFRAMES, exist_ok=True)

    # 1. extract take frames once per unique take (1280x720, 24fps)
    takes = sorted({s["take"] for s in plan})
    for take in takes:
        stem = take[:-4]
        fdir = os.path.join(FRAMES_ROOT, stem)
        expect = 240
        n = len([f for f in os.listdir(fdir)]) if os.path.isdir(fdir) else 0
        if n != expect:
            src = os.path.join(P, "takes", take)
            os.makedirs(fdir, exist_ok=True)
            run(["ffmpeg", "-y", "-v", "error", "-i", src, "-vf",
                 VF.get(take, VF_DEFAULT), "-compression_level", "1",
                 os.path.join(fdir, "f_%04d.png")])
            n = len([f for f in os.listdir(fdir)])
            assert n == expect, f"{take}: {n} frames extracted != {expect}"
        print(f"frames ready: {take} ({n})", flush=True)

    # 2. per-segment render + encode
    qc = {}
    for s in plan:
        idx = s["idx"]
        key = f"seg{idx:03d}"
        seg_path = os.path.join(SEGDIR, f"{key}.mp4")
        target = s["frames"][1] - s["frames"][0]
        if key in led and os.path.exists(seg_path) \
                and probe_frames(seg_path) == target:
            print(f"{key}: cached ({target}f)", flush=True)
            continue
        stem = s["take"][:-4]
        fdir = os.path.join(FRAMES_ROOT, stem)
        odir = os.path.join(OUTFRAMES, key)
        swp = os.path.join(MAPS, f"{key}_songwords.json")
        twp = os.path.join(MAPS, f"{key}_takewords.json")
        json.dump(s.get("song_words", []), open(swp, "w"))
        json.dump(s.get("take_words", []), open(twp, "w"))
        out = run(["python3", os.path.join(A, "render_capped.py"),
                   "--src-frames", fdir,
                   "--map", os.path.join(MAPS, f"{key}_capped.json"),
                   "--song-words", swp, "--take-words", twp,
                   "--out-dir", odir,
                   "--log-out", os.path.join(MAPS, f"{key}_render.json")])
        print(f"{key}: {out.strip()}", flush=True)
        rlog = json.load(open(os.path.join(MAPS, f"{key}_render.json")))
        qc[key] = {"ratio_min": rlog["per_frame_ratio_min"],
                   "ratio_max": rlog["per_frame_ratio_max"],
                   "word_errors": rlog["per_word_realized_onset_error"]}
        run(["ffmpeg", "-y", "-v", "error", "-framerate", "24",
             "-i", os.path.join(odir, "frame_%03d.png"),
             "-vf", "format=yuv420p,tpad=stop_mode=clone:stop_duration=2",
             "-frames:v", str(target), "-c:v", "libx264", "-preset",
             "veryfast", "-crf", "14", seg_path])
        got = probe_frames(seg_path)
        assert got == target, f"{key}: {got} frames != target {target}"
        led[key] = {"frames": got, "scene": s["scene"], "kind": s["kind"],
                    "take": s["take"]}
        save_ledger(led)
        shutil.rmtree(odir, ignore_errors=True)
        print(f"{key}: encoded {got}f", flush=True)

    with open(os.path.join(A, "warp_qc.json.tmp"), "w") as f:
        json.dump(qc, f, indent=1)
    json.load(open(os.path.join(A, "warp_qc.json.tmp")))
    os.rename(os.path.join(A, "warp_qc.json.tmp"),
              os.path.join(A, "warp_qc.json"))

    # 3. concat + joined assert (single assembly pass owns joined.mp4)
    lst = os.path.join(A, "concat.txt")
    with open(lst, "w") as f:
        for s in plan:
            f.write(f"file '{os.path.join(SEGDIR, 'seg%03d.mp4' % s['idx'])}'\n")
    joined = os.path.join(P, "work", "joined.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", lst, "-c", "copy", joined])
    nf = probe_frames(joined)
    dur = float(run(["ffprobe", "-v", "error", "-show_entries",
                     "format=duration", "-of", "csv=p=0", joined]).strip())
    assert nf == TOTAL_FRAMES, f"joined frames {nf} != {TOTAL_FRAMES}"
    assert abs(dur - TOTAL_FRAMES / FPS) < 0.05, f"joined duration {dur}"
    info = {"joined": joined, "frames": nf, "duration_s": round(dur, 3),
            "segments": len(plan)}
    with open(os.path.join(A, "joined.json.tmp"), "w") as f:
        json.dump(info, f, indent=1)
    json.load(open(os.path.join(A, "joined.json.tmp")))
    os.rename(os.path.join(A, "joined.json.tmp"),
              os.path.join(A, "joined.json"))
    print("JOINED_OK", info, flush=True)


if __name__ == "__main__":
    main()
