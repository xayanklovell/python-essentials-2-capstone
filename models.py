class Student:
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score

        Student.total_students += 1