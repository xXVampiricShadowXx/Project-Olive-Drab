import pathlib
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IGNORED_PARTS = {".git", "node_modules"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}


def heading_anchor(heading):
    heading = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", heading)
    heading = re.sub(r"<[^>]*>", "", heading).lower()
    heading = "".join(
        character
        for character in heading
        if character in "-_"
        or not unicodedata.category(character).startswith(("P", "S"))
    )
    return heading.replace(" ", "-")


def anchors(text):
    result = set()
    counts = {}
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker.group(1)[0]
            elif marker.group(1)[0] == fence:
                fence = None
            continue
        if fence:
            continue
        for identifier in re.findall(r'<[^>]+\b(?:id|name)=["\']([^"\']+)["\']', line):
            result.add(identifier)
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            anchor = heading_anchor(heading.group(1))
            suffix = counts.get(anchor, 0)
            counts[anchor] = suffix + 1
            result.add(anchor + (f"-{suffix}" if suffix else ""))
    return result


def validate(root):
    root = root.resolve()
    failures = []
    anchor_cache = {}
    for document in sorted(root.rglob("*.md")):
        if any(part in IGNORED_PARTS for part in document.relative_to(root).parts):
            continue
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            if not target:
                continue
            parsed = urlsplit(target)
            if parsed.scheme in EXTERNAL_SCHEMES:
                continue
            candidate = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
            try:
                candidate.relative_to(root)
            except ValueError:
                failures.append(f"{document}: link escapes repository: {raw_target}")
                continue
            if not candidate.exists():
                failures.append(f"{document}: missing target: {raw_target}")
                continue
            if parsed.fragment:
                if not candidate.is_file() or candidate.suffix.lower() != ".md":
                    failures.append(f"{document}: fragment target is not Markdown: {raw_target}")
                    continue
                if candidate not in anchor_cache:
                    anchor_cache[candidate] = anchors(candidate.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in anchor_cache[candidate]:
                    failures.append(f"{document}: missing fragment: {raw_target}")
    return failures


def main():
    failures = validate(ROOT)
    if failures:
        print("\n".join(failures))
        return 1
    print("All relative Markdown links and fragments point to existing repository targets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
