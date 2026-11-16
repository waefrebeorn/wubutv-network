#!/usr/bin/env python3
"""MV-5 lyrics redo — full-clip re-extraction (large-v3-turbo, standing method).

Method (tested, standing): faster-whisper large-v3-turbo, int8,
cpu_threads=2, NO VAD, numpy-array input (mono 16k), pinned "en",
condition_on_previous_text=False, beam 1, repetition_penalty 1.1,
no_repeat_ngram 3, word timestamps on.
"""
import json, sys, time
import numpy as np

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
OUT = PROJ + "/work/lyrics-redo/words_full_v3turbo.json"
LOG = PROJ + "/work/lyrics-redo/transcribe_full.log"

def log(msg):
    print(msg, flush=True)
    with open(LOG, "a") as f:
        f.write(f"{time.strftime('%H:%M:%S')} {msg}\n")

def decode_mono16k(path):
    import av
    c = av.open(path)
    stream = c.streams.audio[0]
    resampler = av.audio.resampler.AudioResampler(format="flt", layout="mono", rate=16000)
    chunks = []
    for frame in c.decode(stream):
        out = resampler.resample(frame)
        for o in out:
            # CRITICAL: planes[0] buffer is padded — slice to o.samples,
            # else the array inflates (was 240.8s for a 206.4s track).
            chunks.append(np.frombuffer(o.planes[0], dtype=np.float32)[:o.samples].copy())
    for o in (resampler.resample(None) or []):
        chunks.append(np.frombuffer(o.planes[0], dtype=np.float32)[:o.samples].copy())
    c.close()
    return np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.float32)

def main():
    t0 = time.time()
    log("decoding track.mp3 -> mono 16k numpy")
    audio = decode_mono16k(PROJ + "/track.mp3")
    log(f"audio: {len(audio)/16000:.2f}s, {len(audio)} samples")
    from faster_whisper import WhisperModel
    log("loading large-v3-turbo int8 (cpu_threads=2)")
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
    log("transcribing full clip (no VAD, word timestamps)")
    segments, info = model.transcribe(
        audio, language="en", word_timestamps=True, vad_filter=False,
        condition_on_previous_text=False, beam_size=1,
        repetition_penalty=1.1, no_repeat_ngram_size=3,
    )
    segs, words = [], []
    for s in segments:
        segs.append({"start": s.start, "end": s.end, "text": s.text})
        for w in (s.words or []):
            words.append({"word": w.word, "start": w.start, "end": w.end, "prob": w.probability})
    log(f"done: {len(segs)} segments, {len(words)} words in {time.time()-t0:.0f}s")
    with open(OUT, "w") as f:
        json.dump({"model": "large-v3-turbo", "compute_type": "int8",
                   "language": info.language, "language_probability": info.language_probability,
                   "duration": info.duration, "segments": segs, "words": words}, f, indent=1)
    log(f"wrote {OUT}")

if __name__ == "__main__":
    main()
