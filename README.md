# YGit Schema

> Official JSON Schema Specification for the YGit Ecosystem

[![Schema Version](https://img.shields.io/badge/schema-v1-blue.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Astro](https://img.shields.io/badge/docs-Astro-ff5d01.svg)](#)
[![Cloudflare Pages](https://img.shields.io/badge/deploy-Cloudflare%20Pages-f38020.svg)](#)

---

## Overview

**YGit Schema** is the official schema specification repository for the **YGit Ecosystem**.

It defines standardized manifest formats, validation rules, documentation, examples, and implementation guidelines that allow developers and tools to describe projects in a consistent, machine-readable format.

The repository is designed to provide:

- A stable schema specification
- Official documentation
- Reference implementations
- Validation examples
- Long-term version management
- AI-friendly project standards

---

# Project Goals

The primary goals of this project are:

- Define an official schema specification
- Standardize project manifests
- Improve interoperability across tools
- Simplify validation
- Provide complete developer documentation
- Maintain backward compatibility where possible
- Support automation and AI-assisted development

---

# Repository Structure

```text
ygit-schema/

.github/
    workflows/

assets/
    logo/

examples/

project/

scripts/

test/
    valid/
    invalid/

v1/

v2/

README.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
```

---

# Directory Overview

| Directory | Purpose |
|-----------|---------|
| `.github/` | GitHub workflows and repository automation |
| `assets/` | Project logos and branding assets |
| `examples/` | Official reference manifest examples |
| `project/` | Complete project specifications, architecture, design system, roadmap, and development standards |
| `scripts/` | Validation and release automation scripts |
| `test/` | Valid and invalid schema test cases |
| `v1/` | Current stable schema version |
| `v2/` | Future schema version (reserved) |

---

# Current Schema

Current release:

```text
v1/
    vibproject.schema.json
```

This schema defines the official **Vib Project Manifest**.

Future schema versions will be added as new directories without modifying previous releases.

Example:

```text
v1/

v2/

v3/
```

---

# Documentation

All project specifications are located in:

```text
project/
```

The documentation includes:

- Brand Guidelines
- Layout System
- Component Library
- Page Templates
- Design System
- UI Framework
- Project Architecture
- Coding Standards
- Component Development Guide
- Deployment Specification
- Official Roadmap

The `project/README.md` file explains the purpose and organization of each document.

---

# Examples

The `examples/` directory contains complete reference implementations of official manifests.

Current example:

```text
examples/

vibproject-full.ygit
```

These examples are intended for:

- Learning
- Validation
- Documentation
- Tool development
- AI-assisted generation

See `examples/README.md` for detailed guidelines.

---

# Validation

Schema validation resources are organized as follows:

```text
test/

valid/

invalid/
```

Validation scripts are located in:

```text
scripts/

validate.py
```

Example manifests should always validate successfully against the corresponding schema version.

---

# Design & Development Standards

The project follows a documented engineering standard covering:

- Brand identity
- Design system
- Project architecture
- Component architecture
- Coding standards
- Deployment workflow
- Development roadmap

These standards are maintained under the `project/` directory and should be followed throughout development.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Documentation | Markdown (MD) |
| Frontend Documentation Site | Astro |
| Styling | Tailwind CSS |
| Language | TypeScript |
| Content | MDX |
| Search | Pagefind |
| Syntax Highlighting | Shiki |
| Icons | Lucide Icons |
| Hosting | Cloudflare Pages |
| Source Control | GitHub |

---

# Deployment

Official documentation is designed to be deployed using:

```text
GitHub

↓

Cloudflare Pages

↓

Automatic Build

↓

Automatic Deployment
```

The deployment process is fully documented in:

```text
project/10-DEPLOYMENT.md
```

---

# Development Workflow

```text
Planning

↓

Architecture

↓

Implementation

↓

Validation

↓

Documentation

↓

Release
```

All implementation work should follow the official project roadmap.

---

# Versioning

Schema versions are maintained independently.

Example:

```text
v1/

v2/

v3/
```

Existing versions should remain stable after release.

New functionality should be introduced through new version directories when appropriate.

---

# Contributing

Contributors should:

- Follow the official coding standards
- Follow the component development guide
- Validate all schema changes
- Keep examples synchronized with the schema
- Update documentation when specifications change

Before submitting changes, review:

- `CONTRIBUTING.md`
- `project/08-CODING_STANDARDS.md`
- `project/09-COMPONENT_GUIDE.md`

---

# Project Principles

The project is built around the following principles:

- Consistency
- Simplicity
- Maintainability
- Predictability
- Documentation-first
- Developer-first
- AI-friendly architecture
- Long-term stability

---

# Repository Status

| Component | Status |
|-----------|--------|
| Schema Specification | Active |
| Documentation | Active |
| Design System | Frozen |
| Project Architecture | Frozen |
| Coding Standards | Frozen |
| Component Rules | Frozen |
| Deployment Standard | Frozen |
| Roadmap | Frozen |

---

# License

This project is released under the terms of the **MIT License**.

See the `LICENSE` file for details.

---

# Maintainers

Maintained by the **YGit** project.

---

# Project Status

```text
Repository

Production Structure Ready

Documentation Complete

Architecture Defined

Implementation Ready
```