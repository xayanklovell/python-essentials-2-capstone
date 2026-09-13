import os
import platform
import calendar
from datetime import date, datetime
from analytics import class_average, highest, lowest, pass_rate


def environment_report():
    file_path = "data/students.txt"
    exists = os.path.isfile(file_path)
    size = "Unavailable"

    if exists:
        try:
            size = f"{os.path.getsize(file_path)} bytes"
        except OSError as error:
            size = f"Unavailable: {error}"

    lines = [
        "ENVIRONMENT REPORT",
        f"Operating system: {platform.system()} {platform.release()}",
        f"Python version: {platform.python_version()}",
        f"Working directory: {os.getcwd()}",
        f"Student file: {os.path.abspath(file_path)}",
        f"Student file exists: {exists}",
        f"Student file size: {size}",
    ]

    return "\n".join(lines)


def date_report():
    now = datetime.now()
    today = now.date()
    target = date(today.year + 1, 1, 1)

    days_remaining = (target - today).days
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    leap_year = calendar.isleap(today.year)

    lines = [
        "DATE REPORT",
        f"Today: {today.strftime('%A, %d %B %Y')}",
        f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Chosen future date: {target.strftime('%d %B %Y')}",
        f"Days until chosen date: {days_remaining}",
        f"Leap year: {leap_year}",
        f"Days in {calendar.month_name[today.month]}: {days_in_month}",
    ]

    return "\n".join(lines)

def student_report(students):
    if not students:
        return "No students loaded. Generate and load data first."

    top = highest(students)
    bottom = lowest(students)
    passed = 0

    for student in students:
        if student.has_passed():
            passed += 1

    lines = [
        "STUDENT ANALYTICS REPORT",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"School: {students[0].school_name}",
        f"Students: {len(students)}",
        f"Class average: {class_average(students):.2f}",
        f"Highest: {top.name} ({top.student_id}) - {top.score}",
        f"Lowest: {bottom.name} ({bottom.student_id}) - {bottom.score}",
        f"Passed: {passed}",
        f"Failed: {len(students) - passed}",
        f"Pass rate: {pass_rate(students):.2f}%",
        "",
        "STUDENT DETAILS",
    ]

    for student in students:
        lines.append(str(student))

        if hasattr(student, "research_topic"):
            lines.append(f"  Research topic: {student.research_topic}")

    return "\n".join(lines) + "\n"