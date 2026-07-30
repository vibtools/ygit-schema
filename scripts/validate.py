#!/usr/bin/env python3
"""Validate YGit manifests and the complete repository validation suite."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / 'v1' / 'vibproject.schema.json'
ROOT_MANIFEST = ROOT / 'vibproject.ygit'

SCHEMA_PATHS: Mapping[int, Path] = {
  1: DEFAULT_SCHEMA,
  2: ROOT / 'v2' / 'vibproject.schema.json',
}

SCHEMA_URLS: Mapping[str, int] = {
  'https://schema.ygit.dev/vpms/v1/vibproject.schema.json': 1,
  'https://schema.ygit.dev/vpms/v2/vibproject.schema.json': 2,
}


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

  return Draft202012Validator(
    schema,
    format_checker=FormatChecker(),
  )


def create_validators() -> dict[int, Draft202012Validator]:
  return {
    version: create_validator(path)
    for version, path in SCHEMA_PATHS.items()
  }


def select_schema_version(manifest: Any) -> int:
  if not isinstance(manifest, dict):
    raise RuntimeError('Manifest root must be a JSON object.')

  schema_url = manifest.get('$schema')

  if isinstance(schema_url, str) and schema_url in SCHEMA_URLS:
    return SCHEMA_URLS[schema_url]

  schema_version = manifest.get('schemaVersion')

  if (
    isinstance(schema_version, int)
    and not isinstance(schema_version, bool)
    and schema_version in SCHEMA_PATHS
  ):
    return schema_version

  supported = ', '.join(
    str(version)
    for version in sorted(SCHEMA_PATHS)
  )

  raise RuntimeError(
    'Unable to select a VPMS schema. Expected a recognized $schema URL or '
    f'a supported integer schemaVersion ({supported}).'
  )


def validate_file(
  path: Path,
  validator: Draft202012Validator | None = None,
  *,
  validators: Mapping[int, Draft202012Validator] | None = None,
) -> ValidationResult:
  try:
    manifest = load_json(path)
    selected_validator = validator

    if selected_validator is None:
      if validators is None:
        raise RuntimeError('No schema validator was provided.')

      schema_version = select_schema_version(manifest)

      try:
        selected_validator = validators[schema_version]
      except KeyError as error:
        raise RuntimeError(
          f'No validator is configured for schemaVersion {schema_version}.'
        ) from error

  except RuntimeError as error:
    return ValidationResult(
      path=path,
      is_valid=False,
      errors=(str(error),),
    )

  errors = tuple(
    format_error(error)
    for error in sorted(
      selected_validator.iter_errors(manifest),
      key=lambda item: (
        list(item.absolute_path),
        item.message,
      ),
    )
  )

  return ValidationResult(
    path=path,
    is_valid=not errors,
    errors=errors,
  )


def discover_files(directory: Path) -> list[Path]:
  if not directory.exists():
    return []

  return sorted(
    path
    for path in directory.rglob('*.ygit')
    if path.is_file()
  )


def display_path(path: Path) -> str:
  try:
    return path.relative_to(ROOT).as_posix()
  except ValueError:
    return str(path)


def print_result(
  result: ValidationResult,
  expected_valid: bool | None = None,
) -> bool:
  expectation_met = (
    result.is_valid
    if expected_valid is None
    else result.is_valid == expected_valid
  )

  status = 'PASS' if expectation_met else 'FAIL'

  expectation = (
    ''
    if expected_valid is None
    else f' (expected {"valid" if expected_valid else "invalid"})'
  )

  print(f'[{status}] {display_path(result.path)}{expectation}')

  if not expectation_met or (
    expected_valid is None
    and not result.is_valid
  ):
    for error in result.errors:
      print(f'  - {error}')

  return expectation_met


def _require_discovery(
  label: str,
  paths: list[Path],
) -> bool:
  if paths:
    return True

  print(f'[FAIL] No {label} manifests were discovered.')
  return False


def validate_repository(
  validators: Mapping[int, Draft202012Validator],
  validator: Draft202012Validator | None = None,
) -> bool:
  checks: list[bool] = []

  valid_groups = [
    (
      'root',
      [ROOT_MANIFEST] if ROOT_MANIFEST.is_file() else [],
    ),
    (
      'example',
      discover_files(ROOT / 'examples'),
    ),
    (
      'published example',
      discover_files(ROOT / 'public' / 'examples'),
    ),
    (
      'positive fixture',
      discover_files(ROOT / 'test' / 'valid'),
    ),
  ]

  invalid_paths = discover_files(
    ROOT / 'test' / 'invalid'
  )

  for label, paths in valid_groups:
    checks.append(
      _require_discovery(label, paths)
    )

    for path in paths:
      result = validate_file(
        path,
        validator,
        validators=validators,
      )

      checks.append(
        print_result(
          result,
          expected_valid=True,
        )
      )

  checks.append(
    _require_discovery(
      'negative fixture',
      invalid_paths,
    )
  )

  for path in invalid_paths:
    result = validate_file(
      path,
      validator,
      validators=validators,
    )

    checks.append(
      print_result(
        result,
        expected_valid=False,
      )
    )

    if not result.errors:
      print(
        f'[FAIL] {display_path(path)} '
        'produced no validation diagnostic.'
      )
      checks.append(False)

  return all(checks)


def parse_args(
  argv: Iterable[str] | None = None,
) -> argparse.Namespace:
  parser = argparse.ArgumentParser(
    description=__doc__,
  )

  parser.add_argument(
    'manifests',
    nargs='*',
    type=Path,
    help='Manifest files to validate.',
  )

  parser.add_argument(
    '--schema',
    type=Path,
    default=None,
    help=(
      'Force one schema file instead of selecting '
      'by $schema/schemaVersion.'
    ),
  )

  parser.add_argument(
    '--all',
    action='store_true',
    help='Validate repository manifests and all fixtures.',
  )

  return parser.parse_args(argv)


def main(
  argv: Iterable[str] | None = None,
) -> int:
  args = parse_args(argv)

  try:
    validators = create_validators()

    forced_validator = (
      create_validator(args.schema.resolve())
      if args.schema is not None
      else None
    )

  except RuntimeError as error:
    print(
      f'ERROR: {error}',
      file=sys.stderr,
    )
    return 2

  if args.all or not args.manifests:
    passed = validate_repository(
      validators,
      forced_validator,
    )
  else:
    passed = all(
      print_result(
        validate_file(
          path.resolve(),
          forced_validator,
          validators=validators,
        )
      )
      for path in args.manifests
    )

  print(
    'Validation passed.'
    if passed
    else 'Validation failed.'
  )

  return 0 if passed else 1


if __name__ == '__main__':
  raise SystemExit(main())
