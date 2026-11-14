#!/usr/bin/env python3
"""Build re-fire prompts for Q3 run 2026-10-14 12:45 EDT.
B-766 named-failure strengthens LEAD each prompt (B-871: correction first,
stated positively)."""
import pathlib

SLATE = pathlib.Path.home() / "workspace/wubutv-network/slate"

CORRECTIONS = {
    134: ("FIRE_E134_2026-10-14_1245.txt", "FIRE_E134_2026-10-14_1245_refire.txt",
"""CORRECTION — the previous attempt failed in two ways and both are WRONG: (1) it rendered a loud voice-like sound from 1.0 to 3.6 seconds while the Colonel's mouth was closed and motionless — a voice event on a closed mouth. The first four seconds are a SILENT read: his mouth stays closed and motionless with lips together from 0s through 3.9s, and there is NO voice event and NO loud sound of any kind before 4s — only quiet studio tone. (2) The ONLY voice event in the entire take is ONE continuous read beginning at 4s: his mouth opens at 4s and never fully closes until 8s, the appointed slot held mid-read as open-mouth silence with no voice for one full beat, then the read completes and his mouth closes. The unread area is never named aloud.

"""),
    135: ("FIRE_E135_2026-10-14_1245.txt", "FIRE_E135_2026-10-14_1245_refire.txt",
"""CORRECTION — the previous attempt rendered the hoodie wordmark as '~WuBu' with the TRAILING TILDE ABSENT in the 0.5s and 6.0s frames while present at 8s — a flickering tilde — and that is WRONG. The hoodie wordmark reads ~WuBu~ with BOTH tildes present and legible in EVERY frame from 0s to 10s: tilde, capital W, plain lowercase u, capital B, plain lowercase u, tilde — the trailing tilde touches the final lowercase u, is fully legible in every frame including profile views, and never flickers, never goes absent.

"""),
    136: ("FIRE_E136_2026-10-14_1245.txt", "FIRE_E136_2026-10-14_1245_refire.txt",
"""CORRECTION — the previous attempt rendered a legible 'EMPTY LOT' label on the red dispatch tray — and that is WRONG. The ONLY text that exists anywhere in the frame is "ROOM 1102" on the key tag, glyph-exact. The dispatch tray is unlettered: plain red, no label, no words, no letters, no marks of any kind — nothing on the tray is readable to camera at any time.

"""),
}

for num, (src, out, corr) in CORRECTIONS.items():
    base = (SLATE / src).read_text()
    (SLATE / out).write_text(corr + base)
    print(f"OK #{num}: {out}")
