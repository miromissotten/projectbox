# run from the site folder:  python check.py
import re
from pathlib import Path
root = Path(".")
html = (root / "index.html").read_text(encoding="utf-8-sig")
refs = re.findall(r'(?:src|href)="([^"]+)"', html)
missing = [r for r in refs if not r.startswith(("http", "#")) and not (root / r).exists()]
ids = set(re.findall(r'id="([^"]+)"', html))
anchors = [a for a in re.findall(r'href="#([^"]+)"', html) if a not in ids]
for t in ["article", "figure", "section", "nav"]:
    o, c = len(re.findall(rf"<{t}[ >]", html)), len(re.findall(rf"</{t}>", html))
    assert o == c, f"<{t}> unbalanced: {o} open / {c} close"
print("chips:", re.findall(r"chip chip-(\w+)", html))
print("missing files:", missing or "none")
print("broken anchors:", anchors or "none")
