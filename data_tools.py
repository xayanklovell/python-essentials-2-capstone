import os 
import random
from datetime import datetime

def generate_data_file():
    os.makedirs("data", exist_ok=True)

    names = [
        "  lIsA nDlOvU  ",
        " tHaBo mOkOeNa ",
        "  aMINA pATEL ",
        " SIPHO dlamini  ",
        "  nAlEdI KHUMALO ",
        "jOhAn bOtHa  ",
        "  ZINHLE zulu ",
        " kabelo MOLEFE  ",
    ]

    with open("data/students.txt", "w", encoding="utf-8") as data_file:
        for name in names:
            score = random.randint(0, 100)
            data_file.write(f"{name} ,  {score}  \n")

    return "data/students.txt"

def load_students(file_path="data/students.txt"):
    students = []

    try:
        with open(file_path, "r", encoding="utf-8") as data_file:
            for line_number, line in enumerate(data_file, start=1):
                if not line.strip():
                    continue

                try:
                    fields = line.strip().split(",")

                    if len(fields) != 2:
                        raise ValueError("expected one name and one score")

                    name = " ".join(fields[0].strip().lower().split()).title()

                    if not name:
                        raise ValueError("the name is empty")

                    score = int(fields[1].strip())

                    if not 0 <= score <= 100:
                        raise ValueError("score must be between 0 and 100")

                    students.append((name, score))

                except ValueError as error:
                    print(f"Skipping line {line_number}: {error}")

    except FileNotFoundError:
        print("Student data file not found. Generate data first.")

    except (OSError, UnicodeError) as error:
        print(f"Could not read student data: {error}")
        return []

    return students

def export_report(text):
    os.makedirs("data", exist_ok=True)

    with open("data/report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(text)

    return "data/report.txt"


def log_event(message):
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/activity.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

    return "data/activity.log"