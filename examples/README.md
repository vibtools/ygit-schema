# Examples

This directory contains official, valid VPMS reference manifests.

## Current example

| File | Purpose |
| --- | --- |
| `vibproject-full-example.ygit` | Complete Version 1 manifest demonstrating every supported root object |

## Rules

Examples must:

- Use UTF-8, LF line endings, and two-space indentation.
- Use the `.ygit` extension.
- Follow the schema property order.
- Contain only supported fields.
- Avoid secrets, access tokens, passwords, and private data.
- Pass `python scripts/validate.py --all`.

The full example is copied to `public/examples/` for registry downloads and is displayed on the website examples page.
