"""QC transcription for MV-2 v6 volley 12 — faster-whisper base, word timestamps.
Prompt-grounded: take words matched in order to the scene's own BEAT line
only, never cross-line. Vocal span = first matched word onset to last
matched word end. Ratio = song span / take span. Known Whisper mishear
classes normalized before matching: tall=toll, told=toll, toe=toll,
paid=pay. Song spans from SONG_WORDS_BASE.json (v5 verified) and
V6_10S_CUT_PLAN.md. Second-delivery check: after a full beat match, scan
remaining words for a repeat of the beat. RAW word list must also be read
for repeat-tail defects (a repeated final word, or a partial-line tail
starting mid-line, slips past the full-line scan — see R4 t4, S22 t2,
S16 t6). repeat_scan flags any beat-word subsequence (len>=2) or single
beat word recurring in the remaining words.
"""
import json, pathlib, subprocess
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "S16": ("mv2_s16_t7.mp4", "sell you speed for a dollar and a dime", 3.02),
    "S22": ("mv2_s22_t4.mp4", "toll roads are done", 2.20),
    "R4": ("mv2_r4_t7.mp4", "toll roads are done", 2.42),
    "R3": ("mv2_r3_t8.mp4", "toll roads are done", 2.16),
    "R6": ("mv2_r6_t6.mp4", "toll roads are done", 2.18),
    "S23": ("mv2_s23_t8.mp4", "toll roads are dumb", 1.60),
}
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
import wave as _wave
import numpy as _np
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay", "tell": "sell"}
out = {}
for sid, (fname, beat, song_dur) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6v12_{sid}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?")
            txt = NORM.get(txt, txt)
            if txt == "we've":
                words.append(["we", round(w.start, 2), round(w.start, 2)])
                words.append(["have", round(w.start, 2), round(w.end, 2)])
            else:
                words.append([txt, round(w.start, 2), round(w.end, 2)])
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
        ratio = round(song_dur / (span[1] - span[0]), 2) if span[1] > span[0] else None
    second = []
    if rest_start is not None:
        j = 0
        for w, s, e in words[rest_start:]:
            if j < len(beat_words) and w == beat_words[j]:
                second.append([w, s, e])
                j += 1
    # subsequence repeat scan over remaining words
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
        # single-word recurrences (final-word tail class)
        for w, s, e in rest_t:
            if w in beat_words:
                repeat_scan.append({"single": w, "time": [s, e]})
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span, "ratio": ratio,
                "second_delivery": second, "repeat_scan": repeat_scan}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat_words),
          "span=", span, "ratio=", ratio, "second_delivery=", second,
          "repeat_scan=", repeat_scan, flush=True)
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY12.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY12.json")
