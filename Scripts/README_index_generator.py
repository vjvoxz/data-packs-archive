#!/usr/bin/env python3
"""
README Index Generator

Creates (or updates) a README file section named "Index" based on your
project's files/folders.

Usage:
  1) Put this script in your project root (or run it from there).
  2) Install nothing (uses only stdlib).
  3) Run:
       python readme_index.py --root .
       python readme_index.py --root . --output README.md --title "My Project"
"""

import argparse
import os
from pathlib import Path
from datetime import datetime


DEFAULT_EXCLUDES = {
    ".git", ".github", ".gitlab", ".svn", "__pycache__",
    "node_modules", "dist", "build", ".venv", "venv", ".mypy_cache",
    ".pytest_cache", ".idea", ".vscode",
}


def should_exclude(rel_path: Path, exclude_names: set[str]) -> bool:
    parts = rel_path.parts
    return any(p in exclude_names for p in parts)


def collect_tree(root: Path, exclude_names: set[str], max_depth: int) -> list[tuple[str, str]]:
    """
    Returns list of (type, relative_path) where type is "dir" or "file".
    Only includes items up to max_depth (files and dirs).
    """
    items: list[tuple[str, str]] = []
    root = root.resolve()

    for dirpath, dirnames, filenames in os.walk(root):
        dirpath_p = Path(dirpath)
        rel_dir = dirpath_p.relative_to(root)

        # Depth pruning
        depth = len(rel_dir.parts) if rel_dir.parts else 0
        if depth > max_depth:
            dirnames[:] = []
            continue

        # Exclude directories in-place
        dirnames[:] = [
            d for d in dirnames
            if d not in exclude_names and not should_exclude((rel_dir / d), exclude_names)
        ]

        # Add directories (excluding root itself)
        if rel_dir.parts:
            items.append(("dir", str(rel_dir).replace("\\", "/")))

        # Add files
        for fn in sorted(filenames):
            file_path = rel_dir / fn
            if should_exclude(file_path, exclude_names):
                continue
            # If we're at max_depth, include files only (no more descent already handled)
            items.append(("file", str(file_path).replace("\\", "/")))

    return items


def make_markdown_index(lines: list[str], title: str | None = None) -> str:
    header = "## Index"
    if title:
        header = f"## {title}"

    content = [header, ""]
    # Simple grouped buckets
    buckets = []
    # If you want different grouping logic later, modify here.
    # Current logic: by top-level folder (or "root" if none).
    for line in lines:
        content.append(line)
    content.append("")
    return "\n".join(content)


def build_index_bullets(root: Path, items: list[tuple[str, str]], include_globs: list[str], exclude_globs: list[str]) -> list[str]:
    """
    Creates markdown bullets like:
      - [src/](#src)  (dir)
      - [README.md](#readme-md) (file)

    Note: Anchor generation here is "best-effort" and works for most GitHub cases.
    """
    def matches_globs(path: str, globs: list[str]) -> bool:
        # Very small glob matcher: supports '*' wildcard only (no full fnmatch complexity).
        # For more control, replace this with fnmatch.fnmatch.
        import re
        for g in globs:
            g2 = re.escape(g).replace(r"\*", ".*")
            if re.fullmatch(g2, path):
                return True
        return False

    # Filter items
    filtered: list[tuple[str, str]] = []
    for typ, rel in items:
        if include_globs:
            if not matches_globs(rel, include_globs):
                continue
        if exclude_globs:
            if matches_globs(rel, exclude_globs):
                continue
        filtered.append((typ, rel))

    # Determine "top-level grouping"
    groups: dict[str, list[tuple[str, str]]] = {}
    for typ, rel in filtered:
        parts = rel.split("/")
        top = parts[0] if len(parts) > 1 else "root"
        groups.setdefault(top, []).append((typ, rel))

    # Sort and format
    def github_anchor_from_path(rel: str) -> str:
        # Convert "a/b-c" -> "a-b-c" roughly
        # GitHub anchors for headings differ; but for README links, we often link to headings.
        # Here we're linking just to file paths for convenience (works only if you use GitHub file links).
        # We'll use "blob" links instead, so anchor isn't needed.
        return rel

    # GitHub-friendly links: use relative links to files in repo.
    def github_blob_link(rel: str) -> str:
        # Relative link inside README typically works on GitHub:
        # [path](path)
        return f"{rel}"

    out: list[str] = []
    # stable order of groups
    for top in sorted(groups.keys()):
        out.append(f"- **{top}/**")
        group_items = sorted(groups[top], key=lambda x: (x[0] != "dir", x[1]))  # dirs first-ish
        for typ, rel in group_items:
            display = rel
            # Indent file entries under the group
            if typ == "dir":
                out.append(f"  - `{display}/`")
            else:
                out.append(f"  - [`{display}`]({github_blob_link(display)})")
        out.append("")  # blank line between groups

    if not out:
        out.append("- (No files found)")
    # remove trailing blank line for neatness
    if out and out[-1] == "":
        out.pop()
    return out


def update_readme(readme_path: Path, index_block: str, marker_start: str, marker_end: str) -> None:
    """
    Replace content between markers, or append if markers not found.
    """
    content = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

    start_tag = f"<!-- {marker_start} -->"
    end_tag = f"<!-- {marker_end} -->"

    if start_tag in content and end_tag in content and content.index(start_tag) < content.index(end_tag):
        before = content.split(start_tag)[0]
        after = content.split(end_tag)[1]
        new_content = before + start_tag + "\n" + index_block + "\n" + end_tag + after
    else:
        # Append at end with markers
        new_content = content.rstrip() + "\n\n" + start_tag + "\n" + index_block + "\n" + end_tag + "\n"

    readme_path.write_text(new_content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--output", default="README.md", help="README file to update/create")
    parser.add_argument("--title", default=None, help='Heading text for the index (default: "## Index")')
    parser.add_argument("--max-depth", type=int, default=4, help="Max directory depth to scan")
    parser.add_argument("--exclude", action="append", default=[], help="Extra names to exclude (repeatable)")
    parser.add_argument("--include", action="append", default=[], help="Include globs like '*.py' (optional)")
    parser.add_argument("--exclude-glob", action="append", default=[], help="Exclude globs like 'package-lock.json' (optional)")
    parser.add_argument("--marker-start", default="README_INDEX_START", help="Marker name start (HTML comment)")
    parser.add_argument("--marker-end", default="README_INDEX_END", help="Marker name end (HTML comment)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    readme_path = (root / args.output).resolve()

    excludes = set(DEFAULT_EXCLUDES)
    excludes.update(args.exclude)

    items = collect_tree(root, excludes, max_depth=args.max_depth)
    bullets = build_index_bullets(root, items, include_globs=args.include, exclude_globs=args.exclude_glob)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    index_block = make_markdown_index(
        lines=bullets,
        title=args.title if args.title else None
    )
    # Add small timestamp line inside marker region
    index_block = f"<!-- Generated: {timestamp} -->\n" + index_block

    update_readme(readme_path, index_block, args.marker_start, args.marker_end)
    print(f"Updated: {readme_path}")


if __name__ == "__main__":
    main()
