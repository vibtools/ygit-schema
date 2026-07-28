# Examples

This directory contains the official example files for **ygit-schema**.

The purpose of this folder is to provide complete, valid, and practical examples that demonstrate how every schema should be used in real-world projects.

These examples act as the primary reference for developers, contributors, documentation writers, validators, and AI coding assistants.

---

# Purpose

The `examples/` directory exists to:

- Demonstrate correct schema usage
- Provide production-style example files
- Help developers understand the specification
- Support testing and validation
- Serve as documentation references
- Provide AI-friendly reference implementations

The examples in this directory are intended to be copied, modified, and used as starting points for new projects.

---

# Directory Structure

Example:

```text
examples/

README.md

vibproject-full.ygit
```

As additional schemas are introduced, this directory will expand.

Future example structure may become:

```text
examples/

README.md

vibproject-full.ygit

project-basic.ygit

project-advanced.ygit

plugin-example.ygit

workspace-example.ygit

organization-example.ygit
```

---

# Current Files

## vibproject-full.ygit

Purpose

A complete reference implementation of the official **Vib Project Manifest**.

This example demonstrates every supported section of the schema.

It is intended to show the recommended project structure rather than the smallest possible configuration.

Use this file when:

- Creating a new project
- Learning the schema
- Testing validators
- Building automation
- Training AI systems
- Writing documentation

---

# Example Philosophy

All example files should be:

- Valid
- Complete
- Readable
- Well-organized
- Production-oriented
- Consistent with the latest schema version

Examples should demonstrate **best practices**, not shortcuts.

---

# What Examples Should Demonstrate

Examples should include only officially supported fields.

Each example should demonstrate:

- Correct object structure
- Recommended property ordering
- Proper data types
- Required fields
- Optional fields
- Nested objects
- Arrays
- References
- Metadata

---

# What Examples Should NOT Contain

Examples must never contain:

- Invalid syntax
- Experimental properties
- Deprecated fields
- Placeholder production secrets
- Personal information
- API keys
- Passwords
- Access tokens
- Fake unsupported fields

---

# Example Naming Convention

Official naming format:

```text
<schema>-<purpose>.ygit
```

Examples:

```text
vibproject-full.ygit

project-basic.ygit

project-advanced.ygit

plugin-example.ygit

workspace-example.ygit
```

Use:

- lowercase
- kebab-case

---

# File Format

Official extension:

```text
.ygit
```

Encoding:

```
UTF-8
```

Line Ending:

```
LF
```

Indentation:

```
2 Spaces
```

---

# Property Ordering

Example files should follow the official schema property order.

Do not rearrange fields randomly.

Keeping a consistent order improves:

- readability
- reviews
- documentation
- AI understanding
- version control diffs

---

# Validation

Every example file should successfully validate against the corresponding official schema.

An example is considered complete only if:

- JSON syntax is valid
- Schema validation passes
- Required fields are present
- Unsupported properties are absent

---

# Relationship with the Schema

The schema defines the rules.

The example demonstrates the implementation.

```text
Schema

↓

Validation Rules

↓

Example File

↓

Developer Implementation
```

---

# Relationship with Documentation

Documentation explains **how** something works.

Examples demonstrate **how it is actually written**.

Developers should use both together.

---

# AI Usage

AI coding assistants may use the examples as reference implementations.

When generating new manifests, AI should:

- preserve the official structure
- preserve property ordering
- preserve naming conventions
- follow the latest schema specification

AI should not invent unsupported properties.

---

# Testing

Example files are also used during validation.

Typical workflow:

```text
Schema Updated

↓

Example Updated

↓

Validator Executed

↓

Validation Passed

↓

Documentation Updated
```

---

# Contribution Guidelines

When adding a new example:

- Follow the official schema
- Validate before committing
- Use meaningful values
- Remove unnecessary fields
- Keep formatting consistent
- Update this README if a new example category is introduced

---

# Future Expansion

As new schemas are added, corresponding examples should also be added.

Examples should remain synchronized with the latest released schema version.

---

# Scope

This directory contains:

- Official example manifests
- Reference implementations
- Validation examples
- Documentation examples

This directory does **not** contain:

- Test fixtures
- Temporary files
- Generated files
- Draft examples
- Experimental manifests

---

# Directory Status

```
Examples Directory

Purpose

Official Reference Implementations

Status

Maintained
Versioned
Validation Ready
Developer Ready
```