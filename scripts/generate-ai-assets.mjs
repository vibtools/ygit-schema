#!/usr/bin/env node
/* global console, process */
/**
 * Automated AIO & SEO Machine-Readable Asset Generator
 *
 * Generates:
 * - public/robots.txt (with explicit AI/LLM crawler permissions)
 * - public/sitemap.xml (valid XML sitemap for all static routes)
 * - public/llms.txt (llmstxt.org compliant AI context summary)
 * - public/llms-full.txt (complete stripped, aggregated text content for LLMs)
 * - public/docs/*.md (raw markdown representations of all documentation pages)
 */

import { readdir, readFile, writeFile, mkdir } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = join(__dirname, '..');
const PUBLIC_DIR = join(ROOT, 'public');
const DOCS_DIR = join(ROOT, 'src', 'content', 'docs');
const DATA_DIR = join(ROOT, 'src', 'data');
const EXAMPLES_DIR = join(ROOT, 'examples');

const SITE_URL = 'https://schema.ygit.dev';
const CURRENT_DATE = new Date().toISOString().split('T')[0];
const TIMESTAMP = new Date().toISOString();

// 1. Static Routes definitions
const STATIC_ROUTES = [
  { path: '/', title: 'Home', priority: '1.0', changefreq: 'weekly', description: 'Build, validate, and version YGit manifests.' },
  { path: '/schemas/', title: 'All Schemas', priority: '0.9', changefreq: 'weekly', description: 'Browse official VPMS, DPMS, and VibTools schemas.' },
  { path: '/schemas/vibproject/', title: 'VPMS Version 1 Schema', priority: '0.8', changefreq: 'monthly', description: 'Vib Project Manifest Specification Version 1.' },
  { path: '/schemas/vibproject-v2/', title: 'VPMS Version 2 Schema', priority: '0.8', changefreq: 'monthly', description: 'Vib Project Manifest Specification Version 2 (Frozen).' },
  { path: '/schemas/dpms/', title: 'DPMS Version 1 Schema', priority: '0.8', changefreq: 'monthly', description: 'Documentation Package Manifest Specification Version 1.' },
  { path: '/schemas/vibtools/', title: 'VibTools Manifest Schema', priority: '0.8', changefreq: 'monthly', description: 'VibTools Product Catalog Manifest Specification Version 1.' },
  { path: '/versions/', title: 'Versions Matrix', priority: '0.7', changefreq: 'monthly', description: 'YGit schema version history and lifecycle status.' },
  { path: '/examples/', title: 'Examples Gallery', priority: '0.8', changefreq: 'monthly', description: 'Official valid VPMS, DPMS, and VibTools reference manifests.' },
  { path: '/changelog/', title: 'Changelog', priority: '0.7', changefreq: 'weekly', description: 'YGit Schema Registry release history.' },
  { path: '/search/', title: 'Search', priority: '0.5', changefreq: 'monthly', description: 'Search YGit schemas, documentation, and reference manifests.' },
  { path: '/docs/', title: 'Documentation Index', priority: '0.9', changefreq: 'weekly', description: 'Official YGit and manifest documentation guide.' },
  { path: '/docs/getting-started/', title: 'Getting Started', priority: '0.8', changefreq: 'monthly', description: 'Overview of YGit manifests and core concepts.' },
  { path: '/docs/installation/', title: 'Installation', priority: '0.8', changefreq: 'monthly', description: 'Setup instructions for schema validation tooling.' },
  { path: '/docs/create-manifest/', title: 'Create a Manifest', priority: '0.8', changefreq: 'monthly', description: 'Step-by-step guide to authoring a manifest.' },
  { path: '/docs/schema-reference/', title: 'Schema Reference', priority: '0.8', changefreq: 'monthly', description: 'Exhaustive property definitions, data types, and validation rules.' },
  { path: '/docs/vpms-v2/', title: 'VPMS Version 2', priority: '0.8', changefreq: 'monthly', description: 'Complete specification of VPMS Version 2.' },
  { path: '/docs/dpms-v1/', title: 'DPMS Version 1', priority: '0.8', changefreq: 'monthly', description: 'Complete specification of Documentation Package Manifests.' },
  { path: '/docs/vibtools-v1/', title: 'VibTools Manifest', priority: '0.8', changefreq: 'monthly', description: 'Product catalog specification and 1-click GitHub import guide.' },
  { path: '/docs/validation/', title: 'Validation', priority: '0.8', changefreq: 'monthly', description: 'Schema validation using Python, Node.js, and CI pipelines.' },
  { path: '/docs/versioning/', title: 'Versioning', priority: '0.8', changefreq: 'monthly', description: 'Versioning policies, stability guarantees, and URI conventions.' },
  { path: '/docs/best-practices/', title: 'Best Practices', priority: '0.8', changefreq: 'monthly', description: 'Recommended patterns for manifest authoring and maintenance.' },
  { path: '/docs/migration/', title: 'Migration Guide', priority: '0.8', changefreq: 'monthly', description: 'Upgrading manifests between schema versions.' },
  { path: '/docs/faq/', title: 'FAQ', priority: '0.8', changefreq: 'monthly', description: 'Answers to common implementation and validation questions.' },
];

