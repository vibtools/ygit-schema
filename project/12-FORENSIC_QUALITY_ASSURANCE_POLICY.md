# Forensic Quality Assurance Policy

Version: 1.0

Status: Frozen

---

# Purpose

This document defines the mandatory forensic quality assurance process for the entire project.

Its purpose is to ensure that every update is production-ready before it is considered complete.

No implementation may be considered finished until it successfully passes the complete forensic verification process described in this document.

This policy is mandatory for all contributors, maintainers, automated systems, and AI development agents.

---

# Core Principle

Writing code is NOT the final step.

Verification is the final step.

Every implementation must be proven correct before it can be accepted.

Nothing is considered complete simply because it compiles locally.

Everything must be verified.

---

# Mandatory Development Workflow

Every implementation must follow this workflow.

Requirement

↓

Planning

↓

Implementation

↓

Documentation Update

↓

Internal Validation

↓

Forensic Audit

↓

Issue Detection

↓

Issue Resolution

↓

Dependency Verification

↓

Build Verification

↓

Workflow Verification

↓

Regression Verification

↓

Final Confirmation

↓

Commit

↓

Release

No step may be skipped.

---

# Mandatory Forensic Audit

After every implementation, a complete forensic audit MUST be performed.

The audit must inspect the entire project.

The audit must never inspect only the modified files.

Every update may introduce hidden side effects.

Therefore the entire repository must always be verified.

---

# Repository Integrity Verification

Every forensic audit must verify

Project Architecture

Folder Structure

Naming Conventions

Coding Standards

Documentation

Examples

Schema

Validation

Tests

Deployment

Build Configuration

Automation Scripts

GitHub Workflows

Assets

Configuration Files

Everything must remain internally consistent.

---

# Dependency Verification

Every dependency must be verified.

Including

Node Packages

Python Packages

Astro

TypeScript

ESLint

Tailwind

Pagefind

Build Tools

Validation Libraries

Documentation Libraries

GitHub Actions

Every dependency must be compatible with every other dependency.

No deprecated usage should remain unless intentionally documented.

No missing exports.

No missing modules.

No incompatible versions.

No broken imports.

---

# Static Analysis

Every implementation must pass

Type Checking

Linting

Schema Validation

Static Analysis

No unresolved diagnostics may remain.

Warnings should be investigated.

Errors are never acceptable.

---

# Build Verification

Every implementation must successfully complete

Production Build

Static Site Generation

Asset Generation

Search Index Generation

Documentation Generation

Release Packaging

The project must build successfully on a clean environment.

Local success alone is insufficient.

---

# GitHub Actions Verification

Every workflow must be verified before release.

Including

Validation Workflow

Deployment Workflow

Documentation Workflow

Build Workflow

Release Workflow

Every workflow must execute successfully.

No workflow failures are acceptable.

---

# Continuous Integration Verification

Every change must be validated in a clean environment.

The verification process must assume

No cached dependencies

Fresh installation

Fresh build

Fresh validation

Fresh workflow execution

The project must remain fully reproducible.

---

# Regression Verification

Every implementation must verify that existing functionality remains operational.

New features must never break

Existing Features

Existing Documentation

Examples

Schema Compatibility

Validation

Deployment

Automation

Backward Compatibility

Regression is unacceptable.

---

# Error Resolution Policy

If any issue is discovered,

the implementation is NOT complete.

Every discovered issue must be resolved.

Examples include

Compilation Errors

Type Errors

Lint Errors

Runtime Errors

Build Errors

CI Failures

GitHub Actions Failures

Missing Imports

Missing Exports

Dependency Conflicts

Broken Links

Broken References

Broken Documentation

Broken Examples

Schema Violations

Validation Failures

Configuration Errors

Packaging Errors

Deployment Errors

Everything must be resolved.

Nothing may be ignored.

---

# Reverification Rule

After fixing any issue,

the complete forensic audit MUST be executed again.

Never verify only the fixed file.

The entire repository must be revalidated.

Every fix must itself be verified.

---

# Completion Rule

A task is NOT complete until

All Errors Fixed

All Dependencies Verified

All Modules Verified

All Imports Verified

All Exports Verified

All Builds Successful

All GitHub Actions Successful

All Documentation Updated

All Examples Updated

All Validation Passed

All Tests Passed

All Configuration Verified

All Packaging Verified

Repository Integrity Confirmed

Only then may the task proceed to commit.

---

# AI Development Requirements

Every AI development agent must follow this policy.

AI must never assume an implementation is correct.

AI must actively search for

Hidden Problems

Architecture Violations

Dependency Conflicts

Broken Imports

Broken Exports

Type Errors

Build Errors

Workflow Failures

Compatibility Problems

Regression Risks

AI must resolve every discovered issue before declaring the implementation complete.

---

# Zero Freedom Rule

AI is NOT allowed to

Ignore warnings without investigation

Ignore CI failures

Ignore GitHub Actions failures

Ignore build failures

Ignore dependency conflicts

Ignore module conflicts

Ignore missing exports

Ignore missing imports

Ignore documentation inconsistencies

Ignore validation failures

Declare a task complete before forensic verification

Every issue must be investigated.

Every issue must be resolved.

Every resolution must be verified.

---

# Definition of Done

A task is considered complete only when

✓ Complete Forensic Audit Passed

✓ Repository Integrity Confirmed

✓ Documentation Synchronized

✓ Dependency Compatibility Confirmed

✓ Module Compatibility Confirmed

✓ Type Checking Passed

✓ Linting Passed

✓ Validation Passed

✓ Production Build Passed

✓ GitHub Actions Passed

✓ CI Passed

✓ Regression Testing Passed

✓ Final Repository Verification Passed

Only after all conditions are satisfied may the implementation be committed and released.

---

# Policy Status

This document is a mandatory engineering policy.

This policy is frozen.

Every contributor and every AI development agent must follow this policy without exception.
