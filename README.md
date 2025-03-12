[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/OoqleT-K)

# :microscope: File Sorting

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## :sparkles: Table of Contents

<!---toc start-->

* [:microscope: File Sorting](#-file-sorting)
  * [:sparkles: Table of Contents](#-table-of-contents)
  * [:checkered_flag: Introduction](#-introduction)
  * [:handshake: Seeking Assistance](#-seeking-assistance)
  * [:airplane: Project Overview](#-project-overview)
  * [:tada: Program Specification](#-program-specification)

<!---toc end-->

## :checkered_flag: Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date or check the
due date by clicking the appropriate box inside of this file. Please note that
the content provided in the `README.md` file for this GitHub repository is an
overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project.

## :handshake: Seeking Assistance

Even though the course instructor will have covered all the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## :airplane: Project Overview

This project invites you to implement and use a program called `filesorter`
that conducts an experiment to evaluate the performance of sorting data that
comes from an input file and is represented by the program in memory in an
object-oriented fashion. When provided with an input file, like the one in the
`input/people.txt` file, the `filesorter` will create instances of the
`People` class that have the following attributes:

- `name: str`
- `country: str`
- `phone_number: str`
- `job: str`
- `email: str`

The `filesorter` program should read in the data from the input file and then
create an instance of the `Person` class for each line in the file. This program
should then use the specified `approach` to sort all the data inside of the
list that contains the `Person` objects. The `approach` can be one of the
following five ways to sort the data:

- `bubblesort`: Use the Bubblesort algorithm to sort the data in the list of
`Person` objects according to the specified `attribute`.

- `quicksort`: Use an iterative Quicksort algorithm to sort the data in the list
of `Person` objects according to the specified `attribute`.

- `lambdafunction`: Create a `dict` called `attribute_name_to_property` that has
key-value pairs organized like `"name": lambda person: person.name` and then
call Python's sorting function in the following way: `sorted(people,
key=attribute_name_to_property[attribute])`.

- `attrgetter`: Create a `dict` called `attribute_name_to_property` that has
key-value pairs organized like `"name": attrgetter("name")` and then
call Python's sorting function in the following way: `sorted(people,
key=attribute_name_to_property[attribute])`.

- `customcompare`: Defined a nested function `compare_persons(person_one:
Person, person_two: Person) -> int` that can return a numerical value that
encodes the similarity between two `Person` objects. This approach will then use
the `functools.cmp_to_key` function as the `key` parameter to the built-in
`sorted` function. The `compare_persons` function that this approach uses
should have return values that adhere to the following requirements:
  - Return `0` if the two `Person` objects are identical
  - Return `-1` if the first `Person` object is "less than" the second `Person`
  - Return `1` if the first `Person` object is "greater than" the second
  `Person`
  - Use a lexical comparison of the `attribute` inside of each `Person` object

Note that the distinction between the way that `lambdafunction` and `attrgetter`
work is that the first one uses a `lambda` function to create the mapping
between the name of the attribute and the actual attribute (i.e., the
"property") in the `Person`. One of the goals of this project is to empirically
study whether or not there are performance differences between these two
approaches. It is also worth noting that the `customcompare` approach uses the
`compare_persons` function to aid Python's `sorted` function when it compares
instances of the `Person` class during the sorting process. This means that a
follow-on goal of this project is to empirically evaluate the performance of
`customcompare` in the context of the two aforementioned approaches.

The final version of the `filesorter` program should included "timing
instrumentation" that records the cost associated with various aspects of
specified process such as (i) the time needed to read or write the text file,
(ii) the time needed to complete the entire sorting process, and/or (iii) the
time needed for perform different parts of the input, output, or sorting steps
For instance, the `filesorter` could use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of the `in` operator for different data containers, following one of
the approaches outlined in the article called [measure execution time with
timeit in Python](https://note.nkmk.me/en/python-timeit-measure/). Finally, for
more details about a simple approach to collecting timing data through the use
of `contextlib.contextmanager`, please refer to the implementation details in
the `filesorter/profile.py` file.

After cloning this repository to your computer, please take the following steps
to get started on the project:

- To install the necessary software for running the `filesorter` program
that you will create as a part of this project, you may consider installing and
using the [`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind
that it is not necessary for you to install the `cachix` program that may be
referenced by these installation instructions. Please note that students who
are using Windows 11 should first install Windows subsystem for Linux (`wsl2`)
before attempting to install `devenv`. Once you have installed `devenv` and
cloned this repository to your computer, you can `cd` into the directory that
contains the `pyproject.toml` file and then type `devenv shell`. It is
important to note that the first time you run this command it may complete
numerous steps and take a considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains a recent version of Python and Poetry! You can verify
that you have the correct version of these two programs by typing:
  - `python --version`
  - `poetry --version`
- If you do not see a recent version of Python after typing the two
aforementioned commands, then it is possible that some part of the installation
process did not work correctly. If that occurs, then please read the following
suggestions and talk with the course instructor and a student technical leader
about what to do next.
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop using a
tool like [`mise`](https://mise.jdx.dev/). With that said, please make sure
that you use the most recent version of Python and Poetry to complete this
project and, whenever possible, those versions match the ones chosen in GitHub
Actions. This means that, to ensure that the results from running the
experiments are consistent and, as best as is possible, comparable to the
results from other computers, you should use exactly the same version of Python
and Poetry on your laptop and in GitHub Actions. For instance, when you run
`filesorter` in GitHub Actions, you should normally see that it is using
at least Poetry version `1.8.5` and Python version `3.12.8`.
- Before moving to the next step, you may need to again type `poetry install`
in order to avoid the appearance of warnings when you next run the
`filesorter` program. Now you can type the command `poetry run
filesorter --help` and explore how to use the program.

## :tada: Program Specification

Before implementing the program so that it adheres to the following requirements
and produces the expected output, please note that the program will not work
unless you add the required source code at the designated `TODO` markers. With
that said, after you complete a correct implementation of all the `filesorter`'s
features you can run it with the command `poetry run filesorter --attribute
email --approach lambdafunction --input-file input/people.txt --output-file
output/people.txt` and see that it produces output like the following.

```text
🧮 Reading in the data from the specified file input/people.txt

🚀 Parsing the data file and transforming it into people objects

🏃 Sorting the people according to the email

💥 Using a sorting approach called customcompare

✨ Saving the sorted people data to the file output/people.txt

🔬 Time to Sort Person Data Using a Custom Comparator (ms): 106.96 ms
```

Here is an example of the first lines in the `output/people.txt` file that you
would see after running the `filesorter` program with the command specified:

```text
Paula White,India,001-725-708-0158x2308,"Scientist, clinical (histocompatibility and immunogenetics)",aadams@example.com
Jessica Craig,United States of America,187.894.2220x221,Water quality scientist,aadams@example.net
April Mcguire,Kyrgyz Republic,+1-927-438-7339,Advertising copywriter,aadams@example.net
Karla Bradley,Romania,001-881-666-9775x438,"Conservator, furniture",aadams@example.net
Katherine Simmons MD,Bosnia and Herzegovina,+1-388-796-4683,"Engineer, site",aadams@example.org
Frank Rose,Sao Tome and Principe,+1-365-068-1332,Archaeologist,aaguilar@example.net
```

It is important to point out that the `output/` directory will now contain a
file called `people.txt` that should be a sorted version of the `people.txt`
file in the `input` directory. Even though the size of these two files should be
the same, there contents should not be the same because the one in the output
directory should now be sorted according to the `email` attribute. When you are
inside of the directory that contains both the `input/` and `output/`
directories, you can run the following shell command on either MacOS or Linux
and see that it produces the following output. Note that a variant of this
command is also run inside of GitHub Actions and thus students who use Windows
on their laptop can still see the output from running this command.

- Shell Command for Use on MacOS and Linux:

```shell
wc -l input/people.txt output/people.txt; du -sh input/people.txt output/people.txt; cmp -s input/people.txt output/people.txt && echo "Sorted file incorrectly same as unsorted file" || echo "Sorted file correctly not the same as the unsorted file"
```

- Output from the Shell Command for Use on MacOS and Linux:

```shell
49998 input/people.txt
49998 output/people.txt
99996 total
4.3M    input/people.txt
4.3M    output/people.txt
Sorted file correctly not the same as the unsorted file
```

Please note that your implementation of the `filesorter` program should work
for all the specified experimental configurations in the introduction to the
project and in the `writing/reflection.md` file. If you study the files in the
`filesorter/` directory you will see that they have many `TODO` markers that
designate the functions you must implement so as to ensure that `filesorter`
runs the desired experiment and produces the correct output. Once you complete
a task associated with a `TODO` marker, make sure that you delete it and revise
the prompt associated with the marker into a meaningful comment.

Ultimately, you should design your own experiment and state and run experiments
to answer your own research questions, focusing on these key issues:

- **Data file**: either subsets of or the entire `input/people.txt` or
alternative files that contain rows of data with `Person` attributes
- **Sorting algorithms**: the sorting algorithms that the `filesorter` uses to
sort the instances of the `Person` class that are stored in memory.
- **Input time**: the time overhead associated with reading in the specified
data file
- **Output time**: the time overhead associated with writing to a specified file
all the details about each matching instance of the `Person` class
- **Sorting time**: the time overhead associated with sorting the data while
using one of the file approaches for sorting (e.g., `bubblesort`, `quicksort`,
`lambdafunction`, `attrgetter`, `customcompare`).

As you design and conduct this experiment, you should consider ways in which you
can proportionally change the size of the input so that you can study, in the
worst-case, the performance of the key algorithms in `filesorter`. It is
important to note that the `writing/reflection.md` file contains more details
about the ways in which you should design the experiments for this project.
Please make sure that, at the start of the second week of this assignment, you
meet with the course instructor to receive feedback on the design of your
experiment before you embark on conducting the experiments and analyzing the
data. Finally, here are other issues that you should keep in mind as you work on
the `filesorter` program:

- You must implement test cases for all the untested modules, excepting the
`main` module, while further ensuring that the test suite achieves the desired
level of code coverage. It is important to note that the coverage report
produced by the `pytest-cov` plugin will, by default, only report the coverage
for the test cases already defined in the `tests/` directory. This means that if
you have not already implemented a test suite for a module it will not appear in
the coverage report and thus the test coverage may appear artificially higher
than it is in actuality.
- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
