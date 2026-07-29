# Test Suite

The test suite verifies the Draft 2020-12 schema itself, the repository root manifest, official and published examples, positive fixtures, negative fixtures, source/public synchronization, and validator CLI behavior.

## Structure

```text
test/
├── valid/
├── invalid/
└── test_validation.py
```

## Positive fixtures

The root `vibproject.ygit`, every official example, every published example, and every `.ygit` file under `test/valid/` must pass schema validation.

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

Every negative fixture must also produce at least one diagnostic. Unexpected passes, unexpected failures, schema drift, published-copy drift, or CLI failures all fail CI.
