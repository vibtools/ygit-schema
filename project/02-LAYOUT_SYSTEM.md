# ১১. Layout System

## Layout Philosophy

schema.ygit.dev-এর Layout সম্পূর্ণভাবে **Documentation First** হবে।

Layout-এর প্রধান লক্ষ্য—

```
Navigation

↓

Reading

↓

Reference

↓

Validation
```

Visual decoration কখনো Layout-এর উদ্দেশ্য হবে না।

---

## Desktop Layout

Desktop-এর Standard Grid

```
┌──────────────────────────────────────────────────────────────┐
│ Header (60px)                                                │
├───────────────┬──────────────────────────────┬───────────────┤
│               │                              │               │
│ Left Sidebar  │     Main Content             │ Right Panel   │
│               │                              │               │
│               │                              │               │
└───────────────┴──────────────────────────────┴───────────────┘
```

---

## Standard Width

```
Maximum Width

1440px
```

Content কখনো Full Width হবে না।

---

## Desktop Columns

| Area | Width |
|-------|------:|
| Left Sidebar | 240px |
| Main Content | Flexible |
| Right Panel | 260–280px |

---

## Mobile Layout

```
Header

↓

Content

↓

Bottom Navigation
```

Sidebar Mobile-এ Overlay Drawer হবে।

---

## Page Padding

Desktop

```
20px
```

Mobile

```
16px
```

---

## Content Width

Documentation Content

```
Maximum

760–820px
```

এর বেশি লাইন লম্বা করা যাবে না।

---

# ১২. Header

## Header Height

```
60px
```

Mobile

```
56px
```

---

## Header Structure

```
Logo

↓

Primary Navigation

↓

Utility Area
```

---

Example

```
┌─────────────────────────────────────────────┐

schema.ygit.dev

Schemas

Documentation

Examples

Versions

Search

GitHub

└─────────────────────────────────────────────┘
```

---

## Header Rules

Header সবসময়

```
Sticky
```

হবে।

---

Background

```
#0D1117
```

---

Border

```
1px

#30363D
```

---

Shadow

```
Not Allowed
```

---

Header Content

Vertical Center

---

Logo

Left aligned

---

Search

Right aligned

---

Navigation

Center

---

# ১৩. Sidebar

Sidebar Documentation Website-এর সবচেয়ে গুরুত্বপূর্ণ অংশ।

---

Width

```
240px
```

---

Sidebar Position

```
Sticky
```

---

Sidebar Structure

```
Overview

Reference

Examples

Validation

Resources
```

---

Group Title

```
11px

Uppercase
```

---

Menu Item

```
14px
```

---

Active Menu

```
Background

#21262D

Accent

#38BDF8
```

---

Hover

```
Surface Hover
```

---

Indentation

Nested Menu

```
16px
```

---

Sidebar Scroll

Independent Scroll

---

Sidebar Rules

সবসময় Visible থাকবে Desktop-এ।

---

# ১৪. Navigation

Navigation Style

```
Simple

Flat

Compact
```

---

Navigation Font

```
13px

Weight 500
```

---

Spacing

```
20–24px
```

---

Active Navigation

```
Accent Color
```

---

Inactive

```
Muted Text
```

---

Navigation Animation

```
100–150ms
```

---

Dropdown

Minimal

Border Only

---

Mega Menu

```
Not Allowed
```

---

# ১৫. Breadcrumb

সব Documentation Page-এ Breadcrumb থাকবে।

Example

```
Documentation

/

Reference

/

Project

/

Metadata
```

---

Font

```
12px
```

---

Color

```
Muted
```

---

Clickable

Yes

---

# ১৬. Search Bar

Search Position

```
Header

or

Top Content
```

---

Search Height

```
40px
```

---

Placeholder

```
Search schemas, docs, examples...
```

---

Border

```
1px
```

---

Search Result

Compact List

---

# ১৭. Right Panel (Table of Contents)

Desktop Documentation Page-এ Right Panel থাকবে।

---

Width

```
260–280px
```

---

Content

```
On This Page

↓

Section Links
```

---

Sticky

```
Yes
```

---

Font

```
13px
```

---

Active Section

Accent Color

---

Mobile

Hidden

---

# ১৮. Footer

Footer হবে অত্যন্ত Minimal।

---

Structure

```
Logo

↓

Links

↓

Copyright
```

---

Example

```
schema.ygit.dev

Documentation

Schemas

Examples

GitHub

License

MIT
```

---

Footer Background

```
#0D1117
```

---

Border Top

```
1px

#30363D
```

---

Padding

```
24px
```

---

Text

```
13px
```

---

Footer Links

Muted

Hover করলে Accent Color হবে।

---

# ১৯. Layout Spacing

## Vertical Rhythm

Section Gap

```
24px
```

---

Card Gap

```
16px
```

---

Paragraph Gap

```
12px
```

---

Heading Gap

```
16px
```

---

Component Gap

```
16px
```

---

Grid Gap

Desktop

```
20px
```

---

Mobile

```
16px
```

---

# ২০. Frozen Layout Rules

নিচের Layout Rule-গুলো অপরিবর্তিত থাকবে।

- সর্বোচ্চ Layout Width: **1440px**
- Header: **60px** (Mobile: **56px**)
- Left Sidebar: **240px**
- Right Panel: **260–280px**
- Documentation Content Width: **760–820px**
- Desktop: **Three-column layout**
- Mobile: **Single-column layout**
- Header এবং Sidebar Sticky থাকবে।
- Sidebar Desktop-এ Visible, Mobile-এ Drawer হবে।
- Footer সর্বদা Minimal থাকবে।
- Shadow-এর পরিবর্তে **1px Border** ব্যবহার করা হবে।
- Navigation Compact থাকবে; Mega Menu ব্যবহার করা হবে না।
- Search Bar, Breadcrumb এবং Right-side Table of Contents Documentation Page-এর Standard Layout-এর অংশ হবে।
- Layout সর্বদা Documentation First নীতি অনুসরণ করবে।
```