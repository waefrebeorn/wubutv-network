#!/usr/bin/env python3
"""U6 plates tuned to the ACCEPTED take U6_t4's actual framings.

U6_t4 does not hold the PEAK wide framing: its head frames
(0-4.5s) carry the wall/door field at center-right, and its
tail frames (4.5-10s) carry the wall at frame left in
perspective (down-street view). The pre-built U6 plates were
origined for the PEAK geometry, so these variants re-origin
the same stack (same text, same hand, same erosion):
  plate_U6a_t.png      stage 1, for the head framing
  plate_U6b_t.png      stage 2, for the wall-side/tail framing
  plate_U6freeze_t.png stage 2 + vote question, tail framing
"""
import importlib.util
import random

spec = importlib.util.spec_from_file_location(
    "make_plates",
    "/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
    "E3_hold-on/work/assembly_part2/make_plates.py")
mp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mp)

random.seed(20261124)
out = ("/home/hatch/workspace/wubutv-network/new-era/morph-episodes/"
       "E3_hold-on/work/assembly_part2")

# head framing: brick field right of the board, above the door
mp.stack((688, 22), 22).save(f"{out}/plate_U6a_t.png")
print("wrote plate_U6a_t.png")
# tail framing: wall at frame left, stack on the upper-left brick
mp.stack((26, 26), 20, stage=2).save(f"{out}/plate_U6b_t.png")
print("wrote plate_U6b_t.png")
mp.stack((26, 26), 20, stage=2, question=True).save(
    f"{out}/plate_U6freeze_t.png")
print("wrote plate_U6freeze_t.png")
