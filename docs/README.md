# Documentation

This directory contains the official documentation for the **YGit Schema** project.

The documentation explains how to design, implement, validate, version, migrate, and use the YGit Schema ecosystem.

It serves as the primary knowledge base for developers, contributors, maintainers, technical writers, and AI coding assistants.

---

# Purpose

The `docs/` directory exists to:

- Explain the schema
- Help developers get started
- Document every supported feature
- Provide implementation guidance
- Maintain versioned documentation
- Support AI-assisted development
- Keep documentation synchronized with the project

Documentation should always reflect the latest released schema and project specifications.

---

# Documentation Structure

```text
docs/

README.md

01-getting-started/

02-schema-reference/

03-guides/

04-examples/

05-validation/

06-versioning/

07-migration/

08-faq/

assets/
```

---

# Directory Overview

| Directory | Purpose |
|-----------|---------|
| `01-getting-started/` | Installation, quick start, first manifest, and introductory documentation. |
| `02-schema-reference/` | Complete reference documentation for every schema, property, object, and validation rule. |
| `03-guides/` | Practical guides, tutorials, best practices, and implementation walkthroughs. |
| `04-examples/` | Documentation explaining official example manifests and real-world usage. |
| `05-validation/` | Validation rules, validator usage, common errors, and troubleshooting. |
| `06-versioning/` | Schema versioning strategy, release lifecycle, and compatibility documentation. |
| `07-migration/` | Migration guides for upgrading between schema versions. |
| `08-faq/` | Frequently asked questions and common developer issues. |
| `assets/` | Images, diagrams, screenshots, icons, and other documentation assets. |

---

# Documentation Categories

The documentation is divided into two primary categories.

## 1. Reference Documentation

Reference documentation describes the schema specification.

Typical content includes:

- Objects
- Properties
- Data Types
- Validation Rules
- Enumerations
- Required Fields
- Default Values
- Examples

Reference documentation should always match the latest official schema.

---

## 2. Developer Guides

Developer guides explain how to use the schema in real projects.

Typical content includes:

- Tutorials
- Best Practices
- Common Mistakes
- Integration Guides
- Recommendations
- Troubleshooting
- Migration Examples

Guides focus on practical implementation rather than specification details.

---

# Recommended Reading Order

New developers should follow this order.

```text
Getting Started

↓

Schema Reference

↓

Guides

↓

Examples

↓

Validation

↓

Versioning

↓

Migration

↓

FAQ
```

This order progresses from basic concepts to advanced implementation topics.

---

# Documentation Workflow

Documentation should evolve alongside the project.

Official workflow:

```text
Requirement

↓

Planning

↓

Development

↓

Documentation Update

↓

Validation

↓

Review

↓

Release
```

Documentation is an integral part of development and should not be treated as a post-development task.

---

# Synchronization Policy

The documentation must always remain synchronized with:

- Schema
- Examples
- Validation Rules
- Version Information
- Project Architecture
- Development Standards

Any project change affecting functionality, structure, or behavior should be reflected in the relevant documentation before release.

---

# Relationship with Other Directories

```text
Schema

↓

v1/
v2/

↓

Examples

↓

Validation

↓

Documentation
```

The documentation explains and complements the implementation found in other directories.

---

# Documentation Principles

All documentation should be:

- Accurate
- Complete
- Versioned
- Consistent
- Developer-friendly
- AI-readable
- Easy to maintain
- Easy to navigate

---

# Writing Standards

Documentation should follow these guidelines:

- Use clear and descriptive headings.
- Explain concepts before implementation details.
- Include practical examples where appropriate.
- Keep terminology consistent across all documents.
- Avoid duplicated content whenever possible.
- Update existing documentation instead of creating conflicting documents.

---

# Documentation Sources

Documentation should be based on the official project specifications.

Primary sources include:

- JSON Schema
- Project Specifications
- Examples
- Validation Rules
- Development Standards

Documentation should never contradict the official schema.

---

# AI Compatibility

The documentation is designed to be consumed by both humans and AI coding assistants.

Documentation should therefore:

- Use consistent terminology.
- Preserve predictable document structure.
- Clearly separate specification from guidance.
- Avoid ambiguous language.
- Reference official examples whenever applicable.

---

# Documentation Maintenance

Whenever the project changes, review the affected documentation.

Typical update scenarios include:

- New schema property
- New validation rule
- New example
- Version release
- Breaking change
- New feature
- Deprecated functionality

Documentation should always represent the current state of the project.

---

# Scope

This directory contains:

- User documentation
- Developer documentation
- Schema reference
- Guides
- Examples
- Validation documentation
- Versioning documentation
- Migration documentation
- FAQ

This directory does **not** contain:

- Schema implementation
- Production source code
- Test manifests
- Automation scripts
- Build artifacts

---

# Related Directories

| Directory | Relationship |
|-----------|--------------|
| `v1/` | Official schema definitions |
| `examples/` | Reference manifests documented here |
| `test/` | Validation behavior described here |
| `scripts/` | Documentation for validation and release tooling |
| `project/` | Internal project specifications, architecture, design system, and engineering standards |

---

# Documentation Status

```text
Documentation

Purpose

Official Project Documentation

Status

Maintained

Versioned

Developer Ready

AI Ready
```
