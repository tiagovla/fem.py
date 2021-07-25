from __future__ import annotations


class Mesh:
    """Represent a base mesh class."""
    def __init__(self, x, conn: dict | None = None, sets: dict | None = None):
        self.x = x
        self.conn = conn if conn else {}
        self.sets = sets if sets else {}
        self.data = {}
