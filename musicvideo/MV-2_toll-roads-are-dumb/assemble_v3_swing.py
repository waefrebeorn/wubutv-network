#!/usr/bin/env python3
"""MV-2 v3 swing assembly: whisper word anchors, UNCLAMPED video time-stretch.
User order 2026-11-02 ~03:39: swing the speeds, make the words match, time sweeping.
Song audio untouched. Take audio discarded. Video only, setpts per segment.
Anchors: WORD_MATCH_V3.json (window+-12s + monotonic, base whisper).
Noise rule: if an onset-interval speed is >4x or <0.25x, drop the middle
anchor and merge the interval (whisper short-word timing noise, not swing).
Window model (fixed 2026-11-02 after the first render crashed on S27 and
squeezed S16 to 0.56s): words land EXACTLY on their song times. A scene
starts at max(its raw start, previous scene's last word end) -- its
pre-vocal action is trimmed when the previous word runs late, never its
first word. A scene ends where the next scene starts, so its post-vocal
tail is swept (fast or slow) into the gap to the next first word, never
allowed to swallow the next scene. S27 has no song anchor (its phrase is
the same final line S26 already sang); it takes over at S26's last word
end (260.80) as the visual outro -- full take swept uniformly to 268.01,
tear landing in the final seconds. Gaps before S01 are held on S01's
first frame.
"""
import json, os, subprocess, sys
PROJ=os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-2_toll-roads-are-dumb")
TAKES=os.path.join(PROJ,"takes"); WORK=os.path.join(PROJ,"masters_work_v3"); MASTERS=os.path.join(PROJ,"masters")
TRACK=os.path.join(PROJ,"track.mp3"); FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ACTIVE=[("S01","mv2_s01_t4.mp4"),("S02","mv2_s02_t3.mp4"),("S03","mv2_s03_t2.mp4"),("S04","mv2_s04_t4.mp4"),("S05","mv2_s05_t4.mp4"),("S06","mv2_s06_t2.mp4"),("S07","mv2_s07_t2.mp4"),("S08","mv2_s08_t1.mp4"),("S09","mv2_s09_t2.mp4"),("S10","mv2_s10_t1.mp4"),("S11","mv2_s11_t2.mp4"),("S12","mv2_s12_t3.mp4"),("S13","mv2_s13_t2.mp4"),("S14","mv2_s14_t1.mp4"),("S15","mv2_s15_t2.mp4"),("S16","mv2_s16_t1.mp4"),("S17","mv2_s17_t2.mp4"),("S18","mv2_s18_t1.mp4"),("S19","mv2_s19_t1.mp4"),("S20","mv2_s20_t2.mp4"),("S21","mv2_s21_t2.mp4"),("S22","mv2_s22_t1.mp4"),("S23","mv2_s23_t1.mp4"),("S24","mv2_s24_t1.mp4"),("S25","mv2_s25_t2.mp4"),("S26","mv2_s26_t2.mp4"),("S27","mv2_s27_t2.mp4")]
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode!=0:
        print("FAILED:"," ".join(cmd)); print(r.stderr[-3000:]); sys.exit(1)
    return r
