import csv
from typing import List

from filesorter.constants import person_index
from filesorter.person import Person


def extract_person_data(data: str) -> List[Person]:
    """Extract a specified data column from the provided textual contents."""
    """All attributes are extracted from the CSV file."""
    person_data = []  # List to store extracted person records
    for line in csv.reader(
        data.splitlines(),
        quotechar='"',  # Double quotes are used as the quote character
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        # Extract each of the attributes about a person from the line variable
        current_name = line[person_index.Name]  # Extract name from CSV row
        current_country = line[person_index.Country]  # Extract country
        current_phone_number = line[
            person_index.Phone_Number
        ]  # Extract phone number
        current_job = line[person_index.Job]  # Extract job
        current_email = line[person_index.Email]  # Extract email

        # Check if all attributes are present before creating a Person instance
        if None in (
            current_name,
            current_country,
            current_phone_number,
            current_job,
            current_email,
        ):
            continue

        # Create a new Person instance with extracted attributes
        row = Person(
            current_name,
            current_country,
            current_phone_number,
            current_job,
            current_email,
        )

        # Add the person to the list of extracted people
        person_data.append(row)
    return person_data


def write_person_data(file_name: str, person_data: List[Person]) -> None:
    """Write the person data stored in a list to the specified file."""
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row using keys from the first Person object
        if person_data:
            writer.writerow(vars(person_data[0]).keys())

        # Write data rows by extracting values from each Person instance
        for person in person_data:
            writer.writerow(vars(person).values())
