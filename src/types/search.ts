export type SearchCategory = 'all' | 'schema' | 'documentation' | 'example';

export type SearchResult = Readonly<{
  title: string;
  url: string;
  excerpt: string;
  category: Exclude<SearchCategory, 'all'>;
}>;
