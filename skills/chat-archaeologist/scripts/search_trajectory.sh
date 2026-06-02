#!/bin/bash
# 会话考古学家 🏛️ - 搜索历史聊天记录
# 用法: search-trajectory <关键词> [日期] [可选: --after HH:MM --before HH:MM]

set -e

KEYWORD="$1"
DATE_FILTER="$2"
AFTER_TIME=""
BEFORE_TIME=""

# Parse optional time filters
shift 2 2>/dev/null || true
while [ $# -gt 0 ]; do
  case "$1" in
    --after) AFTER_TIME="$2"; shift 2 ;;
    --before) BEFORE_TIME="$2"; shift 2 ;;
    *) shift ;;
  esac
done

if [ -z "$KEYWORD" ]; then
  echo "用法: search-chat <关键词> [日期] [--after HH:MM] [--before HH:MM]"
  echo ""
  echo "示例:"
  echo "  search-chat 复习              # 搜索所有含'复习'的对话"
  echo "  search-chat 过程控制 2026-05-30  # 限定日期"
  echo "  search-chat 考试 2026-05-30 --after 12:00 --before 16:00"
  exit 1
fi

SESSION_DIR="${HOME}/.openclaw/agents/main/sessions"
if [ ! -d "$SESSION_DIR" ]; then
  echo "❌ 会话目录不存在: $SESSION_DIR"
  exit 1
fi

found_any=false

for f in "$SESSION_DIR"/*.trajectory.jsonl; do
  [ -f "$f" ] || continue
  fname=$(basename "$f" .trajectory.jsonl)
  size=$(ls -lh "$f" | awk '{print $5}')

  # Extract user messages that match keyword
  # Using jq to get prompt.submitted entries with user messages
  msgs=$(jq -r 'select(.type=="prompt.submitted") | .data.messages[]? | select(.role=="user") | .content[]? | select(.type=="text") | .text' "$f" 2>/dev/null)

  if echo "$msgs" | grep -qi "$KEYWORD" 2>/dev/null; then
    # Found a match - get session start time
    start_ts=$(jq -r 'select(.type=="session.started") | .ts[:19]' "$f" 2>/dev/null | head -1)
    start_local=$(date -d "$start_ts" +"%Y-%m-%d %H:%M CST" 2>/dev/null || echo "$start_ts")

    # Apply date filter
    if [ -n "$DATE_FILTER" ]; then
      if ! echo "$start_local" | grep -q "$DATE_FILTER"; then
        continue
      fi
    fi

    found_any=true

    echo ""
    echo "━━━ 会话: ${fname:0:12}... | 开始: $start_local | 大小: $size ━━━"

    # Extract all user messages with timestamps
    echo "━━━ 用户消息 ━━━"
    jq -r 'select(.type=="prompt.submitted") | .data.messages[]? | select(.role=="user") | .content[]? | select(.type=="text") | .text' "$f" 2>/dev/null | grep -vi "\[cron:" | while read -r msg; do
      # Extract time from message (format: [Sat 2026-05-30 HH:MM GMT+8])
      time_part=$(echo "$msg" | grep -oP '\d{2}:\d{2}(?= GMT)' 2>/dev/null || echo "??:??")
      # Apply time filters
      if [ -n "$AFTER_TIME" ] && [ "$(echo "$time_part" | tr -d ':')" -lt "$(echo "$AFTER_TIME" | tr -d ':')" ]; then
        continue
      fi
      if [ -n "$BEFORE_TIME" ] && [ "$(echo "$time_part" | tr -d ':')" -gt "$(echo "$BEFORE_TIME" | tr -d ':')" ]; then
        continue
      fi
      # Clean time prefix for display
      clean_msg=$(echo "$msg" | sed 's/\[.*GMT[+-]8\] //')
      echo "  $time_part → $clean_msg" | head -3
    done

    # Extract assistant text responses
    echo "━━━ 助手回复摘要 ━━━"
    jq -r 'select(.type=="model.completed") | .data.assistantTexts[]' "$f" 2>/dev/null | while read -r reply; do
      first_line=$(echo "$reply" | head -1 | cut -c1-80)
      [ -n "$first_line" ] && echo "  💬 $first_line..."
    done | head -5

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  fi
done

if [ "$found_any" = false ]; then
  echo "🔍 未找到包含「$KEYWORD」的会话记录"
fi
