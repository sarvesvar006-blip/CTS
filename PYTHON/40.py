class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        if not isinstance(data, str) or "," not in data:
            return "Invalid input! Use format 'Name,Salary'."

        name, salary = data.split(",")

        if not salary.strip().isdigit():
            return "Invalid salary! Must be a number."

        return cls(name.strip(), int(salary.strip()))

    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"


emp_data = "Shubh,75000"

emp = Employee.from_string(emp_data)

if isinstance(emp, str):
    print(emp)
else:
    print(emp.display())