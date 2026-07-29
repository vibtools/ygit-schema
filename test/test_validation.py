from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

import validate as validation  # noqa: E402


class SchemaValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = validation.create_validator(ROOT / 'v1' / 'vibproject.schema.json')

    def test_valid_fixtures_pass(self) -> None:
        for path in validation.discover_files(ROOT / 'test' / 'valid'):
            with self.subTest(path=path.name):
                result = validation.validate_file(path, self.validator)
                self.assertTrue(result.is_valid, '\n'.join(result.errors))

    def test_invalid_fixtures_fail(self) -> None:
        for path in validation.discover_files(ROOT / 'test' / 'invalid'):
            with self.subTest(path=path.name):
                self.assertFalse(validation.validate_file(path, self.validator).is_valid)

    def test_official_example_passes(self) -> None:
        result = validation.validate_file(
            ROOT / 'examples' / 'vibproject-full-example.ygit',
            self.validator,
        )
        self.assertTrue(result.is_valid, '\n'.join(result.errors))


if __name__ == '__main__':
    unittest.main()
