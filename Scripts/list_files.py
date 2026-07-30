from pathlib import Path

def list_files_to_markdown(folder_path: str, output_md: str = "file_list.md"):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Not a folder: {folder_path}")

    # Collect relative paths for nicer output
    files = sorted(
        p.relative_to(folder).as_posix()
        for p in folder.rglob("*")
        if p.is_file()
    )

    lines = []
    lines.append(f"# File list: {folder.as_posix()}")
    lines.append("")
    if files:
        for name in files:
            lines.append(f"- {name}")
    else:
        lines.append("_No files found._")
    lines.append("")

    Path(output_md).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(files)} file(s) to {output_md}")

if __name__ == "__main__":
    # Change these paths as needed
    list_files_to_markdown(r"your_folder_path_here", "file_list.md")