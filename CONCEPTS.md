# Concepts Demonstrated

## 1. How my files use the PE2 modules

- **models.py — Module 3:** This file defines the Student and HonoursStudent classes. It uses constructors, instance variables, class variables, inheritance, `super()`, and method overriding.
- **data_tools.py — Modules 2 and 4:** This file cleans names using string methods and converts scores into integers. It also reads and writes files, appends activity logs, and handles missing files and invalid records.
- **analytics.py — Modules 1 and 4:** This file imports `mean` from the standard-library statistics module. It calculates class statistics and includes a generator, a closure, and an explicit use of `iter()` and `next()`.
- **reporting.py — Modules 1 and 4:** This file uses `os` and `platform` for environment information, plus `datetime` and `calendar` for dates and month information. It also imports the analytics functions to build the student report.
- **main.py — All four modules:** This file imports from the other four files and connects their features through the menu. Its loop keeps the program running, and its input checks handle invalid choices and custom pass marks.

## 2. Why I split the program into several files

Each file has a specific job, which makes it easier to find the code I need. For example, a change to how names are cleaned belongs in data_tools.py, while a change to the distinction threshold belongs in models.py. Separating the files also let me test individual functions before connecting them to the menu.

## 3. A class versus an object

A class defines the data and behaviour that its objects will have. Student is the class, while the following line creates one Student object and assigns it to the variable `lisa`:

```python
lisa = Student("Lisa", "S1", 72)
```

That object has its own name, student ID, and score. The class variables `school_name` and `total_students` are shared, and the counter increases each time a student object is created. HonoursStudent inherits from Student, uses `super().__init__()` to set up the common fields, and overrides `get_grade()` to use a distinction threshold of 75.

## 4. A generator versus a normal function

My `class_average()` function calculates an average and returns the result, or returns `None` when there are no students. Calling `passing_students()` instead creates a generator that produces passing students as they are requested.

Inside that generator, `yield student` gives back one matching student and pauses the function. The next request continues from where it paused, so the function does not need to build a separate list of all passing students. Menu option 5 uses a loop to consume these results.

My `highest()` function also demonstrates an iterator. It calls `iter(students)` and uses `next(student_iterator, None)` to get the first student, then compares the remaining students against the best one found so far. The default value `None` lets it handle an empty collection.

## 5. How my closure works

The `make_grader()` function returns an inner function called `grade`. That inner function remembers the `pass_mark` supplied when it was created, even after `make_grader()` has finished.

```python
standard = make_grader(50)
strict = make_grader(75)

print(standard(60))  # Pass
print(strict(60))    # Fail
```

Both graders receive the same score, but their remembered pass marks are different. Menu option 6 uses this to display results for a custom threshold without changing the students' stored scores or their regular grades.

## 6. Write mode versus append mode

Write mode (`"w"`) replaces the contents of an existing file, or creates the file if it does not exist. My `export_report()` function uses it so data/report.txt contains the latest exported report. Exporting twice leaves the second report in the file.

Append mode (`"a"`) adds new content to the end of a file, or creates it if it does not exist. My `log_event()` function uses it so earlier activity entries remain in data/activity.log when a new timestamped entry is added. Calling it twice adds two entries instead of replacing the first one.

Both functions use `with open(...)`, which closes the file when the block finishes, including when an error occurs inside the block.

## 7. The hardest part and how I worked through it

A difficulty I ran into while working with separate files was an ImportError when importing Student from models. I checked the saved models.py file in Terminal and started a new Python session. The import then worked, and I could create students and check their details and the shared counter.

I continued by testing the classes, file functions, analytics, and reports separately before connecting them through main.py. This made it possible to check one part at a time. After connecting the menu, I tested the complete program in a fresh clone, including generating data, loading students, running an analysis, exporting a report, and entering invalid input.
