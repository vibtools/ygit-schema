from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from validate import create_validator, discover_files, validate_file  # noqa: E402


class ValidationSuiteTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls) -> None:
    cls.schema_path = ROOT / 'v1' / 'vibproject.schema.json'
    cls.validator = create_validator(cls.schema_path)

  def test_schema_is_valid_draft_2020_12(self) -> None:
    schema = json.loads(self.schema_path.read_text(encoding='utf-8'))
    Draft202012Validator.check_schema(schema)

  def test_root_manifest_is_valid(self) -> None:
    result = validate_file(ROOT / 'vibproject.ygit', self.validator)
    self.assertTrue(result.is_valid, '\n'.join(result.errors))

  def test_all_valid_manifests_pass(self) -> None:
    paths = [
      *discover_files(ROOT / 'examples'),
      *discover_files(ROOT / 'public' / 'examples'),
      *discover_files(ROOT / 'test' / 'valid'),
    ]
    self.assertGreater(len(paths), 0)
    for path in paths:
      with self.subTest(path=path):
        result = validate_file(path, self.validator)
        self.assertTrue(result.is_valid, '\n'.join(result.errors))

  def test_all_invalid_manifests_fail_with_diagnostics(self) -> None:
    paths = discover_files(ROOT / 'test' / 'invalid')
    self.assertGreater(len(paths), 0)
    for path in paths:
      with self.subTest(path=path):
        result = validate_file(path, self.validator)
        self.assertFalse(result.is_valid)
        self.assertGreater(len(result.errors), 0)

  def test_published_schema_matches_source(self) -> None:
    self.assertEqual(
      self.schema_path.read_bytes(),
      (ROOT / 'public' / 'vpms' / 'v1' / 'vibproject.schema.json').read_bytes(),
    )

  def test_published_example_matches_source(self) -> None:
    self.assertEqual(
      (ROOT / 'examples' / 'vibproject-full-example.ygit').read_bytes(),
      (ROOT / 'public' / 'examples' / 'vibproject-full-example.ygit').read_bytes(),
    )

  def test_repository_cli_suite_passes(self) -> None:
    completed = subprocess.run(
      [sys.executable, 'scripts/validate.py', '--all'],
      cwd=ROOT,
      capture_output=True,
      text=True,
      check=False,
    )
    self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == '__main__':
  unittest.main()
