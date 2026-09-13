from models import Student, HonoursStudent
from data_tools import generate_data_file, load_students, export_report, log_event
from analytics import passing_students, make_grader
from reporting import environment_report, date_report, student_report


MENU = """===== STUDENT ANALYTICS TOOLKIT =====
1. Generate sample data file
2. Load & clean records from file
3. View all students
4. Analyse (averages, pass/fail, top student)
5. Filter students (generator)
6. Grade with a custom pass mark (closure)
7. Environment & date report
8. Export results to a file
9. Exit"""


def record_event(message):
    try:
        log_event(message)
    except (OSError, UnicodeError) as error:
        print(f"Could not update the activity log: {error}")


def build_students(records):
    students = []

    for number, (name, score) in enumerate(records, start=1):
        student_id = f"S{number}"

        if name == "Thabo Mokoena":
            student = HonoursStudent(name, student_id, score, "Data science")
        else:
            student = Student(name, student_id, score)

        students.append(student)

    return students


def main():
    students = []

    while True:
        try:
            print("\n" + MENU)
            choice = input("Choose an option (1-9): ").strip()

            if choice == "9":
                record_event("Exited the toolkit")
                print("Goodbye!")
                break

            if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                print("Please choose a number from 1 to 9.")
                continue

            if choice in ("3", "4", "5", "6", "8") and not students:
                print("No students loaded. Use option 1, then option 2.")
                continue

            if choice == "1":
                path = generate_data_file()
                students = []
                print(f"Generated sample data: {path}")
                print("Choose option 2 to load the new records.")
                record_event("Generated sample data")

            elif choice == "2":
                students = build_students(load_students())

                if students:
                    print(f"Loaded {len(students)} students.")
                    record_event(f"Loaded {len(students)} students")
                else:
                    print("No valid students loaded. Check or regenerate the data file.")

            elif choice == "3":
                for student in students:
                    print(student)

                print(f"Objects created this session: {Student.total_students}")
                record_event("Viewed all students")

            elif choice == "4":
                print(student_report(students))
                record_event("Analysed student results")

            elif choice == "5":
                print("Passing students (50+):")
                found = False

                for student in passing_students(students):
                    print(student)
                    found = True

                if not found:
                    print("No students passed.")

                record_event("Filtered passing students")

            elif choice == "6":
                try:
                    pass_mark = int(input("Custom pass mark (0-100): "))
                    grader = make_grader(pass_mark)
                except ValueError:
                    print("Please enter a whole number from 0 to 100.")
                    continue

                print(f"Results using pass mark {pass_mark}:")
                for student in students:
                    print(f"{student.name}: {grader(student.score)}")

                standard = make_grader(50)
                strict = make_grader(75)
                print("Closure example using score 60:")
                print(f"Pass mark 50: {standard(60)}")
                print(f"Pass mark 75: {strict(60)}")
                record_event(f"Used custom pass mark {pass_mark}")

            elif choice == "7":
                print(environment_report())
                print()
                print(date_report())
                record_event("Viewed environment and date reports")

            elif choice == "8":
                path = export_report(student_report(students))
                print(f"Report exported to {path}")
                record_event("Exported student report")

        except (OSError, UnicodeError) as error:
            print(f"File operation failed: {error}")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()