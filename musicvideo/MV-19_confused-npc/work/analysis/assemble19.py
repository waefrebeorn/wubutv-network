#!/usr/bin/env python3
"""MV-19 assembly (SINGLE PASS — MV-17 lesson): concat segments ->
joined.mp4 -> PROBE joined == 3686f BEFORE any master encode ->
pre-grain master (ASS only, for zero-still enumeration) ->
house master (ASS + texture pass, CRF 18, AAC from track.mp3)."""
import subprocess, os, sys

ROOT = os.path.expanduser('~/workspace/wubutv-network/musicvideo/MV-19_confused-npc')
SEG = f'{ROOT}/work/segments'
lst = f'{SEG}/concat_list.txt'
scenes = ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10',
          'S11', 'S12', 'S13', 'S13B', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19',
          'S19B', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S25B', 'S26', 'S27',
          'S28', 'S28B', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36']
open(lst, 'w').write(''.join(f"file '{SEG}/{s}.mp4'\n" for s in scenes))
joined = f'{ROOT}/work/joined.mp4'
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
                '-c', 'copy', joined], check=True)

def frames(p):
    return int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-count_frames', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', p]).decode().strip())

nf = frames(joined)
print(f'joined.mp4 frames: {nf} (expect 3686)')
assert nf == 3686, f'joined.mp4 has {nf} frames, expected 3686 — STOP before master encode'

ass = f'{ROOT}/work/mv19_kinetic.ass'
tex = "eq=saturation=0.90:brightness=0.012:contrast=0.99,vignette=PI/5,noise=alls=3:allf=t"

def encode(vf, out):
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', joined,
           '-i', f'{ROOT}/track.mp3',
           '-vf', vf, '-map', '0:v:0', '-map', '1:a:0',
           '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2',
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
           '-pix_fmt', 'yuv420p', '-r', '24', '-movflags', '+faststart', out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-800:]); sys.exit(1)

os.makedirs(f'{ROOT}/masters', exist_ok=True)
encode(f"ass={ass}", f'{ROOT}/work/master_pregrain.mp4')
print('pre-grain master done')
encode(f"ass={ass},{tex}", f'{ROOT}/masters/mv19_confused_npc_16x9.mp4')
print('house master done')
print(f'master frames: {frames(f"{ROOT}/masters/mv19_confused_npc_16x9.mp4")}')
