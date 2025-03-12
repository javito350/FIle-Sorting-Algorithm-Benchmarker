"""Test suite for the constants module."""

# ruff: noqa: PLR2004

from filesorter import constants


def test_constant_values_for_person_attributes():
    """Ensure that all of the person_attributes constants have a value."""
    assert len(vars(constants.person_attributes).items()) == 5
    for _, value in vars(constants.person_attributes).items():
        assert value is not None


def test_constant_values_for_file_types():
    """Ensure that all of the file_types constants have a value."""
    assert len(vars(constants.file_types).items()) > 0
    for _, value in vars(constants.file_types).items():
        assert value is not None


def test_constant_values_for_sorting_options():
    """Ensure that all of the sorting_options constants have a value."""
    assert len(vars(constants.sorting_options).items()) > 0
    for _, value in vars(constants.sorting_options).items():
        assert value is not None
