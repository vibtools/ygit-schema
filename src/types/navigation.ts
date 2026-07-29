export type NavigationItem = Readonly<{
  label: string;
  href: string;
  description?: string;
}>;

export type NavigationGroup = Readonly<{
  title: string;
  items: readonly NavigationItem[];
}>;
