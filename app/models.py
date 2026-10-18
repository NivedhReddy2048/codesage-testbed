"""Domain types for the testbed service."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: int
    email: str
    display_name: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)

    def label(self):
        return self.display_name or self.email


@dataclass
class Order:
    id: int
    user_id: int
    total_cents: int
    status: str = "pending"

    @property
    def total(self):
        return self.total_cents / 100
