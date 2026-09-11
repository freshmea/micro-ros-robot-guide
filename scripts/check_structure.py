from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
errors = []
for path in root.rglob("*.md"):
    if any(part in {".git", "output", "node_modules"} for part in path.relative_to(root).parts):
        continue
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http:", "https:", "#", "mailto:")):
            continue
        if not (path.parent / target.split("#", 1)[0]).exists():
            errors.append(f"Missing link: {path.relative_to(root)} -> {target}")
manifest = root / "book/book-manifest.txt"
if manifest.exists():
    entries = [s.strip() for s in manifest.read_text(encoding="utf-8").splitlines() if s.strip() and not s.startswith("#")]
    if len(entries) != len(set(entries)):
        errors.append("Duplicate manifest entries")
    for entry in entries:
        if not (manifest.parent / entry).is_file():
            errors.append(f"Missing manuscript: {entry}")
    print(f"Manifest: {len(entries)} files")
if errors:
    raise SystemExit("\n".join(errors))
print("Structure and local file links OK")
