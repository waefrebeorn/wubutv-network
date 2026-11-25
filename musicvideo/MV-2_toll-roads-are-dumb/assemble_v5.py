#!/usr/bin/env python3
"""MV-2 v5 prompt-grounded assembly (2026-11-02, user correction 07:26 EST).

Rules (V5_DESIGN.md):
1. Anchors = fresh take word times -> song word times for the scene's OWN
   line only, in order. No cross-line LCS, no +-12s window, NO noise-merge
   dropping, NO visible-mouth shifting of the first anchor.
2. A scene's vocal segment runs first prompted take word -> last prompted
   take word (+ at most 0.3s rest, capped by the next vocal start). It ends
   there; NEVER swept across seconds it is not singing.
3. Gaps filled ONLY with non-singing footage: the next take's pre-vocal
   choreography (if it contains no singing -- S03's pre-vocal chorus is
   EXCLUDED), the previous take's post-vocal footage at natural speed, a
   frozen frame, or a word-correct REUSE segment (a kept take singing the
   exact repeated line, disclosed). Never a stretched mouth, never
   another line's vocal.
4. S27 cutaway outro: take post-vocal only (2.96-10.0) warped to
   260.80-268.01. Never its 0-2.96 vocal over silence.
5. Holds/leaders built -an; every concat input stream-checked (video-only
   clips, -an on segment outputs). Song audio untouched. Captions + bug
   as in v4.

Interval modes (per warp interval take [a,b] -> song [A,B],
factor = (B-A)/(b-a)):
- factor in [0.4, 2.5]: setpts warp (v4 style).
- factor > 2.5 (would be slow-mo mouth): play take [a,b] at natural
  speed from A, then FREEZE the take frame at b for the remainder.
  Never a slow-mo mouth.
- factor < 0.4 (fast squeeze): warp to fit, FLAGGED in the report.
  Only expected case: S21's zero-duration Whisper burst (song words
  332-338 all at 205.20), spread over the real window [204.24, 205.20].

Reuse segments (word-correct repeats, disclosed in CUTLIST_V5.json):
R1 S06 Pay -> 237-246, R2 S07 We've -> 247-252, R3 S07 Toe -> 253-256,
R4 S07 Toe -> 258-261, R5 S06 Fast -> 262-265, R6 S20 toll -> 324-327,
R7 S19 fast -> 328-331, R8 S07 We've -> 353-358, R9 S06 Fast -> 133-136,
R10 S19 fast -> 366-373, R11 S01 Yeah -> 383.
"""
import json, os, subprocess, sys

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb")
TAKES = os.path.join(PROJ, "takes")
WORK = os.path.join(PROJ, "masters_work_v5")
MASTERS = os.path.join(PROJ, "masters")
TRACK = os.path.join(PROJ, "track.mp3")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TOTAL = 268.01
ORDER = [f"S{i:02d}" for i in range(1, 28)]

# take word times for reuse sources: {scene_take: [(word, start, end)]}
REUSE_SRC = {
    "S06": json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]["S06"]["take_words"],
    "S07": json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]["S07"]["take_words"],
    "S19": json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]["S19"]["take_words"],
    "S20": json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]["S20"]["take_words"],
    "S01": json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]["S01"]["take_words"],
}
REUSE_TAKE = {"S06": "mv2_s06_t2.mp4", "S07": "mv2_s07_t2.mp4",
              "S19": "mv2_s19_t2.mp4", "S20": "mv2_s20_t2.mp4",
              "S01": "mv2_s01_t4.mp4"}
# (label, src_scene, [(take_idx, song_idx)...])
REUSE = [
    ("R1-Pay", "S06", [(9, 237), (10, 238), (11, 239), (12, 240), (13, 242), (14, 243), (15, 244), (16, 245), (17, 246)]),
    ("R2-Weve", "S07", [(0, 247), (1, 248), (2, 249), (3, 251), (4, 252)]),
    ("R3-Toe", "S07", [(5, 253), (6, 254), (7, 255), (8, 256)]),
    ("R4-Toe", "S07", [(5, 258), (6, 259), (7, 260), (8, 261)]),
    ("R5-Fast", "S06", [(1, 262), (2, 263), (3, 264), (4, 265)]),
    ("R6-toll", "S20", [(0, 324), (1, 325), (2, 326), (3, 327)]),
    ("R7-fast", "S19", [(0, 328), (1, 329), (2, 330), (3, 331)]),
    ("R8-Weve", "S07", [(0, 353), (1, 354), (2, 355), (3, 357), (4, 358)]),
    ("R9-Fast", "S06", [(1, 133), (2, 134), (3, 135), (4, 136)]),
    ("R10-fast", "S19", [(0, 366), (1, 367), (2, 368), (3, 369), (4, 371), (5, 372), (6, 373)]),
    ("R11-Yeah", "S01", [(0, 383)]),
]
PRE_VOCAL_EXCLUDED = {"S03"}  # leading chorus is singing, never gap filler


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FAILED:", " ".join(cmd)); print(r.stderr[-3000:]); sys.exit(1)
    return r


