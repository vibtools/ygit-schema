const DATE_FORMAT = new Intl.DateTimeFormat('en-US', {
  year: 'numeric',
  month: 'short',
  day: 'numeric',
  timeZone: 'UTC',
});

export function formatDate(value: string): string {
  return DATE_FORMAT.format(new Date(`${value}T00:00:00Z`));
}
