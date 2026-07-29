# Version 1 (v1)

This directory contains the official VPMS Version 1 schema.

## Files

| File | Purpose |
| --- | --- |
| `vibproject.schema.json` | Draft 2020-12 schema for `vibproject.ygit` |

## Canonical identifier

```text
https://schema.ygit.dev/vpms/v1/vibproject.schema.json
```

## Required root fields

- `$schema`
- `schemaVersion`
- `manifestVersion`
- `project`

The `project` object requires `id`, `name`, `description`, and `version`.

## Validation guarantees

- Unknown root and nested properties are rejected.
- Semantic version strings are constrained.
- Project identifiers use lowercase kebab-case.
- Paths must be repository-relative and cannot traverse parent directories.
- URI, email, and date-time fields use JSON Schema format validation.

## Compatibility

Version 1 is maintained as an independent major schema generation. Breaking changes require a new directory such as `v2/`. Existing Version 1 manifests continue to target this schema URL.

## Verification

```bash
python -m pip install -r requirements.txt
python scripts/validate.py --all
```
