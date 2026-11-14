"""Warp-rescue QC, Batch 2 (v5-era greys) — same pattern as qc_warp_rescue.py.
Beat lines are the v5 PROMPT lines from WORD_MATCH_V5.json. Song spans are
first-word onset to last-word end in SONG_WORDS_BASE.json at the v5
song_span indices. Normalization: v6 classes (tall/told/toe=toll,
paid=pay, tell=sell) PLUS the v5 mishear map entries that apply here
(done=dumb, down=dumb) — both are established v5 classes, recorded in
WORD_MATCH_V5.json mishear_map. robes=roads is PROPOSED only — NOT
normalized. S17's 'meaner' garble ('me in her') is NOT normalized: a
garbled middle word is a failed clean delivery, recorded as such.
Split-half rule applies as in Batch 1. Writes TAKE_WORDS_WARP_RESCUE_B2.json.
"""
import json, pathlib, subprocess
import wave as _wave
import numpy as _np
from faster_whisper import WhisperModel

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb"
# slot, warped file, source file, beat, song span (s), warp factor, v5 ratio
takes = {
    "S09": ("mv2_s09_t2_warped.mp4", "mv2_s09_t2.mp4",
            "express lanes look clean merges get hot", 3.32, 1.0843, 0.7378),
    "S20": ("mv2_s20_t2_warped.mp4", "mv2_s20_t2.mp4",
            "toll roads are dumb", 1.78, 1.1236, 0.7120),
    "S17": ("mv2_s17_t2_warped.mp4", "mv2_s17_t2.mp4",
            "road gets meaner every time one lane flying other stuck", 5.60, 1.3085, 0.6114),
    "S14": ("mv2_s14_t2_warped.mp4", "mv2_s14_t2.mp4",
            "fast lanes make crashes wrecks just come", 6.46, 0.9713, 1.2869),
    "S19": ("mv2_s19_t2_warped.mp4", "mv2_s19_t2.mp4",
            "fast lanes make crashes wrecks just come", 6.62, 0.9667, 1.2930),
    "S15": ("mv2_s15_t2_warped.mp4", "mv2_s15_t2.mp4",
            "they just keep coming", 4.16, 0.9255, 1.3506),
    "S18": ("mv2_s18_t1_warped.mp4", "mv2_s18_t1.mp4",
            "somebody's going to get it when timing's up oh toll roads are dumb", 7.26, 0.8712, 1.4348),
}
NORM = {"tall": "toll", "told": "toll", "toe": "toll", "paid": "pay", "tell": "sell",
        "done": "dumb", "down": "dumb",
        "timings": "timing's"}  # v5 record: take 'timings' covers song timing's
model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_file(path, tag):
    wav = f"/tmp/mv2_warpb2_{tag}.wav"
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
    out = []
    for half, (ss, to) in enumerate([(0, 5), (5, None)]):
        wav = f"/tmp/mv2_warpb2_{tag}_h{half}.wav"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", path]
        if to is not None:
            cmd += ["-t", str(to - ss)]
        cmd += ["-ac", "1", "-ar", "16000", wav]
        subprocess.run(cmd, check=True)
        with _wave.open(wav) as wf:
            frames = wf.readframes(wf.getnframes())
        audio = _np.frombuffer(frames, dtype=_np.int16).astype(_np.float32) / 32768.0
        segments, _ = model.transcribe(audio, word_timestamps=True, language="en")
        for seg in segments:
            for w in (seg.words or []):
                txt = w.word.strip().lower().strip(".,!?")
                txt = NORM.get(txt, txt)
                out.append([txt, round(w.start + ss, 2), round(w.end + ss, 2)])
    return out

out = {}
for sid, (wfile, sfile, beat, song_dur, factor, v5_ratio) in takes.items():
    path = str(proj / "takes" / wfile)
    words = transcribe_file(path, sid)
    split_used = False
    if len(words) == 0:
        words = transcribe_split(path, sid)
        split_used = True
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
                "song_dur": song_dur, "warp_factor": factor, "v5_ratio": v5_ratio,
                "take_words": words, "matched": matched, "vocal_span": span,
                "ratio": ratio, "second_delivery": second,
                "repeat_scan": repeat_scan, "split_half_used": split_used}
    print(sid, wfile, "words=", len(words), "matched=", len(matched), "/",
          len(beat_words), "span=", span, "ratio=", ratio,
          "second=", second, "repeat_scan=", repeat_scan,
          "split_half=", split_used, flush=True)

pathlib.Path(proj / "TAKE_WORDS_WARP_RESCUE_B2.json").write_text(json.dumps(out, indent=2))
print("wrote TAKE_WORDS_WARP_RESCUE_B2.json")
