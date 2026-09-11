class Student:
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score

        Student.total_students += 1

    def get_grade(self):
        if self.score >= 80:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "Fail"

    def has_passed(self):
        return self.score >= 50

    def __str__(self):
        return (
            f"{self.student_id}: {self.name} | "
            f"Score: {self.score} | Grade: {self.get_grade()}"
        )