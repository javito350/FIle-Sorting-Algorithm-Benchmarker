"""Extract and save the data about the person from the CSV file."""

import csv
from typing import List

from filesorter.constants import person_index
from filesorter.person import Person


def extract_person_data(data: str) -> List[Person]:
    """Extract a specified data column from the provided textual contents."""
    person_data = []  # Initialize an empty list to store person objects
    for line in csv.reader(
        data.splitlines(),
        quotechar='"',  # Define quote character for CSV parsing
        delimiter=",",  # Use comma as delimiter
        quoting=csv.QUOTE_ALL,  # Ensure all fields are quoted
        skipinitialspace=True,  # Remove spaces after delimiters
    ):
        # Extract each of the attributes about a person from the line variable
        current_name = line[person_index.Name]  # Extract name from CSV row
        current_country = line[person_index.Country]  # Extract country
        current_phone_number = line[
            person_index.Phone_Number
        ]  # Extract phone number
        current_job = line[person_index.Job]  # Extract job
        current_email = line[person_index.Email]  # Extract email
        # Check if all attributes are present
        if None in (
            current_name,
            current_country,
            current_phone_number,
            current_job,
            current_email,
        ):
            continue  # Skip rows with missing values
        # Construct a new instance of the Person class that contains all
        # of the attributes that were extracted from the CSV file
        row = Person(
            current_name,  # Assign extracted name
            current_country,  # Assign extracted country
            current_phone_number,  # Assign extracted phone number
            current_job,  # Assign extracted job
            current_email,  # Assign extracted email
        )
        # Add the person to the list of people that have been extracted
        person_data.append(row)
    return person_data  # Return the list of extracted person objects


def write_person_data(file_name: str, person_data: List[Person]) -> None:
    """Write the person data stored in a list to the specified file."""
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)  # Create a CSV writer object
        # Write the header
        if person_data:  # Check if person_data is not empty
            writer.writerow(vars(person_data[0]).keys())  # Write column names
        # Write the data rows
        for person in person_data:
            writer.writerow(vars(person).values())  # Write attribute values
