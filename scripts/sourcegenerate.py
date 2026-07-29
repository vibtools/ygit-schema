#!/usr/bin/env python3
"""Generate a complete, deterministic source ZIP and SHA-256 checksum."""

from __future__ import annotations

import argparse
import hashlib
import os
import stat
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = {
  '.git',
  '.astro',
  '.venv',
  'dist',
  'node_modules',
  'project/update',
  'release',
  'venv',
  '__pycache__',
}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.zip', '.sha256'}


def relative(path: Path) -> Path:
  return path.relative_to(PROJECT_ROOT)


def is_excluded(path: Path, output_zip: Path, checksum_path: Path) -> bool:
  resolved = path.resolve()
  if resolved in {output_zip.resolve(), checksum_path.resolve()}:
    return True
  rel = relative(path)
  rel_text = rel.as_posix()
  if any(part in EXCLUDED_DIRECTORIES for part in rel.parts):
    return True
  if rel_text.startswith('project/update/'):
    return True
  return path.suffix.lower() in EXCLUDED_SUFFIXES


def sha256(path: Path) -> str:
  digest = hashlib.sha256()
  with path.open('rb') as stream:
    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
      digest.update(chunk)
  return digest.hexdigest()


def collect_items(output_zip: Path, checksum_path: Path) -> tuple[list[Path], list[Path]]:
  files: list[Path] = []
  empty_directories: list[Path] = []
  for item in sorted(PROJECT_ROOT.rglob('*'), key=lambda path: relative(path).as_posix()):
    if is_excluded(item, output_zip, checksum_path):
      continue
    if item.is_symlink():
      raise RuntimeError(f'Symbolic links are not supported in source packages: {relative(item)}')
    if item.is_dir():
      children = [child for child in item.iterdir() if not is_excluded(child, output_zip, checksum_path)]
      if not children:
        empty_directories.append(item)
    elif item.is_file():
      files.append(item)
  return files, empty_directories


def zip_timestamp() -> tuple[int, int, int, int, int, int]:
  epoch = int(os.environ.get('SOURCE_DATE_EPOCH', '315532800'))
  value = datetime.fromtimestamp(epoch, tz=timezone.utc)
  return (max(value.year, 1980), value.month, value.day, value.hour, value.minute, value.second)


def write_directory(archive: zipfile.ZipFile, path: Path, timestamp: tuple[int, ...]) -> None:
  info = zipfile.ZipInfo(relative(path).as_posix().rstrip('/') + '/', timestamp)
  info.external_attr = (stat.S_IFDIR | 0o755) << 16
  archive.writestr(info, b'')


def write_file(archive: zipfile.ZipFile, path: Path, timestamp: tuple[int, ...]) -> None:
  info = zipfile.ZipInfo(relative(path).as_posix(), timestamp)
  info.compress_type = zipfile.ZIP_DEFLATED
  mode = 0o755 if os.access(path, os.X_OK) else 0o644
  info.external_attr = (stat.S_IFREG | mode) << 16
  archive.writestr(info, path.read_bytes())


def create_zip(output_zip: Path, files: list[Path], empty_directories: list[Path], verbose: bool) -> None:
  output_zip.parent.mkdir(parents=True, exist_ok=True)
  timestamp = zip_timestamp()
  with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for directory in empty_directories:
      write_directory(archive, directory, timestamp)
      if verbose:
        print(f'[DIR ] {relative(directory).as_posix()}/')
    for path in files:
      write_file(archive, path, timestamp)
      if verbose:
        print(f'[FILE] {relative(path).as_posix()}')


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
  timestamp = datetime.now(tz=timezone.utc).strftime('%Y%m%d-%H%M%S')
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('--dry-run', action='store_true', help='List package contents without writing files.')
  parser.add_argument('--verbose', action='store_true', help='Print every packaged path.')
  parser.add_argument(
    '--output',
    type=Path,
    default=PROJECT_ROOT / f'{PROJECT_ROOT.name}-source-{timestamp}.zip',
    help='Destination ZIP path.',
  )
  return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
  args = parse_args(argv)
  output_zip = args.output.resolve()
  checksum_path = output_zip.with_suffix('.zip.sha256')
  start = time.perf_counter()
  try:
    files, empty_directories = collect_items(output_zip, checksum_path)
    if args.dry_run:
      for directory in empty_directories:
        print(f'[DIR ] {relative(directory).as_posix()}/')
      for path in files:
        print(f'[FILE] {relative(path).as_posix()}')
      print(f'Directories: {len(empty_directories)}')
      print(f'Files: {len(files)}')
      return 0
    output_zip.unlink(missing_ok=True)
    checksum_path.unlink(missing_ok=True)
    create_zip(output_zip, files, empty_directories, args.verbose)
    digest = sha256(output_zip)
    checksum_path.write_text(f'{digest}  {output_zip.name}\n', encoding='utf-8', newline='\n')
  except (OSError, RuntimeError, zipfile.BadZipFile, ValueError) as error:
    print(f'ERROR: Source package generation failed: {error}')
    return 1

  elapsed = time.perf_counter() - start
  print(f'Source ZIP: {output_zip}')
  print(f'SHA-256: {checksum_path}')
  print(f'Files: {len(files)}; empty directories: {len(empty_directories)}; elapsed: {elapsed:.2f}s')
  return 0


if __name__ == '__main__':
  raise SystemExit(main())
