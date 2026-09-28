import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from manager import StudentManager


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "students.json")
        self.m = StudentManager(self.path)

    def tearDown(self):
        self.tmp.cleanup()

    def test_add_and_grade(self):
        s = self.m.add_student("Test One", 20, "Cs", {"A": 90, "B": 80})
        self.assertEqual(s.student_id, 1)
        self.assertEqual(s.total_marks(), 170)
        self.assertEqual(s.percentage(), 85.0)
        self.assertEqual(s.grade(), "A")

    def test_persistence(self):
        self.m.add_student("Test One", 20, "Cs", {"A": 50})
        again = StudentManager(self.path)
        self.assertEqual(len(again.students), 1)

    def test_update_delete_search(self):
        self.m.add_student("Test One", 20, "Cs", {"A": 50})
        self.m.update_student(1, name="Renamed")
        self.assertEqual(self.m.search("renam")[0].student_id, 1)
        self.assertTrue(self.m.delete_student(1))
        self.assertFalse(self.m.delete_student(1))

    def test_id_not_reused(self):
        self.m.add_student("A", 20, "X", {"S": 60})
        self.m.add_student("B", 20, "X", {"S": 60})
        self.m.delete_student(1)
        self.assertEqual(self.m.add_student("C", 20, "X", {"S": 60}).student_id, 3)


if __name__ == "__main__":
    unittest.main()