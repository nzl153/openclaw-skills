#!/usr/bin/env python3
"""search — Multi-layer search: session_index → FTS → grep"""
import sys, os, subprocess

WORKSPACE = os.environ.get("WORKSPACE", os.path.expanduser("~/.openclaw/workspace"))

def run_cmd(cmd, timeout=5):
    try:
        r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
        out = r.stdout.decode('utf-8', errors='replace')
        return r.returncode == 0, out.strip()
    except: return False, ""

def search_session_index(query):
    ok, out = run_cmd(["session_index", "search", query])
    return out.split("\n") if ok and out else []

def search_grep(query):
    diary_dir = os.path.join(WORKSPACE, "memory")
    if not os.path.isdir(diary_dir): return []
    ok, out = run_cmd(["grep", "-r", "-l", query, diary_dir], timeout=10)
    return [f"📄 {f.split('/')[-1]}" for f in out.split("\n")[:5]] if ok and out else []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search <keyword>")
        sys.exit(1)
    query = sys.argv[1]
    
    print(f"\n🔍 Searching: {query}")
    print("═" * 30)
    found = False
    
    r = search_session_index(query)
    if r:
        found = True; print(f"\n📋 Sessions ({len(r)}):")
        for line in r[:5]: print(f"  {line}")
    
    r = search_grep(query)
    if r:
        found = True; print(f"\n📁 Files:")
        for line in r[:5]: print(f"  {line}")
    
    if not found: print("\n📭 No results")
    print()
