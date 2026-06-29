import csv
import json
import logging

# Configure logging
logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class StudentNotFoundError(Exception):
    pass

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

# ---------- Utility Functions ----------
def load_students_csv():
    try:
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_students_csv(students):
    with open(CSV_FILE, mode="w", newline="") as file:
        fieldnames = ["reg_no", "name", "program"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def load_students_json():
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_students_json(details):
    with open(JSON_FILE, "w") as file:
        json.dump(details, file, indent=4)

# ---------- Core Operations ----------
def add_student():
    reg_no = input("Enter registration number: ").strip()
    name = input("Enter student name: ").strip()
    program = input("Enter program: ").strip()
    address = input("Enter address: ").strip()
    contact = input("Enter contact: ").strip()

    students = load_students_csv()
    if any(s["reg_no"] == reg_no for s in students):
        print("❌ Registration number already exists.")
        logging.error(f"Duplicate reg_no {reg_no}")
        return

    students.append({"reg_no": reg_no, "name": name, "program": program})
    save_students_csv(students)

    details = load_students_json()
    details[reg_no] = {"address": address, "contact": contact, "program": program}
    save_students_json(details)

    logging.info(f"Added student {reg_no}")
    print("✅ Student added successfully.")

def view_students():
    students = load_students_csv()
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"{s['reg_no']} - {s['name']} - {s['program']}")

def search_student():
    reg_no = input("Enter registration number to search: ").strip()
    students = load_students_csv()
    details = load_students_json()
    for s in students:
        if s["reg_no"] == reg_no:
            print(f"Found: {s['reg_no']} - {s['name']} - {s['program']}")
            print("Details:", details.get(reg_no, "No extra details"))
            return
    logging.error(f"Student {reg_no} not found")
    raise StudentNotFoundError(f"Student {reg_no} not found")

def update_student():
    reg_no = input("Enter registration number to update: ").strip()
    students = load_students_csv()
    details = load_students_json()

    for s in students:
        if s["reg_no"] == reg_no:
            s["name"] = input("Enter new name: ").strip()
            s["program"] = input("Enter new program: ").strip()
            save_students_csv(students)

            details[reg_no]["address"] = input("Enter new address: ").strip()
            details[reg_no]["contact"] = input("Enter new contact: ").strip()
            save_students_json(details)

            logging.info(f"Updated student {reg_no}")
            print("✅ Student updated successfully.")
            return
    logging.error(f"Update failed: {reg_no} not found")
    raise StudentNotFoundError(f"Student {reg_no} not found")

def delete_student():
    reg_no = input("Enter registration number to delete: ").strip()
    students = load_students_csv()
    details = load_students_json()

    new_students = [s for s in students if s["reg_no"] != reg_no]
    if len(new_students) == len(students):
        logging.error(f"Delete failed: {reg_no} not found")
        raise StudentNotFoundError(f"Student {reg_no} not found")

    save_students_csv(new_students)
    details.pop(reg_no, None)
    save_students_json(details)

    logging.info(f"Deleted student {reg_no}")
    print("✅ Student deleted successfully.")

# ---------- Menu ----------
def menu():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()
        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Exiting system...")
                break
            else:
                print("❌ Invalid choice. Try again.")
        except StudentNotFoundError as e:
            print(e)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            print("❌ An error occurred.")
        finally:
            logging.info("Menu loop executed.")

if __name__ == "__main__":
    menu()
