import json, os, re, subprocess
import numpy as np
P = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
scenes = {s["n"]: s for s in json.load(open(os.path.join(P, "work/scenes.json")))}
song_words = json.load(open(os.path.join(P, "SONG_WORDS.json")))
from faster_whisper import WhisperModel
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
def norm(w): return re.sub(r"[^a-z']", "", w.lower().strip())
WORDLESS = {10, 21}
for n in (10, 16, 20, 21, 22):
    s = scenes[n]
    take = os.path.join(P, f"takes/mv25_s{n:02d}_t2.mp4")
    wav = os.path.join(P, f"work/qc/s{n:02d}t2.wav")
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
    json.dump({"segments": seglist, "sung": sung}, open(os.path.join(P, f"work/qc/s{n:02d}t2_asr.json"), "w"), indent=1)
    if n in WORDLESS:
        pw = []
    else:
        txt = re.sub(r"\(.*?\)", "", s["lines"])
        pw = [norm(w) for w in txt.replace("/", " ").split() if norm(w)]
    sw = [norm(w["w"]) for w in sung]
    overlap = (len(set(sw) & set(pw)) / len(set(pw))) if pw else (1.0 if not sw else 0.0)
    w0, w1 = s["win"]
    sng = [w for w in song_words if w0 - 0.05 <= w["start"] < w1]
    song_span = (round(min(w["start"] for w in sng),2), round(max(w["end"] for w in sng),2)) if sng else None
    take_span = (sung[0]["s"], sung[-1]["e"]) if sung else None
    ratio = None
    if song_span and take_span and take_span[1] > take_span[0]:
        ratio = round((song_span[1]-song_span[0]) / (take_span[1]-take_span[0]), 3)
    print(n, {"g7": round(overlap,3), "sung": len(sung), "song_span": song_span, "take_span": take_span,
              "ratio": ratio, "text": " ".join(w["w"] for w in sung)}, flush=True)
print("T2 QC DONE")
