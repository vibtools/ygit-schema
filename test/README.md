# Test Suite

The test suite verifies that VPMS Version 1 accepts valid manifests and rejects invalid manifests.

## Structure

```text
test/
├── valid/
├── invalid/
└── test_validation.py
```

## Positive fixtures

Every `.ygit` file under `test/valid/` must pass schema validation.

## Negative fixtures

Every `.ygit` file under `test/invalid/` must fail. Current coverage includes:

- Missing root properties.
- Unsupported root properties.
- Invalid schema and manifest versions.
- Empty required project data.
- Invalid project identifiers and enumerations.

## Run

```bash
python scripts/validate.py --all
python -m unittest discover -s test -p "test_*.py"
```

Unexpected passes and unexpected failures both fail CI.
