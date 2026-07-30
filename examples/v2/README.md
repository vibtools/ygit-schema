# VPMS Version 2 Examples

These files are official valid reference manifests for `https://schema.ygit.dev/vpms/v2/vibproject.schema.json`.

## Files

| File | Coverage |
| --- | --- |
| `vibproject-minimal-example.ygit` | Required root fields only |
| `vibproject-full-example.ygit` | Complete Version 2 field coverage |
| `vibproject-desktop-app-example.ygit` | `desktop-app` classification |
| `vibproject-web-service-example.ygit` | `web-service` classification |
| `vibproject-library-example.ygit` | `library` classification |
| `vibproject-community-project-example.ygit` | `community-project` classification |
| `vibproject-worker-example.ygit` | `worker` classification |

## Rules

- UTF-8 without BOM.
- LF line endings.
- Two-space JSON indentation.
- `.ygit` extension.
- Canonical Version 2 `$schema` URL.
- `schemaVersion` must equal `2`.
- `manifestVersion` and `metadata.specificationVersion` must use major version `2`.
- No credentials, tokens, passwords, or private data.
- Source and published copies must remain byte-identical.
