#!/usr/bin/env python3
"""Intake ASR: faster-whisper large-v3-turbo, house lyrics config.
Usage: intake_asr.py PROJ [PROJ ...]  — skips projects with valid SONG_WORDS.json.
Writes asr_words.json (segments+words) and SONG_WORDS.json (flat word list).
"""
import json, os, sys

import numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel

def load_wav(path):
    """PyAV in this env rejects faster-whisper's decode kwargs — feed numpy."""
    sr, data = wavfile.read(path)
    assert sr == 16000, sr
    y = data.astype(np.float32)
    if np.abs(y).max() > 1.5:
        y = y / 32768.0
    if y.ndim > 1:
        y = y[:, 0]
    return y

def valid(p):
    try:
        with open(p) as f:
            d = json.load(f)
        return isinstance(d, list) and len(d) > 0
    except Exception:
        return False

def main():
    projs = sys.argv[1:]
    model = None
    for proj in projs:
        sw = os.path.join(proj, "SONG_WORDS.json")
        if valid(sw):
            print(f"SKIP {proj} (SONG_WORDS.json valid)", flush=True)
            continue
        wav = os.path.join(proj, "work", "track16k.wav")
        if model is None:
            model = WhisperModel("large-v3-turbo", device="cpu",
                                 compute_type="int8", cpu_threads=2)
        segments, info = model.transcribe(
            load_wav(wav), word_timestamps=True, vad_filter=False,
            condition_on_previous_text=False)
        seg_out, flat = [], []
        for s in segments:  # consume generator fully
            words = []
            for w in (s.words or []):
                wd = {"word": w.word, "start": round(w.start, 3),
                      "end": round(w.end, 3),
                      "probability": round(w.probability, 4)}
                words.append(wd)
                flat.append(wd)
            seg_out.append({"start": round(s.start, 3), "end": round(s.end, 3),
                            "text": s.text, "words": words})
        with open(os.path.join(proj, "asr_words.json"), "w") as f:
            json.dump({"language": info.language,
                       "duration": round(info.duration, 3),
                       "segments": seg_out}, f, indent=1)
        with open(sw, "w") as f:
            json.dump(flat, f, indent=1)
        if flat:
            print(f"DONE {proj}: {len(flat)} words, first {flat[0]['word']!r}@{flat[0]['start']}, "
                  f"last {flat[-1]['word']!r}@{flat[-1]['end']}", flush=True)
        else:
            print(f"DONE {proj}: 0 words (instrumental?)", flush=True)

if __name__ == "__main__":
    main()
