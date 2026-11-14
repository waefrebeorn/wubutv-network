"""QC transcription + frame gate for MV-2 v6 volley 16, S11 restage only.
Adapted from qc_v6_volley15.py (same Whisper base, same mishear map with
beat words normalized through the same map, same subsequence repeat scan,
same split-half rule) and vocal_window_audit_v13refire.py (160x90 gray,
native 24fps, FAIL if vocal near-dup run >=24 OR vocal mean diff <0.5).
Beat: "lexus lanes they call them", song span 108.02-109.52, song_dur 1.50.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "done": "dumb", "paid": "pay",
        "plasers": "plazas", "comin": "coming", "tell": "sell"}

def transcribe(path, wav, audio_range=None):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    if audio_range is not None:
        a, b = audio_range
        audio = audio[int(a * 16000):int(b * 16000)]
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?")
            raw = txt
            txt = NORM.get(txt, txt)
            off = audio_range[0] if audio_range else 0.0
            words.append([txt, round(w.start + off, 2), round(w.end + off, 2), raw])
    return words

def analyze(words, beat):
    beat_words = [NORM.get(w, w) for w in beat.split()]
    idx = 0
    matched = []
    rest_start = None
    for i, (w, s, e, raw) in enumerate(words):
        if idx < len(beat_words) and w == beat_words[idx]:
            matched.append([w, s, e, raw])
            idx += 1
            if idx == len(beat_words):
                rest_start = i + 1
    sub_repeats = []
    singles = []
    if rest_start is not None:
        rest = [w for w, s, e, raw in words[rest_start:]]
        rest_t = words[rest_start:]
        for k in range(len(beat_words)):
            sub = beat_words[k:]
            if len(sub) < 2:
                continue
            for p in range(len(rest) - len(sub) + 1):
                if rest[p:p+len(sub)] == sub:
                    sub_repeats.append({"from_beat_index": k, "sub": sub})
        for w, s, e, raw in rest_t:
            if w in beat_words:
                singles.append({"word": w, "time": [s, e]})
    return matched, rest_start, sub_repeats, singles

def longest_run(mask):
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return int(best)

fname = "mv2_s11lexus_v6gap3_t1.mp4"
beat = "lexus lanes they call them"
song_dur = 1.50
song_words = [(108.02, 108.32), (108.32, 108.74), (108.74, 109.02), (109.02, 109.28), (109.28, 109.52)]
path = str(proj / "takes" / fname)
wav = "/tmp/mv2_v6v16_S11LEX.wav"
words = transcribe(path, wav)
split_half = None
if len(words) == 0:
    w1 = transcribe(path, wav, (0.0, 5.0))
    w2 = transcribe(path, wav, (5.0, 10.0))
    split_half = {"half_0_5": w1, "half_5_10": w2}
    words = w1 + w2
matched, rest_start, sub_repeats, singles = analyze(words, beat)
span = None
ratio = None
drift = None
if matched and len(matched) == len(beat.split()):
    span = [matched[0][1], matched[-1][2]]
    if span[1] > span[0]:
        ratio = round(song_dur / (span[1] - span[0]), 3)
        s0, s1 = span
        t0 = song_words[0][0]
        drifts = []
        for (w, s, e, raw), (ws0, ws1) in zip(matched, song_words):
            mapped = t0 + (0.5 * (s + e) - s0) / (s1 - s0) * song_dur
            drifts.append(round((mapped - 0.5 * (ws0 + ws1)) * 24, 1))
        ds = sorted(drifts)
        drift = {"per_word_frames": drifts,
                 "median": ds[len(ds)//2] if len(ds) % 2 == 1 else round((ds[len(ds)//2 - 1] + ds[len(ds)//2]) / 2, 1),
                 "range": [min(drifts), max(drifts)]}
out = {"S11LEX": {"take": fname, "beat": beat, "song_dur": song_dur,
       "take_words": words, "matched": matched, "vocal_span": span,
       "ratio": ratio, "drift": drift,
       "sub_repeats": sub_repeats, "single_recurrences": singles,
       "split_half": split_half}}
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY16.json").write_text(json.dumps(out, indent=2))
print("S11LEX", fname, "words=", len(words), "matched=", len(matched), "/", len(beat.split()),
      "span=", span, "ratio=", ratio, "drift=", drift,
      "sub_repeats=", sub_repeats, "singles=", singles, "split_half_used=", split_half is not None)

# Frame gate on the vocal span
if span:
    s0, s1 = span
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=160:90,format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    n = len(raw) // (160 * 90)
    frames = _np.frombuffer(raw, dtype=_np.uint8).reshape(n, 160 * 90).astype(_np.int16)
    diffs = _np.array([float(_np.mean(_np.abs(frames[i] - frames[i - 1]))) for i in range(1, n)])
    idx = [i for i in range(1, n) if (i / 24) >= s0 - 0.05 and (i / 24) <= s1 + 0.05]
    vd = diffs[[i - 1 for i in idx]] if idx else _np.array([])
    r = {"take": fname, "sid": "S11LEX", "volley": "16", "vocal_span": [s0, s1],
         "vocal_transitions": int(len(vd)),
         "vocal_changed_gt_0_5": int((vd > 0.5).sum()) if len(vd) else 0,
         "vocal_changed_gt_1_0": int((vd > 1.0).sum()) if len(vd) else 0,
         "vocal_near_dup_run": longest_run(vd < 0.5) if len(vd) else 0,
         "vocal_frozen_run": longest_run(vd < 0.2) if len(vd) else 0,
         "vocal_mean_diff": round(float(vd.mean()), 2) if len(vd) else None}
    r["frame_gate"] = "PASS" if (r["vocal_near_dup_run"] < 24 and (r["vocal_mean_diff"] or 0) >= 0.5) else "FAIL"
    pathlib.Path(proj / "VOCAL_WINDOW_V6V16.json").write_text(json.dumps({fname: r}, indent=2))
    print("FRAME", r)
else:
    print("FRAME skipped: no full matched span")
