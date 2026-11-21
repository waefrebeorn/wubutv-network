"""QC transcription for MV-2 v6 volley 3 — faster-whisper base, word timestamps.
Prompt-grounded: take words matched in order to the scene's own BEAT line
only, never cross-line. Vocal span = first matched word onset to last
matched word end. Ratio = song span / take span. Known Whisper mishear
tall=toll normalized before matching. Song spans from SONG_WORDS_BASE.json
(v5 verified) and V6_10S_CUT_PLAN.md section 4 for the S06 split.
"""
import json, pathlib, subprocess
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "S06a": ("mv2_s06a_t2.mp4", "fast lanes make crashes the wrecks just come", 5.68),
    "S10": ("mv2_s10_t4.mp4", "speed up cut over somebody gets caught", 3.18),
    "S16": ("mv2_s16_t4.mp4", "sell you speed for a dollar and a dime", 3.02),
    "S13": ("mv2_s13_t5.mp4", "toll roads are dumb", 1.52),
    "S23": ("mv2_s23_t4.mp4", "toll roads are dumb", 1.38),
    "S05": ("mv2_s05_t6.mp4", "toll roads are dumb", 1.98),
}
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
out = {}
import wave as _wave
import numpy as _np
for sid, (fname, beat, song_dur) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6v3_{sid}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?")
            if txt == "tall":
                txt = "toll"
            words.append([txt, round(w.start, 2), round(w.end, 2)])
    beat_words = beat.split()
    idx = 0
    matched = []
    for w, s, e in words:
        if idx < len(beat_words) and w == beat_words[idx]:
            matched.append([w, s, e])
            idx += 1
    span = None
    ratio = None
    if matched and len(matched) == len(beat_words):
        span = [matched[0][1], matched[-1][2]]
        ratio = round(song_dur / (span[1] - span[0]), 2) if span[1] > span[0] else None
    out[sid] = {"take": fname, "beat": beat, "song_dur": song_dur,
                "take_words": words, "matched": matched, "vocal_span": span, "ratio": ratio}
    print(sid, fname, "words=", len(words), "matched=", len(matched), "/", len(beat_words),
          "span=", span, "ratio=", ratio, flush=True)
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY3.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY3.json")
