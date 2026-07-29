# Validation

## Repository validation

```bash
python scripts/validate.py --all
```

The command validates official examples and asserts the expected result of every positive and negative fixture.

## Custom manifests

```bash
python scripts/validate.py path/to/vibproject.ygit
```

## Regression tests

```bash
python -m unittest discover -s test -p "test_*.py"
```

## Exit codes

| Code | Meaning |
| ---: | --- |
| `0` | All expectations passed |
| `1` | A manifest produced an unexpected validation result |
| `2` | Schema loading or command configuration failed |

Errors include the JSON property path and failed constraint.
