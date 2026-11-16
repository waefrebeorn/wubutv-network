"""MV-5 volley 8 QC: frames, Whisper line check, motion audit, repeat check."""
import json, os, subprocess
import numpy as np
from faster_whisper import WhisperModel

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAKES = os.path.join(BASE, "takes")
WORK = os.path.join(BASE, "work")
QC = os.path.join(WORK, "qc_v9")
os.makedirs(QC, exist_ok=True)

# scene: (take file, prompted line or None, song slot duration, take window for motion, frame times)
SCENES = {
 "s24": ("mv5_s24_t2.mp4", "Easy now, easy now", 6.74, (0, 5.8), (2, 5)),
 "s25": ("mv5_s25_t1.mp4", "Easy now, easy now", 5.26, (0, 3.7), (2, 4)),
 "s26": ("mv5_s26_t1.mp4", "Easy now, easy now", 7.16, (0, 4.3), (2, 4, 6)),
 "s27": ("mv5_s27_t1.mp4", "Easy now, easy now", 5.84, (0, 5.8), (2, 4)),
 "s28": ("mv5_s28_t1.mp4", "Till the morning comes", 2.16, (0, 2.2), (1, 3)),
 "s13": ("mv5_s13_t7.mp4", "Ice cup sweating, on the rail by the steps, didn't, not yet, kids with a boombox, cutting through the crowd, you took my sleeve and spun me once, like none of it was loud", 9.50, (0, 9.6), (2, 5, 8)),
}

FORBIDDEN = {
 "s13": ["you said", "don't think"],
 "s24": ["we hold the sun", "keep it loose", "let it drift"],
 "s25": ["we're good where", "just two small sparks"],
 "s26": ["we ride"],
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

def transcribe(model, audio, line):
    segs, _ = model.transcribe(audio, language="en", word_timestamps=True,
                               initial_prompt=line, beam_size=5)
    seg_list = list(segs)  # segs is a generator — materialise once, never iterate twice
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
    for sc, (take, line, slot, (w0, w1), ftimes) in SCENES.items():
        path = os.path.join(TAKES, take)
        r = {"take": take, "song_slot": slot}
        for t in ftimes:
            out = os.path.join(QC, f"{sc}_t{t}.png")
            subprocess.run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",path,"-frames:v","1",out], check=True)
        m, diffs = motion(path)
        r["motion"] = m
        r["vocal_motion"] = vocal_motion(diffs, w0, w1)
        if line:
            audio = wav16k(path, os.path.join(QC, f"tmp_{sc}.f32"))
            text, words, allw = transcribe(model, audio, line)
            if not allw:
                # SPLIT-HALF RULE: zero-word full-clip decode is not a no-line verdict
                half = audio[:len(audio)//2]
                text, words, allw = transcribe(model, half, line)
                r["split_half_recheck"] = True
            r["whisper_text"] = " ".join(text)
            r["whisper_words"] = words
            r["whisper_nwords"] = len(words)
            if allw:
                r["take_line_span"] = round(allw[-1].end - allw[0].start, 2)
                r["first_word"] = round(allw[0].start, 2)
                r["last_word_end"] = round(allw[-1].end, 2)
                r["line_ratio"] = round(slot / max(r["take_line_span"], 0.01), 2)
                r["word_times"] = [(w.word.strip(), round(w.start,2), round(w.end,2)) for w in allw]
            norm = [w.lower().strip().strip(".,!?") for w in words]
            seen = set(); rep = []
            for i in range(len(norm)-1):
                bg = (norm[i], norm[i+1])
                if bg in seen and bg not in rep:
                    rep.append(bg)
                seen.add(bg)
            r["repeat_bigrams"] = [" ".join(b) for b in rep]
            # forbidden-word scan (response lines must not be sung in refrain scenes)
            low = " ".join(text).lower()
            r["forbidden_found"] = [f for f in FORBIDDEN.get(sc, []) if f in low]
            # refrain delivery count for s08/s09/s16/s17/s23
            if sc in ("s08", "s09", "s16", "s17", "s23", "s24", "s25", "s26", "s27"):
                r["easy_now_count"] = sum(1 for i in range(len(norm)-1) if norm[i] == "easy" and norm[i+1] == "now")
        results[sc] = r
        print(json.dumps(r, indent=1), flush=True)
    with open(os.path.join(QC, "qc_v9_results.json"), "w") as f:
        json.dump(results, f, indent=1)

if __name__ == "__main__":
    main()
