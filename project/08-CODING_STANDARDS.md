# CODING_STANDARDS.md

# schema.ygit.dev
## Official Coding Standards

Version: 1.0

Status: **Frozen**

Applies To

- Astro
- TypeScript
- Tailwind CSS
- MDX
- Cloudflare Pages

---

# ১. Philosophy

Code সর্বদা হবে—

- Simple
- Readable
- Predictable
- Maintainable
- Modular
- Reusable

---

Core Principle

```
Readability

>

Clever Code
```

---

Code এমন হবে যাতে

নতুন Developer

↓

৫ মিনিটে

↓

বুঝতে পারে।

---

# ২. Official Language

Frontend

```
TypeScript
```

---

Markup

```
Astro
```

---

Documentation

```
MDX
```

---

Styling

```
Tailwind CSS
```

---

# ৩. Code Style

Rule

```
Consistency

>

Personal Preference
```

---

সব Developer একই Style Follow করবে।

---

# ৪. Naming Convention

## Component

```
PascalCase
```

Example

```ts
SchemaCard

SearchBox

VersionBadge
```

---

## Function

```
camelCase
```

Example

```ts
formatDate()

getSchema()

createSlug()
```

---

## Variable

```
camelCase
```

Example

```ts
schemaName

currentVersion

isStable
```

---

## Constant

```
UPPER_SNAKE_CASE
```

Example

```ts
MAX_RESULTS

DEFAULT_LANGUAGE

SITE_NAME
```

---

## Type

```
PascalCase
```

Example

```ts
Schema

NavigationItem

VersionInfo
```

---

## Interface

Prefix ব্যবহার করা হবে না।

Good

```ts
interface Schema
```

Bad

```ts
interface ISchema
```

---

# ৫. Folder Naming

সব Folder

```
lowercase
```

Example

```text
components

layouts

content

services

utils
```

---

# ৬. File Naming

Components

```
PascalCase
```

```text
Header.astro

SchemaCard.astro
```

---

Utilities

```
camelCase
```

```text
formatDate.ts
```

---

Data

```
kebab-case
```

```text
schema-list.json
```

---

# ৭. Import Order

ক্রম হবে—

```ts
// Astro

// Third Party

// Components

// Layouts

// Services

// Utils

// Constants

// Types

// Styles
```

---

Alphabetical Import

Recommended

---

# ৮. Component Rules

একটি Component

↓

একটি Responsibility

---

Large Component Allowed নয়।

---

Reusable Component Preferred।

---

Maximum

```
250 Lines
```

Target

```
100–150 Lines
```

---

# ৯. Function Rules

একটি Function

↓

একটি কাজ করবে।

---

Target

```
20–40 Lines
```

---

Maximum

```
60 Lines
```

---

Function Name

Verb দিয়ে শুরু হবে।

Example

```ts
getSchema()

loadVersion()

formatDate()

validateManifest()
```

---

# ১০. TypeScript Rules

```
strict

Required
```

---

Avoid

```ts
any
```

---

Use

```ts
unknown
```

অথবা

Proper Types

---

সব Function-এর Return Type থাকবে।

Example

```ts
function getSchema(): Schema
```

---

# ১১. Props Rules

Props

Readonly

---

Optional Props

```
?
```

---

Default Value

স্পষ্টভাবে Declare করা হবে।

---

# ১২. Error Handling

Never

```ts
catch {}
```

---

Always

```ts
try

↓

catch

↓

log

↓

return
```

---

Meaningful Error Message ব্যবহার করতে হবে।

---

# ১৩. Comments

Comment

↓

কেন

Explain করবে।

কি করছে

তা নয়।

---

Good

```ts
// Cache the schema list to avoid repeated file reads.
```

---

Bad

```ts
// Loop starts here
```

---

# ১৪. Formatting

Indent

```
2 Spaces
```

---

Line Ending

```
LF
```

---

Encoding

```
UTF-8
```

---

Trailing Whitespace

Not Allowed

---

# ১৫. String Rules

Default

```
Single Quote
```

Example

```ts
'Schema'
```

---

Template String

প্রয়োজন হলে।

---

# ১৬. Boolean Rules

Name শুরু হবে

```text
is

has

can

should
```

Example

```ts
isStable

hasSearch

canDownload
```

---

# ১৭. CSS Rules

Component CSS

Avoid

---

Tailwind

Preferred

---

Inline Style

Avoid

---

Custom CSS

শুধু

Global Tokens-এর জন্য।

---

# ১৮. Magic Number

Avoid

---

Use

```ts
const MAX_RESULTS = 20
```

---

# ১৯. Duplicate Code

Never

Copy

↓

Paste

↓

Modify

Reusable Function তৈরি করতে হবে।

---

# ২০. Logging

Development

```
console.log()

Allowed
```

---

Production

Remove

---

# ২১. Async Rules

সব Async Function

```
async

await
```

ব্যবহার করবে।

---

Promise Chain

Avoid

---

# ২২. Dependencies

নতুন Library যোগ করার আগে—

- প্রয়োজন আছে?
- Existing Solution আছে?
- Bundle Size কত?

বিবেচনা করতে হবে।

---

# ২৩. Security

Never

- Hardcoded Secret
- API Key
- Token
- Password

---

সব Secret

Environment Variable-এ থাকবে।

---

# ২৪. Performance

Avoid

- Unused Package
- Duplicate Library
- Large Bundle
- Dead Code

---

Optimize

- Images
- Fonts
- Assets
- Components

---

# ২৫. Git Rules

Commit ছোট হবে।

এক Commit

↓

এক Logical Change

---

Commit Message

Conventional Commits

ব্যবহার করতে হবে।

---

# ২৬. Linting

Official

```
ESLint
```

Required

---

Formatting

Official

```
Prettier
```

Required

---

Build Fail

↓

Lint Error

↓

Fix First

---

# ২৭. Testing Rules

নতুন Utility Function

↓

Test করা Recommended।

---

Critical Logic

↓

Test Required।

---

UI

Visual Review Required।

---

# ২৮. Documentation Rules

Public Function

↓

Description থাকবে।

---

Complex Logic

↓

Documentation থাকবে।

---

README

সব Major Module-এর জন্য Recommended।

---

# ২৯. Forbidden

Allowed নয়—

- any
- Large Function
- Large Component
- Nested Ternary
- Deep Nesting
- Inline CSS
- Hardcoded Color
- Hardcoded Spacing
- Duplicate Component
- Circular Dependency
- Dead Code
- Commented-Out Code
- Unused Import

---

# ৩০. Frozen Coding Standards

পরিবর্তন করা যাবে না—

- Language → TypeScript
- Framework → Astro
- Styling → Tailwind CSS
- Indentation → 2 Spaces
- Encoding → UTF-8
- Line Ending → LF
- Component Naming → PascalCase
- Function Naming → camelCase
- Constants → UPPER_SNAKE_CASE
- Strict TypeScript → Required
- ESLint → Required
- Prettier → Required
- Tailwind-first Styling → Required
- Reusable Component Architecture → Required
- Conventional Commits → Required

---

# Coding Standards Status

```
Official Coding Standards

Status

✅ Frozen
```