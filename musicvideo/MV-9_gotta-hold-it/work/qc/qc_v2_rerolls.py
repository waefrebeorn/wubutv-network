import json, subprocess, numpy as np, os
from scipy.io import wavfile
from faster_whisper import WhisperModel
takes = {
 "s01a-t2": ("takes/media-generation-mv9-s01a-t2-0-b3c3d77b-2b21-4061-9d19-038c7d2d28f1.mp4", 10.0, False),
 "s05a-t2": ("takes/media-generation-mv9-s05a-t2-0-af98082e-f958-4060-a988-4bb54ebeabf3.mp4", 10.0, False),
 "s07-t2":  ("takes/media-generation-mv9-s07-t2-0-959b2bab-1e99-4893-9bed-8da41176766c.mp4", 5.0, False),
}
model = WhisperModel("small", device="cpu", compute_type="int8")
for tag,(path,reqdur,singing) in takes.items():
    d=f"work/qc/{tag}"; os.makedirs(d, exist_ok=True)
    r=subprocess.run(["ffprobe","-v","error","-show_entries","stream=codec_name,width,height,r_frame_rate","-show_entries","format=duration,size","-of","default=noprint_wrappers=1",path],capture_output=True,text=True)
    print(f"== {tag} ==\n{r.stdout.strip()}")
    m=subprocess.run(["md5sum",path],capture_output=True,text=True)
    print("MD5", m.stdout.strip())
    subprocess.run(["ffmpeg","-v","error","-y","-i",path,"-vn","-ac","1","-ar","16000",f"{d}/audio.wav"],check=True)
    fps = 1 if reqdur>=10 else 2
    subprocess.run(["ffmpeg","-v","error","-y","-i",path,"-vf",f"fps={fps},scale=416:234,tile=5x2",f"{d}/sheet_key.png"],check=True)
    raw=subprocess.run(["ffmpeg","-v","error","-i",path,"-vf","scale=160:90","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True)
    arr=np.frombuffer(raw.stdout,dtype=np.uint8); n=160*90
    frames=arr.reshape(-1,n).astype(np.int16)
    diff=np.abs(np.diff(frames,axis=0)).mean(axis=1)
    run=0; maxrun=0
    for x in diff:
        run=run+1 if x<0.5 else 0; maxrun=max(maxrun,run)
    print(f"MOTION frames={len(frames)} mean_diff={diff.mean():.2f} longest_near_dup_run={maxrun}f first12={[round(float(x),2) for x in diff[:12]]}")
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
