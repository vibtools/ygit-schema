# AI Development Verification Protocol

Version: 1.0

Status: Frozen

---

# Purpose

This document defines the mandatory verification protocol for all AI development agents contributing to this project.

Its purpose is to ensure that every AI-generated implementation is accurate, reproducible, production-ready, and fully verified before it is considered complete.

Verification is mandatory.

Generation alone is never sufficient.

---

# Scope

This protocol applies to every AI-assisted task, including

- New Features
- Bug Fixes
- Refactoring
- Documentation
- Schema Updates
- Configuration Changes
- Dependency Updates
- Build System Changes
- CI/CD Changes
- Release Preparation

No AI-generated change is exempt.

---

# Core Principle

AI must verify every implementation before returning the final result.

AI must never assume

- generated code is correct
- generated documentation is correct
- dependencies are compatible
- builds will succeed
- CI will pass

Everything must be verified.

---

# Required Project Review

Before writing or modifying any code, AI must review

README.md

CHANGELOG.md

CONTRIBUTING.md

Project Documentation

Architecture Documents

Policy Documents

compatibility/compatibility.yaml

Configuration Files

Examples

Existing Source Code

AI must understand the project before making changes.

---

# Required Policy Review

AI must follow every mandatory engineering policy.

Including

FORENSIC_QUALITY_ASSURANCE_POLICY

DEPENDENCY_MANAGEMENT_POLICY

CI_CD_VERIFICATION_POLICY

COMPATIBILITY_POLICY

PRE_RELEASE_CHECKLIST

No implementation may violate any project policy.

---

# Development Workflow

Every implementation must follow

Understand Project

↓

Review Policies

↓

Review Compatibility Matrix

↓

Plan Implementation

↓

Implement Changes

↓

Update Documentation

↓

Update Examples

↓

Validate Changes

↓

Type Checking

↓

Linting

↓

Dependency Verification

↓

Compatibility Verification

↓

Production Build

↓

GitHub Actions Verification

↓

Regression Verification

↓

Forensic Audit

↓

Repository Integrity Verification

↓

Final Review

↓

Return Result

No step may be skipped.

---

# Documentation Verification

AI must verify

README synchronization

Documentation accuracy

Examples

Migration Guides

Configuration References

Schema References

Version References

Documentation must always match the implementation.

---

# Dependency Verification

AI must verify

Supported Versions

Package Compatibility

Missing Packages

Deprecated APIs

Breaking Changes

Lock File

Dependency Integrity

No dependency assumption is permitted.

---

# Compatibility Verification

AI must verify compatibility across

Operating System

Runtime

Package Manager

Framework

Language

Libraries

Validation

Testing

Build System

CI/CD

Deployment

Everything must remain compatible.

---

# Source Code Verification

AI must verify

Imports

Exports

Naming

Architecture

Project Structure

Module Resolution

Generated Code

Configuration

No unresolved issue is acceptable.

---

# Static Analysis Verification

AI must verify

Type Checking

Linting

Schema Validation

Configuration Validation

Documentation Validation

Every issue must be investigated.

---

# Build Verification

AI must verify

Development Build

Production Build

Documentation Build

Search Index

Packaging

Generated Artifacts

Clean Environment Build

The project must build successfully.

---

# GitHub Actions Verification

AI must verify

Validation Workflow

Build Workflow

Documentation Workflow

Deployment Workflow

Release Workflow

Automation Workflow

Workflow compatibility is mandatory.

---

# Regression Verification

AI must verify that existing functionality continues to work.

Verify

Existing Features

Schema

Examples

Documentation

Automation

Configuration

Build System

Backward Compatibility

No regression is acceptable.

---

# Repository Integrity Verification

AI must verify

Repository Structure

Folder Structure

Naming Standards

Configuration Files

Assets

Documentation

Examples

Generated Files

Ignore Rules

Repository integrity must always be preserved.

---

# Forensic Audit

Before returning the final result,

AI must perform

Repository Audit

Dependency Audit

Compatibility Audit

Documentation Audit

Configuration Audit

Build Audit

CI Audit

Architecture Audit

No unresolved finding is acceptable.

---

# AI Self-Verification Checklist

AI must confirm

✓ Project Reviewed

✓ Policies Reviewed

✓ Compatibility Matrix Reviewed

✓ Documentation Updated

✓ Examples Updated

✓ Dependencies Verified

✓ Compatibility Verified

✓ Type Checking Passed

✓ Validation Passed

✓ Production Build Passed

✓ GitHub Actions Compatible

✓ No Missing Imports

✓ No Missing Exports

✓ No Dependency Conflicts

✓ No Build Failures

✓ No Documentation Inconsistencies

✓ Regression Verification Passed

✓ Repository Integrity Confirmed

✓ Final Forensic Audit Passed

---

# Completion Rules

AI must never state

"Done"

"Completed"

"Finished"

"Production Ready"

unless every verification step has successfully passed.

If verification has not been completed,

AI must explicitly state

Verification Pending

---

# Zero Freedom Rules

AI and contributors are NOT allowed to

Skip project review

Skip policy review

Skip documentation updates

Skip dependency verification

Skip compatibility verification

Skip validation

Skip type checking

Skip build verification

Skip GitHub Actions verification

Skip forensic audit

Skip repository integrity verification

Assume generated code is correct

Declare completion without verification

Every requirement must be satisfied.

---

# Definition of Done

An AI-generated implementation is complete only when

✓ Project Reviewed

✓ Policies Followed

✓ Compatibility Matrix Verified

✓ Documentation Synchronized

✓ Dependencies Verified

✓ Compatibility Verified

✓ Validation Passed

✓ Type Checking Passed

✓ Production Build Passed

✓ GitHub Actions Compatible

✓ Regression Verification Passed

✓ Repository Integrity Confirmed

✓ Final Forensic Audit Passed

Only then may the implementation be considered complete, committed, merged, deployed, or released.

---

# Policy Status

This document is a mandatory engineering protocol.

It is frozen.

Every AI development agent contributing to this project must follow this protocol without exception.