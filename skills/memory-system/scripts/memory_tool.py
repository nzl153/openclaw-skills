#!/usr/bin/env python3
"""
memory_tool — Structured facts storage (memory.json)

Usage:
  memory_tool set <key> <value> [namespace]
  memory_tool get <key> [namespace]
  memory_tool list [namespace]
  memory_tool delete <key> [namespace]
"""
import json, os, sys, datetime

MEMORY_FILE = os.environ.get("MEMORY_FILE", os.path.expanduser("~/.claw/memory.json"))

def load():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE) as f:
            return json.load(f)
    return {}

def save(data):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def set_key(ns, key, value, ttl_days=0):
    data = load()
    if ns not in data:
        data[ns] = {}
    entry = {"_v": value}
    if ttl_days > 0:
        expiry = (datetime.date.today() + datetime.timedelta(days=ttl_days)).isoformat()
        entry["_e"] = expiry
        entry["_created"] = datetime.date.today().isoformat()
    data[ns][key] = entry
    save(data)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__.strip())
        sys.exit(1)
    cmd = args[0]
    data = load()
    if cmd == "set" and len(args) >= 3:
        ns = args[3] if len(args) > 3 else "default"
        set_key(ns, args[1], args[2])
        print(f"✅ [{ns}] {args[1]} = {args[2]}")
    elif cmd == "get" and len(args) >= 2:
        ns = args[2] if len(args) > 2 else "default"
        entry = data.get(ns, {}).get(args[1], {})
        val = entry.get("_v", entry) if isinstance(entry, dict) else entry
        print(val)
    elif cmd == "list":
        ns = args[1] if len(args) > 1 else None
        if ns:
            for k in data.get(ns, {}):
                print(f"  {k}")
        else:
            for ns_name in data:
                print(f"[{ns_name}]")
                for k in list(data[ns_name].keys())[:10]:
                    print(f"  {k}")
    elif cmd == "delete" and len(args) >= 2:
        ns = args[2] if len(args) > 2 else "default"
        if ns in data and args[1] in data[ns]:
            del data[ns][args[1]]
            save(data)
            print(f"✅ 已删除 [{ns}] {args[1]}")
    else:
        print("Unknown command")
