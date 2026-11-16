import json, subprocess, numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel
from PIL import Image
import io, os
T="takes/media-generation-mv9-s04a-t1-0-cc670d72-82e2-4690-b252-b38331b7e097.mp4"
# duration via ffprobe
r=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",T],capture_output=True,text=True)
print("DURATION", r.stdout.strip())
# transcribe
sr,data=wavfile.read("work/qc/s04a/audio.wav")
audio=data.astype(np.float32)/32768.0
print("AUDIO rms", float(np.sqrt((audio**2).mean())), "max", float(np.abs(audio).max()))
model=WhisperModel("small",device="cpu",compute_type="int8")
segs,info=model.transcribe(audio,language="en",word_timestamps=True)
words=[]
for s in segs:
    print(f"  SEG [{s.start:.2f}-{s.end:.2f}] {s.text.strip()}")
    for w in (s.words or []):
        words.append({"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)})
json.dump(words,open("work/qc/s04a/words.json","w"))
print("WORDS",len(words), words[:12])
# motion: frame diff at native fps via ffmpeg rawvideo
p=subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=r_frame_rate,nb_frames","-of","csv=p=0",T],capture_output=True,text=True)
print("FPS/FRAMES",p.stdout.strip())
raw=subprocess.run(["ffmpeg","-v","error","-i",T,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True)
arr=np.frombuffer(raw.stdout,dtype=np.uint8)
n=160*90
frames=arr.reshape(-1,n).astype(np.int16)
d=np.abs(np.diff(frames,axis=0)).mean(axis=1)
print(f"MOTION frames={len(frames)} mean_diff={d.mean():.2f} min={d.min():.2f} max={d.max():.2f}")
# longest near-dup run (diff<0.5) during 0-7s vocal window (24fps)
fps=24
vocal=d[:int(7*fps)]
run=0; maxrun=0
for x in vocal:
    run=run+1 if x<0.5 else 0
    maxrun=max(maxrun,run)
print(f"VOCAL 0-7s: mean_diff={vocal.mean():.2f} longest near-dup run={maxrun}f")
# frame 0 vs frame 12 (motion at cut point)
print(f"FIRST 12f diffs: {[round(float(x),2) for x in d[:12]]}")
