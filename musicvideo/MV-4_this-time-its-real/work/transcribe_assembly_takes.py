#!/usr/bin/env python3
"""MV-4 assembly: transcribe all KEEP takes (unprompted + prompted) with
faster-whisper base (same model/settings as QC). Saves per-take word
JSONs to work/assembly_take_words/. Sequential, per-take temp wav,
never shared (cross-check method discipline)."""
import json, os, subprocess, sys

PROJ = "/home/hatch/workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
OUT = os.path.join(PROJ, "work", "assembly_take_words")
os.makedirs(OUT, exist_ok=True)

# scene -> (take file, performed line text for initial_prompt)
TAKES = {
 "S01": ("mv4_s01_t1.mp4", "They said it was over back in '03, then they said it again in twenty-thirteen."),
 "S02": ("mv4_s02_t1.mp4", "Hulu hit rewind and we all leaned in, fourteen seasons later, we're still on the screen."),
 "S03": ("mv4_s03_t1.mp4", "Final Ending: The Last Conclusion, that's the label on the last file."),
 "S04": ("mv4_s04_t1.mp4", "Matt said, we're not done yet, but the streamer closed the door in style."),
 "S05": ("mv4_s05_t1.mp4", "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark."),
 "S06": ("mv4_s06_t3.mp4", "Futurama's finished, Futurama's finished, no fresh episodes, that's the hard part."),
 "S07": ("mv4_s07_t1.mp4", "Good news, everyone, the ride is done, good news, everyone, the ship won't run."),
 "S08": ("mv4_s08_t1.mp4", "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark."),
 "S09": ("mv4_s09_t1.mp4", "Three more specials lined up in twenty-seven, Christmas first, then two more after."),
 "S10": ("mv4_s10_t1.mp4", "But a whole new season? Not on the board. They sealed it up and walked out after."),
 "S11": ("mv4_s11_t1.mp4", "We've seen this loop from Fox to cable, then streaming gave it one more round."),
 "S12": ("mv4_s12_t1.mp4", "But this song's about the day they mean it, when the last new line never comes down."),
 "S13": ("mv4_s13_t1.mp4", "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark."),
 "S14": ("mv4_s14_t1.mp4", "Futurama's finished, Futurama's finished, no fresh episodes, that's the hard part."),
 "S15": ("mv4_s15_t1.mp4", "Good news, everyone, the ride is done, good news, everyone, the ship won't run."),
 "S16": ("mv4_s16_t1.mp4", "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark."),
 "S17": ("mv4_s17_t1.mp4", "They always joke before the ending, like they can talk the credits back."),
 "S18": ("mv4_s18_t2.mp4", "We'll rise again, he keeps on saying, but the paperwork says otherwise."),
 "S19": ("mv4_s19_t1.mp4", "You can binge the old ones on your couch, quote every line like muscle memory."),
 "S20": ("mv4_s20_t1.mp4", "But the new ones stopped at the doorstep, and the hallway stays empty."),
 "S21": ("mv4_s21_t1.mp4", "Futurama's finished, Futurama's finished, for real this time, no more reruns in the dark."),
 "S22": ("mv4_s22_t1.mp4", "Futurama's finished, Futurama's finished, no fresh episodes, that's the hard part."),
 "S24": ("mv4_s24_t1.mp4", "Good news, everyone, good news, everyone, no more coming on."),
 "S26": ("mv4_s26_t1.mp4", "For real this time."),
 "S27": ("mv4_s27_t1.mp4", "No more coming on."),
 "S28": ("mv4_s28_t1.mp4", ""),
 "S29": ("mv4_s29_t1.mp4", "Good news, everyone. For real this time."),
 "S30a": ("mv4_s30a_t1.mp4", ""),
 "S30b": ("mv4_s30b_t1.mp4", ""),
}

import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe(wav, prompt):
    import wave
    with wave.open(wav, "rb") as wf:
        pcm = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
    audio = pcm.astype(np.float32) / 32768.0
    kwargs = dict(language="en", word_timestamps=True)
    if prompt:
        kwargs["initial_prompt"] = prompt
    segs, _ = model.transcribe(audio, **kwargs)
    words = []
    for seg in segs:
        for w in seg.words or []:
            words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
    return words

summary = {}
for sc, (fn, line) in TAKES.items():
    path = os.path.join(PROJ, "takes", fn)
    wav = f"/tmp/mv4_asm_{sc}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path,
                    "-vn", "-ac", "1", "-ar", "16000", "-f", "wav", wav], check=True)
    unp = transcribe(wav, None)
    pr = transcribe(wav, line) if line else []
    json.dump(unp, open(os.path.join(OUT, f"{sc}_unprompted.json"), "w"), indent=1)
    json.dump(pr, open(os.path.join(OUT, f"{sc}_prompted.json"), "w"), indent=1)
    os.remove(wav)
    def span(ws):
        return (ws[0]["start"], ws[-1]["end"]) if ws else (None, None)
    summary[sc] = {
        "file": fn,
        "unprompted_n": len(unp), "unprompted_span": span(unp),
        "unprompted_words": " ".join(w["word"] for w in unp),
        "prompted_n": len(pr), "prompted_span": span(pr),
        "prompted_words": " ".join(w["word"] for w in pr),
    }
    print(f"{sc}: unprompted {len(unp)}w span={span(unp)} | prompted {len(pr)}w span={span(pr)}", flush=True)
json.dump(summary, open(os.path.join(OUT, "summary.json"), "w"), indent=1)
print("DONE", len(summary), "takes")
