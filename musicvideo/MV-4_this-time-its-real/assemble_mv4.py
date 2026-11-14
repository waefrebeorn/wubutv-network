#!/usr/bin/env python3
"""MV-4 assembly: ONE 16:9 master from measured word-span placements.

Method (WORD-SYNC, MV-3 re-cut precedent):
- Per-scene placement from work/assembly_fit.json (grid-optimized warp/trim:
  maximize words inside +-0.50s, then median |off|; first word within +-0.30s;
  last-word end residual in [-0.75, +0.50]s; warp in [0.80, 1.25]).
- Segment boundaries = cumulative rounded song first-word times (sum = 5731f).
- Whole-clip setpts warp per scene, trim at first word, exact frame counts.
- Deficits covered by tail-loops (moving post-line footage, never during words).
- S23/S25 = montage from post-word tails (slice starts verified >= the donor's
  segment-use end AND >= last-word end + 1 frame; never a rejected take).
- S11 trimmed at first-delivery end (7.22s); S28/S30a/S30b are 0-word cutaways.
- Audio: track.mp3 muxed untouched as the sole master audio; clip audio dropped.
- Captions (captions_16x9.ass, line-block + per-word highlight) + "~ WuBu ~"
  corner bug burned in the final pass. Output: masters/mv4_this_time_its_real_16x9.mp4
  1280x720, 24fps, 5731 frames, 238.805s, h264 + AAC 48kHz, faststart.
"""
import json, os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit.json")))
SONG_FRAMES = 5731  # round(238.805333 * 24)
FPS = 24

# Segment boundaries (song first-word times; final = song end). Cumulative
# rounding keeps the total exactly SONG_FRAMES.
BOUNDS = [0.00, 7.70, 16.00, 23.34, 32.36, 39.72, 46.88, 54.20, 64.82, 72.80,
           79.52, 86.96, 95.40, 103.36, 110.34, 117.96, 126.44, 133.82, 140.56,
           148.40, 158.76, 166.54, 173.90, 181.24, 188.24, 194.06, 198.38,
           205.09, 211.75, 220.77, 229.00, 238.805333]
SCENES = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10",
          "S11", "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20",
          "S21", "S22", "S23", "S24", "S25", "S26", "S27", "S28", "S29",
          "S30a", "S30b"]
SEG_F = [round(BOUNDS[i + 1] * FPS) - round(BOUNDS[i] * FPS) for i in range(len(SCENES))]
assert sum(SEG_F) == SONG_FRAMES, (sum(SEG_F), SONG_FRAMES)

TAKE_FILE = {
    "S01": "mv4_s01_t1", "S02": "mv4_s02_t1", "S03": "mv4_s03_t1",
    "S04": "mv4_s04_t1", "S05": "mv4_s05_t1", "S06": "mv4_s06_t3",
    "S07": "mv4_s07_t1", "S08": "mv4_s08_t1", "S09": "mv4_s09_t1",
    "S10": "mv4_s10_t1", "S11": "mv4_s11_t1", "S12": "mv4_s12_t1",
    "S13": "mv4_s13_t1", "S14": "mv4_s14_t1", "S15": "mv4_s15_t1",
    "S16": "mv4_s16_t1", "S17": "mv4_s17_t1", "S18": "mv4_s18_t2",
    "S19": "mv4_s19_t1", "S20": "mv4_s20_t1", "S21": "mv4_s21_t1",
    "S22": "mv4_s22_t1", "S24": "mv4_s24_t1", "S26": "mv4_s26_t1",
    "S27": "mv4_s27_t1", "S28": "mv4_s28_t1", "S29": "mv4_s29_t1",
    "S30a": "mv4_s30a_t1", "S30b": "mv4_s30b_t1",
}
# S11: trim at first-delivery end (7.22s); the repeat tail is not used.
END_OVERRIDE = {"S11": 173}  # frames
CUTAWAYS = {"S28", "S30a", "S30b"}  # 0-word takes, w = 1.0

# Montage slices: (donor scene, length in frames). Start frame is computed
# as the donor's segment-use end (conservative) and asserted >= last-word
# end + 1 frame and inside the take. Order = playback order.
MONTAGE = {
    # S23 (176f): dance-floor tails, fast cuts across the final-chorus repeat.
    "S23": [("S13", 25), ("S06", 24), ("S14", 29), ("S16", 18), ("S24", 26),
            ("S10", 17), ("S07", 15), ("S15", 11), ("S17", 7), ("S22", 4)],
    # S25 (139f): observation deck + ship window for the soft reprise.
    "S25": [("S12", 51), ("S26", 88)],
}


def probe_frames(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=nb_frames", "-of", "csv=p=0",
                        path], capture_output=True, text=True, check=True)
    return int(r.stdout.strip())


