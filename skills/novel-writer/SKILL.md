---
name: novel-writer
description: Write and manage serialized Chinese webnovels for 番茄小说 and similar platforms. Use when the user wants to: (1) Write new chapters, (2) Plan plot, world-building, and character arcs, (3) Maintain story consistency across sessions via save files, (4) Edit or polish existing chapters, (5) Brainstorm story ideas and plot points. Covers popular webnovel genres (穿越修仙, 系统流, 都市, 玄幻, 重生等), 番茄 platform writing conventions (fast pace, frequent cliffhangers, chapter hooks, day-update for full attendance).
---

# Novel Writer Skill

## Core Workflow

### Session Start: Load Story State

At the start of each writing session, read the story save file to refresh memory:

```
references/<novel-name>-存档.md
```

This file contains: last chapter summary, current arc status, character states, next planned scene, and unresolved threads.

### Chapter Writing

1. **Load context**: Read archive → understand where the story is
2. **Review character/villain/plot tracking** from the save file
3. **Write draft chapter** (target: 2000-4000 characters for 番茄)
4. **User reviews** and gives feedback → iterate
5. **Update save file** with new chapter summary and next plans

### Chapter Structure (番茄)

Each chapter should follow:

```
【开篇钩子】→ 第一段制造悬念/冲突/爽点，抓住滑屏读者
【中段推进】→ 推进剧情，穿插爽点/笑点/金手指展示
【结尾悬念】→ 留钩子（突破前、大战前、秘密揭晓前断章）
```

- 番茄读者是"滑屏"阅读，前100字决定留存
- 段落短（2-4句一段为宜）
- 对话多、描写精炼
- 每章至少一个爽点/笑点/悬念

### Customizing Writing Style

Ask the user to define their preferred style on the first session, then record it in the save file:

- **文风**: e.g. 轻松吐槽风、热血战斗风、细腻文青风
- **节奏**: e.g. 开局慢（穿越感写足）、快节奏（第一章就开打）
- **金手指类型**: e.g. AI助手、系统面板、修炼加速、重生记忆
- **主角性格**: e.g. 聪明嘴贫、沉稳老练、热血冲动
- **世界观**: e.g. 游戏世界、修真大陆、都市异能

**Example preferences (from an actual user):**
- 文风: 轻松吐槽风，主角心理活动丰富
- 节奏: 开局慢，穿越感写足，不急着暴露金手指
- 金手指: AI助手型，前期高冷理性，中期展现情感萌芽，后期觉醒
- 主角: 聪明、嘴贫、遇到大事不怂
- 世界: 基于游戏设定，但现实化处理

## Story Save File Format

Each novel has its own 存档 file in `references/`:

```markdown
# <书名>-存档

## 上次写作会话
- 日期: YYYY-MM-DD
- 最后写到的章节: 第X章
- 最后写到的场景: [简述]

## 当前章节/下一章计划
- 当前/下一章标题:
- 本章目标:
- 需要出现的角色:
- 需要推进的剧情线:
- 待解决的伏笔:

## 角色状态
### 主角: [名字]
- 当前能力/实力阶段:
- 当前所在位置:
- 当前目标:
- 当前携带物品/金手指状态:
- 情绪状态:

### 女主角/金手指: [名字]
- 当前与主角关系状态:
- 阶段性进展:
- 特殊能力/功能:

### 配角
- [名字]: [当前状态和位置]

## 世界进展
- 当前主线:
- 已完成的关键事件:
- 进行中的危机/任务:
- 世界背景逐步揭露到哪一步:

## 未使用伏笔/素材
- [列表，待用的伏笔、角色、设定等]

## 下章建议方向
- [写作助手给的建议及待办]
```

### When No Save File Exists

If no save file exists, this is a new novel. Create one by asking the user:
1. Book title and genre
2. Core premise (one sentence)
3. Main characters
4. Key world-building rules
5. Writing preferences (vibe, pace, style)

## Writing Principles

### Genre-Specific Rules

For the genre the user chooses, follow its conventions. Detailed writing guides for each genre are in `references/writing-guide.md`:

**穿越/重生修仙玄幻:**
- 第一章靠五感描写立住穿越感，金手指不要急着出
- 修炼体系通过打斗和突破自然展示，不写说明文档
- 战力系统保持一致性，避免越到后面越崩
- 金手指有成长线，不是一开始就无敌

**武侠:**
- 体系更稳定，不容易战力崩坏
- 内力+招式+轻功+兵器，读者天然理解
- 武林门派、正邪对立，天然剧情驱动力
- 秘籍/兵器可以成为章节钩子和爽点载体

**都市/现代:**
- 主角的生活细节要真实（工作、租房、收入），让读者共情
- 金手指要和现实生活产生化学反应
- 职业装逼/财富逆袭/身份暴露是核心爽点

**系统流/签到流:**
- 第一章就要让读者明白系统规则
- 首奖要香，建立期待感
- 系统有成长性，后期会升级解锁新功能
- 系统面板不要每章都贴，偶尔出现即可

**游戏/电竞:**
- 让读者快速理解是什么游戏类型
- 操作描写要有真实感
- 游戏内成就影响现实生活

**科幻/末世:**
- 第一章快速建立世界观
- 生存压力拉满
- 人性刻画是核心看点

### 番茄平台注意事项
- 前3章决定留存率，开局要有吸引力
- 每章2000-4000字为宜
- 断章在爽点/悬念处，保持追读
- 更新频率建议日更，至少4000字/天拿全勤

## Scripts

- `scripts/save-novel-state.py` — Helper script to update the save file automatically after writing

## When to Read References

- **存档文件**: Read at the START of every writing session
- **Writing guide** (`references/writing-guide.md`): Read when:
  - Planning chapter structure and pacing
  - Designing cliffhangers or爽点 sequences
  - Need refresher on番茄platform writing conventions
  - User asks for style/plot adjustments
  - First session when starting a new novel (to internalize the rules)
