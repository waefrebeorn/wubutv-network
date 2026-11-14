#!/usr/bin/env python3
"""v3: Count h264 slice frames in the partial MV-8 v2 master via longest-chain
linking of AVCC NAL candidates. The mdat interleaves video NALs (4-byte BE
length prefix) with raw AAC audio chunks (~1KB, no prefix). Candidates are
positions with a sane length + slice header; true NALs chain: each NAL's end
lands within 8KB of the next NAL's start (the audio gap). Longest chain from
the known-good start (offset 48) ~= frames encoded so far.
"""
import re, struct

SRC = "/home/hatch/workspace/wubutv-network/musicvideo/MV-8_wipe-and-its-still-there/masters/mv8_wipe_and_its_still_there_v2_16x9.mp4"
with open(SRC, "rb") as f:
    data = f.read()
L = len(data)
print(f"file bytes: {L}")

# candidate slice-NAL starts: header byte 0x21/0x41/0x61 (type 1) or 0x65 (type 5)
cands = []
for m in re.finditer(rb"[\x21\x41\x61\x65]", data):
    h = m.start()
    if h < 4:
        continue
    ln = struct.unpack(">I", data[h - 4:h])[0]
    if 50 <= ln <= 1_000_000 and h + ln <= L:
        t = data[h] & 0x1F
        if t in (1, 5):
            cands.append((h - 4, ln, t))
print(f"candidates: {len(cands)}")
# de-dup (regex finds each byte once, so no dups; sort by pos)
cands.sort()
# longest chain: dp[i] = chain length ending at candidate i; prev pointer
import bisect
starts = [c[0] for c in cands]
n = len(cands)
dp = [1] * n
prev = [-1] * n
for i in range(n):
    pos, ln, t = cands[i]
    end = pos + 4 + ln
    # next candidates must start within [end, end+8192]
    j = bisect.bisect_left(starts, end, i + 1)
    k = bisect.bisect_right(starts, end + 8192, i + 1)
    best, bestj = 1, -1
    for jj in range(j, k):
        if dp[jj] + 1 > best:
            best, bestj = dp[jj] + 1, jj
    # NOTE: dp is forward-looking; do a backward pass instead below
# backward DP: longest chain STARTING at i
dp2 = [1] * n
nxt = [-1] * n
for i in range(n - 1, -1, -1):
    pos, ln, t = cands[i]
    end = pos + 4 + ln
    j = bisect.bisect_left(starts, end, i + 1)
    k = bisect.bisect_right(starts, end + 8192, i + 1)
    best, bestj = 1, -1
    for jj in range(j, k):
        if dp2[jj] + 1 > best:
            best, bestj = dp2[jj] + 1, jj
    dp2[i], nxt[i] = best, bestj
# start from the known-good first slice NALs (offset 48 SEI, 738 IDR, 80814 slice)
# find the candidate nearest to 738 (IDR) and report its chain
start_idx = bisect.bisect_left(starts, 738)
print(f"chain from IDR candidate @{starts[start_idx] if start_idx < n else 'none'}: {dp2[start_idx] if start_idx < n else 'n/a'} frames")
# also report the single longest chain anywhere (in case the start anchor is off)
bi = max(range(n), key=lambda i: dp2[i])
print(f"longest chain anywhere: {dp2[bi]} frames, starts @{cands[bi][0]}")
# walk the chain from the IDR anchor and show its end offset + last few positions
i = start_idx
walk = []
while i != -1:
    walk.append(cands[i])
    i = nxt[i]
print(f"walked chain length: {len(walk)}")
if walk:
    print(f"chain ends at file offset {walk[-1][0] + 4 + walk[-1][1]} / {L}")
    print(f"last 5 chain NALs: {walk[-5:]}")
