#!/usr/bin/env python3
"""Validate YGit manifests and the repository validation fixtures."""

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
        for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.absolute_path))
    )
    return ValidationResult(path=path, is_valid=not errors, errors=errors)


def discover_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(path for path in directory.rglob('*.ygit') if path.is_file())


def print_result(result: ValidationResult, expected_valid: bool | None = None) -> bool:
    expectation_met = result.is_valid if expected_valid is None else result.is_valid == expected_valid
    status = 'PASS' if expectation_met else 'FAIL'
    expectation = '' if expected_valid is None else f' (expected {"valid" if expected_valid else "invalid"})'
    print(f'[{status}] {result.path.relative_to(ROOT)}{expectation}')
    if not expectation_met or (expected_valid is None and not result.is_valid):
        for error in result.errors:
            print(f'  - {error}')
    return expectation_met


def validate_repository(validator: Draft202012Validator) -> bool:
    checks: list[bool] = []
    for path in discover_files(ROOT / 'examples'):
        checks.append(print_result(validate_file(path, validator), expected_valid=True))
    for path in discover_files(ROOT / 'test' / 'valid'):
        checks.append(print_result(validate_file(path, validator), expected_valid=True))
    for path in discover_files(ROOT / 'test' / 'invalid'):
        checks.append(print_result(validate_file(path, validator), expected_valid=False))
    if not checks:
        print('[FAIL] No manifests were discovered.')
        return False
    return all(checks)


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifests', nargs='*', type=Path, help='Manifest files to validate.')
    parser.add_argument('--schema', type=Path, default=DEFAULT_SCHEMA, help='Schema file to use.')
    parser.add_argument('--all', action='store_true', help='Validate examples and all positive/negative fixtures.')
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
