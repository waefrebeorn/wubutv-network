#!/usr/bin/env python3
"""Transcribe the 5 MDX vocal-stem excerpts with faster-whisper
large-v3-turbo (same standing method as the mix backbone) and re-offset
word times to song time. Each stem writes its JSON immediately.
"""
import json, sys, wave
import numpy as np
from faster_whisper import WhisperModel

ROOT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons/work/lyrics-redo"
STEMS = [("head", 0.0), ("c1tail", 59.0), ("bridge", 130.0),
         ("fc", 179.0), ("outro", 214.0)]


def load_wav(path):
    with wave.open(path, "rb") as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(n)
    if sw == 2:
        a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    elif sw == 4:
        a = np.frombuffer(raw, dtype=np.int32).astype(np.float32) / 2147483648.0
    else:
        raise ValueError("sampwidth %d" % sw)
    if ch > 1:
        a = a.reshape(-1, ch).mean(axis=1)
    return a


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
                         cpu_threads=2, num_workers=1)
    print("model loaded", flush=True)
    for name, off in STEMS:
        wav = f"{ROOT}/stems/{name}_16k.wav"
        out_path = f"{ROOT}/song_words_{name}_stem.json"
        audio = load_wav(wav)
        segments, info = model.transcribe(
            audio, word_timestamps=True, language="en", vad_filter=False,
            beam_size=1, condition_on_previous_text=False,
            repetition_penalty=1.1, no_repeat_ngram_size=3)
        words, segs = [], []
        for s in segments:
            segs.append({"start": round(s.start + off, 3),
                         "end": round(s.end + off, 3), "text": s.text.strip()})
            for w in (s.words or []):
                words.append({"word": w.word.strip(),
                              "start": round(w.start + off, 3),
                              "end": round(w.end + off, 3),
                              "prob": round(w.probability, 3)})
            print(f"[{name}] seg {s.start+off:.2f}-{s.end+off:.2f}: {s.text.strip()[:80]}", flush=True)
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
