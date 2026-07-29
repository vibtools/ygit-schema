# YGit Schema

> Official JSON Schema Specification and Registry for the YGit Ecosystem

[![Schema Version](https://img.shields.io/badge/schema-v1-blue.svg)](v1/vibproject.schema.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Astro](https://img.shields.io/badge/docs-Astro-ff5d01.svg)](package.json)
[![Cloudflare Pages](https://img.shields.io/badge/deploy-Cloudflare%20Pages-f38020.svg)](project/10-DEPLOYMENT.md)
[![Validate](https://github.com/vibtools/ygit-schema/actions/workflows/validate.yml/badge.svg)](https://github.com/vibtools/ygit-schema/actions/workflows/validate.yml)
[![Build Readiness](https://github.com/vibtools/ygit-schema/actions/workflows/deploy.yml/badge.svg)](https://github.com/vibtools/ygit-schema/actions/workflows/deploy.yml)

## Overview

YGit Schema publishes the **Vib Project Manifest Specification (VPMS)**, official examples, validation tooling, regression fixtures, documentation, and the `schema.ygit.dev` static registry portal.

The Version 1 schema validates `vibproject.ygit` files using JSON Schema Draft 2020-12. The registry portal is built with Astro, Tailwind CSS, TypeScript, MDX, Shiki, Pagefind, and Lucide icons, then deployed through Cloudflare Pages Git integration.

## Repository structure

```text
ygit-schema/
├── .github/workflows/     CI validation and build-readiness checks
├── assets/                Source brand assets
├── compatibility/         Supported runtime and dependency matrix
├── docs/                  Repository documentation
├── examples/              Official valid manifests
├── project/               Frozen architecture, design, and workflow specifications
├── public/                Registry assets and published schema files
├── scripts/               Validation and release automation
├── src/                   Astro application source
├── test/                  Positive, negative, and Python regression tests
├── v1/                    VPMS Version 1 schema
├── v2/                    Reserved future-major-version boundary
├── SECURITY.md            Private vulnerability reporting policy
├── SUPPORT.md             Support scope and channels
├── CODE_OF_CONDUCT.md     Community participation standards
├── FORENSIC_AUDIT_REPORT.md
├── .gitattributes
├── .editorconfig
├── .gitignore
├── astro.config.mjs
├── package.json
├── tailwind.config.ts
└── tsconfig.json
```

## Current schema

- Schema: `v1/vibproject.schema.json`
- Published URL: `https://schema.ygit.dev/vpms/v1/vibproject.schema.json`
- Example: `examples/vibproject-full-example.ygit`
- Schema version: `1`
- Manifest format: `1.0.0`

Minimal manifest:

```json
{
  "$schema": "https://schema.ygit.dev/vpms/v1/vibproject.schema.json",
  "schemaVersion": 1,
  "manifestVersion": "1.0.0",
  "project": {
    "id": "example-project",
    "name": "Example Project",
    "description": "A minimal valid VPMS manifest.",
    "version": "1.0.0"
  }
}
```

## Install

### Validator

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate.py --all
```

### Registry portal

Node.js 24.16.0 or later and npm 11 or later are required. The `.nvmrc` file pins the supported Node.js major version.

```bash
npm install
npm run dev
```

## Quality commands

```bash
npm run format:check
npm run audit
npm run check
npm run validate
npm run test
npm run build
```

`npm run build` produces static output in `dist/` and generates the Pagefind search index.

## Validation behavior

The validator enforces the following expectations:

- The repository root `vibproject.ygit`, every manifest in `examples/`, every published example, and every manifest in `test/valid/` pass.
- Every manifest in `test/invalid/` fails.
- Unknown root and nested properties are rejected.
- Required fields, types, semantic versions, paths, URLs, email addresses, and timestamps are checked.

Validate custom manifests:

```bash
python scripts/validate.py path/to/vibproject.ygit
```

## Release preparation

```bash
python scripts/release.py --version 1.0.0
```

The release script verifies version synchronization, requires a clean worktree when Git metadata is present, runs the forensic audit, validation, tests, frontend checks, and production build, then creates a deterministic ZIP plus SHA-256 checksum in `release/`. Tagged releases are verified and published by `.github/workflows/release.yml`.

## Deployment

- Source of truth: GitHub
- Production branch: `main`
- Build command: `npm run build`
- Output directory: `dist`
- Hosting: Cloudflare Pages
- Deployment: Cloudflare Pages Git integration

GitHub Actions validates quality and build readiness. It does not perform production deployment.

## Documentation

- User and developer documentation: `docs/`
- Website content: `src/content/docs/`
- Frozen project specifications: `project/`
- Schema reference: `v1/README.md`
- Test philosophy: `test/README.md`
- Automation reference: `scripts/README.md`

## Status

| Component | Status |
| --- | --- |
| VPMS Version 1 schema | Implemented |
| Examples and fixtures | Implemented |
| Validation and release automation | Implemented |
| Documentation portal | Implemented |
| Search | Implemented |
| CI quality checks | Implemented |
| Cloudflare Pages configuration | Ready |
| Production deployment | Requires repository-to-Cloudflare connection |

## Source snapshot

Create a deterministic direct-replacement source archive without generated caches or build output:

```bash
python scripts/sourcegenerate.py --output ../ygit-schema-source.zip
```

The command writes a matching `.zip.sha256` checksum file.

## Security and support

- Vulnerabilities: [SECURITY.md](SECURITY.md)
- Usage and defect support: [SUPPORT.md](SUPPORT.md)
- Community expectations: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- Latest repository verification: [FORENSIC_AUDIT_REPORT.md](FORENSIC_AUDIT_REPORT.md)

## License

Released under the [MIT License](LICENSE).
