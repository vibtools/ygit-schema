# VIBTOOLS-V1 Documentation

Canonical Source: https://schema.ygit.dev/docs/vibtools-v1/
Raw Markdown: https://schema.ygit.dev/docs/vibtools-v1.md

# VibTools Product Manifest Specification

**Version:** 1.0.0 (Stable)

The **VibTools Product Manifest Specification** defines the standard `vibtools.json` format placed in the root directory of applications, packages, and open-source tools.

Instead of manually typing product descriptions, download URLs, versions, categories, and image links into multiple website databases, placing `vibtools.json` in your repository enables **1-Click Import from GitHub**.

## Canonical Schema URL

Add this `$schema` property to your `vibtools.json` for IDE autocomplete and schema validation in VS Code, JetBrains, or automated CI tools:

```json
{
  "$schema": "https://schema.ygit.dev/vibtools/v1/vibtools.schema.json",
  "schemaVersion": 1,
  "name": "Session Manager Pro",
  "slug": "session-manager-pro"
}
```

[View the Schema Reference](/schemas/vibtools/) or [Download Sample Manifest](/examples/).

## How GitHub Import Works

When managing a catalog website or app directory:

1. **Project Root**: The developer places `vibtools.json` at the root of the repository alongside the source code.
2. **Import Trigger**: In your catalog website admin panel, click **"Import with GitHub Repo"** and enter the repository name (e.g. `vibtools/session-manager-pro` or full GitHub URL).
3. **Automated Fetch**: Your website fetches `https://raw.githubusercontent.com/{owner}/{repo}/main/vibtools.json`.
4. **Instant Form Population**: All form inputs—product name, slug, subtitle, description, category, tags, links, flags, and assets—fill automatically.

## Field Specification

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `$schema` | `string (URI)` | **Yes** | `https://schema.ygit.dev/vibtools/v1/vibtools.schema.json` |
| `schemaVersion` | `integer` | No | Major version number (must equal `1`). |
| `name` | `string` | **Yes** | Product name (e.g. `Session Manager Pro`). |
| `slug` | `string` | **Yes** | URL identifier (e.g. `session-manager-pro`). |
| `category` | `string` | No | Catalog category (`Desktop Apps`, `Web Apps & Scripts`, `Browser Extensions`, etc.). |
| `status` | `string` | No | Availability status (`Available`, `In Development`, `Beta`, `Preview`, `Archived`). |
| `version` | `string` | No | Current release version (e.g. `1.0.0`). |
| `subtitle` | `string` | No | Primary tag or subtitle summary. |
| `repository` | `string` | No | GitHub repository path (`owner/repo`). |
| `description` | `string` | No | Markdown or plain text description. |
| `assets.logoUrl` | `string (URI)` | No | Square logo or icon image URL. |
| `assets.thumbnailUrl` | `string (URI)` | No | Banner or social preview thumbnail image URL. |
| `assets.screenshots` | `array` | No | Array of screenshot image URLs. |
| `links.liveDemo` | `string (URI)` | No | Web demo or preview URL. |
| `links.download` | `string (URI)` | No | Release download or installer URL. |
| `links.docs` | `string (URI)` | No | Documentation website URL. |
| `tags` | `array` | No | Keywords and filter tags list. |
| `flags.isActive` | `boolean` | No | Visible in public catalog (`true`/`false`). |
| `flags.isOpenSource` | `boolean` | No | Open source repository flag (`true`/`false`). |
| `flags.isFeatured` | `boolean` | No | Featured highlight toggle (`true`/`false`). |

## Reference Manifest (`vibtools.json`)

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
    "thumbnailUrl": "https://raw.githubusercontent.com/vibtools/session-manager-pro/main/assets/banner.png",
    "screenshots": [
      "https://raw.githubusercontent.com/vibtools/session-manager-pro/main/assets/screenshot-main.png"
    ]
  },
  "links": {
    "liveDemo": "https://demo.vib.tools",
    "download": "https://vib.tools/downloads/v1.0.0.exe",
    "docs": "https://docs.vib.tools/session-manager-pro",
    "github": "https://github.com/vibtools/session-manager-pro"
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

## Website Implementation Snippet

Here is an example client-side function to implement the **"Import with GitHub Repo"** feature in your catalog admin modal:

```typescript
async function importFromGitHub(repoInput: string) {
  // Normalize input: handles "vibtools/session-manager-pro" or "https://github.com/vibtools/session-manager-pro"
  const cleanRepo = repoInput.replace(/^https?:\/\/github\.com\//, '').replace(/\/$/, '');
  const url = `https://raw.githubusercontent.com/${cleanRepo}/main/vibtools.json`;

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Could not find vibtools.json at ${url}`);
  }

  const manifest = await response.json();

  // Auto-fill form fields
  return {
    name: manifest.name ?? '',
    slug: manifest.slug ?? '',
    category: manifest.category ?? 'Desktop Apps',
    status: manifest.status ?? 'Available',
    version: manifest.version ?? '1.0.0',
    subtitle: manifest.subtitle ?? '',
    repository: manifest.repository ?? cleanRepo,
    description: manifest.description ?? '',
    downloadUrl: manifest.links?.download ?? '',
    liveDemoUrl: manifest.links?.liveDemo ?? '',
    filterTags: Array.isArray(manifest.tags) ? manifest.tags.join(', ') : '',
    isActive: manifest.flags?.isActive ?? true,
    isOpenSource: manifest.flags?.isOpenSource ?? true,
    isFeatured: manifest.flags?.isFeatured ?? false,
    logoUrl: manifest.assets?.logoUrl ?? '',
    thumbnailUrl: manifest.assets?.thumbnailUrl ?? '',
  };
}
```
