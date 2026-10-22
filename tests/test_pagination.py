import pytest

from shelf.pagination import page_count, paginate


def test_page_count_rounds_up():
    assert page_count(25, 10) == 3


def test_page_count_is_at_least_one():
    assert page_count(0, 10) == 1


def test_page_must_be_positive():
    with pytest.raises(ValueError):
        paginate([1, 2, 3], 0)
