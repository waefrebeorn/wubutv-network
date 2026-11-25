#!/usr/bin/env python3
"""MV-17 performed-word extraction: faster-whisper large-v3-turbo.

House lyrics pipeline config: large-v3-turbo, int8, cpu_threads=2,
NO VAD (fatal on chant), numpy-array input, pinned "en",
condition_on_previous_text=False, beam 1, repetition_penalty 1.1,
no_repeat_ngram 3. Chunked 60s + 2s overlap with per-chunk atomic
checkpoints; stitch = time-boundary split on word middles.
Output: work/analysis/SONG_WORDS.json {segments, words}
words: {word, start, end, prob}.
"""
import json, os, pathlib, subprocess, sys, wave as _wave
import numpy as _np

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery"
OUT = PROJ / "work" / "analysis"
OUT.mkdir(parents=True, exist_ok=True)
WAV = str(OUT / "mv17_16k.wav")
CHUNK = 60.0
OVERLAP = 2.0

if not os.path.exists(WAV):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(PROJ / "track.mp3"),
                    "-ac", "1", "-ar", "16000", WAV], check=True)
with _wave.open(WAV) as wf:
    frames = wf.readframes(wf.getnframes())
audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
SR = 16000
total = len(audio) / SR
print(f"audio: {len(audio)} samples ({total:.2f}s)", flush=True)

from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                     cpu_threads=2)

n_chunks = int(total // CHUNK) + (1 if total % CHUNK > 0 else 0)
all_words, all_segs = [], []
for ci in range(n_chunks):
    ckpt = OUT / f"asr_chunk{ci}.json"
    cstart, cend = ci * CHUNK, min((ci + 1) * CHUNK, total)
    if ckpt.exists():
        d = json.load(open(ckpt))
        all_words += d["words"]; all_segs += d["segments"]
        print(f"chunk {ci} checkpointed, skip", flush=True)
        continue
    lo = max(0.0, cstart - (OVERLAP if ci > 0 else 0.0))
    hi = min(total, cend + (OVERLAP if ci < n_chunks - 1 else 0.0))
    seg_audio = audio[int(lo * SR):int(hi * SR)]
    segments, info = model.transcribe(
        seg_audio, language="en", beam_size=1, word_timestamps=True,
        vad_filter=False, condition_on_previous_text=False,
        repetition_penalty=1.1, no_repeat_ngram_size=3)
    cwords, csegs = [], []
    for s in segments:
        st0, st1 = lo + s.start, lo + s.end
        csegs.append({"start": round(st0, 3), "end": round(st1, 3),
                      "text": s.text, "avg_logprob": round(s.avg_logprob, 3)})
        for w in (s.words or []):
            wt0, wt1 = lo + w.start, lo + w.end
            mid = (wt0 + wt1) / 2.0
            if cstart - 0.001 <= mid < cend + 0.001 or (ci == n_chunks - 1 and mid >= cstart):
                cwords.append({"word": w.word.strip().lower(),
                               "start": round(wt0, 3), "end": round(wt1, 3),
                               "prob": round(w.probability, 3)})
    tmp = str(ckpt) + ".tmp"
    json.dump({"words": cwords, "segments": csegs}, open(tmp, "w"))
    os.replace(tmp, ckpt)
    all_words += cwords; all_segs += csegs
    print(f"chunk {ci} [{cstart:.0f}-{cend:.0f}] words={len(cwords)}", flush=True)

all_words.sort(key=lambda w: w["start"])
out = {"duration": round(total, 3), "segments": all_segs, "words": all_words}
tmp = str(OUT / "SONG_WORDS.json") + ".tmp"
json.dump(out, open(tmp, "w"), indent=1)
os.replace(tmp, OUT / "SONG_WORDS.json")
print(f"DONE words={len(all_words)} segments={len(all_segs)}", flush=True)
