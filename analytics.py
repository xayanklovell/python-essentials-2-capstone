from statistics import mean


def class_average(students):
    scores = [student.score for student in students]

    if not scores:
        return None

    return mean(scores)


def highest(students):
    student_iterator = iter(students)
    best = next(student_iterator, None)

    if best is None:
        return None

    for student in student_iterator:
        if student.score > best.score:
            best = student

    return best

def lowest(students):
    lowest_student = None

    for student in students:
        if lowest_student is None or student.score < lowest_student.score:
            lowest_student = student

    return lowest_student


def pass_rate(students):
    passed = 0
    total = 0

    for student in students:
        total += 1

        if student.has_passed():
            passed += 1

    if total == 0:
        return 0.0

    return passed / total * 100

def passing_students(students):
    for student in students:
        if student.has_passed():
            yield student