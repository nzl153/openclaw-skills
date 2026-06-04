---
name: memory-system
description: 10层记忆系统 — 让你的 OpenClaw Agent 不再忘记你。
---

# 10层记忆系统（Memory System）

让你的 OpenClaw Agent 拥有永不遗忘的记忆。

从日记到长时记忆，从全文搜索到实体关系图联，从会话索引到能力自检——全链路覆盖。

## 架构一览

```
memory/                    ← 日记（每日 markdown）
MEMORY.md                  ← 长时记忆（精华沉淀）
~/.claw/
├── memory.json            ← 结构化事实（支持TTL过期）
├── memory-graph.json      ← 实体关联图（带温度🔥💧🧊）
└── session_index.json     ← 跨会话搜索索引
```

## 10层记忆详解

| 层级 | 载体 | 更新方式 | 作用 |
|------|------|---------|------|
| L1 | 日记 | 自动 | 当日原始事件 |
| L2 | 长时记忆文件 | 手动/自动提升 | 长期真理、教训 |
| L3 | 结构化事实 | 即时存 | 用户偏好、项目信息 |
| L4 | 图联 | 有关系时 | 实体关联，带温度标记 |
| L5 | 会话索引 | 会话结束时 | 跨会话搜索摘要 |
| L6 | 全文索引 | Cron+增量 | 日记全文搜索 |
| L7 | 每日快照 | Cron | 今日热点头脑风暴 |
| L8 | 反思日志 | Cron | 自我改进记录 |
| L9 | 错误日志 | 被纠正时 | 用户的纠正历史 |
| L10 | 能力注册表 | 配置时 | 工具可用性自检 |

## 工具

### `remember` — 统一写入
```bash
remember "发生了一件事"              # 日记 + 事实 + 索引
remember "速记" --short               # 只记日记
remember "永久事实" --perm            # 只记结构化
```

### `search` — 四层降级搜索
```bash
search "关键词"    # 会话索引 → 全文搜索 → 图联 → 文件grep
```

### `cap_check` — 能力自检
```bash
cap_check    # 一眼看清所有工具可用状态
```

### `memory_tool` — 结构化事实
```bash
memory_tool set <key> <value> [ns]
memory_tool get <key> [ns]
memory_tool list [ns]
```

### `session_index` — 历史会话搜索
```bash
session_index add <日期> <摘要>
session_index search <关键词>
```

### `graph` — 图联记忆
```bash
graph context <实体名>    # 看关联
graph add <A> 喜欢 <B>    # 加关系
graph stats               # 统计
```

### `cleanup_graph` — 关系老化清理
```bash
cleanup_graph    # 45天无更新自动删除，14天无更新自动冻结
```

## 快速开始

```bash
# 1. 把脚本链接到PATH
chmod +x scripts/*.py
ln -s $(pwd)/scripts/*.py /usr/local/bin/

# 2. 初始化日记目录
mkdir -p memory ~/.claw

# 3. 试试看
remember "Hello world" --short
cap_check
```

## 定时维护（示例Cron）

```
# 每晚
30 23 * * *  提取关系写入图联
35 23 * * *  提取智慧写入长时记忆
36 23 * * *  自动反思

# 每天凌晨
30 4  * * *  重建全文索引
0  6  * * *  刷新每日快照
5  5  * * *  清理过期TTL
```

## 许可证

MIT
