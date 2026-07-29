#!/usr/bin/env python3
"""
Generate a complete source ZIP of the repository.

Policy
------
Included:
    ✓ Everything in the repository

Excluded:
    ✗ .git/
    ✗ project/update/
    ✗ Generated *.zip
    ✗ Generated *.sha256

Features
--------
- Complete source snapshot
- Preserves folder structure
- Preserves empty directories
- SHA256 checksum generation
- Compression Level 9
- --dry-run
- --verbose
- Statistics
- Cross-platform
"""

from __future__ import annotations

import argparse
import hashlib
import time
from datetime import datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

PROJECT_ROOT = Path(__file__).resolve().parent.parent

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

zip_name = f"{PROJECT_ROOT.name}-source-{timestamp}.zip"
zip_path = PROJECT_ROOT / zip_name
sha_path = zip_path.with_suffix(".zip.sha256")

EXCLUDED = [
    Path(".git"),
    Path("project/update"),
]


def is_excluded(path: Path) -> bool:
    rel = path.relative_to(PROJECT_ROOT)

    for excluded in EXCLUDED:
        if rel == excluded or excluded in rel.parents:
            return True

    if path == zip_path:
        return True

    if path == sha_path:
        return True

    if path.suffix.lower() == ".zip":
        return True

    if path.suffix.lower() == ".sha256":
        return True

    return False


def sha256(file: Path) -> str:
    h = hashlib.sha256()

    with file.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)

    return h.hexdigest()


def collect_items():

    files = []
    empty_dirs = []

    for item in PROJECT_ROOT.rglob("*"):

        if is_excluded(item):
            continue

        if item.is_dir():

            try:
                next(item.iterdir())
            except StopIteration:
                empty_dirs.append(item)

        elif item.is_file():
            files.append(item)

    return files, empty_dirs


def create_zip(files, empty_dirs, verbose=False):

    with ZipFile(
        zip_path,
        "w",
        compression=ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:

        for d in empty_dirs:

            rel = d.relative_to(PROJECT_ROOT).as_posix() + "/"

            archive.writestr(rel, "")

            if verbose:
                print(f"[DIR ] {rel}")

        for f in files:

            rel = f.relative_to(PROJECT_ROOT)

            archive.write(f, rel)

            if verbose:
                print(f"[FILE] {rel}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show files without creating ZIP",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print every file",
    )

    args = parser.parse_args()

    start = time.perf_counter()

    files, empty_dirs = collect_items()

    if args.dry_run:

        print("\nDirectories")
        print("-" * 60)

        for d in empty_dirs:
            print(d.relative_to(PROJECT_ROOT))

        print("\nFiles")
        print("-" * 60)

        for f in files:
            print(f.relative_to(PROJECT_ROOT))

        print("\nSummary")
        print("-" * 60)
        print(f"Directories : {len(empty_dirs)}")
        print(f"Files       : {len(files)}")

        return

    if zip_path.exists():
        zip_path.unlink()

    if sha_path.exists():
        sha_path.unlink()

    create_zip(files, empty_dirs, args.verbose)

    digest = sha256(zip_path)

    sha_path.write_text(
        f"{digest}  {zip_path.name}\n",
        encoding="utf-8",
    )

    elapsed = time.perf_counter() - start

    size = zip_path.stat().st_size / (1024 * 1024)

    print("=" * 70)
    print("Source package created successfully")
    print("=" * 70)
    print(f"Project      : {PROJECT_ROOT.name}")
    print(f"Directories  : {len(empty_dirs)}")
    print(f"Files        : {len(files)}")
    print(f"ZIP          : {zip_path.name}")
    print(f"SHA256       : {sha_path.name}")
    print(f"Size         : {size:.2f} MB")
    print(f"Time         : {elapsed:.2f} sec")
    print("=" * 70)


if __name__ == "__main__":
    main()