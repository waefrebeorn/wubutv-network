#!/usr/bin/env python3
"""MV-14 take-audio ASR — recreated 2026-11-11 after /tmp was cleared.
Proven config (from MV-11/13/14 intake): faster-whisper large-v3-turbo,
int8, cpu_threads=2, NO VAD, beam 1, numpy-array input (PyAV file-path
decode is broken with faster-whisper 1.2.1 + PyAV 19), pinned "en",
condition_on_previous_text=False, word timestamps on.
Usage: python3 mv14_take_asr.py work/qc_sNN_t1/audio.wav [...]
Prints one JSON object per file (segments + per-word times/probs).
"""
import sys
import json
import wave

import numpy as np
from faster_whisper import WhisperModel

MODEL = WhisperModel("large-v3-turbo", device="cpu",
                     compute_type="int8", cpu_threads=2)


def load_wav(path):
    with wave.open(path, "rb") as w:
        n = w.getnframes()
        raw = w.readframes(n)
        sr = w.getframerate()
        ch = w.getnchannels()
    audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        audio = audio.reshape(-1, ch).mean(axis=1)
    return audio, sr


def main(paths):
    for path in paths:
        audio, sr = load_wav(path)
        assert sr == 16000, f"{path}: sample rate {sr}, expected 16000"
        segments, _info = MODEL.transcribe(
            audio,
            language="en",
            beam_size=1,
            vad_filter=False,
            condition_on_previous_text=False,
            word_timestamps=True,
            compression_ratio_threshold=2.4,
            log_prob_threshold=-1.0,
            no_speech_threshold=0.6,
            repetition_penalty=1.1,
            no_repeat_ngram_size=3,
        )
        out = []
        for seg in segments:
            words = [
                {"word": w.word, "start": round(w.start, 2),
                 "end": round(w.end, 2), "prob": round(w.probability, 3)}
                for w in (seg.words or [])
            ]
            out.append({
                "start": round(seg.start, 2),
                "end": round(seg.end, 2),
                "text": seg.text.strip(),
                "avg_logprob": round(seg.avg_logprob, 3),
                "no_speech_prob": round(seg.no_speech_prob, 3),
                "words": words,
            })
        print(json.dumps({"file": path, "segments": out}, indent=1),
              flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
