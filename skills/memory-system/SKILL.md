---
name: memory-system
description: OpenClaw Agent 10-layer memory system. Diary + FTS search + Memory graph + Session indexing + Auto-maintenance cron pipeline.
---

# Memory System Skill

A complete memory system for OpenClaw agents: short-term diaries, long-term knowledge, associative graphs, and full-text search.

## Architecture

```
memory/                    # Diaries (daily markdown)
├── YYYY-MM-DD.md
├── YYYY-MM-DD.md
└── ...

MEMORY.md                  # Long-term promoted knowledge
~/.claw/
├── memory.json            # Structured facts (TTL-support)
├── memory-graph.json      # Entity-relation graph
└── session_index.json     # Cross-session search index
```

## 10 Memory Layers

| Layer | File | Update | Purpose |
|-------|------|--------|---------|
| L1 | `memory/YYYY-MM-DD.md` | Auto | Today's raw events |
| L2 | `MEMORY.md` | Manual/Promoted | Long-term truths, lessons |
| L3 | `memory.json` | On-set | Structured facts (user preferences, project info) |
| L4 | `memory-graph.json` | On-relation | Entity associations with temperature |
| L5 | `session_index.json` | On-end | Session summaries for cross-search |
| L6 | `.fts_index.db` | Cron+Incremental | Full-text search across diaries |
| L7 | `active-context.md` | Cron | Today's snapshot + hot topics |
| L8 | `~/.reflect/` | Cron | Self-improvement reflections |
| L9 | `5-已纠正错误.md` | On-error | User correction history |
| L10 | Capabilities registry | On-register | Tool availability check |

## Tools

### `remember` — Unified write
```bash
remember "something happened"              # diary + memory.json + FTS
remember "quick note" --short               # diary only
remember "permanent fact" --perm            # memory.json only
remember "tagged note" --tag=project       # with tag
```

### `search` — Unified search (4-layer fallback)
```bash
search "keyword"           # session_index → FTS → graph → grep
```

### `memory_tool` — Structured facts
```bash
memory_tool set <key> <val> [ns]     # store fact
memory_tool get <key> [ns]           # retrieve
memory_tool list [ns]                # browse namespace
memory_tool delete <key> [ns]        # remove
```

### `session_index` — Session history
```bash
session_index add <date> <summary>         # record a session
session_index search <keyword>             # find past sessions
session_index list [count]                 # recent sessions
```

### `graph` — Entity relations
```bash
graph context <entity>    # show entity associations (🔥hot 💧warm 🧊cold)
graph add <A> <rel> <B>   # add relation
graph stats               # statistics
```

### `cap_check` — Capability health
```bash
cap_check                 # check all registered tools
```

### `cleanup_graph` — TTL management
```bash
cleanup_graph             # remove 45d+ stale relations, freeze 14d+
```

## Setup

### 1. Create workspace tools
Copy `scripts/` to your workspace, or symlink:
```bash
chmod +x scripts/*.py
ln -s $(pwd)/scripts/*.py /usr/local/bin/
```

### 2. Initialize
```bash
mkdir -p memory ~/.claw
python3 scripts/fts_index.py init
```

### 3. Cron pipeline (example, adjust times)
```
30 23 * * *  extract_relations    # diary → graph
35 23 * * *  extract_wisdom       # diary → MEMORY.md
36 23 * * *  auto_reflect         # reflections
0  5  * * *  cleanup_memory       # TTL expiry
30 4  * * *  fts_index init       # daily FTS rebuild
0  6  * * *  gen_active_context   # refresh daily snapshot
```

## Files

### `references/_template/`

| Template | Description |
|----------|-------------|
| `0-设定速查.md` | World settings template (for novel writing) |
| `1-角色档案.md` | Character sheet template |
| `2-剧情进度.md` | Plot progress template |
| `3-章节摘要.md` | Chapter summary template |
| `4-时间线.md` | Timeline template |
| `5-已纠正错误.md` | Error log template |
| `diary.md` | Daily diary template |
| `MEMORY.md` | Long-term memory template |
| `active-context.md` | Daily snapshot template |
