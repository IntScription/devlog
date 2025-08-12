import re
import sys
from pathlib import Path
from urllib.parse import quote

def build_note_index(root):
    """
    Build a mapping from note title (filename without extension) to site-relative URL
    like '/notes/Folder/Subfolder/File.html' with percent-encoding for spaces.
    """
    index = {}
    for md_file in root.rglob("*.md"):
        title = md_file.stem
        rel_path = md_file.relative_to(root).with_suffix(".html").as_posix()
        # Prefix with '/notes/' and percent-encode path segments but keep slashes
        url = "/notes/" + quote(rel_path, safe="/")
        index[title] = url
    return index

def convert_links(text, note_index):
    # [[Target|Text]] → - [Text]({{ '/notes/..../File.html' | relative_url }})
    def repl_wikilink_with_text(match):
        target, link_text = match.group(1), match.group(2)
        url = note_index.get(target)
        if not url:
            # Fallback: naive dash replacement, .html
            url = "/notes/" + quote(target.replace(" ", "-") + ".html")
        return f"- [{link_text}]({{{{ '{url}' | relative_url }}}})"

    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", repl_wikilink_with_text, text)

    # [[Target]] → - [Target]({{ '/notes/..../File.html' | relative_url }})
    def repl_wikilink(match):
        target = match.group(1)
        url = note_index.get(target)
        if not url:
            url = "/notes/" + quote(target.replace(" ", "-") + ".html")
        return f"- [{target}]({{{{ '{url}' | relative_url }}}})"

    text = re.sub(r"\[\[([^\]]+)\]\]", repl_wikilink, text)

    # Ensure each list item is on its own line
    # Insert a newline before any '- ' that doesn't already start a line
    text = re.sub(r"(?<!\n)- ", "\n- ", text)
    # Trim leading newlines
    text = text.lstrip("\n")
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