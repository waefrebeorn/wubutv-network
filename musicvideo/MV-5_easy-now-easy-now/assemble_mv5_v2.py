#!/usr/bin/env python3
"""MV-5 v2 assembly: corrected retimed master from the audit re-time plan.

Method (WORD-SYNC, MV-4 precedent):
- Per-scene placement from work/assembly_fit_mv5_v2.json (build_v2_plan.py:
  per-line least-squares fits of take word starts -> v2 song word starts;
  grey warps where the fit band forces them; structural scenes as
  closed-mouth cover + captions, never a mouth-sung slot).
- Segment boundaries = plan scene starts (partition of 0..206.40s); every
  scene's pieces sum EXACTLY to its segment frames (total 4954).
- Exact frame counts: after the setpts warp + fps, each piece is padded
  with cloned last frames (tpad, +1 frame slack) and trimmed to exactly
  out_f — the MV-4 lesson applied per piece.
- The one pre-word freeze is the S01 leader (frame 0 held 40f before the
  first word at 1.66s — MV-3 re-cut precedent); no frozen frame while
  words play anywhere else.
- Audio: track.mp3 (md5 verified before muxing) as the sole master audio;
  clip audio dropped. Captions (captions_16x9_v2.ass, 437 events, line-block
  + per-word cadmium highlight) + "~ WuBu ~" corner bug burned in.
  Output: masters/mv5_easy_now_easy_now_16x9_v2.mp4, 1280x720, 24fps,
  4954 frames, 206.400s, h264 + AAC 48kHz, faststart.
"""
import hashlib, json, os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v2.json")))
SCENES = FIT["scenes"]
TOTAL_FRAMES = FIT["total_frames"]  # 4954
FPS = 24
TRACK_MD5 = "0c1bcafa568547e2d4fa36e133ad3626"
OUT = "masters/mv5_easy_now_easy_now_16x9_v2.mp4"
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
    print(f"track.mp3 md5 OK: {got}")

    pieces = []  # (take, sf, ef, w, out_f, scene, kind)
    for sc in SCENES:
        for p in FIT["plan"][sc]:
            pieces.append((p["take"], p["sf"], p["ef"], p["warp"], p["out"], sc, p["kind"]))
    total = sum(p[4] for p in pieces)
    assert total == TOTAL_FRAMES, f"pieces sum {total} != {TOTAL_FRAMES}"
    print(f"pieces: {len(pieces)}  total frames: {total}")

    inputs, parts = [], []
    for idx, (take, sf, ef, w, out_f, sc, kind) in enumerate(pieces):
        inputs.append(f"takes/{take}.mp4")
        # expected warped frames; pad with cloned last frames (+1 slack)
        # so the trim always has >= out_f to cut from.
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
    subs = f",subtitles=captions_16x9_v2.ass:fontsdir={FONTDIR}"
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
    print(f"ffmpeg inputs: {len(inputs)}  filter chars: {len(filt)}")
    for p in pieces:
        print(f"  {p[5]:5} {p[6]:16} {p[0]:14} sf={p[1]:3} ef={p[2]:3} "
              f"w={p[3]:.3f} out={p[4]}f")
    r = subprocess.run(cmd, cwd=PROJ, capture_output=True, text=True)
    print(r.stdout[-2000:] if r.stdout else "")
    if r.returncode != 0:
        print(r.stderr[-4000:], file=sys.stderr)
        sys.exit(r.returncode)
    print("BUILD OK ->", OUT)

if __name__ == "__main__":
    main()