async function generateRobotsTxt() {
  const content = `# ==============================================================================
# Robots.txt for YGit Schema Registry (https://schema.ygit.dev)
# ==============================================================================

User-agent: *
Allow: /

# Explicit scrape and crawl permissions for major AI & LLM Search Agents
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: Bytespider
Allow: /

User-agent: cohere-ai
Allow: /

User-agent: CCBot
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

User-agent: Applebot-Extended
Allow: /

# Sitemaps
Sitemap: ${SITE_URL}/sitemap.xml
Sitemap: ${SITE_URL}/sitemap-index.xml

# LLM Machine-Readable Index
# https://llmstxt.org
# llms.txt: ${SITE_URL}/llms.txt
# llms-full.txt: ${SITE_URL}/llms-full.txt
`;
  await writeFile(join(PUBLIC_DIR, 'robots.txt'), content, 'utf-8');
  console.log('✓ Generated public/robots.txt');
}

async function generateSitemapXml() {
  const urlsXml = STATIC_ROUTES.map(
    (route) => `  <url>
    <loc>${SITE_URL}${route.path}</loc>
    <lastmod>${CURRENT_DATE}</lastmod>
    <changefreq>${route.changefreq}</changefreq>
    <priority>${route.priority}</priority>
  </url>`,
  ).join('\n');

  const content = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urlsXml}
</urlset>
`;
  await writeFile(join(PUBLIC_DIR, 'sitemap.xml'), content, 'utf-8');
  console.log('✓ Generated public/sitemap.xml');
}

async function generateRawDocs() {
  const publicDocsDir = join(PUBLIC_DIR, 'docs');
  await mkdir(publicDocsDir, { recursive: true });

  const docFiles = await readdir(DOCS_DIR);
  for (const file of docFiles) {
    if (file.endsWith('.mdx') || file.endsWith('.md')) {
      const slug = file.replace(/\.mdx?$/, '');
      const rawContent = await readFile(join(DOCS_DIR, file), 'utf-8');

      // Strip frontmatter but keep clean markdown
      const cleaned = rawContent.replace(/^---[\s\S]*?---\n*/, '').trim();
      const output = `# ${slug.toUpperCase()} Documentation\n\nCanonical Source: ${SITE_URL}/docs/${slug}/\nRaw Markdown: ${SITE_URL}/docs/${slug}.md\n\n${cleaned}\n`;

      await writeFile(join(publicDocsDir, `${slug}.md`), output, 'utf-8');
    }
  }
  console.log('✓ Generated public/docs/*.md (raw markdown files)');
}

