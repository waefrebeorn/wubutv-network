"""MV-4 volley 6 re-check: prompted re-transcription + split-half for S23 t2.
Per the skill: prompted decode may recover garbled words; split-half recheck
before calling any take repeat-less. Sequential, per-take temp wavs.
Also RMS-check the 'pause' token window (2.16-2.38s) in S23 t2.
"""
import json, pathlib, subprocess
import numpy as np

proj = pathlib.Path.home() / "workspace/wubutv-network/musicvideo/MV-4_this-time-its-real"
work = proj / "work" / "qc_volley6"
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
name = "mv4_s23_t2"
line = "Good news, everyone, good news, everyone, the ride is done, the ride is done"
path = proj / "takes" / f"{name}.mp4"
wav = work / f"{name}_recheck.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
words = decode(wav, prompt=line)
print(f"{name} PROMPTED full: {len(words)} words: {' '.join(w['word'] for w in words)}", flush=True)
print(f"  times: {[(w['word'], w['start'], w['end']) for w in words]}", flush=True)
out[name] = {"prompted": words}
for (a, b) in [(0.0, 5.0), (5.0, 10.0)]:
    hw = work / f"{name}_half_{int(a)}_{int(b)}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a),
                    "-i", str(path), "-vn", "-ac", "1", "-ar", "16000", str(hw)], check=True)
    hw_words = decode(hw)
    print(f"{name} half {a}-{b}s: {len(hw_words)} words: {' '.join(w['word'] for w in hw_words)}", flush=True)
    print(f"  times: {[(w['word'], w['start'], w['end']) for w in hw_words]}", flush=True)
    out[name][f"half_{int(a)}_{int(b)}"] = hw_words
    hw.unlink(missing_ok=True)
# RMS per second, to judge the 'pause' token window 2.16-2.38s
audio = load_wav_np(wav)
for s in range(0, 10):
    seg = audio[s * 16000:(s + 1) * 16000]
    rms = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0.0
    print(f"  RMS {s}-{s+1}s: {rms:.4f}", flush=True)
out[name]["rms_per_second"] = [round(float(np.sqrt(np.mean(audio[s*16000:(s+1)*16000]**2))), 4) for s in range(10)]
wav.unlink(missing_ok=True)

(work / "qc_volley6_recheck.json").write_text(json.dumps(out, indent=2))
print("DONE")
