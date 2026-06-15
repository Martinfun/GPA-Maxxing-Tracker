import csv
import os

file = "grades.csv"
fields = ["module", "CU", "percentage", "grade", "GP"]
# CU = credit units (how much a module is worth)
# GP = grade point (0.0 to 4.0)


def get_grade(percentage):
    if percentage >= 80:
        return "A", 4.0
    if percentage >= 75:
        return "B+", 3.5
    if percentage >= 70:
        return "B", 3.0
    if percentage >= 65:
        return "C+", 2.5
    if percentage >= 60:
        return "C", 2.0
    if percentage >= 55:
        return "D+", 1.5
    if percentage >= 50:
        return "D", 1.0
    if percentage >= 45:
        return "D-", 0.5
    return "F", 0.0


def load_data():
    if not os.path.exists(file):
        return []
    with open(file, newline="") as f:
        return list(csv.DictReader(f))


def save_data(data):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def get_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a number.\n")


def show_modules(data):
    if not data:
        print("No modules yet.\n")
        return

    total_GP = 0.0
    total_CU = 0.0

    for entry in data:
        print(entry["module"], "-", entry["percentage"], "%", entry["grade"], "GP", entry["GP"], "CU", entry["CU"])
        total_GP += float(entry["GP"]) * float(entry["CU"])
        total_CU += float(entry["CU"])

    cgpa = total_GP / total_CU if total_CU else 0.0
    print("\nTotal CU:", int(total_CU))
    print("CGPA:", round(cgpa, 2), "\n")


def add_module(data):
    module = input("Module name: ").strip()
    if not module:
        print("Module name can't be empty.\n")
        return

    #  check if mod alr is present
    for i in range(len(data)):
        if data[i]["module"].lower() == module.lower():
            print("Module already exists. Perhaps you meant to edit it?\n")
            return

    CU = get_float("Credit units (CU): ")
    percentage = get_float("Percentage (%): ")
    grade, GP = get_grade(percentage)

    data.append({
        "module": module,
        "CU": CU,
        "percentage": percentage,
        "grade": grade,
        "GP": GP
    })

    save_data(data)
    print("Saved!", module, "-", percentage, "%", grade, "\n")


def edit_module(data):
    if not data:
        print("No modules to edit yet.\n")
        return

    name = input("Module name to edit: ").strip()

    for entry in data:
        if entry["module"].lower() == name.lower():
            new_pct = get_float("New percentage for " + entry["module"] + " (was " + str(entry["percentage"]) + "%): ")
            grade, GP = get_grade(new_pct)
            entry["percentage"] = new_pct
            entry["grade"] = grade
            entry["GP"] = GP
            save_data(data)
            print("Updated!", entry["module"], "-", new_pct, "%", grade, "\n")
            return

    print("No module called", name, "found.\n")


def menu():
    data = load_data()

    while True:
        print("--- GPAMAXXING TRACKER ---")
        show_modules(data)
        print("1. Add module")
        print("2. Edit module")
        print("3. Exit")

        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            add_module(data)
        elif choice == "2":
            edit_module(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")


menu()
