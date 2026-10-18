const EMAIL_PATTERN = /^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$/;

export function isValidEmail(value) {
  if (!value || value.length > 254) {
    return false;
  }
  return EMAIL_PATTERN.test(value.trim());
}

export function isPositiveInteger(value) {
  return Number.isInteger(value) && value > 0;
}

export function clamp(value, low, high) {
  return Math.max(low, Math.min(high, value));
}
