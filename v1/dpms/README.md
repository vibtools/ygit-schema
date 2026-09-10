# Documentation Package Manifest Specification (DPMS)

**Version:** 1.0.0 (Stable)

---

# Overview

The Documentation Package Manifest Specification (DPMS) defines a standardized manifest for documentation packages.

Its purpose is to allow documentation platforms to automatically discover, identify, organize and publish documentation directly from a project's repository without requiring any manual configuration.

DPMS is intentionally small and focused.

It describes a documentation package only.

It does not describe a documentation website.

---

# Purpose

The primary purpose of DPMS is to make project documentation portable, discoverable and machine-readable.

Instead of manually copying documentation into a documentation website, the documentation platform reads a project's documentation manifest and automatically imports the documentation package.

This allows new projects to appear in the documentation registry with minimal manual work.

---

# Typical Workflow

A project repository contains:

```
Repository
│
├── vibproject.ygit
│
└── docs/
    │
    ├── docs.manifest.ygit
    ├── getting-started/
    ├── installation/
    ├── api/
    ├── faq/
    └── assets/
```

A documentation platform registers the repository once.

The platform then:

1. Reads the repository.
2. Locates the `docs/` directory.
3. Reads `docs.manifest.ygit`.
4. Discovers documentation files.
5. Organizes the documentation structure.
6. Builds the documentation registry.
7. Makes the documentation searchable.
8. Publishes the documentation automatically.

No manual page creation is required.

---

# Scope

DPMS is responsible for describing a documentation package.

This includes:

- Documentation identity
- Documentation root
- Entry document
- Documentation discovery rules
- Documentation structure
- Documentation version information
- Vendor extensions

DPMS intentionally does not describe:

- Website themes
- User interface
- Navigation rendering
- Search engine configuration
- Analytics
- SEO
- Comments
- Styling
- Branding
- Portal configuration

Those responsibilities belong to the documentation platform.

---

# Design Principles

DPMS follows several core principles.

## Documentation First

DPMS describes documentation only.

---

## Platform Independent

Any documentation platform can implement DPMS.

It is not tied to any specific implementation.

---

## Repository First

Documentation always lives inside the project repository.

The repository remains the single source of truth.

---

## Automatic Discovery

Documentation platforms should discover documentation automatically.

Manual synchronization should not be required.

---

## Renderer Agnostic

DPMS never defines how documentation should be rendered.

Rendering is always the responsibility of the documentation platform.

---

## Machine Readable

The manifest is designed primarily for automated tools.

Humans can edit it, but machines consume it.

---

# Repository Layout

A typical repository should follow this structure.

```
Repository
│
├── vibproject.ygit
│
└── docs/
    │
    ├── docs.manifest.ygit
    ├── getting-started/
    ├── installation/
    ├── api/
    ├── faq/
    ├── images/
    └── ...
```

---

# Discovery Process

A DPMS-compatible documentation platform should follow this process.

```
Repository
        │
        ▼
Locate docs/
        │
        ▼
Read docs.manifest.ygit
        │
        ▼
Read discovery rules
        │
        ▼
Discover documentation
        │
        ▼
Build logical structure
        │
        ▼
Generate documentation registry
        │
        ▼
Create searchable documentation
```

---

# Relationship with vibproject.ygit

The project manifest and the documentation manifest have different responsibilities.

## vibproject.ygit

Describes the project.

Examples:

- Project information
- Repository metadata
- Product metadata
- Release metadata

---

## docs.manifest.ygit

Describes the documentation package.

Examples:

- Documentation identity
- Documentation discovery
- Documentation structure
- Documentation versions

---

# Versioning

DPMS follows semantic versioning.

The manifest contains:

- schemaVersion
- manifestVersion

Future schema improvements should maintain backward compatibility whenever possible.

---

# Extension Model

DPMS reserves the `custom` object for vendor-specific extensions.

Platforms may safely store additional implementation-specific data inside this object without affecting the core specification.

---

# Compatibility

A documentation package following DPMS can be discovered by any compatible documentation platform.

No assumptions are made about:

- Programming language
- Framework
- Static site generator
- Documentation renderer
- Hosting platform

---

# Implementation Status

| Version    | Status |
| ---------- | ------ |
| DPMS 1.0.0 | Stable |

---

# License

This specification is published as an open standard for documentation package interoperability.
