#!/usr/bin/env python3
"""MV-14 scene table computation: song line spans + take line spans -> warp f, take-start a.
f = song_span / take_span (builder convention: setpts=f*PTS, f=out/in).
a = take_first_start - (song_first_start - slot_start)/f  (onset alignment, clamped >=0).
Per-word landing error measured after the uniform warp.
"""
import json

SONG = json.load(open('analysis/SONG_WORDS.json'))['words']
TAKE = json.load(open('/tmp/mv14_take_words.json'))

# plan slot boundaries (scene -> (start, end)); boundary moves adjudicated in-line
SLOTS = {
 'S01':(0.00,2.83),'S02':(2.83,5.43),'S03':(5.43,8.02),'S04':(8.02,10.62),'S05':(10.62,13.21),
 'S06':(13.21,16.14),'S07':(16.14,18.40),'S08':(18.40,21.04),'S09':(21.04,23.59),'S10':(23.59,26.22),
 'S11':(26.22,29.02),'S12':(29.02,31.64),'S13':(31.64,34.56),'S14':(34.56,36.56),'S15':(36.56,37.86),
 'S16':(37.86,39.16),'S17':(39.16,41.75),'S18':(41.75,43.05),'S19':(43.05,44.58),'S20':(44.58,46.44),
 'S21':(46.44,47.74),'S22':(47.74,49.52),'S23':(49.52,52.18),'S24':(52.18,55.90),'S25':(55.90,58.49),
 'S26':(58.49,60.88),'S27':(60.88,63.22),'S28':(63.22,65.56),'S29':(65.56,68.28),'S30':(68.28,70.74),
 'S31':(70.74,73.33),'S32':(73.33,76.54),'S33':(76.54,78.07),'S34':(78.07,79.37),'S35':(79.37,80.94),
 'S36':(80.94,83.32),'S37':(83.32,84.62),'S38':(84.62,86.24),'S39':(86.24,87.54),'S40':(87.54,89.90),
 'S41':(89.90,91.34),'S42':(91.34,94.02),'S43':(94.02,98.50),'S44':(98.50,101.26),'S45':(101.26,103.44),
 'S46':(103.44,106.24),'S47':(106.24,108.76),'S48':(108.76,112.16),'S49':(112.16,113.46),'S50':(113.46,115.10),
 'S51':(115.10,117.69),'S52':(117.69,120.56),'S53':(120.56,122.66),'S54':(122.66,123.96),'S55':(123.96,125.54),
 'S56':(125.54,128.20),'S57':(128.20,132.55),'S58':(132.55,137.74),'S59':(137.74,142.93),'S60':(142.93,148.12),
 'S61':(148.12,150.72),'S62':(150.72,153.31),'S63':(153.31,155.90),'S64':(155.90,158.50),'S65':(158.50,161.60),
}
# song line spans (measured) per singing scene; take line spans (take-local, the ledgered rendition)
LINES = {
 'S06':((14.14,16.14),(1.46,3.00)),'S07':((16.36,18.34),(1.04,2.60)),'S08':((19.10,21.04),(0.00,2.00)),
 'S09':((21.46,23.32),(0.86,2.18)),'S10':((23.32,26.22),(0.00,1.72)),'S11':((26.96,29.02),(0.50,1.92)),
 'S12':((29.02,31.64),(0.00,1.80)),'S13':((31.64,34.56),(0.00,1.62)),'S15':((36.44,37.80),(0.00,1.84)),
 'S16':((37.80,39.16),(0.00,2.18)),'S18':((41.26,42.96),(0.00,1.68)),'S19':((42.96,44.58),(0.00,1.06)),
 'S21':((46.44,47.36),(0.52,1.14)),'S22':((47.36,49.52),(0.00,2.52)),'S23':((49.52,52.18),(0.00,2.26)),
 'S25':((55.90,58.16),(0.00,2.54)),'S26':((58.16,60.06),(0.00,2.32)),'S27':((60.88,63.22),(0.00,1.68)),
 'S28':((63.22,65.56),(0.00,1.20)),'S29':((65.56,68.28),(0.00,2.24)),'S30':((68.46,70.74),(2.44,5.96)),
 'S31':((70.74,73.24),(0.00,1.74)),'S32':((73.24,76.54),(0.00,2.24)),'S34':((77.78,79.50),(0.00,1.76)),
 'S35':((79.58,80.94),(0.00,1.78)),'S37':((83.32,84.72),(0.00,1.40)),'S38':((84.84,86.24),(0.00,2.46)),
 'S39':((86.24,87.36),(0.00,0.54)),'S40':((89.38,89.90),(3.78,4.56)),'S41':((89.96,91.34),(0.00,2.30)),
 'S42':((91.34,94.02),(0.00,2.10)),'S43':((94.02,95.24),(0.00,1.44)),'S44':((98.50,101.26),(0.00,2.86)),
 'S45':((101.26,103.44),(2.04,3.90)),'S46':((103.44,106.24),(0.00,2.18)),'S47':((106.24,108.76),(1.16,2.82)),
 'S49':((112.16,113.64),(0.00,1.56)),'S50':((113.72,115.10),(4.02,5.74)),'S51':((115.10,116.30),(0.00,1.40)),
 'S52':((117.40,120.56),(0.00,2.94)),'S54':((122.66,124.08),(0.00,1.50)),'S55':((124.08,125.54),(0.00,2.78)),
 'S56':((125.54,128.20),(0.66,2.78)),
}
# special handling notes
SPECIAL = {
 'S37': 'MOUTH ANCHOR: take audio lags mouth ~0.88s; visual line is take 0-1.40 (mouth open frame 0); f=1.000, a=0',
 'S39': 'BAD-WORD: "Clip" 2.07x only; "it" 7.45x UNWARPABLE -> tail covers 87.36-89.00 (see S40)',
 'S40': 'segment = S39-take tail 87.54-89.00 + S40 take "post it" 89.00-89.90; boundary S40/S41 moved 89.70->89.90',
 'S43': 'two-part: line 0-1.44 warped 0.85x, tail 1.44-3.57 stretched to fill slot',
 'S08': 'END-ALIGNED: take sings from frame 0, song line starts 0.70s into slot; f=1.32 lands the line end exact, onset 0.70s early (disclosed)',
 'S46': 'ledger warp 0.78x is INVERTED; true span warp = 2.80/2.18 = 1.28x',
 'S55': 'f=0.52x; a clamps at 0 (onset alignment needs -0.23s); line lands 0.12s early (disclosed)',
}
def contract(ss, se): return round(se*24) - round(ss*24)

