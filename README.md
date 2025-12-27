# FileSorter

## What is FileSorter?
FileSorter is a small project to test how fast different sorting methods work. It reads text records, makes a `Person` object for each record, and sorts the objects.

## Main points
- We compare five sorting ways: Bubblesort, Quicksort, `sorted()` with `lambda`, `operator.attrgetter`, and a custom comparator.
- The program measures time for each step: reading the file, parsing data, sorting, and writing the result.
- It works with large files (tens of thousands of records) to show how algorithms scale.

## Data format
See `input/people.txt`. Each record becomes a `Person` with: `name`, `country`, `phone_number`, `job`, `email`.

## How to install
You need Python (3.10 or newer is best). Devenv and Poetry are helpful but not required.

```bash
# If you use Devenv (optional)
devenv shell

# Install packages
poetry install
```

## How to run
Example command to sort by email using quicksort:

```bash
poetry run filesorter --attribute email --approach quicksort \
	--input-file input/people.txt --output-file output/people.txt
```

Flags:
- `--attribute` : which field to sort (for example `email` or `name`).
- `--approach` : which sorting way (`bubblesort`, `quicksort`, `lambda`, `attrgetter`, `comparator`).

## Output and results
The program shows time for each phase: read, parse, sort, and write. Use these times to compare methods and see which is faster.

## Tests and code style
- Tests are in `filesorter/tests`. Run them with `pytest`.
- Use Ruff for linting.

## How to help (contribute)
1. Fork the repo and make a new branch.
2. Add tests for new features.
3. Run `poetry run pytest` and fix any issues before a pull request.
