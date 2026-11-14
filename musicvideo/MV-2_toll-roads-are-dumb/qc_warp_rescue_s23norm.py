"""S23 warped re-measurement ONLY, with done->dumb normalization.
First-pass qc_warp_rescue.py heard 'done' for 'dumb' on both sped-up S23
warped takes, while the SAME performances unwarped were heard as 'dumb'
(t4 exact, t5 'told roads are dumb'). done->dumb is an established v5
mishear class (WORD_MATCH_V5.json mishear_map). This script re-transcribes
the two warped files with that single extra normalization and writes
TAKE_WORDS_WARP_RESCUE_S23NORM.json. The raw first-pass file is untouched;
the manifest records both raw and normalized results and flags this call.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
from faster_whisper import WhisperModel

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "S23_t4": ("mv2_s23_t4_warped.mp4", "toll roads are dumb", 1.60, 1.26),
    "S23_t5": ("mv2_s23_t5_warped.mp4", "toll roads are dumb", 1.60, 1.27),
}
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay", "tell": "sell",
        "done": "dumb"}
model = WhisperModel("base", device="cpu", compute_type="int8")
out = {}
for sid, (wfile, beat, song_dur, factor) in takes.items():
    path = str(proj / "takes" / wfile)
    wav = f"/tmp/mv2_warp_s23n_{sid}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path,
                    "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    raw_words = []
    words = []
    for seg in segments:
        for w in (seg.words or []):
            raw = w.word.strip().lower().strip(".,!?")
            raw_words.append([raw, round(w.start, 2), round(w.end, 2)])
            words.append([NORM.get(raw, raw), round(w.start, 2), round(w.end, 2)])
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
    if matched and len(matched) == len(beat_words):
        span = [matched[0][1], matched[-1][2]]
        ratio = song_dur / (span[1] - span[0]) if span[1] > span[0] else None
    second = []
    repeat_scan = []
    if rest_start is not None:
        j = 0
        for w, s, e in words[rest_start:]:
            if j < len(beat_words) and w == beat_words[j]:
                second.append([w, s, e])
                j += 1
        rest = [w for w, s, e in words[rest_start:]]
        rest_t = words[rest_start:]
        for k in range(len(beat_words)):
            sub = beat_words[k:]
            for p in range(len(rest) - len(sub) + 1):
                if rest[p:p + len(sub)] == sub:
                    repeat_scan.append({"from_beat_index": k, "sub": sub,
                                        "times": [rest_t[p], rest_t[p + len(sub) - 1]]})
        for w, s, e in rest_t:
            if w in beat_words:
                repeat_scan.append({"single": w, "time": [s, e]})
    out[sid] = {"warped_take": wfile, "beat": beat, "song_dur": song_dur,
                "warp_factor": factor, "raw_words": raw_words,
                "normalized_words": words, "matched": matched,
                "vocal_span": span, "ratio": ratio,
                "second_delivery": second, "repeat_scan": repeat_scan,
                "normalization": "done->dumb (v5 established mishear class)"}
    print(sid, wfile, "raw=", raw_words, "matched=", len(matched), "/",
          len(beat_words), "span=", span, "ratio=", ratio,
          "second=", second, "repeat_scan=", repeat_scan, flush=True)
pathlib.Path(proj / "TAKE_WORDS_WARP_RESCUE_S23NORM.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_WARP_RESCUE_S23NORM.json")
