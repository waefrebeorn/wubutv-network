#!/usr/bin/env python3
"""Build merged .ass: captions (lyrics.txt verbatim, performed timing) + kinetic type."""
import json, os, subprocess, sys

ROOT = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-6_sell-the-lemons")
ASM = os.path.join(ROOT, "work/assembly")
TOOL = os.path.expanduser("~/workspace/wubutv-network/musicvideo/visual-forms/tools/kinetic_ass.py")

CAPS = [
    (0.60, 2.60, "(Tick, tock, click, clack)"),
    (2.72, 5.32, "Bacon head on the stand…"),
    (6.88, 8.34, "Sell the lemons"), (9.92, 11.60, "Sell the lemons"),
    (15.70, 18.00, "Sell the lemons"),
    (19.86, 22.98, "I spawn in with the default hair,"),
    (22.98, 25.72, "Bacon head, simple smile, no care."),
    (25.72, 28.94, "Start with the stand, one lemon at a time,"),
    (28.94, 31.90, "Click the button, watch the cash climb."),
    (31.90, 34.82, "Upgrade the juicer, double the pay,"),
    (34.82, 38.02, "Automate the stand so I can walk away."),
    (38.02, 41.14, "Money on the floor, walk over and grab,"),
    (41.14, 44.20, "Then buy the next thing, keep on the tab."),
    (45.00, 47.50, "Sell the lemons, sell the lemons,"),
    (47.50, 50.58, "Bacon head selling lemons all day."),
    (50.58, 53.78, "Sell the lemons, sell the lemons,"),
    (53.78, 57.02, "Click, upgrade, sell, don't stop the play."),
    (57.02, 58.44, "Sell the lemons (sell the lemons),"),
    (58.44, 61.04, "Sell the lemons (sell the lemons),"),
    (61.04, 64.36, "Bacon head, sell the lemons,"),
    (64.36, 67.52, "Never gonna stop."),
    (67.52, 70.10, "Sell the lemons, never gonna stop."),
    (70.10, 73.30, "Never gonna stop."),
    (73.32, 76.24, "Lemon Dash, Lemon Depot, the numbers get big,"),
    (76.24, 80.10, "Jetpack on, fly up high, do a little jig."),
    (80.10, 82.58, "Rebirth when the buttons cost too much,"),
    (82.58, 86.02, "Joe the alien shows up, give the button a touch."),
    (86.02, 88.90, "Multipliers stack, the cash comes in waves,"),
    (88.90, 92.06, "Void portal opens, evolution saves."),
    (92.06, 95.14, "From stand to space, the empire keeps growing,"),
    (95.14, 98.58, "Bacon head on the screen, the lemons still flowing."),
    (98.58, 100.88, "Sell the lemons, sell the lemons,"),
    (100.88, 104.12, "Bacon head selling lemons all day."),
    (104.12, 107.14, "Sell the lemons, sell the lemons,"),
    (107.14, 110.30, "Click, upgrade, sell, don't stop the play."),
    (110.30, 111.86, "Sell the lemons (sell the lemons),"),
    (111.86, 113.64, "Sell the lemons (sell the lemons),"),
    (113.64, 117.04, "Bacon head, sell the lemons,"),
    (117.04, 120.90, "Never gonna stop."),
    (121.00, 124.08, "Click, sell, upgrade, sell,"),
    (124.08, 126.84, "Click, sell, upgrade, sell."),
    (126.84, 129.90, "Automate the line, watch the cash fly,"),
    (129.90, 133.00, "Bacon head dancing while the numbers go high."),
    (133.00, 136.05, "Sell the lemons…"), (136.05, 139.10, "Sell the lemons…"),
    (139.10, 142.15, "Sell the lemons…"), (142.15, 145.20, "Sell the lemons…"),
    (145.90, 148.94, "World 2 comes, oxygen next,"),
    (148.94, 152.14, "Same loop, bigger checks, never perplexed."),
    (152.14, 155.14, "Offline cash keeps ticking while I sleep,"),
    (155.14, 158.52, "Wake up richer, the empire is deep."),
    (158.52, 160.80, "Shake the trees, grab the bags, do the deals,"),
    (160.80, 163.80, "Bacon head still selling, that's how it feels."),
    (163.80, 166.66, "From one little stand to the top of the sky,"),
    (166.66, 170.50, "Sell the lemons, keep the machine running high."),
    (173.38, 176.28, "Sell the lemons, sell the lemons,"),
    (176.28, 179.52, "Bacon head selling lemons all day."),
    (179.52, 182.66, "Sell the lemons, sell the lemons,"),
    (182.66, 185.74, "Click, upgrade, sell, don't stop the play."),
    (185.74, 188.80, "Sell the lemons (sell the lemons),"),
    (188.80, 193.64, "Sell the lemons (sell the lemons),"),
    (193.64, 199.72, "Never gonna stop."),
    (199.72, 204.48, "Sell the lemons…"),
    (204.48, 208.92, "Sell the lemons…"),
    (208.92, 212.20, "Never gonna stop."),
    (218.46, 220.38, "Bacon head…"),
    (220.38, 223.14, "Sell the lemons."),
    (224.70, 226.36, "Sell the lemons."),
    (226.62, 228.60, "Sell the lemons."),
]

