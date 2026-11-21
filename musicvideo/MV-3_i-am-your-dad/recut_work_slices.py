#!/usr/bin/env python3
"""Slice re-transcription for burst-drop takes (full-clip Whisper drops
later quiet bursts; QC precedent: slice recheck recovers them).

Slices (start offsets added back to word times):
  s22_t1 2.5s, s32_t1 2.0s, s33_t1 2.0s, s24_t2 2.0s,
  s25_t1 2.5s, s25_t2 2.0s, s35_t1 3.0s, s35_t2 3.5s
Output: recut_work/measure/<take>_slice.json
"""
import json, os, subprocess, wave as _wave
import numpy as _np

PROJ = os.path.dirname(os.path.abspath(__file__))
TAKES = os.path.join(PROJ, "takes")
OUT = os.path.join(PROJ, "recut_work", "measure")

SLICES = [
    ("mv3_s22_t1.mp4", 2.5), ("mv3_s32_t1.mp4", 2.0), ("mv3_s33_t1.mp4", 2.0),
    ("mv3_s24_t2.mp4", 2.0), ("mv3_s25_t1.mp4", 2.5), ("mv3_s25_t2.mp4", 2.0),
    ("mv3_s35_t1.mp4", 3.0), ("mv3_s35_t2.mp4", 3.5),
]

def main():
    from faster_whisper import WhisperModel
    model = WhisperModel("base", device="cpu", compute_type="int8")
    for fn, off in SLICES:
        out_path = os.path.join(OUT, fn.replace(".mp4", "_slice.json"))
        if os.path.exists(out_path):
            print(f"skip {fn} slice (done)", flush=True)
            continue
        wav = os.path.join(OUT, fn.replace(".mp4", "_slice.wav"))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(off),
                        "-i", os.path.join(TAKES, fn), "-ac", "1",
                        "-ar", "16000", "-vn", wav], check=True)
        with _wave.open(wav) as wf:
            frames = wf.readframes(wf.getnframes())
        audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
        segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
        segs, words = [], []
        for seg in segments:
            segs.append({"start": round(seg.start + off, 2),
                         "end": round(seg.end + off, 2), "text": seg.text.strip()})
            for w in (seg.words or []):
                txt = w.word.strip().lower().strip(".,!?\"'’")
                if txt:
                    words.append([txt, round(w.start + off, 2),
                                  round(w.end + off, 2)])
        json.dump({"file": fn, "slice_offset": off, "segments": segs,
                   "words": words}, open(out_path, "w"), indent=1)
        os.remove(wav)
        print(f"{fn} slice@{off}: {len(words)} words: "
              f"{[(w, t0, t1) for w, t0, t1 in words]}", flush=True)
    print("SLICES DONE", flush=True)

if __name__ == "__main__":
    main()
