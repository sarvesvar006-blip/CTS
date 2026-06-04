class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Invalid salary amount!")
            return self
        self.salary = amount
        return self

    def apply_raise(self, percent):
        if not isinstance(percent, (int, float)) or percent < 0:
            print("Invalid raise percentage!")
            return self
        self.salary += self.salary * (percent / 100)
        return self

    def display_salary(self):
        print(f"{self.name}'s Final Salary: {self.salary:.2f}")
        return self


emp = Employee("John")

emp.set_salary(50000).apply_raise(10).display_salary()