async function generateLlmsTxt() {
  const content = `# YGit Schema Registry

> Official JSON Schema registry, documentation, examples, and validation reference for the YGit ecosystem, VPMS (Vib Project Manifest Specification), DPMS (Documentation Package Manifest Specification), and VibTools product catalog manifests.

The YGit Schema Registry provides versioned, machine-verifiable JSON Schema Draft 2020-12 specifications for structuring project metadata, documentation packages, and software catalogs.

## Schemas

- [VPMS Version 1](${SITE_URL}/schemas/vibproject/): Vib Project Manifest Specification Version 1 for software project metadata.
- [VPMS Version 2](${SITE_URL}/schemas/vibproject-v2/): Frozen Version 2 specification for project manifests.
- [DPMS Version 1](${SITE_URL}/schemas/dpms/): Documentation Package Manifest Specification for multi-version documentation trees.
- [VibTools Manifest](${SITE_URL}/schemas/vibtools/): Product catalog manifest for 1-click GitHub repository import.
- [All Schemas](${SITE_URL}/schemas/): Complete index of all supported JSON Schemas.

## Core Documentation

- [Getting Started](${SITE_URL}/docs/getting-started/): Overview of YGit manifests, canonical schema URIs, and basic workflows.
- [Installation](${SITE_URL}/docs/installation/): Setup instructions for schema validation tooling in Python and Node.js.
- [Create a Manifest](${SITE_URL}/docs/create-manifest/): Step-by-step guide to authoring your first manifest.
- [Schema Reference](${SITE_URL}/docs/schema-reference/): Complete property definitions, nested types, and constraints.
- [Validation](${SITE_URL}/docs/validation/): Validating manifests using jsonschema, Python test suites, and CI pipelines.
- [Versioning](${SITE_URL}/docs/versioning/): Strict semantic versioning rules, compatibility policies, and immutable URIs.

## Specifications & Guides

- [VPMS Version 2 Specification](${SITE_URL}/docs/vpms-v2/): Exhaustive technical specification of VPMS v2.
- [DPMS Version 1 Specification](${SITE_URL}/docs/dpms-v1/): Exhaustive technical specification of DPMS v1.
- [VibTools Manifest Guide](${SITE_URL}/docs/vibtools-v1/): Catalog specification and automated GitHub import script.
- [Best Practices](${SITE_URL}/docs/best-practices/): Production recommendations for authoring and maintaining manifests.
- [Migration Guide](${SITE_URL}/docs/migration/): Guide for upgrading between specification versions.
- [FAQ](${SITE_URL}/docs/faq/): Frequently asked questions about VPMS and YGit.

## Examples & Registry

- [Examples Gallery](${SITE_URL}/examples/): Minimal and full reference manifests for VPMS, DPMS, and VibTools.
- [Versions Matrix](${SITE_URL}/versions/): Version history, draft standards, and lifecycle statuses.
- [Changelog](${SITE_URL}/changelog/): Release notes and schema evolution history.

## Optional

- [Full Context Documentation](${SITE_URL}/llms-full.txt): Aggregated complete text content of all schemas, specifications, guides, and manifest examples for direct LLM ingestion.
`;

  await writeFile(join(PUBLIC_DIR, 'llms.txt'), content, 'utf-8');
  console.log('✓ Generated public/llms.txt');
}

