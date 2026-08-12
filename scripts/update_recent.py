import re
from pathlib import Path
from datetime import datetime

LOGS_DIR = Path("logs")
INDEX_PATH = Path("index.md")
CONFIG_PATH = Path("_config.yml")


def get_baseurl() -> str:
    if not CONFIG_PATH.exists():
        return ""
    for line in CONFIG_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r'baseurl:\s*"([^"]*)"', line.strip())
        if m:
            return m.group(1)
    return ""


def get_front_matter_title(index_file: Path) -> str:
    """Read the `title:` front matter value, mirroring archive.md's default."""
    lines = index_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return "Devlog"
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"title:\s*(.*)", line.strip())
        if m:
            title = m.group(1).strip().strip('"').strip("'")
            return title if title else "Devlog"
    return "Devlog"


def get_recent_logs(limit=5):
    """Newest log dirs by date, mirroring the sort archive.md uses."""
    entries = []
    for log_dir in LOGS_DIR.iterdir():
        if not log_dir.is_dir():
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})", log_dir.name)
        index_file = log_dir / "index.md"
        if not m or not index_file.exists():
            continue
        date_str = m.group(1)
        entries.append((datetime.strptime(date_str, "%Y-%m-%d"), date_str, index_file))
    entries.sort(key=lambda e: e[0], reverse=True)
    return entries[:limit]


def build_recent_lines(limit=5):
    baseurl = get_baseurl()
    lines = []
    for _, date_str, index_file in get_recent_logs(limit):
        title = get_front_matter_title(index_file)
        lines.append(f"- [{date_str} — {title}]({baseurl}/logs/{date_str}/)")
    return lines


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
    block = "\n".join([start, ""] + new_lines + ["", end])
    return pattern.sub(block, index_text)


def main():
    recent = build_recent_lines()
    if not recent:
        return
    index_text = INDEX_PATH.read_text(encoding="utf-8")
    updated = replace_recent_block(index_text, recent)
    if updated != index_text:
        INDEX_PATH.write_text(updated, encoding="utf-8")
        print("Updated Recent Devlog Entries in index.md")


if __name__ == "__main__":
    main()
