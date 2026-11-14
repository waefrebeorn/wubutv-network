#!/usr/bin/env python3
"""MV-2 cheap lip sync + assembly (Slopcannon assemble.md).

For each active take: mine its generated audio for onset peaks (mouth-timing
map), pair them in order with Suno-track onset peaks inside the same scene
window (target map), build a clamped piecewise time-remap (segment speeds
0.8x-1.25x, slack redistributed so the scene keeps its exact song duration),
render the time-tweened scene, concat in song order, mux the Suno track as
sole master audio, add a subtitle caption track and the ~ WuBu ~ corner bug,
and emit 16:9 + 9:16 masters.
"""
import json, math, os, subprocess, sys, wave

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb")
TAKES = os.path.join(PROJ, "takes")
WORK = os.path.join(PROJ, "masters_work")
MASTERS = os.path.join(PROJ, "masters")
TRACK = os.path.join(PROJ, "track.mp3")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

ACTIVE = {  # scene -> (take file, song start, song end)
    "S01": ("mv2_s01_t2.mp4", 0, 10), "S02": ("mv2_s02_t3.mp4", 10, 20),
    "S03": ("mv2_s03_t2.mp4", 20, 30), "S04": ("mv2_s04_t3.mp4", 30, 40),
    "S05": ("mv2_s05_t2.mp4", 40, 50), "S06": ("mv2_s06_t2.mp4", 50, 60),
    "S07": ("mv2_s07_t1.mp4", 60, 70), "S08": ("mv2_s08_t1.mp4", 70, 80),
    "S09": ("mv2_s09_t1.mp4", 80, 90), "S10": ("mv2_s10_t1.mp4", 90, 100),
    "S11": ("mv2_s11_t1.mp4", 100, 110), "S12": ("mv2_s12_t1.mp4", 110, 120),
    "S13": ("mv2_s13_t1.mp4", 120, 130), "S14": ("mv2_s14_t1.mp4", 130, 140),
    "S15": ("mv2_s15_t1.mp4", 140, 150), "S16": ("mv2_s16_t1.mp4", 150, 160),
    "S17": ("mv2_s17_t1.mp4", 160, 170), "S18": ("mv2_s18_t1.mp4", 170, 180),
    "S19": ("mv2_s19_t1.mp4", 180, 190), "S20": ("mv2_s20_t1.mp4", 190, 200),
    "S21": ("mv2_s21_t1.mp4", 200, 210), "S22": ("mv2_s22_t1.mp4", 210, 220),
    "S23": ("mv2_s23_t1.mp4", 220, 230), "S24": ("mv2_s24_t1.mp4", 230, 240),
    "S25": ("mv2_s25_t1.mp4", 240, 250), "S26": ("mv2_s26_t1.mp4", 250, 260),
    "S27": ("mv2_s27_t1.mp4", 260, 268.01),
}
LYRICS = {  # scene -> caption line (from MV_PREPRO lyric column)
    "S01": "listen here, baby, shiny roads ain't what they seem",
    "S02": "build the toll roads, pay to roll, plazas stop then go",
    "S03": "cars slam brakes, back ends crash, NTSB worst on the map",
    "S04": "fast lanes, rich fly by, rest crawl, money flash by",
    "S05": "weave in weave out, speeds don't match, toll roads are dumb",
    "S06": "fast lanes make crashes, wrecks just come, pay to go faster, rest slow",
    "S07": "weaving and slamming, danger grows, toll roads are dumb, fast lanes make crashes",
    "S08": "they just keep coming",
    "S09": "express lanes look clean, merges get hot",
    "S10": "speed up cut over, somebody gets caught, paid side safer, free side takes hit",
    "S11": "crashes just move over, same old mess, Lexus lanes, money buys the clear",
    "S12": "poor folks sit in traffic, rich disappear, stop-and-go plazas, electronic helps a bit, split creates chaos",
    "S13": "toll roads are dumb, fast lanes make crashes, the wrecks just come",
    "S14": "pay to go faster, the rest of us slow, weaving and slamming, the danger grows",
    "S15": "toll roads are dumb, fast lanes make crashes, they just keep coming",
    "S16": "they just keep coming, sell you speed for a dollar and a dime",
    "S17": "road gets meaner every time, one lane flying, other stuck",
    "S18": "somebody's going to get it when timing's up, oh, toll roads are dumb",
    "S19": "fast lanes make crashes, wrecks just come, toll roads are dumb",
    "S20": "toll roads are dumb, fast lanes make crashes",
    "S21": "toll roads are dumb, fast lanes make crashes",
    "S22": "toll roads are dumb, fast lanes make crashes",
    "S23": "toll roads are dumb, fast lanes make crashes",
    "S24": "don't pay for the fast lane, honey, it ain't worth the crash",
    "S25": "toll roads are dumb, toll roads are dumb",
    "S26": "toll roads are dumb",
    "S27": "toll roads are dumb",
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(cmd)); print(r.stderr[-2000:]); sys.exit(1)
    return r

