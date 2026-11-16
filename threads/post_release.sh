#!/bin/bash
# WuBuTV Threads release poster — posts ONE explicit file with ONE explicit
# caption (queue-driven; the release lane decides WHAT, this script only posts).
# Usage: post_release.sh <abs_file> <caption>
# Exit: 0 posted (prints "POSTED: post_id=<id>"), 2 rate limit, 1 other failure.
# Writes NO ledger/registry/queue state — the calling lane records the post.

set -uo pipefail

FILE=${1:-}
CAPTION=${2:-}
if [ -z "$FILE" ] || [ -z "$CAPTION" ]; then
  echo "FAIL: usage: post_release.sh <abs_file> <caption>"
  exit 1
fi
if [ ! -s "$FILE" ]; then
  echo "FAIL: file missing or empty: $FILE"
  exit 1
fi

# Threads text cap: 500 chars — truncate defensively (legacy post_next.sh rule).
if [ ${#CAPTION} -gt 480 ]; then
  CAPTION="${CAPTION:0:477}..."
fi

ACCOUNT_ID=17841463063141818
WORK=~/workspace/threads
mkdir -p "$WORK"
STAMP=$(date +%s)
STAGED="$WORK/release_${STAMP}.mp4"
COVER="$WORK/release_${STAMP}_cover.jpg"
trap 'rm -f "$STAGED" "$COVER"' EXIT

cp "$FILE" "$STAGED" || { echo "FAIL: could not stage $FILE"; exit 1; }
ffmpeg -y -v error -ss 5 -i "$STAGED" -vframes 1 -q:v 3 "$COVER" || {
  echo "FAIL: cover extraction failed for $FILE"; exit 1; }

# Capture CLI output WITHOUT set -e killing the script before we can read it
# (standing lesson from post_next.sh, 2026-10-18). 429 check comes BEFORE the
# generic failure exit: a 429 usually arrives with a non-zero exit, and exit 2
# is the documented rate-limit contract the lanes key their backoff off.
result=$(/opt/hatch/bin/threads-cli publish-post --account-id $ACCOUNT_ID \
  --text "$CAPTION" \
  --media-item "{\"file\":\"$STAGED\",\"cover\":\"$COVER\"}" 2>&1) || cli_rc=$?
cli_rc=${cli_rc:-0}
echo "$result"
if echo "$result" | grep -qiE "rate limit|429|too many requests"; then
  echo "RATE LIMIT: threads-cli reported a rate limit"
  exit 2
fi
if [ "$cli_rc" -ne 0 ]; then
  echo "FAIL: threads-cli exited ${cli_rc}"
  exit 1
fi

post_id=$(echo "$result" | grep -oE '"post_id":"[0-9]+"' | grep -oE '[0-9]+' | head -1 || true)
if [ -z "$post_id" ]; then
  echo "FAIL: no post_id in result"
  exit 1
fi

echo "POSTED: post_id=${post_id}"
exit 0
