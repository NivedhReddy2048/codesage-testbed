export function formatCurrency(cents, currency = "USD") {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency,
  }).format(cents / 100);
}

export function truncate(text, maxLength = 80) {
  if (text.length <= maxLength) {
    return text;
  }
  return `${text.slice(0, maxLength - 1)}\u2026`;
}

export function pluralise(count, singular, plural) {
  return count === 1 ? singular : plural || `${singular}s`;
}
