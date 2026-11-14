import subprocess, json, struct, hashlib, os, sys
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
# SEI crf
raw = run(["bash","-c",f"dd if={M} bs=1M count=4 2>/dev/null | strings | grep -o 'crf=[0-9.]*' | head -1"], text=True).stdout.strip()
out["sei"] = raw
# faststart: moov before mdat
with open(M,'rb') as f: head = f.read(2_000_000)
out["faststart"] = head.find(b'moov') < head.find(b'mdat') and head.find(b'moov')>=0
def stills(path):
    r = run(["ffmpeg","-v","error","-i",path,"-vf","scale=640:360,format=gray","-f","rawvideo","-"])
    a = np.frombuffer(r.stdout, dtype=np.uint8)
    n = a.size // (640*360); a = a[:n*640*360].reshape(n,640*360).astype(np.int16)
    d = np.abs(np.diff(a, axis=0)).mean(axis=1)
    below = d < 0.5
    longest = cur = 0; worst_start = 0; cs = 0
    for i,v in enumerate(below):
        if v: cur += 1; 
        else: cur = 0
        if cur > longest: longest = cur; worst_start = i-cur+1
    return {"frames_decoded": int(n), "longest_near_dup_run_frames": int(longest), "worst_run_start_frame": int(worst_start), "worst_run_time_s": round(worst_start/24,2), "min_pair_diff": float(d.min()), "mean_pair_diff": float(d.mean())}
out["zero_still_master"] = stills(M)
out["zero_still_pregrain"] = stills(PG)
# audio agreement: master AAC vs track.mp3, 16k mono, global + worst 10s window corr
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
json.dump(out, open(f"{P}/work/qc/GATES.json","w"), indent=1)
print(json.dumps(out, indent=1))
