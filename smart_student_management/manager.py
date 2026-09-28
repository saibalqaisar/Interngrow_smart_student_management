"""manager.py - business logic (add, update, delete, search, report)."""

from student import Student
from storage import load_students, save_students


class StudentManager:
    def __init__(self, path=None):
        self.path = path
        self.students = load_students(path) if path else load_students()

    def _save(self):
        if self.path:
            return save_students(self.students, self.path)
        return save_students(self.students)

    def find_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def next_id(self):
        if not self.students:
            return 1
        return max(s.student_id for s in self.students) + 1

    def add_student(self, name, age, course, marks):
        student = Student(self.next_id(), name, age, course, marks)
        self.students.append(student)
        self._save()
        return student

    def update_student(self, student_id, name=None, age=None, course=None, marks=None):
        student = self.find_by_id(student_id)
        if student is None:
            return None
        if name is not None:
            student.name = name
        if age is not None:
            student.age = age
        if course is not None:
            student.course = course
        if marks is not None:
            student.marks = marks
        self._save()
        return student

    def delete_student(self, student_id):
        student = self.find_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        self._save()
        return True

    def search(self, keyword):
        keyword = keyword.strip().lower()
        results = []
        for s in self.students:
            if keyword.isdigit() and s.student_id == int(keyword):
                results.append(s)
            elif keyword in s.name.lower() or keyword in s.course.lower():
                results.append(s)
        return results

    def sorted_by_percentage(self):
        return sorted(self.students, key=lambda s: s.percentage(), reverse=True)

    def class_summary(self):
        if not self.students:
            return None
        percentages = [s.percentage() for s in self.students]
        topper = max(self.students, key=lambda s: s.percentage())
        return {
            "count": len(self.students),
            "average": round(sum(percentages) / len(percentages), 2),
            "topper": topper,
        }