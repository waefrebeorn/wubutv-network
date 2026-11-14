"""QC transcription for MV-2 v6 volley 1 — faster-whisper base, word timestamps.
Prompt-grounded: take words are matched in order to the scene's own BEAT line
only (lyrics.txt wording for that scene), never cross-line. Vocal span =
first matched word onset to last matched word end. Ratio = song span / take span.
Song spans (from SONG_WORDS_BASE.json anchors, v5 verified):
 S13 122.92-124.44 (1.52s)  S23 230.22-231.60 (1.38s)  S05 50.84-52.76 (1.92s)
 S10 96.80-99.98 (3.18s)   S16 165.92-168.94 (3.02s)  S08 88.48-93.10 (4.62s)
"""
import json, pathlib, subprocess, sys
proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
takes = {
    "S13": ("mv2_s13_t3.mp4", "toll roads are dumb", 1.52),
    "S23": ("mv2_s23_t2.mp4", "toll roads are dumb", 1.38),
    "S05": ("mv2_s05_t5.mp4", "toll roads are dumb", 1.92),
    "S10": ("mv2_s10_t2.mp4", "speed up cut over somebody gets caught", 3.18),
    "S16": ("mv2_s16_t2.mp4", "sell you speed for a dollar and a dime", 3.02),
    "S08": ("mv2_s08_t3.mp4", "they just keep coming", 4.62),
}
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")
out = {}
import wave as _wave
import numpy as _np
for sid, (fname, beat, song_dur) in takes.items():
    path = str(proj / "takes" / fname)
    wav = f"/tmp/mv2_v6_{sid}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append([w.word.strip().lower().strip(".,!?"), round(w.start, 2), round(w.end, 2)])
    # prompt-grounded match: find beat words in order in take words
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
pathlib.Path(proj / "TAKE_WORDS_V6_VOLLEY1.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_V6_VOLLEY1.json")
