#!/usr/bin/env python3
"""MV-20 take QC: ASR (cached json) + G7 word-set gate + frame gate.
Usage: qc_take.py S01 takes/mv20_s01_t1.mp4 [--asr-only]
G7: screened words (p>=0.5 in segments avg_logprob>=-1.0) vs slot
planned set P (scene_words.json): overlap |A&P|/|P| >= 0.5 PASS."""
import sys, json, subprocess, pathlib, re
sys.path.insert(0, "/home/hatch/workspace/tools/lyrics-venv/lib/python3.12/site-packages")
ROOT = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-20_laundry-life"
ANA = ROOT / "work" / "analysis"
PLAN = json.load(open(ANA / "scene_words.json"))

def norm(w):
    w = w.lower().strip(".,!?()'\"")
    w = w.replace("\u2019", "'")
    return {"basketball": "basket", "told": "toll"}.get(w, w)

def asr(take, out):
    if pathlib.Path(out).exists():
        return json.load(open(out))
    from faster_whisper import WhisperModel
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=2)
    segments, info = model.transcribe(take, language="en", word_timestamps=True,
                                      vad_filter=False, beam_size=5)
    words, segs = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3),
                     "text": s.text.strip(), "avg_logprob": round(s.avg_logprob, 3)})
        for w in (s.words or []):
            words.append({"w": w.word.strip(), "start": round(w.start, 3),
                          "end": round(w.end, 3), "p": round(w.probability, 3)})
    d = {"take": take, "words": words, "segments": segs}
    json.dump(d, open(out, "w"), indent=1)
    return d

def main():
    scene, take = sys.argv[1], sys.argv[2]
    name = pathlib.Path(take).stem
    d = asr(take, ANA / f"asr_{name}.json")
    # screened set: word prob>=0.5 and segment avg_logprob>=-1.0
    good_segs = [(s["start"], s["end"]) for s in d["segments"] if s["avg_logprob"] >= -1.0]
    A = set()
    for w in d["words"]:
        if w["p"] >= 0.5 and any(a - 0.01 <= w["start"] <= b + 0.01 for a, b in good_segs):
            A.add(norm(w["w"]))
    P = set()
    for line in PLAN[scene]:
        for w in line.replace("-", " ").split():
            P.add(norm(w))
    ov = len(A & P) / len(P) if P else (1.0 if not A else 0.0)
    raw = " ".join(w["w"] for w in d["words"])
    span = (d["words"][0]["start"], d["words"][-1]["end"]) if d["words"] else (0, 0)
    print(f"{name}: G7={ov:.3f} {'PASS' if ov >= 0.5 else 'REJECT'} span={span[0]:.2f}-{span[1]:.2f}")
    print(f"  raw: {raw}")
    if "--asr-only" not in sys.argv:
        r = subprocess.run(["python3", str(ANA / "frame_gate.py"), take,
                            str(span[0]), str(span[1])], capture_output=True, text=True)
        print("  frame:", r.stdout.strip() or r.stderr.strip()[-200:])

if __name__ == "__main__":
    main()
