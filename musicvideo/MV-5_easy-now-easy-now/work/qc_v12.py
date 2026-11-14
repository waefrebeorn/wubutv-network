"""MV-5 volley 12 QC: ear-confirmed GIRL inserts (S06 t2, S21 t4-t7).
Adapted from qc_v11_t4.py — same gates, five takes.
S07 t2 was NOT generated (media tool integrity_check_failed, no retry per
parent instruction) — no QC row for it.
Frames + Whisper line check (prompted, with unprompted confirm) + motion
audit + repeat check. Singer is judged by MOUTH FRAMES (read the PNGs),
never by take f0."""
import json, os, subprocess
import numpy as np
from faster_whisper import WhisperModel

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAKES = os.path.join(BASE, "takes")
WORK = os.path.join(BASE, "work")
QC = os.path.join(WORK, "qc_v12")
os.makedirs(QC, exist_ok=True)

# scene: (take file, prompted line, song slot duration, frame times)
SCENES = {
 "s06": ("mv5_s06_t2.mp4", "Yeah, they already understand", 2.28, (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)),
 "s21_t4": ("mv5_s21_t4.mp4", "If the sky turns gray", 1.04, (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)),
 "s21_t5": ("mv5_s21_t5.mp4", "We lean right back", 1.12, (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)),
 "s21_t6": ("mv5_s21_t6.mp4", "You and me, same pace", 1.12, (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)),
 "s21_t7": ("mv5_s21_t7.mp4", "Nothing to prove", 0.98, (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0)),
}

def wav16k(src, out):
    subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le",out], check=True)
    return np.fromfile(out, dtype=np.float32)

def motion(src):
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],
                         capture_output=True, check=True).stdout
    w, h = 160, 90
    n = len(raw)//(w*h)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, w*h).astype(np.int16)
    diffs = np.mean(np.abs(np.diff(frames, axis=0)), axis=1)
    exact = int(np.sum(diffs == 0))
    best = cur = 0
    for d in diffs:
        cur = cur + 1 if d < 0.5 else 0
        best = max(best, cur)
    return {"frames": n, "mean_diff": round(float(np.mean(diffs)),3),
            "longest_neardup_run": int(best), "exact_dup_frames": exact}, diffs

def vocal_motion(diffs, t0, t1):
    seg = diffs[int(t0*24):min(int(t1*24), len(diffs))]
    best = cur = 0
    for d in seg:
        cur = cur + 1 if d < 0.5 else 0
        best = max(best, cur)
    persec = [round(float(np.mean(diffs[i*24:(i+1)*24])),3) for i in range(int(t0), int(t1))]
    return {"vocal_mean_diff": round(float(np.mean(seg)),3), "vocal_longest_neardup": int(best),
            "per_second_mean_diff": persec}

def transcribe(model, audio, line=None):
    kw = dict(language="en", word_timestamps=True, beam_size=5)
    if line:
        kw["initial_prompt"] = line
    segs, _ = model.transcribe(audio, **kw)
    seg_list = list(segs)
    words, text = [], []
    for s in seg_list:
        text.append(s.text.strip())
        words.extend([w.word for w in s.words])
    allw = []
    for s in seg_list:
        allw.extend(s.words)
    return text, words, allw

def main():
    model = WhisperModel("base", device="cpu", compute_type="int8")
    results = {}
    for sc, (take, line, slot, ftimes) in SCENES.items():
        path = os.path.join(TAKES, take)
        r = {"take": take, "song_slot": slot, "line": line}
        for t in ftimes:
            out = os.path.join(QC, f"{sc}_t{t}.png")
            subprocess.run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",path,"-frames:v","1",out], check=True)
        m, diffs = motion(path)
        r["motion"] = m
        audio = wav16k(path, os.path.join(QC, f"tmp_{sc}.f32"))
        # per-0.5s RMS (voice activity evidence)
        sr = 16000
        r["rms_per_0.5s"] = [round(float(np.sqrt(np.mean(audio[i:i+sr//2]**2))), 4)
                             for i in range(0, len(audio), sr//2)]
        text, words, allw = transcribe(model, audio, line)
        if not allw:
            half = audio[:len(audio)//2]
            text, words, allw = transcribe(model, half, line)
            r["split_half_recheck"] = True
        r["whisper_text_prompted"] = " ".join(text)
        r["whisper_words_prompted"] = words
        if allw:
            r["take_line_span"] = round(allw[-1].end - allw[0].start, 2)
            r["first_word"] = round(allw[0].start, 2)
            r["last_word_end"] = round(allw[-1].end, 2)
            r["line_ratio"] = round(slot / max(r["take_line_span"], 0.01), 2)
            r["word_times"] = [(w.word.strip(), round(w.start,2), round(w.end,2)) for w in allw]
            r["vocal_motion"] = vocal_motion(diffs, allw[0].start, allw[-1].end)
        # unprompted confirm (guards against prompted hallucination / repeats)
        utext, uwords, uallw = transcribe(model, audio)
        r["whisper_text_unprompted"] = " ".join(utext)
        r["whisper_words_unprompted"] = [(w.word.strip(), round(w.start,2), round(w.end,2)) for w in uallw]
        norm = [w.lower().strip().strip(".,!?") for w in words]
        seen = set(); rep = []
        for i in range(len(norm)-1):
            bg = (norm[i], norm[i+1])
            if bg in seen and bg not in rep:
                rep.append(bg)
            seen.add(bg)
        r["repeat_bigrams_prompted"] = [" ".join(b) for b in rep]
        results[sc] = r
        print(json.dumps(r, indent=1), flush=True)
    with open(os.path.join(QC, "qc_v12_results.json"), "w") as f:
        json.dump(results, f, indent=1)

if __name__ == "__main__":
    main()
