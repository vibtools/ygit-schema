# Scripts

## `validate.py`

Validates custom manifests or the complete repository fixture suite.

```bash
python scripts/validate.py vibproject.ygit
python scripts/validate.py --all
python scripts/validate.py --schema v1/vibproject.schema.json custom.ygit
```

Exit codes:

- `0`: validation expectations passed.
- `1`: one or more expectations failed.
- `2`: schema or command configuration error.

## `release.py`

Runs schema validation, regression tests, frontend checks, and the production build, then creates a deterministic release ZIP and SHA-256 checksum.

```bash
python scripts/release.py --version 1.0.0
```

Options:

- `--output-dir`: change the release output directory.
- `--allow-dirty`: allow local packaging with uncommitted changes.
- `--skip-frontend`: skip npm checks only when frontend dependencies are unavailable.

Production releases should not use `--allow-dirty` or `--skip-frontend`.

## Repository audit

```bash
python scripts/audit.py
python scripts/audit.py --format-only
```

The audit is dependency-free and verifies UTF-8/LF text hygiene, final newlines, JSON parsing, Markdown fences and relative links, required files, case-insensitive path safety, local source imports, unsupported Lucide brand imports, component size/index rules, package/runtime synchronization, published-copy integrity, manifest paths, secret patterns, conflict markers, and unfinished implementation markers.


## `sourcegenerate.py`

Creates a deterministic direct-replacement source ZIP and SHA-256 checksum while excluding Git metadata, dependency directories, caches, build output, update workspaces, and generated archives.

```bash
python scripts/sourcegenerate.py --dry-run
python scripts/sourcegenerate.py --output ../ygit-schema-source.zip
```

The archive preserves repository-relative paths and intentional empty directories.