def build_plan():
    plan = []  # (take, sf, ef, w, out_frames, kind)
    take_frames = {}
    for sc in SCENES:
        if sc in TAKE_FILE:
            take_frames[sc] = probe_frames(os.path.join(PROJ, "takes", TAKE_FILE[sc] + ".mp4"))
    for i, sc in enumerate(SCENES):
        seg = SEG_F[i]
        if sc in MONTAGE:
            total = 0
            for donor, ln in MONTAGE[sc]:
                f = FIT[donor]
                dsf = round(f["trim"] * FPS)
                dseg = SEG_F[SCENES.index(donor)]
                dw = f["warp"]
                def_ = END_OVERRIDE.get(donor, take_frames[donor])
                dwf = round((def_ - dsf) * dw)
                # Donor must have no deficit (its tail must be free, not looped).
                assert dwf >= dseg, f"{sc} donor {donor} has a deficit (wf {dwf} < seg {dseg})"
                # Conservative use end: the segment shows dseg output frames,
                # i.e. ceil(dseg/dw) input frames from dsf (fps resampling slack).
                use_end = dsf + int(dseg / dw) + (1 if dseg / dw % 1 else 0)
                assert use_end <= def_, f"{sc} donor {donor}: use_end {use_end} > ef {def_}"
                vocal_end_f = int(FIT[donor]["take_last"] * FPS) + 1
                start = max(use_end, vocal_end_f)
                assert start + ln <= take_frames[donor], \
                    f"{sc} donor {donor}: slice {start}+{ln} > take {take_frames[donor]}"
                plan.append((TAKE_FILE[donor], start, start + ln, 1.0, ln, f"montage-{sc}"))
                total += ln
            assert total == seg, f"{sc} montage {total} != seg {seg}"
            continue
        if sc in CUTAWAYS:
            # 0-word cutaway: whole take at 1.0x, trim/loop to the segment.
            tf = take_frames[sc]
            wf = tf
            if wf >= seg:
                plan.append((TAKE_FILE[sc], 0, tf, 1.0, seg, sc))
            else:
                deficit = seg - wf
                plan.append((TAKE_FILE[sc], 0, tf, 1.0, wf, sc))
                need_src = deficit + 2
                ts = tf - need_src
                plan.append((TAKE_FILE[sc], ts, tf, 1.0, deficit + 2, sc + "-loop"))
            continue
        f = FIT[sc]
        tf = take_frames[sc]
        sf = round(f["trim"] * FPS)
        ef = END_OVERRIDE.get(sc, tf)
        w = f["warp"]
        wf = round((ef - sf) * w)
        if wf >= seg:
            plan.append((TAKE_FILE[sc], sf, ef, w, seg, sc))
        else:
            deficit = seg - wf
            plan.append((TAKE_FILE[sc], sf, ef, w, wf, sc))
            need_src = int((deficit + 2) / w) + 1
            ts = tf - need_src
            assert ts >= 0, f"{sc}: loop need_src {need_src} > take {tf}"
            loop_wf = round(need_src * w)
            plan.append((TAKE_FILE[sc], ts, tf, w, deficit + 2, sc + "-loop"))
    # per-segment totals must equal seg frames (loops are trimmed by the segment trim)
    return plan, take_frames


def build_filter(plan):
    parts, inputs = [], []
    for idx, (take, sf, ef, w, out_f, kind) in enumerate(plan):
        inputs.append(f"takes/{take}.mp4")
        v = (f"[{idx}:v]trim=start_frame={sf}:end_frame={ef},"
             f"setpts=PTS-STARTPTS,setpts={w:.4f}*PTS,fps={FPS},"
             f"trim=end_frame={out_f},setpts=PTS-STARTPTS[v{idx}];")
        parts.append(v)
    n = len(plan)
    concat = "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0,trim=end_frame={SONG_FRAMES},setpts=PTS-STARTPTS"
    bug = (",drawtext=fontfile=fonts/DejaVuSans-Bold.ttf:text='~ WuBu ~':"
           "fontsize=26:fontcolor=#FFC61E:x=w-tw-28:y=h-th-22:"
           "box=1:boxcolor=black@0.55:boxborderw=14")
    subs = ",subtitles=captions_16x9.ass:fontsdir=fonts"
    return inputs, "".join(parts) + concat + bug + subs + "[vout]"


def build_cmd(inputs, filt):
    out = "masters/mv4_this_time_its_real_16x9.mp4"
    cmd = ["ffmpeg", "-y"]
    for inp in inputs:
        cmd += ["-i", inp]
    cmd += ["-i", "track.mp3"]
    cmd += ["-filter_complex", filt,
            "-map", "[vout]", "-map", f"{len(inputs)}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            "-movflags", "+faststart", "-video_track_timescale", "24",
            out]
    return cmd, out


if __name__ == "__main__":
    plan, tfs = build_plan()
    print(f"pieces: {len(plan)}  (takes probed: {len(tfs)})")
    for p in plan:
        print(f"  {p[5]:12} {p[0]:14} sf={p[1]:3} ef={p[2]:3} w={p[3]:.3f} out={p[4]}f")
    inputs, filt = build_filter(plan)
    cmd, out = build_cmd(inputs, filt)
    print("\nffmpeg inputs:", len(inputs), " filter chars:", len(filt))
    r = subprocess.run(cmd, cwd=PROJ, capture_output=True, text=True)
    print(r.stdout[-2000:] if r.stdout else "")
    if r.returncode != 0:
        print(r.stderr[-4000:], file=sys.stderr)
        sys.exit(r.returncode)
    print("BUILD OK ->", out)
