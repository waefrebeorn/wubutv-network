"""QC transcription + frame gate for MV-2 Q6 restages (S04a, S07, S21).
Adapted from qc_v6_volley17.py (same Whisper base, same mishear map,
same subsequence repeat scan, same split-half rule) and
vocal_window_audit_v13refire.py (160x90 gray, native 24fps, FAIL if vocal
near-dup run >=24 OR vocal mean diff <0.5).
Beats = the v6final beat lines, so assembly word maps stay valid.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
q6 = proj / "work" / "q6"
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
    """Deletion-tolerant subsequence match (volley-18 S21 precedent): a
    beat word may be DROPPED (take skips it) — when the current take word
    equals the NEXT beat word, record the current beat word as dropped
    and continue. Drops are reported, not silently absorbed."""
    beat_words = [NORM.get(w, w) for w in beat.split()]
    idx = 0
    matched = []
    dropped = []
    rest_start = None
    for i, (w, s, e, raw) in enumerate(words):
        if idx < len(beat_words) and w == beat_words[idx]:
            matched.append([w, s, e, raw, idx])
            idx += 1
            if idx == len(beat_words):
                rest_start = i + 1
        elif idx + 1 < len(beat_words) and w == beat_words[idx + 1]:
            dropped.append({"beat_index": idx, "word": beat_words[idx]})
            matched.append([w, s, e, raw, idx + 1])
            idx += 2
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
    return matched, rest_start, sub_repeats, singles, dropped

def longest_run(mask):
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return int(best)

# S04a song spans: from SONG_WORDS_BASE.json; "flaselines," token
# (35.14-35.70) split in half for the take's two words fast/lanes.
S04A_WORDS = [(34.56,34.68),(34.68,34.82),(34.82,34.96),(34.96,35.14),
 (35.14,35.42),(35.42,35.70),(35.92,36.02),(36.02,36.22),(36.22,36.62),
 (36.62,37.04),(37.04,37.44),(37.44,37.84),(37.84,38.20),(38.20,38.44),
 (38.44,38.70),(38.70,39.10),(39.10,39.28),(39.28,39.58),(40.06,40.36),
 (40.44,40.58),(40.58,40.94),(40.94,41.30)]
S07_WORDS = [(72.28,73.14),(73.14,73.24),(73.24,74.86),(74.86,75.90),(75.90,76.78),
 (76.78,77.68),(78.94,79.80),(79.80,80.16),(80.16,80.46),(80.46,80.78)]
S21_WORDS = [(205.20,205.66),(205.66,206.22),(206.22,206.64),(206.64,207.70),
 (208.36,209.16),(209.16,209.96),(209.96,210.22),(210.22,211.18),(211.18,212.60),
 (212.60,212.88),(212.88,213.26),(213.26,213.56),(213.56,213.80),(213.80,214.44)]

SLOTS = [
    ("S04a", "mv2_s04a_q6_t1.mp4", "now they got the fast lanes the rich ones fly on by while the rest of us crawl watching money flash by", 6.74, S04A_WORDS),
    ("S07", "mv2_s07_q6_t1.mp4", "we've been slamming the danger roads toll roads are dumb", 8.50, S07_WORDS),
    ("S21", "mv2_s21_q6_t1.mp4", "the wrecks just come pay to go faster to the rest of us slow", 9.24, S21_WORDS),
]
out = {}
frames = {}
for sid, fname, beat, song_dur, song_words in SLOTS:
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_q6_{sid}.wav"
    words = transcribe(path, wav)
    split_half = None
    if len(words) == 0:
        w1 = transcribe(path, wav, (0.0, 5.0))
        w2 = transcribe(path, wav, (5.0, 10.0))
        split_half = {"half_0_5": w1, "half_5_10": w2}
        words = w1 + w2
    matched, rest_start, sub_repeats, singles, dropped = analyze(words, beat)
    span = None; ratio = None; drift = None
    if matched and rest_start is not None:
        span = [matched[0][1], matched[-1][2]]
        if span[1] > span[0]:
            ratio = round(song_dur / (span[1] - span[0]), 3)
            s0, s1 = span
            t0 = song_words[0][0]
            drifts = []
            for (w, s, e, raw, bi), (ws0, ws1) in zip(matched, [song_words[b[4]] for b in matched]):
                mapped = t0 + (0.5 * (s + e) - s0) / (s1 - s0) * song_dur
                drifts.append(round((mapped - 0.5 * (ws0 + ws1)) * 24, 1))
            ds = sorted(drifts)
            drift = {"per_word_frames": drifts,
                     "median": ds[len(ds)//2] if len(ds) % 2 == 1 else round((ds[len(ds)//2 - 1] + ds[len(ds)//2]) / 2, 1),
                     "range": [min(drifts), max(drifts)]}
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
           "take_words": words, "matched": matched, "vocal_span": span,
           "ratio": ratio, "drift": drift,
           "sub_repeats": sub_repeats, "single_recurrences": singles,
           "dropped_beat_words": dropped,
           "split_half": split_half}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat.split()),
          "span=", span, "ratio=", ratio, "drift=", drift,
          "sub_repeats=", sub_repeats, "singles=", singles, "dropped=", dropped, "split_half_used=", split_half is not None)
    if span:
        s0, s1 = span
        cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=160:90,format=gray",
               "-f", "rawvideo", "-pix_fmt", "gray", "-"]
        raw = subprocess.run(cmd, capture_output=True, check=True).stdout
        n = len(raw) // (160 * 90)
        fr = _np.frombuffer(raw, dtype=_np.uint8).reshape(n, 160 * 90).astype(_np.int16)
        diffs = _np.array([float(_np.mean(_np.abs(fr[i] - fr[i - 1]))) for i in range(1, n)])
        idx = [i for i in range(1, n) if (i / 24) >= s0 - 0.05 and (i / 24) <= s1 + 0.05]
        vd = diffs[[i - 1 for i in idx]] if idx else _np.array([])
        r = {"take": fname, "sid": sid, "volley": "Q6", "vocal_span": [s0, s1],
             "vocal_transitions": int(len(vd)),
             "vocal_changed_gt_0_5": int((vd > 0.5).sum()) if len(vd) else 0,
             "vocal_changed_gt_1_0": int((vd > 1.0).sum()) if len(vd) else 0,
             "vocal_near_dup_run": longest_run(vd < 0.5) if len(vd) else 0,
             "vocal_frozen_run": longest_run(vd < 0.2) if len(vd) else 0,
             "vocal_mean_diff": round(float(vd.mean()), 2) if len(vd) else None}
        r["frame_gate"] = "PASS" if (r["vocal_near_dup_run"] < 24 and (r["vocal_mean_diff"] or 0) >= 0.5) else "FAIL"
        frames[fname] = r
        print("FRAME", r)
    else:
        print("FRAME skipped: no full matched span")
(q6 / "TAKE_WORDS_V6_Q6.json").write_text(json.dumps(out, indent=2))
(q6 / "VOCAL_WINDOW_V6Q6.json").write_text(json.dumps(frames, indent=2))
print("wrote work/q6/TAKE_WORDS_V6_Q6.json + work/q6/VOCAL_WINDOW_V6Q6.json")
