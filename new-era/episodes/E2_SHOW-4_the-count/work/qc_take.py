#!/usr/bin/env python3
"""Per-take QC: probe, frame grabs, faster-whisper ASR with word times."""
import json, subprocess, sys, os

take = sys.argv[1]
tag = sys.argv[2]
outdir = sys.argv[3]
os.makedirs(outdir, exist_ok=True)

probe = subprocess.run(['ffprobe','-v','error','-show_streams','-show_format',
                        '-of','json', take], capture_output=True, text=True).stdout
pj = json.loads(probe)
v = next(s for s in pj['streams'] if s['codec_type']=='video')
a = next((s for s in pj['streams'] if s['codec_type']=='audio'), None)
print(f"PROBE {tag}: {v['width']}x{v['height']} fps={v.get('avg_frame_rate')} "
      f"dur={pj['format']['duration']} size={pj['format']['size']} "
      f"audio={'yes' if a else 'NO'}")

for t in ['0','0.5','1.0','2.5','5.0','7.5','9.8']:
    subprocess.run(['ffmpeg','-v','error','-ss',t,'-i',take,'-frames:v','1',
                    '-q:v','3', f'{outdir}/{tag}_f{t}.jpg'], check=True)

from faster_whisper import WhisperModel
import numpy as np
raw = subprocess.run(['ffmpeg','-v','error','-i',take,'-f','f32le','-ac','1',
                      '-ar','16000','-'], capture_output=True).stdout
audio = np.frombuffer(raw, dtype=np.float32).copy()
model = WhisperModel('large-v3', device='cpu', compute_type='int8')
segs, _ = model.transcribe(audio, word_timestamps=True, vad_filter=False)
print(f"ASR {tag}:")
for s in segs:
    words = ' '.join(w.word.strip() for w in (s.words or []))
    print(f"  [{s.start:5.2f}-{s.end:5.2f}] {s.text.strip()}")
    if words: print(f"    words: {words}")
