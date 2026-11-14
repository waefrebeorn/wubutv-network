"""MV-4 volley 5 re-check: prompted re-transcription + split-half for S23/S25.
Per the skill: prompted decode may recover garbled words; split-half recheck
before calling any take lineless / repeat-less. Sequential, per-take temp wavs.
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
work = proj / "work" / "qc_volley5"
from faster_whisper import WhisperModel
model = WhisperModel("base", device="cpu", compute_type="int8")

def load_wav_np(wav_path):
    import wave
    with wave.open(str(wav_path), "rb") as w:
        n = w.getnframes()
        raw = w.readframes(n)
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

def decode(wav, prompt=None):
    kw = dict(word_timestamps=True)
    if prompt:
        kw["initial_prompt"] = prompt
    segments, info = model.transcribe(load_wav_np(wav), **kw)
    words = []
    for seg in segments:
        for w in (seg.words or []):
            words.append({"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
    return words

out = {}
for name, line, halves in [
    ("mv4_s23_t1", "Good news, everyone, good news, everyone, the ride is done, the ride is done", [(0.0, 5.0), (5.0, 10.0)]),
    ("mv4_s25_t1", "Futurama's finished, Futurama's finished", [(0.0, 5.0), (5.0, 10.0)]),
]:
    path = proj / "takes" / f"{name}.mp4"
    wav = work / f"{name}_recheck.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                    "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
    words = decode(wav, prompt=line)
    print(f"{name} PROMPTED full: {len(words)} words: {' '.join(w['word'] for w in words)}", flush=True)
    print(f"  times: {[(w['word'], w['start'], w['end']) for w in words]}", flush=True)
    out[name] = {"prompted": words}
    for (a, b) in halves:
        hw = work / f"{name}_half_{int(a)}_{int(b)}.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a),
                        "-i", str(path), "-vn", "-ac", "1", "-ar", "16000", str(hw)], check=True)
        hw_words = decode(hw)
        print(f"{name} half {a}-{b}s: {len(hw_words)} words: {' '.join(w['word'] for w in hw_words)}", flush=True)
        print(f"  times: {[(w['word'], w['start'], w['end']) for w in hw_words]}", flush=True)
        out[name][f"half_{int(a)}_{int(b)}"] = hw_words
        hw.unlink(missing_ok=True)
    wav.unlink(missing_ok=True)

(work / "qc_volley5_recheck.json").write_text(json.dumps(out, indent=2))
print("DONE")
