# schema.ygit.dev
# Design System Specification

Version: 1.0
Status: Frozen
Applies to:
- schema.ygit.dev
- Future Schema Registry UI
- Documentation Portal
- Schema Browser
- Developer Portal

---

# ১. Brand Identity

## Product Name

```
schema.ygit.dev
```

Official Name

```
YGit Schema Registry
```

Short Name

```
Schema Registry
```

---

## Brand Purpose

schema.ygit.dev হচ্ছে YGit Ecosystem-এর Official Schema Registry।

এটি শুধুমাত্র একটি Website নয়।

এটি হবে—

- Official JSON Schema Registry
- Documentation Portal
- Schema Browser
- Developer Reference
- Version Registry
- Validation Reference

---

## Brand Personality

Brand personality সর্বদা হবে—

- Professional
- Technical
- Minimal
- Developer First
- Open Source
- Reliable
- Stable
- Fast
- Clean
- Engineering Focused

---

## Brand Keywords

```
Developer First

Open Source

Technical

Reliable

Stable

Professional

Minimal

Documentation

Registry

Validation
```

---

## Brand Experience

Website ব্যবহার করলে যেন অনুভূত হয়—

```
Official

Professional

Fast

Developer Friendly

Predictable

Consistent

Modern

Minimal
```

Marketing Website-এর অনুভূতি আসবে না।

---

# ২. Design Philosophy

schema.ygit.dev একটি Documentation Website।

Landing Page নয়।

---

Design Priority

```
Developer Experience

↓

Documentation

↓

Readability

↓

Navigation

↓

Consistency

↓

Branding
```

Branding কখনো Documentation-এর উপরে যাবে না।

---

Website-এর মূল উদ্দেশ্য

```
Find

↓

Read

↓

Understand

↓

Copy

↓

Validate
```

---

Website কখনো হবে না—

- Marketing Website
- SaaS Landing Page
- Startup Landing Page
- Animation Showcase
- Fancy Portfolio

---

Website হবে—

```
Developer Portal
```

---

# ৩. UI Philosophy

UI Design-এর মূল লক্ষ্য

```
কম Decoration

বেশি Information
```

---

প্রতিটি Screen-এর Rule

User যেন

```
৩ সেকেন্ডের মধ্যে

↓

যা খুঁজছে

↓

তা খুঁজে পায়।
```

---

Navigation

সবসময় পরিষ্কার হবে।

Hidden Navigation ব্যবহার করা যাবে না।

---

Spacing

Compact

Documentation Friendly

---

Content

Readable

Structured

Predictable

---

Typography

Readable > Stylish

---

Icons

Minimal

Outline

Technical

---

# ৪. Visual Style

Overall Style

```
GitHub Docs

+

JSON Schema Store

+

AsyncAPI Docs

+

Vib Tools
```

---

Visual Feel

```
Dark

Minimal

Technical

Calm

Professional
```

---

Cards

Flat

No Glass

No Blur

No Glow

No Heavy Shadow

---

Border

সব Component-এ Border থাকবে।

Border UI-এর Structure তৈরি করবে।

Shadow নয়।

---

# ৫. Color System

## Primary Interface Colors

| Token | Color | Usage |
|--------|--------|------|
| Background | `#0D1117` | Main Page |
| Deep Background | `#0B0F17` | Outer Canvas |
| Surface | `#161B22` | Card |
| Surface Muted | `#21262D` | Hover |
| Border | `#30363D` | Border |
| Text Primary | `#F8FAFC` | Main Text |
| Text Content | `#D8DEE9` | Body |
| Text Secondary | `#8B949E` | Metadata |
| Primary | `#2563EB` | Button |
| Accent | `#38BDF8` | Links |
| Success | `#22C55E` | Success |
| Warning | `#F59E0B` | Warning |
| Danger | `#EF4444` | Error |

এই palette Vib Tools Brand Specification-এর official interface color system অনুসরণ করবে।

---

## Color Distribution

```
80%

Background

Surface

Border

--------------

15%

Typography

--------------

5%

Accent
```

Accent Color কখনো UI দখল করবে না।

---

## Accent Usage

Allowed

- Active Menu
- Links
- Focus
- Technical Highlight
- Search Highlight

Not Allowed

- Large Background
- Card Background
- Hero Background
- Full Gradient Section

---

## Button Colors

Primary

```
Blue
```

Secondary

```
Surface
```

Ghost

```
Transparent
```

---

# ৬. Typography

## Primary Font

```
Inter
```

Usage

- Navigation
- Button
- Heading
- Body
- Table
- Documentation

---

## Code Font

```
JetBrains Mono
```

Usage

- JSON
- YAML
- Code
- Schema
- Path
- URL
- Version
- Terminal

এটি Vib Tools Brand Specification-এর typography নির্দেশনার সাথে সামঞ্জস্যপূর্ণ।

---

# ৭. Font Size Scale

## H1

```
24px

Weight 700
```

---

## H2

```
18px

Weight 600
```

---

## H3

```
16px

Weight 600
```

---

## Body

```
14px

Weight 400
```

---

## Navigation

```
13px

Weight 500
```

---

## Sidebar

```
14px

Weight 500
```

---

## Sidebar Group

```
11px

Uppercase
```

---

## Metadata

```
12px
```

---

## Badge

```
11px
```

---

## Table

Header

```
12px
```

Body

```
14px
```

---

## Code

```
13px
```

---

## Search Input

```
14px
```

---

## Button

```
13–14px

Weight 600
```

---

# ৮. Typography Rules

Heading

```
Bold

Compact

Short
```

---

Paragraph

```
Readable

Maximum

65–75 Characters
```

---

Documentation

Long paragraph ব্যবহার করা যাবে।

কিন্তু Line Width সীমাবদ্ধ থাকবে।

---

Code Block

সবসময়

JetBrains Mono

---

JSON

সবসময়

Monospace

---

Terminal

Monospace

---

Version Number

Monospace

---

Schema Path

Monospace

---

# ৯. Text Style

সব Text হবে—

```
Technical

Professional

Direct

Simple
```

---

Avoid

```
Amazing

Awesome

Best Ever

Revolutionary

Magic

Super Powerful

Next Generation
```

---

Preferred

```
Official

Stable

Reference

Documentation

Schema

Validation

Registry
```

---

# ১০. Frozen Design Principles

এই Design System-এর মূল নীতিগুলো অপরিবর্তিত থাকবে:

- Documentation আগে, Branding পরে।
- Dark-first interface বজায় থাকবে।
- Flat card + 1px border ব্যবহার করা হবে।
- Primary action শুধুমাত্র Blue (`#2563EB`)।
- Technical highlight শুধুমাত্র Cyan (`#38BDF8`)।
- Inter হবে UI font।
- JetBrains Mono হবে code font।
- Compact typography (H1: 24px, Body: 14px) বজায় থাকবে।
- Large hero, decorative animation, heavy shadow, glassmorphism বা marketing-style section ব্যবহার করা হবে না।
- পুরো Website একই visual language অনুসরণ করবে।
---

# Implementation Reference

The YGit-specific frozen values in this document take precedence over the general `Vib-Tools-Brand-Guidelines.pdf` when exact typography, focus, spacing, or container values differ.
