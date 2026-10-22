"""Command line: python -m shelf list [--page N] [--per-page N]."""

import argparse

from .pagination import page_count, paginate
from .storage import load_books


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="shelf")
    sub = parser.add_subparsers(dest="command", required=True)
    list_cmd = sub.add_parser("list", help="list your books, a page at a time")
    list_cmd.add_argument("--page", type=int, default=1)
    list_cmd.add_argument("--per-page", type=int, default=10)
    args = parser.parse_args(argv)

    books = load_books()
    pages = page_count(len(books), args.per_page)
    first = (args.page - 1) * args.per_page
    for number, book in enumerate(paginate(books, args.page, args.per_page), start=first + 1):
        print(f"{number:>3}. {book['title']} by {book['author']}")
    print(f"page {args.page} of {pages}")
    return 0
