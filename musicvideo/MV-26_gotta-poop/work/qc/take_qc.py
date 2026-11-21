import json, os, re, subprocess, sys
import numpy as np
P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# usage: take_qc.py <tag> <scene,scene,...>   e.g. take_qc.py t1 1,2,3,7,8,15
TAG = sys.argv[1] if len(sys.argv) > 1 else "t1"
WANT = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else None
scenes = {s["n"]: s for s in json.load(open(os.path.join(P, "work/scenes.json")))}
song_words = json.load(open(os.path.join(P, "SONG_WORDS.json")))
from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
MISHEAR = {}
def norm(w):
    w = re.sub(r"[^a-z']", "", w.lower().strip()).rstrip("'")
    return MISHEAR.get(w, w)
def planned_words(s):
    if s["tag"] == "CUTAWAY": return []
    txt = re.sub(r"\(.*?\)", "", s["lines"])
    return [norm(w) for w in txt.replace("/", " ").split() if norm(w)]
out = {}
for n in sorted(scenes):
    if WANT and n not in WANT: continue
    s = scenes[n]
    take = os.path.join(P, f"takes/mv26_s{n:02d}_{TAG}.mp4")
    if not os.path.exists(take): print(n, "MISSING", take); continue
    wav = os.path.join(P, f"work/qc/s{n:02d}_{TAG}.wav")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",take,"-ac","1","-ar","16000",wav], check=True)
    pcm = subprocess.run(["ffmpeg","-v","error","-i",wav,"-f","f32le","-ac","1","-ar","16000","-"], capture_output=True).stdout
    audio = np.frombuffer(pcm, dtype=np.float32).copy()
    segs, _ = model.transcribe(audio, language="en", beam_size=1, word_timestamps=True,
        condition_on_previous_text=False, repetition_penalty=1.1, no_repeat_ngram_size=3,
        compression_ratio_threshold=2.4, log_prob_threshold=-1.0, no_speech_threshold=0.6, vad_filter=False)
    seglist, sung = [], []
    for sg in segs:
        words = [{"w": w.word, "s": round(w.start,2), "e": round(w.end,2), "p": round(w.probability,3)} for w in (sg.words or [])]
        seglist.append({"s": round(sg.start,2), "e": round(sg.end,2), "avg_logprob": round(sg.avg_logprob,3), "text": sg.text, "words": words})
        if sg.avg_logprob >= -1.0:
            for w in words:
                if w["p"] >= 0.5: sung.append(w)
    json.dump({"segments": seglist, "sung": sung}, open(os.path.join(P, f"work/qc/s{n:02d}_{TAG}_asr.json"), "w"), indent=1)
    pw = planned_words(s)
    sw = [norm(w["w"]) for w in sung]
    overlap = (len(set(sw) & set(pw)) / len(set(pw))) if pw else (1.0 if not sw else 0.0)
    w0, w1 = s["win"]
    sng = [w for w in song_words if w0 - 0.05 <= w["start"] < w1]
    song_span = (round(min(w["start"] for w in sng),2), round(max(w["end"] for w in sng),2)) if sng else None
    take_span = (sung[0]["s"], sung[-1]["e"]) if sung else None
    ratio = None
    if song_span and take_span and take_span[1] > take_span[0]:
        ratio = round((song_span[1]-song_span[0]) / (take_span[1]-take_span[0]), 3)
    raw = subprocess.run(["ffmpeg","-v","error","-i",take,"-vf","fps=4,scale=160:90,format=gray",
                          "-f","rawvideo","-"], capture_output=True).stdout
    fr = np.frombuffer(raw, dtype=np.uint8)
    nfr = len(fr)//(160*90); fr = fr[:nfr*160*90].reshape(nfr,160*90).astype(np.float32)
    diffs = np.abs(np.diff(fr, axis=0)).mean(axis=1) if nfr > 1 else np.array([])
    maxrun, run = 0, 0
    for d in diffs:
        run = run+1 if d < 1.0 else 0; maxrun = max(maxrun, run)
    out[n] = {"g7_overlap": round(overlap,3), "planned_n": len(set(pw)), "sung_words": len(sung),
              "song_span": song_span, "take_span": take_span, "ratio": ratio,
              "motion_mean_diff": round(float(diffs.mean()),2) if len(diffs) else None,
              "motion_max_neardup_run_s": round(maxrun/4,2),
              "sung_text": " ".join(w["w"] for w in sung)}
    print(n, out[n], flush=True)
prev = {}
pf = os.path.join(P, "work/qc/take_qc.json")
if os.path.exists(pf): prev = json.load(open(pf))
prev.update({str(k): v for k, v in out.items()})
json.dump(prev, open(pf, "w"), indent=1)
print("QC DONE")
