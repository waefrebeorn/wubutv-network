#!/bin/bash
# WuBuTV Threads episode poster — posts the next unposted E1M/E2M assembly (newest first).
# E1M (60s) and E2M (120s) both fit the Threads <=5min video cap.
# Exit 0 on success/clean skip, 1 on failure, 2 on rate limit.

set -euo pipefail

THREADS_DIR=~/workspace/wubutv-network/threads
EP_DIR=~/workspace/wubutv-network/assembly
LEDGER=$THREADS_DIR/THREADS_EPISODES.md
WORK=~/workspace/threads
ACCOUNT_ID=17841463063141818

if [ ! -f "$LEDGER" ]; then
  echo "| Episode | Title | Posted (EDT) | Post ID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

posted=$(grep -oE '^\| E[12]M-[0-9]+' "$LEDGER" | grep -oE 'E[12]M-[0-9]+' | sort -u || true)

next_file=""
next_id=""
for f in $(ls "$EP_DIR"/e1m_*_16x9.mp4 "$EP_DIR"/e2m_*_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  id=$(echo "$base" | sed -E 's/^(e1m|e2m)_([0-9]+)_.*/\U\1-\2/')
  if ! echo "$posted" | grep -qx "$id"; then
    next_file=$f
    next_id=$id
    break
  fi
done

if [ -z "$next_file" ]; then
  echo "SKIP: no unposted episodes"
  exit 0
fi

title=$(grep -i "$next_id" ~/workspace/wubutv-network/assembly/ASSEMBLY_LOG.md 2>/dev/null | head -1 | cut -d'|' -f3 | sed 's/^ *//; s/ *$//' || true)
if [ -z "$title" ]; then
  title=$(basename "$next_file" _16x9.mp4 | sed -E 's/^(e1m|e2m)_[0-9]+_//; s/_/ /g')
fi

count=$(echo "$posted" | wc -l)
sets=("A" "B" "C" "D")
hset=${sets[$(( count % 4 ))]}
case $hset in
  A) tags="#WuBuTV #deadpan #skit" ;;
  B) tags="#WuBuTV #dryhumor #comedy" ;;
  C) tags="#WuBuTV #absurdist #shortfilm" ;;
  D) tags="#WuBuTV #surreal #indiefilm" ;;
esac
caption="${next_id} \"${title}\" — a WuBuTV minute. ~ WuBu ~ ${tags}"
if [ ${#caption} -gt 480 ]; then
  caption="${caption:0:477}..."
fi

mkdir -p "$WORK"
stage="$WORK/ep_th.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/ep_th_cover.jpg"
# Remove staged files on EVERY exit path (2026-10-23 audit fix).
trap 'rm -f "$stage" "$WORK/ep_th_cover.jpg"' EXIT

result=$(/opt/hatch/bin/threads-cli publish-post --account-id $ACCOUNT_ID \
  --text "$caption" \
  --media-item "{\"file\":\"$stage\",\"cover\":\"$WORK/ep_th_cover.jpg\"}" 2>&1)
echo "$result"

if echo "$result" | grep -qiE "rate limit|429"; then
  echo "THREADS RATE LIMIT — stopping until next day"
  rm -f "$stage" "$WORK/ep_th_cover.jpg"
  exit 2
fi

post_id=$(echo "$result" | grep -oE '"post_id":"[0-9]+"' | grep -oE '[0-9]+' | head -1)
if [ -z "$post_id" ]; then
  echo "FAIL: no post_id in result for ${next_id}"
  rm -f "$stage" "$WORK/ep_th_cover.jpg"
  exit 1
fi

now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
echo "| ${next_id} | ${title} | ${now} | ${post_id} | ${caption} | posted |" >> "$LEDGER"
rm -f "$stage" "$WORK/ep_th_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" post_id=${post_id}"
