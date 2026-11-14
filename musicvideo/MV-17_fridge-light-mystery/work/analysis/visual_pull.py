import json, subprocess, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = f'{ROOT}/work/master_pregrain.mp4'
OUT = f'{ROOT}/work/qc/vgate'; os.makedirs(OUT, exist_ok=True)
grid = json.load(open(f'{ROOT}/work/analysis/grid_lines.json'))
def grab(t, name, w=420):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{t:.2f}', '-i', SRC,
                    '-frames:v', '1', '-vf', f'scale={w}:-1', f'{OUT}/{name}.png'], check=True)
items = []
for ln in grid:
    if ln['kind'] != 'line': continue
    n = ln['n']
    grab(ln['start'], f'L{n:02d}_a'); grab(ln['start'] + 0.15, f'L{n:02d}_b')
    items.append(n)
# tile onset pairs: 6 lines per sheet (12 frames, 3 cols x 4 rows)
for s in range(0, len(items), 6):
    batch = items[s:s+6]
    files = []
    for n in batch: files += [f'{OUT}/L{n:02d}_a.png', f'{OUT}/L{n:02d}_b.png']
    listf = f'{OUT}/sheet{s//6}.txt'
    open(listf, 'w').write('\n'.join(f"file '{f}'" for f in files))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', listf,
                    '-filter_complex', 'tile=3x4:padding=4:margin=4', '-frames:v', '1',
                    f'{OUT}/onsets_{s//6}.png'], check=True)
print('onset sheets done:', (len(items)+5)//6)
# section strips: 6 frames evenly per section
sections = [('intro',0,7.5),('V1',7.5,24.9),('PC1',24.9,33.7),('C1',33.7,46.6),('PC2',46.6,58.0),
            ('V2',58.0,79.2),('C2',79.2,97.6),('BR',97.6,119.3),('C3',119.3,140.0),('OUT',140.0,162.8)]
for name, a, b in sections:
    files = []
    for k in range(6):
        t = a + (b-a)*(k+0.5)/6
        grab(t, f'sec_{name}_{k}'); files.append(f'{OUT}/sec_{name}_{k}.png')
    listf = f'{OUT}/sec_{name}.txt'
    open(listf, 'w').write('\n'.join(f"file '{f}'" for f in files))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', listf,
                    '-filter_complex', 'tile=3x2:padding=4:margin=4', '-frames:v', '1',
                    f'{OUT}/sec_{name}.png'], check=True)
print('section strips done')
