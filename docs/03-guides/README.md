# Guides

Practical implementation guides are maintained as MDX in `src/content/docs/`:

- `getting-started.mdx`
- `installation.mdx`
- `create-manifest.mdx`
- `best-practices.mdx`
- `validation.mdx`
- `versioning.mdx`
- `migration.mdx`
- `faq.mdx`

## Authoring principles

- Keep `project.id` stable.
- Use repository-relative paths with forward slashes.
- Do not store secrets in manifests.
- Preserve the official property order.
- Validate every schema, example, and fixture change before release.
