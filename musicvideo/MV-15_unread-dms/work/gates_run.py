import subprocess, json, hashlib, os
import numpy as np
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
M = f"{P}/masters/mv15_unread_dms_16x9.mp4"; PG = f"{P}/work/master_pregrain.mp4"
def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, **kw)
out = {}
out["master_md5"] = hashlib.md5(open(M,'rb').read()).hexdigest()
out["master_bytes"] = os.path.getsize(M)
pr = json.loads(run(["ffprobe","-v","error","-show_entries","stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels","-show_entries","format=duration","-of","json",M]).stdout)
out["probe"] = pr
nf = run(["ffprobe","-v","error","-count_frames","-select_streams","v:0","-show_entries","stream=nb_read_frames","-of","csv=p=0",M], text=True).stdout.strip()
out["master_frames"] = int(nf); out["frames_ok"] = (int(nf)==4167)
raw = run(["bash","-c",f"dd if={M} bs=1M count=4 2>/dev/null | strings | grep -o 'crf=[0-9.]*' | head -1"], text=True).stdout.strip()
out["sei"] = raw
with open(M,'rb') as f: head = f.read(2_000_000)
out["faststart"] = head.find(b'moov') < head.find(b'mdat') and head.find(b'moov')>=0
W,H = 640,360; FS = W*H
def stills(path):
    # identical math to gates.py stills(), streamed frame-by-frame (memory-safe)
    p = subprocess.Popen(["ffmpeg","-v","error","-i",path,"-vf","scale=640:360,format=gray","-f","rawvideo","-"], stdout=subprocess.PIPE)
    prev = None; n = 0; longest = cur = 0; worst_start = 0; dmin = 1e9; dsum = 0.0; npairs = 0
    while True:
        buf = p.stdout.read(FS)
        if len(buf) < FS: break
        a = np.frombuffer(buf, dtype=np.uint8).astype(np.int16)
        n += 1
        if prev is not None:
            d = float(np.abs(a-prev).mean()); npairs += 1; dsum += d; dmin = min(dmin, d)
            below = d < 0.5
            i = npairs - 1
            if below: cur += 1
            else: cur = 0
            if cur > longest: longest = cur; worst_start = i-cur+1
        prev = a
    p.wait()
    return {"frames_decoded": int(n), "longest_near_dup_run_frames": int(longest), "worst_run_start_frame": int(worst_start), "worst_run_time_s": round(worst_start/24,2), "min_pair_diff": float(dmin), "mean_pair_diff": float(dsum/max(npairs,1))}
out["zero_still_master"] = stills(M)
print("master stills done", flush=True)
out["zero_still_pregrain"] = stills(PG)
print("pregrain stills done", flush=True)
run(["ffmpeg","-v","error","-y","-i",M,"-vn","-ac","1","-ar","16000",f"{P}/work/qc/master_audio.wav"])
run(["ffmpeg","-v","error","-y","-i",f"{P}/track.mp3","-ac","1","-ar","16000",f"{P}/work/qc/track_audio.wav"])
def wav(p):
    r = run(["ffmpeg","-v","error","-i",p,"-f","f32le","-ac","1","-ar","16000","-"])
    return np.frombuffer(r.stdout, dtype=np.float32)
x = wav(f"{P}/work/qc/master_audio.wav"); y = wav(f"{P}/work/qc/track_audio.wav")
n = min(len(x), len(y)); x, y = x[:n], y[:n]
def corr(a,b):
    a = a-a.mean(); b = b-b.mean(); return float((a*b).sum()/ (np.sqrt((a*a).sum()*(b*b).sum())+1e-12))
out["audio_corr_global"] = corr(x,y)
worst = 1.0
for s in range(0, n-160000, 160000):
    worst = min(worst, corr(x[s:s+160000], y[s:s+160000]))
out["audio_corr_worst_10s"] = worst
out["runner"] = "gates_run.py (streaming twin of gates.py — identical scale/threshold/math; gates.py itself OOM-died on the whole-buffer decode)"
json.dump(out, open(f"{P}/work/qc/GATES.json","w"), indent=1)
print(json.dumps(out, indent=1))