def W(word, start, end, line):
    return {"word": word, "start": start, "end": end, "line": line}

SLAM = [
    W("SELL", 15.70, 16.50, "i3"), W("THE", 16.50, 17.30, "i3"), W("LEMONS", 17.30, 18.00, "i3"),
    W("SELL", 57.02, 57.88, "c15"), W("THE", 57.88, 58.12, "c15"), W("LEMONS", 58.12, 58.44, "c15"),
    W("SELL", 58.44, 58.74, "c16"), W("THE", 58.74, 59.66, "c16"), W("LEMONS,", 59.66, 60.14, "c16"),
    W("SELL", 60.14, 60.44, "c16"), W("THE", 60.44, 60.74, "c16"), W("LEMONS", 60.74, 61.04, "c16"),
    W("BACON", 61.04, 61.60, "c17"), W("HEAD,", 61.60, 62.00, "c17"), W("SELL", 62.00, 62.30, "c17"),
    W("THE", 62.30, 62.68, "c17"), W("LEMONS", 62.68, 64.36, "c17"),
    W("NEVER", 64.36, 65.06, "c18"), W("GONNA", 65.06, 65.96, "c18"), W("STOP", 65.96, 67.52, "c18"),
    W("SELL", 67.52, 68.48, "c19"), W("THE", 68.48, 68.64, "c19"), W("LEMONS,", 68.64, 69.16, "c19"),
    W("NEVER", 69.16, 69.34, "c19"), W("GONNA", 69.34, 69.68, "c19"), W("STOP", 69.68, 70.10, "c19"),
    W("NEVER", 70.10, 70.80, "c1a"), W("GONNA", 70.80, 71.02, "c1a"), W("STOP,", 71.02, 72.08, "c1a"),
    W("NEVER", 72.08, 72.36, "c1a"), W("GONNA", 72.36, 72.56, "c1a"), W("STOP", 72.56, 73.30, "c1a"),
    W("SELL", 110.30, 111.30, "c25"), W("THE", 111.30, 111.50, "c25"), W("LEMONS", 111.50, 111.86, "c25"),
    W("SELL", 111.86, 112.12, "c26"), W("THE", 112.12, 112.32, "c26"), W("LEMONS,", 112.32, 112.74, "c26"),
    W("SELL", 112.74, 112.90, "c26"), W("LEMONS", 112.90, 113.64, "c26"),
    W("SELL", 115.08, 116.14, "c27"), W("THE", 116.14, 116.24, "c27"), W("LEMONS", 116.24, 117.04, "c27"),
    W("NEVER", 117.04, 118.52, "c28"), W("GONNA", 118.52, 119.70, "c28"), W("STOP", 119.70, 120.90, "c28"),
    W("SELL", 133.00, 133.32, "b1"), W("THE", 133.32, 133.56, "b1"), W("LEMONS,", 133.56, 134.32, "b1"),
    W("SELL", 134.32, 134.88, "b1"), W("THE", 134.88, 135.08, "b1"), W("LEMONS,", 135.08, 135.72, "b1"),
    W("SELL", 135.72, 136.40, "b1"), W("THE", 136.40, 136.68, "b1"), W("LEMONS", 136.68, 137.46, "b1"),
    W("SELL", 137.46, 138.00, "b2"), W("THE", 138.00, 138.26, "b2"), W("LEMONS,", 138.26, 138.98, "b2"),
    W("SELL", 138.98, 139.42, "b2"), W("THE", 139.42, 139.98, "b2"), W("LEMONS,", 139.98, 141.00, "b2"),
    W("SELL", 141.00, 141.20, "b2"), W("THE", 141.20, 141.40, "b2"), W("LEMONS", 141.40, 142.20, "b2"),
    W("SELL", 142.20, 142.72, "b3"), W("THE", 142.72, 142.94, "b3"), W("LEMONS,", 142.94, 143.40, "b3"),
    W("SELL", 143.40, 143.84, "b3"), W("THE", 143.84, 145.06, "b3"), W("LEMONS", 145.06, 145.20, "b3"),
    W("SELL", 166.66, 167.48, "v38"), W("THE", 167.48, 167.68, "v38"), W("LEMONS,", 167.68, 168.12, "v38"),
    W("SELL", 185.74, 187.00, "f15"), W("THE", 187.00, 188.42, "f15"), W("LEMONS", 188.42, 188.80, "f15"),
    W("SELL", 188.80, 189.06, "f16"), W("THE", 189.06, 189.24, "f16"), W("LEMONS", 189.24, 189.54, "f16"),
    W("NEVER", 189.54, 189.90, "f17"), W("GONNA", 189.90, 193.64, "f17"), W("STOP", 193.64, 196.60, "f17"),
    W("SELL", 199.72, 200.56, "f18"), W("THE", 200.56, 200.90, "f18"), W("LEMONS,", 200.90, 201.50, "f18"),
    W("SELL", 201.50, 203.64, "f18"), W("THE", 203.64, 204.04, "f18"), W("LEMONS", 204.04, 204.48, "f18"),
    W("SELL", 204.48, 204.90, "f19"), W("THE", 204.90, 205.28, "f19"), W("LEMONS", 205.28, 205.52, "f19"),
    W("NEVER", 205.52, 206.50, "f1a"), W("GONNA", 206.50, 208.92, "f1a"), W("STOP", 208.92, 212.20, "f1a"),
    W("SELL", 226.62, 227.30, "o3"), W("THE", 227.30, 227.80, "o3"), W("LEMONS.", 227.80, 228.60, "o3"),
    W("SELL", 224.70, 225.35, "o2"), W("THE", 225.35, 225.60, "o2"), W("LEMONS.", 225.60, 226.36, "o2"),
]

