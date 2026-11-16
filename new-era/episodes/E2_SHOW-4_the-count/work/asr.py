#!/usr/bin/env python3
"""ASR only: faster-whisper large-v3-turbo from the LOCAL cached snapshot.
Usage: asr.py <mediafile> <tag>"""
import subprocess, sys
import numpy as np

MODEL = ('/home/hatch/.cache/huggingface/hub/'
         'models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/'
         'snapshots/0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf')

take, tag = sys.argv[1], sys.argv[2]
raw = subprocess.run(['ffmpeg','-v','error','-i',take,'-f','f32le','-ac','1',
                      '-ar','16000','-'], capture_output=True).stdout
audio = np.frombuffer(raw, dtype=np.float32).copy()
print(f'audio decoded: {len(audio)/16000:.2f}s', flush=True)

from faster_whisper import WhisperModel
model = WhisperModel(MODEL, device='cpu', compute_type='int8')
segs, _ = model.transcribe(audio, word_timestamps=True, vad_filter=False)
print(f"ASR {tag}:", flush=True)
for s in segs:
    print(f"  [{s.start:5.2f}-{s.end:5.2f}] {s.text.strip()}", flush=True)
    if s.words:
        print('    words: ' + ' '.join(
            f"{w.word.strip()}@{w.start:.2f}" for w in s.words), flush=True)
