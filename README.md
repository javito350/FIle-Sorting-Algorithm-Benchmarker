# File Sorting Algorithm Benchmarker

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-managed-blue)](https://python-poetry.org/)

## 📖 Overview

File Sorting Algorithm Benchmarker is a performance testing tool that compares the efficiency of different sorting algorithms on real-world data. It processes text records, converts them into `Person` objects, and benchmarks various sorting implementations to help you understand their performance characteristics with large datasets.

## ✨ Features

- **Multiple Sorting Algorithms**: Compare five different sorting approaches:
  - **Bubblesort**: Classic O(n²) comparison-based algorithm
  - **Quicksort**: Efficient O(n log n) divide-and-conquer algorithm
  - **Lambda sorting**: Python's built-in `sorted()` with lambda functions
  - **Attrgetter**: Optimized sorting using `operator.attrgetter`
  - **Custom Comparator**: Sorting with user-defined comparison functions

- **Detailed Performance Metrics**: Measures execution time for each phase:
  - File reading
  - Data parsing
  - Sorting operation
  - Output writing

- **Scalable Testing**: Designed to handle large datasets (tens of thousands of records) to demonstrate algorithm performance at scale

- **Flexible Sorting**: Sort by any Person attribute (name, country, phone, job, email)

## 📋 Data Format

The input file (`input/people.txt`) contains structured records that are parsed into `Person` objects with the following attributes:
- `name`: Full name
- `country`: Country of residence
- `phone_number`: Contact number
- `job`: Occupation
- `email`: Email address

## 🚀 Installation

### Prerequisites
- Python 3.10 or newer
- Poetry (for dependency management)
- Devenv (optional, for development environment)

### Setup

```bash
# Clone the repository
git clone https://github.com/javito350/FIle-Sorting-Algorithm-Benchmarker.git
cd FIle-Sorting-Algorithm-Benchmarker

# Optional: Activate devenv shell
devenv shell

# Install dependencies
poetry install
```

## 💻 Usage

### Basic Command

```bash
poetry run filesorter --attribute <ATTRIBUTE> --approach <ALGORITHM> \
  --input-file <INPUT_PATH> --output-file <OUTPUT_PATH>
```

### Command-Line Arguments

| Argument | Description | Options |
|----------|-------------|---------|
| `--attribute` | Field to sort by | `name`, `country`, `phone_number`, `job`, `email` |
| `--approach` | Sorting algorithm | `bubblesort`, `quicksort`, `lambda`, `attrgetter`, `comparator` |
| `--input-file` | Path to input data file | Any valid file path |
| `--output-file` | Path for sorted output | Any valid file path |

### Examples

Sort by email using quicksort:
```bash
poetry run filesorter --attribute email --approach quicksort \
  --input-file input/people.txt --output-file output/people.txt
```

Sort by name using Python's optimized attrgetter:
```bash
poetry run filesorter --attribute name --approach attrgetter \
  --input-file input/people.txt --output-file output/sorted_by_name.txt
```

Compare bubblesort vs quicksort on the same data:
```bash
# Bubblesort
poetry run filesorter --attribute country --approach bubblesort \
  --input-file input/people.txt --output-file output/bubble.txt

# Quicksort
poetry run filesorter --attribute country --approach quicksort \
  --input-file input/people.txt --output-file output/quick.txt
```

## 📊 Performance Analysis

The tool provides detailed timing information for each execution phase, allowing you to:
- Compare algorithm efficiency across different dataset sizes
- Identify bottlenecks in data processing pipelines
- Understand the practical performance differences between theoretical O(n) complexities
- Make informed decisions about sorting strategies in production code

## 🧪 Testing

Tests are located in `filesorter/tests/`. Run the test suite with:

```bash
poetry run pytest
```

For coverage report:
```bash
poetry run pytest --cov=filesorter
```

## 🔍 Code Quality

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and code formatting:

```bash
# Run linter
poetry run ruff check .

# Auto-fix issues
poetry run ruff check --fix .

# Format code
poetry run ruff format .
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository** and create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and add tests for new functionality

3. **Run tests and linting**:
   ```bash
   poetry run pytest
   poetry run ruff check .
   ```

4. **Commit your changes** with a descriptive message:
   ```bash
   git commit -m "Add: Description of your feature"
   ```

5. **Push to your fork** and submit a pull request

### Contribution Ideas
- Add new sorting algorithms (merge sort, heap sort, etc.)
- Improve performance metrics and visualization
- Add support for different data formats (CSV, JSON, etc.)
- Enhance documentation and examples
- Optimize existing implementations

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with Python, Poetry, and a passion for algorithmic analysis.

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub or reach out to [@javito350](https://github.com/javito350).

---

**Happy Sorting! 🚀**