def main():
    os.makedirs(WORK,exist_ok=True); os.makedirs(MASTERS,exist_ok=True)
    match=json.load(open(os.path.join(PROJ,"WORD_MATCH_V3.json")))
    scenes=[]
    for sc,fn in ACTIVE:
        m=[a for a in match[sc]["anchors"] if a["song"]]
        # noise-merge first, so windows derive from surviving anchors
        changed=True
        while changed and len(m)>=3:
            changed=False
            for i in range(len(m)-1):
                td=m[i+1]["take"]["t0"]-m[i]["take"]["t0"]; sd=m[i+1]["song"]["t0"]-m[i]["song"]["t0"]
                if sd>0 and (td/sd>4 or td/sd<0.25):
                    del m[i+1]; changed=True; break
        if m:
            ws_raw=m[0]["song"]["t0"]-m[0]["take"]["t0"]
            last_end=m[-1]["song"]["t1"]
        else:
            ws_raw=None; last_end=None
        scenes.append({"sc":sc,"fn":fn,"anchors":m,"ws_raw":ws_raw,"last_end":last_end})
    # sequential starts: words exact, actions trimmed/swept
    prev_last_end=None
    for i,s in enumerate(scenes):
        if s["anchors"]:
            s["ws"]=s["ws_raw"] if i==0 else max(s["ws_raw"], prev_last_end)
            assert s["ws"] <= s["anchors"][0]["song"]["t0"], f"{s['sc']} start would cut first word"
            prev_last_end=s["last_end"]
        else:
            # S27: visual outro, starts when the last sung word ends
            s["ws"]=prev_last_end
    for i,s in enumerate(scenes):
        s["we"]=scenes[i+1]["ws"] if i+1 < len(scenes) else 268.01
        assert s["we"] > s["ws"], f"{s['sc']} empty window {s['ws']}-{s['we']}"
    clips=[]; report={}
    prev_end=0.0
    for s in scenes:
        src=os.path.join(TAKES,s["fn"]); m=s["anchors"]
        if s["ws"]>prev_end+0.05:
            gap=s["ws"]-prev_end
            hold=os.path.join(WORK,f"{s['sc']}_hold.mp4")
            if clips:
                run(["ffmpeg","-v","error","-y","-i",clips[-1],"-vf",f"trim=end_frame=1,setpts=PTS-STARTPTS,loop=loop=-1:size=1:start=0,trim=end={gap:.3f},fps=24,format=yuv420p","-an",hold])
            else:
                run(["ffmpeg","-v","error","-y","-i",src,"-vf",f"trim=end_frame=1,setpts=PTS-STARTPTS,loop=loop=-1:size=1:start=0,trim=end={gap:.3f},fps=24,format=yuv420p","-an",hold])
            clips.append(hold)
        if m:
            take_start=s["ws"]-s["ws_raw"]  # >=0, <= first anchor take t0
            ain=[take_start]+[a["take"]["t0"] for a in m]+[10.0]
            aout=[s["ws"]]+[a["song"]["t0"] for a in m]+[s["we"]]
        else:
            ain=[0.0,10.0]; aout=[s["ws"],s["we"]]
        ci,co=[ain[0]],[aout[0]]
        for a,b in zip(ain[1:],aout[1:]):
            if a>ci[-1] and b>co[-1]: ci.append(a); co.append(b)
        if ci[-1]<10.0: ci.append(10.0); co.append(s["we"])
        parts=[]; ins=[]
        for i in range(len(ci)-1):
            di=ci[i+1]-ci[i]; do=co[i+1]-co[i]
            if di<=0 or do<=0: continue
            factor=do/di
            parts.append(f"[0:v]trim=start={ci[i]:.3f}:end={ci[i+1]:.3f},setpts=PTS-STARTPTS,setpts=PTS*{factor:.4f},fps=24,format=yuv420p[v{i}]")
            ins.append(f"[v{i}]")
        assert parts, f"{s['sc']} produced no segments"
        filt=";".join(parts)+";"+"".join(ins)+f"concat=n={len(parts)}:v=1:a=0[out]"
        out=os.path.join(WORK,f"{s['sc']}_swing.mp4")
        run(["ffmpeg","-v","error","-y","-i",src,"-filter_complex",filt,"-map","[out]","-c:v","libx264","-crf","18","-preset","fast","-an",out])
        clips.append(out); prev_end=s["we"]
        speeds=[]
        for i in range(len(ci)-1):
            di=ci[i+1]-ci[i]; do=co[i+1]-co[i]
            if di>0 and do>0: speeds.append(round(di/do,2))
        report[s["sc"]]={"take":s["fn"],"window":[round(s["ws"],2),round(s["we"],2)],"anchors":len(m),"speeds":speeds}
        print(s["sc"],s["fn"],f"window {s['ws']:.2f}-{s['we']:.2f}","anchors",len(m),"speeds",speeds,flush=True)
    json.dump(report,open(os.path.join(PROJ,"CUTLIST_V3_SWING.json"),"w"),indent=1)
    lst=os.path.join(WORK,"concat_v3.txt")
    with open(lst,"w") as f:
        for p in clips: f.write(f"file '{p}'\n")
    video=os.path.join(WORK,"video_v3_16x9.mp4")
    run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",lst,"-c","copy",video])
    srt=os.path.join(PROJ,"captions_v2.srt")
    bug=(f"drawtext=fontfile={FONT}:text='~ WuBu ~':fontsize=32:fontcolor=0xFFC61E:x=w-tw-24:y=h-th-24:shadowcolor=0x000000:shadowx=2:shadowy=2")
    out16=os.path.join(MASTERS,"mv2_toll_roads_are_dumb_v3_16x9.mp4")
    run(["ffmpeg","-v","error","-y","-i",video,"-i",TRACK,"-i",srt,"-filter_complex",f"[0:v]{bug}[v]","-map","[v]","-map","1:a","-map","2:s","-c:v","libx264","-crf","18","-preset","medium","-c:a","aac","-b:a","192k","-ar","48000","-ac","2","-c:s","mov_text","-metadata:s:s:0","language=eng","-movflags","+faststart","-t","268.01",out16])
    print("V3 MASTER DONE",out16)
if __name__=="__main__": main()
