# Test Suite

This directory contains the official validation test suite for **YGit Schema**.

The purpose of this directory is to verify that every schema behaves exactly as specified by ensuring valid manifests pass validation and invalid manifests fail validation.

The test suite is an essential part of maintaining schema quality, stability, and backward compatibility.

---

# Purpose

The `test/` directory exists to:

- Verify schema correctness
- Prevent regressions
- Validate future schema updates
- Ensure consistent validator behavior
- Provide reference test cases
- Support automated CI validation

Every schema release should pass all tests before publication.

---

# Directory Structure

Current structure:

```text
test/

README.md

valid/

invalid/
```

---

# Directory Overview

| Directory | Purpose |
|-----------|---------|
| `valid/` | Manifest files that **must pass** schema validation |
| `invalid/` | Manifest files that **must fail** schema validation |

---

# valid/

This directory contains official manifests that fully comply with the corresponding schema.

Every file inside this directory should validate successfully.

Typical examples include:

```text
valid/

minimal.ygit

basic.ygit

full.ygit
```

These files demonstrate supported and correct usage of the schema.

---

# invalid/

This directory contains manifests intentionally created with validation errors.

These files are used to verify that validators correctly reject invalid manifests.

Typical examples include:

```text
invalid/

missing-required-field.ygit

invalid-type.ygit

unknown-property.ygit

invalid-version.ygit
```

These files are not examples of correct usage.

They exist solely for validation testing.

---

# Validation Rules

Every file inside `valid/` must:

- Pass JSON parsing
- Pass schema validation
- Contain required properties
- Follow official property definitions
- Contain only supported fields

---

Every file inside `invalid/` must fail for one or more reasons, such as:

- Missing required property
- Invalid data type
- Unsupported property
- Invalid enum value
- Invalid object structure
- Schema constraint violation
- Incorrect version identifier

---

# Test Philosophy

Validation testing follows a simple principle:

```text
Correct Input

↓

Validation

↓

PASS
```

```text
Invalid Input

↓

Validation

↓

FAIL
```

Unexpected results should always be treated as defects.

---

# Relationship with the Schema

```text
Schema

↓

Validation Rules

↓

Test Files

↓

Validation Result
```

The schema defines the rules.

The test suite verifies that those rules are correctly enforced.

---

# Relationship with Examples

The `examples/` directory demonstrates how manifests should be written.

The `test/` directory verifies whether manifests are accepted or rejected.

```text
examples/

↓

Reference Implementation

test/

↓

Validation Verification
```

---

# Validation Workflow

Recommended validation process:

```text
Schema Updated

↓

Valid Test Files

↓

Invalid Test Files

↓

Validation Script

↓

Results Verified

↓

Release
```

---

# CI Integration

The test suite is intended to be executed automatically during Continuous Integration.

Typical workflow:

```text
Git Push

↓

GitHub Actions

↓

Run Validator

↓

Run Test Suite

↓

Pass

↓

Continue Pipeline
```

If any validation test fails, the build should fail.

---

# File Naming Convention

Use descriptive, lowercase, kebab-case names.

Examples:

```text
minimal.ygit

basic-project.ygit

full-project.ygit

missing-name.ygit

invalid-platform.ygit

unsupported-property.ygit
```

Avoid generic names such as:

```text
test1.ygit

sample.ygit

new.ygit
```

---

# Test Coverage

The complete test suite should cover:

- Required properties
- Optional properties
- Data types
- Arrays
- Objects
- Nested objects
- Enumerations
- Default values (if applicable)
- Pattern validation
- String constraints
- Numeric constraints
- Additional property restrictions
- Version compatibility

---

# Adding New Tests

When introducing a new schema feature:

1. Update the schema.
2. Add at least one valid test case.
3. Add one or more invalid test cases.
4. Verify all tests pass.
5. Update documentation if required.

Every new validation rule should be accompanied by corresponding tests.

---

# Version Compatibility

Tests should always target a specific schema version.

Example future structure:

```text
test/

v1/
    valid/
    invalid/

v2/
    valid/
    invalid/
```

If version-specific testing becomes necessary, each schema version should maintain its own independent test suite.

---

# Scope

This directory contains:

- Validation test manifests
- Positive test cases
- Negative test cases
- Schema verification data

This directory does **not** contain:

- Documentation examples
- Draft manifests
- Production manifests
- Temporary files
- Generated output

---

# Directory Status

```text
Test Suite

Purpose

Schema Validation

Status

Maintained
Validation Ready
CI Ready
Quality Assurance Ready
```