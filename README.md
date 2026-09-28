# Smart Student Management System

A menu-driven Python console application to manage student records.
Built as **Task 1** of the InternGrow Python Programming Track.

## Features
- Add, update, delete and search students
- Automatic total, percentage and grade calculation
- Display all records with class average and topper
- Permanent storage in a JSON file
- Input validation and exception handling on every input
- Automatic IDs that are never reused

## Project Structure
Inside the `smart_student_management` folder:

| File | Purpose |
|------|---------|
| `main.py` | Starts the program |
| `menu.py` | Menu and user interaction |
| `manager.py` | Add / update / delete / search logic |
| `student.py` | `Student` class (OOP) with grade calculation |
| `storage.py` | Reads and writes `data/students.json` |
| `validators.py` | Safe input functions |
| `tests/` | Automated unit tests |

## How to Run
```bash
cd smart_student_management
python main.py
```
Requires Python 3.8+. No external libraries needed.

## Run Tests
```bash
cd smart_student_management
python -m unittest discover tests
```

## Grade Scale
A+ >= 90, A >= 80, B >= 70, C >= 60, D >= 50, E >= 40, F < 40

## Skills Used
Python basics, functions, loops, OOP, JSON, exception handling, modular design.
