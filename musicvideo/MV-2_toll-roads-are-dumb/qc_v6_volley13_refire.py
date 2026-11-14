"""QC transcription for MV-2 v6 volley 13 REFIRE takes — faster-whisper base,
word timestamps. Prompt-grounded: take words matched in order to the scene's
own BEAT line only, never cross-line. Vocal span = first matched word onset
to last matched word end. Ratio = song span / take span. Known Whisper
mishear classes normalized before matching: tall=told=toe=toll, paid=pay,
tell=sell. Second-delivery check + subsequence/single-word repeat scan over
the RAW word list (a repeated final word or partial-line tail slips past the
full-line scan). SPLIT-HALF recheck handled in a second pass if any take
returns zero words full-clip.
"""
import json, pathlib, subprocess
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "R4": ("mv2_r4_t8.mp4", "toll roads are done", 2.42),
    "R3": ("mv2_r3_t9.mp4", "toll roads are done", 2.16),
    "R6": ("mv2_r6_t7.mp4", "toll roads are done", 2.18),
    "S23": ("mv2_s23_t9.mp4", "toll roads are dumb", 1.60),
}
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
import wave as _wave
import numpy as _np
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay", "tell": "sell"}

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
            txt = NORM.get(txt, txt)
            off = audio_range[0] if audio_range else 0.0
            if txt == "we've":
                words.append(["we", round(w.start + off, 2), round(w.start + off, 2)])
                words.append(["have", round(w.start + off, 2), round(w.end + off, 2)])
            else:
                words.append([txt, round(w.start + off, 2), round(w.end + off, 2)])
    return words

def analyze(words, beat):
    beat_words = beat.split()
    idx = 0
    matched = []
    rest_start = None
    for i, (w, s, e) in enumerate(words):
        if idx < len(beat_words) and w == beat_words[idx]:
            matched.append([w, s, e])
            idx += 1
            if idx == len(beat_words):
                rest_start = i + 1
    span = None
    ratio = None
    ratio_raw = None
    if matched and len(matched) == len(beat_words):
        span = [matched[0][1], matched[-1][2]]
        if span[1] > span[0]:
            ratio_raw = None  # filled by caller with song_dur
    second = []
    if rest_start is not None:
        j = 0
        for w, s, e in words[rest_start:]:
            if j < len(beat_words) and w == beat_words[j]:
                second.append([w, s, e])
                j += 1
    repeat_scan = []
    if rest_start is not None:
        rest = [w for w, s, e in words[rest_start:]]
        rest_t = words[rest_start:]
        for k in range(len(beat_words)):
            sub = beat_words[k:]
            for p in range(len(rest) - len(sub) + 1):
                if rest[p:p+len(sub)] == sub:
                    repeat_scan.append({"from_beat_index": k, "sub": sub,
                                        "times": [rest_t[p], rest_t[p+len(sub)-1]]})
        for w, s, e in rest_t:
            if w in beat_words:
                repeat_scan.append({"single": w, "time": [s, e]})
    return matched, span, second, repeat_scan

out = {}
for sid, (fname, beat, song_dur) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6v13r_{sid}.wav"
    words = transcribe(path, wav)
    split_half = None
    if len(words) == 0:
        # SPLIT-HALF RULE: zero-word full-clip result is not a no-line verdict
        w1 = transcribe(path, wav, (0.0, 5.0))
        w2 = transcribe(path, wav, (5.0, 10.0))
        split_half = {"half_0_5": w1, "half_5_10": w2}
        words = w1 + w2
    matched, span, second, repeat_scan = analyze(words, beat)
    ratio = None
    ratio_raw = None
    if span and span[1] > span[0]:
        ratio_raw = song_dur / (span[1] - span[0])
        ratio = round(ratio_raw, 2)
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span,
                "ratio": ratio, "ratio_raw": ratio_raw,
                "second_delivery": second, "repeat_scan": repeat_scan,
                "split_half": split_half}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat.split()),
          "span=", span, "ratio=", ratio, "raw=", ratio_raw, "second_delivery=", second,
          "repeat_scan=", repeat_scan, "split_half_used=", split_half is not None, flush=True)
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY13_REFIRE.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY13_REFIRE.json")
