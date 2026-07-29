# Production Architecture

## Execution flow

```text
MDX and static data
        ↓
Astro content collections and services
        ↓
Layouts and reusable components
        ↓
Static HTML in dist/
        ↓
Pagefind index
        ↓
Cloudflare Pages
```

## Module responsibilities

- `src/pages/`: route composition only.
- `src/layouts/`: shared page structure and metadata.
- `src/components/`: reusable, typed UI rendering.
- `src/content/`: MDX documentation.
- `src/data/`: static schema and navigation data.
- `src/services/`: schema retrieval and business logic.
- `src/utils/`: deterministic helper functions.
- `src/constants/`: routes and immutable application configuration.
- `src/types/`: TypeScript domain types.
- `src/styles/`: exactly `tokens.css`, `fonts.css`, and `global.css`.
- `public/`: published schemas, examples, icons, robots, headers, redirects, and web manifest.

## Data flow

`src/services/schema.service.ts` exposes typed records from `src/data/schema-list.json`. Schema pages use static path generation, so no runtime API or database is required.

Documentation is loaded from `src/content/docs/` through `src/content.config.ts`, rendered at build time, and indexed by Pagefind after Astro writes `dist/`.

## Validation flow

`scripts/validate.py` loads `v1/vibproject.schema.json`, enables Draft 2020-12 format checking, and validates the root manifest, source and published examples, and all positive/negative fixtures. `test/test_validation.py` verifies schema correctness, diagnostics, CLI behavior, and source/public synchronization. `scripts/audit.py` independently verifies repository structure, text hygiene, links, imports, configuration consistency, security markers, and published assets.

## Deployment flow

GitHub Actions validates schema, tests, formatting, linting, type safety, production output, deterministic release packaging, and release artifacts. Cloudflare Pages Git integration builds and deploys `main`; GitHub Actions verifies deployment readiness but does not deploy the website.

## Extension points

- New schema generations: add a version directory, public registry path, data record, fixtures, docs, and migration guide.
- New docs: add MDX to `src/content/docs/` and navigation entries to `src/data/navigation.json`.
- New components: follow one-component-per-folder and `index.ts` export rules.


## Release and source packaging

- `scripts/release.py` performs mandatory checks, verifies synchronized release versions, and creates a deterministic versioned archive under `release/`.
- `scripts/sourcegenerate.py` creates a deterministic direct-replacement source snapshot without generated dependencies, caches, build output, or Git metadata.
- `.github/workflows/release.yml` verifies tag or manual releases and publishes tagged GitHub releases.
