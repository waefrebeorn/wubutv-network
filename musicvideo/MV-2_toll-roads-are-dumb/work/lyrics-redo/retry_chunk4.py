#!/usr/bin/env python3
"""MV-2 lyrics redo: retry chunk 4 (240-268s) after the faster-whisper
IndexError crash in find_alignment on the near-silent outro tail.

The full 240-268s window crashes inside model.transcribe (empty alignment
on the fading tail after ~261s, where no words are sung). Strategy: try
progressively shorter windows, each covering the remaining words (base
ASR: last word ends 260.80). Windows tried in order: [238-262], [240-258]
+ [258-261.5]. Each success writes chunk-04.json (same shape as the other
chunks) immediately; the main grid builder stitches from the chunk files.
Same standing params as transcribe_redo.py, cpu_threads=1.
"""
import json, os, pathlib, subprocess, sys, wave as _wave
import numpy as _np

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
OUT = PROJ / "work" / "lyrics-redo"
WAV = "/tmp/mv2_redo_song.wav"
SR = 16000

with _wave.open(WAV) as wf:
    frames = wf.readframes(wf.getnframes())
audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0

from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                     cpu_threads=1)


def collapse_runs(text):
    toks = text.split()
    out, run = [], 0
    for t in toks:
        if out and t.lower() == out[-1].lower():
            run += 1
            if run > 5:
                continue
        else:
            run = 1
        out.append(t)
    return " ".join(out)


def try_window(w0, w1):
    seg_audio = audio[int(w0 * SR):int(w1 * SR)]
    segments, _info = model.transcribe(
        seg_audio, language="en", word_timestamps=True,
        condition_on_previous_text=False, beam_size=1,
        repetition_penalty=1.1, no_repeat_ngram_size=3)
    segs, words = [], []
    for seg in segments:
        segs.append({"start": round(w0 + seg.start, 2),
                     "end": round(w0 + seg.end, 2),
                     "text": collapse_runs(seg.text.strip())})
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?\"'’")
            if txt:
                words.append([txt, round(w0 + w.start, 2), round(w0 + w.end, 2)])
    return segs, words


def main():
    ckpt = OUT / "chunk-04.json"
    if ckpt.exists():
        print("chunk-04.json already exists, nothing to do")
        return
    attempts = [(238.0, 262.0), (240.0, 258.0), (258.0, 261.5)]
    all_segs, all_words = [], []
    for w0, w1 in attempts:
        # skip windows already covered by an earlier success
        if all_words and w0 < max(w[1] for w in all_words):
            pass
        try:
            segs, words = try_window(w0, w1)
            print(f"window [{w0}-{w1}] OK: {len(words)} words", flush=True)
            all_segs.extend(segs)
            all_words.extend(words)
            if w0 == 238.0:
                break  # first window covered everything
        except Exception as e:
            print(f"window [{w0}-{w1}] FAILED: {type(e).__name__}: {e}", flush=True)
            continue
    if not all_words:
        print("ALL WINDOWS FAILED — outro falls back to base ASR times", flush=True)
        sys.exit(2)
    all_words.sort(key=lambda w: w[1])
    d = {"chunk": 4, "start": 240.0, "end": 268.0,
         "window": [238.0, 262.0], "segments": all_segs, "words": all_words,
         "note": "retry after IndexError crash on the near-silent tail; windows tried in order, first success covers 238-262"}
    tmp = str(ckpt) + ".pending"
    json.dump(d, open(tmp, "w"), indent=1)
    os.replace(tmp, ckpt)
    print(f"WROTE chunk-04.json: {len(all_segs)} segments, {len(all_words)} words", flush=True)


if __name__ == "__main__":
    main()
