# Version 1 (v1)

This directory contains the **official Version 1 (v1)** schema specification for the YGit Schema project.

Version directories are designed to preserve long-term compatibility by allowing each released schema version to evolve independently.

---

# Purpose

The purpose of the `v1/` directory is to provide:

- The official Version 1 schema
- Stable validation rules
- Long-term compatibility
- Versioned schema references
- A permanent implementation target for tools and developers

Once Version 1 is officially released, breaking changes should not be introduced within this directory.

---

# Directory Structure

Current structure:

```text
v1/

README.md

vibproject.schema.json
```

Future versions will be added alongside, not inside, this directory.

Example:

```text
v1/

v2/

v3/
```

---

# Current Schema

| File | Description |
|------|-------------|
| `vibproject.schema.json` | Official Version 1 Vib Project Manifest Schema |

This schema defines the structure, validation rules, and supported properties for the Version 1 project manifest.

---

# Scope

The Version 1 schema defines the official format for:

- Project metadata
- Repository information
- Organization details
- Technology stack
- Platform configuration
- Entry points
- Build configuration
- Documentation
- Automation
- AI metadata
- Release information
- Quality settings

The exact list of supported properties is defined inside the schema itself.

---

# Versioning Policy

Each schema version is maintained independently.

Example:

```text
v1/

↓

Stable

v2/

↓

Next Generation

v3/

↓

Future Release
```

New features should be introduced in future versions when they are not backward compatible.

---

# Compatibility

Applications that support Version 1 should continue to work with Version 1 manifests without requiring modification.

Backward compatibility should be preserved throughout the lifetime of this version.

---

# Validation

Every manifest using Version 1 should validate successfully against:

```text
vibproject.schema.json
```

Validation should verify:

- Required properties
- Data types
- Property structure
- Supported values
- Schema constraints

---

# Related Directories

| Directory | Purpose |
|-----------|---------|
| `examples/` | Official example manifests for Version 1 |
| `test/valid/` | Valid test manifests |
| `test/invalid/` | Invalid validation test cases |
| `scripts/` | Schema validation and release scripts |
| `project/` | Documentation, architecture, standards, and development guides |

---

# Development Rules

Version 1 should follow these principles:

- Stable
- Predictable
- Well documented
- Backward compatible
- Fully validated

Breaking changes should not be introduced after the version is released.

---

# Future Versions

Future schema versions should be created as separate directories.

Example:

```text
v1/

v2/

v3/
```

Each version should contain its own:

- README
- Schema files
- Version-specific documentation (if required)

This approach ensures independent lifecycle management for every released schema version.

---

# Relationship with Examples

Reference implementations are stored in:

```text
examples/
```

Example manifests demonstrate how the Version 1 schema should be used in real projects.

---

# Relationship with Documentation

Complete project documentation is located in:

```text
project/
```

The documentation explains:

- Design philosophy
- Architecture
- Development standards
- Component rules
- Deployment workflow
- Roadmap

The schema contained in this directory is the implementation target described by those documents.

---

# Release Policy

A Version 1 release should meet the following requirements:

- Schema validation passes
- Example manifests validate successfully
- Documentation is synchronized
- Test cases are complete
- Release notes are updated

---

# Directory Status

```
Version

v1

Purpose

Official Stable Schema

Status

Maintained
Versioned
Validation Ready
Implementation Ready
```