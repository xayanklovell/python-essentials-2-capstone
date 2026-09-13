# Student Analytics Toolkit

A Python terminal application that generates messy student data, cleans it, creates student objects, and analyses their results. The toolkit includes standard and honours students, configurable pass/fail grading, environment and date information, and reports exported to files.

## 2. Name and cohort

- **Name:** Xayan Kyle Lovell
- **Cohort:** 2025 Sep Cohort
- **Course:** Python Essentials 2 — Capstone Project

## 3. Features

- Generate eight sample student records with messy names and random scores.
- Clean names and validate scores when loading records.
- Skip malformed records with helpful messages.
- Model students using classes and inheritance.
- Calculate the average, highest score, lowest score, and pass rate.
- Filter passing students using a generator.
- Apply a custom pass mark using a closure.
- Display operating system, Python, file, and date information.
- Export student reports and append timestamped activity logs.
- Handle invalid menu choices, invalid pass marks, and missing data.

## 4. How to run

### Requirements

Python 3 is required. The project was tested with Python 3.13.9 on macOS.

Only the Python standard library is used, so no third-party packages need installing. The requirements.txt file documents this.

### Start the application

Run these commands in your terminal:

```bash
git clone https://github.com/xayanklovell/python-essentials-2-capstone.git
cd python-essentials-2-capstone
python main.py
```

If your system uses `python3` instead of `python`, run:

```bash
python3 main.py
```

Run the application from the project folder because its data paths are relative to that folder.

### Using the menu

On your first run:

1. Choose **1** to generate sample data.
2. Choose **2** to load and clean it.
3. Choose **3** to view students.
4. Choose **4** to see the analysis.
5. Explore options **5–8** for filtering, custom grading, reports, and export.
6. Choose **9** to exit.

On later runs, option **2** can load the existing data file.

### Data and grading behaviour

- Option **1** replaces the sample data file and clears the loaded students. Choose **2** again to load the new records.
- Scores are random integers from 0 to 100, so results vary when data is generated again.
- Standard students pass at 50 and receive a distinction at 80.
- Thabo Mokoena is the sample honours student, with the research topic “Data science”. His distinction threshold is 75.
- Option **6** displays results using a temporary custom pass mark. It does not change the regular grades or exported report.
- The student object counter counts every object created during the session, including objects created by repeated loads.
- The date report counts down to 1 January of the following year.

Generated files:

| File | Purpose |
| --- | --- |
| `data/students.txt` | Sample student records; replaced when data is generated |
| `data/report.txt` | Latest exported student report; replaced on export |
| `data/activity.log` | Timestamped activity history; new entries are appended |

Generated data files and Python cache files are excluded from Git.

## 5. Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Displays the menu and connects the other modules |
| `models.py` | Defines Student and HonoursStudent classes |
| `data_tools.py` | Generates, reads, cleans, exports, and logs data |
| `analytics.py` | Calculates statistics and provides the generator and closure |
| `reporting.py` | Builds student, environment, and date reports |

The `data/` folder holds generated files. The `requirements.txt` file records that no third-party dependencies are required.

## 6. Concepts demonstrated

| PE2 module | Examples in this project |
| --- | --- |
| Module 1 — Modules and the standard library | Imports between project files; random scores; statistics; operating system information |
| Module 2 — Strings and exceptions | Cleaning names with strip, split, lower, and title; converting scores with int; handling invalid records |
| Module 3 — Object-oriented programming | Classes and objects; instance and class variables; constructors; inheritance; super; method overriding; string representations |
| Module 4 — Iteration, functions, files, and dates | Generator using yield; closure remembering a pass mark; iter and next; file reading, writing, and appending; datetime and calendar |

Specific examples:

- `Student` defines the shared structure and behaviour of student objects.
- `HonoursStudent` inherits from Student and overrides its grading method.
- `passing_students()` yields passing students one at a time.
- `make_grader()` returns a function that remembers its chosen pass mark.
- `highest()` uses `iter()` and `next()` to select its starting student.
- File operations use `with open(...)` so files are closed after use.
- Reports use write mode (`w`), while activity logs use append mode (`a`).

## 7. Sample output

### Main menu

```text
===== STUDENT ANALYTICS TOOLKIT =====
1. Generate sample data file
2. Load & clean records from file
3. View all students
4. Analyse (averages, pass/fail, top student)
5. Filter students (generator)
6. Grade with a custom pass mark (closure)
7. Environment & date report
8. Export results to a file
9. Exit
Choose an option (1-9):
```

### Example report from a real run

```text
STUDENT ANALYTICS REPORT
Generated: 2026-09-13 15:17:11
School: Melsoft Academy
Students: 8
Class average: 53.62
Highest: Thabo Mokoena (S2) - 100
Lowest: Johan Botha (S6) - 26
Passed: 5
Failed: 3
Pass rate: 62.50%

STUDENT DETAILS
S1: Lisa Ndlovu | Score: 36 | Grade: Fail
S2: Thabo Mokoena | Score: 100 | Grade: Distinction (Honours)
  Research topic: Data science
S3: Amina Patel | Score: 52 | Grade: Pass
S4: Sipho Dlamini | Score: 49 | Grade: Fail
S5: Naledi Khumalo | Score: 65 | Grade: Pass
S6: Johan Botha | Score: 26 | Grade: Fail
S7: Zinhle Zulu | Score: 50 | Grade: Pass
S8: Kabelo Molefe | Score: 51 | Grade: Pass
```

### Invalid input

```text
Choose an option (1-9): hello
Please choose a number from 1 to 9.
```

```text
Custom pass mark (0-100): 101
Please enter a whole number from 0 to 100.
```