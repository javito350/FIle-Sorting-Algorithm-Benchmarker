"""Test suite for the person module."""

from filesorter.person import Person


def test_person_initialization():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    assert person.name == "Alice"
    assert person.country == "USA"
    assert person.phone_number == "1234567890"
    assert person.job == "Engineer"
    assert person.email == "alice@example.com"


def test_person_repr():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    expected_repr = "Alice is a Engineer who lives in USA. You can call this person at 1234567890 and email them at alice@example.com"
    assert repr(person) == expected_repr


def test_person_create_list():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    expected_list = [
        "Alice",
        "USA",
        "1234567890",
        "Engineer",
        "alice@example.com",
    ]
    assert person.create_list() == expected_list
