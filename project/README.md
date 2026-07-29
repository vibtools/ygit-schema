# Project Documentation

This directory contains the official project specifications, design system, architecture, development standards, deployment standards, roadmap, and UI prototypes for **schema.ygit.dev**.

The documents in this folder define the complete product foundation before implementation begins.

---

# Purpose

This folder serves as the **single source of truth** for:

- Product Design
- UI/UX Standards
- Architecture
- Development Rules
- Deployment Standards
- Project Planning
- Visual Prototypes

Every implementation should follow these documents unless they are officially updated.

---

# Document Order

The documents are intended to be read in the following order.

| Order | Document | Purpose |
|-------:|----------|---------|
| 00 | `00-DOCUMENTATION_POLICY.md` | Mandatory development-to-documentation synchronization policy. |
| 01 | `01-BRAND_GUIDELINES.md` | Brand identity, visual language, colors, typography and design philosophy. |
| 02 | `02-LAYOUT_SYSTEM.md` | Overall layout structure, navigation, header, sidebar, footer and spacing system. |
| 03 | `03-COMPONENT_LIBRARY.md` | Official UI components and component specifications. |
| 04 | `04-PAGE_TEMPLATES.md` | Standard page layouts and page-level structure. |
| 05 | `05-DESIGN_SYSTEM_RULES.md` | Responsive rules, accessibility, motion, design tokens and frozen UI rules. |
| 06 | `06-UI_FRAMEWORK.md` | Official frontend technology stack and framework decisions. |
| 07 | `07-PROJECT_ARCHITECTURE.md` | Project folder structure, architecture and application organization. |
| 08 | `08-CODING_STANDARDS.md` | Coding conventions, naming standards and development rules. |
| 09 | `09-COMPONENT_GUIDE.md` | Component implementation rules and reusable component architecture. |
| 10 | `10-DEPLOYMENT.md` | GitHub → Cloudflare Pages deployment workflow and CI/CD specification. |
| 11 | `11-ROADMAP.md` | Official development roadmap and implementation phases. |
| 12 | `12-FORENSIC_QUALITY_ASSURANCE_POLICY.md` | Mandatory repository-wide verification policy. |
| 13 | `13-DEPENDENCY_MANAGEMENT_POLICY.md` | Dependency selection, update, and integrity requirements. |
| 14 | `14-CI_CD_VERIFICATION_POLICY.md` | Clean-environment CI/CD and release verification requirements. |
| 15A | `15-COMPATIBILITY_POLICY.md` | Cross-platform and runtime compatibility requirements. |
| 15B | `15-DEPENDENCY_COMPATIBILITY_MATRIX.md` | Human-readable dependency compatibility policy. |
| 16 | `16-PRE_RELEASE_CHECKLIST.md` | Mandatory pre-release acceptance checklist. |
| 17 | `17-AI_DEVELOPMENT_VERIFICATION_PROTOCOL.md` | Verification protocol for AI-assisted changes. |
| AI | `AI_DEVELOPMENT_PROMPT.md` | Repository-specific AI development contract. |

---

# Sandbox Files

The HTML files are visual prototypes used for validating layouts before implementation.

These files are **reference prototypes only**.

They are **not** production code.

| File | Purpose |
|------|---------|
| `sandbox-home.html` | Home page prototype |
| `sandbox-documentation.html` | Documentation page prototype |
| `sandbox-schema-details.html` | Schema details page prototype |
| `sandbox-search-results.html` | Search results prototype |
| `sandbox-mobile.html` | Mobile layout prototype |

---

# Reference Assets

| File | Purpose |
|------|---------|
| `Vib-Tools-Brand-Guidelines.pdf` | Original branding and visual identity reference |
| `99-ARCHIVE_ROADMAP.md` | Archived planning document retained for historical reference |

---

# Recommended Reading Flow

```text
Brand Guidelines
        │
        ▼
Layout System
        │
        ▼
Component Library
        │
        ▼
Page Templates
        │
        ▼
Design System Rules
        │
        ▼
UI Framework
        │
        ▼
Project Architecture
        │
        ▼
Coding Standards
        │
        ▼
Component Guide
        │
        ▼
Deployment
        │
        ▼
Roadmap
```

---

# Development Flow

```text
Read Documentation
        │
        ▼
Review Sandbox Prototypes
        │
        ▼
Initialize Project
        │
        ▼
Implement Layout
        │
        ▼
Build Components
        │
        ▼
Develop Pages
        │
        ▼
Add Documentation Content
        │
        ▼
Deploy to Cloudflare Pages
```

---

# Scope

This folder defines:

- Product specifications
- Design specifications
- UI standards
- Development standards
- Project architecture
- Component architecture
- Deployment architecture
- Development roadmap

This folder does **not** contain:

- Production source code
- Runtime configuration
- Build output
- Generated assets
- Application logic

---

# Change Policy

Documentation in this directory represents the official project specification.

Any modification should:

1. Preserve consistency across all related documents.
2. Maintain compatibility with the established design system and architecture.
3. Be reviewed before implementation when it affects multiple specifications.

---

# Audience

This folder is intended for:

- Frontend Developers
- UI Engineers
- Designers
- Technical Writers
- Project Maintainers
- AI Coding Assistants

---

# Directory Status

```
Project Documentation

Status

Official
Maintained
Implementation Ready
```
---

# Implementation Status

The production implementation now lives at the repository root using the frozen Astro architecture. The `project/` HTML files remain reference prototypes only. YGit-specific specifications in `01` through `05` override the general Vib Tools PDF wherever exact values differ.
