#!/usr/bin/env python3
"""Stage-1 plates re-origined at assembly for the accepted
takes' actual wall fields (placement-check frames in
work/placement_part2/):

  U2_t1: wall = the brick corner pier, center frame.
         Pre-built (185,120) landed on the door/board.
  U3_t1: wall = board + brick pier, center-right.
         Pre-built (330,20) crossed Marta's head.
  U4_t1: wall = the narrow brick pier right of the door.
         Pre-built (240,26) landed on the awning/sky.
  U5_t1: wall = brick above the Watcher's head, right of
         the board. Pre-built (24,16) landed on sky.

Same stack, same hand, same erosion as make_plates.py —
only origin/size change, per the brief's assembly tuning.
"""
import importlib.util
import random

spec = importlib.util.spec_from_file_location(
    "make_plates",
    "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
    "E3_hold-on/work/assembly_part2/make_plates.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)

random.seed(20261125)
out = ("/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
       "E3_hold-on/work/assembly_part2")

mp.stack((470, 40), 20).save(f"{out}/plate_U2_t.png")
print("wrote plate_U2_t.png")
mp.stack((560, 14), 26).save(f"{out}/plate_U3_t.png")
print("wrote plate_U3_t.png")
mp.stack((1000, 24), 14).save(f"{out}/plate_U4_t.png")
print("wrote plate_U4_t.png")
mp.stack((690, 8), 15).save(f"{out}/plate_U5_t.png")
print("wrote plate_U5_t.png")
