from typing import Dict
import copy

class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.id = student_id
        self.grades: Dict[int, float] = {}
        self.is_active = True

    def add_grade(self, course_id: int, grade: float) -> None:
        self.grades[course_id] = grade

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def toggle_active_status(self) -> None:
        self.is_active = not self.is_active

    def clone(self):
        return copy.deepcopy(self)

original_student = Student("John Doe", "S12345")
original_student.add_grade(101, 85.5)
original_student.add_grade(102, 90.0)

duplicated_student = original_student.clone()

duplicated_student.add_grade(103, 78.0)

print("Original Student Grades:", original_student.grades)
print("Cloned Student Grades:", duplicated_student.grades)
