# Examples

The official full reference manifest is:

```text
examples/vibproject-full-example.ygit
```

A minimal valid manifest is maintained at:

```text
test/valid/minimal.ygit
```

Every example must:

- Parse as UTF-8 JSON.
- Validate against `v1/vibproject.schema.json`.
- Use only supported properties.
- Preserve official property ordering.
- Avoid credentials and personal data.

Run `python scripts/validate.py --all` to verify all examples.
