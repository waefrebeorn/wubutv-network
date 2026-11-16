import json, subprocess, os
import numpy as np
from faster_whisper import WhisperModel

WORK = os.path.join(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.dirname(WORK)
def wav16k(path, out, start=None, dur=None):
    cmd = ["ffmpeg","-y","-v","error"]
    if start is not None: cmd += ["-ss", str(start)]
    cmd += ["-i", path]
    if dur is not None: cmd += ["-t", str(dur)]
    cmd += ["-ac","1","-ar","16000","-f","f32le",out]
    subprocess.run(cmd, check=True)
    return np.fromfile(out, dtype=np.float32)

model = WhisperModel("base", device="cpu", compute_type="int8")
lyrics = open(os.path.join(BASE,"lyrics.txt")).read()
for (t0, t1, tag) in [(184.0, 206.4, "tail"), (16.0, 23.0, "v1open"), (75.0, 86.0, "c1tail"), (139.0, 150.0, "c2tail")]:
    audio = wav16k(os.path.join(BASE,"track.mp3"), os.path.join(WORK,f"tmp_{tag}.f32"), start=t0, dur=t1-t0)
    for prompt_tag, prompt in [("noprompt", None), ("prompted", lyrics)]:
        segs, info = model.transcribe(audio, language="en", word_timestamps=True,
            initial_prompt=prompt, beam_size=5)
        out = {"tag": tag, "t0": t0, "segments": []}
        for s in segs:
            words = [{"word": w.word, "start": round(t0+w.start,3), "end": round(t0+w.end,3), "prob": round(w.probability,3)} for w in s.words]
            out["segments"].append({"start": round(t0+s.start,3), "end": round(t0+s.end,3), "text": s.text.strip(), "words": words})
        with open(os.path.join(WORK, f"transcript_{tag}_{prompt_tag}.json"), "w") as f:
            json.dump(out, f, indent=1)
        print(tag, prompt_tag, "segs", len(out["segments"]), flush=True)
