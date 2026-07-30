from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from validate import (  # noqa: E402
  create_validator,
  create_validators,
  discover_files,
  validate_file,
)


class ValidationSuiteTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    cls.schema_paths = {
      1: ROOT / 'v1' / 'vibproject.schema.json',
      2: ROOT / 'v2' / 'vibproject.schema.json',
    }

    cls.validators = create_validators()

    cls.v1_validator = create_validator(
      cls.schema_paths[1]
    )

  def test_schemas_are_valid_draft_2020_12(self) -> None:
    for version, schema_path in self.schema_paths.items():
      with self.subTest(version=version):
        schema = json.loads(
          schema_path.read_text(
            encoding='utf-8',
          )
        )

        Draft202012Validator.check_schema(
          schema
        )

  def test_root_manifest_is_valid(self) -> None:
    result = validate_file(
      ROOT / 'vibproject.ygit',
      self.v1_validator,
    )

    self.assertTrue(
      result.is_valid,
      '\n'.join(result.errors),
    )

  def test_all_valid_manifests_pass(self) -> None:
    paths = [
      *discover_files(ROOT / 'examples'),
      *discover_files(
        ROOT / 'public' / 'examples'
      ),
      *discover_files(
        ROOT / 'test' / 'valid'
      ),
    ]

    self.assertGreater(
      len(paths),
      0,
    )

    for path in paths:
      with self.subTest(path=path):
        result = validate_file(
          path,
          validators=self.validators,
        )

        self.assertTrue(
          result.is_valid,
          '\n'.join(result.errors),
        )

  def test_all_invalid_manifests_fail_with_diagnostics(
    self,
  ) -> None:
    paths = discover_files(
      ROOT / 'test' / 'invalid'
    )

    self.assertGreater(
      len(paths),
      0,
    )

    for path in paths:
      with self.subTest(path=path):
        result = validate_file(
          path,
          validators=self.validators,
        )

        self.assertFalse(
          result.is_valid
        )

        self.assertGreater(
          len(result.errors),
          0,
        )

  def test_published_schemas_match_sources(self) -> None:
    for version, schema_path in self.schema_paths.items():
      with self.subTest(version=version):
        published_path = (
          ROOT
          / 'public'
          / 'vpms'
          / f'v{version}'
          / 'vibproject.schema.json'
        )

        self.assertEqual(
          schema_path.read_bytes(),
          published_path.read_bytes(),
        )

  def test_published_examples_match_sources(
    self,
  ) -> None:
    source_root = ROOT / 'examples'
    published_root = ROOT / 'public' / 'examples'

    source_paths = discover_files(
      source_root
    )

    self.assertGreater(
      len(source_paths),
      0,
    )

    for source_path in source_paths:
      relative_path = source_path.relative_to(
        source_root
      )

      published_path = (
        published_root
        / relative_path
      )

      with self.subTest(path=relative_path):
        self.assertTrue(
          published_path.is_file()
        )

        self.assertEqual(
          source_path.read_bytes(),
          published_path.read_bytes(),
        )

  def test_repository_cli_suite_passes(
    self,
  ) -> None:
    completed = subprocess.run(
      [
        sys.executable,
        'scripts/validate.py',
        '--all',
      ],
      cwd=ROOT,
      capture_output=True,
      text=True,
      check=False,
    )

    self.assertEqual(
      completed.returncode,
      0,
      completed.stdout + completed.stderr,
    )


if __name__ == '__main__':
  unittest.main()
