import schemaList from '@/data/schema-list.json';
import type { SchemaRecord } from '@/types/schema';

const SCHEMAS = schemaList as readonly SchemaRecord[];

export function getSchemas(): readonly SchemaRecord[] {
  return SCHEMAS;
}

export function getSchemaBySlug(slug: string): SchemaRecord | undefined {
  return SCHEMAS.find((schema) => schema.slug === slug);
}
