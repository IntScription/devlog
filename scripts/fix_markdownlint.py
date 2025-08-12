import re
import sys
from pathlib import Path

MAX_LEN = 80


def wrap_list_item(line: str) -> list[str]:
    prefix = "- "
    text = line[len(prefix):]
    words = text.split()
    lines = []
    current = prefix
    for w in words:
        if len(current) + len(w) + 1 > MAX_LEN:
            lines.append(current.rstrip())
            current = "  " + w + " "
        else:
            current += w + " "
    if current.strip():
        lines.append(current.rstrip())
    return lines


def fix_markdownlint_errors(content: str) -> str:
    lines = content.split("\n")
    fixed: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Ensure blank line after headings
        fixed.append(line)
        if re.match(r"^#{1,6}\\s+", line):
            if i + 1 < len(lines) and lines[i + 1].strip() != "":
                fixed.append("")
            i += 1
            continue

        # Ensure blank line before list blocks
        if line.strip().startswith("- "):
            if len(fixed) >= 2 and fixed[-2].strip() != "" and not fixed[-2].strip().startswith("- "):
                fixed.insert(-1, "")
            # Wrap long list items
            if len(line) > MAX_LEN:
                fixed.pop()  # remove unwrapped
                for wrapped in wrap_list_item(line):
                    fixed.append(wrapped)
                i += 1
                continue

        # Remove multiple blank lines
        if line.strip() == "":
            while i + 1 < len(lines) and lines[i + 1].strip() == "":
                i += 1

        # Convert HTML nav to Markdown
        if '<div class="nav-links">' in line:
            nav = []
            i += 1
            while i < len(lines) and '</div>' not in lines[i]:
                m = re.search(r'href="([^"]+)"[^>]*>([^<]+)<', lines[i])
                if m:
                    href, text = m.group(1), m.group(2)
                    nav.append(f"[{text}]({href})")
                i += 1
            fixed.append("---")
            fixed.append("")
            fixed.append(" | ".join(nav))
            i += 1
            continue

        i += 1

    return "\n".join(fixed)


def process_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    new_content = fix_markdownlint_errors(content)
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Fixed: {file_path}")


def main():
    logs_dir = Path("logs")
    for log_dir in sorted(logs_dir.iterdir()):
        if log_dir.is_dir():
            index_file = log_dir / "index.md"
            if index_file.exists():
                process_file(index_file)


if __name__ == "__main__":
    main() 