#!/usr/bin/env python3
"""Build captions_v2.srt from LYRIC_TIMELINE.md line table (48 lines)."""
LINES = [
    (0, 8, "Yeah\u2026 listen here, baby."),
    (8, 12.5, "Those shiny roads ain't what they seem."),
    (12.5, 23, "They build the toll roads, baby, make you pay to roll,"),
    (23, 28, "Old plazas make you stop, then they make you go."),
    (28, 30.5, "Cars slam the brakes, the back ends crash and smash,"),
    (30.5, 33.5, "NTSB said those booths were the worst on the map."),
    (33.5, 38, "Now they got the fast lanes, the rich ones fly on by,"),
    (38, 41.5, "While the rest of us crawl, watching money flash by."),
    (41.5, 44.5, "Weave in, weave out, the speeds don't match at all,"),
    (44.5, 51.5, "One car's racing, the other one's about to fall."),
    (51.5, 53.5, "Toll roads are dumb, baby, toll roads are dumb,"),
    (53.5, 63, "Fast lanes make crashes, the wrecks just come."),
    (63, 68, "Pay to go faster, the rest of us slow,"),
    (68, 78, "Weaving and slamming, the danger grows."),
    (78, 83, "Toll roads are dumb, baby, toll roads are dumb,"),
    (83, 91.5, "Fast lanes make crashes\u2026 they just keep coming."),
    (91.5, 98, "Express lanes look clean, but the merges get hot,"),
    (98, 100, "Speed up, cut over, somebody gets caught."),
    (100, 103, "They say the paid side is safer, the free side takes the hit,"),
    (103, 108, "Crashes just move over, still the same old mess."),
    (108, 110, "Lexus lanes they call 'em, money buys the clear,"),
    (110, 113, "Poor folks sit in traffic while the rich ones disappear."),
    (113, 118, "Stop-and-go plazas used to kill, electronic helps a bit,"),
    (118, 121.5, "But the split still creates the chaos that won't quit."),
    (121.5, 128, "Toll roads are dumb, baby, toll roads are dumb,"),
    (128, 133, "Fast lanes make crashes, the wrecks just come."),
    (133, 143, "Pay to go faster, the rest of us slow,"),
    (143, 148, "Weaving and slamming, the danger grows."),
    (148, 153, "Toll roads are dumb, baby, toll roads are dumb,"),
    (153, 165.5, "Fast lanes make crashes\u2026 they just keep coming."),
    (165.5, 167.5, "They sell you speed for a dollar and a dime,"),
    (167.5, 173, "But the road gets meaner every single time."),
    (173, 175, "One lane's flying, the other one's stuck,"),
    (175, 178, "Somebody's going to get it when the timing's up."),
    (178, 188, "Oh, toll roads are dumb\u2026 yeah, toll roads are dumb\u2026"),
    (188, 190, "Fast lanes make crashes\u2026 the wrecks just come\u2026"),
    (190, 198, "Toll roads are dumb, baby, toll roads are dumb,"),
    (198, 203, "Fast lanes make crashes, the wrecks just come."),
    (203, 213, "Pay to go faster, the rest of us slow,"),
    (213, 218, "Weaving and slamming, the danger grows."),
    (218, 225.5, "Toll roads are dumb (toll roads are dumb),"),
    (225.5, 229.5, "Fast lanes make crashes (fast lanes make crashes),"),
    (229.5, 233, "Toll roads are dumb, baby\u2026"),
    (233, 238.5, "Toll roads are dumb."),
    (238.5, 243, "Yeah\u2026 don't pay for the fast lane, honey."),
    (243, 248, "It ain't worth the crash."),
    (248, 253, "Toll roads are dumb\u2026"),
    (253, 268.01, "Toll roads are dumb\u2026"),
]

def fmt(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

out = []
for i, (s, e, txt) in enumerate(LINES, 1):
    out.append(f"{i}\n{fmt(s)} --> {fmt(e)}\n{txt}\n")
open("captions_v2.srt", "w", encoding="utf-8").write("\n".join(out))
print(f"wrote {len(LINES)} cues")
