import json, subprocess, numpy as np, os
from scipy.io import wavfile
from faster_whisper import WhisperModel
takes = {
 "s09a-t2": ("takes/media-generation-mv9-s09a-t2-0-8d2fffd5-ae21-43a8-8a85-4ceb786b718e.mp4", 10.0, True),
 "s09b-t2": ("takes/media-generation-mv9-s09b-t2-0-a1b93fc3-a66f-4389-9970-264528d42daa.mp4", 10.0, True),
 "s10a":    ("takes/media-generation-mv9-s10a-t1-0-2f85dbf7-85c3-4075-a883-d2f33e6ec5f6.mp4", 10.0, False),
 "s10b":    ("takes/media-generation-mv9-s10b-t1-0-fc1fb357-9d28-42f9-aad2-1c248d7b57b4.mp4", 5.0, False),
 "s11a":    ("takes/media-generation-mv9-s11a-t1-0-891e45ad-58ce-4c12-be9d-070777ef656b.mp4", 10.0, False),
 "s11b":    ("takes/media-generation-mv9-s11b-t1-0-6b671b89-efd1-499a-8cb8-240a3123231c.mp4", 10.0, False),
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
    # even/odd frame-diff medians (12fps doubling check)
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
