"""Test suite for the person module."""

from filesorter.person import Person


def test_person_initialization():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    assert person.name == "Alice"
    assert person.country == "USA"
    assert person.phone == "1234567890"
    assert person.job == "Engineer"
    assert person.email == "alice@example.com"


def test_person_str():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    assert (
        str(person)
        == "Person(name=Alice, country=USA, phone=1234567890, job=Engineer, email=alice@example.com)"
    )


def test_person_repr():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    assert (
        repr(person)
        == "Person(name=Alice, country=USA, phone=1234567890, job=Engineer, email=alice@example.com)"
    )


def test_person_equality():
    person1 = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    person2 = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    person3 = Person("Bob", "UK", "0987654321", "Doctor", "bob@example.com")
    assert person1 == person2
    assert person1 != person3


def test_person_update_email():
    person = Person(
        "Alice", "USA", "1234567890", "Engineer", "alice@example.com"
    )
    person.update_email("newalice@example.com")
    assert person.email == "newalice@example.com"
