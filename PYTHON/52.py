import json

# ---------------- Core Data ----------------
gradebook = {}  # student -> list of grades


# ---------------- Add Grade ----------------
def add_grade(student, grade):
    if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
        print("Invalid grade! Must be between 0 and 100.")
        return

    if student not in gradebook:
        gradebook[student] = []

    gradebook[student].append(grade)
    print(f"Grade added for {student}")


# ---------------- GPA Calculation ----------------
def calculate_gpa(grades):
    if not grades:
        return 0

    avg = sum(grades) / len(grades)

    if avg >= 90:
        return 4.0
    elif avg >= 80:
        return 3.0
    elif avg >= 70:
        return 2.0
    elif avg >= 60:
        return 1.0
    else:
        return 0.0


# ---------------- Save Data ----------------
def save_data(filename):
    with open(filename, "w") as file:
        json.dump(gradebook, file)
    print("Data saved successfully.")


# ---------------- Load Data ----------------
def load_data(filename):
    global gradebook
    try:
        with open(filename, "r") as file:
            gradebook = json.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found!")


# ---------------- Class Average ----------------
def class_average():
    all_grades = [grade for grades in gradebook.values() for grade in grades]

    if not all_grades:
        print("No grades available.")
        return

    avg = sum(all_grades) / len(all_grades)
    print(f"Class Average: {avg:.2f}")


# ---------------- Demo ----------------
add_grade("John", 85)
add_grade("John", 90)
add_grade("Alice", 78)
add_grade("Alice", 88)
add_grade("Bob", 60)

print("\nGradebook:", gradebook)

print("\nGPA:")
for student, grades in gradebook.items():
    print(student, "->", calculate_gpa(grades))

class_average()

save_data("grades.json")