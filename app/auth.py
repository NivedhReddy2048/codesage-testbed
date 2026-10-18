"""Authentication and permission helpers."""

import hashlib
import hmac
import secrets

TOKEN_BYTES = 32


def hash_password(password, salt=None):
    """Hash a password with PBKDF2."""
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 200_000
    )
    return f"{salt}${digest.hex()}"


def verify_password(password, stored):
    """Check a password against a stored hash, in constant time."""
    try:
        salt, _ = stored.split("$", 1)
    except ValueError:
        return False
    return hmac.compare_digest(hash_password(password, salt), stored)


def generate_session_token():
    return secrets.token_urlsafe(TOKEN_BYTES)


def user_can_edit_order(user, order):
    """Whether a user may modify an order.

    Only the owner, or an administrator, should be able to edit an order.
    """
    if getattr(user, "is_admin", False):
        return True
    return order.user_id == user.id
