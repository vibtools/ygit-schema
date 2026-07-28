# ৪৭. Responsive Rules

## Responsive Philosophy

Responsive Design-এর লক্ষ্য শুধু Screen ছোট করা নয়।

সব Screen-এ একই Developer Experience বজায় রাখা।

```
Desktop

↓

Tablet

↓

Mobile

↓

Same Experience
```

---

## Breakpoints

### Mobile

```
0 — 767px
```

---

### Tablet

```
768 — 1023px
```

---

### Desktop

```
1024px+
```

---

### Large Desktop

```
1440px+
```

---

## Layout Behavior

### Desktop

```
Header

↓

Sidebar

↓

Content

↓

Right TOC
```

---

### Tablet

```
Header

↓

Sidebar (Optional Drawer)

↓

Content
```

Right TOC Optional

---

### Mobile

```
Header

↓

Content

↓

Bottom Navigation
```

---

## Responsive Rules

Desktop

```
3 Columns
```

Tablet

```
2 Columns
```

Mobile

```
1 Column
```

---

## Cards

Desktop

```
3 Cards / Row
```

Tablet

```
2 Cards
```

Mobile

```
1 Card
```

---

## Tables

Desktop

Normal Table

---

Mobile

```
Horizontal Scroll
```

Allowed

---

## Sidebar

Desktop

Visible

---

Tablet

Collapsible

---

Mobile

Drawer

---

## Right TOC

Desktop

Visible

---

Tablet

Optional

---

Mobile

Hidden

---

## Images

```
max-width:100%
height:auto
```

---

## Responsive Typography

Typography Scale পরিবর্তন হবে না।

শুধু Layout পরিবর্তন হবে।

---

# ৪৮. Accessibility

## Goal

Documentation সবাই যেন ব্যবহার করতে পারে।

---

## Minimum Contrast

WCAG AA অনুসরণ করা হবে।

---

## Keyboard Support

সব Interactive Component

Keyboard Accessible

---

## Focus State

```
2px Outline

Accent Color
```

---

## Buttons

Keyboard Accessible

---

## Links

Underline on Hover

---

## Images

সব Image-এ

```
alt
```

থাকবে।

---

## Icons

Decorative হলে

```
aria-hidden="true"
```

---

## Forms

সব Input-এর Label থাকবে।

---

## Error Message

Text + Color

শুধু Color ব্যবহার করা যাবে না।

---

## Minimum Touch Area

```
44px
```

---

## Zoom

200%

Support Required

---

## Motion

Reduce Motion Support থাকবে।

---

# ৪৯. Motion

## Philosophy

Motion থাকবে।

Animation থাকবে।

কিন্তু Attention নেওয়ার জন্য নয়।

Feedback দেওয়ার জন্য।

---

## Duration

Fast

```
100ms
```

Normal

```
150ms
```

Slow

```
200ms
```

---

## Allowed

- Hover
- Focus
- Active
- Drawer
- Dropdown
- Fade
- Skeleton

---

## Not Allowed

- Bounce
- Elastic
- Heavy Scale
- Long Animation
- Parallax
- Floating Cards
- Auto Moving UI

---

## Hover

Background Change

Border Change

---

## Page Transition

Fade Only

---

## Loading

Skeleton

Spinner

Minimal

---

# ৫০. Design Tokens

## Colors

```css
--bg:#0B0F17;
--surface:#161B22;
--surface-hover:#21262D;
--border:#30363D;

--primary:#2563EB;
--accent:#38BDF8;

--success:#22C55E;
--warning:#F59E0B;
--danger:#EF4444;

--text:#F8FAFC;
--text-secondary:#8B949E;
```

---

## Typography

```css
--font-ui:"Inter",sans-serif;

--font-code:"JetBrains Mono",monospace;
```

---

## Font Size

```css
--text-xs:11px;

--text-sm:12px;

--text-md:13px;

--text-base:14px;

--text-h3:16px;

--text-h2:18px;

--text-h1:24px;
```

---

## Radius

```css
--radius-sm:8px;

--radius-md:10px;

--radius-lg:12px;
```

---

## Spacing

```css
--space-1:4px;

--space-2:8px;

--space-3:12px;

--space-4:16px;

--space-5:20px;

--space-6:24px;

--space-7:32px;
```

---

## Border

```css
--border-width:1px;
```

---

## Layout

```css
--header-height:60px;

--header-mobile:56px;

--sidebar-width:240px;

--toc-width:280px;

--content-width:820px;

--page-width:1440px;
```

---

## Shadow

```css
None
```

---

# ৫১. AI Handoff

যেকোনো AI (ChatGPT, Claude, Gemini, Copilot, Cursor ইত্যাদি) যখন `schema.ygit.dev`-এর UI তৈরি করবে, তখন নিচের নিয়মগুলো বাধ্যতামূলকভাবে অনুসরণ করবে।

## Core Rules

- Documentation First
- Developer First
- Minimal UI
- Flat Design
- Border Based Layout
- Compact Typography
- Dark Theme Only

---

## Never Change

AI কখনো পরিবর্তন করবে না—

- Color Palette
- Typography
- Font Family
- Font Size
- Layout Structure
- Component Style
- Navigation Pattern
- Responsive Rules

---

## Never Add

AI নিজে থেকে যোগ করবে না—

- Glassmorphism
- Large Hero
- Gradient Background
- Heavy Shadow
- Fancy Animation
- Marketing Banner
- Auto Carousel
- Decorative Graphics
- Random Colors
- New Typography Scale

---

## Always Preserve

- Header
- Sidebar
- Footer
- Cards
- Buttons
- Code Blocks
- Search
- Tables
- Design Tokens
- Spacing System

---

## Output Requirements

যেকোনো Generated UI অবশ্যই—

- Responsive
- Accessible
- Semantic HTML
- CSS Variable Based
- Production Ready
- Consistent with Official Design System

---

# ৫২. Freeze Checklist

## Branding

- [x] Brand Identity Frozen
- [x] Design Philosophy Frozen

---

## Visual System

- [x] Color System Frozen
- [x] Typography Frozen
- [x] Font Size Frozen
- [x] Spacing Frozen
- [x] Border System Frozen

---

## Layout

- [x] Header Frozen
- [x] Sidebar Frozen
- [x] Navigation Frozen
- [x] Footer Frozen
- [x] Responsive Layout Frozen

---

## Components

- [x] Buttons Frozen
- [x] Cards Frozen
- [x] Forms Frozen
- [x] Tables Frozen
- [x] Search Frozen
- [x] Badges Frozen
- [x] Code Blocks Frozen

---

## Pages

- [x] Home Template Frozen
- [x] Schema Details Frozen
- [x] Documentation Frozen
- [x] Search Results Frozen
- [x] Mobile Layout Frozen

---

## Engineering

- [x] Design Tokens Frozen
- [x] CSS Variables Frozen
- [x] Accessibility Rules Frozen
- [x] Motion Rules Frozen

---

## Final Rule

`schema.ygit.dev`-এর UI উন্নত, সম্প্রসারিত বা নতুন Page যোগ করা যেতে পারে, তবে **Official Design System**-এর নিচের বিষয়গুলো পরিবর্তন করা যাবে না:

- Brand Identity
- Design Philosophy
- Color Palette
- Typography
- Font Scale
- Layout Pattern
- Component Library
- Responsive Behavior
- Accessibility Standards
- Design Tokens

নতুন Feature বা Component যোগ হলেও এই Specification-ই হবে একমাত্র Official Reference।