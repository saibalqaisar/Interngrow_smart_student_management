"""storage.py - saving and loading students using a JSON file."""

import json
import os

from student import Student

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "students.json")


def load_students(path=DATA_FILE):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as file:
            raw_list = json.load(file)
        return [Student.from_dict(item) for item in raw_list]
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Warning: data file is damaged. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Warning: could not read the data file ({error}).")
        return []


def save_students(students, path=DATA_FILE):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            json.dump([s.to_dict() for s in students], file, indent=4)
        return True
    except OSError as error:
        print(f"Error: could not save data ({error}).")
        return False