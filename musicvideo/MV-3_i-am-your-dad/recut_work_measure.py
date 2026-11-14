#!/usr/bin/env python3
"""MV-3 re-cut stage 1: transcribe every take used in the cutlist.

Method (MV-2 QC stack + diagnostic): ffmpeg to mono 16k WAV per take
(never shared between runs), numpy-array input to faster-whisper base
(~/workspace/fw-venv), word_timestamps=True, language=en. Sequential
transcription only. Output: one JSON per take in recut_work/measure/.
"""
import json, os, subprocess, sys, wave as _wave
import numpy as _np

PROJ = os.path.dirname(os.path.abspath(__file__))
TAKES = os.path.join(PROJ, "takes")
OUT = os.path.join(PROJ, "recut_work", "measure")
os.makedirs(OUT, exist_ok=True)

FILES = [
    # 31 active keeps
    "mv3_s01_t2.mp4", "mv3_s02_t2.mp4", "mv3_s03_t1.mp4", "mv3_s06_t1.mp4",
    "mv3_s07_t1.mp4", "mv3_s08_t1.mp4", "mv3_s09_t1.mp4", "mv3_s10_t1.mp4",
    "mv3_s11_t2.mp4", "mv3_s12_t2.mp4", "mv3_s13_t1.mp4", "mv3_s14_t1.mp4",
    "mv3_s15_t1.mp4", "mv3_s16_t1.mp4", "mv3_s17_t1.mp4", "mv3_s18_t2.mp4",
    "mv3_s19_t1.mp4", "mv3_s20_t1.mp4", "mv3_s22_t1.mp4", "mv3_s23_t2.mp4",
    "mv3_s26_t1.mp4", "mv3_s27_t1.mp4", "mv3_s28_t3.mp4", "mv3_s29_t1.mp4",
    "mv3_s31_t1.mp4", "mv3_s32_t1.mp4", "mv3_s33_t1.mp4", "mv3_s34_t1.mp4",
    "mv3_s36_t2.mp4", "mv3_s38_t2.mp4", "mv3_s39_t1.mp4",
    # structural / decision video-cover takes
    "mv3_s04_t1.mp4", "mv3_s05_t1.mp4", "mv3_s21_t2.mp4", "mv3_s24_t2.mp4",
    "mv3_s25_t1.mp4", "mv3_s25_t2.mp4", "mv3_s30_t3.mp4", "mv3_s35_t1.mp4",
    "mv3_s35_t2.mp4", "mv3_s37_t1.mp4",
]

def main():
    from faster_whisper import WhisperModel
    model = WhisperModel("base", device="cpu", compute_type="int8")
    only = sys.argv[1:] or None
    for fn in FILES:
        if only and fn not in only:
            continue
        out_path = os.path.join(OUT, fn.replace(".mp4", ".json"))
        if os.path.exists(out_path):
            print(f"skip {fn} (done)", flush=True)
            continue
        wav = os.path.join(OUT, fn.replace(".mp4", ".wav"))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i",
                        os.path.join(TAKES, fn), "-ac", "1", "-ar", "16000",
                        "-vn", wav], check=True)
        with _wave.open(wav) as wf:
            frames = wf.readframes(wf.getnframes())
        audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
        segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
        segs, words = [], []
        for seg in segments:
            segs.append({"start": round(seg.start, 2), "end": round(seg.end, 2),
                         "text": seg.text.strip()})
            for w in (seg.words or []):
                txt = w.word.strip().lower().strip(".,!?\"'’")
                if txt:
                    words.append([txt, round(w.start, 2), round(w.end, 2)])
        json.dump({"file": fn, "segments": segs, "words": words},
                  open(out_path, "w"), indent=1)
        os.remove(wav)
        span = f"{words[0][1]}-{words[-1][2]}" if words else "NO WORDS"
        print(f"{fn}: {len(words)} words, span {span}", flush=True)
    print("ALL DONE", flush=True)

if __name__ == "__main__":
    main()
