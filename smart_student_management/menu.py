"""menu.py - the menu driven user interface."""

import validators as check
from manager import StudentManager


def show_menu():
    print("\n" + "=" * 42)
    print("     SMART STUDENT MANAGEMENT SYSTEM")
    print("=" * 42)
    print("  1. Add Student")
    print("  2. Update Student")
    print("  3. Delete Student")
    print("  4. Search Student")
    print("  5. Calculate Grades")
    print("  6. Display Student Records")
    print("  7. Exit")
    print("-" * 42)


def print_student_table(students):
    if not students:
        print("\n  No records found.")
        return
    print(f"\n  {'ID':<5}{'Name':<22}{'Age':<6}{'Course':<18}{'Total':<9}{'%':<8}{'Grade'}")
    print("  " + "-" * 76)
    for s in students:
        print(f"  {s.student_id:<5}{s.name:<22}{s.age:<6}{s.course:<18}"
              f"{s.total_marks():<9g}{s.percentage():<8}{s.grade()}")


def read_marks():
    count = check.get_int("  Number of subjects (1-10): ", 1, 10)
    marks = {}
    for i in range(1, count + 1):
        while True:
            subject = check.get_text(f"  Subject {i} name: ").title()
            if subject not in marks:
                break
            print("  Error: this subject was already entered.")
        marks[subject] = check.get_marks(f"  Marks in {subject} (0-100): ")
    return marks


def add_student(manager):
    print("\n--- Add Student ---")
    name = check.get_name("  Name: ")
    age = check.get_int("  Age (5-100): ", 5, 100)
    course = check.get_text("  Course / Class: ").title()
    marks = read_marks()
    student = manager.add_student(name, age, course, marks)
    print(f"\n  Student added successfully with ID {student.student_id}.")


def update_student(manager):
    print("\n--- Update Student ---")
    if not manager.students:
        print("  There are no students yet.")
        return
    student_id = check.get_int("  Enter student ID to update: ", 1, 10**9)
    student = manager.find_by_id(student_id)
    if student is None:
        print("  No student found with that ID.")
        return
    print_student_table([student])
    print("  What do you want to change?")
    print("  1. Name   2. Age   3. Course   4. Marks")
    choice = check.get_int("  Choice: ", 1, 4)
    if choice == 1:
        manager.update_student(student_id, name=check.get_name("  New name: "))
    elif choice == 2:
        manager.update_student(student_id, age=check.get_int("  New age (5-100): ", 5, 100))
    elif choice == 3:
        manager.update_student(student_id, course=check.get_text("  New course: ").title())
    else:
        manager.update_student(student_id, marks=read_marks())
    print("  Student updated successfully.")


def delete_student(manager):
    print("\n--- Delete Student ---")
    if not manager.students:
        print("  There are no students yet.")
        return
    student_id = check.get_int("  Enter student ID to delete: ", 1, 10**9)
    student = manager.find_by_id(student_id)
    if student is None:
        print("  No student found with that ID.")
        return
    print_student_table([student])
    if check.get_yes_no("  Are you sure you want to delete? (y/n): "):
        manager.delete_student(student_id)
        print("  Student deleted.")
    else:
        print("  Delete cancelled.")


def search_student(manager):
    print("\n--- Search Student ---")
    keyword = check.get_text("  Enter ID, name or course: ")
    print_student_table(manager.search(keyword))


def calculate_grades(manager):
    print("\n--- Grades (highest percentage first) ---")
    print_student_table(manager.sorted_by_percentage())
    summary = manager.class_summary()
    if summary:
        print(f"\n  Students: {summary['count']}   "
              f"Class average: {summary['average']}%   "
              f"Topper: {summary['topper'].name} ({summary['topper'].percentage()}%)")
    print("\n  Grade scale: A+ >=90 | A >=80 | B >=70 | C >=60 | D >=50 | E >=40 | F <40")


def display_records(manager):
    print("\n--- All Student Records ---")
    print_student_table(manager.students)
    for s in manager.students:
        subjects = ", ".join(f"{sub}: {m:g}" for sub, m in s.marks.items())
        print(f"    [{s.student_id}] {s.name} -> {subjects}")


def run():
    manager = StudentManager()
    actions = {
        1: add_student,
        2: update_student,
        3: delete_student,
        4: search_student,
        5: calculate_grades,
        6: display_records,
    }
    while True:
        show_menu()
        try:
            choice = check.get_int("  Enter your choice (1-7): ", 1, 7)
            if choice == 7:
                print("\n  Data saved. Goodbye!")
                break
            actions[choice](manager)
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Program interrupted. Your saved data is safe. Goodbye!")
            break
        except Exception as error:
            print(f"\n  Unexpected error: {error}")