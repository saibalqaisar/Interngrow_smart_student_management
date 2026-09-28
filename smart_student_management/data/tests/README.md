# Smart Student Management System

A menu-driven console application in Python to manage student records.
Built as Task 1 of the InternGrow Python Programming Track.

## Features
- Add, update, delete and search students
- Automatic total, percentage and grade calculation
- Display all records with class average and topper
- Data stored permanently in a JSON file
- Input validation and exception handling

## Project Structure
- `main.py` - starts the program
- `menu.py` - menu and user interaction
- `manager.py` - add / update / delete / search logic
- `student.py` - Student class (OOP)
- `storage.py` - reads and writes `data/students.json`
- `validators.py` - safe input functions
- `tests/` - unit tests

## How to Run
```bash
python main.py
```
Requires Python 3.8+. No external libraries needed.

## Run Tests
```bash
python -m unittest discover tests
```

## Grade Scale
A+ >= 90, A >= 80, B >= 70, C >= 60, D >= 50, E >= 40, F < 40

## Skills Used
Python basics, functions, loops, OOP, JSON, exception handling.