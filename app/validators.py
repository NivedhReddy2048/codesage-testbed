"""Input validation shared across the service."""

import re

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")
MAX_EMAIL_LENGTH = 254


def is_valid_email(value):
    """Whether a string looks like an email address."""
    if not value or len(value) > MAX_EMAIL_LENGTH:
        return False
    return bool(EMAIL_PATTERN.match(value.strip()))


def normalise_email(value):
    return value.strip().lower()


def is_valid_page(page):
    return isinstance(page, int) and page >= 1


def clamp(value, low, high):
    return max(low, min(high, value))
