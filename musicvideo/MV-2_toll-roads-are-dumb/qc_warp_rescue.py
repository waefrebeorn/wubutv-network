"""Warp-rescue QC for MV-2 v6 greys (2026-11-03) — NO generation, QC only.
Pattern follows qc_v6_volley12.py: faster-whisper base, av-bypass
(ffmpeg to wav, then ndarray). Prompt-grounded: take words matched in
order to the scene's own BEAT line only, never cross-line. Vocal span =
first matched word onset to last matched word end.
Ratio = song span / take span. Known Whisper mishear classes normalized
before matching: tall=toll, told=toll, toe=toll, paid=pay, tell=sell.
TOWROADS is a toll+roads slur (volley-12 precedent): one token satisfying
two consecutive beat words. robes=roads is PROPOSED only — NOT normalized.
Split-half rule: a zero-word full-clip result is NOT a no-line verdict —
split-half recheck first (0-5s / 5-10s halves, second half offset +5s).
Second-delivery check: after a full beat match, scan remaining words for
a repeat of the beat. RAW word list must also be read for repeat-tail
defects: any beat-word subsequence (len>=2) or single beat word recurring
in the remaining words (volley-11/12 pattern).
Writes TAKE_WORDS_WARP_RESCUE.json (new file; never overwrites volley files).
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
from faster_whisper import WhisperModel

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
# slot, warped file, source file, beat, song span, warp factor
takes = {
    "S16_t7": ("mv2_s16_t7_warped.mp4", "mv2_s16_t7.mp4",
               "sell you speed for a dollar and a dime", 3.02, 1.059603),
    "S16_t8": ("mv2_s16_t8_warped.mp4", "mv2_s16_t8.mp4",
               "sell you speed for a dollar and a dime", 3.02, 1.335099),
    "S22_t4": ("mv2_s22_t4_warped.mp4", "mv2_s22_t4.mp4",
               "toll roads are done", 2.20, 0.965909),
    "R4_t2": ("mv2_r4_t2_warped.mp4", "mv2_r4_t2.mp4",
              "toll roads are done", 2.42, 1.090909),
    "R3_t4": ("mv2_r3_t4_warped.mp4", "mv2_r3_t4.mp4",
              "toll roads are done", 2.16, 1.207407),
    "R6_t4": ("mv2_r6_t4_warped.mp4", "mv2_r6_t4.mp4",
              "toll roads are done", 2.18, 1.269725),
    "S23_t4": ("mv2_s23_t4_warped.mp4", "mv2_s23_t4.mp4",
               "toll roads are dumb", 1.60, 1.26),
    "S23_t5": ("mv2_s23_t5_warped.mp4", "mv2_s23_t5.mp4",
               "toll roads are dumb", 1.60, 1.27),
    "S23_t6": ("mv2_s23_t6_warped.mp4", "mv2_s23_t6.mp4",
               "toll roads are dumb", 1.60, 1.29),
}
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay", "tell": "sell"}
EXPAND = {"towroads": ["toll", "roads"]}  # one token, two beat words

model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_file(path, tag):
    wav = f"/tmp/mv2_warp_{tag}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path,
                    "-ac", "1", "-ar", "16000", wav], check=True)
    with _wave.open(wav) as wf:
        frames = wf.readframes(wf.getnframes())
    audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
    segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
    words = []
    for seg in segments:
        for w in (seg.words or []):
            txt = w.word.strip().lower().strip(".,!?")
            txt = NORM.get(txt, txt)
            words.append([txt, round(w.start, 2), round(w.end, 2)])
    return words

def transcribe_split(path, tag):
    """Split-half recheck: 0-5s and 5s-end halves, second offset +5s."""
    out = []
    for half, (ss, to) in enumerate([(0, 5), (5, None)]):
        wav = f"/tmp/mv2_warp_{tag}_h{half}.wav"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", path]
        if to is not None:
            cmd += ["-t", str(to - ss)]
        cmd += ["-ac", "1", "-ar", "16000", wav]
        subprocess.run(cmd, check=True)
        with _wave.open(wav) as wf:
            frames = wf.readframes(wf.getnframes())
        audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
        segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
        off = ss
        for seg in segments:
            for w in (seg.words or []):
                txt = w.word.strip().lower().strip(".,!?")
                txt = NORM.get(txt, txt)
                out.append([txt, round(w.start + off, 2), round(w.end + off, 2)])
    return out

def match_beat(words, beat_words):
    """In-order match; a token may satisfy several consecutive beat words
    if it is in EXPAND. Returns (matched, rest_start_index)."""
    idx = 0
    matched = []
    rest_start = None
    for i, (w, s, e) in enumerate(words):
        if idx >= len(beat_words):
            break
        if w in EXPAND and EXPAND[w] == beat_words[idx:idx + len(EXPAND[w])]:
            for bw in EXPAND[w]:
                matched.append([bw, s, e])
                idx += 1
            if idx == len(beat_words):
                rest_start = i + 1
        elif w == beat_words[idx]:
            matched.append([w, s, e])
            idx += 1
            if idx == len(beat_words):
                rest_start = i + 1
    return matched, rest_start

out = {}
for sid, (wfile, sfile, beat, song_dur, factor) in takes.items():
    path = str(proj / "takes" / wfile)
    words = transcribe_file(path, sid)
    split_half = None
    if len(words) == 0:
        split_half = transcribe_split(path, sid)
        words = split_half
    beat_words = beat.split()
    matched, rest_start = match_beat(words, beat_words)
    span = None
    ratio = None
    if matched and len(matched) == len(beat_words):
        span = [matched[0][1], matched[-1][2]]
        ratio = song_dur / (span[1] - span[0]) if span[1] > span[0] else None
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
                if rest[p:p + len(sub)] == sub:
                    repeat_scan.append({"from_beat_index": k, "sub": sub,
                                        "times": [rest_t[p], rest_t[p + len(sub) - 1]]})
        for w, s, e in rest_t:
            if w in beat_words:
                repeat_scan.append({"single": w, "time": [s, e]})
    out[sid] = {"warped_take": wfile, "source_take": sfile, "beat": beat,
                "song_dur": song_dur, "warp_factor": factor,
                "take_words": words, "matched": matched, "vocal_span": span,
                "ratio": ratio, "second_delivery": second,
                "repeat_scan": repeat_scan, "split_half_used": split_half is not None}
    print(sid, wfile, "words=", len(words), "matched=", len(matched), "/",
          len(beat_words), "span=", span, "ratio=", ratio,
          "second=", second, "repeat_scan=", repeat_scan,
          "split_half=", split_half is not None, flush=True)

pathlib.Path(proj / "TAKE_WORDS_WARP_RESCUE.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_WARP_RESCUE.json")
