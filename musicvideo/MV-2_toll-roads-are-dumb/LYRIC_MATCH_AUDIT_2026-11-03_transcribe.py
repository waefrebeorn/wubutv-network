"""Fresh uniform dictation for the MV-2 viewing-cut lyric-match audit (2026-11-03).

Transcribes EVERY take used in masters_work_viewingcut/cutlist_working.json
with faster-whisper base, word timestamps, language=en — the same QC stack
as the volley QC scripts, but RAW words only: NO mishear normalization
(tall/told/toe/paid/tell/done classes are NOT folded), because this audit
is exactly about what the take actually sings vs what the song sings.

Output: TAKE_WORDS_AUDIT_2026-11-03.json
  {take_filename: [[word, t0, t1], ...]}  (word lowercased, punctuation stripped)
"""
import json, pathlib, subprocess, sys
import wave as _wave
import numpy as _np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
clips = json.load(open(proj / "masters_work_viewingcut/cutlist_working.json"))["clips"]
takes = sorted(set(c["take"] for c in clips))
print(f"takes to transcribe: {len(takes)}", flush=True)

from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
out = {}
for fname in takes:
    path = proj / "takes" / fname
    if not path.exists():
        print(f"MISSING {fname}", flush=True)
        out[fname] = None
        continue
    wav = f"/tmp/mv2_audit_{fname.replace('.mp4','')}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                    "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?\"'’")
            if txt:
                words.append([txt, round(w.start, 2), round(w.end, 2)])
    out[fname] = words
    print(f"{fname}: {len(words)} words: {' '.join(w for w, _, _ in words)}", flush=True)

json.dump(out, open(proj / "TAKE_WORDS_AUDIT_2026-11-03.json", "w"), indent=1)
print("wrote TAKE_WORDS_AUDIT_2026-11-03.json")
