#!/bin/bash
# Swing-keyframe runs for every sung take-scene in the v3 cut (build 3).
# s01_t1 and s07_t2 already exist in work/swing/ (tooling-agent examples).
set -u
P=~/workspace/wubutv-network/musicvideo/MV-5_easy-now-easy-now
cd "$P" || exit 1
mkdir -p work/swing/runs
TOOL="python3 work/swing/swing_keyframes.py --project $P --beat-grid $P/work/swing/beat_grid.json"
run() {
  name="$1"; take="$2"; w0="$3"; w1="$4"; line="$5"
  out="work/swing/runs/${name}.json"
  if [ -s "$out" ]; then echo "SKIP $name (exists)"; return; fi
  echo "=== RUN $name ($take window $w0-$w1) $(date -u +%H:%M:%S)"
  $TOOL --take "takes/$take" --window "$w0" "$w1" --line "$line" --out "$out" \
    && echo "OK $name" || echo "FAIL $name"
}
run s04_t1 mv5_s04_t1.mp4 22.0 31.48 "Bare feet on the boardwalk, salt on my skin, you came in laughing, said come on let's begin, blue shirt red bicycle"
run s05_t1 mv5_s05_t1.mp4 31.48 40.44 "Rolling past the pier, I was posted up right here, now you're pulling near, backpack half-zipped"
run s06_t1 mv5_s06_t1.mp4 40.44 44.61 "Keys in your hand, you nodded at the waves like"
run s06_t2 mv5_s06_t2.mp4 44.58 47.76 "Yeah, they already understand"
run s07_t1_a mv5_s07_t1.mp4 47.76 51.46 "Slow down, take your time, let the hard week fade"
run s07_t1_b mv5_s07_t1.mp4 52.8 56.5 "And my whole head replays"
run s08_t2 mv5_s08_t2.mp4 57.52 67.06 "Easy now easy now, we ride we ride, easy now easy now, with you by my side, easy now easy now, no need to run, easy now easy now, we hold the sun"
run s09_t1 mv5_s09_t1.mp4 67.06 76.8 "Easy now easy now, keep it loose keep it low, easy now easy now, let it drift let it go, easy now easy now, we're good where we are, easy now easy now, just two small sparks"
run s11_t4 mv5_s11_t4.mp4 85.16 93.8 "Vendor at the corner, calling mango sweet, socks in the sand, and the tide tapping time with our feet"
run s12_t1 mv5_s12_t1.mp4 93.8 102.4 "Your laugh hit the air, like a hand drum roll, I forgot the list forgot the bills, forgot what I was told"
run s15_t1 mv5_s15_t1.mp4 116.0 120.21 "And my whole head replays"
run s17_t1 mv5_s17_t1.mp4 130.78 140.52 "Easy now easy now, keep it loose keep it low, easy now easy now, let it drift let it go, easy now easy now, we're good where we are, easy now easy now, just two small sparks"
run s19b_t1 mv5_s19b_t1.mp4 152.36 155.72 "We still move with it, hand in my hand, no speech no show"
run s20_t1 mv5_s20_t1.mp4 155.72 158.06 "Heart in the breeze, and the bass move slow"
run s23_t1 mv5_s23_t1.mp4 169.16 176.04 "Easy now easy now, we ride we ride, easy now easy now, with you by my side, easy now easy now, no need to run"
run s25_t1 mv5_s25_t1.mp4 182.78 190.42 "Easy now easy now, we're good where we are, easy now easy now, just two small sparks"
run s27_t1 mv5_s27_t1.mp4 197.58 203.42 "Easy now, easy now"
echo "ALL DONE $(date -u +%H:%M:%S)"
