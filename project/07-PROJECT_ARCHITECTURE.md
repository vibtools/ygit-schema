# PROJECT_ARCHITECTURE.md

# schema.ygit.dev
## Project Architecture Specification

Version: 1.0

Status: **Frozen**

---

# ১. Purpose

এই Document `schema.ygit.dev`-এর Official Project Architecture নির্ধারণ করে।

এই Architecture-এর লক্ষ্য:

- Developer Friendly
- Scalable
- Maintainable
- Predictable
- Modular
- Component Based

---

# ২. Architecture Philosophy

Project Structure হবে

```
Feature Based

+

Component Based

+

Documentation First
```

---

Core Principles

- Single Responsibility
- Reusable Components
- Clear Folder Structure
- No Duplicate Code
- Simple Import System
- Predictable File Naming

---

# ৩. Root Directory

```text
schema.ygit.dev/

.github/

.vscode/

public/

src/

package.json

astro.config.mjs

tailwind.config.ts

tsconfig.json

README.md

LICENSE
```

---

# ৪. Source Structure

```text
src/

assets/

components/

content/

data/

layouts/

lib/

pages/

services/

styles/

types/

utils/

constants/
```

---

# ৫. Folder Responsibilities

## assets/

Static UI Assets

```
images

icons

logos

illustrations
```

---

## components/

Reusable UI Components

সব UI Component এখানে থাকবে।

---

## content/

Documentation Content

```
docs/

schemas/

guides/

faq/
```

সব Documentation MDX হবে।

---

## data/

Static JSON Data

Example

```
versions.json

navigation.json

schema-list.json
```

---

## layouts/

সব Layout

Example

```
MainLayout

DocumentationLayout

SearchLayout

MobileLayout
```

---

## lib/

Third-party Library Wrappers

Example

```
pagefind

shiki

markdown
```

---

## pages/

Astro Pages

Example

```
index.astro

schemas/

docs/

search/

404.astro
```

---

## services/

Business Logic

Example

```
schema.service.ts

search.service.ts
```

---

## styles/

Global Styling

Only

```
global.css

tokens.css

fonts.css
```

---

## types/

TypeScript Types

Example

```
schema.ts

navigation.ts

version.ts
```

---

## utils/

Utility Functions

Example

```
formatDate()

slugify()

capitalize()
```

---

## constants/

Application Constants

Example

```
routes.ts

colors.ts

config.ts
```

---

# ৬. Component Architecture

```text
components/

layout/

navigation/

buttons/

cards/

forms/

search/

tables/

badges/

code/

schema/

documentation/

common/
```

---

# ৭. Layout Components

```text
Header

Footer

Sidebar

TopNavigation

BottomNavigation

RightTOC
```

---

# ৮. Documentation Components

```text
Breadcrumb

CodeBlock

Callout

PropertyTable

VersionBadge

SchemaInfo

PageHeader
```

---

# ৯. Common Components

```text
Button

Card

Badge

Container

Divider

Spinner

EmptyState

Pagination
```

---

# ১০. Search Components

```text
SearchBox

SearchResult

SearchFilters

SearchSummary
```

---

# ১১. Naming Convention

Component

```text
Header.astro
```

---

Type

```text
Header.types.ts
```

---

Utility

```text
header.utils.ts
```

---

Constant

```text
header.constants.ts
```

---

Style

Component-level CSS File ব্যবহার করা হবে না।

Tailwind Utility ব্যবহার করা হবে।

---

# ১২. File Naming Rules

Components

```
PascalCase
```

Example

```text
SchemaCard.astro
```

---

Utilities

```
camelCase
```

Example

```text
slugify.ts
```

---

Constants

```
camelCase
```

Example

```text
routes.ts
```

---

Types

```
camelCase
```

Example

```text
schema.ts
```

---

Data

```
kebab-case
```

Example

```text
schema-list.json
```

---

# ১৩. Routing Structure

```text
/

schemas/

/schemas/[slug]

/docs/

/docs/getting-started

/docs/reference

/examples

/search

/changelog

/versions

/404
```

---

# ১৪. Content Structure

```text
content/

docs/

schemas/

examples/

faq/
```

---

Documentation

↓

MDX

---

Schema Examples

↓

JSON

---

# ১৫. Import Rules

Preferred

```ts
import Button from "@/components/common/Button";
```

Avoid

```ts
../../../components/Button
```

---

Alias

```
@
```

↓

src

---

# ১৬. Dependency Rules

pages

↓

layouts

↓

components

↓

utils

↓

constants

Dependency Flow একমুখী হবে।

Circular Dependency Allowed নয়।

---

# ১৭. State Management

বর্তমান Project-এ

Global State Library ব্যবহার করা হবে না।

প্রয়োজনে

- Astro State
- React Island State

শুধু নির্দিষ্ট Component-এ।

---

# ১৮. API Layer

বর্তমানে External API Required নয়।

Future

```
services/
```

ফোল্ডারে যোগ হবে।

---

# ১৯. Search Layer

```
Pagefind

↓

Search Service

↓

Search Components
```

---

# ২০. Content Flow

```text
MDX

↓

Layout

↓

Components

↓

Rendered Page
```

---

# ২১. Build Flow

```text
Content

↓

Astro

↓

Static HTML

↓

dist/

↓

Cloudflare Pages
```

---

# ২২. CSS Architecture

```text
tokens.css

↓

fonts.css

↓

global.css

↓

Tailwind Utilities
```

Custom CSS সর্বনিম্ন রাখা হবে।

---

# ২৩. Design Token Source

Single Source

```
tokens.css
```

সব Color, Radius, Font Size, Spacing এখান থেকে আসবে।

---

# ২৪. Public Assets

```text
public/

favicon

robots.txt

manifest.json

social images
```

---

# ২৫. Future Expansion

নতুন Feature যোগ হলে

নতুন Folder তৈরি করা যাবে।

কিন্তু Existing Structure পরিবর্তন করা যাবে না।

---

# ২৬. Forbidden

Allowed নয়

- Random Folder
- Duplicate Component
- Deep Nested Folder (>3 levels)
- Circular Import
- Inline CSS
- Multiple Global CSS Files
- Component Logic Inside Pages

---

# ২৭. Architecture Principles

- Pages শুধুমাত্র Page Composition করবে।
- Layout শুধুমাত্র Page Structure নিয়ন্ত্রণ করবে।
- Components শুধুমাত্র UI Render করবে।
- Services শুধুমাত্র Business Logic পরিচালনা করবে।
- Utils শুধুমাত্র Helper Function রাখবে।
- Constants শুধুমাত্র Static Value রাখবে।
- Types শুধুমাত্র Type Definition রাখবে।
- Content শুধুমাত্র Documentation ও Static Content রাখবে।

---

# ২৮. Frozen Architecture Rules

নিচের বিষয়গুলো পরিবর্তন করা যাবে না—

- Frontend Framework → Astro
- Root Source Folder → `src/`
- Documentation → `src/content/`
- Components → `src/components/`
- Layouts → `src/layouts/`
- Pages → `src/pages/`
- Services → `src/services/`
- Utilities → `src/utils/`
- Types → `src/types/`
- Constants → `src/constants/`
- Static Assets → `public/`
- Global Styling → `src/styles/`
- Import Alias → `@`
- Component Naming → PascalCase
- Utility Naming → camelCase
- Documentation Format → MDX
- Static Build Output → `dist/`

---

# Architecture Freeze Status

```
Project Architecture

Status

✅ Frozen
```