import subprocess, json, os
import numpy as np

TAKES = {
    "B-1032v2": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1032-parked-bicycle-v2-0-7cda5b8f-ca58-4292-9e24-9efb2f7aaac0.mp4",
    "B-1033v2": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1033-latched-field-gate-v2-0-55a9c99e-efad-4894-9372-ddcdd8ec1c18.mp4",
    "B-1034v2": "/home/hatch/workspace/wubutv-network/takes/2026-10-16/media-generation-b1034-rooftop-antenna-v2-0-d19f8a9c-def4-40c0-ab6a-d4810d82ee13.mp4",
}
OUT = "/home/hatch/workspace/wubutv-network/takes/2026-10-16/qc0145"
os.makedirs(OUT, exist_ok=True)

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

for b, src in TAKES.items():
    print("="*20, b, "="*20)
    r = run(["ffmpeg","-v","error","-i",src,"-f","null","-"])
    print("decode:", r.stderr.strip() or "CLEAN")
    r = run(["ffprobe","-v","error","-show_entries","format=duration:stream=width,height,nb_frames","-of","default=noprint_wrappers=1",src])
    print(r.stdout.strip().replace("\n"," "))
    r = run(["ffmpeg","-v","info","-i",src,"-af","loudnorm=I=-14:TP=-1.0:LRA=11:dual_mono=true:print_format=json","-f","null","-"])
    txt = r.stderr
    try:
        j = json.loads(txt[txt.index("{"):txt.rindex("}")+1])
        print("I:", j["input_i"], "LUFS  TP:", j["input_tp"], "dBTP")
    except Exception as e:
        print("loudnorm parse fail")
    print("0.5s bins (start_s : max_dBFS):")
    for i in range(20):
        s0, s1 = i*0.5, (i+1)*0.5
        r = run(["ffmpeg","-v","info","-ss",str(s0),"-to",str(s1),"-i",src,"-af","volumedetect","-f","null","-"])
        mx = None
        for line in r.stderr.splitlines():
            if "max_volume" in line:
                mx = line.split("max_volume:")[1].split("dB")[0].strip()
        print(f"  {s0:4.1f}s : {mx}")
    tiles = []
    for t, lab in [(0.5,"t05"),(2.0,"t20"),(4.0,"t40"),(6.0,"t60"),(8.0,"t80"),(9.5,"t95")]:
        p = os.path.join(OUT, f"{b}_{lab}.png")
        run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1",p])
        tiles.append(p)
    sheet = os.path.join(OUT, f"{b}_contact.png")
    r = run(["ffmpeg","-v","error","-y","-i",tiles[0],"-i",tiles[1],"-i",tiles[2],"-i",tiles[3],"-i",tiles[4],"-i",tiles[5],
             "-filter_complex","[0][1][2]vstack=inputs=3[r1];[3][4][5]vstack=inputs=3[r2];[r1][r2]hstack,scale=1280:1440",sheet])
    print("contact:", sheet, r.stderr.strip()[:100] or "ok")
    import PIL.Image as I
    f05 = os.path.join(OUT, f"{b}_f05.png"); f95 = os.path.join(OUT, f"{b}_f95.png")
    run(["ffmpeg","-v","error","-y","-ss","0.5","-i",src,"-frames:v","1",f05])
    run(["ffmpeg","-v","error","-y","-ss","9.5","-i",src,"-frames:v","1",f95])
    a = np.asarray(I.open(f05)).astype(float); c = np.asarray(I.open(f95)).astype(float)
    print(f"camera diff top-band: {np.abs(a[:120]-c[:120]).mean():.2f}  full: {np.abs(a-c).mean():.2f}")
    print()
