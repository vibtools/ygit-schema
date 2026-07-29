#!/usr/bin/env python3
"""Validate YGit manifests and the complete repository validation suite."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / 'v1' / 'vibproject.schema.json'
ROOT_MANIFEST = ROOT / 'vibproject.ygit'


@dataclass(frozen=True)
class ValidationResult:
  path: Path
  is_valid: bool
  errors: tuple[str, ...]


def load_json(path: Path) -> Any:
  try:
    return json.loads(path.read_text(encoding='utf-8'))
  except FileNotFoundError as error:
    raise RuntimeError(f'File not found: {path}') from error
  except UnicodeDecodeError as error:
    raise RuntimeError(f'File is not UTF-8: {path}') from error
  except json.JSONDecodeError as error:
    location = f'line {error.lineno}, column {error.colno}'
    raise RuntimeError(f'Invalid JSON in {path}: {error.msg} ({location})') from error


def format_error(error: ValidationError) -> str:
  location = '.'.join(str(part) for part in error.absolute_path) or '<root>'
  return f'{location}: {error.message}'


def create_validator(schema_path: Path) -> Draft202012Validator:
  schema = load_json(schema_path)
  try:
    Draft202012Validator.check_schema(schema)
  except SchemaError as error:
    raise RuntimeError(f'Invalid JSON Schema: {error.message}') from error
  return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_file(path: Path, validator: Draft202012Validator) -> ValidationResult:
  try:
    manifest = load_json(path)
  except RuntimeError as error:
    return ValidationResult(path=path, is_valid=False, errors=(str(error),))

  errors = tuple(
    format_error(error)
    for error in sorted(
      validator.iter_errors(manifest),
      key=lambda item: (list(item.absolute_path), item.message),
    )
  )
  return ValidationResult(path=path, is_valid=not errors, errors=errors)


def discover_files(directory: Path) -> list[Path]:
  if not directory.exists():
    return []
  return sorted(path for path in directory.rglob('*.ygit') if path.is_file())


def display_path(path: Path) -> str:
  try:
    return path.relative_to(ROOT).as_posix()
  except ValueError:
    return str(path)


def print_result(result: ValidationResult, expected_valid: bool | None = None) -> bool:
  expectation_met = result.is_valid if expected_valid is None else result.is_valid == expected_valid
  status = 'PASS' if expectation_met else 'FAIL'
  expectation = '' if expected_valid is None else f' (expected {"valid" if expected_valid else "invalid"})'
  print(f'[{status}] {display_path(result.path)}{expectation}')
  if not expectation_met or (expected_valid is None and not result.is_valid):
    for error in result.errors:
      print(f'  - {error}')
  return expectation_met


def _require_discovery(label: str, paths: list[Path]) -> bool:
  if paths:
    return True
  print(f'[FAIL] No {label} manifests were discovered.')
  return False


def validate_repository(validator: Draft202012Validator) -> bool:
  checks: list[bool] = []
  valid_groups = [
    ('root', [ROOT_MANIFEST] if ROOT_MANIFEST.is_file() else []),
    ('example', discover_files(ROOT / 'examples')),
    ('published example', discover_files(ROOT / 'public' / 'examples')),
    ('positive fixture', discover_files(ROOT / 'test' / 'valid')),
  ]
  invalid_paths = discover_files(ROOT / 'test' / 'invalid')

  for label, paths in valid_groups:
    checks.append(_require_discovery(label, paths))
    for path in paths:
      checks.append(print_result(validate_file(path, validator), expected_valid=True))

  checks.append(_require_discovery('negative fixture', invalid_paths))
  for path in invalid_paths:
    result = validate_file(path, validator)
    checks.append(print_result(result, expected_valid=False))
    if not result.errors:
      print(f'[FAIL] {display_path(path)} produced no validation diagnostic.')
      checks.append(False)

  return all(checks)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('manifests', nargs='*', type=Path, help='Manifest files to validate.')
  parser.add_argument('--schema', type=Path, default=DEFAULT_SCHEMA, help='Schema file to use.')
  parser.add_argument('--all', action='store_true', help='Validate repository manifests and all fixtures.')
  return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
  args = parse_args(argv)
  try:
    validator = create_validator(args.schema.resolve())
  except RuntimeError as error:
    print(f'ERROR: {error}', file=sys.stderr)
    return 2

  if args.all or not args.manifests:
    passed = validate_repository(validator)
  else:
    passed = all(print_result(validate_file(path.resolve(), validator)) for path in args.manifests)

  print('Validation passed.' if passed else 'Validation failed.')
  return 0 if passed else 1


if __name__ == '__main__':
  raise SystemExit(main())
