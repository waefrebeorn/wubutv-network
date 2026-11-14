#!/usr/bin/env python3
"""Refinement pass: faster-whisper SMALL over song 0-30s only.
Goal: upgrade the [inferred] intro / V1 L1-L3 word times in LYRIC_TIMELINE.md.
Pass A: small, loudnormed head, no prompt. Pass B: small + initial_prompt (sheet lyrics).
Pass C: small, raw head + prompt (only if A and B hear no lyric words).
Writes work/head30_small_words.json with every pass's segments+words.
Run with the freeq venv python (has soundfile + faster-whisper):
  ~/workspace/freeq/venv/bin/python work/refine_head30.py
Audio is passed as a numpy array (the system python's PyAV cannot decode paths).
"""
import json
from faster_whisper import WhisperModel
import wave
import numpy as np

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
        a = a.reshape(-1, ch)[:, 0]
    return a


PROMPT = ("Bacon head on the stand. Sell the lemons, sell the lemons. "
          "I spawn in with the default hair, Bacon head, simple smile, no care. "
          "Start with the stand, one lemon at a time, Click the button, watch the cash climb.")
KEY = ["bacon", "lemon", "spawn", "stand", "sell", "hair", "smile", "click", "button", "cash"]


def load16k(path):
    return load_wav(path)


def run(model, audio, prompt=None):
    segments, _info = model.transcribe(
        audio, word_timestamps=True, language="en", vad_filter=False,
        beam_size=1, initial_prompt=prompt)
    segs, words = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3),
                          "end": round(w.end, 3), "prob": round(w.probability, 3)})
    return segs, words


def lyric_hits(words):
    return sum(1 for w in words if any(k in w["word"].lower() for k in KEY))


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4, num_workers=1)
    out = {"passes": []}
    norm = load16k("work/head30_norm.wav")
    raw = load16k("work/head30_raw.wav")

    segs, words = run(model, norm, None)
    out["passes"].append({"name": "A_small_norm_noprompt", "segments": segs, "words": words})
    print("pass A words:", len(words), "lyric hits:", lyric_hits(words), flush=True)

    segs, words = run(model, norm, PROMPT)
    out["passes"].append({"name": "B_small_norm_prompted", "segments": segs, "words": words})
    print("pass B words:", len(words), "lyric hits:", lyric_hits(words), flush=True)

    if max(lyric_hits(p["words"]) for p in out["passes"]) == 0:
        segs, words = run(model, raw, PROMPT)
        out["passes"].append({"name": "C_small_raw_prompted", "segments": segs, "words": words})
        print("pass C words:", len(words), "lyric hits:", lyric_hits(words), flush=True)

    with open("work/head30_small_words.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
