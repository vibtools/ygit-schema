# ৩৫. Page Templates

schema.ygit.dev-এর প্রতিটি Page একই Design System অনুসরণ করবে।

সমস্ত Page-এর Common Layout:

```
Header (Sticky)

↓

Content Area

↓

Footer
```

Desktop Documentation Layout

```
┌──────────────────────────────────────────────────────────────┐
│ Header                                                       │
├───────────────┬──────────────────────────────┬───────────────┤
│ Left Sidebar  │ Main Content                 │ Right Panel   │
└───────────────┴──────────────────────────────┴───────────────┘
```

---

# ৩৬. Home Page

## Purpose

Home Page-এর কাজ Marketing করা নয়।

Home Page হবে—

- Schema Discovery
- Quick Navigation
- Documentation Entry
- Version Access

---

## Layout

```
Header

↓

Hero

↓

Quick Actions

↓

Featured Schemas

↓

Documentation

↓

Latest Updates

↓

Footer
```

---

## Hero

Hero ছোট হবে।

Height

```
280–340px
```

---

Hero Content

```
Title

↓

Description

↓

Search

↓

Quick Buttons
```

---

Example

```
Official Schema Registry

Search Schemas...

[Browse Schemas]

[Documentation]
```

---

## Featured Schemas

Grid Layout

Desktop

```
3 Columns
```

---

Tablet

```
2 Columns
```

---

Mobile

```
1 Column
```

---

Schema Card

Contains

- Badge
- Schema Name
- Description
- Version
- Button

---

## Quick Actions

Cards

- Browse Schemas
- Documentation
- Examples
- GitHub

---

## Latest Updates

Simple Timeline

Not Blog Style

---

# ৩৭. Schema Details Page

## Purpose

একটি নির্দিষ্ট Schema-এর সম্পূর্ণ Reference দেখানো।

---

## Layout

```
Header

↓

Sidebar

↓

Schema Overview

↓

Properties

↓

Definitions

↓

Examples

↓

Related Links
```

---

Desktop

```
Sidebar

|

Content

|

Right TOC
```

---

Overview Card

Contains

- Badge
- Name
- Version
- Draft
- License
- Compatibility

---

Properties

Table

Columns

```
Name

Type

Required

Description
```

---

Definitions

Accordion অথবা Section

---

Example

Code Block

JSON

---

Download Area

Buttons

- Download Schema
- View Raw JSON

---

Right Panel

Contains

```
On This Page
```

---

# ৩৮. Documentation Page

## Purpose

Developer Guide

---

Layout

```
Header

↓

Sidebar

↓

Article

↓

Right TOC
```

---

Content Order

```
Breadcrumb

↓

Title

↓

Description

↓

Callout

↓

Section

↓

Code Example

↓

Next Steps
```

---

Sections

Multiple

---

Heading

Compact

---

Images

Optional

---

Tables

Allowed

---

Code Blocks

Frequently Used

---

Navigation

Previous

↓

Next

---

# ৩৯. Search Results Page

## Purpose

Schemas

Documentation

Examples

একসাথে Search করা।

---

Layout

```
Header

↓

Search Box

↓

Filter Sidebar

↓

Results

↓

Pagination
```

---

Search Area

Contains

```
Search Box

↓

Summary

↓

Filters
```

---

Search Result Card

Contains

- Badge
- Title
- Path
- Description
- Metadata

---

Metadata

Example

```
Schema

Version

Updated
```

---

Filters

- All
- Schemas
- Documentation
- Examples

---

Pagination

Bottom Center

---

No Result

Show

```
No Results Found
```

---

# ৪০. Mobile Layout

## Purpose

Desktop Experience-এর Simplified Version।

---

Layout

```
Header

↓

Search

↓

Content

↓

Bottom Navigation
```

---

Sidebar

Hidden

↓

Drawer

---

Header

Contains

```
Menu

Logo

Search
```

---

Cards

Full Width

---

Tables

Horizontal Scroll

Allowed

---

Right Panel

Hidden

---

Bottom Navigation

Items

- Home
- Schemas
- Docs
- Search

---

Touch Target

Minimum

```
44px
```

---

Spacing

```
16px
```

---

# ৪১. Shared Page Components

প্রতিটি Page-এ নিচের Component একই থাকবে।

- Header
- Footer
- Buttons
- Search
- Typography
- Cards
- Code Block
- Border
- Colors
- Links
- Badge

---

# ৪২. Page Hierarchy

```
Home

├── Schemas

│   ├── Schema Details

│   ├── Version

│   └── Download

│

├── Documentation

│   ├── Getting Started

│   ├── Reference

│   ├── Validation

│   ├── Examples

│   └── FAQ

│

├── Search

│

└── Mobile
```

---

# ৪৩. Navigation Flow

```
Home

↓

Browse Schemas

↓

Schema Details

↓

Documentation

↓

Examples

↓

Download
```

Search যেকোনো Page থেকে Access করা যাবে।

---

# ৪৪. Responsive Behavior

## Desktop

```
3 Column Layout
```

---

## Tablet

```
Sidebar

↓

Content
```

Right Panel Optional।

---

## Mobile

```
Single Column
```

---

Cards

100% Width

---

Navigation

Bottom Navigation

---

Search

Top

---

# ৪৫. Page Consistency Rules

সব Page-এ—

- একই Header
- একই Footer
- একই Typography
- একই Color Palette
- একই Button Style
- একই Card Style
- একই Search Style
- একই Border Style
- একই Code Block Style
- একই Hover Style

---

# ৪৬. Frozen Page Template Rules

- Home Page কখনো Marketing Landing Page হবে না।
- Hero Section সর্বদা Compact থাকবে।
- Schema Details Page-এ Properties Table এবং Download Action বাধ্যতামূলক।
- Documentation Page-এ Breadcrumb, Article Content এবং Right-side Table of Contents থাকবে।
- Search Results Page-এ Filter Sidebar, Search Summary এবং Pagination থাকবে।
- Mobile Layout সর্বদা Single-column হবে।
- Desktop-এ Documentation Layout Three-column (Sidebar + Content + TOC) বজায় থাকবে।
- Mobile-এ Sidebar Drawer হবে এবং Bottom Navigation ব্যবহার করা হবে।
- প্রতিটি Page একই Design System, Color, Typography, Spacing এবং Component Library অনুসরণ করবে।
- ভবিষ্যতে নতুন Page যোগ হলেও এই Template Structure এবং Layout Pattern পরিবর্তন করা হবে না।
