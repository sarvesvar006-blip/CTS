class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


emp1 = Employee("John", 30)
emp2 = Employee("Alice", 25)
emp3 = Employee("Bob", 28)


print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())


print("Employee Names:")
print(emp1.name)
print(emp2.name)
print(emp3.name)