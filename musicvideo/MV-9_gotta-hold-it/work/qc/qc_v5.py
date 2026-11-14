import json, subprocess, numpy as np, os
from scipy.io import wavfile
from faster_whisper import WhisperModel
takes = {
 "s12a": ("takes/media-generation-mv9-s12a-t1-0-680d9adb-e325-4700-af4f-b5a58fb83807.mp4", 10.0, True),
 "s12b": ("takes/media-generation-mv9-s12b-t1-0-0b972743-9611-4a2e-bdc3-b3f5eff8cd84.mp4", 10.0, True),
 "s13a": ("takes/media-generation-mv9-s13a-t1-0-79630a94-9f97-4fb8-b810-6a11fdc5b419.mp4", 5.0, True),
 "s13b": ("takes/media-generation-mv9-s13b-t1-0-0c233528-0d9f-4361-b129-f575d9036e41.mp4", 10.0, False),
 "s14a": ("takes/media-generation-mv9-s14a-t1-0-efd1ba47-db86-486c-8c03-574977475dc8.mp4", 10.0, False),
 "s14b": ("takes/media-generation-mv9-s14b-t1-0-c5049462-434b-4530-acea-14de23e46ec5.mp4", 10.0, False),
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
    ev=diff[0::2]; od=diff[1::2]
    print(f"MOTION frames={len(frames)} mean_diff={diff.mean():.2f} longest_near_dup_run={maxrun}f first12={[round(float(x),2) for x in diff[:12]]}")
    print(f"DOUBLING even_med={float(np.median(ev)):.2f} odd_med={float(np.median(od)):.2f}")
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
