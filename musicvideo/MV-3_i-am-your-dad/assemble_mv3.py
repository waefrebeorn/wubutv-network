#!/usr/bin/env python3
"""MV-3 assembly: frame-exact timeline build (16:9 + 9:16 intermediates).

Rules enforced (parent brief + Slopcannon skill, line-328 discipline wins):
- Master audio = track.mp3 untouched; generated clip audio dropped.
- Grey keeps warped to band edge ONLY (duration factor w = ratio/edge,
  edge 1.25 if ratio > 1.25, 0.80 if ratio < 0.80); never beyond 1.5x.
- NO freeze while words play. Shortfalls after band-edge warp are covered
  by tail-loops (replay of the take's own post-line tail video), never
  by freezing and never by slowing a take to cover a hold.
- True no-word windows (leader, instrumental, breath gaps) are covered
  by the previous scene's take video running on (segment spans run to
  the NEXT scene start); the only freeze is the pre-first-word leader
  (S01 frame 0, a held shot before any word).
- Cuts land on scene (line) boundaries only.
- S03 cutaway: no mouth, no words -> slow-motion 1.382x to fill its
  13.82s instrumental window (freeze alternative reads stalled).
- Structural covers use denied/partial takes as VIDEO cover only; the
  master audio carries every line. No new video is generated.
"""
import json, subprocess, sys, os

FPS = 24
PROJ = os.path.dirname(os.path.abspath(__file__))
TAKES = os.path.join(PROJ, "takes")

# (scene, start_s, take/warp pieces)
# piece: (filename, warp, src_start_s, src_end_s or None=fill remainder)
def F(fn, w, s=0.0, e="FULL"):
    return (fn, w, s, e)

SCENES = [
    ("S01", 2.82,  [F("mv3_s01_t2.mp4", 1.088)]),
    ("S02", 9.32,  [F("mv3_s02_t2.mp4", 1.040)]),
    ("S03", 18.34, [F("mv3_s03_t1.mp4", 1.382)]),
    ("S04", 32.16, [F("mv3_s04_t1.mp4", 1.0, 0.0, 4.40)]),
    ("S05", 36.56, [F("mv3_s05_t1.mp4", 1.0, 0.0, 3.50)]),
    ("S06", 40.06, [F("mv3_s06_t1.mp4", 1.0)]),
    ("S07", 48.12, [F("mv3_s07_t1.mp4", 0.975)]),
    ("S08", 55.14, [F("mv3_s08_t1.mp4", 1.0)]),
    ("S09", 62.64, [F("mv3_s09_t1.mp4", 0.884)]),
    ("S10", 68.36, [F("mv3_s10_t1.mp4", 1.0)]),
    ("S11", 76.28, [F("mv3_s11_t2.mp4", 0.975)]),
    ("S12", 82.92, [F("mv3_s12_t2.mp4", 0.8375)]),
    ("S13", 90.66, [F("mv3_s13_t1.mp4", 1.0)]),
    ("S14", 99.68, [F("mv3_s14_t1.mp4", 1.0)]),
    ("S15", 108.92,[F("mv3_s15_t1.mp4", 1.0)]),
    ("S16", 116.14,[F("mv3_s16_t1.mp4", 1.0)]),
    ("S17", 123.74,[F("mv3_s17_t1.mp4", 1.0)]),
    ("S18", 129.46,[F("mv3_s18_t2.mp4", 1.0)]),
    ("S19", 136.52,[F("mv3_s19_t1.mp4", 1.0)]),
    ("S20", 143.76,[F("mv3_s20_t1.mp4", 0.9625)]),
    ("S21", 150.30,[F("mv3_s21_t2.mp4", 1.0)]),
    ("S22", 160.70,[F("mv3_s22_t1.mp4", 1.0)]),
    ("S23", 168.76,[F("mv3_s23_t2.mp4", 1.216)]),
    ("S24", 183.06,[F("mv3_s24_t2.mp4", 1.0)]),
    ("S25", 195.24,[F("mv3_s25_t1.mp4", 1.0), F("mv3_s25_t2.mp4", 1.0)]),
    ("S26", 215.40,[F("mv3_s26_t1.mp4", 1.0)]),
    ("S27", 220.64,[F("mv3_s27_t1.mp4", 1.0)]),
    ("S28", 230.52,[F("mv3_s28_t3.mp4", 1.256)]),
    ("S29", 245.10,[F("mv3_s29_t1.mp4", 0.8375)]),
    ("S30", 251.04,[F("mv3_s30_t3.mp4", 1.0)]),
    ("S31", 258.32,[F("mv3_s31_t1.mp4", 1.240)]),
    ("S32", 268.50,[F("mv3_s32_t1.mp4", 1.040)]),
    ("S33", 278.50,[F("mv3_s33_t1.mp4", 1.032)]),
    ("S34", 287.80,[F("mv3_s34_t1.mp4", 1.0)]),
    ("S35", 296.70,[F("mv3_s35_t1.mp4", 1.0), F("mv3_s35_t2.mp4", 1.0, 0.0, 4.18)]),
    ("S36", 309.88,[F("mv3_s36_t2.mp4", 1.112)]),
    ("S37", 322.08,[F("mv3_s37_t1.mp4", 1.0), F("mv3_s37_t1.mp4", 1.0, 0.0, None)]),
    ("S38", 338.55,[F("mv3_s38_t2.mp4", 0.9125)]),
    ("S39", 344.55,[F("mv3_s39_t1.mp4", 1.0)]),
]
SONG_END = 354.816
SONG_FRAMES = round(SONG_END * FPS)  # 8516

