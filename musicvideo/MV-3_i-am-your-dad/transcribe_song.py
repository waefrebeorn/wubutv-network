"""MV-3 song transcription: faster-whisper base, word timestamps, language=en.

Input: track.mp3 (md5 4948827344208de31df17dd9d2e52799, 354.816s).
Method per the MV-2 QC stack: ffmpeg to mono 16k WAV, numpy array input
to WhisperModel("base", cpu, int8), word_timestamps=True.
Output: SONG_WORDS.json {segments: [{start, end, text}], words: [[word, t0, t1], ...]}
Words lowercased, punctuation stripped, RAW (no mishear normalization).
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-3_i-am-your-dad"
wav = "/tmp/mv3_song.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(proj / "track.mp3"),
                "-ac", "1", "-ar", "16000", wav], check=True)
with _wave.open(wav) as wf:
    frames = wf.readframes(wf.getnframes())
audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
print(f"audio samples: {len(audio)} ({len(audio)/16000:.1f}s)", flush=True)

from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
segs, words = [], []
for seg in segments:
    segs.append({"start": round(seg.start, 2), "end": round(seg.end, 2),
                 "text": seg.text.strip()})
    for w in (seg.words or []):
        txt = w.word.strip().lower().strip(".,!?\"'’")
        if txt:
            words.append([txt, round(w.start, 2), round(w.end, 2)])
    print(f"{seg.start:7.2f}-{seg.end:7.2f}  {seg.text.strip()}", flush=True)
json.dump({"segments": segs, "words": words},
          open(proj / "SONG_WORDS.json", "w"), indent=1)
print(f"wrote SONG_WORDS.json: {len(segs)} segments, {len(words)} words")
