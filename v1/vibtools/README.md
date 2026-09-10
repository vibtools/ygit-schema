# VibTools Product Catalog Manifest Specification (VibTools Manifest)

**Version:** 1.0.0 (Stable)

---

# Overview

The **VibTools Product Catalog Manifest Specification** defines the standard `vibtools.json` file format stored at the root of project repositories.

It enables centralized portals, websites, and application stores (such as VibTools catalog dashboards) to automatically discover, import, and synchronize project metadata—including product names, slugs, versions, categories, download links, live demos, and assets—without repetitive manual form submissions.

---

# Purpose & Workflow

### 1. The Problem
Adding tools and applications across multiple websites or directories requires manually entering names, versions, tags, links, descriptions, logos, and banners repeatedly. When an app updates its version or release link, every site must be updated manually.

### 2. The Solution
Place a single `vibtools.json` at the root of your GitHub repository. The catalog website's **"Import with GitHub Repo"** feature fetches this file directly from the repository and automatically maps all fields into your database or admin form.

```text
GitHub Repository (e.g. vibtools/session-manager-pro)
  │
  ├── vibtools.json  (Root configuration)
  ├── assets/
  │   ├── logo.png
  │   └── banner.png
  └── src/
          │
          ▼
GitHub Raw CDN / API (https://raw.githubusercontent.com/.../main/vibtools.json)
          │
          ▼
Catalog Website Admin Panel
  ├── 1. Enter Repo URL: "vibtools/session-manager-pro"
  ├── 2. Click "Import from GitHub"
  └── 3. Form fields auto-populate instantly:
         • Product Name: "Session Manager Pro"
         • Slug: "session-manager-pro"
         • Category: "Desktop Apps"
         • Status: "Available"
         • Version: "1.0.0"
         • Subtitle / Primary Tag: "Windows, Automation, Utility"
         • Description, URLs, Tags & Flags
```

---

# Schema Definition

## Root Properties

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `$schema` | `string (URI)` | **Yes** | Canonical schema URL: `https://schema.ygit.dev/vibtools/v1/vibtools.schema.json` |
| `schemaVersion` | `integer` | No (default: `1`) | Major version number of this specification. |
| `name` | `string` | **Yes** | Human-readable product display name. |
| `slug` | `string` | **Yes** | URL-safe identifier (e.g. `session-manager-pro`). |
| `category` | `string` | No | Catalog category (e.g. `Desktop Apps`, `Web Apps & Scripts`, `Browser Extensions`). |
| `status` | `string` | No | Current status (`Available`, `In Development`, `Beta`, `Preview`, `Archived`). |
| `version` | `string` | No | Semantic version string (e.g. `1.0.0` or `v1.0.0`). |
| `subtitle` | `string` | No | Short tagline or primary tags (e.g. `Windows, Automation, Utility`). |
| `repository` | `string` | No | GitHub repository path (`owner/repo`) or full URL. |
| `description` | `string` | No | Comprehensive markdown or plain text description. |
| `assets` | `object` | No | Visual media (`logoUrl`, `thumbnailUrl`, `screenshots`). |
| `links` | `object` | No | Hyperlinks (`liveDemo`, `download`, `docs`, `github`, `website`). |
| `tags` | `array` | No | List of keyword tags (e.g. `["Desktop", "Automation", "Free"]`). |
| `flags` | `object` | No | Visibility toggles (`isActive`, `isOpenSource`, `isFeatured`). |
| `custom` | `object` | No | Vendor-specific key-value extensions. |

---

# Example Manifest (`vibtools.json`)

```json
{
  "$schema": "https://schema.ygit.dev/vibtools/v1/vibtools.schema.json",
  "schemaVersion": 1,
  "name": "Session Manager Pro",
  "slug": "session-manager-pro",
  "category": "Desktop Apps",
  "status": "Available",
  "version": "1.0.0",
  "subtitle": "Windows, Automation, Utility",
  "repository": "vibtools/session-manager-pro",
  "description": "A powerful session and workspace management utility for Windows power users. Automates window positioning, workspace state saving, and instant multi-monitor workspace restoration.",
  "assets": {
    "logoUrl": "https://raw.githubusercontent.com/vibtools/session-manager-pro/main/assets/logo.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/vibtools/session-manager-pro/main/assets/banner.png"
  },
  "links": {
    "liveDemo": "https://demo.vib.tools",
    "download": "https://vib.tools/downloads/v1.0.0.exe"
  },
  "tags": [
    "Desktop",
    "Automation",
    "Free",
    "Open Source"
  ],
  "flags": {
    "isActive": true,
    "isOpenSource": true,
    "isFeatured": false
  }
}
```
