# Development → Documentation Synchronization Policy

> **Status:** Frozen
> **Version:** v1
> **Applies To:** Entire YGit Schema Project

---

# উদ্দেশ্য

এই নীতিমালার উদ্দেশ্য হলো নিশ্চিত করা যে **Project Development** এবং **Documentation** সব সময় সমন্বিত (Synchronized) থাকবে।

কোনো নতুন Feature, Schema, Component, Rule বা পরিবর্তন কখনোই Documentation ছাড়া Merge বা Release করা যাবে না।

Documentation এই Project-এর **Official Source of Truth**।

---

# মূল নীতি

**Code এবং Documentation সব সময় একসাথে উন্নয়ন (Develop) হবে।**

Documentation কখনো Project Development-এর পরে আলাদাভাবে লেখা হবে না।

প্রতিটি Development Task-এর অংশ হিসেবে সংশ্লিষ্ট Documentation একই সময়ে Update করতে হবে।

---

# Official Workflow

```text
Requirement

↓

Planning

↓

Development

↓

Documentation Update

↓

Validation

↓

Review

↓

Commit

↓

Release
```

Documentation Update ছাড়া কোনো Development Task সম্পূর্ণ (Complete) হিসেবে গণ্য হবে না।

---

# Development Rules

প্রতিবার Project-এ কোনো পরিবর্তন হলে নিচের নিয়ম অনুসরণ করতে হবে।

---

## ১. নতুন Feature যোগ হলে

অবশ্যই Update করতে হবে:

- Getting Started (যদি প্রযোজ্য হয়)
- Schema Reference
- Guides
- Examples
- Validation
- FAQ (যদি নতুন প্রশ্ন তৈরি হয়)

---

## ২. নতুন Schema Property যোগ হলে

অবশ্যই Update করতে হবে:

- Schema Reference
- Example Manifest
- Validation Examples
- Migration Guide (যদি Breaking Change হয়)

---

## ৩. Existing Property পরিবর্তন হলে

অবশ্যই Update করতে হবে:

- Schema Reference
- Examples
- Validation Rules
- FAQ
- Migration Guide (যদি প্রয়োজন হয়)

---

## ৪. Component পরিবর্তন হলে

অবশ্যই Update করতে হবে:

- Guides
- Examples
- Screenshots (যদি থাকে)

---

## ৫. Validation Rule পরিবর্তন হলে

অবশ্যই Update করতে হবে:

- Validation Documentation
- Test Examples
- Schema Reference

---

## ৬. Breaking Change হলে

অবশ্যই Update করতে হবে:

- Migration Guide
- Versioning
- Schema Reference
- Examples
- FAQ

---

# Documentation Checklist

প্রতিটি Pull Request অথবা Development Task শেষ হওয়ার আগে নিচের Checklist অনুসরণ করতে হবে।

```text
□ Schema Update হয়েছে

□ Examples Update হয়েছে

□ Documentation Update হয়েছে

□ Validation Update হয়েছে

□ FAQ Update হয়েছে (যদি প্রয়োজন হয়)

□ Migration Guide Update হয়েছে (যদি প্রয়োজন হয়)

□ Version Information Update হয়েছে
```

সবগুলো প্রযোজ্য আইটেম সম্পন্ন না হলে Task Complete ধরা যাবে না।

---

# Documentation Ownership

Project-এর প্রতিটি অংশের Documentation তার সংশ্লিষ্ট Development-এর অংশ।

কোনো Documentation-এর জন্য আলাদা Development Phase রাখা হবে না।

---

# Synchronization Rules

Documentation এবং Source Code-এর মধ্যে নিচের বিষয়গুলো সব সময় Synchronize থাকতে হবে।

- Schema Structure
- Property Names
- Required Fields
- Optional Fields
- Default Values
- Examples
- Validation Rules
- Version Information
- Folder Structure
- Workflow

যদি Source Code পরিবর্তন হয়, Documentation-ও একই পরিবর্তন প্রতিফলিত করবে।

---

# Commit Policy

একটি Feature Commit করার আগে নিশ্চিত করতে হবে:

```text
Feature

✓ Code Updated

✓ Documentation Updated

✓ Examples Updated

✓ Validation Updated
```

Documentation Update ছাড়া Feature Commit করা নিরুৎসাহিত।

---

# Pull Request Policy

কোনো Pull Request Review করার সময় Documentation Review বাধ্যতামূলক।

Review Checklist:

```text
Schema Updated?

Documentation Updated?

Examples Updated?

Validation Updated?

Breaking Changes Documented?

Version Updated?
```

---

# Release Policy

কোনো Release তৈরি করার আগে নিশ্চিত করতে হবে:

- Documentation সম্পূর্ণ আপডেট হয়েছে।
- Examples সর্বশেষ Schema অনুযায়ী আপডেট হয়েছে।
- Validation সফল হয়েছে।
- Migration Guide (যদি প্রয়োজন হয়) আপডেট হয়েছে।
- FAQ (যদি প্রয়োজন হয়) আপডেট হয়েছে।

Documentation অসম্পূর্ণ থাকলে Release করা যাবে না।

---

# AI Development Rules

AI Coding Assistant ব্যবহার করার সময় প্রতিটি Development Task শেষে AI-কে নিচের কাজগুলোও করতে হবে।

- সংশ্লিষ্ট Documentation Update করা।
- Examples Update করা।
- Validation প্রভাবিত হলে Documentation Update করা।
- Breaking Change হলে Migration Guide Update করা।
- নতুন Feature হলে Getting Started এবং Guides Review করা।
- Documentation-এর সাথে Schema-এর সামঞ্জস্য যাচাই করা।

AI কখনো Documentation Update বাদ দেবে না।

---

# Documentation Priority

Documentation Priority Order:

```text
Schema

↓

Examples

↓

Reference Documentation

↓

Developer Guides

↓

Validation

↓

Migration

↓

FAQ
```

---

# Definition of Done (DoD)

কোনো Development Task তখনই সম্পূর্ণ (Done) হিসেবে গণ্য হবে যখন—

- Feature সম্পন্ন।
- Schema আপডেট।
- Examples আপডেট।
- Documentation আপডেট।
- Validation সম্পন্ন।
- Review সম্পন্ন।

এর আগে Task-কে সম্পূর্ণ ধরা যাবে না।

---

# Frozen Rules

এই Project-এ নিচের নিয়মগুলো স্থায়ীভাবে অনুসরণ করা হবে।

- Documentation Development-এর অংশ।
- Documentation পরে লেখা হবে না।
- প্রতিটি Feature-এর সাথে Documentation Update বাধ্যতামূলক।
- প্রতিটি Schema পরিবর্তনের সাথে Reference Documentation Update বাধ্যতামূলক।
- প্রতিটি Breaking Change-এর সাথে Migration Guide Update বাধ্যতামূলক।
- Documentation এবং Schema সব সময় Synchronize থাকতে হবে।
- Documentation Update ছাড়া কোনো Feature Complete, Merge বা Release করা যাবে না।

---

# Policy Status

```text
Status

Frozen

Applies To

Entire Repository

Enforcement

Mandatory

Effective From

Version 1 (v1)
```
