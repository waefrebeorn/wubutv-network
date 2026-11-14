#!/usr/bin/env python3
"""MV-5 v5 assembly (Q10 repair).

Changes vs v4 (work/assembly_fit_mv5_v5.json, build_v5_plan.py):
- S01 intro rebuilt per-word (leader = riding s02_t1, not a freeze; I01/I02/I04
  split so no word lands >0.30s off the grid).
- S02: all riding covers (v4's wrong-words inserts removed); pre-I09 cover
  is s03_t1 f96-115 + s01_t1 f171-176 (S13 owns s03_t1 f115-120).
- S04: fresh take q10_s04 (L01-L04) + s04_t1 L05; L04 split per-word
  ("begin" stretched warp 1.75 + tail cover for the held word).
- S06: L11 is a montage cover (s06_t1 tail + s04_t1 gap, both mouth-closed);
  L12 is the KEEP girl insert s06_t2 in 4 pieces.
- S07: L13/L14 per-line re-anchor; L15 is the restaged KEEP take
  q10_s07_l15 (girl alone, One->51.24 exact); L16 is a montage cover
  (I08/L104/S07-L16 takes were integrity-blocked, never re-fired).
- S11: L40 rebuilt — head ("And the tide tapping") is a cover, tail
  ("time with our feet") is sung at warp 1.105 (v4 put "Time" 2.05s early).
- S12: L41/L42 re-anchored (girl mouth closed during CAT's L42);
  L43 is the KEEP take q10_s12_l43; L44 is a 3-part cover.
- S17: P1 warp 1.11, L69 cover (mouth-closed, NOT a singing insert),
  L70 warp 1.32, P2 warp 1.4667.
- S20: warp 0.50 (breeze ends 156.99 < L81 head 157.02).
- S23: P1 warp 1.2574, L96 re-anchored (No->174.44).
- S24: rebuilt on true 3-pair s24_t1 words (pair 3 unused); L98/L100 covers.
- S27: L109 is a cover (s06_t2 tail + s28_t2 tail, both mouth-closed);
  s28_t1 L110a REMOVED (v4 put the CAT's L110 mouth over the GIRL's L109).
- S28: L110 is s28_t1 f0-57 (moved here from v4 S27) + tail cover.
- L104 stays v4 picture (girl sings the hook; CAT's lead line mouth-less —
  the CAT take was integrity-blocked). S25/S26 verbatim.
- Captions work/lyrics-redo/mv5_kinetic_redo.ass (548 events, lyrics-redo
  grid) + "~ WuBu ~" corner bug burned in.
- Audio: track.mp3 (md5 verified before muxing) as the sole master audio;
  clip audio dropped. Output: masters/mv5_easy_now_easy_now_16x9_v5.mp4,
  1280x720, 24fps, 4954 frames, 206.417s, h264 + AAC 48kHz, faststart.
"""
import hashlib, json, os, subprocess, sys

PROJ = os.path.dirname(os.path.abspath(__file__))
FIT = json.load(open(os.path.join(PROJ, "work", "assembly_fit_mv5_v5.json")))
SCENES = FIT["scenes"]
TOTAL_FRAMES = FIT["total_frames"]  # 4954
FPS = 24
TRACK_MD5 = "0c1bcafa568547e2d4fa36e133ad3626"
OUT = "masters/mv5_easy_now_easy_now_16x9_v5.mp4"
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
    subs = f",subtitles=work/lyrics-redo/mv5_kinetic_redo.ass:fontsdir={FONTDIR}"
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
