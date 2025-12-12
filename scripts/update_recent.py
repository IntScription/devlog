import re
from pathlib import Path

INDEX_PATH = Path("index.md")
ARCHIVE_PATH = Path("archive.md")


def extract_recent_from_archive(limit=5):
    """Grab the most recent devlog lines from archive.md (assumes newest first)."""
    if not ARCHIVE_PATH.exists():
        return []
    lines = ARCHIVE_PATH.read_text(encoding="utf-8").splitlines()
    entries = [ln for ln in lines if ln.strip().startswith("- [")]
    return entries[:limit]


def replace_recent_block(index_text, new_lines):
    start = "<!-- DEVLOG-RECENT-START -->"
    end = "<!-- DEVLOG-RECENT-END -->"
    if start not in index_text or end not in index_text:
        # If markers are missing, leave unchanged
        return index_text
    pattern = re.compile(
        rf"{re.escape(start)}.*?{re.escape(end)}",
        flags=re.DOTALL,
    )
    block = "\n".join([start] + new_lines + [end])
    return pattern.sub(block, index_text)


def main():
    recent = extract_recent_from_archive()
    if not recent:
        return
    index_text = INDEX_PATH.read_text(encoding="utf-8")
    updated = replace_recent_block(index_text, recent)
    if updated != index_text:
        INDEX_PATH.write_text(updated, encoding="utf-8")
        print("Updated Recent Devlog Entries in index.md")


if __name__ == "__main__":
    main()

