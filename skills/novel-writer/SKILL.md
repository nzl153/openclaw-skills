---
name: novel-writer
description: Write and manage serialized Chinese webnovels for 番茄小说 and similar platforms. Use when the user wants to: (1) Write new chapters, (2) Plan plot, world-building, and character arcs, (3) Maintain story consistency across sessions via save files, (4) Edit or polish existing chapters, (5) Brainstorm story ideas and plot points. Covers popular webnovel genres (穿越修仙, 系统流, 都市, 玄幻, 重生等), 番茄 platform writing conventions (fast pace, frequent cliffhangers, chapter hooks, day-update for full attendance).
---

# Novel Writer Skill

## Core Workflow

### Session Start: Load Story State

At the start of each writing session, **按层级顺序读取存档**（详见下方📁存档系统）：

```
references/《书名》/
```

读取顺序（层级式，不跳步）：
1. **第一层·必读少量**: 5-已纠正错误.md → 0-设定速查.md → 2-剧情进度.md（当前计划）
2. **第二层·必读略多**: 1-角色档案.md → 3-章节摘要.md（近3章）
3. **第三层·按需**: 4-时间线.md / 更早的章节摘要

### Chapter Writing

1. **Load context**: 按层级顺序读存档 → 确认当前写到哪了
2. **Review character/villain/plot tracking**: 扫一眼角色表和伏笔清单
3. **Write draft chapter** (target: 2000-4000 characters for 番茄)
4. **User reviews** and gives feedback → iterate
5. **Update存档**: 更新2-剧情进度.md（进度+伏笔）+ 3-章节摘要.md（新章）+ 1-角色档案.md（实力变化）

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

## 📁 存档系统（长篇小说专用）

几十万字的长篇小说，**一个存档文件不够**。
每本书在 `references/` 下创建一个以书名命名的目录，拆成多个文件：

```
references/
  《书名》/
    ├── 0-设定速查.md          # 世界观、力量体系、核心规则（基本不变）
    ├── 1-角色档案.md          # 角色详细表（含实力变化记录）
    ├── 2-剧情进度.md          # 当前章节计划、未解伏笔、待办
    ├── 3-章节摘要.md          # 每章一句话+结尾场景（快速翻查前文）
    ├── 4-时间线.md            # 小说内日期/天数的变化
    └── 5-已纠正错误.md        # ⚠️ 写作前必读！知乐纠正过的坑
```

---

### ⚡ 写作前必读顺序（层级式）

每次新会话开始写本章前，**按这个顺序读**，不跳步：

```
第一层：【必读·少量】
  ① 5-已纠正错误.md          ← 30秒扫完，确认没再犯过的坑
  ② 0-设定速查.md            ← 1分钟扫完世界观和力量体系
  ③ 2-剧情进度.md → 当前章节计划  ← 知道写到哪了

第二层：【必读·略多】
  ④ 1-角色档案.md → 角色表  ← 扫角色表和短期变动群
  ⑤ 3-章节摘要.md → 前3章   ← 看最近3章写了什么

第三层：【按需查阅】
  ⑥ 4-时间线.md              ← 需要确认小说内天数时再读
  ⑦ 3-章节摘要.md → 更早章节 ← 需要查前文伏笔时再翻
```

> 原则：**必读文件尽量短**，不超过100行。长内容拆到独立的文件中，需要时再查。

---

### 各文件格式参考

#### 0-设定速查.md（短·必读）
```markdown
# ⚡ 设定速查

## 世界设定
- **世界观类型**: [例如: 修仙/武侠/都市/末世/游戏穿越]
- **核心设定**: [一句话概括世界怎么运作]
- **力量体系**: [如果有，列出等级]
- **金手指/系统规则**: [核心金手指说明]

## 写作要求
- **文风**: 轻松吐槽风
- **字数**: 每章3000-4000字
```

#### 1-角色档案.md（含实力变化记录）
```markdown
# 👥 角色档案

## 当前角色一览
| 角色 | 性别 | 身份 | 实力 | 当前位置 | 状态 |
|:----|:---:|:----|:----|:-------|:----|
| [主角名] | [男/女] | [身份] | [实力阶段] | [位置] | [状态] |
| [配角1] | [性别] | [身份] | [实力] | [位置] | [状态] |
| [配角2] | [性别] | [身份] | [实力] | [位置] | [状态] |

## 实力变化记录
### [主角名]
| 章节 | 事件 | 实力变化 |
|:---|:----|:--------|
| [章] | [事件] | [变化] |

### [配角名]
| 章节 | 事件 | 实力变化 |
|:---|:----|:--------|
| [章] | [事件] | [变化] |
```

#### 2-剧情进度.md
```markdown
# 🔗 剧情进度

## 上次写作
- **日期**: 
- **最后章节**: 第X章
- **结尾场景**: [一句话]

## 当前章计划
- **章节**: 第X章
- **目标**:
- **角色**:
- **回收伏笔**:

## 未解伏笔
- [ ] [伏笔] | 埋于第X章 | 说明

## 待办
- [ ] 
```

#### 3-章节摘要.md（每章一行）
```markdown
# 📖 章节摘要

| 章 | 标题 | 一句话剧情 | 结尾 |
|:-:|:---|:---------|:----|
| 1 | [标题] | [关键事件] | [结尾一句话] |
| 2 | [标题] | [关键事件] | [结尾一句话] |
| 3 | [标题] | [关键事件] | [结尾一句话] |
```

#### 4-时间线.md
```markdown
# 🕐 故事时间线

**第1天**（第X章）— [事件]
**第X天**（第X章）— [事件]
```

#### 5-已纠正错误.md（写作前必读）
```markdown
# ⚠️ 别再犯了！

- [ ] [已纠正的错误1]
- [ ] [已纠正的错误2]
- [ ] 写每一章前先确认上一章的结尾场景（看3-章节摘要.md）
```

### 当存档不存在时

如果 `references/《书名》/` 目录不存在，这是新书。创建目录和文件时询问用户：
1. 书名和类型
2. 核心设定
3. 主要角色
4. 写作偏好
5. 世界观规则

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

- **存档目录**: 按层级顺序读（1层→2层→3层），每次写作会话开始时必做
- **Writing guide** (`references/writing-guide.md`): Read when:
  - Planning chapter structure and pacing
  - Designing cliffhangers or爽点 sequences
  - Need refresher on番茄platform writing conventions
  - User asks for style/plot adjustments
  - First session when starting a new novel (to internalize the rules)