def ffprobe_streams(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "stream=codec_type", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return r.stdout.strip().split()


class Builder:
    def __init__(self):
        self.clips = []          # ordered clip files (video-only, -an)
        self.report = {"segments": [], "flags": []}
        self.n = 0
        self.prev_end = 0.0      # master time at end of last clip
        self.prev_take = None    # take file of last vocal/reuse content
        self.prev_take_pos = 0.0  # take time at prev_end
        self.prev_clip = None    # last clip file (for freeze frames)

    def out(self, tag):
        self.n += 1
        return os.path.join(WORK, f"v5_{self.n:03d}_{tag}.mp4")

    def note(self, seg):
        self.report["segments"].append(seg)

    def add_clip(self, path, dur, take=None, take_pos=None):
        streams = ffprobe_streams(path)
        assert "video" in streams, f"{path} has no video stream"
        assert "audio" not in streams, f"{path} carries audio, refusing (v3 lesson): {path}"
        self.clips.append(path)
        self.prev_end = round(self.prev_end + dur, 3)
        if take is not None:
            self.prev_take, self.prev_take_pos = take, take_pos
        self.prev_clip = path

    def freeze(self, dur, tag):
        """Freeze last frame of prev_clip (or first frame of a take for leader)."""
        assert dur > 0.01, f"freeze of {dur}s requested"
        o = self.out(tag)
        run(["ffmpeg", "-v", "error", "-y", "-i", self.prev_clip, "-vf",
             f"trim=end_frame=1,setpts=PTS-STARTPTS,loop=loop=-1:size=1:start=0,"
             f"trim=end={dur:.3f},fps=24,format=yuv420p",
             "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an", o])
        start = self.prev_end
        self.add_clip(o, dur)
        self.note({"type": "freeze", "master": [round(start, 2), round(self.prev_end, 2)],
                   "tag": tag})

    def natural(self, take, t0, dur, tag):
        """Play take [t0, t0+dur] at natural speed, video-only."""
        o = self.out(tag)
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(TAKES, take),
             "-vf", f"trim=start={t0:.3f}:end={t0 + dur:.3f},setpts=PTS-STARTPTS,"
             f"fps=24,format=yuv420p",
             "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an", o])
        start = self.prev_end
        self.add_clip(o, dur, take=take, take_pos=t0 + dur)
        self.note({"type": "natural", "take": take, "take_span": [round(t0, 2), round(t0 + dur, 2)],
                   "master": [round(start, 2), round(self.prev_end, 2)], "tag": tag})

    def warped(self, take, points, tag, label):
        """Warp take through (take_t, song_t) points. Points must be
        strictly increasing in both coordinates. Returns master span."""
        pts = [(round(a, 3), round(b, 3)) for a, b in points]
        for i in range(len(pts) - 1):
            assert pts[i + 1][0] > pts[i][0] and pts[i + 1][1] > pts[i][1], \
                f"{label} non-monotonic warp interval {pts[i]} -> {pts[i+1]}"
        parts, ins = [], []
        for i in range(len(pts) - 1):
            a, A = pts[i]; b, B = pts[i + 1]
            di, do = b - a, B - A
            factor = do / di
            if factor > 2.5:
                # slow-stretch guard: natural speed + freeze remainder
                # NOTE (2026-11-02 v5 fix): the freeze frame MUST be picked
                # by frame index, not by time+end_frame=1 -- end_frame is an
                # absolute stream frame number, so start=<time>:end_frame=1
                # selected nothing and the first render lost ~11.8s of
                # freeze time, drifting every later onset. Frame rate is
                # applied once after concat, not per piece (per-piece fps
                # rounded every interval up to a frame and accumulated).
                self.report["flags"].append(
                    f"{label}: interval take {a:.2f}-{b:.2f} -> song {A:.2f}-{B:.2f} "
                    f"factor {factor:.2f} > 2.5: played natural + froze frame at {b:.2f}")
                fi = int(b * 24)
                parts.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS,"
                             f"format=yuv420p[v{i}a]")
                parts.append(f"[0:v]trim=start_frame={fi}:end_frame={fi + 1},"
                             f"setpts=PTS-STARTPTS,"
                             f"loop=loop=-1:size=1:start=0,trim=end={do - di:.3f},"
                             f"format=yuv420p[v{i}b]")
                ins += [f"[v{i}a]", f"[v{i}b]"]
            else:
                if factor < 0.4:
                    self.report["flags"].append(
                        f"{label}: FAST interval take {a:.2f}-{b:.2f} -> song {A:.2f}-{B:.2f} "
                        f"factor {factor:.2f} < 0.4 (squeezed to fit)")
                parts.append(f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS,"
                             f"setpts=PTS*{factor:.4f},format=yuv420p[v{i}]")
                ins.append(f"[v{i}]")
        filt = ";".join(parts) + ";" + "".join(ins) + \
            f"concat=n={len(ins)}:v=1:a=0,fps=24,format=yuv420p[out]"
        o = self.out(tag)
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(TAKES, take),
             "-filter_complex", filt, "-map", "[out]", "-c:v", "libx264",
             "-crf", "18", "-preset", "fast", "-an", o])
        start = self.prev_end
        dur = pts[-1][1] - pts[0][1]
        self.add_clip(o, dur, take=take, take_pos=pts[-1][0])
        self.note({"type": "warped", "take": take, "label": label,
                   "master": [round(start, 2), round(self.prev_end, 2)],
                   "points": pts})
        return start, self.prev_end


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(MASTERS, exist_ok=True)
    match = json.load(open(os.path.join(PROJ, "WORD_MATCH_V5.json")))["scenes"]
    song = json.load(open(os.path.join(PROJ, "SONG_WORDS_BASE.json")))
    # scene vocal spans
    vocal = {}
    for sc in ORDER:
        m = match[sc]
        if not m["anchors"]:
            continue  # S27, handled separately
        first_ti, first_si = m["anchors"][0]
        last_ti, last_si = m["anchors"][-1]
        # vocal start: first anchor's song onset; if that song word is
        # zero-duration (S21 burst), walk back to the previous real word end
        j = first_si
        while song[j]["t1"] == song[j]["t0"] and j > 0:
            j -= 1
        vs = song[j]["t1"] if song[first_si]["t1"] == song[first_si]["t0"] \
            else song[first_si]["t0"]
        vocal[sc] = {"take": m["take"], "take_words": m["take_words"],
                     "anchors": m["anchors"], "start": vs,
                     "last_song_end": song[last_si]["t1"],
                     "last_take_end": m["take_words"][last_ti][2]}
    vocal_scenes = [sc for sc in ORDER if sc in vocal]
    for idx, sc in enumerate(vocal_scenes):
        nxt = vocal[vocal_scenes[idx + 1]]["start"] \
            if idx + 1 < len(vocal_scenes) else TOTAL
        # S27 window start is S26's last word end; next vocal start after S26 is 260.80
        if sc == "S26":
            nxt = 260.80
        vocal[sc]["end"] = min(vocal[sc]["last_song_end"] + 0.3, nxt)
    # reuse segments with song spans
    reuses = []
    for label, src, pairs in REUSE:
        tw = REUSE_SRC[src]
        pts = []
        for ti, si in pairs:
            pts.append((tw[ti][1], song[si]["t0"]))
        last_ti, last_si = pairs[-1]
        pts.append((tw[last_ti][2], song[last_si]["t1"]))
        reuses.append({"label": label, "take": REUSE_TAKE[src], "points": pts,
                       "start": pts[0][1], "end": pts[-1][1]})
    reuses.sort(key=lambda r: r["start"])

    b = Builder()
    # leader: freeze S01 first frame until its first word
    s01_take = vocal["S01"]["take"]
    b.prev_clip = None
    o = b.out("leader")
    run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(TAKES, s01_take),
         "-vf", "trim=end_frame=1,setpts=PTS-STARTPTS,loop=loop=-1:size=1:start=0,"
         f"trim=end={vocal['S01']['start']:.3f},fps=24,format=yuv420p",
         "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-an", o])
    b.clips.append(o); b.prev_end = vocal["S01"]["start"]; b.prev_clip = o
    b.prev_take, b.prev_take_pos = s01_take, 0.0
    b.note({"type": "freeze", "master": [0.0, round(vocal["S01"]["start"], 2)], "tag": "leader"})

    def fill_gap(target, why):
        """Fill [prev_end, target] with reuse segments, then previous
        take post-vocal at natural speed, then freeze. Never overshoots."""
        guard = 0
        while b.prev_end < target - 0.01 and guard < 40:
            guard += 1
            # next reuse fully or partly inside the gap?
            nxt_r = None
            for r in reuses:
                if r["start"] >= b.prev_end - 0.01 and r["start"] < target - 0.01 \
                        and r["end"] <= target + 0.01:
                    nxt_r = r; break
            if nxt_r is not None:
                if nxt_r["start"] > b.prev_end + 0.01:
                    fill_gap(nxt_r["start"], why + ">pre-reuse")
                b.warped(nxt_r["take"], nxt_r["points"], "reuse", nxt_r["label"])
                continue
            remain = target - b.prev_end
            if b.prev_take is not None and b.prev_take_pos < 10.0 - 0.01:
                d = min(remain, 10.0 - b.prev_take_pos)
                b.natural(b.prev_take, b.prev_take_pos, d, "postvocal")
            else:
                b.freeze(remain, "hold")
        if b.prev_end < target - 0.01:
            b.freeze(target - b.prev_end, "hold-tail")

    for sc in ORDER:
        if sc == "S27":
            # cutaway outro: post-vocal only
            fill_gap(260.80, "S27-lead")
            assert abs(b.prev_end - 260.80) < 0.05, f"S27 lead ends {b.prev_end}"
            b.warped("mv2_s27_t2.mp4", [(2.96, 260.80), (10.0, TOTAL)], "outro", "S27-cutaway")
            continue
        v = vocal[sc]
        # pre-vocal choreography (natural) if usable and non-singing
        first_take_start = v["take_words"][v["anchors"][0][0]][1]
        if sc not in PRE_VOCAL_EXCLUDED and first_take_start > 0.01:
            want_start = v["start"] - first_take_start
            if want_start > b.prev_end + 0.01:
                fill_gap(want_start, f"{sc}-pre")
            if b.prev_end < v["start"] - 0.01:
                avail = v["start"] - b.prev_end
                take_from = first_take_start - avail
                assert take_from >= -0.01
                b.natural(v["take"], max(0.0, take_from), avail, f"{sc}-prevocal")
        if b.prev_end < v["start"] - 0.01:
            fill_gap(v["start"], f"{sc}-lead")
        assert abs(b.prev_end - v["start"]) < 0.05, \
            f"{sc} vocal should start {v['start']}, timeline at {b.prev_end}"
        # warp points: anchors (take onset -> song onset), with
        # zero-duration song words collapsed onto the real window
        pts = []
        prev_real_end = None
        zero_run = False
        for ti, si in v["anchors"]:
            w = song[si]
            if w["t1"] == w["t0"]:
                if not zero_run:
                    base = prev_real_end if prev_real_end is not None else v["start"]
                    pts.append((v["take_words"][ti][1], base))
                    b.report["flags"].append(
                        f"{sc}: zero-duration song word {si} ({w['word']}) collapsed: "
                        f"take {v['take_words'][ti][1]:.2f} -> song {base:.2f} (burst window)")
                    zero_run = True
                continue
            zero_run = False
            pts.append((v["take_words"][ti][1], w["t0"]))
            prev_real_end = w["t1"]
        rest = v["end"] - v["last_song_end"]
        assert 0.0 <= rest <= 0.31, f"{sc} rest {rest}"
        pts.append((v["last_take_end"] + rest, v["end"]))
        b.warped(v["take"], pts, f"{sc}-vocal", sc)
    assert abs(b.prev_end - TOTAL) < 0.05, f"timeline ends {b.prev_end}, want {TOTAL}"
    lst = os.path.join(WORK, "concat_v5.txt")
    with open(lst, "w") as f:
        for p in b.clips:
            f.write(f"file '{p}'\n")
    video = os.path.join(WORK, "video_v5_16x9.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", video])
    srt = os.path.join(PROJ, "captions_v2.srt")
    bug = (f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=32:fontcolor=0xFFC61E:"
           f"x=w-tw-24:y=h-th-24:shadowcolor=0x000000:shadowx=2:shadowy=2")
    out16 = os.path.join(MASTERS, "mv2_toll_roads_are_dumb_v5_16x9.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", TRACK, "-i", srt,
         "-filter_complex", f"[0:v]{bug}[v]", "-map", "[v]", "-map", "1:a",
         "-map", "2:s", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
         "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
         "-movflags", "+faststart", "-t", f"{TOTAL}", out16])
    json.dump(b.report, open(os.path.join(PROJ, "CUTLIST_V5.json"), "w"), indent=1)
    print("V5 MASTER DONE", out16)
    print("segments:", len(b.report["segments"]), "flags:", len(b.report["flags"]))
    for fl in b.report["flags"]:
        print("FLAG:", fl)


if __name__ == "__main__":
    main()