rows = []
tot = 0
for i in range(1, 66):
    s = f'S{i:02d}'
    ss, se = SLOTS[s]
    c = contract(ss, se); tot += c
    if s in LINES:
        (ls, le), (ts, te) = LINES[s]
        f = (le - ls) / (te - ts)
        a = ts - (ls - ss) / f
        a_clamped = max(0.0, a)
        win_s = c / 24 / f
        b = a_clamped + win_s
        # per-word error: song words in line span vs take words in take span
        sw = [w for w in SONG if ls - 0.01 <= w['start'] < le + 0.01]
        key = s
        tw = [w for w in TAKE.get(key, []) if ts - 0.01 <= w['start'] < te + 0.01]
        errs = []
        for j, (w1, w2) in enumerate(zip(sw, tw)):
            pred = (w2['start'] - a_clamped) * f + ss
            errs.append((w1['word'], round(pred - w1['start'], 2)))
        rows.append((s, ss, se, c, round(f,3), round(a_clamped,2), round(b,2), errs, SPECIAL.get(s,'')))
    else:
        # wordless: f=1.0, a=0, window=contract; if contract > usable pre-fade 3.57s, stretch
        dur = se - ss
        if dur <= 3.57:
            f, a, b = 1.0, 0.0, dur
        else:
            f = dur / 3.57
            a, b = 0.0, 3.57
        rows.append((s, ss, se, c, round(f,3), round(a,2), round(b,2), [], 'wordless' + (' STRETCH %.2fx (slot %.2fs > 3.57s pre-fade)' % (f, dur) if dur > 3.57 else '')))
print(f'TOTAL FRAMES: {tot} (expect 3878 = {161.60*24:.1f})')
for r in rows:
    s, ss, se, c, f, a, b, errs, note = r
    maxe = max([abs(e[1]) for e in errs], default=0)
    flag = '  <-- MAXERR %.2fs' % maxe if maxe > 0.30 else ''
    print(f"{s} {ss:6.2f}-{se:6.2f} {c:3d}f f={f:.3f} a={a:.2f} b={b:.2f} {note}{flag}")
    if errs and maxe > 0.15:
        print(f"     word errs: {errs}")
json.dump([{'scene': r[0], 'ss': r[1], 'se': r[2], 'frames': r[3], 'f': r[4], 'a': r[5], 'b': r[6], 'note': r[8]} for r in rows], open('work/assembly/scene_table.json','w'), indent=1)
