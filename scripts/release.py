#!/usr/bin/env python3
"""Prepare a deterministic YGit Schema release archive after mandatory quality checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {'.git', '.astro', 'dist', 'node_modules', 'release', '__pycache__', '.venv', 'venv'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.zip', '.sha256'}
SEMVER_PATTERN = re.compile(r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$')


def run(command: list[str]) -> None:
  print(f'$ {" ".join(command)}')
  subprocess.run(command, cwd=ROOT, check=True)


def git_worktree_state() -> bool | None:
  git = shutil.which('git')
  if git is None:
    return None
  probe = subprocess.run(
    [git, 'rev-parse', '--is-inside-work-tree'],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=False,
  )
  if probe.returncode != 0 or probe.stdout.strip() != 'true':
    return None
  status_result = subprocess.run(
    [git, 'status', '--porcelain'],
    cwd=ROOT,
    capture_output=True,
    text=True,
    check=True,
  )
  return not status_result.stdout.strip()


def npm_executable() -> str:
  executable = shutil.which('npm')
  if executable is None:
    raise RuntimeError('npm is required for frontend release verification.')
  return executable


def verify_release_version(version: str) -> None:
  package = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))
  manifest = json.loads((ROOT / 'vibproject.ygit').read_text(encoding='utf-8'))
  package_version = package.get('version')
  project_version = manifest.get('project', {}).get('version')
  latest_version = manifest.get('release', {}).get('latestVersion')
  mismatches = [
    f'package.json={package_version}' if package_version != version else '',
    f'vibproject.ygit project.version={project_version}' if project_version != version else '',
    f'vibproject.ygit release.latestVersion={latest_version}' if latest_version != version else '',
  ]
  mismatches = [item for item in mismatches if item]
  if mismatches:
    raise RuntimeError(f'Release version {version} does not match: {", ".join(mismatches)}')


def iter_release_files() -> list[Path]:
  files: list[Path] = []
  for path in ROOT.rglob('*'):
    if not path.is_file() or path.is_symlink():
      continue
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
      continue
    if rel.as_posix().startswith('project/update/') or path.suffix.lower() in EXCLUDED_SUFFIXES:
      continue
    files.append(path)
  return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def create_archive(version: str, output_dir: Path) -> Path:
  output_dir.mkdir(parents=True, exist_ok=True)
  archive = output_dir / f'ygit-schema-{version}.zip'
  archive.unlink(missing_ok=True)
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
      mode = 0o755 if os.access(path, os.X_OK) else 0o644
      info.external_attr = (stat.S_IFREG | mode) << 16
      bundle.writestr(info, path.read_bytes())
  checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
  archive.with_suffix('.zip.sha256').write_text(f'{checksum}  {archive.name}\n', encoding='utf-8', newline='\n')
  return archive


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('--version', required=True, help='Release version, for example 1.0.0.')
  parser.add_argument('--output-dir', type=Path, default=ROOT / 'release')
  parser.add_argument('--allow-dirty', action='store_true', help='Allow packaging a dirty Git worktree.')
  parser.add_argument('--skip-frontend', action='store_true', help='Skip npm checks only for constrained local verification.')
  return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
  args = parse_args(argv)
  if not SEMVER_PATTERN.fullmatch(args.version):
    print(f'ERROR: Invalid semantic version: {args.version}', file=sys.stderr)
    return 2

  state = git_worktree_state()
  if state is False and not args.allow_dirty:
    print('ERROR: Repository has uncommitted changes. Use --allow-dirty only for local verification.', file=sys.stderr)
    return 2
  if state is None:
    print('NOTICE: No Git worktree detected; cleanliness verification is not applicable to this source snapshot.')

  try:
    verify_release_version(args.version)
    run([sys.executable, 'scripts/audit.py'])
    run([sys.executable, 'scripts/validate.py', '--all'])
    run([sys.executable, '-m', 'unittest', 'discover', '-s', 'test', '-p', 'test_*.py'])
    if not args.skip_frontend:
      npm = npm_executable()
      run([npm, 'run', 'format:check'])
      run([npm, 'run', 'check'])
      run([npm, 'run', 'build'])
    archive = create_archive(args.version, args.output_dir.resolve())
  except (OSError, RuntimeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
    print(f'ERROR: Release preparation failed: {error}', file=sys.stderr)
    return 1

  print(f'Release archive: {archive}')
  return 0


if __name__ == '__main__':
  raise SystemExit(main())
