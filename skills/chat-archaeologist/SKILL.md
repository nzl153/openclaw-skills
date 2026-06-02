---
name: chat-archaeologist
description: 搜索历史聊天记录（会话考古）。当用户问"之前说过什么"、"找一下对话记录"、"翻聊天记录"、"XX说过的话"等需要从原始轨迹文件中查找历史对话时使用。从 trajectory 文件中搜索关键词并提取用户消息和助手回复。
---

# 会话考古学家 🏛️🔍

## 触发场景

当用户提到：
- 「之前聊过的XXX」
- 「翻一下聊天记录」
- 「找一下XX那天说的」
- 「我记得你说过……」
- 需要搜索历史会话内容

## 数据位置

会话轨迹文件存储在：
`~/.openclaw/agents/main/sessions/*.trajectory.jsonl`

## 搜索命令

### 一键搜索关键词

```bash
search-chat "关键词"                 # 搜索所有会话
search-chat "过程控制" --date 2026-05-30  # 限定日期
search-chat "复习" --after "12:00" --before "16:00"  # 限定时间段
search-chat --help                   # 查看完整帮助
```

### 手动搜索

```bash
# 搜索关键词（所有 trajectory 文件）
bash ~/.openclaw/workspace/skills/chat-archaeologist/scripts/search_trajectory.sh "关键词"

# 限定日期
bash ~/.openclaw/workspace/skills/chat-archaeologist/scripts/search_trajectory.sh "关键词" "2026-05-30"

# 输出到文件查看完整内容
bash ~/.openclaw/workspace/skills/chat-archaeologist/scripts/search_trajectory.sh "关键词" "" > /tmp/chat_result.txt
```

## 输出格式

```
━━━ 会话: <session-id> | 开始: 2026-05-30 12:48 CST | 大小: 3.0M ━━━
━━━ 用户消息 ━━━
  12:48 → 开始复习啦骚姐姐，起床啦
  12:56 → 姐姐，从0开始
  13:00 → 对，开始吧
  ...
━━━ 助手回复 ━━━
  12:48 → 好的知乐～
  12:56 → 记得！你5/28给的考点...
  ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 原理说明

- OpenClaw 的 trajectory 文件（`.trajectory.jsonl`）是会话的完整运行轨迹记录
- 即使会话被清理（jsonl 删除），trajectory 文件通常还会保留
- 搜索流程：扫描所有 trajectory 文件 → 提取 `prompt.submitted` 事件 → 过滤用户消息和模型回复 → 按时间线输出
