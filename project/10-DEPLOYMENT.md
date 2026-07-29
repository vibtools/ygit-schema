# GitHub → Cloudflare Pages Deployment Specification

Version: 1.0

Status: **Frozen**

Applies To

- schema.ygit.dev
- Future YGit Documentation Websites
- Static Developer Portal
- Schema Registry

---

# ১. Deployment Philosophy

Deployment System হবে—

```
Simple

Reliable

Automatic

Git Based

Zero Manual Deployment
```

Developer কখনো Manual Upload করবে না।

Production সর্বদা Git Repository থেকে Build হবে।

---

# ২. Official Deployment Flow

```
Developer

↓

Git Commit

↓

GitHub Repository

↓

GitHub Branch

↓

Cloudflare Pages

↓

Automatic Build

↓

Automatic Deploy

↓

schema.ygit.dev
```

---

# ৩. Official Repository

Official Source

```
GitHub
```

GitHub হবে একমাত্র Source of Truth।

Production Server-এ Code Edit করা যাবে না।

---

# ৪. Branch Strategy

Official Branch

```
main
```

Development Branch

```
develop
```

Feature Branch

```
feature/*
```

Bug Fix

```
fix/*
```

Hotfix

```
hotfix/*
```

Release

```
release/*
```

---

# ৫. Production Rules

Production Deploy হবে শুধুমাত্র

```
main
```

Branch থেকে।

---

Develop Branch

Deploy হবে Preview Environment-এ।

---

Feature Branch

Deploy হবে Preview URL-এ।

---

# ৬. Cloudflare Pages

Official Hosting

```
Cloudflare Pages
```

Deployment Type

```
Git Integration
```

Manual Upload

```
Not Allowed
```

---

# ৭. Build Configuration

Framework

```
Astro
```

---

Build Command

```bash
npm run build
```

---

Output Directory

```text
dist
```

---

Root Directory

```text
/
```

---

Node Version

```
LTS
```

Latest Stable LTS Version ব্যবহার করা হবে।

---

Package Manager

```
npm
```

---

# ৮. Git Workflow

```
Create Feature

↓

Commit

↓

Push

↓

Pull Request

↓

Review

↓

Merge

↓

Auto Deploy
```

---

# ৯. Commit Convention

Official Format

```
feat:

fix:

docs:

style:

refactor:

perf:

build:

ci:

test:

chore:
```

Examples

```text
feat: add schema search

fix: sidebar scrolling

docs: update getting started

refactor: optimize schema cards

build: update astro config
```

---

# ১০. Pull Request Rules

Every Change

↓

Pull Request

↓

Review

↓

Merge

↓

Deploy

Direct Push to Production

```
Not Recommended
```

---

# ১১. Build Rules

Build অবশ্যই

```
Production Build
```

হবে।

Development Build Deploy করা যাবে না।

---

Build Fail করলে

Deployment Cancel হবে।

---

# ১২. Preview Deployment

Every Pull Request

↓

Preview URL

Example

```text
feature-search.pages.dev
```

Production Domain ব্যবহার করা হবে না।

---

# ১৩. Production Deployment

Only

```
main
```

↓

Deploy

↓

schema.ygit.dev

---

# ১৪. Environment Variables

Production

Cloudflare Pages Environment Variables

Development

Separate Variables

Secrets

GitHub Repository-তে Hardcode করা যাবে না।

---

# ১৫. Repository Rules

Repository Structure পরিবর্তন করা যাবে।

কিন্তু

```
src

public

package.json

astro.config

tailwind.config

tsconfig
```

Official থাকবে।

---

# ১৬. Build Validation

Deploy-এর আগে

Automatic

- Install Dependencies
- Type Check
- Build
- Output Validation

সব সফল হতে হবে।

---

# ১৭. GitHub Integration

Repository

↓

Connected

↓

Cloudflare Pages

↓

Auto Build

↓

Auto Deploy

Webhook Manual Configure করার প্রয়োজন নেই।

Git Integration ব্যবহার করা হবে।

---

# ১৮. Deployment Frequency

Every Push

↓

Automatic Build

Every Merge

↓

Automatic Production Deployment

---

# ১৯. Rollback Strategy

যদি Production-এ সমস্যা হয়

↓

Cloudflare Pages

↓

Previous Deployment

↓

Rollback

Rollback Manual Upload দিয়ে করা যাবে না।

---

# ২০. Deployment Security

Production Branch Protection

Recommended

---

Force Push

Production Branch-এ

Avoid

---

Secrets

GitHub Secret

↓

Cloudflare Environment Variables

---

# ২১. CI/CD Pipeline

```
Git Push

↓

Install

↓

Build

↓

Validate

↓

Deploy

↓

Production
```

Deployment Pipeline-এ Manual Step থাকবে না।

---

# ২২. GitHub Actions Policy

GitHub Actions ব্যবহার করা যাবে—

- Lint
- Type Check
- Build Validation
- Test
- Preview Quality Check

Production Deployment GitHub Actions দিয়ে করা হবে না।

Production Deployment-এর দায়িত্ব Cloudflare Pages Git Integration-এর।

---

# ২৩. Official CI Responsibilities

GitHub Actions

Responsible For

- ESLint
- TypeScript Check
- Markdown Validation
- Link Validation
- Build Test
- Component Validation

Cloudflare Pages

Responsible For

- Production Build
- Production Deploy
- Preview Deploy

---

# ২৪. Deployment Flow Diagram

```text
Developer

↓

Git Commit

↓

GitHub

↓

Pull Request

↓

Merge to main

↓

Cloudflare Pages

↓

npm install

↓

npm run build

↓

dist/

↓

Deploy

↓

schema.ygit.dev
```

---

# ২৫. Frozen Deployment Rules

নিচের বিষয়গুলো পরিবর্তন করা যাবে না—

- Source Repository → GitHub
- Frontend Framework → Astro
- Build Command → `npm run build`
- Output Directory → `dist`
- Hosting → Cloudflare Pages
- Production Branch → `main`
- Preview Deployment → Enabled
- Git Integration → Required
- Automatic Deployment → Required
- Manual Upload → Not Allowed
- GitHub হবে একমাত্র Source of Truth
- Production Server-এ সরাসরি Code Edit করা যাবে না
- Build ব্যর্থ হলে Deploy হবে না
- GitHub Actions শুধুমাত্র Validation/Quality Check-এর জন্য ব্যবহৃত হবে
- Production Deployment শুধুমাত্র Cloudflare Pages Git Integration-এর মাধ্যমে সম্পন্ন হবে

---

# Official Deployment Standard (Frozen)

```
Developer

↓

Git Commit

↓

GitHub Repository

↓

Pull Request

↓

Merge

↓

Cloudflare Pages

↓

Automatic Build

↓

Automatic Deploy

↓

schema.ygit.dev
```

**Status:** ✅ Frozen

এই Deployment Architecture-ই `schema.ygit.dev`-এর Official CI/CD Standard হিসেবে গণ্য হবে।
---

# Workflow File Clarification

`.github/workflows/deploy.yml` performs production build-readiness verification only. Cloudflare Pages Git integration remains the sole production deployment mechanism.
