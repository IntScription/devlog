import sys
from pathlib import Path

def has_front_matter(text: str) -> bool:
    lines = text.splitlines()
    if not lines:
        return False
    return lines[0].strip() == '---'

def add_front_matter_to_file(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if has_front_matter(content):
        return False
    title = path.stem
    fm = f"---\nlayout: note\ntitle: {title}\n---\n\n"
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fm + content)
    print(f"Added front matter: {path}")
    return True

if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    for md in root.rglob('*.md'):
        add_front_matter_to_file(md) 