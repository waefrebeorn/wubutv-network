"""QC transcription for MV-2 v6 volley 9 — faster-whisper base, word timestamps.
Prompt-grounded: take words matched in order to the scene's own BEAT line
only, never cross-line. Vocal span = first matched word onset to last
matched word end. Ratio = song span / take span. Known Whisper mishear
classes normalized before matching: tall=toll, told=toll, toe=toll,
paid=pay. Song spans from SONG_WORDS_BASE.json (v5 verified) and
V6_10S_CUT_PLAN.md. S23 ratio reported on both base 1.38s and
re-measured 1.60s song spans. S08 gets a second-delivery check: after a
full beat match, scan remaining words for a repeat of the beat.
"""
import json, pathlib, subprocess
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "S08": ("mv2_s08_t9.mp4", "they just keep coming", 4.62),
    "S16": ("mv2_s16_t5.mp4", "sell you speed for a dollar and a dime", 3.02),
    "R3": ("mv2_r3_t5.mp4", "toll roads are done", 2.16),
    "R4": ("mv2_r4_t4.mp4", "toll roads are done", 2.42),
    "R6": ("mv2_r6_t3.mp4", "toll roads are done", 2.18),
    "R11": ("mv2_r11_t2.mp4", "yeah", 0.78),
}
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
import wave as _wave
import numpy as _np
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay"}
out = {}
for sid, (fname, beat, song_dur) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6v9_{sid}.wav"
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
    # second-delivery check: does the beat recur in the remaining words?
    second = []
    if rest_start is not None:
        j = 0
        for w, s, e in words[rest_start:]:
            if j < len(beat_words) and w == beat_words[j]:
                second.append([w, s, e])
                j += 1
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span, "ratio": ratio,
                "second_delivery": second}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat_words),
          "span=", span, "ratio=", ratio, "second_delivery=", second, flush=True)
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY9.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY9.json")
