export type SchemaStatus = 'stable' | 'beta' | 'draft' | 'deprecated';

export type SchemaProperty = Readonly<{
  name: string;
  type: string;
  required: boolean;
  description: string;
}>;

export type SchemaRecord = Readonly<{
  slug: string;
  acronym: string;
  name: string;
  description: string;
  version: string;
  schemaVersion: number;
  status: SchemaStatus;
  draft: string;
  license: string;
  compatibility: string;
  schemaPath: string;
  examplePath: string;
  updatedAt: string;
  properties: readonly SchemaProperty[];
}>;
