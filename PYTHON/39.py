class Employee:
    def work(self):
        return "Employee is working"


class Developer(Employee):
    def work(self):
        return "Developer is writing code"


class Manager(Employee):
    def work(self):
        return "Manager is managing team"


emp1 = Developer()
emp2 = Manager()
emp3 = Employee()


employees = [emp1, emp2, emp3]


for emp in employees:
    print(emp.work())