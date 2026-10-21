#!/bin/bash
# WuBuTV Threads commercial poster — posts the next unposted AD spot (newest first).
# 10s spots fit the Threads <=5min video cap.
# Exit 0 on success/clean skip, 1 on failure, 2 on rate limit.

set -euo pipefail

THREADS_DIR=~/workspace/wubutv-network/threads
AD_DIR=~/workspace/wubutv-network/commercials
LEDGER=$THREADS_DIR/THREADS_ADS.md
WORK=~/workspace/threads
ACCOUNT_ID=17841463063141818

if [ ! -f "$LEDGER" ]; then
  echo "| Ad | Title | Posted (EDT) | Post ID | Caption | Posted |" > "$LEDGER"
  echo "|---|---|---|---|---|---|" >> "$LEDGER"
fi

posted=$(grep -oE '^\| AD-[0-9]+' "$LEDGER" | grep -oE 'AD-[0-9]+' | sort -u || true)

next_file=""
next_id=""
for f in $(ls "$AD_DIR"/ad*_16x9.mp4 2>/dev/null | sort -r); do
  base=$(basename "$f" .mp4)
  num=$(echo "$base" | grep -oE '^ad[0-9]+' | grep -oE '[0-9]+')
  id="AD-${num}"
  if ! echo "$posted" | grep -qx "$id"; then
    next_file=$f
    next_id=$id
    break
  fi
done

if [ -z "$next_file" ]; then
  echo "SKIP: no unposted commercials"
  exit 0
fi

title=$(grep -oE "^\| ${next_id} \"[^\"]+\"" ~/workspace/wubutv-network/slate/COMMERCIALS.md 2>/dev/null | head -1 | sed -E "s/^\\| ${next_id} \"//; s/\"\$//" || true)
if [ -z "$title" ]; then
  title=$(basename "$next_file" _16x9.mp4 | sed -E 's/^ad[0-9]+_//; s/_/ /g')
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
caption="${next_id} \"${title}\" — a WuBuTV spot. ~ WuBu ~ ${tags}"
if [ ${#caption} -gt 480 ]; then
  caption="${caption:0:477}..."
fi

mkdir -p "$WORK"
stage="$WORK/ad_th.mp4"
cp "$next_file" "$stage"
ffmpeg -y -v error -ss 5 -i "$stage" -vframes 1 -q:v 3 "$WORK/ad_th_cover.jpg"

result=$(/opt/hatch/bin/threads-cli publish-post --account-id $ACCOUNT_ID \
  --text "$caption" \
  --media-item "{\"file\":\"$stage\",\"cover\":\"$WORK/ad_th_cover.jpg\"}" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: threads-cli exited ${cli_rc} for ${next_id}"
fi

if echo "$result" | grep -qiE "rate limit|429"; then
  echo "THREADS RATE LIMIT — stopping until next day"
  rm -f "$stage" "$WORK/ad_th_cover.jpg"
  exit 2
fi

post_id=$(echo "$result" | grep -oE '"post_id":"[0-9]+"' | grep -oE '[0-9]+' | head -1)
if [ -z "$post_id" ]; then
  echo "FAIL: no post_id in result for ${next_id}"
  rm -f "$stage" "$WORK/ad_th_cover.jpg"
  exit 1
fi

now=$(TZ=America/New_York date "+%Y-%m-%d %H:%M EDT")
echo "| ${next_id} | ${title} | ${now} | ${post_id} | ${caption} | posted |" >> "$LEDGER"
rm -f "$stage" "$WORK/ad_th_cover.jpg"

echo "POSTED: ${next_id} \"${title}\" post_id=${post_id}"
