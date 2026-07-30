# VPMS Version 2

VPMS Version 2 is frozen at specification version `2.0.0`.

## Canonical schema

- Repository source: `v2/vibproject.schema.json`
- Published copy: `public/vpms/v2/vibproject.schema.json`
- Canonical URL: `https://schema.ygit.dev/vpms/v2/vibproject.schema.json`
- JSON Schema draft: `2020-12`
- SHA-256: `7b1f2686444244b51d7506d6f4fe3b862d8158d0df42856094b97c921ebb1481`

The source and published schema copies must remain byte-identical.

## Freeze policy

The Version 2.0.0 contract is frozen. Do not rename or remove properties, change existing types, narrow accepted values, alter required fields, or change canonical URLs.

A correction is allowed only for a demonstrable defect and must include:

1. A documented compatibility assessment.
2. Updated positive and negative validation fixtures.
3. Updated examples and documentation.
4. A changelog entry.
5. A full Draft 2020-12 and repository validation run.

Breaking changes require VPMS Version 3.

## Official examples

Version 2 examples are maintained in `examples/v2/` and published from `public/examples/v2/`.

| Example | Purpose |
| --- | --- |
| `vibproject-minimal-example.ygit` | Smallest valid Version 2 manifest |
| `vibproject-full-example.ygit` | Every supported Version 2 root section and property |
| `vibproject-desktop-app-example.ygit` | Cross-platform desktop application |
| `vibproject-web-service-example.ygit` | Containerized web service |
| `vibproject-library-example.ygit` | Reusable software library |
| `vibproject-community-project-example.ygit` | Community-owned website |
| `vibproject-worker-example.ygit` | Edge worker application |

All official examples must parse as UTF-8 JSON and validate against the canonical Version 2 schema.
