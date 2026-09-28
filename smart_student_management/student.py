"""student.py - the Student class (OOP)."""


class Student:
    """Represents a single student and their marks."""

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks  # {"Maths": 80, "Physics": 72}

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        """Every subject is out of 100."""
        if not self.marks:
            return 0.0
        return round(self.total_marks() / len(self.marks), 2)

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A+"
        if p >= 80:
            return "A"
        if p >= 70:
            return "B"
        if p >= 60:
            return "C"
        if p >= 50:
            return "D"
        if p >= 40:
            return "E"
        return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["marks"],
        )