async function generateLlmsFullTxt() {
  const sections = [];

  sections.push(`# YGit Schema Registry — Full LLM Knowledge Base
Domain: ${SITE_URL}
Generated: ${TIMESTAMP}
License: MIT
Description: Complete aggregated text content, schema definitions, implementation guides, and manifest examples.`);

  // 1. Core Pages
  sections.push(`
# Page: Home
URL: ${SITE_URL}/
Description: Build, validate, and version YGit manifests.
Content:
The YGit Schema Registry provides versioned JSON Schema specifications, documentation, and validation tooling for YGit projects.
Canonical schema domain: https://schema.ygit.dev/
Supported specifications:
1. VPMS (Vib Project Manifest Specification): Manifests for projects and desktop utilities (vibproject.ygit).
2. DPMS (Documentation Package Manifest Specification): Documentation package discovery and structure (docs.manifest.ygit).
3. VibTools Product Catalog Manifest: Automated project discovery and 1-click GitHub import (vibtools.json).
`);

  // 2. Schema List
  const schemasRaw = await readFile(join(DATA_DIR, 'schema-list.json'), 'utf-8');
  const schemas = JSON.parse(schemasRaw);

  for (const s of schemas) {
    const propsList = s.properties.map(p => `  - ${p.name} (${p.type}${p.required ? ', required' : ''}): ${p.description}`).join('\n');
    sections.push(`
# Page: Schema - ${s.name} (${s.acronym})
URL: ${SITE_URL}/schemas/${s.slug}/
Schema URI: ${SITE_URL}${s.schemaPath}
Version: ${s.version} (Draft ${s.draft})
Status: ${s.status}
Description: ${s.description}
Properties:
${propsList}
`);
  }

  // 3. Documentation Content
  const docFiles = await readdir(DOCS_DIR);
  // Sort docs
  docFiles.sort();

  for (const file of docFiles) {
    if (file.endsWith('.mdx') || file.endsWith('.md')) {
      const slug = file.replace(/\.mdx?$/, '');
      const rawContent = await readFile(join(DOCS_DIR, file), 'utf-8');

      // Parse frontmatter
      const titleMatch = rawContent.match(/title:\s*(.*)/);
      const descMatch = rawContent.match(/description:\s*(.*)/);
      const title = titleMatch ? titleMatch[1].trim() : slug;
      const desc = descMatch ? descMatch[1].trim() : '';

      // Strip frontmatter and clean up
      const cleaned = rawContent
        .replace(/^---[\s\S]*?---\n*/, '')
        .replace(/<Button[^>]*>[\s\S]*?<\/Button>/g, '')
        .replace(/<[A-Z][A-Za-z0-9]*[^>]*\/>/g, '')
        .trim();

      sections.push(`
# Page: Documentation - ${title}
URL: ${SITE_URL}/docs/${slug}/
Raw Markdown: ${SITE_URL}/docs/${slug}.md
Description: ${desc}
Content:
${cleaned}
`);
    }
  }

  // 4. Examples
  const v1Example = await readFile(join(EXAMPLES_DIR, 'vibproject-full-example.ygit'), 'utf-8');
  const dpmsExample = await readFile(join(EXAMPLES_DIR, 'v1', 'dpms', 'docs.full.manifest.ygit'), 'utf-8');
  const vibtoolsExample = await readFile(join(EXAMPLES_DIR, 'v1', 'vibtools', 'vibtools.json'), 'utf-8');

  sections.push(`
# Page: Reference Manifest Examples
URL: ${SITE_URL}/examples/

## Example: VPMS Version 1 (vibproject.ygit)
\`\`\`json
${v1Example}
\`\`\`

## Example: DPMS Version 1 (docs.manifest.ygit)
\`\`\`json
${dpmsExample}
\`\`\`

## Example: VibTools Catalog Manifest (vibtools.json)
\`\`\`json
${vibtoolsExample}
\`\`\`
`);

  const fullContent = sections.join('\n\n---\n\n');
  await writeFile(join(PUBLIC_DIR, 'llms-full.txt'), fullContent, 'utf-8');
  console.log('✓ Generated public/llms-full.txt');
}

async function main() {
  console.log('Generating AI, SEO & Machine-Readable Assets...');
  await generateRobotsTxt();
  await generateSitemapXml();
  await generateRawDocs();
  await generateLlmsTxt();
  await generateLlmsFullTxt();
  console.log('All machine-readable assets generated successfully!');
}

main().catch((err) => {
  console.error('Error generating AI assets:', err);
  process.exit(1);
});
