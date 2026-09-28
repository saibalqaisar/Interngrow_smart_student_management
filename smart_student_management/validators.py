"""validators.py - input validation."""


def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Error: this field cannot be empty.")


def get_name(prompt):
    while True:
        value = input(prompt).strip()
        cleaned = value.replace(" ", "").replace(".", "").replace("-", "")
        if value and cleaned.isalpha():
            return value.title()
        print("  Error: name must contain letters only.")


def get_int(prompt, minimum, maximum):
    while True:
        raw = input(prompt).strip()
        try:
            number = int(raw)
        except ValueError:
            print("  Error: please enter a whole number.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"  Error: number must be between {minimum} and {maximum}.")


def get_marks(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            marks = float(raw)
        except ValueError:
            print("  Error: marks must be a number.")
            continue
        if 0 <= marks <= 100:
            return marks
        print("  Error: marks must be between 0 and 100.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Error: type y or n.")