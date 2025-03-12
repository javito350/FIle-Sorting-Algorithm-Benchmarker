"""Extract and save the data about the person from the CSV file."""

import csv
from typing import List

from filesorter.constants import person_index
from filesorter.person import Person

# TODO: add a complete implementation of the:
# - extract_person_data function
# - write_person_data function
# Make sure that your implementations are tested
# through a test suite in the test_process.py file

# TODO: make sure to add type annotations for the
# parameters and return values for the functions


def extract_person_data(data: str) -> List[Person]:
    """Extract a specified data column from the provided textual contents."""
    person_data = []
    for line in csv.reader(
        data.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # extract each of the attributes about a person from the line variable
        current_name = line[person_index.Name]
        current_country = line[person_index.Country]
        current_phone_number = line[person_index.Phone_Number]
        current_job = line[person_index.Job]
        current_email = line[person_index.Email]
        # Check if all attributes are present
        if None in (
            current_name,
            current_country,
            current_phone_number,
            current_job,
            current_email,
        ):
            continue
        # construct a new instance of the Person class that contains all
        # of the attributes that were extracted from the CSV file
        row = Person(
            current_name,  # Provide a default empty string if it's None
            current_country,
            current_phone_number,
            current_job,
            current_email,
        )
        # add the person to the list of people that have been extracted
        person_data.append(row)
    return person_data


def write_person_data(file_name: str, person_data: List[Person]) -> None:
    """Write the person data stored in a list to the specified file."""
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        if person_data:
            writer.writerow(vars(person_data[0]).keys())
        # Write the data rows
        for person in person_data:
            writer.writerow(vars(person).values())