CASCADE = [
    W("CLICK,", 53.78, 54.22, "c14"), W("UPGRADE,", 54.22, 54.74, "c14"), W("SELL,", 54.74, 55.28, "c14"),
    W("DON'T", 55.28, 55.70, "c14"), W("STOP", 55.70, 55.96, "c14"), W("THE", 55.96, 56.32, "c14"),
    W("PLAY.", 56.32, 57.02, "c14"),
    W("CLICK,", 107.14, 107.58, "c24"), W("UPGRADE,", 107.58, 108.10, "c24"), W("SELL,", 108.10, 108.62, "c24"),
    W("DON'T", 108.62, 109.04, "c24"), W("STOP", 109.04, 109.38, "c24"), W("THE", 109.38, 109.72, "c24"),
    W("PLAY.", 109.72, 110.30, "c24"),
    W("CLICK,", 182.66, 182.98, "f14"), W("UPGRADE,", 182.98, 183.50, "f14"), W("SELL,", 183.50, 184.06, "f14"),
    W("DON'T", 184.06, 184.44, "f14"), W("STOP", 184.44, 184.78, "f14"), W("THE", 184.78, 185.20, "f14"),
    W("PLAY.", 185.20, 185.74, "f14"),
    W("CLICK,", 121.00, 121.52, "br1"), W("SELL,", 121.52, 122.02, "br1"), W("UPGRADE,", 122.02, 122.84, "br1"),
    W("SELL,", 122.84, 124.08, "br1"),
    W("CLICK,", 124.08, 124.66, "br2"), W("SELL,", 124.66, 125.14, "br2"), W("UPGRADE,", 125.14, 125.98, "br2"),
    W("SELL.", 125.98, 126.84, "br2"),
]

HIGHLIGHT = [
    W("AUTOMATE", 126.84, 127.78, "br3"), W("THE", 127.78, 127.96, "br3"), W("LINE,", 127.96, 128.60, "br3"),
    W("WATCH", 128.60, 129.00, "br3"), W("THE", 129.00, 129.16, "br3"), W("CASH", 129.16, 129.42, "br3"),
    W("FLY,", 129.42, 129.90, "br3"),
    W("BACON", 129.90, 130.66, "br4"), W("HEAD", 130.66, 131.20, "br4"), W("DANCING", 131.20, 131.50, "br4"),
    W("WHILE", 131.50, 131.74, "br4"), W("THE", 131.74, 131.90, "br4"), W("NUMBERS", 131.90, 132.20, "br4"),
    W("GO", 132.20, 132.54, "br4"), W("HIGH.", 132.54, 133.00, "br4"),
]

def ts(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def run_kinetic(words, preset, name):
    path = os.path.join(ASM, f"kin_{name}.json")
    with open(path, "w") as fh:
        json.dump({"words": words}, fh)
    out = os.path.join(ASM, f"kin_{name}.ass")
    subprocess.run([sys.executable, TOOL, "--words", path, "--preset", preset,
                    "--out", out, "--fontsize", "54"], check=True)
    return out

def main():
    parts = []
    header = None
    for words, preset, name in [(SLAM, "SLAM", "slam"), (CASCADE, "CASCADE", "casc"),
                                (HIGHLIGHT, "HIGHLIGHT", "high")]:
        out = run_kinetic(words, preset, name)
        text = open(out).read()
        head, _, events = text.partition("[Events]")
        if header is None:
            header = head
        ev = events.split("\n", 1)[1]  # drop Format line
        parts.append(ev)
    cap_style = ("Style: Caption,Noto Sans,40,&HDCEEF4,&HDCEEF4,&H141414,&H96000000,"
                 "-1,0,0,0,100,100,0,0,1,3,0,2,10,10,24,1\n")
    header = header.rstrip("\n") + "\n" + cap_style
    cap_events = []
    for (a, b, txt) in CAPS:
        cap_events.append(f"Dialogue: 1,{ts(a)},{ts(b)},Caption,,0,0,0,,{txt}")
    merged = header + "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    merged += "\n".join(cap_events) + "\n" + "\n".join(p.strip("\n") for p in parts) + "\n"
    outpath = os.path.join(ASM, "mv6.ass")
    with open(outpath, "w") as fh:
        fh.write(merged)
    print("wrote", outpath, "captions:", len(cap_events))

if __name__ == "__main__":
    main()
