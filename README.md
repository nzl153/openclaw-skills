# OpenClaw Skills Collection

🧠 让你的 OpenClaw Agent 拥有记忆、会写小说、不嘴瓢。

## Skills

### 🧠 memory-system — 10层记忆系统
让你的 Agent **不再忘记你**。

| 功能 | 说明 |
|------|------|
| 📝 日记系统 | 每日自动记录，支持标签 |
| 🔍 四层搜索 | 会话索引 → 全文搜索 → 图联 → 文件grep |
| 🧠 图联记忆 | 实体关联网络，带温度标记🔥💧🧊 |
| 💾 结构化事实 | memory.json，支持TTL过期 |
| 📋 会话索引 | 跨会话搜索，秒级定位 |
| ✅ 能力自检 | 一眼看清所有工具状态 |
| 🧹 自动清理 | 45天无更新关系自动删除 |
| ⏰ 定时维护 | 示例Cron配置开箱即用 |

### 📖 novel-writer — 网文写作助手
番茄小说风格写作，带存档记忆系统。

| 功能 | 说明 |
|------|------|
| 📂 存档系统 | 设定+角色+进度+伏笔+原稿，全文件管理 |
| 📋 铁律检查 | 写完自动三查（名字/逻辑/前后矛盾） |
| 📐 番茄范式 | 开篇钩子→中段推进→结尾悬念 |
| 🎭 多流派 | 穿越/武侠/系统流/都市/游戏，写法指南 |

### 🔍 chat-archaeologist — 聊天记录考古
搜索和分析历史对话记录。

### 🔢 verify-numbers — 数字验证
防止AI嘴瓢的日期/数字/时间验证工具。

## Install

```bash
# 克隆仓库
git clone https://github.com/nzl153/openclaw-skills.git

# 安装想要的skill
chmod +x openclaw-skills/skills/memory-system/scripts/*.py
ln -s $(pwd)/openclaw-skills/skills/memory-system/scripts/*.py /usr/local/bin/

# 或者通过ClawHub（如果已发布）
clawhub install memory-system
```

## License

MIT
