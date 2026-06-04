def merge_employee_data(emp1, emp2):
    if not (isinstance(emp1, dict) and isinstance(emp2, dict)):
        return "Invalid input! Both inputs must be dictionaries."

    emp1.update(emp2)
    return f"Updated Employee Data: {emp1}"


employee1 = {"name": "John", "age": 30}
employee2 = {"department": "IT", "salary": 50000}

result = merge_employee_data(employee1, employee2)
print(result)