import json
import re
import sys
import os
from collections import Counter

TEMPLATE_FILE = "template.html"
TASKS_FILE = "tasks.json"
OUTPUT_FILE = "Project3_TaskInventory_KSA_Analyzer.html"

KSA_KEYS = {
    "k": ["prod", "mech", "eng", "math", "comp", "engl", "admin", "cust", "safe", "chem", "des", "phys"],
    "s": ["opmon", "qc", "eqm", "trbl", "crit", "prob", "list", "read", "writ", "msk", "prog", "sys"],
    "a": ["man", "arm", "near", "psens", "ded", "info", "oral", "wcomp", "mrea", "vis", "react", "ctrl"],
}

VALID_INDUSTRIES = {"automotive", "ev_battery", "solar", "aerospace", "nuclear", "general_mfg"}
VALID_DEPTS = {"FLOOR", "ENGINEERING", "QUALITY", "LOGISTICS", "OFFICE", "IT"}
VALID_HAZARDS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

def load_tasks(path=TASKS_FILE):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_template(path=TEMPLATE_FILE):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def cmd_build():
    for f in [TEMPLATE_FILE, TASKS_FILE]:
        if not os.path.exists(f):
            print(f"ERROR: {f} not found.")
            sys.exit(1)
    tasks = load_tasks()
    template = load_template()
    placeholder = "/*{{TASKS_DATA}}*/"
    if placeholder not in template:
        print(f"ERROR: Placeholder not found in {TEMPLATE_FILE}")
        sys.exit(1)
    tasks_json = json.dumps(tasks, ensure_ascii=False, separators=(",", ":"))
    html = template.replace(f"const T={placeholder}[];", f"const T={tasks_json};")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {OUTPUT_FILE}")
    print(f"  Tasks: {len(tasks)}")
    print(f"  Size:  {len(html.encode('utf-8')) / 1024:.0f} KB")

def cmd_stats():
    tasks = load_tasks() if os.path.exists(TASKS_FILE) else extract_from_html(OUTPUT_FILE)
    print(f"Total tasks: {len(tasks)}")
    for label, key in [("Industry", "industry"), ("Department", "dept")]:
        print(f"\n{label} Distribution:")
        for k, v in Counter(t[key] for t in tasks).most_common():
            print(f"  {k:<20} {v:>3}")
    print(f"\nHazard Distribution:")
    haz = Counter(t["hazard"] for t in tasks)
    for level in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]:
        print(f"  {level:<12} {haz.get(level, 0):>3}")

def cmd_validate():
    tasks = load_tasks()
    errors = []
    ids_seen = set()
    for i, t in enumerate(tasks):
        tid = t.get("id", f"index_{i}")
        if tid in ids_seen: errors.append(f"[{tid}] Duplicate ID")
        ids_seen.add(tid)
        for field in ["id", "dept", "soc", "onet", "task", "hazard", "industry", "trir", "dart"]:
            if field not in t: errors.append(f"[{tid}] Missing: {field}")
        if t.get("industry") not in VALID_INDUSTRIES: errors.append(f"[{tid}] Bad industry")
        if t.get("dept") not in VALID_DEPTS: errors.append(f"[{tid}] Bad dept")
        for cat, keys in KSA_KEYS.items():
            for k in keys:
                if cat in t and k not in t[cat]: errors.append(f"[{tid}] Missing {cat}.{k}")
    print(f"Validated {len(tasks)} tasks")
    if errors:
        for e in errors[:20]: print(f"  ✗ {e}")
    else:
        print("  ✓ All checks passed")

def cmd_extract():
    tasks = extract_from_html(OUTPUT_FILE)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(tasks)} tasks")

def extract_from_html(path):
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    m = re.search(r"const T=(\[.*?\]);", html, re.DOTALL)
    if not m: raise ValueError("Could not find task data in HTML")
    return json.loads(m.group(1))

if __name__ == "__main__":
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "build"
    cmds = {"build": cmd_build, "stats": cmd_stats, "validate": cmd_validate, "extract": cmd_extract}
    if cmd in ("-h", "--help", "help"):
        print("Commands: build, stats, validate, extract")
    elif cmd in cmds:
        cmds[cmd]()
    else:
        print(f"Unknown: {cmd}. Try: build, stats, validate, extract")
