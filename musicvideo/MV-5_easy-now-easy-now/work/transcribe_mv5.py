import json, subprocess, sys, os
import numpy as np
from faster_whisper import WhisperModel

PROJ = os.path.dirname(os.path.abspath(__file__))  # work/
BASE = os.path.dirname(PROJ)
mp3 = os.path.join(BASE, "track.mp3")

def wav16k(path, out):
    subprocess.run(["ffmpeg","-y","-v","error","-i",path,"-ac","1","-ar","16000","-f","f32le",out], check=True)
    return np.fromfile(out, dtype=np.float32)

audio = wav16k(mp3, os.path.join(PROJ,"tmp_audio.f32"))
print("samples", len(audio), "dur", len(audio)/16000, flush=True)
model = WhisperModel("base", device="cpu", compute_type="int8")
lyrics = open(os.path.join(BASE,"lyrics.txt")).read()
for tag, prompt in [("prompted", lyrics), ("noprompt", None)]:
    segs, info = model.transcribe(audio, language="en", word_timestamps=True,
        initial_prompt=prompt, beam_size=5, vad_filter=False)
    out = {"tag": tag, "language": info.language, "segments": []}
    nwords = 0
    for s in segs:
        words = [{"word": w.word, "start": round(w.start,3), "end": round(w.end,3), "prob": round(w.probability,3)} for w in s.words]
        nwords += len(words)
        out["segments"].append({"start": round(s.start,3), "end": round(s.end,3), "text": s.text.strip(), "words": words})
    out["nwords"] = nwords
    with open(os.path.join(PROJ, f"song_transcript_{tag}.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(tag, "segments", len(out["segments"]), "words", nwords, flush=True)
