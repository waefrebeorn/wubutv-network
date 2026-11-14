import json, subprocess, numpy as np, os
from scipy.io import wavfile
from faster_whisper import WhisperModel
takes = {
 "s01a": ("takes/media-generation-mv9-s01a-t1-0-782ab29c-4c87-4058-94ac-3b43b43017c0.mp4", 10.0, False),
 "s02":  ("takes/media-generation-mv9-s02-t1-0-fd8b7a23-d52a-439c-b746-17a39abeb28f.mp4", 5.0, True),
 "s05a": ("takes/media-generation-mv9-s05a-t1-0-0d2d85e5-fb1f-4b41-9a63-89bbda4bdc22.mp4", 10.0, False),
 "s07":  ("takes/media-generation-mv9-s07-t1-0-1bb39503-e0ab-4bd9-8aa1-67c433b7fdc3.mp4", 5.0, False),
 "s08a": ("takes/media-generation-mv9-s08a-t1-0-ba328240-e1b1-443a-93c9-50e15426a98d.mp4", 5.0, True),
}
model = WhisperModel("small", device="cpu", compute_type="int8")
for tag,(path,reqdur,singing) in takes.items():
    d=f"work/qc/{tag}"; os.makedirs(d, exist_ok=True)
    r=subprocess.run(["ffprobe","-v","error","-show_entries","stream=codec_name,width,height,r_frame_rate","-show_entries","format=duration,size","-of","default=noprint_wrappers=1",path],capture_output=True,text=True)
    print(f"== {tag} ==\n{r.stdout.strip()}")
    m=subprocess.run(["md5sum",path],capture_output=True,text=True)
    print("MD5", m.stdout.strip())
    subprocess.run(["ffmpeg","-v","error","-y","-i",path,"-vn","-ac","1","-ar","16000",f"{d}/audio.wav"],check=True)
    # key sheet: 10 evenly spaced frames
    fps = 1 if reqdur>=10 else 2
    subprocess.run(["ffmpeg","-v","error","-y","-i",path,"-vf",f"fps={fps},scale=416:234,tile=5x2",f"{d}/sheet_key.png"],check=True)
    # motion
    raw=subprocess.run(["ffmpeg","-v","error","-i",path,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True)
    arr=np.frombuffer(raw.stdout,dtype=np.uint8); n=160*90
    frames=arr.reshape(-1,n).astype(np.int16)
    diff=np.abs(np.diff(frames,axis=0)).mean(axis=1)
    run=0; maxrun=0
    for x in diff:
        run=run+1 if x<0.5 else 0; maxrun=max(maxrun,run)
    print(f"MOTION frames={len(frames)} mean_diff={diff.mean():.2f} longest_near_dup_run={maxrun}f first12={[round(float(x),2) for x in diff[:12]]}")
    # transcribe
    sr,data=wavfile.read(f"{d}/audio.wav")
    audio=data.astype(np.float32)/32768.0
    print(f"AUDIO rms={float(np.sqrt((audio**2).mean())):.3f}")
    segs,info=model.transcribe(audio,language="en",word_timestamps=True)
    words=[]
    for s in segs:
        print(f"  SEG [{s.start:.2f}-{s.end:.2f}] {s.text.strip()}")
        for w in (s.words or []):
            words.append({"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)})
    json.dump(words,open(f"{d}/words.json","w"))
    print(f"WORDS n={len(words)}")
    print()
