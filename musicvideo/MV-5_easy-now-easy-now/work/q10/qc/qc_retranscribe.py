#!/usr/bin/env python3
"""Q10: full re-transcription of takes whose prompted JSONs look truncated
(s06_t1, s12_t1, s24_t1, s24_t3) — large-v3-turbo, lyrics venv.
Saves Q10_*_prompted.json (originals preserved)."""
import json
import numpy as np
from faster_whisper import WhisperModel

TAKES = [
    ("mv5_s06_t1", "Keys in your hand. You nodded at the waves like. Yeah, they already understand.",
     "Q10_S06_T1_prompted.json"),
    ("mv5_s12_t1", "Your laugh hit the air. I forgot the list, forgot the bills.",
     "Q10_S12_T1_prompted.json"),
    ("mv5_s24_t1", "Easy now, easy now, easy now, easy now",
     "Q10_S24_T1_prompted.json"),
    ("mv5_s24_t3", "Easy now, easy now, easy now, easy now",
     "Q10_S24_T3_prompted.json"),
]
BASE = "/home/hatch/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now"
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
for take, prompt, outname in TAKES:
    wav = f"{BASE}/work/q10/qc/take_wavs/{take}.wav"
    try:
        audio = np.fromfile(wav, dtype=np.int16).astype(np.float32) / 32768.0
    except FileNotFoundError:
        import subprocess
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{BASE}/takes/{take}.mp4",
                        "-ac", "1", "-ar", "16000", wav], check=True)
        audio = np.fromfile(wav, dtype=np.int16).astype(np.float32) / 32768.0
    print(f"== {take} {len(audio)/16000:.2f}s ==", flush=True)
    segments, info = model.transcribe(
        audio, language="en", word_timestamps=True, vad_filter=False,
        condition_on_previous_text=False, beam_size=1,
        repetition_penalty=1.1, no_repeat_ngram_size=0,
        initial_prompt=prompt)
    words = []
    for s in segments:
        print(f"  seg {s.start:.2f}-{s.end:.2f}: {s.text.strip()}", flush=True)
        for w in s.words:
            words.append({"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)})
    out = {"take": take, "prompt": f"Q10 full re-transcription large-v3-turbo (lyrics venv) 2026-11-13; prompt={prompt}",
           "take_dur": round(len(audio) / 16000, 3), "words": words}
    with open(f"{BASE}/work/assembly_take_words/{outname}", "w") as f:
        json.dump(out, f, indent=1)
    print(f"  wrote {outname} ({len(words)} words)", flush=True)
