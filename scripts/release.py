#!/usr/bin/env python3
"""Prepare a deterministic YGit Schema release archive after quality checks."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {'.git', '.astro', 'dist', 'node_modules', 'release', '__pycache__'}
SEMVER_PATTERN = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')


def run(command: list[str]) -> None:
    print(f'$ {" ".join(command)}')
    subprocess.run(command, cwd=ROOT, check=True)


def is_git_clean() -> bool:
    result = subprocess.run(
        ['git', 'status', '--porcelain'],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return not result.stdout.strip()


def iter_release_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob('*')
        if path.is_file() and not any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)
    )


def create_archive(version: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f'ygit-schema-{version}.zip'
    source_date_epoch = int(os.environ.get('SOURCE_DATE_EPOCH', '315532800'))
    released_at = datetime.fromtimestamp(source_date_epoch, tz=timezone.utc)
    timestamp = (
        max(released_at.year, 1980),
        released_at.month,
        released_at.day,
        released_at.hour,
        released_at.minute,
        released_at.second,
    )
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in iter_release_files():
            relative = Path('ygit-schema') / path.relative_to(ROOT)
            info = zipfile.ZipInfo(relative.as_posix(), timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
            bundle.writestr(info, path.read_bytes())
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix('.zip.sha256').write_text(f'{checksum}  {archive.name}\n', encoding='utf-8')
    return archive


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True, help='Release version, for example 1.0.0.')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'release')
    parser.add_argument('--allow-dirty', action='store_true', help='Allow packaging a dirty worktree.')
    parser.add_argument('--skip-frontend', action='store_true', help='Skip npm checks when dependencies are unavailable.')
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if not SEMVER_PATTERN.fullmatch(args.version):
        print(f'ERROR: Invalid semantic version: {args.version}', file=sys.stderr)
        return 2
    if not args.allow_dirty and not is_git_clean():
        print('ERROR: Repository has uncommitted changes. Use --allow-dirty only for local verification.', file=sys.stderr)
        return 2

    try:
        run([sys.executable, 'scripts/audit.py'])
        run([sys.executable, 'scripts/validate.py', '--all'])
        run([sys.executable, '-m', 'unittest', 'discover', '-s', 'test', '-p', 'test_*.py'])
        if not args.skip_frontend:
            run(['npm', 'run', 'check'])
            run(['npm', 'run', 'build'])
        archive = create_archive(args.version, args.output_dir.resolve())
    except (OSError, subprocess.CalledProcessError) as error:
        print(f'ERROR: Release preparation failed: {error}', file=sys.stderr)
        return 1

    print(f'Release archive: {archive}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
