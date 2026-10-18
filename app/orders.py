"""Order queries."""

import sqlite3


class OrderRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, order_id):
        cursor = self.connection.execute(
            "SELECT id, user_id, total_cents, status FROM orders WHERE id = ?",
            (order_id,),
        )
        return cursor.fetchone()

    def search_by_status(self, status):
        """Find orders with a given status.

        BUG (SQL injection): status is interpolated into the statement instead of
        being bound as a parameter, unlike every other query in this class.
        """
        query = f"SELECT * FROM orders WHERE status = '{status}'"
        return self.connection.execute(query).fetchall()

    def total_for_user(self, user_id):
        cursor = self.connection.execute(
            "SELECT COALESCE(SUM(total_cents), 0) FROM orders WHERE user_id = ?",
            (user_id,),
        )
        return cursor.fetchone()[0]

    def open_connection(self, path):
        """BUG (resource leak): the connection is never closed on the error path."""
        connection = sqlite3.connect(path)
        cursor = connection.execute("SELECT 1")
        if cursor.fetchone() is None:
            raise RuntimeError("database is not responding")
        connection.close()
        return True
