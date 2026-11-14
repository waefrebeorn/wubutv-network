#!/bin/bash
# WuBuTV Instagram poster — posts the next unposted bumper (newest first).
# Usage: post_next.sh
# Exit 0 on success or clean skip, 1 on failure needing attention.

set -euo pipefail

IG_DIR=~/workspace/wubutv-network/instagram
BUMPERS_DIR=~/workspace/wubutv-network/bumpers
LEDGER=$IG_DIR/INSTAGRAM_POSTS.md
WORK=~/workspace/instagram
ACCOUNT_ID=17841400684652688

# 1. Find posted B-numbers from ledger
posted=$(grep -oE '^\| B-[0-9]+' "$LEDGER" | grep -oE '[0-9]+' | sort -un || true)

# 2. Find highest-numbered bumper file NOT in ledger
next=""
for f in $(ls "$BUMPERS_DIR"/b*_16x9.mp4 2>/dev/null | grep -oE 'b[0-9]+' | grep -oE '[0-9]+' | sort -un | tac); do
  if ! echo "$posted" | grep -qx "$f"; then
    next=$f
    break
  fi
done

if [ -z "$next" ]; then
  echo "SKIP: no unposted bumpers"
  exit 0
fi

# 3. Resolve file and title
file=$(ls "$BUMPERS_DIR"/b${next}_*_16x9.mp4 | head -1)
title=$(grep -oE "^\| B-${next} \"[^\"]+\"" ~/workspace/wubutv-network/slate/BUMPERS.md | head -1 | sed -E 's/^\| B-[0-9]+ "//; s/"$//' || true)
if [ -z "$title" ]; then
  title="B-${next}"
fi

# 4. Build caption — tagline from TikTok queue if available, else generic
tagline=$(grep "^| B-${next} " ~/workspace/wubutv-network/tiktok/CAPTION_QUEUE.md 2>/dev/null | head -1 | cut -d'|' -f4 | sed 's/^ *//; s/ *$//' || true)
if [ -z "$tagline" ]; then
  tagline="~ WuBu ~"
fi

# Hashtag rotation: pick set based on count of posted (cycles A,B,C,D)
count=$(echo "$posted" | wc -l)
sets=("A" "B" "C" "D")
set_idx=$(( count % 4 ))
hset=${sets[$set_idx]}
case $hset in
  A) tags="#WuBuTV #deadpan #skit" ;;
  B) tags="#WuBuTV #dryhumor #comedy" ;;
  C) tags="#WuBuTV #absurdist #shortfilm" ;;
  D) tags="#WuBuTV #surreal #indiefilm" ;;
esac

# Extract just the tagline portion (strip the TikTok number/title prefix if present)
clean_tagline=$(echo "$tagline" | sed -E 's/^B-[0-9]+ "[^"]+" — //; s/ ~ WuBu ~.*//')
caption="B-${next} \"${title}\" — ${clean_tagline}. ~ WuBu ~ ${tags}"

# 5. Stage files under ~/workspace/
mkdir -p "$WORK"
cp "$file" "$WORK/b${next}_ig.mp4"
ffmpeg -y -v error -ss 5 -i "$WORK/b${next}_ig.mp4" -vframes 1 -q:v 3 "$WORK/b${next}_ig_cover.jpg"
# Remove staged files on EVERY exit path (2026-10-23 audit: the failure exits
# below leaked staged copies — b1265_ig from a 429 attempt, pairs back to Oct 17).
trap 'rm -f "$WORK/b${next}_ig.mp4" "$WORK/b${next}_ig_cover.jpg"' EXIT

# 6. Post — capture CLI stderr WITHOUT set -e killing the script before we
#    can print it (2026-10-18: `result=$(cli)` exits silently on CLI failure).
result=$(/opt/hatch/bin/instagram-cli post-feed --account-id $ACCOUNT_ID \
  --file "$WORK/b${next}_ig.mp4" \
  --cover "$WORK/b${next}_ig_cover.jpg" \
  --caption "$caption" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: instagram-cli exited ${cli_rc} for B-${next}"
  exit 1
fi

fbid=$(echo "$result" | grep -oE '"media_fbid":"[0-9]+"' | grep -oE '[0-9]+' | head -1 || true)
if [ -z "$fbid" ]; then
  echo "FAIL: no media_fbid in result for B-${next}"
  exit 1
fi

# 7. Ledger — commit immediately. An uncommitted ledger row was destroyed by
# the cdn-sync orphan-branch checkout dance on 2026-10-18; never leave a
# published row uncommitted.
now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
echo "| B-${next} | ${title} | ${now} | ${fbid} | ${caption} | ${hset} | posted |" >> "$LEDGER"
git -C ~/workspace/wubutv-network add instagram/INSTAGRAM_POSTS.md 2>/dev/null && \
  git -C ~/workspace/wubutv-network -c user.name="WuBu" -c user.email="wubu@waefrebeorn" commit -m "instagram: post B-${next} \"${title}\"" --quiet 2>/dev/null || true

# 7b. Registry back-write (2026-10-19): mark IG-posted so the recycle gate can
# fill. registry_sync_new first (row may not exist for fresh numbers).
python3 ~/workspace/wubutv-network/assembly/registry_sync_new.py >/dev/null 2>&1 || true
python3 ~/workspace/wubutv-network/assembly/registry_backwrite.py --column IG-posted --unit "B-${next}" >/dev/null 2>&1 || true
git -C ~/workspace/wubutv-network add assembly/CLIP_REGISTRY.md 2>/dev/null && \
  git -C ~/workspace/wubutv-network -c user.name="WuBu" -c user.email="wubu@waefrebeorn" commit -m "instagram: registry IG-posted B-${next}" --quiet 2>/dev/null || true

# 8. Cleanup staged files
rm -f "$WORK/b${next}_ig.mp4" "$WORK/b${next}_ig_cover.jpg"

echo "POSTED: B-${next} \"${title}\" fbid=${fbid}"
