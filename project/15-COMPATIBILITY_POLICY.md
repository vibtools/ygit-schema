# Compatibility Policy

Version: 1.0

Status: Frozen

---

# Purpose

This document defines the project's official compatibility policy.

Its purpose is to ensure that every dependency, runtime, framework, build tool, automation system, documentation tool, and validation tool remains fully compatible throughout the entire software lifecycle.

Compatibility is a production requirement.

It is not optional.

---

# Single Source of Truth

The official compatibility definition for this project is maintained in

compatibility/compatibility.yaml

No document, script, workflow, or AI development agent may define compatibility independently.

All compatibility verification must use the compatibility matrix.

---

# Core Principle

Every component must be compatible with every other component.

A successful installation does NOT guarantee compatibility.

Compatibility must always be verified.

---

# Compatibility Scope

Compatibility verification includes

Operating Systems

Node.js

Python

Package Manager

Framework

TypeScript

Build System

Validation System

Documentation System

Testing Framework

Search Engine

Assets

Automation Scripts

GitHub Actions

Deployment Environment

Everything must work together.

---

# Compatibility Hierarchy

The project compatibility hierarchy is

Operating System

↓

Runtime

↓

Package Manager

↓

Framework

↓

Language

↓

Libraries

↓

Build System

↓

Validation

↓

Testing

↓

Documentation

↓

Automation

↓

Deployment

Every layer depends on every layer below it.

---

# Compatibility Verification

Every implementation must verify

Dependency Compatibility

Module Compatibility

Import Compatibility

Export Compatibility

Type Compatibility

Configuration Compatibility

Runtime Compatibility

Build Compatibility

CI Compatibility

Deployment Compatibility

Documentation Compatibility

Compatibility verification is mandatory.

---

# Dependency Updates

Before updating any dependency,

verify

Release Notes

Breaking Changes

Migration Guide

Version Compatibility

Supported Runtime

Supported Framework

Supported Build System

Supported Toolchain

Nothing may be upgraded without verification.

---

# Runtime Compatibility

Every supported runtime must remain compatible.

Including

Node.js

Python

Operating Systems

Package Managers

Any runtime incompatibility is considered a release blocker.

---

# Framework Compatibility

Every framework must remain compatible with

Runtime

Language

Plugins

Extensions

Toolchain

Configuration

No unsupported framework combination may be introduced.

---

# Module Compatibility

Every module must verify

Imports

Exports

Module Resolution

Aliases

Generated Types

Dynamic Imports

Build Resolution

No unresolved module is acceptable.

---

# Type Compatibility

Every implementation must successfully pass

TypeScript

Astro Types

Schema Types

Generated Types

Python Types (where applicable)

No type incompatibility may remain.

---

# Build Compatibility

Every implementation must successfully complete

Development Build

Production Build

Documentation Build

Asset Generation

Search Index Generation

Packaging

The project must build successfully from a clean environment.

---

# GitHub Actions Compatibility

Every supported workflow must execute successfully.

Including

Validation

Build

Documentation

Deployment

Release

Automation

GitHub Actions is considered the authoritative production verification environment.

---

# Documentation Compatibility

Documentation must always remain compatible with

Implementation

Schema

Examples

Validation

Versioning

Deployment

Outdated documentation is considered a compatibility issue.

---

# AI Development Requirements

Every AI development agent must

Read compatibility/compatibility.yaml

Verify supported versions

Verify dependency compatibility

Verify module compatibility

Verify type compatibility

Verify build compatibility

Verify GitHub Actions compatibility

Perform a complete forensic compatibility audit before completing any implementation.

AI must never assume compatibility.

Compatibility must always be verified.

---

# Zero Freedom Rules

AI and contributors are NOT allowed to

Ignore compatibility warnings

Ignore dependency conflicts

Ignore version conflicts

Ignore build failures

Ignore CI failures

Ignore missing imports

Ignore missing exports

Ignore type errors

Ignore runtime incompatibilities

Ignore documentation inconsistencies

Ignore deployment incompatibilities

Every compatibility issue must be investigated.

Every compatibility issue must be resolved.

---

# Reverification Policy

Whenever any dependency changes,

the complete compatibility verification process must be executed again.

Never verify only the updated dependency.

Always verify the complete project ecosystem.

---

# Release Policy

No release is permitted unless

Compatibility Matrix Verified

Dependency Compatibility Confirmed

Runtime Compatibility Confirmed

Module Compatibility Confirmed

Type Compatibility Confirmed

Build Compatibility Confirmed

GitHub Actions Passed

Documentation Synchronized

Forensic Audit Passed

Repository Integrity Confirmed

---

# Definition of Done

Compatibility verification is complete only when

✓ compatibility.yaml Updated (if required)

✓ Dependency Compatibility Verified

✓ Runtime Compatibility Verified

✓ Framework Compatibility Verified

✓ Module Compatibility Verified

✓ Type Checking Passed

✓ Validation Passed

✓ Production Build Passed

✓ GitHub Actions Passed

✓ Documentation Updated

✓ Repository Integrity Confirmed

✓ Final Forensic Audit Passed

Only then may the implementation be committed and released.

---

# Policy Status

This document is a mandatory engineering policy.

The compatibility rules defined here are frozen.

The compatibility data is maintained in

compatibility/compatibility.yaml

Every contributor, maintainer, automation system, CI pipeline, and AI development agent must follow this policy without exception.