#!/usr/bin/env python3
"""Audit repository structure, text hygiene, references, and source imports."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {'.git', '.astro', 'dist', 'node_modules', 'release', '__pycache__'}
TEXT_SUFFIXES = {
    '.astro',
    '.css',
    '.html',
    '.js',
    '.json',
    '.md',
    '.mdx',
    '.mjs',
    '.py',
    '.svg',
    '.ts',
    '.tsx',
    '.txt',
    '.yaml',
    '.yml',
    '.ygit',
}
SOURCE_SUFFIXES = {'.astro', '.js', '.mjs', '.ts', '.tsx', '.mdx'}
IMPORT_PATTERN = re.compile(r"(?:from\s+|import\s*\()(['\"])([^'\"]+)\1")
PROHIBITED_MARKER_PATTERN = re.compile(r'\b(?:TO' + r'DO|FIX' + r'ME|X' + r'XX)\b')


def repository_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob('*')
        if path.is_file()
        and not any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)
    )


def text_files() -> list[Path]:
    return [path for path in repository_files() if path.suffix.lower() in TEXT_SUFFIXES]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def audit_format() -> list[str]:
    errors: list[str] = []
    for path in text_files():
        data = path.read_bytes()
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError as error:
            errors.append(f'{relative(path)}: not valid UTF-8 ({error})')
            continue
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
            json.loads(path.read_text(encoding='utf-8'))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            errors.append(f'{relative(path)}: invalid JSON ({error})')
    return errors


def audit_markdown() -> list[str]:
    errors: list[str] = []
    for path in repository_files():
        if path.suffix.lower() not in {'.md', '.mdx'}:
            continue
        fences = sum(
            1
            for line in path.read_text(encoding='utf-8').splitlines()
            if line.lstrip().startswith('```')
        )
        if fences % 2:
            errors.append(f'{relative(path)}: unbalanced fenced code blocks')
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
        for _, specifier in IMPORT_PATTERN.findall(path.read_text(encoding='utf-8')):
            if specifier.startswith('@/'):
                candidate = source_root / specifier[2:]
            elif specifier.startswith('.'):
                candidate = (path.parent / specifier.split('?', maxsplit=1)[0]).resolve()
            else:
                continue
            if not candidate_exists(candidate):
                errors.append(f'{relative(path)}: unresolved import {specifier!r}')
    return errors


def audit_components() -> list[str]:
    errors: list[str] = []
    components = ROOT / 'src/components'
    for path in sorted(components.rglob('*.astro')):
        line_count = len(path.read_text(encoding='utf-8').splitlines())
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
            for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
                if PROHIBITED_MARKER_PATTERN.search(line):
                    errors.append(f'{relative(path)}:{line_number}: unfinished marker')
    return errors


def audit_required_files() -> list[str]:
    required = [
        'README.md',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'LICENSE',
        'package.json',
        'requirements.txt',
        'astro.config.mjs',
        'tailwind.config.ts',
        'tsconfig.json',
        'v1/vibproject.schema.json',
        'examples/vibproject-full-example.ygit',
        'scripts/validate.py',
        'scripts/release.py',
        '.github/workflows/validate.yml',
        '.github/workflows/deploy.yml',
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
    checks = [('format', audit_format)]
    if not args.format_only:
        checks.extend(
            [
                ('required files', audit_required_files),
                ('JSON', audit_json),
                ('Markdown', audit_markdown),
                ('imports', audit_imports),
                ('components', audit_components),
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
        print(f'Audit failed with {len(errors)} issue(s).', file=sys.stderr)
        return 1
    print('Audit passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
