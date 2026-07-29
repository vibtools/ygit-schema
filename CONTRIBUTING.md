# Contributing to YGit Schema

Thank you for contributing to the official YGit Schema specification and registry portal.

## Scope

This repository contains:

- Versioned JSON Schemas for YGit file formats.
- Official examples and validation fixtures.
- Validation and release automation.
- User and developer documentation.
- The Astro implementation of `schema.ygit.dev`.

Changes must remain within the frozen project architecture and specifications in `project/`.

## Before contributing

1. Search existing issues and pull requests.
2. Read `project/00-DOCUMENTATION_POLICY.md` through `project/11-ROADMAP.md`.
3. Read `project/08-CODING_STANDARDS.md` and `project/09-COMPONENT_GUIDE.md`.
4. Install Python and Node.js dependencies.
5. Create a branch using `feature/*`, `fix/*`, `docs/*`, or `chore/*` as appropriate.

## Formatting

- UTF-8 encoding.
- Unix LF line endings.
- Two-space indentation for JSON, YAML, TypeScript, Astro, CSS, and MDX.
- Python follows the existing two-space repository convention.
- Property names use `camelCase`.
- Components use `PascalCase` and one component folder with an `index.ts` export.
- Utilities and TypeScript modules use `camelCase` filenames.
- Data files use `kebab-case` filenames.

## Schema changes

Released major schema directories must not receive breaking changes.

A schema change must include:

- Updated schema constraints and descriptions.
- At least one positive fixture when behavior is added.
- At least one negative fixture for every new validation rule.
- Updated official examples.
- Updated reference, validation, versioning, migration, and FAQ documentation where applicable.

The schema uses JSON Schema Draft 2020-12 and rejects unsupported properties where appropriate.

## Frontend changes

Frontend work must preserve:

- Astro, Tailwind CSS, TypeScript, MDX, Shiki, Pagefind, Lucide, and Cloudflare Pages.
- The frozen dark-first token system and compact typography.
- Border-based components without shadows, glow, blur, glass, or marketing patterns.
- The desktop three-column documentation layout and mobile single-column layout.
- Keyboard navigation, focus visibility, labels, semantic HTML, 44px mobile touch targets, and reduced-motion support.

Do not add component-level CSS files, hardcoded colors, global state libraries, or production deployment through GitHub Actions.

## Required checks

```bash
python -m pip install -r requirements.txt
npm install
npm run format:check
npm run check
npm run validate
npm run test
npm run build
```

## Commit convention

Use Conventional Commits:

```text
feat(schema): add optional project field
fix(validation): reject unsupported nested property
docs: update VPMS reference
test: add invalid semantic version fixture
ci: strengthen build validation
```

## Pull request checklist

- Architecture and frozen technology choices are unchanged.
- Existing behavior remains compatible unless a new major schema version is introduced.
- Schema, examples, tests, and documentation are synchronized.
- No secrets, tokens, passwords, or private data are committed.
- All required checks pass.
- The production build contains `dist/index.html` and the Pagefind index.

By contributing, you agree that your contribution is licensed under the MIT License.
