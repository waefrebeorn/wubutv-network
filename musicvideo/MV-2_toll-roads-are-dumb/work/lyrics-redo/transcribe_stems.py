#!/usr/bin/env python3
"""MV-2 lyrics redo: transcribe the 4 MDX vocal-stem excerpts with
faster-whisper large-v3-turbo and re-offset word times to song time.

Differs from the standing mix-backbone params in ONE place:
no_repeat_ngram_size=0 (not 3) — these spans hold real repeats/echoes,
so the anti-loop n-gram would suppress REAL words (it did in the mix
backbone: chunk 3 got 33 words vs base's 80). The stems are clean
isolated vocals, so the looping risk is low; outputs are validated
against the Suno lyric video's line structure before use.
Each stem writes its JSON immediately (resumable). cpu_threads=1: the
blade holds ~1.9 GB for the model; run only when >=2.5 GB is available.
"""
import json, os
import numpy as np
from faster_whisper import WhisperModel
from scipy.io import wavfile
from scipy.signal import resample_poly

ROOT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb/work/lyrics-redo"
STEMS = [("l34", 174.0), ("l21", 107.0), ("l17", 91.0), ("echo", 217.0)]


def load_16k_mono(path):
    sr, data = wavfile.read(path)
    assert sr == 44100, f"{path}: expected 44100, got {sr}"
    a = data.astype(np.float64)
    if data.dtype == np.int16:
        a = a / 32768.0
    if a.ndim == 2:
        a = a.mean(axis=1)
    return resample_poly(a, 16000, 44100).astype(np.float32)


def collapse_runs(words, max_run=5):
    out, run, prev = [], 0, None
    for w in words:
        key = w["word"].lower()
        run = run + 1 if key == prev else 1
        prev = key
        if run <= max_run:
            out.append(w)
    return out


def main():
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                         cpu_threads=1, num_workers=1)
    print("model loaded", flush=True)
    for name, off in STEMS:
        out_path = f"{ROOT}/song_words_{name}_stem.json"
        if os.path.exists(out_path):
            print(f"[{name}] already done, skip", flush=True)
            continue
        audio = load_16k_mono(f"{ROOT}/stems/{name}_vocals.wav")
        segments, info = model.transcribe(
            audio, word_timestamps=True, language="en", vad_filter=False,
            beam_size=1, condition_on_previous_text=False,
            repetition_penalty=1.1, no_repeat_ngram_size=0)
        words, segs = [], []
        for s in segments:
            segs.append({"start": round(s.start + off, 3),
                         "end": round(s.end + off, 3), "text": s.text.strip()})
            for w in (s.words or []):
                words.append({"word": w.word.strip(),
                              "start": round(w.start + off, 3),
                              "end": round(w.end + off, 3),
                              "prob": round(w.probability, 3)})
            print(f"[{name}] seg {s.start+off:.2f}-{s.end+off:.2f}: {s.text.strip()[:90]}", flush=True)
        words = collapse_runs(words)
        words = [w for w in words if w["end"] > w["start"]]
        out = {"stem": name, "offset": off, "model": "large-v3-turbo",
               "n_words": len(words), "words": words, "segments": segs}
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1)
        print(f"[{name}] words: {len(words)} segments: {len(segs)} -> {out_path}", flush=True)
    print("ALL STEMS DONE", flush=True)


if __name__ == "__main__":
    main()