def decode_mono_wav(src, dst):
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", "16000",
         "-vn", dst])

def peaks(wav_path, t0, t1, min_sep=0.20):
    """Onset-ish peaks: RMS envelope local maxima above mean+0.5sd."""
    with wave.open(wav_path) as w:
        n = w.getnframes(); raw = w.readframes(n)
    import struct
    samples = struct.unpack("<%dh" % (len(raw) // 2), raw)
    sr = 16000; win = int(sr * 0.02)
    env = []
    for i in range(0, len(samples) - win, win):
        seg = samples[i:i + win]
        env.append(math.sqrt(sum(s * s for s in seg) / win))
    if not env: return []
    mean = sum(env) / len(env)
    sd = math.sqrt(sum((e - mean) ** 2 for e in env) / len(env))
    thr = mean + 0.5 * sd
    cands = []
    for i in range(1, len(env) - 1):
        if env[i] > thr and env[i] >= env[i - 1] and env[i] >= env[i + 1]:
            cands.append((i * 0.02, env[i]))
    out = []
    for t, v in cands:
        if t0 <= t <= t1 and (not out or t - out[-1] >= min_sep):
            out.append(round(t, 3))
        elif out and t - out[-1] < min_sep and v > 0:  # keep first in cluster
            pass
    return out

def remap_anchors(take_peaks, target_peaks, dur):
    """Pair peaks in order; clamp segment speeds; rescale to exact duration."""
    n = min(len(take_peaks), len(target_peaks))
    pairs = list(zip(take_peaks[:n], target_peaks[:n]))
    anchors_in = [0.0] + [p[0] for p in pairs] + [dur]
    anchors_out = [0.0] + [p[1] for p in pairs] + [dur]
    # Drop duplicate / non-increasing anchors
    clean_in, clean_out = [0.0], [0.0]
    for a, b in zip(anchors_in[1:], anchors_out[1:]):
        if a > clean_in[-1] and b > clean_out[-1]:
            clean_in.append(a); clean_out.append(b)
    if clean_in[-1] < dur:
        clean_in.append(dur); clean_out.append(dur)
    # Clamp speeds by adjusting out deltas, then rescale to exact duration
    for _ in range(2):
        deltas_in = [clean_in[i + 1] - clean_in[i] for i in range(len(clean_in) - 1)]
        deltas_out = []
        for i, d in enumerate(deltas_in):
            raw = clean_out[i + 1] - clean_out[i]
            speed = d / raw if raw > 0 else 1.0
            speed = min(1.25, max(0.8, speed))
            deltas_out.append(d / speed)
        total = sum(deltas_out)
        scale = dur / total if total > 0 else 1.0
        deltas_out = [d * scale for d in deltas_out]
        clean_out = [0.0]
        for d in deltas_out:
            clean_out.append(clean_out[-1] + d)
        clean_out[-1] = dur
    speeds = []
    for i in range(len(clean_in) - 1):
        di = clean_in[i + 1] - clean_in[i]; do = clean_out[i + 1] - clean_out[i]
        speeds.append(round(di / do, 3) if do > 0 else 1.0)
    return clean_in, clean_out, speeds, n

def main():
    os.makedirs(WORK, exist_ok=True); os.makedirs(MASTERS, exist_ok=True)
    suno_wav = os.path.join(WORK, "suno.wav")
    decode_mono_wav(TRACK, suno_wav)
    report = {}
    scene_files = []
    for sc in sorted(ACTIVE):
        fname, s0, s1 = ACTIVE[sc]
        dur = round(s1 - s0, 2)
        src = os.path.join(TAKES, fname)
        take_wav = os.path.join(WORK, sc + "_take.wav")
        decode_mono_wav(src, take_wav)
        tp = peaks(take_wav, 0, dur)
        sp = [round(p - s0, 3) for p in peaks(suno_wav, s0, s1)]
        ain, aout, speeds, npairs = remap_anchors(tp, sp, dur)
        report[sc] = {"take": fname, "song": [s0, s1], "take_peaks": tp,
                      "target_peaks": sp, "paired": npairs, "speeds": speeds}
        # Build per-scene filter: trim segments, setpts factor, concat
        parts, concat_ins = [], []
        for i in range(len(ain) - 1):
            di = ain[i + 1] - ain[i]; do = aout[i + 1] - aout[i]
            factor = do / di if di > 0 else 1.0
            parts.append(f"[0:v]trim=start={ain[i]:.3f}:end={ain[i+1]:.3f},"
                         f"setpts=PTS-STARTPTS,setpts=PTS*{factor:.4f},"
                         f"fps=24,format=yuv420p[v{i}]")
            concat_ins.append(f"[v{i}]")
        filt = ";".join(parts) + ";" + "".join(concat_ins) + \
               f"concat=n={len(ain)-1}:v=1:a=0[out]"
        out = os.path.join(WORK, sc + "_tween.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", filt,
             "-map", "[out]", "-c:v", "libx264", "-crf", "18", "-preset", "fast",
             "-an", out])
        scene_files.append(out)
        print(sc, fname, "paired", npairs, "speeds", speeds, flush=True)
    with open(os.path.join(PROJ, "LIPSYNC_REPORT.json"), "w") as f:
        json.dump(report, f, indent=1)
    # Concat list
    lst = os.path.join(WORK, "concat.txt")
    with open(lst, "w") as f:
        for p in scene_files:
            f.write("file '%s'\n" % p)
    video = os.path.join(WORK, "video_16x9.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", video])
    # SRT captions
    def ts(t):
        h, m = int(t // 3600), int((t % 3600) // 60); s = t % 60
        return "%02d:%02d:%06.3f" % (h, m, s)
    srt = os.path.join(WORK, "captions.srt")
    with open(srt, "w") as f:
        for i, sc in enumerate(sorted(ACTIVE), 1):
            _, s0, s1 = ACTIVE[sc]
            f.write("%d\n%s --> %s\n%s\n\n" % (i, ts(s0).replace(".", ","),
                                                ts(s1).replace(".", ","), LYRICS[sc]))
    bug16 = ("drawtext=fontfile=%s:text='~ WuBu ~':fontsize=30:fontcolor=0xFFC61E:"
             "x=w-tw-24:y=h-th-24:shadowcolor=0x000000:shadowx=2:shadowy=2" % FONT)
    out16 = os.path.join(MASTERS, "mv2_toll_roads_are_dumb_16x9.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", TRACK, "-i", srt,
         "-filter_complex", "[0:v]" + bug16 + "[v]",
         "-map", "[v]", "-map", "1:a", "-map", "2:s",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-c:a", "aac", "-b:a", "192k", "-c:s", "mov_text",
         "-metadata:s:s:0", "language=eng", "-t", "268.01", out16])
    # 9:16 blurred-pad reframe of the same cut
    pad = ("[0:v]split[a][b];[a]scale=720:1280:force_original_aspect_ratio=increase,"
           "crop=720:1280[g];[b]scale=720:1280,gblur=sigma=40[bg];"
           "[bg][g]overlay=(W-w)/2:(H-h)/2,drawtext=fontfile=%s:text='~ WuBu ~':"
           "fontsize=30:fontcolor=0xFFC61E:x=w-tw-24:y=h-th-24:shadowcolor=0x000000:"
           "shadowx=2:shadowy=2[v]" % FONT)
    out9 = os.path.join(MASTERS, "mv2_toll_roads_are_dumb_9x16.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", TRACK, "-i", srt,
         "-filter_complex", pad,
         "-map", "[v]", "-map", "1:a", "-map", "2:s",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-c:a", "aac", "-b:a", "192k", "-c:s", "mov_text",
         "-metadata:s:s:0", "language=eng", "-t", "268.01", out9])
    print("MASTERS DONE", out16, out9)

if __name__ == "__main__":
    main()
