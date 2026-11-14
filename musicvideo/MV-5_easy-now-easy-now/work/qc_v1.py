"""MV-5 volley 1 QC: frames, Whisper line check, motion audit."""
import json, os, subprocess, sys
import numpy as np
from faster_whisper import WhisperModel

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAKES = os.path.join(BASE, "takes")
WORK = os.path.join(BASE, "work")
QC = os.path.join(WORK, "qc_v1")
os.makedirs(QC, exist_ok=True)

# scene: (prompted line, song slot duration, take window)
SCENES = {
 "s01": ("Easy now, easy now, we ride, we ride, easy now, easy now, till the morning comes", 8.38),
 "s02": (None, 8.60),
 "s03": ("ta-da, ta-da, ta-da, ta-da, ta-da, ta-da", 3.36),
 "s04": ("Bare feet on the boardwalk, salt on my skin, you came in laughing, said, come on, let's begin, blue shirt, red bicycle", 9.48),
 "s05": ("Rolling past the pier, I was posted up right here, now you're pulling near, backpack half-zipped", 8.96),
 "s08": ("Easy now, easy now", 9.54),  # refrain x4; check count of "easy now" deliveries
}

def wav16k(src, out):
    subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le",out], check=True)
    return np.fromfile(out, dtype=np.float32)

def motion(src, tag):
    # 160x90 frames, mean abs diff between consecutive frames, exact dups
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],
                         capture_output=True, check=True).stdout
    w, h = 160, 90
    n = len(raw)//(w*h)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(n, w*h).astype(np.int16)
    diffs = np.mean(np.abs(np.diff(frames, axis=0)), axis=1)
    exact = int(np.sum(diffs == 0))
    # longest near-dup run (diff < 0.5)
    best = cur = 0
    for d in diffs:
        cur = cur + 1 if d < 0.5 else 0
        best = max(best, cur)
    return {"frames": n, "mean_diff": round(float(np.mean(diffs)),3),
            "longest_neardup_run": int(best), "exact_dup_frames": exact}

def main():
    model = WhisperModel("base", device="cpu", compute_type="int8")
    results = {}
    for sc, (line, slot) in SCENES.items():
        take = os.path.join(TAKES, f"mv5_{sc}_t1.mp4")
        r = {"take": f"mv5_{sc}_t1.mp4", "song_slot": slot}
        # frames at 2/5/8s
        for t in (2, 5, 8):
            out = os.path.join(QC, f"{sc}_t{t}.png")
            subprocess.run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",take,"-frames:v","1",out], check=True)
        r["motion"] = motion(take, sc)
        if line:
            audio = wav16k(take, os.path.join(QC, f"tmp_{sc}.f32"))
            segs, _ = model.transcribe(audio, language="en", word_timestamps=True,
                                       initial_prompt=line, beam_size=5)
            words = []
            text = []
            for s in segs:
                text.append(s.text.strip())
                words.extend([w.word for w in s.words])
            r["whisper_text"] = " ".join(text)
            r["whisper_words"] = words
            r["whisper_nwords"] = len(words)
            # take line duration: first to last word time
            allw = []
            for s in segs:
                allw.extend(s.words)
            if allw:
                r["take_line_span"] = round(allw[-1].end - allw[0].start, 2)
                r["line_ratio"] = round(slot / max(r["take_line_span"], 0.01), 2)
            # repeat check: any word bigram recurring after first delivery
            norm = [w.lower().strip(".,!?") for w in words]
            seen = set(); rep = []
            for i in range(len(norm)-1):
                bg = (norm[i], norm[i+1])
                if bg in seen and bg not in rep:
                    rep.append(bg)
                seen.add(bg)
            r["repeat_bigrams"] = [" ".join(b) for b in rep]
        results[sc] = r
        print(json.dumps(r, indent=1), flush=True)
    with open(os.path.join(QC, "qc_v1_results.json"), "w") as f:
        json.dump(results, f, indent=1)

if __name__ == "__main__":
    main()
