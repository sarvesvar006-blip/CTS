import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "salary": self.salary
        }


def save_employees(emp_dict, filename):
    try:
        data = {emp_id: emp.to_dict() for emp_id, emp in emp_dict.items()}
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)


def load_employees(filename):
    emp_dict = {}
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for emp_id, details in data.items():
                emp = Employee(emp_id, details["name"], details["salary"])
                emp_dict[emp_id] = emp
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found!")
    return emp_dict


emp1 = Employee("E101", "John", 50000)
emp2 = Employee("E102", "Alice", 60000)
emp3 = Employee("E103", "Bob", 55000)


employees = {
    emp1.emp_id: emp1,
    emp2.emp_id: emp2,
    emp3.emp_id: emp3
}


save_employees(employees, "emps.json")


loaded_employees = load_employees("emps.json")


print("Employee List:")
for emp in loaded_employees.values():
    print(emp)