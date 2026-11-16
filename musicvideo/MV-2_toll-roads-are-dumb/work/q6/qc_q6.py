"""Q6 QC: transcribe + lyric/ratio/frame gates for the three Q6 restage takes.
Adapted from qc_v6_volley17.py (same Whisper base int8, same mishear map,
same subsequence repeat scan, same split-half rule; frame gate 160x90 gray
native 24fps, FAIL if vocal near-dup run >=24 OR vocal mean diff <0.5).
Beats: S07 performed line; S21 with BOTH 'to's; S04a 22 words incl lead.
Song-word windows pulled from SONG_WORDS_BASE.json by sequence match.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "done": "dumb", "paid": "pay",
        "plasers": "plazas", "comin": "coming", "tell": "sell",
        "flaselines": "fast lanes"}

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

# song-word windows from SONG_WORDS_BASE by sequence match on the beat
song = json.load(open(proj / "SONG_WORDS_BASE.json"))
song_words_all = song if isinstance(song, list) else song["words"]
song_norm = [NORM.get(x["word"].strip().lower().strip(".,!?"), x["word"].strip().lower().strip(".,!?")) for x in song_words_all]
# "fast lanes" is two song tokens vs beat "fast"+"lanes": handle by splitting
def find_window(beat):
    bw = [NORM.get(w, w) for w in beat.split()]
    for start in range(len(song_norm) - len(bw) + 1):
        if song_norm[start:start+len(bw)] == bw:
            ws = song_words_all[start:start+len(bw)]
            return [(x["t0"], x["t1"]) for x in ws]
    return None

SLOTS = [
    ("S07", "mv2_s07_q6_t1.mp4", "we've been slamming the danger roads toll roads are dumb", 8.50),
    ("S21", "mv2_s21_q6_t1.mp4", "the wrecks just come pay to go faster to the rest of us slow", 9.24),
    ("S04a", "mv2_s04a_q6_t1.mp4", "now they got the fast lanes the rich ones fly on by while the rest of us crawl watching money flash by", 6.74),
]
out = {}
for sid, fname, beat, song_dur in SLOTS:
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_q6_{sid}.wav"
    words = transcribe(path, wav)
    split_half = None
    if len(words) == 0:
        w1 = transcribe(path, wav, (0.0, 5.0))
        w2 = transcribe(path, wav, (5.0, 10.0))
        split_half = {"half_0_5": w1, "half_5_10": w2}
        words = w1 + w2
    matched, rest_start, sub_repeats, singles = analyze(words, beat)
    song_win = find_window(beat)
    span = None; ratio = None; drift = None
    if matched and len(matched) == len(beat.split()):
        span = [matched[0][1], matched[-1][2]]
        if span[1] > span[0]:
            ratio = round(song_dur / (span[1] - span[0]), 3)
            if song_win:
                s0, s1 = span
                t0 = song_win[0][0]
                drifts = []
                for (w, s, e, raw), (ws0, ws1) in zip(matched, song_win):
                    mapped = t0 + (0.5 * (s + e) - s0) / (s1 - s0) * song_dur
                    drifts.append(round((mapped - 0.5 * (ws0 + ws1)) * 24, 1))
                ds = sorted(drifts)
                drift = {"per_word_frames": drifts,
                         "median": ds[len(ds)//2] if len(ds) % 2 == 1 else round((ds[len(ds)//2 - 1] + ds[len(ds)//2]) / 2, 1),
                         "range": [min(drifts), max(drifts)]}
    frame_gate = None
    if span:
        s0, s1 = span
        cmd = ["ffmpeg", "-v", "error", "-i", path, "-vf", "scale=160:90,format=gray",
               "-f", "rawvideo", "-pix_fmt", "gray", "-"]
        raw = subprocess.run(cmd, capture_output=True, check=True).stdout
        n = len(raw) // (160 * 90)
        fr = _np.frombuffer(raw, dtype=_np.uint8).reshape(n, 160 * 90).astype(_np.int16)
        d = _np.abs(_np.diff(fr, axis=0)).mean(axis=1)
        i0, i1 = int(s0 * 24), int(s1 * 24)
        voc = d[i0:max(i0 + 1, i1)]
        near = voc < 0.2
        frame_gate = {"mean": round(float(voc.mean()), 3), "neardup_run": longest_run(near),
                      "frozen_run": longest_run(voc < 0.05), "frames": int(len(voc))}
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span,
                "ratio": ratio, "drift": drift, "song_window": song_win,
                "sub_repeats": sub_repeats, "single_recurrences": singles,
                "split_half": split_half, "frame_gate": frame_gate}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat.split()),
          "span=", span, "ratio=", ratio, "drift=", drift,
          "frame=", frame_gate, "sub_repeats=", sub_repeats, "singles=", singles,
          "split_half_used=", split_half is not None, flush=True)
json.dump(out, open(proj / "TAKE_WORDS_Q6.json", "w"), indent=1)
print("wrote TAKE_WORDS_Q6.json")
