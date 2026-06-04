def get_employee_salary(data, department, employee):
    if not isinstance(data, dict):
        return "Invalid data! Must be a dictionary."

    if department not in data:
        return "Department not found!"

    if employee not in data[department]:
        return "Employee not found!"

    salary = data[department][employee]
    return f"Salary of {employee}: {salary}"


company_data = {
    "IT": {
        "John": 50000,
        "Alice": 60000
    },
    "HR": {
        "Bob": 45000,
        "Emma": 48000
    }
}


result = get_employee_salary(company_data, "IT", "Alice")
print(result)