# ৫৩. Official UI Framework

Status

```
Frozen
```

---

## Official Framework

```
Astro
```

Astro হবে `schema.ygit.dev`-এর একমাত্র Official Frontend Framework।

নতুন Page, Component এবং Feature Astro-এর উপর ভিত্তি করেই তৈরি করা হবে।

---

## Why Astro

Astro নির্বাচন করার কারণ:

- Documentation First Architecture
- Static Site Generation (SSG)
- Excellent Performance
- Minimal JavaScript
- SEO Friendly
- Markdown & MDX Native Support
- TypeScript Support
- Component-based Architecture
- GitHub Friendly
- Cloudflare Pages Friendly
- Long-term Maintainability

---

## Official Technology Stack

```
Astro

↓

Tailwind CSS

↓

TypeScript

↓

MDX

↓

Pagefind

↓

Shiki

↓

Lucide Icons

↓

Cloudflare Pages
```

---

# ৫৪. Framework Standards

## Astro

Role

```
Application Framework
```

---

## Tailwind CSS

Role

```
Official UI Styling System
```

---

## TypeScript

Role

```
Default Language
```

JavaScript নতুন Code-এর জন্য ব্যবহার করা হবে না, প্রয়োজন না হলে।

---

## MDX

Role

```
Documentation Content
```

Documentation Pages MDX Format অনুসরণ করবে।

---

## Pagefind

Role

```
Official Search Engine
```

Local

Static

Self-hosted

---

## Shiki

Role

```
Syntax Highlight
```

JSON

YAML

TypeScript

Bash

Shell

Markdown

---

## Lucide

Role

```
Official Icon Library
```

শুধুমাত্র Outline Style Icon ব্যবহার করা হবে।

---

# ৫৫. Astro Project Structure

```text
schema.ygit.dev/

src/

├── components/
├── layouts/
├── pages/
├── content/
├── styles/
├── lib/
├── utils/
├── assets/

public/

astro.config.mjs

tailwind.config.ts

tsconfig.json

package.json
```

---

# ৫৬. Component Rules

সব UI Component

```
src/components/
```

ফোল্ডারে থাকবে।

উদাহরণ

```text
Header

Footer

Sidebar

SearchBox

Breadcrumb

Card

Badge

Button

Table

CodeBlock

Pagination

SchemaCard

SchemaTable

VersionBadge
```

---

# ৫৭. Layout Rules

সব Page Layout

```
src/layouts/
```

ফোল্ডারে থাকবে।

Official Layout

```text
MainLayout

DocumentationLayout

SearchLayout

MobileLayout
```

---

# ৫৮. Styling Rules

Global CSS শুধুমাত্র নিচের কাজের জন্য ব্যবহৃত হবে:

- CSS Variables
- Font Import
- Reset
- Base Typography
- Theme Tokens

Component Styling-এর জন্য Tailwind CSS Utility Classes ব্যবহার করা হবে।

---

# ৫৯. Deployment Standard

Official Deployment Pipeline

```text
GitHub

↓

Cloudflare Pages

↓

schema.ygit.dev
```

GitHub-এ Push হলেই Cloudflare Pages স্বয়ংক্রিয়ভাবে Build এবং Deploy করবে।

---

# ৬০. Frozen Framework Rules

পরিবর্তন করা যাবে না:

- Frontend Framework → Astro
- Styling Framework → Tailwind CSS
- Language → TypeScript
- Documentation Format → MDX
- Search Engine → Pagefind
- Syntax Highlight → Shiki
- Icon Library → Lucide Icons
- Hosting → Cloudflare Pages

এই Framework Stack-ই `schema.ygit.dev`-এর Official এবং Long-term Supported Technology Stack হিসেবে গণ্য হবে।
