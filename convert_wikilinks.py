import re
import sys
from pathlib import Path

def build_note_index(root):
    """
    Build a mapping from note title (without extension) to relative path from notes root.
    """
    index = {}
    for md_file in root.rglob("*.md"):
        # Get the note title (filename without extension)
        title = md_file.stem
        # Get the relative path from the notes root, with slashes and no .md
        rel_path = md_file.relative_to(root).with_suffix("")
        # Store as POSIX path (for URL)
        index[title] = rel_path.as_posix()
    return index

def convert_links(text, note_index):
    # Convert [[Target|Text]] to - [Text](relative-path)
    def repl_wikilink_with_text(match):
        target, text = match.group(1), match.group(2)
        url = note_index.get(target, target.replace(" ", "-"))
        return f"- [{text}]({url})"
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', repl_wikilink_with_text, text)

    # Convert [[Target]] to - [Target](relative-path)
    def repl_wikilink(match):
        target = match.group(1)
        url = note_index.get(target, target.replace(" ", "-"))
        return f"- [{target}]({url})"
    text = re.sub(r'\[\[([^\]]+)\]\]', repl_wikilink, text)

    # Ensure each list item is on its own line (avoid multiple dashes on one line)
    text = re.sub(r'(?<!\n)- ', '\n- ', text)
    # Remove possible double newlines at the start
    text = text.lstrip('\n')
    return text

def process_file(path, note_index):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = convert_links(content, note_index)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Converted: {path}")

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    note_index = build_note_index(root)
    for md_file in root.rglob("*.md"):
        process_file(md_file, note_index) 