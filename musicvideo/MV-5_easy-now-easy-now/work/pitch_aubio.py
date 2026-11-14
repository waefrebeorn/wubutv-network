"""Per-word median f0 via aubio YIN on the 16k mono mix."""
import json, os, sys
import numpy as np
import aubio

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
SR = 16000

def main(words_path, tag):
    audio = np.fromfile(os.path.join(WORK, "tmp_audio.f32"), dtype=np.float32).astype(np.float32)
    win, hop = 2048, 512
    pitch_o = aubio.pitch("yin", win, hop, SR)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(0.8)
    # run over whole track once
    f0s, confs = [], []
    for i in range(0, len(audio) - hop, hop):
        frame = audio[i:i+hop]
        f = float(pitch_o(frame)[0])
        c = float(pitch_o.get_confidence())
        f0s.append(f); confs.append(c)
    f0s = np.array(f0s); confs = np.array(confs)
    times = np.arange(len(f0s)) * hop / SR
    words = json.load(open(words_path))
    out = []
    for w in words:
        m = (times >= w["start"]) & (times < w["end"]) & (confs > 0.5) & (f0s >= 60) & (f0s <= 500)
        vals = f0s[m]
        out.append({**w, "f0_median": float(np.median(vals)) if len(vals) else None,
                    "f0_n": int(len(vals))})
    with open(os.path.join(WORK, f"pitch_aubio_{tag}.json"), "w") as f:
        json.dump(out, f, indent=1)
    v = [o["f0_median"] for o in out if o["f0_median"]]
    print(tag, "words", len(out), "voiced", len(v),
          "median", round(float(np.median(v)),1) if v else None)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
