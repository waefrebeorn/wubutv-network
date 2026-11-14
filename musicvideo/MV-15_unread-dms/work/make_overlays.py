import json, os
P = os.path.expanduser("~/workspace/wubutv-network/musicvideo/MV-15_unread-dms")
# Canonical performed lines (LYRIC_TIMELINE arbitrated text) with spans
lines = [
 (0.00,5.68,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (5.68,12.08,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (12.08,13.82,"200 UNREAD","SLAM"),(13.82,15.28,"200 UNREAD","SLAM"),
 (15.28,16.80,"I'm-I'm not opening it","SLAM"),(16.80,18.48,"I'm not opening it","SLAM"),
 (18.48,25.04,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (25.04,28.74,"Phone lights up and I freeze on the spot (yeah)","HIGH"),
 (28.74,31.90,"200 messages and I already forgot (what)","HIGH"),
 (31.90,35.34,"If I open it now I'll be stuck for an hour (uh)","HIGH"),
 (35.34,38.54,"So I'm leaving that badge like a nuclear power","HIGH"),
 (38.54,41.02,"Don't open / Don't open","SLAM"),
 (41.02,43.42,"Just mute it / Just mute it","SLAM"),
 (43.42,44.80,"Just mute it","SLAM"),
 (44.80,50.44,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (50.44,56.36,"The group chat has 200 unread / and I'm not opening it","HIGH"),
 (56.36,63.12,"Not opening it / 200 unread / I'm-I'm not opening it","SLAM"),
 (63.12,69.54,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (69.54,76.34,"I'm not opening it / 200 unread","SLAM"),
 (76.34,79.70,"They planning something and I don't wanna know (yeah)","HIGH"),
 (79.70,83.14,"If I scroll back I'll lose the whole day for sure (what)","HIGH"),
 (83.14,86.30,"Badge going red and I'm acting like I'm blind (uh)","HIGH"),
 (86.30,89.46,"Strategic silence is the only peace of mind","HIGH"),
 (89.46,93.48,"Don't open / Just mute it","SLAM"),
 (93.48,96.76,"Just mute it","SLAM"),
 (96.76,102.66,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (102.66,110.66,"200 unread / I'm not opening it (chop field)","SLAM"),
 (110.66,115.20,"I'm-I'm not opening it","SLAM"),
 (115.20,123.02,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (124.72,131.80,"200! 200! 200! 200! — I'm not looking, I'm not looking","SLAM"),
 (131.80,134.70,"LEAVE IT  /  LEAVE IT","STACK"),
 (134.70,139.86,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (139.86,146.70,"The group chat has 200 unread and I'm not opening it","HIGH"),
 (146.70,153.10,"200 UNREAD / I'm-I'm not open it","SLAM"),
 (153.10,162.50,"The group chat has 200 unread and I'm NOT O-O-Open it","HIGH"),
 (162.50,164.42,"Not opening it","HIGH"),
 (165.68,171.00,"Not opening it / 200 unread","HIGH"),
 (171.00,172.00,"(yeah)","HIGH"),
]
def ts(t):
    h=int(t//3600); m=int((t%3600)//60); s=t%60
    return f"{h}:{m:02d}:{s:05.2f}"
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: High,DejaVu Sans,44,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,1,2,40,40,36,1
Style: Slam,DejaVu Sans,64,&H0000E5FF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,5,40,40,20,1
Style: Stack,DejaVu Sans,72,&H00FFFFFF,&H000000FF,&H00E5322D,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,5,40,40,20,1
Style: Hud,DejaVu Sans,40,&H00FFFFFF,&H000000FF,&H00E5322D,&H00000000,-1,0,0,0,100,100,0,0,3,2,0,9,30,30,24,1
Style: Bug,DejaVu Sans,26,&H96FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,1,0,3,24,24,18,1
Style: Mute,DejaVu Sans,54,&H00FFFFFF,&H000000FF,&H00E5322D,&H00000000,-1,0,0,0,100,100,0,0,3,3,0,8,40,40,60,1
Style: Ident,DejaVu Sans,80,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,5,40,40,20,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev = []
for a,b,txt,kind in lines:
    st = "Slam" if kind=="SLAM" else ("Stack" if kind=="STACK" else "High")
    ev.append(f"Dialogue: 1,{ts(a)},{ts(b)},{st},,0,0,0,,{txt}")
# Badge-counter HUD (count line from SCENE_PLAN)
counts = [(0.00,2.62,"199"),(2.62,28.74,"200"),(28.74,44.80,"214"),(44.80,63.12,"247"),(63.12,83.14,"268"),(83.14,96.76,"285"),(96.76,124.72,"312"),(124.72,134.70,"347"),(134.70,153.10,"389"),(153.10,173.61,"389  MUTED")]
for a,b,c in counts:
    ev.append(f"Dialogue: 2,{ts(a)},{ts(b)},Hud,,0,0,0,,  {c} UNREAD  ")
# Full-screen counter SLAM on first "200" (2.62s) — 12 frames
ev.append(f"Dialogue: 3,{ts(2.38)},{ts(2.86)},Ident,,0,0,0,,200")
# MUTE stamps: land ON 44.80 (end of L11) and ON 96.76 entry
ev.append(f"Dialogue: 3,{ts(44.32)},{ts(45.28)},Mute,,0,0,0,,  MUTED  ")
ev.append(f"Dialogue: 3,{ts(96.28)},{ts(97.24)},Mute,,0,0,0,,  MUTED  ")
# Ident over outro tail
ev.append(f"Dialogue: 3,{ts(166.00)},{ts(172.00)},Ident,,0,0,0,,UNREAD DMs")
# Corner bug, whole master
ev.append(f"Dialogue: 0,{ts(0)},{ts(173.61)},Bug,,0,0,0,,~ WuBu ~")
open(f"{P}/work/overlays/kinetic.ass","w").write(hdr + "\n".join(ev) + "\n")
print("ASS events:", len(ev))
