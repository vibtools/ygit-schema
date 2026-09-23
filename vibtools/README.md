# VibTools Specification & Asset Hub

This folder (`/vibtools`) contains the complete reference files, high-resolution branding assets, and non-technical documentation suite for the **VibTools Catalog Manifest Specification (`vibtools.schema.json`)**.

---

## 📁 Directory Structure

```text
vibtools/
├── README.md               # Folder overview and navigation
├── vibtools.json           # Canonical reference manifest adhering to vibtools.schema.json
├── quick-start.md          # 3-step beginner guide for non-technical users
├── features.md             # Non-technical product features and overview
├── faq.md                  # Plain-language Frequently Asked Questions
├── whats-new.md            # Release highlights & new capabilities
└── assets/
    ├── og-image.png        # Social OpenGraph card (1200x630, 16:9)
    ├── logo.png            # High-resolution square logo (512x512, 1:1)
    ├── thumbnail.png       # Catalog banner thumbnail (800x450, 16:9)
    └── screenshot.png      # Visual workspace UI preview (1200x675)
```

---

## 🎯 How It Connects to `vibtools.schema.json`

The schema at `/public/vibtools/v1/vibtools.schema.json` (and `/v1/vibtools/vibtools.schema.json`) defines properties that power these files:

1. **Social OG Image**: `assets.ogImageUrl` and `assets.ogImage` point to `vibtools/assets/og-image.png` (or any remote CDN URL) to generate rich social media preview cards on Twitter, LinkedIn, and Discord.
2. **Non-Technical Documents**: `documents` maps user-facing Markdown files:
   - `documents.quickStart` -> `vibtools/quick-start.md`
   - `documents.features` -> `vibtools/features.md`
   - `documents.faq` -> `vibtools/faq.md`
   - `documents.whatsNew` -> `vibtools/whats-new.md`
3. **1-Click Catalog Import**: Portals and catalog dashboards read `vibtools.json` to automatically discover tools without manual database entry.

---

## 📖 Quick Links

- [Read the Quick Start Guide](./quick-start.md)
- [Explore Features](./features.md)
- [Check the FAQ](./faq.md)
- [Read What's New](./whats-new.md)
- [Inspect the Schema (`/public/vibtools/v1/vibtools.schema.json`)](../public/vibtools/v1/vibtools.schema.json)
