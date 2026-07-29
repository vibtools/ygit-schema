#!/usr/bin/env python3
"""Run dependency-free forensic consistency checks across the repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {
  '.git',
  '.astro',
  'dist',
  'node_modules',
  'release',
  '__pycache__',
  '.venv',
  'venv',
  'project/update',
}
TEXT_SUFFIXES = {
  '.astro',
  '.cjs',
  '.css',
  '.html',
  '.ini',
  '.js',
  '.json',
  '.md',
  '.mdx',
  '.mjs',
  '.py',
  '.svg',
  '.toml',
  '.ts',
  '.tsx',
  '.txt',
  '.xml',
  '.yaml',
  '.ygit',
  '.yml',
}
TEXT_FILENAMES = {
  '.editorconfig',
  '.gitignore',
  '.nvmrc',
  '.prettierignore',
  'LICENSE',
  '_headers',
  '_redirects',
}
SOURCE_SUFFIXES = {'.astro', '.cjs', '.js', '.mjs', '.ts', '.tsx'}
IMPORT_PATTERN = re.compile(
  r"(?:from\s+|import\s*\()(['\"])([^'\"]+)\1|import\s+(['\"])([^'\"]+)\3",
)
MARKDOWN_LINK_PATTERN = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
PROHIBITED_MARKER_PATTERN = re.compile(r'\b(?:TODO|FIXME|HACK|XXX)\b', re.IGNORECASE)
SECRET_PATTERN = re.compile(
  r'(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|'
  r'AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|'
  r'(?i:(?:api[_-]?key|secret|token|password)\s*[:=]\s*["\'][^"\']{8,}["\']))',
)


def relative(path: Path) -> str:
  return path.relative_to(ROOT).as_posix()


def is_excluded(path: Path) -> bool:
  rel = path.relative_to(ROOT)
  rel_text = rel.as_posix()
  return any(part in EXCLUDED_PARTS for part in rel.parts) or rel_text.startswith('project/update/')


def repository_files() -> list[Path]:
  return sorted(path for path in ROOT.rglob('*') if path.is_file() and not is_excluded(path))


def text_files() -> list[Path]:
  return [
    path
    for path in repository_files()
    if path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_FILENAMES
  ]


def read_text(path: Path) -> str:
  return path.read_text(encoding='utf-8')


def audit_format() -> list[str]:
  errors: list[str] = []
  for path in text_files():
    data = path.read_bytes()
    try:
      text = data.decode('utf-8')
    except UnicodeDecodeError as error:
      errors.append(f'{relative(path)}: invalid UTF-8 ({error})')
      continue
    if data.startswith(b'\xef\xbb\xbf'):
      errors.append(f'{relative(path)}: contains UTF-8 BOM')
    if b'\r' in data:
      errors.append(f'{relative(path)}: contains CR/CRLF line endings')
    if text and not text.endswith('\n'):
      errors.append(f'{relative(path)}: missing final newline')
    for line_number, line in enumerate(text.splitlines(), start=1):
      if line.rstrip(' \t') != line:
        errors.append(f'{relative(path)}:{line_number}: trailing whitespace')
        break
  return errors


def audit_json() -> list[str]:
  errors: list[str] = []
  for path in repository_files():
    if path.suffix.lower() not in {'.json', '.ygit'}:
      continue
    try:
      json.loads(read_text(path))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
      errors.append(f'{relative(path)}: invalid JSON ({error})')
  return errors


def _markdown_without_fences(text: str) -> str:
  output: list[str] = []
  fenced = False
  for line in text.splitlines():
    if line.lstrip().startswith('```'):
      fenced = not fenced
      continue
    if not fenced:
      output.append(line)
  return '\n'.join(output)


def _link_target(raw: str) -> str:
  raw = raw.strip()
  if raw.startswith('<') and '>' in raw:
    return raw[1:raw.index('>')]
  if ' "' in raw:
    raw = raw.split(' "', maxsplit=1)[0]
  if " '" in raw:
    raw = raw.split(" '", maxsplit=1)[0]
  return raw.strip()


def _relative_link_exists(document: Path, target: str) -> bool:
  parsed = urlsplit(target)
  if parsed.scheme or parsed.netloc or target.startswith(('#', '/', 'mailto:', 'tel:')):
    return True
  path_text = unquote(parsed.path)
  if not path_text:
    return True
  candidate = (document.parent / path_text).resolve()
  try:
    candidate.relative_to(ROOT)
  except ValueError:
    return False
  if candidate.exists():
    return True
  if candidate.suffix == '':
    return candidate.with_suffix('.md').exists() or candidate.with_suffix('.mdx').exists()
  return False


def audit_markdown() -> list[str]:
  errors: list[str] = []
  for path in repository_files():
    if path.suffix.lower() not in {'.md', '.mdx'}:
      continue
    text = read_text(path)
    fences = sum(1 for line in text.splitlines() if line.lstrip().startswith('```'))
    if fences % 2:
      errors.append(f'{relative(path)}: unbalanced fenced code blocks')
      continue
    for match in MARKDOWN_LINK_PATTERN.finditer(_markdown_without_fences(text)):
      target = _link_target(match.group(1))
      if not _relative_link_exists(path, target):
        errors.append(f'{relative(path)}: broken relative link {target!r}')
  return errors


def candidate_exists(base: Path) -> bool:
  suffixes = ('', '.ts', '.tsx', '.js', '.mjs', '.astro', '.md', '.mdx', '.json')
  return any(Path(f'{base}{suffix}').exists() for suffix in suffixes) or any(
    (base / f'index{suffix}').exists() for suffix in suffixes[1:]
  )


def audit_imports() -> list[str]:
  errors: list[str] = []
  source_root = ROOT / 'src'
  for path in sorted(source_root.rglob('*')):
    if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
      continue
    text = read_text(path)
    for match in IMPORT_PATTERN.finditer(text):
      specifier = match.group(2) or match.group(4)
      if specifier.startswith('@/'):
        candidate = source_root / specifier[2:]
      elif specifier.startswith('.'):
        candidate = (path.parent / specifier.split('?', maxsplit=1)[0]).resolve()
      else:
        continue
      if not candidate_exists(candidate):
        errors.append(f'{relative(path)}: unresolved import {specifier!r}')
    if re.search(r"import\s*\{[^}]*\bGithub\b[^}]*\}\s*from\s*['\"]@lucide/astro['\"]", text):
      errors.append(f'{relative(path)}: unsupported Lucide brand icon import Github')
  return errors


def audit_components() -> list[str]:
  errors: list[str] = []
  components = ROOT / 'src/components'
  for path in sorted(components.rglob('*.astro')):
    line_count = len(read_text(path).splitlines())
    if line_count > 250:
      errors.append(f'{relative(path)}: component exceeds 250 lines ({line_count})')
    if not (path.parent / 'index.ts').exists():
      errors.append(f'{relative(path.parent)}: missing component index.ts')
  return errors


def audit_placeholders() -> list[str]:
  errors: list[str] = []
  implementation_roots = [ROOT / 'src', ROOT / 'scripts', ROOT / 'test', ROOT / '.github/workflows']
  for directory in implementation_roots:
    for path in sorted(directory.rglob('*')):
      if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
        continue
      if path.resolve() == Path(__file__).resolve():
        continue
      for line_number, line in enumerate(read_text(path).splitlines(), start=1):
        if PROHIBITED_MARKER_PATTERN.search(line):
          errors.append(f'{relative(path)}:{line_number}: unfinished marker')
  return errors


def audit_security() -> list[str]:
  errors: list[str] = []
  for path in text_files():
    text = read_text(path)
    if path.resolve() == Path(__file__).resolve():
      continue
    if SECRET_PATTERN.search(text):
      errors.append(f'{relative(path)}: possible embedded secret')
    if '<<<<<<< ' in text or '\n=======' in text or '\n>>>>>>> ' in text:
      errors.append(f'{relative(path)}: unresolved merge-conflict marker')
  return errors


def audit_paths() -> list[str]:
  errors: list[str] = []
  seen: dict[str, str] = {}
  for path in repository_files():
    rel = relative(path)
    folded = rel.casefold()
    if folded in seen and seen[folded] != rel:
      errors.append(f'{rel}: case-insensitive path collision with {seen[folded]}')
    seen[folded] = rel
    if path.is_symlink():
      errors.append(f'{rel}: symbolic links are not permitted in release sources')
  return errors


def audit_public_sync() -> list[str]:
  pairs = [
    ('v1/vibproject.schema.json', 'public/vpms/v1/vibproject.schema.json'),
    ('examples/vibproject-full-example.ygit', 'public/examples/vibproject-full-example.ygit'),
    ('LICENSE', 'public/LICENSE'),
    ('assets/logo/logo-dark.png', 'public/logo-dark.png'),
    ('assets/logo/logo-light.png', 'public/logo-light.png'),
    ('assets/icon/favicon.svg', 'public/favicon.svg'),
    ('assets/icon/favicon-96x96.png', 'public/favicon-96x96.png'),
    ('assets/icon/apple-touch-icon.png', 'public/apple-touch-icon.png'),
    ('assets/icon/web-app-manifest-192x192.png', 'public/web-app-manifest-192x192.png'),
    ('assets/icon/web-app-manifest-512x512.png', 'public/web-app-manifest-512x512.png'),
  ]
  errors: list[str] = []
  for source_name, public_name in pairs:
    source = ROOT / source_name
    public = ROOT / public_name
    if not source.is_file() or not public.is_file():
      continue
    if hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(public.read_bytes()).digest():
      errors.append(f'{public_name}: differs from source {source_name}')
  return errors


def audit_configuration() -> list[str]:
  errors: list[str] = []
  try:
    package = json.loads(read_text(ROOT / 'package.json'))
  except (OSError, json.JSONDecodeError):
    return errors
  scripts = package.get('scripts', {})
  required_scripts = {'build', 'check', 'format', 'format:check', 'validate', 'test', 'audit', 'quality'}
  for name in sorted(required_scripts - set(scripts)):
    errors.append(f'package.json: missing required script {name!r}')
  nvm = read_text(ROOT / '.nvmrc').strip()
  node_engine = package.get('engines', {}).get('node', '')
  if nvm and nvm not in node_engine:
    errors.append(f'.nvmrc: Node {nvm} is not represented by package.json engine {node_engine!r}')
  package_manager = package.get('packageManager', '')
  if not package_manager.startswith('npm@'):
    errors.append('package.json: packageManager must pin npm')
  compatibility = read_text(ROOT / 'compatibility/compatibility.yaml')
  for expected in (node_engine, package.get('engines', {}).get('npm', ''), package.get('version', '')):
    if expected and expected not in compatibility:
      errors.append(f'compatibility/compatibility.yaml: missing package value {expected!r}')
  for workflow in (ROOT / '.github/workflows').glob('*.yml'):
    text = read_text(workflow)
    if 'actions/checkout@v4' in text or 'actions/setup-node@v4' in text or 'actions/setup-python@v5' in text or 'actions/upload-artifact@v4' in text:
      errors.append(f'{relative(workflow)}: contains deprecated Node 20 GitHub Action major')
  return errors


def audit_manifests() -> list[str]:
  errors: list[str] = []
  manifest_path = ROOT / 'vibproject.ygit'
  schema_path = ROOT / 'v1/vibproject.schema.json'
  if not manifest_path.is_file() or not schema_path.is_file():
    return errors
  manifest = json.loads(read_text(manifest_path))
  schema = json.loads(read_text(schema_path))
  allowed = set(schema.get('properties', {}))
  unknown = set(manifest) - allowed
  if unknown:
    errors.append(f'vibproject.ygit: unsupported root properties {sorted(unknown)}')
  for required in schema.get('required', []):
    if required not in manifest:
      errors.append(f'vibproject.ygit: missing required root property {required!r}')
  paths = manifest.get('paths', {})
  if isinstance(paths, dict):
    for key, value in paths.items():
      if isinstance(value, str) and not (ROOT / value).exists():
        errors.append(f'vibproject.ygit: paths.{key} references missing path {value!r}')
  entrypoints = manifest.get('entrypoints', {})
  if isinstance(entrypoints, dict):
    for key, value in entrypoints.items():
      if isinstance(value, str) and not (ROOT / value).exists():
        errors.append(f'vibproject.ygit: entrypoints.{key} references missing path {value!r}')
  return errors


def audit_required_files() -> list[str]:
  required = [
    '.editorconfig',
    '.gitattributes',
    '.gitignore',
    '.github/CODEOWNERS',
    '.github/dependabot.yml',
    '.github/ISSUE_TEMPLATE/bug_report.yml',
    '.github/ISSUE_TEMPLATE/feature_request.yml',
    '.github/ISSUE_TEMPLATE/config.yml',
    '.github/pull_request_template.md',
    '.github/workflows/deploy.yml',
    '.github/workflows/release.yml',
    '.github/workflows/validate.yml',
    'CHANGELOG.md',
    'CODE_OF_CONDUCT.md',
    'CONTRIBUTING.md',
    'FORENSIC_AUDIT_REPORT.md',
    'LICENSE',
    'README.md',
    'SECURITY.md',
    'SUPPORT.md',
    'astro.config.mjs',
    'compatibility/compatibility.yaml',
    'examples/vibproject-full-example.ygit',
    'package.json',
    'public/.well-known/security.txt',
    'requirements.txt',
    'scripts/audit.py',
    'scripts/release.py',
    'scripts/sourcegenerate.py',
    'scripts/validate.py',
    'tailwind.config.ts',
    'test/test_validation.py',
    'tsconfig.json',
    'v1/vibproject.schema.json',
    'v2/README.md',
    'vibproject.ygit',
  ]
  return [f'{path}: required file is missing' for path in required if not (ROOT / path).is_file()]


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    '--format-only',
    action='store_true',
    help='Check UTF-8, LF line endings, final newlines, and trailing whitespace only.',
  )
  return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
  args = parse_args(argv)
  checks: list[tuple[str, Callable[[], list[str]]]] = [('format', audit_format)]
  if not args.format_only:
    checks.extend(
      [
        ('required files', audit_required_files),
        ('paths', audit_paths),
        ('JSON', audit_json),
        ('Markdown', audit_markdown),
        ('imports', audit_imports),
        ('components', audit_components),
        ('configuration', audit_configuration),
        ('manifests', audit_manifests),
        ('published copies', audit_public_sync),
        ('security', audit_security),
        ('unfinished markers', audit_placeholders),
      ]
    )

  errors: list[str] = []
  for label, check in checks:
    findings = check()
    if findings:
      print(f'[FAIL] {label}')
      for finding in findings:
        print(f'  - {finding}')
      errors.extend(findings)
    else:
      print(f'[PASS] {label}')

  if errors:
    counts = Counter(error.split(':', maxsplit=1)[0] for error in errors)
    print(f'Audit failed with {len(errors)} issue(s) across {len(counts)} path(s).', file=sys.stderr)
    return 1
  print('Audit passed.')
  return 0


if __name__ == '__main__':
  raise SystemExit(main())
