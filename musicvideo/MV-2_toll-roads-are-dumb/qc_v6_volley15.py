"""QC transcription for MV-2 v6 volley 15 gap takes — faster-whisper base,
word timestamps. Prompt-grounded: take words matched in order to the scene's
own BEAT line only, never cross-line. Vocal span = first matched word onset
to last matched word end. Ratio = song span / take span. Known Whisper
mishear classes normalized before matching: tall=told=toe=toll, done=dumb
in hook, paid=pay, plasers=plazas, comin'=coming, tell=sell.
Second-delivery check + subsequence repeat scan over the RAW word list
(subsequence length >=2 = defect; single-word recurrences noted separately).
SPLIT-HALF recheck if any take returns zero words full-clip.
Drift: linear fit-map of take vocal span onto song span; per matched word,
mapped midpoint vs song word midpoint, in 24fps frames.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "GAPB": ("mv2_gapb_v6gap2_t1.mp4", "they say the paid side is safer the free side takes the hit", 3.34,
             [(100.26, 100.28), (100.28, 100.42), (100.42, 100.58), (100.58, 100.82), (100.82, 101.16), (101.16, 101.40), (101.40, 101.84), (102.10, 102.30), (102.30, 102.52), (102.52, 102.82), (102.82, 103.08), (103.08, 103.38), (103.38, 103.60)]),
    "HOOK": ("mv2_hook_v6gap2_t1.mp4", "toll roads are dumb baby", 2.64,
             [(50.84, 51.84), (51.84, 52.08), (52.08, 52.40), (52.40, 52.76), (53.22, 53.48)]),
    "S12MID": ("mv2_s12mid_v6gap2_t1.mp4", "used to kill and electronic helps a bit but the", 2.58,
               [(115.60, 115.82), (115.82, 116.04), (116.04, 116.26), (116.26, 116.40), (116.40, 116.70), (116.70, 117.18), (117.18, 117.34), (117.34, 117.56), (117.90, 118.06), (118.06, 118.18)]),
    "S11LEX": ("mv2_s11lexus_v6gap2_t1.mp4", "lexus lanes they call them", 1.50,
               [(108.02, 108.32), (108.32, 108.74), (108.74, 109.02), (109.02, 109.28), (109.28, 109.52)]),
    "S02BABY": ("mv2_s02baby_v6gap2_t1.mp4", "baby make", 0.58,
                [(22.10, 22.38), (22.54, 22.68)]),
}
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
    # Normalize beat words through the same map: a class like paid=pay must
    # not break an exact match when both sides say "paid" (volley-15 GAPB fix).
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

out = {}
for sid, (fname, beat, song_dur, song_words) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6v15_{sid}.wav"
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
            # fit-map drift per word
            s0, s1 = span
            t0 = song_words[0][0]
            drifts = []
            for (w, s, e, raw), (ws0, ws1) in zip(matched, song_words):
                mapped = t0 + (0.5 * (s + e) - s0) / (s1 - s0) * song_dur
                drifts.append(round((mapped - 0.5 * (ws0 + ws1)) * 24, 1))
            drifts_sorted = sorted(drifts)
            drift = {"per_word_frames": drifts,
                     "median": drifts_sorted[len(drifts_sorted)//2] if len(drifts_sorted) % 2 == 1 else round((drifts_sorted[len(drifts_sorted)//2 - 1] + drifts_sorted[len(drifts_sorted)//2]) / 2, 1),
                     "range": [min(drifts), max(drifts)]}
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span,
                "ratio": ratio, "drift": drift,
                "sub_repeats": sub_repeats, "single_recurrences": singles,
                "split_half": split_half}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat.split()),
          "span=", span, "ratio=", ratio, "drift=", drift,
          "sub_repeats=", sub_repeats, "singles=", singles,
          "split_half_used=", split_half is not None, flush=True)
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY15.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY15.json")
