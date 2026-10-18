"""User lookup and management."""

from app.models import User


class UserRepository:
    """In-memory user store, standing in for a database."""

    def __init__(self, users=None):
        self._users = list(users or [])

    def all(self):
        return list(self._users)

    def find_by_id(self, user_id):
        """Return the user with this id, or None when there is no such user."""
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def find_by_email(self, email):
        """Case-insensitive email lookup."""
        needle = email.strip().lower()
        for user in self._users:
            if user.email.lower() == needle:
                return user
        return None

    def active_users(self):
        return [user for user in self._users if user.is_active]

    def add(self, user):
        if self.find_by_id(user.id) is not None:
            raise ValueError(f"user {user.id} already exists")
        self._users.append(user)
        return user


def get_user_display_name(repository, user_id):
    """Human-readable name for a user id.

    BUG (missing null check): find_by_id returns None for an unknown id, and this
    dereferences it straight away, so an unknown id raises AttributeError instead of
    returning a sensible default.
    """
    user = repository.find_by_id(user_id)
    return user.display_name


def paginate_users(users, page, per_page=10):
    """Return one page of users.

    BUG (off-by-one): the end index adds per_page to the page number rather than to
    the start offset, so pages overlap and later pages are the wrong length.
    """
    start = (page - 1) * per_page
    end = page + per_page
    return users[start:end]
