#!/usr/bin/env python3
"""ONE SHORT E1 — conform 6 takes to 240f segments and join (one pass)."""
import subprocess, json, os, sys

EP = '/home/hatch/workspace/wubutv-network/new-era/morph-episodes/E2_one-short'
SEG = f'{EP}/work/segments'
os.makedirs(SEG, exist_ok=True)

VF = ('scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,'
      'fps=24,trim=end_frame=240,setpts=PTS-STARTPTS')
AF = 'atrim=0:10,asetpts=PTS-STARTPTS,apad=whole_dur=10'

TAKES = {1: 'U1_t2.mp4', 2: 'U2_t1.mp4', 3: 'U3_t1.mp4',
         4: 'U4_t1.mp4', 5: 'U5_t1.mp4', 6: 'U6_t1.mp4'}
segs = []
for u in range(1, 7):
    src = f'{EP}/takes/{TAKES[u]}'
    dst = f'{SEG}/seg_U{u}.mp4'
    r = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src,
                        '-vf', VF, '-af', AF,
                        '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', dst])
    if r.returncode != 0:
        sys.exit(f'conform failed U{u}')
    segs.append(dst)
    print(f'seg_U{u} conformed', flush=True)

lst = f'{EP}/work/concat.txt'
with open(lst, 'w') as f:
    for s in segs:
        f.write(f"file '{s}'\n")
joined = f'{EP}/work/joined.mp4'
r = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                    '-i', lst, '-c', 'copy', joined])
if r.returncode != 0:
    sys.exit('concat failed')

out = subprocess.run(['ffprobe', '-v', 'error', '-count_frames',
                      '-select_streams', 'v:0',
                      '-show_entries', 'stream=nb_read_frames,width,height,avg_frame_rate',
                      '-show_entries', 'format=duration',
                      '-of', 'json', joined], capture_output=True, text=True).stdout
pj = json.loads(out)
print(json.dumps(pj, indent=1))

# joint frames: last frame of each segment (frame 239) -> PNL-JOINT-U{n}.png
for u in range(1, 6):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', segs[u - 1],
                    '-vf', "select='eq(n\\,239)'", '-frames:v', '1',
                    f'{EP}/panels/PNL-JOINT-U{u}.png'])
print('joint frames harvested')
