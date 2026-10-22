"""Reading and writing the book list."""

import json
from pathlib import Path

DEFAULT_PATH = Path("books.json")


def load_books(path: Path = DEFAULT_PATH) -> list[dict]:
    """Return the books in `path`, oldest first."""
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_books(books: list[dict], path: Path = DEFAULT_PATH) -> None:
    path.write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
