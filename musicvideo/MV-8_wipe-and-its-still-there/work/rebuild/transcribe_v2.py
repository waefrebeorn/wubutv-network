#!/usr/bin/env python3
"""MV-8 rebuild Stage 1 — re-transcribe the PERFORMED female vocal.
Two passes, both with word timestamps, both saved as they complete:
  A) medium model, no prompt, beam 5, VAD on — clean independent witness
  B) small model, initial_prompt = lyric sheet, beam 5, VAD on — identity witness
Input: work/track_16k.wav (proper 16 kHz decode; avoids the v1 48kHz bug).
Run with ~/workspace/fw-venv/bin/python. Outputs to work/rebuild/.
"""
import json, sys, os
from faster_whisper import WhisperModel
import soundfile as sf

PROJ = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there")
WAV = os.path.join(PROJ, "work", "track_16k.wav")
OUTDIR = os.path.join(PROJ, "work", "rebuild")

SHEET_PROMPT = (
    "Wipe and it's still there. Paper comes back dirty. Brown brown. Still there. "
    "Phantom residue stays. Sitting on the toilet. Wipe once. Still brown. Phantom. "
    "Wipe again. Still there. Never clean. Endless wipe forever. Still brown. "
    "Phantom wiper never stops. Wipe. STILL THERE! Brown brown. "
    "Paper comes back dirty. Brown brown. Still there. Phantom wipe. Endless wipe forever."
)

def run(model_name, out_path, initial_prompt=None, vad=True, beam=5):
    print(f"=== pass {model_name} prompt={'YES' if initial_prompt else 'no'} -> {out_path}", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8",
                         cpu_threads=4, num_workers=2)
    audio, _sr = sf.read(WAV, dtype="float32")
    if audio.ndim > 1:
        audio = audio[:, 0]
    kw = dict(word_timestamps=True, language="en", vad_filter=vad, beam_size=beam)
    if initial_prompt:
        kw["initial_prompt"] = initial_prompt
    segments, info = model.transcribe(audio, **kw)
    words, segs = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
        for w in (s.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 3),
                          "end": round(w.end, 3), "prob": round(w.probability, 3)})
    out = {"track": WAV, "model": model_name, "language": info.language,
           "duration": 187.2, "initial_prompt": bool(initial_prompt), "vad_filter": vad,
           "beam_size": beam, "n_words": len(words), "words": words, "segments": segs}
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"=== {model_name}: {len(words)} words, {len(segs)} segments", flush=True)
    print("first:", words[:4], flush=True)
    print("last:", words[-4:], flush=True)
    return out

# Pass B first (fast, small) so a baseline lands on disk early; then Pass A (medium).
run("small", os.path.join(OUTDIR, "SONG_WORDS_v2_small_prompted.json"),
    initial_prompt=SHEET_PROMPT)
run("medium", os.path.join(OUTDIR, "SONG_WORDS_v2_medium.json"))
print("ALL DONE", flush=True)
