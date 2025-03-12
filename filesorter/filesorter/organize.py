import functools
import sys
from operator import attrgetter
from typing import List

from filesorter.person import Person
from filesorter.profile import timer

# Register the current module in sys.modules
sys.modules[__name__]


@timer("Time to Sort Person Data Using Iterative Bubble sort (ms)")
def sort_persons_bubblesort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the bubble sort approach."""
    n = len(persons)  # This is how i get the length of the list persons
    for i in range(n):  # Iterate over the list persons
        for j in range(0, n - i - 1):
            if getattr(persons[j], attribute) > getattr(
                persons[j + 1], attribute
            ):
                persons[j], persons[j + 1] = persons[j + 1], persons[j]
    return persons  # Return the sorted list


@timer(
    "Time to Sort Person Data Using Iterative Quick Sort (ms)"
)  # from what he said in class (not sure if i catch up everything but i think is something like that): this function is important, because in the other function like (sort_person,sort_persons_lambdafunction...) where u call the timer, u call this function (sort_persons_quicksort), store it in process.py performance
def sort_persons_quicksort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the iterative quick sort approach."""
    if not persons:
        return persons  # If the list is empty return persons
    stack = [(0, len(persons) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(persons, low, high, attribute)
            stack.append((low, pivot_index - 1))
            stack.append(
                (pivot_index + 1, high)
            )  # Append the pivot index + 1 to the stack
    return persons  # Return the sorted list


def partition(
    persons: List[Person], low: int, high: int, attribute: str
) -> int:
    """Partition the list of Person objects based on a given attribute."""
    pivot = getattr(persons[high], attribute)
    i = low - 1  # i is the index of the smaller element
    attributes = [getattr(person, attribute) for person in persons]
    for j in range(low, high):
        if attributes[j] <= pivot:
            i += 1
            persons[i], persons[j] = persons[j], persons[i]
    persons[i + 1], persons[high] = persons[high], persons[i + 1]
    return i + 1


@timer("Time to Sort Person Data Using Iterative Bubble sort (ms)")
def sort_persons(
    persons: List[Person], attribute: str, approach: str
) -> List[Person]:
    """Sort the list of Person objects according to the requested approach."""
    if (
        approach == "bubblesort"
    ):  # If the approach is bubblesort use the function sort_persons_bubblesort
        return sort_persons_bubblesort(persons, attribute)
    elif (
        approach == "quicksort"
    ):  # If the approach is quicksort use the function sort_persons_quicksort
        return sort_persons_quicksort(persons, attribute)
    elif (
        approach == "lambdafunction"
    ):  # If the approach is lambdafunction use the function sort_persons_lambdafunction
        return sort_persons_lambdafunction(persons, attribute)
    elif (
        approach == "attrgetter"
    ):  # If the approach is attrgetter use the function sort_persons_attrgetter
        return sort_persons_attrgetter(persons, attribute)
    elif (
        approach == "customcompare"
    ):  # If the approach is customcompare use the function sort_persons_customcompare
        return sort_persons_customcompare(persons, attribute)
    else:  # If the approach is not any of the above raise an error
        raise ValueError(f"Unknown sorting approach: {approach}")


@timer("Time to Sort Person Data Using Iterative Bubble sort (ms)")
def sort_persons_lambdafunction(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the lambdafunction approach."""
    if not all(hasattr(person, attribute) for person in persons):
        raise ValueError(f"Attribute {attribute} is not valid for sorting.")
    return sorted(persons, key=lambda person: getattr(person, attribute))


@timer("Time to Sort Person Data Using Iterative Bubble sort (ms)")
def sort_persons_attrgetter(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the attrgetter approach."""
    if not all(hasattr(person, attribute) for person in persons):
        raise ValueError(f"Attribute {attribute} is not valid for sorting.")
    return sorted(persons, key=attrgetter(attribute))


@timer("Time to Sort Person Data Using Iterative Custom Comperator (ms)")
def sort_persons_customcompare(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the customcompare approach."""

    def compare_persons(person_one: Person, person_two: Person) -> int:
        """Compare two people using the provided attribute."""
        value_one = getattr(person_one, attribute)
        value_two = getattr(person_two, attribute)
        if value_one < value_two:
            return -1
        elif value_one > value_two:
            return 1
        else:
            return 0

    if not all(hasattr(person, attribute) for person in persons):
        raise ValueError(f"Attribute {attribute} is not valid for sorting.")
    return sorted(persons, key=functools.cmp_to_key(compare_persons))
