#!/usr/bin/env python3
"""MV-2 lyrics redo: re-extract song words with faster-whisper large-v3-turbo.

Standing method (MV lyrics pipeline): large-v3-turbo, int8, cpu_threads=2,
NO VAD (fatal on chant), numpy-array input, pinned "en",
condition_on_previous_text=False, beam 1, repetition_penalty 1.1,
no_repeat_ngram 3, collapse runs >5. Word timestamps are the timing
authority. Chunked 60s + 2s overlap (transcribe_recordings pattern) with
per-chunk atomic checkpoints so a daemon restart / VM reboot resumes
instead of restarting. Stitch = time-boundary split on word middles;
words within +/-0.5s of a chunk boundary are flagged for review.
Output: work/lyrics-redo/SONG_WORDS_v3turbo.json {segments, words}
(words: [text_lower_stripped, t0, t1] like the old SONG_WORDS.json,
 plus raw segment text preserved in segments[].text).
Temp wav is unique to this run (/tmp/mv2_redo_song.wav) — never shared.
"""
import json, os, pathlib, subprocess, sys, wave as _wave
import numpy as _np

PROJ = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
OUT = PROJ / "work" / "lyrics-redo"
OUT.mkdir(parents=True, exist_ok=True)
WAV = "/tmp/mv2_redo_song.wav"
CHUNK = 60.0
OVERLAP = 2.0

subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(PROJ / "track.mp3"),
                "-ac", "1", "-ar", "16000", WAV], check=True)
with _wave.open(WAV) as wf:
    frames = wf.readframes(wf.getnframes())
audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
SR = 16000
total = len(audio) / SR
print(f"audio: {len(audio)} samples ({total:.1f}s)", flush=True)

from faster_whisper import WhisperModel
# cpu_threads=1: sibling lyrics-redo coordinators (MV-4/5/6) already hold
# ~1.9GB each for their own large-v3-turbo; keep this process lean.
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8",
                     cpu_threads=1)

def collapse_runs(text):
    # collapse runs >5 of the same word (standing rule)
    toks = text.split()
    out = []
    run = 0
    for t in toks:
        if out and t.lower() == out[-1].lower():
            run += 1
            if run > 5:
                continue
        else:
            run = 1
        out.append(t)
    return " ".join(out)

n_chunks = int(total // CHUNK) + (1 if total % CHUNK > 0 else 0)
all_words, all_segs, boundary_review = [], [], []
for ci in range(n_chunks):
    cstart, cend = ci * CHUNK, min((ci + 1) * CHUNK, total)
    ckpt = OUT / f"chunk-{ci:02d}.json"
    if ckpt.exists():
        d = json.load(open(ckpt))
        print(f"chunk {ci} [{cstart:.0f}-{cend:.0f}] REUSED ({len(d['words'])} words)", flush=True)
    else:
        w0 = max(0.0, cstart - OVERLAP)
        w1 = min(total, cend + OVERLAP)
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
        d = {"chunk": ci, "start": cstart, "end": cend,
             "window": [w0, w1], "segments": segs, "words": words}
        tmp = str(ckpt) + ".pending"
        json.dump(d, open(tmp, "w"), indent=1)
        os.replace(tmp, ckpt)
        print(f"chunk {ci} [{cstart:.0f}-{cend:.0f}] done ({len(words)} words)", flush=True)
    # stitch: keep words whose middle is inside this chunk's span
    for w in d["words"]:
        mid = (w[1] + w[2]) / 2
        if cstart - 1e-6 <= mid < cend - 1e-6 or (ci == n_chunks - 1 and mid <= cend):
            all_words.append(w)
            for b in [cstart, cend]:
                if abs(mid - b) < 0.5:
                    boundary_review.append([w[0], w[1], w[2], f"near chunk boundary {b:.0f}s"])
    for s in d["segments"]:
        if cstart - 1e-6 <= s["start"] < cend - 1e-6 or (ci == n_chunks - 1 and s["start"] <= cend):
            all_segs.append(s)

all_words.sort(key=lambda w: w[1])
json.dump({"segments": all_segs, "words": all_words,
           "boundary_review": boundary_review,
           "model": "large-v3-turbo", "chunk_seconds": CHUNK, "overlap": OVERLAP},
          open(OUT / "SONG_WORDS_v3turbo.json", "w"), indent=1)
print(f"WROTE SONG_WORDS_v3turbo.json: {len(all_segs)} segments, "
      f"{len(all_words)} words, {len(boundary_review)} boundary-review words", flush=True)
