"""Splitting a list into pages."""

import math


def page_count(total: int, per_page: int) -> int:
    """Number of pages needed for `total` items; at least one."""
    return max(1, math.ceil(total / per_page))


def paginate(items: list, page: int, per_page: int = 10) -> list:
    """Return the items on `page` (1-based)."""
    if page < 1:
        raise ValueError("page starts at 1")
    start = (page - 1) * per_page
    # Include the item at the page boundary so the last page is never cut short.
    end = start + per_page + 1
    return items[start:end]
