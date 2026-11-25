import subprocess, numpy as np, json
P="/home/hatch/workspace/wubutv-network/musicvideo/MV-34_jensens-back"
# per-frame mean luma at 160x90 via ffmpeg signalstats-free path: decode gray small
cmd=["ffmpeg","-v","error","-i",f"{P}/work/joined.mp4","-vf","scale=160:90,format=gray","-f","rawvideo","-"]
raw=subprocess.run(cmd,capture_output=True).stdout
F=160*90; n=len(raw)//F
fr=np.frombuffer(raw[:n*F],dtype=np.uint8).reshape(n,160,90).astype(np.float32)
diff=np.abs(np.diff(fr,axis=0)).mean(axis=(1,2))
plan=json.load(open(f"{P}/work/assembly/segment_plan.json"))
bounds=[s["frames"][0] for s in plan[1:]]
print("JOINTS (frame: diff at cut, scene-baseline median):")
for b in bounds:
    base=np.median(diff[max(0,b-24):b+24])
    print(f"  f{b:4d} t={b/24:5.2f}s diff={diff[b-1]:.2f} baseline={base:.2f} {'IN-MOTION' if diff[b-1]>0.5*base else 'CHECK'}")
# frozen runs: diff < 0.15 for >=12 consecutive frames
run=0; worst=[]
for i,d in enumerate(diff):
    run=run+1 if d<0.15 else 0
    if run>=12: worst.append((i-run+2,run))
print("frozen runs >=12f (start_frame, len):", worst if worst else "NONE")
print(f"global diff: median={np.median(diff):.2f} p5={np.percentile(diff,5):.2f} min={diff.min():.2f}")
json.dump({"joints":[{"frame":int(b),"diff":round(float(diff[b-1]),2)} for b in bounds],"frozen_runs":worst},open(f"{P}/work/assembly/motion_audit.json","w"),indent=1)