def ffprobe_frames(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=nb_frames,width,height,avg_frame_rate",
        "-of", "json", path], capture_output=True, text=True, check=True).stdout
    s = json.loads(out)["streams"][0]
    assert int(s["width"]) == 1280 and int(s["height"]) == 720, (path, s)
    assert s["avg_frame_rate"] == "24/1", (path, s)
    return int(s["nb_frames"])

def build_plan():
    take_frames = {}
    for _, _, pieces in SCENES:
        for fn, _, _, _ in pieces:
            if fn not in take_frames:
                take_frames[fn] = ffprobe_frames(os.path.join(TAKES, fn))
    # segment frame boundaries: leader + each scene runs to next scene start
    bounds = [("LEADER", 0.0)] + [(sc, st) for sc, st, _ in SCENES]
    starts = {}
    for i, (sc, st) in enumerate(bounds):
        starts[sc] = round(st * FPS)
    ends = {}
    for i in range(len(bounds) - 1):
        ends[bounds[i][0]] = starts[bounds[i + 1][0]]
    ends["S39"] = SONG_FRAMES
    plan = []
    for sc, st, pieces in SCENES:
        seg_frames = ends[sc] - starts[sc]
        plist = []
        total = 0
        for fn, w, s, e in pieces:
            tf = take_frames[fn]
            if e is None:
                # fill remainder of segment
                need = seg_frames - total
                src_frames = round(need / w)
                assert src_frames <= tf, (sc, fn, "fill exceeds take")
                wf = round(src_frames * w)
                plist.append((fn, w, 0, src_frames, wf))
                total += wf
            else:
                sf = round(s * FPS)
                ef = tf if e == "FULL" else min(round(e * FPS), tf)
                wf = round((ef - sf) * w)
                plist.append((fn, w, sf, ef, wf))
                total += wf
        deficit = seg_frames - total
        plan.append({"scene": sc, "start_f": starts[sc], "seg_frames": seg_frames,
                     "pieces": plist, "warped_total": total, "deficit": deficit})
    return plan, take_frames

def main():
    plan, take_frames = build_plan()
    print(f"song frames: {SONG_FRAMES}  total segment frames: "
          f"{sum(p['seg_frames'] for p in plan) + round(2.82*FPS)}")
    for p in plan:
        ps = " + ".join(f"{fn}[{sf}:{ef}]x{w}={wf}f"
                        for fn, w, sf, ef, wf in p["pieces"])
        print(f"{p['scene']} seg={p['seg_frames']}f warped={p['warped_total']}f "
              f"deficit={p['deficit']}f :: {ps}")
    print("shortfalls (tail-loop cover):",
          [(p["scene"], p["deficit"]) for p in plan if p["deficit"] > 0])

