# ২১. Components

Components Design Philosophy

```
Simple

Compact

Consistent

Developer First
```

---

প্রতিটি Component হবে—

- Flat
- Predictable
- Border Based
- Documentation Friendly

---

# ২২. Buttons

## Primary Button

Usage

- Download Schema
- View JSON
- Validate
- Submit

Background

```
#2563EB
```

Text

```
#FFFFFF
```

Border

```
None
```

Font

```
14px

Weight 600
```

Height

```
40px
```

Border Radius

```
8px
```

Hover

```
Brightness +5%
```

---

## Secondary Button

Background

```
Transparent
```

Border

```
1px

#30363D
```

Text

Primary Text

---

## Ghost Button

Background

Transparent

Border

None

Hover

Surface Hover

---

## Small Button

Height

```
32px
```

Font

```
13px
```

---

## Large Button

Height

```
44px
```

Font

```
14px
```

---

## Button Rules

Allowed

- Icon + Text
- Text Only

Not Allowed

- Gradient
- Glow
- Heavy Shadow
- Rounded Pill Style

---

# ২৩. Cards

Card হচ্ছে Primary Container।

---

Background

```
#161B22
```

Border

```
1px

#30363D
```

Radius

```
12px
```

Padding

```
16px
```

Desktop Large Card

```
20px
```

---

Shadow

```
None
```

---

Hover

```
Background

↓

#21262D
```

---

Card Types

- Information Card
- Schema Card
- Documentation Card
- Search Result Card
- Metadata Card

---

Card Header

```
16px

Weight 600
```

---

Card Content

```
14px
```

---

# ২৪. Tables

Tables Documentation-এর জন্য Optimize করা হবে।

---

Header

Background

```
Transparent
```

---

Border Bottom

```
1px

#30363D
```

---

Header Font

```
12px

Weight 600
```

---

Body Font

```
14px
```

---

Row Height

```
44px
```

---

Hover

```
#21262D
```

---

Alignment

Left

---

Numeric

Right

---

Allowed

- Property Table
- Version Table
- Compatibility Table

---

# ২৫. Forms

Input Background

```
#0D1117
```

Border

```
1px

#30363D
```

Height

```
40px
```

Radius

```
8px
```

Font

```
14px
```

---

Focus

Border

```
#38BDF8
```

---

Placeholder

```
#8B949E
```

---

Label

```
13px

Weight 500
```

---

Textarea

Minimum Height

```
120px
```

---

Select

Input-এর Style Follow করবে।

---

Checkbox

Square

---

Switch

Minimal

---

Validation

Error Border

```
#EF4444
```

---

Success Border

```
#22C55E
```

---

# ২৬. Search

Search Bar Height

```
40px
```

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

Font

```
14px
```

---

Placeholder

```
Search schemas, docs, examples...
```

---

Search Result Card

Padding

```
18px
```

---

Result Title

```
18px

Weight 600
```

---

Result Path

```
12px

JetBrains Mono

Accent
```

---

Result Description

```
14px
```

---

Search Summary

```
13px
```

---

# ২৭. Badges

Badge Height

```
22px
```

Padding

```
3px 8px
```

Radius

```
999px
```

Font

```
11px

Weight 600
```

---

Stable

```
Background

#13321D

Text

#22C55E
```

---

Beta

```
Background

#3B2A12

Text

#F59E0B
```

---

Deprecated

```
Background

#341414

Text

#EF4444
```

---

Draft

```
Background

#1A2433

Text

#38BDF8
```

---

Version Badge

Monospace Allowed

---

# ২৮. Code Blocks

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

Radius

```
10px
```

---

Padding

```
16px
```

---

Font

```
JetBrains Mono
```

---

Size

```
13px
```

---

Line Height

```
1.6
```

---

Horizontal Scroll

Allowed

---

Syntax Highlight

Minimal

---

Supported

- JSON
- YAML
- Bash
- Shell
- JavaScript
- TypeScript

---

Copy Button

Top Right

---

# ২৯. Links

Default

```
#38BDF8
```

---

Hover

Underline

---

Visited

Same Color

---

External Link

Icon Allowed

---

# ৩০. Status Components

Status Card

Border Only

---

Success

```
#22C55E
```

---

Warning

```
#F59E0B
```

---

Error

```
#EF4444
```

---

Info

```
#38BDF8
```

---

Icons

Outline Only

---

# ৩১. Pagination

Height

```
36px
```

---

Current Page

```
#2563EB
```

---

Inactive

Border Only

---

Font

```
13px
```

---

# ৩২. Empty State

Structure

```
Icon

↓

Title

↓

Description

↓

Action
```

---

Illustration

Optional

---

Text Alignment

Center

---

# ৩৩. Loading State

Skeleton UI ব্যবহার করা হবে।

---

Spinner

Minimal

---

Animation

Subtle

---

Duration

```
1s
```

Loop

---

# ৩৪. Frozen Component Rules

- সব Component Flat হবে।
- Shadow ব্যবহার করা যাবে না।
- সব Container-এ `1px #30363D` Border থাকবে।
- Primary Button শুধুমাত্র `#2563EB` ব্যবহার করবে।
- Links শুধুমাত্র `#38BDF8` ব্যবহার করবে।
- Border Radius:
  - Button → **8px**
  - Input → **8px**
  - Code Block → **10px**
  - Card → **12px**
- Base UI Font → **Inter**
- Code Font → **JetBrains Mono**
- Base Text → **14px**
- Metadata → **12px**
- Badge → **11px**
- Code → **13px**
- সকল Hover State-এ Surface Hover (`#21262D`) ব্যবহার হবে।
- Components সর্বদা Compact, Consistent এবং Documentation First নীতি অনুসরণ করবে।