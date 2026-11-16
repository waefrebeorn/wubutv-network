#!/usr/bin/env python3
"""MV-5 assembly measurement: transcribe every KEEP take (prompted with its
own scene lines, word timestamps) + RMS envelopes for the grey-rescue scenes.

Sources of truth: LYRIC_TIMELINE.md performed lines; VOLLEY_PROGRESS.md
dispositions. Output: work/assembly_take_words/<scene>_prompted.json (words)
and <scene>_rms.json (per-0.1s RMS envelope, for S17 R4 / S19b head /
S22 t3 cover decision / S21 head). Per-take temp wavs in /tmp, deleted after.
"""
import json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(PROJ)  # work/ -> project root
OUT = os.path.join(PROJ, "work", "assembly_take_words")
os.makedirs(OUT, exist_ok=True)

from faster_whisper import WhisperModel

# scene -> (take file stem, prompted line text, song line ids covered)
TAKES = {
    "S01": ("mv5_s01_t1", "Easy now, easy now. We ride, we ride. Easy now, easy now. Till the morning comes."),
    "S03": ("mv5_s03_t1", "Ta-da, ta-da, ta-da, ta-da, ta-da, ta-da."),
    "S04": ("mv5_s04_t1", "Bare feet on the boardwalk. Salt on my skin. You came in laughing. Said, come on, let's begin. Blue shirt, red bicycle."),
    "S05": ("mv5_s05_t1", "Rolling past the pier. I was posted up right here. Now you're pulling near. Backpack half-zipped."),
    "S06": ("mv5_s06_t1", "Keys in your hand. You nodded at the waves like. Yeah, they already understand."),
    "S07": ("mv5_s07_t1", "Slow down, take your time. Let the hard week fade. One small look from you. And my whole head replays."),
    "S08": ("mv5_s08_t2", "Easy now, easy now. Easy now, easy now. Easy now, easy now. Easy now, easy now."),
    "S09": ("mv5_s09_t1", "Easy now, easy now. Easy now, easy now. Easy now, easy now. Easy now, easy now."),
    "S11": ("mv5_s11_t4", "Calling mango sweet. Socks in the sand. Time with our feet."),
    "S12": ("mv5_s12_t1", "Your laugh hit the air. Like a hand drum roll. I forgot the list, forgot the bills. Forgot what I was told."),
    "S15": ("mv5_s15_t1", "And my whole head replays."),
    "S17": ("mv5_s17_t1", "Easy now, easy now. Easy now, easy now. Easy now, easy now. Easy now, easy now."),
    "S19b": ("mv5_s19b_t1", "We still move with it. Hand in my hand. No speech, no show."),
    "S20": ("mv5_s20_t1", "Heart in the breeze."),
    "S21": ("mv5_s21_t3", "If the sky turns gray. We don't fold in. We lean right back. Let the whole thing spin. You and me, same pace."),
    "S23": ("mv5_s23_t1", "Easy now, easy now. Easy now, easy now. Easy now, easy now. No need to."),
    "S25": ("mv5_s25_t1", "Easy now, easy now. Easy now, easy now."),
    "S26": ("mv5_s26_t1", "Easy now, easy now."),
    "S27": ("mv5_s27_t1", "Easy now, easy now."),
    "S28": ("mv5_s28_t1", "Till the morning comes."),
    # S22 t3 is REJECTED (ratio) but its head-shake picture is the S22 cover
    # candidate: measure its RMS/mouth windows only, never as a sung take.
    "S22": ("mv5_s22_t3", "No, no, no."),
}
RMS_SCENES = ["S17", "S19b", "S22", "S21", "S11", "S08", "S09", "S25", "S26"]

def extract_wav(src, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vn", "-ac", "1",
                    "-ar", "16000", "-f", "f32le", dst], check=True)
    return np.fromfile(dst, dtype=np.float32)

def rms_env(pcm, sr=16000, win=0.1):
    n = int(sr * win)
    out = []
    for i in range(0, len(pcm) - n + 1, n):
        seg = pcm[i:i + n]
        out.append(round(float(np.sqrt(np.mean(seg ** 2))), 4))
    return out

def main():
    model = WhisperModel("base", device="cpu", compute_type="int8")
    for sc, (stem, prompt) in TAKES.items():
        src = os.path.join(PROJ, "takes", stem + ".mp4")
        tmp = f"/tmp/mv5_{stem}.f32"
        pcm = extract_wav(src, tmp)
        dur = len(pcm) / 16000
        segs, _ = model.transcribe(pcm, word_timestamps=True, language="en",
                                   beam_size=1, initial_prompt=prompt)
        words = []
        for seg in segs:
            words += [{"word": w.word.strip(), "start": round(float(w.start), 3),
                       "end": round(float(w.end), 3)} for w in seg.words]
        # drop zero-duration pile-up words from the report line (kept in file)
        real = [w for w in words if w["end"] > w["start"]]
        json.dump({"take": stem, "prompt": prompt, "take_dur": round(dur, 3),
                   "words": words},
                  open(os.path.join(OUT, f"{sc}_prompted.json"), "w"), indent=1)
        if real:
            print(f"{sc} {stem}: n={len(real)} first={real[0]['word']}@{real[0]['start']:.2f} "
                  f"last_end={real[-1]['end']:.2f} span={real[-1]['end']-real[0]['start']:.2f} "
                  f"text={' '.join(w['word'] for w in real)}", flush=True)
        else:
            print(f"{sc} {stem}: NO WORDS", flush=True)
        if sc in RMS_SCENES:
            env = rms_env(pcm)
            json.dump({"take": stem, "win": 0.1, "rms": env},
                      open(os.path.join(OUT, f"{sc}_rms.json"), "w"), indent=1)
            print(f"   rms(0.1s): {env}", flush=True)
        os.remove(tmp)

if __name__ == "__main__":
    main()
