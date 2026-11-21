#!/usr/bin/env python3
"""v7 finish (Q6): mux master (silent video + untouched track.mp3 + captions
+ bug), build chat copy, verify everything.

Master: masters/mv2_toll_roads_are_dumb_v7_16x9.mp4 (1280x720/24fps,
exactly 6432 frames, h264 + 48kHz stereo AAC, faststart).
Chat: masters/mv2_toll_roads_are_dumb_v7_16x9_chat.mp4 (crf 26, audio
copied untouched from the master per Slopcannon stage 7).
NO 9:16 reframe (standing ONE 16:9 rule, 2026-11-05).
"""
import hashlib
import json
import pathlib
import subprocess
import sys

import numpy as _np

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
WORK = PROJ / "masters_work_v7"
MASTERS = PROJ / "masters"
MASTERS.mkdir(parents=True, exist_ok=True)


def sh(cmd):
    r = subprocess.run(cmd)
    if r.returncode != 0:
        raise SystemExit("FAILED: %s" % " ".join(cmd))


def ffprobe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration,size",
                          "-show_entries", "stream=codec_type,codec_name,width,height,"
                          "r_frame_rate,nb_frames,sample_rate,channels",
                          "-of", "json", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def frame_count(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                          "-select_streams", "v:0",
                          "-show_entries", "stream=nb_read_frames",
                          "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return int(out.strip())


def main():
    silent = WORK / "v7_silent.mp4"
    assert silent.exists(), "render the silent video first (assemble_v7.py)"
    master = MASTERS / "mv2_toll_roads_are_dumb_v7_16x9.mp4"
    bug = ("drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
           "text='~ WuBu ~':fontsize=30:fontcolor=#FFC61E:x=w-tw-20:y=20:"
           "shadowcolor=black:shadowx=2:shadowy=2")
    sh(["ffmpeg", "-v", "error", "-y",
        "-i", str(silent), "-i", str(PROJ / "track.mp3"),
        "-vf", "subtitles=%s,%s" % (WORK / "captions.ass", bug),
        "-map", "0:v", "-map", "1:a",
        "-c:v", "libx264", "-crf", "18", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", str(master)])
    print("master:", master)
    chat = MASTERS / "mv2_toll_roads_are_dumb_v7_16x9_chat.mp4"
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(master),
        "-c:v", "libx264", "-crf", "26", "-preset", "veryfast",
        "-c:a", "copy",
        "-movflags", "+faststart", str(chat)])
    print("chat:", chat)
    info = {}
    for name, path in [("master", master), ("chat", chat)]:
        info[name] = {"path": str(path), "md5": md5(path),
                      "size": path.stat().st_size, "probe": ffprobe(path),
                      "frames": frame_count(path)}
        print(name, "md5", info[name]["md5"], "size", info[name]["size"],
              "frames", info[name]["frames"])
    assert info["master"]["frames"] == 6432, info["master"]["frames"]
    assert info["chat"]["frames"] == 6432, info["chat"]["frames"]
    assert info["chat"]["size"] <= 50 * 1024 * 1024, info["chat"]["size"]
    (WORK / "outputs_v7.json").write_text(json.dumps(info, indent=1))
    print("outputs recorded")


def motion_audit(path, out_json):
    """Full-fps 160x90 grayscale consecutive-frame mean abs diff (v6 method)."""
    cmd = ["ffmpeg", "-v", "error", "-i", str(path),
           "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    fr = _np.frombuffer(raw, dtype=_np.uint8).reshape(n, 160 * 90).astype(_np.int16)
    diffs = _np.array([float(_np.mean(_np.abs(fr[i] - fr[i - 1]))) for i in range(1, n)])
    runs = []
    cur = 0
    start = 0
    for i, dval in enumerate(diffs):
        if dval < 0.5:
            if cur == 0:
                start = i
            cur += 1
        else:
            if cur >= 6:
                runs.append({"start_s": round(start / 24, 2),
                             "end_s": round((start + cur) / 24, 2),
                             "frames": cur,
                             "min_diff": round(float(diffs[start:start + cur].min()), 3)})
            cur = 0
    if cur >= 6:
        runs.append({"start_s": round(start / 24, 2),
                     "end_s": round((start + cur) / 24, 2),
                     "frames": cur,
                     "min_diff": round(float(diffs[start:start + cur].min()), 3)})
    res = {"frames": n, "mean_diff": round(float(diffs.mean()), 3),
           "frozen_seconds_lt_0_2": round(float((diffs < 0.2).sum()) / 24, 3),
           "longest_near_dup_run": max([r["frames"] for r in runs], default=0),
           "runs_ge_6f": runs}
    pathlib.Path(out_json).write_text(json.dumps(res, indent=1))
    print("motion audit:", res["mean_diff"], "mean;",
          res["frozen_seconds_lt_0_2"], "s frozen;",
          res["longest_near_dup_run"], "f longest near-dup;",
          len(runs), "runs >=6f")
    for r in runs:
        print("  run", r)
    return res


def cut_check():
    """Every MOUTH-involved cut must land on a word boundary or in silence."""
    cutlist = json.loads((WORK / "cutlist_v7.json").read_text())
    clips = cutlist["clips"]
    d = json.loads((PROJ / "SONG_WORDS_BASE.json").read_text())
    words = d["words"] if "words" in d else d
    bad = []
    for prev, cur in zip(clips, clips[1:]):
        t = prev["out1"]
        if prev["kind"] != "MOUTH" and cur["kind"] != "MOUTH":
            continue
        active = [w for w in words if w["t0"] - 0.02 < t < w["t1"] + 0.02]
        near = min([min(abs(t - w["t0"]), abs(t - w["t1"])) for w in words])
        if active and near > 0.15:
            bad.append({"t": t, "prev": prev["label"], "next": cur["label"],
                        "active_word": active[0]["word"], "near": round(near, 2)})
    print("mouth-cut violations:", len(bad))
    for b in bad:
        print("  ", b)
    return bad


def audio_agreement(master, track):
    """PCM correlation between the master audio and track.mp3 (full length,
    16kHz mono). The master re-encodes track.mp3 to AAC 192k; correlation
    should be >=0.998."""
    def pcm(path):
        cmd = ["ffmpeg", "-v", "error", "-i", str(path),
               "-ac", "1", "-ar", "16000", "-f", "f32le", "-"]
        raw = subprocess.run(cmd, capture_output=True, check=True).stdout
        return _np.frombuffer(raw, dtype=_np.float32)
    a = pcm(master)
    b = pcm(track)
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    a = a - a.mean()
    b = b - b.mean()
    corr = float((a * b).sum() / (_np.linalg.norm(a) * _np.linalg.norm(b)))
    print("audio agreement (full-length PCM corr):", round(corr, 6), "n=", n)
    return corr


if __name__ == "__main__":
    if "--motion" in sys.argv:
        motion_audit(MASTERS / "mv2_toll_roads_are_dumb_v7_16x9.mp4",
                     WORK / "motion_audit_v7.json")
    elif "--cuts" in sys.argv:
        cut_check()
    elif "--audio" in sys.argv:
        audio_agreement(MASTERS / "mv2_toll_roads_are_dumb_v7_16x9.mp4",
                        PROJ / "track.mp3")
    else:
        main()
