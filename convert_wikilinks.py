import re
import sys
from pathlib import Path

def convert_links(text):
    # [[Target|Text]] → [Text](Target-with-dashes)
    text = re.sub(
        r'\[\[([^\]|]+)\|([^\]]+)\]\]',
        lambda m: f'[{m.group(2)}]({m.group(1).replace(" ", "-")})',
        text
    )
    # [[Target]] → [Target](Target-with-dashes)
    text = re.sub(
        r'\[\[([^\]]+)\]\]',
        lambda m: f'[{m.group(1)}]({m.group(1).replace(" ", "-")})',
        text
    )
    return text

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = convert_links(content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Converted: {path}")

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    for md_file in root.rglob("*.md"):
        process_file(md_file) 