# OpenClaw Skills Collection

A curated collection of [OpenClaw](https://github.com/openclaw) Agent Skills.

## Skills

| Skill | Description |
|-------|-------------|
| [memory-system](skills/memory-system/) | 10-layer memory system: diary + FTS + graph + session indexing |
| [novel-writer](skills/novel-writer/) | Webnovel writing assistant with save-file system |
| [chat-archaeologist](skills/chat-archaeologist/) | Search and analyze session history |
| [verify-numbers](skills/verify-numbers/) | Number/date/time verification for AI outputs |

## Install

```bash
# Via ClawHub (if published)
clawhub install memory-system

# Manual: clone and symlink
git clone https://github.com/nzl153/openclaw-skills.git
ln -s $(pwd)/openclaw-skills/skills/* /path/to/your/skills/
```

## License

MIT
