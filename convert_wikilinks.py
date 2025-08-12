import re
import sys
from pathlib import Path
from urllib.parse import quote
from typing import Dict, List

WikiTarget = str
RelPathStr = str


def build_note_indices(root: Path):
    """
    Build indices for resolving wiki links:
    - stem_to_paths: map from note stem (filename without extension) to list of relative paths (no extension)
    - all_paths: set of all relative paths (no extension) for explicit path matches
    - path_to_url: map from relative path (no extension) to site URL '/notes/.../File.html'
    """
    stem_to_paths: Dict[WikiTarget, List[Path]] = {}
    all_paths: Dict[RelPathStr, Path] = {}
    path_to_url: Dict[RelPathStr, str] = {}

    for md_file in root.rglob("*.md"):
        rel_no_ext = md_file.relative_to(root).with_suffix("")
        stem = md_file.stem
        stem_to_paths.setdefault(stem, []).append(rel_no_ext)
        all_paths[rel_no_ext.as_posix()] = rel_no_ext
        url = "/notes/" + quote(md_file.relative_to(root).with_suffix(".html").as_posix(), safe="/")
        path_to_url[rel_no_ext.as_posix()] = url

    return stem_to_paths, all_paths, path_to_url


def top_level_segment(rel_path: Path) -> str:
    parts = rel_path.parts
    return parts[0] if parts else ""


def path_distance(from_dir: Path, to_path_no_ext: Path) -> int:
    """Heuristic distance between directories for choosing the closest note."""
    try:
        rel = to_path_no_ext.parent.relative_to(from_dir)
        # Prefer notes deeper inside current subtree (shorter relative path without '..')
        score = len(rel.parts)
    except ValueError:
        # Different branches; compute rough distance via common prefix length
        from_parts = from_dir.parts
        to_parts = to_path_no_ext.parent.parts
        i = 0
        while i < min(len(from_parts), len(to_parts)) and from_parts[i] == to_parts[i]:
            i += 1
        # penalize number of steps up and down
        score = (len(from_parts) - i) + (len(to_parts) - i)
    return score


def resolve_target(current_file: Path, target: str, root: Path, stem_to_paths, all_paths) -> RelPathStr:
    # 1) Explicit path target (contains '/') – try exact match (no extension)
    if "/" in target:
        explicit = target.rstrip("/")
        # Try both exact case and with spaces preserved
        if explicit in all_paths:
            return explicit
        # Also try with spaces replaced by dashes (in case links were already normalized)
        dash_explicit = explicit.replace(" ", "-")
        if dash_explicit in all_paths:
            return dash_explicit
        # Fall through to stem resolution using last segment
        target = Path(target).name

    # 2) Resolve by stem, preferring same directory, then same top-level, then closest by distance
    candidates: List[Path] = stem_to_paths.get(target, [])
    if not candidates:
        return target.replace(" ", "-")  # fallback string; will likely 404 but better than empty

    current_rel_dir = current_file.parent.relative_to(root)
    top_current = top_level_segment(current_rel_dir)

    # Same directory
    same_dir = [p for p in candidates if p.parent == current_rel_dir]
    if same_dir:
        return same_dir[0].as_posix()

    # Same top-level folder
    same_top = [p for p in candidates if top_level_segment(p) == top_current]
    if same_top:
        # pick the closest by path distance
        best = min(same_top, key=lambda p: path_distance(current_rel_dir, p))
        return best.as_posix()

    # Global best by distance
    best_global = min(candidates, key=lambda p: path_distance(current_rel_dir, p))
    return best_global.as_posix()


def convert_links(text: str, current_file: Path, root: Path, stem_to_paths, all_paths, path_to_url) -> str:
    def url_for_rel_no_ext(rel_no_ext: RelPathStr) -> str:
        url = path_to_url.get(rel_no_ext)
        if not url:
            # fallback naive
            url = "/notes/" + quote(rel_no_ext + ".html")
        return url

    # [[Target|Text]] → - [Text]({{ '/notes/.../File.html' | relative_url }})
    def repl_wikilink_with_text(m):
        target, link_text = m.group(1), m.group(2)
        rel_no_ext = resolve_target(current_file, target, root, stem_to_paths, all_paths)
        url = url_for_rel_no_ext(rel_no_ext)
        return f"- [{link_text}]({{{{ '{url}' | relative_url }}}})"

    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", repl_wikilink_with_text, text)

    # [[Target]] → - [Target]({{ '/notes/.../File.html' | relative_url }})
    def repl_wikilink(m):
        target = m.group(1)
        rel_no_ext = resolve_target(current_file, target, root, stem_to_paths, all_paths)
        url = url_for_rel_no_ext(rel_no_ext)
        return f"- [{target}]({{{{ '{url}' | relative_url }}}})"

    text = re.sub(r"\[\[([^\]]+)\]\]", repl_wikilink, text)

    # Ensure each list item is on its own line
    text = re.sub(r"(?<!\n)- ", "\n- ", text)
    text = text.lstrip("\n")
    return text


def process_file(path: Path, root: Path, stem_to_paths, all_paths, path_to_url):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = convert_links(content, path, root, stem_to_paths, all_paths, path_to_url)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Converted: {path}")


if __name__ == "__main__":
    notes_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    stem_to_paths, all_paths, path_to_url = build_note_indices(notes_root)
    for md_file in notes_root.rglob("*.md"):
        process_file(md_file, notes_root, stem_to_paths, all_paths, path_to_url) 