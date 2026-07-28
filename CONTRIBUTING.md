# Contributing to YGit Schema

Thank you for your interest in contributing to **YGit Schema**.

This repository contains the **official JSON Schema specifications** for the YGit ecosystem. These schemas define the structure and validation rules for all official YGit file formats.

Our goal is to keep every schema stable, versioned, backward-compatible, and easy for developers and tools to consume.

---

# Repository Purpose

This repository is the canonical source for all YGit JSON Schemas.

Examples include:

* Project Schema
* Workspace Schema
* Package Schema
* Plugin Schema
* Configuration Schema
* Lock File Schema

Only schema definitions and related resources belong in this repository.

---

# Repository Structure

```text
v1/
    project.json
    workspace.json
    package.json
    plugin.json
    config.json
    lock.json

v2/
    ...

examples/
test/
scripts/
```

---

# Before You Contribute

Before creating an Issue or Pull Request:

* Search existing Issues.
* Search existing Pull Requests.
* Verify that the proposed change has not already been discussed.
* Keep discussions focused on schema specifications.

---

# Design Principles

Every schema should follow these principles:

* Simple
* Predictable
* Explicit
* Stable
* Versioned
* Tool-friendly
* Language-independent

Avoid unnecessary complexity.

---

# JSON Schema Standard

All schemas must use:

* JSON Schema Draft 2020-12
* UTF-8 encoding
* Four-space indentation
* Unix line endings (LF)

---

# Naming Conventions

Property names should use:

```text
camelCase
```

Example:

```json
{
    "projectName": "",
    "projectVersion": "",
    "minimumCliVersion": ""
}
```

Avoid:

* Spaces
* PascalCase
* snake_case
* kebab-case

unless compatibility requires otherwise.

---

# Schema Versioning

Released schema versions are immutable.

Never introduce breaking changes to an existing released version.

Instead, create a new version.

Good:

```text
v1/project.json
v2/project.json
```

Avoid:

```text
Modify v1 after release
```

---

# Backward Compatibility

Whenever possible:

* Preserve existing fields.
* Preserve existing behavior.
* Introduce new functionality using optional properties.
* Reserve breaking changes for new schema versions only.

---

# Schema Guidelines

Each schema should:

* Have a descriptive title.
* Include a description.
* Define the object type.
* Validate required properties.
* Validate property types.
* Reject invalid structures where appropriate.

Every property should include a meaningful description whenever practical.

---

# Examples

Whenever a schema changes:

* Update example files.
* Add new examples if necessary.
* Keep examples valid.

Examples should represent real-world usage.

---

# Testing

Every schema should be validated before submitting a Pull Request.

Please verify:

* Valid examples pass validation.
* Invalid examples fail validation.
* No existing schema behavior is unintentionally changed.

---

# Documentation

If a schema introduces new behavior:

* Update the README if necessary.
* Update examples.
* Document any migration requirements.

---

# Commit Message Convention

Use clear commit messages.

Examples:

```text
feat(project): add minimumCliVersion

feat(plugin): introduce plugin permissions

fix(config): correct default property type

docs: update schema documentation

test: add invalid project examples
```

---

# Pull Request Checklist

Before submitting a Pull Request, verify:

* Schema is valid.
* Examples are updated.
* Tests pass.
* No unnecessary breaking changes.
* Documentation is updated where applicable.

---

# Reporting Issues

When reporting an issue, include:

* Schema version
* Schema file
* Expected behavior
* Actual behavior
* Example JSON (if applicable)

---

# Feature Requests

Feature requests should explain:

* The problem being solved.
* The proposed solution.
* Why the change belongs in the schema instead of application logic.

---

# Code of Conduct

Please be respectful and constructive during discussions.

Technical disagreements are welcome.
Personal attacks are not.

---

# License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

Thank you for helping improve the YGit ecosystem.
