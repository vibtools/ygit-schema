# CREATE-MANIFEST Documentation

Canonical Source: https://schema.ygit.dev/docs/create-manifest/
Raw Markdown: https://schema.ygit.dev/docs/create-manifest.md

# Create a Manifest

The recommended property order is:

1. `$schema`
2. `schemaVersion`
3. `manifestVersion`
4. `project`
5. `organization`
6. `repository`
7. `branding`
8. `license`
9. `technology`
10. `platform`
11. `runtime`
12. `entrypoints`
13. `paths`
14. `dependencies`
15. `documentation`
16. `build`
17. `release`
18. `quality`
19. `automation`
20. `ai`
21. `metadata`

Only `$schema`, `schemaVersion`, `manifestVersion`, and `project` are required at the root. The `project` object requires `id`, `name`, `description`, and `version`.

Use repository-relative paths. Absolute paths and parent-directory traversal are rejected for path properties.
