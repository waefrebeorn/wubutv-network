#!/usr/bin/env python3
"""MV-5 v3 assembly: corrected master from the v2 plan as amended.

Changes vs v2 (work/assembly_fit_mv5_v4.json, build_v3_plan.py):
- S07 L15: s07_t2 at uniform warp 0.5234375 (playback 1.91x, DISCLOSED
  out-of-band warp — parent decision; L15 is structural for per-line
  generation, pace floor ~2.2-2.6s/line; a closed-mouth cover under a sung
  line is banned by the user's 2026-11-06 law). Measured word-start
  offsets: max +0.113s, median 0.027s — inside the +/-0.50s working band.
- S21 bridge L82-L89: beat-matched montage from volley-14 clips (warp 1.0,
  cuts on line boundaries, GIRL-first alternation). s21_t7 NOT used.
- s28_t5 DISCARDED, s07_t3 unused, s21_t7 unused — none in the plan.
- Everything else copies the v2 plan verbatim. Total 4954 frames.
- Captions captions_16x9_v3.ass (byte-identical to v2's 437-event file —
  the song grid is unchanged) + "~ WuBu ~" corner bug burned in.
- Audio: track.mp3 (md5 verified before muxing) as the sole master audio;
  clip audio dropped. Output: masters/mv5_easy_now_easy_now_16x9_v4.mp4,
  1280x720, 24fps, 4954 frames, 206.400s, h264 + AAC 48kHz, faststart.
"""
import hashlib, json, os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v4.json")))
SCENES = FIT["scenes"]
TOTAL_FRAMES = FIT["total_frames"]  # 4954
FPS = 24
TRACK_MD5 = "0c1bcafa568547e2d4fa36e133ad3626"
OUT = "masters/mv5_easy_now_easy_now_16x9_v4.mp4"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTDIR = "/usr/share/fonts/truetype/dejavu"

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    got = md5(os.path.join(PROJ, "track.mp3"))
    assert got == TRACK_MD5, f"track.mp3 md5 {got} != {TRACK_MD5}"
    print(f"track.mp3 md5 OK: {got}", flush=True)
    blob = json.dumps(FIT)
    for banned in ("mv5_s28_t5", "mv5_s07_t3", "mv5_s21_t7"):
        assert banned not in blob, f"{banned} in v3 plan!"
    print("banned takes absent from plan: s28_t5 / s07_t3 / s21_t7", flush=True)

    pieces = []  # (take, sf, ef, w, out_f, scene, kind)
    for sc in SCENES:
        for p in FIT["plan"][sc]:
            pieces.append((p["take"], p["sf"], p["ef"], p["warp"], p["out"], sc, p["kind"]))
    total = sum(p[4] for p in pieces)
    assert total == TOTAL_FRAMES, f"pieces sum {total} != {TOTAL_FRAMES}"
    print(f"pieces: {len(pieces)}  total frames: {total}", flush=True)

    inputs, parts = [], []
    for idx, (take, sf, ef, w, out_f, sc, kind) in enumerate(pieces):
        inputs.append(f"takes/{take}.mp4")
        exp = round((ef - sf) * w)
        pad = max(0, out_f - exp + 1)
        v = (f"[{idx}:v]trim=start_frame={sf}:end_frame={ef},"
             f"setpts=PTS-STARTPTS,setpts={w:.4f}*PTS,fps={FPS},")
        if pad:
            v += f"tpad=stop_mode=clone:stop_duration={pad / FPS:.4f},"
        v += f"trim=end_frame={out_f},setpts=PTS-STARTPTS[v{idx}];"
        parts.append(v)
    n = len(pieces)
    concat = "".join(f"[v{i}]" for i in range(n)) + \
        f"concat=n={n}:v=1:a=0,trim=end_frame={TOTAL_FRAMES},setpts=PTS-STARTPTS"
    bug = (f",drawtext=fontfile={FONT}:text='~ WuBu ~':"
           "fontsize=26:fontcolor=#FFC61E:x=w-tw-28:y=h-th-22:"
           "box=1:boxcolor=black@0.55:boxborderw=14")
    subs = f",subtitles=captions_16x9_v3.ass:fontsdir={FONTDIR}"
    filt = "".join(parts) + concat + bug + subs + "[vout]"

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
            OUT]
    print(f"ffmpeg inputs: {len(inputs)}  filter chars: {len(filt)}", flush=True)
    for p in pieces:
        if p[5] in ("S07", "S21"):
            print(f"  {p[5]:5} {p[6]:18} {p[0]:14} sf={p[1]:3} ef={p[2]:3} "
                  f"w={p[3]:.4f} out={p[4]}f", flush=True)
    r = subprocess.run(cmd, cwd=PROJ, capture_output=True, text=True)
    print(r.stdout[-2000:] if r.stdout else "")
    if r.returncode != 0:
        print(r.stderr[-4000:], file=sys.stderr)
        sys.exit(r.returncode)
    print("BUILD OK ->", OUT)

if __name__ == "__main__":
    main()
