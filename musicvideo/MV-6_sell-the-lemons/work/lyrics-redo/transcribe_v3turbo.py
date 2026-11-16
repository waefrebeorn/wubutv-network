#!/usr/bin/env python3
"""MV-6 lyrics redo: faster-whisper large-v3-turbo full-clip transcription.

Standing method (lyrics pipeline): int8, cpu_threads=2, NO VAD (fatal on
chant), numpy-array input (stdlib wave -> numpy; PyAV cannot decode paths),
pinned "en", condition_on_previous_text=False, beam 1,
repetition_penalty 1.1, no_repeat_ngram 3, collapse runs >5.
Audio: track.mp3 decoded to 16k mono wav by ffmpeg (deterministic).
Writes work/lyrics-redo/song_words_v3turbo.json (words + segments).
"""
import json, sys, wave
import numpy as np
from faster_whisper import WhisperModel

ROOT = "/home/hatch/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons"
WAV = ROOT + "/work/lyrics-redo/track_16k.wav"
OUT = ROOT + "/work/lyrics-redo/song_words_v3turbo.json"


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
    """Collapse runs of >max_run identical consecutive words to max_run."""
    out, run, prev = [], 0, None
    for w in words:
        key = w["word"].lower()
        run = run + 1 if key == prev else 1
        prev = key
        if run <= max_run:
            out.append(w)
    return out


def main():
    audio = load_wav(WAV)
    print("audio samples:", len(audio), "sr 16000, dur", len(audio) / 16000.0, flush=True)
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                         cpu_threads=2, num_workers=1)
    print("model loaded", flush=True)
    segments, info = model.transcribe(
        audio, word_timestamps=True, language="en", vad_filter=False,
        beam_size=1, condition_on_previous_text=False,
        repetition_penalty=1.1, no_repeat_ngram_size=3)
    words, segs = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3),
                     "text": s.text.strip()})
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3),
                          "end": round(w.end, 3), "prob": round(w.probability, 3)})
        print(f"seg {s.start:.2f}-{s.end:.2f}: {s.text.strip()[:90]}", flush=True)
    n_before = len(words)
    words = collapse_runs(words)
    # drop degenerate stamps (end==start at track tail)
    words = [w for w in words if not (w["end"] <= w["start"])]
    out = {"track": "track.mp3", "model": "large-v3-turbo",
           "language": info.language, "duration": round(len(audio) / 16000.0, 3),
           "n_words": len(words), "n_words_before_collapse": n_before,
           "words": words, "segments": segs}
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    print("words:", len(words), "segments:", len(segs), flush=True)
    print("first:", words[:5], flush=True)
    print("last:", words[-5:], flush=True)


if __name__ == "__main__":
    main()
