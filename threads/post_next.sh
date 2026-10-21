#!/bin/bash
# WuBuTV Threads poster — posts the next unposted bumper (newest first).
# Usage: post_next.sh
# Exit 0 on success or clean skip, 1 on failure needing attention.

set -euo pipefail

THREADS_DIR=~/workspace/wubutv-network/threads
BUMPERS_DIR=~/workspace/wubutv-network/bumpers
LEDGER=$THREADS_DIR/THREADS_POSTS.md
WORK=~/workspace/threads
ACCOUNT_ID=17841463063141818

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

# 3. Resolve file and title (fallback if slate row not yet committed)
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

# Threads text cap: 500 chars — truncate caption if needed
if [ ${#caption} -gt 480 ]; then
  caption="${caption:0:477}..."
fi

# 5. Stage files under ~/workspace/threads/
mkdir -p "$WORK"
cp "$file" "$WORK/b${next}_th.mp4"
ffmpeg -y -v error -ss 5 -i "$WORK/b${next}_th.mp4" -vframes 1 -q:v 3 "$WORK/b${next}_th_cover.jpg"

# 6. Post — capture CLI stderr WITHOUT set -e killing the script before we
#    can print it (same silent-failure fix as instagram/post_next.sh).
result=$(/opt/hatch/bin/threads-cli publish-post --account-id $ACCOUNT_ID \
  --text "$caption" \
  --media-item "{\"file\":\"$WORK/b${next}_th.mp4\",\"cover\":\"$WORK/b${next}_th_cover.jpg\"}" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
# 429 = stop for the day. Check BEFORE the generic CLI-failure exit: a 429
# usually comes with a non-zero exit, and the exit-2 path is the documented
# contract for rate limits (workers key PAUSE_FLAG creation off it).
if echo "$result" | grep -qiE "rate limit|429"; then
  echo "THREADS RATE LIMIT — stopping until next day"
  rm -f "$WORK/b${next}_th.mp4" "$WORK/b${next}_th_cover.jpg"
  exit 2
fi
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: threads-cli exited ${cli_rc} for B-${next}"
  rm -f "$WORK/b${next}_th.mp4" "$WORK/b${next}_th_cover.jpg"
  exit 1
fi

post_id=$(echo "$result" | grep -oE '"post_id":"[0-9]+"' | grep -oE '[0-9]+' | head -1)
if [ -z "$post_id" ]; then
  echo "FAIL: no post_id in result for B-${next}"
  rm -f "$WORK/b${next}_th.mp4" "$WORK/b${next}_th_cover.jpg"
  exit 1
fi

# 7. Ledger — commit immediately. An uncommitted ledger row was destroyed by
# the cdn-sync orphan-branch checkout dance on 2026-10-18; never leave a
# published row uncommitted.
now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
echo "| B-${next} | ${title} | ${now} | ${post_id} | ${caption} | ${hset} | posted |" >> "$LEDGER"
git -C ~/workspace/wubutv-network add threads/THREADS_POSTS.md 2>/dev/null && \
  git -C ~/workspace/wubutv-network -c user.name="WuBu" -c user.email="wubu@waefrebeorn" commit -m "threads: post B-${next} \"${title}\"" --quiet 2>/dev/null || true

# 7b. Registry back-write (2026-10-19): mark TT-posted so the recycle gate can
# fill. registry_sync_new first (row may not exist for fresh numbers).
python3 ~/workspace/wubutv-network/assembly/registry_sync_new.py >/dev/null 2>&1 || true
python3 ~/workspace/wubutv-network/assembly/registry_backwrite.py --column TT-posted --unit "B-${next}" >/dev/null 2>&1 || true
git -C ~/workspace/wubutv-network add assembly/CLIP_REGISTRY.md 2>/dev/null && \
  git -C ~/workspace/wubutv-network -c user.name="WuBu" -c user.email="wubu@waefrebeorn" commit -m "threads: registry TT-posted B-${next}" --quiet 2>/dev/null || true

# 8. Cleanup staged files
rm -f "$WORK/b${next}_th.mp4" "$WORK/b${next}_th_cover.jpg"

echo "POSTED: B-${next} \"${title}\" post_id=${post_id}"