def build_filter(plan, take_frames, crops=None):
    """Returns (inputs, filter_complex, vout_label). crops=None -> 16:9."""
    # unique inputs in order of first use
    inputs, idx = [], {}
    def input_of(fn):
        if fn not in idx:
            idx[fn] = len(inputs)
            inputs.append(os.path.join(TAKES, fn))
        return idx[fn]
    s01 = input_of("mv3_s01_t2.mp4")
    for p in plan:
        for fn, _, _, _, _ in p["pieces"]:
            input_of(fn)
    chains, seg_labels = [], []
    # leader: freeze S01 frame 0 (pre-first-word held shot)
    n_lead = round(2.82 * FPS)
    extra = ""
    if crops is not None:
        extra = f",crop=405:720:{crops['S01']}:0,scale=720:1280"
    # NOTE: ffmpeg loop=N on 1 frame emits N+2 frames (verified: 67->69,
    # 66->68), so use n_lead-2 for exactly n_lead frames.
    chains.append(
        f"[{s01}:v]trim=start_frame=0:end_frame=1,setpts=PTS-STARTPTS,"
        f"loop=loop={n_lead-2}:size=1:start=0,setpts=PTS-STARTPTS,"
        f"fps={FPS},scale=1280:720,format=yuv420p{extra},setpts=PTS-STARTPTS[seg_leader]")
    seg_labels.append("seg_leader")
    for p in plan:
        sc = p["scene"]
        piece_labels = []
        for pi, (fn, w, sf, ef, wf) in enumerate(p["pieces"]):
            ii = input_of(fn)
            trim = f"trim=start_frame={sf}:end_frame={ef},setpts=PTS-STARTPTS,"
            lab = f"s_{sc}_{pi}"
            c = (f"[{ii}:v]{trim}setpts={w}*PTS,fps={FPS},"
                 f"trim=end_frame={wf},setpts=PTS-STARTPTS,"
                 f"scale=1280:720,format=yuv420p")
            if crops is not None:
                c += f",crop=405:720:{crops[sc]}:0,scale=720:1280"
            c += f",setpts=PTS-STARTPTS[{lab}]"
            chains.append(c)
            piece_labels.append(lab)
        if p["deficit"] > 0:
            # tail-loop: replay the last piece's warped tail (post-line hold
            # video, moving) to cover the deficit; oversize by 2 frames,
            # segment trim below cuts the excess.
            fn, w, sf, ef, wf = p["pieces"][-1]
            ii = input_of(fn)
            tf = take_frames[fn]
            need_src = int((p["deficit"] + 2) / w) + 1
            ts = max(0, tf - need_src)
            lab = f"s_{sc}_loop"
            c = (f"[{ii}:v]trim=start_frame={ts}:end_frame={tf},"
                 f"setpts=PTS-STARTPTS,setpts={w}*PTS,fps={FPS},"
                 f"trim=end_frame={p['deficit'] + 2},setpts=PTS-STARTPTS,"
                 f"scale=1280:720,format=yuv420p")
            if crops is not None:
                c += f",crop=405:720:{crops[sc]}:0,scale=720:1280"
            c += f",setpts=PTS-STARTPTS[{lab}]"
            chains.append(c)
            piece_labels.append(lab)
        if len(piece_labels) == 1:
            chains.append(f"[{piece_labels[0]}]trim=end_frame={p['seg_frames']},"
                          f"setpts=PTS-STARTPTS[seg_{sc}]")
        else:
            ins = "".join(f"[{l}]" for l in piece_labels)
            chains.append(f"{ins}concat=n={len(piece_labels)}:v=1:a=0,"
                          f"trim=end_frame={p['seg_frames']},"
                          f"setpts=PTS-STARTPTS[seg_{sc}]")
        seg_labels.append(f"seg_{sc}")
    ins = "".join(f"[{l}]" for l in seg_labels)
    chains.append(f"{ins}concat=n={len(seg_labels)}:v=1:a=0,setpts=PTS-STARTPTS[vout]")
    return inputs, ";".join(chains), "vout"

def run_build():
    plan, take_frames = build_plan()
    crops = json.load(open(os.path.join(PROJ, "crops.json")))
    os.makedirs(os.path.join(PROJ, "masters"), exist_ok=True)
    for name, cr in [("16x9", None), ("9x16", crops)]:
        inputs, fc, _ = build_filter(plan, take_frames, cr)
        out = os.path.join(PROJ, "masters", f"mv3_intermediate_{name}.mp4")
        cmd = ["ffmpeg", "-y", "-v", "error"]
        for ip in inputs:
            cmd += ["-i", ip]
        cmd += ["-filter_complex", fc, "-map", "[vout]", "-c:v", "libx264",
                "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p",
                "-r", str(FPS), "-an", out]
        print(f"building {name} intermediate ({len(inputs)} inputs) ...")
        subprocess.run(cmd, check=True)
        nf = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
            "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames",
            "-of", "csv=p=0", out], capture_output=True, text=True,
            check=True).stdout.strip()
        print(f"  {out}: {nf} frames (target {SONG_FRAMES})")
        assert int(nf) == SONG_FRAMES, (name, nf)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        run_build()
    else:
        main()
