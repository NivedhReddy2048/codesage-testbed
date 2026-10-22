"""Helpers for fetching users in the reporting layer."""


def lookup_user(users, user_id):
    """Find a user by id in a list of users.

    Returns the matching user, or None when nothing matches.
    """
    for user in users:
        if user.id == user_id:
            return user
    return None


def lookup_user_name(users, user_id):
    """Display name for a user id, falling back to a placeholder."""
    user = lookup_user(users, user_id)
    if user is None:
        return "(unknown user)"
    return user.display_name
