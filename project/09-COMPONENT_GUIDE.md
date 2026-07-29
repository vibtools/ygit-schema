# COMPONENT_DEVELOPMENT_GUIDE.md

# schema.ygit.dev
## Official Component Development Rules

Version: 1.0

Status: **Frozen**

Applies To

- Astro Components
- Tailwind CSS
- TypeScript
- MDX Components

---

# ১. Purpose

এই Document `schema.ygit.dev`-এর সকল UI Component তৈরির Official Standard নির্ধারণ করে।

উদ্দেশ্য

- Consistent UI
- Reusable Components
- Predictable Structure
- Easy Maintenance
- Long-term Scalability

---

# ২. Component Philosophy

সব Component হবে

- Small
- Independent
- Reusable
- Predictable
- Stateless (যতটা সম্ভব)

---

Core Principle

```
One Component

↓

One Responsibility
```

---

# ৩. Component Categories

Official Categories

```text
Layout

Navigation

Documentation

Schema

Forms

Search

Tables

Cards

Buttons

Feedback

Common
```

---

# ৪. Folder Structure

প্রতিটি Component নিজের Folder-এ থাকবে।

Example

```text
components/

SchemaCard/

    SchemaCard.astro

    SchemaCard.types.ts

    index.ts
```

---

Complex Component

```text
SearchBox/

    SearchBox.astro

    SearchBox.types.ts

    SearchBox.utils.ts

    index.ts
```

---

# ৫. Component Naming

সব Component

```
PascalCase
```

Example

```text
SchemaCard

SearchBox

VersionBadge

PropertyTable

CodeBlock
```

---

# ৬. File Naming

Component

```text
Button.astro
```

---

Types

```text
Button.types.ts
```

---

Utilities

```text
button.utils.ts
```

---

Constants

```text
button.constants.ts
```

---

Exports

```text
index.ts
```

---

# ৭. Export Rules

সব Component

```
index.ts
```

থেকে Export হবে।

Example

```ts
export { default } from './Button.astro';
```

---

# ৮. Component Size

Recommended

```
100–150 Lines
```

Maximum

```
250 Lines
```

এর বেশি হলে Component ভেঙে ফেলতে হবে।

---

# ৯. Props Rules

সব Props

Strongly Typed হবে।

Example

```ts
type ButtonProps = {
  label: string;
  variant?: 'primary' | 'secondary';
};
```

---

Props

Minimal হবে।

---

Unused Props Allowed নয়।

---

# ১০. Variants

Variant ব্যবহার করা হবে।

Example

```text
primary

secondary

ghost

danger

success
```

---

Boolean Props দিয়ে UI Control Avoid করতে হবে।

---

# ১১. Default Values

সব Optional Props-এর Default Value থাকবে।

Example

```ts
variant = 'primary'
```

---

# ১২. Component State

Default

```
Stateless
```

Preferred

---

State লাগলে

Local State ব্যবহার করা হবে।

---

Global State ব্যবহার করা হবে না।

---

# ১৩. Component Communication

Parent

↓

Props

↓

Child

---

Child

↓

Custom Event

↓

Parent

---

Sibling Component

Direct Communication করবে না।

---

# ১৪. Styling Rules

সব Styling

↓

Tailwind CSS

---

Inline Style

Allowed নয়।

---

Component CSS File

Avoid

---

Hardcoded Color

Allowed নয়।

---

সব Color

↓

Design Token

↓

Tailwind Theme

থেকে আসবে।

---

# ১৫. Responsive Rules

সব Component

Responsive হবে।

---

Desktop

Tablet

Mobile

Support Required

---

# ১৬. Accessibility

সব Interactive Component-এ

- Keyboard Support
- Focus Ring
- aria-label (যেখানে প্রয়োজন)
- Semantic HTML

Required

---

# ১৭. Buttons

সব Button

Official Variant ব্যবহার করবে।

---

Random Color

Allowed নয়।

---

Disabled State থাকবে।

---

Loading State থাকলে

Visual Feedback দিতে হবে।

---

# ১৮. Forms

সব Input

Label থাকবে।

---

Placeholder

Optional

---

Validation Message

Supported

---

Error State

Required

---

# ১৯. Tables

Responsive

Required

---

Overflow Support

Required

---

Header Fixed

Optional

---

# ২০. Cards

সব Card

Official Card Style ব্যবহার করবে।

- Radius
- Border
- Padding
- Background

Design Token থেকে আসবে।

---

# ২১. Icons

Official Library

```
Lucide
```

---

Random Icon Library

Allowed নয়।

---

# ২২. Animations

Only

- Hover
- Focus
- Fade
- Expand
- Collapse

Allowed

---

Bounce

Rotate

Flash

Elastic

Allowed নয়।

---

# ২৩. Composition

Complex Component

↓

Small Components

দিয়ে তৈরি হবে।

Example

```text
SearchPage

↓

SearchBox

↓

SearchFilters

↓

SearchSummary

↓

SearchResultCard
```

---

# ২৪. Reusability

Duplicate UI

Allowed নয়।

একই UI

↓

এক Component

↓

Multiple Use

---

# ২৫. Logic Rules

Business Logic

Component-এ থাকবে না।

---

Business Logic

↓

services/

অথবা

utils/

এ থাকবে।

---

# ২৬. Content Rules

Hardcoded Text

Avoid

---

Content

↓

MDX

↓

JSON

↓

Config

থেকে আসবে।

---

# ২৭. Error Handling

Broken Data

↓

Graceful UI

---

Empty State

Support Required

---

Loading State

Support Required

---

# ২৮. Performance

Lazy Load

যেখানে সম্ভব।

---

Heavy Component

Split করতে হবে।

---

Unnecessary Re-render

Avoid

---

# ২৯. Testing Checklist

নতুন Component তৈরি হলে—

- Responsive
- Accessibility
- Keyboard Navigation
- Dark Theme
- Empty State
- Error State
- Loading State
- Mobile Layout

সব Check করতে হবে।

---

# ৩০. Documentation

সব Public Component-এর জন্য

সংক্ষিপ্ত Description থাকবে।

Props Documentation

Recommended।

---

# ৩১. Forbidden

Allowed নয়—

- Inline CSS
- Hardcoded Color
- Hardcoded Font Size
- Duplicate Component
- Random Spacing
- Deep Component Nesting
- Business Logic Inside UI
- Multiple Responsibilities
- Unused Props
- Unused Imports
- Direct DOM Manipulation (যদি Astro-এর স্বাভাবিক পদ্ধতি যথেষ্ট হয়)

---

# ৩২. Official Component Library

```text
Layout

Header
Footer
Sidebar
TopNavigation
RightTOC

Navigation

Breadcrumb
Pagination

Buttons

Button
IconButton

Cards

Card
SchemaCard

Documentation

CodeBlock
Callout
PropertyTable
VersionBadge

Search

SearchBox
SearchFilters
SearchSummary
SearchResultCard

Forms

Input
Textarea
Select
Checkbox

Feedback

Alert
Spinner
EmptyState

Common

Badge
Divider
Container
```

---

# ৩৩. Frozen Component Rules

পরিবর্তন করা যাবে না—

- Component Framework → Astro
- Styling → Tailwind CSS
- Language → TypeScript
- Icon Library → Lucide
- Component Naming → PascalCase
- Folder Structure → One Component per Folder
- Export Pattern → `index.ts`
- Strongly Typed Props → Required
- Responsive Support → Required
- Accessibility → Required
- Design Token Usage → Required
- Reusable Component Architecture → Required
- Business Logic Outside UI → Required

---

# Component Development Status

```
Official Component Development Rules

Status

✅ Frozen
```
