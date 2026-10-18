"""Tests for the user repository."""

from app.models import User
from app.users import UserRepository


def make_repo():
    return UserRepository(
        [
            User(id=1, email="ada@example.com", display_name="Ada"),
            User(id=2, email="Grace@example.com", display_name="Grace"),
        ]
    )


def test_find_by_id_returns_the_user():
    assert make_repo().find_by_id(1).display_name == "Ada"


def test_find_by_id_returns_none_for_unknown():
    assert make_repo().find_by_id(99) is None


def test_find_by_email_is_case_insensitive():
    assert make_repo().find_by_email("grace@example.com").id == 2
