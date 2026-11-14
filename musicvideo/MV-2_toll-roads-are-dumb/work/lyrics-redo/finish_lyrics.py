#!/usr/bin/env python3
"""MV-2 lyrics redo: finish — encode the new master from the v7 base.

Same recipe as masters_work_v7/finish_v7.py, only the caption layer changes:
  silent video  masters_work_v7/v7_silent.mp4 (verified 6432f, caption-free)
  captions      work/lyrics-redo/mv2_kinetic_redo.ass (new corrected grid)
  bug           drawtext '~ WuBu ~' (same as v7)
  audio         track.mp3 as SOLE master audio (AAC 192k, never stream-copy)
Master: masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4
  libx264 CRF 18 preset medium, yuv420p 1280x720 24fps, faststart.
Chat:   masters/mv2_toll_roads_are_dumb_v7_16x9_lyrics_chat.mp4
  854x480 crf 23, audio copied untouched from the master, faststart, <=50MB.
NEVER overwrites the v7 or v6 master. Writes outputs_lyrics.json.
"""
import hashlib
import json
import pathlib
import subprocess

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
WORK = PROJ / "work" / "lyrics-redo"
SILENT = PROJ / "masters_work_v7" / "v7_silent.mp4"
MASTERS = PROJ / "masters"
MASTER = MASTERS / "mv2_toll_roads_are_dumb_v7_16x9_lyrics.mp4"
CHAT = MASTERS / "mv2_toll_roads_are_dumb_v7_16x9_lyrics_chat.mp4"


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
    assert SILENT.exists(), "v7_silent.mp4 missing"
    assert (WORK / "mv2_kinetic_redo.ass").exists(), ".ass missing"
    # safety: the v7 master must still exist (we never overwrite it)
    assert (MASTERS / "mv2_toll_roads_are_dumb_v7_16x9.mp4").exists(), "v7 master missing"
    bug = ("drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
           "text='~ WuBu ~':fontsize=30:fontcolor=#FFC61E:x=w-tw-20:y=20:"
           "shadowcolor=black:shadowx=2:shadowy=2")
    sh(["ffmpeg", "-v", "error", "-y",
        "-i", str(SILENT), "-i", str(PROJ / "track.mp3"),
        "-vf", "subtitles=%s,%s" % (WORK / "mv2_kinetic_redo.ass", bug),
        "-map", "0:v", "-map", "1:a",
        "-c:v", "libx264", "-crf", "18", "-preset", "medium",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
        "-movflags", "+faststart", str(MASTER)])
    print("master:", MASTER, flush=True)
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(MASTER),
        "-vf", "scale=854:480",
        "-c:v", "libx264", "-crf", "23", "-preset", "veryfast",
        "-c:a", "copy",
        "-movflags", "+faststart", str(CHAT)])
    print("chat:", CHAT, flush=True)
    info = {}
    for name, path in [("master", MASTER), ("chat", CHAT)]:
        info[name] = {"path": str(path), "md5": md5(path),
                      "size": path.stat().st_size, "probe": ffprobe(path),
                      "frames": frame_count(path)}
        print(name, "md5", info[name]["md5"], "size", info[name]["size"],
              "frames", info[name]["frames"], flush=True)
    assert info["master"]["frames"] == 6432, info["master"]["frames"]
    assert info["chat"]["frames"] == 6432, info["chat"]["frames"]
    assert info["chat"]["size"] <= 50 * 1024 * 1024, info["chat"]["size"]
    (WORK / "outputs_lyrics.json").write_text(json.dumps(info, indent=1))
    print("outputs recorded", flush=True)


if __name__ == "__main__":
    main()
