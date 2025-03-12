from dataclasses import dataclass


# Person attributes constant
@dataclass(frozen=True)
class PersonAttributes:
    """Define the PersonAttributes dataclass for constant(s)."""

    Name: str
    Country: str
    Phone_Number: str
    Job: str
    Email: str


person_attributes = PersonAttributes(
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)


# Person index constant
@dataclass(frozen=True)
class PersonIndex:
    """Define the PersonIndex dataclass for constant(s)."""

    """Define the index locations for the person."""

    Name: int
    Country: int
    Phone_Number: int
    Job: int
    Email: int


person_index = PersonIndex(
    Name=0,
    Country=1,
    Phone_Number=2,
    Job=3,
    Email=4,
)
