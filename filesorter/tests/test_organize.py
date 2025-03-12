"""Test the sorting functions in the organize module."""

import pytest

from filesorter.organize import (
    sort_persons_attrgetter,
    sort_persons_bubblesort,
    sort_persons_customcompare,
    sort_persons_lambdafunction,
    sort_persons_quicksort,
)
from filesorter.person import Person


@pytest.fixture
def persons_list():
    """Create a list of Person objects for testing as a fixture."""
    return [
        Person("Alice", "USA", "1234567890", "Engineer", "alice@example.com"),
        Person("Bob", "UK", "0987654321", "Doctor", "bob@example.com"),
        Person(
            "Charlie", "Canada", "5555555555", "Artist", "charlie@example.com"
        ),
    ]


def test_sort_persons_attrgetter(persons_list):
    sorted_list = sort_persons_attrgetter(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_bubblesort(persons_list):
    sorted_list = sort_persons_bubblesort(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_customcompare(persons_list):
    sorted_list = sort_persons_customcompare(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_lambdafunction(persons_list):
    sorted_list = sort_persons_lambdafunction(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]


def test_sort_persons_quicksort(persons_list):
    sorted_list = sort_persons_quicksort(persons_list, "name")
    assert [person.name for person in sorted_list] == [
        "Alice",
        "Bob",
        "Charlie",
    ]
