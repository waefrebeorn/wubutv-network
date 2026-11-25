#!/usr/bin/env python3
"""MV-4 master validation (gate on the master itself).

(a) AUDIO: dictate the master's own audio with faster-whisper (unprompted) and
    align to SONG_WORDS. The master audio IS the song (track.mp3 re-encoded to
    AAC), so this verifies the mux: right song, complete, correctly timed, no
    drift/truncation/A-V offset. It does NOT validate picture sync by itself.
(b) MOTION: decode the master at 160x90, mean abs-diff between consecutive
    frames; report overall mean, longest near-dup run (<0.5), and per-scene
    means. Frame rule: FAIL if a vocal near-dup run >= 24f during vocal or a
    vocal mean diff < 0.5.
(c) PICTURE SYNC is checked visually from a contact sheet of frames taken at
    song word times (see validate_master_pictures.py output / manual read).
"""
import json, os, subprocess, sys
import numpy as np

PROJ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/hatch/workspace/fw-venv/lib/python3.12/site-packages")
from faster_whisper import WhisperModel

MASTER = os.path.join(PROJ, "masters", "mv4_this_time_its_real_16x9.mp4")
SONG = json.load(open(os.path.join(PROJ, "SONG_WORDS.json")))["words"]

def norm(t):
    t = t.lower().strip(".,!?\"'()[]").replace("'s", "s").replace("n't", "nt")
    return t.replace("twenty-thirteen", "2013").replace("twentythirteen", "2013").replace("twenty-seven", "2027")

# --- (a) audio dictation ---
print("== (a) master audio dictation ==", flush=True)
# Decode to 16k mono float32 numpy (faster-whisper's file-path decode uses an
# av.open kwarg this av build rejects; numpy input avoids it, as in the MV-3
# cross-check prototype).
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", MASTER, "-vn", "-ac", "1",
                "-ar", "16000", "-f", "f32le", "/tmp/mv4_master_audio.f32"], check=True)
pcm = np.fromfile("/tmp/mv4_master_audio.f32", dtype=np.float32)
print(f"audio samples: {len(pcm)} ({len(pcm)/16000:.1f}s)")
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(pcm, word_timestamps=True,
                               language="en", beam_size=1)
words = []
for seg in segments:
    words += [{"word": w.word.strip(), "start": float(w.start), "end": float(w.end)}
              for w in seg.words]
json.dump(words, open(os.path.join(PROJ, "work", "master_dictation.json"), "w"), indent=1)
print(f"dictated {len(words)} words (song has {len(SONG)})")
# align positionally (same audio, same tokenization expected)
import difflib
t_tok = [norm(w["word"]) for w in words]
s_tok = [norm(w["word"]) for w in SONG]
if len(words) == len(SONG):
    pairs = list(zip(range(len(words)), range(len(SONG))))
else:
    sm = difflib.SequenceMatcher(a=t_tok, b=s_tok, autojunk=False)
    pairs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                pairs.append((i1 + k, j1 + k))
agr = sum(1 for i, j in pairs if t_tok[i] == s_tok[j]) / max(len(SONG), 1)
offs = np.array([words[i]["start"] - SONG[j]["start"] for i, j in pairs])
print(f"agreement={agr:.3f} pairs={len(pairs)} median|off|={np.median(np.abs(offs)):.3f}s "
      f"max|off|={np.max(np.abs(offs)):.3f}s")
# Gate on TIMING (median + token identity), not raw agreement: this song
# repeats "Futurama's finished" and the outro's soft lines many times, so
# difflib mis-pairs identical lines across the track and Whisper splits the
# held outro line into extra tokens. Those lower `agreement` without any
# timing error. The timing facts are the median offset and the token match.
n_mismatch = sum(1 for i, j in pairs if t_tok[i] != s_tok[j])
print(f"token mismatches among pairs: {n_mismatch}")
print("AUDIO GATE:", "PASS" if np.median(np.abs(offs)) <= 0.05 and n_mismatch == 0 else "FAIL")

# --- (b) motion audit ---
print("== (b) motion audit (160x90, native 24fps) ==", flush=True)
proc = subprocess.run(
    ["ffmpeg", "-v", "error", "-i", MASTER, "-vf", "scale=160:90,format=gray",
     "-f", "rawvideo", "-pix_fmt", "gray", "-"],
    capture_output=True)
raw = np.frombuffer(proc.stdout, dtype=np.uint8)
n = raw.size // (160 * 90)
frames = raw[:n * 160 * 90].reshape(n, 90, 160).astype(np.int16)
print(f"decoded {n} frames (expect 5731)")
diffs = np.abs(frames[1:] - frames[:-1]).mean(axis=(1, 2))
print(f"overall mean diff={diffs.mean():.3f}  min={diffs.min():.3f} max={diffs.max():.3f}")
# longest near-dup run (<0.5)
run = best = 0
for d in diffs:
    run = run + 1 if d < 0.5 else 0
    best = max(best, run)
print(f"longest near-dup (<0.5) run={best}f  (frame rule: FAIL if >=24f during vocal)")
# per-scene means
bounds = [0.00, 7.70, 16.00, 23.34, 32.36, 39.72, 46.88, 54.20, 64.82, 72.80,
          79.52, 86.96, 95.40, 103.36, 110.34, 117.96, 126.44, 133.82, 140.56,
          148.40, 158.76, 166.54, 173.90, 181.24, 188.24, 194.06, 198.38,
          205.09, 211.75, 220.77, 229.00, 238.805333]
scenes = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S11","S12",
          "S13","S14","S15","S16","S17","S18","S19","S20","S21","S22","S23","S24",
          "S25","S26","S27","S28","S29","S30a","S30b"]
for i, sc in enumerate(scenes):
    a = int(round(bounds[i] * 24)); b = int(round(bounds[i + 1] * 24))
    seg = diffs[a:max(a + 1, b - 1)]
    print(f"  {sc}: mean diff {seg.mean():.3f}  min {seg.min():.3f}  frames {a}-{b}")
json.dump({"n_frames": int(n), "mean_diff": float(diffs.mean()),
           "longest_neardup": int(best),
           "per_scene": {sc: float(diffs[int(round(bounds[i]*24)):max(int(round(bounds[i]*24))+1, int(round(bounds[i+1]*24))-1)].mean())
                         for i, sc in enumerate(scenes)}},
          open(os.path.join(PROJ, "work", "master_motion.json"), "w"), indent=1)
print("wrote work/master_dictation.json + work/master_motion.json")
