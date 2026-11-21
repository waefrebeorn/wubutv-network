#!/usr/bin/env python3
"""MV-17 assembly: concat segments -> texture pass + kinetic ASS burn ->
house master (CRF 18, AAC from track.mp3) -> gate probes.
Also builds the pre-grain video (segments + ASS, no texture) for the
zero-still enumeration."""
import subprocess, os, json, sys

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-17_fridge-light-mystery')
SEG = f'{ROOT}/work/segments'
lst = f'{SEG}/concat_list.txt'
scenes = [f'S{i:02d}' for i in range(1, 35)]
open(lst, 'w').write(''.join(f"file '{SEG}/{s}.mp4'\n" for s in scenes))
joined = f'{ROOT}/work/joined.mp4'
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                '-c', 'copy', joined], check=True)
ass = f'{ROOT}/work/mv17_kinetic.ass'
tex = "eq=saturation=0.88:brightness=0.015:contrast=0.98,vignette=PI/5,noise=alls=3:allf=t"

def encode(vf, out, audio=True):
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', joined]
    if audio:
        cmd += ['-i', f'{ROOT}/track.mp3']
    cmd += ['-vf', vf, '-map', '0:v:0']
    if audio:
        cmd += ['-map', '1:a:0', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']
    cmd += ['-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
            '-pix_fmt', 'yuv420p', '-r', '24', '-movflags', '+faststart', out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-800:]); sys.exit(1)

# pre-grain (ASS only) for zero-still enumeration
encode(f"ass={ass}", f'{ROOT}/work/master_pregrain.mp4')
# house master (ASS + texture)
encode(f"ass={ass},{tex}", f'{ROOT}/masters/mv17_fridge_light_mystery_16x9.mp4')
print('assembly done')
