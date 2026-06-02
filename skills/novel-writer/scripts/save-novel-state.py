import sys
import json
import os
from datetime import datetime

def update_save_file(novel_name, chapter_num, summary, next_plan, characters_update=None):
    """Update or create a novel save file with current state.
    
    Usage: python3 save-novel-state.py <novel-name> --chapter <num> --summary "<text>" --next "<text>"
    """
    save_dir = os.path.join(os.path.dirname(__file__), "..", "references")
    save_file = os.path.join(save_dir, f"{novel_name}-存档.md")
    
    # Parse args
    args = sys.argv[1:]
    
    if len(args) < 1:
        print("Usage: python3 save-novel-state.py <novel-name> --chapter <num> --summary <text> --next <text>")
        sys.exit(1)
    
    novel_name = args[0]
    chapter_num = None
    summary = ""
    next_plan = ""
    
    for i in range(1, len(args)):
        if args[i] == "--chapter" and i + 1 < len(args):
            chapter_num = args[i + 1]
        elif args[i] == "--summary" and i + 1 < len(args):
            summary = args[i + 1]
        elif args[i] == "--next" and i + 1 < len(args):
            next_plan = args[i + 1]
    
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    content = f"""# {novel_name}-存档

## 上次写作会话
- 日期: {today}
- 最后写到的章节: 第{chapter_num or '?'}章
- 最后写到的场景: {summary or '（待更新）'}

## 下一章计划
- 下一章目标: {next_plan or '（待更新）'}

## 状态速查
（下次写作时由写作助手更新）
"""
    
    with open(save_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Save file updated: {save_file}")
    return save_file

if __name__ == "__main__":
    update_save_file()
