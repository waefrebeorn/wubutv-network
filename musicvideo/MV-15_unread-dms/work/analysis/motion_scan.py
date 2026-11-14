import subprocess, json, sys
import numpy as np
TAKES = {
 "S01":"mv15_s01_t3","S02":"mv15_s02_t1","S03":"mv15_s03_t1","S04":"mv15_s04_t2",
 "S05":"mv15_s05_t1","S06":"mv15_s06_t1","S07":"mv15_s07_t2","S08":"mv15_s08_t1",
 "S09":"mv15_s09_t1","S10":"mv15_s10_t1","S11":"mv15_s11_t2","S12":"mv15_s12_t1",
 "S13":"mv15_s13_t1","S14":"mv15_s14_t1","S15":"mv15_s15_t2","S16":"mv15_s16_t2",
 "S17":"mv15_s17_t1","S18":"mv15_s18_t1","S19":"mv15_s19_t1","S20":"mv15_s20_t1",
 "S21":"mv15_s21_t1","S22":"mv15_s22_t1","S23":"mv15_s23_t1","S24":"mv15_s24_t1"}
W,H=160,90
def frames(path):
    cmd=["ffmpeg","-v","error","-i",path,"-vf","fps=24,scale=160:90,format=gray","-f","rawvideo","-"]
    raw=subprocess.run(cmd,capture_output=True).stdout
    n=len(raw)//(W*H)
    return np.frombuffer(raw[:n*W*H],dtype=np.uint8).reshape(n,H,W).astype(np.float32)
out={}
for sid,name in TAKES.items():
    F=frames(f"takes/{name}.mp4")
    d=np.abs(np.diff(F,axis=0)).mean(axis=(1,2))
    still=d<0.5
    runs=[]; i=0
    while i<len(still):
        if still[i]:
            j=i
            while j<len(still) and still[j]: j+=1
            if j-i>=1: runs.append({"start_f":int(i+1),"len":int(j-i),"min_diff":round(float(d[i:j].min()),3)})
            i=j
        else: i+=1
    out[sid]={"take":name,"frames":int(len(F)),"mean_diff":round(float(d.mean()),2),"min_diff":round(float(d.min()),3),"still_runs_ge1":runs}
    print(sid,name,"frames",len(F),"mean",out[sid]["mean_diff"],"runs>=2:",[r for r in runs if r["len"]>=2])
json.dump(out,open("work/analysis/motion_scan.json","w"),indent=1)
