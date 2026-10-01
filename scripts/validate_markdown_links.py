import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IGNORED_PARTS = {".git", "node_modules"}
EXTERNAL_PREFIXES = ("#", "http://", "https://", "mailto:", "tel:")

failures = []

for document in ROOT.rglob("*.md"):
    if any(part in IGNORED_PARTS for part in document.parts):
        continue
    text = document.read_text(encoding="utf-8")
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip().strip("<>")
        if not target or target.startswith(EXTERNAL_PREFIXES):
            continue
        target = unquote(urlsplit(target).path)
        candidate = (document.parent / target).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            failures.append(f"{document}: link escapes repository: {raw_target}")
            continue
        if not candidate.exists():
            failures.append(f"{document}: missing target: {raw_target}")

if failures:
    print("\n".join(failures))
    sys.exit(1)

print("All relative Markdown links point to existing repository paths.")
