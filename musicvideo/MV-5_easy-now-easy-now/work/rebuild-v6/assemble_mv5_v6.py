#!/usr/bin/env python3
"""MV-5 v6 assembly: fit work/rebuild-v6/assembly_fit_mv5_v6.json (0 errors,
4954 frames) -> masters/mv5_easy_now_easy_now_16x9_v6.mp4 + chat copy.

Mechanics per the house chain (cf. work/lyrics-redo/assemble_mv5_lyrics.py):
per-piece trim -> setpts warp -> fps 24 -> tpad clone-pad to exact out
frames -> concat -> texture pass (grain/vignette/saturation) -> ~ WuBu ~
bug -> burn work/lyrics-redo/mv5_kinetic_redo.ass -> mux track.mp3 as sole
audio (AAC 192k/48k/stereo). S22's piece carries the 7.2 blackout-snap
grade (fade dip). House: CRF 18, 1280x720, 24fps, exactly 4954 frames,
faststart. Chat copy: 854x480 crf 23, AAC copied, <=50MB.
"""
import hashlib, json, os, subprocess, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
V6 = os.path.join(PROJ, "work", "rebuild-v6")
FIT = json.load(open(os.path.join(V6, "assembly_fit_mv5_v6.json")))
TOTAL_FRAMES = FIT["total_frames"]
FPS = 24
TRACK_MD5 = "0c1bcafa568547e2d4fa36e133ad3626"
OUT = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v6.mp4")
CHAT = os.path.join(PROJ, "masters", "mv5_easy_now_easy_now_16x9_v6_chat.mp4")
ASS = os.path.join(PROJ, "work", "lyrics-redo", "mv5_kinetic_redo.ass")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONTDIR = "/usr/share/fonts/truetype/dejavu"
TAKESRC = os.path.join(V6, "takes")
TAKEDST = os.path.join(PROJ, "takes")

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def resolve_take(name):
    """fit name -> source mp4 in work/rebuild-v6/takes."""
    import glob
    direct = os.path.join(TAKESRC, name + ".mp4")
    if os.path.exists(direct):
        return direct
    if name.startswith("mv5_v6_"):
        stem = name[len("mv5_v6_"):].replace("_", "-")
        hits = glob.glob(os.path.join(TAKESRC, f"media-generation-mv5-v6-{stem}-0-*.mp4"))
        if len(hits) == 1:
            return hits[0]
    if name == "pilot_p2_cat":
        hits = glob.glob(os.path.join(TAKESRC, "media-generation-mv5-v6-p2-cat-hook-0-*.mp4"))
        if len(hits) == 1:
            return hits[0]
    raise SystemExit(f"cannot resolve take {name}")

def main():
    got = md5(os.path.join(PROJ, "track.mp3"))
    assert got == TRACK_MD5, f"track.mp3 md5 {got} != {TRACK_MD5}"
    print(f"track.mp3 md5 OK: {got}", flush=True)
    blob = json.dumps(FIT)
    for banned in ("mv5_v6_s25_cat\"", "mv5_v6_s09_duet", "pilot_p1", "pilot_p3"):
        assert banned not in blob, f"banned take in fit: {banned}"
    print("banned takes absent from fit: s25_cat(v1) / s09_duet / p1 / p3", flush=True)

    pieces = []
    for sc, sdata in FIT["scenes"].items():
        for p in sdata["pieces"]:
            pieces.append((p["take"], p["src"][0], p["src"][1], p["out"], sc, p["kind"]))
    total = sum(p[3] for p in pieces)
    assert total == TOTAL_FRAMES, f"pieces sum {total} != {TOTAL_FRAMES}"
    print(f"pieces: {len(pieces)}  total frames: {total}", flush=True)

    # register used takes into project takes/ under their fit names
    used = {}
    for take, *_ in pieces:
        if take not in used:
            src = resolve_take(take)
            dst = os.path.join(TAKEDST, take + ".mp4")
            if not os.path.exists(dst):
                subprocess.run(["cp", src, dst], check=True)
            used[take] = dst
    print(f"registered {len(used)} takes into project takes/", flush=True)

    inputs, parts = [], []
    for idx, (take, sa, sb, out_f, sc, kind) in enumerate(pieces):
        inputs.append(os.path.join(TAKEDST, take + ".mp4"))
        src_dur = sb - sa
        out_dur = out_f / FPS
        k = out_dur / src_dur  # setpts factor
        exp = round(src_dur * k * FPS)
        pad = max(0, out_f - exp + 1)
        v = (f"[{idx}:v]trim=start={sa:.3f}:end={sb:.3f},setpts=PTS-STARTPTS,"
             f"scale=1280:720:flags=lanczos,setsar=1,"
             f"setpts={k:.5f}*PTS,fps={FPS},")
        if sc == "S22":
            v += "fade=t=in:st=0:d=0.12,fade=t=out:st=1.05:d=0.17,"
        if pad:
            v += f"tpad=stop_mode=clone:stop_duration={pad / FPS:.4f},"
        v += f"trim=end_frame={out_f},setpts=PTS-STARTPTS[v{idx}];"
        parts.append(v)
    n = len(pieces)
    concat = "".join(f"[v{i}]" for i in range(n)) + \
        f"concat=n={n}:v=1:a=0,trim=end_frame={TOTAL_FRAMES},setpts=PTS-STARTPTS"
    texture = ",noise=alls=5:allf=t+u,vignette=angle=PI/5,eq=saturation=0.88:contrast=1.02"
    bug = (f",drawtext=fontfile={FONT}:text='~ WuBu ~':"
           "fontsize=26:fontcolor=#FFC61E:x=w-tw-28:y=h-th-22:"
           "box=1:boxcolor=black@0.55:boxborderw=14")
    subs = f",subtitles={ASS}:fontsdir={FONTDIR}"
    filt = "".join(parts) + concat + texture + bug + subs + "[vout]"

    cmd = ["ffmpeg", "-y"]
    for inp in inputs:
        cmd += ["-i", inp]
    cmd += ["-i", os.path.join(PROJ, "track.mp3")]
    cmd += ["-filter_complex", filt,
            "-map", "[vout]", "-map", f"{len(inputs)}:a",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
            "-movflags", "+faststart", "-video_track_timescale", "24",
            OUT]
    print(f"ffmpeg inputs: {len(inputs)}  filter chars: {len(filt)}", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-4000:], file=sys.stderr)
        sys.exit(r.returncode)
    print("HOUSE BUILD OK ->", OUT, flush=True)

    cmd2 = ["ffmpeg", "-y", "-i", OUT, "-vf", "scale=854:480:flags=lanczos",
            "-c:v", "libx264", "-preset", "medium", "-crf", "26",
            "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "copy",
            "-movflags", "+faststart", CHAT]
    r = subprocess.run(cmd2, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:], file=sys.stderr)
        sys.exit(r.returncode)
    size = os.path.getsize(CHAT) / 1e6
    print(f"CHAT BUILD OK -> {CHAT}  {size:.1f} MB", flush=True)
    assert size <= 50.0, "chat copy over 50MB"

if __name__ == "__main__":
    main()
